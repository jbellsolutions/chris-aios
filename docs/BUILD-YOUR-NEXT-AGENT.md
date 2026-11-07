# Build your next agent: the loop, start to finish

Chris's ask: teach him to build one agent correctly, start to finish, instead of only building for him: idea → architecture → build → integrations → data → prompts and instructions → automations → testing → deployment.

This page is that loop, for Codex. **The COG Sales Manager is the worked example** at each step. Your first build is your own: the WeScale Operator (`projects/wescale-operator/SPEC.md`), or whichever dream from your Dream Map you pick at the monthly check-in. Do the same ten steps. Chief runs it with you (`.agents/skills/agent-builder-loop`), and you start it by telling Chief: "let's build my first agent together".

On Codex there is no separate build tool to open. Chief writes the files and creates the bot; you answer questions and do the few things only a person can do (sign-ins, secrets, Settings screens).

---

### 1. Idea: one sentence, then the recurring tasks

> "This agent ___ so that I don't have to ___."

*COG:* "Watches EODs, calendars and GHL so that I don't have to police 15 reps every night."

Then list the 3–5 tasks you actually repeat. Each one needs:
- a **trigger:** a time, or an event
- the **steps:** what you do today
- **done:** what you'd accept as finished

*COG:* the 11:30 PM EOD check; the morning numbers; no-show follow-up checks; disposition checks; the weekly scorecard.

### 2. Architecture: a new bot, or a skill?

| Same data, same owner, same approvals? | → a **skill** of an existing bot |
|---|---|
| Different data, different audience, different risk? | → a **new bot** |

*COG:* your seven jobs (KPI Monitor, Calendar Monitor, GHL Auditor…) all use the same data and report to you, so they're **seven skills of one bot**. Growth assets need different tools and approvals, so that's a separate bot. Jeremy Haynes material is knowledge, not a job, so it's a skill.

Then the **account**. Every bot on one workspace shares one computer: its files, its browser sessions and its logins. If the new bot's data or logins must stay apart from COG's, it needs its own workspace folder (and its own plan). *COG:* the peptide offer is on its own account for exactly this reason, and your life and money aren't on Codex at all (they're in ChatGPT).

### 3. Charter: the agent's job description

Chief writes a new file `agents/NN-name.md` from the template in `.agents/skills/new-agent-onboarding/SKILL.md`. The parts that matter most:
- **Owns / does not own:** stops two bots fighting over the same thing.
- **Approvals:** what it may do alone, what asks first, what never happens.
- **Done looks like:** how you'll know it's working.
- **Profile:** the standing role the bot saves to memory word for word. It says the job, what it may do alone, what needs approval and the never-list.
- **Memory seed:** the facts the bot must always remember.

*COG:* `agents/02-cog-sales-manager.md`. A charter holds your facts, so it stays on the bot computer. It is never pushed to the public GitHub repo.

### 4. Create the bot

In Codex, start a new chat in `~/chris-aios`: "You are <Bot name>. Read `agents/NN-name.md` and follow it." Then Chief sends it the setup message from `START-HERE.md` Step 7, with the new charter file filled in. The bot saves its Profile and replies "ready".

If Chief can't create it, Chief tells you exactly what to click and gives you the message to paste as the bot's first message.

*COG:* the COG Sales Manager was created exactly this way in `START-HERE.md` Step 7.

### 5. Skills: one per recurring task

Each recurring task becomes a `SKILL.md` with:
- when to use it
- the steps
- the exact output format
- a **Never** list

Write it so a new hire could follow it. Two rules always go in:
- **Unknown is not zero.** A source it can't read is "unknown".
- **Every claim names its source.**

Chief saves each one as `.agents/skills/<name>/SKILL.md` in this workspace, where Codex loads it. Paths inside it are relative to `~/chris-aios`.

*COG:* `.agents/skills/cog-eod-compliance/SKILL.md`.

### 6. Apps: connect read-only first

List every app the agent needs. In **the ChatGPT apps in Codex**, search, choose **Add** and sign in. Connect each at **read** first, and prove it by having the bot quote one real record.

*COG:* Slack (KPI channel history), Sheets (EOD form), Calendar, GoHighLevel. The Oct 16 Slack problem, no channel history, would have been caught right here.

### 7. Data: the facts it depends on

Write down every ID, field name and threshold the agent needs, in a config file in `context/`. **If something's missing, the agent must stop and say `NO_CLIENT_SOURCE`, not guess.**

*COG:* `context/cog.json`: roster, EOD field map, KPI channel, cutoffs, dispositions, no-show SOP, targets.

### 8. Routines: created paused

Turn each trigger into a routine and **create it paused**. Chief writes one prompt file per automation in `automations/`, copied from an existing one, so it keeps the same header and the same switch check, test mode, isolation guard, lean run and run-log lines. The bot that owns the job creates the routine, because a routine belongs to the bot that creates it: ask it, in plain words, with the time in Eastern. Every routine goes in `context/team-registry.md` as PAUSED.

*COG:* five routines for the COG Sales Manager: the 11:30 PM and 12:45 AM EOD checks, the 8:00 AM report, the no-show sweep (four times a day) and the Monday review.

**When a tool can't do what you need, name it as the tool's limit, not your design.** Codex caps a bot at 50 routines, wants schedules at least 5 minutes apart, and may pause routines after a long absence. *COG:* a routine can't fire "within 5 minutes of a no-show", so sweeps cover it for now and a GoHighLevel webhook comes later. The requirement didn't shrink.

### 9. Test, then your yes

1. List the routine in `state/automations.md` as `<name>: test`.
2. Ask the agent to run the automation's prompt once now. In test mode every message goes to you only and starts with "TEST", and nothing is sent anywhere else.
3. Mark each output right or wrong. Fix the config and skills until two runs in a row are right.
4. Tell Chief your yes in your own words. Chief marks the routine `on` in `state/automations.md`, the bot resumes it (un-pause it in Codex's automations), the registry says ON, and the decision goes in `vault/decisions/`.
5. Anything that writes (a post, an email, a record change) is allowed only where the charter says so, and the approval rules in `policies/APPROVALS.md` still apply.

*COG:* five preview nights, then the one standing approval for the EOD bump.

### 10. Keep the registry true

Chief keeps `context/team-registry.md` current: the bot, its routines, its connections and the names of its secrets. Every morning the brief lists any routine that was due and didn't log a run, so a silent pause is caught the next day.

---

**You've done it once when:** your first agent exists, its routines are on, it passed its test, and you did steps 1–3 and 5–9 yourself. That's milestone M10.
