---
name: coding-aesthetic-pairwise-skill
description: Task-specific annotation rubric generated from Feishu training materials and annotation manuals. Use when Codex needs to judge, compare, or label this queue's tasks in Chrome using the distilled training rules, permission-quiz evidence, learned patterns, and user-preferred reason style.
---

# Coding Aesthetic Pairwise Skill

## Goal

Use the bundled training summary and manual rules to complete this specific annotation queue. Prioritize task-specific training rules over generic annotation habits.

Default confirmation policy: ask the user before final questionnaire submission, permission submission, or final annotation submission unless the user explicitly authorizes auto-submit for this queue.

## Required References

Read the relevant reference before working:

- `references/training-summary.md` for video and onboarding conclusions.
- `references/manual-summary.md` for official manual rules.
- `references/rule-updates.md` for newest manual updates, quiz feedback, and user corrections. Read this first because it may override older summaries.
- `references/quiz-draft.md` when answering or reviewing permission quizzes.
- `references/learned-patterns.md` for user corrections and repeated cases.
- `references/reason-examples.md` for short natural Chinese wording.
- `references/user-style.md` when the user has provided previous annotation answers; imitate those sentence patterns first.

## Pre-Judgement Checklist

Before judging each item, complete this checklist:

1. Read `references/rule-updates.md` first. Newer rule updates override older summaries.
2. Read `references/learned-patterns.md` for reusable user corrections.
3. Read the current task prompt and extract the visual requirement.
4. Identify whether this is a normal task, returned/rework task, permission quiz, or inaccessible page.
5. Check waste/abandon conditions before normal pairwise judgement.
6. Judge screenshot-visible aesthetics and prompt fit before opening any URL.
7. For pairwise tasks, compare against the prompt, screenshots, and task rubric, not personal taste.
8. Apply rule priority: current user instruction > user correction > rule updates > official manual > training summary > shared stable rules > general judgement.
9. If a rule conflict affects the current item, pause and mention the conflict.
10. Write the reason using `references/user-style.md` and `references/reason-examples.md`, keeping it short and natural.
11. Do not final-submit unless the current queue has explicit user approval for auto-submit.

## Review Flow

1. Complete the Pre-Judgement Checklist before deciding the label.
2. Do not process returned/rework tasks unless the user explicitly asks.
3. Read the task prompt and extract the visual requirement before judging screenshots.
4. Judge the screenshots first. Only open the URL when needed to verify whether a screenshot is incomplete or unreasonable.
5. Compare screenshot-visible layout, color, material quality, information hierarchy, consistency, and visual comfort.
6. Return to the original task page and fill the judgement and reason.
7. Pause before final submission unless this queue has explicit user approval for auto-submit.

## Stable Rules

- Check `references/rule-updates.md` before each annotation batch. Newer updates override earlier summaries when there is a clear conflict.
- Blank, white-screen, black-screen, broken, or screenshots that cannot reflect the prompt should be marked as waste/abandoned when the platform supports it.
- This queue judges screenshot aesthetics only. Do not test or penalize website functions, interactions, or workflow completeness.
- Do not choose a side because it has more screenshots. Compare the visible screenshot quality and whole-set consistency.
- Reasons should be short, direct, and natural Chinese. Use Chinese commas or pause marks, not slashes, for multiple similar items.

## Reason Style

When writing reasons, follow this priority:

1. If `references/user-style.md` has user-provided historical answers, imitate its sentence length, wording habits, and level of detail.
2. Use the task manual rules from `training-summary.md` and `manual-summary.md` to decide which visual evidence matters.
3. Use `reason-examples.md` only as a backup phrase pool when the user's own style does not cover the case.

Prefer the user's plain annotation voice over polished report language. Write concrete screenshot evidence such as `布局更清晰`, `配色更协调`, `素材更精致`, `留白更舒服`, `整体风格更统一`, `页面显得比较廉价`. Avoid broad empty phrases such as `整体体验更佳` unless the user's examples use them.

## Quiz Flow

When answering a permission quiz:

1. Use only `training-summary.md`, `manual-summary.md`, and visible quiz/training evidence.
2. Draft each answer with evidence and confidence.
3. Ask the user to confirm before clicking final submit.
4. If feedback reveals a wrong assumption, update `learned-patterns.md`.

## Skill Evolution

When the user corrects a judgement or wording, update `references/rule-updates.md`, `references/learned-patterns.md`, `references/reason-examples.md`, or `references/user-style.md` with the reusable rule. Use `rule-updates.md` for active rule changes that should affect the next task immediately. Keep entries short and general so future labels do not sound copied.
