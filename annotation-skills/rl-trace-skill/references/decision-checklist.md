# Decision Checklist

For every item, build a short current-item checklist before judging. Do not try to hold the whole rubric in memory.

## Step 1: Classify The Item

- [ ] Is this a normal annotation item?
- [ ] Is it returned/rework, permission quiz, inaccessible, or outside the requested queue?
- [ ] Is there a login, CAPTCHA, permission, risk, or account challenge that requires pausing?
- [ ] RL Trace task type is filled from prompt/reference evidence: 复刻 / 草图 / 无法判断.
- [ ] Explicit function requirement is filled from prompt only: 是 / 否 / 无法判断.

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

- [ ] If the prompt has explicit function requirements, or function rubrics are non-empty, open A and B HTML and test the required interactions.
- [ ] Test each prompt-named control or natural visible control needed for judgement.
- [ ] Verify that clicks, inputs, sliders, toggles, generators, drawing tools, counters, or camera controls visibly or textually change something.
- [ ] Judge core behavior before visual polish.
- [ ] For pairwise tasks, compare both candidates against the prompt and rubric before choosing.
- [ ] If the prompt has no explicit function requirement and function rubrics are empty, do not invent function failures from buttons, inputs, or navigation merely being present.
- [ ] Treat `自然反馈`, `交互反馈`, `状态反馈`, `正常作业`, and `正常运行` as function requirements that require HTML operation.

## Step 5: Decide

- [ ] Label follows the highest-priority applicable rule.
- [ ] I cited the current-item checklist point by point when forming the judgement.
- [ ] I considered all applicable dimensions from the priority stack, not only the most recent correction or the most obvious visual detail.
- [ ] New user corrections were used as guardrails inside the full rubric, not as replacements for other rules.
- [ ] For pairwise tasks, I first checked whether higher-priority dimensions have a clear winner.
- [ ] I did not flatten to Same because of lower-priority color, image mood, or small visual details when layout, position, size, spacing, first-screen content, module order, or core content clearly differs.
- [ ] For RL Trace visual GSB, I compared only visual quality and did not include function behavior.
- [ ] For RL Trace overall GSB, I included explicit function requirements only when the prompt or function rubrics require them.
- [ ] For sketch tasks, I checked whether the candidate productized the sketch instead of preserving wireframe, Lorem ipsum, Placeholder, gray blocks, arrows, or annotations.
- [ ] For replication tasks, I checked layout, element completeness, content accuracy, visual restoration, and hallucinated extra modules against the reference image.
- [ ] Reason names the main working or broken core point.
- [ ] Reason style follows active constraints in `user-style.md`, including comma-only punctuation and colloquial wording when requested, and uses `reason-examples.md` only as a phrase pool.
