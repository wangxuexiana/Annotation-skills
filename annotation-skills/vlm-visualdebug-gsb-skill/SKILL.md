---
name: vlm-visualdebug-gsb-skill
description: Task-specific annotation rubric generated from Feishu training materials and annotation manuals. Use when Codex needs to judge, compare, or label this queue's tasks in Chrome using the distilled training rules, permission-quiz evidence, learned patterns, and user-preferred reason style.
---

# Vlm Visualdebug Gsb Skill

## Goal

Use the bundled training summary and manual rules to complete this specific annotation queue. Prioritize task-specific training rules over generic annotation habits.

Default confirmation policy: ask the user before final questionnaire submission, permission submission, or final annotation submission unless the user explicitly authorizes auto-submit for this queue.

## Required References

Read the relevant reference before working:

- `references/priority-rules.md` for rule priority, conflict handling, and what each file is allowed to decide.
- `references/decision-checklist.md` for the per-item executable judgement checklist. Complete it before deciding.
- `references/pre-submit-audit.md` for the final audit before filling or submitting an answer.
- `references/common-failure-patterns.md` for recurring traps and concrete examples.
- `references/training-summary.md` for video and onboarding conclusions.
- `references/manual-summary.md` for official manual rules.
- `references/quiz-draft.md` when answering or reviewing permission quizzes.
- `references/learned-patterns.md` for user corrections and repeated cases.
- `references/rule-updates.md` for latest rule changes. Read this before older summaries because it may override previous understanding.
- `references/reason-examples.md` for short natural Chinese wording.
- `references/user-style.md` for active wording constraints and the user's historical answer style. Treat explicit punctuation and tone preferences in that file as hard checks.

## Per-Item Execution Contract

Do not rely on memory from the full skill. For every annotation item, follow this short execution contract:

1. Read `references/priority-rules.md` and `references/rule-updates.md` before the first item in a batch.
2. Convert the current task prompt into a 3-8 point current-item checklist using `references/decision-checklist.md`, including the full applicable rule set rather than only the newest correction.
3. Check hard gates and waste/abandon conditions before normal pass/fail or pairwise judgement.
4. Test the prompt-named core functions and visible natural controls.
5. Compare observations against the current-item checklist one point at a time.
6. Draft the reason under the active constraints in `references/user-style.md`, then run `references/pre-submit-audit.md` before filling the final label or reason.
7. Pause if a rule conflict, hidden permission gate, login challenge, CAPTCHA, or destructive action appears.

## Review Flow

1. Complete the Per-Item Execution Contract before deciding the label.
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

1. If `references/user-style.md` contains active wording constraints, such as comma-only punctuation or colloquial wording, treat them as hard checks.
2. If `references/user-style.md` contains historical answers from the user, imitate its sentence length, wording habits, and level of detail.
3. Use `training-summary.md` and `manual-summary.md` to decide which evidence matters for this queue.
4. Use `reason-examples.md` as a backup phrase pool, not as fixed templates.

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

When the user corrects a judgement or wording, update `references/learned-patterns.md`, `references/user-style.md`, or `references/reason-examples.md` with the reusable rule. Keep entries short and general so future labels do not sound copied.
