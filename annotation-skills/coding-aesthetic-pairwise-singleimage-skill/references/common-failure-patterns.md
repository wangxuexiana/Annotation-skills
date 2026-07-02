# Common Failure Patterns

Use these examples as reminders, not fixed labels.

## Function Creep

Situation: The prompt mentions interactions, but the queue only shows screenshots.

Judgement: Do not open the page or test controls. Judge visible aesthetics only. If aesthetics cannot be judged from the screenshot, mark waste.

Reason pattern: 只能通过截图看美观度，当前画面信息不足

## Waste Mistaken For Same

Situation: One or both screenshots are white screen, black screen, erroring, garbled, badly cropped, or too incomplete to evaluate.

Judgement: Use waste/abandoned rather than Same.

Reason pattern: 截图无法正常判断美观度

## Forced Winner

Situation: Both sides have similar quality and comparable flaws.

Judgement: Choose Same. Do not invent a preference from tiny color or spacing differences.

Reason pattern: 两边整体观感接近，没有稳定优劣

## Same Overuse

Situation: One side clearly wins on fatal defects, core readability, layout hierarchy, material completeness, or scenario fit, while the other only has small decorative advantages.

Judgement: Choose the side that wins the higher-priority dimension.

Reason pattern: 一边核心层级和可读性更清楚，另一边只是局部视觉更顺眼

## Empty Minimalism Trap

Situation: A page is sparse and has few visible mistakes, but also lacks content, hierarchy, materials, and detail.

Judgement: Do not treat emptiness as premium design. Rich coherent execution can be better.

Reason pattern: 另一边内容和视觉完成度更高，不只是空白简洁

## Content Richness Trap

Situation: A page has more content but poor hierarchy, noisy color, or inconsistent components.

Judgement: More content is not automatically better. It must fit the scenario and remain coherent.

Reason pattern: 内容更多但层级和配色更乱

## Color Abuse

Situation: Large pure red, pure blue, neon, vivid purple, harsh red-green conflict, or multiple high-saturation colors dominate the screenshot.

Judgement: Penalize when the colors look harsh, cheap, or hard to read, unless the page scenario strongly supports the style.

Reason pattern: 配色过饱和，整体观感比较刺眼

## Non-Core Text Overweight

Situation: Footer, copyright, or auxiliary tiny text is slightly small or fuzzy, while core content is readable.

Judgement: Treat it as minor. Do not let it outweigh stronger overall layout and material quality.

Reason pattern: 小字问题不在核心区域，整体仍更完整

## Broken Key Material

Situation: Hero/product/card/avatar/chart/gallery images are broken, blank, half-loaded, distorted, or covered by overlays.

Judgement: Treat as a serious aesthetic and completeness defect.

Reason pattern: 关键图片没有正常展示，页面完成度更低

## Scenario Mismatch

Situation: A candidate looks visually polished but does not fit the requested page type or audience, such as a dashboard that hides key data or a retro page that lacks retro style.

Judgement: Scenario fit wins over personal taste.

Reason pattern: 更符合题目场景，整体风格也更贴合
