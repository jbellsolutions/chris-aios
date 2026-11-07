NAME: Weekly creative brief
OWNER: Media Buyer
WORKSPACE: ~/chris-peptide
WHEN: Mondays at 10:00 AM (Eastern)
MILESTONE: M6
STATUS AT INSTALL: reserved for a later milestone (do not create yet)
---
Stop check: if state/STOP exists, append "<time ET> · STOPPED" to the run log and stop.
Switch check: read state/automations.md. If "Weekly creative brief" isn't listed there as "on" or "test", append "<time ET> · Weekly creative brief · SKIPPED_OFF" to runs/runs-<YYYY-MM>.md and stop.
Test mode: if it's listed as "test", send every message to Chris only, never to a channel or anyone else, and start each message with "TEST".
Isolation guard: work only in ~/chris-peptide and this account's connected apps. If context/owner.md is missing, append "<time ET> · Weekly creative brief · NO_CLIENT_SOURCE" to the run log and stop. Never use another bot's files, logins or memory.
Lean run: read only what this job needs. If nothing changed, append "<time ET> · Weekly creative brief · NO_CHANGE" to the run log and stop.
Run log: when you finish, append "<time ET> · Weekly creative brief · EXECUTED · <one-line result>" to runs/runs-<YYYY-MM>.md, or FAILED with the reason. A source you couldn't read is UNKNOWN in your output, never zero.

Use the ad-account-pulse skill, section Monday creative brief. Draft ten hooks and angles and three full ad concepts from this week's call objections, the Scale Advisor's latest memo in vault/Advisor/Memos/ and the ads winning now.
Check every concept against the ad platform's policy for this category and the "Claims we never make" list in OFFER.md. Drop any that fail.
Save the brief to vault/Ads/Briefs/<week>.md and as a new Google Doc, and send Chris the link and the top three hooks. Publish nothing.
