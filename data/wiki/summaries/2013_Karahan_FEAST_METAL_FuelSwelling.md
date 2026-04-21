# Extended Fuel Swelling Models for U-Pu-Zr Metallic Fuel Using FEAST-METAL

**Authors:** Aydın Karahan, Nathan C. Andrews  
**Year:** 2013  
**Journal:** Nuclear Engineering and Design, 258, 26–34  
**DOI:** 10.1016/j.nucengdes.2013.02.004  
**Affiliation:** MIT, Center for Advanced Nuclear Energy Systems  
**Fuel System:** [[wiki/entities/FuelAlloy|U-Pu-Zr]] (U-19Pu-10Zr, U-6Zr); Cladding: HT9

---

## Overview

This paper presents extended fuel swelling models for [[wiki/entities/FuelAlloy|U-Pu-Zr metallic fuel]] in the FEAST-METAL code, validated against EBR-II X425/X430 assemblies and applied to ultra-high burnup (36 at.%) design.

**Key innovations:**
- **Phase-dependent modeling**: bubble morphology, [[wiki/entities/FissionGasDiffusion|gas diffusion]] activation energies, and sintering compressibility all vary with phase structure (α+δ, β+δ, or single γ)
- **10% gas swelling threshold** for open porosity confirmed probabilistically
- **Solid FP swelling** corrected to 1.2%/at.% (from 1.5%)
- Dual-phase sintering compressibility $C = 0.23$ vs. γ-phase $C = 1.0$

**Ultra-high burnup prediction:** 36 at.% fuel with 60% smear density at 550 °C peak clad temperature achieves <3% clad hoop strain and 95% gas release.

---

## Key Equations

### Fission Gas Diffusion Coefficient (Phase-Dependent)

**Dual phase** ($T < T_6$, $T_6 = 923\,\text{K}$ for U-19Pu-10Zr):

$$D_g = 1.0 \times 10^{-4} \exp\!\left(-\frac{52{,}000}{RT}\right) \quad [\text{m}^2/\text{s}]$$

**Single $\gamma$ phase** ($T > T_6$):

$$D_g = 0.3 \times 10^{-8} \exp\!\left(-\frac{28{,}500}{RT}\right) \quad [\text{m}^2/\text{s}]$$

where $R = 1.987\,\text{cal/(mol·K)}$.

### Pressure Sintering Compressibility Factor

$$\alpha = \begin{cases} 0 & \varepsilon_{\text{opn}} = 0 \\ C \times \tfrac{1}{6} \times \varepsilon_{\text{opn}} \times 0.1^{1.5} & 0 < \varepsilon_{\text{opn}} < 0.1 \\ C \times \tfrac{1}{6} & \varepsilon_{\text{opn}} > 0.1 \end{cases}$$

$C = 1.0$ (single $\gamma$), $C = 0.23$ (dual phases).

### Solid Fission Product Swelling

$$\left(\frac{\Delta V}{V}\right)_{\text{solid FP}} = 1.2\% \text{ per at.% burnup}$$

### Gas Swelling Threshold for Open Porosity

$$S_{\text{threshold}} = 10\% \quad \text{(confirmed probabilistically)}$$

> Full equations and parameter tables: [[wiki/summaries/2013_Karahan_FEAST_METAL_FuelSwelling/KeyEquations|Key Equations sub-page]]

---

## Detailed Sections

- [[wiki/summaries/2013_Karahan_FEAST_METAL_FuelSwelling/PhysicalMechanisms|Physical Mechanisms]] — Bubble nucleation, phase-dependent morphology, open porosity, pressure sintering, FCMI, FCCI
- [[wiki/summaries/2013_Karahan_FEAST_METAL_FuelSwelling/KeyEquations|Key Equations & Parameters]] — Phase-dependent diffusion coefficients, compressibility factor, bubble group parameters
- [[wiki/summaries/2013_Karahan_FEAST_METAL_FuelSwelling/ExperimentalData|Experimental Data & Benchmark Results]] — EBR-II X425/X430 validation, ultra-high burnup predictions

---

## Relationships

- [[wiki/entities/FuelAlloy|FuelAlloy]] — U-Pu-Zr metallic fuel alloy swelling across multiple phases is the subject material
- [[wiki/concepts/SwellingMechanisms|SwellingMechanisms]] — phase-dependent gas bubble swelling, solid fission product swelling, and pressure sintering are all modeled
- [[wiki/entities/FissionGasDiffusion|FissionGasDiffusion]] — phase-dependent fission gas diffusion coefficients (dual vs. single γ phase) are key inputs
- [[wiki/concepts/SwellingModelComparison|SwellingModelComparison]] — FEAST-METAL benchmarks against EBR-II data and extends ultra-high burnup predictions
- [[wiki/summaries/2001_Rest_GRSIS_FissionGasMetallic|2001_Rest_GRSIS_FissionGasMetallic]] — FEAST-METAL uses the GRSIS algorithm as its core fission gas module
- [[wiki/summaries/1990_Hofman_SwellingBehaviorUPuZr|1990_Hofman_SwellingBehaviorUPuZr]] — EBR-II experimental data from Hofman's program provides validation benchmarks

---

*Source: Karahan, A., & Andrews, N.C. (2013). Nuclear Engineering and Design, 258, 26–34.*
