# Common Failure Patterns

Use these examples to avoid missing recurring rules. Add queue-specific examples as real cases appear.

## Function Counted In Visual GSB

Situation: A candidate has broken or missing interactions, and that functional defect is used to decide the visual-only GSB.

Judgement: Do not include function behavior in 仅视觉 GSB. Use function behavior only for function rubrics and 整体 GSB when the prompt or function rubrics require it.

Reason pattern: 仅视觉只看视觉质量，功能问题放到整体判断里

## Function Judged From Screenshot

Situation: The answer marks a function rubric from the screenshot without opening and operating the HTML.

Judgement: Invalid for RL Trace. Function rubrics must be verified through actual operation unless blocked by login, permission, external service, or unclear rubric.

Reason pattern: function 需要打开 HTML 实测，截图不能证明交互可用

## Invented Function Requirement

Situation: A page contains buttons, navigation, inputs, or cards, but the prompt only asks for visual restoration or layout.

Judgement: Do not infer a function requirement from visible controls alone. Mark explicit function requirement as 否 unless prompt or function rubrics require interaction.

Reason pattern: UP 没有明确功能要求，页面有按钮也不单独评功能

## Feedback Words Missed

Situation: The prompt says `自然反馈`, `交互反馈`, `状态反馈`, `正常作业`, or `正常运行`, but the item is treated as pure visual.

Judgement: These words count as function requirements and require HTML operation.

Reason pattern: prompt 要求反馈或正常运行，需要实际操作验证

## Sketch Copied As Wireframe

Situation: In a sketch task, the candidate preserves wireframe style, Lorem ipsum, Placeholder, gray blocks, arrows, comments, or annotation marks.

Judgement: Treat this as a visual/productization defect. A sketch task should become a real high-fidelity webpage.

Reason pattern: 草图没有产品化，还保留占位和线框痕迹

## Replication Made Prettier But Less Similar

Situation: In a replication task, one candidate is visually polished but less faithful to the reference image in layout, element completeness, content, or proportions.

Judgement: Prefer the candidate closer to the reference image. Do not reward unrelated beautification over restoration accuracy.

Reason pattern: 复刻任务看接近参考图，不看单纯更好看

## Hallucinated Extra Modules

Situation: A replication candidate adds large modules, ads, popups, unrelated navigation, unrelated images, or content not present in the reference.

Judgement: Treat as hallucination or restoration defect, especially if it changes first-screen content or core structure.

Reason pattern: 新增了参考图没有的大模块，影响复刻准确性

## Static Shell Instead Of Function

Situation: The page looks polished, but the prompt-named button, slider, toggle, generator, editor, filter, sort, tab, popup, carousel, form, navigation, or flowchart interaction does not change anything.

Judgement: Treat the core function as missing or failed, even if visual design is good.

Reason pattern: 核心控件操作后没有实际反馈，关键功能不可用

## Waste Mistaken For Fail

Situation: The screenshot or HTML is blank, broken, stuck loading, white-screen, black-screen, inaccessible, or cannot be inspected enough to judge.

Judgement: For RL Trace, if either screenshot or HTML cannot open, mark waste and add a note.

Reason pattern: 关键材料打不开，无法完成标注判断

## Reason Copying Trap

Situation: A previous reason sounds close but does not match the current visible evidence.

Judgement: Reword from current evidence. Use examples as phrase pools only.
