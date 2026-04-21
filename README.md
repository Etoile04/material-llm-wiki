# material-llm-wiki

LLM Wiki for nuclear material property knowledge extraction, normalization, validation, and comparison.

## What this repo contains

This repository mainly hosts the `llm-wiki` skill and related planning materials for building a structured literature-to-knowledge workflow.

### Core directories

- `skills/llm-wiki/` - the main skill, prompts, references, and helper scripts
- `plans/` - development plans and workflow notes
- `clawd/` - supporting workspace tooling retained in this repository

## Quick start

### 1. Inspect the main skill

Start from:

- `skills/llm-wiki/SKILL.md`

That file contains the operating workflow, ingestion guidance, validation expectations, and supporting references.

### 2. Review supporting references

Useful supporting materials live under:

- `skills/llm-wiki/references/`
- `skills/llm-wiki/scripts/`

### 3. Adapt to your own local data

This public repository does **not** include the generated knowledge-base outputs or raw extraction artifacts.

You are expected to bring your own:

- PDF / literature corpus
- extraction outputs
- local data directories
- private configuration and tokens

## Intended workflow

Typical usage looks like this:

1. ingest literature PDFs or text sources
2. extract structured parameters and equations
3. validate schema and parameter quality
4. generate normalized summaries and comparison-ready outputs
5. iterate on prompts, scripts, and extraction rules

## What is not tracked

Generated knowledge-base outputs and local workspace/private files are intentionally excluded from version control, including:

- extracted literature data
- raw MinerU outputs
- private memory/persona files
- local learning logs
- local secrets and tokens

## Public repo note

This repository was cleaned for public sharing, so some local workspace files referenced by older notes may not be present here.

## License

This project is currently released under the MIT License.
