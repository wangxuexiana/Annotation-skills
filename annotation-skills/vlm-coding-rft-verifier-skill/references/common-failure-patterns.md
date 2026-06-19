# Common Failure Patterns

Use these examples to avoid recurring errors in VisualCoding Verifier / VLM Coding RFT chart reproduction tasks.

## Blindly Trusting Machine Rubrics

Situation: The provided rubric is vague, wrong, or misses a key GT feature, but the annotator scores directly.

Judgement: Repair or supplement rubrics before scoring. The rubric should describe GT under the correct O1/O2/O3 dimension and be observable by another annotator.

Reason pattern: 机标 rubric 没覆盖这个关键差异，先补充后再评分

## O1 Mixed With O2 Or O3

Situation: The generated image has correct chart type, but values are wrong, text overlaps, or colors differ, and O1 is lowered for those issues.

Judgement: Do not lower O1 for data, overlap, crop, color, font, or layout unless the O1 rubric explicitly makes it part of intent. Put data issues in O2 and layout/style issues in O3.

Reason pattern: O1 只看图表类型和意图，这个问题应放到 O2 或 O3

## Missing Composite Chart Component

Situation: GT is a composite chart such as radar plus scatter, dual-axis combo, stacked plus line, or multi-layer chart, but the generated image reproduces only one component.

Judgement: Lower O1 because chart type/intent is incomplete. The model did not fully identify the composite chart structure.

Reason pattern: 缺少原图中的散点层，组合图类型没有完整复现

## Data Error Hidden By Visual Similarity

Situation: A candidate looks visually close, but axis range, trend direction, key peak, colorbar polarity, or data series mapping is wrong.

Judgement: Penalize O2 heavily and do not let O3 style similarity dominate pairwise.

Reason pattern: 视觉风格接近，但关键数据映射错误，图表传递的信息不可靠

## Static Semantic Element Missing

Situation: Title, label, legend, unit, tick label, colorbar, data source note, or statistical annotation is missing or unreadable.

Judgement: Treat it as O2 when it affects chart interpretation. If the issue is mainly placement or overlap, also consider O3.

Reason pattern: 图例和单位缺失，静态辅助信息不完整

## Overlap Assigned To The Wrong Dimension

Situation: Legend, label, or text overlaps marks or is cropped.

Judgement: Use O3 for spatial overlap, crop, margins, and layout. Use O2 only when semantic labels, legend, ticks, or units become unreadable or inaccurate.

Reason pattern: 图例遮挡数据点，属于布局和可读性问题，O3 需要扣分

## O1 Zero Shortcut

Situation: O1 is zero, so the annotator skips O2/O3, reasons, or pairwise.

Judgement: Overall is zero when O1 is zero, but the current queue still requires all scores and reasons to be completed.

Reason pattern: O1 为 0 也要继续填完 O2 O3 和理由

## Pairwise Beauty Trap

Situation: One image has nicer colors or smoother style, but the other has more accurate chart type and data.

Judgement: Prefer the chart that is more faithful and trustworthy as data visualization. Use O3 as a tiebreaker only after O1/O2 are close.

Reason pattern: image2 视觉更好，但 image1 的数据和坐标轴更准确，因此 image1 更可靠

## Report Needed

Situation: Overall score and visible critical-error judgement conflict, or one image has a severe O2 issue that the numeric total underweights.

Judgement: Mark/report for discussion and explain the conflict clearly.

Reason pattern: 总分和主需错误严重程度不一致，需要 report 讨论
