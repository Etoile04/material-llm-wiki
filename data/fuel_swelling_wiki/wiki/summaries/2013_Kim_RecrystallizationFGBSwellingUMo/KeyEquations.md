# Kim 2013 — Key Equations & Parameters

**Source:** [[wiki/summaries/2013_Kim_RecrystallizationFGBSwellingUMo|Kim 2013 Index]]

---

## 1. Modified Avrami Recrystallization Equation

$$V_{rx} = 1 - \exp[-K(F - F_0)^n]$$

| Symbol | Meaning |
|--------|---------|
| $V_{rx}$ | wiki/entities/Recrystallization|Recrystallized]] volume fraction |
| $K$ | Reaction constant (depends on Mo content) |
| $F$ | Fission density (f/cm³) |
| $F_0$ | Incubation fission density (onset threshold) |
| $n$ | Avrami exponent |

## 2. Mo Content Dependence of Reaction Constant

$$K = K_0 \left[0.75(10 - x_{Mo}) + 1\right], \quad K_0 = 0.1$$

where $x_{Mo}$ is Mo content in wt.%.

## 3. FGB Swelling Rate Equation (Recrystallization Stage)

**Mixed-phase formula:**

$$\left.\frac{\Delta V}{V_0}\right|_g = (1 - V_{rx})\left.\frac{\Delta V}{V_0}\right|_{g,0} + V_{rx}\left.\frac{\Delta V}{V_0}\right|_{g,rx}$$

**Integral form:**

$$\left.\frac{\Delta V}{V_0}\right|_g = \left.\frac{\Delta V}{V_0}\right|_{g,0} \cdot F + \left(\left.\frac{\Delta V}{V_0}\right|_{g,rx} - \left.\frac{\Delta V}{V_0}\right|_{g,0}\right)\int_0^F V_{rx}\,dF$$

**Analytical solution using incomplete Gamma function:**

$$\int_0^F V_{rx}\,dF = F - F_0 + \frac{n K^{-1/n}}{n}\left[\Gamma(1/n,\,K(F-F_0)^n) - \Gamma(1/n,\,0)\right]$$

## 4. Extended K with Fission Rate Effect (Optional)

$$K = K_0\left[0.125\times10^{14}(\dot{f} - 2\times10^{14}) + 1\right]\left[0.67(10 - x_{Mo}) + 1\right]$$

where $\dot{f}$ is fission rate (f/cm³·s).

---

## Recrystallization Model Parameters

| Parameter | Atomized Powder | Ground Powder |
|-----------|----------------|---------------|
| $F_0$ (incubation density) | $1.67\times10^{21}$ f/cm³ | $1.38\times10^{21}$ f/cm³ |
| $n$ (Avrami exponent) | 2.6 | 2.6 |
| $K_0$ | 0.1 | 0.1 |

## FGB Swelling Rate Parameters

| Stage | Swelling Rate |
|-------|--------------|
| Pre-recrystallization ($\Delta V/V_0\big\|_{g,0}$) | 0.6% per $10^{21}$ f/cm³ |
| Post-recrystallization ($\Delta V/V_0\big\|_{g,rx}$) | 5.2% per $10^{21}$ f/cm³ |

**Key ratio:** Post-recrystallization FGB swelling rate ≈ **8.7×** pre-recrystallization rate.

## Fuel Parameters

| Parameter | Value |
|-----------|-------|
| U-10Mo Mo content at grain boundaries | ~17 at.% |
| Atomized powder average grain size | 70 μm |
| Enrichment | 19.5% U-235 |
| Operating temperature range | 60–160 °C |

---

## See Also

- [[wiki/summaries/2013_Kim_RecrystallizationFGBSwellingUMo/PhysicalMechanisms|Physical Mechanisms]]
- [[wiki/summaries/2013_Kim_RecrystallizationFGBSwellingUMo/ExperimentalData|Experimental Data]]
- [[wiki/entities/Recrystallization|Recrystallization]]
- [[wiki/summaries/2005_Rest_RecrystallizationSwellingUO2UMo|Rest 2005 — Analytical recrystallization model]]
