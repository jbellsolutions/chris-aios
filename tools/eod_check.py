#!/usr/bin/env python3
"""EOD KPI check for Circle of Greatness: who was expected, who submitted, who is late or missing,
and the one bump message. Standard library only. This tool is the ONLY way the bump is ever posted.

    python3 tools/eod_check.py check --check first --post    # the 11:30 PM automation
    python3 tools/eod_check.py check --check final --post    # the 12:45 AM automation
    python3 tools/eod_check.py check --date 2026-11-06       # replay a past night: draft only
    python3 tools/eod_check.py check --messages saved.json --date 2026-11-06   # from a saved channel read

It reads the KPI channel with SLACK_BOT_TOKEN (from .env.local), including thread replies. It posts only if
ALL of these hold, and otherwise prints the draft for Chris:
  --post was given, with no --now, --date or --messages; context/eod-mode.md says `live`;
  context/standing-approvals.md holds the exact bump template; state/STOP does not exist; the run started
  on time; the channel was read; at least one rep submitted (everyone missing = a broken source);
  no submission is unmatched; this check isn't in data/eod/<date>.posted yet; and no other bot bumped tonight.

--messages takes a JSON list of Slack messages ({"ts", "user", "bot_id", "text"}), or {"messages": [...]}.
"""
import argparse
import json
import os
import re
import sys
import urllib.parse
import urllib.request
from datetime import date, datetime, time, timedelta
from pathlib import Path

try:
    from zoneinfo import ZoneInfo
except ImportError:  # Python < 3.9
    sys.exit("Python 3.9 or later is needed (zoneinfo).")

ROOT = Path(os.environ.get("AIOS_ROOT") or Path(__file__).resolve().parent.parent)
DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
GRACE_MINUTES = 30
SLACK_SOURCES = ("slack_workflow_channel", "slack")
MEMBER_ID = re.compile(r"^[UW][A-Z0-9]{6,}$")


def load_env():
    env = ROOT / ".env.local"
    if env.exists():
        for line in env.read_text().splitlines():
            if "=" in line and not line.lstrip().startswith("#"):
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip().strip('"'))


def expected_reps(cfg, rdate):
    return [r for r in cfg.get("roster", []) if r.get("active", True) and r.get("eod_required", True)
            and "EXAMPLE" not in r.get("name", "")
            and date.fromisoformat(r.get("active_since", "2000-01-01")) <= rdate]


def missing_config(cfg):
    out = []
    eod = cfg.get("eod", {})
    roster = [r for r in cfg.get("roster", []) if "EXAMPLE" not in r.get("name", "")]
    if not roster:
        out.append("roster")
    bad_ids = [r.get("name", "?") for r in roster if not MEMBER_ID.match(str(r.get("slack_member_id", "")))]
    if bad_ids:
        out.append("slack_member_id for " + ", ".join(bad_ids))
    for key in ("slack_channel_id", "identity_column"):
        if not eod.get(key) or "REQUIRED" in str(eod.get(key)):
            out.append(f"eod.{key}")
    src = eod.get("source_type", "slack_workflow_channel")
    if src not in SLACK_SOURCES:
        out.append(f"eod.source_type is {src}: this tool reads Slack only (a sheet or GHL form needs its own reader)")
    return out


def hm(s):
    h, m = s.split(":")
    return time(int(h), int(m))


def report_date(now):
    """The selling day that just ended. Before noon (the final check, after midnight) it is yesterday."""
    d = now.date()
    if now.time() < time(12, 0):
        d -= timedelta(days=1)
    return d


def at(d, t, tz):
    """A check time for report date d: times before noon fall on the next calendar day."""
    dt = datetime.combine(d, t, tz)
    return dt + timedelta(days=1) if t < time(12, 0) else dt


def times(rdate, eod, tz):
    first = at(rdate, hm(eod.get("first_check", "23:30")), tz)
    final = at(rdate, hm(eod.get("final_check", "00:45")), tz)
    cutoff = at(rdate, hm(eod.get("cutoff", "01:00")), tz)
    return first, final, cutoff, cutoff - timedelta(days=1)   # the window opens at the previous cutoff


