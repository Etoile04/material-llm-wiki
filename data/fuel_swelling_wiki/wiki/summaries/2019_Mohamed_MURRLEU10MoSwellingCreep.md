# Fuel Swelling and Creep Analysis for a MURR LEU U-10Mo Monolithic Plate

## Metadata
- **Title:** Fuel Swelling and Creep Analysis for a MURR LEU U-10Mo Monolithic Plate
- **Authors:** Walid Mohamed, Hee Seok Roh, John Stillman, Erik Wilson
- **Year:** 2019
- **Journal:** ANL/RTR/TM-18/19 (Technical Report, Argonne National Laboratory)
- **DOI:** N/A
- **Affiliations:** Argonne National Laboratory
- **Fuel System:** U-10Mo monolithic plate (MURR LEU conversion)

## Physical Mechanisms

### Fuel Swelling
- Combined solid + gaseous fission product swelling
- Confined to plate thickness direction by cladding constraint
- Thickness change attributed to swelling + irradiation creep (fuel relocation)

### Irradiation Creep
- Kim et al. model: $\dot{\varepsilon} = A \cdot \sigma \cdot \dot{f}$
- Causes fuel relocation (no net volume change)
- Affects stress distribution and thickness profiles
- Creep rate coefficient uncertain; sensitivity analysis performed

### Thermal Conductivity Degradation
- Porosity from fission gas bubbles reduces thermal conductivity
- Modeled as function of porosity

## Key Equations

### Kim Swelling Correlation (Eq. 1-2)
- $f_d \leq 3 \times 10^{27}$ fissions/m³: $(\Delta V/V_0)_f = 5.0 \times f_d$ (%)
- $f_d > 3 \times 10^{27}$: $(\Delta V/V_0)_f = 15 + 6.3(f_d - 3) + 0.33(f_d - 3)^2$ (%)

### INL Swelling Correlation (Eq. 3, excluding AFIP-6 MKII)
$$\%\text{ Swelling} = 3.83 \times 10^{-21}f_d^2 + 4.54 \times 10^{-21}f_d$$

### 95% UCL Swelling (Eq. 4, including AFIP-6 MKII)
$$\%\text{ Swelling} = 6.39 \times 10^{-43}f_d^2 + 3.86 \times 10^{-21}f_d + 5.28$$

### Irradiation Creep (Eq. 5)
$$\dot{\varepsilon} = A \cdot \sigma \cdot \dot{f}$$

where $A$ = creep rate coefficient (cm³/MPa-fission), $\sigma$ = equivalent stress (MPa), $\dot{f}$ = fission rate (fissions/cm³·s)

## Parameters

### Plate 23 Geometry (Table 2)

| Section | Thickness (mm) | Length (mm) | Width (mm) |
|---------|---------------|-------------|-----------|
| U-10Mo fuel core | 0.4318 | 609.6 | 102.81 |
| Zr barrier (each side) | 0.0254 | 609.6 | 102.81 |
| AA6061 cladding (each side) | 0.381 | 647.7 | 109.72 |

### Irradiation Conditions (Table 1)

| Time (hr) | Avg Power (W/cm³) | Avg Fission Density (fissions/m³) |
|-----------|-------------------|----------------------------------|
| 48 | 5982 | 3.20×10²⁵ |
| 1258 | 5776 | 8.26×10²⁶ |
| 1560 | 5746 | 1.02×10²⁷ |
| 2873 (EOL) | 5225 | 1.86×10²⁷ |

### FEA Model
- Element type: C3D8T (8-node thermally coupled brick)
- Total elements: 186,624
- Solver: ABAQUS
- Maximum local fission density: 2.62×10²⁷ fissions/m³ (EOL)
- Local-to-average ratio: up to ~1.4
- Coolant channel 23 (inboard): 2.3622 mm
- Coolant channel 24 (outboard): 2.4257 mm

### Creep Rate Coefficients Tested
- A = 750, 500, 250, 5 (×10⁻²⁵ cm³/MPa-fission)
- A = 500: Kim et al. calibrated value (with Kim swelling correlation)

## Experimental Data

