# Integrated Simulation U-10Mo — Physical Mechanisms

*Sub-page of [[2023_Ye_IntegratedSimulationU10Mo]]*

---

## 1. Fission Gas Bubble Nucleation

### Intragranular
- **Dimer-based nucleation model** — two Xe atoms form a bubble nucleus
- Nucleation rate depends on gas atom concentration, diffusivity, and nucleation probability $f_N$

### Intergranular
- Similar to intragranular but with grain boundary (GB) diffusion enhancement factor $z$ (calibrated: $3 \times 10^4$)

---

## 2. Radiation-Induced Bubble Re-solution

- Fission fragments traverse bubbles, ejecting gas atoms (thermal spike mechanism)
- **Size-dependent**: Small bubbles ($r_b \leq \lambda$) are completely destroyed; large bubbles only lose outer shell of thickness $r_\text{resol}$
- Competing effect with bubble growth — higher fission rate enhances both diffusion and re-solution

---

## 3. Bubble Growth via Coalescence

- Bubbles grow by coalescence with other bubbles and gas atoms
- Probability depends on:
  1. Random Brownian motion (diffusivity inversely proportional to bubble volume)
  2. Biased migration in temperature gradient (negligible for thin U-10Mo foils)

---

## 4. Gas Atom Migration to Grain Boundaries

- Gas atoms generated as fission products within grains
- Migrate to GBs via diffusion (concentration + temperature gradient)
- Repeated trapping by intragranular bubbles and radiation-induced re-solution (Speight's model)
- Upon reaching grain faces → grain edges → grain corners (triple points)

---

## 5. Grain Subdivision (Recrystallization)

- Occurs at intermediate-to-high fission densities (> 2 × 10²¹ fissions/cm³)
- Grain size decreases from tens of μm to sub-μm (~0.5 μm)
- Increases GB area per unit volume → accelerates swelling (nonlinear regime)
- **Gas sweeping**: All bulk gas atoms swept to grain boundaries upon recrystallization — one-off event causing abrupt porosity increase
- Grain-size-dependent kinetics: larger grains recrystallize later

---

## 6. Temperature Effect on Swelling

- Apparent fission rate effect is actually a **temperature effect**
- Higher temperature → larger bubble volume (via equation of state), not increased thermal diffusion
- Effect stronger for large bubbles → swelling difference grows with fission density
- Isolating temperature from radiation-driven processes showed 34°C difference caused ~9% absolute swelling difference at $6 \times 10^{21}$ fis/cm³

---

## See Also

- [[2023_Ye_IntegratedSimulationU10Mo]] — index page
- [[2023_Ye_IntegratedSimulationU10Mo/KeyEquations]] — Xe diffusivity, nucleation, re-solution, and swelling equations
- [[2023_Ye_IntegratedSimulationU10Mo/ModelArchitecture]] — DART/GRASS code structure and calibration
- [[2001_Rest_GRSIS_FissionGasMetallic]] — GRASS module origins
- [[2005_Rest_RecrystallizationSwellingUO2UMo]] — grain subdivision model
- [[entities/Recrystallization]] — grain refinement and HBS formation
- [[entities/FissionGasDiffusion]] — gas atom migration to grain boundaries
