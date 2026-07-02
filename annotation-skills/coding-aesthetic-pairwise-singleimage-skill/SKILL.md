---
name: coding-aesthetic-pairwise-singleimage-skill
description: Coding美观度 pairwise SingleImage annotation rubric for screenshot-only webpage aesthetic comparison. Use when Codex needs to learn, review, draft, or assist human-confirmed labels for this queue by comparing two single screenshots, choosing page purpose, applying waste rules, and producing -1/0/1 aesthetic judgements. Do not use for functional interaction testing or full implementation completeness scoring.
---

# Coding Aesthetic Pairwise SingleImage Skill

## Goal

Support the Coding美观度 pairwise SingleImage queue from the official Feishu manual. This queue compares two model screenshots for webpage aesthetics only.

Hard boundary: judge only screenshot-visible aesthetics. Do not test interactions, hidden code, prompt feature completeness, or runtime behavior unless the screenshot itself visibly proves the issue. The manual also says AI must not be used to polish dimension comments or assist scoring, so keep a human-confirmation gate before any final answer or submission.

## Required References

Load only what is needed:

- `references/priority-rules.md`: rule priority and conflict handling.
- `references/decision-checklist.md`: per-item checklist for screenshot comparison.
- `references/pre-submit-audit.md`: final audit before filling labels, waste flags, reasons, or quiz answers.
- `references/manual-summary.md`: official manual rules.
- `references/training-summary.md`: distilled workflow and examples.
- `references/common-failure-patterns.md`: recurring traps.
- `references/rule-updates.md`: latest overrides. Read before older summaries.
- `references/learned-patterns.md`: reusable user corrections.
- `references/reason-examples.md`: wording examples.
- `references/user-style.md`: active wording and punctuation constraints.
- `references/quiz-draft.md`: likely quiz facts and evidence.

## Per-Item Flow

For every item:

1. Read `priority-rules.md`, `rule-updates.md`, and the current visible platform instruction.
2. Read the prompt and inspect the two screenshots. Use zoom if needed, but do not open candidate pages to test functions.
3. Update `state/current-item.md` with task ID, prompt summary, page purpose candidates, applicable rules, and a 3-8 point checklist.
4. Check waste first: cannot judge from screenshot, bad capture, too little information, white screen, black screen, garbled text, error page, or severe rendering failure.
5. If judgeable, infer page purpose, such as SaaS landing page, dashboard, blog, ecommerce, portfolio, game, education, or product page.
6. Compare by the manual's priority stack: fatal visible defects, scenario fit, ambitious high-quality execution, then the four dimensions.
7. Decide `-1`, `0`, or `1`. Judge objectively from visible quality gaps. Use `0` when both sides are genuinely close, have similar problem severity, or no obvious stable preference can be supported.
8. Draft a compact Chinese reason grounded in visible evidence.
9. Run `pre-submit-audit.md`.
10. Pause before final submission, quiz submission, or any action that would violate platform policy or user confirmation rules.

## Aesthetic Rubric

Apply the three top principles first:

- Fatal visible defects beat minor flaws: unreadable core text, unrecognizable core buttons, broken key images, blocked core materials, large placeholders, or failed rendering matter heavily.
- Scenario fit beats personal taste: judge whether the page fits its purpose and audience.
- Ambitious polished execution beats empty safety: rich, coherent, high-quality pages can beat sparse pages that are merely not wrong.

Then compare four dimensions:

- Layout and information hierarchy: guidance, hierarchy, spacing, alignment, centering, symmetry.
- Color and typography: scenario fit, contrast, core text readability, harmony, saturation quality.
- Image, icon, and material quality: rendering integrity, theme fit, image clarity, professional visual materials.
- Consistency and detail polish: unified design language, consistent same-type components, coherent details.

## Labels

- `-1`: model 1 is more aesthetically pleasing.
- `0`: both are basically equal, or no obvious stable preference can be supported from visible aesthetic evidence. Prefer this when the visible quality gap is not clear enough to objectively choose a winner.
- `1`: model 2 is more aesthetically pleasing.
- Waste/abandoned: the screenshot cannot support aesthetic judgement or has severe capture/rendering problems.

## State And Recovery

Use the `state/` files for recoverable work:

- `state/current-item.md`: current prompt, page purpose, checklist, draft label, draft reason, and audit notes.
- `state/browser-observation.json`: screenshot observation summary only, not long DOM or interaction traces.
- `state/batch-log.md`: compact per-item outcomes and submission status.
- `state/corrections.md`: user corrections waiting to be merged.
- `state/pending-uncertainties.md`: blockers requiring user or platform action.

## Stable Rules

Shared generic rules live at `../annotation-workflow-skill/references/stable-annotation-rules.md`, but this queue overrides generic function-testing rules. Screenshot-only aesthetic rules from this skill win when they conflict with shared rules.

## Skill Evolution

When the user corrects a judgement or reason style, update `learned-patterns.md`, `rule-updates.md`, `reason-examples.md`, or `user-style.md` as appropriate. Keep reusable rules compact and avoid one-off details in long-term references.
