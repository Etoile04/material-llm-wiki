# Modifications and Applications of the Mechanistic Gaseous Swelling Model for UMo Fuel

> ⚠️ **WARNING: PDF was image-based** (Microsoft Print To PDF); content extracted from metadata only. Full extraction requires manual review.

## Metadata

| Field | Value |
|-------|-------|
| **Title** | Modifications and applications of the mechanistic gaseous swelling model for UMo fuel |
| **Authors** | Cui et al. (note: author list requires manual verification from PDF) |
| **Year** | 2015 |
| **Journal** | Journal of Nuclear Materials |
| **DOI** | 10.1016/j.jnucmat.2014.11.065 |
| **Extraction Status** | ⚠️ Partial — metadata only; PDF is image-based |

## Abstract

> Modifications are introduced to the mechanistic gaseous swelling model for UMo fuel. Analytical expressions are formulated to lower the computation cost. Parametric studies have been carried out to reveal the influence of intergranular resolution rate, hydrostatic pressure, and grain-boundary diffusion enhancement factor. The modified mechanistic swelling model is incorporated to perform the finite element (FE) simulation. This mechanistic model demonstrates comparably high efficiency toward the… *(truncated)*

## Physical Mechanisms

*(Inferred from abstract — verify against full text)*

1. **Gaseous swelling in U-Mo fuel** — Fission gas production and accumulation drives volumetric swelling of UMo alloy fuel.
2. **Intergranular fission gas behavior** — Gas atoms migrate to grain boundaries, nucleate and grow bubbles causing intergranular swelling.
3. **Gas resolution** — Re-dissolution of gas atoms from bubbles back into the matrix (intergranular resolution rate is a key parameter).
4. **Hydrostatic pressure effects** — External/mechanical pressure constrains bubble growth.
5. **Grain-boundary diffusion enhancement** — Accelerated diffusion along grain boundaries influences gas bubble coalescence and growth kinetics.

## Key Equations

> ⚠️ **Note**: PDF was image-based; equations reconstructed from the paper's methodology and related literature (Rest, 2005; Kim, 2013; Jian, 2022) which cite and extend this model.

### 1. Intrangranular Gas Diffusion (Booth-type)

The concentration of fission gas atoms $c_g$ within a grain follows the diffusion equation with production and resolution source terms:

$$\frac{\partial c_g}{\partial t} = \nabla \cdot (D_g \nabla c_g) + \dot{f} y - b \cdot c_b$$

where $D_g$ is the athermal fission gas diffusivity, $\dot{f}$ is the fission rate density, $y$ is the fission gas yield per fission, $b$ is the resolution rate, and $c_b$ is the concentration of gas atoms in bubbles.

### 2. Intergranular Bubble Growth

The growth rate of intergranular bubbles is governed by the balance between gas atom absorption and resolution:

$$\frac{dn_b}{dt} = D_{gb} \cdot c_g^{gb} \cdot S_{gb} - b_i \cdot n_b$$

where $n_b$ is the number of gas atoms in grain-boundary bubbles, $D_{gb}$ is the grain-boundary diffusivity (enhanced by factor $f_{enh}$), $c_g^{gb}$ is the gas concentration at the grain boundary, and $S_{gb}$ is the grain-boundary sink strength.

### 3. Hydrostatic Pressure Effect on Bubble Equilibrium

The equilibrium bubble radius under hydrostatic pressure $P_{ext}$:

$$r_{eq} = \frac{2\gamma}{P_{gas} - P_{ext}}$$

where $\gamma$ is the surface energy and $P_{gas} = nk_BT / (\frac{4}{3}\pi r^3)$ is the internal gas pressure from the ideal gas law.

### 4. Gaseous Swelling Strain

$$\epsilon_{gas} = \frac{\Delta V}{V} = \frac{4}{3}\pi r_b^3 \cdot N_b$$

where $r_b$ is the average bubble radius and $N_b$ is the bubble number density per unit volume.

### 5. Grain-Boundary Diffusion Enhancement

$$D_{gb}^{eff} = f_{enh} \cdot D_{gb}^{0} \cdot \exp\left(-\frac{Q_{gb}}{k_B T}\right)$$

where $f_{enh}$ is the grain-boundary diffusion enhancement factor (key parameter studied), $D_{gb}^{0}$ is the pre-exponential, and $Q_{gb}$ is the activation energy for grain-boundary diffusion.

### 6. FE Coupling

The volumetric swelling strain enters the mechanical equilibrium as a thermal-expansion-like eigenstrain:

$$\boldsymbol{\epsilon}^{swell} = \frac{1}{3}\epsilon_{gas} \mathbf{I}$$

This is coupled with irradiation creep and constitutive laws in the FE framework.

## Parameters

| Parameter | Description | Notes |
|-----------|-------------|-------|
| Intergranular resolution rate | Rate of gas atom re-dissolution from grain-boundary bubbles | Parametric study performed |
| Hydrostatic pressure | Mechanical pressure acting on fuel matrix | Parametric study performed |
| Grain-boundary diffusion enhancement factor | Multiplier for diffusion rate along grain boundaries | Parametric study performed |

*(Quantitative values require manual extraction from PDF)*

## Experimental Data

⚠️ No experimental data extractable from image-based PDF. The paper appears to focus on **model modifications and finite element simulation** rather than new experimental results. Specific validation cases and comparison data must be extracted manually.

## Key Findings

*(Inferred from abstract)*

1. **Computational efficiency** — Analytical expressions significantly reduce computation cost compared to original model.
2. **Parametric sensitivity** — Intergranular resolution rate, hydrostatic pressure, and grain-boundary diffusion enhancement factor are key controlling parameters for gaseous swelling.
3. **FE integration** — The modified model was successfully coupled with finite element simulation.
4. **Model performance** — The mechanistic approach demonstrates high efficiency for UMo fuel swelling prediction.

## Relationships to Other Work

- **Extends**: Prior mechanistic gaseous swelling models for UMo fuel (specific references require manual extraction)
- **Application**: U-Mo dispersion or monolithic fuel performance modeling
- **FE framework**: Coupled with finite element fuel performance codes
- **Related topics**: Fission gas release, fuel swelling, UMo alloy fuel behavior

---

*This entry was auto-generated from metadata due to image-based PDF. Manual review and enrichment needed.*

## Relationships

- [[wiki/entities/FuelAlloy|FuelAlloy]] — U-Mo alloy fuel gaseous swelling is the subject
- [[wiki/entities/FissionGasDiffusion|FissionGasDiffusion]] — intergranular resolution rate and grain-boundary diffusion enhancement are key parameters studied
- [[wiki/concepts/SwellingMechanisms|SwellingMechanisms]] — mechanistic gaseous swelling model with FE coupling is the main contribution
- [[wiki/concepts/SwellingModelComparison|SwellingModelComparison]] — provides an analytical/FE mechanistic model for comparison with empirical correlations
- [[wiki/summaries/2011_Kim_FissionProductInducedSwellingUMo|2011_Kim_FissionProductInducedSwellingUMo]] — empirical swelling correlations that this mechanistic model extends or replaces
- [[wiki/summaries/2013_Kim_RecrystallizationFGBSwellingUMo|2013_Kim_RecrystallizationFGBSwellingUMo]] — recrystallization-driven swelling model is complementary
- [[wiki/summaries/2022_Jian_FissionGasSwellingModelU10Mo|2022_Jian_FissionGasSwellingModelU10Mo]] — later mechanistic fission gas swelling model for U-10Mo with similar scope
