NAME: Weekly coaching report
OWNER: Sales Coach
WORKSPACE: ~/chris-aios
WHEN: Fridays at 3:00 PM (Eastern)
MILESTONE: M9
STATUS AT INSTALL: reserved for a later milestone (do not create yet)
---
Stop check: if state/STOP exists, append "<time ET> · STOPPED" to the run log and stop.
Switch check: read state/automations.md. If "Weekly coaching report" isn't listed there as "on" or "test", append "<time ET> · Weekly coaching report · SKIPPED_OFF" to runs/runs-<YYYY-MM>.md and stop.
Test mode: if it's listed as "test", send every message to Chris only, never to a channel or anyone else, and start each message with "TEST".
Isolation guard: work only in ~/chris-aios and this account's connected apps. If context/owner.md is missing, append "<time ET> · Weekly coaching report · NO_CLIENT_SOURCE" to the run log and stop. Never use another bot's files, logins or memory.
Lean run: read only what this job needs. If nothing changed, append "<time ET> · Weekly coaching report · NO_CHANGE" to the run log and stop.
Run log: when you finish, append "<time ET> · Weekly coaching report · EXECUTED · <one-line result>" to runs/runs-<YYYY-MM>.md, or FAILED with the reason. A source you couldn't read is UNKNOWN in your output, never zero.

Use the call-qc skill, section Friday report. From this week's scorecards in vault/coaching/Calls/, draft one coaching note per active rep in vault/coaching/Reps/, and write the team patterns to vault/coaching/Patterns/<week>.md: the top three objections with the best answer heard, where calls die, and one drill for the next team meeting. Add new clips to vault/coaching/Game-film.md.
Put each objection or winning line that came up three or more times in queue/jobs/growth-operator/ as a request.
Send Chris the team summary under 150 words, with the rep notes linked as drafts. Send nothing to reps.
