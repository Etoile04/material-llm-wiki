# Investigation of Swelling Behaviors of U-10Zr Metallic Fuel in the Low Temperature Regime via a Cavitational Void Swelling Model (2022, Qian, Xie, Fu, Yun et al.)

## Metadata
- **Journal**: Journal of Nuclear Materials, 564, 153665 (2022)
- **DOI**: 10.1016/j.jnucmat.2022.153665
- **Authors**: Zhengyu Qian, Xin Xie, Yingjie Fu, Di Yun*, Wenbo Liu, Xiankun Liu, Qijie Feng, Haibing Guo, Yong Sun, Wei Zhou, Xinfu He, Jinli Cao, Wenjie Li
- **Material System**: U-10Zr
- **Method**: Rate-theory / cavitational void swelling model + FEA (COMSOL)
- **Key Topic**: Void swelling in low temperature regime (400–600 K)

## Physical Mechanisms

1. **Cavitational void swelling** in α-U phase: Gas bubbles nucleate on grain/phase boundaries, and when they exceed a critical size, they transform into cavities that grow by bias-driven net vacancy influx.
2. **Two competing mechanisms**:
   - Gas-bubble-driven swelling (overpressurized cavities) — dominant in γ-U phase
   - Bias-driven void swelling (underpressurized cavities) — dominant in α-U phase
3. **Transition criterion**: When cavity radius exceeds critical radius rc, growth transitions from gas-driven to bias-driven (cavitational void swelling).
4. **Low-temperature mechanism**: At 400–600 K, fission gas atoms have low diffusivity, so traditional gas-bubble growth kinetics cannot explain observed ~12% swelling. Cavitational void swelling with lower vacancy migration energy provides the explanation.
5. **Hydrostatic stress analysis**: COMSOL FEA shows hydrostatic stress of 60–130 MPa (compressive), much higher than the ~2.3 MPa estimated from equilibrium gas bubble assumption → structures are cavities, not equilibrium gas bubbles.

## Key Equations & Parameters

### Key Parameters (Low Temperature Regime)
| Parameter | Value | Source |
|-----------|-------|--------|
| Pre-exponential factor for vacancy diffusion | 1.0 × 10⁻⁷ cm²/s | This work |
| Migration energy for vacancy diffusion | **0.34 eV** | DFT (Huang & Wirth 2011) |
| Formation energy for vacancy | 1.77 eV | This work (VASP) |
| Pre-exponential factor for interstitial diffusion | 1 × 10⁻⁴ cm²/s | This work |
| Migration energy for interstitial diffusion | 0.19 eV | DFT |
| Pre-exponential factor for fission gas diffusion | 1.2 × 10⁻³ cm²/s | Ogata et al. 1996 |
| Migration energy for fission gas diffusion | 1.16 eV | Ogata et al. 1996 |
| Dislocation density | 7 × 10⁹ cm⁻² | Rest 1993 |
| Bubble nucleation factor (bulk & boundaries) | 1 × 10⁻⁵ | Rest 1993 |
| Grain size | 1 × 10⁻³ cm | This work (TEM estimate) |
| Surface energy of U-10Zr | 0.5 J/m² | Rest 1993 |

### Key Equations

#### Cavity Growth Rate (Rest 1993, Eq. 1)

$$\frac{dR_c}{dt} = \frac{\Omega}{4\pi R_c^2} \left[ Z_c D_v C_v - Z_v D_i C_i - Z_v D_v C_{v0}(R_c) \right]$$

where:
- $R_c$: cavity radius
- $\Omega$: atomic volume
- $Z_c, Z_v$: cavity and dislocation bias factors
- $D_v, D_i$: vacancy and interstitial diffusion coefficients
- $C_v, C_i$: bulk vacancy and interstitial concentrations
- $C_{v0}(R_c)$: vacancy concentration at cavity surface (depends on gas pressure and surface tension)

#### Critical Radius

Setting $dR_c/dt = 0$ and solving for $R_c = r_c$:

$$r_c: \quad Z_c D_v C_v = Z_v D_i C_i + Z_v D_v C_{v0}(r_c)$$

For $R_c > r_c$: net vacancy influx → bias-driven void growth (cavitational swelling)
For $R_c < r_c$: gas pressure driven growth (overpressurized bubble)

#### Vacancy Diffusion Coefficient

$$D_v = D_{v0} \exp\left(-\frac{E_m^v}{k_B T}\right)$$

With $E_m^v = 0.34$ eV (this work, DFT) vs. Rest's original 1.28 eV, vacancy diffusivity is 3–4 orders of magnitude higher at 500–600 K.

#### Interstitial Diffusion Coefficient

$$D_i = D_{i0} \exp\left(-\frac{E_m^i}{k_B T}\right)$$

where $E_m^i = 0.19$ eV.

#### Vacancy Concentration at Cavity Surface

$$C_{v0}(R_c) = C_v^e \exp\left(\frac{2\gamma}{R_c} \cdot \frac{\Omega}{k_B T}\right) \exp\left(-\frac{P_{\text{gas}} \Omega}{k_B T}\right)$$

where $C_v^e$ is the thermal equilibrium vacancy concentration, $\gamma = 0.5$ J/m² is the surface energy, and $P_{\text{gas}}$ is the gas pressure inside the cavity.

