# Swelling of U-Mo Monolithic Fuel: Developing a Predictive Swelling Correlation

## Metadata
- **Title:** Swelling of U-Mo Monolithic Fuel: Developing a Predictive Swelling Correlation under Research Reactor Conditions
- **Authors:** A.B. Robinson, W.J. Williams, W.A. Hanson, B.H. Rabin, N.J. Lybeck, M.K. Meyer
- **Year:** 2021
- **Journal:** Journal of Nuclear Materials, 544, 152703
- **DOI:** 10.1016/j.jnucmat.2020.152703
- **Affiliations:** Idaho National Laboratory
- **Fuel System:** U-10Mo monolithic plate-type fuel (HPRR program)

## Physical Mechanisms

### Solid Fission Product Swelling
- Dominant at low-to-medium fission density
- 2-4% per 10²¹ fissions/cm³ (Hofman & Walter estimates)
- Linear with fission density, largely independent of temperature, fabrication, and irradiation conditions

### Gaseous Fission Product Swelling
- Xe and Kr precipitate into gas bubbles
- Nano-bubble superlattice (FCC): 2-3 nm diameter, 11-12 nm lattice parameter
- Stable up to ~3×10²¹ fissions/cm³
- At 2.5-3.5×10²¹ fissions/cm³: grain refinement onset → additional GB surface → intergranular bubble nucleation
- Bubble superlattice collapse releases over-pressurized gas to new sub-micron grain boundaries
- At highest fission densities: localized amorphization of γ-(U,Mo)

### Irradiation-Assisted Creep
- Causes fuel relocation (not volumetric change)
- Cladding constrains swelling to plate thickness direction only

### Interaction Layer Formation
- Contributes to dimensional changes

## Key Equations

### Recommended Swelling Correlation (Eq. 17)
$$\%\text{ Swelling} = 6.13 \times 10^{-43} f_d^2 + 4.00 \times 10^{-21} f_d$$

where $f_d$ = fission density in fissions/cm³.

### Prediction Bounds (binned data, Eq. 18-19)
$$\text{Lower} = 5.87 \times 10^{-43} f_d^2 + 4.14 \times 10^{-21} f_d - 5.28$$
$$\text{Upper} = 6.39 \times 10^{-43} f_d^2 + 3.86 \times 10^{-21} f_d + 5.28$$

### Prediction Bounds (raw data, Eq. 20-21)
$$\text{Lower} = 6.12 \times 10^{-43} f_d^2 + 4.00 \times 10^{-21} f_d - 14.79$$
$$\text{Upper} = 6.13 \times 10^{-43} f_d^2 + 4.00 \times 10^{-21} f_d + 14.79$$

### Historical Models Compared

**Kim-Hofman (Eq. 11-12):**
- $f_d \leq 3 \times 10^{21}$: $(\Delta V/V_0)_f = 5.0 \cdot f_d$
- $f_d > 3 \times 10^{21}$: $(\Delta V/V_0)_f = 15 + 6.3(f_d - 3) + 0.33(f_d - 3)^2$

**Rest (Eq. 8-10):**
- Solid: $(\Delta V/V_0)_s = 3.5 \times 10^{-21} f_d$
- Gas ($f_d \leq 3 \times 10^{21}$): $(\Delta V/V_0)_g = 1.8 \times 10^{-21} f_d$
- Gas ($f_d > 3 \times 10^{21}$): $(\Delta V/V_0)_g = 5.4 + 2.1 \times 10^{-21}(f_d - 3 \times 10^{21}) + 0.43 \times 10^{-42}(f_d - 3 \times 10^{21})^2$

### Local Fuel Swelling Calculation (Eq. 16)
$$\%\text{ Fuel Swelling} = \frac{(t_p - \frac{1}{1.975}t_{ox}) - t_{p0}}{(t_f - 2t_{Zr})} \times 100\%$$

## Parameters

