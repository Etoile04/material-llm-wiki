# Models for Effective Elastic Constants of Irradiated U-10Mo Fuels with Distributed Fission Gas Bubbles

## Metadata

| Field | Value |
|-------|-------|
| **Authors** | Yong Li, Guochen Ding, Zhexiao Xie, Jing Zhang, Xiaobin Jian, **Shurong Ding** (corresponding), Yuanming Li |
| **Affiliation** | Fudan University (Institute of Mechanics and Computational Engineering); Nuclear Power Institute of China |
| **Journal** | Journal of Nuclear Materials |
| **Year** | 2023 |
| **Volume/Pages** | 579, 154359 |
| **DOI** | 10.1016/j.jnucmat.2023.154359 |
| **Keywords** | Irradiated U-10Mo fuels, Fission gas bubbles, Recrystallization, Effective elastic constants, Homogenization theory, Numerical simulation |

---

## Physical Mechanisms

### Fission Gas Bubble (FGB) Formation and Distribution
- Fission gas atoms generated during irradiation diffuse toward grain boundaries, forming **inter-granular FGBs** (0.1–1 μm diameter)
- **Intra-granular FGBs** form ordered nano-bubble FCC superlattice in BCC U-Mo matrix (2–6 nm diameter, 4–12 nm spacing)
- Intra-granular nm-bubbles treated as solid precipitates (negligible effect on elastic constants)

### Grain Recrystallization
- Recrystallization occurs at intermediate fission densities
- Original large grains subdivide into fine grains, starting near grain boundaries and propagating inward
- Creates two distinct regions during recrystallization:
  - **Bubble-contained region** (outer, contains FGBs)
  - **No-bubble region** (inner, grain interior)
- Recrystallization accelerates FGB formation by increasing grain boundary density and shortening gas diffusion paths

### Porosity Effect on Elastic Properties
- FGBs convert U-10Mo to porous structure, degrading thermo-mechanical properties
- Effective elastic constants depend on **macroscopic porosity** (volume-averaged over fuel), not local porosity distribution
- Bubble pressure has negligible effect on effective elastic constants (<1% variation)

---

## Key Equations & Parameters

### Material Properties of Unirradiated U-10Mo Skeleton

| Property | Value | Source |
|----------|-------|--------|
| Young's modulus E | 85,000 MPa (85 GPa) | Kim et al. 2013 [7] |
| Poisson's ratio ν | 0.34 | Kim et al. 2013 [7] |

### Porosity Definitions

- **Local porosity** (bubble-contained region): f_bc = V_bubbles / V_bubble-contained-region
- **Macroscopic porosity**: f_bm = η_bc × f_bc, where η_bc = volume fraction of bubble-contained region

### Effective Bulk Modulus (Degenerated Mori-Tanaka)

$$\bar{K} = K \left[1 - \frac{f_{bm}}{1 - \frac{1+\nu}{3(1-\nu)}(1-f_{bm})}\right]$$

where α = (1+ν) / [3(1-ν)]

### Effective Shear Modulus (Degenerated Mori-Tanaka)

$$\bar{G} = G \left[1 - \frac{f_{bm}}{1 - \frac{2(4-5\nu)}{15(1-\nu)}(1-f_{bm})}\right]$$

where β = 2(4-5ν) / [15(1-ν)]

### Effective Young's Modulus and Poisson's Ratio

$$\bar{E} = \frac{3E(1-f_{bm})}{2(1+\nu)(1+b_g f_{bm}) + (1-2\nu)(1+b_k f_{bm})}$$

$$\bar{\nu} = \frac{(1+\nu)(1+b_g f_{bm}) - (1-2\nu)(1+b_k f_{bm})}{2(1+\nu)(1+b_g f_{bm}) + (1-2\nu)(1+b_k f_{bm})}$$

where:
- b_k = (1+ν) / [2(1-2ν)]
- b_g = (8-10ν) / (7-5ν)

### Modified Van der Waals Gas Law (Bubble Pressure)

$$P_b(V - h_s b_v N) = NkT$$

| Parameter | Value |
|-----------|-------|
| k (Boltzmann constant) | 1.38 × 10⁻²³ J/K |
| h_s (fitting parameter) | 0.6 |
| b_v (Van der Waals constant for Xe) | 8.5 × 10⁻²⁹ m³/atom |

### Key Coefficients for ν = 0.34

- α = (1+0.34) / [3×0.66] = 0.677
- β = 2(4-5×0.34) / [15×0.66] = 2×2.3/9.9 = 0.465
- b_k = 1.34 / [2×0.32] = 2.094
- b_g = (8-3.4) / (7-1.7) = 4.6/5.3 = 0.868

---

## Experimental Data

### L1P773 Irradiated U-10Mo Fuel (Schulthess & Lloyd et al. [3])

| Property | Measured Values | Conditions |
|----------|----------------|------------|
| Effective Young's modulus | 57, 64, 65 GPa (different locations) | Fission density: 3.3–3.4 × 10²⁷ fissions/m³ |
| Reported porosity | 13.7% | L1P773, location-averaged |
| Unirradiated Young's modulus | ~85 GPa | Reference value |

### Model Validation
- At f_bm = 13.7%: Model predicts Ē = 64.5 GPa (matches 64 and 65 GPa measurements)
- Specimen with 57 GPa may have higher local porosity or degraded skeleton properties

### Bubble Pressure Variation Tests (Table B.1)

