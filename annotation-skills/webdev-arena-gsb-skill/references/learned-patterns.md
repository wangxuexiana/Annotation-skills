# Learned Patterns

Add reusable user corrections here.

## Starter Guardrails

- Pattern: Full rubric coverage
  Pass/choose condition: The judgement considered every applicable rule family for the item, including prompt fit, layout, element completeness, content accuracy, visual details, hallucination control, broken images, and function checks when functions are part of the task.
  Fail/waste condition: The judgement focused only on the latest user correction or one visible detail while ignoring higher-priority applicable rules.
  Reason style: Keep the reason grounded in the main deciding evidence.

- Pattern: User wording constraints
  Pass/choose condition: The submitted reason follows active punctuation and tone constraints in `user-style.md`.
  Fail/waste condition: The reason uses formal audit language, extra punctuation, or a copied template that conflicts with the user's requested style.
  Reason style: Natural, compact, colloquial Chinese, with comma-only clause breaks when that preference is active.

- Pattern: Brief waste reasons
  Pass/choose condition: When marking abandoned or waste, the reason only gives the broad abandonment cause.
  Fail/waste condition: Do not write a detailed GSB-style comparison, long feature checklist, or full testing narrative for waste items.
  Reason style: Keep it short, for example 两边都无法正常显示，直接废弃 or 题目要求 Markdown 文件，但产出是网页，直接废弃.

- Pattern: Manual reason template
  Pass/choose condition: The reason follows the official recommended structure for this queue: chosen G/S/B label, stronger model's concrete advantages, weaker model's concrete problems, the key gap, and the relation to the prompt.
  Fail/waste condition: The reason gives the correct label but only contains a loose evidence list, a one-sentence conclusion, or does not explicitly compare both sides and the key gap.
  Reason style: One compact Chinese paragraph, beginning with the label when useful, then stronger side, weaker side, key gap, and prompt fit.

- Pattern: Avoid obscure English
  Pass/choose condition: The reason uses natural Chinese wording for visible interface, layout, data, functions, and prompt-following evidence, keeping English only for essential labels from the task or platform.
  Fail/waste condition: The reason includes English terms that ordinary annotators may not understand when a clear Chinese replacement is available.
  Reason style: Prefer Chinese words such as 题目要求, 首屏, 数据卡片, 图表, 筛选, 搜索, 导出, 打印, 文案, 设计感, 完成度.

- Pattern: No quotation marks in reasons
  Pass/choose condition: The submitted reason contains no quotation marks and rewrites cited prompt wording as plain Chinese prose.
  Fail/waste condition: The reason contains Chinese corner quotes, straight quotes, curly quotes, or quoted fragments copied from the prompt.
  Reason style: Replace quoted wording with unquoted descriptions, for example write 不像鸽子、颜色不对的反馈 instead of quoting the feedback.

- Pattern: Avoid excessive exact numbers
  Pass/choose condition: The reason focuses on visible differences and prompt fit instead of repeating exact numeric details from the prompt.
  Fail/waste condition: The reason contains many specific numbers, dimensions, counts, or measurements when those numbers are not the decisive comparison point.
  Reason style: Prefer general Chinese wording such as 尺寸要求明确、素材数量感更足、页面信息更完整, and avoid exact numeric strings unless they decide the label.

- Pattern: Close model preview tabs after each task
  Pass/choose condition: After filling the annotation, newly opened model product preview pages are closed and only the original annotation page is kept for user review, unless the user asks to keep previews.
  Fail/waste condition: Multiple product preview tabs from previous items remain open after the task is finished.
  Reason style: Not applicable to submitted reason; this is a browser workflow rule.

- Pattern: Both candidates only show ready-to-build placeholders
  Pass/choose condition: If both model products show only a ready-to-build placeholder, blank shell, or no usable generated page, mark the item as abandoned or waste directly and write only the waste reason.
  Fail/waste condition: Do not continue with normal GSB comparison or fill a normal detailed comparison reason when both sides cannot normally display a product.
  Reason style: 两个产物都只显示待构建占位页，没有实际页面内容，无法正常评估，直接废弃.

- Pattern: Requested Markdown file but product is webpage
  Pass/choose condition: If the task asks for Markdown file content or a Markdown document, but the product is a webpage instead of the requested file or document content, mark the item as abandoned or waste directly.
  Fail/waste condition: Do not continue normal GSB comparison between webpage candidates when the required output form is a Markdown file and the candidates deliver websites.
  Reason style: 题目要求实现 Markdown 文件内容，但产出的是网页，需求产出不对应，直接废弃。

- Pattern: Existing HTML operation without reference image
  Pass/choose condition: If the task asks to operate on or modify existing HTML, but no reference image or sufficient source/reference information is provided, mark the item as abandoned or waste directly.
  Fail/waste condition: Do not infer the missing target design or compare normal candidates when the required reference information is absent.
  Reason style: 题目要求在现有 HTML 上进行操作，但未提供参考图，信息缺失，直接废弃。

- Pattern: Both products cannot display
  Pass/choose condition: If both candidates cannot open normally, cannot render usable content, show preview unavailable, blank pages, or only unusable placeholders, mark abandoned or waste directly.
  Fail/waste condition: Do not continue normal GSB comparison when neither side can be normally inspected.
  Reason style: 两个模型产物都无法正常打开或显示正常内容，无法查看页面和测试核心功能，直接废弃。

- Pattern: Same structure but only one opens
  Pass/choose condition: If both candidates are structurally the same task output but one cannot open while the other can be inspected, choose the available side as better.
  Fail/waste condition: Do not mark Same when one side is unavailable and the other side can normally display.
  Reason style: 两个产物结构基本一致，但一方无法正常打开，另一方可以正常查看和使用，因此可用的一方更好。

- Pattern: Static reference images
  Pass/choose condition: If the prompt asks to implement content while referencing one or more static images and does not require motion, judge mainly by visual resemblance and visible page effect.
  Fail/waste condition: Do not over-penalize missing script/content logic when the task is essentially static visual reproduction.
  Reason style: 题目主要要求参考静态图片实现视觉效果，因此优先比较整体画面、布局、元素、颜色和参考图贴合度。

- Pattern: Dynamic visual reference
  Pass/choose condition: If the prompt provides a file or visual-effect reference and clearly asks for a dynamic effect, judge mainly by the produced dynamic visual effect.
  Fail/waste condition: Do not choose a visually static or weakly animated output over a candidate that better reproduces the requested motion.
  Reason style: 题目重点是动态视觉效果，因此优先比较动画、状态变化、运动节奏和视觉还原度。

- Pattern: Full screenshot reproduction
  Pass/choose condition: If both candidates are screenshot-like pages and the provided reference image is a complete page screenshot, judge by complete page reproduction.
  Fail/waste condition: Do not judge only isolated components or small local details when the reference is a full-page screenshot.
  Reason style: 参考图是完整页面截图，因此优先比较整页布局、首屏结构、模块位置、视觉层级和页面整体还原度。

Format:

- Pattern: <task or situation>
  Pass/choose condition: <what is enough>
  Fail/waste condition: <what is not enough>
  Reason style: <preferred wording>
