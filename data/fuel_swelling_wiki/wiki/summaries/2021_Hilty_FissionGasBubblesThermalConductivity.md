# Impact of Fission Gas Bubbles on Thermal Conductivity of UO₂ Fuels with High Thermal Conductivity Additives

## Metadata

| Field | Value |
|-------|-------|
| **Authors** | Floyd W. Hilty, Dong-Uk Kim, Michael R. Tonks |
| **Year** | 2021 |
| **Journal** | Journal of Nuclear Materials |
| **Volume** | 546 |
| **Article** | 152779 |
| **DOI** | 10.1016/j.jnucmat.2021.152779 |
| **Affiliation** | Dept. of Materials Science and Engineering, University of Florida |
| **Keywords** | Fission gas bubbles, UO₂, High thermal conductivity additives |
| **Method** | 2D mesoscale simulation (phase-field + AEH homogenization via MOOSE) |

---

## Overview

This paper studies how fission gas bubbles forming at additive-UO₂ interfaces degrade the thermal conductivity benefit of high-conductivity additives (e.g., BeO). Using phase-field + AEH homogenization in MOOSE, the authors show that bubbles can **completely screen** additives from heat flow — eliminating or even reversing their benefit.

Key contributions:
- **Screening fraction** ($S$) as the best single metric for bubble impact on ETC
- Analytical ETC model: $(k_\text{eff} - k_0)/k_0 = a(k_1/k_0 - 1)S^2$
- Aspect ratio correction: $a = 0.54 - 0.2\ln(R)$
- Critical thresholds: bubble vf ~0.04 (θ = 35°) and ~0.07 (θ = 45°) eliminate additive benefit
- Contact angle is the dominant unknown controlling screening severity

---

## Key Equations

> Key equations from Hilty, Kim & Tonks, J. Nucl. Mater. 546 (2021) 152779.

### Analytical Effective Thermal Conductivity (ETC) Model

The fractional change in thermal conductivity due to additive particles with bubble screening:

$$\frac{k_{\text{eff}} - k_0}{k_0} = a \left( \frac{k_1}{k_0} - 1 \right) S^2$$

where:
- $k_0$: thermal conductivity of UO₂ matrix
- $k_1$: thermal conductivity of additive (e.g., BeO)
- $k_{\text{eff}}$: effective thermal conductivity
- $S$: screening fraction (fraction of additive surface covered by fission gas bubbles)
- $a$: aspect ratio correction factor

### Screening Fraction

$$S = \frac{A_{\text{bubbles}}}{A_{\text{additive surface}}}$$

$S = 0$: no screening (full additive benefit); $S = 1$: complete screening (no additive benefit).

### Aspect Ratio Correction

$$a = 0.54 - 0.2 \ln(R)$$

where $R$ is the bubble aspect ratio (minor/major axis). For spherical bubbles ($R = 1$): $a = 0.54$.

### Critical Bubble Volume Fractions

Additive benefit is eliminated when bubble volume fraction exceeds:
- $f_b^{\text{crit}} \approx 0.04$ at contact angle $\theta = 35°$
- $f_b^{\text{crit}} \approx 0.07$ at contact angle $\theta = 45°$

Contact angle $\theta$ is the dominant unknown controlling screening severity.

### AEH Homogenization (MOOSE)

The asymptotic expansion homogenization solves:

$$\nabla \cdot \left( k(\mathbf{x}) \nabla T_0 \right) = 0$$

with periodic boundary conditions on the mesoscale RVE containing UO₂, additive particles, and fission gas bubbles, yielding the effective conductivity tensor $\mathbf{k}^{\text{eff}}$.

---

## Sub-Pages

- [[wiki/summaries/2021_Hilty_FissionGasBubblesThermalConductivity/PhysicalMechanisms|2021_Hilty_FissionGasBubblesThermalConductivity/PhysicalMechanisms]] — bubble formation, thermal screening, contact angle dependence
- [[wiki/summaries/2021_Hilty_FissionGasBubblesThermalConductivity/AnalyticalModel|2021_Hilty_FissionGasBubblesThermalConductivity/AnalyticalModel]] — ETC model equations, screening fraction, aspect ratio fitting
- [[wiki/summaries/2021_Hilty_FissionGasBubblesThermalConductivity/SimulationResults|2021_Hilty_FissionGasBubblesThermalConductivity/SimulationResults]] — MOOSE/AEH results, critical bubble fractions, parameter studies

---

## Relationships

- [[wiki/entities/PhaseFieldModeling|PhaseFieldModeling]] — MOOSE phase-field + AEH homogenization methodology
- [[wiki/entities/FissionGasDiffusion|FissionGasDiffusion]] — Xe/Kr diffusion to additive-UO₂ interfaces drives bubble formation and thermal screening
- [[wiki/concepts/SwellingMechanisms|SwellingMechanisms]] — fission gas bubble volume fraction and contact angle drive thermal conductivity degradation
- [[wiki/summaries/2020_Aagesen_BisonUPuZrSwellingLowerLengthScale|2020_Aagesen_BisonUPuZrSwellingLowerLengthScale]] — Aagesen phase-field model used in this work
- [[wiki/summaries/2016_Hu_GasBubbleSuperlatticeFormationPF|2016_Hu_GasBubbleSuperlatticeFormationPF]] — related phase-field bubble modeling
- [[wiki/summaries/2011_Millett_PhaseFieldGasBubbleKinetics|2011_Millett_PhaseFieldGasBubbleKinetics]] — phase-field bubble kinetics framework
- [[wiki/summaries/2023_Ye_IntegratedSimulationU10Mo|2023_Ye_IntegratedSimulationU10Mo]] — integrated fuel simulation using Bruggeman thermal conductivity model for bubble-containing fuel
- [[wiki/summaries/2020_Williams_PIRT_SwellingUZr|2020_Williams_PIRT_SwellingUZr]] — PIRT framework for fission gas effects on fuel performance

## Related Work
- [[wiki/summaries/2011_Millett_PhaseFieldGasBubbleKinetics|2011_Millett_PhaseFieldGasBubbleKinetics]] — 气泡动力学相场框架，方法基础
- [[wiki/summaries/2016_Hu_GasBubbleSuperlatticeFormationPF|2016_Hu_GasBubbleSuperlatticeFormationPF]] — 超点阵相场模型，气泡-热导率耦合的前驱
- [[wiki/summaries/2023_Ye_IntegratedSimulationU10Mo|2023_Ye_IntegratedSimulationU10Mo]] — 集成燃料模拟中使用Bruggeman热导率模型
- [[wiki/summaries/2020_Aagesen_BisonUPuZrSwellingLowerLengthScale|2020_Aagesen_BiperUPuZrSwellingLowerLengthScale]] — Aagesen相场模型被本文采用
- [[wiki/entities/PhaseFieldModeling|PhaseFieldModeling]] — MOOSE相场+AEH均匀化方法论
- [[wiki/concepts/SwellingMechanisms|SwellingMechanisms]] — 裂变气泡体积分数驱动热导率退化机制
