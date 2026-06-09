# Annotation Workflow Checklist

## Intake

- Confirm the queue name, task type, Feishu video link, manual link, and permission questionnaire link.
- Keep the browser in the user's logged-in Chrome profile.
- Record the current workflow state: `待学习`, `待答卷`, `待开权限`, `可标注`, `标注中`, or `规则复盘`.

## Training Summary

Write `training-summary.md` with these headings:

- `任务与队列`: task name, platform, target queue, related links.
- `核心判定`: what counts as pass/better/same/fail/waste.
- `操作流程`: how to open previews, test scenes, close test tabs, and return to the task page.
- `易错点`: common traps, strict rules, and user corrections.
- `理由话术`: preferred short Chinese reason style.
- `问卷知识点`: facts likely to appear in permission quizzes.

## Browser Safety

- Do not bypass login, CAPTCHA, access controls, or platform risk checks.
- Do not submit permission quizzes or final labels before the current confirmation policy allows it.
- Stop and ask when a page asks for identity verification, payment, new authorization, or irreversible account action.
- If a video, manual, or queue is inaccessible, report the exact blocker and needed user action.

## Generated Skill Structure

Generated task skills should keep `SKILL.md` compact and move executable safeguards into focused reference files:

- `references/priority-rules.md`: rule priority and conflict handling.
- `references/decision-checklist.md`: per-item judgement checklist.
- `references/pre-submit-audit.md`: final audit before filling or submitting.
- `references/common-failure-patterns.md`: recurring traps and concrete examples.
- `references/rule-updates.md`: newest active overrides.
- `references/learned-patterns.md`: reusable user corrections.
- `references/user-style.md`: active reason punctuation and tone constraints, plus historical answer style.

Do not rely on a long list of rules in memory. For each item, extract a small current-item checklist from the prompt and required references.
The checklist must cover the full applicable rule set, not only the newest user correction or the most recently discussed detail.

## Pre-Judgement Checklist

Add this checklist to generated task skills through `references/decision-checklist.md` and complete it before judging each annotation item:

1. Read `references/priority-rules.md` and `references/rule-updates.md` first.
2. Read the current task prompt and extract the core requirement.
3. Build a 3-8 point current-item checklist from the prompt and applicable task rules.
4. Include the full applicable rule set in that checklist, including prompt fit, layout, element completeness, content accuracy, visual details, hallucination control, broken images, function checks when relevant, and active reason-style constraints.
5. Identify whether this is a normal task, returned/rework task, permission quiz, or inaccessible page.
6. Check waste/abandon conditions before normal pass/fail or pairwise judgement.
7. Check key visible images for broken loading, especially hero, card, product, avatar, doctor, chart, gallery, or required comparison images.
8. Test prompt-named core functions before judging visual polish.
9. For pairwise tasks, compare higher-priority dimensions before color mood, decorative polish, or small details.
10. Apply rule priority from `references/priority-rules.md`; treat new user corrections as guardrails inside the full rubric, not replacements for all other applicable rules.
11. If a rule conflict affects the current item, pause and mention the conflict.
12. Run `references/pre-submit-audit.md` before filling the final label or reason.
13. Write the reason using active `user-style.md` constraints and reason examples, keeping it short, colloquial, and comma-only when that preference is active.
14. Do not final-submit unless the current queue has explicit user approval for auto-submit.

## Annotation Loop

- Complete the task skill's Pre-Judgement Checklist before deciding the label.
- Read the task prompt before opening the test scene.
- Build and follow a current-item checklist instead of relying on the whole rubric from memory.
- Avoid overfitting to the latest correction and avoid underfitting by skipping older still-valid rules.
- Open scene or candidate pages in a separate tab/window.
- Test prompt-named functions before visual polish.
- Check broken key images before deciding.
- Run the pre-submit audit before filling labels, reasons, or waste flags.
- Close the test tab/window after testing.
- Return to the task page and fill the judgement.
- Log reusable corrections into the task skill.
