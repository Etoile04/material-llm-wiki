# Integrated Simulation of U-10Mo Monolithic Fuel Swelling Behavior

## Metadata

| Field | Value |
|-------|-------|
| **Authors** | Bei Ye, Aaron Oaks, Shenyang Hu, Benjamin Beeler, Jeff Rest, Zhi-Gang Mei, Abdellatif Yacout |
| **Year** | 2023 |
| **Journal** | Journal of Nuclear Materials |
| **Volume/Pages** | 583, 154542 |
| **DOI** | 10.1016/j.jnucmat.2023.154542 |
| **Affiliation** | Argonne National Laboratory (primary), PNNL, NCSU/INL |
| **Keywords** | U-Mo fuel, fuel performance modeling, fission gas behavior, fuel swelling |
| **Code** | DART (Dispersion Analysis Research Tool) with GRASS module |

---

## Overview

This paper presents an integrated, rate-theory-based mechanistic model for U-10Mo monolithic fuel swelling using the **DART code** with the **GRASS fission gas module**. The model tracks fission gas bubble nucleation, radiation-induced re-solution, and coalescence at intragranular, grain face, grain edge, and grain corner locations. Grain subdivision (recrystallization) using phase-field-predicted kinetics is explicitly incorporated.

Key contributions:
- Recalibrated U-10Mo-specific parameters (vs. prior UO₂-based values): surface energy 1850 dyn/cm (DFT), $D_0$ reduced ~100×
- Three-level spatial meshing with 4 grain sizes (1.34–17 μm)
- Temperature is identified as dominant driver of apparent fission-rate effects
- Solid FP swelling: $\Delta V/V_0 = 4.0 \times F_D$; swelling rate transition at ~3–3.5 × 10²¹ fis/cm³
- Corner bubbles dominate porosity at high burnup

## Key Equations

### Xe Diffusivity in U-10Mo (reconstructed from GRASS model)

Arrhenius form for Xe diffusion in γ-U-10Mo:

$$D_{Xe} = D_0 \exp\left(-\frac{Q}{k_B T}\right)$$

where $D_0$ is the pre-exponential factor (recalibrated ~100× lower than UO₂-based values) and $Q$ is the activation energy. Surface energy from DFT: $\gamma = 1850$ dyn/cm = 1.85 J/m².

### Bubble Nucleation Rate (reconstructed)

Classical nucleation theory for intragranular fission gas bubbles:

$$J = J_0 \exp\left(-\frac{\Delta G^*}{k_B T}\right)$$

where the critical nucleation barrier:

$$\Delta G^* = \frac{16\pi \gamma^3}{3(\Delta P)^2}$$

$\Delta P$ is the effective pressure difference driving nucleation, $\gamma$ is the surface energy.

### Bubble Growth by Vacancy Absorption (reconstructed)

$$\frac{dN}{dt} = 4\pi r^2 D_v (c_v - c_v^{eq})$$

$$\frac{dr}{dt} = \frac{D_v \Omega}{r}\left(S_v - \frac{2\gamma \Omega}{r k_B T}\right)$$

where $N$ is the number of gas atoms in the bubble, $D_v$ is vacancy diffusivity, $\Omega$ is atomic volume, and $S_v$ is vacancy supersaturation.

### Fission Gas Release Rate (reconstructed)

For grain boundary bubble interconnection and gas release:

$$\frac{dR}{dt} = f(\dot{F}, T, d_{grain}, \phi_{GB})$$

where $\dot{F}$ is the fission rate, $d_{grain}$ is grain diameter, and $\phi_{GB}$ is the fractional coverage of grain faces by bubbles.

### Solid Fission Product Swelling (from summary)

$$\frac{\Delta V}{V_0} = 4.0 \times F_D$$

where $F_D$ is the fission density in fissions/cm³.

### Recrystallization Kinetics (reconstructed)

Grain subdivision fraction based on accumulated fission density:

$$f_{rx} = 1 - \exp\left[-\left(\frac{F_D - F_D^{crit}}{F_0}\right)^n\right]$$

where $F_D^{crit} \approx 3 \times 10^{21}$ f/cm³ is the critical fission density for recrystallization onset, and $F_0$, $n$ are fitting parameters from phase-field predictions.

### Bubble Population Balance (reconstructed)

$$\frac{\partial f(r,t)}{\partial t} + \frac{\partial}{\partial r}\left[\dot{r} \cdot f(r,t)\right] = J\delta(r - r_c) - \lambda f(r,t) + \text{coalescence terms}$$

where $f(r,t)$ is the bubble size distribution, $J$ is the nucleation rate, $\lambda$ is the re-solution rate, and coalescence terms account for bubble merging.

---

## Sub-Pages

- [[2023_Ye_IntegratedSimulationU10Mo/PhysicalMechanisms]] — nucleation, re-solution, coalescence, gas migration, recrystallization
- [[2023_Ye_IntegratedSimulationU10Mo/KeyEquations]] — Xe diffusivity, nucleation rates, re-solution, calibrated parameters
- [[2023_Ye_IntegratedSimulationU10Mo/ModelArchitecture]] — DART/GRASS code, three-level meshing, calibration plates, key findings

---

## Relationships

- [[wiki/entities/FuelAlloy|FuelAlloy]] — U-10Mo monolithic fuel integrated swelling simulation is the subject
- [[wiki/entities/Recrystallization|Recrystallization]] — grain subdivision kinetics from phase-field model are explicitly incorporated
- [[wiki/concepts/RateTheoryFramework|RateTheoryFramework]] — DART/GRASS rate-theory ODE framework is the core methodology
- [[wiki/entities/FissionGasDiffusion|FissionGasDiffusion]] — recalibrated Xe diffusivity and re-solution parameters for U-10Mo are key contributions
- [[wiki/summaries/2001_Rest_GRSIS_FissionGasMetallic|2001_Rest_GRSIS_FissionGasMetallic]] — GRASS module origin (Rest's methodology)
- [[wiki/summaries/2005_Rest_RecrystallizationSwellingUO2UMo|2005_Rest_RecrystallizationSwellingUO2UMo]] — recrystallization swelling model basis
- [[wiki/summaries/2020_Beeler_ImprovedEOSXeBubbleUMo|2020_Beeler_ImprovedEOSXeBubbleUMo]] — improved Xe equation of state used here
- [[wiki/summaries/2021_Robinson_PredictiveSwellingUMoMonolithic|2021_Robinson_PredictiveSwellingUMoMonolithic]] — swelling correlation used for validation
- [[wiki/summaries/2025_Hanson_StablePredictableSwellingU10Mo|2025_Hanson_StablePredictableSwellingU10Mo]] — subsequent experimental validation of swelling model
- [[wiki/summaries/2021_Hilty_FissionGasBubblesThermalConductivity|2021_Hilty_FissionGasBubblesThermalConductivity]] — thermal conductivity treatment of bubble-containing composite fuel
- [[wiki/concepts/SwellingModelComparison|SwellingModelComparison]] — DART/GRASS compared against Kim-Hofman and Robinson empirical correlations
