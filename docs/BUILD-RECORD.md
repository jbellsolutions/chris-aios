# Build record

## 2026-11-07: the Codex edition

**Why:** Chris asked for it "90% done for you": less building, more results. He already pays for ChatGPT with Codex. Justin asked for an AIOS in Codex for his business and personal life, with an install Chris barely touches.

**What was built:**
- Ported from the GrokBot edition (`wescale-grokbot-team`, same charters and skills): the Chief, the COG Sales Manager and its seven skills, the Pre-Call Concierge, the Growth Operator, the Sales Coach, the peptide trio, the KPI definitions, the Slack app manifest and the intake. Paths moved from `/workspace/cog-team/` to this workspace; Grok Bot's routines became Codex automations; the approval rules became the code and rules described in `policies/APPROVALS.md`.
- New for Codex: `AGENTS.md` as the router, `START-HERE.md` (eleven steps, five questions), `INSTALL-PROMPT.md` (two pastes), the four install-time automations, `tools/eod_check.py` with its tests, the life side (from the ChatGPT "My Life" setup; copied to `~/chris-life` at setup) and the peptide area (offer, delivery, compliance; copied to `~/chris-peptide`).

**Choices made where it was unclear:**
- The nightly EOD check is code, not a prompt, because it's the one action that posts by itself.
- Life and peptide are copied to their own folders outside this workspace, so business chats can't read or load them.
- The peptide numbers stay "Chris to fill in" or UNKNOWN; partnership terms are not in the package.
- Lead Radar (from the AIOS template) is left out; Chris didn't ask for lead finding.

**Not verified yet:**
- Not yet run on Chris's Mac or his real KPI channel.
- The EOD source type (Slack workflow, sheet or GHL form) is unknown; the tool reads Slack only.
- GHL audits, call QC and pre-call need M2, M8 and M9.
- Codex automations need the Mac awake at 11:30 PM.
