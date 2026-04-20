# An Improved Equation of State for Xe Gas Bubbles in γU-Mo Fuels

## Metadata
- **Title:** An improved equation of state for Xe gas bubbles in γU-Mo fuels
- **Authors:** Benjamin W. Beeler, Shenyang Hu, Yongfeng Zhang, Yipeng Gao
- **Year:** 2020
- **Journal:** Journal of Nuclear Materials, 530, 151961
- **DOI:** 10.1016/j.jnucmat.2019.151961
- **Affiliations:** North Carolina State University; Idaho National Laboratory; Pacific Northwest National Laboratory
- **Fuel System:** U-10Mo (γ phase) monolithic fuel

## Physical Mechanisms

### Xe Bubble Thermodynamics
- Xe atoms in γU-Mo: substitutional is low-energy configuration (6.1 eV formation energy)
- Xe always energetically favored to reside in bubble vs. bulk lattice (negative binding energy for all Xe/Vac ratios)
- Relative bubble energy increases **quadratically** with Xe/vacancy ratio
- Larger bubbles exhibit more rapid energy increase (harder to achieve high Xe/Vac ratio)

### Under-to-Over-Pressurized Transition
- Below equilibrium Xe/Vac ratio: system volume < equilibrium U-10Mo volume
- Above equilibrium Xe/Vac ratio: system volume > equilibrium volume
- Transition at Xe/Vac ratio: 0.13 (3.1 nm) to 0.20 (8.5 nm diameter)
- Maximum Xe/Vac ratio achieved: ~0.5

### Surface Energy
- Void surface energy converges to ~1.2 J/m² for radii >1.5 nm
- Consistent across 400-700 K temperature range

### Young-Laplace Equation Limitation
- Standard Young-Laplace equation ($P = 2\gamma/R$) **does not hold** for bubbles <10 nm
- Overpredicts equilibrium pressure for small bubbles
- Convergence to Young-Laplace for bubbles >6 nm radius

## Key Equations

### Void Surface Energy (Eq. 1)
$$E_{surf} = \frac{(E^* - E) \cdot N}{A}$$

### Bubble Formation Energy (Eq. 2)
$$E_{bub}^f = \frac{E_{bub} - N_{void} \cdot E_{sys}}{N_{sys}}$$

### Xe Binding Energy (Eq. 3)
$$E_{bind} = E(n) - E(n-1) - E_{Sub}^{Xe} + E_{Vac}$$

### Modified Young-Laplace Equation (Eq. 7) ⭐
$$P = \frac{2\gamma}{R} - A \cdot \exp(-B \cdot R)$$

where $\gamma = 1.2$ J/m², $A = 4.94$, $B = -0.87$ (GPa, nm units). Decays to standard Young-Laplace for $R > 6$ nm.

### Kaplun EOS (Eq. 8)
$$P = \frac{RT}{v}\left(1 + \frac{c}{v - b}\right) - \frac{a}{v^2}$$

Optimized parameters: $a = -870912.08$ J·cm³/mol², $b = 27.133$ cm³/mol, $c = 88.987$ cm³/mol

### Virial EOS (Eq. 9) ⭐ (recommended)
$$P = \frac{RT}{v}\left(1 + \frac{B}{v} + \frac{C}{v^2} + \frac{D}{v^3}\right)$$

where $B = b_0 + b_1/T + b_2/T^2$, $C = c_0 + c_1/T + c_2/T^2$, $D = d_0 + d_1/T + d_2/T^2$

## Parameters

### Virial EOS Parameters (Table 3)

| Parameter | Value | Units |
|-----------|-------|-------|
| $b_0$ | 197.229 | cm³/mol |
| $b_1$ | 120307.145 | cm³·K/mol |
| $b_2$ | 60.555 | cm³·K²/mol |
| $c_0$ | -22038.723 | cm⁶/mol² |
| $c_1$ | 2292.793 | cm⁶·K/mol² |
| $c_2$ | -117.564 | cm⁶·K²/mol² |
| $d_0$ | 1030015.045 | cm⁹/mol³ |
| $d_1$ | -5.200 | cm⁹·K/mol³ |
| $d_2$ | -280.677 | cm⁹·K²/mol³ |

