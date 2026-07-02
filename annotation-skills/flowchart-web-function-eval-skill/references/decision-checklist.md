# Decision Checklist

For every item, build a short current-item checklist before judging. Do not try to hold the whole rubric in memory.

## Step 1: Classify The Item

- [ ] Is this a normal annotation item?
- [ ] Is it returned/rework, permission quiz, inaccessible, or outside the requested queue?
- [ ] Is there a login, CAPTCHA, permission, risk, or account challenge that requires pausing?

## Step 2: Extract Current Core Requirements

Before judging, write a `current-item-checklist` with 3-8 concrete checks for this exact prompt. The checklist is mandatory evidence, not optional notes. Each final judgement must reference these checks one by one.

- [ ] Prompt-requested webpage and core flow:
- [ ] Reference flowchart entries, branches, routing, and completion states:
- [ ] Every rubric and its type, including `flow_coverage`, `function`, `flow_routing`, `flow_decision`, or `flow_completion` when present:
- [ ] Rubrics requiring actual interaction, clicking, input, validation, routing, modal display, filtering, submission, or completion:
- [ ] Overall score evidence from prompt, flowchart, and actual interaction:
- [ ] Screenshot correctness comparison target, meaning the initial loaded `modelA` page before any interaction:
- [ ] Waste/abandon blockers, if any:

## Step 2.5: External State

- [ ] `state/current-item.md` contains the current item type, prompt summary, applicable rule sources, current-item checklist, draft label, draft reason, and pre-submit audit notes.
- [ ] `state/browser-observation.json` contains only structured observations using these keys: `task_id`, `prompt`, `page_load_state`, `tested_controls`, `visible_evidence`, `failures`, `screenshots`, `uncertain_points`, and `recommended_pause`.
- [ ] Long DOM dumps, long accessibility snapshots, repeated screenshot descriptions, and unrelated browser history are not kept in chat.
- [ ] If an uncertainty remains, add it to `state/pending-uncertainties.md` and pause instead of guessing.
- [ ] If the user corrects a reusable rule or style, add it to `state/corrections.md` before merging it into references.

## Step 3: Hard Gates First

- [ ] Reference flowchart loads and is usable for understanding the target flow.
- [ ] `modelA` opens and is inspectable enough to evaluate.
- [ ] Required item fields are present and not obviously mismatched: prompt, reference flowchart, `modelA`, `modelA_img`, and rubrics.
- [ ] The page can be judged from visible behavior, not hidden DOM evidence.
- [ ] If `modelA` is white-screen, crashed, inaccessible, or unrelated enough that no meaningful evaluation is possible, use waste/abandon when supported.

Waste/abandon is narrow in this queue. Do not abandon merely because the page is ugly, incomplete, has failed rubrics, has an incorrect screenshot, or has several missing functions. If the item can be evaluated, judge normally.

## Step 4: Functional Checks

- [ ] Rubrics are independent: judge each rubric only against its own wording and evidence.
- [ ] Test each rubric independently against its own wording.
- [ ] For interaction rubrics, actually click, input, submit, filter, route, open, close, or trigger the described behavior.
- [ ] Do not add unstated requirements to a rubric. If it only asks whether validation exists, any relevant validation feedback can satisfy it unless the rubric specifies the exact standard.
- [ ] Record visible evidence for every rubric label in `state/browser-observation.json`.
- [ ] Judge core behavior and flow completion before visual polish.
- [ ] Compare `modelA_img` with the initial loaded page before any interaction. Do not confuse screenshot correctness with functional quality.

## Step 5: Decide

- [ ] Every rubric has an independent `1/0` label and a concrete reason when required.
- [ ] Overall score is an integer from `0` to `10`, based on prompt, flowchart, and actual interaction rather than a simple average.
- [ ] Overall score is broadly consistent with rubric results; `8+` normally requires no completely unmet rubric and at most one partial/minor rubric defect.
- [ ] Screenshot correctness is `1` only if `modelA_img` matches the initial loaded page state, and `0` if it shows cropped content, missing loaded elements, post-interaction state, selected filters, expanded cards, menus, modals, or other mismatch.
- [ ] Label follows the highest-priority applicable rule.
- [ ] I cited the current-item checklist point by point when forming the judgement.
- [ ] I considered all applicable dimensions from the priority stack, not only the most recent correction or the most obvious visual detail.
- [ ] New user corrections were used as guardrails inside the full rubric, not as replacements for other rules.
- [ ] For pairwise tasks, I first checked whether higher-priority dimensions have a clear winner.
- [ ] I did not flatten to Same because of lower-priority color, image mood, or small visual details when layout, position, size, spacing, first-screen content, module order, or core content clearly differs.
- [ ] Reason names the main working or broken core point.
- [ ] Reason style follows active constraints in `user-style.md`, including comma-only punctuation and colloquial wording when requested, and uses `reason-examples.md` only as a phrase pool.
