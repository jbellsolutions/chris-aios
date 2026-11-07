# Slack setup

The team uses Slack two ways:

| | How | Used for |
|---|---|---|
| **Reading as Chris** | The Slack app in Codex (ChatGPT apps), signed in as Chris | Chris's DMs and mentions for the brief |
| **The team bot** | The "COG Sales Manager" Slack app's bot token, used only by `tools/eod_check.py` | Reading the KPI channel at night, and the EOD bump once Chris approves it. Nothing else |

The bump comes from the bot, so reps see "COG Sales Manager", not Chris, and the bot can only post where Chris invited it.

## Which workspace

Chris may be in two workspaces: WeScale and COG's own. The KPI channel is in one of them (`cog.json` → `eod.slack_workspace`).

| The KPI channel is in | Reading (connector, as Chris) | Posting the bump (bot) |
|---|---|---|
| **WeScale** | Chris signs in to WeScale in the ChatGPT apps in Codex | Reuse the "COG Sales Manager" Slack app installed in WeScale on Oct 16 (below) |
| **COG's own workspace** | Chris signs in to COG's workspace in the ChatGPT apps in Codex | Install the app from `slack-app-manifest.json` in COG's workspace. Its admin approves the install |

If the connector holds only one workspace at a time, connect the KPI channel's workspace. Say in the first brief that DMs in the other one aren't scanned yet.

Ask COG's admin before installing. A pending install is the most common reason the bot "can't see" a channel.

**Read only what's needed.** The COG Sales Manager reads the KPI channel and the team channels listed in `cog.json`. Chief reads Chris's DMs and mentions.

## Option 1: reuse the app installed in WeScale on Oct 16

Use this when the KPI channel is in WeScale. **Replace its token with a fresh one.** That also cuts the old Hermes COG bot off, so only one bot can ever bump.

1. Go to https://api.slack.com/apps and open **COG Sales Manager**.
2. **OAuth & Permissions** → **Bot Token Scopes**. It needs exactly: `chat:write`, `channels:history`, `groups:history`, `channels:read`, `groups:read` and `users:read`. Add any that are missing. Remove nothing without asking Chris.
3. **Reinstall to Workspace** after adding scopes. The Oct 16 problem, no channel history, was a missing history scope.
4. **Regenerate the token:** OAuth & Permissions → **Revoke** the current token (or uninstall and reinstall), then install again and copy the new **Bot User OAuth Token** (starts with `xoxb-`). Don't paste it into any chat.
5. Continue at "Invite the bot and give the token to the team".

## Option 2: create the app from the manifest

Use this when the KPI channel is in COG's own workspace, or when the Oct 16 app can't be reused.

1. Go to https://api.slack.com/apps → **Create New App** → **From a manifest** → pick the workspace the KPI channel is in.
2. Paste the contents of [`slack-app-manifest.json`](slack-app-manifest.json) → **Next** → **Create**.
3. **Install to Workspace** → **Allow**. If it says "request to install", that workspace's admin has to approve it.
4. **OAuth & Permissions** → copy the **Bot User OAuth Token** (starts with `xoxb-`). Don't paste it into any chat.

## Invite the bot and give the token to the team

1. In Slack, invite the bot to the KPI channel: `/invite @COG Sales Manager`. Private channels need this too.
2. Chris opens Terminal and runs `cd ~/chris-aios && tools/add_secret.sh SLACK_BOT_TOKEN`, then pastes the token there (it's hidden and saved to `.env.local`, mode 600).
3. **Check:** `auth.test` names the bot, and the replay of last night (`python3 tools/eod_check.py check --date <date>`) prints a real table. Nothing is posted.

## No admin rights?

Without the app, Codex reads the KPI channel through the Slack app in Codex, signed in as Chris, and the EOD check runs from that saved read (`cog-eod-compliance` skill). That path never posts: Chris gets the bump as a draft and pastes it himself.

## Scopes and why

| Scope | Why |
|---|---|
| `channels:history`, `groups:history` | Read the KPI channel (public or private), and check whether a bump already landed |
| `channels:read`, `groups:read` | Find the channel's ID by name |
| `chat:write` | Post the bump |
| `users:read` | Turn user IDs into names |

Not included on purpose: DMs, reactions, inviting people, managing channels, files, user groups, admin scopes.

## When something breaks

| Symptom | Fix |
|---|---|
| `not_in_channel` | `/invite @COG Sales Manager` in that channel |
| `missing_scope` | Add the scope under OAuth & Permissions → **Reinstall** (the token usually stays the same) |
| `invalid_auth` / `token_revoked` | Reinstall, copy the new token, paste it again in Terminal with `tools/add_secret.sh` |
| Install stuck on "pending" | The workspace admin hasn't approved it yet |
| A token was pasted into a chat | Regenerate it: **OAuth & Permissions** → **Revoke** (or reinstall), then paste the new one in Terminal with `tools/add_secret.sh` |
