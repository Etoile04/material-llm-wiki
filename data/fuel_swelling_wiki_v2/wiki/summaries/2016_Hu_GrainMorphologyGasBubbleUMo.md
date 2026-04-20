# Effect of Grain Morphology on Gas Bubble Swelling in UMo Fuels – 3D Booth Model (Index)

## Metadata

| Field | Value |
|-------|-------|
| **Authors** | Shenyang Hu, Douglas Burkes, Curt A. Lavender, Vineet Joshi (PNNL) |
| **Journal** | Journal of Nuclear Materials |
| **Year** | 2016 |
| **Volume/Pages** | 480, 323–331 |
| **DOI** | 10.1016/j.jnucmat.2016.08.038 |
| **Fuel Type** | γ-UMo (dispersion and monolithic) |

---

## Overview

This paper extends the classical Booth model from a single representative spherical grain to a **3D polycrystalline microstructure**, enabling spatially resolved simulation of fission gas diffusion, intra-granular and inter-granular gas bubble nucleation/growth/re-solution, and swelling kinetics in UMo fuels.

**Core innovation**: Grain morphology (size and aspect ratio) is shown to significantly affect swelling kinetics. Smaller grains and higher aspect ratios both accelerate swelling by shortening fission gas diffusion paths to grain boundaries.

Key physical mechanisms include athermal fission gas diffusion ($D_g \propto \dot{f}$), radiation-induced re-solution, and grain boundary as perfect sink. The model is valid **before recrystallization** (< 3.1–3.5 × 10²⁷ fissions/m³).

---

## Key Equations

> Equations reconstructed from the paper's 3D Booth model formulation (extension of classical Booth diffusion model to polycrystalline microstructures).

### 1. Generalized Booth Diffusion Equation

Gas concentration $c(r,\theta,\phi,t)$ within a grain of arbitrary morphology:

$$\frac{\partial c}{\partial t} = D_g \nabla^2 c + \dot{f} y_{Xe} - b \cdot c_b(1-\eta)$$

where $D_g$ is the athermal gas diffusivity, $\dot{f}$ is the local fission rate, $y_{Xe}$ is the Xe yield, $b$ is the re-solution rate, $c_b$ is the bubble gas concentration, and $\eta$ is the bubble volume fraction.

### 2. Athermal Fission Gas Diffusivity

$$D_g = \frac{\chi a^2 \dot{f}}{4}$$

where $\chi$ is the gas atom jump probability per fission event and $a$ is the lattice parameter. This is the athermal (radiation-enhanced) diffusion — temperature-independent.

### 3. Boundary Conditions (Grain Boundary as Perfect Sink)

$$c|_{\partial \Omega} = c_{eq} \quad \text{(equilibrium solubility at grain boundary)}$$

$$D_g \frac{\partial c}{\partial n}\bigg|_{\partial \Omega} = \dot{g}_{gb} \quad \text{(gas flux to grain boundary)}$$

### 4. Intergranular Bubble Growth

$$\frac{d n_b}{dt} = 4\pi r_b D_{gb} c_{gb} - b_i n_b$$

$$\frac{d r_b}{dt} = \frac{D_{gb} (c_{gb} - c_{eq})}{r_b} - \frac{b_i n_b}{4\pi r_b^2}$$

where $n_b$ is gas atoms per bubble, $r_b$ is bubble radius, $D_{gb}$ is grain-boundary diffusivity, $c_{gb}$ is gas concentration at grain boundary, and $b_i$ is the intergranular resolution rate.

### 5. Equation of State (Van der Waals for Gas in Bubbles)

$$\left(P_{gas} + \frac{a_{vdW}}{V_m^2}\right)(V_m - b_{vdW}) = n_b k_B T$$

where $P_{gas}$ is the internal bubble pressure, $V_m$ is the molar volume, and $a_{vdW}$, $b_{vdW}$ are Van der Waals constants for Xe.

### 6. Bubble Radius from EOS

Mechanical equilibrium of a bubble:

$$r_b = \frac{2\gamma + P_{ext} r_b}{P_{gas}}$$

### 7. Swelling Strain

$$\epsilon_{swell} = \frac{\Delta V}{V} = \frac{4}{3}\pi r_b^3 N_b$$

where $N_b$ is the grain-boundary bubble number density per unit volume.

### 8. Grain Morphology Effect

The model solves the diffusion equation on actual 3D grain geometries (Voronoi tessellation), so the effective diffusion length $L_{eff}$ depends on grain size $d$ and aspect ratio $AR$:

$$L_{eff} \propto \frac{d}{f(AR)}$$

Smaller $d$ and higher $AR$ → shorter diffusion path → faster gas release to grain boundaries → accelerated swelling.

## Sub-Pages

- [[wiki/summaries/2016_Hu_GrainMorphologyGasBubbleUMo/KeyEquations|KeyEquations]] — Full rate-equation system (generalized Booth model, EOS, swelling formula)
- [[wiki/summaries/2016_Hu_GrainMorphologyGasBubbleUMo/ModelParameters|ModelParameters]] — Parameter table, crystal structures, Mo inhomogeneity
- [[wiki/summaries/2016_Hu_GrainMorphologyGasBubbleUMo/FindingsRelevance|FindingsRelevance]] — Key findings, JSRT relevance, limitations

---

## Relationships

- [[wiki/entities/RateTheory|RateTheory]] — rate-equation framework underpinning this generalized Booth model
- [[wiki/concepts/RateTheoryFramework|RateTheoryFramework]] — athermal fission gas diffusion and radiation-induced re-solution rate equations are core
- [[wiki/entities/Recrystallization|Recrystallization]] — model validity threshold (~3.1–3.5×10²⁷ fissions/m³) before recrystallization
- [[wiki/entities/FuelAlloy|FuelAlloy]] — γ-UMo alloy fuel grain morphology (size, aspect ratio) effects on swelling
- [[wiki/entities/FissionGasDiffusion|FissionGasDiffusion]] — athermal fission gas diffusion is the core transport mechanism
- [[wiki/concepts/SwellingMechanisms|SwellingMechanisms]] — grain morphology effects on fission gas bubble swelling kinetics are quantified
- [[wiki/summaries/2018_Liang_3DPhaseFieldIntragranularBubbleUMo|Liang 2018 Phase-Field]] — related 3D simulations with additional dislocation physics
- [[wiki/summaries/2013_Kim_RecrystallizationFGBSwellingUMo|Kim 2013]] — recrystallization effect on swelling
- [[wiki/summaries/2015_Cui_MechanisticGaseousSwellingUMo|Cui 2015]] — mechanistic swelling model for comparison
