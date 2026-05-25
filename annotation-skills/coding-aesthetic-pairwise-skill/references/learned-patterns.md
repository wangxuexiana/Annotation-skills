# Learned Patterns

- Pattern: Coding 美观度 pairwise
  Choose condition: 只根据截图可见的布局、配色、素材精致度、信息层级、整体协调性判断 repo_0 与 repo_1 哪个更美观。
  Same condition: 两边整体美观度接近，或各有优劣但没有明显一方更好。
  Waste condition: 白屏、黑屏、报错、截图无法反映 prompt 要求内容、仅通过截图无法判断。
  Reason style: 用截图可见证据说明差异，不写功能交互是否可用。

- Pattern: 多截图场景
  Choose condition: 综合整套截图的统一性、视觉舒适度和内容丰富度，不按截图数量定胜负。
  Same condition: 一方内容更满，另一方更简约舒适，整体差距不明显。
  Waste condition: 关键截图缺失到无法判断 prompt 要求内容。
  Reason style: 说明“整体风格更统一”“多页视觉更协调”“留白更舒服”等具体原因。

- Pattern: 素材与 emoji
  Choose condition: 精致统一的图标或 SVG 素材通常优于系统原生 emoji 堆叠。
  Same condition: emoji 或素材差异不影响整体布局和视觉观感。
  Waste condition: 素材严重裂图或主体截图不可判断。
  Reason style: 说明素材是否精致、统一、廉价或突兀。
