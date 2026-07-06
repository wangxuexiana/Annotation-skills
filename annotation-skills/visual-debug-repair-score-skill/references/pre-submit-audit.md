# Pre-Submit Audit

Run this audit before filling the final score, abandon flag, reason, quiz answer, or final submit.

## Judgement Audit

- [ ] Did I read the problem repair description and identify the exact defect that should be fixed?
- [ ] Did I inspect the reference image target and the repaired webpage output?
- [ ] Did I scan the repaired webpage from first screen to bottom?
- [ ] Did I check official abandon rules before assigning 0/1/2?
- [ ] If the repaired webpage is stuck loading or cannot be normally viewed, did I score 0 rather than abandon unless a separate task-invalid rule applies?
- [ ] If the core problem is still present, did I score 0?
- [ ] If the core problem is fixed but visual fidelity is clearly low, did I score 1?
- [ ] If considering 2 points, did I confirm high reference fidelity and full UP instruction implementation?
- [ ] If multiple candidates could be 2, did I keep only the best one as 2 and downgrade the others to 1?
- [ ] Did I avoid using hidden DOM, source code, or metadata as evidence instead of visible page behavior?
- [ ] Did I write or update the current-item checklist and browser observation state?

## Reason Audit

- [ ] Reason matches the visible evidence and chosen score/abandon result.
- [ ] Reason is short, natural Chinese, and focused on the main scoring point.
- [ ] Reason follows active constraints in `user-style.md`.
- [ ] Reason examples were used as phrase pools, not copied blindly.

## Submission Gate

- [ ] No login, CAPTCHA, permission, account, payment, or irreversible-action prompt is blocking the page.
- [ ] No unresolved item in `state/pending-uncertainties.md` affects this score, reason, abandon flag, quiz answer, or final submit.
- [ ] No completed-answer/result/submission-status log will be written locally unless the user explicitly asked for logging.
- [ ] The user has approved final submission, or this exact queue has explicit auto-submit approval.

If any box is uncertain, pause and resolve it before submitting.
