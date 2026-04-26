# Irradiation Swelling, Phase Reversion, and Intergranular Cracking of U-10 wt% Mo Fuel Alloy

## Metadata
- **Title**: Irradiation Swelling, Phase Reversion, and Intergranular Cracking of U-10 wt% Mo Fuel Alloy
- **Authors**: R.M. Willard, A.R. Schmitt
- **Year**: 1965 (Report issued 1965, work from NAA-SR-8956)
- **Report**: NAA-SR-8956, Atomics International (Division of North American Aviation, Inc.)
- **Journal**: AEC Research and Development Report (not journal-published)
- **DOI**: None
- **Affiliation**: Atomics International, Canoga Park, California
- **Key context**: Hallam Nuclear Power Facility (HNPF) Core I fuel development; U-10Mo fuel alloy

## Physical Mechanisms

### Swelling Mechanism
- **Linear swelling** with burnup in range 3000-12,000 Mwd/MTU
- Swelling primarily from **intergranular void formation** (wedge and elliptical types)
- Voids nucleate at grain boundaries due to stress concentrations from grain boundary sliding
- Void growth by: (1) tip advancement from continued grain sliding, (2) vacancy condensation, or both
- **Wedge-shaped cracks**: grow by tip advancement + vacancy condensation (higher stress)
- **Elliptical cavities**: grow by vacancy condensation only (lower stress)

### Phase Reversion Mechanism
- U-10Mo has a **eutectoid transformation** at 1065°F (575°C): γ → α + γ'
- Metastable γ phase can be retained at room temperature (transformation is sluggish, ~20 hr at 900°F to reach TTT nose)
- **Competing mechanisms** during irradiation:
  - **Thermal diffusion** (DT): drives γ → α + γ' transformation
  - **Radiation-induced diffusion** (DR): from fission displacement spikes, can retain or form γ phase
- When DT > DR: thermal transformation predominates → α + γ' forms
- When DR > DT: radiation effect predominates → γ retained or formed

### Intergranular Cracking Sequence
1. Voids produced at grain junctions and along grain boundaries
2. Voids grow by vacancy condensation and tip advancement from continued grain sliding
3. Voids coalesce at critical size/distribution
4. Cracks from different grain boundaries join → macrocracks
5. Macrocracks extend from ~1/3 radius to surface

### Cracking Conditions
- Requires **peak central temperatures > 1125°F** (except one case at 1029°F)
- Enhanced by: thermal gradients, thermal cycling (reactor scrams at several hundred °F/min), phase transformation stresses
- Specimens experienced up to **300 thermal shocks** to room temperature during irradiation

## Key Equations

### Thermal Diffusion Coefficient
$$D_T = D_0 \exp\left(-\frac{Q}{RT}\right)$$

Where:
- $D_0 = 10^{-2}$ cm²/sec
- $Q/R = 24,600$ K (for U-10 wt% Mo)
- At T = 640°C: $D_T = 2 \times 10^{-14}$ cm²/sec

### Radiation-Induced Diffusion Coefficient
$$(D_R)_{\frac{1}{2}} = 1.4 \times 10^{-18} \text{ to } 0.6 \times 10^{-18} \text{ cm}^2/\text{sec}$$

At reference burnup rate $(\dot{B}u)_{\frac{1}{2}} = 5.25 \times 10^{12}$ fissions/cm³·sec:
$$D_R = 2.67 \times 10^{-31} \times \dot{B}u \text{ (cm}^2/\text{sec)}$$

### Critical Fission Rate (Phase Stability Boundary)
$$\dot{B}u_{critical} = \frac{D_0 \exp(-Q/RT)}{2.67 \times 10^{-31}} = 3.75 \times 10^{28} \exp\left(-\frac{24,600}{T}\right) \text{ (fissions/cm}^3\text{-sec)}$$

### Critical Fission Rate vs Temperature

| Temperature (°F) | Temperature (°C) | Critical Fission Rate (fissions/cm³·sec) |
|-----------------|-----------------|----------------------------------------|
| 700 | 371 | 8.8 × 10¹¹ |
| 725 | 385 | 2.2 × 10¹² |
| 750 | 399 | 4.8 × 10¹² |
| 775 | 413 | 9.2 × 10¹² |

## Parameters

### Specimen Conditions
- **Geometry**: 0.5" diameter × 2.0" long cast slugs (unrestrained)
- **Irradiation facility**: Materials Testing Reactor (MTR)
- **Fission rate range**: 2.5-8.0 × 10¹² fissions/cm³·sec
- **Average central temperatures**: 750-1085°F (399-585°C)
- **Burnup range**: 3,000-12,000 Mwd/MTU

### Pre-Irradiation Heat Treatments
1. **As-cast (AC)**: Inhomogeneous metastable γ phase
2. **Gammatized (G)**: 24 hr at 1650°F → homogeneous metastable γ
3. **Partially transformed (PT)**: 100 hr at 900°C → α + γ' + γ

### HNPF Core I Design Conditions
- 240 Mwt, 75 Mwe, sodium-cooled, graphite-moderated
- Fuel: 3.6% enriched as-cast U-10Mo, 0.590" diameter, 159" length
- Cladding: Type 304 SS, 0.640" ID, sodium-bonded

## Experimental Data

