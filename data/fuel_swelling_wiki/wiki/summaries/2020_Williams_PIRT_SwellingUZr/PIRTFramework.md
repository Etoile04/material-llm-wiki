# PIRT U-Zr — PIRT Framework & Key Equations

*Sub-page of [[2020_Williams_PIRT_SwellingUZr]]*

---

## PIRT Methodology

The Phenomena Identification and Ranking Table (PIRT) framework quantifies knowledge gaps by scoring each source variable on Impact and Knowledge ratios.

### Weighting Factor Formula

$$\text{Weighting Factor} = IR \times \frac{100 - KR}{100}$$

Where:
- **IR** = Impact Ratio: H = 100, M = 50, L = 0
- **KR** = Knowledge Ratio: K = 100, P = 50, U = 0

High weighting → significant knowledge gap → priority for future research.

---

## PIRT Results Table (Selected Source Variables)

| Source Variable | Swelling IR | Swelling KR | Swelling Weight | Redistribution IR | Redistribution KR | Redistribution Weight |
|---|---|---|---|---|---|---|
| External mechanical constraint | 100 | 50 | **50** | 100 | 50 | **50** |
| Temperature | 100 | 56 | **44** | 100 | 56 | **44** |
| Composition | 100 | 94 | 6 | 100 | 61 | **39** |
| Crystallographic texture | 50 | 38 | **31** | 50 | 38 | **31** |
| Temperature gradient | 50 | 50 | **25** | 50 | 50 | **25** |
| Fission rate | 43 | 50 | **22** | 43 | 44 | **24** |
| Grain size pre-irradiation | 43 | 50 | **22** | 43 | 50 | **22** |
| Initial porosity | 78 | 89 | 9 | 50 | 89 | 6 |
| Fission density | 100 | 100 | **0** | 100 | 100 | **0** |
| Impurities | 19 | 88 | 2 | 19 | 88 | 2 |
| Phase fraction | 14 | 81 | 3 | 14 | 61 | 5 |

---

## Key Parameters Table

| Parameter | Value | Notes |
|---|---|---|
| Operating temperature range | 550–850°C | Fast reactor conditions |
| Internal temperature gradient | 50–150°C | Centerline to cladding interface |
| Smear density (typical) | ~75% | Accommodates ~30% swelling before FCMI |
| Fuel slug diameter (EBR-II) | 0.439 cm | Sodium bonded |
| Cladding thickness (HT9) | 0.76 cm | EBR-II standard |
| Fission gas interconnection threshold | ~33% volumetric swelling | ~30% with 75% smear density |
| Solid FP swelling rate | ~1.5% per at% burnup | Volumetric |
| Rapid swelling period | 0–2 at% burnup | Fission gas driven |
| Zr redistribution range | ~0 to ~40 wt.% Zr | From initial U-10Zr |
| Constituent redistribution composition bounds | 4–36.5 wt.% Zr | Required β/γ″ phases present |
| Plenum-to-fuel ratio | >1 | Prevents excessive plenum pressure |
| Qualified burnup (EBR-II) | 10 at% | Demonstrated to 20 at% |

---

## Modeling Approaches Cited

### Constituent Redistribution
- **Thermomigration / Soret effect**: Used in BISON code (Galloway et al., 2015; Carlson et al., 2013)
  - Variables: lattice site density, diffusivity (microstructure-dependent)
  - Phase transformation driven phenomenon requiring β and γ″ phases
- **Irreversible thermodynamics** framework

### Swelling Models
- **Rest (1993)**: Fission-gas-bubble-nucleated void swelling model for α-U phase — cavitation nucleation rate correlated to temperature
- **ALFUS** (Ogata & Yokoo, 1999): Irradiation behavior analysis code for metallic fuels
- **FEAST-METAL** (Karahan & Andrews, 2013): Extended swelling models for ultra-high burnup

### Knowledge Gaps for Modeling
- No fundamental equations coupling fission gas retention to cladding stress or plenum pressure
- Interdependence of temperature, fission rate, and fission density prevents mechanistic model calibration
- Need for separate effects tests to decouple source variables

---

## Key Findings

1. **Top knowledge gaps** (highest weighted) for both swelling and redistribution:
   - External mechanical constraint (weight = 50)
   - Temperature (weight = 44)
   - Crystallographic texture (weight = 31)
   - Temperature gradient (weight = 25)

2. **Well-understood parameters** (low weighting, high KR):
   - Fission density (IR = 100, KR = 100 → weight = 0)
   - Hydrostatic pressure

3. **Critical need for decoupling** temperature, fission rate, and composition — historically convoluted in EBR-II tests

4. **Composition effects on redistribution:** 2 wt.% Zr variation produces noticeably different microstructure; no detailed kinetics studies exist

5. **Recommendation:** Separate effects irradiation tests (e.g., thin foils) to isolate source variables

---

## See Also

- [[2020_Williams_PIRT_SwellingUZr]] — index page
- [[2020_Williams_PIRT_SwellingUZr/PhysicalMechanisms]] — swelling and redistribution mechanisms
- [[2020_Williams_PIRT_SwellingUZr/ExperimentalData]] — historic irradiation data
- [[1993_Rest_VoidSwellingAlphaU]] — Rest swelling model referenced here
- [[2013_Karahan_FEAST_METAL_FuelSwelling]] — FEAST-METAL model
- [[entities/FissionGasDiffusion]] — diffusion theory underpinning redistribution models
