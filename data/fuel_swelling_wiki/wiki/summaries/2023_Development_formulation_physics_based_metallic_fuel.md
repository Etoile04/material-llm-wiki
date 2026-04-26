# Summary: Development and Formulation of Physics Based Metallic Fuel Models (Matthews et al. 2023)

## English

Matthews et al. (2023) present a comprehensive baseline metallic fuel modeling capability implemented in the BISON fuel performance code for U-xPu-yZr fuels. The work establishes semi-empirical/semi-mechanistic models for thermal conductivity, Young's modulus, thermal expansion, fission gas swelling/release, hot-pressing, zirconium redistribution, and cladding creep, validated against the EBR-II X441/X441A experimental assembly (61 pins, ~10% FIMA target burnup).

Key model contributions include: (1) A new thermal conductivity correlation spanning 0–50 wt.% Zr and 0–20 wt.% Pu with <1.3 W/m/K standard deviation; (2) A fission gas swelling model based on Olander's rapid-diffusion assumption with calibrated bubble number density (N=10¹⁵ m⁻³), surface tension (γ=1.6 J/m²), and retained gas fractions (ζ₀=0.25, ζI=0.50); (3) Porosity interconnection modeled via a smoother-step function (f_start=0.23, f_end=0.25); (4) Hot-pressing from McDeavitt & Solomon with D_b·δ_b=4×10⁻²⁹ m³/s; (5) An anisotropic swelling factor (a=0.45) calibrated to X441 axial growth; (6) Zirconium redistribution using Galloway's Fickian+Soret model with phase-dependent diffusivities. Cladding models for HT9 and D9 (thermal/irradiation creep, void swelling) are also provided. The simulations reproduce general trends in cladding strain, FGR, and axial fuel growth, with identified gaps motivating future mechanistic model development (phase-dependent properties, stress-coupled swelling, FCCI, low-temperature swelling).

## 中文

Matthews 等人（2023）在 BISON 燃料性能代码中建立了 U-xPu-yZr 合金燃料的基线建模能力。该工作建立了涵盖热导率、杨氏模量、热膨胀、裂变气体肿胀/释放、热压致密化、锆重分布和包壳蠕变的半经验/半力学模型，并以 EBR-II X441/X441A 实验组件（61根棒，目标燃耗约 10% FIMA）进行了验证。

主要模型贡献包括：（1）覆盖 0–50 wt.% Zr 和 0–20 wt.% Pu 的新热导率关联式，标准偏差 <1.3 W/m/K；（2）基于 Olander 快速扩散假设的裂变气体肿胀模型，标定气泡数密度 N=10¹⁵ m⁻³、表面张力 γ=1.6 J/m²、截留气体份额 ζ₀=0.25 和 ζI=0.50；（3）通过 smoother-step 函数（f_start=0.23, f_end=0.25）建模孔隙率连通；（4）采用 McDeavitt & Solomon 热压模型，D_b·δ_b=4×10⁻²⁹ m³/s；（5）各向异性肿胀因子 a=0.45 标定至 X441 轴向生长；（6）使用 Galloway 的 Fickian+Soret 模型处理锆重分布，含相依赖扩散系数。同时提供了 HT9 和 D9 包壳的热/辐照蠕变及空洞肿胀模型。模拟结果再现了包壳应变、裂变气体释放和燃料轴向生长的一般趋势，并指出未来需发展力学耦合肿胀、FCCI、低温肿胀等机理模型。

## Metadata
- **Authors**: Christopher Matthews, Stephen Novascone, Al Casagranda, Larry Aagesen, Cetin Unal, David Andersson
- **Journal**: Journal of Nuclear Materials 578 (2023) 154343
- **DOI**: 10.1016/j.jnucmat.2023.154343
- **Institutions**: LANL, INL, TerraPower
- **Code**: BISON/MOOSE (NEAMS program)
- **Validation**: EBR-II X441/X441A (61 pins, U-19Pu-10Zr, HT9/D9 cladding)

## Related Work
- [[wiki/summaries/2021_Paaren_AutomatedFuelPerformance_BISON_EBR2|2021_Paaren_AutomatedFuelPerformance_BISON_EBR2]] — BISON EBR-II自动化验证，本文模型的验证基础
- [[wiki/summaries/2016_Hales_BISON_TheoryManual|2016_Hales_BISON_TheoryManual]] — BISON理论手册，本文金属燃料模型的理论框架
- [[wiki/concepts/FuelPerformanceCodes|FuelPerformanceCodes]] — 本文核心工具BISON所属类别
- [[wiki/summaries/1990_Hofman_SwellingBehaviorUPuZr|1990_Hofman_SwellingBehaviorUPuZr]] — EBR-II U-Pu-Zr肿胀实验数据，本文模型验证基准
- [[wiki/summaries/2013_Karahan_FEAST_ExtendedSwelling_UPuZr|2013_Karahan_FEAST_ExtendedSwelling_UPuZr]] — FEAST-METAL肿胀模型，本文BISON模型的对比参考
- [[wiki/summaries/2022_Qian_U10Zr_CavitationalVoidSwelling|2022_Qian_U10Zr_CavitationalVoidSwelling]] — 低温肿胀机制研究，本文指出需发展的方向
