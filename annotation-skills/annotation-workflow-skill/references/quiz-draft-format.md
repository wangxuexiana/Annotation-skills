# Permission Quiz Draft Format

Use this format before submitting a queue-permission questionnaire.

```text
问卷：<queue or questionnaire name>
资料：<video/manual links or filenames>
结论：建议提交前人工确认

1. 题目：<question text>
   推荐答案：<answer>
   依据：<training-summary/manual section>
   置信度：高/中/低

2. 题目：<question text>
   推荐答案：<answer>
   依据：<training-summary/manual section>
   置信度：高/中/低
```

Confidence guidance:

- `高`: directly stated by the manual, video transcript, or quiz training example.
- `中`: strongly implied by multiple training examples but not stated as a sentence.
- `低`: likely but not well supported; ask the user before submitting.

Do not invent unsupported answers. If the answer is not in the materials, write `资料中未找到明确依据`.
