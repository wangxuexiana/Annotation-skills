# Manual Summary

## Primary Manual

Source: `0526 Video2code数据标注手册`

- The queue evaluates generated HTML pages against a video and original/GT HTML rendering.
- The annotation includes static restoration and dynamic behavior.
- Static restoration uses a 0/1/2/3 scale. Multiple static 2-point candidates should be resolved by promoting the best candidate to 3.
- Dynamic evaluation scores each rubric as 0/1 and then gives an overall 0/1/2 dynamic score.
- Rubrics should be reviewed before rollout scoring: fix over-specific text, drop rubrics that do not match video/GT, merge small same-module tests, mark core/non-core, and cap at 10 key rubrics when the original list is too long.
- Core rubric judgement is based on visible importance: large visual share, clear motion/change, high interaction frequency, video emphasis, and prompt's main function.
- Newer rule: if static restoration is 0, do not score individual Rubrics; only assess overall dynamic effect and write the reason.
- Core content missing, page elements missing, blank/empty page, or severe render failure should be treated as waste/abandon when available.
- Recording rules apply mainly to static 1-point rollouts and "非还原，可利用" cases. Record full page layout/static state, all dynamic effects, and all rubric-1 interactions.

## Static Reference Manual

Source: `RFT标注文档 - RFT人标支持VLM Coding（bon7）`

- Goal: compare generated page to reference screenshot/page for restoration quality.
- Static principle: judge visual restoration only; do not judge function or interaction in the static score.
- Score `2`: overall layout, structure, main elements, hierarchy, and key modules are highly consistent; not pixel-perfect, but no substantive issue.
- Score `1`: overall framework is basically correct but style, layout, or details differ.
- Score `0`: large difference, subject structure wrong, key content missing, or serious visual inconsistency.
- If all models are 0, no best model is needed.
- If not all models are 0, choose exactly one best model among the top candidates in the referenced static workflow; in the Video2code queue this maps to promoting the best static 2-point candidate to static 3.
- For 0/1 static scores, mark visual insufficiency when the platform field exists.
- Every score needs a reason.
- Image content mismatch, random images, or placeholders can be ignored if the image is rendered and not broken.
- Broken images are not exempt and cannot receive a top static score because of that issue.

## Conflicts And Priority

- The primary manual contains an older note that static-failed rollouts are eliminated and dynamic scoring is not needed.
- The later "新标准同步" section overrides this: static 0 rollouts skip individual Rubric scoring but still receive an overall dynamic assessment and reason.
- Use the newest manual section, live user corrections, and `references/rule-updates.md` before older notes.

## Reason Examples

- `还原度：主体结构接近，但页面顺序和细节有偏差`
- `整体动效：核心点击反馈已实现，加载动画未体现`
- `已实现`
- `悬停反馈未实现`
- `全部未实现`
- `还原度：关键内容缺失，主体页面无法判断`
- `整体动效：静态还原为0，仅能确认部分按钮有反馈`
