NAME: New bookings sweep
OWNER: Pre-Call Concierge
WORKSPACE: ~/chris-aios
WHEN: Every day at 1:00 PM (Eastern)
MILESTONE: M8
STATUS AT INSTALL: reserved for a later milestone (do not create yet)
---
Stop check: if state/STOP exists, append "<time ET> · STOPPED" to the run log and stop.
Switch check: read state/automations.md. If "New bookings sweep" isn't listed there as "on" or "test", append "<time ET> · New bookings sweep · SKIPPED_OFF" to runs/runs-<YYYY-MM>.md and stop.
Test mode: if it's listed as "test", send every message to Chris only, never to a channel or anyone else, and start each message with "TEST".
Isolation guard: work only in ~/chris-aios and this account's connected apps. If context/owner.md is missing, append "<time ET> · New bookings sweep · NO_CLIENT_SOURCE" to the run log and stop. Never use another bot's files, logins or memory.
Lean run: read only what this job needs. If nothing changed, append "<time ET> · New bookings sweep · NO_CHANGE" to the run log and stop.
Run log: when you finish, append "<time ET> · New bookings sweep · EXECUTED · <one-line result>" to runs/runs-<YYYY-MM>.md, or FAILED with the reason. A source you couldn't read is UNKNOWN in your output, never zero.

Use the precall-indoctrination-sequence skill for COG appointments booked since the morning run. If there are none, write NO_CHANGE and stop. Draft briefs and sequences only, and send Chris one batch to approve. Update daily/<today>/precall.md.
