---
name: slack-api
description: Use to read Slack for the business side (the KPI channel, Chris's DMs and mentions), to find a channel's or a rep's ID, or to check that the Slack token works. Reading only. The one post in this whole workspace is the EOD bump, and only tools/eod_check.py sends it.
---

# Slack, read-only

| Job | Use |
|---|---|
| Chris's DMs, mentions and search, for his brief | The Slack app in Codex (ChatGPT apps), signed in as Chris |
| The KPI channel at night, unattended | `tools/eod_check.py` with `SLACK_BOT_TOKEN` (the COG Sales Manager Slack app, `docs/SLACK-SETUP.md`) |
| Find the KPI channel's ID or a rep's member ID, or test the token | The calls below with `SLACK_BOT_TOKEN` |

**You never post.** No message, DM, thread reply, edit or reaction, with the token or with the Slack app. If Chris wants something said in Slack, draft it in `queue/drafts/chief/` and he sends it. The EOD bump goes only through `tools/eod_check.py` (the `cog-eod-compliance` skill).

## The token

`SLACK_BOT_TOKEN` lives in `~/chris-aios/.env.local`. Chris puts it there by running `tools/add_secret.sh SLACK_BOT_TOKEN` in Terminal, which hides what he pastes and keeps every other key in the file. Load it for a call without printing it:

```bash
set -a; . ./.env.local; set +a
```

Never print, echo or log it, and never ask for it in chat. If it's missing, say so, log `UNKNOWN: Slack bot token`, and put "run `tools/add_secret.sh SLACK_BOT_TOKEN`" on `queue/needs-chris.md`.

## Calls (read-only)

`curl -s -H "Authorization: Bearer $SLACK_BOT_TOKEN" "https://slack.com/api/<method>?…"`. **Check `"ok": true`** in every response.

| What | Method |
|---|---|
| Check the token | `auth.test` (the bot's `user_id` and the workspace `url`) |
| A channel's ID | `conversations.list?types=public_channel,private_channel&limit=1000` (follow `response_metadata.next_cursor`) |
| A rep's member ID | `users.list?limit=1000`, matched by real name or email |
| Read a channel | `conversations.history?channel=C…&oldest=<unix>&latest=<unix>&limit=200` |

## Errors

| Error | Meaning | Do |
|---|---|---|
| `not_in_channel` / `channel_not_found` | The bot isn't in that channel | Chris types `/invite @COG Sales Manager` in the KPI channel |
| `missing_scope` | The app lacks a scope | Chris adds it and reinstalls (`docs/SLACK-SETUP.md`) |
| `invalid_auth`, `token_revoked` | Token dead | Chris reinstalls and runs `tools/add_secret.sh SLACK_BOT_TOKEN` again |
| `ratelimited` | Too fast | Wait the `Retry-After` seconds once, then continue |
