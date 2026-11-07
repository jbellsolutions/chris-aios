---
name: cog-rep-scorecard
description: Compute each COG closer's and setter's daily and weekly Sales Compliance Score (0-100) from logged compliance events, with the 30-day patterns behind it. Use in the Monday weekly review or when Chris asks about a rep.
---

# Rep scorecard

1. Read `docs/KPI-DEFINITIONS.md` → "Sales Compliance Score" for the components, weights and formulas. Never change the weights unless Chris asks; record any change in `vault/decisions/`.
2. For each active rep (roster in `context/cog.json`), compute each component from the events and appointment rows in `vault/daily/` and `vault/reps/<Name>.md`:
   - over the week (Mon–Sun ET)
   - over the trailing 30 days
3. Leave out components with no data, and re-normalise the weights. Show "n/a" rather than 100% or 0%. A component whose source was `UNKNOWN` that week is "n/a", not a low score.
4. **Patterns** (the part Chris cares about), stated as counts with dates:
   - "missed no-show SOP 7× in 30 days (Oct 2, 5, 9…)"
   - "dispositions late every Friday"
   - "EOD late 4 of last 5 days"
5. Update each rep note: a `## Scores` table, newest week first, plus links to the event days.
6. **Output to Chris, sorted lowest score first.** Scores go to Chris only, never to a channel or a rep:

```
Weekly scorecards — w/e Sun Oct 25
Alex 97 · Dana 95 (setter) · John 94 · Sarah 88 · Mike 71 ⚠
Mike 71: KPI 80% · Dispo 74% · No-show FU 60% · Calendar 85% · Lead resp 58%
  pattern: no-show SOP missed 5× in 30d; KPI vs GHL live-call mismatch 3×
```

**A score is a pointer, not a verdict.** Always include the evidence for anyone under 80 or down 10 or more points week over week.
