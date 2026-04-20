# Model Parameters – 2016 Hu: Grain Morphology & Gas Bubble Swelling

## Key Parameters (Table 1)

| Parameter | Symbol | Value | Unit |
|-----------|--------|-------|------|
| Characteristic length | $l_0$ | 50 | nm |
| Grid size | $dx=dy=dz$ | 50 | nm |
| Xe diffusivity prefactor | $D_0$ | 1.0 × 10⁻⁴⁰ | m⁵/fission |
| Xe diffusivity | $D_g = D_0\dot{f}$ | ∝ fission rate | m²/s |
| Grain boundary energy | $\gamma$ | 1.0 | J/m² |
| Xe yield per fission | $Y$ | 0.25 | atoms/fission |
| Fission rate range | $\dot{f}$ | 1.2×10²⁰ – 2.4×10²² | fissions/m³/s |
| GB enhancement factor | $\chi$ | 0.25 | — |
| Dissolution rate prefactor | $b_0$ | 2.0 × 10⁻²⁴ | m³ |
| Van der Waals const. (Xe) | $b_v$ | 8.5 × 10⁻²⁹ | m³ |
| Nucleation factor | $f_n$ | 0.01–0.03 | — |
| EOS fitting factor (Xe) | $h_s$ | 0.6 | — |
| GB thickness | $d$ | 1 | nm |
| GB potential | $\mu_\text{GB}$ | 0.0 | eV/atom |
| Xe atom radius | $r_g$ | 2.16 × 10⁻¹⁰ | m |
| Nearest jump sites | $z$ | 8 | — |
| Xe formation volume | $\varepsilon_0$ | 1.05 × 10⁻²⁹ | m³ |
| Equilibrium GB concentration | $c^\text{eq}_\text{GB}$ | 1.5 × 10⁻⁵ | — |

## Crystal Structures Used

| Structure | Grains | Avg Diameter | Aspect Ratio |
|-----------|--------|-------------|--------------|
| Crystal A | 548 | 1.34 μm | 1:1 (equiaxed, small) |
| Crystal B | 20 | 4.36 μm | 1:1 (equiaxed, large) |
| Crystal C | 20 | same as B | 4:1 (elongated) |
| Crystal D | 20 | same as B | 16:1 (elongated) |

## Recrystallization Threshold

Critical fission density: **3.1–3.5 × 10²⁷ fissions/m³** — model valid only below this threshold.

## Mo Distribution in U-10Mo

- Mo concentration varies **10–25 at%** across grains (core-shell structure)
- Higher Mo at grain center, lower at grain boundaries
- Affects U²³⁵ distribution → spatially dependent fission rate

## See Also

- [[wiki/summaries/2016_Hu_GrainMorphologyGasBubbleUMo|Index: Grain Morphology Booth Model]]
- [[wiki/summaries/2016_Hu_GrainMorphologyGasBubbleUMo/KeyEquations|Key Equations]]
- [[wiki/entities/FuelAlloy|FuelAlloy]] — UMo alloy composition details
- [[wiki/entities/Recrystallization|Recrystallization]] — threshold context
