# Common Failure Patterns

Use these examples to avoid recurring Visual Debug GSB+Rubrics traps.

## Treating Aesthetic Polish As Repair

Situation: A candidate looks cleaner or prettier, but the current reported problem remains.

Judgement: Target problem repair has priority. Do not give a high score or choose the prettier side when the core issue is not repaired.

Reason pattern: A 先修好了当前问题，B 虽然整体更顺眼，但目标区域的问题还在。

## Marking Failure As Unable To Judge

Situation: A candidate is accessible and visibly fails a rubric, but the draft marks `无法判断`.

Judgement: Mark `0`. Use `无法判断` only when evidence is truly insufficient.

Reason pattern: 该功能点击后没有真实状态变化，可以确认未满足 rubric，不应标无法判断。

## Rubric Pass Rate Average Trap

Situation: A side passes more minor rubrics but fails the current reported problem, while the other fixes the core issue.

Judgement: Overall score is not a simple pass-rate average. Core repair usually controls the score ceiling.

Reason pattern: B 的 rubric 通过项更多，但当前要修的问题仍未解决，整体不能高于 A。

## Hover Or Animation Mistaken For Function

Situation: A button has hover style or animation, but click/input does not produce a real state change or result.

Judgement: Treat the function as not repaired.

Reason pattern: B 的按钮只有 hover 效果，点击后没有实际反馈，目标交互没有修好。

## Side Effect Hidden By Partial Fix

Situation: A candidate fixes the target issue but introduces serious layout shift, content loss, visual obstruction, unreadable text, or broken interaction.

Judgement: Penalize the side effect. Choose the other side if its repair is close and side effects are lighter.

Reason pattern: A 虽然修了目标问题，但把下方卡片挤压错位，B 的副作用更轻。

## Same Used Too Broadly

Situation: Both sides have some defects, but one side clearly wins on target repair, request/reference match, or side-effect control.

Judgement: Do not choose Same just because both sides are imperfect.

Reason pattern: 两边都有小问题，但 A 修复了目标问题，B 的核心错误仍明显，所以不能选 Same。

## Over-Wasting

Situation: One non-core image is broken, or one candidate is poor, but enough evidence exists to score the task.

Judgement: Do not waste. Score the visible candidate quality and mention the defect if relevant.

Reason pattern: A 的局部图片未加载，但主体和目标交互仍可判断，应按实际修复质量评分。

## Returned Task Reason Only

Situation: A returned item has a quality comment, and the agent only rewrites the reason.

Judgement: Re-check rubrics, scores, preference, and reason. The return comment may change the actual label.

Reason pattern: 根据返修意见重新检查后，B 的移动端菜单仍无法展开，rubric 和偏好都需要同步调整。

## Empty Reason

Situation: The reason says only `更好看`, `感觉不错`, `差不多`, `都可以`, or `无`.

Judgement: Rewrite with one or two locatable evidence points.

Reason pattern: A 的移动端菜单能展开并显示完整导航，B 点击菜单无反应，所以 A 更好。

