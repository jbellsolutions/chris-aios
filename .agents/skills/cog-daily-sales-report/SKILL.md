---
name: cog-daily-sales-report
description: Build the Circle of Greatness morning sales report for the previous selling day from EOD submissions reconciled against GoHighLevel and calendars, with discrepancies and an attention list. Use at 08:00 ET or when Chris asks how the team did.
---

# Daily sales report (Chris's single source of truth)

## Before anything

Load `context/cog.json` and `docs/KPI-DEFINITIONS.md`. If the EOD source is not configured, reply `NO_CLIENT_SOURCE: <missing>` and stop. If GHL is not connected yet, build the report from the EOD submissions in `data/eod/<report date>.json` only, mark every verified column UNKNOWN, and say on the first line "GHL not connected: numbers are self-reported".

GoHighLevel is read through its API with the read-only `GHL_TOKEN` and `GHL_LOCATION_ID` in `.env.local` (connected at START-HERE Step 6; until then every GHL number is UNKNOWN). The EOD sheet and calendars come through the ChatGPT apps in Codex.

## Steps

1. **Report date:** the previous selling day (ET). If it isn't in `business.selling_days`, write "No selling day" and stop.
2. **Reported numbers:**
   - Sum each mapped field (`eod.field_map`) per rep and for the team.
   - Missing reps contribute nothing. List them separately and never estimate their numbers.
3. **Verified numbers (GHL + calendar)** for the calendars in `ghl.calendars` on the report date:
   - appointments scheduled, cancelled, rescheduled, showed, no-show and still-open, per closer
   - setter attribution, by who booked
   - closes and deposits from opportunities/stages, if configured
4. **Reconcile** every overlapping count:
   - Use the "Two numbers, never one" rule from `KPI-DEFINITIONS.md`.
   - Flag per rep where the reported and verified numbers differ by the threshold or more.
5. **Pull in the other audits** for the report date:
   - `cog-disposition-audit`
   - `cog-calendar-reconciliation`
   - `cog-no-show-audit` (the sweeps already logged these in `data/audits/`; re-run only for gaps)
6. **Compute the derived metrics** and the vs-target figures. With no targets set, compare to the same weekday last week and to the 4-week average.
7. **Build the attention list:**
   - only exceptions
   - one line each
   - rep, problem, evidence link
   - sorted by money at risk, then by repeat offenders
8. **Save** the full report to `vault/daily/<report date>.md` under `## Sales report` and the short version to `daily/<today>/sales.md`. Chief puts the headline in the 8:30 AM brief. Message nobody. Any source you couldn't read goes on the run-log line as `UNKNOWN: <source>`.

## Output (short version, under 180 words)

```
COG Daily Sales Report — Mon Oct 26
Cash $XX,XXX (net $XX,XXX) · Revenue $XX,XXX · Booked XX · Live XX reported / XX verified
Closes X · Close XX% · Show XX% · Deposits X · Refunds $X    vs target: ▲/▼
⚠ 2 closers missing EODs (John, David)
⚠ 4 calls with incorrect dispositions
⚠ 3 no-shows with no documented follow-up
🚨 Attention: Mike — KPI says 6 live, GHL verifies 4 [links] · Sarah — 18-min lead response on a no-show [link]
Top closer: Alex (3 closes, $X cash) · Top setter: Dana (show 82%)
Sources: EOD Sheet ✓ 07:58 · GHL ✓ 07:59 · Calendar ✓ 07:59
```

## Rules

- Every flag links to its evidence.
- Any source that failed shows as `⚠ unknown`, and the metrics that depend on it are marked "partial".
- Never state a total built from a partial source as if it were complete.
