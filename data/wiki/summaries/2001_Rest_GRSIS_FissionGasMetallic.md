# GRSIS: Fission Gas Release and Swelling Model of Metallic Fast Reactor Fuel (2001, Lee, Kim, Jung)

## Metadata
- **Journal**: Journal of Nuclear Materials, 288, 29–42 (2001)
- **DOI**: 10.1016/S0022-3115(00)00718-2
- **Authors**: Chan Bock Lee*, Dae Ho Kim, Youn Ho Jung (Korea Atomic Energy Research Institute)
- **Material System**: U-Pu-10Zr
- **Method**: Mechanistic rate-theory model (GRSIS code)
- **Key Topic**: Fission gas release and swelling in isotropic fuel matrix

## Physical Mechanisms

1. **Isotropic bubble nucleation**: Fission gas bubbles nucleate isotropically from gas atoms in the metallic fuel matrix — can nucleate at both grain boundaries and phase boundaries (randomly distributed), unlike oxide fuel where bubbles preferentially form at grain boundaries.
2. **Three bubble size classes**: Bubbles classified into sizes 1, 2, 3 based on radius:
   - Bubble-1: smallest stabilized bubbles (~0.5 μm radius)
   - Bubble-2: intermediate (~2.5 μm radius)
   - Bubble-3: largest closed bubbles (~12.5 μm radius)
   - Bubble-4: open bubbles (interconnected to external free space)
3. **Bubble growth mechanisms**:
   - Gas atom diffusion into bubbles
   - Bubble coalescence by diffusion and collision
   - Radial growth by gas diffusion
4. **Bubble interconnection**: When closed bubble swelling reaches threshold (Sth = 0.2 based on SC lattice percolation theory), bubbles interconnect forming open channels to external free space → instantaneous fission gas release.
5. **Percolation theory**: Based on Monte Carlo simulations for SC lattice: critical concentration Pc = 0.32, fractional volume VSC = 0.17, critical swelling ΔV/V = 0.20.
6. **Post-interconnection behavior**: Fission gases successively released through open bubbles; closed bubbles absorbed by open bubbles.

## Key Equations & Parameters

### Bubble Classification
| Bubble Type | Radius (μm) | Description |
|------------|-------------|-------------|
| Bubble-1 | 0.5 | Minimum stabilized size |
| Bubble-2 | 2.5 | Intermediate |
| Bubble-3 | 12.5 | Maximum closed bubble |
| Bubble-4 | Variable | Open (interconnected) |

### Key Rate Equations

**Gas atom balance:**
$$\frac{dC_g}{dt} = YF - \sum J_{gi} - J_{b1}^{\text{nucl}} \quad \text{(Eq. 6)}$$

**Bubble-$i$ gas balance:**
$$\frac{dC_{gbi}}{dt} = [\text{nucleation + gas diffusion + coalescence gains}] - [\text{integration losses + interconnection release}] \quad \text{(Eqs. 7–10)}$$

**Gas diffusion to bubble-$i$:**
$$J_{gi} = k_{gi} \times C_g \times N_{bi}, \quad k_{gi} = E_{gbi} \times 4\pi r_{bi} \times D_g \quad \text{(Eqs. 18–19)}$$

**Bubble diffusion coefficient:**
$$D_{bi} = \frac{3a_0^4}{2\pi r_{bi}^4} \times D_s \quad \text{(Eq. 20)}$$

**Surface diffusion:**
$$D_s = D_{s0} \exp(-Q_s/kT) \quad \text{(Eq. 21)}$$

**Collision probability:**
$$P_{ij} = \frac{\Delta r_{bi}}{0.25 l_j - (r_{bi} + r_{bj})} \quad \text{(Eq. 27)}$$

### Fission Gas Release

$$\text{FGR} = \begin{cases} 0 & S_t < S_{\text{th}} \\ f_{\text{th}}(C_{gb1} + C_{gb2} + C_{gb3}) & S_t = S_{\text{th}} \\ C_{gb4} & S_t > S_{\text{th}} \end{cases}$$

where $S_{\text{th}} = 0.20$ (percolation threshold) and $f_{\text{th}} = 0.30$.

### Key Parameters
| Parameter | Value |
|-----------|-------|
| Gas diffusion factor (Dg0) | 9.5 × 10⁻⁸ m²/s |
| Activation energy of gas diffusion (Qg) | 32,000 cal/gm mole |
| Surface diffusion factor (Ds0) | 9.5 × 10⁻⁵ m³/s |
| Activation energy of surface diffusion (Qs) | 32,000 cal/gm mole |
| Surface tension | 1.0 N/m |
| Bubble-1 nucleation constant | 1 × 10⁻²⁰ bub-1/s·atom |
| Bias factors (Egbi, Ebb, Ebb4) | 1.0 |
| Threshold closed bubble swelling (Sth) | 0.2 |
| Fraction interconnected at threshold (fth) | 0.3 |
| Volume correction factor (fv) | 1.0 |
| Surface area correction factor (fs) | 0.6 |

