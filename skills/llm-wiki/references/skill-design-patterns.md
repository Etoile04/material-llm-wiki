# Skill Design Patterns — Lessons from llm-wiki

> These patterns apply to ANY OpenClaw skill, not just llm-wiki.
> Extracted from 2026-04-26 fuel_swelling_wiki experience.

---

## Pattern 1: Trigger Table at the Top

**Problem**: Agent reads SKILL.md, sees 500+ lines of theory, forgets details by the time it needs to act. Falls back to "muscle memory" operations (direct sessions_spawn, exec, etc.).

**Solution**: Put a **Trigger Table** in the FIRST section after frontmatter, BEFORE any theory.

```markdown
## ⚡ Trigger Table — DO THIS FIRST

| User Intent | Required Script | Mandatory Steps |
|---|---|---|
| "extract parameters" | batch_extract.py | MUST: dedup → generate → extract → validate |
| "ingest paper" | ingest_single.lobster | MUST: check → convert → ingest → validate |
```

**Why it works**:
- LLMs process top of document with highest attention
- Table format is scannable in one pass
- Maps intent → action directly (no theory to wade through)

**Anti-pattern**: Putting scripts in a "Reference" or "Available Tools" section at the bottom.

---

## Pattern 2: Forbidden Actions (Negative Examples)

**Problem**: Telling agent what to do isn't enough. It also needs to know what NOT to do, especially when a familiar-but-suboptimal path exists.

**Solution**: Add explicit 🚫 **Forbidden** list right after the Trigger Table.

```markdown
### 🚫 禁止操作

- **禁止直接 sessions_spawn 手写 prompt** — 必须用标准化脚本
- **禁止不查 registry 就创建新文件** — 必须先查重
- **禁止完成后不校验** — issues 必须 = 0
```

**Why it works**:
- `🚫` emoji is visually distinctive, hard to skip
- "禁止" (forbidden) has stronger compliance than "不要" (don't) or "建议" (suggested)
- Targets the exact shortcuts the agent would otherwise take

**Anti-pattern**: Only describing the correct workflow without mentioning what the agent might incorrectly do instead.

---

## Pattern 3: Scaffold with Guardrails

**Problem**: New knowledge bases/projects start empty. Agent has no context about rules, so it makes mistakes that compound.

**Solution**: `scaffold.py` generates project config files (CLAUDE.md, registry, etc.) with ALL guardrails baked in from day 1.

```python
# scaffold.py generates:
# 1. CLAUDE.md with Pre-Action Checks + Anti-Dup rules
# 2. paper_registry.json (empty but ready)
# 3. Directory structure
```

**Why it works**:
- Rules are in the project, not in the agent's memory (which resets)
- Every new project inherits lessons from all previous projects
- No dependency on "the agent remembers"

---

## Pattern 4: Post-Action Validation Gate

**Problem**: Agent completes a task and reports success, but output has errors (wrong field names, duplicates, malformed data).

**Solution**: Add a **validation gate** that MUST pass before task completion.

```markdown
### AFTER ANY parameter write:
1. Run: `python3 scripts/batch_extract.py --mode post-validate`
2. If issues > 0: fix before reporting completion
3. NEVER report "done" with issues > 0
```

**Why it works**:
- Catches errors at the source, before they compound
- Creates a binary pass/fail state (not "mostly OK")
- Prevents the agent from declaring premature victory

---

## Pattern 5: Standardized Prompt Generation

**Problem**: Hand-written prompts for sub-agents are inconsistent. Each one describes rules slightly differently, causing variable output quality.

**Solution**: One script generates ALL prompts from a template.

```python
# batch_extract.py has EXTRACTION_PROMPT_TEMPLATE
# Every sub-agent gets the exact same rules
prompt = generate_prompt(slug, raw_path, param_path, existing_count)
```

**Why it works**:
- Eliminates prompt drift across sessions
- Rules live in ONE place (the template), easy to update
- Sub-agents can't "forget" rules they never saw

---

## Pattern 6: Lessons Learned File

**Problem**: Agent makes mistakes, fixes them, but doesn't record what went wrong. Next session repeats the same mistakes.

**Solution**: `references/lessons-learned.md` in the skill repo, with concrete examples and remediation templates.

```markdown
## 1. Slug Duplication — P0 Critical ⚠️
**Root cause**: No unique identifier for papers.
**4-layer defense**: ...
**Template**: ...
```

**Why it works**:
- Future agents read the file and learn from others' mistakes
- Structured format (Root cause → Defense → Template) makes it actionable
- Lives in the repo, so it travels with the skill

---

## Pattern 7: Scripts Referenced IN Workflow Steps, Not Just Listed

**Problem**: Scripts exist in `scripts/` directory, mentioned in a reference table, but never connected to actual workflow steps.

**Solution**: Every operation step directly names the script to run.

```markdown
## Operations

### ingest
1. Run: `python3 scripts/batch_extract.py --mode find-unextracted`
2. For each candidate: `python3 scripts/run_llm_ingest.py ...`
3. After: `python3 scripts/batch_extract.py --mode post-validate`
```

**Anti-pattern**:
```markdown
## Available Scripts
- batch_extract.py — does batch extraction
- validate_params.py — validates parameters

## Operations
### ingest
1. Find papers to extract
2. Extract parameters
3. Validate results
```
(Scripts listed separately, steps are vague)

---

## Applying to Other Skills

| Skill | Applicable Patterns | How |
|---|---|---|
| **coding-agent** | 1, 2, 4 | Trigger: "debug" → `coding-agent SKILL.md` workflow. Forbidden: don't run random commands without reading context. Validate: build/test after changes. |
| **deep-research** | 1, 2, 5 | Trigger: "research X" → standard workflow. Forbidden: don't use single source. Standardize: report template. |
| **feishu-docx-powerwrite** | 1, 2, 4 | Trigger: "write doc" → check token → append/write. Forbidden: don't overwrite without confirmation. Validate: preview before sending. |
| **any skill with sub-agents** | 5, 6 | Standardize prompts. Record lessons. |

---

*Version: 2026-04-26. Based on fuel_swelling_wiki experience (2,494 → 0 validation issues, 5 GitHub commits).*
