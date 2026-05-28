# Visual Coding Verifier Manual Summary

## Official Manual Source

- Feishu Wiki title: `Visual Coding Verifier数据标注文档`.
- The manual defines the same three-image input format and the two-queue output format.

## Data Form

- Provided:
  - `gt image`: original/target chart.
  - `generate image1`: first reproduced chart.
  - `generate image2`: second reproduced chart.
- Annotate:
  - Rubrics for O1/O2/O3.
  - Image 1 O1/O2/O3 score.
  - Image 2 O1/O2/O3 score.
  - Image 1 O1/O2/O3 pointwise reasons.
  - Image 2 O1/O2/O3 pointwise reasons.
  - Pairwise result.
  - Pairwise reason.

## Core Evaluation Prompt

- Act as a precise data visualization/chart reproduction evaluator.
- Compare `target_image` and `generated_image` using visual evidence only.
- Data and logic have higher priority than aesthetics.
- Do not tolerate data hallucination, wrong chart type, or wrong coordinate logic.
- Evaluate O1, O2, and O3 separately and output a 0-4 score for each.

## O1 Manual Definition

- Dimension: chart type and intent understanding accuracy.
- 4: main type and all variants are perfectly identified.
- 3: main type correct, special variant slightly degraded.
- 2: broad direction correct, but core statistical property lost.
- 1: core chart type seriously wrong.
- 0: meaningless HTML/CSS shapes, no chart component, blank, or error.

## O2 Manual Definition

- Dimension: core element accuracy.
- Covers dynamic data mapping and static auxiliary elements.
- Dynamic data: numerical distribution, trend, extrema, proportion, axis range, and coordinate logic.
- Static elements: title, labels, legend, axis ticks, auxiliary/grid lines.
- 4: data and all important static elements match.
- 3: tiny defects only, not affecting conclusions.
- 2: obvious mapping issue or missing important context.
- 1: severe distortion, fake data/text, swapped axes, or unreadable heavy overlap.
- 0: no data elements or only a meaningless bare/abstract chart.

## O3 Manual Definition

- Dimension: layout structure and visual style consistency.
- Spatial layout: panels, modules, relative placement, margins, occlusion, callout/leader lines.
- Visual style: colors, fonts, line widths, point styles.
- 4: layout and style closely match, with no cropping/overlap.
- 3: overall structure correct, with minor space/style defects.
- 2: obvious overlap or style mismatch.
- 1: severe deformation or style shift.
- 0: layout and style collapse.

## Pairwise Manual Definition

- Pairwise result is based on overall intuitive comparison of the two generated images, not a mechanical sum of O1/O2/O3.
- Still follow macro priority: chart type accuracy > chart value accuracy > aesthetics.
- Ask: if only one generated image can be kept, which is more like the original, more trustworthy, and more usable as a chart reproduction?
- If the two are close and hard to distinguish, choose `打平`.
- Pairwise may differ from O1/O2/O3 score totals.
- Forbidden:
  - Simple weighted summing.
  - Treating pairwise as an automatic "higher total score wins" result.
  - Forcing pairwise to match pointwise score logic.

## Manual Examples

- Example 1: image1 wins because its overall line style and trend are closer to the target, even though both images have O1 correct.
- Example 2: image2 wins because image1's orange series data is mostly wrong, while image2 has much higher core data accuracy despite missing legend/fill style issues.
