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

- `references/priority-rules.md` for rule priority, conflict handling, and what each file is allowed to decide.
- `references/decision-checklist.md` for the per-item executable judgement checklist. Complete it before deciding.
- `references/pre-submit-audit.md` for the final audit before filling or submitting an answer.
- `references/common-failure-patterns.md` for recurring traps and concrete examples.
- `references/training-summary.md` for video and onboarding conclusions.
- `references/manual-summary.md` for official manual rules.
- `references/quiz-draft.md` when answering or reviewing permission quizzes.
- `references/learned-patterns.md` for user corrections and repeated cases.
- `references/rule-updates.md` for latest rule changes. Read this before older summaries because it may override previous understanding.
- `references/reason-examples.md` for short natural Chinese wording.
- `references/user-style.md` for active wording constraints and the user's historical answer style. Treat explicit punctuation and tone preferences in that file as hard checks.

## Per-Item Execution Contract

Do not rely on memory from the full skill. For every annotation item, follow this short execution contract:

1. Read `references/priority-rules.md` and `references/rule-updates.md` before the first item in a batch.
2. Read the current page prompt and update `state/current-item.md` with the item type, applicable rule sources, and prompt summary.
3. Convert the current task prompt into a 3-8 point current-item checklist using `references/decision-checklist.md`, including the full applicable rule set rather than only the newest correction.
4. Compress browser testing into `state/browser-observation.json`; do not keep long DOM dumps, long accessibility snapshots, or repeated screenshot descriptions in chat.
5. Check hard gates and waste/abandon conditions before normal pass/fail or pairwise judgement.
6. Test the prompt-named core functions and visible natural controls.
7. Compare observations against the current-item checklist one point at a time.
8. Write the draft label, reason, and audit notes back to `state/current-item.md` while the item is active. After successful annotation, do not append completed answers, results, or submission status to a local log unless the user explicitly asks for logging.
9. Draft the reason under the active constraints in `references/user-style.md`, then run `references/pre-submit-audit.md` before filling the final label or reason.
10. Pause if a rule conflict, hidden permission gate, login challenge, CAPTCHA, destructive action, or unresolved uncertainty appears.

## Context Budget Contract

Keep the live chat context small and recoverable:

- Store per-item working state in `state/current-item.md`, not in long chat narration.
- Store browser observations in `state/browser-observation.json` using the fixed schema from the state template.
- Store reusable user corrections in `state/corrections.md` before merging them into references with `update_task_skill.py --from-correction-log`.
- Store unresolved blockers in `state/pending-uncertainties.md`.
- Use screenshots only as evidence pointers; summarize what matters instead of retaining large visual descriptions.
- After context compaction or a new session, restore from `state/current-item.md`, `state/pending-uncertainties.md`, `references/priority-rules.md`, and `references/rule-updates.md`.

## Review Flow

1. Complete the Per-Item Execution Contract before deciding the label.
2. Do not process returned/rework tasks unless the user explicitly asks.
3. Read the task prompt and extract the core requirement before testing.
4. Open the scene, candidate, or preview link in a separate new Chrome tab/window.
5. Test prompt-named core functions and visible natural controls.
6. Close the test tab/window after testing.
7. Return to the original task page and fill the judgement and reason.
8. Pause before final submission unless this queue has explicit user approval for auto-submit.

## Stable Rules

Read the shared generic rules first:

- `../annotation-workflow-skill/references/stable-annotation-rules.md`

Task-specific manuals, `references/rule-updates.md`, and explicit user corrections override shared generic rules when they clearly conflict.

Minimal fallback if the shared file is unavailable:

- Broken or unrenderable previews are waste/abandoned when supported.
- Prompt-named core functions outweigh visual polish.
- Named controls must produce visible or textual changes.
- Reasons should be short, direct, and natural Chinese.

## Reason Style

When writing reasons, follow this priority:

1. If `references/user-style.md` contains active wording constraints, such as comma-only punctuation or colloquial wording, treat them as hard checks.
2. If `references/user-style.md` contains historical answers from the user, imitate its sentence length, wording habits, and level of detail.
3. Use `training-summary.md` and `manual-summary.md` to decide which evidence matters for this queue.
4. Use `reason-examples.md` as a backup phrase pool, not as fixed templates.

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

