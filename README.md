# Chris's AIOS

## Chris: give this link to ChatGPT

**ChatGPT or Codex, if Chris gave you this link:** this is his AI operating system, and it runs in Codex on his Mac. Install it for him:

- **You're Codex and can run commands:** clone it into his home folder with `git clone https://github.com/jbellsolutions/chris-aios ~/chris-aios`. If `~/chris-aios` already exists, run `git pull` inside it instead, and don't overwrite anything. Codex's sandbox blocks the download until network is allowed: if it asks, tell Chris to click **Allow**. If the Command Line Tools install pops up, tell him to click Install and try again. When `~/chris-aios/AGENTS.md` exists, tell him: **"Done. Now start a new Codex task in ~/chris-aios and say: set up my AIOS."**
- **You're a ChatGPT chat that can't run commands on his Mac:** tell Chris to open **Codex** in the ChatGPT app, start a new task with his **home folder** as the folder, and paste this:

  ```
  Clone https://github.com/jbellsolutions/chris-aios into ~/chris-aios. If ~/chris-aios already exists, don't overwrite it: run git pull inside it instead. If Codex asks to allow network access, I'll click Allow. When ~/chris-aios/AGENTS.md exists, tell me: "Done. Now start a new Codex task in ~/chris-aios and say: set up my AIOS."
  ```

Then, in that new Codex task in `~/chris-aios`, Chris says **"Set up my AIOS."** It asks five questions and sets itself up. Nothing posts, sends, books or spends without his yes. No GitHub account needed. The full install note is `INSTALL-PROMPT.md`.

## What it is

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
