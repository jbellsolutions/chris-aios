NAME: Daily call QC
OWNER: Sales Coach
WORKSPACE: ~/chris-aios
WHEN: Weekdays at 7:30 AM (Eastern)
MILESTONE: M9
STATUS AT INSTALL: reserved for a later milestone (do not create yet)
---
Stop check: if state/STOP exists, append "<time ET> · STOPPED" to the run log and stop.
Switch check: read state/automations.md. If "Daily call QC" isn't listed there as "on" or "test", append "<time ET> · Daily call QC · SKIPPED_OFF" to runs/runs-<YYYY-MM>.md and stop.
Test mode: if it's listed as "test", send every message to Chris only, never to a channel or anyone else, and start each message with "TEST".
Isolation guard: work only in ~/chris-aios and this account's connected apps. If context/owner.md is missing, append "<time ET> · Daily call QC · NO_CLIENT_SOURCE" to the run log and stop. Never use another bot's files, logins or memory.
Lean run: read only what this job needs. If nothing changed, append "<time ET> · Daily call QC · NO_CHANGE" to the run log and stop.
Run log: when you finish, append "<time ET> · Daily call QC · EXECUTED · <one-line result>" to runs/runs-<YYYY-MM>.md, or FAILED with the reason. A source you couldn't read is UNKNOWN in your output, never zero.

Use the call-qc skill. The call source is calls.transcript_source in context/cog.json. If it still says REQUIRED, or context/call-standard.md is missing, append "<time ET> · Daily call QC · NO_CLIENT_SOURCE" to the run log and stop.
Read only the calls recorded since the last run (Monday's run covers the weekend). If there are none, append NO_CHANGE and stop. Score each one against the rubric with timestamps and save the scorecards in vault/coaching/Calls/. A call you can't read is UNKNOWN and listed; never score from a summary.
Write the totals, the best call and up to three calls that need Chris to daily/<today>/coaching.md for Chief's brief. Message Chris directly only when a call needs him today (a compliance problem, a deal at risk), under 120 words. Message no rep.
