# Common Failure Patterns

Use these examples to avoid missing recurring VisualDebug GSB traps.

## Target Repair Ignored

Situation: One side looks more polished, but the other side is the only one that clearly fixes the target issue named in the prompt.

Judgement: Choose the side that fixes the target issue unless its side effects are severe enough to outweigh the repair.

Reason pattern: A 胜出，A 把题目指出的核心问题修好啦，B 虽然局部更顺眼但目标问题还在

## Restoration Over Target Fix

Situation: A side is closer to the reference image in small style details, but it fails the target repair while the other side fixes it.

Judgement: Target repair has priority over small color, font, or polish differences.

Reason pattern: B 胜出，B 先把目标问题修复了，A 只是局部样式接近但核心差异还在

## Side Effect Hidden By Partial Fix

Situation: A side fixes the target issue but introduces serious new layout shift, content missing, visual obstruction, white screen, or interaction failure.

Judgement: Penalize severe side effects. Choose the other side if it has fewer serious regressions, or Same if both are similarly damaged.

Reason pattern: A bad B，A 虽然修了目标问题，但把主体内容挤压变形，B 的副作用更轻

## Same Used Too Easily

Situation: Both sides have pros and cons, but one side clearly wins on target repair, functional completion, or important content restoration.

Judgement: Do not choose Same only because both sides have some defects. Apply target repair, restoration/completion, then side effects.

Reason pattern: A 胜出，两侧都有小问题，但 A 的目标修复和页面还原更完整，差异已经影响核心判断

## Open Repair Misses Major Difference

Situation: The prompt is open-ended, and a side repairs only a tiny local detail while missing the most important visual difference from the reference.

Judgement: The side that discovers and repairs the higher-impact difference should win.

Reason pattern: B 胜出，B 处理了最影响还原度的主要差异，A 只改了局部小问题

## Functional Repair Judged As Visual Only

Situation: The prompt names a function or interaction, but the judgement only compares visual similarity.

Judgement: Test the prompt-named function. A visually nice page loses if the target functional path is still unusable.

Reason pattern: A 胜出，A 的核心交互可以正常走通，B 只是视觉接近但目标功能不可用

## White Screen Or Unusable Page

Situation: One or both candidate pages are white screen, cannot open, or main content is invisible/unusable.

Judgement: Treat it as a severe failure for that side. If both sides fail similarly, choose Same when GSB labels are the only available labels.

Reason pattern: A bad B，A 页面白屏无法判断主体内容，B 至少可以正常展示和对比

## Empty Reason

Situation: The drafted reason says only "更好看", "更完整", or "更符合要求".

Judgement: Rewrite with one or two visible evidence points: target repair, restoration/completion, or side effect.

Reason pattern: B 胜出，B 修复了输入框背景色问题，A 该问题仍明显存在
