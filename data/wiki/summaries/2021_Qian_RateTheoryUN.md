# A Kinetic Rate Theory Modelling of Fission Gas Release and Fuel Swelling for UN Fuels (2021, Qian et al.)

## Metadata
- **Journal**: Journal of Nuclear Materials, 556 (2021) 153188
- **DOI**: 10.1016/j.jnucmat.2021.153188
- **Material System**: UN (uranium nitride)
- **Method**: Kinetic rate theory (GRASS-SST/FASTGRASS framework)
- **Key Topic**: Fission gas release / fuel swelling / bubble size distribution / parameter determination

## Physical Mechanisms
1. **Fission gas generation**: Xe and Kr produced as fission byproducts; Xe:Kr ratio ~9:1
2. **Intragranular bubble nucleation**: Gas atoms form stable bubble cores (dimers) with nucleation probability FN
3. **Bubble growth**: Via vacancy capture, gas atom absorption, and bubble coalescence
4. **Re-solution**: Fission fragments knock gas atoms from bubbles back to matrix — main driver of bimodal bubble size distribution
5. **Gas transport to GB**: Diffusion of gas atoms through concentration gradient to grain boundaries
6. **Intergranular bubble growth and interconnection**: Bubbles on grain faces and edges grow, interconnect into tunnels → gas release
7. **Bubble migration**: Both random (concentration gradient) and biased (temperature gradient) migration
8. **Grain boundary sweeping**: Moving GBs can capture or release bubbles

## Key Equations & Parameters

### Rate equations
- **General form**:

$$\frac{dC_{\alpha,i}}{dt} = -a_{\alpha,i} C_{\alpha,i}^2 - b_{\alpha,i} C_{\alpha,i} + e_{\alpha,i}$$

where $\alpha$ denotes bubble location (intragranular/intergranular) and $i$ is the size group index. Terms represent coalescence loss, resolution loss, and gas production gain respectively.

- **Bubble size grouping**: $N_i = m \cdot N_{i-1}$ ($m = 2$ for fine simulation); groups contain $2^{\text{group label}}$ gas atoms
- **Interpolation**: For bubbles with $N_k$ between groups $i$ and $i+1$: $P_i = (N_{i+1} - N_k)/(N_{i+1} - N_i)$

### Intragranular gas atom balance

$$\frac{dC_g}{dt} = -16\pi F_N R_g D_g C_g^2 - \sum_i \text{(capture by bubbles)}_i - \text{(diffusion to GB)} - \text{(GB sweeping)} + \sum_i b_i C_{\alpha,i} + \eta f$$

where $C_g$ is the dissolved gas atom concentration, $F_N$ is the nucleation factor, $R_g$ is the capture radius, $D_g$ is gas atom diffusivity, and $\eta f$ is the fission gas production rate.

### Bubble coalescence rate

$$P_{i,j} = 4\pi(R_i + R_j)\left[D_i + D_j + \frac{\pi(R_i + R_j)}{4}|\mathbf{V}_j - \mathbf{V}_i|^2 \right]$$

Two terms: random migration (diffusion $D_i, D_j$) and biased migration (temperature gradient-driven drift $\mathbf{V}$).

### Van der Waals bubble model

$$P\left(\frac{4}{3}\pi R_i^3 - BN_i\right) = N_i k_B T$$

$$P = \frac{2\gamma}{R_i} + P_h$$

where $\gamma = 10$ N/m (surface energy), $P_h = 10^7$ N/m² (hydrostatic pressure), and $B = 8.5 \times 10^{-32}$ m³ (Van der Waals constant).

### Bubble diffusivity and velocity

$$D_i = \frac{3 a_0^4 D_s}{4 R_i^4}$$

$$V_i = \frac{3 D_s Q_s^* a_0}{k_B T^2} \cdot \frac{dT}{dx} \cdot \frac{1}{2R_i}$$

$$D_s = 1.92 \times 10^3 \exp\left(\frac{-4.22 \times 10^5}{RT}\right) \text{ m}^2/\text{s}$$

where $a_0 = 0.49$ nm (UN lattice constant), $Q_s^*$ is the heat of transport for surface diffusion, and $dT/dx$ is the local temperature gradient.

### Re-solution constant (Lösönen form)

$$b_i = b_0 \cdot \frac{3d}{3d + R_i} \cdot \frac{\delta^3}{\frac{4}{3}\pi(\delta + R_i)^3} \cdot f$$

where $d = 1$ nm (escape layer thickness), $\delta = 0.4$ nm (return layer thickness), and $f$ is the fission rate.

### Key calibrated parameters
| Parameter | Value | Notes |
|---|---|---|
| Dg (Xe diffusivity) | 4.05×10⁻³ exp(-2.15×10⁵/RT) cm²/s | Newly determined, based on Oi's formula ×20 |
| FN (nucleation factor) | 1×10⁻⁴ | Determined by sensitivity analysis |
| b₀ (resolution constant) | 1×10⁻¹⁸ cm³ | Much smaller than Feng's 1.36×10⁻¹⁵ |
| dg (grain diameter) | 10 μm | |
| η (fission yield) | 0.25 | |

### Fission gas release and swelling

$$\text{FGR} = \frac{\text{gas from face venting} + \text{edge venting} + \text{long-range migration}}{\text{total gas produced}}$$

