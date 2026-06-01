---
name: webdev-optimization-skill
description: Use for WebDev optimization annotation tasks on AIDP, including scoring generated web pages, UI pages, games, animation scenes, white screens, ready-to-build states, console errors, mobile-responsiveness checks, and Chinese annotation reasons using the WebDev v3.0 manual and rule updates.
---

# Webdev Optimization Skill

## Goal

Use the WebDev v3.0 manual, training meetings, and rule updates to annotate AIDP WebDev optimization tasks. Prioritize task-specific rules over generic annotation habits.

Default confirmation policy: ask the user before final questionnaire submission, permission submission, or final annotation submission unless the user explicitly authorizes auto-submit for this queue.

## Runtime Checklist

Before judging each item, follow this checklist:

1. Read `references/rule-updates.md` first, then the needed parts of `training-summary.md`, `manual-summary.md`, `learned-patterns.md`, and `user-style.md`.
2. Identify the item type: normal Web page, UI page, game, animation scene, card/greeting page, white screen, ready-to-build state, returned/rework task, permission quiz, or inaccessible page.
3. Read the prompt and extract explicit requirements: core functions, visual style, colors, controls, animation, game rules, mobile/responsive requirements, and special wording.
4. Open the generated page in a separate Chrome tab/window. Do not judge only from the embedded AIDP preview.
5. Test prompt-named core functions and natural visible controls such as buttons, tabs, sliders, uploaders, game controls, replay buttons, drawing tools, and selectors.
6. Open the browser console in the generated page tab when checking white screen, blank page, ready to build, rendering failure, or suspicious behavior. Record useful errors in the 功能缺陷 dimension.
7. Check mobile or responsive behavior only when the prompt explicitly requires mobile friendliness, responsive layout, small-screen support, or similar wording. Use around 375px for mobile checks.
8. Score the three dimensions independently: 功能完整度, 功能缺陷, 美观度.
9. Fill every required field: overall evaluation, 功能完整度, 功能缺陷, and 美观度. Never leave a dimension blank just because it passes.
10. When a defect or aesthetic problem is named, also state the reasonable expectation for the next fix, unless a narrower task-specific rule says to only state the problem.
11. Write submitted reasons in a casual, spoken Chinese style. Use commas as the only punctuation mark in submitted text.
12. Do not mention version, comparison, baseline, initial version, old version, or V0 in submitted reasons.
13. Pause before final submission unless auto-submit is explicitly authorized for this queue.

## Current Manual Addenda

- Open the generated page in a separate tab for judgment. When feasible, check the generated page console for every item, not only white-screen or suspicious items. Record useful errors or warnings in the functional-defect field, but use the actual product experience and prompt fit to decide pass or fail.
- The V0/baseline view may be used internally as a tie-breaker, especially when a UI item is hard to classify between `0` and `+1`. Submitted reasons must describe only the current product and must not mention versions, comparisons, baselines, initial versions, old versions, or V0.
- Every score level and every required dimension needs concrete wording. When a defect, aesthetic issue, or optimization point is named, describe the current state plus the expected behavior or improvement. If no functional defect is found, say that clearly.
- For UI items, overall and aesthetic reasons should consider page angle and atmosphere angle when useful: overall presentation, texture, interaction smoothness, theme fit, and whether the intended mood or emotion comes through. This adds descriptive guidance without changing the scoring logic.
- For animation-scene items under the 0515 rule, do not apply the UI page-angle or atmosphere-angle expansion. Point out existing problems only, and avoid broad expectation writing.
- For games, judge explicit prompt requirements first, then consider whether the overall play loop meets common expectations for the game type, such as reasonable control speed, playable difficulty, and coherent failure or scoring feedback.

## Reference Order

- `references/rule-updates.md`: newest active overrides. Read first.
- `references/training-summary.md`: workflow, scoring, special cases, quiz facts.
- `references/manual-summary.md`: official manual summary and source links.
- `references/learned-patterns.md`: reusable case patterns from doubt table and user corrections.
- `references/user-style.md`: preferred reason wording.
- `references/reason-examples.md`: short phrase pool.
- `references/quiz-draft.md`: likely quiz facts and answer patterns.
- `../annotation-workflow-skill/references/stable-annotation-rules.md`: shared generic rules, overridden by this skill when conflicts exist.

Conflict priority:

1. Current explicit user instruction.
2. `references/rule-updates.md`.
3. `references/learned-patterns.md` and `references/user-style.md`.
4. `training-summary.md` and `manual-summary.md`.
5. Shared stable annotation rules.

