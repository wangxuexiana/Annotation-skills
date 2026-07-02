# Pre-Submit Audit

Run this audit before filling the final label, reason, waste flag, or quiz answer.

## Judgement Audit

- [ ] Did I read the current task prompt and extract the core requirement?
- [ ] Did I apply `priority-rules.md` and newest `rule-updates.md`?
- [ ] Did I apply the full applicable rubric, instead of over-focusing on the newest user correction?
- [ ] Did I list the current item's applicable dimensions before deciding, including layout, element completeness, content accuracy, visual details, hallucination control, functions if explicit, broken images, and user wording constraints?
- [ ] Did I compare higher-priority dimensions first, especially layout, position, size, spacing, first-screen content, module order, and core content?
- [ ] If a higher-priority dimension clearly wins, did I avoid using lower-priority color, image mood, or small detail advantages to force Same?
- [ ] Did I check both candidates for broken images, especially hero images, cards, product images, doctor photos, charts, and other key visible content?
- [ ] Did I check waste or abandon conditions before normal fail?
- [ ] Did I test prompt-named core functions instead of judging only the visual shell?
- [ ] Did every tested control produce visible or textual feedback when required?
- [ ] For pairwise tasks, did I compare against the rubric rather than personal preference?
- [ ] Did I avoid using hidden DOM, code, or metadata as feature evidence?

## Reason Audit

- [ ] Reason matches the actual visible evidence.
- [ ] Reason is short, natural Chinese, and focused on the main core issue.
- [ ] Reason does not include unnecessary technical jargon.
- [ ] Reason examples and old user answers were used as style anchors, not copied blindly.
- [ ] Reason follows active `user-style.md` constraints.
- [ ] If the user requested comma-only comparison reasons, the reason contains commas only and no other punctuation.
- [ ] Reason sounds口语化, direct, and close to human annotation wording.

## Submission Gate

- [ ] No login, CAPTCHA, permission, account, payment, or irreversible-action prompt is blocking the page.
- [ ] The user has approved final submission, or this exact queue has explicit auto-submit approval.

If any box is uncertain, pause and resolve it before submitting.
