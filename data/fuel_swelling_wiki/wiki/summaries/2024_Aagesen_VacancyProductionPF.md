# Parameterization of Vacancy Production Rate in Phase-Field Models of Fission Gas Bubble Evolution (2024, Aagesen)

## Metadata
- **Journal**: Journal of Nuclear Materials, 601 (2024) 155311
- **DOI**: 10.1016/j.jnucmat.2024.155311
- **Material System**: UO2 / U-(Pu)-Zr (general methodology)
- **Method**: Phase-field (KKS formulation) + analytical models
- **Key Topic**: Vacancy production rate / parameterization / source-only vs source+sink

## Physical Mechanisms
1. **Frenkel pair production**: Energetic fission fragments create collision cascades → interstitial-vacancy pairs (Frenkel pairs)
2. **Rapid recombination**: Many Frenkel pairs recombine quickly after cascade; net vacancy production much lower than Frenkel pair production rate
3. **Biased sink absorption**: Interstitials preferentially absorbed at dislocation sinks → net excess vacancies → bubble/void growth
4. **Vacancy supersaturation**: Irradiation-induced defect supersaturation drives bubble growth ("chemical stress")
5. **Equilibrium bubbles**: Gas pressure balanced by surface tension; no local stress variations on microstructure scale

## Key Equations

### Phase-Field Free Energy Functional (KKS formulation)

$$F = \int_V \left[ f_{chem}(c_v, \eta) + W g(\eta) + \frac{\kappa}{2}|\nabla \eta|^2 \right] dV$$

where $f_{chem}$ is the chemical free energy density, $\eta$ is the order parameter (0 = matrix, 1 = bubble), $W$ is the double-well barrier height, $\kappa$ is the gradient energy coefficient, and $g(\eta) = \eta^2(1-\eta)^2$.

### Parabolic Chemical Free Energies

$$f_{matrix} = \frac{1}{2}k_v^m(c_v - c_v^{eq})^2, \quad f_{bubble} = \frac{1}{2}k_v^b(c_v - 1)^2$$

with $k_v^m = 1.1 \times 10^{10}$ J/m³, $k_v^b = 1.5 \times 10^9$ J/m³.

### Interfacial Parameters (from $\gamma$ and interface width $l$)

$$\kappa = \frac{2\sqrt{2}\gamma l}{6} \approx 5.52 \times 10^{-12} \text{ J/m}, \quad W = \frac{6\gamma}{\sqrt{2}l} \approx 9.93 \times 10^8 \text{ J/m}^3$$

with interfacial energy $\gamma = 1.17$ J/m² and interface thickness $2l = 10$ nm.

### Source-Only (SO) Model — Steady-State Diffusion

$$D\nabla^2 c_v + s_v = 0$$

with boundary conditions: $c_v = c_\infty$ at domain boundary; Gibbs-Thomson at bubble surface.

### SO Growth Rate

$$\dot{R} = \frac{D \Omega}{R} \cdot \frac{c_\infty - c_R}{1 - R/R_{dom}}$$

Approximate form for small $R$:

$$\dot{R} \approx \frac{D \Omega s_v}{R} \cdot \frac{R_{dom}^2 - R^2}{6D}$$

where $R_{dom}$ is the domain radius, $D$ is vacancy diffusivity, $\Omega$ is atomic volume, and $s_v$ is the vacancy source term.

### Source+Sink (SS) Model

$$D\nabla^2 c_v - Z^2 c_v + s_v = 0$$

where $Z^2$ is the effective sink strength. Steady-state bulk vacancy concentration:

$$c_{\infty,SS} = \frac{s_v}{Z^2}$$

Solution using modified spherical Bessel functions:

$$c_v(r) = (c_\infty - s_v/Z^2) \cdot \frac{i_0(Zr)}{i_0(ZR)} \cdot \frac{R}{r} + \frac{s_v}{Z^2}$$

### Chemical Stress Model (Full Vacancy-Interstitial)

$$\dot{R} = \frac{\Omega}{R^2}(D_v c_{v\infty} - D_i c_{i\infty})$$

The "chemical stress" driving force:

$$S_v = \frac{D_v c_{v\infty} - D_i c_{i\infty}}{D_v}$$

Steady-state relation at far field:

$$D_v c_{v\infty} - D_i c_{i\infty} = \frac{D_v Z_v^2 c_{v\infty} - D_i Z_i^2 c_{i\infty}}{Z^2}$$

### Gibbs-Thomson Boundary Condition

$$c_R = c_v^{eq} \exp\left(\frac{2\gamma \Omega}{R k_B T}\right) \approx c_v^{eq}\left(1 + \frac{2\gamma \Omega}{R k_B T}\right)$$

where $c_R$ is the vacancy concentration at the bubble surface of radius $R$.