$$\frac{\Delta V}{V} = \sum_i \frac{4}{3}\pi R_{\alpha,i}^3 \cdot C_{\alpha,i}$$

summed over all bubble locations ($\alpha$) and size groups ($i$).

## Experimental Data

### JOYO experiment validation (UN fuel)
| Parameter | Value |
|---|---|
| Fuel diameter | 7.43 mm |
| Height | 8 mm |
| Bulk density | 86% T.D. |
| U-235 enrichment | 19.39 wt% |
| Cladding | 15Cr-20Ni stainless steel |
| Gas in grain bulk | ~80% |
| Gas at GB | ~15% |
| Gas released | ~5% |

### Thermal conductivity models
- UN: k = 1.37T⁰·⁴¹(1-P)(1+P) W/m/K
- Cladding (D9): λ = 7.598 + 2.391×10⁻²T - 8.899×10⁻⁶T² (T<1000K)

### Diffusion coefficients compared (cm²/s)
| Source | Value |
|---|---|
| Melehan & Gates | 4.0×10⁻⁶ exp(-2.71×10⁵/RT) |
| Biddle | 3.0×10⁻⁸ exp(-2.41×10⁵/RT) |
| **Oi (selected basis)** | **2.05×10⁻⁴ exp(-2.15×10⁵/RT)** |
| BMI | 4.65×10⁻⁵ exp(-3×10⁵/RT) |
| NASA | 2.4×10⁻¹⁰ exp(-1.57×10⁵/RT) |
| **This work** | **4.05×10⁻³ exp(-2.15×10⁵/RT)** |

## Model Description
- Based on FASTGRASS + GRASS-SST framework, adapted for UN fuel
- Bubble size grouping method with m=2 (fine resolution)
- Temperature distribution from COMSOL finite element model
- He gap closing simulated as linear temperature decrease
- Parameter determination: systematic sensitivity analysis of 210+ test combinations
- Validated against JOYO experimental data (FGR, swelling, intragranular gas fraction)

## Key Findings
1. **New Xe diffusion coefficient** for UN: 4.05×10⁻³ exp(-2.15×10⁵/RT) cm²/s — 20× Oi's value, needed to match 80% intragranular gas fraction
2. **Nucleation factor FN = 10⁻⁴** most suitable for UN (vs 1 for UO₂, 0.01 for U₃Si₂, 10⁻⁴-10⁻¹⁰ for metallic fuels)
3. **Resolution constant b₀ = 10⁻¹⁸ cm³** — much smaller than Feng's 1.36×10⁻¹⁵ cm³ for UN
4. **Bimodal bubble size distribution** is driven by resolution: small bubbles increase (re-nucleation from resolved atoms) while medium bubbles decrease; large bubbles increase then decrease with increasing resolution constant
5. **Resolution has complex effects**: FGR decreases then increases; swelling increases then decreases — opposite trends due to competing mechanisms
6. **Diffusion coefficient has minimal effect on swelling** because two opposing effects cancel (less gas in grains vs more coalescence)
7. **Grain size sensitivity**: Larger grains → more intragranular gas retention → less FGR

## Relevance to JSRT Model
- **Most directly comparable framework**: Rate-theory approach similar to JSRT; demonstrates parameter determination methodology
- **Bubble size grouping method**: The 2^N grouping strategy with interpolation is directly applicable to JSRT bubble population modeling
- **Parameter sensitivity methodology**: Systematic approach to determine FN, b₀, and Dg from limited experimental data is a template for JSRT calibration
- **Resolution-driven bimodal distribution**: Important finding that resolution (not surface/volume diffusion) is the main driver — may need to be captured in JSRT
- **New UN parameters**: The calibrated Dg, FN, and b₀ for UN fuel are directly usable if JSRT is applied to nitride fuels
- **Competing effects insight**: The cancellation of diffusion coefficient effects on swelling suggests JSRT swelling predictions may be robust against D uncertainty
- **Van der Waals equation of state**: The P-V relationship for bubbles is essential for JSRT bubble size calculations
- **Gas distribution partitioning**: The 80/15/5 split (intragranular/GB/released) provides validation targets for JSRT

## Relationships

- [[wiki/concepts/RateTheoryFramework|RateTheoryFramework]] — GRASS-SST/FASTGRASS-based kinetic rate theory framework adapted for UN fuel is the core contribution
- [[wiki/entities/FissionGasDiffusion|FissionGasDiffusion]] — new Xe diffusion coefficient (20× Oi's value), re-solution constant, and nucleation factor for UN are determined
- [[wiki/concepts/SwellingMechanisms|SwellingMechanisms]] — bubble nucleation, growth, re-solution, interconnection, and gas release in UN fuel are modeled
- [[wiki/summaries/1979_Ronchi_FissionGasSwellingMX_Fuels|1979_Ronchi_FissionGasSwellingMX_Fuels]] — Ronchi's MX fuel rate-equation model is the methodological predecessor
- [[wiki/summaries/1993_Rest_VoidSwellingAlphaU|1993_Rest_VoidSwellingAlphaU]] — Rest's GRASS-SST framework is the basis for this model
- [[wiki/summaries/2001_Rest_GRSIS_FissionGasMetallic|2001_Rest_GRSIS_FissionGasMetallic]] — GRSIS provides an alternative approach to compare with this rate-theory model
