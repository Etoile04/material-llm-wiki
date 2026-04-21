# Audit Guide — Human Feedback System

## Overview

The audit system lets humans correct the wiki without losing corrections in chat history. Feedback is filed as individual markdown files in `audit/`.

## Filing Feedback

From Obsidian or chat, create a file in `audit/`:

```markdown
---
filed: 2026-04-19T14:30:00
target: wiki/concepts/SwellingMechanisms.md
severity: medium
anchor_text: "swelling rate of 5%/at% BU"
---

The swelling rate should be 2-5%/at% BU, not a fixed 5%.
See Rest 2001 Table 3 for the range.
```

### Severity Levels

| Level | Meaning |
|-------|---------|
| `high` | Factually wrong — fix immediately |
| `medium` | Imprecise or misleading — fix soon |
| `low` | Style, clarity, or completeness — fix when convenient |

## Processing Feedback (AI)

1. Read open audit files in `audit/`
2. Locate target text using `anchor_text`
3. Decide action:
   - **Accept**: Apply correction
   - **Partial**: Apply what makes sense
   - **Reject**: Explain why (may be based on misreading)
   - **Defer**: Add to CLAUDE.md open questions
4. Append resolution:

```markdown
# Resolution

2026-04-19 · accepted.
Changed "5%/at% BU" to "2-5%/at% BU (depends on temperature and burnup)".
Updated: wiki/concepts/SwellingMechanisms.md line 47.
```

5. Move to `audit/resolved/` (filename unchanged)
6. Log: `## [HH:MM] audit | resolved <filename> — <one-line what>`

## Rules

- **Never delete** audit files — rejected ones go to resolved/ too
- **Never ignore** open audits — process them periodically
- **One issue per file** — keeps resolution tracking clean
- **Anchors matter** — use exact text so AI can locate the target
