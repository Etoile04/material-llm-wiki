# Further Development of the Fission Gas Swelling Model for U-10Mo Fuels

## Metadata

- **Title:** Further development of the fission gas swelling model for U-10Mo fuels
- **Authors:** Xiaobin Jian, Feng Yan, Xiangzhe Kong, Yong Li, Shurong Ding
- **Year:** 2022
- **Journal:** Journal of Nuclear Materials, 565, 153769
- **DOI:** 10.1016/j.jnucmat.2022.153769
- **Affiliations:** Fudan University

## Physical Mechanisms

### Mechanistic Fission Gas Swelling Framework
1. **Fission gas atom diffusion** within equivalent spherical grains → governed by diffusion equation with source terms
2. **Intra-granular bubble evolution** — trapping and resolution of gas atoms
3. **Grain recrystallization** — increases GB area, accelerates gas atom transport to GBs
4. **Inter-granular bubble nucleation and growth** — primary contributor to fission gas swelling
5. **External hydrostatic pressure** — constrains bubble growth via modified Van der Waals gas law
6. **Irradiation creep** — correlated with porosity from fission gas swelling

### Bubble Density Evolution
- Non-monotonic behavior: saturation at ~4.5–4.7 × 10²⁷ fissions/m³ for U-7Mo, followed by reduction at higher fission densities
- New model captures this via $(F_{d0}/F_d)^2$ form for recrystallized region contribution
- Bubble density in un-recrystallized region: relatively constant
- Bubble density in recrystallized region: increases then stabilizes

### Swelling Behavior
- Fission gas swelling < 5% before recrystallization
- Increases to ~18% when recrystallization completes
- Bubble pressure decreases as bubble radius increases (inverse relationship)

## Key Equations

### Fission Gas Diffusion Equation (Spherical Grain)
$$\frac{\partial c}{\partial t} = D_g \left(\frac{\partial^2 c}{\partial r^2} + \frac{2}{r}\frac{\partial c}{\partial r}\right) + Y\dot{f} - 16\pi f_n D_g r_g c_g^2 - 4\pi r_b D_g c_g c_b + b n_b c_b$$

### Simplified Diffusion (φ = c + n_b c_b)
$$\frac{\partial \phi}{\partial t} = D_g \left(\frac{\partial^2 \phi}{\partial r^2} + \frac{2}{r}\frac{\partial \phi}{\partial r}\right) + Y\dot{f}$$

### Boundary Conditions (Inter-granular Resolution)
$$\phi(0, t) = 0$$
$$\phi(r_{gr}, t) = b' \lambda N / (2D_g)$$

### Conservation Equation
$$\frac{4}{3}\pi r_{gr}^3 \int_0^t Y\dot{f} d\tau = \int_0^{r_{gr}} 4\pi r^2 \phi dr + 4\pi r_{gr}^2 \frac{N}{2}$$

### Bubble Number Model
**Un-recrystallized region:**
$$N_{bubble1} = 2\pi(1-\eta_r)^{2/3} r_{gr0}^2 \cdot C_b \cdot N_b$$

**Recrystallized region:**
$$N_{bubble2} = \frac{2}{3}\pi r_{gr0}^3 \eta_r \cdot \eta_{Fd} \cdot C_{bx} N_{bx}$$

Where $\eta_{Fd} = (F_{d0}/F_d)^2$ for $F_d \geq F_{d0}$, and 1 otherwise.

### Grain-Boundary Bubble Concentration
$$C_b = \sqrt{\frac{8za \left.\frac{dN}{dt}\right|_{r_{gr}=(1-\eta_r)^{1/3}r_{gr0}}}{\sqrt{12}\pi\xi\delta}}$$

### Recrystallization Volume Fraction
$$\eta_r = 1 - \left(1 - \frac{16\gamma_s B^2(F_d - B_{ux})}{r_{gr0} \cdot \frac{(1-\nu/2)(1-\nu)}{2\pi}}\right)^3$$

### Modified Van der Waals Gas Law (Bubble Radius)
$$P_b \cdot \frac{4\pi \bar{R}^3}{3} - h_s b_v \bar{N}_{atom} = \bar{N}_{atom} kT$$

### Bubble Pressure
$$P_b = \begin{cases} H_p + 2\gamma/\bar{R} & H_p > 0 \\ 2\gamma/\bar{R} & H_p \leq 0 \end{cases}$$

### Fission Gas Swelling
$$S_{fg} = \frac{V_{bubble}}{V_{fuel}} = \frac{4}{3}\pi \bar{R}^3 \cdot n_{bubble}$$

### Irradiation Creep Coefficient
$$\dot{\varepsilon}_{cr} = A \cdot \sigma \cdot \dot{f} \cdot (1 + B \cdot \phi_p)$$
Where $A = 180 \times 10^{-22}$ mm³/MPa (newly identified for dense U-10Mo)

## Parameters

### Model Parameters
| Parameter | Value | Unit | Source |
|-----------|-------|------|--------|
| Y (gas yield per fission) | 0.25 | atoms/fission | [7] |
| $b_0$ (resolution coefficient) | 2 × 10⁻²⁴ | m² | [7] |
| $f_n$ (nucleation factor) | 10⁻² | — | [7] |
| $r_g$ (gas atom radius) | 2.16 × 10⁻¹⁰ | m | — |
| $b'_0$ (un-recrystallized) | 4.0 × 10⁻²⁶ | m² | — |
| $b'_0$ (fine grain) | 1.9 × 10⁻²⁵ | m² | — |
| $D_0$ (diffusion coefficient) | — | m²/s | calibrated |
| $F_{d0}$ (saturation fission density) | 4.7 × 10²⁷ | fissions/m³ | fitted |
| $h_s$ (fitting parameter) | 0.6 | — | [28] |
| $b_v$ (Van der Waals, Xe) | 8.5 × 10⁻²⁹ | m³/atom | [15] |
| A (creep coefficient) | 180 × 10⁻²² | mm³/MPa | newly identified |

