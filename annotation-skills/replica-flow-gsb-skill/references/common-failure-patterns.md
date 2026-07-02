# Common Failure Patterns

Use these examples to avoid missing recurring rules. Add queue-specific examples as real cases appear.

## Priority Flattening Trap

Situation: One candidate is clearly better on layout, position, size, spacing, first-screen content, module order, or core content, while the other is only better on color, image mood, or a small visual detail.

Judgement: Do not call Same. The higher-priority dimension should decide unless the higher-priority gap is tiny.

Reason pattern: A 的布局和模块顺序更贴参考图，B 只是颜色细节更接近

## Broken Image In Key Content

Situation: A candidate has a broken image, zero-sized image, empty image area, failed avatar, failed product image, failed doctor photo, failed hero image, or visible missing media placeholder.

Judgement: If the broken image is in a key visible area, treat it as a significant element-completeness and visual-restoration defect. In pairwise judging, the other candidate should usually win when it is otherwise judgeable. If the whole preview cannot be judged because of broken rendering, use waste or abandon when the platform supports it.

Reason pattern: B 有关键图片没加载出来，页面完整度明显差一些

## Static Shell Instead Of Function

Situation: The page looks polished, but the prompt-named button, slider, toggle, generator, editor, or scene control does not change anything.

Judgement: Treat the core function as missing or failed, even if the visual design is good.

Reason pattern: 核心控件操作后没有实际反馈，关键功能不可用

## Waste Mistaken For Fail

Situation: The preview is blank, broken, stuck loading, black-screen, white-screen, or cannot be inspected enough to judge.

Judgement: Prefer waste or abandoned when the platform supports it.

Reason pattern: 页面无法正常渲染，无法判断核心内容

## Prompt Ignored

Situation: The candidate provides a generic page or game, but misses the specific object, workflow, comparison target, or interaction named in the prompt.

Judgement: Fail or choose the other candidate when the missing prompt requirement is central.

Reason pattern: 没有体现题目要求的核心内容

## Pairwise Personal Taste Trap

Situation: One candidate looks prettier, but the other follows the prompt and functional requirements better.

Judgement: Choose the candidate that better satisfies the task rubric, not the one that is merely more visually polished.

Reason pattern: 更符合题目要求，核心功能和反馈更完整

## Reason Copying Trap

Situation: A previous reason sounds close but does not match the current visible evidence.

Judgement: Reword from current evidence. Use examples as phrase pools only.

## Function Requirement Overreach

Situation: The prompt only says to replicate the page or convert a sketch into a webpage, but visible buttons, navigation, forms, hover states, or modals appear in the reference.

Judgement: Do not require a real trigger chain unless the prompt explicitly asks for behavior. Judge these as visual elements or reference states.

Reason pattern: 功能不是题目明确要求，主要按视觉还原判断

## Sketch Placeholder Residue

Situation: A sketch task candidate keeps Lorem ipsum, Title, Heading, TODO, Placeholder, gray boxes, crossed image boxes, red annotations, arrows, or handwritten notes.

Judgement: Penalize visual/productization quality. These are not acceptable final webpage content unless the prompt explicitly asks for wireframe style.

Reason pattern: 草图占位内容残留，页面不像完整成品

## Webpage Beauty Trap

Situation: One webpage-replica candidate is prettier as an independent design, but it changes layout, colors, copy, modules, or visual hierarchy away from the reference image.

Judgement: Reference fidelity wins over independent beauty for webpage replica tasks.

Reason pattern: 虽然视觉更精致，但与参考图还原偏差更大

## Flowchart Redraw Trap

Situation: A flowchart task candidate redraws nodes, arrows, swimlanes, or tree diagrams instead of implementing the underlying product workflow.

Judgement: Prefer a candidate that turns the flow into usable forms, steps, dashboards, status cards, result pages, or other real web UI, even if it does not visually resemble the diagram.

Reason pattern: 主要是在重画流程图，缺少真实网页流程

## Flow Semantics Vs Interaction Count

Situation: A candidate has many clickable controls, but misses or misunderstands core nodes, paths, branches, states, inputs, outputs, or constraints from the flowchart.

Judgement: It cannot win by interaction quantity. Flow semantics and key path coverage are higher priority.

Reason pattern: 交互数量较多，但关键流程语义理解错误

## Mock State Missing

Situation: A flowchart includes API, login, payment, notification, submission, or backend-like behavior, but the candidate only shows static text or a button without loading, success, failure, or response feedback.

Judgement: Penalize interaction and state implementation. Front-end mock is acceptable, but visible state progression is required.

Reason pattern: 缺少请求后的状态反馈，流程链路不完整
