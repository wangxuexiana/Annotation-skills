# GSB Manual Summary

Source manual: `草图生成网页 GSB 评价标准（对外）`.

## Task Definition

Given one user prompt and one or more sketch/reference images, compare candidate webpage A and candidate webpage B. Output `A 更好`, `B 更好`, or `Same`.

The goal is not pixel-copying the sketch and not free design. The output should translate a low-fidelity sketch into a structurally correct, information-complete, visually finished webpage.

Core口径: 指令优先，草图约束布局与信息结构；在不违背草图核心结构的前提下，将低保真草图产品化为正常、美观、可读的网站。

## Priority Checklist

1. **P0 渲染有效性**: white screen, no content, broken HTML, or invisible main body loses strongly.
2. **P1 指令遵循**: style, color, element count, specified copy, default state, interaction, and restrictions from prompt.
3. **P2 草图布局与空间关系**: module order, page sections, element positions, alignment, proportions, hierarchy, first-screen visible content.
4. **P3 元素完整性**: core sections, navigation, cards, buttons, forms, icons, charts, image placeholders, labels, status elements.
5. **P4 内容准确性与语义完整**: titles, buttons, labels, numbers, task text, image semantics, chart trend/meaning.
6. **P5 交互可用性与状态反馈**: only for interactive review; core controls should work and give stable feedback.
7. **P6 视觉完成度与美观**: color, font, spacing, hierarchy, component consistency, product polish.
8. **P7 幻觉与不相关内容控制**: large unrelated blocks, popups, ads, wrong navigation, irrelevant material, or sketch notes kept as UI.

## Annotation Page Dimensions

On a live GSB annotation page, judge every visible row, not only the overall row.

- Always include `整体`.
- Include each page-defined dimension exactly as displayed, such as `rendering`, `O1`, `O2`, `O3`, `S1`, `O2S1`, or custom names.
- Use the rubric text shown beside that dimension as the local judgment standard.
- Give `A 更好`, `B 更好`, or `Same` for each row.
- Write a separate concise reason for each row with concrete evidence.
- Do not skip lower rows just because the overall winner is clear.

Typical row meanings:

- `整体`: combined judgment across major dimensions.
- `rendering`: whether the page renders normally; no white screen, no missing main content.
- `O1`: usually instruction following or whether named core modules exist.
- `O2`: often text/content accuracy, numbers, labels, card text, chart meaning.
- `O3`: often layout, left-right structure, alignment, overlap, proportion.
- `S1`: visual style, color, button/card style, typography, polish.
- `O2S1`: small content and visual elements, such as tags, icons, status dots, progress bars.

## Text Handling

- Clear core text: preserve or translate accurately according to prompt.
- Clear but non-core small text: semantic similarity is enough.
- Blurry or unreadable text: do not invent exact original text; use reasonable page-themed copy.
- Prompt-specified text overrides sketch text.
- Sketch annotations, red bubbles, arrows, handwritten notes are usually design instructions, not final UI.

## Interactive Review

Static GSB judges default visible state only. Interactive review may test core operations:

- sorting, filtering, tab switch, form validation, save button enablement, checkbox multi-select, batch action, modal, hover, sticky header;
- visible state changes in the sketch such as selected, active card, expand/collapse, owner bubble, status switch;
- natural visible controls such as button click, input focus, dropdown expansion, card hover, navigation switch.

Evaluate whether controls are discoverable, triggerable, semantically correct, clearly fed back, and do not break the page.

Core interaction failure can decide the winner. Minor hover or decorative animation should not override major prompt/layout/content differences.

## Common Disputes

### More Sketch-like But No Text

If the task asks for a normal webpage, a side with only empty boxes or missing core text should not win just because its outline resembles the sketch. Prefer the side that keeps main layout while providing readable content.

### Red Notes Or Handwritten Markups Kept

Usually a penalty. Convert annotation intent into normal UI, such as turning `Owner: Mike` into an owner label or bubble.

### Sketch Text Unclear

Do not require exact reproduction of unreadable small text. Penalize only when clear core titles, buttons, key numbers, or field labels are wrong or missing.

### Structure Accurate But Not A Normal Webpage

Structure matters, but the result should still be a usable webpage, not a sketch copy or unfinished prototype.

### More Beautiful But Structure Wrong

Do not choose a visually prettier side if it clearly violates core layout, module count, or page sections.

### Both Sides Bad

Choose `Same` when both sides deviate a lot and neither clearly better meets the core goal.

### Static Better But Core Interaction Broken

In interactive review, if one side is slightly less polished but has correct required interaction while the prettier side's core interaction fails, prefer the functional side.

## Point-wise Indicators

- **O1 指令遵循**: 5 fully meets explicit requirements; 3 mostly right but visible hard-requirement/style deviations; 1 largely conflicts; 0 unrelated.
- **O2 布局与空间关系**: 5 very close layout/order/proportion; 3 core skeleton maps to sketch but noticeable differences; 1 only local fragments; 0 no layout.
- **O3 元素完整性**: 5 all core blocks and components present; 3 main modules present but secondary items missing; 1 only partial page; 0 no content.
- **O4 内容准确性与语义完整**: 5 core text/labels/numbers/image/chart meaning accurate; 3 local semantic errors but main info recognizable; 1 much fake/garbled/unrelated content; 0 no content.
- **O5 网页正常性与产品化完成度**: 5 complete, readable, product-like page; 3 usable but prototype-like; 1 sketch outline/fragments; 0 broken.
- **O6 交互可用性与状态反馈**: 5 core interactions work with clear feedback; 3 basic chain works but result/feedback unstable; 1 mostly static decoration; 0 unusable.
- **S1 视觉还原度与美观完成度**: 5 high visual completion after satisfying instruction/structure; 3 correct structure but weak polish; 1 almost no webpage completion; 0 unrelated.

## Reason Phrase Pool

Use these as phrase pools, not fixed outputs. Rewrite based on current evidence.

- `A 的主体分区和草图更一致，B 把核心模块顺序打乱`
- `B 更像正常网页，A 只有空框且缺少核心文字`
- `A 满足黑金配色要求，B 仍保留草图批注颜色`
- `B 的导航、卡片和按钮更完整，A 少了关键操作区`
- `A 的核心标题和数字更准确，B 有明显无关文案`
- `B 的表单校验能触发，A 点击后没有有效反馈`
- `A 结构更准，B 虽然好看但模块数量不符合草图`
- `Same，两侧都缺少主要内容，没有明显一侧更接近`

## Skill Evolution

When repeated GSB cases appear, add concise learned patterns here only if they are stable or user-corrected:

- sketch type or webpage type;
- decisive pass/fail or A/B preference signal;
- common reason wording variations;
- important exceptions.

Do not add one-off details. Keep examples varied so later reasons do not sound templated.
