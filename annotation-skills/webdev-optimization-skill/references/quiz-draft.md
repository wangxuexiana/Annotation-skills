# Permission Quiz Draft

No concrete permission questionnaire questions were visible in the fetched materials. Use these as likely quiz facts and draft answers only after seeing the actual quiz.

## Likely Facts

1. WebDev 优化项目采用三档评分：`+1`、`0`、`-1`。
2. `+1` 表示三个维度都通过，交互正常，UI 观感良好。根据 0429 更新，无额外亮点也可以 +1。
3. `0` 表示基本满足题目，但存在瑕疵或可优化点。
4. `-1` 表示严重缺陷，例如核心功能缺失、不遵从 prompt、游戏基本不可玩、UI 严重影响体验。
5. 功能完整度关注 prompt 明确功能点是否覆盖。
6. 功能缺陷关注已实现功能是否有 bug，如按钮无响应、图片加载失败、白屏、控制台报错。
7. 美观度关注布局、样式、对齐、边距、滚动、遮挡、整体观感。
8. 白屏、空白页、单一无功能页面、ready to build 不直接废弃，要新窗口打开产物 URL 并查看控制台。
9. prompt 明确要求移动端或响应式时才强制检查移动端，通常可用 375px 视窗。
10. 标注文案不能提版本、对比、基线、初始版、V0。
11. 动画场景必须有动效，完全没有动效不行。
12. 游戏类未在 prompt 中明确提出的通用扩展功能，默认不作为不通过理由。

## Draft Answer Pattern

- 判断题：优先引用主手册和规则更新日期。
- 单选题：先找关键词对应的维度，功能点覆盖归功能完整度，已实现功能故障归功能缺陷，视觉布局样式归美观度。
- 多选题：白屏、ready to build、控制台报错、资源加载失败等通常都要记录在功能缺陷。
- 问答题：回答要围绕当前产物，不提版本、对比、基线、初始版或 V0。

## Confidence

- High：三档评分、三个维度、白屏控制台规则、移动端按 prompt、文案不提版本。
- Medium：UI 类 0513 规则细节，因为引用文档当前读取失败。
