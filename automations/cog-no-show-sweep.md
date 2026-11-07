NAME: No-show sweep
OWNER: COG Sales Manager
WORKSPACE: ~/chris-aios
WHEN: Every day at 12:00 PM, 3:00 PM, 6:00 PM and 9:00 PM (Eastern)
MILESTONE: M3
STATUS AT INSTALL: reserved for a later milestone (do not create yet)
---
Stop check: if state/STOP exists, append "<time ET> · STOPPED" to the run log and stop.
Switch check: read state/automations.md. If "No-show sweep" isn't listed there as "on" or "test", append "<time ET> · No-show sweep · SKIPPED_OFF" to runs/runs-<YYYY-MM>.md and stop.
Test mode: if it's listed as "test", send every message to Chris only, never to a channel or anyone else, and start each message with "TEST".
Isolation guard: work only in ~/chris-aios and this account's connected apps. If context/owner.md is missing, append "<time ET> · No-show sweep · NO_CLIENT_SOURCE" to the run log and stop. Never use another bot's files, logins or memory.
Lean run: read only what this job needs. If nothing changed, append "<time ET> · No-show sweep · NO_CHANGE" to the run log and stop.
Run log: when you finish, append "<time ET> · No-show sweep · EXECUTED · <one-line result>" to runs/runs-<YYYY-MM>.md, or FAILED with the reason. A source you couldn't read is UNKNOWN in your output, never zero.

Use the cog-no-show-audit skill for COG appointments that ended since the previous sweep (since 12:00 AM ET for the first one). If none ended, write NO_CHANGE and stop.
For each no-show, check the SOP in context/cog.json against GoHighLevel activity: call attempts, the text, the setter notified, the status updated, within the SOP window. Write findings to data/audits/<date>-no-show.md. Send Chris one grouped message only if there are violations, each with its evidence link. Never message a rep.