def guard(now, rdate, eod, check, tz):
    """None if the run is on time, else the reason it must stay a draft."""
    first, final, cutoff, _ = times(rdate, eod, tz)
    due = first if check == "first" else final
    if now < due:
        return f"early run: started {now:%H:%M} ET, expected {due:%H:%M} ET"
    if now > due + timedelta(minutes=GRACE_MINUTES):
        return f"late run: started {now:%H:%M} ET, expected {due:%H:%M} ET"
    if check == "final" and now >= cutoff:
        return f"after cutoff: started {now:%H:%M} ET, cutoff {cutoff:%H:%M} ET"
    return None


def norm(s):
    return re.sub(r"\s+", " ", (s or "").strip().lower())


def is_bot(msg):
    return bool(msg.get("bot_id")) or msg.get("subtype") == "bot_message"


def identity_value(msg, identity_column):
    m = re.search(rf"^\W*{re.escape(identity_column)}\W*[:]\s*(.+)$", msg.get("text", ""), re.I | re.M)
    return m.group(1).strip("*_ ") if m else None


def is_bump(msg, identity_column):
    """A bot message that tags people about EODs and isn't a submission (ours, Hermes's, anyone's)."""
    t = msg.get("text", "")
    return is_bot(msg) and "<@" in t and re.search(r"\beod", t, re.I) and not identity_value(msg, identity_column)


def who(msg, roster, identity_column):
    """Match a submission to a rep. Never a guess: a rep posting it, or the form's identity field."""
    if msg.get("user") and not is_bot(msg):
        for r in roster:
            if r.get("slack_member_id") == msg["user"]:
                return r["name"]
        return None                                   # a person who isn't a rep: not a submission
    value = identity_value(msg, identity_column)
    if value is None:
        sub = re.search(r"submitted by\W*<@([A-Z0-9]+)", msg.get("text", ""), re.I)
        if not sub:
            return None
        value = f"<@{sub.group(1)}>"
    ids = re.findall(r"<@([A-Z0-9]+)", value)
    for r in roster:
        if (ids and r.get("slack_member_id") in ids) or norm(value) in (norm(r["name"]), norm(r.get("email"))):
            return r["name"]
    return "?" + value[:40]


def classify(cfg, messages, rdate, tz, check, now=None):
    eod = cfg["eod"]
    first, _, cutoff, start = times(rdate, eod, tz)
    idcol = eod.get("identity_column", "Name")
    owner = (cfg.get("owner") or {}).get("slack_member_id")
    expected = expected_reps(cfg, rdate)
    pattern = eod.get("submission_match", r"\b(eod|kpi)")
    seen, unmatched = {}, []
    for m in messages:
        try:
            ts = datetime.fromtimestamp(float(m["ts"]), tz)
        except (KeyError, TypeError, ValueError):
            continue
        if not (start <= ts < cutoff) or (now and ts > now) or (owner and m.get("user") == owner):
            continue
        if not re.search(pattern, m.get("text", ""), re.I) or is_bump(m, idcol):
            continue
        name = who(m, expected, idcol)
        if name is None:
            continue
        if name.startswith("?"):
            unmatched.append(name[1:] or "unnamed")
        elif name not in seen or ts < seen[name][0]:
            seen[name] = (ts, m.get("text", ""))
    rows = []
    for r in expected:
        ts, text = seen.get(r["name"], (None, None))
        status = "missing" if ts is None else ("submitted" if ts <= first else "late")
        if check == "final":
            status = {"missing": "eod_missing", "late": "eod_late"}.get(status, status)
        rows.append({"name": r["name"], "slack_member_id": r.get("slack_member_id"), "status": status,
                     "at": ts.strftime("%H:%M") if ts else None, "submission": text})
    return rows, unmatched


def bump_text(cfg, rows, rdate, now, check):
    missing = [r for r in rows if r["status"] in ("missing", "eod_missing")]
    if not missing:
        return None
    tpl = cfg["bump"]["template_first" if check == "first" else "template_final"]
    return tpl.format(mentions=" ".join(f"<@{r['slack_member_id']}>" for r in missing),
                      report_date=rdate.strftime("%a %b %-d"), time=now.strftime("%-I:%M %p"),
                      cutoff=datetime.combine(rdate, hm(cfg["eod"].get("cutoff", "01:00"))).strftime("%-I:%M %p"))


def slack(method, token, params=None, body=None):
    url = "https://slack.com/api/" + method
    if params:
        url += "?" + urllib.parse.urlencode(params)
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, headers={"Authorization": f"Bearer {token}",
                                                         "Content-Type": "application/json; charset=utf-8"})
    with urllib.request.urlopen(req, timeout=30) as r:
        out = json.load(r)
    if not out.get("ok"):
        raise RuntimeError(out.get("error", "unknown_error"))
    return out


