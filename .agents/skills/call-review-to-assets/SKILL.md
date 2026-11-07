---
name: call-review-to-assets
description: Mine COG sales-call transcripts and the COG Sales Manager's findings for recurring objections, drop-off points and top-closer language, and turn each recurring problem into an asset request in the backlog. Use for the Tuesday weekly run or when Chris shares calls.
---

# Call review → asset backlog

1. **Gather** the last 7 days of calls.
   - **Sales Coach scorecards first.** If the Sales Coach is on, its scorecards in `vault/coaching/Calls/` and its Friday patterns in `vault/coaching/Patterns/` already hold the objections, turning points and best lines, with timestamps. Use them, and read a transcript only to quote it or for a call it didn't score. Don't score calls again.
   - **Otherwise, transcripts** from `calls.transcript_source` in `context/cog.json`. If it isn't configured, reply `NO_CLIENT_SOURCE` and stop. If the source can't be read, put `UNKNOWN: <source>` on the run-log line and stop.
   - Also read open requests in `queue/jobs/growth-operator/`, including the Sales Coach's.
2. **Read the COG weekly review** (`vault/Weekly/`) for its recurring problems: show rate, no-shows, disposition errors.
3. **Extract from each call**, with timestamps:
   - objections (price, timing, spouse, trust, "need to think")
   - the point where the call turned
   - what the closer said that worked or failed
   - questions the prospect asked that pre-call content could have answered
4. **Cluster** the findings across calls. Keep clusters with 3 or more occurrences, or those tied to lost cash.
5. **For each cluster, write a backlog row** in `vault/assets/Backlog.md`:

```
| Problem | Evidence (calls, timestamps) | Proposed asset | Owner | Status |
| "Price" objection lost 6 calls | [call A 23:10], [call B 41:02]… | Rebuttal doc + 3 script lines + pre-call video pick | Growth Operator | proposed |
```

6. **Pick the top 1–3 by money at risk** and start them with `sales-asset-builder`. Send pre-call content gaps to the Pre-Call Concierge as requests in `queue/jobs/precall-concierge/`.
7. **Send Chris a summary** (under 150 words): the top problems, the assets started, and the decisions needed. Write `daily/<today>/growth.md` so Chief can put it in the brief.

## Rules

- Quote prospects only as much as needed.
- Never put full transcripts in Slack.
- No personal data in asset drafts.
