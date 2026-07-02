# Quiz Draft

No concrete permission quiz questions were provided with the manual link.

Use these evidence-backed answers if related questions appear:

| Likely Question | Draft Answer | Evidence | Confidence |
|-|-|-|-|
| WebDev GSB mainly focuses on which dimensions? | Functional completeness, functional defects, and aesthetics. | Manual lists `功能完整度`, `功能缺陷`, `美观度`. | High |
| For Game scenes, which dimension has higher priority, functional defects or aesthetics? | Functional defects have higher priority than aesthetics. | Manual says Game scenes mainly check functional completeness plus functional defects, and `功能缺陷` outranks `美观度`. | High |
| For UI scenes, which dimension has higher priority, aesthetics or functional defects? | Aesthetics has higher priority than functional defects, while still considering functional completeness. | Manual says UI scenes mainly check functional completeness plus aesthetics, and `美观度` outranks `功能缺陷`. | High |
| Should generic features not mentioned by the prompt be required for functional completeness? | No. Use prompt-explicit function points as the core basis; generic features not mentioned are not included by default. | Manual's functional-completeness row. | High |
| If a model implements a clickable control not explicitly required by the prompt, and clicking it has no response, what dimension is affected? | Functional defect. | Manual's functional-defect example. | High |
| Are failed images a functional defect? | Yes. | Manual explicitly says image loading failure belongs to `功能缺陷`. | High |
| Should waste data receive a waste tag in this task? | No. Do not apply a waste tag; describe A/B waste reason in remarks. | Manual callout on waste handling. | High |
| If A is waste and B is normal, what is the GSB judgement? | `A < B`. | Manual waste pair rule. | High |
| If both A and B are waste, what is the GSB judgement? | `A = B`. | Manual waste pair rule. | High |
