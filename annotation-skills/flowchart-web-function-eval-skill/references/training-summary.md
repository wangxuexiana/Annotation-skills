# Training Summary

Source: https://bytedance.larkoffice.com/minutes/obcn4lt749yij8r13zmj41b9

## Queue And Task Type

Task: flowchart-based webpage functional evaluation.

This is an evolved webpage-evaluation task. The central evidence is a reference flowchart plus the prompt. The generated webpage may contain buttons, filters, forms, routing, modals, validation, or completion steps. The annotator must open the webpage and actually interact with it.

The queue has four practical fields:

- Whether to waste/abandon.
- Rubric `1/0` labels and reasons.
- Overall functionality score `0-10`.
- Screenshot correctness.

## Video Overrides And Emphasis

The recording is treated as the active training override when it conflicts with the written manual.

Key emphases:

- Interaction is the main point. Do not judge only from the screenshot.
- Waste/abandon is narrow. Only waste when the webpage cannot truly open/evaluate, the flowchart cannot be viewed, or required materials are unavailable or mismatched.
- If the page opens but is ugly, flawed, incomplete, or has several failed rubrics, do not waste; evaluate normally.
- Rubrics are independent. Judge exactly what each rubric says, and do not invent extra requirements.
- If a rubric says to check validation, only check whether validation and feedback exist. Do not require the exact validation standard in your own mind unless the rubric states it.
- Overall score must be based on prompt and flowchart requirements. Do not penalize missing features that are not requested by the prompt, flowchart, or rubrics.
- An `8+` score generally requires rubrics to be basically satisfied: no fully unmet rubric, and at most one partial or minor rubric defect.
- Reasons should be normal concise Chinese, describing the actual verified result.

## Screenshot Correctness From Recording

To judge screenshot correctness:

1. Open `modelA`.
2. Wait for resources and animations to finish.
3. Do not click, filter, expand, open a card, or otherwise interact.
4. Compare `modelA_img` to the resulting initial page state.

Give screenshot correctness `0` if the screenshot is only a cropped part of the full page, misses lower-page content that belongs to the initial page capture, shows a selected filter, expanded card, modal, menu, popup, or other post-interaction state, or otherwise does not match the initial loaded page.

If the actual initial page itself has a defect, the screenshot can still be `1` when it shows that same defect. Screenshot correctness is only about matching the initial loaded state; it is not a judgement of whether the webpage is good.

## Rubric Examples From Recording

If the rubric asks whether year filtering and detail-card viewing are supported, the page must be tested by applying the filter and opening the detail view. If both work as described, the rubric can be `1`.

If the rubric asks whether email-format validation exists and gives feedback, entering an invalid value and seeing any relevant prompt or error feedback is enough. Do not require a specific email-regex behavior unless the rubric says so.

If a button exists but clicking it has no feedback or state change when the rubric requires an action, the rubric is `0`.

## QC Notes From Recording

In QC mode, inspect the existing submitted labels and reasons. If an annotation answer is wrong, return it for revision rather than silently changing the annotator's answer. If the platform asks for both a QC conclusion reason and a return reason, the same concise reason may be used.

If a QC item is unqualified, ensure the QC conclusion field is set to unqualified or return-for-revision as required by the platform. Otherwise the item may flow to acceptance incorrectly.

## Quiz Facts Likely To Be Tested

- Must open the webpage and test interactions; screenshot-only judgement is not enough.
- Waste only when the item cannot be evaluated, not when the page is merely poor.
- Rubrics are independent and must be judged according to their own wording.
- Overall score is `0-10` integer and follows prompt/flowchart implementation and interaction completeness.
- Do not invent extra product requirements that are not in prompt, flowchart, or rubric.
- Screenshot correctness compares the screenshot with the initial loaded webpage before any interaction.
- A page with visual or functional defects can still have a correct screenshot if the screenshot matches the same initial state.
- A screenshot showing a clicked filter, opened modal, expanded card, or cropped partial page is incorrect.
