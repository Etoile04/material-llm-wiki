# Prudil 2015 - FAST燃料性能程序开发与测试：瞬态条件（第二部分）

**文献**: A. Prudil, B.J. Lewis, P.K. Chan, J.J. Baschuk, D. Wowk, "Development and testing of the FAST fuel performance code: Transient conditions (Part 2)", Nuclear Engineering and Design 282 (2015) 169–177.

## 摘要

本文介绍了燃料与包壳建模工具(FAST)的瞬态条件扩展及验证。FAST是基于COMSOL Multiphysics的多物理场、多维燃料性能分析程序，是首个统一的CANDU燃料分析程序，可同时处理稳态运行条件(NOC)和高温瞬态(事故)条件。

扩展内容包括：(1)高温包壳蠕变模型(NIRVANA模型)——涵盖晶界滑移蠕变、位错蠕变和相变蠕变三种机制，温度范围700-1600 K；(2)包壳氧化模型——基于Urbanic-Heidrick的抛物线生长模型，涵盖氧化层和α稳定相层的生长；(3)多芯块几何模型——支持任意数量芯块的2D轴对称几何，实现了全元件建模能力。

高温蠕变模型中，等效应力采用Hill各向异性准则(F_Hill=0.773, G_Hill=0.532, H_Hill=0.195)。晶界滑移蠕变速率与σ²eqv成正比，激活温度9431/T K⁻¹。位错蠕变通过内应力演化方程描述，初始内应力53.4 MPa。相变蠕变仅在α→β相变时发生(>1100 K)。再结晶通过无位错体积分数df的演化方程描述。

氧化模型中，氧化层生长速率在T≤1853 K和T>1853 K两个温区采用不同参数，氧化反应放热586 kJ/mol，氧化导致56%体积增加。氧化层的热阻通过附加薄层模型处理。

验证采用FIO-131实验（模拟失水事故的辐照实验），比较了单芯块和全25芯块模型与ELESTRES/ELOCA程序及实验数据的一致性。全元件模型展示了改进的包壳变形预测，包括环脊效应。FAST是首个统一处理CANDU燃料NOC和瞬态条件的程序，采用隐式后向差分公式(BDF)实现时间步长自适应。

## Related Work
- [[wiki/concepts/FuelPerformanceCodes|FuelPerformanceCodes]] — FAST是燃料性能代码之一
- [[wiki/summaries/VanUffelen_2019_FuelPerformanceReview|VanUffelen_2019_FuelPerformanceReview]] — 燃料性能建模综述，涵盖多种代码
- [[wiki/summaries/Hales_2016_BISON_TheoryManual|Hales_2016_BISON_TheoryManual]] — BISON理论手册，与FAST同为燃料性能代码
- [[wiki/summaries/2025_Pizzocri_MultiFidelity_FuelPerformance|2025_Pizzocri_MultiFidelity_FuelPerformance]] — 多保真度燃料性能建模，与FAST代码理念相关
