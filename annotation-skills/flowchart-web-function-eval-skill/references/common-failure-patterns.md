# Common Failure Patterns

Use these examples to avoid missing recurring rules. Add queue-specific examples as real cases appear.

## Screenshot-Only Judgement

Situation: The annotator judges rubrics or overall score from `modelA_img` without opening `modelA`.

Judgement: Wrong for behavior-related rubrics. Open the webpage and test the required interactions.

Reason pattern: 需要打开网页实际操作，不能只看截图判断功能

## Over-Abandoning Bad Pages

Situation: The page is ugly, incomplete, or fails several rubrics, but it opens and can be evaluated.

Judgement: Do not waste/abandon. Judge rubrics as `0/1`, assign the score, and evaluate screenshot correctness.

Reason pattern: 页面可打开并评价，按具体功能缺陷正常打分

## Rubric Cross-Contamination

Situation: One rubric fails, so another unrelated rubric is also marked `0`.

Judgement: Wrong. Each rubric is independent and only its own wording decides its label.

Reason pattern: 该项只看本条要求，其他功能问题不影响此项判断

## Invented Requirement

Situation: The rubric asks whether validation exists, but the judgement requires an exact validation standard not stated by the prompt, flowchart, or rubric.

Judgement: Do not invent stricter product requirements. If relevant validation and feedback exist, the rubric can be `1`.

Reason pattern: 该项只要求有校验反馈，页面已给出提示

## Screenshot Post-Interaction State

Situation: `modelA_img` shows a selected filter, expanded card, modal, menu, popup, or other state that appears only after interaction.

Judgement: Screenshot correctness is `0`, because the screenshot must match the initial loaded page before any interaction.

Reason pattern: 截图展示了操作后的状态，实际初始页面不一致

## Screenshot Cropped Or Partial

Situation: The screenshot captures only the current viewport or misses lower-page content that belongs to the initial page capture.

Judgement: Screenshot correctness is `0` when the screenshot is incomplete or cropped compared with the expected full initial page state.

Reason pattern: 截图只截取了部分页面，缺少完整初始内容

## Bad Page But Correct Screenshot

Situation: The actual webpage initially has broken images, flaws, or rendering defects, and the screenshot shows the same flawed state.

Judgement: Screenshot correctness can still be `1`; functional quality and screenshot correctness are separate.

Reason pattern: 实际初始页面也有该缺陷，截图状态一致

## High Score With Fully Failed Rubric

Situation: Overall score is `8+`, but at least one rubric is completely unmet.

Judgement: Usually inconsistent. `8+` requires rubrics to be basically satisfied, with no completely unmet rubric and at most one partial or minor defect.

Reason pattern: 存在完全未满足的功能项，整体分不应给到 8 分以上

## QC Direct Edit Trap

Situation: In QC mode, the reviewer sees an incorrect annotation and directly changes the annotator's answer.

Judgement: Follow QC workflow. Mark unqualified or return for revision and write the return reason instead of silently editing the answer.

Reason pattern: 标注结果有误，需要打回返修

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

## Priority Flattening Trap

Situation: One candidate clearly wins on a higher-priority dimension such as layout, position, size, spacing, first-screen content, module order, core content, or element completeness, but the other candidate has nicer colors, image mood, or small visual polish.

Judgement: Do not mark Same just because each side has some advantages. Apply the priority stack first and choose the side that wins the higher-priority dimension.

Reason pattern: 布局和核心内容更贴近题目，另一个只是局部视觉细节更好

## Broken Image In Key Content

Situation: A candidate has broken images in key visible content such as hero, product, card, doctor, avatar, chart, gallery, or required comparison content.

Judgement: Treat this as a significant element-completeness or visual-restoration defect. If the page is broadly unrenderable or cannot be inspected, prefer waste or abandon when supported.

Reason pattern: 关键图片没有正常显示，核心内容不完整

## Latest Correction Overfit Trap

Situation: A recent user correction mentions one rule, so the judgement focuses only on that rule and forgets other applicable manual, priority, layout, content, completeness, or style requirements.

Judgement: Use the correction as a guardrail inside the full rubric. Before deciding, scan every applicable rule family and then apply priority.

Reason pattern: 按完整规则看，不只看刚提到的一个点

## Reason Copying Trap

Situation: A previous reason sounds close but does not match the current visible evidence.

Judgement: Reword from current evidence. Use examples as phrase pools only.
