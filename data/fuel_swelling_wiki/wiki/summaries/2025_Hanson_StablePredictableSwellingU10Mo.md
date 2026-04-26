# Microstructurally Validated Stable and Predictable Swelling in Low-Enriched Uranium Monolithic U-10Mo Fuel Mini-Plates

## Metadata

| Field | Value |
|-------|-------|
| **Authors** | William A. Hanson, Daniele Salvato, Adam B. Robinson, Nancy J. Lybeck, Jan-Fong Jue, Tammy L. Trowbridge, Jatuporn Burns, Fidelma G. Di Lemma, Charlyne A. Smith, Margaret A. Marshall, Dennis D. Keiser Jr., Jeffrey J. Giglio, James I. Cole |
| **Year** | 2025 |
| **Journal** | Journal of Nuclear Materials |
| **Volume/Pages** | 609, 155746 |
| **DOI** | 10.1016/j.jnucmat.2025.155746 |
| **Affiliation** | Idaho National Laboratory |
| **Material** | Monolithic U-10 wt%Mo (U-10Mo) LEU fuel |
| **Keywords** | Low-enriched uranium, high-performance research reactor fuel, monolithic U-10Mo, post-irradiation examination, fuel swelling, microstructural evolution |

---

## Overview

This paper presents **post-irradiation examination (PIE)** of the MP-1 experiment — ~47,000 swelling-fission density data pairs from 74 LEU monolithic U-10Mo mini-plates irradiated in ATR. It validates the **Robinson et al. empirical quadratic swelling model** against commercially fabricated fuel plates across fission densities up to ~6 × 10²¹ f/cm³.

Key contributions:
- **No breakaway swelling** observed up to 6 × 10²¹ f/cm³ — stable, predictable behavior confirmed
- Commercial fabrication (homogenized C-plates) produces **lower swelling** than non-homogenized B-plates, statistically significant at all fission densities
- Three-stage microstructural evolution identified: grain boundary bubble precipitation → grain refinement + superlattice collapse → HBS
- Recommended Robinson et al. model is **conservative** for both fabrication types
- Swelling measurement formula accounts for Pilling-Bedworth ratio (1.975) for U oxide

---

## Key Equations

### Swelling Calculation with Pilling-Bedworth Correction (reconstructed)

Fuel swelling accounting for oxide formation:

$$\frac{\Delta V}{V_0} = \frac{\Delta V_{meas}}{V_0} \cdot \frac{1}{PB}$$

where $PB = 1.975$ is the Pilling-Bedworth ratio for U oxide (ratio of oxide volume to metal volume consumed), and $\Delta V_{meas}/V_0$ is the raw volumetric swelling from dimensional measurements.

### Robinson et al. Empirical Quadratic Swelling Model (reconstructed)

$$\frac{\Delta V}{V_0} = A \cdot F_D + B \cdot F_D^2$$

where $F_D$ is the fission density (fissions/cm³), and $A$, $B$ are empirical coefficients fitted to irradiation data. This model is validated as **conservative** for both homogenized (C-plate) and non-homogenized (B-plate) fabrication types up to $6 \times 10^{21}$ f/cm³.

### Three-Stage Swelling Model (reconstructed)

$$\frac{\Delta V}{V_0}(F_D) = \begin{cases} \alpha_1 F_D & F_D < F_D^{GBS} \text{ (Stage I: GB bubble precipitation)} \\ \alpha_1 F_D^{GBS} + \alpha_2(F_D - F_D^{GBS}) & F_D^{GBS} < F_D < F_D^{rx} \text{ (Stage II: superlattice + recrystallization)} \\ \alpha_1 F_D^{GBS} + \alpha_2(F_D^{rx} - F_D^{GBS}) + \alpha_3(F_D - F_D^{rx}) & F_D > F_D^{rx} \text{ (Stage III: HBS porosity)} \end{cases}$$

Transition points: $F_D^{GBS} \approx 1 \times 10^{21}$ f/cm³ (GBS onset), $F_D^{rx} \approx 3 \times 10^{21}$ f/cm³ (recrystallization/superlattice collapse). Swelling rate accelerates in Stage III due to enhanced grain boundary area from grain refinement.

### Fission Density from Burnup (reconstructed)

$$F_D = \frac{BU \cdot N_A \cdot \rho}{M_{U-235} \cdot \bar{\nu}}$$

where $BU$ is the burnup (MWd/kgU), $N_A$ is Avogadro's number, $\rho$ is the fuel density, $M_{U-235}$ is the molar mass of U-235, and $\bar{\nu}$ is the average neutrons per fission.

