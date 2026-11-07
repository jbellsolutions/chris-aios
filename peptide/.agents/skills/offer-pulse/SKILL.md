---
name: offer-pulse
description: Use for the Peptide Operator's morning pulse (the funnel from ad to cash against target), the bottleneck of the week, client fulfilment tracking and the Friday blind-spot check for Chris's peptide offer.
---

# Offer pulse

Work only in `~/chris-peptide`. Never read COG data.

## When to use

The 8:30 AM pulse, the Friday blind-spot check, or "how's the offer doing", "where's it leaking", "which clients are behind".

## Inputs and access

- **`OFFER.md`:** what's sold, the fulfilment steps, the targets (booked calls a day, show rate, close rate, monthly cash, cash per ad dollar), where each number lives, and the claims never made. If it's missing, reply `NO_CLIENT_SOURCE: offer facts` and stop. If the targets are missing, report numbers without judging them and ask Chris for targets once.
- **Where the numbers live** (a section of `offer.md`): the CRM for leads, appointments and outcomes; payments for cash, refunds and chargebacks; the setter's and closer's EOD sheet or channel; the client tracker.
- **The Media Buyer's pulse** for spend: `daily/<date>/ads.md`.
- **Clients:** `vault/Clients/<first name>.md`, one per client: start date, current step, the step's due date.

## Morning pulse

1. Yesterday and the 7-day average, each against target:
   - leads, calls booked, shows, closes;
   - cash collected, refunds;
   - ad spend, cost per booked call, cost per client, cash per ad dollar.
2. Stage conversion: lead to booked, booked to show, show to close.
3. **Bottleneck:** the stage furthest below target over 7 days, with the evidence. Hand it off with a request in `queue/jobs/<bot>/`:
   - ads to the Media Buyer;
   - offer, show rate or scripts to the Scale Advisor;
   - the sales team's behaviour to Chris.
4. **Fulfilment:** each client's step. Flag any step more than 2 days overdue.
5. Send one screen, under 120 words, ending with one action. Save it to `daily/<date>/pulse.md`.

## Friday blind-spot check

What's true this week that nobody's looking at?
- refunds and chargebacks trend;
- one ad or channel carrying too much;
- a lead source going stale;
- a slipping fulfilment step;
- cash collected against closes reported;
- gaps in the setter's or closer's EODs.

Name the top two, each with evidence and a first step. Log them in `vault/Offer/Blind-spots.md`.

## Validate before sending

- A source that can't be read is UNKNOWN, never 0.
- Cash comes from the payment source, not from what reps report. Show both if they differ.

## Return

The pulse or the blind-spot message.

## Needs Chris's yes

Any change to ads, the CRM, prices or client-facing material, and any message to a client, prospect or team member.
