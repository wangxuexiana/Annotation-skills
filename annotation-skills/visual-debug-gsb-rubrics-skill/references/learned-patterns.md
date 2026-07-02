# Learned Patterns

Add reusable user corrections here.

## Starter Guardrails

- Pattern: Full rubric coverage
  Pass/choose condition: The judgement considered the current problem, original request/reference, all rubrics, A/B scores, side effects, waste rules, and reason requirements.
  Fail/waste condition: The judgement focused only on one visible detail or the latest correction while ignoring official queue outputs.
  Reason style: Keep the reason grounded in the main deciding evidence.

- Pattern: Current problem first
  Pass/choose condition: Target repair is judged before reference similarity or aesthetic polish.
  Fail/waste condition: A prettier page is chosen even though it does not fix the current reported problem.
  Reason style: Name the repaired or still-broken target area first.

- Pattern: Unable-to-judge restraint
  Pass/choose condition: `无法判断` is used only for inaccessible or contradictory evidence.
  Fail/waste condition: A confirmed candidate failure is marked `无法判断`.
  Reason style: When used, name what cannot be verified and why.

Format:

- Pattern: <task or situation>
  Pass/choose condition: <what is enough>
  Fail/waste condition: <what is not enough>
  Reason style: <preferred wording>

