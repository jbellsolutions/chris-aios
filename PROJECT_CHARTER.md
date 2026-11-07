# Project charter: Chris's AIOS (Codex)

## 1. Why this project exists

Chris runs the Circle of Greatness (COG) sales team, WeScale Marketing, and a done-for-you peptide business build-out, and he manages 10–15 reps by hand. He wants **"AI watches everything. Chris manages the exceptions."** (Slack, Oct 15), and he wants it done for him: "90% done for you and 10% done with me" (Slack, Nov 6). This AIOS runs in Codex on his Mac, which he already pays for, so there's no new platform to learn.

## 2. Objectives (what "done" means)

1. Every night, the EOD check knows who submitted, who's late and who's missing, and bumps only the missing reps, with Chris's exact approved wording.
2. Every morning, one brief: his day, the emails that need him, last night's EOD result and the COG numbers, with what needs him first.
3. His personal life (weekends, dates, money, special dates) runs in its own folder that business never sees.
4. The peptide business has a backend: every client delivered the same way, with guardrails on everything a buyer sees.
5. Nothing outward without his yes, except the one standing approval he gives himself.

## 3. Scope

In: the business Chief of Staff and COG team, the life side, the peptide area, the four install-time automations, and the build-your-next-agent loop. Later milestones: GHL audits, call QC, pre-call sequences, the WeScale Operator. Out: anything that pays, signs, orders, or changes GHL records.

## 4. The team and who owns what

One owner per job, per record and per outward action.

| # | Agent | Folder | Owns | Sole writer of | Milestone |
|---|---|---|---|---|---|
| 01 | **Chief of Staff** | business | Chris's attention, the morning brief, routing, the inbox and calendar (drafts only), the Dream Map, building new agents | `queue/`, `vault/decisions/`, `context/dream-map.md`, email drafts | M1 |
| 02 | **COG Sales Manager** | business | EOD compliance, the morning report, calendar, no-show and disposition audits, rep scorecards, the weekly review | The EOD bump (through `tools/eod_check.py` only), `data/eod/`, `vault/reps/` | M1 |
| 03 | **Pre-Call Concierge** | business | Closer briefs and pre-call sequences for booked COG calls (drafts) | `vault/prospects/` | M8 |
| 04 | **Growth Operator** | business | Scripts, SOPs, objection docs and ad hooks built from calls (drafts) | `vault/assets/` | M8 |
| 06 | **Sales Coach** | business | Call scorecards and rep coaching, from recordings, on Chris's rubric | `vault/coaching/` | M9 |
| — | **Life chief of staff** | `life/` | Weekends, dates, money (read-only), special dates | `life/` | M5 |
| 09 | **Peptide Operator** | `peptide/` | The offer's numbers, client delivery trackers, the blind-spot check, compliance checks | `peptide/vault/` | M6 |
| 10 | **Media Buyer** | `peptide/` | Scale, hold or cut on Chris's rules (recommendations only) | `peptide/vault/ads/` | M6 |
| 11 | **Scale Advisor** | `peptide/` | Cited answers from the expert libraries ("Jeremy AI") | `peptide/vault/advisor/` | M6 |

Numbers 05, 07 and 08 are unused. Charters: `agents/` and `peptide/agents/`.

## 5. How it runs in Codex

- Chris opens `~/chris-aios` in Codex (or `life/`, or `peptide/`) and talks. `AGENTS.md` makes that chat the Chief of Staff; it starts specialists as sub-agents.
- Skills live in `.agents/skills/` (and `life/.agents/skills/`, `peptide/.agents/skills/`), which Codex loads for that folder.
- Scheduled jobs are Codex automations, created paused at install from `automations/`. They run on his Mac, so the Mac must be awake with the ChatGPT app open (the platform's limit, closed at M3b if needed).
- Memory is the Obsidian vault in `vault/` (and `life/vault/`).
- The one outward action that runs by itself, the EOD bump, goes through `tools/eod_check.py`, which enforces its guards in code and has tests.

## 10. Milestones and dependencies

No dates. A milestone is done when its proof passes.

| Milestone | Depends on | Proof it's done |
|---|---|---|
| **M0 Installed** | Chris pastes `INSTALL-PROMPT.md` in Codex | The chat answers as the Chief of Staff, tests pass, `context/cog.json` exists |
| **M1 Connected, read-only** | M0; Slack (app token or the Codex Slack app), Gmail, Google Calendar | The replay of last night's EOD check prints a real table Chris says is right; the brief reads his real calendar |
| **M2 GHL read-only** | A read-only GHL private integration token | One real appointment read back; the no-show and disposition audits run in preview |
| **M3 Preview week** | M1 | Five nights in a row the EOD checks and the morning report reach Chris only, and he marks them right |
| **M3b Always-on nights** (only if needed) | M3; the Mac is often asleep at 11:30 PM | The nightly check runs on an always-on computer instead (an Orgo box), same tool, same guards |
| **M4 Live accountability** | M3; Chris's standing approval with the exact wording; the Hermes COG bot paused | The bump posts by itself; only one bot bumps |
| **M5 Life side** | Chris opens `life/` once | His Thursday weekend plan arrives; one money check from a real export |
| **M6 Peptide team** | The numbers in `peptide/OFFER.md`; read access to its CRM, payments and ads; the lawyer's review | The morning pulse arrives with every number sourced or UNKNOWN; one client tracked end to end |
| **M7 Real-time no-shows** | M2, M4; a GHL webhook | A test no-show alerts Chris within the SOP window |
| **M8 Pre-Call and Growth live** | M3; the Jeremy Haynes library link | One pre-call sequence and one asset drafted from real data and approved |
| **M9 Call QC live** | M3; where call recordings live; Chris's call standard | A week of calls scored; Chris agrees with five spot-checked scorecards |
| **M10 Chris builds an agent** | M4 | Guided by the Chief of Staff, Chris builds his own next agent (the WeScale Operator, or the dream he picks) |

## 13. Decisions

| # | Decision | By | Why |
|---|---|---|---|
| 1 | Codex on his Mac, not Grok Bot or Hermes | Justin, Nov 7 | He already pays for ChatGPT with Codex; nothing new to learn or log into |
| 2 | Life and peptide in their own folders with their own rules | Justin, Nov 7 | Business never sees his personal life; peptide keeps its own logins |
| 3 | The EOD bump is enforced in code, not only in prose | Build, Nov 7 | It's the one thing that posts by itself |
