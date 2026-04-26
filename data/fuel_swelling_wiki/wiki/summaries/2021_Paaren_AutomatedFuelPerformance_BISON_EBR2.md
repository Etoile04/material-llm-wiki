# BISON 自动化燃料性能建模 — EBR-II 金属燃料初步验证

## 元数据

| 字段 | 值 |
|------|-----|
| **标题** | Initial Demonstration of Automated Fuel Performance Analysis of EBR-II Metallic Fuel Pins Using BISON |
| **作者** | K.M. Paaren, R.L. Williamson, J.D. Hales, A.M. Caspersen, C.J. Matthews, A. Soderquist, B.W. Spencer, D.L. Porter |
| **期刊** | Nuclear Engineering and Design 382 (2021) 111393 |
| **年份** | 2021 |
| **Slug** | 2021_Paaren_AutomatedFuelPerformance_BISON_EBR2 |
| **关键词** | BISON, EBR-II, 金属燃料, U-Pu-Zr, 燃料性能建模, 自动化, PIE验证 |

## 中文摘要

本文展示了利用 BISON 燃料性能代码对 EBR-II 反应堆金属燃料棒进行自动化建模与验证的初步成果。研究开发了一套 Python 脚本，从 IMIS 和 FIPD 两个数据库自动提取燃料棒几何尺寸、功率历史、冷却剂边界条件、中子通量等信息，生成标准化的 BISON 2D R-Z 轴对称输入文件。

验证选取了四根燃料棒：X430 实验的 T653（U-19Pu-10Zr, 75% TD）、X441 实验的 DP20 和 DP45（U-19Pu-10Zr, 75% 和 85% TD）、X486 实验的 J555（U-10Zr, 75% TD, SS316 包壳）。模拟采用 SmearedPelletMesh 网格，包含 UPuZr 燃料相模型、热传导、蠕变、热膨胀、裂变气体肿胀与释放、固体肿胀等材料模型。

主要结果：(1) 燃耗预测与 IMIS/FIPD 数据吻合良好，最大偏差 6.51%（DP20）；(2) 裂变气体释放分数预测约 70%，与 PIE 测量（最高 73%）一致；(3) 包壳轮廓形变在无摩擦接触条件下大致吻合，但摩擦系数 μ=0.4 时高密度棒出现过预测；(4) 轴向燃料肿胀预测系统性偏高约 15-26%，主要归因于 FCMI 模型的不确定性。

本文建立了 EBR-II 金属燃料 BISON 建模的标准化流程，为大规模燃料性能代码验证和材料模型基准测试奠定了基础。

## 关键材料模型

| 现象 | BISON 对象 | 参考文献 |
|------|-----------|---------|
| 燃料相 | PhaseUPuZr | Galloway et al., 2015 |
| 热传导 | ThermalUPuZr | Billone 1968; Savage 1968 |
| 弹性张量 | UPuZrElasticityTensor | Hofman et al., 2019 |
| 蠕变 | UPuZrCreepUpdate | Hofman et al., 2019 |
| 热膨胀 | UPuZrThermalExpansionEigenstrain | Geelhood & Porter, 2018 |
| 气态肿胀 | UPuZrGaseousEigenstrain | Olander 1976; Karahan 2010 |
| 裂变气体释放 | UPuZrFissionGasRelease | Hofman et al., 1997 |
| 固体肿胀 | BurnupDependentEigenstrain | Ogata & Takeshi, 1999 |
| FCCI | MetallicFuelWastage | Hales et al., 2015 |

## 关键参数

- 每次裂变能量：3.2 × 10⁻¹¹ J
- 冷却剂压力：0.151 MPa（钠冷却剂）
- 初始充气压力：0.086 MPa
- 网格平均纵横比：25.18
- 摩擦系数对比：0（无摩擦）vs 0.4
- 各向异性肿胀因子：0.5
- LGHR 截止值：< 15 kW/m

## 验证结果

| 参数 | BISON vs PIE 一致性 |
|------|-------------------|
| 燃耗 | ✅ 良好（偏差 < 7%） |
| FGR 分数 | ✅ 良好（~70%） |
| 包壳轮廓 | ⚠️ 中等（依赖摩擦模型） |
| 轴向肿胀 | ❌ 偏高 15-26% |
| CDF | ✅ 无摩擦时均 < 1 |

## Related Work
- [[wiki/summaries/2023_Development_formulation_physics_based_metallic_fuel|2023_Development_formulation_physics_based_metallic_fuel]] — BISON金属燃料物理模型基线，本文建立的自动化流程的后续发展
- [[wiki/summaries/2016_Hales_BISON_TheoryManual|2016_Hales_BISON_TheoryManual]] — BISON理论手册，本文使用的材料模型的理论基础
- [[wiki/concepts/FuelPerformanceCodes|FuelPerformanceCodes]] — 本文核心工具BISON所属的燃料性能代码类别
- [[wiki/summaries/2013_Karahan_FEAST_ExtendedSwelling_UPuZr|2013_Karahan_FEAST_ExtendedSwelling_UPuZr]] — FEAST-METAL金属燃料肿胀模型，本文BISON验证的对比参考
- [[wiki/summaries/1990_Hofman_SwellingBehaviorUPuZr|1990_Hofman_SwellingBehaviorUPuZr]] — EBR-II U-Pu-Zr肿胀实验经典数据，本文验证数据来源
