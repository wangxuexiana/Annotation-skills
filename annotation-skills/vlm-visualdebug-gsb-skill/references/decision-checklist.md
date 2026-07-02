# Decision Checklist

For every item, build a short current-item checklist before judging. Do not try to hold the whole rubric in memory.

## Step 1: Classify The Item

- [ ] Is this a normal annotation item?
- [ ] Is it returned/rework, permission quiz, inaccessible, or outside the requested queue?
- [ ] Is there a login, CAPTCHA, permission, risk, or account challenge that requires pausing?

## Step 2: Extract Current Core Requirements

Write 3-8 checks for this exact prompt:

- [ ] Core output or scene requested:
- [ ] Prompt-named controls or interactions:
- [ ] Required data, text, visual state, or comparison target:
- [ ] Must-not-have failure modes from this queue:
- [ ] Pairwise comparison basis, if applicable:
- [ ] Full applicable rule set for this item, not only the newest correction:

For VisualDebug GSB, include these task-specific checks:

- [ ] Task type is explicit visual repair, open visual repair, or function/interaction repair.
- [ ] Target problem or main visual difference has been identified from prompt, reference image, and before-fix page.
- [ ] A and B are both checked against the target repair first.
- [ ] If both solve or both miss the target similarly, compare restoration to reference image or prompt requirement completion.
- [ ] Side effects are checked last, including white screen, broken opening, content missing, layout shift, obstruction, and failed interaction.
- [ ] Final label is exactly one of `A good B`, `A bad B`, or `A same B`.

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
- [ ] I considered all applicable dimensions from the priority stack, not only the most recent correction or the most obvious visual detail.
- [ ] New user corrections were used as guardrails inside the full rubric, not as replacements for other rules.
- [ ] For pairwise tasks, I first checked whether higher-priority dimensions have a clear winner.
- [ ] I did not flatten to Same because of lower-priority color, image mood, or small visual details when layout, position, size, spacing, first-screen content, module order, or core content clearly differs.
- [ ] Reason names the main working or broken core point.
- [ ] Reason style follows active constraints in `user-style.md`, including comma-only punctuation and colloquial wording when requested, and uses `reason-examples.md` only as a phrase pool.

VisualDebug GSB decision order:

- [ ] I did not let minor polish beat target problem repair.
- [ ] I did not ignore restoration/completion when both sides fixed the target problem.
- [ ] I did not ignore serious side effects introduced by a repair.
- [ ] I used Same only when both sides are close, equally good, or equally bad.
