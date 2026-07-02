# Pre-Submit Audit

Run this audit before filling the final label, reason, waste flag, or quiz answer.

## Judgement Audit

- [ ] Did I read the current task prompt and extract the core requirement?
- [ ] Did I apply `priority-rules.md` and newest `rule-updates.md`?
- [ ] Did I apply the full applicable rubric instead of over-focusing on the newest correction?
- [ ] Did I list the applicable dimensions before deciding, including layout, element completeness, content accuracy, visual details, hallucination control, function checks when relevant, broken images, and active user wording constraints?
- [ ] Did I check waste/abandon conditions before normal fail?
- [ ] Did I check both candidates or the current preview for broken images in key visible content?
- [ ] Did I test prompt-named core functions instead of judging only the visual shell?
- [ ] Did every tested control produce visible or textual feedback when required?
- [ ] For pairwise tasks, did I compare higher-priority dimensions before color mood, decorative polish, or small details?
- [ ] For pairwise tasks, did I avoid forcing Same when a higher-priority dimension clearly favors one side?
- [ ] Did I avoid using hidden DOM, code, or metadata as feature evidence?
- [ ] For VisualDebug GSB, did I classify the item as explicit visual, open visual, or function/interaction repair?
- [ ] For VisualDebug GSB, did I compare target repair before restoration/completion and side effects?
- [ ] For VisualDebug GSB, is the selected label exactly `A good B`, `A bad B`, or `A same B`?

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
- [ ] The user has approved final submission, or this exact queue has explicit auto-submit approval.

If any box is uncertain, pause and resolve it before submitting.
