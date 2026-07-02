# Manual Summary

Source: `https://bytedance.larkoffice.com/docx/Lg1ndfb0AoXGxkxZQCdcW91anog`, revision 61, title `Visual Debug GSB+Rubrics 标注手册`.

## Page Fields

- Current reported problem: the primary repair target. Read this first and make all later checks revolve around it.
- Original user request: the page's initial intended structure, function, and visual requirements.
- Full task description: use when details or constraints are unclear.
- Before-fix webpage: must be opened to confirm the baseline defect and original normal content.
- Reference image: inspect when present. If prompt and reference conflict, follow the prompt.
- Candidate A/B: inspect both independently.
- Rubrics: item-specific checklist scored separately for A and B.

## Rubric Values

- `1`: the candidate satisfies the rubric's core requirement and evidence is stable through visible inspection or simple interaction.
- `0`: the candidate does not satisfy the rubric, key conditions fail, the target area remains wrong, the function has no real response, only superficial effects are added, or the candidate page truly fails.
- `无法判断`: evidence is insufficient to judge reliably, such as link/resource inaccessible due to environment, key content failed to load and cannot be attributed to the candidate, rubric contradicts the page, or verification requires unavailable account, permission, device, or external condition.

Do not mark a confirmed bad candidate as `无法判断`. When using `无法判断`, the reason must name what cannot be judged and why.

## Overall 0-5 Scores

Overall score is not the average of rubric pass rate. Prioritize current problem repair, then original request/reference match, then side effects.

- `0`: white screen, cannot open, main content invisible, or target operation cannot be performed.
- `1`: core problem basically not repaired, or repair direction is wrong.
- `2`: only a small part is repaired and the core problem remains obvious.
- `3`: obvious improvement, but visible residue or an important branch still fails.
- `4`: main problem is repaired, with only light residue, edge issue, or local visual difference.
- `5`: target problem is fully repaired, original request/reference is satisfied, and no obvious side effect is introduced.

If the current problem is not repaired, do not give a high score because the page is prettier overall.

## GSB Preference

- A better: A is overall better in current repair, requirement/reference match, and side-effect control.
- Same/Tie: A and B are substantively close, with no reliable quality gap.
- B better: B is overall better.

Comparison priority:

1. Who more completely fixes the current reported problem.
2. If close, who better matches the original request or reference image.
3. If still close, who has fewer side effects and a more stable page.

## Common Scene Focus

- Explicit visual repair: check whether the specified visual issue is fixed and whether it remains aligned with original request/reference.
- Open visual repair: check overall layout, hierarchy, main color, core copy, and reference/request similarity.
- Function or interaction repair: check the complete operation path, state change, and result feedback. Do not treat hover, animation, or console output as a real function.
- Responsive/mobile repair: switch to the specified viewport only when the task requires it; check menus, layout, overlap, and readability.

## Returned And Waste Rules

- Returned tasks: read the top return comment first, then re-check rubrics, A/B scores, preference, and reason. Do not only edit the reason.
- Waste: use only when the item truly cannot be judged, such as missing key input, both A/B links inaccessible, or severe task abnormality.
- Do not waste for a single non-core broken image, local minor issue, or one poor candidate; score by actual evidence.
- Waste reason must name the abnormal link or field and explain why judgement cannot continue.

## Reason Requirements

Reason should be short but locatable, usually 1-3 sentences. Include at least one or two concrete evidence points from modules, buttons, images, navigation, cards, hero, forms, menus, theme switch, mobile layout, popups, route changes, or other visible/interactive evidence.

Avoid empty reasons like `A 更好看`, `B 感觉不错`, `差不多`, `都可以`, or `无`.
