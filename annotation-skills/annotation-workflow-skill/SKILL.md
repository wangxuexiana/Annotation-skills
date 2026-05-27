---
name: annotation-workflow-skill
description: End-to-end annotation workflow for Feishu training videos, annotation manuals, permission quizzes, task-specific skill generation, and Chrome-based semi-automated annotation queues. Use when Codex needs to learn a newly released annotation task, summarize training materials, draft queue-permission quiz answers, generate or update annotation skills, and later operate the user's browser with confirmation gates.
---

# Annotation Workflow Skill

## Goal

Run a semi-automated annotation onboarding loop: learn the training materials, produce reviewable summaries and quiz drafts, generate a task-specific annotation skill, then use that skill to operate Chrome on the user's annotation queue after permission is open.

Default to human confirmation for quiz submission, permission requests, and final annotation submission. Do not bypass login, CAPTCHA, access control, platform risk checks, or hidden permission gates.

## Workflow State

Use these states and state transitions explicitly:

1. `待学习`: collect Feishu video, transcript, manual, task page text, and any queue instructions.
2. `待答卷`: summarize materials and draft permission quiz answers with evidence.
3. `待开权限`: wait for the user or platform to open the queue; do not repeatedly submit or probe restricted pages.
4. `可标注`: create or update the task-specific skill and confirm the queue entry page.
5. `标注中`: operate Chrome according to the task skill and the user's submission policy.
6. `规则复盘`: incorporate user corrections into learned patterns and reason examples.

## Learning Materials

When a new task is released:

1. Use Chrome because Feishu and the annotation platform need the user's login state.
2. Open the Feishu training video and manual links provided by the user or visible in the release message.
3. Prefer structured material in this order: official manual, video transcript/subtitles, chapter notes, page text, pinned comments, screenshots.
4. If no transcript is available, inspect visible page text and ask the user to export or provide subtitles/audio only when needed.
5. Produce `training-summary.md` with:
   - task type and target queue
   - pass/fail or pairwise decision rules
   - waste/abandon rules
   - required browser test flow
   - easy-to-misjudge cases
   - wording style for reasons
   - quiz facts likely to be tested
6. If the user has historical annotation answers from this or other queues, collect them as `user-style.md` or pass them to the generator with `--style-corpus`. Use those answers for wording style, not for task rules unless the user explicitly says the rule transfers.

Use [workflow-checklist.md](references/workflow-checklist.md) as the operating checklist.

## Permission Quiz

For permission questionnaires:

1. Read each question and identify the rule it is testing.
2. Draft an answer from the training summary or manual only; do not guess from general knowledge when task-specific evidence is missing.
3. For every answer, include the evidence source and confidence.
4. Show the draft to the user before clicking final submit.
5. If the platform gives feedback after submission, update the task skill with corrected rules.

Use [quiz-draft-format.md](references/quiz-draft-format.md) for the output shape.

## Generate Task-Specific Skills

Create one task skill per distinct annotation queue or rubric. The skill name should be short, lowercase, and hyphenated, such as `sft3-skill`, `gsb-skill`, or `aidp-widget-skill`.

Use the bundled generator when summaries are available:

```powershell
python annotation-skills/annotation-workflow-skill/scripts/create_task_skill.py `
  --task-name aidp-widget-skill `
  --output-dir annotation-skills `
  --training-summary path/to/training-summary.md `
  --manual-summary path/to/manual-summary.md `
  --quiz-draft path/to/quiz-draft.md `
  --style-corpus path/to/user-previous-answers.txt
```

The generated skill must include:

- `SKILL.md`: compact operating instructions, safety gates, and review flow.
- `references/training-summary.md`: distilled video/manual notes.
- `references/manual-summary.md`: manual-specific rules.
- `references/quiz-draft.md`: permission quiz answers and evidence, if present.
- `references/learned-patterns.md`: user corrections and recurring judgement rules.
- `references/rule-updates.md`: newest manual updates, quiz feedback, and user corrections that may override earlier rules.
- `references/reason-examples.md`: short natural Chinese reason examples.
- `references/user-style.md`: the user's historical answer style and wording habits, when available.

Generated task skills should reference the shared generic rules in `references/stable-annotation-rules.md` and include only a short fallback summary. Do not duplicate the full shared rules into every generated skill unless the user explicitly wants a standalone snapshot.

After generation, validate with the skill-creator quick validator.

## Live Rule Updates

When the user says a rule changed, a quiz answer was corrected, or the task manual updated, update the task skill immediately before continuing annotation.

Use:

```powershell
python annotation-skills/annotation-workflow-skill/scripts/update_task_skill.py `
  --skill-dir annotation-skills/<task-name>-skill `
  --target rule `
  --title "规则更新标题" `
  --text "新的规则内容" `
  --source "用户纠正/飞书手册/问卷反馈"
```

Targets:

- `rule`: append to `references/rule-updates.md`; use for new rules that may override earlier summaries.
- `pattern`: append to `references/learned-patterns.md`; use for recurring judgement patterns.
- `style`: append to `references/user-style.md`; use for historical answers or user wording preferences.
- `reason`: append to `references/reason-examples.md`; use for new reason examples.
- `quiz`: append to `references/quiz-draft.md`; use for permission quiz feedback.
- `manual`: append to `references/manual-summary.md`; use for newly discovered manual text.

After updating, revalidate the skill. Before annotating, load `rule-updates.md` first because it contains the newest overrides.

## Annotation Execution

When queue permission is open and the user asks Codex to annotate:

1. Load the task-specific skill, not only this workflow skill.
2. Read the task prompt first.
3. Open the scene or candidate link in a separate new Chrome tab/window for testing.
4. Test only the prompt-named core functions and natural visible controls needed for judgement.
5. Close the test tab/window after testing.
6. Return to the original task page and fill the label, reason, and waste flag.
7. Respect the current confirmation policy before final submit.

Default confirmation policy: ask before final quiz submission, permission submission, and annotation submission. If the user explicitly authorizes auto-submit for a queue, apply it only to that queue and keep pausing for login, CAPTCHA, permission, or unclear destructive actions.

## Stable Annotation Rules

Maintain the canonical shared rules in [stable-annotation-rules.md](references/stable-annotation-rules.md). Generated task skills should reference that file and keep only a compact fallback summary. Task-specific manuals, rule updates, and explicit user corrections override shared rules when they clearly conflict.

Core shared rules include:

- Returned/rework tasks are not processed unless the user explicitly asks.
- Blank, white-screen, black-screen, broken, or unrenderable previews are marked as waste/abandoned rather than normal fail.
- Prompt-named core functions outweigh the visual shell.
- Sliders, toggles, buttons, generators, drawing tools, counters, camera controls, and similar named controls must visibly or textually change something.
- Reasons should be short, natural Chinese, with commas instead of slashes for multiple similar items.
- Use more colloquial wording for specialized labels when the user prefers it.

## Updating The System

After any user correction:

1. Update the relevant task skill's `references/learned-patterns.md` when the correction is reusable.
2. Update `references/rule-updates.md` when the correction changes an active judgement rule or overrides the manual.
3. Update `references/user-style.md` or `references/reason-examples.md` when the user corrects wording style.
4. Keep one-off details out of the main skill unless they affect a recurring judgement rule.
5. Revalidate the edited skill.
