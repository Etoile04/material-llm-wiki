# Impact of Grain Boundary and Surface Diffusion on Predicted Fission Gas Bubble Behavior and Release in UO2 Fuel (2024, Muntaha et al.)

## Metadata
- **Journal**: Journal of Nuclear Materials, 594 (2024) 155032
- **DOI**: 10.1016/j.jnucmat.2024.155032
- **Material System**: UO2
- **Method**: Hybrid phase-field / cluster dynamics (MOOSE-Xolotl coupling)
- **Key Topic**: Fission gas bubble / grain boundary diffusion / surface diffusion / fission gas release

## Physical Mechanisms
1. **Three-stage fission gas release process**: (1) gas generation within bulk + trapping by intragranular bubbles or diffusion to GBs; (2) GB bubble nucleation, growth, coalescence → interconnected networks; (3) gas flow through TJ tunnels to free surfaces
2. **Fast GB and surface diffusion**: Point defects (U vacancies, Xe atoms) diffuse faster along GBs and surfaces than through bulk, accelerating gas transport
3. **Bubble coalescence and mobility**: Surface diffusivity impacts bubble coalescence and bubble migration along GBs
4. **Re-solution**: Fission fragments can fully re-dissolve xenon bubbles (Turnbull model), releasing mobile Xe back into grains
5. **Equilibrium bubble assumption**: Gas pressure balanced by surface tension at bubble-matrix interface

## Key Equations

### Cluster Dynamics — Xe Cluster Evolution (Xolotl)

$$\frac{\partial C_n}{\partial t} = D_n \nabla^2 C_n + \dot{Y} y_n - Q(C_n)$$

where $C_n$ is the concentration of $n$-Xe clusters, $D_n$ is the cluster diffusivity (only $D_1 > 0$ for single Xe atoms; $D_{n>1} = 0$), $\dot{Y}$ is the fission gas production rate, $y_n$ is the yield fraction, and $Q(C_n)$ represents clustering/re-solution sink terms. Migration energy barriers for clusters are 1.5–2.1 eV higher than for monomers.

### Phase-Field — Allen-Cahn Equation (MARMOT)

$$\frac{\partial \eta_i}{\partial t} = -L \frac{\delta \Omega}{\delta \eta_i}$$

where $\eta_i$ are grain order parameters, $L$ is the mobility, and $\Omega$ is the grand potential functional:

$$\Omega = \int_V \left[\omega(c_g, c_v, \{\eta_i\}) + \sum_i \frac{\kappa_i}{2}|\nabla \eta_i|^2\right] dV$$

### Grand Potential Formulation

$$\omega = f(c_g, c_v, \{\eta_i\}) - \mu_g c_g - \mu_v c_v$$

Chemical potentials:

$$\mu_g = V_a k_g^m(c_g - c_g^{m,eq}), \quad \mu_v = V_a k_v^m(c_v - c_v^{m,eq})$$

Equilibrium bubble composition: $c_v^{b,eq} = 0.546$, $c_g^{b,eq} = 0.454$.

### Heterogeneous Diffusivity Model

$$D_i = \tilde{D}_{bulk} h_{bulk} + \tilde{D}_{GB} h_{GB} + \tilde{D}_{surf} h_{surf}$$

where $i \in \{g, v\}$ (gas or vacancy species). Interpolation functions:

$$h_{GB} = 16 \sum_i \sum_j \eta_i^2 \eta_j^2$$

$$h_{surf} = 16 \eta_0^2 (1 - \eta_0)^2$$

### Hart Approximation for Reduced Interface Diffusivity

$$\tilde{D}_{int} = D_{int} \cdot \frac{w_{int}}{l_{int}} + D_{bulk} \cdot \left(1 - \frac{w_{int}}{l_{int}}\right)$$

where $w_{int}$ is the physical GB/surface width and $l_{int}$ is the diffuse interface width. Required when $l_{int} > w_{int}$ to avoid overestimating GB transport.

### GB Energy and Gradient Coefficient

$$m = \frac{6 \sigma_{GB}}{l_{int}}, \quad \kappa = \frac{3 \sigma_{GB} l_{int}}{4}$$

### Key Diffusivity Ranges at T = 1600 K

| Pathway | U vacancy (m²/s) | Xe (m²/s) |
|---------|-----------------|-----------|
| Bulk | 10⁻²⁰ – 10⁻¹³ | — |
| GB | 10⁻¹⁵ – 10⁻⁸ | 10⁻¹⁶ – 10⁻⁹ |
| Surface | ~10⁻¹⁴ (mass transfer) | — |

