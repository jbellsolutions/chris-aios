---
name: cog-eod-compliance
description: Nightly EOD KPI compliance for Circle of Greatness: who was expected, who submitted, who is late or missing, repeat offenders, and the one Slack bump. Use at the 11:30 PM ET first check, the 12:45 AM final check, or when Chris asks "who's missing EODs?".
---

# EOD KPI compliance

**The tool does the check and the only post. You never post the bump yourself**: not through the Slack app, not with curl, not in a test. `tools/eod_check.py` refuses to post unless every guard holds (its docstring lists them). If it says DRAFT, the bump stays a draft.

## Run it

| Situation | Command (from `~/chris-aios`) |
|---|---|
| The 11:30 PM automation | `python3 tools/eod_check.py check --check first --post` |
| The 12:45 AM automation | `python3 tools/eod_check.py check --check final --post` |
| The automation is `test` in `state/automations.md` | The same command **without** `--post` |
| Chris asks "who's missing?" during the evening | `python3 tools/eod_check.py check --check first` (no `--post`) |
| Chris asks about a past night | `python3 tools/eod_check.py check --date YYYY-MM-DD` |
| No Slack token yet (Slack came through the Codex Slack app) | Read that night's KPI channel with the Slack app, thread replies included. Save it as a JSON list of messages (`ts`, `user`, `bot_id`, `text`) to `data/eod/<date>.messages.json`, then run with `--messages` that file and `--date`. This path never posts; Chris pastes the bump himself if he wants |

## Then

1. Send Chris the tool's output exactly as printed: the table, then either `bump posted <link>` or the `DRAFT (...)` line with the bump it would post. Don't reword it.
2. Copy the table into `vault/daily/<report date>.md` under `## EOD compliance`, and into `daily/<today>/sales.md` for the morning brief.
3. At the final check, append each rep's result to `vault/reps/<Name>.md` (`eod_missing` or `eod_late`, with the date). Count each rep's misses over the last 30 days and name anyone at 3 or more as a repeat offender.
4. If the output says `NO_CLIENT_SOURCE`, `UNKNOWN`, `unmatched` or `nobody submitted`, put the one fix on `queue/needs-chris.md` ("which rep is 'Jon S.'?", "the KPI channel came back empty: is it the right channel?").

## Never

- Post, edit, react, thread-reply or DM anyone in Slack yourself.
- Treat an unreadable source as "everyone submitted" or "everyone missing".
- Change the bump wording. It lives in `context/cog.json`, and changing it cancels the standing approval.
- Edit or delete anyone's submission.
