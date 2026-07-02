# Rule Updates

Newer entries override older summaries and shared annotation rules when they conflict.

## 2026-06-01 Online Manual Refresh

- Source refresh: WebDev v3.0 online manual revision 494, UI rule document revision 602, and 0515 animation rule revision 91.
- Open the generated page in a separate tab for judgment. When feasible, check console errors and warnings for every item, not only white screen or ready-to-build cases. Console output is iteration evidence, not sufficient by itself to decide pass or fail.
- The annotator may use V0/baseline internally as a judging aid, especially for UI items where `0` vs `+1` is unclear. Submitted reasons must still describe only the current page and must not mention versions, comparison, baseline, initial version, old version, V0, or similar wording.
- All required fields should contain concrete reasons. For unreasonable behavior or visual issues, write the current state plus the expected behavior or improvement. If no functional defect is found, it is acceptable to say no obvious functional defect was found.
- Prompt-explicit details such as color, theme, animation, controls, layout, and responsive requirements must be verified. If prompt explicitly requires colors and the page does not follow them, this can lower the score even if the page is otherwise usable.
- UI item reasons should consider page angle and atmosphere angle in the overall evaluation or aesthetic field when useful: overall presentation, visual texture, interaction flow, theme fit, and whether the intended mood or emotion comes through. This does not change the base scoring logic.
- Animation-scene reasons under the 0515 rule should not apply the UI page-angle or atmosphere-angle expansion. Point out existing problems only and avoid broad expectation writing.

## 2026-06-02 Strict +1 Override

- `1 优质` must be assigned cautiously. It is not enough for only the prompt's core workflow to work.
- Before assigning `1 优质`, test all visible functions and all visible buttons or controls in their intended states, including secondary controls such as reset, restart, replay, difficulty, tabs, toggles, filters, uploads, sliders, mode switches, and naturally clickable game/UI controls.
- The UI must also have no obvious problem in layout, spacing, alignment, readability, overlap, clipping, visual hierarchy, or polish.
- If any visible control is broken, untested, confusing, has no reasonable feedback, or if the UI has a noticeable issue, prefer `0 合格` unless the issue is truly irrelevant. Write the concrete issue and expected behavior.
- Disabled controls are acceptable only when the disabled state is contextually reasonable, such as difficulty selection being disabled during an active game. If a disabled state blocks expected use, record it as a functional defect.

## Active Overrides

### +1 Does Not Require Extra Highlights

- 0429 update: if 功能完整度, 功能缺陷, and 美观度 all pass, the item can receive `+1` even without an extra highlight.
- Do not force `0` only because the implementation is not surprising or especially creative.

### White Screen And Ready-To-Build Are Not Waste By Default

- 0430 update: white screen, blank page, and single no-function page are normal model-output states for this queue. Do not directly abandon or mark waste by default.
- Open the generated page in a separate tab, inspect console, and record concrete errors under 功能缺陷.
- 0506 update: `ready to build` usually means the model did not finish compiling. If there is a console error, record it under 功能缺陷. If no error is visible, note the ready-to-build state.

### Mobile Checks Depend On Prompt

- 0507 update: check mobile or responsive adaptation only when the prompt explicitly asks for mobile friendly behavior, responsive layout, or related requirements.
- Use around 375px as a mobile reference viewport.
- If prompt does not mention mobile/responsive requirements or clearly says web scene, mobile adaptation is not a mandatory deduction point.

### UI Pages Have A Higher Bar But Are Not Pixel-Strict

- 0513 update from the main manual: UI class products have a higher judging bar and more dimension checks.
- The referenced UI-specific document could not be fetched due to backend error code 10071, so use the visible manual rule: overall UI should look good enough, satisfy the basic request, and avoid multiple or major interaction defects.

### Animation Scene Rule

- 0515 update: animation scenes must be dynamic. A completely static scene is not acceptable.
- First-round animation scoring: `-1` for functional defect, extremely poor effect, or basically unusable/unplayable; `0` for average output with UI or partial interaction issues; `+1` for generally good output with no major issue.
- Later rounds use the first round as an internal judging anchor: `0` can mean no clear improvement, `+1` should be generally good and clearly improved, with minor flaws allowed.
- Animation scene reasons should only point out existing problems and should not add broad expectation writing.

### Submitted Wording Must Not Mention Versions

- The annotator may internally refer to old output or V0, but submitted reasons must not mention version, comparison, baseline, initial version, old version, V0, or similar expressions.
- Submitted wording should describe only the current generated page: what works, what fails, and what the expected current behavior should be.

### Rework Reasons Must Be Actionable And Complete

- 2026-06-01 user correction: after naming a functional defect or aesthetic issue, also write the reasonable expectation for the next fix. Do not only say "has a problem".
- Every required reason field must be filled: overall evaluation, 功能完整度, 功能缺陷, and 美观度.
- If QA returns a `+1 优质` because the generated result is too abstract or not polished enough, revise to `0 合格` when core functions work, and explain the specific gap plus expected improvement.
- Example: for an interactive tree/simulator where planting works but the tree visual is too abstract, write that core controls and planting are usable, then expect clearer trunk structure, branch/leaf hierarchy, color texture, and growth feedback.

### Submitted Reasons Should Be Casual And Comma-Only

- 2026-06-01 user correction: write reasons in a more casual spoken Chinese style, not stiff audit language.
- Submitted reasons may use commas only as punctuation.
- Avoid periods, colons, semicolons, parentheses, slashes, dashes, percent signs, and other symbols in submitted reasons. Replace symbols with words when needed, for example write 进度没有变化 instead of `0%`.
- Keep all required fields complete even when using this shorter style.

## Update Log

- 2026-06-01: Added user style constraint: casual Chinese wording, comma-only punctuation in submitted reasons.
- 2026-06-01: Added rework rule from QA feedback: all dimensions must be filled, and defect/aesthetic comments need a concrete next-fix expectation.
- 2026-06-01: Generated active overrides from the provided manual, two training meetings, 0515 rule update, and doubt-table records.