## Experimental Data
- Comprehensive literature survey of U vacancy and Xe diffusivities in UO2 bulk, GB, and surfaces
- Reference values from Auskern & Belle (bulk U vacancy), Turnbull (bulk Xe)
- GB diffusivity from Olander & Van Uffelen (two estimates: upper and lower), Liu et al. MD simulations
- Surface diffusivity from mass transfer techniques vs. Zhou & Olander tracer technique

## Model Description
- **Hybrid model**: MARMOT (phase field) coupled with Xolotl (cluster dynamics) via MOOSE framework
- Cluster dynamics handles intragranular gas generation, diffusion, clustering, and re-solution
- Phase field handles GB migration, intergranular bubble growth/coalescence, bubble migration, GB gas diffusion
- 2D and 3D simulations with modified boundary conditions for free surface gas release
- Re-solution model changed from heterogeneous (single atom ejection) to Turnbull model (full bubble re-solution)

## Key Findings
1. **GB diffusivity directly impacts gas release rate** via GB transport; GB diffusivity likely below 10⁴× the lower value from Olander & Van Uffelen (2001)
2. **Surface diffusivity impacts bubble coalescence and mobility**; bubble surface diffusivity likely below 10⁻⁴× the Zhou & Olander (1984) value
3. Fast GB diffusion accelerates gas transport to free surfaces → earlier fission gas release
4. Fast surface diffusion promotes bubble coalescence and changes intergranular bubble morphology
5. Both GB and surface diffusivity values have large uncertainty (many orders of magnitude), motivating parametric studies
6. The Hart approximation must be applied to reduce interface diffusivities when using diffuse interfaces wider than physical GB/surface widths

## Relevance to JSRT Model
- **Directly relevant**: Provides comprehensive diffusivity data and parametric bounds for GB and surface transport in UO2
- The heterogeneous diffusivity framework (bulk/GB/surface) is applicable to JSRT multi-pathway gas transport modeling
- The finding that GB diffusivity must be bounded (not arbitrarily high) informs JSRT parameter calibration
- The hybrid model architecture (cluster dynamics + phase field) offers a framework comparison for JSRT rate-theory approach
- Key insight: GB diffusivity likely 10³-10⁴× bulk (not higher); surface diffusivity likely 10²-10⁴× bulk (not higher)

## Relationships

- [[wiki/entities/PhaseFieldModeling|PhaseFieldModeling]] — MARMOT (MOOSE) phase-field + Xolotl cluster dynamics hybrid model is the methodology
- [[wiki/entities/FissionGasDiffusion|FissionGasDiffusion]] — grain boundary and surface diffusion effects on fission gas bubble behavior and release in UO2
- [[wiki/concepts/RateTheoryFramework|RateTheoryFramework]] — cluster dynamics (Xolotl) handles intragranular gas clustering; heterogeneous diffusivity model provides rate parameters
- [[wiki/summaries/2011_Millett_PhaseFieldGasBubbleKinetics|2011_Millett_PhaseFieldGasBubbleKinetics]] — earlier phase-field gas bubble kinetics model as methodological predecessor
- [[wiki/summaries/2024_Aagesen_VacancyProductionPF|2024_Aagesen_VacancyProductionPF]] — companion work on vacancy production rate parameterization in phase-field models
- [[wiki/summaries/1979_Ronchi_FissionGasSwellingMX_Fuels|1979_Ronchi_FissionGasSwellingMX_Fuels]] — Ronchi's foundational percolation-based gas release model is related

## Related Work
- [[wiki/summaries/2024_Aagesen_VacancyProductionPF|2024_Aagesen_VacancyProductionPF]] — 同期相场空位产生率参数化工作，与本文组成MOOSE相场燃料性能工具链
- [[wiki/summaries/2011_Millett_PhaseFieldGasBubbleKinetics|2011_Millett_PhaseFieldGasBubbleKinetics]] — 早期相场气泡动力学模型，本文MARMOT方法论的先驱
- [[wiki/summaries/2020_Aagesen_BisonUPuZrSwellingLowerLengthScale|2020_Aagesen_BisonUPuZrSwellingLowerLengthScale]] — BISON肿胀模型参数化，本文的扩散系数数据可为其提供输入
- [[wiki/summaries/2018_Liang_3DPhaseFieldIntragranularBubbleUMo|2018_Liang_3DPhaseFieldIntragranularBubbleUMo]] — 3D相场晶内气泡模拟，与本文的晶间气泡/晶界扩散研究互补
- [[wiki/entities/FissionGasDiffusion|FissionGasDiffusion]] — 本文系统梳理了UO₂中体/晶界/表面扩散系数的不确定性范围，是该领域的最新参考
- [[wiki/concepts/FissionGasReleaseModels|FissionGasReleaseModels]] — 晶界扩散直接控制裂变气体释放速率，本文提供了关键的参数约束
