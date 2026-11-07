---
name: team-health-check
description: Chief's daily and weekly check that every routine ran, every source is readable, approvals aren't stuck and the week's usage is sane, from the run log and the team registry. Use inside the 8:30 AM brief, the Friday wrap, or when something seems broken.
---

# Team health check

The facts are in two files. Read nothing else for this check unless a line points you there.
- The run log: `runs/runs-<YYYY-MM>.md`. Every routine appends one line per run: `<time ET> · <routine> · EXECUTED | NO_CHANGE | SKIPPED_OFF | NO_CLIENT_SOURCE | FAILED · <reason>`. A routine that couldn't read a source puts `UNKNOWN: <source>` in its reason.
- The registry: `context/team-registry.md`. It lists every routine with its owner, WHEN and state.

## Daily (inside the 8:30 AM brief; one line, details only on a problem)

1. **Routines.** For each routine the registry marks ON, work out the runs that were due since the last brief from its WHEN. A routine with several times (the no-show sweep) is due once per time. Look for its line in the run log, and in last month's log across a month boundary.
   - **No line for a due run: "didn't run, paused?"** Tell Chris to open Codex's automations list and check it isn't paused. Codex may pause a routine after a long absence, so this is the first thing to suspect.
   - `FAILED`: list the routine and the reason.
   - `SKIPPED_OFF` on a routine the registry says is ON: the registry and `state/automations.md` disagree. Say which one is wrong.
   - `NO_CHANGE` and `EXECUTED` are fine.
2. **Sources.** Don't poll anything. Use what the runs already recorded: a source named `UNKNOWN` in two runs in a row gets one line with the fix ("reconnect Slack in the ChatGPT apps in Codex", "re-check the EOD sheet's name"). Before 8:00 AM, an `UNKNOWN` source means the COG report will show it as unknown. Say so.
3. **Approvals.** Count the items waiting on Chris in `queue/approved/` and the oldest one's age. A request in `queue/jobs/` with no answer from its owner after one working day is "waiting on <bot>".
4. **Connections and keys.** Note any connection showing a re-sign-in prompt, or a Slack error of `invalid_auth` or `token_revoked`. Never print a key.

## Weekly (Friday wrap; under 200 words)

- **Routine reliability** from the run log: "62/63 runs ok", and which one failed.
- **Sources that were `UNKNOWN`,** and when.
- **Usage.** Read Codex's weekly usage meter once. If you can't read it, ask Chris for the percentage; never guess. Past 80% of the week's normal share (`PROJECT_CHARTER.md` §9), propose which optional routine to pause first (Growth, then the Pre-Call midday sweep) and wait for Chris.
- **Connections check.** Refresh the registry's "checked on" column with one cheap read each: the newest KPI channel message, tomorrow's calendar events, the EOD sheet's header row, one read-only GHL call (today's appointments), the unread count in Gmail.
- **Access review.** Each agent's connected apps and skills against its charter. Propose removing anything unused; Chris decides. The GoHighLevel token's scopes must all end in `.readonly`.
- **Skill freshness.** `git pull` in `~/chris-aios` brings Justin's updates; list any `SKILL.md` that changed.
- One improvement proposal: a routine or skill tweak, with the reason and evidence.

## Rules

- Chief may diagnose freely.
- Resuming or turning on a routine, changing access, or re-saving a skill **asks Chris first**.
- Never "fix" a data problem by editing the source data.