def fetch(channel, oldest, latest, token):
    """Channel history for the window, plus every thread's replies."""
    msgs, cursor = [], None
    while True:
        p = {"channel": channel, "oldest": f"{oldest:.6f}", "latest": f"{latest:.6f}", "limit": 200}
        if cursor:
            p["cursor"] = cursor
        out = slack("conversations.history", token, p)
        msgs += out.get("messages", [])
        cursor = (out.get("response_metadata") or {}).get("next_cursor")
        if not cursor:
            break
    for m in [m for m in msgs if m.get("reply_count")]:
        replies = slack("conversations.replies", token, {"channel": channel, "ts": m["ts"], "limit": 200})
        msgs += [r for r in replies.get("messages", []) if r.get("ts") != m["ts"]]
    return msgs


def read_word(path, default=""):
    words = path.read_text().split() if path.exists() else []
    return words[0].lower() if words else default


def post_blockers(cfg, a, rdate, rows, unmatched, bump, messages, guard_reason):
    tpl = cfg["bump"]["template_first" if a.check == "first" else "template_final"]
    approvals = ROOT / "context/standing-approvals.md"
    posted = ROOT / f"data/eod/{rdate}.posted"
    out = []
    if not bump:
        return ["nobody is missing"]
    if not a.post:
        out.append("--post not given")
    if a.now or a.date or a.messages:
        out.append("a test or replay run never posts")
    if (ROOT / "state/STOP").exists():
        out.append("state/STOP is set")
    if read_word(ROOT / "context/eod-mode.md", "preview") != "live":
        out.append("eod-mode is preview")
    if not approvals.exists() or tpl not in approvals.read_text():
        out.append("no standing approval for this exact wording")
    if guard_reason:
        out.append(guard_reason)
    if not any(r["status"] in ("submitted", "late", "eod_late") for r in rows):
        out.append("nobody submitted, so the source looks wrong")
    if unmatched:
        out.append("unmatched submissions need Chris first")
    if posted.exists() and any(l.startswith(a.check + " ") for l in posted.read_text().splitlines()):
        out.append(f"the {a.check} bump is already posted")
    mine = posted.read_text() if posted.exists() else ""
    tz = ZoneInfo(cfg["business"].get("team_timezone", "America/New_York"))
    evening = datetime.combine(rdate, time(18, 0), tz).timestamp()
    idcol = cfg["eod"].get("identity_column", "Name")
    for m in messages:
        try:
            late_enough = float(m.get("ts", 0)) >= evening
        except ValueError:
            continue
        if late_enough and is_bump(m, idcol) and m["ts"] not in mine:
            out.append("another bot already bumped tonight (second bumper)")
            break
    if not os.environ.get("SLACK_BOT_TOKEN"):
        out.append("no SLACK_BOT_TOKEN")
    return out


def log_run(rdate, check, line, write=True):
    if not write:
        return
    d = ROOT / "runs"
    d.mkdir(parents=True, exist_ok=True)
    with open(d / f"runs-{datetime.now():%Y-%m}.md", "a") as f:
        f.write(f"- {datetime.now():%Y-%m-%d %H:%M} · EOD {check} check ({rdate}) · {line}\n")


def post(cfg, a, rdate, bump):
    token, channel = os.environ["SLACK_BOT_TOKEN"], cfg["eod"]["slack_channel_id"]
    out = slack("chat.postMessage", token, body={"channel": channel, "text": bump})
    posted = ROOT / f"data/eod/{rdate}.posted"
    posted.parent.mkdir(parents=True, exist_ok=True)
    with open(posted, "a") as f:                     # record the post before anything else can fail
        f.write(f"{a.check} {out['ts']}\n")
    try:
        team = slack("auth.test", token)
        link = f"{team['url']}archives/{out['channel']}/p{out['ts'].replace('.', '')}"
    except Exception:
        link = f"channel {out['channel']} ts {out['ts']}"
    return link


