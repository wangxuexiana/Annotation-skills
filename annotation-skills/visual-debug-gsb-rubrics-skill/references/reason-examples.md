# Reason Examples

Use these as phrase pools only. Adapt them to the current visible evidence.

- A 更好，A 的移动端菜单能展开并显示完整导航，B 点击菜单无反应。
- B 更好，两边都修复了图片显示，但 B 保留了发音图标和进度条布局，A 修复后卡片错位。
- A 更好，A 修好了题目指出的导航栏高度问题，B 虽然局部更美观但目标问题仍然明显。
- B 更好，B 的表单提交有校验和状态反馈，A 只是静态展示按钮。
- 两者相当，A/B 都没有修复按钮点击后的真实状态变化，只增加了 hover 效果。
- 两者相当，两边都修好了目标问题，剩余差异很小，不影响核心判断。
- 无法判断，A 的候选链接因权限无法打开，无法确认该 rubric 指向的功能是否满足。
- 题目废弃，A/B 链接均无法访问，且无法检查当前问题是否被修复。

## Evidence Pattern Pool

- Target repair: 修好了当前问题，目标区域仍错误，问题仍明显，核心缺陷还在。
- Request/reference match: 布局更接近参考图，主体结构保留更完整，原需求中的导航/表单/卡片仍完整。
- Functional completion: 点击后有状态反馈，菜单能展开收起，主题切换后文字仍可读，提交后有校验结果。
- Side effect: 修复后文字被遮挡，卡片错位，主体内容丢失，页面白屏，关键图片未加载。
- Unable to judge: 链接打不开，关键资源加载失败且无法判断来源，需要登录或特定权限。

