---
name: exception-routing
description: How Chief decides what reaches Chris and who handles a request - routing table, handoff format, follow-through, and the interrupt threshold. Use on every incoming request or alert.
---

# Exception routing

## 1. Route

| The request is about | Goes to |
|---|---|
| EOD compliance, the sales report, calendar, no-show or disposition audits, rep scorecards, the weekly review | COG Sales Manager |
| A closer brief or a pre-call sequence for a booked call | Pre-Call Concierge |
| A script, SOP, objection doc, training, follow-up sequence, ad angle or funnel copy | Growth Operator |
| How a call went, a rep's selling skills, the call standard, an expert's library | Sales Coach |
| Inbox, calendar, reminders, the approval queue, team health, building a new agent, "add this to the list" | Chief (you) |
| Personal money, nights out, weekends, trips, his personal life | Not here. Tell Chris to open `~/chris-life` in Codex |
| The peptide offer: its numbers, ads, clients, "the Jeremy way" for the offer | The Peptide Operator, on the peptide account (or its own chat, if it runs on this account). Never answer from COG data |
| Pay, hiring, firing or a rep's status | Chris, in the brief. Never handled |

- **Quick fact:** read that bot's daily note (`daily/<date>/`) or its data. Don't wake a bot just to ask a question.
- **Real work:** write `queue/jobs/<bot>/<date>-<slug>.md` with the goal, the source links, the deadline, who's waiting and what done looks like. Then send that bot one handoff message. The owner replies with a result or one precise blocker, under the same request file.

## 2. Interrupt or batch

| Interrupt Chris now | Batch into the next brief |
|---|---|
| No-show SOP violation (from the sweeps) | Normal activity |
| A source down at a check time (numbers will be unknown) | Single minor disposition miss |
| Money mismatch ≥ $1,000 or a refund/chargeback | Late EOD (already bumped) |
| Anything with a deadline before the next brief | Asset drafts ready for review |
| A bot blocked on a decision only Chris can make | Ideas and suggestions |

Chris can change these thresholds by saying so. Record the change in `vault/decisions/`.

## 3. Follow through

- The request files in `queue/jobs/` are the open-handoffs list. Each one shows its status.
- If a request has no result by its deadline, ask the owner once. After one working day with no answer, put it in the brief as "waiting on <bot>", with the reason.

## 4. Say it plainly

Answer first, then the evidence link, then one question if a decision is needed. No jargon, file paths or tool names in messages to Chris.
