# Swelling Behavior of U-Pu-Zr Fuel

## Metadata
- **Title**: Swelling Behavior of U-Pu-Zr Fuel
- **Authors**: Gerard L. Hofman, R.G. Pahl, C.E. Lahm, D.L. Porter
- **Year**: 1990
- **Journal**: Metallurgical Transactions A, Vol. 21A, March 1990, pp. 517-528
- **DOI**: 10.1007/BF02671924
- **Affiliation**: Argonne National Laboratory, EBR-II Division
- **Key context**: IFR (Integral Fast Reactor) fuel development program

## Physical Mechanisms

### Primary Swelling Mechanism
- **Fission gas bubble nucleation and growth** of insoluble Xe and Kr is the universal swelling mechanism
- Metallic fuels (like U-Pu-Zr) exhibit **high fission-gas-induced swelling** due to high thermal conductivity
- Intragranular fission-gas bubbles are largely immobile; intergranular bubbles grow larger via gas diffusion to grain boundaries
- At sufficient burnup, intergranular bubbles interconnect → fission gas release

### Additional Mechanisms in Metallic Fuels
1. **Irradiation growth of α-uranium phase**: Anisotropic shape change — (010) elongation + (100) shrinkage, caused by anisotropic condensation of interstitial and vacancy loops
2. **Fission-enhanced creep**: High creep rate in metallic fuel contributes to rapid pre-contact swelling
3. **Grain boundary tearing**: In α-U phase, microtears form at twin boundaries from martensitic transformation, exacerbated by anisotropic thermal expansion
4. **Solid fission product swelling**: At high burnup, rare earth elements (Ce, Nd, Pr, La) migrate to fuel periphery and fill fission-gas pores; fuel-soluble metallic FPs decrease alloy density

### Anisotropic Swelling
- Radial swelling > axial swelling consistently observed
- Caused by:
  - Radial temperature gradient → distinct microstructural zones with different swelling rates
  - Hotter center (γ phase, isotropic swelling) exerts radial stress on cooler outer shell
  - Outer shell (α phase) responds anisotropically with higher circumferential strain
  - Circumferential tensile stress ≈ 2× axial tensile stress in outer zone

### Phase-Dependent Swelling
| Phase | Temperature Range | Swelling Character |
|-------|------------------|-------------------|
| α (orthorhombic) | <617°C | Grain boundary tearing, highly anisotropic |
| α + δ | <617°C | Fine two-phase, some pores on δ phase |
| α + γ₂ | 617-662°C | Mixed: tearing at α GB + bubble growth in γ₂ lamellae |
| γ (cubic) | >662°C | Large interconnected gas bubbles, isotropic, high plasticity |

## Key Equations

*(This paper is primarily descriptive/observational; the following are reconstructed key relationships from the reported data and physical mechanisms described.)*

### Total Fuel Swelling

$$\frac{\Delta V}{V} = \left(\frac{\Delta V}{V}\right)_{\text{gas}} + \left(\frac{\Delta V}{V}\right)_{\text{solid FP}} + \left(\frac{\Delta V}{V}\right)_{\text{irradiation growth}}$$

where solid fission product (rare earth) swelling and anisotropic irradiation growth of $\alpha$-U are additive to gas-driven swelling.

### Gas Bubble-Driven Swelling

$$\left(\frac{\Delta V}{V}\right)_{\text{gas}} = \frac{4}{3}\pi N_b \langle r^3 \rangle$$

where $N_b$ is the bubble number density and $\langle r^3 \rangle$ is the mean cube bubble radius.

### Irradiation Growth of $\alpha$-Uranium

$$\frac{\Delta L}{L_0} = G_1 (010) \cdot f + G_2 (100) \cdot f$$

where $G_1 > 0$ (elongation along $[010]$) and $G_2 < 0$ (shrinkage along $[100]$), $f$ is fission density. The anisotropy ratio $\Delta D / \Delta L \approx 2$–$4$ was observed.

### Swelling vs. Burnup (Characteristic Curve)

$$\frac{\Delta V}{V}(b) = \begin{cases} 0 & b < b_{\text{incubation}} \approx 0.3\,\text{at.\%} \\ \text{rapid increase} & b_{\text{incubation}} < b < b_{\text{contact}} \approx 1\,\text{at.\%} \\ \text{mechanically restrained} & b > b_{\text{contact}} \end{cases}$$

### Incubation Burnup

$$b_{\text{incubation}} \approx 0.3\,\text{at.\%} \quad \text{(onset of rapid swelling)}$$

### Key Observations (Quantitative)

