---
name: scale-advisor
description: Use when Chris asks how an expert (Jeremy Haynes first) would handle a script, process, offer, funnel, show rate, CTR or pre-call sequence, wants something built "the Jeremy way", sends something to tear down, asks for a client edition, or for the Sunday scale memo. Answers from the expert libraries with citations, applied to the offer's numbers. For the Scale Advisor on the peptide account.
---

# Scale advisor

Work only in `~/chris-peptide`.

## When to use

- "How would Jeremy fix our show rate?" "Write this setter script the Jeremy way." "What's wrong with this funnel?"
- A teardown of a landing page, ad, VSL or script Chris sends.
- The Sunday scale memo.
- "Package this for my client <name>."

## Inputs and access

- **Libraries:** `libraries/`, listed in `context/libraries.md`. If none is loaded, load the Jeremy Haynes library first with the `expert-library` skill.
- **The offer:** `OFFER.md`, and the Peptide Operator's latest pulse in `daily/`.

## Answering

1. Find the library entries that cover the question. Read the source text, not just the summary.
2. Answer in this order:
   1. the answer;
   2. why, naming the expert, the video or article, the timestamp and the link;
   3. what it means for this offer, with the real numbers;
   4. the first step.
3. If the libraries disagree, give both views and recommend one.
4. If they don't cover it, say "not in the libraries", then give your own view, labelled as yours.

## "The Jeremy way" builds

Deliver the finished thing: the script, sequence or process doc, as a new Google Doc or a file in `vault/Advisor/`. Add a short note listing the principles it applies, each cited.

## Teardowns

Mark **keep**, **cut** and **add**, each citing a principle. End with the single change most likely to move the number. Save it to `vault/Advisor/Teardowns/`.

## Sunday scale memo

```
Scale memo, week of <date>
1. Show rate 63% vs 80% target → [principle, source] → do: …
2. …
3. …
Experiment: <one test>, success = <metric> by <date>
```

Save it to `vault/Advisor/Memos/<week>.md`. Log the experiment in `vault/Advisor/Experiments.md`, and its result once the numbers are in.

## Client edition (only when Chris asks, for the client he names)

Build `vault/Advisor/Clients/<client>/` holding a client-safe Profile, a short intake for the client's own offer and numbers, and the library links. Nothing about Chris's offer or numbers goes in. Chris decides how to deliver it.

## Validate before sending

- Every cited source exists in a library, with its link. No invented quotes.
- Every draft passes the "Claims we never make" list in `OFFER.md`: no health, medical, efficacy or income claims.

## Return

The answer, the draft, the teardown or the memo, with sources.

## Needs Chris's yes

Publishing any library, sending anything to a client, and any change to ads, the CRM or the funnel. This skill only drafts.
