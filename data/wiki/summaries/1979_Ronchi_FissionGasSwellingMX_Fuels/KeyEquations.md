# Ronchi 1979 — Key Equations & Parameters

**Source:** [[wiki/summaries/1979_Ronchi_FissionGasSwellingMX_Fuels|Ronchi 1979 Index]]

---

## Rate Equation System (System 2)

$$\frac{dc}{dt} = p - \frac{db^*}{dt} - \frac{dg}{dt} - \frac{dR}{dt} \quad \text{(gas in dynamic solution)}$$

$$\frac{db_j}{dt} = K_j r_j c - C_0 r_j n_j \quad \text{(gas in } j\text{th bubble class)}$$

Where:
- $K_j = 4\pi n_j D_g$ (capture rate constant)
- $C_0 = 4\pi d q f / b'$ (re-solution parameter)
- $D_g$ = [[wiki/entities/FissionGasDiffusion|gas diffusion coefficient]]
- $d$ = bubble shell thickness, $f$ = re-solution frequency, $b'$ = van der Waals co-volume

## Bubble Diffusion Coefficient

$$D_b = \frac{h^2}{6} f \left[\frac{3D_V}{r^3} + \frac{4\pi D_s a^4}{r^4}\right] \quad \text{for } r > r_+ \quad \text{(eq. 15)}$$

## Statistical Bubble Distribution (Log-Normal)

$$f(V) = (2\pi\sigma^2)^{-1/2} \exp\left\{-\frac{[\ln(V-V_0)-m]^2}{2\sigma^2}\right\}$$

Parameters: $m$ (mean), $V_0$ (smallest admissible volume), $n$ (concentration), $\sigma$ (dispersion).

Fractional variance: $\sigma^2 = n/n_T$ where $n_T$ = total sub-individuals subject to capture.

All moment distributions are also log-normal with parameters $(m + i\sigma^2, \sigma^2)$.

## Van der Waals Equation of State

$$(p + a^*/V^2)(V - b^*) = nRT \quad \rightarrow \quad p = 2\gamma/r \text{ (equilibrium)}$$

## Growth Rate Equations (Porosity Dynamics)

Constitutive creep law (eq. 40):
$$\dot{\varepsilon} = K \sigma_e^n \exp(-\Delta H / RT)$$

Stress in hollow sphere (plastic, eqs. 41, 43):
$$\sigma_r(R) = G R^{-2/n} + D$$
$$\sigma_t = \sigma_r(1 - 2n) + 2nD / R^{2/n}$$

Microscopic and total swelling rates:
$$\dot{\mu} = 3\bar{a}\,\dot{\varepsilon}(\bar{a}) \quad \text{(eq. 51)}$$
$$\Lambda = 3\,\dot{\varepsilon}_r(b) \quad \text{(eq. 52)}$$

## Swelling–Gas Relationship (Equilibrium)

$$\frac{\Delta V}{V} = K b^{3/2} \quad \text{(eq. 27)}$$

Under sweeping with period $\Delta t/J$:
$$\left(\frac{\Delta V}{V}\right)_{\text{swept}} = \frac{1}{J}\left(\frac{\Delta V}{V}\right)_{\text{unswept}} \quad \text{(eq. 29)}$$

## Percolation Condition

$$P = \frac{1}{2}N_c \left[\pi r_p^2 (n_p + n_g n_p / n_g)\right] \quad \text{(eq. 56)}$$

Interlinkage when $P > 1.569$. Open pore fraction from Gaussian integral (eq. 59).

---

## Table 1: Key Parameters for Calculations

| Parameter | Symbol | Value |
|-----------|--------|-------|
| Volume diffusion coefficient | $D_V$ | $1.2\times10^{-3}\exp(-48000/T + K_p)$ m²/s |
| Surface diffusion coefficient | $D_s$ | $4.9\times10^{-4}\exp(-35000/T + K_p)$ m²/s |
| [[wiki/entities/FissionGasDiffusion\|Fission gas diffusion coefficient]] | $D_g$ | $1.2\times10^{-6}\exp(-38600/T + K_p)$ m²/s |
| Surface tension | $\gamma$ | 0.6 J/m² |
| Relaxed surface bubble size | $r'$ | 0.5 nm |
| Atomic radius of gas-in-fuel | $r_0$ | 0.3 nm |
| Van der Waals constant | $K$ | 1.942 m⁵/mol |
| Re-solution constant | — | $10^{-14}$ |
| Gas creation rate | $p$ | $3.4\times10^{-5}$ mol/(m³·s) |
| Temperature range | $T$ | 800–1500 °C |

## Table 2: Ripening Efficiency

| Temperature (K) | 1300 | 1500 | 1700 |
|-----------------|------|------|------|
| $N$ (m⁻³) | $10^{18}$–$10^{20}$ | $10^{19}$–$10^{20}$ | $10^{19}$–$10^{18}$ |
| $\bar{r}$ (from avg $D_s$) | $10^{-2}$–$10^{-1}$ | $6\times10^{-1}$ | — |
| $r_{\min}/\bar{r}$ | $10^{-1}$–10 | 1–10 | — |

---

## See Also

- [[wiki/summaries/1979_Ronchi_FissionGasSwellingMX_Fuels/PhysicalMechanisms|Physical Mechanisms]]
- [[wiki/summaries/1979_Ronchi_FissionGasSwellingMX_Fuels/ExperimentalData|Experimental Data]]
- [[wiki/entities/FissionGasDiffusion|FissionGasDiffusion]]
- [[wiki/entities/RateTheory|RateTheory]]
