# Learned Patterns

Add reusable user corrections here.

## Starter Guardrails

- Pattern: Full rubric coverage
  Pass/choose condition: The judgement considered every applicable rule family for the item, including prompt fit, layout, element completeness, content accuracy, visual details, hallucination control, broken images, and function checks when functions are part of the task.
  Fail/waste condition: The judgement focused only on the latest user correction or one visible detail while ignoring higher-priority applicable rules.
  Reason style: Keep the reason grounded in the main deciding evidence.

- Pattern: User wording constraints
  Pass/choose condition: The submitted reason follows active punctuation and tone constraints in `user-style.md`.
  Fail/waste condition: The reason uses formal audit language, extra punctuation, or a copied template that conflicts with the user's requested style.
  Reason style: Natural, compact, colloquial Chinese, with comma-only clause breaks when that preference is active.

- Pattern: 0-score explanation required
  Pass/choose condition: Every rubric marked 0 because a requirement is missing, broken, or not implemented has a short concrete reason in its corresponding explanation field.
  Fail/waste condition: A 0-scored rubric is left without explanation, or the reason only says it is bad without naming the missing or broken requirement.
  Reason style: Briefly name the unmet point, such as 按钮点击后没有变化 or 品牌文字没有随背景适配.

Format:

- Pattern: <task or situation>
  Pass/choose condition: <what is enough>
  Fail/waste condition: <what is not enough>
  Reason style: <preferred wording>

## User Corrections

- Pattern: Current page rubric fidelity
  Pass/choose condition: Before scoring, read the current page's actual rubric names and order, then judge and output those exact rubrics.
  Fail/waste condition: Reusing a generic fixed visual rubric order, such as a repeated six-item template, when the current page shows different rubric names or order.
  Reason style: Use the page's rubric wording as the label, then add concise evidence only where needed, especially for 0 scores.
