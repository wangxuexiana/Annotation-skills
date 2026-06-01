# Learned Patterns

Add reusable user corrections here.

Format:

- Pattern: <task or situation>
  Pass/choose condition: <what is enough>
  Fail/waste condition: <what is not enough>
  Reason style: <preferred wording>

- Pattern: Data-heavy charts with explicit coordinates, values, ranges, distributions, or point locations
  Pass/choose condition: For each scoring dimension, compare the reproduction against the original item by item using the numbered requirements shown under that dimension on the task page
  Fail/waste condition: If reproduced data is shifted, missing, wrong, covered, occluded, crossed by grid/axis/box lines, or hard to read because of overlap, mention that defect in O2 instead of only saying the overall chart is close
  Reason style: For any non-full score, name the specific unmet requirement in that dimension without necessarily saying its item number. Chinese-only reasons can be natural and complete; do not over-compress them. When the reason contains numbers, coordinate/range values, time spans, or English labels/object names, keep that part simple and precise, avoiding long range lists or object-by-object binding unless needed for clarity. For O2, name the data/readability defect, such as data shift, box/whisker mismatch, wrong outlier count, label overlap, or covered values; list affected values or labels only when useful

- Pattern: Rubrics dimensions with multiple visible requirements
  Pass/choose condition: For O1, O2, and O3, compare every requirement listed under that dimension against the original before scoring, then also check other visible differences not explicitly named in the rubric
  Fail/waste condition: Do not limit scoring to only the listed rubric bullets. Any obvious visible difference that affects reproduction quality, such as missing or shifted data, wrong values, title or label overlap, cropping, margin/proportion differences, legend placement, grid style, color mapping, font weight, or readability defects, should influence the matching dimension score and reason
  Reason style: The submitted reason can include a little more evidence and may use up to three lines, but should still be clear and not padded. Mention important visible defects even when they are not explicitly named below the dimension; do not only do item-by-item checking for O2

- Pattern: O3 visual style differences after O1/O2 look correct
  Pass/choose condition: Only give high O3 when typography, text color, text fill/stroke/outline, font weight, title/subtitle/legend placement, layer spacing, cropping, overlap, and overall visual proportions are also close to the original
  Fail/waste condition: Do not stop after confirming chart type, labels, values, and geometric hierarchy. If the original uses white outlined or high-contrast text but the reproduction uses black text, different stroke/halo, heavier shadow, wrong contrast, cropped legend, oversized title, cramped spacing, or missing gaps between layers, lower O3 and mention the specific visual mismatch
  Reason style: Name the visible O3 defect directly, such as "文字颜色由原图白色描边变成黑色", "标题过大且图例裁切", or "层间间距与原图不一致"; keep O2 reasons for data/geometry and O3 reasons for visual style/layout

- Pattern: O2/O3 full-score threshold
  Pass/choose condition: Assign O2=4 or O3=4 only when the reproduction is highly consistent with the reference in the corresponding dimension, with no obvious mismatch in data/core elements for O2 or layout/visual style for O3
  Fail/waste condition: Do not give full score if a visible difference remains in that dimension, even when the overall chart looks close or other dimensions are correct
  Reason style: For non-full O2/O3, state the most important mismatch directly, such as wrong value/position/order for O2 or font/color/crop/spacing/legend difference for O3

- Pattern: Strict O2 scoring for large data differences
  Pass/choose condition: O2 can stay high only when the quantitative marks are close to the reference, including positions, heights, curve shapes, endpoints, ranges, labels, and weights
  Fail/waste condition: When core data has large visible differences, such as shifted scatter positions, changed curve peaks, wrong bar heights, shortened or lengthened error bars, missing labels, or altered edge weights, score O2 more strictly even if categories and overall chart type are correct
  Reason style: Name the affected data mark and location directly, for example 顶部两个期限的紫色误差棒右端明显长于原图, or 蓝色曲线下午峰值时段比原图提前

- Pattern: Non-full rubric reasons should be concrete about the defect
  Pass/choose condition: The reason names the visible defect in the scored dimension and points to where it appears, using layer order, color, position, direction, chart component, or affected mark/text. Brief matching context is allowed when it helps explain the score
  Fail/waste condition: Do not write broad reasons like "layout/proportion is different" without saying where, and do not use meta-judgement phrases such as "cannot give full score"
  Reason style: Mention matching points only if useful, then state the defect concretely, for example "顶层蓝色漏斗左右端点比原图内收", "第四层紫色和第五层粉色文字横向超出色块边界", or "底部图例左右两侧被裁切"

- Pattern: Repeated English categories with one shared defect
  Pass/choose condition: Use a concise Chinese group phrase when all categories share the same issue
  Fail/waste condition: Do not list many English category names just to say the same defect applies to all of them
  Reason style: Prefer phrases like "各类别", "各气候区", or "五类冷却方式" unless a specific English label must be named to avoid ambiguity

- Pattern: Avoid English labels in visual-style reasons when Chinese location is enough
  Pass/choose condition: Use Chinese ordinal/color/position descriptions for O3 defects when the image location uniquely identifies the issue
  Fail/waste condition: Do not mention English layer or category names merely to locate a visual defect, especially when the user asked for Chinese-style reasons
  Reason style: Prefer "第四层紫色和第五层粉色文字横向超出色块边界" over naming the English labels; keep English only when label text content itself is wrong or Chinese wording would be ambiguous

- Pattern: Submitted reason punctuation
  Pass/choose condition: All filled reason fields use plain Chinese wording and commas only when punctuation is needed
  Fail/waste condition: Do not include quotation marks, square brackets, parentheses, colons, semicolons, slashes, dashes, or other symbols in submitted reason fields
  Reason style: Prefer comma separated clauses, for example 图表类型为分组散点叠加分布椭圆，展示参赛年限与最终得分分组差异的意图一致