## Scoring Guardrails

### Overall Score

- `+1`: three dimensions pass, interaction works, UI is good enough. No extra highlight is required.
- `0`: basically satisfies the prompt but has minor or moderate defects, weak polish, simple implementation, or optimization points.
- `-1`: severe issue such as prompt core requirement missing, core function unusable, game basically unplayable, serious UI/layout failure, rendering failure, process blockage, or very poor experience.
- If QA says an item is "too abstract" or "not good enough for 优质", usually revise from `+1` to `0` when core functions still work, then write the concrete visual/function gap and the expected improvement.

### 功能完整度

- Judge whether explicit prompt requirements are implemented.
- Required prompt details can include colors, theme, text effects, sliders, tabs, uploads, animations, game mechanics, specific visual elements, mobile friendliness, or responsive behavior.
- Do not fail missing generic game or app features that the prompt did not request.
- Extension features not named in the prompt can only help as bonuses; they cannot compensate for missing prompt core requirements.

### 功能缺陷

- Judge bugs in implemented or naturally expected functions.
- Count as defects: button no response, link no response, image load failure, white screen, ready to build, console error, render crash, broken resource, drawing not working, click-position offset, game controls broken, workflow blocked, or visible feature unusable.
- A designed button can be a defect even if the prompt did not explicitly define its destination, because visible controls create interaction expectations.
- Console errors are evidence for iteration, but do not automatically decide pass/fail unless they affect actual function or rendering.

### 美观度

- Judge layout, spacing, alignment, visual hierarchy, typography, color/theme match, scrolling, crop, overlap, readability, and overall polish.
- UI pages should not be judged by tiny taste preferences, but obvious visual problems, many layout defects, or interaction/scrolling that hurts viewing should lower the score.
- Game visuals only need to be acceptable if the game is playable, unless visual defects block operation or strongly violate the prompt.

## Special Cases

- White screen or blank page: do not mark waste by default for this queue. Open the generated page in a new tab, inspect console, and write the concrete error or visible state under 功能缺陷.
- Ready to build: if console has an error, record it under 功能缺陷. If no error is visible, note the ready-to-build state.
- Single page with no real function: record the lack of actual functionality; score depends on prompt and whether the page still satisfies a simple static request.
- Animation scene: it must be dynamic. A completely static scene fails the animation requirement.
- Animation scene after 0515: reasons only need to point out existing problems; do not add broad expectation writing.
- Resources requiring special network conditions: record loading failure or white screen and the observed environment dependency.
- Screen, device, or viewport differences: if they affect rendering or operation, record the issue. If prompt asks mobile/responsive, treat it as a required check.
- UI batch with a game-like prompt: judge by the prompt's core requirement, not only by the batch label.

## Reason Style

Use `references/user-style.md` first.

- Write natural Chinese, compact and specific, usually around 30 Chinese characters when possible.
- For good results, name what works.
- For defects, name the concrete issue and expected behavior.
- For returned/rework items, explicitly answer the QA concern and include a reasonable next-step expectation after the problem, e.g. "树木呈现较抽象，期望增强树干、枝叶层次和生长反馈".
- Fill all required reason boxes: overall evaluation, 功能完整度, 功能缺陷, and 美观度.
- Prefer conversational wording over formal audit wording.
- In submitted reasons, only use commas for punctuation. Avoid periods, colons, semicolons, parentheses, slashes, dashes, percent signs, and other symbols when they can be replaced with words.
- Do not mention version, comparison, baseline, initial version, old version, V0, or similar wording in submitted reasons.
- For white screen, ready to build, or rendering errors, include the visible state and concise console error when available.
- For animation scene after 0515, only state the existing problem; avoid expansive expectation statements.

## Quiz Flow

When answering a permission quiz:

1. Read `references/quiz-draft.md`, `training-summary.md`, and `manual-summary.md`.
2. Match each question to the tested rule: score definition, dimension distinction, white screen handling, mobile check, version-wording ban, game rule, or animation rule.
3. Draft answer, evidence, and confidence.
4. Ask the user to confirm before final quiz submission.
5. If feedback reveals a reusable correction, update `references/rule-updates.md` or `references/learned-patterns.md`.

## Skill Evolution

When the user corrects a judgement or wording:

- Add active rule changes to `references/rule-updates.md`.
- Add recurring case logic to `references/learned-patterns.md`.
- Add wording preferences to `references/user-style.md` or `references/reason-examples.md`.
- Keep entries short and reusable.
