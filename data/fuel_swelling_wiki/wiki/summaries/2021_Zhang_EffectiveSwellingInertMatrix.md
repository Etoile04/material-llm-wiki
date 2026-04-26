# Modelling of Effective Irradiation Swelling for Inert Matrix Fuels

## Metadata
- **Title:** Modelling of effective irradiation swelling for inert matrix fuels
- **Authors:** Jing Zhang, Haoyu Wang, Hongyang Wei, Jingyu Zhang, Changbing Tang, Chuan Lu, Chunlan Huang, Shurong Ding, Yuanming Li
- **Year:** 2021
- **Journal:** Nuclear Engineering and Technology, 53, 2616-2628
- **DOI:** 10.1016/j.net.2021.02.019
- **Affiliations:** Fudan University; Nuclear Power Institute of China
- **Fuel System:** PuO₂/Zr inert matrix fuel (dispersion fuel)

## Physical Mechanisms

### Solid Fission Product Swelling
- Linear function of fission density
- Independent of temperature at low burnup

### Fission Gas Swelling
- Complex mechanism dependent on gas atom diffusion within fuel grain
- After critical fission density, grain recrystallization occurs, accelerating fission gas swelling
- Affected by external hydrostatic pressure
- Intergranular gas atom resolution effect included

### Matrix Effects
- Irradiation creep in inert metal matrix relaxes mechanical interactions between fuel particles and matrix
- Thermal creep at high temperatures must be included
- Work hardening effects in matrix plasticity considered
- Irradiation hardening of matrix

### Effective Irradiation Swelling
- Homogenized swelling under irradiation environments
- Coupling between matrix creep, external hydrostatic pressure, and temperature
- Equivalent spherical RVE model used for homogenization

## Key Equations

### Effective Irradiation Swelling (Eq. 1)
$$\frac{\Delta V}{V_0} = \left(\frac{r}{r_0}\right)^3 - 1$$

where $V$ is post-irradiation spherical volume, $V_0$ is initial volume, $r$ is post-irradiation outer radius, $r_0$ is initial outer radius.

### Intergranular Bubble Radius (Van der Waals, Eq. 2)
$$\frac{2\gamma}{R_b} + P_h - \left(\frac{4\pi R_b^3}{3} - h_{sb}v_b N_b\right) = N_b k T$$

where $\gamma$ = surface tension, $R_b$ = bubble radius, $P_h$ = external hydrostatic pressure, $h_s$ = fitting parameter, $v_b$ = Van der Waals gas constant of Xe, $N_b$ = average number of gas atoms per bubble.

### Particle Hydrostatic Pressure Relationship (Eq. 4)
$$H_{pf} \approx H_p + H_{p0}$$

### Stable Hydrostatic Pressure $H_{p0}$ (fitted)
For 473K ≤ T < 673K:
$$H_{p0} = \left(-0.0625f_{v0}^2 + 0.04775f_{v0} - 0.01237\right)T^2 + \left(54.375f_{v0}^2 - 39.4865f_{v0} + 9.54425\right)T + \left(-7686.3125f_{v0}^2 + 4371.05475f_{v0} - 618.28387\right)$$

### DART Model Verification (Eq. 3)
$$\frac{\Delta V}{V_0} = \frac{\Delta V_f}{V_0}$$

(no chemical reaction or irradiation-enhanced sintering for PuO₂/Zr)

## Parameters

| Parameter | Value | Notes |
|-----------|-------|-------|
| Particle radius | 0.05 mm | RVE model |
| Temperature range | 473-773 K | |
| Fission rate | 1×10²⁰ fissions/(m³·s) | fuel particle |
| Fast neutron flux | 2.01568×10¹¹ n/(mm²·s) | |
| Particle volume fractions | 10%, 20%, 30%, 40% | |
| Initial grain size (UO₂) | 5-15 μm | validation |
| Van der Waals gas constant $v_b$ | for Xe | from Refs [38,39] |
| Boltzmann constant $k$ | 1.38×10⁻²³ J/K | |

