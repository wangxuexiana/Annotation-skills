# Pre-Submit Audit

Run this before filling a label, reason, waste flag, page-purpose dropdown, or quiz answer.

## Scope Audit

- [ ] I judged only screenshot-visible webpage aesthetics.
- [ ] I did not test interactions or functional completeness.
- [ ] I did not use hidden code, DOM, network state, or metadata as evidence.
- [ ] I respected the manual's warning against AI-assisted scoring or polishing by keeping human confirmation before final use.

## Judgement Audit

- [ ] I checked waste/abandoned conditions before normal scoring.
- [ ] If the screenshot was unjudgeable, I marked waste instead of forcing Same.
- [ ] I inferred the page purpose and judged against that scenario.
- [ ] I applied fatal visible defects before minor cosmetic flaws.
- [ ] I checked layout and information hierarchy.
- [ ] I checked color and typography, especially core text readability.
- [ ] I checked image, icon, and material quality, including broken images and placeholders.
- [ ] I checked consistency and detail polish.
- [ ] I considered whether rich coherent execution beats empty safe design.
- [ ] I used Same when the visible evidence is genuinely close, problem severity is comparable, or no obvious objective quality gap exists.
- [ ] I treated Same as the preferred answer for close cases.
- [ ] I chose A or B only if an obvious visible quality gap is present.
- [ ] I can point to the weaker screenshot's objective visible issue instead of relying on element count, personal taste, or content quantity.

## Reason Audit

- [ ] The reason is short and grounded in visible evidence.
- [ ] The reason mentions the main deciding difference, not every minor detail.
- [ ] The reason does not sound like over-polished AI prose.
- [ ] The reason follows `user-style.md` if active style constraints exist.
- [ ] The reason examples were used as phrase support, not copied blindly.

## Submission Gate

- [ ] No login, CAPTCHA, permission, account, or platform-risk prompt is blocking the page.
- [ ] No unresolved uncertainty in `state/pending-uncertainties.md` affects this answer.
- [ ] `state/batch-log.md` can recover the item after context compaction.
- [ ] The user has explicitly approved final submission or the intended use does not submit to the platform.

If any box is uncertain, pause before submitting.
