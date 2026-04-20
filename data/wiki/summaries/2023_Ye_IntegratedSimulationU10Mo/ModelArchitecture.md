# Integrated Simulation U-10Mo — Model Architecture & Calibration

*Sub-page of [[2023_Ye_IntegratedSimulationU10Mo]]*

---

## DART Code Architecture

- **Two branches**: dispersion fuel and monolithic fuel
- **Shared**: thermal models (coolant → oxide → cladding → fuel centerline)
- **Monolithic-specific**: GRASS module for fission gas behavior

### Three-Level Meshing

| Level | Nodes | Purpose |
|-------|-------|---------|
| Level-1 (x, z) | Spatial grid | Thermal / power calculations |
| Level-2 (k) | 4 grain sizes | Different initial grain sizes (1.34, 4.36, 8.5, 17 μm) |
| Level-3 (p) | 50 segments per k-node | Track grain subdivision progression |

### Parallelization
- MPI-based parallel computation for GRASS calculations across (x, z) nodes

---

## GRASS Module

- Rate-theory-based mechanistic fission gas behavior model
- Tracks bubble nucleation, re-solution, and growth at:
  - Bulk (intragranular)
  - Grain face
  - Grain edge
  - Grain corner
- Solves coupled nonlinear ODEs for bubble size distributions
- Uses **Ronchi hard-sphere EOS** for bubble size calculation
- Outputs: total porosity + intra/intergranular bubble size distributions

---

## Recrystallization Model

- Phase-field-predicted grain-size-specific kinetics (Hu et al., 2017)
- 4 grain sizes calculated: 1.34, 4.36, 8.5, 17 μm
- Upon recrystallization: grain size → 0.5 μm
- Gas sweeping: all intragranular gas swept to boundaries (one-off event)

---

## Thermal Conductivity Model

- Bruggeman model: U-Mo treated as composite of gas bubbles + U-Mo matrix

---

## Calibration Data (RERTR-5, ATR)

| Plate | FD (10²¹ fis/cm³) | Fission Rate (10¹⁴ fis/cm³/s) | Temp (°C) | Grain Size (μm) | Avg Bubble Ø (μm) | Recrystallized? |
|-------|-------------------|-------------------------------|-----------|-----------------|-------------------|----------------|
| V6018G | 2.31 | 2.3 | 121 | 4.9 ± 2.0 | 0.14 | No |
| V6019G | 2.91 | 2.9 | 142 | 8.5 ± 3.6 | 0.16 | No |
| V8005B | 2.41 | 2.4 | 170 | 8.1 ± 4.5 | 0.16 | No |

---

## Key Findings

1. **Grain size effect**: Larger grains → less swelling. 1.34 μm grain fuel completes recrystallization earliest.

2. **Recalibrated parameters significantly different from previous UO₂-based values**: Surface energy 1850 vs 200 dyn/cm, activation energy 40,559 vs 33,000 cal, $D_0$ reduced by ~2 orders of magnitude.

3. **Swelling rate transition** at ~3–3.5 × 10²¹ fis/cm³ coincides with grain subdivision onset.

4. **Corner bubbles dominate porosity** at high burnup after recrystallization. Face and edge porosities are transient peaks during grain subdivision.

5. **Sensitivity results**:
   - $D_0$ and $z$: increase shifts bubble distribution to larger sizes
   - $f_N$ and $f_{N\text{-GB}}$: increase shifts distribution to smaller sizes (more nucleation)
   - $b_0$: decrease increases porosity (less re-solution)
   - FaceCovMax: sensitive at high burnup; lower values → more swelling
   - $\lambda$: insensitive in tested range

6. **Calculated swelling for all 4 grain sizes bounds the experimental correlation**, validating the model.

---

## JSRT Relevance

| Contribution | Detail |
|---|---|
| Core rate-theory framework | GRASS module = Rest's methodology → same ODEs JSRT builds upon |
| U-10Mo specific parameters | Table 3 most recent calibrated set, replaces UO₂-derived values |
| Grain subdivision model | Phase-field-based grain-size-specific recrystallization kinetics |
| Multi-scale integration | DFT + MD → phase-field → engineering code pipeline |
| Gas sweeping mechanism | Abrupt porosity increase during recrystallization |
| Solid FP swelling | $\Delta V/V_0 = 4.0 \times F_D$ — non-gaseous swelling baseline |

---

## See Also

- [[2023_Ye_IntegratedSimulationU10Mo]] — index page
- [[2023_Ye_IntegratedSimulationU10Mo/PhysicalMechanisms]] — mechanism descriptions
- [[2023_Ye_IntegratedSimulationU10Mo/KeyEquations]] — all model equations and parameters
- [[2021_Robinson_PredictiveSwellingUMoMonolithic]] — swelling correlation used for validation
- [[2025_Hanson_StablePredictableSwellingU10Mo]] — subsequent experimental validation
- [[2016_Hu_GrainMorphologyGasBubbleUMo]] — phase-field grain subdivision kinetics (Hu et al., 2017)
- [[entities/Recrystallization]] — grain subdivision model theory
- [[entities/RateTheory]] — rate-theory ODE framework
