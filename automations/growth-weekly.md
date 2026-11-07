NAME: Weekly call review
OWNER: Growth Operator
WORKSPACE: ~/chris-aios
WHEN: Tuesdays at 10:00 AM (Eastern)
MILESTONE: M8
STATUS AT INSTALL: reserved for a later milestone (do not create yet)
---
Stop check: if state/STOP exists, append "<time ET> · STOPPED" to the run log and stop.
Switch check: read state/automations.md. If "Weekly call review" isn't listed there as "on" or "test", append "<time ET> · Weekly call review · SKIPPED_OFF" to runs/runs-<YYYY-MM>.md and stop.
Test mode: if it's listed as "test", send every message to Chris only, never to a channel or anyone else, and start each message with "TEST".
Isolation guard: work only in ~/chris-aios and this account's connected apps. If context/owner.md is missing, append "<time ET> · Weekly call review · NO_CLIENT_SOURCE" to the run log and stop. Never use another bot's files, logins or memory.
Lean run: read only what this job needs. If nothing changed, append "<time ET> · Weekly call review · NO_CHANGE" to the run log and stop.
Run log: when you finish, append "<time ET> · Weekly call review · EXECUTED · <one-line result>" to runs/runs-<YYYY-MM>.md, or FAILED with the reason. A source you couldn't read is UNKNOWN in your output, never zero.

Use the call-review-to-assets skill on the last 7 days of calls (the Sales Coach's scorecards in vault/coaching/ first, transcripts only for calls it didn't score) and this week's COG weekly review, plus open requests in queue/jobs/growth-operator/. Update vault/assets/Backlog.md, then use sales-asset-builder to draft the top one to three assets as new Google Docs in the Drive folder "Codex Drafts". Every draft cites its evidence.
Send Chris a summary under 150 words. Nothing is published, shared or sent. Write daily/<today>/growth.md.
