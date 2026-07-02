# Training Summary

Source: https://bytedance.larkoffice.com/wiki/CMUww2CzIimYe6kdTlgclKVxnjh

## Queue And Task Type

Task: WebDev GSB comparison for `场景GSB` and `评测GSB`.

Queues from the manual:

- `场景GSB-试标`: `7649606298007621414「场景GSB」试标队列-webdev场景GSB-严格备注丨0610`
- `评测GSB`: `7649344261260283699「评测GSB」webdev评测GSB-严格备注丨0610`

This is a WebDev-derived GSB task. The annotator compares candidate webpage outputs, usually A/B and sometimes three models, against the prompt and visible preview behavior. The decision should focus on three dimensions: functional completeness, functional defects, and aesthetics.

No separate training recording was provided with this request. Treat the Wiki manual as the official source until a video, quiz feedback, platform instruction, or user correction adds newer rules.

## Core Judgement

Use the page type to decide dimension priority:

- Game scenes: prioritize functional completeness and functional defects. For games, functional defects outrank aesthetics.
- UI scenes: prioritize functional completeness and aesthetics. For UI pages, aesthetics outranks functional defects.

Always judge prompt-named requirements first. Features not mentioned in the prompt are not default requirements for functional completeness, though defects in implemented visible controls can still count as functional defects.

## Dimensions

Functional completeness:

- Check whether the prompt's explicit functional points are implemented.
- Missing prompt-named entries, pages, interactions, tab jumps, or required outputs are functional-completeness problems.
- Do not require generic features that the prompt did not ask for.

Functional defects:

- Check whether implemented functions have bug-like failures.
- Examples include buttons with no response, broken clicks, broken routing, failed image loading, and visible controls that look interactive but do nothing.
- A feature not required by the prompt can still hurt as a functional defect when the model implemented it and it visibly fails.
- Image loading failure is a functional defect.

Aesthetics:

- Check unreasonable layout or styling in the produced page.
- Do not over-focus on tiny details. Judge the overall visual impression.
- For UI outputs, a page can be acceptable when the overall visual quality is good, basic needs are met, and there are no multiple or major interaction defects.

## Waste And Abandon Handling

This queue does not use a waste tag for data that would normally be abandoned. Waste cases still participate in GSB comparison and the reason/remark must describe the waste reason for A/B.

Pairwise rules:

- If A is waste/abandoned and B is normal, choose `A < B`.
- If A and B are both waste/abandoned, choose `A = B`.
- If B is waste/abandoned and A is normal, choose `A > B`.

Three-model GSB follows the same principle: normal evaluable outputs outrank waste outputs, and equally waste outputs are tied unless another visible rule separates them.

## Browser Test Flow

1. Read the prompt and classify the scene as Game, UI, or other visible webpage type.
2. Open each candidate preview in Chrome when the platform requires real interaction or when screenshots are not enough.
3. Test prompt-named core functions first.
4. Test visible natural controls that the model implemented when they may create functional defects.
5. Check key visible images for broken loading.
6. Compare the candidates under the correct scene priority.
7. Write a concise Chinese reason or strict remark that names the deciding evidence.

## Common Traps

- Do not use the same priority for Game and UI scenes. Game defects outrank visual polish; UI visual quality can outrank smaller functional defects.
- Do not penalize a candidate for missing generic features that the prompt never requested.
- Do not ignore a broken implemented feature just because it was not explicitly requested.
- Do not mark waste and stop; this queue still requires a GSB comparison and a remark explaining waste reasons.
- Do not choose Same because both candidates have small issues if one is clearly better in the scene's higher-priority dimension.

## Reason Style

Use compact natural Chinese. Mention the scene type when priority matters, then give the decisive evidence:

- `A功能更完整，Prompt要求的关卡切换和计分都能用，B按钮点击无反应`
- `B整体布局更规整，主要信息展示完整，A样式错乱影响UI观感`
- `A废弃，B可正常打开和评测`

Follow the user's active punctuation preference when present, especially comma-only concise wording.

## Quiz Facts Likely To Be Tested

- This task is a WebDev-derived GSB comparison task.
- Main dimensions are functional completeness, functional defects, and aesthetics.
- Game scenes emphasize functional completeness and functional defects; functional defects outrank aesthetics.
- UI scenes emphasize functional completeness and aesthetics; aesthetics outranks functional defects.
- Prompt-explicit functions are the main basis for functional completeness.
- Generic features not mentioned in the prompt are not default functional-completeness requirements.
- Implemented visible controls that fail can count as functional defects even if not prompt-required.
- Image loading failure is a functional defect.
- Waste data does not get a waste tag in this queue; it still participates in GSB and the remark must explain the waste reason.
- A waste vs B normal means `A < B`; both waste means `A = B`.
