# Pre-Submit Audit

Run this audit before filling the final label, reason, waste flag, or quiz answer.

## Judgement Audit

- [ ] Did I read the current task prompt and extract the core requirement?
- [ ] Did I read the UP instruction and decide whether it changes the expected target?
- [ ] Did I compare against the reference image baseline rather than only judging general page beauty?
- [ ] Did I apply `priority-rules.md` and newest `rule-updates.md`?
- [ ] Did I write a 3-8 point current-item checklist in `state/current-item.md` before deciding?
- [ ] Did I compress browser observations into `state/browser-observation.json` instead of retaining long browser context in chat?
- [ ] Did I compare the final judgement against each current-item checklist point?
- [ ] Did I apply the full applicable rubric instead of over-focusing on the newest correction?
- [ ] Did I avoid overfitting to the latest user correction while still applying it as a guardrail?
- [ ] Did I avoid missing any higher-priority rule from `priority-rules.md`, `rule-updates.md`, the visible platform instruction, or the official manual summary?
- [ ] Did I list the applicable dimensions before deciding, including layout, element completeness, content accuracy, visual details, hallucination control, function checks when relevant, broken images, and active user wording constraints?
- [ ] Did I check the manual discard case before normal scoring?
- [ ] Did I check both candidates or the current preview for broken images in key visible content?
- [ ] Did I test UP-required or prompt-named core functions instead of judging only the visual shell?
- [ ] Did every tested control produce visible or textual feedback when required?
- [ ] Did I first decide each product's 0/1 eligibility before promoting one best 1-point product to 2?
- [ ] Did I avoid assigning 2 directly without confirming the product qualifies as 1?
- [ ] For each 0-point product, did I prepare or upload a screenshot of the deciding problem when required?
- [ ] Did I avoid using hidden DOM, code, or metadata as feature evidence?

## Reason Audit

- [ ] Reason matches the actual visible evidence.
- [ ] Reason is short, natural Chinese, and focused on the deciding restoration mismatch, function miss, or small remaining flaw.
- [ ] Reason follows all active constraints in `user-style.md`.
- [ ] If comma-only punctuation is active, the reason uses commas for clause breaks and contains no other punctuation.
- [ ] Reason sounds like a human annotation note, not a formal audit report.
- [ ] Reason does not include unnecessary technical jargon.
- [ ] Reason examples and old user answers were used as style anchors, not copied blindly.

## Submission Gate

- [ ] No login, CAPTCHA, permission, account, payment, or irreversible-action prompt is blocking the page.
- [ ] No unresolved item in `state/pending-uncertainties.md` affects this label, reason, waste flag, quiz answer, or final submit.
- [ ] No completed-answer/result/submission-status log will be written locally unless the user explicitly asked for logging.
- [ ] The user has approved final submission, or this exact queue has explicit auto-submit approval.

If any box is uncertain, pause and resolve it before submitting.
