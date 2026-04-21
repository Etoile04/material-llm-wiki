# PIRT U-Zr — Physical Mechanisms

*Sub-page of [[2020_Williams_PIRT_SwellingUZr]]*

---

## Fuel Swelling Mechanisms

Three main driving forces for fuel swelling in U-Zr:

1. **Solid and gaseous fission product accumulation** — Intrinsic to fission events; unavoidable
2. **Mechanical cavitation from anisotropic crystal growth** — Crystallographic anisotropy in α-U (orthorhombic) and δ U-Zr₂ (hexagonal P6/mmm) phases causes preferential radial swelling
3. **Defect-induced growth from interstitial and vacancy loops** — Irradiation-induced defects nucleate cavitation voids on grain boundaries, increasing swelling beyond fission-induced swelling alone

**Key characteristics:**
- Rapid swelling occurs until ~2 at% burnup, driven by fission gas generation
- Majority of radial growth occurs at ~1–2 at% burnup before fuel-cladding contact
- Anisotropic swelling: preferential radial direction over axial
- At ~33% volumetric swelling, fission gas porosity becomes interconnected → gas released to plenum → swelling rate dramatically decreases
- Solid fission products contribute ~1.5% volumetric swelling per 1 at% burnup

**Fission gas bubble evolution:**
- Damage-induced vacancies and gas atoms migrate to sinks (grain boundaries)
- Coalesce and nucleate into fission gas bubbles
- Bubble nucleation induces swelling until porosity interconnects
- Temperature-dependent: cavitation void nucleation ability directly correlated to fuel temperature

---

## Constituent Redistribution (Thermomigration)

**Mechanism:** Zr atoms migrate up the temperature gradient toward the hotter fuel center (Soret effect / thermodiffusion).

**Resulting three-zone structure:**
- **Center:** Zr-rich zone (~40 wt.% Zr possible from initial U-10Zr)
- **Middle ring:** Zr-depleted zone (nearly pure U)
- **Outer ring:** Partial Zr enrichment adjacent to cladding

**Driving forces:**
- Thermal gradient (centerline to cladding): typically 50–150°C
- Compositional gradient
- Phase transformation driven: redistribution requires presence of β and γ″ phases
- Accelerated by irradiation (radiation-enhanced diffusion, though considered negligible compared to thermal diffusion at operating temperatures)

**Applicable composition range:** Any U-X wt.%Zr alloy where X = 4–36.5 wt.% (10–60 at%), as required phases are present.

---

## Four Performance-Limiting Phenomena

1. **Fuel swelling** — fission-gas and solid-FP driven
2. **Constituent redistribution** — Soret-effect thermodiffusion of Zr
3. **Fuel-Cladding Chemical Interaction (FCCI)** — U and lanthanide FP interdiffusion into cladding; Ni/Fe back-diffusion lowers solidus temperature
4. **Fuel-Cladding Mechanical Interaction (FCMI)** — mitigated by ≤75% smear density and plenum/fuel ratio > 1; not life-limiting to 10 at% burnup

---

## Crystal Phase vs. Temperature

| Radial Region | Temperature Range | Phases |
|---|---|---|
| Peripheral (cool) | ~550–650°C | α + δ |
| Intermediate | ~650–750°C | β + γ″ |
| Center (hot) | ~750–850°C | γ′ → γ |

**Swelling anisotropy crystal structures:**
- α-U: orthorhombic → anisotropic
- δ U-Zr₂: modified C32 (P6/mmm hexagonal) → anisotropic
- γ phase: cubic BCC → isotropic behavior above transition

---

## See Also

- [[2020_Williams_PIRT_SwellingUZr]] — index page
- [[2020_Williams_PIRT_SwellingUZr/PIRTFramework]] — PIRT methodology and weighting results
- [[2020_Williams_PIRT_SwellingUZr/ExperimentalData]] — historic irradiation programs
- [[2021_Hilty_FissionGasBubblesThermalConductivity]] — fission gas bubble thermal effects
- [[2023_Ye_IntegratedSimulationU10Mo]] — integrated swelling simulation
- [[entities/RateTheory]] — bubble nucleation and growth theory
- [[entities/CavitationalVoid]] — void swelling mechanisms
