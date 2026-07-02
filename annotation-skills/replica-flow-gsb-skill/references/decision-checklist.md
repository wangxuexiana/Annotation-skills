# Decision Checklist

For every item, build a short current-item checklist before judging. Do not try to hold the whole rubric in memory.

## Step 1: Classify The Item

- [ ] Is this a normal annotation item?
- [ ] Is it returned or rework, permission quiz, inaccessible, or outside the requested queue?
- [ ] Is there a login, CAPTCHA, permission, risk, or account challenge that requires pausing?

## Step 2: Extract Current Core Requirements

Write 3-8 checks for this exact prompt:

- [ ] Core output or scene requested:
- [ ] Prompt-named controls or interactions:
- [ ] Required data, text, visual state, or comparison target:
- [ ] Must-not-have failure modes from this queue:
- [ ] Pairwise comparison basis, if applicable:
- [ ] Full applicable rule set for this item, not only the newest correction:

For this queue, also classify the reference type:

- [ ] Sketch-to-webpage: prioritize layout, content filling, productization, prompt style, then explicit functions.
- [ ] Webpage-replica: prioritize reference fidelity, element completeness, content accuracy, visual details, hallucination control, then explicit functions.
- [ ] Flowchart-to-webpage: prioritize flow semantics, web productization, interaction/state chain, information architecture, then visual completion.

## Step 3: Hard Gates First

- [ ] Page or preview loads and is inspectable.
- [ ] It is not blank, white-screen, black-screen, broken, or unrenderable.
- [ ] The core requested feature exists visibly.
- [ ] The page can be judged from visible behavior, not hidden DOM evidence.

If a hard gate fails and the platform supports waste or abandon, prefer waste or abandon over normal fail.

## Step 4: Functional Checks

- [ ] Test each prompt-named control or natural visible control needed for judgement.
- [ ] Verify that clicks, inputs, sliders, toggles, generators, drawing tools, counters, or camera controls visibly or textually change something.
- [ ] Judge core behavior before visual polish.
- [ ] For pairwise tasks, compare both candidates against the prompt and rubric before choosing.

Function boundary:

- [ ] If the prompt does not explicitly request behavior, do not require hidden real functionality.
- [ ] If the prompt explicitly requests behavior, test both candidates on the same key operation chain.
- [ ] For flowchart tasks, test the state progression that represents the core flow, including mock success or failure feedback when relevant.

## Step 5: Decide

- [ ] Label follows the highest-priority applicable rule.
- [ ] I considered all applicable dimensions from the queue priority stack, not only the most recent user correction.
- [ ] New user corrections are guardrails inside the full rubric, not replacements for the full rubric.
- [ ] For pairwise tasks, first decide whether any higher-priority dimension has a clear winner.
- [ ] If layout, position, size, spacing, first-screen content, module order, or core content has a clear winner, do not downgrade to Same just because the other side has better color, image mood, or small visual details.
- [ ] Check both candidates for broken images before final label.
- [ ] If one side has a broken image in a key visible area, treat it as a significant element-completeness and visual-restoration defect.
- [ ] Reason names the main working or broken core point.
- [ ] Reason style follows `user-style.md` and `reason-examples.md`, but does not copy them mechanically.
- [ ] If `user-style.md` says comparison reasons should only use commas, rewrite the reason until it contains no other punctuation.
- [ ] Reason sounds口语化 and compact, not like a formal report.
