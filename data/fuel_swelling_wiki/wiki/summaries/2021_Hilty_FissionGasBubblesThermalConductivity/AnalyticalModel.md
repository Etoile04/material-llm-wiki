# Fission Gas Bubbles & Thermal Conductivity — Analytical Model

*Sub-page of [[2021_Hilty_FissionGasBubblesThermalConductivity]]*

---

## Key Equations

### Effective Thermal Conductivity (ETC) Model (Eq. 1)

$$\frac{k_{\text{eff}} - k_0}{k_0} = a \left(\frac{k_1}{k_0} - 1\right) S^2$$

Where:
- **$k_{\text{eff}}$** = effective thermal conductivity of composite with bubbles
- **$k_0$** = ETC of fresh composite fuel (no gas) — best case, S = 0
- **$k_1$** = ETC of UO₂ without additive with the largest bubble fraction — worst case, S = 1
- **$S$** = screening fraction (0 to 1)
- **$a$** = fitting parameter for additive particle aspect ratio

### Aspect Ratio Fitting Parameter (Eq. 2)

$$a = 0.54 - 0.2 \ln(R)$$

Where:
- **R** = aspect ratio of additive particle (length/width with respect to heat flow direction)
- For spherical particle (1:1): $a = 1$

### Screening Fraction Definition

$$S = \frac{\text{fraction of additive volume that has bubble along heat flow direction}}{\text{total additive volume}}$$

Represents the fraction of additive that is "screened" from contributing to heat transport. Best metric among three tested (surface coverage, cross-sectional coverage, screening fraction).

---

## Thermal Conductivity Reference Values (at 300 K)

| Phase | Thermal Conductivity | Reference |
|-------|---------------------|-----------|
| UO₂ | 8.24 W/mK | Fink (2000) |
| BeO | 370 W/mK | Slack & Austerman (1971) |
| Xe gas | 0.0055 W/mK | Assael et al. (2018) |

---

## Model Development Steps

1. Identified **screening fraction** as best metric correlating bubble morphology with ETC (vs. surface coverage, cross-sectional coverage)
2. Observed ETC decreases as **$S^2$** trend for both spherical and rectangular particles
3. Built analytical model with two endpoints: $k_0$ (fresh, S = 0) and $k_1$ (worst case, S = 1)
4. Added aspect-ratio-dependent fitting parameter **$a$**

---

## Model Limitations

- **2D only** — known to overestimate secondary phase impact; 3D needed for validation
- **Single particle** — real systems have many particles with varying shapes/sizes
- **Discrete particles only** — not applicable to continuous additive structures along grain boundaries
- **Assumes ETC ≥ $k_1$** — in reality, can go below for extreme bubble shapes (crescent)
- Contact angles and interface energies unknown for most additives
- Model applicability limit: bubble vf ~0.04 when additive k >> bulk k (two orders of magnitude)

---

## JSRT Integration Notes

- The **$S^2$ relationship** and screening fraction concept provide a physics-based framework for modeling how fission gas bubbles degrade ETC in composite fuels
- The **$a = 0.54 − 0.2 \ln(R)$** formula can be incorporated for non-spherical additive geometries
- Critical thresholds: bubble volume fraction at which additive benefits are negated (0.04 for θ = 35°, 0.07 for θ = 45°) provides quantitative thresholds for burnup-dependent property models
- Model's validity across 300–1500 K covers operational temperature range

---

## See Also

- [[2021_Hilty_FissionGasBubblesThermalConductivity]] — index page
- [[wiki/summaries/2021_Hilty_FissionGasBubblesThermalConductivity/PhysicalMechanisms|2021_Hilty_FissionGasBubblesThermalConductivity/PhysicalMechanisms]] — screening and contact angle physics
- [[wiki/summaries/2021_Hilty_FissionGasBubblesThermalConductivity/SimulationResults|2021_Hilty_FissionGasBubblesThermalConductivity/SimulationResults]] — numerical validation
- [[wiki/summaries/2011_Millett_PhaseFieldGasBubbleKinetics|2011_Millett_PhaseFieldGasBubbleKinetics]] — phase-field bubble modeling context
- [[entities/PhaseFieldModeling]] — AEH homogenization methods
