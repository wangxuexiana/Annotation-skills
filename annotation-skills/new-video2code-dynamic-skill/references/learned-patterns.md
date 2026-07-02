# Learned Patterns

Add reusable user corrections here.

Format:

- Pattern: <task or situation>
  Pass/choose condition: <what is enough>
  Fail/waste condition: <what is not enough>
  Reason style: <preferred wording>

- Pattern: Overall dynamic score 1
  Pass/choose condition: all dynamic effects and interactions have been checked and correspond to the video and original/GT HTML
  Fail/waste condition: any visible dynamic effect or interaction is missing, mismatched, or not confidently verified, even if core rubrics are mostly implemented
  Reason style: name the missing, mismatched, or unverified interaction directly

- Pattern: Overall note formatting
  Pass/choose condition: note contains restoration reason on the first line and dynamic reason on the immediately following second line
  Fail/waste condition: note contains a blank line between restoration and dynamic reasons that may hide later content during QA
  Reason style: use two adjacent lines: `还原度：...` then `整体动效：...`