### Material Properties
- From INL/EXT-17-40975 Rev. 1
- U-10Mo, Zr, AA6061-O properties as functions of temperature and irradiation
- Ideal bonding at all interfaces (no delamination)

### Swelling Correlation Comparison (Fig. 3)
- Kim and INL (excluding AFIP-6 MKII) agree up to ~1.8×10²⁷ fissions/m³
- INL predicts higher swelling at maximum MURR fission density
- 95% UCL is most conservative (highest swelling)

## Key Findings

### Fuel Swelling Results (Table 3)
- Fuel swelling at EOL (2.62×10²⁷ fissions/m³):
  - Kim: ~9-11%
  - INL (excl. AFIP-6): ~12-14%
  - 95% UCL: ~18-20%

### Plate Thickness Increase (Table 4)
- Maximum thickness increase depends on swelling correlation and creep coefficient
- Higher creep coefficient → more fuel relocation → more uniform thickness distribution
- Lower creep coefficient → more localized swelling at plate center
- **Most conservative case** (95% UCL, A=5): highest peak thickness increase
- **Kim correlation, A=500**: baseline case for MURR safety analysis

### Stress Analysis (Table 5)
- Peak equivalent stress in U-10Mo fuel core
- Stress levels depend on swelling magnitude and creep relaxation

### Safety Implications
- Coolant channel constriction must maintain adequate flow for heat removal
- Channel 23 (between plates 22-23) is most limiting
- Results used for margin-to-flow-instability calculations

## Relationships to Other Work

- **Kim et al. (2013):** Swelling correlation + irradiation creep model
- **INL/EXT-17-40975:** Material properties database and swelling correlations
- **Robinson et al. (2021):** Updated swelling correlation (this batch) - supersedes INL correlations
- **Beeler et al. (2020):** Xe bubble EOS (this batch) - provides thermodynamic basis
- **MURR LEU conversion program:** Application context
- **AFIP-6 MKII experiment:** Controversial data set showing higher swelling
- **RERTR campaigns:** Source of historical irradiation data

## Relationships

- [[wiki/entities/FuelAlloy|FuelAlloy]] — U-10Mo monolithic plate fuel for MURR LEU conversion is analyzed
- [[wiki/concepts/SwellingMechanisms|SwellingMechanisms]] — combined solid + gaseous fission product swelling and creep-driven relocation are modeled
- [[wiki/concepts/SwellingModelComparison|SwellingModelComparison]] — Kim, INL, and 95% UCL swelling correlations are compared
- [[wiki/summaries/2011_Kim_FissionProductInducedSwellingUMo|2011_Kim_FissionProductInducedSwellingUMo]] — Kim swelling correlation used as baseline
- [[wiki/summaries/2013_Kim_FissionInducedSwellingCreepUMo|2013_Kim_FissionInducedSwellingCreepUMo]] — irradiation creep model source
- [[wiki/summaries/2021_Robinson_PredictiveSwellingUMoMonolithic|2021_Robinson_PredictiveSwellingUMoMonolithic]] — updated swelling correlation that supersedes INL correlations used here

## Related Work
- [[wiki/summaries/2021_Robinson_PredictiveSwellingUMoMonolithic|2021_Robinson_PredictiveSwellingUMoMonolithic]] — 基于更多数据建立的U-10Mo肿胀关联，取代本文使用的INL关联
- [[wiki/summaries/2011_Kim_FissionProductInducedSwellingUMo|2011_Kim_FissionProductInducedSwellingUMo]] — 本文使用的Kim肿胀关联的原始来源
- [[wiki/summaries/2013_Kim_FissionInducedSwellingCreepUMo|2013_Kim_FissionInducedSwellingCreepUMo]] — 辐照蠕变模型的原始来源
- [[wiki/summaries/2020_Beeler_ImprovedEOSXeBubbleUMo|2020_Beeler_ImprovedEOSXeBubbleUMo]] — U-Mo中Xe气泡EOS，为肿胀模型提供热力学基础
- [[wiki/concepts/CreepSwellingCoupling|CreepSwellingCoupling]] — 蠕变与肿胀耦合机制的概念框架
- [[wiki/entities/GasBubbleSuperlattice|GasBubbleSuperlattice]] — U-10Mo中纳米气泡超点阵影响肿胀行为
