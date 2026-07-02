# Priority Rules

Use this file to decide which rule wins for Coding美观度 pairwise SingleImage.

## Rule Priority

Apply rules in this order:

1. Current explicit user instruction, unless it asks to bypass platform policy or hidden gates.
2. Visible platform instruction on the current task page.
3. `references/rule-updates.md`.
4. Official manual rules in `references/manual-summary.md`.
5. Distilled workflow in `references/training-summary.md`.
6. Reusable user corrections in `references/learned-patterns.md` when the same situation appears.
7. Shared stable rules from `../annotation-workflow-skill/references/stable-annotation-rules.md`, only when they do not conflict with screenshot-only aesthetic rules.
8. General judgement only when no task-specific rule exists.

## Queue-Specific Overrides

- Screenshot-only wins over generic browser testing. Do not test interactions or functional completeness for this queue.
- Waste judgement happens before `-1 / 0 / 1`.
- Fatal visible defects outrank minor aesthetic taste differences.
- Scenario fit outranks personal style preference.
- Ambitious, rich, coherent execution can outrank sparse "no obvious error" pages.
- Same is valid when differences are genuinely small or problem severity is comparable, but do not use Same when one side clearly wins on fatal defects, core readability, layout hierarchy, material completeness, or scenario fit.
- The manual's AI-use warning is a submission gate. Do not secretly auto-score or auto-submit.

## File Roles

- `rule-updates.md`: newest active overrides.
- `manual-summary.md`: official rules and label definitions.
- `training-summary.md`: concise workflow and common traps.
- `decision-checklist.md`: per-item execution steps.
- `common-failure-patterns.md`: examples and analogies, not fixed labels.
- `learned-patterns.md`: reusable user corrections.
- `reason-examples.md`: wording support only.
- `user-style.md`: style and punctuation constraints.

## Conflict Handling

- Follow newer task-specific rules over older summaries.
- Use user corrections as guardrails inside the full rubric, not replacements for the rubric.
- If a conflict changes a label, pause before submission and explain the conflict.
- If only wording is affected, follow `user-style.md` without changing the label.
