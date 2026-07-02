# Manual Summary

Source: https://bytedance.larkoffice.com/wiki/CMUww2CzIimYe6kdTlgclKVxnjh

Manual title: `「场景GSB丨评测GSB」Webdev-GSB标注手册丨OnePage`

## Online Queues

- `场景GSB-试标`: `7649606298007621414「场景GSB」试标队列-webdev场景GSB-严格备注丨0610`
- `评测GSB`: `7649344261260283699「评测GSB」webdev评测GSB-严格备注丨0610`

## Core Priority By Scene Type

The manual says the core basis for judging the three dimensions depends on the Web scene type:

- Game scenes: mainly judge functional completeness and functional defects. For games, `功能缺陷` has higher priority than `美观度`.
- UI scenes: mainly judge functional completeness and aesthetics. For UI outputs, `美观度` has higher priority than `功能缺陷`.

## Dimension Definitions

### 功能完整度

Main question: whether the prompt is implemented completely, especially whether all prompt-described function points are present.

Judgement points:

- Use functions explicitly described in the prompt as the core basis.
- General features not mentioned in the prompt are not considered by default.
- If the prompt explicitly requires a tab click to route or jump, but clicking has no response, this is a functional-completeness problem.

### 功能缺陷

Main question: whether prompt functions and model-implemented functions contain bug-like defects.

Judgement points:

- Focus on actual failure phenomena in implemented functions, such as unresponsive buttons and failed image loading.
- If the prompt did not explicitly require a click function, but the model implemented a clickable element and it has no response, this is a functional-defect problem.
- Image loading failure belongs to functional defects.

### 美观度

Main question: whether the produced page has unreasonable layout or style.

Judgement points:

- Do not over-scrutinize tiny details. Pay attention to the overall visual impression.
- For UI products, if the overall visual impression is good, basic needs are satisfied, and there are no multiple or major interaction defects, the aesthetics side can pass.

## Waste Handling

The manual explicitly changes normal waste handling:

- For all queues in this task, data that needs to be abandoned should not receive a waste tag.
- The remark must describe the A/B waste reason.
- Waste pairs still participate in GSB evaluation.

Pairwise judgement:

- A waste and B normal: judge `A < B`.
- A waste and B waste: judge `A = B`.
- B waste and A normal: judge `A > B`.

Three-model GSB follows the same idea.

## Required Annotation Behavior

1. Identify the scene type from the prompt and candidate pages.
2. Apply the scene-specific priority before deciding GSB.
3. Compare prompt implementation, implemented-function defects, and visual quality.
4. For interactive or bug-like claims, open and test the candidate pages rather than relying only on screenshots.
5. Check image loading because broken images are functional defects.
6. Do not apply a waste tag for this queue; write waste explanations in remarks and still choose the GSB relationship.

## Source Text Captured From Manual

Important source facts distilled:

- `注意本GSB为webdev队列的衍生任务，重点关注以下三个维度`
- `对于Game场景：主要看功能完整性+功能缺陷，即对游戏场景而言「功能缺陷」优先级高于>「美观度」`
- `对于UI类场景：主要看功能完整性+美观度，即对于UI类场景「美观度」优先级高于>「功能缺陷」优先级`
- `本任务所有队列需要废弃的数据，不打废弃标签了，但是需要在备注里描述A/B的废弃原因`
- `废弃的 Pair 同样需要参与 GSB 评测`
