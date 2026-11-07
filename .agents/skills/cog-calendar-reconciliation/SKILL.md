---
name: cog-calendar-reconciliation
description: Reconcile every closer's scheduled sales calls (closer, lead, time, status, outcome) between calendars and GoHighLevel and find appointments that never got a final status. Use inside the morning report, the no-show sweeps, or when Chris asks about a specific call.
---

# Calendar reconciliation

Calendars come through the ChatGPT apps in Codex; GoHighLevel through its API with the read-only `GHL_TOKEN` in `.env.local` (START-HERE Step 6). Load `context/cog.json`.

## Steps

1. For the window (default: the report date, or "since the last sweep"), list every appointment on the sales calendars (`ghl.calendars` and each rep's `calendar_id`), with:
   - `closer`, from the calendar owner or the GHL assigned user
   - `lead`: GHL contact name and ID
   - `start`, in ET
   - `status` (GHL)
   - `outcome`/disposition
   - `booked_by` (setter)
2. Match calendar events to GHL appointments by event ID, then by lead + start time within 15 minutes.
   - A calendar event with no matching GHL appointment, or the reverse, is a `calendar_mismatch`.
   - List them and don't guess which one is right.
3. For each appointment whose start has passed, answer Chris's four questions, with evidence for each:
   - **Did the lead show?** Status, call duration over 2 minutes, or a closer note.
   - **Was there a live call?** A call record or meeting link activity.
   - **Was it dispositioned?** The configured disposition field is set.
   - **Was there a follow-up?** A next appointment, task or follow-up disposition.
4. Still "booked/confirmed" at the morning report means `calendar_stale`.
5. Write one row per appointment to `vault/daily/<date>.md` under `## Appointments`:

```
14:00 · John → Sarah Smith (#c_123) · showed ✓ · live ✓ (34m) · dispo "Follow Up" ✓ · follow-up Thu 11:00 ✓
15:00 · John → Ray Ortiz (#c_456) · NO-SHOW · dispo — ✗ · follow-up — ✗ → see no-show audit
```

## Rules

- Evidence over assumptions. If call records aren't readable, mark "live: unknown", not "live: no", and put `UNKNOWN: <source>` on the run-log line.
- Don't edit calendars or GHL.
