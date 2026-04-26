# Schema Guide — CLAUDE.md Template

> What to put in the wiki's CLAUDE.md file

## Template

```markdown
# <Wiki Topic> — Schema

## Scope

This wiki covers <one-sentence scope>.
It does NOT cover <explicit exclusions>.

## Naming Conventions

- **Files**: `YYYY_FirstAuthor_ShortTitle.md` (PascalCase)
- **Concepts**: `ConceptName.md` (no spaces, PascalCase)
- **Entities**: `EntityName.md`
- **Parameters**: `<source_slug>.json` — **MUST match summary filename exactly**
- **Registry**: `paper_registry.json` — DOI/slug → paper metadata mapping

## Anti-Duplication Rules ⚠️ MANDATORY

**Before writing any file, check `paper_registry.json`!**

1. **DOI lookup**: Search registry by DOI. If found → append to existing slug
2. **Title fuzzy match**: similarity > 0.85 → same paper, reuse slug
3. **Author+Year**: Check `first_author` + `year` combination
4. **Slug format**: MUST be `YYYY_FirstAuthor_ShortTitle` (year first). Forbidden: `Author_YYYY_Title`
5. **Register**: After creating new paper entry → update `paper_registry.json`
6. **Reports/handbooks** without DOI: use `report_id` (e.g., `INL/EXT-15-36520`) as key

### paper_registry.json Format

```json
{
  "<DOI_or_report_id>": {
    "slug": "YYYY_Author_ShortTitle",
    "title": "Full paper title",
    "year": 2022,
    "first_author": "Author",
    "doi": "10.xxxx/...",
    "report_id": null,
    "has_params": true,
    "param_count": 42
  }
}
```

## Terminology

- <Term 1>: <Definition>
- <Term 2>: <Definition>

## Units

- Temperature: Kelvin (K) or °C (specify)
- Length: meters (m), nanometers (nm)
- Energy: electronvolts (eV)
- Pressure: pascals (Pa), megapascals (MPa)
- Diffusivity: m²/s
- Swelling: % (specify linear or volumetric)

## Current Articles

### Concepts (<N>)
- [[concepts/ConceptA]] — one-line summary
- ...

### Entities (<N>)
- [[entities/EntityA]] — one-line summary
- ...

### Summaries (<N>)
- [[summaries/SourceA]] — one-line summary
- ...

## Research Gaps

1. <Gap 1>: <What's missing>
2. <Gap 2>: <What's missing>

## Open Questions

1. <Question 1>
2. <Question 2>

## Recent Activity

- YYYY-MM-DD: <What happened>
```

## Rules

1. **Read at session start** — CLAUDE.md + wiki/index.md together define the wiki state
2. **Update after every compile** — reflect structural changes
3. **Keep gaps current** — drive future ingestion priorities
4. **Naming is law** — consistent naming enables wikilinks and lint checks
