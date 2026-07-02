# Manual Summary

Source: https://bytedance.larkoffice.com/wiki/DN9HwxnCuigeTtkjlZocIfjunqf

## Task Goal

This queue evaluates whether one generated webpage correctly implements the functional flow shown by a reference flowchart. The task is not a visual-aesthetic review and not a generic webpage-quality review. Judge against the prompt, the reference flowchart, the actual opened webpage, the screenshot, and all rubrics.

Each item requires four outputs:

- Waste or abandon decision, when applicable.
- Independent `1/0` label for every rubric, plus concise reasons when fields exist.
- Integer overall functionality score from `0` to `10`.
- Screenshot correctness label, `1` or `0`.

## Inputs

- `id`: item identifier only.
- `prompt`: the user's original request and the main source for overall functionality.
- `refs[0]`: one reference flowchart image. Use it to understand the target page, entry points, branches, routing, and completion states.
- `modelA`: generated webpage link. Open it and interact with it before judging behavior.
- `modelA_img`: screenshot to compare against the webpage's initial loaded state.
- `rubrics`: 3-8 or more independent evaluation points.
- `rubrics[].level`: common types include `flow_coverage`, `function`, `flow_routing`, `flow_decision`, and `flow_completion`.
- `rubrics[].rubric`: the direct requirement for that rubric's `1/0` judgement.

## Required Review Order

1. Read the prompt and identify the user's requested workflow.
2. Inspect the reference flowchart and identify entries, nodes, branches, and final states.
3. Open `modelA` and wait for the page to load.
4. Test rubrics in order. Any rubric involving interaction, routing, decision logic, submission, filtering, modal display, or completion must be triggered in the browser.
5. Label each rubric independently as `1` or `0`.
6. Assign the overall `0-10` functionality score based on prompt, flowchart, and actual interaction.
7. Compare `modelA_img` with the actual initial loaded page before any interaction and label screenshot correctness.
8. If the item cannot be judged, mark waste/abandon and write a concrete reason.

## Rubric Judgement

Give `1` only when the specific rubric requirement is present, operable, and produces the expected result. If a rubric describes multiple required conditions, every condition must be satisfied for `1`.

Give `0` when the function or entry is missing, the entry exists but has no effect, the result conflicts with the flowchart or rubric, a required interaction is unusable, the page cannot be opened enough to verify it, or the webpage is only static while the rubric requires an interactive flow.

Rubrics are independent:

- Do not let one failed rubric make other rubrics fail automatically.
- Do not let a bad overall page quality make every rubric `0`.
- Do not give `1` because something merely looks like a feature; interact when behavior is required.
- Do not add unstated requirements to a rubric.

## Rubric Types

- `flow_coverage`: whether the page covers a required entry, module, or workflow.
- `function`: whether a specific feature works.
- `flow_routing`: whether the user can move to the expected section, page, step, or state.
- `flow_decision`: whether conditional branches behave correctly.
- `flow_completion`: whether the flow reaches the required final state, such as successful submission, reservation, checkout, or completion.

When a rubric has multiple levels, apply all named concerns.

## Overall Function Score

Score is an integer from `0` to `10`. Use this priority:

1. User request implementation: core prompt and flowchart requirements.
2. Interaction completeness: whether the core flow can proceed from entry to completion.
3. Robustness: whether special inputs or operations cause obvious failure.

Anchors:

- `10`: all prompt-required functions are fully implemented and interactive, with no obvious bug.
- `9`: all required functions are usable, with only one minor detail issue that does not affect use.
- `8`: main functions are complete and usable; at most 1-2 minor secondary issues; no fully unmet rubric.
- `7`: core functions are usable, with a few missing secondary functions or small bugs.
- `6`: core functions are usable, but some important interaction has a defect.
- `5`: core functions are partly usable, but major interaction chains are broken.
- `4`: most core functions are missing or significantly buggy.
- `3`: core functions are basically absent; mostly a static shell.
- `2`: almost no functional implementation, only scattered static elements.
- `1`: no interaction or the page is too broken to operate meaningfully.
- `0`: white screen, crash, syntax/runtime failure, or page unusable.

The overall score is not a simple average of rubric labels, but it should be broadly consistent with them. If most rubrics are `1`, the overall score should not be very low unless prompt-critical behavior outside the rubrics fails. If the score is `0-2`, most functional rubrics should normally be `0`.

## Screenshot Correctness

Screenshot correctness compares `modelA_img` against the actual `modelA` page after opening it, waiting for resources and animations to finish, and doing no interaction.

Give `1` when the screenshot basically matches the loaded initial page: layout, visible elements, image states, and default states are consistent. If the actual webpage itself has missing images or rendering defects, the screenshot can still be correct when it shows the same defective initial state.

Give `0` when the screenshot misses images that are visible in the actual page, has clearly different layout or element positions, is cropped or incomplete, lacks key elements, shows a post-click state such as a modal/menu/expanded card/filter selection, or otherwise does not represent the initial page state.

Screenshot correctness is independent from functional quality.

## Waste And Abandon

Waste/abandon only when the item cannot be judged effectively:

- `modelA` cannot open or cannot be evaluated.
- The reference flowchart is missing or cannot be viewed.
- Required task data is wrong or mismatched, such as prompt, link, screenshot, and reference flowchart being unrelated.
- The page content is completely unrelated to the item.
- Permission/resource issues block key material.

Do not abandon merely because the webpage is ugly, incomplete, has failed rubrics, has a wrong screenshot, or has several missing functions. If it can be evaluated, judge normally.

Waste reasons must be concrete and reviewable, for example:

- 网页链接打开后白屏，无法验证任何功能
- 参考流程图无法加载，无法确认目标流程
- 网页内容与参考流程图和 prompt 完全不相关，无法按题目要求评价

## Return Or QC Mode

For returned annotation, read the QC reason first and re-check the affected fields. For QC/return-review mode, do not directly edit the annotator's answer unless the platform explicitly makes that the workflow. If the existing annotation is wrong, mark the QC conclusion as unqualified or return for revision and write the return reason.

## Reason Requirements

Reasons should be short, concrete, and reviewable. Name the verified interaction or failure point, such as click result, submit result, routing result, validation result, completion state, or screenshot mismatch. Do not write only `1`, `0`, `是`, `否`, `满足`, or vague phrases like `有问题`.
