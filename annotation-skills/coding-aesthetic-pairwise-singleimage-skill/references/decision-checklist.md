# Decision Checklist

Build a 3-8 point current-item checklist before judging. This queue is screenshot-only.

## Step 1: Classify

- [ ] This is the Coding美观度 pairwise SingleImage queue.
- [ ] The item is normal, not returned/rework unless the user explicitly asked to handle returned data.
- [ ] There is no login, CAPTCHA, permission, account, or platform warning that requires pausing.
- [ ] The task page does not require an action that would bypass the manual's AI-use warning.

## Step 2: Waste First

Mark waste/abandoned if any condition prevents screenshot-based aesthetic judgement:

- [ ] Screenshot is white screen, black screen, garbled, erroring, broken, or severely unrendered.
- [ ] Screenshot was captured badly, severely cropped, or contains too little information.
- [ ] Screenshot only shows an unjudgeable first frame or a state where aesthetics cannot be inferred.
- [ ] Key visible content is so missing or obstructed that comparison would be speculation.

If waste applies, stop normal pairwise scoring and draft a short waste reason.

## Step 3: Infer Page Purpose

- [ ] Identify likely page type: SaaS landing page, data dashboard, blog/article, ecommerce product page, portfolio, game, education app, tool UI, or other.
- [ ] Note the likely audience and use context.
- [ ] Select the matching platform dropdown option when required.

## Step 4: Build Current-Item Checklist

Write 3-8 concrete checks in `state/current-item.md`, usually covering:

- [ ] Prompt and page purpose fit.
- [ ] Fatal visible defects, including unreadable core text, broken images, blocked core content, or placeholders.
- [ ] Layout and information hierarchy.
- [ ] Color and typography readability.
- [ ] Image, icon, and material quality.
- [ ] Consistency and detail polish.
- [ ] Whether Same is justified by genuinely close evidence.

## Step 5: Compare Screenshots

- [ ] Compare only visible screenshot evidence.
- [ ] Do not test buttons, links, sliders, forms, camera, generators, or other interactions.
- [ ] Do not use hidden DOM, source code, network state, or metadata as evidence.
- [ ] Apply fatal defects before minor polish.
- [ ] Apply scenario fit before personal taste.
- [ ] Give credit for rich, coherent, polished execution over empty safe design.
- [ ] Do not treat "more content" as automatically better.
- [ ] Do not treat "more minimal" as automatically better.
- [ ] Do not treat element count as the basis for scoring unless it creates a concrete visible issue such as clutter, imbalance, or missing support.

## Step 6: Decide Label

- [ ] `-1` if model 1 is clearly more aesthetically pleasing.
- [ ] `0` if both are basically equal or no stable visible preference exists.
- [ ] `1` if model 2 is clearly more aesthetically pleasing.
- [ ] Treat Same as the preferred answer for close cases.
- [ ] Choose A or B only when there is an obvious visible quality gap.
- [ ] Same was not used to ignore a clear higher-priority difference.
- [ ] The reason names the deciding visible defect or advantage, not only a quantity difference.
