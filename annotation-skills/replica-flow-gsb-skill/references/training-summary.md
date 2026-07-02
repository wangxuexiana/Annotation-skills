# Training Summary

## Task And Queue

- Task family: GSB pairwise review for generated web pages against a user prompt plus a reference image.
- Covered queues:
  - Sketch-to-webpage GSB: `RFT人标支持 GSB 评估-草图复刻（盲审模式）7646617432569024266`
  - Webpage-replica GSB: `RFT人标支持 GSB 评估-网页复刻（盲审模式）7646455196222557961`
  - Flowchart-to-webpage GSB: `RFT人标支持 GSB 评估-流程图复刻（盲审模式）7648851418979831602`
- Source materials:
  - Training minutes: https://bytedance.larkoffice.com/minutes/obcn4f8w921l399ngo4kmzby
  - Sketch/webpage manual: https://bytedance.larkoffice.com/wiki/WXJMw60FQioCo7kEvZzcQFIAnMg
  - Flowchart manual: https://bytedance.larkoffice.com/wiki/HbRzwxNetiwn5ZkEDBwcF3L1nlf

## Workflow State

- Current workflow state: `可标注`. The materials were collected and distilled into a task-specific skill.
- Default submission policy: ask the user before final annotation submission unless the user explicitly authorizes auto-submit for this queue.

## Core Task Shape

For the same user prompt and same reference image, compare model A and model B web outputs. Choose:

- `A good B`: A is better than B.
- `A bad B`: B is better than A.
- `A same B`: A and B are close in overall quality, equally good, equally bad, or have balanced key tradeoffs.

Do not assign numeric scores. The label is a pairwise judgement.

## Browser Test Flow

1. Read the user prompt first.
2. Identify whether the prompt has explicit function or interaction requirements.
3. Inspect the reference image type: sketch, webpage screenshot/design, or flowchart.
4. Switch between model A and model B outputs on the task page.
5. Open each candidate in a full new page or new window when the embedded preview is too small or incomplete.
6. For mobile screenshots or mobile-app-like pages, use mobile viewport inspection when needed.
7. Test only prompt-named core interactions and natural controls needed for judgement.
8. Return to the task page and fill one GSB label plus a concise reason.

## Decision Priority

Use different priority stacks by task type.

Sketch-to-webpage:

1. Layout restoration: module count, sections, relative positions, hierarchy, information flow.
2. Content filling: placeholders, gray blocks, fake text, image boxes, annotations replaced by realistic topic-specific content.
3. Productized completion: color, font, spacing, radius, shadow, images, icons, high-fidelity webpage feel.
4. Prompt style requirements: brand, color, industry style, state requirements.
5. Prompt-named functions only when explicit.

Webpage-replica:

1. Layout and spatial relationship against the reference.
2. Element completeness.
3. Content accuracy.
4. Visual restoration: color, font, type size, weight, radius, shadow, border, background, texture, whitespace, hierarchy.
5. Hallucination control: avoid adding unrelated modules, ads, popups, navigation, images, or copy.
6. Prompt-named functions only when explicit.

Flowchart-to-webpage:

1. Flow semantics: core nodes, paths, branches, states, inputs, outputs, constraints.
2. Web productization: convert process meaning into real UI, not a redrawn flowchart.
3. Interaction chain: user actions, state transitions, mock requests, success/failure feedback.
4. Information architecture: current state and next action are understandable.
5. Visual completion only after the above are close.

## Function Requirement Rule

Only evaluate real function or interaction when the user prompt explicitly asks for verifiable behavior, such as:

- Clicking a button opens or closes a modal.
- Tabs switch content.
- Email field validates format.
- Sorting changes order.
- Filters update results.
- Checkboxes support multi-select and batch actions.
- Hover reveals details or visible feedback.
- Desktop/mobile responsive adaptation is required.

When the prompt only says to replicate a page, make a webpage from a sketch, or restore the reference image without explicit behavior:

- Do not test or reward hidden real functionality.
- Do not inspect source code to infer functionality.
- Treat buttons, nav, forms, hover states, and visual states as visual elements only.
- Judge by visual restoration or productization quality.

## Flowchart-Specific Rule

Flowchart tasks are not about drawing the flowchart itself. A candidate should implement the product experience behind the process:

- Use forms, wizards, dashboards, lists, detail areas, modals, status cards, result pages, role switches, and feedback states as appropriate.
- If the flow includes backend APIs, persistence, login, payment, notifications, or third-party services, front-end mock behavior is enough when it shows reasonable loading, success, failure, request, and response states.
- If the flow contains multiple steps or roles, implement corresponding multi-step UI and state transitions so a user can complete the process end to end.

## Easy-To-Misjudge Cases

- Do not give extra credit for functions the prompt did not request.
- If extra functions hurt visual restoration or flow clarity, count them as negative.
- If one side looks prettier but misses a prompt-named core function, prefer the other side when its visual quality is still acceptable.
- If one side has more interactions but misunderstands the flow semantics or misses key paths, it cannot win on interaction count.
- In webpage replica tasks, independent beauty does not beat reference-image fidelity.
- In sketch tasks, a polished webpage is expected; keeping wireframe, pencil, gray-box, or placeholder style is negative unless the prompt explicitly asks for that style.
- In flowchart tasks, redrawing nodes and arrows is usually negative when it replaces the real product flow.
- If both candidates fail, still choose the relatively better side unless their key failure impact is close.
- If both candidates are close, compare the more important dimensions first before using visual polish as the tiebreaker.

## Waste Or Abandon Rules

Use platform waste/abandon only when the item cannot be judged, such as:

- Preview or candidate page is blank, white-screen, black-screen, broken, or unrenderable.
- Reference image or prompt is missing or inaccessible.
- Candidate cannot be inspected enough to compare A and B.
- The task page is blocked by login, CAPTCHA, permission, risk control, or platform issue.

When the candidate is bad but still inspectable, use a normal GSB label instead of waste.

## Reason Style

Reasons should be concise Chinese, but more specific than "整体更好" or "更接近". State the winning line first, then give 1-2 visible evidence points.

Preferred structure:

- `A good B。视觉胜出：...`
- `A bad B。功能落败：...`
- `A good B。视觉和功能都胜出：...`
- `A same B：...`
- `A 胜出。...`
- `B 胜出。...`

For flowchart tasks, cite flow nodes, path relations, state feedback, web components, or information architecture. For sketch/webpage tasks, cite layout, content filling, restoration, core function, or hallucinated additions.
