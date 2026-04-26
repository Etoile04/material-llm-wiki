# Lower Length Scale Informed Improvements to Bison U-Pu-Zr Fuel Swelling Model

## Metadata
- **Title:** Lower length scale informed improvements to Bison U-Pu-Zr fuel swelling model
- **Authors:** Larry Aagesen, Andrea Jokisaari, Jia-Hong Ke
- **Year:** 2020
- **Journal:** INL/EXT-20-59990 (Technical Report)
- **DOI:** 10.2172/1670431
- **Affiliations:** Idaho National Laboratory
- **Fuel System:** U-(Pu)-Zr metallic fuel (fast reactor)

## Physical Mechanisms

### High-Temperature Swelling (γ phase, BCC, >600°C/873K)
- Gaseous swelling dominates over solid swelling
- Large spherical bubbles: diameters on order of tens of microns
- Uniform size distribution assumed in BISON
- Bubble interconnection → gas release → swelling ceases
- Two BISON models parameterized: UPuZrGaseousEigenstrain and ADFissionGasViscoplasticityStressUpdateBase

### Low-Temperature Swelling (α-U phase, <600°C/873K)
- Morphologically distinct: elongated porosity with ragged edges
- Mechanism: **mechanical cavitation** from irradiation-induced crystal shape changes
- α-U crystals shrink in [100], grow in [010], unchanged in [001]
- Internal strains: hundreds of MPa at burnup ~0.001% FIMA
- Plastic deformation alone does NOT increase pore volume
- **Burnup eigenstrain** (irradiation-induced crystal shape change) increases existing porosity volume and makes it anisotropic

### Cluster Dynamics (Early-Stage Fission Gas)
- Xe clustering in γ phase at early stages
- Extremely low Xe solubility → large density of fission gas clusters
- Growth assisted by vacancy mechanism and radiation-induced point defects

## Key Equations

### Gaseous Swelling - UPuZrGaseousEigenstrain (Eq. 1)
$$\left(\frac{\Delta V}{V_0}\right)_g = \left(\frac{3}{4\pi}\right)^{1/2}\left[\frac{kT}{2\sigma}Y_{Xe}\dot{F}t\right]^{3/2} N^{1/2}$$

where $k$ = Boltzmann constant, $T$ = temperature, $\sigma$ = surface tension, $Y_{Xe}$ = gaseous fission product yield, $\dot{F}$ = fission rate density, $t$ = time, $N$ = bubble number density.

### Interconnectivity Function (smooth step, Eq. 3)
$$I(p) = \frac{1}{1 + \exp[-M(p - p_c)]}$$

where $p$ = porosity, $p_c$ = percolation threshold, $M$ = sharpness parameter.

### Irradiation Creep (Kim model, referenced)
$$\dot{\varepsilon} = A \cdot \sigma \cdot \dot{f}$$

### Burnup Eigenstrain for α-U
$$\varepsilon_{ij}^{bu} = \beta_{ij} \cdot \text{FIMA}$$

where $\beta_{ij}$ is the anisotropic burnup shape change tensor.

## Parameters

### Interconnection Parameters (Phase-Field Results)

| Configuration | $p_c$ (percolation threshold) | $p_{0.8}$ (80% connected) |
|---|---|---|
| N = 3×10¹⁴/m³, M = 1 | ~0.18 | ~0.22 |
| N = 3×10¹⁴/m³, M = 5 | ~0.13 | ~0.16 |

**BISON Model Parameters:**
- UPuZrGaseousEigenstrain: $p_i \approx 0.20$, $p_t \approx 0.26$ (interconnection initiating/terminating porosity)
- Bubble number density: N = 3×10¹⁴/m³

### Cluster Dynamics Parameters (Table 3)
| Parameter | Value |
|-----------|-------|
| Temperature | 1000 K |
| Xe interface energy | 0.20-0.30 J/m² |
| Xe solubility | 10⁻¹³ - 10⁻¹⁰ |
| Vacancy migration barrier | 0.6-1.2 eV |
| Vacancy cluster interface energy | 0.1-0.5 J/m² |
| Vacancy formation energy | 0.6-1.4 eV |