### Swelling Data (Figure 5, Table 3)
| Specimen | Fission Rate (×10¹²) | Avg Central T (°F) | ΔDiameter (%) | Burnup (Mwd/MTU) | Pre-Structure | Post-Structure | Cracking |
|----------|---------------------|-------------------|---------------|-------------------|---------------|----------------|----------|
| 2-1 | 7.9 | 750 | 1.0 | 11,000 | AC | G | No |
| 4-2 | 6.35 | 965 | 25.2 | 10,100 | G | T | Yes |
| 4-5 | 7.1 | 1085 | 23.1 | 11,800 | G | T&S | Yes |
| 4-9 | 5.9 | 910 | 35.3 | 10,900 | PT | T | Yes |
| 6-3 | 4.6 | 905 | 9.0 | 5,600 | PT | T | No |
| 6-4 | 5.2 | 990 | 10.2 | 6,100 | AC | T | Yes |
| 6-7 | 5.3 | 975 | 10.6 | 6,300 | AC | T&S | No |
| 6-9 | 4.2 | 810 | 12.3 | 4,700 | PT | T | No |
| 7-3 | 2.5 | 725 | 0.8 | 3,000 | PT | G | No |
| 7-6A | 3.3 | 1025 | 5.4 | 4,600 | PT | T&S | No |
| 7-6B | 3.5 | 1025 | 15.7 | 4,600 | PT | T&S | Yes |

### Post-Irradiation Microstructure vs Temperature
- **<805°F**: Retained or transformed to γ structure (radiation-induced reversion)
- **800-910°F**: Lamellar transformed structure (α + γ')
- **>910°F**: Spheroidized transformed structure

### Void/Cracking Observations
- 5 of 11 specimens showed intergranular voids
- All void-bearing specimens had peak T > 1125°F (except 4-2 at 1029°F)
- Cracking begins ~1/3 distance from center, maximum density at ~1/2 radius
- 7-6A vs 7-6B comparison: same burnup/temperature, but 7-6B cracked (15.7% swelling) vs 7-6A intact (5.4%)

## Key Findings

1. **Linear swelling-burnup relationship** from 3000-12,000 Mwd/MTU, deviations from temperature excursions or mechanical instability
2. **γ phase retention** below 800°F at fission rates of 10¹²-10¹³ f/cm³·sec
3. **Critical fission rate theory** (Bleiberg) successfully predicts phase stability boundaries
4. **Phase reversion**: α + γ' reverts to γ when temperature lowered below ~800°F at prescribed fission rates
5. **Intergranular cracking** is the primary cause of excessive swelling deviations; requires T > 1125°F peak
6. **Specimen 2-1** demonstrated excellent dimensional stability at 11,000 Mwd/MTU (low temperature, high fission rate)
7. **Thermal cycling** (reactor scrams, ~300 events) contributes to structural degradation
8. **Pre-irradiation heat treatment** does not prevent phase transformation during irradiation

## Relationships to Other Work

- **Bleiberg (1959)**: Established radiation-induced diffusion theory and critical fission rate concept for U-Mo alloys
- **Shoudy et al. (1962)**: Studied radiation stability of U-10Mo as function of temperature and fission rate
- **Conrad (1961, in Dorn)**: Summarized intergranular cracking theory (wedge vs elliptical cavities)
- **McLean (1961)**: Cavity shape dependence on boundary stress magnitude
- **Hofman et al. (1990)**: Similar grain boundary tearing mechanism observed in α-U phase of U-Pu-Zr fuel; connects U-Mo and U-Pu-Zr swelling behavior through common α-phase anisotropy
- **U-Mo fuel for research reactors**: This early work established baseline understanding of U-10Mo irradiation behavior relevant to modern dispersion fuel development (although at much higher temperatures than typical research reactor conditions)

## Relationships

- [[wiki/entities/FuelAlloy|FuelAlloy]] — U-10Mo alloy fuel phase stability, swelling, and intergranular cracking are the central topics
- [[wiki/concepts/SwellingMechanisms|SwellingMechanisms]] — intergranular void formation and swelling mechanisms in U-10Mo are characterized here
- [[wiki/entities/CavitationalVoid|CavitationalVoid]] — wedge-shaped and elliptical intergranular voids described here connect to cavitational void swelling models
- [[wiki/summaries/1990_Hofman_SwellingBehaviorUPuZr|1990_Hofman_SwellingBehaviorUPuZr]] — Hofman (1990) identifies the same grain boundary tearing mechanism in U-Pu-Zr α-phase
- [[wiki/summaries/1992_Rest_CavitationalSwellingAlphaUPuZr|1992_Rest_CavitationalSwellingAlphaUPuZr]] — Rest's cavitational model addresses void formation in α-U phase of metallic fuels

## Related Work
- [[wiki/summaries/1990_Hofman_SwellingBehaviorUPuZr|1990_Hofman_SwellingBehaviorUPuZr]] — Hofman 在 U-Pu-Zr 中观察到相同的 α-U 晶界撕裂机制，与本文 U-10Mo 中的晶间开裂现象直接对应
- [[wiki/summaries/2005_Rest_RecrystallizationSwellingUO2UMo|2005_Rest_RecrystallizationSwellingUO2UMo]] — Rest 的再结晶模型覆盖 U-10Mo，与本文 γ 相稳定性问题互补
- [[wiki/summaries/2011_Kim_FissionProductInducedSwellingUMo|2011_Kim_FissionProductInducedSwellingUMo]] — Kim (2011) 在现代 U-Mo 燃料中系统量化了裂变产物诱导肿胀，是本文早期工作的后续发展
- [[wiki/summaries/2008_Kim_IntergranularFGBubblesUMo|2008_Kim_IntergranularFGBubblesUMo]] — Kim (2008) 详细表征了 U-Mo 晶间气泡，与本文观察的晶间空洞形成机制一致
- [[wiki/entities/FuelAlloy|FuelAlloy]] — U-10Mo 合金的相稳定性与辐照行为是本文核心主题
- [[wiki/concepts/SwellingMechanisms|SwellingMechanisms]] — 本文描述的晶间空洞形成是低温肿胀机制的重要实例
