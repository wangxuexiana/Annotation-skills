# VLM VisualDebug GSB Manual Summary

## Official Manual Scope

The manual evaluates VisualDebug final repair artifacts. Annotators compare two model repairs against the task prompt, reference image, and before-fix page.

## Pairwise GSB Judgement

Use GSB labels only:

- `A good B`: A is better than B.
- `A bad B`: B is better than A.
- `A same B`: A and B are similar overall, both good, or both bad.

Selection rules:

- Choose A when A fixes the target problem more clearly, or after fixing it has better restoration or usability.
- Choose B when B fixes the target problem more clearly, or after fixing it has better restoration or usability.
- Choose Same when both are close, both fix with tiny differences, or both fail to a similar degree.

## Priority Rules

1. Target problem repair is highest priority.
2. Restoration to reference image or completion of prompt requirement is second priority.
3. Side effects are third priority and can outweigh a partial repair when severe.

Side effects include white screen, broken opening, important content missing, severe layout shift, visual obstruction, and failed interaction.

## Explicit Visual Repair Dimensions

### V1 Specified Visual Problem Repair

- 5: manual issue fully repaired with no visible residue.
- 4: main issue repaired with only tiny residue.
- 3: obvious improvement but issue remains visible.
- 2: only a small part repaired and core issue remains.
- 1: basically not repaired or repaired in the wrong direction.
- 0: white screen, cannot open, or main content invisible.

### V2 Reference Image Restoration

- 5: layout, proportion, spacing, color, font, images, and core content are highly close to reference.
- 4: overall close with minor local detail differences.
- 3: structure basically correct, but color, font, spacing, or local content differs obviously.
- 2: main elements exist, but layout proportion is messy and visual distance is large.
- 1: only rough content remains and the page does not look like reference.
- 0: unrelated to reference or no effective page content.

### V3 Visual Side Effects

- 5: repair does not damage other areas.
- 4: only slight local degradation.
- 3: visible side effects that do not affect core judgement.
- 2: important area becomes shifted, blocked, missing, or clearly degraded.
- 1: serious new problem and overall quality drops significantly.
- 0: white screen, cannot open, or main content unusable.

## Open Visual Repair Dimensions

### O1 Main Visual Difference Discovery And Repair

- 5: actively repairs the most important restoration differences with reasonable priority.
- 4: repairs most major differences, missing only minor issues.
- 3: repairs some obvious differences but misses important problems.
- 2: handles only small local issues while major differences remain.
- 1: finds almost no effective issue or changes in the wrong direction.
- 0: white screen, cannot open, or main content invisible.

### O2 Overall Visual Restoration

- 5: layout, core blocks, and visual hierarchy are very close to reference.
- 4: overall close with only small detail inconsistency.
- 3: large structure is correct, but multiple areas differ obviously.
- 2: most elements exist, but layout, proportion, or hierarchy is obviously wrong.
- 1: only a few similar elements remain and visual distance is large.
- 0: unrelated to reference or no effective content.

### O3 Open Repair Side Effects

- 5: repairs main differences without damaging the original page.
- 4: slight side effects but gain clearly outweighs loss.
- 3: repair and side effects coexist, overall improvement is limited.
- 2: damages other important areas while fixing local problems.
- 1: the page is worse than before repair.
- 0: white screen, cannot open, or main content unusable.

## Functional Or Interaction Repair Dimensions

### F1 Target Function Repair

- 5: target function is fully usable and key path matches prompt.
- 4: target function is basically usable with only minor edge issues.
- 3: function improves, but some steps or states remain incorrect.
- 2: only surface symptom is fixed while core function remains unusable.
- 1: basically not repaired or wrong repair direction.
- 0: white screen, cannot open, or target operation cannot be performed.

### F2 Functional Completeness

- 5: related buttons, routes, forms, data, and state feedback all satisfy requirements.
- 4: main path is complete with only minor non-core state or boundary defects.
- 3: core path can run, but feedback, data update, or local state still has issues.
- 2: only part of the operation can be completed and later state/result is wrong.
- 1: page appears to change but actual functional flow is basically unusable.
- 0: no effective page or cannot operate.

### F3 Functional Side Effects

- 5: after target function repair, original page and other interactions remain normal.
- 4: only slight visual or non-core interaction degradation.
- 3: some side effects exist but do not affect the target function's main path.
- 2: target repair breaks other important function or main UI.
- 1: serious new problem and overall usability drops significantly.
- 0: white screen, cannot open, or main function unusable.

## Reason Requirements

Reasons must first state the overall judgement, then provide one or two locatable facts. Valid evidence includes target problem repair, restoration/requirement completion, and side effects.

Bad reasons are broad claims without evidence, such as only saying "更好看", "更完整", or "更符合要求".

## Manual Case

In the contact-page case, the target issues are navigation bar height and input background color. The better side is the one that repairs the input background color while both sides repair the navigation height. The example conclusion is B wins because B fixes the input background issue and both sides repair the navigation issue.
