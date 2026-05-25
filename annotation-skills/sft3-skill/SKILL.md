---
name: sft3-skill
description: SFT 三期 AIDP/Juejin task review rubric for judging generated web games, interactive demos, UI pages, charts, and similar annotation tasks. Use when Codex needs to inspect an SFT 三期 task page or preview, decide pass/fail, compare with an existing human label, or write a short natural Chinese reason based on whether the core requested function or gameplay is basically implemented.
---

# SFT 三期 Skill

## Goal

Judge only whether the prompt's core function is implemented and basically usable. Do not fail a task for weak polish, imperfect visuals, minor wording differences, or missing edge effects when the main interaction works.

When operating in a live AIDP page, inspect and report unless the user explicitly asks to submit. Do not click final submit, receive, authorize, or other state-changing controls without confirmation.

Be moderately strict about interactions explicitly named in the prompt. If the prompt asks for a slider, toggle, button, drag action, camera control, drawing tool, generator, counter, score, or other adjustable/interactive control, it must produce a visible or textual change when operated. Do not mark `通过` only because the static scene looks close while a named core control has no effect.

Prompt-named functions have higher weight than the visual shell. A good-looking page or scene does not pass if a required named behavior is missing, such as a date-driven calendar that does not update, crossed paths that do not reveal symbols, a closed circuit that does not light LEDs, or a required levitation base/body that is absent. Prefer judging by the working behavior requested in the prompt before judging general visual similarity.

## AIDP Task Priority

Do not process returned/rework (`返修`) tasks. If the current item is marked `返修`, skip it and move to a normal annotation task; do not judge, fill, temporarily save, or submit the returned item unless the user explicitly changes this rule.

If a preview is blank, broken, or cannot render the main content after a reasonable load/retry, choose `废弃` instead of marking ordinary `不通过`. Use a short waste reason such as `页面白屏，无法正常渲染` or `预览无法加载，无法判断核心功能`.

## Review Flow

1. Read the prompt and identify the one or two core requirements.
2. If the current item is marked `返修`, skip it and handle a normal annotation task instead.
3. On the task page, open the preview only long enough to read or extract the scene URL. Do not test inside the preview drawer/modal unless there is no other option.
4. Open the scene URL in a new browser window or new tab and test the page there.
5. After testing, close the separate test window/tab, then return to the original task window to fill the label, reason, waste flag, and submit if the user has authorized submission.
6. First check whether it is basically playable or basically usable according to the production manual.
7. If the preview is blank or cannot render the main content, mark `废弃` and write the direct render/load reason.
8. Test each prompt-named core control at least once. For sliders and toggles, verify the label, value, scene, animation, or object state changes after operation.
9. If a prompt-named core control has no visible/textual effect, mark `不通过` even if the static scene is mostly correct.
10. If the core loop is already basically playable and named core controls respond, mark `通过` without exhaustively testing every secondary feature.
11. If the basic core function is missing, blocked, or cannot be operated, mark `不通过` and write the direct core reason.
12. Ignore boundary decorations and secondary effects unless the prompt makes them the core feature.
13. If comparing with the user's old label, give counts for same/different and mention only meaningful disagreements.

When a task type looks familiar, read [learned-patterns.md](references/learned-patterns.md) and reuse the closest stable pattern. Still inspect the current preview enough to confirm the core condition; do not judge only from the pattern name.

## Pass Standard

Mark `通过` when the main requested experience is present and usable:

- The game can start and respond to input.
- The primary action works, such as moving, jumping, attacking, cutting, shooting, selecting, dragging, drawing, placing, collecting, or answering.
- Prompt-named controls such as sliders, toggles, switches, menus, buttons, and camera operations visibly respond after use.
- The main target can be reached, hit, collected, judged, displayed, or otherwise verified.
- The result may be rough, but the user can tell that the requested feature was implemented.
- Once basic playability is confirmed, stop testing minor or optional functions unless they are clearly part of the core requirement.

Mark `不通过` when the core feature is missing or blocked:

- The game cannot start, cannot be controlled, or gets stuck before the first meaningful step.
- A required key action has no effect.
- A prompt-named slider, toggle, button, generator, or camera control is present but does not change anything observable.
- The first essential obstacle or task cannot be completed, preventing the core loop.
- The visible result is unrelated to the prompt's main request.
- Cosmetic effects exist, but the main requested function does not.

Mark `废弃` when the task cannot be judged because the preview itself is unusable:

- The page is blank, broken, or cannot render the main content.
- The preview fails to load after a reasonable retry.
- The render area shows only an error/loading failure and no usable generated result.

## Scenario Rules

- Fighting: pass if attacking and combat exchange work. Fail if the character cannot attack or combat is unusable.
- Cut-the-rope: pass if the rope swings, can be cut, and the object can reach the target.
- Platform jumping: pass if movement and jumping let the player progress. Fail if the first key obstacle cannot be crossed.
- Block-building or Minecraft-like: pass if moving plus placing, destroying, building, or exploring works.
- Racing: pass if the car can move along the track. Lap counting or polish issues alone usually do not fail it.
- Shooting: pass if aiming, firing, and hitting or damaging targets works. Fail if firing or hitting the core target does not work.
- Physics sandbox: pass if the requested physical interaction runs and reacts.
- 3D scene: pass if the scene loads and the requested viewing or interaction works. Fail if the prompt clearly asks for a key control such as intensity, density, camera, generator, or object toggle and that control has no observable effect.
- UI page or component: pass if the main page, control, form, list, chart, or workflow is usable.
- Animation or particle effect: pass if the core animation or interaction is visible. Fail if the named central effect is absent, such as no visible burst after a required click burst.
- Quiz or choice game: pass if questions, choices, feedback, scoring, or progress work. Fail if options cannot be selected or no answer feedback appears.

