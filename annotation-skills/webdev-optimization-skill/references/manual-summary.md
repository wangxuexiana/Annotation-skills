# WebDev Optimization Manual Summary

## 2026-06-01 Online Manual Refresh

- Main manual fetched successfully from `https://bytedance.larkoffice.com/wiki/HkXmwvEC1iGAwjkzybMcrpuZnKc`, revision `494`.
- The referenced UI rule document is now readable, revision `602`. UI item comments should add page-angle and atmosphere-angle observations when useful: overall presentation, texture, interaction smoothness, theme fit, and whether the intended mood or emotion comes through. This affects comment detail, not the base scoring logic.
- The 0515 animation rule document is readable, revision `91`. Animation scenes must be dynamic. For animation-scene comments, point out existing problems only, avoid broad expectation writing, and do not apply the UI page-angle or atmosphere-angle expansion.
- The manual explicitly says to open the generated URL separately and, when feasible, inspect console errors and warnings for all items. Console messages are useful iteration evidence but do not automatically determine pass or fail.
- V0/baseline can be used internally as a judging aid, especially for UI `0` vs `+1` tie-breaks, but submitted reasons must not mention version, comparison, baseline, initial version, old version, or V0.
- For all scores and dimensions, reasons should be concrete. If something is unreasonable, write the current state plus the expected behavior or improvement. If no functional defect is found, writing that no obvious functional defect was found is acceptable.

## Sources

- 主手册：`WebDev优化项目标注手册v3.0`，链接 `https://bytedance.larkoffice.com/wiki/HkXmwvEC1iGAwjkzybMcrpuZnKc`。
- 培训会议 1：`https://bytedance.larkoffice.com/minutes/obcnbe7rx2x2eeni1b2y5sdd`。
- 培训会议 2：`https://bytedance.larkoffice.com/minutes/obcngoyv1gke9l8cvub993s3`。
- 疑难数据表：`https://bytedance.larkoffice.com/wiki/VXXKwwXziiTM2vkJhD2cd0CEnyd?table=tbl3kr46g671jME1&view=vewo7OY2Ap`。
- 0515 规则调整：`https://bytedance.larkoffice.com/wiki/VEV2wTD0ziYGVUkm5l4comAXnGW`。
- 手册引用的 `UI 类产物标注规则迭代` 文档当前读取失败，接口返回后端错误 code 10071。已先记录主手册中可见的 UI 规则。

## Official Task Description

- 任务目标：规范 WebDev 优化项目标注操作，确保标注数据准确统一。
- 标注对象：prompt 和模型生成的 Web 产物，包含标注平台视窗和可单独打开的 URL。
- 标注平台：AIDP。
- 标注人员需严格遵照手册，标注质量直接关联结算和汰换。

## Output Fields

- 分值：`+1`、`0`、`-1`。
- 维度：功能完整度、功能缺陷、美观度。
- 总体评价：完成打分后写明具体原因，建议约 30 字。
- 特殊问题：白屏、空白页、ready to build、单一无功能页、控制台报错、资源异常等需在功能缺陷中说明。

## Score Definitions

| 分值 | 定义 | 官方描述 |
| --- | --- | --- |
| +1 | 优质 | 交互完全正常，UI 观感良好，页面这样已经不错 |
| 0 | 合格 | 基本满足题目，但偶有瑕疵，还有可优化点 |
| -1 | 不合格 | 美观度、功能完整度、功能缺陷上存在严重问题，例如不遵从题目、边距或对齐明显问题、游戏基本不可玩、UI 交互滚动影响观感 |

## Dimension Definitions

### 功能完整度

- 判断 prompt 明确要求的功能点是否实现。
- 如果 prompt 明确提到 tab、跳转、弹窗、主题切换、颜色、控件、玩法、动画等，必须验证。
- 未在 prompt 中提及的通用游戏特性，默认不纳入功能完整度考核。
- 在功能正常完成的前提下，部分扩展功能只能作为加分项，不能作为不通过原因。

### 功能缺陷

- 判断模型实现出的功能是否有 bug。
- 包括按钮无响应、链接跳转异常、图片加载失败、页面白屏、控制台报错、画布或画笔失灵、资源加载异常。
- 即使 prompt 未明确规定某个按钮的跳转逻辑，页面上自然设计出的按钮如果无反应，也属于功能缺陷。
- 模块较多但没实现的功能，若有 `敬请期待` 等提示会更友好。

### 美观度

- 判断页面中不合理布局或样式。
- 对 UI：不死抠细节，整体观感良好、满足基本需求、无多处或重大交互缺陷即可通过。
- 在没有明显 UI 缺陷时，可以提出美学建议；若有缺陷，应先指出缺陷。

## Official Rule Updates

- 0429：只要所有维度都通过就可以 +1，无亮点也可。
- 0430：模型产出物本身可能有 bug。白屏或单一无功能页面属于正常现象，需要新窗口打开 URL，F12 打开控制台，把具体报错复制到功能缺陷维度。
- 0506：`ready to build` 多为模型未编译完成。若有报错，打开控制台复制报错并登记到功能缺陷；若无报错，仅备注 ready to build 状态。
- 0507：移动端适配要按 prompt 判断。prompt 明确要求移动端友好或相关内容时，以 375px 等移动端常用视窗检查；prompt 未提及或明确为 web 场景时，不强制按移动端适配减分。
- 0513：UI 类产物打分门槛提高，维度判断增加。具体文档暂未成功读取，先以主手册可见 UI 规则为准。
- 0515：动画场景新增规则，完全没有动效不行；评语只指出存在问题，无需发散性标注期待效果。

## Annotation Text Rule

- 可以参考旧版本或初始版本帮助自己判断，但提交文案中不能提版本、对比、基线、初始版、V0 等字眼。
- 标注文案只描述当前产物本身，写当前哪里做得好、哪里有问题、预期逻辑应是什么。

## Case Notes From Doubt Table

- 简单贺卡类：只用 enjoy 表情但整体表现可接受时，若参考旧产物明显更好，可倾向 +1。
- 过于简单的贺卡：完成度高但功能简单，且相对旧产物无明显提升时，倾向 0。
- UI 批次中出现游戏模拟器需求时，按 prompt 的核心需求判断，不只看批次名。
- 多人测试结果不一致时，可按多数可复现结果处理，并记录设备、浏览器、屏幕或网络差异。
- 白屏类需要记录具体控制台报错，例如 ReferenceError、TypeError、R3F hooks 或 THREE namespace 错误。
- 不同视口导致动画渲染异常，例如小于 1024 正常、大于等于 1024 彩色横线，应记录为渲染/适配问题。

## Compliance And Workflow

- 单条数据领取超过 60 分钟自动释放。
- 返修数据 18 小时不处理自动释放。
- 质检不可自标自检。
- 每条 case 返修机会有限，返修后仍不达标不予结算。
- 白屏和空白页先不予结算，但标注阶段仍需按规则记录问题。
