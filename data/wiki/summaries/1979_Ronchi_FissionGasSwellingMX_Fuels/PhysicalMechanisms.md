# Ronchi 1979 — Physical Mechanisms of Fission Gas Swelling in MX Fuels

**Source:** [[wiki/summaries/1979_Ronchi_FissionGasSwellingMX_Fuels|Ronchi 1979 Index]]

---

## 1. Fission Gas Kinetics

Fission gas (Xe, Kr) is created at rate **p** and partitions into:
- Intragranular [[wiki/entities/GasBubbleSuperlattice|gas bubbles]]
- Pre-existing pores and stable bubbles

Gas is re-injected into the matrix by fission fragment spikes (resolution) at rate $dR/dt$.
The full system is governed by a coupled rate equation system (eqs. 2a–2e) with M bubble classes.

## 2. Bubble Nucleation and Growth

Gas atoms accumulate to saturation concentration and then precipitate into bubbles. After an incubation time (dependent on resolution frequency and [[wiki/entities/FissionGasDiffusion|gas diffusion coefficient]]), a stable population is established.

- At $T > 1000\,°C$ in MC fuels: steady-state within days
- At low $T$: steady-state may not be reached within fuel lifetime

## 3. Resolution (Re-solution)

Fission fragments re-eject gas atoms from bubbles. Re-solution rate:

$$\frac{dR}{dt} = C_0 \cdot r_j(t) \cdot n_j(t), \quad C_0 = \frac{4\pi d q f}{b'}$$

**Key difference from oxides:** In MX-type fuels, there is no bulk displacement/sputtering from fission spikes — only primary/secondary collision re-ejection of gas atoms. This is why [[wiki/entities/RateTheory|Ostwald ripening]] is effective in MX fuels but negligible in oxides.

## 4. Coalescence

Bubbles undergo Brownian motion and coalesce via sweeping of capture volumes:

$$X = \sqrt{6 D_b t}$$

where $D_b$ is the bubble diffusion coefficient. The capture volume radius $X$ reaches an asymptotic value quickly, simplifying the coalescence description:

$$n = \left(\frac{4}{3}\pi X^3\right)^{-1}$$

## 5. Ripening (Ostwald Ripening)

Larger bubbles grow at the expense of smaller ones due to thermodynamic potential differences. Ripening:
- Is significant when gas concentration approaches the solubility value (high $T$)
- Establishes a minimum stable bubble size $r_{\min}$ (eq. 26)
- Limits bubble concentration: $N < 10^{24}\,\text{m}^{-3}$

## 6. Sweeping Mechanisms

Four mechanisms for bubble removal from the fuel matrix:

| Mechanism | Temperature Range | Timescale |
|-----------|------------------|-----------|
| **(a) Brownian sweeping** | All $T$ | $\tau_0 \sim 10^5$–$10^{10}$ s at 2000°C — negligible |
| **(b) Directed pore migration** (thermal gradient) | 1500–1800°C | $\sim 10^6$–$10^8$ s at 100°C/mm gradient |
| **(c) Random pore migration** | ~1800°C | $u \sim 10^{-12}$ m/s |
| **(d) Grain boundary sweeping** | Practical range | Most effective for bubbles up to hundreds of Å |

## 7. Porosity Growth (Non-Equilibrium)

Growth is driven by gas overpressure balanced against surface tension + external stress. The model uses **non-equilibrium (dynamic) growth** via diffusional creep (Nabarro-Herring mechanism).

The **constriction factor** $F = (\mu - \mu_0)/\mu_0$ measures deviation from the equilibrium model:
- At high $T$: $F \to 0$ (equilibrium model valid)
- At low $T$: $F$ is large (dynamic model essential)

## 8. Critical Temperature $T_c$

An abrupt increase in bubble size occurs at $T_c$ due to:
1. Activation of mechanical yielding of the matrix
2. Decrease of bubble concentration with temperature

The transition occurs over a narrow interval (~tens of degrees) and is confirmed experimentally.

## 9. Pore Interlinkage and Gas Release

A [[wiki/entities/RateTheory|percolation model]] governs interconnected grain boundary pores:
- Interlinkage when average bonds per site $P > 1.569$
- Open porosity fraction calculated from statistical distribution of $P$
- Open pores release gas → pressure drops → hot pressing activated

---

## See Also

- [[wiki/summaries/1979_Ronchi_FissionGasSwellingMX_Fuels/KeyEquations|Key Equations]]
- [[wiki/summaries/1979_Ronchi_FissionGasSwellingMX_Fuels/ExperimentalData|Experimental Data]]
- [[wiki/entities/FissionGasDiffusion|FissionGasDiffusion]]
- [[wiki/entities/RateTheory|RateTheory]]
- [[wiki/summaries/2001_Rest_GRSIS_FissionGasMetallic|Rest 2001 — GRSIS metallic fuel model]]
