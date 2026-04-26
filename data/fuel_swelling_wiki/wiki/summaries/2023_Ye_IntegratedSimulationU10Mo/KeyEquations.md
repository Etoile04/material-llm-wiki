# Integrated Simulation U-10Mo — Key Equations & Parameters

*Sub-page of [[2023_Ye_IntegratedSimulationU10Mo]]*

---

## Xe Diffusivity in U-Mo (Eq. 2)

$$D_{Xe} = 1.28 \times 10^{-5} \exp\!\left(\frac{-1.76}{kT}\right) + 5.07 \times 10^{-31} \dot{f}$$

- First term: intrinsic (thermal) diffusion; activation energy $Q = 40{,}559$ cal (~1.76 eV)
- Second term: radiation-driven diffusion
- $k = 8.617 \times 10^{-5}$ eV/K, $T$ in K, $\dot{f}$ in fissions/cm³/s

---

## Intragranular Bubble Nucleation Rate (Eq. 1)

$$\dot{N}_{R\text{-intra}} = \frac{1}{6\pi} \cdot f_N \cdot D_{Xe} \cdot r_{Xe} \cdot C^2_{Xe\text{-intra}}$$

- $r_{Xe} = 2.16 \times 10^{-8}$ cm (Xe atom radius)

---

## Intergranular Bubble Nucleation Rate (Eq. 3)

$$\dot{N}_{R\text{-inter}} = \frac{1}{6\pi} \cdot (f_N \cdot f_{N\text{-GB}}) \cdot (D_{Xe} \cdot z) \cdot r_{Xe} \cdot C^2_{Xe\text{-inter}}$$

---

## Radiation-Induced Re-solution (Eq. 4–6)

$$b = b_0 \cdot \dot{f} \cdot R$$

Piecewise function $R$:
- $r_b \leq \lambda$: $R = 1$ (complete destruction)
- $r_b > \lambda$: $R = 1 - \left(1 - \frac{r_b - r_\text{resol}}{r_b}\right)^3$ (partial, outer shell only)

---

## Bubble Coalescence Probability (Eq. 8)

$$P_{ij} = 4\pi(r_i + r_j)(D_i + D_j) + \pi(r_i + r_j)^2 |v_j - v_i|$$

---

## Gas Atom Diffusion to GB (Speight's Model, Eq. 9)

$$R_{g,I} = 3(C_I - C_g) \cdot \left\{\left[\frac{D_{Xe} \cdot b}{a^2(b+g)(t-t_0)}\right]^{0.5} - \frac{D_{Xe} \cdot b}{a^2(b+g)}\right\}$$

---

## Solid Fission Product Swelling (Eq. 13)

$$\left(\frac{\Delta V}{V_0}\right)_\text{solid} = 4.0 \times F_D \quad [F_D \text{ in } 10^{21} \text{ fissions/cm}^3]$$

---

## Calibrated Parameter Set (Table 3)

| Parameter | Description | Optimized Value | Previous Value |
|-----------|-------------|----------------|----------------|
| $D_0$ | Radiation-driven diffusivity coefficient | $5 \times 10^{-31}$ cm⁵ | $8 \times 10^{-29}$ |
| $Q$ | Activation energy (intrinsic diffusion) | 40,559 cal | 33,000 |
| $z$ | GB diffusion enhancement factor | $3 \times 10^4$ | $1 \times 10^4$ |
| $f_N$ | Intragranular nucleation probability | $2 \times 10^{-7}$ | $3 \times 10^{-8}$ |
| $f_{N\text{-GB}}$ | GB nucleation adjustment factor | $6 \times 10^{-10}$ | $6 \times 10^{-7}$ |
| $\gamma_{U10Mo}$ | Surface energy | 1850 dyn/cm (DFT) | 200 |
| $b_0$ | Bubble destruction probability | $2 \times 10^{-18}$ cm³ | $7 \times 10^{-18}$ |
| $\lambda$ | Gas atom knockout distance | $5 \times 10^{-7}$ cm | $1 \times 10^{-6}$ |
| $r_\text{resol}$ | Destroyed outer-shell thickness | $3 \times 10^{-9}$ cm | N/A |

---

## Thermal Properties

| Property | Value |
|----------|-------|
| Oxide layer thermal conductivity | 2.25 W/m·K |
| Al 6061 cladding thermal conductivity | 167 W/m·K |
| Unirradiated U-10Mo thermal conductivity | 11.2 W/m·K |
| Coolant pressure | 2.7 MPa |
| Coolant velocity | 14.5 m/s |
| Fuel foil thickness | 0.0254 cm |

---

## See Also

- [[2023_Ye_IntegratedSimulationU10Mo]] — index page
- [[wiki/summaries/2023_Ye_IntegratedSimulationU10Mo/PhysicalMechanisms|2023_Ye_IntegratedSimulationU10Mo/PhysicalMechanisms]] — detailed mechanism descriptions
- [[wiki/summaries/2023_Ye_IntegratedSimulationU10Mo/ModelArchitecture|2023_Ye_IntegratedSimulationU10Mo/ModelArchitecture]] — DART/GRASS code and calibration data
- [[wiki/summaries/2020_Beeler_ImprovedEOSXeBubbleUMo|2020_Beeler_ImprovedEOSXeBubbleUMo]] — improved Xe EOS for bubble size calculation
- [[entities/RateTheory]] — rate theory framework for nucleation/re-solution equations
