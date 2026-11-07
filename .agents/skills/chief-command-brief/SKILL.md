---
name: chief-command-brief
description: Chris's one-screen morning brief - what needs him today across COG, approvals waiting, inbox, calendar, prospect prep and team health. Use at 08:30 ET, for the Friday wrap, or when Chris asks "what's my day?".
---

# Command brief

1. **Collect**, without redoing the specialists' work:
   - the COG Sales Manager's report: `daily/<today>/sales.md` (attention list and headline numbers)
   - team health, from the `team-health-check` skill: routines that were due and didn't run, sources that were `UNKNOWN` twice in a row
   - the Pre-Call Concierge's prep status for today's booked calls: `daily/<today>/precall.md`
   - drafts waiting for approval from the Growth Operator: `daily/<today>/growth.md`
   - the Sales Coach's call QC (calls scored, the best call, up to three calls that need Chris): `daily/<today>/coaching.md`. It runs on weekdays only, so on Saturdays and Sundays a missing note is expected, not "not in"
   - approvals still waiting on Chris from every bot (`queue/approved/`)
   - today's calendar, on every connected calendar
   - inbox items that need a reply from him, and his Slack DMs and mentions since the last brief
2. **Rank "Needs you":**
   - money at risk
   - deadlines today
   - people waiting on Chris
   - repeat problems
   - Five items at most. Everything else goes in one summary line.
3. Each item has a link and, where possible, a ready action ("draft ready", "approve?", "pick A or B").
4. If a specialist didn't report, say so ("COG report not in"). Never fill its numbers in yourself.
5. **Number the items** and write them to `queue/approved/<today>.md` exactly as shown, so "approve 1, 3" covers items 1 and 3 as shown. When Chris answers, record his exact words there and send each owning bot only its own approved items. If an item changes, ask again.
6. Send it to Chris in your chat in under 200 words, using the format in `agents/01-chief.md` ("The morning command brief"). Save it to `daily/<today>/brief.md` and append it to `vault/daily/<today>.md` under `## Brief`.

**Friday wrap** (17:00 ET): the week's wins, misses, decisions made (from `vault/decisions/`), open decisions, the top 3 for next week, routine reliability and the week's usage (from `team-health-check`). Under 200 words. Save it to `vault/Weekly/<week>-wrap.md`.
