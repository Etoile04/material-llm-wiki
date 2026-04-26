# Physical Processes and Mechanisms Related to Fission Gas Swelling in MX-Type Nuclear Fuels

**Author:** C. Ronchi  
**Year:** 1979  
**Journal:** Journal of Nuclear Materials, Vol. 84, pp. 55–84  
**DOI:** 10.1016/0022-3115(79)90150-8  
**Affiliation:** Joint Research Centre, Karlsruhe Establishment, European Institute for Transuranium Elements

---

## Overview

This foundational 1979 paper by Ronchi presents a mechanistic treatment of [[wiki/entities/FissionGasDiffusion|fission gas]] swelling in MX-type fuels (carbides MC, carbonitrides, nitrides MN). The TPROF code is developed to model bubble nucleation, growth, coalescence, [[wiki/entities/RateTheory|Ostwald ripening]], sweeping, grain boundary release, and pore interlinkage.

**Key distinction from oxide fuels:** In MX fuels, fission spikes cause only gas-atom re-ejection (not bulk displacement), making ripening effective and allowing self-similar log-normal bubble distributions to emerge naturally from the stochastic physics.

**Temperature regimes:**
- **Below $T_c$**: Swelling ~linear in burnup; matrix is rigid; non-equilibrium model essential
- **Above $T_c$**: Swelling ~$b^{3/2}$; matrix relaxes; equilibrium model applicable
- **Critical $T_c$**: Sharp transition (experimental observation confirmed)

**Percolation release threshold:** $P > 1.569$ bonds per grain boundary site; fabrication porosity >10% needed for >50% open pores.

---

## Detailed Sections

- [[wiki/summaries/1979_Ronchi_FissionGasSwellingMX_Fuels/PhysicalMechanisms|Physical Mechanisms]] — Nucleation, growth, resolution, coalescence, ripening, sweeping, porosity dynamics
- [[wiki/summaries/1979_Ronchi_FissionGasSwellingMX_Fuels/KeyEquations|Key Equations & Parameters]] — Full rate equations, diffusion coefficients, swelling relationships, percolation condition
- [[wiki/summaries/1979_Ronchi_FissionGasSwellingMX_Fuels/ExperimentalData|Experimental Data & Model Description]] — TPROF code structure, observations, JSRT relevance

---

## Key Equations

### Rate Equation System (Gas Atom Balance)

$$\frac{dc}{dt} = p - \frac{db^*}{dt} - \frac{dg}{dt} - \frac{dR}{dt}$$

$$\frac{db_j}{dt} = K_j r_j c - C_0 r_j n_j$$

where $K_j = 4\pi n_j D_g$ is the capture rate constant for the $j$th bubble class, $C_0 = 4\pi d q f / b'$ is the re-solution parameter, $p$ is the fission gas production rate.

### Bubble Diffusion Coefficient

$$D_b = \frac{h^2}{6} f \left[\frac{3D_V}{r^3} + \frac{4\pi D_s a^4}{r^4}\right] \quad \text{for } r > r_+$$

where $D_V$ is volume diffusivity, $D_s$ is surface diffusivity, $a$ is the jump distance.

### Swelling–Burnup Relationship

- **Below $T_c$ (rigid matrix):** Swelling $\sim$ linear in burnup $b$
- **Above $T_c$ (relaxed matrix):** $\frac{\Delta V}{V} = K b^{3/2}$

### Van der Waals Equation of State for Bubble Gas

$$(p + a^*/V^2)(V - b^*) = nRT, \quad p = 2\gamma/r \text{ (equilibrium)}$$

### Percolation Condition for Gas Release

$$P > 1.569 \quad \text{(bonds per grain boundary site)}$$

Fabrication porosity $>$ 10% needed for $>$ 50% open pores.

> Full equations and parameter tables: [[wiki/summaries/1979_Ronchi_FissionGasSwellingMX_Fuels/KeyEquations|Key Equations sub-page]]

---

## Relationships

- [[wiki/entities/FissionGasDiffusion|FissionGasDiffusion]] — Diffusion coefficients and gas kinetics
- [[wiki/entities/RateTheory|RateTheory]] — Bubble population rate theory and percolation framework
- [[wiki/entities/CavitationalVoid|CavitationalVoid]] — Contrast: void vs. gas bubble swelling mechanisms
- [[wiki/summaries/2001_Rest_GRSIS_FissionGasMetallic|Rest 2001 — GRSIS metallic fuel model]] — Extended gas release model building on this framework
- [[wiki/summaries/2013_Karahan_FEAST_ExtendedSwelling_UPuZr|Karahan 2013 — FEAST-METAL]] — Modern fuel performance code using similar gas swelling physics

---

*Source: Ronchi, C. (1979). Journal of Nuclear Materials, 84, 55–84.*

## Related Work
- [[wiki/summaries/1990_Hofman_SwellingBehaviorUPuZr|1990_Hofman_SwellingBehaviorUPuZr]] — Hofman 对 U-Pu-Zr 金属燃料的肿胀行为研究，与本文 MX 型燃料形成陶瓷/金属燃料对比
- [[wiki/summaries/2001_Rest_GRSIS_FissionGasMetallic|2001_Rest_GRSIS_FissionGasMetallic]] — GRSIS 模型借鉴了本文气泡成核、长大和渗透释放的理论框架，应用于金属燃料
- [[wiki/entities/RateTheory|RateTheory]] — 本文 TPROF 代码基于速率理论描述气泡种群动力学
- [[wiki/concepts/FissionGasReleaseModels|FissionGasReleaseModels]] — 本文的渗透理论阈值条件是裂变气体释放模型的重要基础
- [[wiki/summaries/2008_Surh_VoidNucleationGrowthCoalescence|2008_Surh_VoidNucleationGrowthCoalescence]] — Surh 用团簇动力学方法处理空洞形核与合并，是本文气泡合并物理的后续发展
