# TEM Characterization of Fission Gas Bubble Superlattice in Irradiated U–7 wt%Mo Dispersion Fuels

**Authors:** B.D. Miller, J. Gan, D.D. Keiser Jr., A.B. Robinson, J.F. Jue, J.W. Madden, P.G. Medvedev  
**Year:** 2015  
**Journal:** Journal of Nuclear Materials, 458, 115–121  
**DOI:** 10.1016/j.jnucmat.2014.12.012  
**Affiliation:** Idaho National Laboratory  
**Material:** U–7 wt%Mo dispersion fuel in Al-Si matrix  
**Techniques:** TEM (JEOL-2010, 200 keV), FIB lift-out, SEM, EDS

---

## Overview

This TEM study characterizes the evolution of the [[wiki/entities/GasBubbleSuperlattice|fission gas bubble superlattice]] in U–7 wt%Mo dispersion fuel across fission densities from 3.0 to 5.2 × $10^{21}$ fiss/cm³. The superlattice forms an FCC structure coherent with the BCC U-Mo matrix — the first reported non-isomorphic case.

**Key transitions:**
- **<3.0 × $10^{21}$ fiss/cm³**: Superlattice fully ordered with saturated bubble size 3.1–3.6 nm
- **3.0–4.5 × $10^{21}$ fiss/cm³**: Bubble size saturated; additional gas goes to grain boundaries
- **~4.5 × $10^{21}$ fiss/cm³**: [[wiki/entities/Recrystallization|Grain subdivision]] triggers superlattice collapse; 0.1–1 μm intergranular bubbles form; solid FP precipitate on bubble surfaces

The formation mechanism (1-D SIA migration along ⟨110⟩) is elucidated computationally in [[wiki/summaries/2016_Hu_GasBubbleSuperlatticeFormationPF|Hu 2016]].

---

## Key Equations

> This is primarily an experimental TEM paper. The following equations are reconstructed from the reported quantitative data and domain knowledge for modeling purposes.

### GBS Number Density from Superlattice Constant

For an FCC superlattice with lattice constant $a_{SL}$ in the BCC host:

$$N_b = \frac{4}{a_{SL}^3}$$

With $a_{SL} = 12\,\text{nm}$: $N_b \approx 2.3 \times 10^{23}\,\text{m}^{-3}$.

### GBS-Induced Swelling

$$\frac{\Delta V}{V}_{GBS} = \frac{4}{3}\pi \bar{r}_b^3 \cdot N_b$$

With saturated bubble radius $\bar{r}_b = 3.1\text{--}3.6\,\text{nm}$ and $N_b$ above: $\Delta V/V \approx 0.3\text{--}0.5\%$.

### Fission Gas Production Rate

$$\dot{c}_{Xe} = y_{Xe} \cdot \dot{f}$$

where $y_{Xe} \approx 0.25$ atoms/fission (Xe yield) and $\dot{f}$ is the fission rate density.

### GBS Formation Window

$$0.15\,T_m \leq T_{irr} \leq 0.35\,T_m$$

### Bubble Size Saturation Criterion (Reconstructed)

The bubble size saturates when the gas supply rate equals the re-solution loss rate:

$$\frac{d\bar{r}_b}{dt} = 0 \quad \text{when} \quad \dot{f} \cdot V_{Xe} \cdot y_{Xe} = b \cdot n_b$$

Beyond saturation (~3.0 × 10²¹ fiss/cm³), additional gas migrates to grain boundaries rather than growing existing GBS bubbles.

### 1-D SIA Diffusion Anisotropy Ratio

$$D^* = \frac{D_{SIA}^{\langle 110 \rangle}}{D_{Xe}} \geq 10^4$$

This ratio (from Hu 2016) explains why the FCC superlattice forms in the BCC host: fast 1-D SIA migration along $\langle 110 \rangle$ directions creates anisotropic vacancy fluxes.

## Detailed Sections

- [[wiki/summaries/2015_Miller_TEMGasBubbleSuperlatticeU7Mo/StructureFormation|Structure & Formation Mechanisms]] — FCC-in-BCC superlattice, saturation, grain subdivision collapse, proposed mechanisms
- [[wiki/summaries/2015_Miller_TEMGasBubbleSuperlatticeU7Mo/ExperimentalData|Experimental Data & Measurements]] — TEM measurements, irradiation conditions, comparison with ion-irradiated systems

---

## Relationships

- [[wiki/entities/GasBubbleSuperlattice|GasBubbleSuperlattice]] — Primary subject: FCC superlattice in BCC U-7Mo, saturation at ~3.1–3.6 nm, and collapse at ~4.5×10²¹ f/cm³
- [[wiki/entities/Recrystallization|Recrystallization]] — Grain subdivision analogy to UO₂ rim effect; collapse triggers
- [[wiki/entities/FuelAlloy|FuelAlloy]] — U-7 wt% Mo dispersion fuel in Al-Si matrix is the subject material
- [[wiki/entities/FissionGasDiffusion|FissionGasDiffusion]] — fission gas (Xe, Kr) self-organization into nanoscale bubbles via radiation-driven processes
- [[wiki/summaries/2016_Hu_GasBubbleSuperlatticeFormationPF|Hu 2016]] — Phase-field model explaining 1-D SIA formation mechanism
- [[wiki/summaries/2013_Kim_RecrystallizationFGBSwellingUMo|Kim 2013]] — Recrystallization & FGB swelling model; complements this TEM study
- [[wiki/summaries/2015_Gan_ThermalStabilityGasBubbleSuperlattice|Gan 2015]] — Thermal stability of the gas bubble superlattice
- [[wiki/summaries/2017_Casella_CharacterizationFissionGasBubblesU10Mo|Casella 2017]] — Further characterization of fission gas bubbles in U-10Mo

---

*Source: Miller, B.D. et al. (2015). Journal of Nuclear Materials, 458, 115–121.*

## Related Work
- [[wiki/summaries/2015_Gan_ThermalStabilityGasBubbleSuperlattice|2015_Gan_ThermalStabilityGasBubbleSuperlattice]] — companion in-situ heating TEM study on GBS thermal stability
- [[wiki/summaries/2016_Hu_GasBubbleSuperlatticeFormationPF|2016_Hu_GasBubbleSuperlatticeFormationPF]] — phase-field model explaining the 1-D SIA formation mechanism observed here
- [[wiki/summaries/2013_Kim_RecrystallizationFGBSwellingUMo|2013_Kim_RecrystallizationFGBSwellingUMo]] — recrystallization-driven swelling model linked to GBS collapse threshold
- [[wiki/summaries/2017_Casella_CharacterizationFissionGasBubblesU10Mo|2017_Casella_CharacterizationFissionGasBubblesU10Mo]] — further characterization of post-recrystallization fission gas bubbles in U-10Mo
- [[wiki/summaries/2023_Smith_EarlySelfOrganizationGBS|2023_Smith_EarlySelfOrganizationGBS]] — early-stage self-organization of gas bubble superlattice modeling
- [[wiki/entities/GasBubbleSuperlattice|GasBubbleSuperlattice]] — primary subject: FCC-in-BCC superlattice structure, saturation, and collapse
