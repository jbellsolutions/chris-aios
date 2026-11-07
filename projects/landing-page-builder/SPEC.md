# Landing page builder: project spec

**Owner:** Chris · **Builder:** Codex or Claude Code · **Runs on:** a Codex skill + GoHighLevel funnels (or a static host) · **Status:** draft

## 0. Charter

**What:** From a one-paragraph brief, an agent writes, builds and previews a complete landing page or funnel step on its own. Chris reviews one preview link and says publish or change.

**Why:** On Oct 6 Chris asked for an agent that builds sites and landing pages on its own, without him having to watch over it.

**Users:** Chris, his EA, and the Growth Operator and Media Buyer, who need pages for new angles.

**Done means:** A brief turns into a working preview link in one run, with copy, design, the form wired to the right GHL pipeline and tracking in place, and zero manual fixes for three pages in a row.

## 1. How it works

1. The brief: offer, audience, angle, call to action, where leads go.
2. Copy from the Growth Operator's `sales-asset-builder`, or the Scale Advisor for "the Jeremy way".
3. A design that follows the brand kit for that business (`context/brand.md` in its workspace).
4. The build:
   - in GHL's funnel builder through its AI builder or the browser;
   - or as a static page on a host Chris picks.
5. Wire the form to the GHL pipeline and add tracking (pixel or conversion events, UTMs).
6. Test-submit the form, confirm the lead lands, and send Chris the preview link.
7. On his yes, publish.

## 2. Requirements

| # | Requirement | Must / should |
|---|---|---|
| 1 | Runs end to end from the brief without Chris stepping in | Must |
| 2 | The form lands in the right pipeline, checked by a test submission | Must |
| 3 | Nothing goes live without Chris's yes | Must |
| 4 | Mobile-first and fast | Must |
| 5 | Passes the ad platform's landing-page policy for the category | Must |
| 6 | Reuses winning sections from past pages | Should |

## 3. Data

Briefs, copy and preview links go in that business's vault (`vault/assets/` or `peptide/vault/Ads/`). Leads go in its CRM only.

## 4. Integrations

GHL (funnels, forms, pipelines), the ad pixel, and the host if not GHL. Access is scoped to a test sub-account or draft pages until approved.

## 5. INPUT NEEDED

- Brand kit (logo, colors, fonts, tone).
- Which GHL sub-account and pipelines.
- The domain.
- One page Chris considers "the standard".

## 6. Acceptance

- [ ] Three pages from three briefs, each preview working with zero manual fixes.
- [ ] Test leads land in the right pipeline.

## 7. Build order

1. Copy and preview only.
2. Form wiring.
3. Tracking.
4. Publish on yes.

## 8. Out of scope

Building full websites and CRMs. That comes later, on the same pattern.
