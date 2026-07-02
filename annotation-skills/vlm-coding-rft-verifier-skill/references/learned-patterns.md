# Learned Patterns

Add reusable user corrections here.

## Starter Guardrails

- Pattern: O1 independent scoring
  Pass/choose condition: O1 only considers chart type, special variant, composite structure, and high-level intent.
  Fail/waste condition: O1 is lowered for trend error, value error, text overlap, color, font, crop, or layout when the O1 rubric does not define them as intent.
  Reason style: State whether the chart type and variant were reproduced.

- Pattern: Rubric repair before scoring
  Pass/choose condition: Machine rubrics are checked against GT and repaired if inaccurate, vague, wrong-dimension, or missing a key difference.
  Fail/waste condition: Scores are filled using obviously wrong or incomplete machine rubrics.
  Reason style: Say what rubric point was missing or corrected.

- Pattern: O1 zero still complete fields
  Pass/choose condition: Overall is set or checked as zero when O1 is zero, but all remaining fields are still scored and reasoned.
  Fail/waste condition: O2/O3 or pairwise fields are skipped because O1 is zero.
  Reason style: Keep O1 zero explanation concise, then continue scoring evidence.

- Pattern: Full rubric coverage
  Pass/choose condition: The judgement considered every applicable rule family for the item, including prompt fit, layout, element completeness, content accuracy, visual details, hallucination control, broken images, and function checks when functions are part of the task.
  Fail/waste condition: The judgement focused only on the latest user correction or one visible detail while ignoring higher-priority applicable rules.
  Reason style: Keep the reason grounded in the main deciding evidence.

- Pattern: Strict point scoring from enlarged images
  Pass/choose condition: GT, image1, and image2 are inspected as separate/enlarged images, and each rubric score is based on direct comparison of the corresponding element or region.
  Fail/waste condition: A score of `1` is given because the image is generally similar, despite visible coordinate, label, layout, color, text, or style differences in that rubric.
  Reason style: Use `完全一致/准确` only for true matches; use `基本保留/有偏差/不完全一致` for `0.5`; use `缺失/错误/严重偏离` for `0`.

- Pattern: User wording constraints
  Pass/choose condition: The submitted reason follows active punctuation and tone constraints in `user-style.md`.
  Fail/waste condition: The reason uses formal audit language, extra punctuation, or a copied template that conflicts with the user's requested style.
  Reason style: Natural, compact, colloquial Chinese, with comma-only clause breaks when that preference is active.

Format:

- Pattern: <task or situation>
  Pass/choose condition: <what is enough>
  Fail/waste condition: <what is not enough>
  Reason style: <preferred wording>