| f_bc | T (K) | P_b0 (MPa) | V_b/V_b0 | P_b/P_b0 |
|------|-------|------------|-----------|----------|
| 0.10 | 373 | 10 | 0.9923 | 1.0078 |
| 0.25 | 373 | 100 | 0.9907 | 1.0094 |
| 0.10 | 473 | 10 | 0.9923 | 1.0078 |
| 0.25 | 473 | 100 | 0.9907 | 1.0094 |

External hydrostatic pressure: 200 MPa. Conclusion: bubble pressure change < 1%.

---

## Model Description

### Multi-Level Homogenization Framework

1. **First-level homogenization**: Bubble-contained region → isotropic homogeneous material
   - FGBs distributed uniformly/randomly in U-10Mo skeleton
   - Equivalent spherical model (analytical) → bulk modulus
   - Random distribution model (FE simulation, ABAQUS, C3D10 elements, 69,305 elements) → Young's modulus → shear modulus

2. **Second-level homogenization** (during recrystallization only):
   - Homogenized bubble-contained region + no-bubble region → overall isotropic material
   - Same RVE approach with two-phase spherical model

### RVE Models
- **Equivalent spherical model**: Analytical solution for bulk modulus; hollow sphere with FGB core and U-10Mo shell
- **Random distribution model**: 25 FGBs randomly distributed in U-10Mo matrix cube; periodic boundary conditions; FE uniaxial tension

### Comparison Models (Appendix D)

| Model | Type | Notes |
|-------|------|-------|
| Mori-Tanaka | Mean-field | Best agreement with this study (<1.53% difference for Ḡ) |
| Power-law | Empirical | Good agreement for Ḡ |
| Exponential | Empirical | Underestimates at high porosity |
| Dilute | Mean-field | Overestimates at high porosity |
| Ramakrishnan | Semi-empirical | Systematically underestimates; contains pressure amplification error |

---

## Key Findings

1. **Effective elastic constants depend only on macroscopic porosity** f_bm, not on local porosity distribution or bubble pressure
2. **Derived bulk modulus model = degenerated Mori-Tanaka** with zero elastic constants for inclusion (bubble) phase
3. **Bubble pressure negligible**: Pressure variation from elastic deformation < 1%, does not affect elastic constants
4. **Model validated** against L1P773 experimental data: predicted Ē = 64.5 GPa at 13.7% porosity matches measured 64–65 GPa
5. **No energy dissipation** during homogenization of equivalent spherical RVE
6. Ramakrishnan model contains an error: external pressure amplified by 1/(1-f_bm) is incorrect; should use actual external pressure directly

---

## Relevance to JSRT Model

This paper is **highly relevant** to JSRT (Jian et al.) fuel swelling modeling:

1. **Elastic property degradation model**: Provides closed-form equations (Eq. 28–29) linking macroscopic porosity to effective elastic constants — essential for thermo-mechanical coupling simulations
2. **Same research group**: Shurong Ding (corresponding author) is the advisor of Xiaobin Jian (JSRT model developer), ensuring model compatibility
3. **Multi-level homogenization**: Framework directly applicable to JSRT model's treatment of recrystallization stages (bubble-contained vs. no-bubble regions)
4. **Porosity-swelling coupling**: The macroscopic porosity f_bm used here is the output of fission gas swelling models (e.g., Jian et al. 2022 [29], 2023 [36]), creating a direct link between swelling and mechanical property degradation
5. **Practical implementation**: All equations are closed-form with known U-10Mo skeleton parameters (E=85 GPa, ν=0.34), ready for integration into fuel performance codes
6. **Bubble pressure treatment**: Confirms that bubble pressure can be neglected for elastic property calculations, simplifying JSRT model implementation

## Relationships

- [[wiki/entities/FuelAlloy|FuelAlloy]] — U-10Mo fuel thermo-mechanical property degradation from fission gas bubbles is the subject
- [[wiki/entities/Recrystallization|Recrystallization]] — recrystallization creates bubble-contained and no-bubble regions requiring two-level homogenization
- [[wiki/concepts/SwellingMechanisms|SwellingMechanisms]] — macroscopic porosity from fission gas swelling degrades elastic constants
- [[wiki/summaries/2022_Jian_FissionGasSwellingModelU10Mo|2022_Jian_FissionGasSwellingModelU10Mo]] — fission gas swelling model from same group that generates the porosity input for this model
- [[wiki/summaries/2023_Ye_IntegratedSimulationU10Mo|2023_Ye_IntegratedSimulationU10Mo]] — integrated DART simulation that uses these elastic property models

## Related Work
- [[wiki/summaries/2022_Jian_FissionGasSwellingModelU10Mo|2022_Jian_FissionGasSwellingModelU10Mo]] — 同组Jian的裂变气体肿胀模型，本文所需的宏观孔隙率输入
- [[wiki/summaries/2023_Ye_IntegratedSimulationU10Mo|2023_Ye_IntegratedSimulationU10Mo]] — DART集成模拟使用本文的等效弹性常数模型
- [[wiki/summaries/2025_Hanson_StablePredictableSwellingU10Mo|2025_Hanson_StablePredictableSwellingU10Mo]] — 实验验证L1P773燃料的弹性模量数据，为本文提供验证基准
- [[wiki/summaries/2021_Hilty_FissionGasBubblesThermalConductivity|2021_Hilty_FissionGasBubblesThermalConductivity]] — 气泡对热导率的影响，与本文弹性性质退化形成互补的材料性能退化研究
- [[wiki/concepts/SwellingMechanisms|SwellingMechanisms]] — 本文揭示了孔隙率→弹性性质退化的定量关系，是肿胀-力学耦合的核心环节