### Key Parameters (High Temperature Regime, γ-U)
| Parameter | Value |
|-----------|-------|
| Irradiation-enhanced bubble diffusivity | 1 × 10⁻²⁹ cm²/s |
| Gas bubble re-solution constant | 1 × 10⁻¹⁸ cm³ |
| Grain size (γ zone) | 5 × 10⁻³ cm |
| Phase boundary temperature | 903 K |

## Experimental Data

### Low Temperature Regime (This Work)
- **Fuel**: U-10Zr slugs, 5 mm × 15 mm cylinders
- **Irradiation**: CMRR pool-type research reactor
- **Burnup**: 0.55–0.7 at.%
- **Temperature range**: 450 K (outer) to 560 K (center)
- **Volumetric swelling**: ~12% at 0.55 at.% burnup
- **Cavity observations**: Average diameter ~3 μm (mean 2.98 μm, σ = 0.988 μm, n = 1328), number density ~8 × 10⁹ cavities/cm³

### High Temperature Regime (EBR-II, X423 Assembly)
- **Fuel**: U-10Zr, 343 mm × 5.66 mm diameter
- **Temperature**: 800–1000 K
- **Swelling**: ~10% at 0.4 at.% burnup, ~25% at 0.65 at.% burnup
- **Fission gas release**: Incubation at ~0.65 at.%, rapid rise to ~70%

## Model Description

1. **Two-zone model**: Fuel divided into α-U zone (cavitational void swelling) and γ-U zone (gas bubble growth kinetics), with phase boundary at 903 K.
2. **FEA thermal-mechanical analysis** (COMSOL): Calculates temperature distribution and hydrostatic stress to verify cavity nature of observed spherical structures.
3. **Rate theory code**: Based on Rest's cavitational void swelling model (1993), modified with DFT-calculated vacancy migration energy of 0.34 eV.
4. **Validation**: Model captures swelling at both low (400–600 K) and high (800–1000 K) temperature regimes with a single consistent parameter set.

## Key Findings

1. **Spherical structures in low-T fuel are cavities**, not equilibrium gas bubbles (confirmed by hydrostatic stress analysis showing 60–130 MPa vs. ~2.3 MPa needed for equilibrium).
2. **Lower vacancy migration energy (0.34 eV)** is the key to explaining observed swelling at low temperatures — this is 3–4 orders of magnitude higher vacancy diffusivity at 500–600 K compared to Rest's original model.
3. **Bubble growth kinetics cannot explain** low-temperature swelling: even with artificially raised gas diffusion coefficient (6 orders of magnitude), only 10% swelling achieved.
4. **Cavitational void swelling model** with modified parameters successfully predicts swelling at both temperature regimes.
5. **Swelling vs. temperature curve** shows bell-shaped behavior with peak, consistent with void swelling in structural metals.
6. **Fission gas release** at high temperature shows incubation period (~0.65 at.% burnup) followed by rapid rise to ~70%, consistent with EBR-II observations.

## Relevance to JSRT Model

- **Directly relevant**: This paper builds on Rest's cavitational void swelling framework (the theoretical basis for JSRT).
- **Critical parameter revision**: The vacancy migration energy of 0.34 eV (vs. Rest's 1.28 eV) is a major revision that JSRT should consider.
- **Multi-phase treatment**: The two-zone model (α-U + γ-U) with different swelling mechanisms in each zone provides a template for JSRT implementation.
- **Validation data**: Provides both low-T (400–600 K) and high-T (800–1000 K) swelling data for model validation.
- **Cavity characterization**: Measured cavity size (~3 μm) and number density (~8 × 10⁹ cm⁻³) provide important microstructural benchmarks.
- **Transition criterion**: The critical radius concept (gas-driven → bias-driven) is central to the JSRT framework.

## Relationships

- [[wiki/entities/CavitationalVoid|CavitationalVoid]] — cavitational void swelling model for U-10Zr at 400–600 K with revised vacancy migration energy is the core contribution
- [[wiki/concepts/RateTheoryFramework|RateTheoryFramework]] — Rest's rate-theory framework with DFT-revised parameters (Em_v = 0.34 eV) is the model basis
- [[wiki/entities/FuelAlloy|FuelAlloy]] — U-10Zr metallic alloy fuel in both α-U and γ-U zones is modeled
- [[wiki/summaries/1993_Rest_VoidSwellingAlphaU|1993_Rest_VoidSwellingAlphaU]] — Rest (1993) cavitational void model is directly extended with revised parameters
- [[wiki/summaries/1992_Rest_CavitationalSwellingAlphaUPuZr|1992_Rest_CavitationalSwellingAlphaUPuZr]] — original conference paper with earlier parameter set
- [[wiki/summaries/2020_Aagesen_BisonUPuZrSwellingLowerLengthScale|2020_Aagesen_BisonUPuZrSwellingLowerLengthScale]] — Aagesen (2020) also revisits the cavitational model for BISON
- [[wiki/concepts/SwellingModelComparison|SwellingModelComparison]] — two-zone model (α-U cavitational + γ-U gas bubble) represents a synthesis approach
