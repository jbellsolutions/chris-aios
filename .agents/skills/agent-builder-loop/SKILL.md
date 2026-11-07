---
name: agent-builder-loop
description: Teach and run the full build loop for a new Codex agent - idea, architecture, charter, create the bot, skills, apps, data, routines, test, go-live - doing it with Chris step by step so he can replicate it. Use when Chris asks to build an agent, learn how agents are built, or add a capability.
---

# The agent-builder loop (Chris's "ONE thing")

Chris asked to understand the whole chain, from the idea to a running agent: **Idea → architecture → build → integrations → data → prompts/instructions → automations → testing → deployment.** On Codex, Chief does the typing. Chris answers questions and does the Owner steps (sign-ins, secrets, the Settings screens).

Walk him through it one step at a time:
- Show the result of each step before moving on.
- Ask whether he wants to do the step himself or watch.
- Explain each step in one plain sentence first.
- The long version is `docs/BUILD-YOUR-NEXT-AGENT.md`.

| # | Step | What you produce with Chris | Check before moving on |
|---|---|---|---|
| 1 | **Idea** | One sentence: "This agent ___ so that Chris doesn't have to ___." Plus the 3–5 recurring tasks (intake in `new-agent-onboarding`; for a dream that already has a spec, start from `projects/<name>/SPEC.md`, for example the WeScale Operator) | Each task has a trigger, the steps and what "done" looks like |
| 2 | **Architecture** | New bot, or a skill of an existing one? (Same data, same owner, same approvals → a skill. Different data, approvals or audience → a bot.) Then which workspace: every bot on one account shares one computer, its files and its logins, so a bot whose data or logins must stay apart needs its own workspace folder | Chris agrees with the call |
| 3 | **Charter** | A new file `agents/NN-name.md` (the next free number) from the template in `new-agent-onboarding`, with a **Profile** block and a **Memory seed** | Has owns / does not / approvals / never. The Profile says what needs approval |
| 4 | **Create the bot** | a new Codex chat in `~/chris-aios`: "You are <Bot name>. Read `agents/NN-name.md` and follow it." Then send it the setup message from `START-HERE.md` Step 7 with its charter file filled in | It replies "ready" and has saved its Profile |
| 5 | **Skills** | One `SKILL.md` per recurring task (steps, output format, never-list, paths relative to ~/chris-aios), saved as `.agents/skills/<name>/SKILL.md` in this workspace, where Codex loads it | A teammate could follow each one without asking |
| 6 | **Apps** | **the ChatGPT apps in Codex** (sidebar) → search → Add, **read-only first**. Anything it needs to write comes later, from the charter | The bot quotes one real record from each app |
| 7 | **Data** | Its config in `context/`: the IDs, field maps and thresholds it depends on. Missing ones → `NO_CLIENT_SOURCE` | No REQUIRED placeholders left |
| 8 | **Routines** | One prompt file per automation in `automations/`, copied from an existing one. The owning bot creates each in Codex **paused** (a routine belongs to the bot that creates it), in Eastern Time | Each is in `context/team-registry.md` as PAUSED, with its owner and WHEN |
| 9 | **Test** | Add `<routine name>: test` to `state/automations.md`, ask the agent to run it once now, and mark the output right or wrong. In test mode every message goes to Chris only | Two clean runs in a row, one run-log line each |
| 10 | **Chris's yes, then the registry** | His yes in his own words → `<routine name>: on` in `state/automations.md`, Chief un-pauses the Codex automation for the routine, registry rows updated, decision written to `vault/decisions/` | Chris's words are in `Decisions.md` and the registry says ON |

**Name the tool's limit as the tool's limit.** Codex caps a bot at 50 routines, wants schedules at least 5 minutes apart, and may pause routines after a long absence. Routines run on a schedule or an event, so "within minutes of an appointment" needs a webhook, not a sweep. If a limit blocks what the agent needs, say so and propose another tool. Don't shrink the requirement.

**Who does what:** you (Chief) write the charter, skills, config and routine files, and you create the bot. Chris signs in to apps, fills secrets in Terminal with `tools/add_secret.sh`, and adds approval rules (`policies/APPROVALS.md`). If you can't create the bot yourself, give him the **Owner step** wording from `START-HERE.md` Step 7.

End every session with: what was built, what's still paused, and the next step.