## Experimental Data

### Validation Data
- UO₂ rim-zone fission gas swelling experimental data used for validation
- DART model comparison for Al-based dispersion fuel
- Agreement between simulation and experimental results confirmed

### Key Results
- Matrix creep effect increases effective swelling by ~13.3% at fission density 4.3×10²⁷ fissions/m³
- Hydrostatic pressure 0-300 MPa shows remarkable dependence
- Above 300 MPa particle pressure, fission gas swelling hardly reduced
- Stable $H_{p0}$ at 573K ≈ 430 MPa; at 673K ≈ 85 MPa (for fv0 = 20%)
- Maximum relative error of $H_{p0}$ fitting: ~7%

## Key Findings

1. Matrix creep, external hydrostatic pressure, and temperature effects are **coupled** with each other
2. Matrix creep effects at high temperatures (>573K) **must** be included
3. External hydrostatic pressure (0-300 MPa) shows remarkable dependence on effective swelling
4. Fission gas swelling plays important role only at higher fission densities (>2×10²⁷ fissions/m³)
5. An explicit multi-variable mathematical model established as function of: particle volume fraction, temperature, external hydrostatic pressure, fission density
6. The effective swelling is not very sensitive to particle hydrostatic pressure at high pressure levels (>300 MPa)

## Relationships to Other Work

- **DART model** [26,35,36]: Verified against; extended by including creep and work hardening effects
- **Hu et al. (2017)**: Van der Waals gas equation for intergranular bubbles
- **UO₂ rim-zone studies** [38,39,41-44]: Used for model validation
- **Relevant to:** Dispersion nuclear fuel design, composite fuel pellet optimization
- **Connection to:** Yun et al. (2022) cavitational void swelling model (different mechanism focus)

## Relationships

- [[wiki/concepts/SwellingMechanisms|SwellingMechanisms]] — effective irradiation swelling model coupling solid FP, fission gas, matrix creep, and hydrostatic pressure
- [[wiki/entities/FissionGasDiffusion|FissionGasDiffusion]] — intergranular bubble growth via gas atom diffusion and Van der Waals EOS
- [[wiki/entities/Recrystallization|Recrystallization]] — grain recrystallization accelerates fission gas swelling at high fission density
- [[wiki/concepts/SwellingModelComparison|SwellingModelComparison]] — DART model comparison and RVE homogenization approach
- [[wiki/summaries/2022_Yun_CavitationalVoidSwelling|2022_Yun_CavitationalVoidSwelling]] — cavitational void swelling (different mechanism, complementary focus)
- [[wiki/summaries/2001_Rest_GRSIS_FissionGasMetallic|2001_Rest_GRSIS_FissionGasMetallic]] — GRSIS model for comparison of gas bubble swelling approaches

## Related Work
- [[wiki/summaries/2022_Yun_CavitationalVoidSwelling|2022_Yun_CavitationalVoidSwelling]] — 空泡肿胀机制不同但互补的U-10Zr模型
- [[wiki/summaries/2020_Williams_PIRT_SwellingUZr|2020_Williams_PIRT_SwellingUZr]] — PIRT评估肿胀知识差距，涵盖多种燃料体系
- [[wiki/summaries/2013_Karahan_FEAST_ExtendedSwelling_UPuZr|2013_Karahan_FEAST_ExtendedSwelling_UPuZr]] — FEAST-METAL肿胀模型，可比较的工程尺度方法
- [[wiki/concepts/SwellingMechanisms|SwellingMechanisms]] — 有效肿胀耦合固体FP、裂变气体、基体蠕变和静水压
- [[wiki/concepts/SwellingModelComparison|SwellingModelComparison]] — DART模型比较与RVE均匀化方法
- [[wiki/entities/FissionGasDiffusion|FissionGasDiffusion]] — 晶间气泡生长通过气体原子扩散和Van der Waals EOS