### Sensitivity Analysis Results
- Xe solubility and vacancy migration barrier are **most sensitive** parameters
- Xe interface energy has moderate effect
- Vacancy cluster interface energy and vacancy formation energy have less effect

## Experimental Data

- Phase-field simulations of bubble interconnection with 5 random configurations
- Microstructurally resolved FEA of α-U pore growth with crystal plasticity + burnup eigenstrain
- Cluster dynamics of Xe + vacancy clustering at 1000 K

## Key Findings

1. **Percolation threshold** for bubble interconnection: $p_c \approx 0.13-0.20$ depending on mobility and density
2. **Plastic deformation does NOT increase pore size** - only changes shape
3. **Burnup eigenstrain** is the primary driver of pore volume increase in α-U at low temperature
4. Pore shape becomes **anisotropic** under burnup eigenstrain (elongated)
5. Temperature dependence of pore volume change is **weak** for burnup eigenstrain mechanism
6. **Xe solubility** and **vacancy migration barrier** are critical parameters for cluster dynamics
7. Phase-field interconnectivity results used to parameterize two BISON swelling models

## Relationships to Other Work

- **BISON fuel performance code:** Target application for model improvements
- **Previous BISON models:** Novasane et al. (UPuZrGaseousEigenstrain), Aagesen (viscoplasticity model)
- **Phase-field interconnection:** Extension of preliminary work from FY19
- **Rest (1993, 2001):** Cavitational void swelling in α-U (provides mechanistic basis)
- **Yun et al. (2022):** Cavitational void swelling model for U-10Zr (this wiki)
- **Hu et al. (2020):** Cluster dynamics + phase-field for UMo (complementary approach)
- **NEAMS program:** Sponsor of lower-length scale simulations

## Relationships

- [[wiki/entities/CavitationalVoid|CavitationalVoid]] — burnup eigenstrain in α-U drives pore volume increase, building on Rest's cavitational void model
- [[wiki/entities/PhaseFieldModeling|PhaseFieldModeling]] — phase-field simulations of bubble interconnection are used to parameterize BISON models
- [[wiki/concepts/RateTheoryFramework|RateTheoryFramework]] — cluster dynamics of Xe+vacancy clustering are core
- [[wiki/entities/FuelAlloy|FuelAlloy]] — U-Pu-Zr metallic fast reactor fuel swelling in both α and γ phases
- [[wiki/concepts/SwellingMechanisms|SwellingMechanisms]] — mechanistic separation of high-T gaseous vs. low-T cavitational swelling mechanisms
- [[wiki/summaries/1993_Rest_VoidSwellingAlphaU|1993_Rest_VoidSwellingAlphaU]] — Rest's cavitational void model provides mechanistic basis
- [[wiki/summaries/2022_Yun_CavitationalVoidSwelling|2022_Yun_CavitationalVoidSwelling]] — Yun et al. revisit Rest's model with revised parameters

## Related Work
- [[wiki/summaries/2022_Aagesen_PFBubbleInterconnection|2022_Aagesen_PFBubbleInterconnection]] — 同一团队的3D相场气泡互联模拟，提供渗流阈值参数
- [[wiki/summaries/1993_Rest_VoidSwellingAlphaU|1993_Rest_VoidSwellingAlphaU]] — α-U空洞肿胀的cavitational模型，本文低温肿胀的物理基础
- [[wiki/summaries/2020_Hu_DefectClusterGasBubbleUMo|2020_Hu_DefectClusterGasBubbleUMo]] — 团簇动力学+相场耦合模型，互补的介观方法
- [[wiki/summaries/2016_Hales_BISON_TheoryManual|2016_Hales_BISON_TheoryManual]] — BISON理论手册，本文模型集成的目标平台
- [[wiki/concepts/LowTemperatureSwellingMechanisms|LowTemperatureSwellingMechanisms]] — 低温肿胀机制的分类框架
- [[wiki/entities/BISONCode|BISONCode]] — 模型集成的燃料性能分析代码
