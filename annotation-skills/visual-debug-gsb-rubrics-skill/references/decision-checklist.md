# Decision Checklist

For every item, build a short current-item checklist before judging. Store it in `state/current-item.md`.

## Step 1: Classify The Item

- [ ] Is this a normal annotation item?
- [ ] Is it returned/rework, permission quiz, inaccessible, waste candidate, or outside the requested queue?
- [ ] Is there a login, CAPTCHA, permission, risk, or account challenge that requires pausing?

## Step 2: Extract Task Evidence

- [ ] Current reported problem:
- [ ] Original user request:
- [ ] Full task description constraints:
- [ ] Before-fix baseline defect and originally normal content:
- [ ] Reference image target, if any:
- [ ] Candidate A evidence:
- [ ] Candidate B evidence:
- [ ] Rubrics to score:

## Step 3: Build Current-Item Checklist

Write 3-8 concrete checks for this exact item. Include:

- [ ] The current problem that must be repaired.
- [ ] Original request/reference requirements that must remain satisfied.
- [ ] Prompt-named functions or interactions that must be tested.
- [ ] Important side effects to watch for.
- [ ] Rubric-specific conditions.
- [ ] Waste or unable-to-judge risks.

## Step 4: Hard Gates And Waste

- [ ] Page or preview loads and is inspectable.
- [ ] It is not blank, white-screen, black-screen, broken, or unrenderable.
- [ ] Before-fix, A, and B links are accessible enough to judge.
- [ ] Key visible images are not broken when they are core evidence.
- [ ] The core requested feature exists visibly.
- [ ] The page can be judged from visible behavior, not hidden DOM evidence.

Use waste only when the item truly cannot be judged. If only one candidate is poor, score that candidate rather than wasting the item.

## Step 5: Score Rubrics

- [ ] For each rubric, score A as `1`, `0`, or `无法判断`.
- [ ] For each rubric, score B as `1`, `0`, or `无法判断`.
- [ ] Mark `1` only when the core requirement is visibly or interactively satisfied.
- [ ] Mark `0` when the candidate fails the requirement or only has superficial repair.
- [ ] Mark `无法判断` only when evidence is insufficient, and record the cause for the reason.

## Step 6: Score A/B 0-5

- [ ] A score follows current problem repair first.
- [ ] B score follows current problem repair first.
- [ ] Request/reference match is considered after target repair.
- [ ] Side effects are considered after target repair and can lower the score.
- [ ] Scores are not a simple average of rubric pass rate.

## Step 7: Choose GSB Preference

- [ ] Choose A better only if A is overall better in target repair, request/reference match, or side-effect control.
- [ ] Choose B better only if B is overall better in those same dimensions.
- [ ] Choose Same/Tie only if A and B are substantively close.
- [ ] If preference and scores/rubrics appear inconsistent, write the exception in the reason.

## Step 8: Reason Draft

- [ ] Reason contains at least one concrete module, function, visual region, or interaction evidence.
- [ ] Reason avoids empty aesthetic claims.
- [ ] If `无法判断` is used, reason names the object and cause.
- [ ] Reason follows `user-style.md`.

