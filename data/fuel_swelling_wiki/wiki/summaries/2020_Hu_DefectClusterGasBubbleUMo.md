# Defect Cluster and Nonequilibrium Gas Bubble Associated Growth in Irradiated UMo Fuels

## Metadata
- **Title:** Defect cluster and nonequilibrium gas bubble associated growth in irradiated UMo fuels – A cluster dynamics and phase field model
- **Authors:** Shenyang Hu, Wahyu Setyawan, Benjamin W. Beeler, Jian Gan, Douglas E. Burkes
- **Year:** 2020
- **Journal:** Journal of Nuclear Materials, 542, 152441
- **DOI:** 10.1016/j.jnucmat.2020.152441
- **Affiliations:** Pacific Northwest National Laboratory; Idaho National Laboratory; North Carolina State University
- **Fuel System:** U-10wt%Mo (UMo) monolithic fuel

## Physical Mechanisms

### Irradiation-Induced Recrystallization
- Refines grains from several μm coarse grains to 200-300 nm fine grains
- Dramatically speeds up gas bubble swelling kinetics
- Gas bubble superlattice collapses in recrystallization zone
- Gas bubbles with uniform distribution and low density form

### Gas Bubble Growth in Coarse Grains
- Nano-sized bubbles form FCC superlattice
- Bubble density ~1-4 × 10²⁴/m³
- Internal pressure: few GPa (Xe bubbles)
- Compressive stress from dense nano-bubbles prevents interstitial accumulation
- Low vacancy concentration → slow bubble growth

### Gas Bubble Growth in Recrystallization Zone
- Small grain size (200-300 nm) + low bubble density releases matrix stress
- **Interstitial clustering is energetically favored** → more vacancies for bubble growth
- Faster swelling kinetics than coarse grains
- **Key hypothesis:** Interstitial clustering drives fast gas bubble growth

### Defect Production
- ²³⁵U fission generates ~14,825 Frenkel pairs per fission in γU
- Gas atoms, vacancies, interstitials, and clusters continuously produced
- Bubble growth requires both gas atoms AND vacancies
- Bubbles grow with vacancy absorption, shrink with interstitial absorption

## Key Equations

### Cluster Dynamics Rate Equations (Eq. 2)
$$\frac{dC_i(x,t)}{dt} = \nabla[D_i\nabla C_i + D_i C_i \nabla U_i/k_BT] + \dot{G}_i - \alpha C_i C_j + K_{lj}^{(2)} C_j C_i^2 + \sum_{m=3}^{M_I}\left[\dot{\gamma}_{li}^{(m)} - K_{li}^{(m)} C_i\right]$$

### KKS Phase-Field Free Energy (Eq. 8)
$$G = p(\chi)f_b(c_v^b) + (1-p(\chi))f_m(c_v^m) + wg(\chi)$$

where $p(\chi) = \chi^3(10 - 15\chi + 6\chi^2)$, $g(\chi) = 30\chi^2(1-\chi)^2$

### Total Free Energy (Eq. 9)
$$F(C_{gV}, \chi) = \int\left[G(C_{gV}, \chi) + \frac{\kappa}{2}|\nabla\chi|^2\right]d\Omega$$

### Gas Bubble Evolution (Eq. 12-13)
$$\frac{\partial C_{gV}}{\partial t} = \nabla\left[D_{gV}\frac{\partial G}{\partial C_{gV}}\nabla C_{gV}\right] + \dot{S}_{V,bb} - \dot{S}_{I,bb} + \text{cluster sink terms}$$

$$\frac{\partial\chi}{\partial t} = L\left[-\frac{\partial}{\partial\chi}\left(\frac{\kappa}{2}|\nabla\chi|^2\right) + p'(\chi)\left[f_m(c_v^m) - f_b(c_v^b) - (c_v^m - c_v^b)\frac{\partial f_m}{\partial c_v^m}\right] + wg'(\chi)\right]$$

### Gas Phase Evolution (Eq. 14-15)
$$G_1 = A_{bb}(C_{gg} - C_{gg}^{eq})^2$$
$$\frac{\partial C_{gg}}{\partial t} = \nabla[D_{gg}\nabla\frac{\partial G_1}{\partial C_{gg}}] + \dot{S}_{g,bb}$$

