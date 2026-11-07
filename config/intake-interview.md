# Intake interview: filling `context/cog.json`

**For Chief (run from `START-HERE.md` Step 2):**
- Ask Chris **one question at a time**, in plain English, and fill `context/cog.json` as you go. The schema is `config/cog.example.json`.
- Look up every ID yourself through the connected apps where possible. Only ask Chris to confirm. Slack, Sheets and GoHighLevel are connected after the intake (`START-HERE.md` Steps 5 and 6), so what you can't see yet stays `REQUIRED`; fill it in then and have Chris confirm it.
- If he doesn't know an answer, keep the default and note it in `vault/decisions/` as "assumed, confirm later".
- Never ask for a password, token or key here.

## A. The team (→ `roster`)

1. "Who's on the sales team right now? For each person: closer or setter?"
2. For each person, look up and confirm:
   - their Slack member ID (Slack → profile → ⋯ → Copy member ID)
   - their GHL user ID
   - their calendar
3. "Is anyone exempt from EODs, or new this week?" → `eod_required`, `active_since`.

## B. EODs (→ `eod`)

4. "When a closer submits their EOD, where does it go? A Google Form into a Sheet, a Slack workflow, a GHL form, something else?" → `source_type`. For a Sheet, get the spreadsheet and the tab.
5. Open one real submission together. Map each question or column to the standard fields in `docs/KPI-DEFINITIONS.md` → `field_map`. Note which column identifies the rep and which is the timestamp.
6. "Which Slack channel is the KPI channel, and is it in WeScale or in COG's own Slack?" → `slack_channel_id`, `slack_workspace`. Chris has to be signed in to that workspace in the ChatGPT apps in Codex so the bot can read it (`START-HERE.md` Step 5). If it's COG's own workspace, the team's posting app needs that workspace's admin to approve it (`docs/SLACK-SETUP.md`).
7. "11:30 PM ET is the first check. When's the real cutoff?" (Default: final check 12:45 AM, cutoff 1:00 AM ET.)
8. "Do setters submit EODs too?"

## C. Bumps (→ `bump`)

9. The bump comes from the COG Sales Manager Slack app, so reps see "COG Sales Manager". It needs the app in the KPI channel's workspace and a bot token, which Chris pastes once in Terminal with `tools/add_secret.sh SLACK_BOT_TOKEN` (`docs/SLACK-SETUP.md`). Without the app, the bump stays a draft he pastes himself.
   Explain the tradeoff. Tell him the bump goes live at milestone M4, after five good preview nights, and not before.
10. Show him the two bump templates. "Want any wording changed?" Keep them factual, with no insults.

## D. GoHighLevel (→ `ghl`)

11. Location ID; which calendars are sales calls → `calendars`.
12. "When a call is over, where does the closer set the outcome? A custom field, an opportunity stage, a tag?" → `dispositions.field`. Read the exact list of allowed values → `dispositions.allowed`.
13. Map GHL appointment statuses to showed / no-show / cancelled / rescheduled → `appointment_status_map`.

## E. No-show SOP (→ `no_show_sop`)

14. "When someone no-shows, what exactly should the closer do, and how fast?" The default from your brief: call twice, text, notify the setter, update GHL, within 10 minutes. Confirm the steps and minutes.
15. "How fast should a no-show be contacted?" → `thresholds.lead_response_minutes`.

## F. Numbers (→ `targets`, `thresholds`)

16. "Do you have daily or weekly targets: cash, closes, live calls, show %, close %?" Leave them null if none. The report then compares to last week.
17. "How big a gap between what a closer reports and what GHL shows should get flagged?" (Default: 1 live call.)

## G. Calls, assets and knowledge (→ `calls`, `knowledge`)

18. "Where do call recordings and transcripts live? GHL, Zoom, read.ai, Fathom?"
19. "Where are your current SOPs and scripts?" → `knowledge.sops_folder`.
20. "What's the link to the Jeremy Haynes knowledge base we built on Oct 16?" (The repo or here.now page; it was published from your side.) → `knowledge.jeremy_haynes_kb_url`.
21. "Where are your case studies, testimonials and videos? Which are you allowed to share with prospects?" → `knowledge.content_library_folder`.

## H. You (→ `owner`, `owner.md`, `priority-people.md`)

22. Your Slack member ID → `owner.slack_member_id`. "Reports and the morning brief come to you in each bot's chat in the Codex app. Anything you'd change?" → `owner.report_channel`.
23. "The team runs on Eastern. You chose Eastern Daylight on Oct 16, right?" Check that Codex's time zone setting is Eastern (`START-HERE.md` Step 2). Routines run in the cloud on it.
24. "Which businesses should the team know about? Names only." → `owner.md`.
25. "How do you like messages: short, numbered, numbers first? Anything you hate? When are you off, and which hours are protected?" → `owner.md`.
26. "Who are your priority people: the ones whose messages need you fast?" → `priority-people.md`. Look up their Slack and email handles yourself.

## I. Personal (not on Codex)

27. Don't ask this. His personal life and money run in `~/chris-life`. If he brings it up, point him there.

When done:
- Check that `context/cog.json` is valid JSON, that every field marked `REQUIRED` is filled, and that nothing still says `REQUIRED` or `EXAMPLE`. Anything left goes on a short list for `START-HERE.md` Step 5.
- Read the roster back to Chris in one message and get his "right". Then read the summary back in 5 lines.
