# Visual Coding Verifier Training Summary

## Task Type And Queues

- Task: compare one target/original chart image with two generated reproduction images.
- Queue 1: Rubrics queue. Review and, if needed, edit O1/O2/O3 rubrics for the original image, then score image 1 and image 2 independently on O1/O2/O3 and write pointwise reasons.
- Queue 2: Pairwise queue. Choose `image1胜出`, `image2胜出`, or `打平` based on which generated chart is overall closer, more trustworthy, and more usable as a reproduction of the original.
- The two queues use the same underlying data but are split to avoid people mechanically deriving pairwise results from O1/O2/O3 scores.

## Required Inputs And Outputs

- Inputs: target image, generated image 1, generated image 2.
- Rubrics queue outputs:
  - Edited rubrics for O1/O2/O3 when the provided rubrics are inaccurate or severely incomplete.
  - Image 1 score as `[o1, o2, o3]`.
  - Image 2 score as `[o1, o2, o3]`.
  - Image 1 pointwise reasons as `[o1 reason, o2 reason, o3 reason]`.
  - Image 2 pointwise reasons as `[o1 reason, o2 reason, o3 reason]`.
- Pairwise queue outputs:
  - Pairwise result: `image1胜出`, `image2胜出`, or `打平`.
  - A short pairwise reason.

## Rubrics Editing Rules

- First check whether the machine-provided rubrics correctly describe the original image.
- Only edit rubrics when they are wrong or severely missing an evaluation point required by that dimension.
- Do not delete the rubric and write arbitrary content. Repair it so it correctly describes the original image under the current dimension.
- If the machine rubric is completely unusable, write a new rubric aligned with the corresponding O1/O2/O3 dimension.
- Edit rubrics before scoring. If rubrics are edited after scoring, the score was based on the wrong criteria.
- Rubrics edits are shared across both generated images, but image 1 and image 2 scores remain independent.

## O1: Chart Type And Intent Accuracy

- O1 asks whether the generated image reproduced the original chart type, special variant, and high-level intent.
- Focus on chart family and variant: line chart, smooth line, grouped/stacked bar, histogram, radar, area, scatter, dual axis, error bars, multi-series, etc.
- Do not penalize O1 for wrong data values, wrong trend, poor labels, text overlap, or visual style unless the O1 rubric itself explicitly names that feature as part of the chart intent.
- If the original is a line chart and the generated image is also the same line-chart variant, O1 can be 4 even if the numerical trend is wrong. Trend belongs mainly to O2 unless the rubric states the trend as the core intent.
- O1 score scale:
  - 4: main chart type and all important variants match.
  - 3: main type matches, but a special variant is degraded, such as smooth line to regular line or stacked bar to grouped bar.
  - 2: broad direction is right, but a core statistical property is lost, such as a no-gap histogram becoming an ordinary spaced bar chart.
  - 1: serious chart-type mismatch, such as radar to pie or area to scatter.
  - 0: meaningless shapes, no chart component, blank, error, or unrenderable output.

## O2: Core Element Accuracy

- O2 asks whether the chart content and data expression are accurate.
- Primary focus: numerical mapping, distribution, trend, extrema, point positions, proportions, axis scale/range, and coordinate logic.
- Also consider static auxiliary elements when they affect interpretation: titles, labels, legends, axis ticks, units, grid/guide lines, spelling, presence, and readability.
- O2 is where wrong trends, wrong values, shifted extrema, missing legends, missing units, unreadable tick labels, or hallucinated data should be penalized.
- O2 should not absorb O3 issues such as general aesthetics, color style, background, margins, or layout conflicts unless those conflicts make core data/labels unreadable.
- O2 score scale:
  - 4: data distribution/trend and all important text, legend, ticks, and labels match visually.
  - 3: data and static structure are extremely close, with only tiny dense-point or minor decorative errors.
  - 2: obvious data-mapping or important context problems, such as misaligned axes, shifted peaks, missing legend, or missing units.
  - 1: severe data distortion, hallucinated/opposite trend, swapped dimensions, fake text, or unreadable heavy overlap.
  - 0: no meaningful data elements, or only an abstract/bare image with no chart context.

