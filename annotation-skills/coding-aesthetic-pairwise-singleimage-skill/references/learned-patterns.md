# Learned Patterns

Add reusable user corrections here. Do not store one-off item details.

## Starter Guardrails

- Pattern: Screenshot-only scope
  Pass/choose condition: The judgement is based only on visible screenshot aesthetics.
  Fail/waste condition: The judgement relies on testing interactions, hidden code, or assumptions about functional completeness.
  Reason style: Mention visible layout, color, material, readability, or scenario fit.

- Pattern: Full aesthetic rubric coverage
  Pass/choose condition: The judgement checks waste, page purpose, fatal visible defects, layout, color/type, material quality, and consistency.
  Fail/waste condition: The judgement focuses only on one recent correction or one small visual detail.
  Reason style: Keep the reason grounded in the main deciding visible evidence.

- Pattern: Same discipline
  Pass/choose condition: Same is preferred when both sides are genuinely close, have comparable flaw severity, or no obvious objective quality gap exists.
  Fail/waste condition: Same hides a clear winner on fatal defects, core readability, layout hierarchy, material completeness, or scenario fit.
  Reason style: Use Same reasons when no stable preference exists and do not force A or B.

- Pattern: Objective defect based reasons
  Pass/choose condition: A winner is supported by concrete visible defects on the weaker side, such as cluttered hierarchy, weak alignment, low contrast, poor readability, inconsistent style, or unbalanced spacing.
  Fail/waste condition: The judgement relies on vague taste, richer content, fewer elements, or element quantity without explaining the resulting visual problem.
  Reason style: State the observable design issue directly and keep quantity comments only when they explain clutter, imbalance, or missing visual support.

- Pattern: User wording constraints
  Pass/choose condition: The submitted reason follows active punctuation and tone constraints in `user-style.md`.
  Fail/waste condition: The reason sounds formal, over-polished, copied, or unsupported by the screenshot.
  Reason style: Natural, compact Chinese.

## Format

- Pattern: <task or situation>
  Pass/choose condition: <what is enough>
  Fail/waste condition: <what is not enough>
  Reason style: <preferred wording>
