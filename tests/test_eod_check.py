"""Tests for tools/eod_check.py. Run: python3 -m unittest discover -s tests"""
import importlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import unittest
from argparse import Namespace
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo

HERE = Path(__file__).resolve().parent
TOOL = HERE.parent / "tools" / "eod_check.py"
FIX = HERE / "fixtures"
TZ = ZoneInfo("America/New_York")


def ts(iso):
    return f"{datetime.fromisoformat(iso).replace(tzinfo=TZ).timestamp():.6f}"


class Base(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp())
        (self.root / "context").mkdir()
        (self.root / "state").mkdir()
        self.cfg = json.loads((FIX / "cog.test.json").read_text())
        (self.root / "context/cog.json").write_text(json.dumps(self.cfg))
        self.msgs = json.loads((FIX / "kpi-channel.json").read_text())["messages"]

    def tearDown(self):
        shutil.rmtree(self.root)

    def go_live(self, tpl="template_first"):
        (self.root / "context/eod-mode.md").write_text("live\n")
        (self.root / "context/standing-approvals.md").write_text("1. EOD bump:\n" + self.cfg["bump"][tpl] + "\n")

    def run_cli(self, *args, msgs=None, token=""):
        f = self.root / "msgs.json"
        f.write_text(json.dumps(self.msgs if msgs is None else msgs))
        env = dict(os.environ, AIOS_ROOT=str(self.root), SLACK_BOT_TOKEN=token)
        p = subprocess.run([sys.executable, str(TOOL), "check", "--messages", str(f), *args],
                           capture_output=True, text=True, env=env)
        return p.returncode, p.stdout + p.stderr


class Classify(Base):
    def test_on_time_first_check(self):
        code, out = self.run_cli("--check", "first", "--now", "2026-11-06T23:31")
        self.assertEqual(code, 0, out)
        self.assertIn("Expected 4 · Submitted 2 · Late 0 · Missing 2", out)
        self.assertIn("Missing: Demo Closer C, Demo Setter D", out)   # C posts at 23:50, after this run
        self.assertIn('"Jon S."', out)                                 # unmatched, never guessed
        self.assertNotIn("Demo New Hire", out)                         # not active yet

    def test_final_check_marks_late(self):
        _, out = self.run_cli("--check", "final", "--now", "2026-11-07T00:46")
        self.assertIn("Late: Demo Closer C 23:50", out)
        self.assertIn("Missing: Demo Setter D", out)

    def test_owner_mention_is_not_a_submission(self):
        msgs = self.msgs + [{"ts": ts("2026-11-06T22:00"), "user": "U000000OWN", "text": "<@U000000DDD> where's your EOD?"},
                            {"ts": ts("2026-11-06T22:01"), "user": "U000000ZZZ", "text": "EOD done for the day"}]
        _, out = self.run_cli("--check", "final", "--now", "2026-11-07T00:46", msgs=msgs)
        self.assertIn("Missing: Demo Setter D", out)

    def test_a_bump_is_not_a_submission(self):
        msgs = self.msgs + [{"ts": ts("2026-11-06T23:31"), "bot_id": "BCOG", "text": "<@U000000CCC> <@U000000DDD> EOD KPIs please, it's late"}]
        _, out = self.run_cli("--check", "final", "--now", "2026-11-07T00:46", msgs=msgs)
        self.assertIn("Late: Demo Closer C 23:50", out)

    def test_window_starts_at_previous_cutoff(self):
        # Thursday's EOD posted at 00:30 Friday belongs to Thursday, not Friday.
        msgs = [m for m in self.msgs if "Demo Closer A" not in m["text"]] + [
            {"ts": ts("2026-11-06T00:30"), "bot_id": "BWF", "text": "EOD KPI Report\nName: Demo Closer A"}]
        _, out = self.run_cli("--check", "final", "--now", "2026-11-07T00:46", msgs=msgs)
        self.assertIn("Missing: Demo Closer A, Demo Setter D", out)

    def test_thread_reply_counts(self):
        msgs = self.msgs + [{"ts": ts("2026-11-06T21:00"), "thread_ts": ts("2026-11-06T20:00"), "user": "U000000DDD", "text": "my EOD: 40 dials"}]
        _, out = self.run_cli("--check", "final", "--now", "2026-11-07T00:46", msgs=msgs)
        self.assertNotIn("Demo Setter D", out)


