# Characterization of Fission Gas Bubbles in Irradiated U-10Mo Fuel (Index)

## Metadata

| Field | Value |
|-------|-------|
| **Authors** | Andrew M. Casella, Douglas E. Burkes, Paul J. MacFarlan, Edgar C. Buck (PNNL) |
| **Journal** | Materials Characterization |
| **Year** | 2017 |
| **Volume/Pages** | 131, 459–471 |
| **DOI** | 10.1016/j.matchar.2017.06.007 |
| **Experiment** | AFIP-3BZ (ATR, 101 EFPD, 63.5 at.% burnup) |

---

## Overview

This paper establishes a **simple, repeatable baseline method** for characterizing fission gas bubbles in irradiated U-10Mo monolithic fuel using SEM imaging and automated image analysis. Mechanical polishing is used instead of FIB to avoid curtaining artifacts. Three software packages (CellProfiler, MATLAB, Mathematica) are compared — MATLAB and Mathematica produce identical results with Otsu threshold 0.4706.

**Key results**: At 4.32 × 10²¹ fissions/cm³ (~63.5 at.% burnup), mean bubble ESD is **0.22–0.32 μm** (log-normal distributed). Average eccentricity ~0.70 indicates moderately elongated bubbles, with grain boundary bubbles elongated along recrystallized matrix channels.

**Note**: This high-burnup sample is post-recrystallization. The observed bubbles are predominantly intergranular/grain-boundary scale, much larger than the nm-scale intragranular bubbles at early irradiation.

---

## Key Equations

> This is primarily an experimental characterization paper (SEM + image analysis). The following equations are reconstructed from the methodology and domain knowledge for model input purposes.

### 1. Bubble Size Distribution

Bubble equivalent spherical diameter (ESD) follows a **log-normal distribution**:

$$f(d) = \frac{1}{d \cdot \sigma \sqrt{2\pi}} \exp\left(-\frac{(\ln d - \mu)^2}{2\sigma^2}\right)$$

Reported parameters: mean ESD = 0.22–0.32 μm (post-recrystallization, intergranular bubbles).

### 2. Otsu Thresholding

Image segmentation uses Otsu's method to find optimal threshold $T^*$:

$$T^* = \arg\min_T \left[ \omega_0(T) \sigma_0^2(T) + \omega_1(T) \sigma_1^2(T) \right]$$

where $\omega_0, \omega_1$ are class weights and $\sigma_0^2, \sigma_1^2$ are class variances. Optimal threshold for this work: $T^* = 0.4706$.

### 3. Bubble Eccentricity

$$e = \sqrt{1 - \frac{b^2}{a^2}}$$

where $a$ and $b$ are the semi-major and semi-minor axes. Reported average eccentricity: $\bar{e} \approx 0.70$.

### 4. Swelling from Bubble Statistics

$$\frac{\Delta V}{V} = \frac{\pi}{6} \sum_i d_i^3 \cdot N_i$$

where $d_i$ is the ESD of bubble $i$ and $N_i$ is the number density.

### 5. Fission Density to Burnup Conversion

$$\text{BU (at.\%)} = \frac{f_d \cdot V_{atom}}{N_A} \cdot 100$$

where $f_d$ is the fission density and $V_{atom}$ is the atomic density. For this sample: $f_d = 4.32 \times 10^{21}\,\text{fiss/cm}^3$ → 63.5 at.% burnup.

### 6. Recrystallization Threshold

$$f_d^{crit} \approx 3.0\text{--}4.5 \times 10^{21}\,\text{fiss/cm}^3$$

Above this threshold, grain subdivision destroys the intragranular bubble superlattice and large intergranular bubbles form.

## Sub-Pages

- [[wiki/summaries/2017_Casella_CharacterizationFissionGasBubblesU10Mo/ExperimentalData|ExperimentalData]] — irradiation conditions, SEM data, bubble statistics by magnification
- [[wiki/summaries/2017_Casella_CharacterizationFissionGasBubblesU10Mo/ModelMethodJSRT|ModelMethodJSRT]] — image analysis methodology, JSRT model inputs, limitations

---

## Relationships

- [[wiki/entities/Recrystallization|Recrystallization]] — high burnup sample is post-recrystallization; causes elongated intergranular bubbles
- [[wiki/entities/FuelAlloy|FuelAlloy]] — U-10Mo alloy fuel at high burnup (~63.5 at%) is characterized
- [[wiki/entities/FissionGasDiffusion|FissionGasDiffusion]] — intergranular fission gas bubble size distribution and morphology are quantified
- [[wiki/concepts/SwellingMechanisms|SwellingMechanisms]] — post-recrystallization bubble morphology (log-normal size distribution, eccentricity) is characterized
- [[wiki/summaries/2016_Hu_GrainMorphologyGasBubbleUMo|Hu 2016 Booth Model]] — rate-theory model predicting bubble structures before recrystallization
- [[wiki/summaries/2015_Miller_TEMGasBubbleSuperlatticeU7Mo|Miller 2015 TEM]] — complementary TEM characterization of intragranular bubble superlattice
- [[wiki/summaries/2015_Gan_ThermalStabilityGasBubbleSuperlattice|Gan 2015]] — thermal stability of gas bubble superlattice context
- [[wiki/summaries/2021_Hilty_FissionGasBubblesThermalConductivity|Hilty 2021]] — thermal conductivity degradation from gas bubbles
