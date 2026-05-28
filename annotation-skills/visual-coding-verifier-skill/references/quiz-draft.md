# Visual Coding Verifier Quiz Draft Notes

No actual permission quiz questions have been provided yet. Use these as evidence-backed answer anchors when the questionnaire appears.

## Likely Answers

1. If asked what O1 evaluates:
   - Answer: O1 evaluates whether the generated chart reproduces the original chart type, special variant, and high-level intent.
   - Evidence: Manual O1 definition and training examples around 00:11:38-00:21:44.
   - Confidence: High.

2. If asked whether wrong trend should reduce O1:
   - Answer: Usually no. If the chart type/variant is correct and the O1 rubric does not explicitly require the trend as core intent, wrong trend belongs to O2.
   - Evidence: Training around 00:15:09-00:20:24 and 00:52:00-00:52:36.
   - Confidence: High.

3. If asked what O2 evaluates:
   - Answer: O2 evaluates data/value mapping and important static chart elements such as labels, legends, ticks, units, and readability.
   - Evidence: Manual O2 definition and training around 00:22:12-00:30:12.
   - Confidence: High.

4. If asked what O3 evaluates:
   - Answer: O3 evaluates spatial layout and visual style, including overlap, cropping, margins, colors, fonts, line thickness, background, and overall style.
   - Evidence: Manual O3 definition and training around 00:28:46-00:33:00.
   - Confidence: High.

5. If asked whether pairwise equals O1/O2/O3 score sum:
   - Answer: No. Pairwise should use overall visual judgement and may disagree with pointwise score totals.
   - Evidence: Manual Pairwise section and training around 00:38:03-00:50:32.
   - Confidence: High.

6. If asked the pairwise priority:
   - Answer: Follow the macro priority of chart type/intent first, data accuracy second, aesthetics/layout third.
   - Evidence: Manual Pairwise section and training around 00:39:09-00:43:47.
   - Confidence: High.

7. If asked whether `打平` is allowed:
   - Answer: Yes, when both generated images are genuinely close and hard to distinguish after careful inspection.
   - Evidence: Manual Pairwise section and training around 00:43:47-00:45:08.
   - Confidence: High.

8. If asked what to do before scoring in Rubrics queue:
   - Answer: Check whether the machine rubrics correctly describe the original image; edit them before scoring if they are wrong or severely incomplete.
   - Evidence: Training around 00:02:28-00:10:26.
   - Confidence: High.
