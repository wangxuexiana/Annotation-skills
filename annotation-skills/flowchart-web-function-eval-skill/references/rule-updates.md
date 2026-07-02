# Rule Updates

Newer entries override older summaries when they clearly conflict. Add updates with `update_task_skill.py` or append manually.

## Active Overrides

- Recording/video rules override the written manual for this queue when they conflict.
- Waste/abandon is narrow: abandon only when `modelA` truly cannot open/evaluate, the reference flowchart cannot be viewed, required materials are unavailable/mismatched, or the item cannot be judged. Do not abandon merely because the page is ugly, flawed, incomplete, or has several failed rubrics.
- This queue has four main fields to handle: waste/abandon, rubric labels and reasons, overall function score, and screenshot correctness.
- Rubrics are independent. Judge each rubric only against its own wording. Do not add requirements that the rubric does not state, and do not let other rubric failures affect the current rubric.
- Every rubric involving behavior must be tested by opening `modelA` and interacting. Do not judge from screenshot alone.
- If a rubric asks whether validation exists, only verify that validation and corresponding prompt/feedback exist. Do not require the exact validation standard you personally expect unless the rubric says so.
- Overall score must be based only on prompt, flowchart, and stated requirements. Do not invent extra product requirements that the user did not ask for.
- Overall score `8+` requires rubrics to be basically satisfied: no completely unmet rubric, and at most one rubric with a partial/minor defect. Use lower scores when rubrics include fully unmet core functions.
- Screenshot correctness compares `modelA_img` with the actual page after opening `modelA`, waiting for resources/animations to load, and doing no interaction.
- Screenshot correctness should reflect the full initial page state, not only a cropped visible viewport. It should not contain extra content, clicked filters, selected states, expanded cards, modals, menus, or other post-interaction states.
- If the actual webpage initially has flaws, missing images, or rendering defects, the screenshot can still be correct when it shows the same flawed initial state.
- Screenshot correctness is independent from functional quality: a bad page can have a correct screenshot, and a functional page can have an incorrect screenshot.
- In QC/return-review mode, do not directly edit the annotator's answers. If the annotation is wrong, mark the QC conclusion as unqualified/return for revision and write the return reason. If the platform asks for both QC conclusion reason and return reason, they may be the same.
- In QC mode, if a normal annotation item should be waste/abandon, follow the platform's current QC waste flow rather than silently changing the annotator answer.

## Update Log

- 2026-06-09: Regenerated from Feishu Wiki manual `DN9HwxnCuigeTtkjlZocIfjunqf` and Feishu Minutes `obcn4lt749yij8r13zmj41b9` using the context-budget state-file workflow.
