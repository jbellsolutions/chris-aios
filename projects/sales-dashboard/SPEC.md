# Sales dashboard: project spec

**Owner:** Chris · **Builder:** Codex or Claude Code · **Runs on:** Google Sheets plus a dashboard Chris opens on his phone · **Status:** draft

## 0. Charter

**What:** One page with COG's numbers as charts: team and rep trends, compliance scores, no-show and disposition violations, and 30-day patterns. It's updated every morning from what the COG Sales Manager already collects.

**Why:**
- On Oct 6 Chris agreed he wanted charts and graphs from the sales tracking.
- His Oct 16 checklist has the agent working across Slack, dashboards and the CRM.
- On Oct 15 he said the morning report should be his single source of truth.

**Users:** Chris, and later his rep leads.

**Done means:** Chris opens one link on his phone at 8 AM and sees yesterday and the last 30 days, and every number on it matches the COG Sales Manager's morning report.

## 1. How it works

1. Each morning the COG Sales Manager writes yesterday's numbers to the `Dashboard data` sheet in Drive. There is one row per rep per day, with the metrics in `docs/KPI-DEFINITIONS.md` or the repo's KPI file.
2. The dashboard reads that sheet. Choose the tool on the requirements, measuring each option (for example Looker Studio or a small web page):
   - phone-friendly;
   - free or cheap;
   - no new logins for reps;
   - updates by itself.
3. Charts:
   - team cash, calls and close rate (30 days);
   - show rate;
   - compliance score by rep;
   - no-show SOP violations;
   - disposition errors;
   - late or missing EODs;
   - leaderboard.

## 2. Requirements

| # | Requirement | Must / should |
|---|---|---|
| 1 | Numbers match the morning report exactly | Must |
| 2 | Missing data shows as "unknown", never 0 | Must |
| 3 | Readable on a phone | Must |
| 4 | Only Chris (and people he adds) can open it | Must |
| 5 | Filter by rep and date range | Should |

## 3. Data

Rep names and numbers are COG's data. They stay in Chris's Drive and the dashboard tool, and never go in this repo.

## 4. Integrations

Google Sheets (written by the COG Sales Manager) and the dashboard tool. Access is read-only for viewers.

## 5. INPUT NEEDED

- Who else should see it.
- Which charts matter most. Chris ranks the list above.

## 6. Acceptance

- [ ] Seven days of numbers on the dashboard match the morning reports.
- [ ] It opens fast on Chris's phone.

## 7. Build order

1. The data sheet and the morning write.
2. Three core charts.
3. The rest.
4. Sharing.

## 8. Out of scope

Editing data from the dashboard.
