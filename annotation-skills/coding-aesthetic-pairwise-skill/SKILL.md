---
name: coding-aesthetic-pairwise-skill
description: Task-specific annotation rubric generated from Feishu training materials and annotation manuals. Use when Codex needs to judge, compare, or label this queue's tasks in Chrome using the distilled training rules, permission-quiz evidence, learned patterns, and user-preferred reason style.
---

# Coding Aesthetic Pairwise Skill

## Goal

Use the bundled training summary and manual rules to complete the Coding 美观度 pairwise SingleImage queue. Prioritize screenshot-visible aesthetic evidence over generic web-app annotation habits.

This queue is screenshot-only: judge the two model screenshots for webpage aesthetics. Do not test functionality, interaction completeness, or prompt feature implementation unless the visible screenshot itself makes the issue obvious.

Default confirmation policy: ask the user before final questionnaire submission, permission submission, or final annotation submission unless the user explicitly authorizes auto-submit for this queue.

## Required References

Read the relevant reference before working:

- `references/training-summary.md` for video and onboarding conclusions.
- `references/manual-summary.md` for official manual rules.
- `references/quiz-draft.md` when answering or reviewing permission quizzes.
- `references/learned-patterns.md` for user corrections and repeated cases.
- `references/rule-updates.md` for latest rule changes. Read this before older summaries because it may override previous understanding.
- `references/reason-examples.md` for short natural Chinese wording.
- `references/user-style.md` when the user has provided previous annotation answers; imitate those sentence patterns first.

## Pre-Judgement Checklist

Before judging each item, complete this checklist:

1. Read `references/rule-updates.md` first. Newer rule updates override older summaries.
2. Read `references/learned-patterns.md` for reusable user corrections.
3. Read the current task prompt and extract the core requirement.
4. Identify whether this is a normal task, returned/rework task, permission quiz, or inaccessible page.
5. Check waste/abandon conditions before normal pass/fail or pairwise judgement.
6. Do not open URLs to test functions. Use URLs only when needed to understand whether the screenshot matches the current product.
7. Compare the two screenshots against the prompt, inferred page purpose, and this aesthetic rubric, not personal taste.
8. Apply rule priority: current user instruction > user correction > rule updates > official manual > training summary > shared stable rules > general judgement.
9. If a rule conflict affects the current item, pause and mention the conflict.
10. Write the reason using `references/user-style.md` and `references/reason-examples.md`; include concrete visible differences across layout, color/type, material quality, or consistency when relevant.
11. Do not final-submit unless the current queue has explicit user approval for auto-submit.

## Review Flow

1. Complete the Pre-Judgement Checklist before deciding the label.
2. Do not process returned/rework tasks unless the user explicitly asks.
3. Read the task prompt, then click the page's "已阅读 prompt" control if required to unlock annotation fields.
4. Inspect both model screenshots on the task page; use the built-in image zoom when detail is too small.
5. Decide whether the item is waste before normal pairwise judgement.
6. Select the inferred page purpose in the dropdown.
7. Compare layout hierarchy, color/type, material quality, and consistency/detail.
8. Fill the four dimension comments, then the overall `-1 / 0 / 1` judgement and reason.
9. Pause before final submission unless this queue has explicit user approval for auto-submit.

## Stable Rules

Read the shared generic rules first:

- `../annotation-workflow-skill/references/stable-annotation-rules.md`

Task-specific manuals, `references/rule-updates.md`, and explicit user corrections override shared generic rules when they clearly conflict.

Minimal fallback if the shared file is unavailable:

- Broken or unrenderable previews are waste/abandoned when supported.
- In this queue, screenshot aesthetics outweigh functional completeness.
- Do not test named controls or interactions for this queue.
- Reasons should be short, direct, and natural Chinese.

## Queue-Specific Labels

- `-1`: 模型 1 更美观。
- `0`: 两者美观度基本相当，或无法稳定区分优劣但仍可评测。
- `1`: 模型 2 更美观。
- 废弃：无法通过截图判断美观度，或截图存在白屏、黑屏、乱码、报错、主体缺失、严重裁切、信息过少等质量问题。

## Aesthetic Rubric

Judge the two screenshots by first inferring the page purpose, then applying these priorities:

1. Fatal visible defects beat minor flaws: unreadable core text, unrecognizable core buttons, broken images, failed rendering, blocked core material, and unreplaced placeholders matter heavily.
2. Page goal beats personal taste: dashboards can be dense, children's education can be colorful, and visual style must fit the prompt and likely users.
3. Ambitious high-quality execution beats plain but empty execution: rich content, strong materials, and unified detail can beat a sparse layout with no obvious errors.

Then compare four dimensions:

- 布局与信息层级：core guidance, hierarchy, spacing, alignment, centering, symmetry.
- 色彩与排版：scene fit, contrast, core text readability, harmony, saturation quality.
- 图像、图标与素材质量：rendering integrity, theme fit, image quality, icon/material polish.
- 一致性与细节精致度：unified design language, consistent component sizes, coherent details.

## Reason Style

When writing reasons, follow this priority:

1. If `references/user-style.md` contains historical answers from the user, imitate its sentence length, wording habits, and level of detail.
2. Use `training-summary.md` and `manual-summary.md` to decide which evidence matters for this queue.
3. Use `reason-examples.md` as a backup phrase pool, not as fixed templates.

Do not copy old answers mechanically. Adapt the user's style to the current task and current visible evidence.

## Rule Updates

Before each annotation batch, check `references/rule-updates.md` first. If it contains a newer rule that conflicts with `training-summary.md`, `manual-summary.md`, or `learned-patterns.md`, follow the newer rule and mention the conflict to the user when it affects the current task.

## Quiz Flow

When answering a permission quiz:

1. Use only `training-summary.md`, `manual-summary.md`, and visible quiz/training evidence.
2. Draft each answer with evidence and confidence.
3. Ask the user to confirm before clicking final submit.
4. If feedback reveals a wrong assumption, update `learned-patterns.md`.

## Skill Evolution

When the user corrects a judgement or wording, update `references/learned-patterns.md` or `references/reason-examples.md` with the reusable rule. Keep entries short and general so future labels do not sound copied.
