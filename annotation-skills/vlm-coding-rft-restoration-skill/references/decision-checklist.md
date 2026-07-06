# Decision Checklist

For every item, build a short current-item checklist before judging. Do not try to hold the whole rubric in memory.

## Step 1: Classify The Item

- [ ] Is this a normal annotation item?
- [ ] Is it returned/rework, permission quiz, inaccessible, or outside the requested queue?
- [ ] Is there a login, CAPTCHA, permission, risk, or account challenge that requires pausing?

## Step 2: Extract Current Core Requirements

Before judging, write a `current-item-checklist` with 3-8 concrete checks for this exact prompt. The checklist is mandatory evidence, not optional notes. Each final judgement must reference these checks one by one.

- [ ] Core output or scene requested:
- [ ] Whether UP instruction changes the expected layout, style, interaction, or target state:
- [ ] Reference-image baseline and first-screen structure:
- [ ] Prompt-named controls or interactions:
- [ ] Required data, text, visual state, or comparison target:
- [ ] Must-not-have failure modes from this queue:
- [ ] Candidate list and which products qualify for 1-point comparison:
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
- [ ] It is not severely misaligned and does not miss the core visible content.
- [ ] Prompt and reference image correspond, or if they do not correspond, the product follows the prompt and should be treated as the manual's discard case.
- [ ] Key visible images are not broken, especially hero, card, product, avatar, doctor, chart, gallery, and other required content images.
- [ ] The core requested feature exists visibly.
- [ ] The page can be judged from visible behavior, not hidden DOM evidence.

If a hard gate fails, apply this queue's visible option: discard only for the manual's prompt/reference mismatch case; otherwise use 0 for white-screen, severe misalignment, core content missing, or mostly unrestored products.

Broken images in key visible content are significant element-completeness or visual-restoration defects. Whole-page blank, unrenderable, or uninspectable states remain waste/abandon when supported.

## Step 4: Functional Checks

- [ ] Test each UP-required or prompt-named control needed for judgement.
- [ ] Verify that required clicks, switches, layout adjustments, style adjustments, or visible controls produce the expected visible/textual change.
- [ ] Do not require real interaction for hover, popup, selected, or expanded reference states unless UP asks for it.
- [ ] Confirm extra interaction does not break layout, color, content, or state restoration.
- [ ] Judge required function coverage together with visual restoration; do not score from visual polish alone.

## Step 5: Decide

- [ ] Label follows the highest-priority applicable rule.
- [ ] Each product is first considered for 0 or 1, and only an already qualified best 1-point product is promoted to 2.
- [ ] Exactly one product is promoted to 2 when the platform expects a best product and multiple products reach 1.
- [ ] Any 0-point product has a screenshot plan or uploaded issue screenshot when the platform requires it.
- [ ] I cited the current-item checklist point by point when forming the judgement.
- [ ] I considered layout/spatial relation, element completeness, content accuracy, visual restoration, hallucination control, and UP-required functions.
- [ ] New user corrections were used as guardrails inside the full rubric, not as replacements for other rules.
- [ ] Reason names the main visible mismatch, missing function, or small remaining flaw.
- [ ] Reason style follows active constraints in `user-style.md`, including comma-only punctuation and colloquial wording when requested, and uses `reason-examples.md` only as a phrase pool.
