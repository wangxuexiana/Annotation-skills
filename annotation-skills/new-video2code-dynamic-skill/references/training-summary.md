# Video2code Dynamic Annotation Training Summary

## Task Type And Queue

- Task: `VideoEvaluation` / Video2code coding annotation.
- Main queue: `7646678663594299187 【coding】VideoEvaluation`.
- Legacy/test queue: `7644220788530761482 【coding】VideoEvaluation-test`.
- Inputs: video, original HTML / GT rendered page, rubrics extracted from user instruction.
- Outputs to judge: multiple model-generated HTML pages and their preview links.

## Core Judgement Model

- Judge each rollout on two axes: static restoration and dynamic behavior.
- Static restoration compares the rollout against the video and original/GT page, using the referenced RFT bon7 static restoration standard.
- Dynamic judgement compares rollout behavior against the video, original/GT page, and rubric list.
- Newer "新标准同步" rules override older notes where they conflict.

## Static Restoration

- Static score range is `0/1/2/3`.
- `3`: when multiple rollouts qualify as static `2`, choose the best one and promote it to `3`.
- `2`: layout, structure, major elements, visual hierarchy, and key modules are highly consistent; no substantive issue.
- `1`: overall frame is basically correct but there are style, layout, or detail deviations.
- `0`: large difference from reference video/original page, main structure wrong, key content missing, or page mostly empty.
- Core content missing, major page elements missing, blank/empty page, or severe rendering failure should be treated as waste/abandon when the platform supports it.
- Layout order differences between video and rollout can still receive static `1` if the actual implementation looks usable and the overall effect is acceptable.

## Rubric Review And Fixing

- Review rubrics before judging rollouts.
- Rubrics may need to be split, merged, fixed, dropped, or marked core/non-core.
- Overly precise timing such as "4 秒", "2s", or "1.2s 展开" should be softened to the visible requirement, such as "需要加载动画" or "需要播放".
- If a rubric conflicts completely with the video or GT page, mark it as `should_drop=true`.
- If a conflicting rubric describes an important visible behavior, fix it and keep it.
- Classify rubrics:
  - Dynamic: element animation, transition, loading state, or visual change.
  - Interaction: user-triggered response such as click, hover, drag, or feedback.
  - Functional: module layout or core function presentation that should still be scored.
- Static visual-style restoration rubrics should be judged precisely on visual attributes, such as glassmorphism, gradient, translucency, blur, and similar visible style requirements.
- Mark a rubric as core if it covers at least about 30 percent of visible area, is emphasized in the video, changes clearly, appears frequently, or matches the prompt's main function.

## Rubric Quantity Control

- Merge small tests from the same module, such as hover and click effects for one calendar module, into one rubric where reasonable.
- If initial rubrics exceed 10, keep only the 10 most core functional/dynamic rubrics; do not keep non-core rubrics.
- If initial rubrics are 10 or fewer, keep reasonable non-core rubrics but make sure core functions are not underrepresented.
- Aim for at least 5 core rubrics when the original page actually supports that many core functions; if not, note the limitation.

## Dynamic Scoring

- Per-rubric score is `0/1`.
- `0`: rollout does not meet the rubric.
- `1`: rollout meets the rubric.
- For each rubric, record whether it is fixed, its fixed text if fixed, whether it should be dropped, whether it is core, and the score for each rollout.
- Overall dynamic score is `0/1/2`.
- `0`: rollout is overall not satisfactory dynamically.
- `1`: rollout meets all dynamic and interaction requirements; all visible dynamic effects and interactions correspond to the video and original/GT HTML.
- `2`: if multiple rollouts receive dynamic `1`, pick the best one; each sample may have at most one dynamic `2`.
- Core rubrics still matter for severity and best-rollout selection, but they do not lower the bar for overall dynamic `1`: missing or mismatched non-core visible motion/interaction should prevent `1`.

## Static-Dynamic Override

- Earlier handout text says static failure may eliminate the rollout, but the newer rule says: when static restoration is `0`, do not score individual Rubrics; only evaluate overall dynamic performance and explain the reason in notes.
- Static scores `0/1/2` plus "非还原，可利用" scores `1/2` may require recording a video according to the queue template.
- Until the platform template requires otherwise, follow the visible fields on the task page and do not invent unavailable fields.

## Recording / Non-Restored But Useful

- Recording is mainly considered when static restoration is `1`; judge whether dynamic interactions are rich, ignoring static quality.
- "非还原，可利用" score `1`: the rollout's existing functions/interactions are better, more optimized, or more reasonable than the original.
- "非还原，可利用" score `2`: the rollout adds interactions or improves same/new functions beyond the original in a useful way.
- Recording should include page layout/static state, all dynamic interactions, and all interactions whose rubric score is `1`.

## Recommended Browser Flow

1. Open a sample.
2. Play `video_tos_url`.
3. Render or inspect `ground_truth_html_tos_url`.
4. Build a mental reference for page layout, key modules, and dynamic behavior.
5. Review and fix/drop/merge rubrics.
6. For each rollout, open/render `html_tos_url` and judge static restoration.
7. If static score is `0`, skip per-rubric scoring and write the dynamic overall reason.
8. Otherwise test rubric-related visible interactions and animations.
9. Score each rubric and overall dynamic performance.
10. Fill notes in the required format.

## Reason Style

- Overall notes can use:

```text
还原度：xxxx

整体动效：xxxx
```

- Rubric notes:
  - Fully implemented: `已实现` or `全部实现`
  - Partly implemented: name what is missing, such as `点击反馈未实现`
  - Not implemented: `全部未实现`
- Reasons should be short, concrete, and based on visible evidence.

## Easy-To-Misjudge Cases

- Do not fail a good rollout only because exact timing does not match the original rubric; soften timing to visible behavior.
- Do not keep non-core rubrics when there are more than 10.
- Do not mark a rubric as dropped merely because wording is too specific; fix it if the visible behavior matters.
- Do not score individual Rubrics when static restoration is `0` under the newer rule.
- Do not judge function and interaction as irrelevant; module layout and core function presentation can be rubric-scored.
- Do not require pixel-perfect static restoration for score `2`.
- Do not penalize image content mismatch if the image is not broken and the rest of the page is well restored.
