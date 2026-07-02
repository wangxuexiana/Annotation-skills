# Rule Updates

Newer entries override older summaries when they clearly conflict. Add updates with `update_task_skill.py` or append manually.

## Active Overrides

- Current queue has no ordinary waste/abandon path. Training says all current annotation items must be completed unless the platform later exposes a waste option or the user gives a different workflow.
- If O1 is `0`, overall is `0`, but all remaining rubrics, O2/O3 dimension scores, reasons, pairwise choice, and pairwise reason still must be completed.
- Rubrics must be checked before scoring. Inaccurate, vague, wrong-dimension, or incomplete machine rubrics must be repaired or supplemented first.
- Pointwise scores must be strict: `1` means the rubric is completely matched against GT, not merely close; `0.5` means basically/partially matched with visible differences; `0` means severe mismatch, missing element, wrong element, or unusable execution for that rubric.
- Before pairwise judgement or any high score, inspect GT, image1, and image2 as separate enlarged images, then compare the corresponding regions and named rubric elements. Do not score from thumbnails or a rough overall impression.
- Do not penalize O1 for data trend, label overlap, crop, color, font, or layout defects unless the O1 rubric explicitly makes that feature part of the chart intent.
- For this queue, dimension reasons need more detail than per-rubric reasons because six dimension scores from double-blind annotation determine whether the item enters QC.

## Update Log
