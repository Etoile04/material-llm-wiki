# Fission Gas Bubble Nucleated Cavitational Swelling of the Alpha-Uranium Phase of Irradiated U-Pu-Zr Fuel (1992, Rest)

## Metadata
- **Journal**: Conference proceeding — Effects of Radiation on Materials: 16th International Symposium, ASTM STP 1175 (1993)
- **Report Number**: ANL/CP--76000, DE92 014854
- **Author**: J. Rest (Argonne National Laboratory)
- **Material System**: U-Pu-Zr (specifically U-19Pu-10Zr)
- **Method**: Rate-theory (GRASS-SST / FASTGRASS based)
- **Key Topic**: Cavitational void swelling / void nucleation mechanism

## Physical Mechanisms

1. **Cavitational swelling** identified as potential swelling mechanism for α-U phase of irradiated U-Pu-Zr fuels for the Integral Fast Reactor (IFR).
2. **Gas bubble nucleated void growth**: Gas bubbles formed on grain and phase boundaries during incubation period act as void nuclei. When they exceed critical radius, they transform into cavities growing by bias-driven vacancy influx.
3. **Bias-driven vs. gas-driven growth**: Dislocations preferentially absorb interstitials, creating a net excess vacancy flux to cavities (voids). Below critical radius, cavities are stabilized by gas; above critical radius, they grow as voids.
4. **Reduced re-solution at boundaries**: Gas-atom re-solution is less effective on grain/phase boundary bubbles because ejected atoms remain within the steep concentration gradient and are quickly recaptured.
5. **Interconnection and gas release**: After incubation, cavities interconnect forming pathways for gas release. Subsequent gas production is released directly → linear dependence of gas release on burnup + asymptotic fractional release behavior (~70–80%).
6. **Microstructure**: α-U zone shows "tear-like" porosity — coarse cavities along grain boundaries + finer laminar structure along α/δ phase boundaries.

## Key Equations & Parameters

### Cavity Growth Rate

$$\frac{dR_c}{dt} = \frac{\Omega}{4\pi R_c^2} \left[Z_c D_v C_v - Z_i D_i C_i - Z_v D_v C_{v0}(R_c)\right] \quad \text{(Eq. 1)}$$

where $R_c$ = cavity radius, $\Omega$ = atomic volume, $D_v$, $D_i$ = vacancy/interstitial diffusivities, $C_v$, $C_i$ = vacancy/interstitial fractions, $Z_c$, $Z_i$ = capture efficiencies.

### Thermal Vacancy Concentration Near Cavity

$$C_{v0}(R_c) = C_{v0} \exp\left[-\frac{(P_g - 2\gamma/R_c)\Omega}{kT}\right] \quad \text{(Eq. 2)}$$

where $P_g$ = gas pressure, $\gamma$ = surface energy.

### Bulk Thermal Equilibrium Vacancy Concentration

$$C_{v0} = \exp(-E_{fv}/kT) \quad \text{(Eq. 3)}$$

### Steady-State Vacancy Concentration (recombination-dominated)

$$C_v = \left(\frac{\Omega}{4\pi r_{iv} D_v}\right)^{1/2} K^{1/2} \quad \text{(Eq. 6)}$$

where $K$ = Frenkel pair production rate, $r_{iv}$ = recombination volume radius.

### Critical Radius

$$R_c = \frac{2\gamma}{P_g + kT \ln\left(\frac{(1-Z)C_v}{C_{v0}}\right)} \quad \text{(Eq. 8)}$$

where $Z = Z_{i,d} Z_{v,c} / (Z_c Z_{v,d})$ is the capture efficiency ratio.

### Table 1 Parameters
| Parameter | Value |
|-----------|-------|
| Vacancy formation energy (Efv) | 1.23 eV |
| Pre-exponential vacancy diffusivity (Dv0) | 2.0 × 10⁻⁴ m²/s |
| Vacancy migration energy (Em) | 0.74 eV |
| Recombination volume radius (riv) | 2 × 10⁻¹⁰ m |
| Surface energy (γ) | 1.37 J/m² |
| Atomic volume (Ω) | 4.09 × 10⁻²⁹ m³ |

