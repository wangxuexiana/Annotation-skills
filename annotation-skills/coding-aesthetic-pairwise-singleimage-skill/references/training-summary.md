# Training Summary

Source manual: Coding美观度pairwise标注手册-SingleImage, Lark Wiki `Km1NwuQ4Aio91ckSKs1cnNLcnzb`, fetched 2026-06-11.

## Task Type And Target Queue

- Queue type: Coding aesthetic pairwise, SingleImage.
- Input: one screenshot for model 1 and one screenshot for model 2, plus the prompt and platform fields.
- Required output: inferred page purpose dropdown, pairwise overall judgement, and concise reason.
- Judgement labels:
  - `-1`: model 1 is more aesthetically pleasing.
  - `0`: both are basically equal, or the visible evidence cannot support a stable preference while still being judgeable.
  - `1`: model 2 is more aesthetically pleasing.

## Core Operating Rule

This queue is screenshot-only. Judge visible webpage aesthetics from the single screenshot. Do not test functionality, interaction completeness, hidden code, or full product behavior. If the screenshot itself cannot support an aesthetic judgement, mark the item as waste/abandoned and explain why.

The manual also states that AI must not be used to polish dimension comments or provide auxiliary scoring. Treat that as a submission gate: use this skill for learning, checklist support, and human-reviewed drafting only unless the user confirms the platform policy and their intended use.

## Workflow

1. Check whether the item should be abandoned before comparing aesthetics.
2. Infer the likely page purpose from content and layout, such as SaaS landing page, dashboard, blog article, ecommerce product page, game page, education app, or portfolio.
3. Compare the two screenshots under the inferred purpose.
4. Apply the three core principles:
   - Fatal visible defects outweigh minor cosmetic flaws.
   - Page goal and scenario fit outweigh personal taste.
   - Ambitious, rich, well-executed design can beat safe but empty minimalism.
5. Compare the four dimensions:
   - Layout and information hierarchy.
   - Color and typography.
   - Image, icon, and material quality.
   - Consistency and detail polish.
6. Use Same only when the visible evidence is genuinely close or the two sides have comparable problem severity.
7. Fill the page purpose, label, and reason. Pause before final submission unless explicitly authorized.

## Waste And Abandon Rules

Mark waste/abandoned when the screenshot cannot support an aesthetic judgement, including:

- The first screenshot view is insufficient to judge aesthetics.
- The screenshot was captured badly, is severely cropped, or contains too little information.
- White screen, black screen, obvious error page, garbled text, or rendering failure.
- The visible page is so incomplete that the aesthetic comparison would be speculation.

Waste data is not normally scored and should be recorded in the special-case table when the platform requires it.

## Easy-To-Misjudge Cases

- Do not judge function implementation. This queue only sees screenshots.
- Do not force a winner when the difference is small or both sides have similar flaws.
- Do not equate sparse content with good minimalist design.
- Do not equate rich content with good design; richness must still be coherent, polished, and scenario-fitting.
- Do not punish dense dashboards merely for having less whitespace when the density improves data reading.
- Do not punish colorful children's education pages merely for being colorful when the style fits the audience.
- Do not over-penalize non-core footer text or auxiliary small copy that is slightly small or fuzzy.
- Do heavily penalize unreadable core text, broken key images, blocked core content, unreplaced placeholders, or obvious failed rendering.

## Reason Style

- Keep reasons short, concrete, and based on visible differences.
- Prefer natural Chinese wording.
- Mention the deciding evidence, such as layout hierarchy, scenario fit, color readability, material quality, or consistency.
- Do not add polished rhetorical language or unsupported dimension-by-dimension filler.
