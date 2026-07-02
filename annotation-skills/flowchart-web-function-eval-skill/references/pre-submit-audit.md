# Pre-Submit Audit

Run this audit before filling the final label, reason, waste flag, or quiz answer.

## Judgement Audit

- [ ] Did I read the current task prompt and extract the core requirement?
- [ ] Did I inspect the reference flowchart and identify entries, branches, routing, and final states?
- [ ] Did I apply `priority-rules.md` and newest `rule-updates.md`?
- [ ] Did I write a 3-8 point current-item checklist in `state/current-item.md` before deciding?
- [ ] Did I compress browser observations into `state/browser-observation.json` instead of retaining long browser context in chat?
- [ ] Did I compare the final judgement against each current-item checklist point?
- [ ] Did I apply the full applicable rubric instead of over-focusing on the newest correction?
- [ ] Did I avoid overfitting to the latest user correction while still applying it as a guardrail?
- [ ] Did I avoid missing any higher-priority rule from `priority-rules.md`, `rule-updates.md`, the visible platform instruction, or the official manual summary?
- [ ] Did I list the applicable dimensions before deciding, including layout, element completeness, content accuracy, visual details, hallucination control, function checks when relevant, broken images, and active user wording constraints?
- [ ] Did I check waste/abandon conditions before normal fail?
- [ ] Did I avoid abandoning an item that can still be evaluated normally?
- [ ] Did I test every behavior-related rubric in `modelA` instead of judging from screenshot alone?
- [ ] Did every tested control, route, validation, submission, filter, popup, or completion step produce the required visible result when needed?
- [ ] Did I judge every rubric independently according to its own wording?
- [ ] Did I avoid inventing extra product requirements beyond the prompt, flowchart, and rubrics?
- [ ] Did I assign an integer overall score from `0` to `10`?
- [ ] Is the overall score consistent with prompt/flowchart implementation and the rubric labels?
- [ ] Did I compare `modelA_img` with the initial loaded page before any interaction?
- [ ] Did I keep screenshot correctness separate from functional quality?
- [ ] Did I avoid using hidden DOM, code, or metadata as feature evidence?

## Reason Audit

- [ ] Reason matches the actual visible evidence.
- [ ] Reason is short, natural Chinese, and focused on the main core issue.
- [ ] Reason follows all active constraints in `user-style.md`.
- [ ] If comma-only punctuation is active, the reason uses commas for clause breaks and contains no other punctuation.
- [ ] Reason sounds like a human annotation note, not a formal audit report.
- [ ] Reason does not include unnecessary technical jargon.
- [ ] Reason examples and old user answers were used as style anchors, not copied blindly.

## Submission Gate

- [ ] No login, CAPTCHA, permission, account, payment, or irreversible-action prompt is blocking the page.
- [ ] No unresolved item in `state/pending-uncertainties.md` affects this label, reason, waste flag, quiz answer, or final submit.
- [ ] `state/batch-log.md` has enough information to recover this item after context compaction.
- [ ] All required fields are ready: waste/abandon, every rubric label and reason when required, overall score, screenshot correctness, and QC conclusion when in QC mode.
- [ ] The user has approved final submission, or this exact queue has explicit auto-submit approval.

If any box is uncertain, pause and resolve it before submitting.