### No Breakaway Swelling Criterion (from experimental observation)

No breakaway swelling threshold observed up to $F_D = 6 \times 10^{21}$ f/cm³, meaning:

$$\frac{d^2(\Delta V/V_0)}{dF_D^2} \leq 2B$$

throughout the measured range — the quadratic model remains valid with no higher-order terms needed.

---

## Sub-Pages

- [[wiki/summaries/2025_Hanson_StablePredictableSwellingU10Mo/PhysicalMechanisms|2025_Hanson_StablePredictableSwellingU10Mo/PhysicalMechanisms]] — three-stage microstructural evolution, Mo homogenization effect, swelling constraint
- [[wiki/summaries/2025_Hanson_StablePredictableSwellingU10Mo/ExperimentalData|2025_Hanson_StablePredictableSwellingU10Mo/ExperimentalData]] — MP-1 experiment design, measurements, historical experiment contributions
- [[wiki/summaries/2025_Hanson_StablePredictableSwellingU10Mo/SwellingModel|2025_Hanson_StablePredictableSwellingU10Mo/SwellingModel]] — swelling calculation equations, empirical model, statistical analysis, JSRT parameters

---

## Relationships

- [[wiki/entities/FuelAlloy|FuelAlloy]] — LEU monolithic U-10Mo fuel from the MP-1 experiment (~47k data pairs, 74 mini-plates) is validated
- [[wiki/entities/Recrystallization|Recrystallization]] — three-stage microstructural evolution including grain refinement and HBS formation
- [[wiki/entities/GasBubbleSuperlattice|GasBubbleSuperlattice]] — FCC superlattice collapse at ~3×10²¹ f/cm³ marks stage II transition
- [[wiki/concepts/SwellingMechanisms|SwellingMechanisms]] — no breakaway swelling up to 6×10²¹ f/cm³; stable and predictable behavior is the key finding
- [[wiki/concepts/SwellingModelComparison|SwellingModelComparison]] — Robinson et al. empirical model validated as conservative for both C-plate and B-plate types
- [[wiki/summaries/2021_Robinson_PredictiveSwellingUMoMonolithic|2021_Robinson_PredictiveSwellingUMoMonolithic]] — the recommended empirical swelling model validated here
- [[wiki/summaries/2023_Ye_IntegratedSimulationU10Mo|2023_Ye_IntegratedSimulationU10Mo]] — mechanistic DART/GRASS simulation of the same swelling stages
- [[wiki/summaries/2022_Hanson_EMPIrESwellingAnalysis|2022_Hanson_EMPIrESwellingAnalysis]] — earlier swelling analysis methodology from the same group
- [[wiki/summaries/2015_Gan_ThermalStabilityGasBubbleSuperlattice|2015_Gan_ThermalStabilityGasBubbleSuperlattice]] — gas bubble superlattice in U-Mo thermal stability context
- [[wiki/summaries/2023_Smith_EarlySelfOrganizationGBS|2023_Smith_EarlySelfOrganizationGBS]] — fission gas superlattice self-organization and collapse
- [[wiki/summaries/2026_FigueroaBengoa_HighBurnupPorosityUMo|2026_FigueroaBengoa_HighBurnupPorosityUMo]] — high burnup porosity data beyond MP-1 fission density range

## Related Work
- [[wiki/summaries/2022_Hanson_EMPIrESwellingAnalysis|2022_Hanson_EMPIrESwellingAnalysis]] — 同作者早期EMPIrE实验分析，本文是其后续验证研究
- [[wiki/summaries/2026_FigueroaBengoa_HighBurnupPorosityUMo|2026_FigueroaBengoa_HighBurnupPorosityUMo]] — 高燃耗(>8×10²¹ f/cm³)孔隙率数据，延伸了本文MP-1的燃耗范围
- [[wiki/summaries/2023_Ye_IntegratedSimulationU10Mo|2023_Ye_IntegratedSimulationU10Mo]] — DART/GRASS机理模拟，本文的三阶段微结构演化模型可与其对照
- [[wiki/summaries/2023_Smith_EarlySelfOrganizationGBS|2023_Smith_EarlySelfOrganizationGBS]] — GBS早期自组织TEM研究，对应本文Stage I→II的微观转变机理
- [[wiki/summaries/2021_Robinson_PredictiveSwellingUMoMonolithic|2021_Robinson_PredictiveSwellingUMoMonolithic]] — 本文验证的Robinson经验二次肿胀模型
- [[wiki/concepts/SwellingModelComparison|SwellingModelComparison]] — 本文对B-plate和C-plate的统计比较是该概念的重要实例