## Parameters

| Parameter | Value | Notes |
|-----------|-------|-------|
| Frenkel pairs per fission | ~14,825 | in γU |
| Displacement threshold energy | 35.6 eV | γU at 800K |
| Recrystallized grain size | 200-300 nm | |
| Coarse grain size | several μm | |
| Bubble density (coarse) | 1-4 × 10²⁴/m³ | superlattice |
| Bubble density (recrystallized) | lower | uniform distribution |
| Xe bubble pressure (nano) | few GPa | |
| Nucleation check interval | N₁ = 5000 steps | |
| Critical vacancy concentration | c_crt = 1.0 | for nucleation |
| Gas equilibrium concentration | C_eq_gg = 0.45 | inside bubbles |
| Interface mobility | L | calibrated |
| Gradient coefficient | κ | from interfacial energy |

### Thermodynamic Properties (Table 2)
| Property | Value |
|----------|-------|
| U vacancy formation energy | ~1.6 eV |
| U interstitial formation energy | ~1.1 eV |
| Xe substitutional energy | 6.1 eV |
| Divacancy binding energy | -1.2 eV |
| Xe sub-vacancy pair binding | -0.4 eV |

## Experimental Data

- PIE data used for model calibration
- Gas bubble swelling kinetics compared before/after recrystallization
- Measured vs simulated kinetics matched by adjusting defect generation, clustering, emission, and sink rates

## Key Findings

1. **Interstitial clustering** is a key physical mechanism for fast gas bubble swelling in recrystallization zone
2. First coupled **cluster dynamics + phase-field** model for gas bubble evolution in UMo
3. Model can describe **nonequilibrium gas bubbles**: transition from over-pressurized to void-like
4. Small grain size + low bubble density in recrystallized zone → matrix stress release → interstitial clustering favored
5. Defect emission zones (non-uniform) used instead of uniform redistribution
6. Statistical nucleation method based on total vacancy concentration threshold
7. Model extensible to defect + second-phase precipitate associated growth

## Relationships to Other Work

- **Hu et al. (2016, 2017):** Previous Booth model and rate-theory-phase-field recrystallization model
- **Beeler et al. (2020):** Xe bubble EOS (this batch) - provides thermodynamic input
- **Liang et al. (2016-2018):** Phase-field models of recrystallization and bubble evolution in U-Mo
- **Robinson et al. (2021):** Experimental swelling correlation (this batch) - provides validation data
- **Setyawan et al.:** Fission product yield calculations used for defect generation

## Relationships

- [[wiki/entities/PhaseFieldModeling|PhaseFieldModeling]] — first coupled cluster dynamics + phase-field model for gas bubble evolution in U-Mo
- [[wiki/entities/Recrystallization|Recrystallization]] — recrystallization-driven grain refinement changes bubble growth kinetics fundamentally
- [[wiki/entities/FuelAlloy|FuelAlloy]] — U-10Mo monolithic fuel gas bubble growth in coarse and recrystallized grains
- [[wiki/entities/FissionGasDiffusion|FissionGasDiffusion]] — nonequilibrium gas bubble associated growth via defect cluster dynamics
- [[wiki/concepts/RateTheoryFramework|RateTheoryFramework]] — cluster dynamics rate equations (vacancies, interstitials, gas atoms) are the core framework
- [[wiki/summaries/2020_Beeler_ImprovedEOSXeBubbleUMo|2020_Beeler_ImprovedEOSXeBubbleUMo]] — Xe bubble EOS provides thermodynamic input
- [[wiki/summaries/2018_Liang_3DPhaseFieldIntragranularBubbleUMo|2018_Liang_3DPhaseFieldIntragranularBubbleUMo]] — 3D phase-field bubble model that this work extends with cluster dynamics
- [[wiki/summaries/2013_Kim_RecrystallizationFGBSwellingUMo|2013_Kim_RecrystallizationFGBSwellingUMo]] — experimental context for recrystallization-driven swelling enhancement
