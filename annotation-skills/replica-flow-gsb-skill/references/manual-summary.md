# Manual Summary

## Shared Pairwise GSB Rules

- Compare model A and model B under the same user prompt and same reference image.
- Use only three labels:
  - `A good B`: A is better.
  - `A bad B`: B is better.
  - `A same B`: overall quality is close, equally good, equally bad, or key tradeoffs are balanced.
- Judge from visible rendered behavior and reference/task evidence. Do not use hidden DOM, source structure, or implementation internals as feature evidence.
- If a prompt-named function exists, test it. If no explicit function is requested, evaluate visual or flow realization only.
- Do not reward extra unrequested functionality. Penalize extra content or behavior when it damages visual restoration, flow semantics, or task relevance.

## Sketch-To-Webpage GSB

### Visual Priority

1. Layout restoration: module count, section division, relative position, hierarchy, and information flow should match the sketch.
2. Content filling: placeholder text, gray boxes, image frames, fake copy, and annotations should become realistic content fitting the prompt topic.
3. Productized completion: color, font, spacing, radius, shadow, images, icons, and page polish should feel like a high-fidelity real webpage.
4. Prompt style requirements: brand, color, industry style, and requested states must be followed.

### Function Priority

Only when the user prompt explicitly requests interactions:

1. Core function exists.
2. Operation chain works.
3. Result is correct.
4. Feedback is visible and stable.
5. The page remains stable after interaction.

### Common Deductions

- Lorem ipsum, Title, Heading, xxx, TODO, Placeholder, and similar placeholders remain.
- Red annotations, arrows, handwritten notes, or sketch explanations appear in the final page.
- Images remain gray boxes, crossed boxes, or "image here" placeholders.
- Page keeps hand-drawn lines, pencil fonts, or wireframe style when the prompt did not ask for draft style.
- Prompt-required core interactions have only visual controls and no real state change.

## Webpage-Replica GSB

### Visual Priority

1. Layout and spatial relationship: page structure, position, size ratio, alignment, spacing, and first-screen content should be close to the reference.
2. Element completeness: core sections, navigation, cards, buttons, icons, images, charts, backgrounds, and decorative elements should be complete.
3. Content accuracy: readable text, numbers, labels, button copy, prices, dates, and chart semantics should match.
4. Visual restoration: colors, fonts, type size, weight, radius, shadow, border, background, texture, whitespace, and hierarchy should be close.
5. Hallucination control: do not add large modules, ads, popups, navigation, images, or unrelated text that the reference lacks.

### Function Priority

Only evaluate functions that the user prompt explicitly requires:

1. Requested clicks, switches, sorting, filtering, validation, submission, responsiveness, and other interactions are covered.
2. Event binding, state change, view update, and result feedback are complete.
3. Reference-state visuals such as modal, hover, active, error, and disabled states should remain close when relevant.
4. Extra interactions must not break restoration.

Important: if the reference image shows hover, modal, selected, or expanded states but the prompt did not ask for a trigger chain, evaluate visual state restoration only. Do not automatically expand it into a function requirement.

## Flowchart-To-Webpage GSB

### Evaluation Priority

1. Flow semantics: cover core nodes, paths, branches, states, inputs, outputs, and constraints correctly.
2. Web productization: convert the flowchart into real webpage or web-app structure. It should not be a flowchart viewer.
3. Interaction chain: user actions, state transitions, mock requests, success/failure paths, and feedback should be verifiable.
4. Information architecture: users should understand current status and next action.
5. Visual completion: compare visual polish and local errors after the first four dimensions are close.

### Flowchart Core Requirements

- The reference flowchart or flow sketch is the requirement source.
- Do not redraw the flowchart as nodes, arrows, swimlanes, tree diagrams, or diagrams instead of implementing the product experience.
- Implement the real user experience behind the flow: pages, forms, dashboards, wizards, tools, result pages, modals, status cards, lists, or detail views.
- Complete interaction chains should include user actions, page states, step changes, validation, loading, success paths, failure paths, and condition branches where relevant.
- Backend APIs, persistence, login, payment, notifications, and third-party services may be mocked in the front end, but the mock should show reasonable request, response, loading, success, and error states.
- Multi-step or multi-role flows should have corresponding UI and state transitions.

### Common Deductions

- Redraws the flowchart instead of building a usable web product.
- Builds only a marketing or introduction page and misses the process operations.
- Ignores condition branches, exceptional paths, failed states, confirmation feedback, or result states.
- Forms, buttons, steps, and tabs exist but do not change state.
- Mock behavior is only conceptual and has no loading, response, success, or failure feedback.
- Multi-role flow lacks role entry, permission difference, or role state switching.
- Copy is unrelated to the flowchart topic or keeps Lorem ipsum, placeholder, TODO, or template text.
- Adds many business modules unrelated to the flowchart or user prompt.

## Choosing A Good B, A Bad B, Or A Same B

- If A is not worse on visual/restoration and function, and one key dimension is clearly better than B, choose `A good B`.
- If B is not worse on visual/restoration and function, and one key dimension is clearly better than A, choose `A bad B`.
- If one side has much better visual quality but the prompt-named core function is unusable, prefer the other side if its visual quality is acceptable and core function works.
- If one side has complete interactions but fails sketch layout, content filling, webpage reference fidelity, flow semantics, or key path coverage, it cannot win by function count alone.
- If one side is only locally prettier but less faithful to the reference or flow, it cannot win.
- If A and B each have strengths and weaknesses with similar key impact, choose `A same B`.
- If both are bad, compare which one better preserves the core requirement. Use same only when failures are similarly severe.

## Reason Writing

Reasons must state the main winning or losing line and include concrete evidence.

Avoid:

- "整体更好"
- "更接近"
- "功能更完整"
- "视觉更好"

Use:

- `视觉胜出：A 的草图布局和内容填充更完整，三列卡片与顶部导航关系更符合草图；B 仍有占位灰块残留。`
- `功能落败：A 视觉略好但排序按钮无实际效果；B 虽然视觉略弱，但排序和多选批量操作都能跑通。`
- `流程胜出：B 覆盖登录、权限校验、提交失败重试和最终通知；A 首屏更美观，但省略失败分支和结果反馈。`
- `A same B：A 的视觉还原略好，B 的 Tab 切换更完整，但两者核心页面结构都成立且短板影响接近。`

## Quality And Risk Notes From Training

- The platform may use blind review and further sampling when A/B/C judgements diverge. Be careful and evidence-based.
- If early items feel ambiguous, annotate a small number first and use user or queue feedback to update `rule-updates.md`.
- When a candidate can only be partially seen in the embedded page, open it in a new page and inspect it fully before judging.
