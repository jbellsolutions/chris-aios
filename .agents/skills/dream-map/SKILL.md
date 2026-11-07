---
name: dream-map
description: Use to keep Chris's Dream Map - every business goal and AI idea he has mentioned, in his words, with who owns it and its status - and for the monthly Dream check-in that picks the next thing to build and builds it with him. Also use when Chris says "add this to the list", "what's next" or "what have we built".
---

# Dream Map

Chris keeps having ideas and asks for them to be added to the list. He also asked to learn to build one agent correctly, start to finish. The Dream Map holds every idea in one list per account. Each month Chief picks the next one and builds it with him, so the team keeps growing and Chris learns by doing.

## Which file

| Account | Dream Map | Kept by | Seeded from (if Chris attached it at setup) |
|---|---|---|---|
| Business | `context/dream-map.md` | Chief | `DREAM-MAP.md` |
| Peptide | `peptide/context/dream-map.md` | Peptide Operator | the dream rows in `GROWTH-CONTEXT.md` |

Use only your account's row. A dream that belongs on the other account gets one line to Chris: "That one lives on your <business / peptide> account. Tell <lead bot> there." A personal dream (his life, his money) isn't kept on Codex: "That one's for your ChatGPT project, My Life."

## When to use

- At setup, to seed the map from the attachment, or from his first answers if there's none.
- "Add this to the list", "I want an agent that…", "what's next?", "what have we built?"
- The monthly Dream check-in (business account, Chief).

## The file

```
# Dream Map
| # | Dream (his words) | Area | Owner | Status | Next step |
|---|---|---|---|---|---|
| 1 | "AI watches everything. Chris manages the exceptions." | COG | COG Sales Manager | live | — |
| 2 | Media buyer that runs and updates ads | Growth | Media Buyer | built | Chris sets ad rules |
| 3 | AI voice caller, small tests | Outbound | — | spec'd | projects/voice-caller-tests |
```

Status is one of **idea**, **spec'd**, **built**, **live** or **parked**. `projects/` in this repo holds a spec for each dream that needs more than a skill.

## Adding a dream

Write it in Chris's words. Set the area, and the owner if a bot already covers it. Reply in one line: "Added #14. <Owner> can do it now" or "Added #14 as an idea. Want it next month?"

## Monthly Dream check-in (Chief)

1. **Wins:** what moved to live this month, one line each.
2. **Stuck:** anything built but not live, and the one thing it's waiting on from Chris.
3. **Next:** one dream to build this month, the most value for the least setup, with a one-line reason. Ask whether anything on his peptide list should go first; the Peptide Operator builds it.
4. On his yes, build it with him using the `agent-builder-loop` skill. Ask whether he wants to do each step or watch, and explain each step in one plain sentence first.
5. Update the map.

The Peptide Operator answers "what's next?" the same way when Chris asks, and builds with him by following `docs/BUILD-YOUR-NEXT-AGENT.md` in its own copy of the repo.

## Validate

- Every dream keeps his original words.
- Nothing is marked live unless its routine is on in that account's `state/automations.md` and has run cleanly.

## Return

The one-line confirmation, or the check-in message under 150 words.

## Needs Chris's yes

Creating a bot, turning on a routine, connecting a new app, and any spend.
