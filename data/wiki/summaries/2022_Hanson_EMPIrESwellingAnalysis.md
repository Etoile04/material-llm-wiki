# Non-Destructive Analysis of Swelling in the EMPIrE Fuel Test

## Metadata

- **Title:** Non-destructive analysis of swelling in the EMPIrE fuel test
- **Authors:** William A. Hanson, Adam B. Robinson, Nancy J. Lybeck, Joseph W. Nielsen, Bei Ye, Zhi-Gang Mei, Dennis D. Keiser Jr, Laura M. Jamison, Gerard L. Hofman, Abdellatif M. Yacout, Ann Leenaers, Bertrand Stepnik, Irina Y. Glagolenko
- **Year:** 2022
- **Journal:** Journal of Nuclear Materials, 564, 153683
- **DOI:** 10.1016/j.jnucmat.2022.153683
- **Affiliations:** INL; ANL; SCK CEN; Framatome CERCA

## Physical Mechanisms

### U-Mo Dispersion Fuel Swelling Regimes
1. **Solid fission product regime** (low fission density):
   - Gaseous fission products reside as gas atoms or in nano-bubble superlattice
   - Linear swelling behavior
   
2. **Gaseous fission product dominated regime** (intermediate, 2.5–3.5 × 10²¹ fissions/cm³):
   - Nano-bubble lattice collapses
   - Micrometer-scale bubbles form
   - Largely attributed to grain refinement/subdivision during irradiation
   - Accelerated swelling rate

3. **Breakaway swelling** (high fission density):
   - Al-U-Mo interaction layer interfaces act as fission gas sinks
   - Large bubbles form, interlink, and compromise fuel meat integrity
   - May result in "pillowing" of the plate (observed in FUTURE experiment)

### Al-U-Mo Interaction Layer Effects
- Amorphous interaction layer forms between U-Mo particles and Al matrix
- Fission gases are **insoluble** in interaction layer
- Layer interfaces serve as gas sinks → large bubble formation outside fuel particles
- Significantly increases overall plate swelling rate beyond particle swelling alone

### Coating Effects on Swelling
- **ZrN coating (PVD):** Virtually eliminates Al-U-Mo interaction layer when intact
- **ZrN coating (ALD):** Alternative application method tested
- **AlN secondary coating (ALD):** Mitigates ZrN-Al matrix interaction
- At higher fission densities: acceleration in swelling rate still observed even with intact coatings
- **Si addition to Al matrix:** Forms stable Si-U layer, reduces interaction layer

### Grain Refinement Delay Hypothesis
- Increasing initial grain size through pre-irradiation heat treatment may delay grain refinement
- Delayed refinement → delayed onset of gaseous fission product dominated swelling

## Key Equations

### Fuel Particle Swelling Fraction (Eq. 1)
$$S = \frac{\Delta V_{fuel}}{V_{fuel,0}}$$

Where $\Delta V_{fuel}$ is the dimensional growth within the fuel meat relative to initial fuel particle volume. Assumes Al matrix does not contribute to swelling.

### Local Swelling Analysis
- Based on 2D post-irradiation plate profilometry (Robinson et al.)
- Statistical methods used to separate effects of convoluted fabrication variables
- Plate constraint confines volumetric swelling to thickness direction

## Parameters

### Irradiation Conditions
| Parameter | Value |
|-----------|-------|
| Reactor | ATR (INL) |
| Meat power density | ~21 kW/cm³ |
| Max fission density | ~6.4 × 10²¹ fissions/cm³ |
| Fuel composition | U-7wt%Mo (primary), U-10wt%Mo (subset) |
| Enrichment | 19.75 ± 0.2 wt% ²³⁵U |
| Target particle diameter | ~80 µm |

### Fabrication Variables Tested
| Variable | Levels |
|----------|--------|
| Coating method | PVD (ZrN), ALD (ZrN), ALD (ZrN+AlN), uncoated |
| Heat treatment | Yes (delay grain refinement), No |
| Fines fraction | 0%, 10%, 25% |
| Fuel composition | U-7Mo, U-10Mo |
| Powder source | KAERI (large-scale), Framatome CERCA (lab-scale) |
| Coating thickness | ~1 µm (ZrN target) |

### Concurrent Experiments
- **SEMPER FIDELIS:** Full-size plate experiment at SCK CEN BR-2 reactor (Europe)
- EMPIrE designed to match BR-2 bounding conditions

## Experimental Data

### Key Findings
1. **First experiment** to test coated fuel particles (PVD and ALD ZrN) in mini-plates with comparison to full-size SEMPER FIDELIS experiment
2. **High-fidelity profilometry** enables local swelling analysis with statistical separation of fabrication variable effects
3. **Subtle and competing effects:** Some fabrication variables had subtle, others had significant (and possibly competing) effects on swelling
4. **ZrN coating effectiveness:** Intact coating virtually eliminates interaction layer, but swelling acceleration at high fission density persists
5. **Fines fraction:** Higher fines = more surface area = potentially more interaction layer volume
6. **Mo content effect:** Higher Mo (U-10Mo vs U-7Mo) → slight delay in recrystallization behavior

### Methodology
- Mini-plate profilometry → local swelling analysis → statistical methods (ANOVA-like) → separate fabrication effects
- Non-destructive evaluation allows further destructive examination of selected plates

## Relationships to Other Work

- **Robinson et al.:** Local swelling analysis methodology from profilometry — directly applied
- **SELENIUM experiment:** PVD ZrN coating methodology developed — extended with ALD in EMPIrE
- **FUTURE experiment:** Breakaway swelling and pillowing observed — motivation for coating approach
- **Kim's model:** Empirical swelling model — background for comparison
- **Ye et al. (2023):** DART code simulation — complementary modeling of monolithic fuel
- **Hanson et al. (2025):** Follow-up study on monolithic U-10Mo swelling validation
- **Gan et al. (2017):** Grain refinement and recrystallization mechanisms — theoretical basis for delay hypothesis

## Relationships

- [[wiki/entities/FuelAlloy|FuelAlloy]] — U-7Mo and U-10Mo dispersion fuels with various coatings in Al matrix are tested
- [[wiki/entities/Recrystallization|Recrystallization]] — grain refinement/subdivision drives swelling acceleration; pre-irradiation heat treatment attempts to delay it
- [[wiki/entities/GasBubbleSuperlattice|GasBubbleSuperlattice]] — nano-bubble lattice collapse at ~2.5–3.5×10²¹ f/cm³ is the onset of the gaseous FP regime
- [[wiki/concepts/SwellingMechanisms|SwellingMechanisms]] — three swelling regimes (solid FP, gaseous FP, breakaway) and coating effects on each
- [[wiki/concepts/SwellingModelComparison|SwellingModelComparison]] — statistical analysis separates contributions of fabrication variables to swelling
- [[wiki/summaries/2021_Robinson_PredictiveSwellingUMoMonolithic|2021_Robinson_PredictiveSwellingUMoMonolithic]] — Robinson's swelling correlation methodology is directly applied here
- [[wiki/summaries/2025_Hanson_StablePredictableSwellingU10Mo|2025_Hanson_StablePredictableSwellingU10Mo]] — follow-up study validating U-10Mo monolithic fuel swelling behavior
