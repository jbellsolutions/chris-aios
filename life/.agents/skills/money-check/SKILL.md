---
name: money-check
description: Read-only view of Chris's personal money from the exports he drops in money/. Use when he asks how much he spent, where it went, how much free cash he has, what's due, or whether he's on track.
---

# Money check (read-only)

1. Read every CSV or statement in `money/` (Amex first, then the other cards and banks he named in `me.md`). Note each file's date range.
2. Work out, for the period he asked about (default: this month so far):
   - spending by category, and the top five merchants
   - income in
   - each card's balance as of its export date
   - subscriptions and recurring charges, flagging anything new, doubled or unusual
   - bills due in the next 14 days
   - **free cash** = checking + savings − bills due in 14 days
   - progress on the goals in `me.md`
3. An account with no export is **UNKNOWN**, never $0; list it at the bottom with "drop a fresh export to include it".
4. Under 150 words, the answer to his question first. Save the numbers to `vault/money/<YYYY-MM>.md`.

Never move money, pay anything, log in to a bank, or recommend specific investments. Never repeat a card or account number; show the last four digits at most.
