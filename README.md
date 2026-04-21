# material-llm-wiki

LLM Wiki for nuclear material property knowledge extraction, normalization, validation, and comparison.

## What this repo contains

This repository mainly hosts the `llm-wiki` skill and related planning/materials for building a structured literature-to-knowledge workflow.

### Core directories

- `skills/llm-wiki/` - the main skill, prompts, references, and helper scripts
- `plans/` - development plans and workflow notes
- `clawd/` - supporting skill/tooling code kept in the workspace

## What is not tracked

Generated knowledge-base outputs and local workspace/private memory files are intentionally excluded from version control, including:

- extracted literature data
- raw MinerU outputs
- private memory/persona files
- local learning logs

## Main use case

The repo is designed for workflows like:

1. ingest literature PDFs or text sources
2. extract structured parameters and equations
3. validate schema and parameter quality
4. generate normalized summaries and comparison-ready outputs

## Notes

This repository was cleaned for public sharing, so some local workspace files referenced by older notes may not be present here.

## License

No license has been added yet. Add one before accepting external reuse or contributions.
