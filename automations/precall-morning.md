NAME: Booked-call briefs and sequences
OWNER: Pre-Call Concierge
WORKSPACE: ~/chris-aios
WHEN: Every day at 7:00 AM (Eastern)
MILESTONE: M8
STATUS AT INSTALL: reserved for a later milestone (do not create yet)
---
Stop check: if state/STOP exists, append "<time ET> · STOPPED" to the run log and stop.
Switch check: read state/automations.md. If "Booked-call briefs and sequences" isn't listed there as "on" or "test", append "<time ET> · Booked-call briefs and sequences · SKIPPED_OFF" to runs/runs-<YYYY-MM>.md and stop.
Test mode: if it's listed as "test", send every message to Chris only, never to a channel or anyone else, and start each message with "TEST".
Isolation guard: work only in ~/chris-aios and this account's connected apps. If context/owner.md is missing, append "<time ET> · Booked-call briefs and sequences · NO_CLIENT_SOURCE" to the run log and stop. Never use another bot's files, logins or memory.
Lean run: read only what this job needs. If nothing changed, append "<time ET> · Booked-call briefs and sequences · NO_CHANGE" to the run log and stop.
Run log: when you finish, append "<time ET> · Booked-call briefs and sequences · EXECUTED · <one-line result>" to runs/runs-<YYYY-MM>.md, or FAILED with the reason. A source you couldn't read is UNKNOWN in your output, never zero.

Use the precall-indoctrination-sequence skill for COG appointments in the next 72 hours that don't have a brief in vault/prospects/ yet. For each: read the prospect's GoHighLevel record read-only, profile them, write the one-page closer brief, and draft the timed sequence from the tagged content library.
Send Chris one batch to approve. Never message a prospect, add anyone to a workflow or change a contact. Skip anyone who opted out or has no consent on record, and say so. Write today's summary to daily/<today>/precall.md.
