# Fission Gas Bubbles & Thermal Conductivity — Simulation Results

*Sub-page of [[2021_Hilty_FissionGasBubblesThermalConductivity]]*

---

## Computational Approach

1. **Phase-field model** (Aagesen et al., 2018) used to create equilibrium bubble morphologies at additive interfaces in MOOSE framework
2. **Asymptotic Expansion Homogenization (AEH)** used to calculate ETC from heterogeneous microstructures
3. 2D Cartesian domain with three phases: UO₂ matrix, additive particle, Xe gas bubble

---

## Simulation Parameters

| Parameter | Value |
|-----------|-------|
| Domain size | 400 × 400 μm |
| Mesh size | 1 μm uniform |
| Additive volume fraction | 0.11 |
| Spherical particle radius | 75 μm |
| Rectangular particle size | 230 × 77 μm (3:1 aspect ratio) |
| Bubble volume fraction range | 0.003 – 0.040 (extended to ~0.10) |
| Real fuel bubble volume fractions | 0.03 – 0.12 (from literature) |

---

## Key Numerical Results

### Critical Bubble Fractions (composite ETC = UO₂ + bubble, no additive)

| Contact Angle | Critical Bubble Volume Fraction |
|---------------|-------------------------------|
| 35° | ~0.04 |
| 45° | ~0.07 |

### ETC Trends

- Fresh composite (BeO additive, vf = 0.11): ETC significantly higher than pure UO₂
- Spherical additive + bubble (θ = 35°, vf = 0.04): ETC ≈ same as UO₂ with bubble (no additive) — **additive benefit completely eliminated**
- Rectangular additive (3:1): ~2 W/mK higher ETC than spherical with same volume fraction
- Bubble on top of rectangular particle: little impact on ETC
- Bubble on side of rectangular particle (heat flow direction): 2 W/mK reduction at vf = 0.02

### Temperature Dependence (tested at 300, 900, 1500 K)
- As temperature increases, all phase conductivities decrease → lower, flatter ETC
- Model captures temperature effects well

### Additive Conductivity Variation (at 300 K, UO₂ matrix)

| Additive k | Crossover bubble vf |
|------------|----------------------|
| 50 W/mK | ~0.035 |
| 370 W/mK (BeO) | ~0.04 |
| 500–1000 W/mK | ~identical (diminishing returns) |

### Bulk Conductivity Variation (at 300 K, BeO additive)
- Bulk k = 2.52, 4.24, 12.24 W/mK tested
- Bulk phase dominates ETC — changing bulk conductivity has strong impact
- Mirrors temperature effect (since temperature primarily changes bulk conductivity)

---

## Caveats for JSRT Integration

- The model is 2D; 3D corrections may be needed
- Single-particle assumption; multi-particle effects not captured
- Contact angle data needed for specific additive materials used in JSRT
- Only tested with isolated (not continuous) additive morphologies

---

## See Also

- [[2021_Hilty_FissionGasBubblesThermalConductivity]] — index page
- [[wiki/summaries/2021_Hilty_FissionGasBubblesThermalConductivity/PhysicalMechanisms|2021_Hilty_FissionGasBubblesThermalConductivity/PhysicalMechanisms]] — contact angle and screening physics
- [[wiki/summaries/2021_Hilty_FissionGasBubblesThermalConductivity/AnalyticalModel|2021_Hilty_FissionGasBubblesThermalConductivity/AnalyticalModel]] — the $S^2$ ETC model
- [[wiki/summaries/2020_Aagesen_BisonUPuZrSwellingLowerLengthScale|2020_Aagesen_BisonUPuZrSwellingLowerLengthScale]] — Aagesen phase-field model used here
- [[2016_Hu_GasBubbleSuperlatticeFormationPF]] — related phase-field gas bubble work
- [[entities/PhaseFieldModeling]] — MOOSE / AEH framework
