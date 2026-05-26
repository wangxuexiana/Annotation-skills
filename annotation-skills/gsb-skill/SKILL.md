---
name: gsb-skill
description: GSB pairwise review rubric for sketch/low-fidelity wireframe to webpage tasks. Use when Codex needs to compare candidate webpage A and B against a user prompt plus one or more sketch/reference images, choose A better, B better, or Same, verify limited interactions when available, and write a concise natural Chinese reason with concrete evidence.
---

# GSB Skill

## Goal

Compare two candidate webpages generated from the same prompt and sketch/reference image. Choose `A 更好`, `B 更好`, or `Same`.

This skill is for sketch-to-web GSB tasks, not SFT game pass/fail tasks. Do not use the SFT rule "basically playable means pass" here. The target is a normal, readable, product-like webpage that follows the user instruction and preserves the sketch's core layout and information structure.

When operating in a live annotation page, inspect and report unless the user explicitly asks to submit. Do not click final submit, receive, authorize, or other state-changing controls without confirmation.

## Live Annotation Workflow

- Compare the two model outputs directly inside the current annotation webpage. Use the page's own model tabs or toggles, such as `模型一` and `模型二`, to switch between candidates.
- Do not open candidate output pages in new tabs or new windows just to inspect them. Treat `新窗口打开` links as off-limits unless the user explicitly asks for that.
- Keep the current task page as the source of truth for prompt, reference image, dimensions, rubrics, existing selections, and candidate previews.
- When the user says only to do the GSB question or not to submit, fill or report the judgments and reasons only. Do not click `提交`, `继续下一题`, receive, authorize, or other state-changing controls.

## Review Flow

1. Read the user prompt and identify hard requirements: style, color, element count, copy, default state, interaction, and restrictions.
2. Inspect all reference sketches. If there are multiple images, decide whether they represent states, viewports, pages, or detail supplements.
3. Read every dimension shown on the annotation page, including `整体` and each rubric row such as `rendering`, `O1`, `O2`, `O3`, `S1`, `O2S1`, or any custom dimension.
4. Compare A and B for each visible dimension separately and write a reason for each one. Do not only give the overall result.
5. For each dimension, use that row's rubric text as the local standard, while still following the priority order below for conflicts.
6. Compare A and B by the priority order below. Stop within a dimension when an earlier high-priority gap clearly decides that dimension.
7. For static GSB, judge visible default state only. Do not assume hidden interactions work or fail.
8. For interactive human review, verify only core interactions from the prompt, sketch, or natural visible controls.
9. Use `Same` when both sides are close, equally good, equally poor, or trade off without a clear winner.
10. Write concise Chinese reasons with concrete, locatable evidence points.

## Dimension-by-Dimension Output

For live annotation pages, output all visible dimensions. The overall row is required, and every rubric row on the page is required. If the page uses different dimension names, preserve the page's names.

Use this format:

```text
整体：B 更好
B 的深色风格和右侧卡片组更接近参考，A 页面过亮且主标题发虚。

rendering：Same
两边都能正常渲染，没有白屏或主体缺失。

O1：Same
两边都有顶部标签、主标题、特性标签、操作按钮和右侧卡片组。
```

When judging each row:

- `整体`: summarize the most important differences across dimensions.
- `rendering`: only compare whether each side renders effective content without white screen, missing body, or broken page.
- `O1` / instruction or module completeness rows: compare the exact modules named in the page rubric.
- `O2` / content rows: compare title, copy, labels, numbers, chart or card text named in the rubric.
- `O3` / layout rows: compare layout structure, alignment, overlap, proportions, and spatial relationship named in the rubric.
- `S1` / visual rows: compare color, typography, button/card style, visual hierarchy, and polish named in the rubric.
- Combined rows such as `O2S1`: compare the small elements named in the row, such as tags, icons, status dots, progress bars, and microcopy.

Do not skip a row because the overall winner is already clear.

## Priority Order

Use this order. Earlier items override later ones when the gap is clear.

1. **Rendering validity**: white screen, no effective content, invisible main body, broken HTML, or unusable page is significantly worse.
2. **Instruction following**: explicit prompt requirements for style, color, element count, copy, state, and restrictions are high priority.
3. **Sketch layout and spatial relationship**: module order, sections, positions, alignment, proportions, visual hierarchy, and first-screen content should match the sketch's intent.
4. **Element completeness**: core sections, navigation, cards, buttons, forms, icons, charts, image placeholders, labels, and states should appear.
5. **Content accuracy and semantic completeness**: clear titles, buttons, labels, numbers, task text, image meaning, and chart meaning should be correct or reasonable.
6. **Interaction usability and state feedback**: only for interactive review. Core interactions should be discoverable, triggerable, semantically correct, clearly fed back, and not break layout.
7. **Visual completion and aesthetics**: compare color, font, spacing, hierarchy, component consistency, and product polish only after instruction, structure, and content are close.
8. **Hallucination and irrelevant content**: penalize large unrelated blocks, ads, popups, wrong navigation, irrelevant assets, or sketch annotations treated as final UI.

