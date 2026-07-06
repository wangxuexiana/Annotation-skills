# Decision Checklist

For every Visual Debug repair-scoring item, build a 3-8 point current-item checklist before judging.

## Step 1: Classify The Item

- [ ] Is this a normal Visual Debug repair-scoring item?
- [ ] Is it returned/rework, permission quiz, inaccessible, or outside this queue?
- [ ] Is there a login, CAPTCHA, permission, risk, or account challenge that requires pausing?

## Step 2: Extract Current Core Requirements

Write these fields into `state/current-item.md` before judging:

- [ ] Prompt/problem description: what exact visual bug or defect should be fixed?
- [ ] Reference image target: what final layout, modules, content, and visual style should the repaired page match?
- [ ] Repaired webpage output: which candidate/page is being scored?
- [ ] Required UP instruction details, if shown.
- [ ] Current-item checklist with 3-8 concrete checks covering abandon gates, page load, bug repair, reference fidelity, and 2-point uniqueness if multiple candidates exist.

## Step 3: Abandon Gates Before Scoring

Abandon the item instead of giving 0/1/2 when any official abandon rule applies:

- [ ] The problem description says an error exists, but that error is not present in the pre-repair output.
- [ ] The task itself is obviously invalid, such as Prompt/reference mismatch, abnormal reference image, wrong screenshot order, or missing information.
- [ ] The reference image itself is flawed and the task asks the model to repair according to that flawed reference.
- [ ] For non-text tasks, there is no usable problem description and no usable reference image.

## Step 4: Page And Repair Checks

- [ ] Open the repaired webpage output and inspect from first screen to page bottom.
- [ ] If the repaired webpage never loads, stays loading, or cannot be normally viewed, score 0.
- [ ] Check whether the prompt-described core problem is actually fixed. If not fixed, score 0.
- [ ] If prompt-named interactions affect the requested repair, test only those controls and record visible feedback.
- [ ] Compare layout, module order, element completeness, text/content, spacing, size, color/style, and visual state against the reference image.
- [ ] Check key visible images or required visual assets for broken loading.
- [ ] Confirm whether all corresponding UP instruction requirements are fully implemented before considering 2 points.

## Step 5: Score

- [ ] 0 points: core problem not fixed, or repaired webpage cannot load/cannot be inspected normally.
- [ ] 1 point: core problem fixed, but the result is not close enough to the reference image; layout, style, content, or visual details still differ obviously.
- [ ] 2 points: core problem fixed, reference-image fidelity is high, and corresponding UP instructions are fully implemented.
- [ ] If multiple candidates in the same task qualify for 2 points, compare repair completion and reference fidelity, keep only the best candidate as 2, and downgrade all other 2-point candidates to 1.
- [ ] Reason names the main scoring evidence and follows active constraints in `user-style.md`.
