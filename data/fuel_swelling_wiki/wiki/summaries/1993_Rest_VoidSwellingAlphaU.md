# Kinetics of Fission-Gas-Bubble-Nucleated Void Swelling of the Alpha-Uranium Phase (1993, Rest)

## Metadata
- **Journal**: Journal of Nuclear Materials, 207, 192–204 (1993)
- **DOI**: 10.1016/0022-3115(93)90261-V
- **Author**: J. Rest (Argonne National Laboratory)
- **Material System**: U-Zr, U-Pu-Zr (U-10Zr, U-19Pu-10Zr specifically)
- **Method**: Rate-theory (Cavity code)
- **Key Topic**: Cavitational void swelling of α-uranium phase

## Physical Mechanisms

1. **Cavitational void swelling** identified as major swelling mechanism in α-U phase of irradiated U-Zr and U-Pu-Zr metallic fuels for the Integral Fast Reactor (IFR).
2. **Gas-bubble-nucleated void growth**: Gas bubbles formed on α/δ phase boundaries during incubation period serve as void nuclei. When they exceed critical radius, cavities grow by bias-driven net vacancy influx (void swelling).
3. **Bias-driven growth mechanism**: Dislocations preferentially absorb interstitials → net vacancy excess → vacancy flux to cavities drives growth. This is distinct from gas-driven swelling (overpressurized bubbles).
4. **Transition from gas-driven to bias-driven growth**: Monitored by tracking excess pressure Pex = Pg - 2γ/Rc - σ:
   - Pex > 0 and dRc/dt > 0: Gas-driven (overpressurized bubble)
   - Pex < 0 and dRc/dt > 0: Bias-driven (underpressurized void)
5. **Reduced gas-bubble nucleation on phase boundaries**: α/δ phase boundary lamellae are less efficient gas-bubble incubators than normal high-angle grain boundaries → explains long incubation times observed in IFR fuels.
6. **Cavity interconnection**: When areal coverage of phase boundaries by cavities reaches threshold, interconnection occurs → gas release pathway to free surfaces.
7. **No intragranular cavity growth**: Irradiation-induced gas atom re-solution prevents intragranular bubbles from reaching critical size → only boundary bubbles grow to critical size.

## Key Equations & Parameters

### Gas Evolution in Bulk (α-U Lamina)

$$\frac{dC_{gb}}{dt} = -\frac{16\pi F_b R_b^2 D_{gb} C_b^2}{C_b} - 4\pi R_b^2 D_{gb} C_g C_b - j_g(t) + \beta f + BC_b C_{gb} \quad \text{(Eq. 1)}$$

Terms: bubble nucleation, gas diffusion to cavities, gas diffusion to phase boundaries, fission gas generation, gas atom re-solution.

### Gas Evolution on Phase Boundaries

$$\frac{dC_{gf}}{dt} = -\frac{16\pi F_f R_f^2 D_{gf} C_f^2}{C_f} - 4\pi R_f D_{gf} C_f C_f + j_g(t) - \dot{r}_{gf} \quad \text{(Eq. 6)}$$

### Cavity Growth Rate (Net Vacancy Flux)

$$\frac{dR_c}{dt} = \frac{\Omega}{4\pi R_c^2} \left[k_{vc} D_v C_v - k_{i,c} D_i C_i - k_{vc} D_v C_{v0}(R_c)\right] C_c \quad \text{(Eq. 14)}$$

### Thermal Vacancy Concentration Near Cavity

$$C_{v0}(R_c) = C_{v0} \exp\left[-\frac{(P_g - 2\gamma/R_c - \sigma)\Omega}{kT}\right] \quad \text{(Eq. 15)}$$

### Point Defect Rate Equations

$$\frac{dC_v}{dt} = \frac{1}{2}K_f - k_v^2 D_v C_v - \alpha C_v C_i \quad \text{(Eq. 17)}$$

$$\frac{dC_i}{dt} = \frac{1}{2}K_f - k_i^2 D_i C_i - \alpha C_v C_i \quad \text{(Eq. 18)}$$