| Parameter | Value | Notes |
|-----------|-------|-------|
| Data points | 18,000+ | 74 irradiated plates |
| Experiments | AFIP-3BZ, AFIP-4, RERTR-9, RERTR-10, RERTR-12, AFIP-6MkII, AFIP-7 | |
| Plate thickness | 1.27 mm | standard |
| Fuel foil thickness | 0.254, 0.508, 0.635 mm | RERTR-12 variants |
| Peak power density | 2,200-40,000 W/cm³ | range across experiments |
| Fission density range | 0.35-10.7 × 10²¹ fissions/cm³ | |
| Operating temperature | <250°C | research reactor conditions |
| Cladding | AA6061 Al alloy | |
| Diffusion barrier | Zr | hot co-rolled |
| Bin size | 100 data points | selected method |

## Experimental Data

### PIE Methods
- Post-irradiation profilometry (primary)
- Immersion density (Archimedes method) for plate-average
- Optical microscopy
- Ultrasonic testing
- Eddy current for oxide thickness

### Key Data Sets
- RERTR-12: 56 mini-plates, 4 pillowed (excluded), 52 analyzed
- AFIP-6MkII: Higher swelling than other experiments at same fission density
- Recrystallization range: 3.0-4.5 × 10²¹ fissions/cm³

### Validation
- Recommended correlation validated against RERTR-12 immersion density data
- Kim-Hofman model underpredicts at fission densities >5.0×10²¹ fissions/cm³

## Key Findings

1. **Quadratic fit** selected (R² > 96%); constrained through origin
2. No **power or temperature dependence** assumed for swelling rate (all models to date)
3. **AFIP-6MkII** shows higher swelling in recrystallization regime (possibly due to earlier recrystallization onset from Mo variations, impurities, or higher power density/temperature)
4. **Piecewise linear** fit rejected due to instability of inflection point location
5. Recrystallization occurs **gradually** over a range, not at a sharp threshold
6. Binned data (100 points/bin) with quadratic fit provides most robust correlation
7. **Breakaway swelling** not observed in U-10Mo monolithic fuel within tested range

## Relationships to Other Work

- **Kim & Hofman (2011, 2013):** Previous correlation; underpredicts at high fission density
- **Rest (2016):** Mechanistic model comparison
- **Leenaers (2013):** U-7Mo dispersion fuel (different system)
- **Perez & Robinson (INL report):** Statistical approach to swelling data
- **Wachs (unpublished):** Ultrasonic testing-based correlation
- **Williams et al. (2015):** PIE report showing accelerated swelling
- **Beeler et al. (2020):** Xe bubble EOS for γU-Mo (this batch)
- **Hu et al. (2020):** Defect cluster model for recrystallization zone (this batch)
- **Mohamed et al. (2019):** MURR LEU plate FEA using these correlations (this batch)

## Relationships

- [[wiki/entities/FuelAlloy|FuelAlloy]] — U-10Mo monolithic plate fuel swelling correlation from 74 irradiated plates is the central contribution
- [[wiki/concepts/SwellingMechanisms|SwellingMechanisms]] — solid FP + gaseous FP swelling and nano-bubble superlattice collapse are described
- [[wiki/entities/Recrystallization|Recrystallization]] — gradual recrystallization onset at 2.5–3.5×10²¹ f/cm³ drives the quadratic swelling increase
- [[wiki/entities/GasBubbleSuperlattice|GasBubbleSuperlattice]] — nano-bubble superlattice collapse at ~3×10²¹ f/cm³ is a key mechanism discussed
- [[wiki/concepts/SwellingModelComparison|SwellingModelComparison]] — Robinson correlation is compared with Kim-Hofman and Rest models
- [[wiki/summaries/2011_Kim_FissionProductInducedSwellingUMo|2011_Kim_FissionProductInducedSwellingUMo]] — Kim-Hofman correlation that this updated model supersedes at high fission densities
- [[wiki/summaries/2019_Mohamed_MURRLEU10MoSwellingCreep|2019_Mohamed_MURRLEU10MoSwellingCreep]] — MURR LEU FEA that uses these correlations