When the user corrects a judgement or wording, update `references/learned-patterns.md`, `references/user-style.md`, or `references/reason-examples.md` with the reusable rule. Keep entries short and general so future labels do not sound copied.
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

## Starter Guardrails

- Pattern: Full rubric coverage
  Pass/choose condition: The judgement considered every applicable rule family for the item, including prompt fit, layout, element completeness, content accuracy, visual details, hallucination control, broken images, and function checks when functions are part of the task.
  Fail/waste condition: The judgement focused only on the latest user correction or one visible detail while ignoring higher-priority applicable rules.
  Reason style: Keep the reason grounded in the main deciding evidence.

- Pattern: User wording constraints
  Pass/choose condition: The submitted reason follows active punctuation and tone constraints in `user-style.md`.
  Fail/waste condition: The reason uses formal audit language, extra punctuation, or a copied template that conflicts with the user's requested style.
  Reason style: Natural, compact, colloquial Chinese, with comma-only clause breaks when that preference is active.

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


def default_priority_rules() -> str:
    return """# Priority Rules

Use this file to decide which rule wins and what each reference file is allowed to influence.

## Rule Priority

Apply rules in this order:

1. Current explicit user instruction in the chat.
2. User correction for this queue.
3. `references/rule-updates.md`.
4. Current official manual or visible platform instruction.
5. `references/manual-summary.md`.
6. `references/training-summary.md`.
7. `references/learned-patterns.md` when it matches the same situation.
8. `../annotation-workflow-skill/references/stable-annotation-rules.md`.
9. General judgement only when no task-specific rule exists.

## File Roles

- `rule-updates.md`: newest active overrides. This can change judgement.
- `manual-summary.md`: official task rules. This can change judgement.
- `training-summary.md`: distilled onboarding rules. This can change judgement unless a newer file conflicts.
- `learned-patterns.md`: reusable corrections and repeated cases. This can change judgement only when the same pattern appears.
- `common-failure-patterns.md`: examples that make abstract rules concrete. Use as analogies, not fixed labels.
- `reason-examples.md`: wording support only. It must not change the label.
- `user-style.md`: wording style only unless the user explicitly says a historical rule transfers.

## Conflict Handling

- If a newer task-specific rule conflicts with an older summary, follow the newer rule.
- Treat new user corrections as guardrails inside the full rubric, not replacements for all other applicable rules.
- Do not overfit to the newest correction, and do not underfit by skipping older official rules that still apply.
- If a conflict changes the current label, pause and mention the conflict before submitting.
- If only the reason wording is affected, follow `user-style.md` and keep judging from task rules.
"""


