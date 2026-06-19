# Pre-Submit Audit

Run this audit before filling the final label, reason, waste flag, or quiz answer.

## Judgement Audit

- [ ] Did I read the current task prompt and extract the core requirement?
- [ ] Did I apply `priority-rules.md` and newest `rule-updates.md`?
- [ ] Did I write a 3-8 point current-item checklist in `state/current-item.md` before deciding?
- [ ] Did I compress browser observations into `state/browser-observation.json` instead of retaining long browser context in chat?
- [ ] Did I compare the final judgement against each current-item checklist point?
- [ ] Did I inspect GT, image1, and image2 rather than relying on thumbnail impression?
- [ ] Did I verify and repair O1/O2/O3 rubrics before scoring?
- [ ] Did every final rubric receive separate image1 and image2 scores?
- [ ] Did I keep O1, O2, and O3 dimension boundaries independent?
- [ ] If O1 is `0`, did I still complete O2/O3 scores, reasons, pairwise, and all remaining fields?
- [ ] Did I check that overall follows `O1=0 => 0`, otherwise `0.25*O1 + 0.65*O2 + 0.10*O3`?
- [ ] If pairwise winner conflicts with score arithmetic or visible severity, did I mark/report and explain the conflict?
- [ ] Did I apply the full applicable rubric instead of over-focusing on the newest correction?
- [ ] Did I avoid overfitting to the latest user correction while still applying it as a guardrail?
- [ ] Did I avoid missing any higher-priority rule from `priority-rules.md`, `rule-updates.md`, the visible platform instruction, or the official manual summary?
- [ ] Did I list the applicable dimensions before deciding, including layout, element completeness, content accuracy, visual details, hallucination control, function checks when relevant, broken images, and active user wording constraints?
- [ ] Did I follow the current queue rule that ordinary items are not abandoned unless the platform exposes such a path?
- [ ] For pairwise tasks, did I compare overall first, then O2/O1 critical errors, then O3?
- [ ] For pairwise tasks, did I avoid letting color mood, decorative polish, or small style details override chart type or data correctness?
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
- [ ] No completed-answer/result/submission-status log will be written locally unless the user explicitly asked for logging.
- [ ] The user has approved final submission, or this exact queue has explicit auto-submit approval.

If any box is uncertain, pause and resolve it before submitting.
