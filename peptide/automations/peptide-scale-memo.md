NAME: Weekly scale memo
OWNER: Scale Advisor
WORKSPACE: ~/chris-peptide
WHEN: Sundays at 6:00 PM (Eastern)
MILESTONE: M6
STATUS AT INSTALL: reserved for a later milestone (do not create yet)
---
Stop check: if state/STOP exists, append "<time ET> · STOPPED" to the run log and stop.
Switch check: read state/automations.md. If "Weekly scale memo" isn't listed there as "on" or "test", append "<time ET> · Weekly scale memo · SKIPPED_OFF" to runs/runs-<YYYY-MM>.md and stop.
Test mode: if it's listed as "test", send every message to Chris only, never to a channel or anyone else, and start each message with "TEST".
Isolation guard: work only in ~/chris-peptide and this account's connected apps. If context/owner.md is missing, append "<time ET> · Weekly scale memo · NO_CLIENT_SOURCE" to the run log and stop. Never use another bot's files, logins or memory.
Lean run: read only what this job needs. If nothing changed, append "<time ET> · Weekly scale memo · NO_CHANGE" to the run log and stop.
Run log: when you finish, append "<time ET> · Weekly scale memo · EXECUTED · <one-line result>" to runs/runs-<YYYY-MM>.md, or FAILED with the reason. A source you couldn't read is UNKNOWN in your output, never zero.

Use the scale-advisor skill, section Sunday scale memo. From this week's pulses in daily/ and the libraries in libraries/, send Chris the three biggest levers, what the frameworks say about each (cited), and one experiment with its success metric, under 200 words.
Save the memo to vault/Advisor/Memos/<week>.md. Log the experiment in vault/Advisor/Experiments.md, and fill in last week's result if the numbers are in.