def default_decision_checklist() -> str:
    return """# Decision Checklist

For every item, build a short current-item checklist before judging. Do not try to hold the whole rubric in memory.

## Step 1: Classify The Item

- [ ] Is this a normal annotation item?
- [ ] Is it returned/rework, permission quiz, inaccessible, or outside the requested queue?
- [ ] Is there a login, CAPTCHA, permission, risk, or account challenge that requires pausing?

## Step 2: Extract Current Core Requirements

Before judging, write a `current-item-checklist` with 3-8 concrete checks for this exact prompt. The checklist is mandatory evidence, not optional notes. Each final judgement must reference these checks one by one.

- [ ] Core output or scene requested:
- [ ] Prompt-named controls or interactions:
- [ ] Required data, text, visual state, or comparison target:
- [ ] Must-not-have failure modes from this queue:
- [ ] Pairwise comparison basis, if applicable:
- [ ] Full applicable rule set for this item, not only the newest correction:

## Step 2.5: External State

- [ ] `state/current-item.md` contains the current item type, prompt summary, applicable rule sources, current-item checklist, draft label, draft reason, and pre-submit audit notes.
- [ ] `state/browser-observation.json` contains only structured observations using these keys: `task_id`, `prompt`, `page_load_state`, `tested_controls`, `visible_evidence`, `failures`, `screenshots`, `uncertain_points`, and `recommended_pause`.
- [ ] Long DOM dumps, long accessibility snapshots, repeated screenshot descriptions, and unrelated browser history are not kept in chat.
- [ ] If an uncertainty remains, add it to `state/pending-uncertainties.md` and pause instead of guessing.
- [ ] If the user corrects a reusable rule or style, add it to `state/corrections.md` before merging it into references.

## Step 3: Hard Gates First

- [ ] Page or preview loads and is inspectable.
- [ ] It is not blank, white-screen, black-screen, broken, or unrenderable.
- [ ] Key visible images are not broken, especially hero, card, product, avatar, doctor, chart, gallery, and other required content images.
- [ ] The core requested feature exists visibly.
- [ ] The page can be judged from visible behavior, not hidden DOM evidence.

If a hard gate fails and the platform supports waste or abandon, prefer waste/abandon over normal fail.

Broken images in key visible content are significant element-completeness or visual-restoration defects. Whole-page blank, unrenderable, or uninspectable states remain waste/abandon when supported.

## Step 4: Functional Checks

- [ ] Test each prompt-named control or natural visible control needed for judgement.
- [ ] Verify that clicks, inputs, sliders, toggles, generators, drawing tools, counters, or camera controls visibly or textually change something.
- [ ] Judge core behavior before visual polish.
- [ ] For pairwise tasks, compare both candidates against the prompt and rubric before choosing.

## Step 5: Decide

- [ ] Label follows the highest-priority applicable rule.
- [ ] I cited the current-item checklist point by point when forming the judgement.
- [ ] I considered all applicable dimensions from the priority stack, not only the most recent correction or the most obvious visual detail.
- [ ] New user corrections were used as guardrails inside the full rubric, not as replacements for other rules.
- [ ] For pairwise tasks, I first checked whether higher-priority dimensions have a clear winner.
- [ ] I did not flatten to Same because of lower-priority color, image mood, or small visual details when layout, position, size, spacing, first-screen content, module order, or core content clearly differs.
- [ ] Reason names the main working or broken core point.
- [ ] Reason style follows active constraints in `user-style.md`, including comma-only punctuation and colloquial wording when requested, and uses `reason-examples.md` only as a phrase pool.
"""


def default_pre_submit_audit() -> str:
    return """# Pre-Submit Audit

Run this audit before filling the final label, reason, waste flag, or quiz answer.

## Judgement Audit

- [ ] Did I read the current task prompt and extract the core requirement?
- [ ] Did I apply `priority-rules.md` and newest `rule-updates.md`?
- [ ] Did I write a 3-8 point current-item checklist in `state/current-item.md` before deciding?
- [ ] Did I compress browser observations into `state/browser-observation.json` instead of retaining long browser context in chat?
- [ ] Did I compare the final judgement against each current-item checklist point?
- [ ] Did I apply the full applicable rubric instead of over-focusing on the newest correction?
- [ ] Did I avoid overfitting to the latest user correction while still applying it as a guardrail?
- [ ] Did I avoid missing any higher-priority rule from `priority-rules.md`, `rule-updates.md`, the visible platform instruction, or the official manual summary?
- [ ] Did I list the applicable dimensions before deciding, including layout, element completeness, content accuracy, visual details, hallucination control, function checks when relevant, broken images, and active user wording constraints?
- [ ] Did I check waste/abandon conditions before normal fail?
- [ ] Did I check both candidates or the current preview for broken images in key visible content?
- [ ] Did I test prompt-named core functions instead of judging only the visual shell?
- [ ] Did every tested control produce visible or textual feedback when required?
- [ ] For pairwise tasks, did I compare higher-priority dimensions before color mood, decorative polish, or small details?
- [ ] For pairwise tasks, did I avoid forcing Same when a higher-priority dimension clearly favors one side?
- [ ] Did I avoid using hidden DOM, code, or metadata as feature evidence?

## Reason Audit

- [ ] Reason matches the actual visible evidence.
- [ ] Reason is short, natural Chinese, and focused on the main core issue.
- [ ] Reason follows all active constraints in `user-style.md`.
- [ ] If comma-only punctuation is active, the reason uses commas for clause breaks and contains no other punctuation.
- [ ] Reason sounds like a human annotation note, not a formal audit report.
- [ ] Reason does not include unnecessary technical jargon.
- [ ] Reason examples and old user answers were used as style anchors, not copied blindly.

## Submission Gate

- [ ] No login, CAPTCHA, permission, account, payment, or irreversible-action prompt is blocking the page.
- [ ] No unresolved item in `state/pending-uncertainties.md` affects this label, reason, waste flag, quiz answer, or final submit.
- [ ] No completed-answer/result/submission-status log will be written locally unless the user explicitly asked for logging.
- [ ] The user has approved final submission, or this exact queue has explicit auto-submit approval.

If any box is uncertain, pause and resolve it before submitting.
"""


