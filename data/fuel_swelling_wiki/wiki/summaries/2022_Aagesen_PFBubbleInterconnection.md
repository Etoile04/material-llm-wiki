# Phase-Field Simulations of Fission Gas Bubble Growth and Interconnection in U-(Pu)-Zr Nuclear Fuel (2022, Aagesen et al.)

## Metadata
- **Journal**: Materials Theory, 6:8 (2022)
- **DOI**: 10.1186/s41313-021-00041-5
- **Material System**: U-(Pu)-Zr metallic fuel
- **Method**: Phase-field (Cahn-Hilliard with source term)
- **Key Topic**: Bubble growth / interconnection / percolation / swelling

## Physical Mechanisms
1. **Bubble growth in γ phase**: In hotter central regions of U-(Pu)-Zr, large spherical bubbles (5-10 μm) form, grow, and interconnect
2. **Coalescence**: Individual bubbles coalesce with neighbors as they grow, forming elongated voids or larger spheres
3. **Interconnection → gas release**: When interconnected structure connects to free surface, gas is released; further gas production flows out rather than growing existing bubbles
4. **Equilibrium bubble assumption**: Gas pressure exactly balanced by surface tension; no local stress variations
5. **Swelling anisotropy**: Cylindrical metallic fuel swells anisotropically with radial bias; 30%+ in-plane swelling at ~2% FIMA
6. **Phase-dependent morphology**: α+δ phase (T<890K): GB/interphase tearing; γ phase (T>890K): large spherical bubbles

## Key Equations & Parameters

### Cahn-Hilliard model with source term
- **Total free energy**:

$$F = \int_V \left[ f_b(c) + f_{\text{grad}}(c) \right] dV$$

- **Bulk free energy** (double-well, minima at $c=0$ matrix, $c=1$ bubble):

$$f_b(c) = W c^2(1-c)^2$$

- **Gradient energy**:

$$f_{\text{grad}} = \frac{\kappa}{2}|\nabla c|^2$$

- **Evolution equation**:

$$\frac{\partial c}{\partial t} = \nabla \cdot (M \nabla \mu) + s$$

where the chemical potential is:

$$\mu = \frac{\delta F}{\delta c} = \frac{\partial f_b}{\partial c} - \kappa \nabla^2 c$$

- **Source term** (gas production, only active in matrix phase):

$$s = s_0[1 - h(c)]$$

$$h(c) = c^3(6c^2 - 15c + 10)$$

where $h(c)$ is a smooth interpolation function: $h(0)=0$ (full source in matrix), $h(1)=1$ (no source in bubble).

### Porosity definition (accounting for matrix growth)

$$p = \frac{V_f}{1 + V_f}$$

where $V_f = V_{\text{bubble}} / V_{\text{original domain}}$. The denominator $(1+V_f)$ accounts for interstitial deposition expanding the matrix.

### Key parameters
| Parameter | Value |
|---|---|
| σ (interfacial energy) | 1.8 J/m² |
| lint (interface thickness) | 1.5 μm |
| κ (gradient energy) | 4.05×10⁻⁶ J/m |
| W (double-well height) | 1.44×10⁷ J/m³ |
| D (defect diffusivity) | 1.33-10 nm²/s (varied) |
| s₀ (source rate) | 5×10⁻⁹ s⁻¹ |
| Va (atomic volume, γ-U) | 0.02089 nm³ |
| S₀ (total defect production) | 2.4×10⁻⁷ /nm³/s |
| Ḟ (fission rate, EBR-II) | 7.91×10⁻⁸ fissions/nm³/s |
| yXe (Xe fission yield) | 0.2156 |

### Percolation/venting fitting function

$$f_V = \frac{1}{2}\left[1 + \text{erf}\left(\frac{p - p_{\text{cen}}}{\delta}\right)\right]$$

where $p_{\text{cen}}$ is the center porosity and $\delta$ is the characteristic width of the interconnection transition.

- **Mean $p_{\text{cen}}$ values**: 0.244–0.269 depending on parameters
- **Percolation threshold** $p_c \approx 0.26$ (for $N = 3 \times 10^{14}$ m⁻³)

## Experimental Data
- **Bubble number density**: N = 3.0×10¹⁴/m³ at 1.3% burnup (from Bauer & Holland 1995, U-10Zr)
- Swelling of 30%+ in-plane at ~2% FIMA in EBR-II (Hofman et al. 1997)
- Bubble morphology: initially spherical, 5-10 μm diameter in γ phase (Hofman et al. 1990)

