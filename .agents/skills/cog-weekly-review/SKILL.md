---
name: cog-weekly-review
description: Weekly COG sales-management review - team trends, rep scorecards, recurring problems, and a split of what needs Chris's judgment versus what can be automated next. Use Monday 08:30 ET or when Chris asks for trends.
---

# Weekly review

1. Run `cog-rep-scorecard` for the week that just ended.
2. **Team trends:** for cash, closes, live calls, show %, close % and cash per live call, show this week vs last week vs the 4-week average, plus vs target if one is set.
   - Call out any move of 15% or more, and the reps driving it.
3. **Recurring problems** (3 or more occurrences), from the vault (`vault/`):
   - top objections, from the Growth Operator's call notes if available
   - disposition error types
   - no-show SOP steps most often missed
   - setters whose booked calls show worst
4. **Attention vs. automate**, two lists:
   - **Needs Chris:** coaching conversations, a policy decision, a target change, a rep at risk. One line each, with evidence.
   - **Can be automated/handled:** repeat patterns the team could fix with a process, an asset or a reminder. Recurring sales problems go to the Growth Operator as asset requests in `queue/jobs/growth-operator/` (for example, "no-show text template reps can paste"). Show-rate patterns go to the Pre-Call Concierge in `queue/jobs/precall-concierge/`. Routine ideas go to Chief in `queue/jobs/chief/`.
5. **Source health for the week:** any night or sweep in the run log (`runs/runs-<YYYY-MM>.md`) that ran with an `UNKNOWN` source, so Chris knows which numbers were partial.
6. Save the review to `vault/Weekly/<week>.md`. Send Chris a summary of 250 words or less. Rep scores go to Chris only, never to a channel.

Close with **three decisions for Chris this week**, each with a recommended option.
