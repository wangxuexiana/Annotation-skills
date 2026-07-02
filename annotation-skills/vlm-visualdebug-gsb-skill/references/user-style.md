# User Style

## Active Style

- Reasons should be short, natural Chinese, and evidence-based.
- Prefer colloquial wording matching the manual examples when appropriate, such as "胜出", "进行啦修复", "问题还在".
- Use one or two concrete evidence points, not a long rubric dump.
- Avoid empty praise such as "更好看", "更完整", or "更符合要求" unless paired with exact evidence.

## Historical Examples From Manual

- A 胜出，A 把出现的导航栏错位问题进行啦修复，B 虽然修复啦导航栏问题，但是把页面格式进行了挤压导致布局错乱
- B 胜出，A 和 B 都进行啦问题的修复，但是 B 在页面还原与功能实现上比 A 更好，B 实现了表单的提交验证
- A 胜出，两侧的问题修复与视觉完成度接近，但 A 的页面弹出框完全按照 prompt 进行啦实现，B 把多个节点堆在一屏，用户难以理解下一步操作

## Style Notes

- Active wording constraints in this file are hard checks before filling a reason.
- Default comparison reasons should be compact and colloquial.
- Prefer the user's direct annotation voice over formal audit language.
- Use current-task evidence from the prompt, reference image, and tested pages. Use historical answers for style only unless the user says the rule also transfers.
