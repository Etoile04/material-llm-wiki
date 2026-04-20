# Metal Fuel Irradiation Swelling — Schema

## Scope

This wiki covers the physics, modeling, and experimental data of irradiation-induced swelling in metallic nuclear fuels (U-Mo, U-Zr, U-Pu-Zr). It supports model parameter determination for fuel performance codes.

It does NOT cover: oxide fuels (UO₂), ceramic fuels (UN, UC as primary), reactor physics, or cladding-only behavior.

## Naming Conventions

- **Summaries**: `YYYY_FirstAuthor_ShortTitle.md` (e.g., `1992_Rest_CavitationalSwellingAlphaUPuZr.md`)
- **Concepts**: `ConceptName.md` (PascalCase, e.g., `SwellingMechanisms.md`)
- **Entities**: `EntityName.md` (e.g., `Recrystallization.md`)
- **Parameters**: `<source_slug>.json` (matches summary filename)
- **Logs**: `YYYYMMDD.md`

## Terminology

- **FCCI**: Fuel-Cladding Chemical Interaction
- **GBS**: Gas Bubble Superlattice
- **PF**: Phase-Field (modeling method)
- **SRT**: Simple Rate Theory
- **GRSIS**: Generalized Rate Theory for Swelling in Irradiated Solids
- **JSRT**: Jiao's SRT (calibrated version)
- **LEU**: Low-Enriched Uranium
- **burnup**: measured in at% (atomic percent) or fissions/m³

## 语言规范

- **页面内容**: 中文为主，英文术语首次出现标注括号
- **文件名**: 保持英文（YYYY_Author_Title.md）
- **参数符号**: 英文（$D_v$, $E_m$ 等）
- **术语对照表**: `raw/terminology.md`（160+ 条目）
- **格式示例**: 「裂变气体气泡（Fission Gas Bubble, FGB）」

## 单位规范

- 温度: K 或 °C（注明）
- 肿胀: %（注明线性 ΔL/L 或体积 ΔV/V）
- 扩散系数: m²/s
- 能量: eV
- 气泡半径: nm
- 气泡密度: m⁻³
- 位错密度: m⁻²
- 燃耗: at% 或 fissions/m³
- 热导率: W/(m·K)
- 压力: Pa 或 MPa

## Current Articles

### Concepts (3)
- [[wiki/concepts/SwellingMechanisms|SwellingMechanisms]] — Overview of swelling mechanisms
- [[wiki/concepts/RateTheoryFramework|RateTheoryFramework]] — Mathematical framework for rate theory
- [[wiki/concepts/SwellingModelComparison|SwellingModelComparison]] — Systematic model comparison

### Entities (7)
- [[wiki/entities/CavitationalVoid|CavitationalVoid]] — Void formation by fission gas nucleation
- [[wiki/entities/GasBubbleSuperlattice|GasBubbleSuperlattice]] — Ordered bubble arrays
- [[wiki/entities/Recrystallization|Recrystallization]] — Irradiation-induced grain restructuring
- [[wiki/entities/FuelAlloy|FuelAlloy]] — U-Mo, U-Zr, U-Pu-Zr alloy systems
- [[wiki/entities/FissionGasDiffusion|FissionGasDiffusion]] — Gas transport mechanisms
- [[wiki/entities/PhaseFieldModeling|PhaseFieldModeling]] — Computational simulation method
- [[wiki/entities/RateTheory|RateTheory]] — Mean-field defect/gas evolution

### Summaries (47)
(see wiki/index.md for full list)

## Research Gaps

1. **Constituent redistribution** — Only 1 source covers Zr migration in U-Zr; need more
2. **Creep-swelling coupling** — 9 sources mention creep but parameters are sparse
3. **FCCI quantitative data** — Wastage rates, diffusion coefficients need systematic extraction
4. **600K data** — JSRT calibration fails at 600K; need low-T validation data
5. **Multi-physics coupling** — Thermal-mechanical-swelling feedback loops
6. **Parameter uncertainty** — Most parameters lack confidence intervals

## Open Questions

1. Why does JSRT predict zero swelling at 600K? Is it physical or a model artifact?
2. What is the correct vacancy migration energy in U-10Mo? (0.34 eV vs 0.6 eV in literature)
3. How to model the swelling transition at recrystallization onset?
4. Can U-Mo parameters be transferred to U-Zr with simple scaling?

## Recent Activity

- 2026-04-19: Restructured to LLM Wiki format; 47 sources, 7 entities, 1001 parameters extracted
- 2026-04-19: Created 5 new entities (Recrystallization, FuelAlloy, FissionGasDiffusion, PhaseFieldModeling, RateTheory)
- 2026-04-19: Parameter database v2.0 — 1001 parameters from 47 sources