## Key Principles

- Instruction first. If the prompt clearly specifies style, color, number, text, or state, prioritize it over minor sketch details.
- Sketches constrain layout and information structure. They do not always require pixel-level copying.
- Convert low-fidelity sketches into normal webpages unless the prompt asks to preserve hand-drawn or wireframe style.
- Do not keep red notes, arrows, handwritten labels, or temporary sketch annotations as final UI unless the prompt explicitly asks for them.
- Clear core text should be preserved or translated according to the prompt. Blurry small text may be reasonably filled in.
- A side that is more beautiful but structurally wrong usually should not beat a side that follows prompt and sketch structure.
- A side that looks more like the sketch but lacks text, semantics, or webpage completion may lose to a more product-like side with similar structure.
- Overall impact matters more than counting differences. Main module loss, hard instruction conflict, and broken rendering outweigh small icon, spacing, or border differences.
- GSB is not a pixel-level spot-the-difference task. Do not force a winner for tiny spacing, color, font, or alignment differences unless they clearly affect the intended layout, content, visual hierarchy, or user experience.

## Same Rules

Choose `Same` normally when:

- A and B are equally good with only small detail differences.
- A and B are equally bad and neither better serves the core goal.
- One side has slightly better layout while the other has slightly better visual/content quality, and the overall gain is close.
- Both are far from the prompt/sketch to a similar degree.
- Differences are visible but not meaningful enough to affect the GSB outcome, such as minor pixel-level spacing, near-identical colors, or small typography variations.

Do not force a winner just because a tiny difference exists.

## Interactive Review

Only test limited core paths:

- User-explicit interactions: sorting, filtering, tab switching, form validation, save button enabling, checkbox multi-select, batch actions, modals, hover, sticky header.
- Sketch-expressed state changes: selected state, active card, expand/collapse, owner bubble, status switch.
- Natural visible controls: button click, input focus, dropdown expansion, card hover, navigation switch.

Interaction failures matter most when interaction is a core requirement. Do not let a minor hover animation override major differences in prompt, layout, content, or visual completion.

## Reason Style

Write plain Chinese, one sentence when possible. Use concrete evidence, not empty praise. Prefer 20-45 Chinese characters unless the comparison needs slightly more.

When writing reasons in annotation text boxes, use Chinese commas or normal commas for separation. Do not use colons, semicolons, or Chinese enumeration commas as separators, including after `A 更好`, `B 更好`, or `Same`.

For `Same` judgments, do not call out minor detail differences just to explain why they are minor. Use varied natural wording that means neither side clearly pulls ahead, with brief shared evidence. Do not repeat the exact same phrase for every row.

In annotation text boxes, do not repeat the selected GSB label or winner at the start of the reason. The dropdown already records `Same`, `Bad`, `Good`, `A 更好`, or `B 更好`. Write only the evidence and judgment basis.

Good reason shapes:

- `模块顺序和草图更接近，三张卡片也完整保留`
- `整体是正常网页，A 只保留空框且缺少核心文字`
- `两侧主体布局都偏差较大，没有明显一侧更接近`
- `两侧核心模块都完整，视觉效果无明显差距`
- `两边内容都完整，默认状态下难以拉开差距`
- `两侧都能满足这一项，没有一边明显更好`
- `黑金配色符合要求，B 保留了草图红色批注`
- `表单字段和按钮更完整，A 缺少关键提交区`
- `排序按钮点击后能重排，B 只是静态装饰`

Avoid:

- `A 更美观`, `B 更接近`, `整体更好` without evidence.
- Colons, semicolons, and Chinese enumeration commas in reasons, such as `B 更好：...`, `A 偏宽；B 更准`, `标题、正文、按钮`.
- Same reasons that over-explain tiny differences, such as `差异属于细节差距`, when a natural no-clear-winner wording is enough.
- Repeating the same Same wording in every row, such as using `无明显差距` mechanically for all dimensions.
- Repeating the dropdown result in the reason, such as `Same，...`, `B 更好，...`, or `A 更好，...`.
- Long formal audit language.
- Overusing the same sentence pattern across nearby tasks.
- Copying prompt-specific names unnecessarily when a normal phrase is clearer.

## References

- Use [manual-summary.md](references/manual-summary.md) for the full condensed rubric, common dispute cases, point-wise indicators, and self-update rules.
