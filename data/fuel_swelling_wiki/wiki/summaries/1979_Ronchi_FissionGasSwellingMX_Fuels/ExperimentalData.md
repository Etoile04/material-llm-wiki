# Ronchi 1979 — Experimental Data & Model Description

**Source:** [[wiki/summaries/1979_Ronchi_FissionGasSwellingMX_Fuels|Ronchi 1979 Index]]

---

## Experimental Observations

- Bubble size distributions are **skew** and **self-similar** at different magnifications (TEM, REM, optical)
- Log-normal distributions confirmed experimentally
- After cooldown from 2000→1500 °C at 1–5% FIMA: bubbles up to 1–5 μm
- Grain growth at constant volume rate confirmed
- Critical temperature $T_c$ observed with abrupt slope change in swelling vs. $T$

### Sweeping Lifetimes (2000 °C, MC fuel, 500 Å bubbles)

| Mechanism | Lifetime |
|-----------|----------|
| Brownian (vaporization) | $\tau_0 \sim 10^5$ s |
| Brownian (solid state) | $\tau_0 \sim 10^{10}$ s |
| Thermal gradient (1500–1800 °C, 100 °C/mm) | $\tau_0 \sim 10^6$–$10^8$ s |

---

## Model Description: TPROF Code

### Overall Structure

The TPROF code solves the following sequential steps:

1. **Gas kinetics** — Rate equations for gas in solution, precipitated in bubbles, and migrating to grain boundaries
2. **Bubble population analysis** — Statistical treatment using log-normal distributions (4 parameters: $m$, $V_0$, $n$, $\sigma$)
3. **Ripening effects** — Determine minimum stable bubble size and nucleation limits
4. **Sweeping corrections** — Bubble lifetime and correction factor
5. **Porosity dynamics** — Non-equilibrium growth via creep
6. **Gas release** — [[wiki/entities/RateTheory|Percolation model]] for grain boundary pore interlinkage

### Key Innovations

1. **Statistical bubble populations**: Log-normal distributed populations replace deterministic size classes
2. **Non-equilibrium growth**: Dynamic kinetics, not equilibrium radius assumption
3. **Variable temperature treatment**: Analytical solutions for gas release under both increasing and decreasing temperature
4. **Percolation-based release**: Statistical model for pore interlinkage

### Temperature Regime Classification

| Regime | Behavior |
|--------|----------|
| **Low $T$** (below $T_c$) | Swelling ~linear in burnup; coalescence does NOT increase swelling (rigid matrix) |
| **High $T$** (above $T_c$) | Swelling ~$b^{3/2}$; rapid matrix relaxation; concentration decreases → larger bubbles |
| **Critical $T_c$** | Sharp transition between regimes |

---

## Key Findings

1. Log-normal bubble distributions arise naturally from stochastic processes — not an arbitrary assumption
2. Resolution in MX fuels differs fundamentally from oxides: no bulk displacement, only gas atom re-ejection → ripening effective in MX
3. Bubble concentration is self-limiting — ripening and coalescence set upper bounds on $N$
4. Non-equilibrium effects are crucial at low $T$ — equilibrium models overpredict swelling
5. Coalescence only increases swelling if matrix is plastic enough to relax resulting overpressure
6. Grain boundary sweeping is the most effective bubble removal mechanism
7. Percolation threshold for interlinkage: $P > 1.569$ bonds per site; fabrication porosity >10% needed for >50% open pores
8. Large grain-to-pore size ratio favors gas release; intragranular pores act as gas reservoirs without contributing to release

---

## Relevance to JSRT Model

### Direct Applicability
- **Log-normal bubble distribution**: Theoretical basis for bubble size distribution inputs
- **Non-equilibrium growth model**: Critical for transient swelling at lower temperatures
- **Constriction factor $F$**: Quantifies deviation from equilibrium — usable as correction factor
- **Rate equation system**: Adaptable for numerical JSRT implementation

### Key Parameters
- Surface tension $\gamma = 0.6$ J/m²
- Gas creation rate $p = 3.4\times10^{-5}$ mol/(m³·s)
- Temperature-dependent diffusion coefficients (Table 1)
- Bubble concentration limits from ripening analysis

### Limitations
- Parameters calibrated for MC (carbide); MN (nitride) may differ
- Dislocation density poorly known (estimated $10^{13}$–$10^{14}$ m⁻² from creep fits)
- Gas solubility in MX fuels poorly characterized
- Radiation-enhanced creep not well quantified

---

## See Also

- [[wiki/summaries/1979_Ronchi_FissionGasSwellingMX_Fuels/PhysicalMechanisms|Physical Mechanisms]]
- [[wiki/summaries/1979_Ronchi_FissionGasSwellingMX_Fuels/KeyEquations|Key Equations]]
- [[wiki/entities/CavitationalVoid|CavitationalVoid]]
- [[wiki/summaries/2001_Rest_GRSIS_FissionGasMetallic|Rest 2001 — GRSIS Model]]
- [[wiki/summaries/2013_Karahan_FEAST_METAL_FuelSwelling|Karahan 2013 — FEAST-METAL]]
