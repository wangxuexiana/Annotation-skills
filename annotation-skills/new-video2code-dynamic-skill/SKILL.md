---
name: new-video2code-dynamic-skill
description: Video2code / VideoEvaluation annotation rubric for judging generated HTML pages against a video, original GT HTML, static restoration, dynamic effects, interactions, function-layout rubrics, recording usefulness, and 0/1/2/3 rollout scoring. Use when Codex needs to label this queue in Chrome, fix or drop rubrics, choose core rubrics, score static/dynamic dimensions, or write Chinese annotation reasons for ByteDance AIDP VideoEvaluation tasks.
---

# Video2code Dynamic Skill

## Goal

Judge VideoEvaluation / Video2code tasks where each sample provides a video, original or GT HTML rendering, rubrics, and multiple model-generated HTML rollouts.

Ask before final quiz, permission, or annotation submission unless the user explicitly authorizes auto-submit for this queue.

## Load Order

Read these files before a batch:

1. `references/rule-updates.md`: newest overrides and user corrections.
2. `references/learned-patterns.md`: reusable judgement patterns.
3. `references/training-summary.md`: distilled Video2code workflow.
4. `references/manual-summary.md`: static reference rules and conflict resolution.
5. `references/reason-examples.md`: Chinese reason phrase pool.

Shared fallback rules live at `../annotation-workflow-skill/references/stable-annotation-rules.md`. Task-specific files above override shared rules.

## Per-Sample Flow

1. Open the sample and identify the video, original/GT HTML, rubrics, rollout HTML links, and required platform fields.
2. Play the video and inspect the original/GT HTML rendering to understand layout, core modules, and expected motion or interaction.
3. Review rubrics before scoring rollouts:
   - Fix over-specific timing into visible requirements, such as "4 秒加载" to "需要加载动画".
   - Drop rubrics that do not match the video or GT page at all.
   - Fix and keep mismatched rubrics when the underlying behavior is important.
   - Merge small same-module tests when needed.
   - Mark each rubric as core or non-core.
4. For each rollout, inspect the rendered HTML visibly. Use DOM only for navigation or troubleshooting, not as scoring evidence.
5. Score static restoration first.
6. If static restoration is `0`, do not score individual Rubrics under the newer manual rule; only assess overall dynamic effect and explain the reason.
7. If static restoration is not `0`, test the visible interactions and dynamic effects needed for the rubrics.
8. Fill rubric scores, overall dynamic score, notes, and any platform-required visual insufficiency or recording/usefulness fields.

## Static Restoration

Score static restoration as `0/1/2/3`:

- `3`: multiple rollouts qualify as static `2`; choose the best one and promote it to `3`.
- `2`: layout, structure, main elements, visual hierarchy, and key modules are highly consistent; not pixel-perfect, but no substantive issue.
- `1`: overall framework is basically right, but style, layout, or details differ.
- `0`: large difference from video/original page, main structure wrong, key content missing, mostly empty page, or severe visual mismatch.

Static score judges visual restoration only; do not use function/interaction quality to inflate the static score.

Image content mismatch, random images, or placeholders can be ignored if the image renders and the rest of the page is restored. Broken images are not exempt and cannot receive top static score.

Core content missing, blank/empty page, major element loss, or unjudgeable rendering should be treated as waste/abandon when the platform supports it.

## Rubric Rules

Rubrics may include dynamic, interaction, and function-layout requirements:

- Dynamic: animation, transition, loading state, page element motion, visual state change.
- Interaction: click, hover, drag, selection, or other user-triggered feedback.
- Function: visible module layout or core function presentation.
- Static style restoration in a rubric should be judged precisely when it names concrete visual attributes, such as gradient glass navigation, translucent blur, or similar style requirements.

Core rubric criteria:

- Mark core when visual area is about 30 percent or more, the effect is emphasized in the video, the interaction is frequent, the change is visually obvious, or the prompt's main function depends on it.
- Mark non-core when it is small, incidental, rarely visible, or does not affect the main experience.

Quantity control:

- If rubrics exceed 10, keep only the 10 most core rubrics and drop non-core extras.
- If rubrics are 10 or fewer, non-core rubrics may remain, but core functions should not be underrepresented.
- Aim for at least 5 core rubrics when the original/GT page actually has that many meaningful core functions; otherwise note that the original page does not support more.

## Dynamic Scoring

Per-rubric score:

- `1`: rollout satisfies the rubric.
- `0`: rollout does not satisfy the rubric.

Overall dynamic score:

- `0`: overall dynamic behavior does not meet requirements.
- `1`: rollout meets all dynamic and interaction requirements; every visible dynamic effect and interaction must correspond to both the video and the original/GT HTML.
- `2`: if multiple rollouts receive dynamic `1`, choose the best one; each sample may have at most one dynamic `2`.

Core rubrics are useful for deciding severity and choosing the best rollout, but they do not relax the threshold for overall dynamic `1`: any missing or mismatched dynamic effect or interaction means the rollout should not receive overall dynamic `1`. Use visible importance from the video and original page, not personal preference, when explaining the reason and choosing the best among fully matching rollouts.

## Recording And Usefulness

Recording mainly applies when static restoration is `1`, and the dynamic interactions are rich enough to be useful independent of static mismatch.

- "非还原，可利用" `1`: existing rollout functions/interactions are better, more optimized, or more reasonable than the original.
- "非还原，可利用" `2`: rollout adds useful interactions or improves same/new functions beyond the original.
- Recording should include the page layout/static state, all dynamic effects, and all interactions whose rubric score is `1`.

Follow the actual platform template if it differs from the manual.

## Reason Style

Overall notes can use:

```text
还原度：xxxx

整体动效：xxxx
```

Rubric notes:

- Fully implemented: `已实现` or `全部实现`
- Partly implemented: name what is missing, such as `点击反馈未实现`
- Not implemented: `全部未实现`

Keep reasons short, concrete, and based on visible evidence. Do not submit final labels without the user's approval unless auto-submit is already authorized for this queue.

## Conflict Priority

Use this priority when rules conflict:

1. Current user instruction.
2. User corrections in `references/rule-updates.md` or `references/learned-patterns.md`.
3. Newer "新标准同步" manual section.
4. Primary Video2code manual.
5. Static RFT bon7 reference manual.
6. Shared stable annotation rules.

Known override: older text says static-failed rollouts can be directly eliminated, but the newer rule says static `0` rollouts skip individual Rubric scoring while still receiving an overall dynamic assessment and reason.

User correction: overall dynamic `1` requires all dynamic effects and interactions to correspond to the video and original/GT HTML; core/non-core weighting cannot excuse missing visible motion or interaction.
