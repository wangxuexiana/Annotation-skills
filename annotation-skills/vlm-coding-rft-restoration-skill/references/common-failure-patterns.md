# Common Failure Patterns

Use these examples to avoid missing recurring VLM Coding RFT restoration rules. Treat them as analogies, not fixed labels.

## UP Function Missing

Situation: The page looks visually close, but a UP-required click, switch, layout adjustment, or style adjustment does not work.

Judgement: Treat the UP function as a significant defect. If most prompt functions are absent, score 0.

Reason pattern: UP要求的切换没有实现，关键功能不符合

## Static State Over-Tested

Situation: The reference image shows hover, popup, selected, or expanded state, but UP does not ask for real interaction.

Judgement: Judge the visual state restoration only. Do not penalize for missing real interaction unless UP requires it.

Reason pattern: 视觉状态已按参考图还原，不额外要求真实交互

## White Screen Or Core Missing

Situation: The product is white-screen, severely misaligned, or misses core visible content.

Judgement: Score 0. This queue uses 0 for these severe restoration failures.

Reason pattern: 页面白屏，核心内容没有正常还原

## Prompt Reference Mismatch Discard

Situation: The prompt demand and reference image do not correspond, but the actual product follows the prompt.

Judgement: Treat as the manual's discard case instead of normal 0/1/2 scoring when the platform exposes discard handling.

Reason pattern: prompt和参考图不对应，产物是按prompt生成

## Direct Two-Point Trap

Situation: A product looks best at first glance, so 2 is selected before checking whether it qualifies as 1.

Judgement: First score all products as 0 or 1. Promote exactly one best 1-point product to 2 only after confirming 1-point eligibility.

Reason pattern: 先确认达到1分，再从1分里选最佳产物

## Broken Image In Key Content

Situation: A candidate has broken images in key visible content such as hero, product, card, avatar, chart, gallery, or required comparison content.

Judgement: Broken images are generally not allowed for 1 unless the broken area is tiny and non-core. Broadly broken or uninspectable pages score 0.

Reason pattern: 关键图片没有正常显示，核心内容不完整

## Small-Flaw One Point

Situation: The product is near-complete, with only small font, icon, button, image, or layout differences that are hard to notice at first glance.

Judgement: Score 1. If multiple products qualify, compare them and promote the best one to 2.

Reason pattern: 整体按参考图完整实现，仅局部图标存在差异

## Visual Polish Trap

Situation: A product is aesthetically polished but has wrong layout, missing modules, wrong first-screen content, hallucinated sections, or inaccurate core text.

Judgement: Do not give 1 for beauty alone. Restoration to the reference and prompt requirements comes first.

Reason pattern: 页面美观但核心布局和参考图不一致

## Latest Correction Overfit Trap

Situation: A recent user correction mentions one rule, so the judgement focuses only on that rule and forgets layout, element completeness, content accuracy, visual restoration, hallucination control, UP functions, or screenshot requirements.

Judgement: Use the correction as a guardrail inside the full rubric. Before deciding, scan every applicable rule family and then apply priority.

Reason pattern: 按完整规则看，不只看刚提到的一个点

## Reason Copying Trap

Situation: A previous reason sounds close but does not match the current visible evidence.

Judgement: Reword from current evidence. Use examples as phrase pools only.
