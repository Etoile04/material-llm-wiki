# Fission Gas Release and Swelling Model of Metallic Fast Reactor Fuel (GRSIS)

## Metadata
- **Title**: Fission gas release and swelling model of metallic fast reactor fuel
- **Authors**: Chan Bock Lee, Dae Ho Kim, Youn Ho Jung
- **Year**: 2001
- **Journal**: Journal of Nuclear Materials, Vol. 288, pp. 29–42
- **Affiliation**: Korea Atomic Energy Research Institute (KAERI)
- **Key context**: KALIMER fast reactor fuel development; mechanistic GRSIS model for U-Pu-Zr metallic fuel

## Summary

**English (200–400 words)**

Lee, Kim, and Jung developed the GRSIS (Gas Release and Swelling in ISotropic fuel matrix) model — a mechanistic fission gas release and swelling model for U-Pu-Zr metallic fuel in fast reactors. Unlike UO₂ fuel models (e.g., STARS, ALFUS) which assume grain-boundary-dominated bubble nucleation, GRSIS assumes **isotropic nucleation** of fission gas bubbles throughout the fuel matrix, justified by the random distribution of phase boundaries within grains in metallic fuel. This eliminates the grain-size dependence characteristic of ceramic fuel models.

The model classifies closed bubbles into three size classes: bubble-1 (nucleation, r₁ = 0.5 μm), bubble-2 (intermediate, r₂ = 2.5 μm), and bubble-3 (largest closed, r₃ = 12.5 μm). Bubbles grow by gas atom diffusion and coalescence. A fourth class (bubble-4) represents open bubbles connected to external free space. Rate equations track gas atom concentrations and bubble populations, incorporating gas diffusion to bubbles, bubble diffusion, collision/coalescence, and transition between bubble classes.

A key feature is the **threshold swelling mechanism** based on percolation theory. When closed bubble swelling reaches a critical value (Sth ≈ 0.2, from SC lattice percolation with Pc = 0.32), a fraction (fth ≈ 0.3) of bubbles instantaneously interconnect to form open channels, releasing their gas. The model also accounts for fuel-cladding contact: after gap closure, external pressure suppresses closed bubble swelling while open bubbles may collapse, until the porous fuel yields and deforms axially.

The model uses Adda's correlation for gas atom diffusion (Dg₀ = 9.5×10⁻⁸ m²/s, Qg = 32,000 cal/mol) and surface diffusion (Ds₀ = 9.5×10⁻⁵ m²/s, Qs = 32,000 cal/mol). Parametric studies show FGR is sensitive to gas diffusivity and bubble size classification, but insensitive to bubble nucleation rate and fission density. GRSIS predictions agree reasonably with ANL irradiation data for U-10Zr, U-8Pu-10Zr, and U-19Pu-10Zr fuels at 550°C, though it does not address anisotropic cavitational void swelling at low temperatures.

**中文摘要**

Lee、Kim和Jung开发了GRSIS（各向同性基体中气体释放与肿胀）模型，用于快堆U-Pu-Zr金属燃料的裂变气体释放和肿胀预测。与UO₂燃料模型不同，GRSIS假设裂变气泡在燃料基体中**各向同性形核**，因为金属燃料中相界在晶粒内随机分布，消除了晶粒尺寸依赖性。

模型将闭合气泡分为三类：气泡-1（形核，r₁=0.5μm）、气泡-2（中间，r₂=2.5μm）和气泡-3（最大闭合气泡，r₃=12.5μm）。气泡通过气体原子扩散和合并生长。第四类（气泡-4）为开放气泡，与外部自由空间连通。模型建立速率方程跟踪气体原子浓度和气泡种群变化。

核心特征是基于**渗透理论的阈值肿胀机制**。当闭合气泡肿胀达到临界值（Sth≈0.2）时，部分气泡瞬间互连形成开放通道并释放气体。模型还考虑了燃料-包壳接触效应：间隙闭合后，外部压力抑制闭合气泡肿胀，开放气泡可能坍塌。

