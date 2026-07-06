# Corrections

Record user corrections here before merging reusable items into references with:

```powershell
python scripts/update_task_skill.py --skill-dir <skill-dir> --from-correction-log
```

## Format

Use one entry per correction. Set `Type` to one of:

- `rule`: reusable judgement correction, merged into `references/learned-patterns.md`
- `override`: active rule override, merged into `references/rule-updates.md`
- `style`: reason wording or punctuation preference, merged into `references/user-style.md`
- `reason`: reusable phrase example, merged into `references/reason-examples.md`
- `checklist`: recurring checklist item, merged into `references/decision-checklist.md`
- `audit`: recurring pre-submit check, merged into `references/pre-submit-audit.md`
- `failure`: recurring trap, merged into `references/common-failure-patterns.md`
- `manual`: official manual clarification, merged into `references/manual-summary.md`
- `priority`: priority or conflict handling change, merged into `references/priority-rules.md`
- `one-off`: item-specific correction only; do not merge into long-term references and do not create a completed-answer log unless the user explicitly asks for logging

## Pending Corrections

<!--
### YYYY-MM-DD HH:MM - <short title>

Type: rule
Source: user correction
Text:
The reusable correction goes here.
-->
