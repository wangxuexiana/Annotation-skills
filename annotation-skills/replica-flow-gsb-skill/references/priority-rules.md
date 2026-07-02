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

- If a newer task-specific rule conflicts with an older summary, follow the newer rule.
- If a conflict changes the current label, pause and mention the conflict before submitting.
- If only the reason wording is affected, follow `user-style.md` and keep judging from task rules.

## Queue-Specific Priority Stack

First classify the task as sketch-to-webpage, webpage-replica, or flowchart-to-webpage.

Sketch-to-webpage priority:

1. Prompt explicit requirements.
2. Layout restoration against the sketch.
3. Realistic content filling instead of placeholders.
4. Productized high-fidelity webpage completion.
5. Prompt-specified brand, style, color, industry, and state.
6. Explicit prompt-named functions and interactions.

Webpage-replica priority:

1. Prompt explicit requirements.
2. Reference image fidelity: layout, position, size, spacing, first-screen content.
3. Element completeness and content accuracy.
4. Visual restoration details.
5. Hallucination control.
6. Explicit prompt-named functions and interactions.

Flowchart-to-webpage priority:

1. Flow semantics: nodes, paths, branches, states, inputs, outputs, constraints.
2. Web productization: real UI/application, not redrawn flowchart.
3. Interaction and state chain: actions, validation, loading, success, failure, mock feedback.
4. Information architecture and next-action clarity.
5. Visual completion and local polish.

## Function Requirement Boundary

- Explicit behavior in the prompt makes function testing mandatory.
- A visible button, form, hover state, modal, or selected state in the reference is not enough by itself to require a trigger chain.
- Extra unrequested functionality does not improve the label.
- Extra functionality that damages restoration, flow clarity, or relevance is negative.
