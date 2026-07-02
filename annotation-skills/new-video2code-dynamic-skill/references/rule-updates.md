# Rule Updates

Newer entries override older summaries when they clearly conflict. Add updates with `update_task_skill.py` or append manually.

## Active Overrides

- 新标准同步覆盖旧流程：静态还原度为0分时，Rubric不用逐项打分，只需要评估整体动效，并在备注原因中写明给分理由。
- 静态页面核心内容缺失、主要元素丢失、首页无内容或严重不可判断时，优先按废弃/不可判断处理；若平台没有废弃入口，再按静态0并说明原因。
- 整体动效1分要求全部动效和交互都能对应上视频和原始/GT HTML；不能因为核心项完成、非核心项缺失就给整体动效1分。
- 整体动效1分需要慎重给分，必须逐项确认所有可见动效和交互都对齐后再给；只要存在未确认、缺失或不匹配的动效/交互，优先不给1分。

## Update Log

- 2026-06-06: Generated from primary Video2code manual and RFT bon7 static reference manual.
- 2026-06-06: User clarified that overall dynamic score 1 requires all dynamic effects and interactions to match video and original/GT HTML.
- 2026-06-06: User emphasized being conservative when assigning overall dynamic score 1.

## 2026-06-06 Note Formatting Override

- 备注需要分两行写，第一行写 `还原度：...`，第二行紧接着写 `整体动效：...`；两行之间不要出现空白行，避免质检侧看不见后半段。
