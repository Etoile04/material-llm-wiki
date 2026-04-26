# Computational & Experimental Studies of Microstructure-Scale Porosity in Metallic Fuels (Index)

## Metadata

| Field | Value |
|-------|-------|
| **PI/Authors** | Paul Millett (U. Arkansas), Sean McDeavitt (Texas A&M), Chaitanya Deo (Georgia Tech), Robert Mariani (INL) |
| **Year** | 2018 |
| **DOI** | 10.2172/1419662 |
| **Report Type** | Final Report, NEUP Project 14-6472, DOE Grant DE-NE0008309 |
| **Key Journal Paper** | Berry & Millett, J. Nucl. Mater. 491 (2017) 48–54 |

---

## Overview

This DOE-NEUP final report investigates **bimodal pore size distributions** in metallic fuels (U, U-Zr) as a strategy to resist densification during early in-pile service, preserving pore volume to accommodate fission gas swelling.

**Core computational finding**: Using a 2D Cahn-Hilliard phase-field model, bimodal distributions (small + large pores) resist densification **significantly more** than monomodal small-pore distributions at the same overall porosity. The optimum is ξ = 60 (60% small pores by area) at 96% theoretical density, which outperforms even a monomodal large-pore distribution.

**Physical mechanism**: Large pores act as vacancy sinks, intercepting vacancies released by dissolving small pores and interrupting long-range vacancy transport to the outer surface. In some bimodal configurations, intermediate pores nucleate from vacancy-dense regions, further retarding densification.

**Experimental scope**: Powder fabrication (hydride-dehydride, rotating electrode atomization) and sintering of U and U-10Zr compacts at Texas A&M; atomistic simulations (MEAM/MD) of U-Zr diffusion and interfacial energies at Georgia Tech.

---

## Sub-Pages

- [[wiki/summaries/2018_Millett_ComputationalExperimentalPorosityMetallic/KeyEquations|KeyEquations]] — Cahn-Hilliard model, free energy functional, bimodal parameter ξ, simulation parameters
- [[wiki/summaries/2018_Millett_ComputationalExperimentalPorosityMetallic/FindingsDesign|FindingsDesign]] — Key findings, densification resistance data, design implications, open questions

---

## Key Equations

> Reconstructed from Berry & Millett, J. Nucl. Mater. 491 (2017) 48–54 and standard Cahn-Hilliard phase-field methodology.

### Cahn-Hilliard Free Energy Functional

The total free energy of the two-phase (matrix + pore) system:

$$F = \int_V \left[ f_b(c) + \frac{\kappa}{2}|\nabla c|^2 \right] dV$$

where:
- $c$ is the conserved order parameter ($c = 0$: matrix, $c = 1$: pore)
- $f_b(c)$: bulk free energy density (double-well potential)
- $\kappa$: gradient energy coefficient (related to interface energy $\sigma$ and interface width $l$)

### Double-Well Potential

$$f_b(c) = W c^2(1-c)^2$$

where $W$ is the double-well height controlling the energy barrier between matrix and pore phases.

### Evolution Equation

$$\frac{\partial c}{\partial t} = \nabla \cdot \left( M \nabla \mu \right)$$

where the chemical potential is:

$$\mu = \frac{\delta F}{\delta c} = \frac{\partial f_b}{\partial c} - \kappa \nabla^2 c = 2Wc(1-c)(1-2c) - \kappa \nabla^2 c$$

and $M$ is the mobility (related to vacancy diffusivity $D_v$ and atomic volume $\Omega$).

### Bimodal Pore Distribution Parameter

$$\xi = \frac{A_{\text{small}}}{A_{\text{small}} + A_{\text{large}}} \times 100$$

where $A_{\text{small}}$ and $A_{\text{large}}$ are the total cross-sectional areas of small and large pores respectively. Optimum found at $\xi = 60$ (60% small pores by area) at 96% theoretical density.

### Interface Energy-Gradient Coefficient Relationship

$$\sigma = \frac{2\sqrt{2}}{3}\sqrt{W\kappa}, \quad l = \frac{2\sqrt{2\kappa}}{\sqrt{W}}$$

where $\sigma$ is the matrix-pore interfacial energy and $l$ is the diffuse interface width.

---

## Relationships

- [[wiki/entities/PhaseFieldModeling|PhaseFieldModeling]] — Cahn-Hilliard model for bimodal pore distribution and densification resistance
- [[wiki/entities/CavitationalVoid|CavitationalVoid]] — vacancy-driven porosity evolution and densification mechanism
- [[wiki/entities/FuelAlloy|FuelAlloy]] — U and U-10Zr metallic alloy porosity design
- [[wiki/concepts/SwellingMechanisms|SwellingMechanisms]] — bimodal pore design strategy to preserve pore volume for fission gas swelling accommodation
- [[wiki/summaries/2009_Rokkam_PhaseFieldVoidNucleationGrowth|Rokkam 2009 PF Void]] — phase-field void nucleation/growth model (related methodology)
- [[wiki/summaries/2008_Surh_VoidNucleationGrowthCoalescence|Surh 2008 Void Coalescence]] — void nucleation, growth, and coalescence model
- [[wiki/summaries/1990_Hofman_SwellingBehaviorUPuZr|Hofman 1990 U-Pu-Zr Swelling]] — metallic fuel swelling behavior reference
- [[wiki/summaries/2018_Liang_3DPhaseFieldIntragranularBubbleUMo|Liang 2018 Phase-Field]] — related PF methodology for gas bubble evolution in UMo

## Related Work
- [[wiki/summaries/2009_Rokkam_PhaseFieldVoidNucleationGrowth|2009_Rokkam_PhaseFieldVoidNucleationGrowth]] — 相场方法模拟空位形核与生长的先驱工作
- [[wiki/summaries/2011_Millett_PhaseFieldGasBubbleKinetics|2011_Millett_PhaseFieldGasBubbleKinetics]] — Millett 早期相场气泡动力学模型
- [[wiki/summaries/2018_Liang_3DPhaseFieldIntragranularBubbleUMo|2018_Liang_3DPhaseFieldIntragranularBubbleUMo]] — 3D相场晶内气泡演化，方法互补
- [[wiki/summaries/2022_Aagesen_PFBubbleInterconnection|2022_Aagesen_PFBubbleInterconnection]] — Cahn-Hilliard相场模拟气泡互联，同一框架的延伸
- [[wiki/summaries/1990_Hofman_SwellingBehaviorUPuZr|1990_Hofman_SwellingBehaviorUPuZr]] — 金属燃料肿胀行为的基础实验参考
- [[wiki/concepts/SwellingMechanisms|SwellingMechanisms]] — 双峰孔隙设计策略与肿胀机制的关联