## Reason Style

Write reasons in plain Chinese, usually one sentence around 20-35 Chinese characters. Avoid English terms, framework names, and technical jargon. Mention what was implemented and the visible effect, or the one core thing that failed.

When a reason mentions multiple similar implemented or missing items, separate them with Chinese commas, not `/` or slash-like wording. For example, write `温度、密度、颜色调节有反馈` or `广告、列车等核心元素缺失`, not `温度/密度/颜色` or `广告/列车`.

Use natural, user-like wording for specialized features. For EVA or similar professional labels, prefer口语化 descriptions such as `宇航员出舱装备切换有效` or `宇航员穿戴状态能切换`, instead of formal wording like `EVA穿戴有效`, unless the page itself only exposes that exact label.

For the user's preferred wording, read [reason-examples.md](references/reason-examples.md) when writing more than one reason, when the user says the output still sounds like AI, or when judging page/UI/chart tasks. Mimic its direct patterns: `能够...核心功能基本实现`, `无法...无法正常游戏`, `未实现...功能`, `点击...无反应`, `页面...未正常渲染`, `和参考图不符`.

For repeated task types, also read [learned-patterns.md](references/learned-patterns.md) for the judgment rule and wording direction. Do not copy its reasons as fixed templates. Rewrite the reason based on the current page, changing the sentence shape and concrete details so repeated tasks do not sound identical.

Vary sentence openings in batches. Do not start every pass reason with `能够`; mix ordinary wording such as `实现了`, `可以`, `能正常`, `点击后`, `页面有`, `角色可以`. For game reasons, avoid copying prompt-specific names that sound artificial; prefer generic words like `角色`, `人物`, `车辆`, `敌人`, `目标`, `碎片`, `障碍物`, or `关卡` unless the specific name is needed to explain the issue.

Avoid template repetition. If several recent reasons used the same structure, change the next one by varying:

- the verb: `能`, `可以`, `实现了`, `支持`, `点击后`, `页面有`, `已经有`
- the subject: `角色`, `页面`, `选项`, `关卡`, `按钮`, `图表`, `画面`
- the ending: `可以正常进行`, `核心功能基本实现`, `能继续推进`, `有明显反馈`, `不能正常使用`

Prefer current-observation wording over generic labels. For example, write `点开始后能进入答题，有进度和奖励显示` instead of repeatedly writing `可以选择同义词答题，有进度和奖励反馈`.

For user-like SFT wording, allow direct partial-implementation reasons. It is okay to write `能够进行移动，能够实现破拆与建造元素，但是无法切换不同方块` when the core is partly present but a named core subfunction is missing. For opponent-controlled games, prefer ordinary words such as `对手` instead of `AI` unless the page itself uses that label.

Good examples:

- `实现路线绘制和车流模拟，有拥堵热力显示`
- `实现水晶发射光束，可绘制镜面反射`
- `角色可以移动，有机关和收集目标`
- `强度滑块调节无效，核心交互未正常实现`
- `按钮点击后画面没有变化，关键功能不可用`
- `点击后没有明显粒子爆发效果`
- `选项点击无反馈，无法正常答题`
- `角色无法跳过首个障碍，后续关卡无法推进`
- `可以控制角色跳跃冲刺，并收集碎片`

Avoid:

- Long explanations listing every detail.
- Reasons that sound like a formal audit report.
- English names such as `canvas`, `WebGL`, `Node-RED`, `particle system`, unless the user explicitly asks for technical detail.
- Failing a task only because an edge visual or decorative detail is weak.
- Over-polished phrasing such as `整体体验完整`, `交互链路闭环`, `符合预期效果`, or other generic assistant language.

## Output Patterns

Single task:

```text
通过：实现了海带森林和粒子流动，点击后有气泡上升效果
```

Comparison batch:

```text
共 10 题，一致 9 题，不一致 1 题，一致率 90%。
分歧题：我判通过，你原判不通过；按首个障碍阻断核心流程看，不通过更稳。
```

## Skill Evolution

After handling repeated tasks or receiving user corrections, update this skill so it improves over time.

Update [learned-patterns.md](references/learned-patterns.md) when:

- The same task type appears at least 3 times with a stable judgment rule.
- The user corrects the pass/fail standard.
- The user corrects the wording style for a recurring reason.
- A batch review reveals a recurring disagreement pattern.

Do not update the skill for one-off details. Summarize patterns generally, using words like `角色`, `页面`, `选项`, `目标`, `关卡`, and `图表` instead of copying prompt-specific names. Keep each learned pattern short and practical: core pass condition, core fail condition, and 1-2 reason examples.

When adding reason examples to [learned-patterns.md](references/learned-patterns.md), treat them as phrase pools, not canned outputs. Add varied example phrasings for the same pattern so later reasons can be rewritten naturally.
