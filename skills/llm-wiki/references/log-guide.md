# Log Guide — Operation Log Convention

## File Naming

One file per day: `log/YYYYMMDD.md`

Example: `log/20260419.md`

## Format

```markdown
# 2026-04-19

## [09:21] ingest | Rest_1992_Cavitational — Cavitational void swelling model (touched 5 pages)
## [09:25] ingest | Karahan_2013_FEAST — FEAST metal fuel model (touched 8 pages)
## [09:45] compile | Split VoidSwelling into 3 sub-pages
## [10:00] query | "What is the swelling rate of U-10Mo at 400°C?"
## [10:30] lint | 3 dead links fixed, 2 orphans found
## [14:00] audit | resolved 20260419-100022-formula-error — Fixed D_v value
```

## Entry Format

```
## [HH:MM] <operation> | <description>
```

### Operations

| Op | Description |
|----|-------------|
| `compile` | Restructure wiki content |
| `ingest` | Add new source |
| `query` | Answer question against wiki |
| `lint` | Health check |
| `audit` | Process human feedback |
| `promote` | Promote query answer to concept page |
| `split` | Split oversized page |
| `scaffold` | Create new wiki |

## Rules

1. **Append only** — never edit past entries
2. **Every operation** must be logged
3. **Include file count** — "touched N pages"
4. **Keep descriptions short** — one line max

## Quick History

```bash
# Recent operations
grep -rh "^## \[" log/ | tail -20

# All ingests
grep -rh "ingest" log/

# Operations today
cat log/$(date +%Y%m%d).md
```
