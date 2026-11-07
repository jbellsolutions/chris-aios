# AI voice caller, small tests: project spec

**Owner:** Chris · **Builder:** Codex or Claude Code, with the GoHighLevel bots · **Runs on:** GoHighLevel Voice AI first · **Status:** draft

## 0. Charter

**What:** Two small, safe tests of an AI voice agent on real calls, measured against a human doing the same job.

**Why:** On Oct 6 Chris asked how good AI voice callers are now. He'd tried GHL's caller a long time ago, and he's up for small tests.

**Users:** Chris; leads who asked to be called.

**Done means:** 20 real calls per test, with booked-appointment rate and show rate compared with the human baseline, and a keep or kill decision from Chris.

**Decisions already made (Oct 6, Justin):**
- Voice AI is strong now for inbound reception and for calling people who expect the call.
- Cold outbound appointment setting isn't ready yet.
- Start with small tests.

## 1. How it works

**Test A: inbound receptionist.**
1. A lead calls the offer's number after hours or when the setter is busy.
2. The voice agent answers, qualifies on the setter's questions and books on the calendar.
3. It logs a summary and recording to the contact in GHL.

**Test B: speed-to-lead callback.**
1. Someone opts in and ticks "call me".
2. The voice agent calls within 2 minutes, confirms interest and books the call, or hands off to the setter.

## 2. Requirements

| # | Requirement | Must / should |
|---|---|---|
| 1 | Says it's an AI assistant when asked, and in markets that require it | Must |
| 2 | Calls only people who asked to be called (Test B). No cold calls | Must |
| 3 | Recording disclosure where the law requires it | Must |
| 4 | Books only into real open slots on the setter or closer calendar | Must |
| 5 | No health, medical, efficacy or price promises beyond the approved script | Must |
| 6 | Hands off to a human on request, or when stuck | Must |
| 7 | Every call logged to GHL: summary, outcome, recording | Must |
| 8 | Voice and pacing that sound natural in the market's language | Should |

## 3. Data

Call recordings and summaries live in GHL on the contact. Test results go in a sheet: call, test, outcome, booked, showed, closed.

## 4. Integrations

- GHL Voice AI and the calendar. Chris's EA can build the GHL side.
- If GHL's voice falls short on quality or control, test a dedicated voice platform next. Measure it first; don't assume.

## 5. INPUT NEEDED

- Which business and offer each test runs for.
- The setter's qualifying questions and the booking calendar.
- Which numbers and markets.
- The consent wording on the opt-in form, for Test B.

## 6. Acceptance

- [ ] 10 internal test calls pass (books right, discloses, hands off on request).
- [ ] 20 real calls per test, with results in the sheet.
- [ ] Chris decides keep, change or kill.

## 7. Build order

1. Test A script and build.
2. Internal tests.
3. Live for one week.
4. Test B after Test A passes.

## 8. Out of scope

Cold outbound calling. Calls to anyone who didn't ask to be called.