class Guards(Base):
    def test_preview_never_posts(self):
        _, out = self.run_cli("--check", "first", "--now", "2026-11-06T23:31", "--post")
        self.assertIn("eod-mode is preview", out)

    def test_test_inputs_never_post(self):
        self.go_live()
        _, out = self.run_cli("--check", "first", "--now", "2026-11-06T23:31", "--post", token="x")
        self.assertIn("a test or replay run never posts", out)

    def test_wrong_wording_stays_draft(self):
        self.go_live()
        (self.root / "context/standing-approvals.md").write_text("1. EOD bump: something else\n")
        _, out = self.run_cli("--check", "first", "--now", "2026-11-06T23:31", "--post")
        self.assertIn("no standing approval for this exact wording", out)

    def test_late_and_early_runs(self):
        self.go_live()
        _, out = self.run_cli("--check", "first", "--now", "2026-11-07T00:10", "--post")
        self.assertIn("late run", out)
        _, out = self.run_cli("--check", "first", "--now", "2026-11-06T14:00", "--post")
        self.assertIn("early run", out)
        _, out = self.run_cli("--check", "final", "--now", "2026-11-07T01:05", "--post")
        self.assertIn("after cutoff", out)

    def test_stop_file(self):
        self.go_live()
        (self.root / "state/STOP").write_text("")
        _, out = self.run_cli("--check", "first", "--now", "2026-11-06T23:31", "--post")
        self.assertIn("state/STOP is set", out)

    def test_everyone_missing_is_a_broken_source(self):
        _, out = self.run_cli("--check", "first", "--now", "2026-11-06T23:31", msgs=[])
        self.assertIn("nobody submitted, so the source looks wrong", out)

    def test_unmatched_blocks(self):
        _, out = self.run_cli("--check", "first", "--now", "2026-11-06T23:31")
        self.assertIn("unmatched submissions need Chris first", out)

    def test_second_bumper(self):
        msgs = self.msgs + [{"ts": ts("2026-11-06T23:30"), "bot_id": "BHERMES", "text": "<@U000000DDD> EOD KPIs are missing"}]
        _, out = self.run_cli("--check", "first", "--now", "2026-11-06T23:31", msgs=msgs)
        self.assertIn("second bumper", out)

    def test_unreadable_source_is_unknown(self):
        env = dict(os.environ, AIOS_ROOT=str(self.root))
        env.pop("SLACK_BOT_TOKEN", None)
        p = subprocess.run([sys.executable, str(TOOL), "check", "--check", "first"], capture_output=True, text=True, env=env)
        self.assertEqual(p.returncode, 3, p.stdout + p.stderr)
        self.assertIn("UNKNOWN: KPI channel unreadable", p.stdout)

    def test_missing_config(self):
        cfg = dict(self.cfg, roster=[{"name": "Rep", "slack_member_id": "REQUIRED"}])
        (self.root / "context/cog.json").write_text(json.dumps(cfg))
        code, out = self.run_cli("--check", "first", "--now", "2026-11-06T23:31")
        self.assertEqual(code, 2)
        self.assertIn("slack_member_id for Rep", out)

    def test_non_slack_source(self):
        cfg = json.loads(json.dumps(self.cfg)); cfg["eod"]["source_type"] = "google_sheet"
        (self.root / "context/cog.json").write_text(json.dumps(cfg))
        code, out = self.run_cli("--check", "first", "--now", "2026-11-06T23:31")
        self.assertEqual(code, 2)
        self.assertIn("reads Slack only", out)

    def test_sunday(self):
        _, out = self.run_cli("--check", "first", "--now", "2026-11-08T23:31")
        self.assertIn("No selling day", out)


class Posting(Base):
    """In-process, with Slack faked: the full live path, and that it posts once."""
    def run_live(self, check="first"):
        os.environ["AIOS_ROOT"] = str(self.root)
        os.environ["SLACK_BOT_TOKEN"] = "xoxb-test"
        sys.path.insert(0, str(TOOL.parent))
        mod = importlib.reload(importlib.import_module("eod_check"))
        calls = []
        msgs = [m for m in self.msgs if "Jon S." not in m["text"]]
        mod.fetch = lambda *a: msgs
        mod.guard = lambda *a: None
        mod.report_date = lambda now: date(2026, 11, 6)
        def fake(method, token, params=None, body=None):
            calls.append((method, body))
            return {"ok": True, "channel": "C000TEST01", "ts": "1.5", "url": "https://x.slack.com/"}
        mod.slack = fake
        a = Namespace(check=check, config="context/cog.json", messages=None, now=None, date=None, post=True, no_write=False)
        from io import StringIO
        out, old = StringIO(), sys.stdout
        sys.stdout = out
        try:
            mod.cmd_check(a)
        finally:
            sys.stdout = old
            os.environ.pop("AIOS_ROOT"); os.environ.pop("SLACK_BOT_TOKEN")
        return out.getvalue(), calls

    def test_posts_once_and_records_it(self):
        self.go_live()
        out, calls = self.run_live()
        posts = [c for c in calls if c[0] == "chat.postMessage"]
        self.assertEqual(len(posts), 1, out)
        self.assertIn("<@U000000DDD>", posts[0][1]["text"])
        self.assertNotIn("U000000AAA", posts[0][1]["text"])
        self.assertIn("first 1.5", (self.root / "data/eod/2026-11-06.posted").read_text())
        out, calls = self.run_live()
        self.assertFalse([c for c in calls if c[0] == "chat.postMessage"])
        self.assertIn("already posted", out)


if __name__ == "__main__":
    unittest.main()
