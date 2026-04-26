# BISON 中 SiC 包壳燃料性能模型的早期实现

**Authors:** J. J. Powers (ORNL)  
**Report:** ORNL/TM-2015/452  
**Date:** 2015-09-18  
**Program:** DOE-NE Advanced Fuels Campaign (ATF)

## 元数据

| 字段 | 值 |
|------|-----|
| **标题** | Early Implementation of SiC Cladding Fuel Performance Models in BISON |
| **作者** | J. J. Powers |
| **机构** | Oak Ridge National Laboratory (ORNL) |
| **报告编号** | ORNL/TM-2015/452 |
| **年份** | 2015 |
| **Slug** | 2015_Powers_BISON_SiC_Cladding_FuelPerformance |
| **关键词** | SiC, 包壳, BISON, 事故容错燃料(ATF), SiC/SiC 复合材料, CVD SiC, PWR, 热力学性能 |
| **与核心主题相关性** | ★ 间接相关（SiC 包壳而非金属燃料肿胀，但为 BISON 燃料性能建模框架的重要参考） |

## 中文摘要

本文报告了在美国能源部事故容错燃料（ATF）计划框架下，于 BISON 燃料性能代码中建立 SiC 基复合包壳热力学模型的早期工作。BISON 是基于 MOOSE 框架的有限元燃料性能分析工具，原本主要针对 UO₂/Zircaloy 体系，本文扩展了其对 SiC 材料的建模能力。

研究背景方面，SiC/SiC 陶瓷基复合材料因其高温强度（≥1400°C 无强度退化）、低中子吸收截面（Σa = 0.0021 cm⁻¹，低于 Zircaloy 的 0.0028 cm⁻¹）和优异的高温蒸汽氧化抗性，被视为替代 Zircaloy 的 ATF 包壳候选材料。中子学分析表明，使用标准 Zircaloy 厚度（571.5 μm）时 SiC 仅需 4.81% 富集度即可匹配循环长度（低于 Zircaloy 的 4.9%），但若厚度增至 ~900 μm 则需 5.5% 富集度。然而，SiC 的低热导率导致包壳内外壁大温差和大热应力。

材料模型方面，文中针对多种 SiC 材料形式建立了物性模型：化学气相沉积（CVD）SiC 的物性数据较成熟；纳米浸渗瞬态共晶相（NITE）SiC 和化学气相渗透（CVI）SiC 的实验数据也在近年得到补充。BISON 公开版本仅包含 CVD SiC 的蠕变模型，其余物性需通过通用材料模型或新开发模块实现。本文开发了针对 CVD SiC 和复合 SiC 的专用材料模型。

验证方面，采用 2014 年 MIT SiC 建模技术研讨会定义的基准问题——一个双层（内层单晶、外层复合 SiCf/SiCm）无燃料的 2D R-Z 稳态包壳管模型。计算得到的径向、轴向和环向应力剖面与其他燃料性能代码结果吻合良好，峰值压应力约 -24 MPa，验证了 BISON 实现 SiC 建模的基本功能正确性。

本文为后续更复杂的 SiC 包壳设计评估（如 duplex vs. triplex 设计、层厚优化、材料敏感性分析）奠定了基础。对金属燃料项目而言，本文展示了 BISON 框架扩展新材料模型的通用方法论。

## Key Equations

### 1. BISON 控制方程（基于 MOOSE 框架）

BISON 求解耦合非线性偏微分方程组，包括：

**能量守恒（热传导）：**
$$\rho c_p \frac{\partial T}{\partial t} = \nabla \cdot (k \nabla T) + \dot{Q}$$

**动量守恒（Cauchy 方程）：**
$$\nabla \cdot \boldsymbol{\sigma} + \mathbf{b} = \rho \ddot{\mathbf{u}}$$

**组分守恒：**
$$\frac{\partial C_i}{\partial t} = \nabla \cdot (D_i \nabla C_i) + S_i - \lambda_i C_i$$

### 2. SiC 关键材料属性对比

| 属性 | Zircaloy | FeCrAl | SiC |
|------|----------|--------|-----|
| 密度 (g/cm³) | 6.56 | 7.1 | 2.58 |
| Σa (cm⁻¹, 0.253 eV) | 0.0028 | 0.0634 | 0.0021 |
| 高温强度保持 | ≤1200°C | 优于Zr | ≥1400°C |

### 3. 中子学匹配关系（SiC Case II）

保持 Zircaloy 参考包壳厚度 571.5 μm 时：
- $^{235}$U 富集度：4.81%（低于 Zircaloy 的 4.9%）
- 比功率：38.33 MW/tHM
- 卸料燃耗：57.9 GWd/tHM（1500 EFPD）

## 实验与模拟数据

### 基准问题规格
- **几何**: 双层 SiC 包壳管（内层 CVD 单晶 + 外层 SiCf/SiCm 复合材料）
- **维度**: 2D R-Z 轴对称
- **条件**: 稳态，无时间依赖，无燃料
- **网格**: 每层 10 个径向间隔
- **初始温度**: 600°C

### 应力结果
- 径向峰值压应力: ~-24 MPa
- 计算结果与其他代码（FRAPCON, FEMAXI 等）吻合

## 局限性与未来工作

1. 仅使用简化材料模型，未考虑辐照损伤效应
2. 仅验证稳态基准问题，未涉及瞬态或辐照工况
3. 未来需开发温度和辐照剂量相关的材料模型
4. 需扩展至 BWR 包壳和通道箱分析
5. 需进行工程设计尺度模拟评估不同 SiC 包壳概念

## Related Work
- [[wiki/entities/BISONCode|BISONCode]] — 本文在BISON框架中扩展SiC包壳材料模型
- [[wiki/concepts/FuelPerformanceCodes|FuelPerformanceCodes]] — BISON作为燃料性能代码的代表，本文展示了其扩展新材料的通用方法论
- [[wiki/summaries/2016_Hales_BISON_TheoryManual|2016_Hales_BISON_TheoryManual]] — BISON理论手册，系统描述BISON代码的物理框架和方程
- [[wiki/summaries/2019_VanUffelen_FuelPerformanceReview|2019_VanUffelen_FuelPerformanceReview]] — 燃料性能建模综述，涵盖BISON等主要代码的对比