| Metric | Value |
|--------|-------|
| Axial swelling at 4.5 at.% burnup | 6–9% (composition dependent) |
| Anisotropy ratio ($\Delta D / \Delta L$) | 2–4× (Pu dependent) |
| Peak diametral swelling rate | ~16%/at.% (pre-contact) |
| Fuel-cladding contact burnup | ~1 at.% (B elements, 0.230") |

## Parameters

### Fuel Compositions Studied
- U-xPu-10Zr with x = 0, 3, 8, 19, 22, 26 wt% Pu
- Two cladding diameters: 0.230" (B elements) and 0.290" (A elements)

### Operating Conditions
| Parameter | A Elements (0.290") | B Elements (0.230") |
|-----------|-------------------|-------------------|
| Peak centerline T | 610°C | 610°C |
| Radial ΔT | 130°C | 130°C |
| Radial T gradient | 1160°C | 1520°C |
| Peak U-235 fission rate | 4.5×10¹³ f/cm³·s | 8.8×10¹³ f/cm³·s |
| Planar smeared density | ~75% | ~75% |

### Incubation Burnup
- **~0.3 at.%** incubation burnup before rapid swelling onset
- Rapid swelling over ~1 at.% burnup interval
- Fuel-cladding contact at **~1 at.%** burnup for B elements

## Experimental Data

### Axial Swelling vs Burnup (A elements, Figure 1)
- 0% Pu: Highest axial growth, reaching ~9% at ~4.5 at.% burnup
- 3-26% Pu: Similar behavior, axial growth 6-8% at ~4.5 at.%
- Leveling off due to fuel-cladding contact

### Anisotropy Ratio (Figure 2)
- 0% Pu: Highly anisotropic (diametral >> axial)
- 3% Pu: Maximum anisotropy
- 8% Pu: High anisotropy
- 19% Pu: Lower anisotropy (less α phase)
- 22-26% Pu: Further reduced anisotropy

### Contact Swelling
- 75% smeared density → contact at ~16% diametral swelling (isotropic theory)
- Actual: 0.230" B elements contact at ~1 at.% with only ~3% axial swelling
- Indicates extreme anisotropy (radial >> axial)

### Temperature Dependence of Diametral Swelling (Figure 11)
- All compositions show swelling decrease at higher surface temperatures (where α is absent)
- Highest Pu alloys show singular swelling mode (no α phase contribution)

### Non-Gaseous Fission Product Effects (at high burnup)
1. **Na-solubles** (Cs): migrate to bond sodium, no swelling contribution
2. **Fuel-soluble metals**: dissolve in alloy, decrease density
3. **Rare earths** (Ce, Nd, Pr, La): precipitate in pores at periphery, contribute to swelling

## Key Findings

1. **Rapid, anisotropic swelling** prior to fuel-cladding contact is the dominant behavior
2. **Three-zone microstructure** develops due to radial temperature gradient, each with distinct swelling properties
3. **Pu content effect**: Increases swelling rate and anisotropy at low Pu (3-8%), but reduces anisotropy at high Pu (19+%) due to α phase suppression
4. **Early redistribution** of U and Zr in high-Pu, high-fission-rate fuels creates a third intermediate zone with unique swelling behavior
5. **Peripheral zone cracking** occurs in fuels with early redistribution, further increasing anisotropy
6. **γ phase regions** swell isotropically with large interconnected gas bubbles and high plasticity
7. **α phase regions** swell anisotropically via grain boundary tearing
8. Fuel-cladding contact occurs at very low burnup (~1 at.%), after which swelling is mechanically restrained

## Relationships to Other Work

- **Rest 1993**: Builds on this work by developing mechanistic void swelling model for α-U phase based on single-vacancy/single-interstitial kinetics
- **Rest 2001 (GRSIS)**: Incorporates Hofman's observations into comprehensive fission gas release and swelling model (GRSIS)
- **Hofman's earlier work**: Referenced Kittel & Paine (1958) for α-U irradiation growth, Buckley (1962, 1966) for loop formation mechanisms
- **Phase diagram basis**: Uses U-Zr and U-Pu-Zr equilibrium phase diagrams for interpreting microstructural zones
- **Connection to U-Mo fuels**: The α-phase tearing mechanism described here is analogous to intergranular cracking observed in U-10Mo (Willard 1985)

## Relationships

- [[wiki/entities/FuelAlloy|FuelAlloy]] — U-Pu-Zr metallic fuel alloy swelling behavior and phase-dependent microstructure are the core subject
- [[wiki/concepts/SwellingMechanisms|SwellingMechanisms]] — anisotropic swelling, grain boundary tearing, fission gas bubble growth, and creep are all described
- [[wiki/entities/FissionGasDiffusion|FissionGasDiffusion]] — intragranular and intergranular fission gas bubble nucleation and growth are central mechanisms
- [[wiki/entities/CavitationalVoid|CavitationalVoid]] — grain boundary tearing in α-U phase leads to cavity/void formation described in Rest (1992, 1993)
- [[wiki/summaries/1992_Rest_CavitationalSwellingAlphaUPuZr|1992_Rest_CavitationalSwellingAlphaUPuZr]] — Rest directly builds the cavitational model on Hofman's α-U phase observations
- [[wiki/summaries/2001_Rest_GRSIS_FissionGasMetallic|2001_Rest_GRSIS_FissionGasMetallic]] — GRSIS integrates Hofman's observations into a comprehensive metallic fuel swelling model
- [[wiki/concepts/SwellingModelComparison|SwellingModelComparison]] — this paper motivates development of competing swelling models (gas-bubble vs. cavitational)