def default_common_failure_patterns() -> str:
    return """# Common Failure Patterns

Use these examples to avoid missing recurring rules. Add queue-specific examples as real cases appear.

## Static Shell Instead Of Function

Situation: The page looks polished, but the prompt-named button, slider, toggle, generator, editor, or scene control does not change anything.

Judgement: Treat the core function as missing or failed, even if the visual design is good.

Reason pattern: 核心控件操作后没有实际反馈，关键功能不可用

## Waste Mistaken For Fail

Situation: The preview is blank, broken, stuck loading, black-screen, white-screen, or cannot be inspected enough to judge.

Judgement: Prefer waste or abandoned when the platform supports it.

Reason pattern: 页面无法正常渲染，无法判断核心内容

## Prompt Ignored

Situation: The candidate provides a generic page or game, but misses the specific object, workflow, comparison target, or interaction named in the prompt.

Judgement: Fail or choose the other candidate when the missing prompt requirement is central.

Reason pattern: 没有体现题目要求的核心内容

## Pairwise Personal Taste Trap

Situation: One candidate looks prettier, but the other follows the prompt and functional requirements better.

Judgement: Choose the candidate that better satisfies the task rubric, not the one that is merely more visually polished.

Reason pattern: 更符合题目要求，核心功能和反馈更完整

## Priority Flattening Trap

Situation: One candidate clearly wins on a higher-priority dimension such as layout, position, size, spacing, first-screen content, module order, core content, or element completeness, but the other candidate has nicer colors, image mood, or small visual polish.

Judgement: Do not mark Same just because each side has some advantages. Apply the priority stack first and choose the side that wins the higher-priority dimension.

Reason pattern: 布局和核心内容更贴近题目，另一个只是局部视觉细节更好

## Broken Image In Key Content

Situation: A candidate has broken images in key visible content such as hero, product, card, doctor, avatar, chart, gallery, or required comparison content.

Judgement: Treat this as a significant element-completeness or visual-restoration defect. If the page is broadly unrenderable or cannot be inspected, prefer waste or abandon when supported.

Reason pattern: 关键图片没有正常显示，核心内容不完整

## Latest Correction Overfit Trap

Situation: A recent user correction mentions one rule, so the judgement focuses only on that rule and forgets other applicable manual, priority, layout, content, completeness, or style requirements.

Judgement: Use the correction as a guardrail inside the full rubric. Before deciding, scan every applicable rule family and then apply priority.

Reason pattern: 按完整规则看，不只看刚提到的一个点

## Reason Copying Trap

Situation: A previous reason sounds close but does not match the current visible evidence.

Judgement: Reword from current evidence. Use examples as phrase pools only.
"""


def _legacy_default_reason_examples() -> str:
    return """# Reason Examples

Add short natural Chinese examples here after real tasks are reviewed.

- 通过：核心功能可以正常操作，反馈也比较明确
- 不通过：按钮点击后没有变化，关键功能不可用
- 废弃：页面白屏，无法判断核心内容
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

- Active wording constraints in this file are hard checks before filling a reason.
- Default comparison reasons should be compact and colloquial, using Chinese commas for clause breaks and no other punctuation unless the queue explicitly requires another format.
- Prefer the user's direct annotation voice over formal audit language.
- Keep reasons compact unless the queue explicitly asks for detailed comparison.
- Use current-task evidence from the manual and screenshots; use historical answers for style only unless the user says the rule also transfers.
"""
    return """# User Style

Use this file as the first source for reason wording when the user provides historical annotation answers.

## How To Learn From User Answers

- Treat active wording constraints in this file as hard checks before filling a reason.
- Default comparison reasons should be compact and colloquial.
- Use Chinese commas for clause breaks. Avoid slashes, colons, semicolons, pause marks, parentheses, and final full stops in submitted reasons unless the queue explicitly requires them.
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


def default_current_item_state() -> str:
    return """# Current Item

