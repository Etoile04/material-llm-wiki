# Parameters & Key Findings – 2018 Liang: 3D Phase-Field Intragranular Bubbles in U-Mo

## Material Properties of U-7Mo (Table 1)

| Parameter | Symbol | Value | Source |
|-----------|--------|-------|--------|
| Temperature | T | 473 K | This work |
| Lattice constant | a | 3.43×10⁻¹⁰ m | — |
| Surface energy (bcc 110) | γ | 1.81 J/m² | DFT |
| Gradient coefficients | κ | 6.91×10⁻⁹ J/m | — |
| Potential height | w | 7.73×10⁹ J/m³ | — |
| Vacancy formation energy | $E_V^f$ | 1.12 eV | DFT |
| Interstitial formation energy | $E_I^f$ | 1.48 eV | DFT |
| Xe solution energy | $E_X^f$ | 6.95 eV | DFT |
| Xe diffusivity | $D_X$ | 4.10×10⁻¹⁷ m²/s | Rest (2010) |
| Interstitial diffusivity | $D_I$ | 2.05×10⁻¹⁴ m²/s | MD |
| Vacancy diffusivity | $D_V$ | 3.84×10⁻¹⁷ m²/s | MD |
| Kinetic coefficient | L | 9.04×10⁻⁸ m³/(J·s) | — |
| Elastic C₁₁ | — | 173.0 GPa | DFT |
| Elastic C₁₂ | — | 138.0 GPa | DFT |
| Elastic C₄₄ | — | 50.0 GPa | DFT |
| Resolution rate | β | 2.0×10⁻²⁵ × fr | — |
| Dislocation bias (V) | $Z_V$ | 1.0 | Rest (1993) |
| Dislocation bias (SIA) | $Z_I$ | 1.025 | Rest (1993) |
| Xe generation rate | K | 0.25 | — |

### Lattice Misfit Strains

| Defect | $\varepsilon^0$ |
|--------|-----------------|
| Xe | −0.006 |
| Vacancy | 0.02 |
| SIA | 0.02 |
| Bubble | 0.003 |

## Simulation Setup

| Parameter | Value |
|-----------|-------|
| Domain size | 22.4 × 22.4 × 22.4 nm |
| Grid spacing | Δl = 0.35 nm |
| Boundary conditions | Periodic |
| Solver | Semi-implicit FFTW |
| Fission rate | 5.0×10²⁰ m⁻³ s⁻¹ |
| Grain boundary density | 0.41 µm⁻¹ |
| Dislocation density | 0.43×10¹⁵ m⁻² |

## Key Findings

### 1. Stable Intragranular Bubble Structure
- Stable nanometer-size bubbles reproduced by balancing defect production with recombination + sink reactions
- Bubble sizes stabilize at **2.7–3.8 nm** at dynamic equilibrium
- Average bubble pressure: **~1.3 GPa** (van der Waals EOS)
- Bubble density: ~2.40 × 10²⁴ m⁻³

### 2. Fission Rate Effect
- Higher fission rate → larger bubbles, higher density, higher swelling
- Bubble density: 2.05 → 2.40 → 2.67 × 10²⁴ m⁻³ for fission rates 3.0 → 5.0 → 7.0 × 10²⁰ m⁻³ s⁻¹

### 3. Grain Size Effect
- **Smaller grains → lower intragranular swelling** (more gas diffuses to grain boundaries)
- But small grains increase intergranular swelling at high fission densities
- **Large grains are beneficial** for containing gas intragranularly and reducing total swelling

### 4. Rolling-Induced Dislocation Effect
- **Higher dislocation density → increased intragranular swelling**
- Swelling: ~2.8% → 5.9% for dislocation density 0.10 → 1.52 × 10¹⁵ m⁻²
- Mechanism: Biased SIA absorption by dislocations reduces recombination → more vacancies flow to bubbles

### 5. Overall Swelling Behavior
- Swelling rises rapidly early, then plateaus
- At high fission density: recrystallization destroys intragranular bubbles → intergranular bubbles dominate

## Validation

| Quantity | Simulated | Experimental |
|----------|-----------|-------------|
| Avg bubble size | ~3.2 nm | 1–5 nm (TEM) |
| Bubble density | 2.40×10²⁴ m⁻³ | Consistent with measurements |
| Avg bubble pressure | ~1.3 GPa | Consistent with other PF simulations |

## See Also

- [[wiki/summaries/2018_Liang_3DPhaseFieldIntragranularBubbleUMo|Index: Liang 2018]]
- [[wiki/summaries/2018_Liang_3DPhaseFieldIntragranularBubbleUMo/KeyEquations|Key Equations]]
- [[wiki/entities/Recrystallization|Recrystallization]] — destroys intragranular bubble structure at high fission density
- [[wiki/entities/GasBubbleSuperlattice|GasBubbleSuperlattice]] — related ordered bubble structure (not modeled here)
- [[wiki/summaries/2016_Hu_GrainMorphologyGasBubbleUMo|Hu 2016]] — complementary rate-theory model with grain morphology effects
- [[wiki/summaries/2015_Miller_TEMGasBubbleSuperlatticeU7Mo|Miller 2015 TEM]] — TEM validation data for intragranular bubble structures
