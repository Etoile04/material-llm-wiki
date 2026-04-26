# Recrystallization and Fission-Gas-Bubble Swelling of U-Mo Fuel

**Authors:** Yeon Soo Kim (ANL), G.L. Hofman (ANL), J.S. Cheon (KAERI)  
**Year:** 2013  
**Journal:** Journal of Nuclear Materials, 436, 14–22  
**DOI:** 10.1016/j.jnucmat.2013.01.291

---

## Overview

This paper establishes the mechanistic link between [[wiki/entities/Recrystallization|recrystallization]] and enhanced fission-gas-bubble (FGB) swelling in U-Mo fuels. A semi-empirical modified Avrami equation describes recrystallization kinetics, and a combined swelling model spans pre- and post-recrystallization regimes.

**Key finding:** Post-recrystallization FGB swelling rate (5.2% per $10^{21}$ f/cm³) is **8.7×** higher than the pre-recrystallization rate (0.6%). [[wiki/entities/Recrystallization|Recrystallization]] subdivides original micron grains into sub-micron new grains, dramatically increasing grain boundary area and FGB nucleation sites.

**Critical thresholds:**
- Recrystallization onset: ~$3\times10^{21}$ f/cm³
- Full recrystallization (atomized U-10Mo): ~$5.0$–$5.5\times10^{21}$ f/cm³
- Pre-rx [[wiki/entities/GasBubbleSuperlattice|bubble superlattice]] collapses during recrystallization

---

## Key Equations

### Modified Avrami Recrystallization Equation

$$V_{rx} = 1 - \exp[-K(F - F_0)^n]$$

| Symbol | Meaning |
|--------|---------|
| $V_{rx}$ | Recrystallized volume fraction |
| $K$ | Reaction constant (depends on Mo content) |
| $F$ | Fission density (f/cm³) |
| $F_0$ | Incubation fission density |
| $n$ | Avrami exponent (= 2.6) |

### Mo Content Dependence

$$K = K_0 \left[0.75(10 - x_{\text{Mo}}) + 1\right], \quad K_0 = 0.1$$

### Combined FGB Swelling Rate

$$\left.\frac{\Delta V}{V_0}\right|_g = (1 - V_{rx})\left.\frac{\Delta V}{V_0}\right|_{g,0} + V_{rx}\left.\frac{\Delta V}{V_0}\right|_{g,rx}$$

Pre-recrystallization rate: $0.6\%$ per $10^{21}$ f/cm³; Post-recrystallization: $5.2\%$ per $10^{21}$ f/cm³ (**8.7×** increase).

### Analytical Solution (Incomplete Gamma Function)

$$\left.\frac{\Delta V}{V_0}\right|_g = \left.\frac{\Delta V}{V_0}\right|_{g,0} F + \left(\left.\frac{\Delta V}{V_0}\right|_{g,rx} - \left.\frac{\Delta V}{V_0}\right|_{g,0}\right)\int_0^F V_{rx}\,dF$$

$$\int_0^F V_{rx}\,dF = F - F_0 + \frac{n K^{-1/n}}{n}\left[\Gamma(1/n,\,K(F-F_0)^n) - \Gamma(1/n,\,0)\right]$$

> Full equations and parameter tables: [[wiki/summaries/2013_Kim_RecrystallizationFGBSwellingUMo/KeyEquations|Key Equations sub-page]]

---

## Detailed Sections

- [[wiki/summaries/2013_Kim_RecrystallizationFGBSwellingUMo/PhysicalMechanisms|Physical Mechanisms]] — Three-stage bubble evolution, recrystallization physics
- [[wiki/summaries/2013_Kim_RecrystallizationFGBSwellingUMo/KeyEquations|Key Equations & Parameters]] — Avrami equation, FGB swelling rate formulae, Gamma function solution
- [[wiki/summaries/2013_Kim_RecrystallizationFGBSwellingUMo/ExperimentalData|Experimental Data]] — RERTR-1 to RERTR-5 results across 20 samples

---

## Relationships

- [[wiki/entities/Recrystallization|Recrystallization]] — Central phenomenon in this paper; Avrami kinetics model quantified
- [[wiki/entities/GasBubbleSuperlattice|GasBubbleSuperlattice]] — Pre-recrystallization intragranular bubble structure collapses during recrystallization
- [[wiki/entities/FuelAlloy|FuelAlloy]] — U-Mo alloy fuels (4–10 wt% Mo) across different fabrication routes are studied
- [[wiki/concepts/SwellingMechanisms|SwellingMechanisms]] — recrystallization-driven FGB swelling rate increase (~8.7×) is the main finding
- [[wiki/summaries/2015_Miller_TEMGasBubbleSuperlatticeU7Mo|Miller 2015 — TEM superlattice collapse]] — TEM evidence for collapse at ~$4.5\times10^{21}$ f/cm³
- [[wiki/summaries/2016_Hu_GasBubbleSuperlatticeFormationPF|Hu 2016 — Phase-field superlattice model]] — Mechanistic explanation of superlattice formation
- [[wiki/summaries/2005_Rest_RecrystallizationSwellingUO2UMo|Rest 2005]] — Analytical recrystallization model used for comparison
- [[wiki/summaries/2008_Kim_IntergranularFGBubblesUMo|Kim 2008 — Intergranular FGBs in U-Mo]] — pre-transition bubble data
- [[wiki/summaries/2013_Kim_FissionInducedSwellingCreepUMo|Kim 2013 — Creep]] — companion paper using the same RERTR dataset

---

*Source: Kim, Y.S., Hofman, G.L., & Cheon, J.S. (2013). Journal of Nuclear Materials, 436, 14–22.*

## Related Work
- [[wiki/summaries/2013_Kim_FissionInducedSwellingCreepUMo|2013_Kim_FissionInducedSwellingCreepUMo]] — companion paper using the same RERTR dataset focusing on creep behavior
- [[wiki/summaries/2015_Miller_TEMGasBubbleSuperlatticeU7Mo|2015_Miller_TEMGasBubbleSuperlatticeU7Mo]] — TEM evidence for superlattice collapse at ~4.5×10²¹ f/cm³, confirming recrystallization threshold
- [[wiki/summaries/2016_Hu_GasBubbleSuperlatticeFormationPF|2016_Hu_GasBubbleSuperlatticeFormationPF]] — phase-field explanation of superlattice formation mechanism before recrystallization
- [[wiki/summaries/2005_Rest_RecrystallizationSwellingUO2UMo|2005_Rest_RecrystallizationSwellingUO2UMo]] — analytical recrystallization model for comparison
- [[wiki/summaries/2008_Kim_IntergranularFGBubblesUMo|2008_Kim_IntergranularFGBubblesUMo]] — pre-transition intergranular bubble data in U-Mo
- [[wiki/entities/GasBubbleSuperlattice|GasBubbleSuperlattice]] — pre-recrystallization bubble structure that collapses during grain subdivision
