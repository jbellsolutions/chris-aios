# Outbound test: project spec

**Owner:** Chris · **Builder:** Codex or Claude Code, then a Codex · **Runs on:** Codex, plus a cold email sending tool · **Status:** idea

## 0. Charter

**What:** A capped, measured test of agent-run cold email that books appointments for one offer Chris picks. The agent researches every lead itself, writes a personal first line for each, and books replies onto the calendar.

**Why:**
- On Oct 6 Chris saw Justin's agent running cold email that books appointments.
- Justin offered a slot for an outbound channel Chris wants to test.

**Users:** Chris.

**Done means:** One offer, one list of 500 researched leads and four weeks of sends. The result is booked calls per 1,000 emails and cost per booked call, compared with paid ads, and Chris decides scale or stop.

## 1. How it works

1. **The offer and the ideal customer**, from Chris.
2. **Leads.** The agent finds and researches every lead itself, with the browser and public sources. No rented enrichment databases.
3. **Copy.** Short, specific, one ask, reviewed by the Scale Advisor.
4. **Sending.** Separate sending domains and inboxes, warmed up before any campaign. The Codex never sends from Chris's main domain.
5. **Replies.** Interested replies are drafted into booking replies for Chris or the setter to send. Unsubscribes are honored at once.
6. **Weekly results** to the Dream Map.

## 2. Requirements

| # | Requirement | Must / should |
|---|---|---|
| 1 | Separate sending domains; main domain protected | Must |
| 2 | Unsubscribe in every email and honored at once; sender address in every email | Must |
| 3 | No paid lead or enrichment databases. The agent does the research | Must |
| 4 | Spend capped (domains, inboxes, sender tool), with every purchase approved by Chris | Must |
| 5 | No sends before Chris approves the copy and the list | Must |
| 6 | One personal line per lead, from real research | Should |

## 5. INPUT NEEDED

- Which offer.
- The ideal customer.
- The budget cap.
- Who answers booked replies.

## 6. Acceptance

- [ ] Domains warmed and the deliverability check passing before the first send.
- [ ] Four weeks of results in the sheet, and Chris's call: scale or stop.

## 7. Build order

1. Offer and ideal customer.
2. 50-lead research sample, approved by Chris.
3. Domains and warm-up.
4. Copy.
5. First 500.
6. Results.

## 8. Out of scope

Cold calling (see `projects/voice-caller-tests`). Buying lists.
