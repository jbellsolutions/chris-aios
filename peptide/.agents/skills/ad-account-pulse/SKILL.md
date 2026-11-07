---
name: ad-account-pulse
description: Use for the Media Buyer's daily ad pulse (spend to booked calls to cash, per campaign), scale/hold/cut calls on Chris's rules, creative-fatigue flags, the Monday creative brief and launch checklists for the peptide offer. Read-only unless Chris approves an exact change list.
---

# Ad account pulse

Work only in `~/chris-peptide`.

## When to use

The 8:00 AM pulse, the Monday creative brief, or "how are the ads doing", "what should I scale", "new angles".

## Inputs and access

- **Ad accounts:** `context/ad-accounts.md` (platform, account name, how it's connected). Read through a connected app or the browser. Read only.
- **The Peptide Operator's numbers:** yesterday's booked calls, shows, closes and cash by source, in `daily/`.
- **Chris's rules:** `context/ad-rules.md`: target cost per booked call, target cash per ad dollar, the daily spend cap, minimum spend before judging, scale step (for example +20% a day) and cut rule. If it's missing, report numbers only and say "no rules set". Write it only in Chris's words.

## Daily pulse

1. For each campaign and ad set, yesterday and the last 7 days: spend, impressions, CPM, CTR, CPC, leads, cost per lead, booked calls, cost per booked call. Add shows, closes, cost per client and cash per ad dollar where the Peptide Operator can attribute them.
2. Judge each ad set against the rules:
   - **SCALE** if under target with enough spend;
   - **CUT** if over the cut line with enough spend;
   - **HOLD** otherwise.

   Show the numbers behind each call.
3. **Fatigue:** frequency rising, CTR down 20% over 3 days, or CPM up while CTR falls.
4. Save to `vault/Ads/Pulse.md` and `daily/<date>/ads.md`. Message Chris only when there's a SCALE, CUT or FATIGUE line or a flag:

```
Ads — Tue (Meta; Google UNKNOWN: not connected)
1. SCALE "Founder story": cost/booked call 30% under target, 3 days → +20%
2. CUT "Lab hook": 2.1x target, 4 days
FATIGUE "Testimonial 2": frequency up, CTR down 3 days → new brief Monday
Reply "do it" for 1 and 2 exactly as written, or "do 1".
```

## Approved changes

When Chris says "do it" or "do 1": make exactly those changes, nothing else. Log before and after in `vault/Ads/Changes.md` and confirm from the platform's change history. If a change fails halfway, stop and report what changed and what didn't.

## Monday creative brief

- Ten hooks and angles from real objections and winning lines on the offer's calls, the Scale Advisor's latest memo and the ads winning now.
- Three full concepts: hook, body, call to action, and a visual or a script with a shot list.
- **Policy check for each concept**, against the platform's rules for this product category and the "Claims we never make" list in `OFFER.md`: no health, medical, efficacy, before/after or income claims, and no restricted wording. Name the rule that applies.

Save to `vault/Ads/Briefs/<week>.md` and as a new Google Doc.

## Launch checklist (draft)

Audience, budget, tracking (pixel or conversion events, UTMs), naming, the creative policy check, and the landing page matching the ad.

## Validate before sending

- An account you couldn't read is UNKNOWN, never 0.
- Every SCALE or CUT shows its numbers.

## Return

The pulse (and a message only if needed), or the brief's link and top three hooks.

## Needs Chris's yes

Every budget, bid, audience, ad or campaign change, any publish, and any spend or payment method. With a yes, change only the exact list.
