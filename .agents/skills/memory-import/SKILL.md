---
name: memory-import
description: Use during setup, or whenever Chris asks, to bring what his ChatGPT already knows about him onto this workspace, so the bots start out knowing him. Chris runs one prompt in ChatGPT and pastes or uploads the answer; it's scrubbed and saved to context/about-me.md.
---

# Memory import

Chris has used ChatGPT for everything for years. It already knows his style and his businesses. This skill moves what's useful onto this account, without passwords or other people's private details, and only the part that belongs on this account.

## When to use

Setup, right after the intake questions, or "import what ChatGPT knows", "update my profile".

## Which file

| Account | Saved to | Prompt |
|---|---|---|
| Business | `context/about-me.md` | Business |
| Peptide | `peptide/context/about-me.md` | Peptide |

## Steps

1. Tell Chris: "Open ChatGPT, start a new chat, paste this, and send me the answer here (paste it or upload the file)." Give him only your account's prompt.

**Business**
```
Write a profile of me for my business AI team. Use everything you remember about me. Sections: my businesses and my role in each; my team and how I manage them; my standards and pet peeves; how I like reports (format, length, timing); the experts and frameworks I follow; my goals for the next 90 days and the next year; projects and AI ideas I've talked about. Leave out anything about my personal life, passwords, account numbers and anyone's private details. Plain bullet points.
```

**Peptide**
```
Write a brief on my peptide business build-out offer for my AI growth team. Use everything you remember. Sections: what the offer is and who buys it; how clients find us; the sales team and process; fulfilment steps; numbers I've mentioned; what's working and what isn't; my growth plans; the experts and frameworks I follow. Leave out passwords, account numbers, client names and anyone's private details. Plain bullet points.
```

2. **Scrub before saving.** Remove anything that looks like a password, key, card or account number, or another person's private details beyond a first name. Tell Chris what you removed, by type only.
3. Save the rest to this account's `about-me.md`, with today's date at the top.
4. Read it back in five lines: "Here's what I now know about you." Ask "Anything wrong?" and fix what he corrects.
5. Tell every bot on this account to read `about-me.md` before its next task, in its handoff message.

## Validate

- No secrets in the file.
- Where ChatGPT's answer conflicts with what Chris told you here, his words here win. Note the conflict in the file.
- Nothing from another account's prompt lands here: the offer stays on the peptide account, COG stays on business, and his personal life stays in `life/`.

## Return

The five-line read-back.

## Needs Chris's yes

Nothing beyond his pasting the answer. The file stays on this account and is never copied to another.
