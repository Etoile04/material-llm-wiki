# Assessment of Swelling and Constituent Redistribution in U-Zr Fuel Using PIRT

## Metadata

| Field | Value |
|-------|-------|
| **Title** | Assessment of Swelling and Constituent Redistribution in Uranium-Zirconium Fuel Using Phenomena Identification and Ranking Tables (PIRT) |
| **Authors** | W. J. Williams, D. M. Wachs, M. A. Okuniewski, S. van den Berghe |
| **Year** | 2020 |
| **Journal** | Annals of Nuclear Energy |
| **DOI** | 10.1016/j.anucene.2019.107016 |
| **Affiliations** | Purdue University; Idaho National Laboratory; SCK•CEN |
| **Keywords** | U-Zr, Constituent Redistribution, Fuel Swelling, PIRT |
| **Paper Type** | Review / Phenomenological Assessment |

---

## Overview

This paper applies the **Phenomena Identification and Ranking Table (PIRT)** methodology to U-Zr metallic fuel, systematically quantifying knowledge gaps for two key phenomena: **fuel swelling** and **constituent redistribution (thermomigration)**. It identifies top research priorities using weighted scoring of impact and knowledge ratios across ~11 source variables.

Key results:
- **External mechanical constraint** and **temperature** are the top knowledge gaps (weights 50 and 44) for both phenomena
- **Fission density** is fully understood (weight = 0)
- Solid FP swelling rate: ~1.5% volumetric per at% burnup
- Gas interconnection threshold: ~33% volumetric swelling
- Zr redistribution driven by Soret effect; spans 0–40 wt.% from initial U-10Zr

---

## Key Equations

> Reconstructed from PIRT methodology and empirical correlations cited in the paper.

### PIRT Weighting Formula

Each phenomenon–variable pair is scored by a composite weight combining **impact** ($I$) and **knowledge** ($K$) ratings from expert panel:

$$W_{\text{PIRT}} = I \times (1 - K)$$

where:
- $I$: normalized importance score (0–1), representing how strongly the variable affects the phenomenon
- $K$: normalized knowledge score (0–1), representing how well the phenomenon is understood/modelled
- $W_{\text{PIRT}}$: composite weight (0–1); higher values indicate greater research priority

Variables with $K \to 1$ (fully understood) get $W \to 0$ (e.g., fission density with weight = 0). Variables with $K \to 0$ (poorly understood) and high $I$ get highest weights (e.g., external mechanical constraint with weight = 50).

### Solid Fission Product Swelling Correlation

$$\frac{\Delta V}{V}\bigg|_{\text{solid FP}} \approx 1.5\% \text{ per at\% burnup}$$

### Gas Interconnection Threshold

$$\frac{\Delta V}{V}\bigg|_{\text{interconnection}} \approx 33\%$$

Above this volumetric swelling level, fission gas bubbles interconnect and rapid gas release begins.

### Soret Effect (Constituent Redistribution)

$$J_{\text{Zr}} = -D_{\text{Zr}} \left( \nabla C_{\text{Zr}} + \frac{Q^* C_{\text{Zr}}}{RT^2} \nabla T \right)$$

where:
- $J_{\text{Zr}}$: Zr flux (mass transport)
- $D_{\text{Zr}}$: Zr diffusion coefficient in U-Zr
- $Q^*$: heat of transport (Soret coefficient)
- $C_{\text{Zr}}$: Zr concentration
- $\nabla T$: temperature gradient

Zr redistributes from ~0 to ~40 wt.% across the fuel radius in U-10Zr, driven by the temperature gradient in the radial direction.

---

## Sub-Pages

- [[2020_Williams_PIRT_SwellingUZr/PhysicalMechanisms]] — Swelling driving forces, constituent redistribution zones, phase-dependent behavior
- [[2020_Williams_PIRT_SwellingUZr/PIRTFramework]] — PIRT weighting formula, full results table, key parameters, modeling approaches
- [[2020_Williams_PIRT_SwellingUZr/ExperimentalData]] — EBR-II / FFTF / AFC irradiation data, JSRT calibration parameters

---

## Relationships

- [[wiki/entities/FuelAlloy|FuelAlloy]] — U-Zr alloy system swelling and constituent redistribution are comprehensively assessed
- [[wiki/entities/CavitationalVoid|CavitationalVoid]] — void nucleation and growth mechanisms are identified as top knowledge gaps
- [[wiki/concepts/SwellingMechanisms|SwellingMechanisms]] — PIRT methodology ranks all swelling driving forces by impact and knowledge level
- [[wiki/concepts/SwellingModelComparison|SwellingModelComparison]] — competing models (JSRT, FEAST-METAL, BISON) and their knowledge gaps are compared
- [[wiki/summaries/1990_Hofman_SwellingBehaviorUPuZr|1990_Hofman_SwellingBehaviorUPuZr]] — early U-Pu-Zr swelling behavior (foundational reference)
- [[wiki/summaries/1993_Rest_VoidSwellingAlphaU|1993_Rest_VoidSwellingAlphaU]] — Rest cavitation/void swelling model for α-U (core modeling reference)
- [[wiki/summaries/2013_Karahan_FEAST_METAL_FuelSwelling|2013_Karahan_FEAST_METAL_FuelSwelling]] — FEAST-METAL extended swelling model cited here
- [[wiki/summaries/2016_Sun_NeutronRadiographyU10ZrSwelling|2016_Sun_NeutronRadiographyU10ZrSwelling]] — experimental U-10Zr swelling measurements
- [[wiki/summaries/2023_Ye_IntegratedSimulationU10Mo|2023_Ye_IntegratedSimulationU10Mo]] — integrated simulation extending similar rate-theory framework
