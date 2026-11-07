---
name: cog-disposition-audit
description: Audit GoHighLevel dispositions against calendar status, call/SMS activity, notes and the closer's EOD KPI submission, and list every inconsistency instead of trusting the KPI form. Use in the morning report or when numbers don't add up.
---

# Disposition audit

Load `context/cog.json` (`ghl.dispositions`, `ghl.appointment_status_map`, `thresholds`). GoHighLevel is read through its API with the read-only `GHL_TOKEN` and `GHL_LOCATION_ID` in `.env.local` (connected at START-HERE Step 6; until then every GHL number is UNKNOWN). If a source can't be read, put `UNKNOWN: <source>` on the run-log line and mark the flags that depend on it "unknown", not "ok".

## Compare, per appointment and per closer

**Calendar status + GHL activity (calls, SMS, notes) + disposition field + the closer's EOD numbers**

## Flags (each with evidence links)

| Flag | Rule |
|---|---|
| Missing disposition | Past start + 2h, disposition empty |
| Not an allowed value | Disposition not in `ghl.dispositions.allowed` |
| Live call marked no-show | Call record over 2 min, or meeting activity, but status/disposition says no-show |
| No-show marked live | No call or meeting activity, but disposition says showed/closed/follow-up |
| Follow-up not marked | Closer note or next appointment shows a follow-up, but disposition isn't follow-up |
| Duplicate disposition | The same lead dispositioned twice for one appointment with conflicting values |
| Appointment never updated | Still booked/confirmed after the day ended |
| KPI vs GHL mismatch | The EOD form's `live_calls`/`no_shows`/`closes` differ from the verified counts by the threshold or more |

Worked example (from Chris's brief):

```
Mike — reported 7 live calls · GHL: 5 completed, 1 no-show, 1 with no disposition
 → kpi_mismatch (+2) · disposition_missing (1) [links]
```

## Rules

- Report the inconsistency. **Don't decide who's right.** Chris (or the closer, through Chris) fixes the source.
- Log the events to the rep ledgers (`vault/reps/<Name>.md`).
- Never edit dispositions. The GoHighLevel token is read-only, so nothing here could. If Chris says "fix it", draft the exact change (field, old → new, appointment link) for him or his team to make, and say it is a draft.
