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

## Pre-Judgement Checklist

Add this checklist to generated task skills and complete it before judging each annotation item:

1. Read `references/rule-updates.md` first. Newer rule updates override older summaries.
2. Read `references/learned-patterns.md` for reusable user corrections.
3. Read the current task prompt and extract the core requirement.
4. Identify whether this is a normal task, returned/rework task, permission quiz, or inaccessible page.
5. Check waste/abandon conditions before normal pass/fail or pairwise judgement.
6. Test prompt-named core functions before judging visual polish.
7. For pairwise tasks, compare against the prompt and task rubric, not personal taste.
8. Apply rule priority: current user instruction > user correction > rule updates > official manual > training summary > shared stable rules > general judgement.
9. If a rule conflict affects the current item, pause and mention the conflict.
10. Write the reason using user style and reason examples, keeping it short and natural.
11. Do not final-submit unless the current queue has explicit user approval for auto-submit.

## Annotation Loop

- Complete the task skill's Pre-Judgement Checklist before deciding the label.
- Read the task prompt before opening the test scene.
- Open scene or candidate pages in a separate tab/window.
- Test prompt-named functions before visual polish.
- Close the test tab/window after testing.
- Return to the task page and fill the judgement.
- Log reusable corrections into the task skill.
