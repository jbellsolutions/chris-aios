# COG KPI and compliance definitions

One set of definitions every bot and report uses. If Chris's form or GHL uses different words, map them in `context/cog.json`. Don't change these.

## The selling day

- A **report date** is the selling day being reported on.
- An EOD submitted before the cutoff (default 01:00 ET) counts for the previous calendar day.
- Times are Eastern (`business.team_timezone`) everywhere: in reports, Slack bumps and the vault.

## Standard EOD fields (what reps report)

| Field | Meaning |
|---|---|
| `calls_booked` | Setter: appointments they booked today (for any date) |
| `calls_scheduled` | Closer: appointments on their calendar today |
| `live_calls` | Closer: calls actually held with the prospect |
| `no_shows` | Scheduled calls the prospect didn't attend |
| `reschedules` / `cancellations` | Moved / cancelled before start |
| `offers_made` | Live calls where the offer and price were presented |
| `closes` | Signed / paid-in-full or deposit-to-close per COG's definition |
| `deposits` | Deposits taken (count) |
| `cash_collected` | Cash actually received today ($) |
| `revenue_contracted` | Total contract value closed today ($) |
| `refunds` | Refunds/chargebacks processed today ($) |
| `follow_ups_set` | Follow-up calls booked from today's live calls |
| `dials`, `conversations` | Setter activity, if tracked |

## Derived metrics

| Metric | Formula | Notes |
|---|---|---|
| **Calls due** | scheduled − cancelled − rescheduled (start time passed) | |
| **Show rate** | live_calls ÷ calls due | |
| **Close rate** | closes ÷ live_calls | Also report closes ÷ offers_made if offers are tracked |
| **Net cash** | cash_collected − refunds | |
| **Cash per live call** | cash_collected ÷ live_calls | |
| **Setter show rate** | showed ÷ due, for appointments that setter booked | From GHL, by `ghl_user_id` of the booker |
| **Setter booked→close** | closes from that setter's booked calls ÷ their booked calls | Lagging; weekly only |
| **vs. target** | actual ÷ target | Only when a target is set; otherwise vs. the same weekday last week and the 4-week average |

## Two numbers, never one

For every count that exists in both places (live calls, no-shows, closes), the report shows:

```
Live calls: 31 reported · 28 verified in GHL · ⚠ 3 unverified (Mike 2, John 1)
```

- **Reported** is from the EOD form.
- **Verified** is from GHL appointment status plus activity.
- The report never silently picks one.

## Compliance events (logged to `vault/reps/<Name>.md`)

| Event | Rule |
|---|---|
| `eod_missing` | No submission by the cutoff for a selling day the rep was active |
| `eod_late` | Submitted after the first check (23:30) but before the cutoff |
| `kpi_mismatch` | Reported vs. verified differs by ≥ `thresholds.kpi_vs_ghl_live_call_mismatch` |
| `disposition_missing` | Appointment past start + 2h with no disposition |
| `disposition_wrong` | Disposition contradicts evidence (live call marked no-show, no-show marked live, follow-up not marked, duplicate) |
| `calendar_stale` | Appointment past start still in "booked/confirmed" at the morning report |
| `no_show_sop_miss` | Any required step missing within the window (see `no_show_sop`) |
| `slow_lead_response` | First contact attempt on a no-show later than `thresholds.lead_response_minutes` |

**Repeat offender:** `repeat_offender_count` or more events of the same type in `repeat_offender_window_days`.

## Sales Compliance Score (0–100, daily and weekly)

Only components with data count. Weights are re-normalised over the components present. A rep with no appointments that day isn't scored on calendar or disposition.

| Component | Closer weight | Setter weight | Formula |
|---|---|---|---|
| KPI compliance | 25 | 35 | EODs on time ÷ EODs required (late = 0.5) |
| Disposition accuracy | 25 | — | Appointments correctly dispositioned ÷ appointments due |
| No-show follow-up | 20 | 15 | No-shows with full SOP in window ÷ no-shows (setter: "setter notified → re-book attempt" steps only) |
| Calendar compliance | 15 | — | Appointments with a final status by the morning report ÷ appointments due |
| Lead response | 15 | 25 | No-shows (closer) / new leads (setter) contacted within threshold ÷ total |
| Booking quality | — | 25 | Setter show rate vs. team setter average (capped at 100%) |

Example, as Chris wrote it:

```
John — 94/100 (week)
KPI compliance 100% · Disposition accuracy 96% · No-show follow-up 100% · Calendar compliance 92% · Lead response 88%
Pattern: no-show SOP missed 0× in 30 days; dispositions missed 3× (all Fridays)
```

**The score is a pointer, not a verdict.** Weekly reviews always show the events behind a score, with links.
