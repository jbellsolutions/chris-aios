NAME: Offer morning pulse
OWNER: Peptide Operator
WORKSPACE: ~/chris-peptide
WHEN: Every day at 8:30 AM (Eastern)
MILESTONE: M6
STATUS AT INSTALL: reserved for a later milestone (do not create yet)
---
Stop check: if state/STOP exists, append "<time ET> · STOPPED" to the run log and stop.
Switch check: read state/automations.md. If "Offer morning pulse" isn't listed there as "on" or "test", append "<time ET> · Offer morning pulse · SKIPPED_OFF" to runs/runs-<YYYY-MM>.md and stop.
Test mode: if it's listed as "test", send every message to Chris only, never to a channel or anyone else, and start each message with "TEST".
Isolation guard: work only in ~/chris-peptide and this account's connected apps. If context/owner.md is missing, append "<time ET> · Offer morning pulse · NO_CLIENT_SOURCE" to the run log and stop. Never use another bot's files, logins or memory.
Lean run: read only what this job needs. If nothing changed, append "<time ET> · Offer morning pulse · NO_CHANGE" to the run log and stop.
Run log: when you finish, append "<time ET> · Offer morning pulse · EXECUTED · <one-line result>" to runs/runs-<YYYY-MM>.md, or FAILED with the reason. A source you couldn't read is UNKNOWN in your output, never zero.

Use the offer-pulse skill. If OFFER.md is missing, append "<time ET> · Offer morning pulse · NO_CLIENT_SOURCE" to the run log and stop.
Read yesterday's numbers from the sources listed in OFFER.md, the Media Buyer's daily/<today>/ads.md and the client tracker in vault/Clients/.
Send Chris one screen, under 120 words: the funnel from leads to cash against target and the 7-day average, the bottleneck with its evidence and who it's handed to, any overdue client step, and one action. Write the handoff to queue/jobs/<bot>/ and the pulse to daily/<today>/pulse.md. A source you can't read is UNKNOWN, never 0. If any peptide routine that was due since yesterday has no line in runs/runs-<YYYY-MM>.md, add one line: "<routine> didn't run: paused? Check Codex's automations list."
