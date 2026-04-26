# A Review of Void and Gas Bubble Superlattices Self-Organization Under Irradiation

**Authors:** Yongfeng Zhang  
**Year:** 2023  
**Journal:** Frontiers in Nuclear Engineering, 2:1110549  
**DOI:** 10.3389/fnuen.2023.1110549  
**Affiliation:** University of Wisconsin-Madison, Department of Engineering Physics  
**Material:** 综述覆盖 fcc/bcc/hcp 金属、陶瓷 (CaF₂)、半导体 (Si)  
**Type:** Review Article

---

## 概述

本文是自 Ghoniem 等人 2001 年综述以来对空位超晶格（VSL）和气泡超晶格（GBSL）自组织现象的首次全面综述。Zhang 系统总结了 2001 年以来新增的实验观测，重点阐述了基于 Cahn-Hilliard 不稳定性与各向异性自间隙原子（SIA）扩散相结合的形成机制理论，该理论由作者团队（Gao, Zhang 等）发展，能定量预测超晶格参数 $a_L$ 对温度、剂量率和剂量的依赖关系，并获得实验与 LKMC 模拟验证。

**核心发现：**

1. **温度窗口统一**：VSL 形成（$0.25T_m < T < 0.5T_m$）与 GBSL 形成（$0.15T_m < T < 0.35T_m$）的窗口可通过 gas-appm/dpa 比统一——该比值越高，窗口越宽且温度下限越低（Sun et al., 2019）
2. **非同构超晶格**：U-7Mo 中 fcc Xe GBSL（bcc 基体）和 bct VSL/GBSL 在 Cr、Mo 中的发现打破了"超晶格结构必与基体相同"的传统认知
3. **三阶段形成过程**：随机排列 → 面内有序 → 三维晶格，具体路径取决于空位积累速率与复合速率的相对快慢
4. **$a_L$ 的解析表达式**：$\lambda_c = 2\pi(\kappa M_v / Q)^{1/4}$，其中 $Q$ 包含复合与尾闾吸收项，可解释温度↑→$a_L$↑、剂量率↑→$a_L$↓、剂量饱和等实验趋势
5. **各向异性 SIA 扩散决定结构**：1D SIA 沿 $\langle 111 \rangle$ → bcc，沿 $\langle 110 \rangle$ → fcc；2D SIA 在 $\{110\}$ 面 → bcc，在 $\{111\}$ 面 → fcc；不依赖于基体结构

**与金属燃料肿胀的关联**：U-7Mo 中 Xe GBSL 在低燃耗时以 VSL 形式形成（极高的有序度），随后被裂变气体充压。纳米尺度有序气泡阵列可能有助于缓解气体肿胀（Chen et al., 2017）。

---

## Key Equations

### Cahn-Hilliard 型空位演化方程

$$\frac{\partial c_v}{\partial t} = P(1 - c_v) + \nabla \cdot M_v \nabla \frac{\delta F}{\delta c_v} - k_{iv}c_i c_v - k_{vs}D_v c_v$$

$$\frac{\partial c_i}{\partial t} = P(1 - c_v) + \nabla \cdot D_i \nabla c_i - k_{iv}c_i c_v - k_{is}D_i c_i$$

其中 $M_v = D_v / k_BT$，$F$ 采用规则溶液模型（混合焓 $E_{mix}$ + 界面能 $\kappa$）。

### 扰动波增长因子

$$R(k) = -(M_v f'' k^2 + M_v \kappa k^4 + Q)$$

其中 $Q = k_{iv}c_i + k_{vs}D_v + P$。当 $c_v$ 超过临界值时，$R(k)$ 对特定 $k_c$ 变为正，触发不稳定性。

### 超晶格参数解析解

$$\lambda_c = 2\pi \left(\frac{\kappa M_v}{Q}\right)^{1/4}$$

对于 bcc 晶体中面间距 $\{110\}$：$a_L = \sqrt{2}\,\lambda_c = 2\sqrt{2}\pi(\kappa M_v / Q)^{1/4}$

### logP 与 1/T 等价性

温度窗口的低边界在 $\log P$ vs $T_m/T$ 图中近似为直线，斜率正比于空位迁移能 $E_v^m$。

### VSL/GBSL 形成窗口

- **VSL:** $0.25T_m < T < 0.5T_m$
- **GBSL:** $0.15T_m < T < 0.35T_m$
- 统一条件：gas-appm/dpa 比越高，窗口越宽

### SIA 扩散各向异性 → 超晶格结构对应表

| SIA 扩散模式 | bcc 基体预测 | fcc 基体预测 | 实验验证 |
|---|---|---|---|
| 1D $\langle 111 \rangle$ | bcc | — | Mo VSL ✓ |
| 1D $\langle 110 \rangle$ | fcc | fcc | U-7Mo Xe GBSL ✓ |
| 1D $\langle 100 \rangle$ | sc | — | — |
| 2D $\{110\}$ | bcc | — | Mo ✓ |
| 2D $\{111\}$ | — | fcc | — |

## Detailed Sections

综述论文，无独立详细章节文件。

---

## Relationships

- [[wiki/summaries/2015_Miller_TEMGasBubbleSuperlatticeU7Mo|Miller 2015]] — U-7Mo 中 Xe GBSL 的 TEM 实验表征
- [[wiki/summaries/2016_Hu_GasBubbleSuperlatticeFormationPF|Hu 2016]] — 1D SIA 扩散相场模拟
- [[wiki/summaries/2008_Kim_IntergranularFGBubblesUMo|Kim 2008]] — U-Mo 晶间气泡
- [[wiki/concepts/RateTheoryFramework|RateTheoryFramework]] — 本综述的理论基础（BEK 速率方程）
- [[wiki/concepts/FissionGasReleaseModels|FissionGasReleaseModels]] — 气泡超晶格与裂变气体释放的关联

## Related Work
- [[wiki/summaries/2016_Hu_GasBubbleSuperlatticeFormationPF|2016_Hu_GasBubbleSuperlatticeFormationPF]] — Hu相场模型建立1D SIA扩散机制，本文综述的核心理论之一
- [[wiki/summaries/2025_Jiang_GasBubbleSuperlatticePhaseField|2025_Jiang_GasBubbleSuperlatticePhaseField]] — 最新相场GBS模拟，验证了本文综述的各向异性SIA扩散理论
- [[wiki/summaries/2023_Smith_EarlySelfOrganizationGBS|2023_Smith_EarlySelfOrganizationGBS]] — 早期GBS自组织的TEM实验观测，验证本文描述的三阶段形成过程
- [[wiki/summaries/2015_Miller_TEMGasBubbleSuperlatticeU7Mo|2015_Miller_TEMGasBubbleSuperlatticeU7Mo]] — U-7Mo GBS表征数据，本文综述的重要实验基础
- [[wiki/summaries/2024_Aagesen_VacancyProductionPF|2024_Aagesen_VacancyProductionPF]] — 相场空位产生率参数化，与本文Cahn-Hilliard框架直接相关
- [[wiki/entities/GasBubbleSuperlattice|GasBubbleSuperlattice]] — 本文是GBS/VSL自组织领域最全面的综述
