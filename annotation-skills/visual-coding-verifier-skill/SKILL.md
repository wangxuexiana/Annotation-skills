---
name: visual-coding-verifier-skill
description: Task-specific annotation rubric generated from Feishu training materials and annotation manuals. Use when Codex needs to judge, compare, or label this queue's tasks in Chrome using the distilled training rules, permission-quiz evidence, learned patterns, and user-preferred reason style.
---

# Visual Coding Verifier Skill

## Goal

Complete this specific chart-reproduction annotation queue using task-specific rules before generic annotation habits.

Default confirmation policy: ask the user before final questionnaire submission, permission submission, or final annotation submission unless the user explicitly authorizes auto-submit for this queue.

## Pre-Judgement Checklist

Before every annotation item or batch, do this short checklist. Treat it as mandatory, not background reading.

1. Read `references/rule-updates.md` first.
2. Read only the needed supporting files: `training-summary.md` and `manual-summary.md` for normal tasks, `quiz-draft.md` for permission quizzes, `learned-patterns.md` and `user-style.md` when judging or writing reasons.
3. Identify the item type: normal rubrics task, pairwise task, returned or rework task, permission quiz, inaccessible page, or broken preview.
4. Skip returned or rework tasks unless the user explicitly asks to handle them.
5. Compare the target image against both generated images using visible evidence only.
6. For O1, judge chart type, special variant, and high-level intent only. Keep O1 lenient and do not penalize data, label overlap, crop, color, or typography unless the O1 rubric explicitly makes that the intent.
7. For O2, strictly compare data and core chart elements: values, positions, trends, axes, ranges, labels, legends, ticks, order, coordinate logic, and readability of semantic elements.
8. For O3, strictly compare layout and visual style: typography, text color or stroke, colors, line or mark thickness, spacing, margins, crop, overlap, viewpoint, legend placement, grid style, and overall proportions.
9. Give O2=4 or O3=4 only when that dimension has no obvious visible mismatch.
10. Before filling reasons, check that every non-full reason names a concrete defect and where it appears, and that submitted reasons use Chinese commas only when punctuation is needed.

## Reference Order

Use the smallest set of references needed for the current task:

- `references/rule-updates.md`: active overrides. Read before older summaries.
- `references/training-summary.md`: queue structure, O1/O2/O3 definitions, pairwise rules.
- `references/manual-summary.md`: official manual summary.
- `references/learned-patterns.md`: reusable user corrections and repeated cases.
- `references/user-style.md`: user-preferred reason wording. Follow this before generic examples.
- `references/reason-examples.md`: backup phrase pool only.
- `references/quiz-draft.md`: permission quiz evidence and draft answers.
- `../annotation-workflow-skill/references/stable-annotation-rules.md`: shared generic rules. Task-specific files override it.

If references conflict, follow this priority:

1. Explicit current user instruction.
2. `references/rule-updates.md`.
3. `references/learned-patterns.md` and `references/user-style.md`.
4. `training-summary.md` and `manual-summary.md`.
5. Shared stable annotation rules.

## Normal Task Flow

1. Read the visible prompt, target image, generated image 1, generated image 2, and the provided O1/O2/O3 rubrics.
2. Check whether the machine-provided rubrics correctly describe the target image. Repair inaccurate or severely incomplete rubrics before scoring.
3. Score image 1 and image 2 independently on O1, O2, and O3. Do not let one image's quality influence the other's pointwise scores.
4. For pairwise tasks, choose the image that is more like the original, more trustworthy, and more usable as a chart reproduction. Do not mechanically sum O1/O2/O3.
5. Use chart type first, data accuracy second, and visual style as a tiebreaker unless a visible issue is severe enough to change usability.
6. Choose `打平` only when careful detail checking leaves no meaningful winner.
7. Fill reasons in the user's style, then pause before final submission unless auto-submit is explicitly authorized.

## Dimension Guardrails

### O1

- O1 is about chart type, special chart variant, and high-level intent.
- Keep O1 broad and lenient. A generated line chart can receive high O1 when it preserves the line-chart variant and intent, even if its values or trends are wrong.
- Do not lower O1 for data errors, value differences, label overlap, crop, color, typography, general layout, or style defects unless the O1 rubric explicitly says those define the chart intent.
- O1 reasons should be one concise line.

### O2

- O2 is about data, mapping, and important semantic chart elements.
- Compare visible numbers, bar heights, point positions, curve shapes, error bars, extrema, ranges, axes, tick labels, legends, category order, units, and readability.
- Lower O2 for wrong values, shifted or swapped data, missing important labels, hallucinated text, unreadable semantic labels, missing legend or units, or coordinate logic errors.
- Do not hide large data errors behind an overall-similarity judgement.

### O3

- O3 is about spatial layout and visual style.
- Check typography, text fill or stroke, font weight, shadows or halos, color palette, mark thickness, line width, point style, gridlines, margins, crop, overlap, legend placement, panel layout, and spacing.
- Lower O3 for obvious style or layout mismatch even when O1 and O2 are strong.
- Do not give O3=4 merely because the chart type, labels, values, or geometry are correct.

## Reason Style

Follow `references/user-style.md` first when it has relevant preferences or historical answers.

Reason rules:

- Write natural Chinese.
- Keep O1 to one concise line.
- O2 and O3 may use up to three short lines when several subpoints matter.
- For non-full O2 or O3, state the concrete mismatch. Avoid meta phrases such as `不能给满分`.
- Point to the visible location using color, layer order, chart component, position, direction, or affected mark.
- Prefer Chinese position or group descriptions over long English label lists when that is unambiguous.
- Use English labels only when label text itself is wrong or needed to avoid ambiguity.
- In submitted reason fields, do not use quotation marks, brackets, parentheses, colons, semicolons, slashes, dashes, or final periods. Use Chinese commas only when punctuation is needed.

## Broken Or Inaccessible Items

Follow the shared stable annotation rules unless this queue says otherwise:

- Blank, black-screen, white-screen, broken, or unrenderable previews are waste or abandoned when the platform supports that label.
- If a preview cannot be inspected enough to judge the core task, prefer waste or abandoned over normal scoring.
- Do not bypass login, CAPTCHA, access control, risk checks, hidden permission gates, or restricted pages.

## Quiz Flow

When answering a permission quiz:

1. Use only `training-summary.md`, `manual-summary.md`, `quiz-draft.md`, and visible quiz or training evidence.
2. Draft each answer with evidence and confidence.
3. Ask the user to confirm before clicking final submit.
4. If feedback reveals a reusable wrong assumption, update `learned-patterns.md`.

## Skill Evolution

When the user corrects a judgement or wording:

- Add reusable judgement rules to `references/learned-patterns.md`.
- Add reusable wording preferences to `references/user-style.md` or `references/reason-examples.md`.
- Add urgent active overrides to `references/rule-updates.md`.
- Keep entries short, general, and non-duplicative so future labels do not sound copied.
