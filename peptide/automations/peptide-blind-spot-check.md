NAME: Blind-spot check
OWNER: Peptide Operator
WORKSPACE: ~/chris-peptide
WHEN: Fridays at 11:00 AM (Eastern)
MILESTONE: M6
STATUS AT INSTALL: reserved for a later milestone (do not create yet)
---
Stop check: if state/STOP exists, append "<time ET> · STOPPED" to the run log and stop.
Switch check: read state/automations.md. If "Blind-spot check" isn't listed there as "on" or "test", append "<time ET> · Blind-spot check · SKIPPED_OFF" to runs/runs-<YYYY-MM>.md and stop.
Test mode: if it's listed as "test", send every message to Chris only, never to a channel or anyone else, and start each message with "TEST".
Isolation guard: work only in ~/chris-peptide and this account's connected apps. If context/owner.md is missing, append "<time ET> · Blind-spot check · NO_CLIENT_SOURCE" to the run log and stop. Never use another bot's files, logins or memory.
Lean run: read only what this job needs. If nothing changed, append "<time ET> · Blind-spot check · NO_CHANGE" to the run log and stop.
Run log: when you finish, append "<time ET> · Blind-spot check · EXECUTED · <one-line result>" to runs/runs-<YYYY-MM>.md, or FAILED with the reason. A source you couldn't read is UNKNOWN in your output, never zero.

Use the offer-pulse skill, section Friday blind-spot check. From this week's pulses in daily/, the payments, the CRM and vault/Clients/, name the two things that are true this week that nobody is looking at (refunds, chargebacks, a stale channel, a slipping step, one-source dependency), each with evidence and a first step.
Send Chris one short message and log it in vault/Offer/Blind-spots.md. Change nothing.