## O3: Layout And Visual Style Consistency

- O3 asks whether spatial organization and visual style match the original.
- Spatial layout: panel divisions, module positions, relative placement, margins, cropping, overlap, callouts, leading lines, and occlusion relationships.
- Visual style: color palette, fonts, line thickness, point markers, background, contrast, and overall chart aesthetics.
- Text overlap, edge cropping, legends covering data, squeezed/distorted chart areas, background mismatch, and line/font/color differences are O3 issues.
- O3 score scale:
  - 4: layout is well controlled with no cropping or overlap; colors, fonts, lines, and markers closely match.
  - 3: overall structure is correct, with minor margin/cropping/style differences.
  - 2: obvious overlap or style mismatch, such as a legend blocking data or colors/line styles being visibly off.
  - 1: major structural deformation, collapsed complex layout, forced axis simplification, or strongly divergent style.
  - 0: elements are scattered and the visual structure collapses.

## Pairwise Decision Rules

- Pairwise is not a mechanical sum or weighted sum of O1/O2/O3 scores.
- Use overall visual judgement, but keep the macro priority: chart type and intent > data/numerical accuracy > layout/visual style.
- Open/inspect the images carefully; do not decide from a quick thumbnail glance.
- Prefer the image that is more like the original, more trustworthy, and more usable as a real chart reproduction.
- If one image has the correct chart type and the other misses the chart type, the correct-type image usually wins without needing to over-focus on downstream details.
- If both chart types are correct, compare data accuracy next: value positions, trends, axes, peaks, legends, labels, and context.
- Use visual style and beauty as a tiebreaker after chart type and data accuracy.
- If the two generated images are genuinely close and no clear winner emerges after checking details, choose `打平`.
- Do not overuse `打平` from a quick glance. If details reveal a meaningful difference, choose the better image.
- Pairwise can reasonably disagree with the pointwise score totals.

## Reason Wording

- Keep reasons short and concrete.
- For pointwise reasons, explain the reason under the exact dimension being scored. Do not put O2 or O3 issues into O1.
- For pairwise reasons, reflect the macro priority: mention chart type first when relevant, then data accuracy, then layout/style.
- Good pairwise pattern: `两张图图表类型都正确，但image1的数据点和趋势更接近原图，image2存在明显数值偏差，因此image1胜出。`
- Good pointwise O1 pattern: `图表类型和多系列折线结构与原图一致。`
- Good pointwise O2 pattern: `主要趋势基本一致，但多个峰值位置偏移，图例缺失影响理解。`
- Good pointwise O3 pattern: `整体布局接近，但右侧标签有裁切，线条颜色与原图有差异。`

## Easy-To-Misjudge Cases

- Do not reduce O1 because labels overlap or text is unreadable. Those are O2/O3 depending on whether they affect semantic element accuracy or layout.
- Do not reduce O1 because trends or values are wrong if the chart type and intent are still correct and the O1 rubric does not explicitly require the trend.
- Do not let background color or visual prettiness dominate pairwise when chart type or data accuracy differs.
- Do not score only the better generated image in the Rubrics queue. Image 1 and image 2 both need independent O1/O2/O3 scores.
- Do not blindly trust machine rubrics; verify against the original image first.
- Do not invent data or infer what the model "intended" beyond visible facts.

## Quiz Facts Likely To Be Tested

- There are two queues: Rubrics and Pairwise.
- In Rubrics queue, edit inaccurate rubrics before scoring.
- O1 evaluates chart type, special variant, and high-level intent, not data trend or layout overlap.
- O2 evaluates data/value mapping and important static chart elements.
- O3 evaluates spatial layout, overlap/cropping, visual style, colors, fonts, lines, and background.
- Pairwise should not be determined by adding O1/O2/O3 scores.
- Pairwise should still respect macro priority: chart type > data accuracy > aesthetics.
- `打平` is allowed when quality is truly close, but should not be used after only a superficial glance.
- Reasons should be concise and should not mix dimension-specific issues into the wrong dimension.
