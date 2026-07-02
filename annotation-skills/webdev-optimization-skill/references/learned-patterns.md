# Learned Patterns

Add reusable user corrections here.

## Rework Corrections

- Pattern: Rework returned for abstract or under-polished visual output
  Pass condition: If prompt core functions work and no blocking bug is found, keep it passable rather than `-1`.
  Lower condition: If the previous score was `+1` but QA says the result is too abstract or not good enough for 优质, revise to `0` unless the current page truly has polished, clear, prompt-matching visuals.
  Reason style: Fill all boxes. State what works, then state the concrete gap and a next-fix expectation, such as 树木呈现较抽象，期望增强树干结构、枝叶层次、颜色质感和生长反馈.

## Patterns From Doubt Table

- Pattern: Strict `1 优质` gate
  Pass condition: All visible functions and all visible buttons or controls are tested and work in their intended states, and the UI has no obvious layout, readability, overlap, clipping, hierarchy, or polish issue.
  Lower condition: If only the core prompt workflow works but secondary buttons, controls, modes, or UI polish are untested or questionable, prefer `0` rather than `1`.
  Reason style: For `1`, name the visible controls that were tested. For `0`, name the untested or problematic control and the expected behavior.

- Pattern: Prompt-explicit colors or style details
  Pass condition: Required colors, theme, material, visual effect, or style details named by the prompt are visibly implemented.
  Lower condition: If a prompt explicitly requires specific colors or visual construction and the page does not follow them, lower the relevant score even if the page is otherwise usable.
  Reason style: Name the missing prompt detail and the expected visible state, without adding version wording.

- Pattern: Functional completeness reason too vague
  Pass condition: The reason names which prompt requirements are covered.
  Lower condition: If a functional-completeness issue exists, the reason must say which prompt point is missing, not only say the function is incomplete.
  Reason style: Mention the concrete prompt point, such as theme switching, palette slider, upload flow, or named game mechanic.

- Pattern: Wrong dimension for non-prompt defects
  Pass condition: Functional completeness focuses on prompt-named requirements.
  Lower condition: Bugs or broken visible controls not named by the prompt should usually be recorded under functional defects, not functional completeness.
  Reason style: Put prompt-missing issues in completeness, and implemented-but-broken issues in defects.

- Pattern: Embedded preview container can mislead
  Pass condition: Open the product URL in a separate generated-page tab before deciding interaction or layout issues.
  Lower condition: Do not lower a score only because the AIDP embedded preview hides or clips a control; verify in the separate page first.
  Reason style: If a real issue only occurs in a specific viewport or container, name that viewing condition.

- Pattern: Game play-loop expectations
  Pass condition: Prompt-named mechanics work and the game is basically playable with coherent score, failure, restart, or feedback where naturally expected.
  Lower condition: Even when prompt details are present, extremely unreasonable speed, control response, difficulty, collision, or failure logic can be a functional defect if it makes the game hard to play or not self-consistent.
  Reason style: Explain the gameplay symptom and the expected playable behavior.

- Pattern: Simple greeting or card page
  Pass condition: A simple implementation may still receive `+1` when the current page satisfies the prompt, interaction is not broken, and overall presentation is acceptable.
  Lower condition: If the function is overly simple and there is no meaningful improvement or richness for the request, prefer `0`.
  Reason style: Name the current simplicity or acceptable presentation without mentioning old versions or baseline.

- Pattern: UI batch with game or simulator prompt
  Pass condition: Judge by the prompt's requested product and core behavior, not by the batch label alone.
  Lower condition: If a prompt asks for a functional simulator or game-like experience but the output is only a static UI shell, lower 功能完整度 or 功能缺陷 as appropriate.
  Reason style: Say which prompt core function is missing or unusable.

- Pattern: White screen or render crash
  Pass condition: None for normal scoring unless the page later loads and core functions can be judged.
  Lower condition: White screen, flashing then white screen, R3F/THREE errors, ReferenceError, TypeError, or similar render crash should be recorded under 功能缺陷.
  Reason style: 页面白屏，控制台报错，当前无法正常判断核心功能

- Pattern: Device, screen, or viewport-specific issue
  Pass condition: If the issue is not reproducible and does not affect the user's current judging environment, describe uncertainty and avoid over-penalizing.
  Lower condition: If screen size, device, or viewport causes operation failure, click offset, fill error, drawing error, or rendering corruption, record it as a functional or visual defect.
  Reason style: Name the affected viewport or operation, such as 大屏视口下动画渲染异常 or 画笔位置与鼠标不一致.

- Pattern: Animation scene
  Pass condition: Dynamic effect is present and the scene is generally usable.
  Lower condition: Completely static scene, failed animation, broken drawing, impossible interaction, or severe rendering corruption should lower the score.
  Reason style: Point out the existing problem only; avoid extra expectation writing.

- Pattern: Resource or network-dependent loading
  Pass condition: If the page loads normally in the required environment and core functions work, judge normally.
  Lower condition: If resources fail to load and cause white screen or missing modules, record loading dependency and visible impact.
  Reason style: 资源加载异常，页面出现白屏，核心内容无法正常查看