## Experimental Data

- **Fuel**: 0.290-inch U-19Pu-10Zr fuel elements
- **Irradiation temperature**: 673 K (for GRASS-SST calculations)
- **Swelling behavior**: 
  - Incubation period before rapid swelling onset
  - Cavitational swelling peaks at ~773 K
  - Decreases above (vacancy emission) and below (reduced mobility) peak temperature
- **Gas release**: Nearly linear dependence on burnup after incubation; asymptotic ~70–80% fractional release
- **Critical radius transition**: At ~0.10 at.% burnup, intergranular bubble radius exceeds critical radius for bias-driven growth → consistent with observed incubation dose

## Model Description

1. **Based on GRASS-SST / FASTGRASS codes**: Mechanistic models for fission gas bubble behavior.
2. **Gas bubble kinetics**: Calculates intergranular bubble density and radius as function of burnup using GRASS-SST code.
3. **Critical radius criterion**: Determines when gas-driven growth transitions to bias-driven (void) growth.
4. **Bubble distribution evolution**: As irradiation proceeds, distribution broadens and peak shifts to larger sizes.
5. **Key result**: At fuel burnups > ~0.10 at.%, intergranular bubbles exceed critical radius and grow as voids → consistent with observed incubation period.
6. **Scoping calculations**: Stand-alone model calculates fuel swelling of α-U zone vs. temperature at ~1 at.% burnup.

## Key Findings

1. **Cavitational swelling is a viable mechanism** for α-U phase of U-Pu-Zr fuel.
2. **Gas bubbles on grain/phase boundaries** evolve to sizes that can serve as void nuclei.
3. **Critical radius concept** explains the observed incubation period for rapid swelling and gas release.
4. **Intergranular bubbles reach critical size at ~0.10 at.% burnup** at 673 K — consistent with experimental incubation dose.
5. **Swelling peaks at ~773 K** — decreases at higher T (vacancy emission) and lower T (reduced mobility).
6. **Gas release from α zone is only weakly dependent on swelling mechanism** — once interconnected porosity forms, gas release is dominated by the dense porosity network.
7. **Bubble growth within bulk material is suppressed** by irradiation-induced gas atom re-solution → only boundary bubbles reach critical size.

## Relevance to JSRT Model

- **Foundational paper**: This is the original conference paper where Rest proposed the cavitational void swelling model for metallic fuel. It is a direct precursor to the 1993 JNM paper.
- **Critical radius formulation**: Eqs. 1–8 form the mathematical basis of the cavitational swelling model used in JSRT.
- **Parameter set**: Table 1 provides the original parameter values (note: vacancy migration energy of 0.74 eV was later revised to 1.28 eV in 1993, and then to 0.34 eV by Yun 2022).
- **Transition criterion**: The gas-driven → bias-driven growth transition is central to JSRT.
- **Incubation period physics**: Reduced nucleation efficiency on α/δ phase boundaries explains long incubation times — relevant for JSRT modeling of swelling onset.

## Relationships

- [[wiki/entities/CavitationalVoid|CavitationalVoid]] — gas-bubble-nucleated cavitational void swelling is the central mechanism of this paper
- [[wiki/concepts/RateTheoryFramework|RateTheoryFramework]] — rate-theory equations (cavity growth, vacancy/interstitial kinetics) are derived using GRASS-SST
- [[wiki/entities/FuelAlloy|FuelAlloy]] — U-Pu-Zr metallic fuel alloy α-phase swelling behavior is modeled
- [[wiki/summaries/1990_Hofman_SwellingBehaviorUPuZr|1990_Hofman_SwellingBehaviorUPuZr]] — Hofman's experimental observations on α-U phase tearing provide the empirical basis
- [[wiki/summaries/1993_Rest_VoidSwellingAlphaU|1993_Rest_VoidSwellingAlphaU]] — this 1992 conference paper is the precursor to Rest's definitive 1993 JNM paper
- [[wiki/concepts/SwellingMechanisms|SwellingMechanisms]] — distinguishes gas-driven vs. bias-driven void growth transitions
