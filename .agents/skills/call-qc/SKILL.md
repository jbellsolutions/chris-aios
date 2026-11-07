---
name: call-qc
description: Use to review recorded COG sales calls - score each against the call standard with timestamps, write weekly per-rep coaching notes and the Friday team patterns report, and send recurring problems to the Growth Operator. For the Sales Coach on the business account.
---

# Call QC

Work only in `~/chris-aios`.

## When to use

The weekday call QC, the Friday coaching report, or "review this call", "how's <rep> doing on calls?"

## Inputs and access

- **Calls:** new recordings or transcripts from `calls.transcript_source` in `context/cog.json` (GHL call recordings, Zoom, read.ai, Fathom or a Drive folder). If it still says REQUIRED, reply `NO_CLIENT_SOURCE: call recordings` and stop. Never go looking for recordings elsewhere.
- **The roster:** `roster` in `context/cog.json` (name, role, active).
- **The standard:** `context/call-standard.md`. If it's missing, draft one from COG's scripts and SOPs in Drive, the default rubric below and the libraries in `libraries/`; send it to Chris and score nothing until he says yes. After his yes, save it in his words.

## The rubric (default; Chris's standard overrides it)

| Line | A 5 looks like |
|---|---|
| Opener and rapport | Sets the agenda, earns the right to ask questions |
| Discovery | Gets the real situation, the pain, the cost of staying put |
| Desired outcome | The prospect says what they want, in their own words |
| Offer and mechanism | Explains why this works for them, tied to their pain |
| Objections | Isolates, answers with their own words, confirms |
| The ask | Asks clearly for the decision, then stays quiet |
| Next steps | A booked next step or payment, no loose ends |
| Compliance | No promise the business can't stand behind |

## Steps for each call

1. Match the call to a roster rep. If it's unclear, list it as "unmatched". Never guess.
2. Read the whole transcript. Score each line 1–5 with the timestamp that proves it.
3. Write one "do this instead" line for the two lowest scores, using the rep's own words.
4. Mark game film: any moment scoring 5 that others should hear.
5. Save to `vault/coaching/Calls/<date>-<rep>-<lead first name>.md`, and add a line to `vault/coaching/Reps/<rep>.md`.

## Daily output

Write to `daily/<date>/coaching.md` for Chief's brief. Message Chris directly only when a call needs him today:

```
Calls QC — Tue (14 scored, 1 unreadable)
Needs you: Mike × Dana, 32:10 — gave a discount without asking <link>
Best call: Ana × Jordan, 4.6 — clip for Friday <link>
Team avg 3.4 (last week 3.2). Weakest: the ask (2.8).
```

## Friday report

- **Per rep** (draft note in `vault/coaching/Reps/<rep>.md`): calls reviewed, average by line, the two habits to fix, a clip of theirs and a clip from the best call.
- **Team** (`vault/coaching/Patterns/<week>.md`): the top three objections with the best answer heard to each, where calls die (the line with the lowest team average), and one drill.
- **Requests:** an objection or winning line heard three or more times becomes `queue/jobs/growth-operator/<date>-<slug>.md`, citing the calls.

## Validate before sending

- Every score has a timestamp.
- No trend is called from fewer than three of a rep's calls.
- Pay and employment never appear in a note.

## Return

The daily note (and a message only if needed), or the Friday summary under 150 words with rep notes linked.

## Needs Chris's yes

Sending a coaching note to a rep, posting in any channel, and any change to the call standard.
