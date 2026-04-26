# Summary: 2025_Hirschhorn_MechanisticMultiscale_FCCI_BISON

**Title:** Development and preliminary validation of a mechanistic multiscale model for fuel-cladding chemical interaction in metallic nuclear fuels

**Authors:** J.A. Hirschhorn, L.K. Aagesen, C. Jiang, G.L. Beausoleil II (Idaho National Laboratory)

**Journal:** Nuclear Engineering and Design 432 (2025) 113811

**DOI:** 10.1016/j.nucengdes.2024.113811

---

## English Summary

This paper presents a mechanistic multiscale model for cladding-side fuel-cladding chemical interaction (FCCI) in metallic nuclear fuels (U-Zr and U-Pu-Zr), implemented in the BISON fuel performance code. FCCI—where lanthanide (Ln) fission products diffuse through the fuel and react with the cladding to form brittle intermetallic wastage layers—remains the primary lifetime-limiting behavior for metallic fuel rods.

The model spans three scales. At the **atomistic scale**, VASP calculations provided Nd diffusivities in α-U (bulk and surface), Fe, and Cr, including radiation-enhanced diffusion effects. At the **mesoscale**, MARMOT simulations using asymptotic expansion homogenization (AEH) and phase-field methods addressed two key problems: (1) effective Ln diffusivity through fuel with evolving porosity (isolated pores → interconnected pores → sodium-infiltrated pores), captured by a composite analytical expression combining the Maxwell-Eucken model with a bicontinuous microstructure model; and (2) intermetallic wastage layer growth kinetics using a grand-potential phase-field model for the Fe₁₇Nd₂ system. At the **engineering scale**, the mesoscale-informed effective diffusivity and an Arrhenius-based Ln flux boundary condition were coupled with BISON's thermomechanics framework through MOOSE MultiApps.

Model parameters were optimized using EBR-II X447 fuel rod DP75 data, yielding M₀ = 5.5×10⁶ m/s and Eₐ = 3 eV for the reaction flux. Validation against five fuel rods (EBR-II X447 and FFTF IFR1) showed the model predicts axial wastage profiles and cladding dilation as well as existing empirical correlations. The model captures the ~1% FIMA incubation period before rapid wastage growth and correctly predicts FFTF's midplane-biased wastage versus EBR-II's top-biased behavior. Future work will refine Ln production/decay terms, expand validation, and develop separate-effects models for fuel cracking and Zr rind breakthrough.

## 中文摘要

本文提出了一种用于金属核燃料（U-Zr 和 U-Pu-Zr）包壳侧燃料-包壳化学相互作用（FCCI）的力学多尺度模型，并在 BISON 燃料性能代码中实现。FCCI 是指镧系裂变产物穿过燃料扩散并与包壳反应形成脆性金属间化合物损耗层的过程，仍是限制金属燃料棒寿命的主要因素。

该模型跨越三个尺度。在**原子尺度**，通过 VASP 计算获得了 Nd 在 α-U（体相和表面）、Fe 和 Cr 中的扩散系数，包括辐照增强扩散效应。在**介观尺度**，使用 MARMOT 的渐近展开均匀化（AEH）方法和相场方法解决了两个关键问题：（1）燃料孔隙演化过程中的有效 Ln 扩散系数（孤立孔→连通孔→钠浸润孔），由 Maxwell-Eucken 模型与双连续微观结构模型的复合解析表达式描述；（2）基于巨势相场模型的 Fe₁₇Nd₂ 金属间化合物损耗层生长动力学。在**工程尺度**，通过 MOOSE MultiApps 将介观尺度获得的有效扩散系数和 Arrhenius 型 Ln 通量边界条件与 BISON 热力学框架耦合。

利用 EBR-II X447 燃料棒 DP75 数据优化模型参数，得到反应通量参数 M₀ = 5.5×10⁶ m/s 和 Eₐ = 3 eV。对五根燃料棒（EBR-II X447 和 FFTF IFR1）的验证表明，该模型预测的轴向损耗分布和包壳胀大与现有经验关联式相当。模型成功捕获了约 1% FIMA 孵化期后快速损耗增长的行为，并正确预测了 FFTF 中偏燃料中平面的损耗分布与 EBR-II 中偏顶部的差异。

---

**Keywords:** BISON, MARMOT, FCCI, multiscale modeling, lanthanide diffusion, phase-field, metallic fuel, wastage layer, U-Zr, U-Pu-Zr

## Related Work
- [[wiki/entities/BISONCode|BISONCode]] — 本文在BISON燃料性能代码中实现多尺度FCCI模型
- [[wiki/concepts/FuelCladdingChemicalInteraction|FuelCladdingChemicalInteraction]] — FCCI是本文的核心物理现象
- [[wiki/summaries/2016_Hales_BISON_TheoryManual|2016_Hales_BISON_TheoryManual]] — BISON理论手册
- [[wiki/summaries/2021_Geiger_TAFID_FCCI_U5FS_U10Zr|2021_Geiger_TAFID_FCCI_U5FS_U10Zr]] — U-Zr燃料的FCCI实验研究
- [[wiki/summaries/2017_Matthews_FCCI_CriticalReview_UPuZr|2017_Matthews_FCCI_CriticalReview_UPuZr]] — U-Pu-Zr燃料FCCI的临界综述
- [[wiki/entities/UPuZrFuel|UPuZrFuel]] — U-Zr和U-Pu-Zr金属燃料的FCCI行为