### Point Defect Energies (Table 1, 400K)

| Defect | Formation Energy (eV) | Binding Energy (eV) |
|--------|----------------------|---------------------|
| Vacancy | 1.6 | - |
| Interstitial | 1.1 | - |
| Xe substitutional | 6.1 | - |
| Divacancy | 2.1 | -1.2 |
| Xe sub-vac pair | 7.4 | -0.4 |

### Simulation Parameters
| Parameter | Value |
|-----------|-------|
| Supercell | 40×40×40 BCC (128,000 atoms) |
| Mo content | ~22 at% (U-10wt%Mo) |
| Temperature range | 400-700 K |
| Bubble diameters | 3.1-12.6 nm |
| Xe/Vac ratio range | 0-0.5 |
| Interatomic potential | U-Mo-Xe EAM (Smirnova et al.) |
| Software | LAMMPS |

## Key Findings

1. **Virial EOS** is most accurate: 5.7% NRMSD, 9.0% total relative error (vs. Kaplun: 6.5%/10.3%)
2. **Negative $a$ parameter** in Kaplun EOS indicates additional repulsion (atypical for isolated gases)
3. Xe/Vac ratio **decreases with increasing bubble diameter** (contradicts constant ratio assumption)
4. Xe/Vac ratios in this study are **lower** than previous estimates but pressures are similar
5. Young-Laplace equation modification will **dramatically change** suggested equilibrium state for small fission gas bubbles
6. Equilibrium pressure extrapolation to zero binding energy → Xe/Vac ≈ 0.94
7. **Temperature dependence of modified Young-Laplace** assumed minimal (surface energy constant)

## Relationships to Other Work

- **Hu et al. (2017):** Previous EOS for small bubbles (<2 nm, >2 GPa); parameters used as starting guess
- **Hu et al. (2020):** Cluster dynamics model (this batch) - uses EOS as input
- **Xiao et al. (2014, 2015):** MD simulations of small Xe bubbles in U-Mo
- **Smirnova et al. (2013):** U-Mo-Xe EAM interatomic potential used
- **Kaplun & Meshalkin (2003):** Original modified van der Waals EOS formalism
- **Kim & Hofman (2011):** ANL swelling correlation
- **Robinson et al. (2021):** INL swelling correlation (this batch)
- **Directly applicable to:** Mesoscale phase-field and rate theory models of fission gas swelling

## Relationships

- [[wiki/entities/FuelAlloy|FuelAlloy]] — γU-Mo (U-10Mo bcc phase) is the material system for Xe bubble EOS
- [[wiki/entities/FissionGasDiffusion|FissionGasDiffusion]] — Xe bubble thermodynamics (EOS, surface energy, pressure) are central inputs
- [[wiki/entities/PhaseFieldModeling|PhaseFieldModeling]] — the improved EOS directly feeds phase-field and rate-theory models of bubble evolution
- [[wiki/concepts/SwellingMechanisms|SwellingMechanisms]] — Xe bubble equilibrium pressure and Xe/vacancy ratio are key parameters for swelling models
- [[wiki/summaries/2016_Hu_GasBubbleSuperlatticeFormationPF|2016_Hu_GasBubbleSuperlatticeFormationPF]] — phase-field superlattice model uses Xe EOS as input
- [[wiki/summaries/2018_Liang_3DPhaseFieldIntragranularBubbleUMo|2018_Liang_3DPhaseFieldIntragranularBubbleUMo]] — 3D bubble phase-field model benefits from improved EOS
- [[wiki/summaries/2022_Jian_FissionGasSwellingModelU10Mo|2022_Jian_FissionGasSwellingModelU10Mo]] — fission gas swelling model for U-10Mo that builds on this EOS
