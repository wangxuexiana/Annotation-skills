# Learned Patterns

- Pattern: SingleImage 截图美观度 pairwise
  Choose condition: 只根据两张截图中可见的布局、配色、排版、素材质量、一致性和细节精致度判断模型1或模型2更美观。
  Same condition: 双方整体视觉表现接近，或各有优劣但没有稳定一方更好。
  Waste condition: 白屏、黑屏、乱码、报错、截图质量不足、主体严重裁切、信息太少，或仅凭截图无法判断美观度。
  Reason style: 写截图里的具体审美证据，不写功能是否可用。

- Pattern: 场景适配优先
  Choose condition: 更符合 prompt 和页面用途的一方优先，例如复古主题、仪表盘密度、儿童教育色彩等要贴合场景。
  Same condition: 两边风格不同但都能合理服务场景，且执行质量接近。
  Waste condition: 场景无法从截图判断，且缺少可评价主体。
  Reason style: 说明哪边更贴合页面定位和用户场景，避免只说个人喜欢。

- Pattern: 颜色滥用边界
  Choose condition: 大面积纯色、荧光色、艳紫等高饱和色造成刺眼廉价或色彩轰炸时，另一方通常更优。
  Same condition: 鲜艳配色若与场景匹配且整体协调，不单独视为严重问题。
  Waste condition: 颜色问题本身通常不废弃，除非伴随白屏、渲染失败或无法判断主体。
  Reason style: 说清是“色彩刺眼廉价、跳跃不协调”，不要简单写“颜色多”。

- Pattern: 进取式高质量执行
  Choose condition: 内容丰富、素材精致、视觉统一且完成度高的一方，优于内容空洞、元素单一但没有明显错误的一方。
  Same condition: 一方更丰富但杂乱，另一方更简洁但偏空，整体优劣难拉开。
  Waste condition: 页面过于空白到无法从美观度维度区分优劣时，可按手册选择 same 或在无法判断时废弃。
  Reason style: 区分“丰富且统一”和“空洞单调”，不要把极简自动当高级。
