# Stable Annotation Rules

These are shared generic rules for annotation queues generated or operated through `annotation-workflow-skill`.

Task-specific manuals, `references/rule-updates.md`, and explicit user corrections override these generic rules when they clearly conflict.

## Queue Handling

- Only process normal annotation tasks by default.
- Do not process returned or rework tasks unless the user explicitly asks. Skip them first and continue to normal annotation items when possible.
- Do not bypass login, CAPTCHA, access control, platform risk checks, hidden permission gates, or restricted pages.
- Ask before final quiz submission, permission submission, and annotation submission unless the user explicitly authorizes auto-submit for the current queue.

## Waste Or Abandoned Items

- Blank, white-screen, black-screen, broken, or unrenderable previews should be marked as waste or abandoned when the platform supports that label.
- If the preview cannot be inspected enough to judge the core task, prefer waste or abandoned over a normal fail label.
- When an item is not waste or abandoned, do not fill the platform's waste/abandoned reason field unless the queue explicitly requires it.
- When an item is marked waste or abandoned, fill only the waste/abandoned reason when the platform supports that workflow; do not also fill normal rating fields, rubric scores, or normal judgement reasons unless the queue explicitly requires them.

## Judgement Priorities

- Prompt-named core functions outweigh visual polish or a good-looking static shell.
- Official manual rules and newest live updates outweigh older summaries or generic habits.
- Test the prompt-named core functions and natural visible controls before judging.
- Named controls such as sliders, toggles, buttons, generators, drawing tools, counters, camera controls, and similar controls must visibly or textually change something.
- Good-looking static output does not pass if the named core behavior is missing.

## Evidence Source

- Judge only from what is visibly shown on the rendered page unless the task manual explicitly says otherwise.
- Do not use DOM inspection, hidden text, component names, source structure, canvas counts, or internal page metadata as evidence that a feature exists.
- DOM or page inspection may be used only to help open the preview, navigate the task page, or recover from tooling issues.
- If a feature is not visible and does not produce visible or textual feedback, treat it as not demonstrated.

## Audio Handling

- Do not specially evaluate sound, music, audio sync, chimes, alerts, or similar audio effects during annotation unless the task manual or prompt makes audio the only meaningful requested output.
- Do not fail a task only because sound was not verified when visible scene, visible controls, textual state, or visual feedback are enough to judge the core requirement.
- When audio is the central requested output, follow the task-specific manual or queue rule first.

## Browser Flow

- Prefer inspecting videos, scenes, candidates, and previews directly inside the current annotation page when the platform makes them viewable there.
- Do not open a new browser tab or window just to inspect a preview that can be judged on the current page.
- Open a scene, candidate, or preview link in a separate Chrome tab or window only when the current page cannot show enough detail to judge it.
- Test only the prompt-named core functions and natural visible controls needed for judgement.
- Close any extra test tab or window after judging it, then return to the original task page.

## Reason Style

- Reasons should be short, direct, and natural Chinese.
- Most submitted reasons should be one sentence, usually around 25-45 Chinese characters unless the queue explicitly asks for more detail.
- Mention the implemented or missing core function plus the visible feedback or failure. Avoid listing every minor detail.
- For pass reasons, say what works and what visible result or feedback appears.
- For fail reasons, say the one core function that is missing, blocked, or unusable.
- For waste or abandoned reasons, say the page is blank, cannot load, cannot render, or cannot be judged.
- Do not include English words, Latin letters, framework names, code terms, or technical jargon in submitted reasons unless the user explicitly asks for technical detail.
- Use Chinese commas for reason clause breaks. Do not use slashes, colons, semicolons, pause marks, or full stops in submitted reasons.
- Do not add a final period or full stop at the end of submitted reasons.
- Prefer the user's historical answer style when available, but do not copy old answers mechanically.
- Use more colloquial wording for specialized labels when the user prefers it.
- Prefer natural spoken wording over compressed report wording, such as `可以`, `已经`, `没有`, `无法`, `不能`, `点击之后`, and `调节之后`.
- Avoid formal audit or generic assistant phrasing, such as `整体体验完整`, `交互链路闭环`, or `符合预期效果`.
- Use everyday Chinese descriptions for objects, controls, charts, and scene elements when possible. Do not mechanically copy prompt-specific proper nouns or professional labels unless needed for clarity.
- When the user asks for less terse reasons, add a small concrete observation instead of making the reason long. Prefer a `function point + visible feedback or failure` sentence.
- In batches, vary sentence openings and structure. Do not start every pass reason with the same phrase, and rewrite repeated task reasons using current visible evidence.
- Treat historical answers, learned patterns, and reason examples as style anchors or phrase pools, not fixed templates.

## Learning And Pattern Updates

- Add a learned pattern only when the same task type appears repeatedly with a stable rule, or when the user explicitly corrects the judgement rule or reason style.
- Do not add one-off details, task-specific names, accidental UI behavior, or temporary page artifacts to shared or task-specific pattern files.
- Keep each pattern short and practical: task type, core pass condition, core fail condition, and a small set of varied reason examples.
- If a new pattern conflicts with an older pattern, update the older pattern instead of duplicating it.
- Treat pattern examples as phrase pools, not fixed reasons. Rewrite them to fit the current page and avoid repeating the same sentence shape across nearby tasks.
