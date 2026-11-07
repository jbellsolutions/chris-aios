---
name: cog-no-show-audit
description: Check that every COG no-show got the full no-show SOP (two call attempts, a text, setter notified, GHL updated) inside the window, and alert Chris on violations. Use at the 12:00/15:00/18:00/21:00 ET sweeps, in the morning report, or on demand.
---

# No-show SOP audit (Chris: "one of the highest-value automations")

## Before anything

Load `no_show_sop`, `thresholds` and the roster from `context/cog.json`. If GHL isn't configured, reply `NO_CLIENT_SOURCE` and stop.

GoHighLevel is read through its API with the read-only `GHL_TOKEN` and `GHL_LOCATION_ID` in `.env.local` (connected at START-HERE Step 6; until then every GHL number is UNKNOWN). Slack is read through the Slack connector (the ChatGPT apps in Codex). If a source can't be read, put `UNKNOWN: <source>` on the run-log line.

## Steps

1. **Find no-shows** since the last sweep (since 12:00 AM ET for the first sweep of the day). If no COG appointment ended since the last sweep, write `NO_CHANGE` to the run log and stop. A no-show is an appointment whose start + `window_minutes` has passed and that is either:
   - GHL status in `appointment_status_map.no_show`, or
   - still open with no call activity: treat it as a **suspected no-show** and label it that way.
2. **For each no-show, gather evidence** from the start time to start + `window_minutes`:
   - **call_1 / call_2:** outbound calls from the closer's GHL user (or number) to the lead, timestamps in order.
   - **text:** an outbound SMS to the lead.
   - **setter_notified:** a Slack message mentioning the setter or the lead in the configured channels, or a GHL note or task assigned to the setter.
   - **ghl_updated:** the status is no-show and a disposition is set.
3. **Lead response:** minutes from the start to the first attempt. Compare with `thresholds.lead_response_minutes`.
4. **Mark each step:**
   - ✓ with a link
   - ✗ when the source was read and nothing was found
   - `?` when the source was unreadable. A `?` is never counted as a violation.
5. **Write the findings** to `data/audits/<date>-no-show.md`.
6. **Violation** = any ✗.
   - Log `no_show_sop_miss` (and `slow_lead_response` if it applies) to `vault/reps/<Closer>.md`.
   - Message Chris, one message per sweep, grouped:

```
⚠ No-show process violations (15:00 sweep)
John · Sarah Smith · 13:00 ET
  ✗ No outbound call detected  ✗ No text detected  ✓ Setter notified <link>  ✗ GHL disposition unchanged
Mike · Ray Ortiz · 14:00 ET · first call at +18 min (SOP: 5)
```

7. **No violations:** one line in the run log only (`EXECUTED · 0 violations`). Don't message Chris about normal activity.

## Real-time alerts (milestone M7, not yet)

A routine runs on a schedule, so these sweeps catch a violation within three hours, not within minutes. Alerts within minutes of an appointment need a GoHighLevel webhook to a routine trigger (milestone M7). Until then, say "real-time checks unavailable; sweeps only" in the weekly review.

## Never

- Contact the rep or the lead.
- Change GHL.
- Count unreadable evidence as a miss.
