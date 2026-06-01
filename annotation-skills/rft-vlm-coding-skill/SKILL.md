---
name: rft-vlm-coding-skill
description: Task-specific annotation rubric generated from Feishu training materials and annotation manuals. Use when Codex needs to judge, compare, or label this queue's tasks in Chrome using the distilled training rules, permission-quiz evidence, learned patterns, and user-preferred reason style.
---

# Rft Vlm Coding Skill

## Goal

Use the bundled training summary and manual rules to complete this specific annotation queue. Prioritize task-specific training rules over generic annotation habits.

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
6. Test prompt-named core functions before judging visual polish.
7. For pairwise tasks, compare against the prompt and task rubric, not personal taste.
8. Apply rule priority: current user instruction > user correction > rule updates > official manual > training summary > shared stable rules > general judgement.
9. If a rule conflict affects the current item, pause and mention the conflict.
10. Write the reason using `references/user-style.md` and `references/reason-examples.md`, keeping it short and natural.
11. Do not final-submit unless the current queue has explicit user approval for auto-submit.

## Review Flow

1. Complete the Pre-Judgement Checklist before deciding the label.
2. Do not process returned/rework tasks unless the user explicitly asks.
3. Read the task prompt and extract the core requirement before testing.
4. Open the scene, candidate, or preview link in a separate new Chrome tab/window.
5. Test prompt-named core functions and visible natural controls.
6. Close the test tab/window after testing.
7. Return to the original task page and fill the judgement and reason.
8. Pause before final submission unless this queue has explicit user approval for auto-submit.

## Stable Rules

Read the shared generic rules first:

- `../annotation-workflow-skill/references/stable-annotation-rules.md`

Task-specific manuals, `references/rule-updates.md`, and explicit user corrections override shared generic rules when they clearly conflict.

Minimal fallback if the shared file is unavailable:

- Broken or unrenderable previews are waste/abandoned when supported.
- Prompt-named core functions outweigh visual polish.
- Named controls must produce visible or textual changes.
- Reasons should be short, direct, and natural Chinese.

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
