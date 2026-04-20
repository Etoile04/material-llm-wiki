# Experimental Data – 2017 Casella: Fission Gas Bubble Characterization in U-10Mo

## Irradiation Conditions (AFIP-3BZ, ATR)

| Parameter | Value |
|-----------|-------|
| Fuel | U-10.3wt%Mo monolithic foil |
| ²³⁵U enrichment | 19.937% |
| Cladding | AA6061 aluminum |
| Diffusion barrier | Zr, 25 μm each side (hot co-rolled, HIP) |
| Irradiation duration | 101.0 EFPD |
| Average burnup | 63.5 at.% |
| Fission density | **4.32 × 10²¹ fissions/cm³** |
| Reactor | ATR (Advanced Test Reactor) |

## Image Analysis Parameters

| Tool | Otsu Threshold |
|------|----------------|
| CellProfiler | 0.4235 (requires manual correction) |
| MATLAB | 0.4706 |
| Mathematica | 0.4706 (recommended) |

**Bubble size metric**: Equivalent Spherical Diameter (ESD) = 2× equivalent disk radius from 2D cross-section.

## Log-Normal Bubble Size Distribution (Position 7)

| Magnification | Mean ESD (μm) | Std. Dev. (μm) |
|---------------|---------------|-----------------|
| 2000× | 0.323 | 0.394 |
| 5000× | 0.286 | 0.281 |
| 10,000× | 0.288 | 0.296 |
| 15,000× | 0.274 | 0.290 |
| 20,000× | 0.262 | 0.287 |
| 25,000× | 0.221 | 0.230 |

**Recommendation**: Use 5000× and above; 2000× overestimates bubble size due to pixel resolution limits.

## Bubble Morphology Statistics

### Position 3, 2000× (With / Without Single-Pixel Artifacts)

| Metric | With | Without |
|--------|------|---------|
| Number of objects | 9324 | 9322 |
| Average area (μm²) | 0.140 | 0.139 |
| Average eccentricity | 0.756 | 0.756 |

### Position 3, 10,000× (Multi-Tool Comparison)

| Metric | CellProfiler | MATLAB | Mathematica |
|--------|-------------|--------|-------------|
| Object count | 1155 | 1328 | 1328 |
| Avg eccentricity | 0.690 | 0.681 | 0.692 |
| Avg orientation | −3.66° | −3.28° | −3.28° |

**Converged eccentricity**: ~0.70 at high magnification (excluding single-pixel artifacts).

## Key Observations

- Two bubble populations: **intragranular** (smaller, spherical) and **intergranular/grain-boundary** (larger, elongated along recrystallized channels)
- Average eccentricity of ~0.70: moderately elongated (0 = circle, 1 = line)
- Bubble orientation correlates with local recrystallized channel direction
- Bubble count decreases linearly with increasing magnification (smaller field of view)
- Log-normal distribution fits bubble size data well

## See Also

- [[wiki/summaries/2017_Casella_CharacterizationFissionGasBubblesU10Mo|Index: Casella 2017 Characterization]]
- [[wiki/summaries/2017_Casella_CharacterizationFissionGasBubblesU10Mo/ModelMethodJSRT|Methodology & JSRT Relevance]]
- [[wiki/entities/Recrystallization|Recrystallization]] — causes the intergranular bubble band structure observed
- [[wiki/entities/FuelAlloy|FuelAlloy]] — U-10Mo fuel composition
