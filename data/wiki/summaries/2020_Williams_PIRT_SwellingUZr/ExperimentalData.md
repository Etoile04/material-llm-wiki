# PIRT U-Zr — Experimental Data & JSRT Relevance

*Sub-page of [[2020_Williams_PIRT_SwellingUZr]]*

---

## Historic Irradiation Programs

- **EBR-II**: Thousands of U-Zr fuel pins irradiated over 30 years; qualified envelope reached 10 at% burnup, demonstrated to 20 at%
- **FFTF**: Fast Flux Test Facility, complementary irradiation data
- **AFC series** (Advanced Fuel Campaign): Low burnup tests at INL's Advanced Test Reactor

---

## Key Experimental Observations

### Swelling vs. Burnup
- Rapid swelling 0–2 at% burnup (fission gas driven)
- ~33% volumetric swelling threshold for gas interconnection
- Solid FP swelling: ~1.5%/at% burnup (Ogata et al., 2012)

### Constituent Redistribution
- Out-of-pile tests confirmed Zr migration up temperature gradient (Ogawa et al., 1991; Sohn et al., 2000)
- Redistribution observed in all U-X Zr alloys (X = 4–36.5 wt.%)
- Redistribution accelerated by irradiation but mechanism not fully decoupled from temperature effects

### Smear Density Effects
- 75% smear density allows ~30% swelling before cladding contact
- Lower smear densities reduce FCMI risk

### Texture Effects
- Out-of-pile annealing of U-10Zr shows combination of texture loss (α-U) and texture memory (δ U-Zr₂)
- Historic fissium fuels show complete loss of initial grain structure after irradiation

---

## Relevance to JSRT Model

### Parameters for JSRT Calibration

| Parameter | Value/Range | Source |
|---|---|---|
| Solid FP swelling rate | 1.5% per at% burnup | Ogata et al., 2012 |
| Gas interconnection threshold | ~33% volumetric | Hofman et al., 1990 |
| Operating T range | 550–850°C | Multiple sources |
| Radial ΔT | 50–150°C | Typical EBR-II |
| Zr redistribution range | 0–40 wt.% | Harp et al., 2017 |
| Applicable Zr range | 4–36.5 wt.% | Phase diagram |
| Smear density (typical) | ~75% | EBR-II standard |

### Model Structure Implications
- Swelling model should be **phase-specific** (different rates in α, δ, β, γ phases)
- Temperature-dependent cavitation nucleation model needed
- Constituent redistribution model needs coupled thermal-compositional gradient framework
- Mechanical constraint (cladding contact) affects swelling anisotropy — needs stress-dependent term
- Solid FP swelling is approximately linear with burnup and can be treated as a baseline

### Key References

- Rest, J. (1993). *J. Nucl. Mater.* 207, 192–204 — Fission gas bubble void swelling model
- Hofman et al. (1996). *J. Nucl. Mater.* 227, 277–286 — Temperature gradient driven constituent redistribution
- Galloway et al. (2015). *Nucl. Eng. Des.* — BISON constituent redistribution model
- Ogata et al. (2012). *Comprehensive Nuclear Materials* — Metal fuel performance modeling
- Hofman et al. (1990). *Metall. Trans. A* 21, 517–528 — U-Pu-Zr swelling behavior

---

## See Also

- [[2020_Williams_PIRT_SwellingUZr]] — index page
- [[2020_Williams_PIRT_SwellingUZr/PhysicalMechanisms]] — mechanisms overview
- [[2020_Williams_PIRT_SwellingUZr/PIRTFramework]] — PIRT methodology
- [[1990_Hofman_SwellingBehaviorUPuZr]] — Hofman swelling reference
- [[1993_Rest_VoidSwellingAlphaU]] — Rest void swelling model
- [[2016_Sun_NeutronRadiographyU10ZrSwelling]] — U-10Zr swelling experiments
- [[entities/FuelAlloy]] — U-Zr alloy system context
