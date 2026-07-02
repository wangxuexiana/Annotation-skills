# Pre-Submit Audit

Run this audit before filling rubric values, A/B scores, preference, reason, waste flag, quiz answer, or final submission.

## Judgement Audit

- [ ] Did I read the current task prompt and extract the core requirement?
- [ ] Did I apply `priority-rules.md` and newest `rule-updates.md`?
- [ ] Did I open the before-fix page to confirm the baseline problem and original normal content?
- [ ] Did I inspect the reference image when present?
- [ ] Did I inspect both candidate A and candidate B?
- [ ] Did I test prompt-named functions or interactions instead of judging from static appearance?
- [ ] Did I score every rubric for both A and B?
- [ ] Did I reserve `无法判断` for true evidence insufficiency rather than confirmed candidate failure?
- [ ] Did I give A and B 0-5 scores using target repair first, request/reference match second, side effects third?
- [ ] Did I choose Same/Tie only when A and B are substantively close?
- [ ] Did I avoid using visual prettiness, larger change, or minor polish as the main reason when current problem repair differs?
- [ ] Did I check serious side effects such as layout collapse, missing core content, unreadable text, broken images, or broken interactions?
- [ ] Did I check waste conditions before normal scoring, and avoid wasting scoreable poor candidates?
- [ ] Did I avoid using hidden DOM, code, or metadata as feature evidence?
- [ ] Did I append the compact result to `state/batch-log.md`?

## Reason Audit

- [ ] Reason matches the actual visible evidence.
- [ ] Reason is short, natural Chinese, and focused on the main core issue.
- [ ] Reason follows all active constraints in `user-style.md`.
- [ ] Reason sounds like a human annotation note, not a formal audit report.
- [ ] Reason does not include unnecessary technical jargon.
- [ ] Reason examples and old user answers were used as style anchors, not copied blindly.
- [ ] If `无法判断` or waste is used, the reason names the exact missing link, field, resource, or condition and why judgement cannot continue.

## Submission Gate

- [ ] No login, CAPTCHA, permission, account, payment, or irreversible-action prompt is blocking the page.
- [ ] No unresolved item in `state/pending-uncertainties.md` affects this answer.
- [ ] The user has approved final submission, or this exact queue has explicit auto-submit approval.

If any box is uncertain, pause and resolve it before submitting.

