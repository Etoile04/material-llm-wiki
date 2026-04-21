# Formation of Gas Bubble Superlattice in U-Mo Alloys: A Phase-Field Study

## Metadata

- **Title:** Formation of gas bubble superlattice in U-Mo alloys: A phase-field study
- **Authors:** Yanbo Jiang, Shisen Gao, Yongxiao La, Wenbo Liu
- **Year:** 2025
- **Journal:** Nuclear Engineering and Design, 435, 113912
- **DOI:** 10.1016/j.nucengdes.2025.113912
- **Affiliations:** Xi'an Jiaotong University

## Physical Mechanisms

### Gas Bubble Superlattice (GBS) Formation
- **GBS characteristics in U-Mo:**
  - Intragranular bubble diameter: ~1–3 nm
  - FCC superlattice structure within BCC U matrix
  - Lattice constants: 7–12 nm
  - Observed at low fission densities only
- **Primary mechanism:** One-dimensional (1D) directional migration of self-interstitial atoms (SIAs) along 〈110〉 direction creates a **shadow effect** — depletion zones behind existing bubbles prevent new nucleation, leading to ordered arrangements
- **SIA diffusion:** Two types with different fast-diffusion directions: one along [11̄0], another along [01]

### Grain Boundary Effects on GBS
- **Denuded zone:** Region adjacent to GB free of bubbles, where vacancy concentration is depleted
- **Peak zone:** Region with elevated bubble density beyond the denuded zone
- **Denuded zone width** increases with GB absorption coefficient (stronger sinks = wider denuded zone)
- **Theoretical derivation:** Using 1D steady-state vacancy diffusion equation to relate denuded zone width to GB absorption strength

### GBS Stability
- At higher fission densities, bubble size and lattice constants remain nearly constant
- GBS maintains structural stability once formed

## Key Equations

### Total Free Energy
$$F = \int [f_{chem} + f_{poly} + f_{double-well} + f_{gradient}] dV$$

Where:
- $f_{chem}$: Chemical free energy density (matrix + bubble phases)
- $f_{poly}$: Polycrystalline energy density (grain boundary energy)
- $f_{double-well}$: Phase transition energy barrier
- $f_{gradient}$: Interface energy density

### Chemical Free Energy
$$f_{chem} = h(\eta) f^b(c_v, c_g) + [1 - h(\eta)] f^m(c_v, c_g) + Wg(\eta)$$

Where $h(\eta)$ is interpolation function, $f^b$ and $f^m$ are bubble and matrix free energy densities, $Wg(\eta)$ is double-well potential.

### KKS Model
- Matrix phase: $c_v + c_g = 0$ (no vacancies or gas in matrix)
- Bubble phase: $c_v + c_g = 1.0$, $c_i = 0.0$ (no SIAs in bubble)
- Chemical potential equality constraint between phases

### Allen-Cahn Evolution
$$\frac{\partial \eta}{\partial t} = -L_\eta \frac{\delta F}{\delta \eta}$$

### Explicit Nucleation Algorithm
- Nucleation probability calculated from local vacancy and gas atom concentrations
- Nucleation rate: $J = J_0 \exp(-\Delta G^*/kT)$

### 1D Steady-State Vacancy Diffusion (Denuded Zone)
$$D_v \frac{d^2 c_v}{dx^2} + \dot{F} - k_{iv} c_i c_v = 0$$
With GB boundary condition: $D_v \frac{dc_v}{dx}\bigg|_{x=0} = -k_a c_v(0)$

## Parameters

### Simulation Parameters
| Parameter | Value/Range |
|-----------|-------------|
| Material | U-7wt.%Mo |
| Bubble diameter (simulation) | ~2-3 nm |
| Lattice constant | 7-12 nm |
| SIA diffusion directions | [11̄0] and [01] |
| GB absorption coefficient | Variable (parametric study) |

### Key Variables
| Symbol | Description |
|--------|-------------|
| $c_v(r,t)$ | Vacancy concentration |
| $c_g(r,t)$ | Gas atom concentration |
| $c_1(r,t), c_2(r,t)$ | SIA concentrations (two diffusion directions) |
| $\eta$ | Order parameter (bubble=1.0, matrix=0.0) |
| $\phi_i(r,t)$ | Grain order parameters |

## Experimental Data

### Simulation Results
1. **Single crystal GBS:** Bubble diameter and lattice constant match experimental results from literature (Gan et al. 2010; Van den Berghe et al. 2008; Miller et al. 2015)
2. **GB influence:** Surrounding region divided into denuded zone and peak zone
3. **Denuded zone width vs GB absorption:** Phase-field results consistent with theoretical predictions from 1D diffusion analysis
4. **Shadow effect:** Directional SIA migration creates ordered bubble patterns by preventing nucleation in depletion shadows

### Key Findings
1. 1D SIA diffusion is the primary mechanism for GBS formation (consistent with Hu et al. 2016)
2. GB absorption strength directly controls denuded zone width — stronger sinks produce wider denuded zones
3. GBS exhibits structural stability at higher fission densities
4. The KKS model + explicit nucleation algorithm successfully reproduces GBS formation dynamics

## Relationships to Other Work

- **Hu et al. (2016):** Phase-field + Monte Carlo model — 1D SIA migration mechanism confirmed; current model improves by including continuous fission gas generation
- **Aagesen et al. (2021):** Large-scale functional phase-field model — current work extends to polycrystalline systems with GB effects
- **Gan et al. (2010, 2017):** Experimental GBS characterization — simulation results validated against
- **Smith et al. (2023):** Early self-organization of GBS — complementary experimental observations
- **Aagesen et al. (2024):** Vacancy production rate parameterization — relevant for improving input parameters

## Relationships

- [[wiki/entities/GasBubbleSuperlattice|GasBubbleSuperlattice]] — FCC GBS formation in BCC U-Mo via 1D SIA migration and grain boundary effects is the central subject
- [[wiki/entities/PhaseFieldModeling|PhaseFieldModeling]] — KKS phase-field model with explicit nucleation algorithm for polycrystalline GBS
- [[wiki/entities/FuelAlloy|FuelAlloy]] — U-7 wt% Mo alloy in BCC γ-phase is the material system
- [[wiki/entities/FissionGasDiffusion|FissionGasDiffusion]] — continuous fission gas generation and SIA directional migration are the driving forces
- [[wiki/summaries/2016_Hu_GasBubbleSuperlatticeFormationPF|2016_Hu_GasBubbleSuperlatticeFormationPF]] — Hu (2016) established the 1D SIA mechanism; this model extends it to polycrystalline systems
- [[wiki/summaries/2024_Aagesen_VacancyProductionPF|2024_Aagesen_VacancyProductionPF]] — companion vacancy production rate parameterization work
- [[wiki/summaries/2023_Smith_EarlySelfOrganizationGBS|2023_Smith_EarlySelfOrganizationGBS]] — experimental GBS early self-organization that this model explains