### Fission Gas Release
(FGR equations shown above in LaTeX format)

## Experimental Data

### Validation against ANL EBR-II Data
- **Fuels**: U-10Zr, U-8Pu-10Zr, U-19Pu-10Zr
- **Temperature**: 550°C (assumed in calculations)
- **Fission gas release behavior**: 
  - Incubation period at 0.5–1.0% burnup
  - Rapid increase to ~70% release
  - Saturation at 4–5% burnup
- **GRSIS predictions**: Good agreement with ANL data for all three fuel compositions

### Parametric Study Results
1. **Gas diffusion coefficient**: Factor of 100 change → no significant change in FGR when above threshold; reduced coefficient delays interconnection.
2. **Temperature**: Significant effect only at low T (<300°C, no interconnection); above ~450°C, threshold burnup and FGR are relatively insensitive to temperature.
3. **Bubble nucleation rate**: No significant effect — bubble growth (not nucleation) is controlling.
4. **Threshold swelling**: Higher threshold → delayed onset of gas release; after threshold, similar FGR trends.
5. **Bubble size classification**: Best fit with radii 0.5, 2.5, 12.5 μm.

## Model Description

1. **GRSIS** (Gas Release and Swelling in ISotropic fuel matrix): Mechanistic computer code for fission gas behavior in metallic fuel.
2. **Isotropic assumption**: Unlike oxide fuel models, GRSIS assumes bubbles nucleate isotropically at both grain and phase boundaries.
3. **Four bubble classes**: Three closed + one open, with transition rules based on size and collision probability.
4. **Percolation-based interconnection**: Critical swelling of 0.20 (ΔV/V) triggers bubble interconnection.
5. **Gap closure**: Model accounts for fuel-cladding contact pressure effects on bubble swelling.
6. **Fuel deformation**: When contact stress exceeds yield stress of porous fuel, open bubble collapse occurs.

## Key Findings

1. **GRSIS model successfully predicts** general fission gas release and swelling behavior of U-Pu-10Zr metallic fuel.
2. **Isotropic nucleation assumption** is appropriate for metallic fuel where phase boundaries are randomly distributed.
3. **Bubble growth (not nucleation)** is the controlling parameter for fission gas release.
4. **Gas diffusion coefficient** is the most sensitive parameter — temperature dependence of gas diffusivity drives bubble growth and interconnection timing.
5. **Below ~300°C**: Bubble swelling too low for interconnection and gas release.
6. **Anisotropic cavitational void swelling not considered** — GRSIS focuses on isotropic gas bubble swelling.
7. **Contact pressure** significantly affects post-gap-closure swelling behavior.
8. **Bubble size classification** (0.5, 2.5, 12.5 μm) provides best fit to ANL irradiation test data.

## Relevance to JSRT Model

- **Alternative modeling approach**: GRSIS uses gas-bubble-driven swelling (not cavitational void swelling) as the primary mechanism — represents the competing school of thought to Rest's approach.
- **Isotropic nucleation**: Important consideration for metallic fuel where phase boundaries provide additional nucleation sites.
- **Percolation threshold**: The Sth = 0.20 threshold provides a practical criterion for bubble interconnection and gas release onset.
- **Bubble size classes**: The three-class system could simplify numerical implementation compared to continuous size distribution.
- **Complementary to JSRT**: GRSIS handles the γ-U phase well (where gas-driven swelling dominates), while JSRT/Rest's model handles α-U phase (where cavitational void swelling dominates). A combined approach may be optimal.
- **Validation data**: ANL EBR-II data for multiple fuel compositions provides benchmark data.
- **Gap closure effects**: Important for realistic fuel performance modeling — restraint effects on swelling.

## Relationships

- [[wiki/concepts/SwellingMechanisms|SwellingMechanisms]] — GRSIS models isotropic gas-bubble-driven swelling via percolation-based interconnection in metallic fuel
- [[wiki/entities/FuelAlloy|FuelAlloy]] — U-Pu-Zr metallic fuel alloy is the primary modeled system
- [[wiki/entities/FissionGasDiffusion|FissionGasDiffusion]] — gas diffusion coefficient is the most sensitive model parameter
- [[wiki/concepts/RateTheoryFramework|RateTheoryFramework]] — rate equations for bubble nucleation, growth, and coalescence are the model backbone
- [[wiki/concepts/SwellingModelComparison|SwellingModelComparison]] — GRSIS represents the gas-bubble-driven alternative to Rest's cavitational model
- [[wiki/summaries/1990_Hofman_SwellingBehaviorUPuZr|1990_Hofman_SwellingBehaviorUPuZr]] — Hofman's observations on metallic fuel swelling are incorporated
- [[wiki/summaries/2013_Karahan_FEAST_METAL_FuelSwelling|2013_Karahan_FEAST_METAL_FuelSwelling]] — FEAST-METAL uses the GRSIS algorithm as its fission gas behavior module
