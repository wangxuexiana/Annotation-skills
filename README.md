# Annotation Skills

这个仓库用于存放让 Codex 辅助完成标注任务的 skills。

当前主要包含：

- `annotation-workflow-skill`：总控型半自动化工作流 skill，用来学习在线培训资料、整理标注规则、草拟权限问卷、生成任务专用 skill，并提供后续规则更新接口。
- `sft3-skill`、`gsb-skill`、`coding-aesthetic-pairwise-skill`、`video2code-dynamic-skill`、`visual-coding-verifier-skill`：已经沉淀好的具体标注 skill，用于实际判断和填写标注任务。


## 半自动化工作流

推荐流程是“Codex 自动整理，关键提交人工确认”：

1. 用户提供培训视频、标注手册、任务发布入口或权限问卷。
2. Codex 使用 `annotation-workflow-skill` 读取培训资料，整理 `training-summary.md` 和 `manual-summary.md`。
3. Codex 根据视频总结和手册生成 `quiz-draft.md`，包含推荐答案、依据和置信度。
4. 用户确认问卷答案后，Codex 再控制 Chrome 提交权限问卷。
5. 队列权限开放后，Codex 根据资料生成一个任务专用 skill。
6. 实际标注时，Codex 使用任务专用 skill 控制 Chrome：先看提示词，再按任务规则打开截图、场景或候选页面测试。
7. 用户纠正过的规则会继续沉淀到 `rule-updates.md`、`learned-patterns.md`、`user-style.md` 或 `reason-examples.md`。

默认安全策略：

- 权限问卷提交前需要用户确认。
- 权限申请或开放操作前需要用户确认。
- 最终标注提交前需要用户确认，除非用户明确允许某个队列自动提交。
- 不绕过登录、验证码、权限墙、风控或平台限制。
- 返修题默认不处理。
- 白屏、黑屏、无法渲染或无法判断的任务按废弃处理。

## 目录结构

```text
annotation-skills/
  annotation-workflow-skill/
    SKILL.md
    agents/openai.yaml
    references/
      workflow-checklist.md
      quiz-draft-format.md
    scripts/
      create_task_skill.py
      update_task_skill.py
  coding-aesthetic-pairwise-skill/
    SKILL.md
    agents/openai.yaml
    references/
      training-summary.md
      manual-summary.md
      quiz-draft.md
      rule-updates.md
      learned-patterns.md
      user-style.md
      reason-examples.md
  gsb-skill/
  sft3-skill/
  video2code-dynamic-skill/
  visual-coding-verifier-skill/
```

## 生成任务专用 Skill

`annotation-workflow-skill/scripts/create_task_skill.py` 可以根据培训总结、手册摘要、问卷草稿和用户历史回答生成新的任务专用 skill。

示例：

```powershell
python annotation-skills/annotation-workflow-skill/scripts/create_task_skill.py `
  --task-name example-annotation-task `
  --output-dir annotation-skills `
  --training-summary path/to/training-summary.md `
  --manual-summary path/to/manual-summary.md `
  --quiz-draft path/to/quiz-draft.md `
  --style-corpus path/to/user-previous-answers.txt
```

脚本会生成：

```text
annotation-skills/example-annotation-task-skill/
  SKILL.md
  agents/openai.yaml
  references/training-summary.md
  references/manual-summary.md
  references/quiz-draft.md
  references/rule-updates.md
  references/learned-patterns.md
  references/user-style.md
  references/reason-examples.md
```

常用参数：

- `--task-name`：新任务 skill 名称。脚本会自动规范为小写短横线格式，并在缺少时补上 `-skill`。
- `--output-dir`：新 skill 的输出目录，通常是 `annotation-skills`。
- `--training-summary`：培训视频总结，必填。
- `--manual-summary`：标注手册摘要，可选但推荐提供。
- `--quiz-draft`：权限问卷草稿，可选但推荐提供。
- `--style-corpus`：用户历史标注回答，可选，用于学习用户理由风格。
- `--overwrite`：当目标 skill 已存在时覆盖生成文件。

生成后建议运行校验：

```powershell
python E:/Codex/.codex/skills/.system/skill-creator/scripts/quick_validate.py annotation-skills/example-annotation-task-skill
```

## 实时更新规则

如果标注规则更新、问卷反馈纠正、手册新增说明，使用 `update_task_skill.py` 写入任务 skill。

示例：

```powershell
python annotation-skills/annotation-workflow-skill/scripts/update_task_skill.py `
  --skill-dir annotation-skills/coding-aesthetic-pairwise-skill `
  --target rule `
  --title "规则更新" `
  --text "新的规则内容" `
  --source "用户纠正/标注手册/问卷反馈"
```

`--target` 可选值：

- `rule`：写入 `references/rule-updates.md`，用于最新规则，优先级最高。
- `pattern`：写入 `references/learned-patterns.md`，用于可复用判断规律。
- `style`：写入 `references/user-style.md`，用于用户历史回答或措辞偏好。
- `reason`：写入 `references/reason-examples.md`，用于新的理由示例。
- `quiz`：写入 `references/quiz-draft.md`，用于权限问卷反馈。
- `manual`：写入 `references/manual-summary.md`，用于手册补充。

任务 skill 在标注前应优先读取 `rule-updates.md`。如果新规则和旧总结冲突，以新规则为准。

## 用户风格语料

用户可以把以前写过的标注理由加入 `user-style.md`，让任务 skill 生成的理由更接近用户本人风格。

直接粘贴一条或多条历史回答：

```powershell
python annotation-skills/annotation-workflow-skill/scripts/update_task_skill.py `
  --skill-dir annotation-skills/coding-aesthetic-pairwise-skill `
  --target style `
  --title "历史标注回答" `
  --text "这里粘贴以前写过的标注理由" `
  --source "用户历史回答"
```

如果历史回答很多，可以放进文本文件：

```powershell
python annotation-skills/annotation-workflow-skill/scripts/update_task_skill.py `
  --skill-dir annotation-skills/coding-aesthetic-pairwise-skill `
  --target style `
  --title "历史标注回答-第一批" `
  --file C:\path\to\my-answers.txt `
  --source "用户历史回答"
```

理由生成优先级：

1. 先读取 `user-style.md`，模仿用户句长、措辞、证据顺序和口吻。
2. 再读取 `rule-updates.md`、`training-summary.md`、`manual-summary.md`，确定当前任务规则。
3. 最后参考 `reason-examples.md`，作为补充话术池。

## 实际标注方式

权限开放后，用户先在 Chrome 中打开任务平台和对应队列。Codex 使用任务专用 skill 执行标注：

1. 读取题目提示词。
2. 优先读取 `rule-updates.md`，确认有没有最新规则。
3. 判断是否为返修题；返修题默认跳过。
4. 根据任务类型查看截图、场景或候选页面。
5. 按当前 skill 的规则判断通过、不通过、废弃、A/B/Same 或其他平台选项。
6. 使用 `user-style.md` 和 `reason-examples.md` 写出更接近用户风格的理由。
7. 按当前确认策略决定是否最终提交。

## 维护建议

- 规则变化写入 `rule-updates.md`。
- 可复用题型规律写入 `learned-patterns.md`。
- 用户历史回答和措辞偏好写入 `user-style.md`。
- 新的可复用理由写入 `reason-examples.md`。
- 一次性的题目细节不写入主规则，避免污染后续判断。
- 更新后重新运行 `quick_validate.py`。
