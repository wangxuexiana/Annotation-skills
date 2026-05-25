#!/usr/bin/env python3
"""Generate a task-specific annotation skill from training artifacts."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


def slugify(name: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", name.strip().lower()).strip("-")
    if not slug:
        raise SystemExit("task name must contain at least one letter or digit")
    if not slug.endswith("-skill"):
        slug += "-skill"
    if len(slug) > 63:
        raise SystemExit("skill name must be 63 characters or fewer")
    return slug


def read_optional(path: str | None, fallback: str) -> str:
    if not path:
        return fallback
    p = Path(path)
    if not p.exists():
        raise SystemExit(f"missing input file: {p}")
    return p.read_text(encoding="utf-8-sig")


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def skill_md(skill_name: str) -> str:
    title = skill_name.replace("-", " ").title()
    return f"""---
name: {skill_name}
description: Task-specific annotation rubric generated from Feishu training materials and annotation manuals. Use when Codex needs to judge, compare, or label this queue's tasks in Chrome using the distilled training rules, permission-quiz evidence, learned patterns, and user-preferred reason style.
---

# {title}

## Goal

Use the bundled training summary and manual rules to complete this specific annotation queue. Prioritize task-specific training rules over generic annotation habits.

Default confirmation policy: ask the user before final questionnaire submission, permission submission, or final annotation submission unless the user explicitly authorizes auto-submit for this queue.

## Required References

Read the relevant reference before working:

- `references/training-summary.md` for video and onboarding conclusions.
- `references/manual-summary.md` for official manual rules.
- `references/quiz-draft.md` when answering or reviewing permission quizzes.
- `references/learned-patterns.md` for user corrections and repeated cases.
- `references/rule-updates.md` for latest rule changes. Read this before older summaries because it may override previous understanding.
- `references/reason-examples.md` for short natural Chinese wording.
- `references/user-style.md` when the user has provided previous annotation answers; imitate those sentence patterns first.

## Review Flow

1. Identify whether the current item is a normal annotation task, a returned/rework task, a permission quiz, or an inaccessible page.
2. Do not process returned/rework tasks unless the user explicitly asks.
3. Read the task prompt and extract the core requirement before testing.
4. Open the scene, candidate, or preview link in a separate new Chrome tab/window.
5. Test prompt-named core functions and visible natural controls.
6. Close the test tab/window after testing.
7. Return to the original task page and fill the judgement and reason.
8. Pause before final submission unless this queue has explicit user approval for auto-submit.

## Stable Rules

- Blank, white-screen, black-screen, broken, or unrenderable previews should be marked as waste/abandoned when the platform supports it.
- Prompt-named functions have higher weight than visual similarity.
- Named controls such as sliders, toggles, buttons, drawing tools, generators, counters, and camera controls must visibly or textually change something.
- Good-looking static output does not pass if the named core behavior is missing.
- Reasons should be short, direct, and natural Chinese. Use Chinese commas or pause marks, not slashes, for multiple similar items.

## Reason Style

When writing reasons, follow this priority:

1. If `references/user-style.md` contains historical answers from the user, imitate its sentence length, wording habits, and level of detail.
2. Use `training-summary.md` and `manual-summary.md` to decide which evidence matters for this queue.
3. Use `reason-examples.md` as a backup phrase pool, not as fixed templates.

Do not copy old answers mechanically. Adapt the user's style to the current task and current visible evidence.

## Rule Updates

Before each annotation batch, check `references/rule-updates.md` first. If it contains a newer rule that conflicts with `training-summary.md`, `manual-summary.md`, or `learned-patterns.md`, follow the newer rule and mention the conflict to the user when it affects the current task.

## Quiz Flow

When answering a permission quiz:

1. Use only `training-summary.md`, `manual-summary.md`, and visible quiz/training evidence.
2. Draft each answer with evidence and confidence.
3. Ask the user to confirm before clicking final submit.
4. If feedback reveals a wrong assumption, update `learned-patterns.md`.

## Skill Evolution

When the user corrects a judgement or wording, update `references/learned-patterns.md` or `references/reason-examples.md` with the reusable rule. Keep entries short and general so future labels do not sound copied.
"""


def openai_yaml(skill_name: str) -> str:
    display = skill_name.replace("-", " ").title()
    return f"""display_name: {display}
