# Common Failure Patterns

Use these examples to avoid missing recurring Visual Debug scoring traps.

## Abandon Mistaken For 0

Situation: The prompt claims a pre-repair defect exists, but the pre-repair output never had that defect, or the task has Prompt/reference mismatch, abnormal reference image, wrong screenshot order, or missing key information.

Judgement: Abandon. Do not force a 0/1/2 score for an invalid task.

Reason pattern: 题目本身不成立，问题描述和修复前产物对不上

## 0 Mistaken For Abandon

Situation: The task is valid, but the repaired webpage is stuck loading, unviewable, or the core problem is still not fixed.

Judgement: Score 0. Page load failure in the repaired output and failed repair are normal 0-point cases in this manual.

Reason pattern: 页面无法正常加载，无法判断修复效果

## Repair-Only 2 Point Trap

Situation: The prompt-described problem is fixed, but the page still differs obviously from the reference image in layout, module order, content, spacing, size, or visual style.

Judgement: Score 1, not 2. Repair completion alone is insufficient for 2 points.

Reason pattern: 问题已修复，但和参考图差异明显

## Pretty But Not Fixed

Situation: The repaired page looks polished, but the exact defect described by the problem remains.

Judgement: Score 0. Core repair completion outranks overall polish.

Reason pattern: 页面观感可以，但核心问题没有修好

## UP Instruction Missed

Situation: The page is close to the reference image, but a corresponding UP instruction or explicit repair requirement is not fully implemented.

Judgement: Do not score 2. Usually score 1 if the main problem is fixed but implementation is incomplete.

Reason pattern: 主问题已修复，但指令没有完全实现

## Multiple 2-Point Candidates

Situation: More than one candidate appears to satisfy the 2-point conditions.

Judgement: Compare repair completion and reference fidelity; only the best candidate keeps 2 points, and all other 2-point candidates become 1 point.

Reason pattern: 同题只能保留最佳 2 分，其他高质量候选降为 1 分

## Partial-Page Inspection

Situation: The first screen looks correct, but lower page sections contain missing modules, wrong order, broken assets, or major style differences.

Judgement: Inspect from first screen to bottom before scoring. Lower-page defects can reduce a candidate from 2 to 1 when they hurt reference fidelity.

Reason pattern: 首屏修复可以，但下方内容和参考图不一致
