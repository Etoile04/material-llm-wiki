# Stable and Predictable Swelling U-10Mo — Swelling Model & Statistical Analysis

*Sub-page of [[2025_Hanson_StablePredictableSwellingU10Mo]]*

---

## Swelling Calculation Equations

### Full Form (Eq. 1)

$$\text{Fuel Swelling Fraction} = \frac{t_{\text{post-plate}} - \left(1 - \frac{1}{1.975}\right) t_{\text{ox}} - t_{\text{pre-plate}}}{t_{\text{pre-foil}} - 2t_{\text{Zr}}}$$

Where:
- $t_{\text{post-plate}}$: post-irradiation plate thickness
- $t_{\text{pre-plate}}$: pre-irradiation plate thickness
- $t_{\text{pre-foil}}$: pre-irradiation fuel-foil thickness after Zr roll-bonding
- $t_{\text{ox}}$: post-irradiation oxide thickness
- $t_{\text{Zr}}$: as-fabricated Zr diffusion barrier thickness per foil side
- **1.975**: Pilling-Bedworth ratio for U oxide (volume correction factor)

### Simplified Form (Eq. 2 — oxide neglected)

$$\text{Fuel Swelling Fraction} = \frac{t_{\text{post-plate}} - t_{\text{pre-plate}}}{t_{\text{pre-foil}} - 2t_{\text{Zr}}}$$

Oxide correction neglected because oxide growth was on the order of the BONA4INL measurement bench resolution (±3 µm).

---

## Recommended U-10Mo Swelling Model (Robinson et al.)

- **Type**: Empirical quadratic fit of binned fuel swelling vs. fission density
- **Training data**: ~18,000 data pairs from historical experiments (AFIP-7, AFIP-3BZ, AFIP-6MKII)
- **Output**: 95% confidence band and 95% prediction bounds
- **Reference**: Robinson et al., *J. Nucl. Mater.* 544 (2020) 152703

### Model Parameters for JSRT Calibration

| Parameter | Value |
|-----------|-------|
| Fit type | Quadratic through origin |
| FD transition point (grain refinement onset) | ~3 × 10²¹ f/cm³ |
| FD threshold (full HBS) | ~5 × 10²¹ f/cm³ |
| Zr diffusion barrier thickness | ~25.4 µm per side |
| Pilling-Bedworth ratio (U oxide) | 1.975 |

---

## Statistical Analysis Method

1. Local swelling fraction and fission density data pairs consolidated by fabricator and fuel-foil geometry
2. Data pairs shuffled and resorted by local fission density to remove geometric/constraint biases
3. Binned by every nearest 100 data points (by fission density)
4. Quadratic fits constrained through origin performed on binned and raw datasets
5. **95% confidence bands**: degree of confidence in empirical fit → detect statistical differences between B and C-plate models
6. **95% prediction bands**: probability of next datapoint location → validate MP-1 data falls within bounds

---

## JSRT Contributions

| Element | Value for JSRT |
|---|---|
| Empirical swelling correlation | Quadratic model with quantified confidence/prediction bands → validated baseline |
| Fission density thresholds | ~3 × 10²¹ f/cm³ (grain refinement onset), ~5 × 10²¹ f/cm³ (full HBS) |
| Plate geometry constraint factors | Axial/transverse constraint → thickness change = volumetric swelling |
| Stable swelling confirmation | No breakaway to ~6 × 10²¹ f/cm³ → safety margin bounds |
| Mo homogeneity effect | Initial microstructure significantly affects swelling trajectory → manufacturing tolerance |

---

## See Also

- [[2025_Hanson_StablePredictableSwellingU10Mo]] — index page
- [[wiki/summaries/2025_Hanson_StablePredictableSwellingU10Mo/PhysicalMechanisms|2025_Hanson_StablePredictableSwellingU10Mo/PhysicalMechanisms]] — microstructural mechanisms
- [[wiki/summaries/2025_Hanson_StablePredictableSwellingU10Mo/ExperimentalData|2025_Hanson_StablePredictableSwellingU10Mo/ExperimentalData]] — MP-1 experiment details
- [[wiki/summaries/2021_Robinson_PredictiveSwellingUMoMonolithic|2021_Robinson_PredictiveSwellingUMoMonolithic]] — the recommended empirical swelling model (quadratic fit)
- [[2023_Ye_IntegratedSimulationU10Mo]] — mechanistic model predicting the same swelling transitions
- [[wiki/summaries/2022_Hanson_EMPIrESwellingAnalysis|2022_Hanson_EMPIrESwellingAnalysis]] — swelling analysis methodology development
- [[wiki/summaries/2026_FigueroaBengoa_HighBurnupPorosityUMo|2026_FigueroaBengoa_HighBurnupPorosityUMo]] — high burnup porosity for context beyond MP-1 range
