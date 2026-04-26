# Lessons Learned — LLM Wiki Parameter Extraction

> Generic lessons from building the fuel_swelling_wiki knowledge base (2026-04-26).
> Apply these to ANY llm-wiki knowledge base.

---

## 1. Slug Duplication — P0 Critical ⚠️

**Root cause**: No unique identifier for papers. Slug is free-form text, same paper can have multiple valid names.

**4-layer defense**:
1. **DOI as primary key** — every paper MUST have `doi` field; no-DOI reports use `report_id`
2. **`paper_registry.json`** — maps DOI/slug → paper metadata; MUST be checked before ANY write
3. **Pre-extraction dedup** — DOI exact match → title fuzzy match (>0.85) → author+year
4. **Slug format enforcement** — `YYYY_FirstAuthor_ShortTitle` ONLY; reject non-conforming

**Template**:
```json
{
  "<doi_or_slug>": {
    "slug": "YYYY_Author_ShortTitle",
    "title": "Paper title",
    "year": 2026,
    "first_author": "Author",
    "doi": "10.xxx/yyy",
    "param_file": "parameters/YYYY_Author_ShortTitle.json",
    "summary_file": "wiki/summaries/YYYY_Author_ShortTitle.md",
    "added_date": "2026-01-01",
    "last_extracted": "2026-01-01"
  }
}
```

## 2. Extraction Prompt Must Be Standardized — P0 ⚠️

**Root cause**: Hand-written prompts cause inconsistent behavior (wrong field names, nested formats, missing values).

**Mandatory extraction rules**:
1. JSON output MUST be flat array `[...]`, NOT nested `{"parameters":[...]}`
2. Numeric values go in `value` field — NEVER `scalar`, `number`, or `constant`
3. `value_type` ONLY allows: `scalar` | `range` | `expression` | `list`
4. Do NOT create records without concrete numeric values
5. Qualitative descriptions use `value_type: expression` with `value_expr`
6. Check `paper_registry.json` BEFORE writing — append to existing file if paper exists
7. Slug format MUST be `YYYY_FirstAuthor_ShortTitle`

**Use `batch_extract.py` to generate standardized prompts. NEVER hand-write.**

## 3. Post-Extraction Validation Is Mandatory — P1

**Root cause**: Without validation, malformed parameters accumulate silently.

**Mandatory post-extraction steps**:
```bash
python3 scripts/batch_extract.py --mode post-validate
# Issues MUST = 0 before reporting completion
```

**Common issues to auto-fix**:
- `confidence` as number (0.95) → map to `high`/`medium`/`low`
- `category` as Chinese text → map to standard English categories
- `value_type: range` without `value_min`/`value_max` → downgrade to `expression`
- Missing `confidence` → default to `medium`
- Missing `symbol` → infer from `name`
- ID format not starting with `YYYY_` → prepend year

## 4. Pipeline Scripts Must Be Referenced IN Workflow Steps — P1

**Root cause**: Scripts exist in `scripts/` but aren't mentioned in operation steps. Agents fall back to familiar patterns (direct sessions_spawn).

**Solution**: Trigger Table at TOP of SKILL.md:
```markdown
| User Intent | Required Script | Mandatory Steps |
|---|---|---|
| "extract parameters" | batch_extract.py | MUST: dedup → generate prompt → extract → validate |
| "ingest paper" | ingest_single_full.lobster | MUST: registry check → PDF→MD → LLM → validate |
| "validate" | batch_extract.py --post-validate | MUST: fix all issues |
```

**Also add forbidden actions**:
- 🚫 Direct sessions_spawn with hand-written extraction prompts
- 🚫 Creating new slugs without checking paper_registry.json
- 🚫 Completing extraction without post-validate

## 5. Sub-Agent Reliability — P2

**Problem**: ~20% of sub-agents exit without doing work (0 tokens used).

**Prevention**:
- Max 6 papers per group
- Write per-paper (don't batch all reads then writes)
- Prompt must state "you MUST complete all read and write operations"
- Timeout: 900s+

## 6. Two-Stage Extraction — P2

- **Stage 1**: Extract from summary/wiki (clear numeric values only)
- **Stage 2**: Extract from PDF raw text (human-triggered, for missed parameters)
- NEVER create skeleton records without values in Stage 1

---

*Template version: 2026-04-26. Adapted from fuel_swelling_wiki experience.*