Use this file as the recoverable working memory for exactly one active annotation item. Replace stale content before starting the next item.

## Item Identity

- Task ID:
- Queue:
- Item type: normal | pairwise | permission-quiz | returned-rework | inaccessible | broken-preview | other
- Current page URL:

## Prompt Summary

Write the current prompt in compact form. Keep only facts needed for judgement.

## Applicable Rule Sources

- `references/priority-rules.md`:
- `references/rule-updates.md`:
- `references/training-summary.md`:
- `references/manual-summary.md`:
- `references/learned-patterns.md`:
- `references/user-style.md`:

## Current-Item Checklist

Write 3-8 concrete checks before judging.

- [ ] 
- [ ] 
- [ ] 

## Browser Observation Summary

Summarize `state/browser-observation.json` in a few lines. Do not paste long DOM, accessibility tree, or screenshot descriptions here.

## Checklist-Based Judgement

Reference each checklist item and state the visible evidence.

## Draft Result

- Draft label:
- Draft waste/abandon flag:
- Draft reason:
- Needs user confirmation: yes | no

## Pre-Submit Audit Notes

- Audit completed: no
- Blocking uncertainty:
- Completion handling: clear-or-overwrite-for-next-item; do-not-log-completed-answer
"""


def default_corrections_log() -> str:
    return """# Corrections

Record user corrections here before merging reusable items into references with:

```powershell
python scripts/update_task_skill.py --skill-dir <skill-dir> --from-correction-log
```

## Format

Use one entry per correction. Set `Type` to one of:

- `rule`: reusable judgement correction, merged into `references/learned-patterns.md`
- `override`: active rule override, merged into `references/rule-updates.md`
- `style`: reason wording or punctuation preference, merged into `references/user-style.md`
- `reason`: reusable phrase example, merged into `references/reason-examples.md`
- `checklist`: recurring checklist item, merged into `references/decision-checklist.md`
- `audit`: recurring pre-submit check, merged into `references/pre-submit-audit.md`
- `failure`: recurring trap, merged into `references/common-failure-patterns.md`
- `manual`: official manual clarification, merged into `references/manual-summary.md`
- `priority`: priority or conflict handling change, merged into `references/priority-rules.md`
- `one-off`: item-specific correction only; do not merge into long-term references and do not create a completed-answer log unless the user explicitly asks for logging

## Pending Corrections

<!--
### YYYY-MM-DD HH:MM - <short title>

Type: rule
Source: user correction
Text:
The reusable correction goes here.
-->
"""


def default_pending_uncertainties() -> str:
    return """# Pending Uncertainties

Pause instead of guessing when an uncertainty affects the label, reason, waste flag, quiz answer, or final submission.

## Open

<!--
### YYYY-MM-DD HH:MM - <task_id>

- Blocker:
- Why it affects judgement:
- Needed user/platform action:
- Status: open | resolved
-->
"""


def default_browser_observation() -> str:
    return """{
  "task_id": "",
  "prompt": "",
  "page_load_state": "",
  "tested_controls": [],
  "visible_evidence": [],
  "failures": [],
  "screenshots": [],
  "uncertain_points": [],
  "recommended_pause": false
}
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
    write(skill_dir / "references" / "priority-rules.md", default_priority_rules())
    write(skill_dir / "references" / "decision-checklist.md", default_decision_checklist())
    write(skill_dir / "references" / "pre-submit-audit.md", default_pre_submit_audit())
    write(skill_dir / "references" / "common-failure-patterns.md", default_common_failure_patterns())
    write(skill_dir / "state" / "current-item.md", default_current_item_state())
    write(skill_dir / "state" / "corrections.md", default_corrections_log())
    write(skill_dir / "state" / "pending-uncertainties.md", default_pending_uncertainties())
    write(skill_dir / "state" / "browser-observation.json", default_browser_observation())

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
