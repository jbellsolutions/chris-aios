NAME: Weekly review and scorecards
OWNER: COG Sales Manager
WORKSPACE: ~/chris-aios
WHEN: Mondays at 8:30 AM (Eastern)
MILESTONE: M3
STATUS AT INSTALL: reserved for a later milestone (do not create yet)
---
Stop check: if state/STOP exists, append "<time ET> · STOPPED" to the run log and stop.
Switch check: read state/automations.md. If "Weekly review and scorecards" isn't listed there as "on" or "test", append "<time ET> · Weekly review and scorecards · SKIPPED_OFF" to runs/runs-<YYYY-MM>.md and stop.
Test mode: if it's listed as "test", send every message to Chris only, never to a channel or anyone else, and start each message with "TEST".
Isolation guard: work only in ~/chris-aios and this account's connected apps. If context/owner.md is missing, append "<time ET> · Weekly review and scorecards · NO_CLIENT_SOURCE" to the run log and stop. Never use another bot's files, logins or memory.
Lean run: read only what this job needs. If nothing changed, append "<time ET> · Weekly review and scorecards · NO_CHANGE" to the run log and stop.
Run log: when you finish, append "<time ET> · Weekly review and scorecards · EXECUTED · <one-line result>" to runs/runs-<YYYY-MM>.md, or FAILED with the reason. A source you couldn't read is UNKNOWN in your output, never zero.

Use the cog-weekly-review skill, which runs cog-rep-scorecard, for the week that just ended: team trends, scorecards lowest first with evidence, recurring problems, what needs Chris's attention vs what can be automated, source health, and three decisions for Chris.
Save it to vault/Weekly/<week>.md. Send it to Chris under 250 words. Write recurring sales problems as requests to queue/jobs/growth-operator/ and show-rate patterns to queue/jobs/precall-concierge/. Rep scores go to Chris only, never to a channel.
