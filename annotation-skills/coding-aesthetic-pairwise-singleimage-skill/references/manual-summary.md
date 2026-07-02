# Manual Summary

Source: `https://bytedance.larkoffice.com/wiki/Km1NwuQ4Aio91ckSKs1cnNLcnzb`

Title: Coding美观度pairwise标注手册-SingleImage

Fetched metadata: underlying object type `docx`, object token `BbETdSIt2oMNvOxAloxcJNZAnOh`, updated at 2026-06-11 08:21:39 UTC.

## Official Scope

The task asks annotators to compare two single screenshots of generated webpages and decide which one is more aesthetically pleasing. The page purpose must first be inferred from the screenshot content and layout. All scoring should focus on aesthetics only.

The 2025-05-18 rule iteration in the manual says:

- Only judge webpage aesthetics from screenshots.
- Do not consider function interaction or completeness.
- If the screenshot is not enough to judge, mark the item as waste/abandoned and add a note.

## Platform And Compliance Notes

- The manual says the task is short and quality-sensitive; careless annotation can affect settlement and staffing.
- A claimed item releases after 60 minutes if not handled.
- Returned/rework data releases after 18 hours if not handled.
- Waste data is not settled.
- The manual explicitly says AI must not be used to polish dimension comments or assist scoring. This skill must preserve a human-confirmation gate and must not be used to secretly auto-score or auto-submit against the platform rule.
- The manual references external Base tables for special cases, Q&A, and high-frequency errors. The embedded cite tokens could not be read as valid Base tokens through the available CLI, so those tables are listed as follow-up sources rather than incorporated as rules.

## Evaluation Flow

1. Decide whether the data is waste.
2. If it is judgeable, infer the page target or scenario.
3. Compare both screenshots against the inferred target.
4. Apply the three core principles before the detailed dimensions.
5. Compare four dimensions and produce the final pairwise judgement.
6. Avoid forcing a preference when differences are small.

## Waste Rules

Mark waste/abandoned before normal judgement if:

- The screenshot cannot support an aesthetic conclusion.
- The first frame is insufficient.
- The original screenshot has quality problems.
- The screenshot is obviously badly captured.
- There is too little visible information to judge aesthetics.
- The page is white screen, black screen, garbled, erroring, or otherwise not visually judgeable.

When the platform requires special-case maintenance, record such cases in the special-case table.

## Core Principle 1: Fatal Defects Beat Minor Flaws

Visible usability defects have the highest priority even though the queue is aesthetic. Fatal defects should heavily lower the judgement:

- Core button cannot be recognized.
- Core text cannot be read normally.
- Key image is broken or failed to render.
- Core material is blocked or covered.
- Large placeholder areas remain unloaded or unreplaced.

Minor flaws should not dominate the decision:

- Footer text, copyright text, and auxiliary small copy can be tolerated when slightly small or fuzzy.
- Small non-core blur or type size issues should be treated as minor unless they affect the user's main reading path.

## Core Principle 2: Scenario Fit Beats Personal Taste

Judge whether the design fits the page purpose, target users, and usage scenario. Do not apply one fixed aesthetic style to all pages.

Examples:

- Financial or analytics dashboards can be dense when that helps data clarity and scanning.
- Children's education pages can reasonably use bright and rich colors.
- A page that is merely content-heavy is not automatically better.
- A page that is merely sparse is not automatically cleaner or more premium.
- If each side has comparable strengths and weaknesses with no stable preference, choose Same.

## Core Principle 3: Ambitious High-Quality Execution Beats Safe Emptiness

High-quality design can combine rich content, multiple components, good materials, and polished detail while keeping the page unified. Such designs should beat conservative pages that are merely empty, single-element, or "not wrong".

Do not mistake empty content, single elements, or monotonous layout for clean design.

## Dimension 1: Layout And Information Hierarchy

Check:

- Whether the layout guides the user toward the core task.
- Whether primary and secondary information are separated by size, position, and spacing.
- Whether whitespace is comfortable and appropriate for the page type.
- Whether elements follow grid alignment.
- Whether the main body is centered reasonably.
- Whether cards, columns, and split layouts are symmetric and balanced.

Visible layout shift, asymmetric card groups, uneven spacing, off-center bodies, or unclear hierarchy should lower the side's aesthetic quality.

## Dimension 2: Color And Typography

Check:

- Whether color and font choices match the page positioning.
- Whether text-background contrast supports normal reading.
- Whether core text such as headings, buttons, navigation, and body content is readable.
- Whether the palette is harmonious rather than clashing.
- Whether colors have quality and restraint.

Deduct for:

- Core text and background colors being too close.
- Abrupt color blocks or harsh red-green conflicts.
- Adjacent areas jumping between incompatible colors.
- Large areas of pure red, pure blue, neon, vivid purple, or other high-saturation colors that look harsh or cheap.
- Multiple high-saturation colors creating color overload.

Prefer lower-saturation, gray-toned, coherent palettes when appropriate to the page.

## Dimension 3: Image, Icon, And Material Quality

Rendering integrity is a serious-defect check. Deduct heavily for:

- Broken images or image loading failure.
- Empty placeholders or blank image areas.
- Partially loaded images.
- Color distortion or severe blur.
- Overlays, popups, navigation, or floating elements blocking core content.
- Unreplaced solid-color or gray placeholder images.

Positive evidence:

- Materials match the theme.
- Images are high-quality and clear.
- Visual style is unified.
- High-quality real photos or polished illustrations generally beat pages that rely only on simple icons or native emoji.

## Dimension 4: Consistency And Detail Polish

Check:

- Whether buttons, cards, forms, icons, and other elements share a unified design language.
- Whether same-type components have consistent size.
- Whether detail treatment is coherent across the page.

Inconsistent button/card styles, uneven component sizes, or mixed visual languages reduce aesthetic quality.

## Pairwise Scoring

Use:

- `-1`: Model 1 is more aesthetically pleasing.
- `0`: Both are basically equal.
- `1`: Model 2 is more aesthetically pleasing.

Choose the side with clearer layout logic, better hierarchy, stronger scenario fit, more harmonious color and type, better material quality, and more consistent detail polish.

Choose Same when:

- The two screenshots have no obvious aesthetic difference.
- Both have similar strengths and weaknesses.
- Both are too simple or basic to distinguish from an aesthetic standpoint but still judgeable.

Do not use Same when one side clearly wins on a higher-priority dimension such as fatal defects, layout hierarchy, core readability, material completeness, or scenario fit.

## Appendix Examples Distilled

- Minimal portfolio: a side can win by using more novel color and type while preserving overall simplicity.
- Retro cassette player: a side can win by better matching the prompt's required retro style.
- Restaurant ranking page: if one side has compressed or incomplete images and the other has some whitespace issue, Same or the less-broken side can be reasonable depending on severity.
- Low contrast corner text alone does not always override a stronger overall page when it is not core content.
- The manual highlights color-abuse cases: harsh or excessive color use is a recurring defect.
