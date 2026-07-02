# Common Failure Patterns

Use these queue-specific examples before judging WebDev Arena GSB items.

## Only Reading The Last Turn

Situation: The last user message is only a partial modification, while earlier turns contain the real page goal, style, assets, or interaction requirements.

Judgement: Read the full multi-turn prompt before comparing. Do not decide from the final turn or Chinese summary alone.

Reason pattern: 模型一更符合完整多轮需求，模型二只处理了最后一轮修改，遗漏了前面要求的核心页面结构和功能

## Summary Replaces Prompt

Situation: The Chinese summary gives the general task, but omits details such as font size, button style, colors, layout, round corners, or specific modules.

Judgement: Use the summary only for orientation. The detailed prompt controls the final judgement.

Reason pattern: 模型二看起来覆盖了摘要方向，但没有落实原始 prompt 里的具体布局和样式细节

## Single Candidate Fails To Load

Situation: One preview is white-screen, erroring, empty, build-failed, or otherwise not normally viewable, while the other loads.

Judgement: Do not abandon the item. Mark the failed side as not normally viewable and compare normally.

Reason pattern: 模型一无法正常加载，模型二可以打开且基本完成题目要求，因此模型二明显更好

## Both Candidates Fail To Load

Situation: Both previews fail to display normal page content.

Judgement: Abandon/waste the item when the platform supports it.

Reason pattern: 两个产物都无法正常显示页面内容，无法进行有效 GSB 比较

## Incomplete Website Replica

Situation: The prompt asks to replicate a complete website, but the candidate only implements the first screen because the reference image is a partial screenshot.

Judgement: Treat missing lower-page content, sections, and footer as a completion defect. If both only implement the first screen, Same is acceptable with a detailed explanation.

Reason pattern: 两边都只复刻了首屏，没有按完整网页补齐后续内容和页脚，完成度都不足

## Mis-Matched Input Assets

Situation: The prompt references uploaded images or logos, but the images are shown separately at the bottom and are easy to mismatch with the corresponding turn.

Judgement: Map each prompt turn to the intended asset before judging. Penalize wrong image use, missing logo, or incorrect design-reference use.

Reason pattern: 模型一正确使用了题目指定素材，模型二把参考图对应错了，页面内容和素材要求不匹配

## Static Or Missing Interaction

Situation: A button, popup, animation, state switch, or other named interaction is visually present but does not work or gives no feedback.

Judgement: Functional interaction defects can outweigh visual polish when the prompt explicitly required the interaction.

Reason pattern: 模型二视觉更完整，但题目要求的弹窗交互没有实现，核心功能完成度低于模型一

## Template Or Empty Content

Situation: The page layout exists, but text is generic, placeholder-like, or unrelated to the requested site/application meaning.

Judgement: Penalize content/data mismatch under content and instruction-following dimensions.

Reason pattern: 模型一的文案更贴合题目场景，模型二大量使用通用占位内容，业务语义不足

## Vague Reason

Situation: The reason only says “A better” or “B more complete” without explaining both sides' concrete advantages and defects.

Judgement: Rewrite the reason to include label, stronger side, weaker side, key gap, and relation to prompt requirements.

Reason pattern: 选择 G，模型一在布局、素材和交互上更贴近题目，模型二虽然能打开但缺少关键模块，整体完成度明显更低
