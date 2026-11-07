# Approvals: what may happen without asking Chris

**The default:** every outward action is a draft that waits for Chris's yes in the chat: a Slack post, a DM, an email, a text, a GHL change, a calendar invite, a booking, a payment, an ad change. "Yes" counts only for that one action.

**A standing approval** lets one exact action run by itself, every time, with the exact wording. Chris gives it in the chat; the Chief of Staff copies the exact wording into `context/standing-approvals.md` with the date, and records the decision in `vault/decisions/`. Changing the wording cancels it.

| # | Standing approval | Offered when | How it's enforced |
|---|---|---|---|
| 1 | The EOD bump in the KPI channel: the first check (11:30 PM ET) and the final check (12:45 AM ET), with the two templates in `context/cog.json`, mentioning only reps who are missing | After five nights of drafts Chris marked right | In code: `tools/eod_check.py` posts only if `context/eod-mode.md` is `live`, the exact template is in `context/standing-approvals.md`, the run is on time, it hasn't posted this check yet, no other bot bumped tonight, and `state/STOP` doesn't exist. Its tests prove each guard |

Nothing else has a standing approval. Everything else is enforced by these rules in `AGENTS.md`, which every chat loads, and by Codex asking before it runs commands that reach outside this Mac.

**Stop everything:** Chris says "stop everything" and the Chief of Staff creates `state/STOP`. The EOD tool refuses to post while it exists, and every automation stops at its first line. Deleting the file (on Chris's yes) starts things again.
