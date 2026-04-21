# 3D Phase-Field Simulations of Intragranular Gas Bubbles in U-Mo Fuel (Index)

## Metadata

| Field | Value |
|-------|-------|
| **Authors** | Linyun Liang, Zhi-Gang Mei, Yeon Soo Kim, Mihai Anitescu, Abdellatif M. Yacout (ANL) |
| **Journal** | Computational Materials Science |
| **Year** | 2018 |
| **Volume/Pages** | 145, 86–95 |
| **DOI** | 10.1016/j.commatsci.2017.12.061 |
| **Material** | U-7Mo (bcc, 7 wt.% Mo) |

---

## Overview

First **3D phase-field model** for intragranular gas bubble evolution in irradiated U-Mo fuel, extending Millett et al. (2011) 2D work with additional physics: fission gas re-solution, dislocation sink bias, grain boundary sinks, and full elastic strain energy. Four interacting fields are tracked: Xe concentration, vacancy concentration, SIA concentration, and bubble phase parameter.

**Key result**: Stable nanometer-size intragranular bubbles (2.7–3.8 nm, ~2.4 × 10²⁴ m⁻³) emerge naturally from the balance between defect production and annihilation without artificial suppression of fission gas. Average bubble pressure ~1.3 GPa.

**Design insight**: Larger fuel grains and lower dislocation density reduce intragranular swelling. Rolling-induced dislocations significantly increase swelling (~2× change over examined dislocation density range).

---

## Key Equations

> Equations reconstructed from the paper's 3D phase-field model formulation (extending Millett 2011 2D work).

### 1. Free Energy Functional

$$F = \int_V \left[ f(c_{Xe}, c_v, c_i, \eta) + \frac{\kappa_{Xe}}{2}|\nabla c_{Xe}|^2 + \frac{\kappa_v}{2}|\nabla c_v|^2 + \frac{\kappa_i}{2}|\nabla c_i|^2 + \frac{\kappa_\eta}{2}|\nabla \eta|^2 + E_{elast} \right] dV$$

where $c_{Xe}$, $c_v$, $c_i$ are Xe, vacancy, and SIA concentrations; $\eta$ is the bubble phase parameter; $\kappa$ are gradient energy coefficients; and $E_{elast}$ is the elastic strain energy.

### 2. Cahn-Hilliard Equations for Conserved Fields

$$\frac{\partial c_{Xe}}{\partial t} = \nabla \cdot (M_{Xe} \nabla \mu_{Xe}) + G_{Xe} - S_{Xe}$$

$$\frac{\partial c_v}{\partial t} = \nabla \cdot (M_v \nabla \mu_v) + G_v - S_v$$

$$\frac{\partial c_i}{\partial t} = \nabla \cdot (M_i \nabla \mu_i) + G_i - S_i$$

where $M$ are mobilities, $\mu = \delta F / \delta c$ are chemical potentials, $G$ are generation rates, and $S$ are sink rates.

### 3. Allen-Cahn Equation for Phase Parameter

$$\frac{\partial \eta}{\partial t} = -L_\eta \frac{\delta F}{\delta \eta}$$

where $L_\eta$ is the kinetic coefficient for the bubble/matrix interface.

### 4. Defect Generation (Fission)

$$G_{Xe} = y_{Xe} \cdot \dot{f}$$

$$G_v = G_i = \frac{\dot{f}}{2} (1 + \alpha)$$

where $\alpha$ is the displacement damage enhancement factor (~25 for U-Mo).

### 5. Sink Terms

**Dislocation sinks (biased absorption):**
$$S_v^{disl} = Z_v \rho_d D_v c_v, \quad S_i^{disl} = Z_i \rho_d D_i c_i$$

where $Z_v < Z_i$ (dislocation bias for SIAs, $Z_i - Z_v \approx 0.01$), $\rho_d$ is dislocation density.

**Grain boundary sinks:**
$$S^{gb} = \frac{\pi^2 D}{d_g^2} c$$

where $d_g$ is the grain diameter.

**Recombination:**
$$S_{rec} = K_{iv} c_i c_v$$

**Fission-induced re-solution:**
$$S_{res} = b \cdot c_{Xe}^{bubble} \cdot (1 - \eta)$$

### 6. Elastic Strain Energy

$$E_{elast} = \frac{1}{2} C_{ijkl} \epsilon_{ij}^{elas} \epsilon_{kl}^{elas}$$

$$\epsilon_{ij}^{elas} = \epsilon_{ij}^{total} - \epsilon_{ij}^0, \quad \epsilon_{ij}^0 = \beta(c_{Xe} - c_{Xe}^0) \delta_{ij}$$

where $\beta$ is the lattice misfit strain (Xe in U-Mo matrix) and $c_{Xe}^0$ is the reference concentration.

### 7. Swelling Calculation

$$\frac{\Delta V}{V} = \langle \eta \rangle + \beta \langle c_{Xe} \rangle$$

where $\langle \eta \rangle$ is the volume-averaged bubble phase fraction and $\beta \langle c_{Xe} \rangle$ accounts for dissolved Xe strain.

### 8. Key Simulation Results

- Stable bubble radius: $r_b = 2.7\text{--}3.8\,\text{nm}$
- Bubble number density: $N_b \approx 2.4 \times 10^{24}\,\text{m}^{-3}$
- Bubble pressure: $P_b \approx 1.3\,\text{GPa}$

## Sub-Pages

- [[wiki/summaries/2018_Liang_3DPhaseFieldIntragranularBubbleUMo/KeyEquations|KeyEquations]] — Free energy functional, governing PDEs, sink/source terms, swelling formula
- [[wiki/summaries/2018_Liang_3DPhaseFieldIntragranularBubbleUMo/ParametersFindings|ParametersFindings]] — Material parameters (DFT/MD), simulation setup, key findings, validation

---

## Relationships

- [[wiki/entities/PhaseFieldModeling|PhaseFieldModeling]] — first 3D phase-field model for intragranular gas bubble evolution in U-Mo
- [[wiki/entities/RateTheory|RateTheory]] — sink/source rate terms and defect balance physics
- [[wiki/concepts/RateTheoryFramework|RateTheoryFramework]] — vacancy, SIA, and Xe concentration rate equations form the model backbone
- [[wiki/entities/Recrystallization|Recrystallization]] — destroys intragranular bubble structure at high fission density; motivates focus on pre-recrystallization regime
- [[wiki/entities/GasBubbleSuperlattice|GasBubbleSuperlattice]] — related ordered structure observed experimentally (not modeled here)
- [[wiki/entities/FuelAlloy|FuelAlloy]] — U-7Mo bcc alloy with dislocation density effects on swelling
- [[wiki/summaries/2011_Millett_PhaseFieldGasBubbleKinetics|Millett 2011 Phase-Field]] — 2D predecessor this work extends
- [[wiki/summaries/2016_Hu_GrainMorphologyGasBubbleUMo|Hu 2016 Booth Model]] — complementary rate-theory model; similar grain size/fission rate findings
- [[wiki/summaries/2015_Miller_TEMGasBubbleSuperlatticeU7Mo|Miller 2015 TEM]] — experimental validation data for bubble density and size
- [[wiki/summaries/2016_Hu_GasBubbleSuperlatticeFormationPF|Hu 2016 Superlattice PF]] — 2D phase-field model for bubble superlattice formation (same fuel, different focus)