short_description: Task-specific annotation queue rubric.
default_prompt: Use this skill to annotate this queue in Chrome using its training summary, manual rules, learned patterns, and reason examples.
"""


def default_learned_patterns() -> str:
    return """# Learned Patterns

Add reusable user corrections here.

Format:

- Pattern: <task or situation>
  Pass/choose condition: <what is enough>
  Fail/waste condition: <what is not enough>
  Reason style: <preferred wording>
"""


def default_rule_updates() -> str:
    return """# Rule Updates

Newer entries override older summaries when they clearly conflict. Add updates with `update_task_skill.py` or append manually.

## Active Overrides

- None yet.

## Update Log
"""


def default_reason_examples() -> str:
    return """# Reason Examples

Add short natural Chinese examples here after real tasks are reviewed.

- 通过：核心功能可以正常操作，反馈也比较明确
- 不通过：按钮点击后没有变化，关键功能不可用
- 废弃：页面白屏，无法判断核心内容
"""


def default_user_style(style_corpus: str | None) -> str:
    if style_corpus:
        return f"""# User Style

Use these historical answers as the main style source for future reasons. Learn wording habits, sentence length, evidence order, and preferred plain-language phrasing. Do not copy old answers verbatim unless the same situation truly repeats.

## Historical Answers

```text
{style_corpus.strip()}
```

## Style Notes

- Prefer the user's direct annotation voice over formal audit language.
- Keep reasons compact unless the queue explicitly asks for detailed comparison.
- Use current-task evidence from the manual and screenshots; use historical answers for style only unless the user says the rule also transfers.
"""
    return """# User Style

Use this file as the first source for reason wording when the user provides historical annotation answers.

## How To Learn From User Answers

- Extract sentence length, common verbs, judgement order, and how much evidence the user usually gives.
- Preserve the user's direct style, but do not copy old answers verbatim unless the same situation truly repeats.
- Convert historical reasons from other task types into style only, not judgement rules, unless the user says the rule also applies here.
- Prefer concrete visible evidence over abstract praise.
- Keep reasons compact; most should be one sentence.

## Historical Answers

```text
（等待用户提供历史标注回答）
```
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--task-name", required=True, help="Skill name or queue name")
    parser.add_argument("--output-dir", required=True, help="Directory that will contain the new skill folder")
    parser.add_argument("--training-summary", required=True)
    parser.add_argument("--manual-summary")
    parser.add_argument("--quiz-draft")
    parser.add_argument("--style-corpus", help="Optional file containing the user's historical annotation answers")
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()

    skill_name = slugify(args.task_name)
    out_dir = Path(args.output_dir).resolve()
    skill_dir = out_dir / skill_name
    if skill_dir.exists() and not args.overwrite:
        raise SystemExit(f"{skill_dir} already exists; pass --overwrite to replace generated files")

    training = read_optional(args.training_summary, "")
    manual = read_optional(args.manual_summary, "# Manual Summary\n\nNo manual summary was provided.")
    quiz = read_optional(args.quiz_draft, "# Quiz Draft\n\nNo permission quiz draft was provided.")
    style = read_optional(args.style_corpus, "") if args.style_corpus else ""

    write(skill_dir / "SKILL.md", skill_md(skill_name))
    write(skill_dir / "agents" / "openai.yaml", openai_yaml(skill_name))
    write(skill_dir / "references" / "training-summary.md", training)
    write(skill_dir / "references" / "manual-summary.md", manual)
    write(skill_dir / "references" / "quiz-draft.md", quiz)
    write(skill_dir / "references" / "user-style.md", default_user_style(style))
    write(skill_dir / "references" / "rule-updates.md", default_rule_updates())

    learned = skill_dir / "references" / "learned-patterns.md"
    reasons = skill_dir / "references" / "reason-examples.md"
    if not learned.exists() or args.overwrite:
        write(learned, default_learned_patterns())
    if not reasons.exists() or args.overwrite:
        write(reasons, default_reason_examples())

    print(f"created {skill_dir}")
    print("next: validate with quick_validate.py")


if __name__ == "__main__":
    main()
