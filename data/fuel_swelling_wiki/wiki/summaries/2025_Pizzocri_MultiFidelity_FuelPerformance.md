# A Multi-Fidelity Multi-Scale Methodology to Accelerate Development of Fuel Performance Codes

**论文**: Pizzocri et al. (2025), *Nuclear Engineering and Design* 432, 113741
**DOI**: https://doi.org/10.1016/j.nucengdes.2024.113741
**关键词**: 多尺度、多保真度、机器学习、燃料性能、裂变气体行为

## 摘要

本文提出了一种多保真度多尺度方法论，用于解决介观尺度模块（SCIANTIX）与工程尺度燃料性能程序（FRAPCON）耦合时输入变量缺失的问题。具体而言，SCIANTIX所需的局部静水应力（hydrostatic stress）在FRAPCON标准模型中无法计算。该方法论利用另一个燃料性能程序TRANSURANUS离线生成虚拟静水应力数据集，训练人工神经网络（ANN）作为代理模型嵌入FRAPCON/SCIANTIX系统。

ANN为前馈网络，含单层10个神经元、6个输入（归一化径向位置、燃耗、接触压力、间隙压力、燃料中心温度、燃料表面温度）和1个输出（局部静水应力）。训练采用Levenberg-Marquardt算法，70%数据用于训练，15%验证，15%测试。

该方法应用于Risø AN3辐照实验模拟，结果表明FRAPCON/SCIANTIX-ANN在裂变气体释放预测上相比标准FRAPCON有显著改善，能够描述功率瞬态期间的晶界微裂纹效应。

## Key Equations

### 晶界气泡空位流入速率
$$\frac{dn_v}{dt} \sim \left(p - \frac{2\gamma}{R} + \sigma_h\right)$$

- $dn_v/dt$：空位流入速率（vacancies·m⁻³·s⁻¹）
- $p$：晶界气泡内压（Pa）
- $\gamma$：表面张力（N·m⁻¹）
- $R$：气泡投影半径（m）
- $\sigma_h$：静水应力（Pa），压缩（负值）时抑制气泡生长

**物理意义**: 静水应力直接影响晶界气泡的过压状态，从而控制空位流入和气泡生长速率。压缩应力减小空位流入，延缓气泡生长和裂变气体释放。

## Related Work
- [[wiki/concepts/FuelPerformanceCodes|FuelPerformanceCodes]] — 多保真度燃料性能建模方法论
- [[wiki/entities/BISONCode|BISONCode]] — BISON是本文讨论的工程尺度燃料性能代码
- [[wiki/summaries/2016_Hales_BISON_TheoryManual|2016_Hales_BISON_TheoryManual]] — BISON理论手册
- [[wiki/summaries/2019_VanUffelen_FuelPerformanceReview|2019_VanUffelen_FuelPerformanceReview]] — 燃料性能建模综述
- [[wiki/concepts/FissionGasReleaseModels|FissionGasReleaseModels]] — 多保真度裂变气体释放建模
- [[wiki/summaries/2023_Ke_MicrostructureModeling|2023_Ke_MicrostructureModeling]] — 微观结构建模与燃料性能代码集成
