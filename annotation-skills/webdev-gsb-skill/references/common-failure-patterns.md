# Common Failure Patterns

Use these examples to avoid missing recurring WebDev GSB rules. Add queue-specific examples as real cases appear.

## Static Shell Instead Of Function

Situation: The page looks polished, but the prompt-named button, slider, toggle, generator, editor, game control, or route does not change anything.

Judgement: Treat the core function as missing or failed, even if the visual design is good.

Reason pattern: 核心控件操作后没有反馈，关键功能不可用

## Waste Tag Trap

Situation: A candidate preview is blank, broken, stuck loading, black-screen, white-screen, or cannot be inspected enough to judge.

Judgement: In this queue, do not apply a waste tag. Explain the waste-like reason in the remark and still compare candidates. A waste-like candidate loses to a normal candidate; two waste-like candidates are Same unless visible evidence separates them.

Reason pattern: A页面无法正常渲染，B可正常评测

## Prompt Ignored

Situation: The candidate provides a generic page or game, but misses the specific object, workflow, comparison target, or interaction named in the prompt.

Judgement: Choose the other candidate when the missing prompt requirement is central.

Reason pattern: 没有体现题目要求的核心内容

## Game Visual Polish Trap

Situation: In a game scene, one candidate looks prettier, but the other has fewer functional defects or better playability.

Judgement: For Game scenes, prioritize functional completeness and functional defects over aesthetics.

Reason pattern: A游戏功能更完整，B虽然画面更好但操作存在明显问题

## UI Small Bug Overweight Trap

Situation: In a UI page, one candidate has stronger overall layout and visual presentation while the other only has a small non-core implemented-control defect.

Judgement: For UI scenes, aesthetics can outrank smaller functional defects when core prompt needs are met and there are no multiple or major interaction defects.

Reason pattern: A整体布局和样式更好，B只是小交互更完整但UI观感明显弱

## Implemented Control Defect

Situation: The prompt did not explicitly request a certain click or control, but the model made it visibly interactive and it does nothing or breaks.

Judgement: Do not mark it as a functional-completeness miss, but do count it as a functional defect when it affects the comparison.

Reason pattern: B实现了该入口但点击无反馈，属于功能缺陷

## Generic Feature Over-Requirement

Situation: A candidate lacks a generic webpage feature that the prompt never requested.

Judgement: Do not penalize functional completeness merely for missing unspecified generic features. Only count it if the prompt, visible rubric, or platform instruction requires it.

Reason pattern: 该功能题目没有要求，不作为主要扣分点

## Priority Flattening Trap

Situation: One candidate clearly wins on the scene's higher-priority dimension, but the other has a lower-priority advantage such as nicer color, mood, or small polish.

Judgement: Do not mark Same just because each side has some advantages. Apply scene priority first.

Reason pattern: 核心维度差异更明显，不应只看局部视觉细节

## Broken Image In Key Content

Situation: A candidate has broken images in key visible content such as hero, product, card, avatar, chart, gallery, or required comparison content.

Judgement: Treat this as a functional defect in this queue. If one candidate has failed key images and the other does not, the image failure can decide the comparison depending on scene priority and severity.

Reason pattern: 关键图片没有正常显示，影响页面功能和内容完整度

## Latest Correction Overfit Trap

Situation: A recent user correction mentions one rule, so the judgement focuses only on that rule and forgets other applicable manual, priority, completeness, defect, aesthetic, or style requirements.

Judgement: Use the correction as a guardrail inside the full rubric. Before deciding, scan every applicable rule family and then apply priority.

Reason pattern: 按完整规则看，不只看刚提到的一个点

## Reason Copying Trap

Situation: A previous reason sounds close but does not match the current visible evidence.

Judgement: Reword from current evidence. Use examples as phrase pools only.
