NAME: Friday wrap
OWNER: Chief
WORKSPACE: ~/chris-aios
WHEN: Fridays at 5:00 PM (Eastern)
MILESTONE: M3
STATUS AT INSTALL: reserved for a later milestone (do not create yet)
---
Stop check: if state/STOP exists, append "<time ET> · STOPPED" to the run log and stop.
Switch check: read state/automations.md. If "Friday wrap" isn't listed there as "on" or "test", append "<time ET> · Friday wrap · SKIPPED_OFF" to runs/runs-<YYYY-MM>.md and stop.
Test mode: if it's listed as "test", send every message to Chris only, never to a channel or anyone else, and start each message with "TEST".
Isolation guard: work only in ~/chris-aios and this account's connected apps. If context/owner.md is missing, append "<time ET> · Friday wrap · NO_CLIENT_SOURCE" to the run log and stop. Never use another bot's files, logins or memory.
Lean run: read only what this job needs. If nothing changed, append "<time ET> · Friday wrap · NO_CHANGE" to the run log and stop.
Run log: when you finish, append "<time ET> · Friday wrap · EXECUTED · <one-line result>" to runs/runs-<YYYY-MM>.md, or FAILED with the reason. A source you couldn't read is UNKNOWN in your output, never zero.

Use the chief-command-brief skill in Friday-wrap mode and the team-health-check skill's weekly part: the week's wins and misses, decisions made (vault/decisions/), open decisions, next week's top three, routine reliability from the run log, and this week's usage from Codex's usage meter.
If usage is past 80% of the normal share (PROJECT_CHARTER.md section 9), propose which optional routine to pause first and wait for Chris. Under 200 words. Save it to vault/Weekly/<week>-wrap.md.