## Model Description
- **3D phase-field simulations**: 72×72×72 μm domain, 112 initial bubbles (matching experimental N)
- Initial bubble radius: 3.4 μm (5% volume fraction), random placement with 10 μm minimum spacing
- 10 different random configurations for statistics
- Hexahedral mesh with adaptivity (min element 0.5 μm), periodic BCs (y,z), no-flux (x free surface)
- Run on 720 cores (INL Lemhi cluster)
- Bubble identification: flood fill algorithm (c > 0.5)
- Venting fraction fV calculated as volume of bubbles touching free surface / total bubble volume

## Key Findings
1. **Percolation threshold pc ≈ 0.26**: consistent across different diffusivities and close to continuum percolation of overlapping 3D spheres (slightly smaller)
2. **Diffusivity affects microstructure but NOT fV vs p relationship**: Higher D → coarser microstructure (more coarsening), but interconnection progress vs porosity is similar
3. **Source-diffusion competition**: Early growth controlled by defect transport rate; later stages controlled by source accumulation as matrix shrinks
4. **Surface area evolution**: Rapid initial increase → slowdown → decrease as interconnection and coarsening reduce area
5. **Bubble number density effect**: Higher N → faster interconnection; pcen decreases from 0.263 to 0.244 as N increases from 3.0 to 4.5×10¹⁴/m³
6. **At p = 0.35**: all bubbles connected to free surface for all configurations
7. **Universal interconnection process**: Similar pcen and δ despite different microstructures suggests scale-independent interconnection mechanism
8. Results used to parameterize **BISON engineering-scale swelling models** for U-(Pu)-Zr fuel

## Relevance to JSRT Model
- **Directly applicable**: The percolation threshold (pc ≈ 0.26) and fV(p) function provide engineering-scale parameters for JSRT swelling/gas release modeling
- **Porosity-swelling relationship**: The p = Vf/(1+Vf) conversion is essential for connecting bubble volume fraction to engineering swelling
- **Bubble interconnection criterion**: The finding that complete interconnection occurs at p ≈ 0.35 provides an upper bound for swelling termination
- **Diffusivity independence of fV(p)**: Suggests that JSRT can use a universal interconnection function regardless of diffusion parameters
- **Bubble number density dependence**: The variation of pcen with N provides sensitivity analysis for JSRT model
- **Phase-dependent morphology**: The α+δ vs γ phase distinction in U-(Pu)-Zr informs temperature-dependent swelling regimes in JSRT
- **BISON parameterization example**: Demonstrates how mesoscale results feed into engineering-scale fuel performance codes — directly analogous to JSRT goals

## Relationships

- [[wiki/entities/PhaseFieldModeling|PhaseFieldModeling]] — 3D phase-field Cahn-Hilliard model for bubble growth and interconnection in U-(Pu)-Zr
- [[wiki/concepts/SwellingMechanisms|SwellingMechanisms]] — percolation threshold (pc ≈0.26) and fV(p) function are the engineering-scale results
- [[wiki/entities/FuelAlloy|FuelAlloy]] — U-(Pu)-Zr metallic fuel in γ phase (central region) is the subject material
- [[wiki/summaries/2020_Aagesen_BisonUPuZrSwellingLowerLengthScale|2020_Aagesen_BisonUPuZrSwellingLowerLengthScale]] — companion report providing BISON model parameterization context
- [[wiki/summaries/1990_Hofman_SwellingBehaviorUPuZr|1990_Hofman_SwellingBehaviorUPuZr]] — experimental U-(Pu)-Zr bubble data (5–10 μm bubbles, N = 3×10¹⁴/m³) provide model inputs
- [[wiki/concepts/SwellingModelComparison|SwellingModelComparison]] — percolation threshold compares with GRSIS (Sth = 0.20) and FEAST-METAL (10%) models

## Related Work
- [[wiki/summaries/2020_Aagesen_BisonUPuZrSwellingLowerLengthScale|2020_Aagesen_BisonUPuZrSwellingLowerLengthScale]] — 同一团队的配套报告，将本文结果参数化到BISON
- [[wiki/summaries/1990_Hofman_SwellingBehaviorUPuZr|1990_Hofman_SwellingBehaviorUPuZr]] — U-(Pu)-Zr气泡实验数据，提供模型输入
- [[wiki/summaries/1993_Rest_VoidSwellingAlphaU|1993_Rest_VoidSwellingAlphaU]] — Rest空泡模型，渗流阈值可相互比较
- [[wiki/summaries/2001_Rest_GRSIS_FissionGasMetallic|2001_Rest_GRSIS_FissionGasMetallic]] — GRSIS中Sth=0.20的渗流阈值与本文pc≈0.26比较
- [[wiki/summaries/2018_Millett_ComputationalExperimentalPorosityMetallic|2018_Millett_ComputationalExperimentalPorosityMetallic]] — Cahn-Hilliard相场方法的另一应用（双峰孔隙）
- [[wiki/entities/BISONCode|BISONCode]] — 本文结果用于参数化的工程尺度燃料分析代码
