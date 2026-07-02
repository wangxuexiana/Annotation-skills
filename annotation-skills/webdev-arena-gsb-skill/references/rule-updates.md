# Rule Updates

Newer entries override older summaries when they clearly conflict. Add updates with `update_task_skill.py` or append manually.

## Active Overrides

- 2026-07-01: Latest 2.2 topic-judgement rules from the manual screenshot. Apply these hard gates before normal GSB comparison:
  1. If both model products cannot open normally or cannot display normal content, mark abandoned or waste directly.
  2. If two products are structurally the same and one cannot open while the other is available, the available side is better.
  3. If the prompt requires an implementation and asks to reference one or more images, but the image is static and does not need motion, judge mainly by visual effect; script/content logic can be ignored.
  4. If the prompt itself is unreasonable, such as asking for Markdown file content but the output is a webpage, the required output form does not match; mark abandoned or waste directly.
  5. If the prompt provides a file or visual-effect reference and explicitly asks to make a dynamic effect, judge mainly by the dynamic visual effect.
  6. If the prompt asks to operate on existing HTML but does not provide the reference image or enough source/reference information, the information is missing; mark abandoned or waste directly.
  7. If two pages render as screenshots and the provided reference image is also a complete screenshot, judge by complete page reproduction.

- 2026-07-01：本 skill 基于飞书 Wiki《WebDev Arena GSB 标注手册》和妙记《人标支持 GSB 评估—WebDev Arena-0630》生成。队列要求详细评价，理由必须覆盖双方优缺点和关键差距，不能只写短句结论。

## Update Log
