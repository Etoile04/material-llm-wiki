# Key Findings & JSRT Relevance – 2016 Hu: Grain Morphology & Gas Bubble Swelling

## Key Findings

### 1. Grain Size Effect
- **Smaller grains → faster swelling kinetics**: shorter diffusion path increases gas flux to grain boundaries
- Intra-granular bubble density and radius decrease with decreasing grain size
- Classical Booth model **underestimates** swelling by ~30% in intra-granular bubble radius due to simplified spherical grain assumption

### 2. Grain Aspect Ratio Effect
- **Higher aspect ratio → faster swelling kinetics** at same grain volume
- Elongated grains (rolling-induced morphology) have shorter diffusion paths perpendicular to the long axis
- Crystal D (16:1) shows significantly higher swelling than Crystal B (1:1)

### 3. Fission Rate Effect
- **Higher fission rate → faster swelling kinetics**
- Total swelling is determined by **fission density** (= rate × time) for a given microstructure
- $D_g = D_0\dot{f}$: Xe diffusivity scales linearly with fission rate (athermal regime)

### 4. Mo Inhomogeneity Effect
- Spatially dependent fission rate (from Mo core-shell distribution) has **minor effect** on swelling
- Strong inhomogeneity (center: 0.71ḟ, boundary: 1.22ḟ) → only ~6.5% swelling increase
- Not significant for grain sizes of a few micrometers before recrystallization

### 5. Comparison with Classical Booth Model
- Good agreement for equiaxed grain structures; Booth underestimates due to:
  - Representative sphere simplification
  - Neglect of grain size distribution effects
- This 3D model provides spatially resolved gas bubble structures (density, radius, gas content vary within grains)

## Relevance to JSRT / Swelling Models

| Aspect | Transferable Insight |
|--------|---------------------|
| Rate equations | Validated framework (Eqs. 1–6) for bubble nucleation, growth, re-solution |
| Parameters | Xe EOS constants, yield, resolution rate, nucleation factor range |
| Grain morphology | Aspect ratio and size are first-order effects on swelling kinetics |
| Athermal diffusion | $D_g \propto \dot{f}$ appropriate for metallic fuels at T < 500 K |
| Recrystallization | Threshold 3.1–3.5 × 10²⁷ f/m³ marks end of model validity |

### Specific Parameters Transferable
- Van der Waals EOS for Xe: $b_v = 8.5 \times 10^{-29}$ m³, $h_s = 0.6$
- Xe yield: $Y = 0.25$ atoms/fission
- Resolution rate: $b = b_0\dot{f}$, $b_0 = 2.0 \times 10^{-24}$ m³
- Nucleation factor range: $f_n = 0.01$–$0.03$

## Limitations

- Model limited to pre-recrystallization regime
- Grain sizes simulated (~few μm) smaller than actual monolithic UMo fuels (~tens of μm)
- $\chi$ (GB enhancement factor, range 15–125) requires fitting
- No temperature-dependent diffusion (athermal assumption only)
- Xe solubility at grain boundaries ($c^\text{eq}_\text{GB}$) not well constrained experimentally

## See Also

- [[wiki/summaries/2016_Hu_GrainMorphologyGasBubbleUMo|Index: Grain Morphology Booth Model]]
- [[wiki/entities/Recrystallization|Recrystallization]] — threshold effects on model validity
- [[wiki/entities/RateTheory|RateTheory]] — general rate-theory framework
- [[wiki/summaries/2013_Kim_RecrystallizationFGBSwellingUMo|Kim 2013 Recrystallization]] — recrystallization effect on swelling
- [[wiki/summaries/2011_Kim_FissionProductInducedSwellingUMo|Kim 2011 Swelling]] — fission product swelling context
- [[wiki/summaries/2018_Liang_3DPhaseFieldIntragranularBubbleUMo|Liang 2018]] — complementary 3D phase-field simulations with dislocation effects
