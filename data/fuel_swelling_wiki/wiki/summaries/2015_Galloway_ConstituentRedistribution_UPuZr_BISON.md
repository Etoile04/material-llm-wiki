# Modeling Constituent Redistribution in U–Pu–Zr Metallic Fuel Using BISON

**Authors**: J. Galloway, C. Unal, N. Carlson, D. Porter, S. Hayes
**Year**: 2015 | **Journal**: Nuclear Engineering and Design 286, 1–17
**Slug**: 2015_Galloway_ConstituentRedistribution_UPuZr_BISON

## English Summary

This paper presents an improved formulation for modeling constituent (zirconium) redistribution in U–Pu–Zr metallic nuclear fuels, implemented in the BISON fuel performance code built on the MOOSE framework. The model addresses several deficiencies in prior work by Kim et al. (2004, 2006) and Karahan & Buongiorno (2009): (1) it corrects inconsistencies between enthalpies of solution and solubility limit curves of the simplified pseudo-binary phase diagram, (2) introduces a modified Soret term ensuring Zr flux vanishes at both concentration limits, and (3) adds artificial diffusion in two-phase regions to stabilize the Galerkin finite element method.

The coupled thermal-diffusion equations are solved simultaneously—unlike previous approaches that imposed artificial temperature profiles. Validation uses EBR-II data from fuel pins T179 (2 at%, 92 days), DP16 (10 at%, 485 days), and T459 (3 at%, 142 days). An iterative calibration between T179 and DP16 yields optimized phase-dependent diffusion coefficients (with multipliers: α×15, δ×1, β×2, γ×7 relative to Kim et al. baseline) and elevated phase transition temperatures (692°C and 722°C versus fresh-fuel values of 595°C and 650°C). A new thermal conductivity model covering 0–100% Zr concentration and an MCNP-derived power redistribution function are also developed.

Key findings: the gamma phase diffusion coefficient is the most influential and uncertain parameter, followed by alpha and beta phases. The significantly higher transition temperatures (~100°C above fresh-fuel values) suggest irradiated fuel may have fundamentally different phase behavior. The model shows strong agreement with T179 and DP16 EMP data and reasonable qualitative agreement with T459 radiographs.

## 中文摘要

本文提出了一种改进的U-Pu-Zr金属核燃料组元（锆）再分布模型，并在基于MOOSE框架的BISON燃料性能代码中实现。该模型修正了先前Kim等人和Karahan & Buongiorno工作中的多个缺陷：(1) 修正了溶解焓与相图溶解度曲线之间的不一致性，(2) 引入修正的Soret项确保Zr通量在浓度上下限时趋零，(3) 在两相区添加人工扩散以稳定Galerkin有限元方法。

模型同时求解耦合的热-扩散方程，而非采用先前工作中的人工温度剖面。验证使用EBR-II燃料棒T179（2 at%，92天）、DP16（10 at%，485天）和T459（3 at%，142天）数据。通过T179与DP16之间的迭代校准，获得了优化的相依赖扩散系数（乘数：α×15, δ×1, β×2, γ×7）和升高的相变温度（692°C和722°C，高于新鲜燃料的595°C和650°C）。还开发了覆盖0-100%Zr浓度的新热导率模型和基于MCNP的功率再分布函数。

关键发现：γ相扩散系数最具影响力且不确定性最大，其次是α相和β相。显著偏高的相变温度（比新鲜燃料高约100°C）表明辐照燃料可能具有根本不同的相行为。

## Related Work
- [[wiki/concepts/ConstituentRedistribution|ConstituentRedistribution]] — 本文核心主题，U-Pu-Zr燃料中Zr组元再分布建模
- [[wiki/concepts/SoretEffectInMetallicFuels|SoretEffectInMetallicFuels]] — 本文引入修正Soret项确保Zr通量在浓度边界处趋零
- [[wiki/entities/BISONCode|BISONCode]] — 本文在BISON代码中实现组元再分布模型
- [[wiki/entities/EBR-II|EBR-II]] — 使用EBR-II燃料棒T179、DP16、T459数据验证模型
- [[wiki/summaries/2004_Kim_ConstituentRedistribution_UPuZr|2004_Kim_ConstituentRedistribution_UPuZr]] — 本文修正了Kim等人再分布模型的多个缺陷
- [[wiki/summaries/1996_Hofman_TemperatureGradientRedistribution_UZr|1996_Hofman_TemperatureGradientRedistribution_UZr]] — 提供Zr再分布的实验基准数据
