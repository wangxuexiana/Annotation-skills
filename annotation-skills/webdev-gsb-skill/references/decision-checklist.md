# Decision Checklist

For every item, build a short current-item checklist before judging. Do not try to hold the whole rubric in memory.

## Step 1: Classify The Item

- [ ] Is this a normal annotation item?
- [ ] Is it returned/rework, permission quiz, inaccessible, or outside the requested queue?
- [ ] Is there a login, CAPTCHA, permission, risk, or account challenge that requires pausing?

## Step 2: Extract Current Core Requirements

Before judging, write a `current-item-checklist` with 3-8 concrete checks for this exact prompt. The checklist is mandatory evidence, not optional notes. Each final judgement must reference these checks one by one.

- [ ] Core output or scene requested:
- [ ] Scene type and priority: Game means functional defects outrank aesthetics; UI means aesthetics outranks smaller functional defects.
- [ ] Prompt-named controls or interactions:
- [ ] Required data, text, visual state, or comparison target:
- [ ] Functional-completeness checks from prompt-explicit requirements:
- [ ] Functional-defect checks from implemented visible controls and broken images:
- [ ] Aesthetic checks for layout, style, and overall UI impression:
- [ ] Must-not-have failure modes from this queue:
- [ ] Pairwise or three-model comparison basis:
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

If a hard gate fails, do not stop at a waste label for this queue. Record the waste or abandoned reason in the remark and still compare the candidates.

Broken images in key visible content are functional defects for this queue. Whole-page blank, unrenderable, or uninspectable states count as waste-like reasons in the remark and still participate in GSB.

## Step 4: Functional Checks

- [ ] Test each prompt-named control or natural visible control needed for judgement.
- [ ] Verify that clicks, inputs, sliders, toggles, generators, drawing tools, counters, or camera controls visibly or textually change something.
- [ ] Treat prompt-required functions that are missing or unimplemented as functional-completeness defects.
- [ ] Treat implemented visible controls that fail, even if not prompt-required, as functional defects.
- [ ] Treat failed image loading as a functional defect.
- [ ] Judge core behavior before visual polish.
- [ ] For pairwise or three-model tasks, compare all candidates against the prompt and queue priority before choosing.

## Step 5: Decide

- [ ] Label follows the highest-priority applicable rule.
- [ ] I cited the current-item checklist point by point when forming the judgement.
- [ ] I considered all applicable dimensions from the priority stack, not only the most recent correction or the most obvious visual detail.
- [ ] New user corrections were used as guardrails inside the full rubric, not as replacements for other rules.
- [ ] For pairwise tasks, I first checked whether higher-priority dimensions have a clear winner.
- [ ] For Game scenes, I did not let visual polish outweigh a meaningful functional defect.
- [ ] For UI scenes, I did not let a smaller implemented-control defect outweigh a clearly better overall UI when core needs are met.
- [ ] I did not flatten to Same because of lower-priority color, image mood, or small visual details when prompt implementation, serious defects, layout, style, or core content clearly differs.
- [ ] I did not apply a waste tag; if a candidate is waste-like, I described the reason and still compared it.
- [ ] Reason names the main working or broken core point.
- [ ] Reason style follows active constraints in `user-style.md`, including comma-only punctuation and colloquial wording when requested, and uses `reason-examples.md` only as a phrase pool.