### Sink Strengths
- **Cavities:** $k_{vc} = 4\pi R_c C_c[1 + kR_c]$ (Eq. 21)
- **Dislocations:** $k_{vd} = Z_{vd}\rho$, $k_{id} = Z_{id}\rho$ (Eqs. 23–24)

### Cavity Interlinkage

$$A_c = \pi R_c^2 C_c \times f(R_c) \quad \text{(Eq. 10)}$$

Interlinkage when $A_c \geq A_T^{1/2}$ (Eq. 11), with distribution width $\sigma_f$ for local microstructure variations.

### Table 1: Material Constants
| Parameter | Value | Reference |
|-----------|-------|-----------|
| Pre-exponential vacancy diffusivity (Dv0) | 2.0 × 10⁻⁸ m²/s | [8] |
| **Vacancy migration energy (Em)** | **1.28 eV** | [13] |
| Vacancy formation energy (Efv) | 1.6 eV | [9] |
| Dislocation bias for vacancies (Zvd) | 1.0 | [9] |
| Dislocation bias for interstitials (Zid) | 1.025 | [9] |
| Surface energy (γ) | 0.5 J/m² | Present calculation |
| Recombination volume radius (riv) | 2 × 10⁻¹⁰ m | [14] |
| Dislocation density (ρ) | 7 × 10¹³ m⁻² (U-10Zr), 2 × 10¹³ m⁻² (U-19Pu-10Zr) | Present calc. |
| Bubble nucleation factor (bulk, Fb) | 1 × 10⁻⁵ | [8] |
| **Bubble nucleation factor (phase boundary, Ff)** | **1 × 10⁻⁵** | Present calc. |
| Atomic volume (Ω) | 4.09 × 10⁻²⁹ m³ | [8] |

## Experimental Data

### U-10Zr (EBR-II, Assembly X423)
- **Swelling**: Rapid increase after ~0.2 at.% burnup incubation, reaching ~50% volumetric swelling at 1.2 at.% burnup
- **Gas release**: Begins at ~0.6 at.% burnup, rises rapidly to ~70% at ~1.2 at.% burnup
- **Dislocation density**: ρ = 7 × 10¹³ m⁻²

### U-19Pu-10Zr (EBR-II, Assembly X423)
- **Lower swelling** than U-10Zr due to lower dislocation density (ρ = 2 × 10¹³ m⁻²)
- **Same incubation behavior** but lower total swelling

### High-Purity Uranium
- **Swelling vs. temperature**: Bell-shaped curve with peak at ~673 K
- **Considerable scatter** in experimental data
- **Swelling decreases above peak** due to increased vacancy emission

## Model Description

1. **Cavity code**: Complete mechanistic model (Eqs. 1–24) for gas-bubble-nucleated cavitational void swelling.
2. **Two-region treatment**: Bulk (α-U lamina) and phase boundary regions treated separately.
3. **Gas atom tracking**: Full accounting of gas atom generation, diffusion, nucleation, re-solution, and release.
4. **Point defect kinetics**: Vacancy and interstitial concentrations determined from rate equations with production, sink absorption, and recombination terms.
5. **Critical radius criterion**: Cavity growth transitions from gas-driven to bias-driven when Rc exceeds critical value.
6. **Cavity interlinkage**: Based on areal coverage of phase boundaries + distribution width for microstructural heterogeneity.
7. **FEA coupling**: Temperature and power history from LIFE-FETE calculations used as input.

## Key Findings

1. **Cavitational void swelling is the primary mechanism** in α-U phase, not gas-bubble-driven swelling.
2. **Long incubation times** (hundreds of dpa vs. 10–20 dpa in pure metals) explained by reduced gas-bubble nucleation efficiency on α/δ phase boundaries (Ff = 10⁻⁵).
3. **Dislocation density is key**: U-19Pu-10Zr has lower dislocation density → lower swelling than U-10Zr. This explains composition-dependent swelling behavior.
4. **Model predicts both gas-driven and bias-driven swelling** and the transition between them.
5. **Good agreement with EBR-II data** for both U-10Zr and U-19Pu-10Zr fuel elements.
6. **Swelling vs. temperature**: Bell-shaped curve with peak, consistent with void swelling in structural metals.
7. **Hydrostatic stress from cladding** inhibits further swelling after gap closure (via Eq. 15).
8. **Comparison with pure uranium data**: Model captures the temperature dependence of swelling in high-purity U.

