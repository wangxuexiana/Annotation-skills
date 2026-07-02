---
name: visual-debug-gsb-rubrics-skill
description: Visual Debug GSB+Rubrics annotation rubric for repair-quality comparison tasks. Use when Codex needs to judge pages with a before-fix webpage, candidate A/B repairs, current reported problem, rubrics scored 1/0/unable-to-judge, A/B 0-5 scores, GSB preference, waste/return handling, and concise Chinese evidence reasons.
---

# Visual Debug GSB+Rubrics

## Goal

Use the bundled manual rules to complete Visual Debug GSB+Rubrics annotation tasks. The core order is: first decide whether the current reported problem is repaired, then check whether the original request or reference image is preserved, then check whether the repair introduced side effects.

Default confirmation policy: ask the user before final questionnaire submission, permission submission, or final annotation submission unless the user explicitly authorizes auto-submit for this queue.

## Required References

Before a batch, read:

- `references/priority-rules.md` for rule priority and conflict handling.
- `references/rule-updates.md` for newest overrides.
- `references/manual-summary.md` for official queue rules.
- `references/decision-checklist.md` for the per-item executable checklist.
- `references/pre-submit-audit.md` before filling rubrics, scores, preference, reason, waste flag, or submitting.
- `references/common-failure-patterns.md` for recurring traps.
- `references/reason-examples.md` and `references/user-style.md` for compact Chinese reasons.
- `references/quiz-draft.md` when answering or reviewing permission quizzes.

## Per-Item Execution Contract

For every annotation item:

1. Read `references/priority-rules.md` and `references/rule-updates.md` before the first item in a batch.
2. Read the visible task fields: current problem, original request, full task description, before-fix page, reference image if present, candidate A, candidate B, and all rubrics.
3. Update `state/current-item.md` with item identity, prompt summary, applicable rule sources, and a 3-8 point current-item checklist.
4. Open the before-fix page to confirm the baseline problem and original normal content.
5. Open A and B separately, test only prompt-named functions and natural visible controls needed for judgement.
6. Compress observations into `state/browser-observation.json`.
7. Score every rubric for A and B as `1`, `0`, or `无法判断`; use `无法判断` only when evidence is insufficient, not when a candidate simply fails.
8. Give A and B 0-5 overall scores based on target repair first, request/reference match second, side effects third.
9. Choose GSB: A better, Same/Tie, or B better. Use Same only when the two sides are substantively close.
10. Draft a short Chinese reason with 1-2 locatable evidence points, then run `references/pre-submit-audit.md`.
11. Append the compact outcome to `state/batch-log.md`.
12. Pause for login, CAPTCHA, permission gates, rule conflicts, inaccessible key evidence, or final submission unless explicitly authorized.

## Returned And Waste Flow

Returned or rework tasks require reading the top return comment first. Do not only rewrite the reason; re-check rubrics, A/B scores, preference, and reason against the return comment.

Waste is reserved for items that truly cannot be judged, such as missing key input, both A/B links inaccessible, or severe task data abnormality. A poor candidate, a local defect, or one broken non-core image is usually scored rather than wasted.

## Stable Rules

Read the shared generic rules first:

- `../annotation-workflow-skill/references/stable-annotation-rules.md`

Task-specific manuals, `references/rule-updates.md`, and explicit user corrections override shared generic rules when they clearly conflict.

## Reason Style

Reasons must be short but reviewable, usually 1-3 sentences. Name concrete modules, buttons, images, navigation, cards, hero area, forms, menus, theme switch, mobile layout, popups, route changes, or other visible evidence. Avoid empty claims such as `更好看`, `不错`, `差不多`, `都可以`, or `无`.

## Quiz Flow

When answering a permission quiz:

1. Use only `training-summary.md`, `manual-summary.md`, and visible quiz/training evidence.
2. Draft each answer with evidence and confidence.
3. Ask the user to confirm before clicking final submit.
4. If feedback reveals a wrong assumption, update `learned-patterns.md` or `rule-updates.md`.

## Skill Evolution

When the user corrects a judgement or wording, update `references/learned-patterns.md`, `references/rule-updates.md`, `references/user-style.md`, or `references/reason-examples.md` with the reusable rule. Keep one-off task details in `state/batch-log.md`.

