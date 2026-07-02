# Decision Checklist

For every item, build a short current-item checklist before judging. Do not try to hold the whole rubric in memory.

## Step 1: Classify The Item

- [ ] Is this a normal annotation item?
- [ ] Is it returned/rework, permission quiz, inaccessible, or outside the requested queue?
- [ ] Is there a login, CAPTCHA, permission, risk, or account challenge that requires pausing?

## Step 2: Extract Current Core Requirements

Before judging, write a `current-item-checklist` with 3-8 concrete checks for this exact prompt. The checklist is mandatory evidence, not optional notes. Each final judgement must reference these checks one by one.

- [ ] GT chart type, special variant, and high-level intent:
- [ ] O1 machine rubrics accuracy and missing chart-type/intent points:
- [ ] O2 core data checks: values, trends, positions, axes, ranges, ticks, labels, legends, units:
- [ ] O3 layout/style checks: crop, overlap, spacing, colors, font, line/marker style, background:
- [ ] Any machine rubric that must be repaired or supplemented before scoring:
- [ ] Pairwise comparison basis: overall, then O2/O1 critical errors, then O3:
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
- [ ] GT chart, image1, and image2 are all visible enough to compare.
- [ ] Enlarged view has been used if small ticks, legends, labels, or data points are unreadable in thumbnail view.
- [ ] GT, image1, and image2 have been inspected as separate/enlarged images before any `1` score or pairwise choice.
- [ ] The platform currently exposes no ordinary waste/abandon option; if a chart is unreadable, pause or follow visible platform-specific fallback rather than inventing a hidden waste label.
- [ ] The page can be judged from visible behavior, not hidden DOM evidence.

If a hard gate fails and the platform exposes a waste/abandon option, follow that visible option. If not, pause and report the blocker.

## Step 4: Chart Checks

- [ ] O1 checked independently for chart type, special variant, and intent only.
- [ ] O2 checked independently for data mapping and semantic elements.
- [ ] O3 checked independently for layout and visual style.
- [ ] Machine rubrics are not trusted until verified against GT.
- [ ] Pointwise rubric scores are assigned independently for image1 and image2.
- [ ] Pointwise rubric scores use strict thresholds: `1` only for complete GT match, `0.5` for basic match with visible differences, `0` for severe mismatch or missing/wrong element.
- [ ] Dimension scores are chosen from the correct scales: O1 `0/2/4`, O2/O3 `0/1/2/3/4`.
- [ ] O1=0 overall rule was applied if needed, but later fields were still completed.

## Step 5: Decide

- [ ] Label follows the highest-priority applicable rule.
- [ ] I cited the current-item checklist point by point when forming the judgement.
- [ ] I considered all applicable dimensions from the priority stack, not only the most recent correction or the most obvious visual detail.
- [ ] New user corrections were used as guardrails inside the full rubric, not as replacements for other rules.
- [ ] For pairwise tasks, I first checked whether higher-priority dimensions have a clear winner.
- [ ] I did not choose a prettier chart over a more data-faithful chart when O1/O2 clearly differ.
- [ ] I did not treat O3 style polish as more important than chart type or data correctness.
- [ ] Reason names the main working or broken core point.
- [ ] Reason style follows active constraints in `user-style.md`, including comma-only punctuation and colloquial wording when requested, and uses `reason-examples.md` only as a phrase pool.
