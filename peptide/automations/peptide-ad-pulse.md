NAME: Daily ad pulse
OWNER: Media Buyer
WORKSPACE: ~/chris-peptide
WHEN: Every day at 8:00 AM (Eastern)
MILESTONE: M6
STATUS AT INSTALL: reserved for a later milestone (do not create yet)
---
Stop check: if state/STOP exists, append "<time ET> · STOPPED" to the run log and stop.
Switch check: read state/automations.md. If "Daily ad pulse" isn't listed there as "on" or "test", append "<time ET> · Daily ad pulse · SKIPPED_OFF" to runs/runs-<YYYY-MM>.md and stop.
Test mode: if it's listed as "test", send every message to Chris only, never to a channel or anyone else, and start each message with "TEST".
Isolation guard: work only in ~/chris-peptide and this account's connected apps. If context/owner.md is missing, append "<time ET> · Daily ad pulse · NO_CLIENT_SOURCE" to the run log and stop. Never use another bot's files, logins or memory.
Lean run: read only what this job needs. If nothing changed, append "<time ET> · Daily ad pulse · NO_CHANGE" to the run log and stop.
Run log: when you finish, append "<time ET> · Daily ad pulse · EXECUTED · <one-line result>" to runs/runs-<YYYY-MM>.md, or FAILED with the reason. A source you couldn't read is UNKNOWN in your output, never zero.

Use the ad-account-pulse skill. Read every account in context/ad-accounts.md, read only. If that file is missing, append "<time ET> · Daily ad pulse · NO_CLIENT_SOURCE" to the run log and stop.
Build yesterday's and the last 7 days' numbers per campaign. Judge each ad set against context/ad-rules.md; if that file is missing, report numbers only. Flag creative fatigue.
Save the pulse to vault/Ads/Pulse.md and daily/<today>/ads.md for the Peptide Operator's 8:30 pulse. Message Chris directly only when there's a SCALE, CUT or FATIGUE call or a flag, as numbered lines he can answer with "do it". Change nothing in any account.
