---
name: flowchart-web-function-eval-skill
description: Task-specific annotation rubric generated from the Feishu manual and recording for flowchart-based webpage function evaluation. Use when Codex needs to label this queue in Chrome by checking prompt, reference flowchart, modelA interactions, rubric 1/0 labels, overall 0-10 score, screenshot correctness, waste rules, and concise Chinese reasons.
---

# Flowchart Web Function Eval Skill

## Goal

Use the bundled training summary and manual rules to complete this flowchart webpage function-evaluation queue. Judge every rubric independently as `1/0`, assign an integer overall functionality score from `0-10`, and judge whether `modelA_img` matches the actual initial loaded `modelA` page before any interaction.

If recording/video training rules conflict with the written manual, follow the recording. Current recording overrides live in `references/rule-updates.md`.

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
2. Read the current page prompt and update `state/current-item.md` with the item type, applicable rule sources, and prompt summary.
3. Convert the current task prompt into a 3-8 point current-item checklist using `references/decision-checklist.md`, including the full applicable rule set rather than only the newest correction.
4. Compress browser testing into `state/browser-observation.json`; do not keep long DOM dumps, long accessibility snapshots, or repeated screenshot descriptions in chat.
5. Check hard gates and narrow waste/abandon conditions before normal rubric judgement.
6. Test every rubric that requires interaction, routing, decision logic, validation, submission, filtering, modal display, or flow completion.
7. Compare observations against the current-item checklist one point at a time, then judge all rubric labels, the overall score, and screenshot correctness.
8. Write the draft rubric labels, reasons, overall score, screenshot label, and audit notes back to `state/current-item.md`, then append the outcome to `state/batch-log.md`.
9. Draft reasons under the active constraints in `references/user-style.md`, then run `references/pre-submit-audit.md` before filling final fields.
10. Pause if a rule conflict, hidden permission gate, login challenge, CAPTCHA, destructive action, or unresolved uncertainty appears.

## Context Budget Contract

Keep the live chat context small and recoverable:

- Store per-item working state in `state/current-item.md`, not in long chat narration.
- Store browser observations in `state/browser-observation.json` using the fixed schema from the state template.
- Store reusable user corrections in `state/corrections.md` before merging them into references with `update_task_skill.py --from-correction-log`.
- Store unresolved blockers in `state/pending-uncertainties.md`.
- Use screenshots only as evidence pointers; summarize what matters instead of retaining large visual descriptions.
- After context compaction or a new session, restore from `state/current-item.md`, `state/batch-log.md`, `state/pending-uncertainties.md`, `references/priority-rules.md`, and `references/rule-updates.md`.

## Review Flow

1. Complete the Per-Item Execution Contract before deciding the label.
2. Do not process returned/rework tasks unless the user explicitly asks.
3. Read the task prompt and extract the core requirement before testing.
4. Open `modelA` in a separate new Chrome tab/window.
5. Test prompt-named core functions and every rubric-named interaction.
6. Close the test tab/window after testing.
7. Return to the original task page and fill waste/abandon status, rubric labels and reasons, overall score, screenshot correctness, and any required notes.
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