### Key Parameterization Strategy
- Frenkel pair production rate $\gg$ fission rate (several orders of magnitude)
- Net vacancy source: $s_v = \alpha \cdot \dot{Y}_{Xe}$, where $\alpha \in [1, 20]$ and $\dot{Y}_{Xe}$ is the Xe production rate
- SO approach provides more flexibility to match full vacancy-interstitial growth rates than SS approach

## Experimental Data
- No direct experimental data; comparison against analytical models
- Phase-field simulations of UO2 intergranular bubble growth compared to previously published results
- The strategy validated by matching SO growth rate to chemical stress model predictions

## Model Description
- **Three models compared**: (1) Source-Only (SO), (2) Source+Sink (SS), (3) Chemical Stress (full v-i)
- Analytical quasi-steady-state solutions derived for all three models
- Phase-field simulations using KKS formulation in MOOSE framework
- Comparison of growth rates and vacancy concentrations between models
- Strategy: fit SO source term to match chemical stress model growth rate

## Key Findings
1. **Source-Only approach has greater flexibility** to match growth rates from full vacancy-interstitial physics than Source+Sink
2. **SS model** forces steady-state vacancy concentration in bulk but constrains growth rate to specific functional form
3. **SO model** can be parameterized by fitting the source term sᵥ to match the chemical stress model growth rate
4. **Parameterization strategy**: Determine sᵥ by equating SO growth rate to chemical stress growth rate for a given bubble radius
5. The effective vacancy source is much less than Frenkel pair production rate due to recombination
6. Previously used range of 1-20× Xe production rate is physically reasonable
7. The approach was validated with 3D phase-field simulations of intergranular bubble growth in UO2

## Relevance to JSRT Model
- **Critical for JSRT parameterization**: Provides rigorous strategy for determining vacancy production rates in bubble growth models
- **Source term calibration**: The SO vs SS comparison helps choose the right approach for JSRT vacancy source terms
- **Chemical stress concept**: The vacancy supersaturation driving force is directly relevant to JSRT swelling rate calculations
- **Frenkel pair recombination**: Understanding net vacancy production vs. total Frenkel pair production is essential for accurate JSRT source terms
- **Multi-scale coupling**: The strategy of fitting mesoscale parameters to match full physics can be applied to JSRT model calibration
- **Range of vacancy production rates**: 1-20× Xe production rate provides bounds for JSRT parameter sensitivity studies

## Relationships

- [[wiki/entities/PhaseFieldModeling|PhaseFieldModeling]] — KKS phase-field model parameterization for vacancy production rate is the core subject
- [[wiki/entities/CavitationalVoid|CavitationalVoid]] — vacancy supersaturation driving force and bubble growth rate are directly relevant to void/cavity growth
- [[wiki/concepts/RateTheoryFramework|RateTheoryFramework]] — Source-Only vs. Source+Sink vs. Chemical Stress model comparison is a rate-theory analysis
- [[wiki/summaries/2009_Rokkam_PhaseFieldVoidNucleationGrowth|2009_Rokkam_PhaseFieldVoidNucleationGrowth]] — Rokkam's phase-field void model provides the methodological foundation
- [[wiki/summaries/2022_Aagesen_PFBubbleInterconnection|2022_Aagesen_PFBubbleInterconnection]] — companion phase-field bubble interconnection study from same author
- [[wiki/summaries/2020_Aagesen_BisonUPuZrSwellingLowerLengthScale|2020_Aagesen_BisonUPuZrSwellingLowerLengthScale]] — BISON model parameterization context for the same research program

## Related Work
- [[wiki/summaries/2022_Aagesen_PFBubbleInterconnection|2022_Aagesen_PFBubbleInterconnection]] — 同作者相场气泡互连研究，与本文组成完整的相场气泡演化参数化体系
- [[wiki/summaries/2025_Jiang_GasBubbleSuperlatticePhaseField|2025_Jiang_GasBubbleSuperlatticePhaseField]] — 相场GBS模拟直接使用本文讨论的空位源项参数化策略
- [[wiki/summaries/2025_Dabas_PhaseField_CavityGrowth|2025_Dabas_PhaseField_CavityGrowth]] — 相场空洞生长模拟，同样面临空位产生率参数化问题
- [[wiki/summaries/2011_Millett_PhaseFieldGasBubbleKinetics|2011_Millett_PhaseFieldGasBubbleKinetics]] — 早期相场气泡动力学模型，本文的方法论先驱
- [[wiki/summaries/2024_Muntaha_GB_SurfaceDiffusion|2024_Muntaha_GB_SurfaceDiffusion]] — 同期相场工作，处理晶界/表面扩散对气泡行为的影响
- [[wiki/concepts/RateTheoryFramework|RateTheoryFramework]] — Source-Only/Source+Sink/Chemical Stress模型的对比分析本质上属于速率理论范畴
