# Summary: 2021_Hirschhorn_CALPHAD_BISON_Redistribution

**Title:** A CALPHAD-informed approach to modeling constituent redistribution in Zr-based metallic fuels using BISON

**Authors:** Jacob Hirschhorn, Michael Tonks, Christopher Matthews

**Journal:** Journal of Nuclear Materials 544 (2021) 152657

**DOI:** 10.1016/j.jnucmat.2020.152657

---

## English Summary (200-400 words)

This paper develops a CALPHAD-informed mechanistic model for constituent redistribution in U-Zr and U-Pu-Zr metallic nuclear fuels, implemented in the BISON fuel performance code. The model replaces the computationally expensive phase-field approach from the authors' earlier work with an efficient lookup table system using pycalphad to pre-calculate equilibrium thermodynamic properties (chemical potentials, equilibrium atom fractions, phase atom fractions). Constituent redistribution is modeled via a modified Cahn-Hilliard equation for Zr atom fraction evolution, driven by chemical potential gradients (Fickian diffusion) and temperature gradients (Soret/thermotransport). Five phases are considered: α (orthorhombic), β (tetragonal), γ (BCC), δ (hexagonal), and ζ (rhombohedral). The γ phase uses DICTRA-assessed atomic mobilities, while other phases use interdiffusion coefficients with Arrhenius temperature dependence. The model was calibrated using EPMA data from two U-10Zr fuel elements (DP-81 at 3.6 at% burnup, DP-11 at 7.7 at%) irradiated in EBR-II. Only three calibrated scalar multipliers (on β interdiffusion, γ chemical mobility, and γ thermal mobility) were needed, ranging from 0.56 to 4.50. The calibrated model accurately predicts the characteristic "Zr bathtub" profile and Zr-enriched central region in both U-Zr elements. For U-Pu-Zr fuels (T-179 and DP-16), predictions were physically reasonable but less accurate, attributed to uncertainties in ternary phase transition temperatures, lack of ζ phase kinetic data, and temperature prediction uncertainties. A 2D axisymmetric full-element simulation of DP-81 demonstrated successful coupling with BISON's thermomechanics models. The new approach achieves ~10x computational speedup over the previous phase-field model (35 seconds vs tens of minutes) while enabling five-phase ternary fuel simulations.

## 中文摘要

本文开发了一种基于CALPHAD方法的力学模型，用于模拟U-Zr和U-Pu-Zr金属核燃料中的组元再分布行为，并集成到BISON燃料性能分析代码中。模型采用pycalphad预计算平衡热力学性质（化学势、平衡原子分数、相原子分数），以查找表替代先前工作中计算代价高昂的相场方法，大幅降低了计算成本。组元再分布通过修正的Cahn-Hilliard方程描述锆原子分数的演化，驱动力包括化学势梯度（菲克扩散）和温度梯度（索雷特效应/热迁移）。模型考虑五个相：α（正交）、β（四方）、γ（体心立方）、δ（六方）和ζ（菱形）。γ相采用DICTRA评估的原子迁移率，其余相使用Arrhenius型互扩散系数。利用EBR-II辐照的两个U-10Zr燃料元件（DP-81，燃耗3.6 at%；DP-11，燃耗7.7 at%）的EPMA数据进行了模型标定，仅需三个标定参数（标定系数0.56~4.50），即可准确预测U-Zr燃料中典型的"锆浴盆"分布和中心富锆区。对U-Pu-Zr燃料（T-179和DP-16）的预测在物理上合理但精度较低，主要归因于三元相转变温度的不确定性、ζ相动力学数据缺失以及温度预测误差。2D轴对称全燃料元件模拟验证了模型与BISON热力学模型的耦合能力。新方法相比先前相场模型实现了约10倍的计算加速（35秒 vs 数十分钟），同时支持五相三元燃料模拟。

---

## Key Contributions

1. Efficient CALPHAD-informed constituent redistribution model using lookup tables
2. Calibrated against EBR-II U-Zr fuel data with only three parameters
3. Extended to five-phase U-Pu-Zr ternary system
4. Integrated into BISON with full 2D thermomechanics coupling demonstration
5. ~10x computational speedup over previous phase-field approach

## Fuel Compositions Studied

- U-10Zr wt% (~U-22Zr at%)
- U-19Pu-10Zr wt% (~U-16Pu-22Zr at%)

## Experimental Data Sources

- EBR-II irradiated fuel elements: DP-81 (3.6 at%), DP-11 (7.7 at%), T-179 (1.9 at%), DP-16 (10.0 at%)
- EPMA radial composition profiles

## Related Work
- [[wiki/concepts/ConstituentRedistribution|ConstituentRedistribution]] — 本文核心主题：金属燃料组元再分布
- [[wiki/summaries/2021_Poschmann_MassTransport_Interdiffusion|2021_Poschmann_MassTransport_Interdiffusion]] — 化学势梯度驱动的U-Zr互扩散模型，与本文CALPHAD查找表方法形成方法论对比
- [[wiki/summaries/2021_Geiger_TAFID_FCCI_U5FS_U10Zr|2021_Geiger_TAFID_FCCI_U5FS_U10Zr]] — 同为CALPHAD方法在金属燃料中的应用，FCCI热力学预测
- [[wiki/summaries/1996_Hofman_TemperatureGradientRedistribution_UZr|1996_Hofman_TemperatureGradientRedistribution_UZr]] — Hofman经典U-Zr温度梯度再分布实验，本文模型标定数据来源
- [[wiki/summaries/2021_Paaren_AutomatedFuelPerformance_BISON_EBR2|2021_Paaren_AutomatedFuelPerformance_BISON_EBR2]] — BISON金属燃料自动化建模，本文模型集成于BISON
- [[wiki/summaries/2020_Hirschhorn_UZr_DiffusionCouple_PF|2020_Hirschhorn_UZr_DiffusionCouple_PF]] — 同作者前期相场方法，本文用查找表替代以提高效率
