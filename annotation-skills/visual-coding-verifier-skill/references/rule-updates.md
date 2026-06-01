# Rule Updates

Newer entries override older summaries when they clearly conflict. Keep active overrides short and execution-oriented so the skill can reliably apply them during annotation.

## Active Overrides

### O1 Stays Lenient

- Score O1 by chart type, special chart variant, and high-level intent only.
- Do not lower O1 for data errors, value differences, label overlap, crop, color, typography, or general style defects when the main chart type and intent are still reproduced.
- O1 reasons should be one concise line about whether the chart type and core intent match.

### O2 Is Strict About Data And Semantic Elements

- Before scoring O2, compare every listed O2 subpoint and the visible chart evidence: data point positions, curve trends, bar heights, error bar endpoints, axis values, displayed numbers, labels, legends, order, ranges, units, and coordinate logic.
- If visible numbers differ, are swapped across bins, are attached to the wrong category or interval, or quantitative marks show large visible differences, lower O2 and name the numeric or data mismatch.
- Do not give high O2 only because the chart type, categories, or broad trend are present.
- Treat overlap, crop, or unreadable text as O2 only when it affects semantic chart elements such as data labels, axis labels, ticks, legends, or units.

### O3 Is Strict About Layout And Visual Style

- Before scoring O3, compare typography, text fill or stroke, font color, font weight, shadow or halo, contrast, title and subtitle placement, legend box and position, gridline or band style, margins, crop, layer spacing, overlap, viewpoint, colors, and overall proportions.
- Compare visible mark thickness for bars, lines, error bars, network edges, and similar marks.
- Lower O3 for obvious text-style, mark-thickness, crop, spacing, legend, grid, color, or layout differences even when O1 and O2 are correct.
- Do not give O3 full credit merely because chart type, values, labels, and geometry are correct.

### O2 And O3 Full Scores Require Near-Complete Consistency

- Give O2=4 or O3=4 only when the reproduction is highly consistent with the reference in that dimension and has no obvious visible mismatch.
- If any listed subpoint is visibly unmet, approximate, shifted, missing, cropped, overlapped, or clearly different, use a lower score and name the most important mismatch.
- Do not assign 4 based on approximate overall similarity.

### Reasons Must Be Concrete And In User Style

- For non-full O2 or O3, the reason must name the concrete mismatch and where it appears, using layer order, color, position, direction, chart component, or affected mark or text.
- It is acceptable to mention matching points briefly when helpful, but the reason must clearly identify the defect. Do not write meta-judgement phrases such as `不能给满分`.
- Prefer Chinese position, color, ordinal layer, or chart-element descriptions when they identify the defect clearly. Use English labels only when the label text itself is wrong or needed to avoid ambiguity.
- For repeated English categories with one shared issue, use a concise Chinese group phrase such as `各类别`, `各气候区`, or `五类冷却方式` instead of listing every English name.
- Chinese-only explanations may be natural and complete. Keep wording simple and precise for numbers, coordinates or ranges, time spans, English labels, and English object names. Avoid long numeric lists or repeated object-by-object binding unless needed for clarity.
- Rubrics reasons may include slightly more evidence and can use up to three short lines when covering multiple subpoints in one dimension. Do not add filler.

### Submitted Reason Punctuation

- Submitted reason fields should use plain Chinese wording and Chinese commas only when punctuation is needed.
- Do not use quotation marks, square brackets, brackets, parentheses, colons, semicolons, slashes, dashes, or final periods in submitted reason fields.

## Update Log

- 2026-06-01: Condensed repeated active overrides into execution-oriented groups so the skill applies the same rules more reliably during annotation.
- 2026-05-29: Added user correction that O3 must explicitly check typography, text color/stroke, layout spacing, crop, and overlap; data correctness alone cannot justify high O3.
- 2026-05-29: Added user correction that O3 must also check visible mark thickness such as bar thickness, line width, edge width, and error bar thickness.
- 2026-05-29: Added user correction that O3 reasons should point out the main visible visual differences present in the current image, not just a single selected issue.
- 2026-05-29: Added user correction that O2/O3 full scores require high consistency with the reference under that dimension and no obvious differences.
- 2026-05-29: Reinforced user correction that O2 and O3 should not receive 4 unless the corresponding dimension is highly consistent with the reference, not merely broadly close.
- 2026-05-30: Reinforced user correction that O2 and O3 4-point scores must be strict and cannot be based on rough overall similarity.
- 2026-05-29: Added user correction that O2 and O3 must be checked against every small rubric point in the dimension, not only an overall visual impression.
- 2026-05-29: Added user correction that O2 should be stricter when core data has large visible differences, including point positions, trends, bar heights, error ranges, or weight labels.
- 2026-05-29: Added user correction that O2 must compare explicit displayed numbers, not only visual bar lengths or broad distribution shape.
- 2026-05-29: Revised user correction for non-full reasons: matching points may be mentioned when helpful, but concrete mismatches must be clearly named; avoid "cannot give full score" phrasing.
- 2026-05-29: Added user correction that reasons must locate the defect precisely by layer/color/position/element, and should avoid English category names when Chinese location descriptions are enough.
- 2026-05-29: Added user correction that submitted reason text should not contain quotation marks, brackets, parentheses, colons, semicolons, slashes, dashes, or other punctuation; use commas only.
- 2026-05-29: Added user correction that concise wording applies mainly to numeric and English-heavy details, not all Chinese reason text.
- 2026-05-29: Added user correction that reasons can be a little fuller, capped at three lines.
- 2026-05-29: Added user correction that O1 reasons should stay to a single concise line.
- 2026-05-29: Added user correction that O1 should not be made stricter alongside O2/O3. Keep O1 focused on type and intent, while O2/O3 remain strict.
