# Pre-Submit Audit

Run this audit before filling the final label, reason, waste flag, or quiz answer.

## Judgement Audit

- [ ] Did I read the current task prompt and extract the core requirement?
- [ ] Did I apply `priority-rules.md` and newest `rule-updates.md`?
- [ ] Did I write a 3-8 point current-item checklist in `state/current-item.md` before deciding?
- [ ] Did I compress browser observations into `state/browser-observation.json` instead of retaining long browser context in chat?
- [ ] Did I compare the final judgement against each current-item checklist point?
- [ ] Did I apply the full applicable rubric instead of over-focusing on the newest correction?
- [ ] Did I avoid overfitting to the latest user correction while still applying it as a guardrail?
- [ ] Did I avoid missing any higher-priority rule from `priority-rules.md`, `rule-updates.md`, the visible platform instruction, or the official manual summary?
- [ ] Did I list the applicable dimensions before deciding, including layout, element completeness, content accuracy, visual details, hallucination control, function checks when relevant, broken images, and active user wording constraints?
- [ ] Did I classify the scene as Game, UI, or other before applying dimension priority?
- [ ] For Game scenes, did I prioritize functional completeness and functional defects over aesthetics?
- [ ] For UI scenes, did I prioritize functional completeness and aesthetics over smaller functional defects?
- [ ] Did I check waste-like conditions and then still choose the GSB relationship instead of applying a waste tag?
- [ ] Did I check both candidates or the current preview for broken images in key visible content?
- [ ] Did I test prompt-named core functions instead of judging only the visual shell?
- [ ] Did I distinguish missing prompt-required functions from defects in implemented but non-required controls?
- [ ] Did every tested control produce visible or textual feedback when required?
- [ ] For pairwise tasks, did I compare higher-priority dimensions before color mood, decorative polish, or small details?
- [ ] For pairwise tasks, did I avoid forcing Same when a higher-priority dimension clearly favors one side?
- [ ] If A is waste-like and B is normal, did I choose `A < B`; if both are waste-like, did I choose `A = B`?
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
- [ ] The user has approved final submission, or this exact queue has explicit auto-submit approval.

If any box is uncertain, pause and resolve it before submitting.
