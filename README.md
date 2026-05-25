# Annotation Skills

这个仓库用于存放让 Codex 辅助完成标注任务的 skills。当前包含两类内容：

- `annotation-workflow-skill`：总控型半自动化工作流 skill，用来学习培训资料、整理规则、草拟权限问卷，并生成具体任务的标注 skill。
- `sft3-skill`、`gsb-skill`：已经沉淀好的具体标注 skill，用于实际判断和填写标注任务。

## 半自动化工作流

推荐流程是“Codex 自动整理，关键提交人工确认”：

1. 用户提供飞书培训视频、标注手册或任务发布入口。
2. Codex 使用 `annotation-workflow-skill` 读取培训资料，整理 `training-summary.md`。
3. Codex 根据视频总结和手册生成 `quiz-draft.md`，包含推荐答案、依据和置信度。
4. 用户确认问卷答案后，Codex 再控制 Chrome 提交权限问卷。
5. 队列权限开放后，Codex 根据资料生成一个任务专用 skill。
6. 实际标注时，Codex 使用任务专用 skill 控制 Chrome：先看提示词，再新标签打开场景测试，测试完成后关闭新标签，回到题目页填写标注。
7. 用户纠正过的规则会继续沉淀到 `learned-patterns.md` 和 `reason-examples.md`。

默认安全策略：

- 权限问卷提交前需要用户确认。
- 权限申请或开放操作前需要用户确认。
- 最终标注提交前需要用户确认，除非用户明确允许某个队列自动提交。
- 不绕过登录、验证码、权限墙、风控或平台限制。
- 返修题默认不处理。
- 白屏、黑屏、无法渲染的任务按废弃处理。

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
  gsb-skill/
    SKILL.md
    agents/openai.yaml
    references/
  sft3-skill/
    SKILL.md
    agents/openai.yaml
    references/
```

## 生成任务专用 Skill

`annotation-workflow-skill/scripts/create_task_skill.py` 可以根据培训总结、手册摘要和问卷草稿生成新的任务专用 skill。

示例：

```powershell
python annotation-skills/annotation-workflow-skill/scripts/create_task_skill.py `
  --task-name aidp-widget `
  --output-dir annotation-skills `
  --training-summary path/to/training-summary.md `
  --manual-summary path/to/manual-summary.md `
  --quiz-draft path/to/quiz-draft.md
```

脚本会生成：

```text
annotation-skills/aidp-widget-skill/
  SKILL.md
  agents/openai.yaml
  references/training-summary.md
  references/manual-summary.md
  references/quiz-draft.md
  references/learned-patterns.md
  references/reason-examples.md
```

参数说明：

- `--task-name`：新任务 skill 名称。脚本会自动规范为小写短横线格式，并在缺少时补上 `-skill`。
- `--output-dir`：新 skill 的输出目录，通常是 `annotation-skills`。
- `--training-summary`：培训视频总结，必填。
- `--manual-summary`：标注手册摘要，可选但推荐提供。
- `--quiz-draft`：权限问卷草稿，可选但推荐提供。
- `--overwrite`：当目标 skill 已存在时覆盖生成文件。

生成后建议运行校验：

```powershell
python E:/Codex/.codex/skills/.system/skill-creator/scripts/quick_validate.py annotation-skills/aidp-widget-skill
```

## 实际标注方式

权限开放后，用户先在 Chrome 中打开任务平台和对应队列。Codex 使用任务专用 skill 执行标注：

1. 读取题目提示词。
2. 判断是否为返修题；返修题默认跳过。
3. 打开场景或候选页面到新标签页测试。
4. 优先测试提示词明确要求的核心功能。
5. 白屏、黑屏、无法渲染时选择废弃。
6. 测试后关闭新标签页，回到任务页填写结论和理由。
7. 按当前确认策略决定是否最终提交。

## 维护规则

当用户纠正 Codex 的判断或话术时，应更新对应任务 skill：

- 可复用判断规则写入 `references/learned-patterns.md`。
- 标注理由风格写入 `references/reason-examples.md`。
- 一次性的题目细节不写入主规则，避免污染后续判断。
- 更新后重新运行 `quick_validate.py`。
