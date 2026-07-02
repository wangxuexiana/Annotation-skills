# Training Summary

Source manual: `Visual Debug GSB+Rubrics 标注手册`, Feishu doc `https://bytedance.larkoffice.com/docx/Lg1ndfb0AoXGxkxZQCdcW91anog`, revision 61.

## Task Type And Target Queue

Visual Debug GSB+Rubrics is a repair-quality comparison queue. Each item gives a before-fix webpage, two candidate repaired webpages A/B, the current reported problem, original user request or full task description, optional reference image, and item-specific rubrics.

The annotator must:

- score every rubric for A and B as `1`, `0`, or `无法判断`
- give A and B separate 0-5 overall scores
- choose whether A is better, both are comparable, or B is better
- write a concise reason with concrete visible or interaction evidence

## Core Principle

This is not a normal webpage-aesthetic comparison. Always judge in this order:

1. Did the candidate repair the current reported problem?
2. After repair, does it still satisfy the original request or reference image?
3. Did it introduce side effects such as missing content, layout collapse, unreadable text, broken interaction, or new visual obstruction?

Do not reward a page simply because it looks prettier or changed more.

## Required Browser Flow

1. Read the current reported problem first.
2. Read the original request and full task description.
3. Open the before-fix page to confirm the baseline issue and originally normal content.
4. If a reference image exists, inspect it; when prompt and reference conflict, follow the prompt.
5. Open candidate A and candidate B, checking both sides independently.
6. Test prompt-named functions and natural visible controls only as needed for the rubric.
7. Fill rubric values, A/B scores, preference, and reason after comparing all applicable evidence.
8. Run the pre-submit audit before final submission.

## Quiz Facts Likely To Be Tested

- Rubric `无法判断` is only for insufficient evidence, not for confirmed candidate failure.
- Overall score is not a simple average of rubric pass rate.
- Current problem repair usually controls the total-score ceiling.
- Same/Tie should be used narrowly, only when A/B are substantively close.
- Returned tasks require rechecking rubrics, scores, preference, and reason.
- Waste/abandon is only for tasks that truly cannot be judged.