## Relevance to JSRT Model

- **Core reference for JSRT**: This is Rest's definitive 1993 paper on cavitational void swelling — the theoretical foundation of JSRT.
- **Complete constitutive model**: Eqs. 1–24 provide the full mathematical framework that JSRT should implement.
- **Critical parameters**: Vacancy migration energy (1.28 eV — note Yun 2022 revised to 0.34 eV), surface energy (0.5 J/m²), nucleation factors (Fb = Ff = 10⁻⁵).
- **Dislocation density effect**: Lower dislocation density in Pu-containing fuel → lower swelling — JSRT must account for composition-dependent dislocation density.
- **Two-region treatment**: Bulk vs. phase boundary treatment provides a template for spatially-resolved JSRT modeling.
- **Transition criterion**: Pex tracking (gas-driven → bias-driven) should be incorporated in JSRT.
- **Interlinkage model**: Areal coverage + distribution width provides a practical gas release criterion.
- **Validation data**: EBR-II X423 data for U-10Zr and U-19Pu-10Zr, plus pure U data, provide comprehensive validation benchmarks.

## Relationships

- [[wiki/entities/CavitationalVoid|CavitationalVoid]] — this is the definitive paper on gas-bubble-nucleated cavitational void swelling in α-U phase
- [[wiki/concepts/RateTheoryFramework|RateTheoryFramework]] — the full rate-theory constitutive model (Eqs. 1–24) is the core contribution
- [[wiki/entities/FuelAlloy|FuelAlloy]] — U-Zr and U-Pu-Zr metallic fuel alloys in EBR-II are the subject materials
- [[wiki/entities/FissionGasDiffusion|FissionGasDiffusion]] — gas atom diffusion, re-solution, and bubble growth on phase boundaries are key processes
- [[wiki/summaries/1992_Rest_CavitationalSwellingAlphaUPuZr|1992_Rest_CavitationalSwellingAlphaUPuZr]] — the 1992 conference precursor with original parameter set
- [[wiki/summaries/2022_Yun_CavitationalVoidSwelling|2022_Yun_CavitationalVoidSwelling]] — Yun (2022) revisits and revises key parameters from this model
- [[wiki/concepts/SwellingModelComparison|SwellingModelComparison]] — this model is one pole in the debate between cavitational vs. gas-bubble-driven swelling

## Related Work
- [[wiki/summaries/1992_Rest_CavitationalSwellingAlphaUPuZr|1992_Rest_CavitationalSwellingAlphaUPuZr]] — 本文的会议论文前驱版本，包含原始参数集
- [[wiki/summaries/1990_Hofman_SwellingBehaviorUPuZr|1990_Hofman_SwellingBehaviorUPuZr]] — Hofman 的实验观察为本文 α-U 空腔肿胀模型提供了经验基础
- [[wiki/summaries/2022_Qian_CavitationalVoidSwellingU10Zr|2022_Qian_CavitationalVoidSwellingU10Zr]] — Qian (2022) 修订了本文的关键参数（空位迁移能）并重新验证
- [[wiki/summaries/2001_Fission_gas_release_swelling_model_metallic_fuel|2001_Fission_gas_release_swelling_model_metallic_fuel]] — GRSIS 代表了与本文空腔肿胀模型竞争的气泡驱动肿胀学派
- [[wiki/entities/CavitationalVoid|CavitationalVoid]] — 气泡形核空腔肿胀是本文的核心贡献
- [[wiki/concepts/SwellingModelComparison|SwellingModelComparison]] — 本文是空腔肿胀 vs. 气泡肿胀模型辩论的核心文献之一
