# Van Uffelen et al. (2019) - 燃料性能建模综述

**论文**: A review of fuel performance modelling  
**期刊**: Journal of Nuclear Materials 516 (2019) 373–412  
**作者**: P. Van Uffelen, J. Hales, W. Li, G. Rossiter, R. Williamson

## 摘要

本文系统综述了轻水堆（LWR）核燃料棒性能模拟代码的发展历程与现状。文章首先回顾了燃料性能建模各主要方面的历史进展，包括热工性能（热导率、间隙导热）、力学性能（燃料开裂、大应变处理、高燃耗结构力学特性）、化学性能（包壳氧化、裂变产物化学）、中子学建模（径向功率分布计算）以及微观结构变化（晶粒长大、孔隙率演化、高燃耗结构建模）。

在热工性能方面，文章详述了UO₂和MOX燃料热导率的声子传导模型 $k_{ph} = 1/(A+BT)$ 及其随燃耗、Gd掺杂、化学计量偏离的退化规律。间隙导热模型涵盖辐射、气体传导和接触传导三个并联分量。力学方面讨论了工程应变、真应变和Lagrangian应变在大变形分析中的适用性，以及1.5D到3D代码的发展趋势。

当前趋势部分涵盖新型燃料应用（MOX、掺杂燃料、事故容错燃料）、先进建模技术（多尺度模拟、相场方法、近场动力学、离散元方法）、多物理场耦合以及不确定性与敏感性分析。文章最后讨论了代码验证与验证策略，包括国际基准测试项目（FUMEX系列）的作用。

本文是一篇综述性论文，汇总了全球主要燃料性能代码（FRAPCON、TRANSURANUS、BISON、ALCYONE、FEMAXI等）的模型特点与验证情况，为燃料性能模拟领域提供了全面的技术参考。

## 关键参数

- UO₂热导率声子散射参数A、B
- 间隙导热模型各分量
- 燃料密度化与肿胀速率（~0.7–1%/MWd/kgHM）
- HBS形成阈值温度和燃耗
- 晶粒长大动力学参数
- 裂变气体扩散系数

## Related Work
- [[wiki/concepts/FuelPerformanceCodes|FuelPerformanceCodes]] — 本文是燃料性能代码的全面综述
- [[wiki/entities/BISONCode|BISONCode]] — 综述涵盖BISON代码的模型特点与验证
- [[wiki/summaries/Hales_2016_BISON_TheoryManual|Hales_2016_BISON_TheoryManual]] — BISON理论手册，与综述中讨论的BISON模型直接相关
- [[wiki/summaries/Piro_2021_ThermodynamicFuelCodes|Piro_2021_ThermodynamicFuelCodes]] — 热力学与燃料代码耦合综述
- [[wiki/summaries/OECD_NEA_2015_MultiscaleModelling|OECD_NEA_2015_MultiscaleModelling]] — 多尺度模拟技术报告，与本文互补
