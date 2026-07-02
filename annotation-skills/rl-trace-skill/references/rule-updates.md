# Rule Updates

Newer entries override older summaries when they clearly conflict. Add updates with `update_task_skill.py` or append manually.

## Active Overrides

- 对未实现或不满足而打 0 分的 rubric，必须在对应说明框中写明具体原因，不能只选择 0 后留空。

## Update Log

- 2026-06-24: Added user correction that every 0-scored unimplemented rubric needs a concrete reason in its explanation field.

## 2026-06-25 Current Page Rubric Override

- 每道题必须先读取当前页面实际显示的 rubric 名称和顺序，再按这些 rubric 逐项评判和输出。
- 不允许套用固定的视觉检查项模板或固定 6 项顺序，除非当前页面实际就是这些 rubric。
- 输出给用户复制时，rubric 标题必须尽量复用页面原文，0 分项仍必须在对应说明里写具体原因。
