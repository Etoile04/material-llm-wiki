# Image Analysis Methodology & JSRT Relevance – 2017 Casella

## Baseline Image Analysis Method

This paper proposes a **simple, repeatable baseline method** for fission gas bubble characterization:

1. **Sample preparation**: Mechanical potting and polishing (avoids FIB curtaining artifacts)
2. **SEM imaging**: Outside hot cell for better instrument control
3. **Image segmentation**: Otsu threshold binarization
4. **Bubble identification**: Connected white pixels = individual bubbles
5. **Characterization**: Number, size (ESD), eccentricity, orientation
6. **Distribution fitting**: Log-normal via Mathematica `FindFit`

**Recommended software**: MATLAB or Mathematica (identical results); CellProfiler requires threshold adjustment.

## 2D → 3D Note

No stereological correction applied in this study. Authors acknowledge that the Schwartz-Saltykov or Xu-Pitot methods could be applied for true 3D size distributions, but baseline 2D characterization is used here.

## Key Findings Summary

1. Mechanical polishing eliminates FIB curtaining artifacts
2. MATLAB and Mathematica produce consistent results
3. Average bubble ESD in irradiated U-10Mo at ~4.3 × 10²¹ fissions/cm³: **~0.22–0.32 μm**
4. Bubble eccentricity consistently ~0.70 (moderately elongated)
5. Grain boundary bubbles elongated along recrystallized channels
6. Single-pixel artifacts inflate eccentricity — removal recommended
7. 2000× overestimates bubble size; 5000×+ recommended

## JSRT / Swelling Model Inputs

| Parameter | Value | Notes |
|-----------|-------|-------|
| Fission density (reference) | 4.32 × 10²¹ f/cm³ | Ground-truth validation condition |
| Mean bubble diameter | 0.22–0.32 μm | Log-normal distributed |
| Bubble eccentricity | ~0.70 | Non-spherical correction needed for volume |
| Fuel composition | U-10.3wt%Mo | γ-phase |
| Burnup | 63.5 at.% | High burnup condition |

**Note**: These are larger bubbles than the intragranular nm-scale bubbles simulated by [[wiki/summaries/2016_Hu_GrainMorphologyGasBubbleUMo|Hu 2016]] or [[wiki/summaries/2018_Liang_3DPhaseFieldIntragranularBubbleUMo|Liang 2018]] — these are predominantly intergranular bubbles in a post-recrystallization sample.

## Limitations

- No 3D stereological correction
- No temperature data for sample positions
- Single sample from one experiment (AFIP-3BZ)
- No explicit swelling % reported — must be derived from area fraction
- No fission gas release data (see Burkes et al., J. Nucl. Mater. 461, 2015)

## Companion References

- Burkes et al., J. Nucl. Mater. 464 (2015) — thermal properties
- Burkes et al., J. Nucl. Mater. 461 (2015) — fission gas release
- Hu et al., J. Nucl. Mater. 462 (2015) — effective thermal conductivity with gas bubbles

## See Also

- [[wiki/summaries/2017_Casella_CharacterizationFissionGasBubblesU10Mo|Index: Casella 2017]]
- [[wiki/summaries/2017_Casella_CharacterizationFissionGasBubblesU10Mo/ExperimentalData|Experimental Data]]
- [[wiki/entities/Recrystallization|Recrystallization]] — high burnup sample is post-recrystallization
- [[wiki/summaries/2016_Hu_GrainMorphologyGasBubbleUMo|Hu 2016 Booth Model]] — model predicting pre-recrystallization bubble structures
- [[wiki/summaries/2015_Miller_TEMGasBubbleSuperlatticeU7Mo|Miller 2015 TEM]] — TEM characterization of intragranular bubbles for comparison
- [[wiki/summaries/2021_Hilty_FissionGasBubblesThermalConductivity|Hilty 2021]] — thermal conductivity impact of fission gas bubbles
