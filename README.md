# Chris's AIOS

Chris's AI operating system for Circle of Greatness, WeScale Marketing, his personal life and the peptide business. It runs in **Codex** on his Mac. He pastes two messages, answers five questions, and it sets itself up.

- **Install:** `INSTALL-PROMPT.md` (two pastes); Codex follows `START-HERE.md`.
- **Business:** `~/chris-aios`. The Chief of Staff runs the COG Sales Manager: the 11:30 PM EOD check and bump, the 8 AM sales report, the 8:30 AM brief.
- **Life:** `~/chris-life` (copied from `life/` at setup). Weekends, dates, money (read-only), birthdays. Never mixes with business.
- **Peptide:** `~/chris-peptide` (copied from `peptide/` at setup). The offer, client delivery, compliance guardrails, the ads and scale team.
- **Rules:** `AGENTS.md`. Nothing goes out without his yes; the one standing approval is enforced in `tools/eod_check.py`.
- **Plan:** `PROJECT_CHARTER.md`. **How it was built:** `docs/BUILD-RECORD.md`.

Test it: `python3 -m unittest discover -s tests`, then the demo:

```bash
python3 tools/eod_check.py check --config tests/fixtures/cog.test.json --messages tests/fixtures/kpi-channel.json --check final --now 2026-11-07T00:46 --no-write
```