def cmd_check(a):
    load_env()
    write = not a.no_write
    cfg_path = ROOT / a.config
    if not cfg_path.exists():
        print(f"NO_CLIENT_SOURCE: {a.config} (copy config/cog.example.json there and fill it in)")
        return 2
    cfg = json.loads(cfg_path.read_text())
    gaps = missing_config(cfg)
    if gaps:
        print("NO_CLIENT_SOURCE: " + "; ".join(gaps))
        return 2
    tz = ZoneInfo(cfg["business"].get("team_timezone", "America/New_York"))
    now = datetime.fromisoformat(a.now).replace(tzinfo=tz) if a.now else datetime.now(tz)
    rdate = date.fromisoformat(a.date) if a.date else report_date(now)
    if DAYS[rdate.weekday()] not in cfg["business"].get("selling_days", DAYS):
        print(f"No selling day ({rdate:%a %b %-d}): nothing expected.")
        return 0
    guard_reason = None if a.date else guard(now, rdate, cfg["eod"], a.check, tz)
    try:
        if a.messages:
            messages = json.loads(Path(a.messages).read_text())
            messages = messages.get("messages", []) if isinstance(messages, dict) else messages
        else:
            token = os.environ.get("SLACK_BOT_TOKEN")
            if not token:
                raise RuntimeError("no SLACK_BOT_TOKEN (Chris runs tools/add_secret.sh SLACK_BOT_TOKEN)")
            _, _, cutoff, start = times(rdate, cfg["eod"], tz)
            messages = fetch(cfg["eod"]["slack_channel_id"], start.timestamp(), cutoff.timestamp(), token)
    except Exception as e:  # unreadable source: never treat as everyone in or everyone out
        line = f"UNKNOWN: KPI channel unreadable at {now:%H:%M} ET ({e}). No bump."
        print(line)
        log_run(rdate, a.check, line, write)
        return 3
    rows, unmatched = classify(cfg, messages, rdate, tz, a.check, None if a.date else now)
    bump = bump_text(cfg, rows, rdate, now, a.check)
    count = lambda *s: sum(r["status"] in s for r in rows)
    head = (f"EOD check {a.check} {now:%-I:%M %p} ET, {rdate:%a %b %-d}\n"
            f"Expected {len(rows)} · Submitted {count('submitted')} · Late {count('late', 'eod_late')} · "
            f"Missing {count('missing', 'eod_missing')}")
    lines = [head]
    missing = [r["name"] for r in rows if r["status"] in ("missing", "eod_missing")]
    late = [f"{r['name']} {r['at']}" for r in rows if r["status"] in ("late", "eod_late")]
    if missing:
        lines.append("Missing: " + ", ".join(missing))
    if late:
        lines.append("Late: " + ", ".join(late))
    if unmatched:
        lines.append("Unmatched submissions: " + ", ".join(f'"{u}"' for u in unmatched) + " (which rep?)")
    blockers = post_blockers(cfg, a, rdate, rows, unmatched, bump, messages, guard_reason)
    if not bump:
        status = "nothing to post"
    elif not blockers:
        try:
            status = "bump posted " + post(cfg, a, rdate, bump)
        except Exception as e:
            status = f"FAILED to post ({e}). Read the channel before any retry; never post twice."
            lines.append(f'Draft: "{bump}"')
    else:
        lines.append(f'Would post: "{bump}"')
        status = "DRAFT (" + "; ".join(blockers) + ")"
    lines.append(status)
    if write and (a.check == "final" or a.date):
        out_dir = ROOT / "data/eod"
        out_dir.mkdir(parents=True, exist_ok=True)
        (out_dir / f"{rdate}.json").write_text(json.dumps({"report_date": str(rdate), "check": a.check,
                                                           "rows": rows, "unmatched": unmatched}, indent=2))
    log_run(rdate, a.check, head.replace("\n", " | ") + " | " + status, write)
    print("\n".join(lines))
    return 0


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("check", help="run the first or final EOD check")
    c.add_argument("--check", choices=["first", "final"], default="first")
    c.add_argument("--config", default="context/cog.json")
    c.add_argument("--messages", help="a saved JSON file of Slack messages instead of reading Slack (never posts)")
    c.add_argument("--now", help="pretend the time is this ISO local time, for tests and demos (never posts)")
    c.add_argument("--date", help="replay a past report date, YYYY-MM-DD (never posts)")
    c.add_argument("--post", action="store_true", help="post the bump if every guard passes")
    c.add_argument("--no-write", action="store_true", help="write no run log or results (demos)")
    sys.exit(cmd_check(p.parse_args()))


if __name__ == "__main__":
    main()
