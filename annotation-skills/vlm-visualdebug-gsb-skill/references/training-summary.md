# VLM VisualDebug GSB Training Summary

## Task Type And Target Queue

- Queue: RFT人标支持 GSB 评估 - VLM VisualDebug, task id `7639212583757991730`.
- Task type: pairwise GSB comparison for VisualDebug final repair artifacts.
- Inputs to inspect: task requirement, reference image, before-fix page, and two after-fix model pages.
- Goal: judge which repaired page better solves the visual or functional issue while preserving page usability.

## Core Decision Order

Always judge in this order:

1. Target problem fixed: the side that better fixes the named or discoverable core issue has priority.
2. Restoration or requirement completion: when both fix the target issue, compare closeness to the reference image or prompt requirement.
3. Side effects: penalize white screen, broken opening, serious layout shift, missing content, interaction failure, or new visible regressions caused by the repair.
4. Same is allowed: use Same when both are similarly good, similarly bad, or differences do not affect the core target.

## Question Types

- V1/V2/V3 explicit visual repair: the prompt states the visual issue; check whether that issue is fixed.
- O1/O2/O3 open visual repair: the prompt does not name the exact issue; check whether the model discovered and repaired major visual differences.
- F1/F2/F3 functional or interaction repair: the prompt names a function or interaction; check whether the target function works and the page stays usable.

## GSB Labels

- `A good B`: A is better than B.
- `A bad B`: B is better than A.
- `A same B`: A and B are close overall, equally good, or equally bad.

## Single Artifact 0/1/2 Mapping

- `0`: target problem not fixed, or page is white screen, cannot open, or main content is seriously abnormal.
- `1`: target problem is basically fixed, but restoration is average, functional flow is incomplete, or there are obvious side effects.
- `2`: target problem is fixed, restoration or requirement completion is good, and there are no obvious side effects.

## Browser Test Flow

1. Read the task prompt and identify whether it is explicit visual, open visual, or function/interaction repair.
2. Open reference image, before-fix page, A page, and B page as needed.
3. Compare the target issue first, then restoration/completion, then side effects.
4. For function tasks, test only the prompt-named core path and natural visible controls.
5. Check that key visible images and main content render.
6. Close test tabs and return to the task page.
7. Fill only the final GSB label and a compact evidence-based reason.

## Waste Or Abandon Rules

- A page that is white screen, cannot open, or has no usable main content is a severe failure for that side.
- If both sides are white screen or unusable to a similar degree, choose Same when the platform only offers GSB labels.
- Do not mark a normal lower-quality but visible repair as waste if GSB comparison is possible.

## Easy-To-Misjudge Cases

- Do not choose a side for minor polish when the other side is the only one that actually fixed the target issue.
- Do not ignore serious new side effects merely because the target issue improved.
- Do not flatten to Same when one side clearly has better target repair or functional completion.
- Do not overvalue color or small style details over layout, missing content, target repair, and core function.
- For function repair, visual similarity alone is not enough if the prompt-named function still fails.

## Reason Style

- Start with the overall judgement, then give one or two concrete pieces of evidence.
- Avoid empty phrases like "更好看", "更完整", or "更符合要求" without locating the evidence.
- Preferred evidence types: target issue fixed, restoration/requirement completion, or side effects.
- Natural Chinese reasons are preferred. Historical examples use colloquial wording such as "进行啦修复"; preserve that style when the user wants it.

## Quiz Facts Likely To Be Tested

- The priority order is target fix, restoration/completion, then side effects.
- GSB labels are A good B, A bad B, and A same B.
- Same is valid when both sides are close, equally good, or equally bad.
- Reasons must include concrete evidence, not only broad praise.
- White screen, cannot open, or invisible main content is a severe failure.
