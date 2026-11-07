NAME: Monthly Dream check-in
OWNER: Chief
WORKSPACE: ~/chris-aios
WHEN: Mondays at 11:00 AM (Eastern)
MILESTONE: M10
STATUS AT INSTALL: reserved for a later milestone (do not create yet)
---
Stop check: if state/STOP exists, append "<time ET> · STOPPED" to the run log and stop.
Switch check: read state/automations.md. If "Monthly Dream check-in" isn't listed there as "on" or "test", append "<time ET> · Monthly Dream check-in · SKIPPED_OFF" to runs/runs-<YYYY-MM>.md and stop.
Test mode: if it's listed as "test", send every message to Chris only, never to a channel or anyone else, and start each message with "TEST".
Isolation guard: work only in ~/chris-aios and this account's connected apps. If context/owner.md is missing, append "<time ET> · Monthly Dream check-in · NO_CLIENT_SOURCE" to the run log and stop. Never use another bot's files, logins or memory.
Lean run: read only what this job needs. If nothing changed, append "<time ET> · Monthly Dream check-in · NO_CHANGE" to the run log and stop.
Run log: when you finish, append "<time ET> · Monthly Dream check-in · EXECUTED · <one-line result>" to runs/runs-<YYYY-MM>.md, or FAILED with the reason. A source you couldn't read is UNKNOWN in your output, never zero.

If today isn't the first Monday of the month, append NO_CHANGE and stop.
Use the dream-map skill, section Monthly Dream check-in. Read context/dream-map.md and context/team-registry.md. Send Chris, under 150 words: what went live this month, what's built but stuck and the one thing it waits on from him, and the one dream you recommend building next, with a one-line reason. Add one line: "Anything on your personal or peptide list first? That account's lead bot builds it."
On his yes, build it with him using the agent-builder-loop skill, one step at a time. Create nothing without his yes.