### Key Variables
| Symbol | Description |
|--------|-------------|
| $c$ | Dissolved fission gas concentration (atoms/m³) |
| $\dot{f}$ | Fission rate (fissions/m³·s) |
| $D_g = D_0 \dot{f}$ | Gas atom diffusion coefficient |
| $b = b_0 \dot{f}$ | Resolution rate |
| $r_{gr}$ | Grain radius |
| $n_{bubble}$ | Bubble volumetric density |
| $\bar{R}$ | Average bubble radius |
| $\bar{N}_{atom}$ | Average gas atoms per bubble |
| $\eta_r$ | Recrystallized volume fraction |
| $H_p$ | External hydrostatic pressure |
| $\gamma_s$ | Surface tension |

## Experimental Data

### Validation Results
1. **Total irradiation swelling:** Good agreement with diverse experimental data, especially at high burnup
2. **Bubble density evolution:** Magnitude consistent with U-7Mo fuel data; captures saturation and decrease
3. **Bubble radius:** Continuous growth to ~0.1 µm at recrystallization onset, then acceleration
4. **Fuel foil thickness increments:** Predictions match monolithic U-10Mo/Al plate measurements
5. **External pressure dependence:** Model captures experimentally observed dominant effect of hydrostatic pressure
6. **Temperature dependence:** Correctly reproduces experimental trends

### Key Trends
- Before recrystallization: bubble density ~constant, radius grows continuously
- During recrystallization: bubble density increases sharply
- After recrystallization: density stabilizes/decreases, radius enlargement dominates
- Bubble porosity: <5% before recrystallization → ~18% at completion
- Bubble pressure: decreases as radius increases

### Parametric Studies
- Temperature increase → enhanced gas atom diffusion → faster swelling
- External pressure increase → constrained bubble growth → reduced swelling
- Grain boundary diffusion enhancement factor → significant influence on swelling rate

## Relationships to Other Work

- **Kim's model:** Widely used empirical model — current work provides mechanistic improvement
- **Cui et al.:** Analytical solutions for gas atom diffusion — directly used
- **Ye et al. (2023):** DART code integrated simulation — complementary modeling approach
- **Hanson et al. (2022, 2025):** Experimental swelling data from EMPIrE — validation source
- **Gan et al. (2017):** Bubble density data for U-7Mo — used for model calibration
- **Robinson-Williams model:** Empirical swelling bounds — compared against

## Relationships

- [[wiki/entities/FuelAlloy|FuelAlloy]] — U-10Mo fuel mechanistic fission gas swelling model is the central contribution
- [[wiki/entities/Recrystallization|Recrystallization]] — grain recrystallization and its non-monotonic effect on bubble density are captured
- [[wiki/entities/FissionGasDiffusion|FissionGasDiffusion]] — fission gas atom diffusion in spherical grains is the core transport process
- [[wiki/concepts/SwellingMechanisms|SwellingMechanisms]] — comprehensive mechanistic model coupling gas diffusion, bubble nucleation/growth, recrystallization, and creep
- [[wiki/concepts/SwellingModelComparison|SwellingModelComparison]] — this model is compared with Kim-Hofman and Cui et al. empirical/semi-empirical approaches
- [[wiki/summaries/2015_Cui_MechanisticGaseousSwellingUMoUMo|2015_Cui_MechanisticGaseousSwellingUMoUMo]] — Cui's mechanistic model is directly built upon
- [[wiki/summaries/2023_Ye_IntegratedSimulationU10Mo|2023_Ye_IntegratedSimulationU10Mo]] — DART code integration uses results from this model

## Related Work
- [[wiki/summaries/2023_Ye_IntegratedSimulationU10Mo|2023_Ye_IntegratedSimulationU10Mo]] — DART/GRASS集成模拟，直接使用本文裂变气体肿胀模型的结果
- [[wiki/summaries/2023_Li_ElasticConstantsU10Mo|2023_Li_ElasticConstantsU10Mo]] — 同组(Li & Ding)的等效弹性常数模型，本文肿胀模型产生的孔隙率作为其输入
- [[wiki/summaries/2015_Cui_MechanisticGaseousSwellingUMoUMo|2015_Cui_MechanisticGaseousSwellingUMoUMo]] — 本文机理模型直接基于Cui的解析解框架发展
- [[wiki/summaries/2025_Hanson_StablePredictableSwellingU10Mo|2025_Hanson_StablePredictableSwellingU10Mo]] — MP-1实验数据可用于验证本模型的高燃耗预测
- [[wiki/summaries/2013_Kim_RecrystallizationFGBSwellingUMo|2013_Kim_RecrystallizationFGBSwellingUMo]] — Kim-Hofman经验模型，本文提供机理改进的出发点
- [[wiki/concepts/RateTheoryFramework|RateTheoryFramework|]] — 本文采用速率理论框架描述裂变气体扩散、气泡形核长大和再结晶
