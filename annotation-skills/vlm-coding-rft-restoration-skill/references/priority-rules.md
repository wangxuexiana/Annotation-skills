# Priority Rules

Use this file to decide which rule wins and what each reference file is allowed to influence.

## Rule Priority

Apply rules in this order:

1. Current explicit user instruction in the chat.
2. User correction for this queue.
3. `references/rule-updates.md`.
4. Current official manual or visible platform instruction.
5. `references/manual-summary.md`.
6. `references/training-summary.md`.
7. `references/learned-patterns.md` when it matches the same situation.
8. `../annotation-workflow-skill/references/stable-annotation-rules.md`.
9. General judgement only when no task-specific rule exists.

## File Roles

- `rule-updates.md`: newest active overrides. This can change judgement.
- `manual-summary.md`: official task rules. This can change judgement.
- `training-summary.md`: distilled onboarding rules. This can change judgement unless a newer file conflicts.
- `learned-patterns.md`: reusable corrections and repeated cases. This can change judgement only when the same pattern appears.
- `common-failure-patterns.md`: examples that make abstract rules concrete. Use as analogies, not fixed labels.
- `reason-examples.md`: wording support only. It must not change the label.
- `user-style.md`: wording style only unless the user explicitly says a historical rule transfers.

## Conflict Handling

- UP instruction overrides the reference image only when it explicitly changes page layout, style, interaction, or target state.
- The 2-point rule is procedural and hard: a product must qualify for 1 before it can be promoted to 2, and only one best product can receive 2.
- The manual discard case is narrow: prompt and reference image do not correspond, while the product follows the prompt.
- If a newer task-specific rule conflicts with an older summary, follow the newer rule.
- Treat new user corrections as guardrails inside the full rubric, not replacements for all other applicable rules.
- Do not overfit to the newest correction, and do not underfit by skipping older official rules that still apply.
- If a conflict changes the current label, pause and mention the conflict before submitting.
- If only the reason wording is affected, follow `user-style.md` and keep judging from task rules.
