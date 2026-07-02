# Priority Rules

Use this file to decide which rule wins and how to compare A/B for Visual Debug GSB+Rubrics.

## Rule Priority

Apply rules in this order:

1. Current explicit user instruction in the chat.
2. User correction for this queue.
3. `references/rule-updates.md`.
4. Current visible platform instruction or updated official manual.
5. `references/manual-summary.md`.
6. `references/training-summary.md`.
7. `references/learned-patterns.md` when it matches the same situation.
8. `../annotation-workflow-skill/references/stable-annotation-rules.md`.
9. General judgement only when no task-specific rule exists.

## VisualDebug Judgement Priority

For each candidate and for A/B preference, apply this order:

1. Current reported problem repair.
2. Original request or reference image match.
3. Side effects and page stability.
4. Minor polish, color mood, or small local details.

Do not let visual prettiness, larger edits, or lower-priority polish outrank a clearly better current-problem repair.

## File Roles

- `rule-updates.md`: newest active overrides. This can change judgement.
- `manual-summary.md`: official task rules. This can change judgement.
- `training-summary.md`: distilled onboarding rules. This can change judgement unless a newer file conflicts.
- `learned-patterns.md`: reusable corrections and repeated cases. This can change judgement only when the same pattern appears.
- `common-failure-patterns.md`: examples that make abstract rules concrete. Use as analogies, not fixed labels.
- `reason-examples.md`: wording support only. It must not change the label.
- `user-style.md`: wording style only unless the user explicitly says a historical rule transfers.

## Conflict Handling

- If a newer task-specific rule conflicts with an older summary, follow the newer rule.
- Treat new user corrections as guardrails inside the full rubric, not replacements for all other applicable rules.
- Do not overfit to the newest correction, and do not underfit by skipping older official rules that still apply.
- If a conflict changes the current label, pause and mention the conflict before submitting.
- If only the reason wording is affected, follow `user-style.md` and keep judging from task rules.

## Output Consistency

- Rubric values, A/B scores, GSB preference, and reason should generally agree.
- If they do not agree, the reason must explain the exception, such as a low rubric count but severe side effect, or an important repair not captured by one rubric.
- Same/Tie is narrow. Use it only when target repair, requirement/reference match, and side effects are close enough that a quality gap is not reliable.