参数研究表明，裂变气体释放对气体扩散系数和气泡尺寸分类敏感，但对气泡形核率和裂变密度不敏感。GRSIS预测与ANL辐照数据基本吻合，但未考虑低温下各向异性空腔肿胀。

## Key Equations

### Gas Atom Balance
$$\frac{dC_g}{dt} = YF - (J_{g1} + J_{g2} + J_{g3} + J_{g4}) - J_{b1}^{nucl}$$

### Gas Diffusion to Bubble-i
$$J_{gi} = k_{gi} \cdot C_g \cdot N_{bi}, \quad k_{gi} = E_{gbi} \cdot 4\pi r_{bi} \cdot D_g$$

### Bubble Diffusion Coefficient
$$D_{bi} = \frac{3a_0^2}{2\pi r_{bi}^4} D_s$$

### Surface Diffusion
$$D_s = D_{s0} \exp(-Q_s/kT)$$

### Bubble Swelling
$$S_b = \frac{4}{3}\pi r_{bj}^3 N_{bj}$$

### Threshold Swelling (Percolation)
$$\frac{\Delta V}{V_{SC}} = \frac{V_{SC}}{1 - V_{SC}} = 0.2, \quad P_c = 0.32$$

### Fission Gas Release
$$FGR = \begin{cases} 0 & S_t < S_{th} \\ f_{th}(C_{gb1} + C_{gb2} + C_{gb3}) & S_t = S_{th} \\ C_{gb4} & S_t > S_{th} \end{cases}$$

### Total Swelling
$$S_t = S_c + S_o = V_1 + V_2 + V_3 + V_4$$

## Key Findings

1. **Isotropic nucleation assumption** is valid for metallic fuel due to random phase boundary distribution
2. **Three-class bubble model** (r₁=0.5, r₂=2.5, r₃=12.5 μm) provides best fit to ANL data
3. **Threshold swelling Sth=0.2** triggers instantaneous gas release via percolation-based bubble interconnection
4. FGR sensitive to gas diffusivity and bubble classification; insensitive to nucleation rate and fission density
5. Temperature dependence significant only below ~450°C due to low diffusion coefficients
6. Fuel-cladding contact mechanism: external pressure suppresses closed bubbles, open bubbles collapse at yield stress
7. Model validated against U-10Zr, U-8Pu-10Zr, U-19Pu-10Zr ANL irradiation data
8. Does not model anisotropic cavitational void swelling at low temperatures (acknowledged limitation)

## Relationships

- [[wiki/summaries/1990_Hofman_SwellingBehaviorUPuZr|1990_Hofman_SwellingBehaviorUPuZr]] — provides microstructural basis and bubble size data used in GRSIS
- [[wiki/summaries/1993_Rest_VoidSwellingAlphaU|1993_Rest_VoidSwellingAlphaU]] — cavitational void swelling at low temperature, not modeled in GRSIS
- [[wiki/entities/FissionGasDiffusion|FissionGasDiffusion]] — GRSIS provides mechanistic framework for gas diffusion and bubble behavior in metallic fuel

## Related Work
- [[wiki/summaries/1990_Hofman_SwellingBehaviorUPuZr|1990_Hofman_SwellingBehaviorUPuZr]] — Hofman 的微观结构观察为 GRSIS 提供了气泡尺寸数据和物理基础
- [[wiki/summaries/1993_Rest_VoidSwellingAlphaU|1993_Rest_VoidSwellingAlphaU]] — Rest 的空腔肿胀模型处理了 GRSIS 未涵盖的低温 α-U 相各向异性肿胀
- [[wiki/summaries/2013_Karahan_FEAST_ExtendedSwelling_UPuZr|2013_Karahan_FEAST_ExtendedSwelling_UPuZr]] — FEAST-METAL 代码直接采用 GRSIS 算法作为裂变气体行为模块
- [[wiki/concepts/SwellingModelComparison|SwellingModelComparison]] — GRSIS 与 Rest 空腔模型代表了两种竞争的金属燃料肿胀理论
- [[wiki/entities/FissionGasDiffusion|FissionGasDiffusion]] — 气体扩散系数是 GRSIS 最敏感的模型参数
