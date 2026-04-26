# Stable and Predictable Swelling U-10Mo — Experimental Data

*Sub-page of [[2025_Hanson_StablePredictableSwellingU10Mo]]*

---

## MP-1 Experiment Design

### LP Thick Fuel vs. MP Thin Fuel

| Parameter | LP Thick Fuel | MP Thin Fuel |
|-----------|---------------|--------------|
| Nominal fuel foil thickness | 0.6350 mm | 0.2159 mm |
| C-plates (commercial, homogenized) | 34 | 28 |
| B-plates (baseline, no homogenization) | 8 | 4 |
| Total plates | 42 | 32 |
| ATR irradiation position | B-position | South Flux Trap |
| Average peak power density | 5–10 kW/cm³ | 20–35 kW/cm³ |
| EOL fission density range | 0.63–3.15 × 10²¹ f/cm³ | 2.52–6.11 × 10²¹ f/cm³ |

---

## Fuel Design Parameters

| Parameter | Value |
|-----------|-------|
| Plate dimensions | 101.47 × 25.4 × 1.24 mm (nominal) |
| Zr diffusion barrier | ~25.4 µm thick per side, hot-roll bonded |
| Cladding | Al-alloy 6061 |
| Measurement resolution | ±3 µm thickness, ±20 µm location |
| Measurement bench | BONA4INL |
| Measurement grid | 1 × 2 mm |
| Total MP-1 data points | ~47,000 swelling-fission density pairs |

---

## Swelling Comparison Results

- Both B and C-plate data fall within **95% prediction band** of the recommended Robinson et al. model
- B-plates show **statistically higher swelling** than C-plates at all fission densities tested (non-overlapping 95% confidence bands)
- C-plate confidence band overlaps with recommended model at low fission density but diverges at moderate-to-high FD (lower swelling observed)
- B-plate model overlaps with recommended model at highest FD tested
- At high FD (> 5 × 10²¹ f/cm³): ~8,500 MP-1 data pairs vs. ~850 in historical model — significant improvement in data density

---

## Historical Experiment Contributions to Recommended Model

| Experiment | Fission Density Range | Notes |
|---|---|---|
| AFIP-7 | ~1.5–3 × 10²¹ f/cm³ | Homogenized microstructure; > 6,700 data pairs |
| AFIP-3BZ | ~2.5–4.5 × 10²¹ f/cm³ | Appears homogeneous despite no explicit homogenization |
| AFIP-6MKII | ~4–5.5 × 10²¹ f/cm³ | Heterogeneous microstructure despite homogenization; 1,950 data pairs; primary contributor at this regime |

---

## Key Findings

1. **Commercially fabricated U-10Mo fuel performs within the recommended swelling model's predictions**, validating commercial-scale fabrication.

2. **Homogenization anneal produces measurable but small reduction in swelling** at all fission densities tested — uniform Mo distribution prevents early grain refinement.

3. **Non-homogenized B-plates show systematically higher swelling** (statistically significant) due to Mo chemical banding → increased grain boundary density → early fission gas porosity.

4. **No evidence of imminent breakaway swelling** in either B or C-plates — bubbles remain discrete and stable up to ~6 × 10²¹ f/cm³.

5. **The recommended Robinson et al. model is conservative** — it predicts upper bounds of scatter for both fabrications.

6. **Model divergence from C-plate behavior** at moderate FD is likely due to AFIP-6MKII's heterogeneous microstructure biasing the historical model toward B-plate-like behavior.

---

## See Also

- [[2025_Hanson_StablePredictableSwellingU10Mo]] — index page
- [[wiki/summaries/2025_Hanson_StablePredictableSwellingU10Mo/PhysicalMechanisms|2025_Hanson_StablePredictableSwellingU10Mo/PhysicalMechanisms]] — microstructural mechanisms
- [[wiki/summaries/2025_Hanson_StablePredictableSwellingU10Mo/SwellingModel|2025_Hanson_StablePredictableSwellingU10Mo/SwellingModel]] — empirical model equations and statistical analysis
- [[wiki/summaries/2021_Robinson_PredictiveSwellingUMoMonolithic|2021_Robinson_PredictiveSwellingUMoMonolithic]] — the recommended empirical swelling model
- [[wiki/summaries/2022_Hanson_EMPIrESwellingAnalysis|2022_Hanson_EMPIrESwellingAnalysis]] — earlier EMPIrE swelling analysis methodology
- [[entities/GasBubbleSuperlattice]] — FCC superlattice collapse at intermediate FD
