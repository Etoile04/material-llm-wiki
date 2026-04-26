# Phase Transformation Mechanism in Irradiation-Induced Superlattice Formation

## Metadata

- **Title:** Phase transformation mechanism in irradiation-induced superlattice formation
- **Authors:** Larry K. Aagesen, Yongfeng Zhang, Chao Jiang, Jian Gan
- **Journal:** Computational Materials Science
- **Year:** 2025
- **DOI:** https://doi.org/10.1016/j.commatsci.2024.113418
- **Affiliation:** Idaho National Laboratory, USA; University of Wisconsin-Madison, USA

## 摘要

本文利用原子动力学蒙特卡洛（AKMC）模拟研究了钼（Mo）在辐照条件下的空洞超晶格（void superlattice）形成机制，重点探讨了从"形核与生长"（nucleation and growth）到"调幅分解"（spinodal decomposition）两种相变机制之间的转变。模拟基于 SPPARKS 代码实现 BCC 结构 Mo 的辐照模型，其中自间隙原子（SIA）沿 ⟨111⟩ 方向进行一维扩散。

核心发现如下：（1）随着剂量率增加，空洞超晶格形成的相变机制从形核与生长转变为调幅分解。低剂量率（$10^{-2}$–$10^{-1}$ dpa/s）下，空洞随机形核后逐渐排列成有序结构，表现为径向分布函数（RDF）峰值的渐进增长；高剂量率（1–10 dpa/s）下，出现平均空位浓度对时间二阶导数 $\partial^2 \bar{c}_v / \partial t^2 > 0$ 的区域，标志着调幅失稳的快速发生，同时 RDF 长程有序峰值急剧增加。（2）温度升高将调幅分解的阈值剂量率推向更高值（如从 773 K 到 873 K 时，1 dpa/s 下的相变机制从调幅分解变为形核与生长）。（3）基于率理论的解析模型将 $\partial^2 \bar{c}_v / \partial t^2 > 0$ 归因于调幅失稳导致的空位-间隙复合率下降，并与 AKMC 结果定性一致。（4）超晶格间距随温度升高而增大（773 K: 3.15 nm → 1023 K: 6.3 nm），与实验趋势一致。（5）对 Mo、Cr、Ni、Cu 的解析分析表明，大多数金属中空洞超晶格以形核与生长方式形成；Ni 是最有可能在离子辐照条件下实验观察到相变机制转变的材料。

## Key Parameters

| 参数 | 值 | 说明 |
|------|-----|------|
| 材料 | Mo (BCC) | 模拟对象 |
| 晶格常数 $a_0$ | 0.315 nm | Mo BCC |
| 混合焓 $E_{mix}$ | 3.0 eV | 用于对键能参数化 |
| 梯度能系数 $\kappa$ | 2.41 eV/nm | Cahn-Hilliard |
| 1NN 键能 $\epsilon_1^{mv}$ | 0.36047 eV | Mo-空位最近邻 |
| 2NN 键能 $\epsilon_2^{mv}$ | 0.01938 eV | Mo-空位次近邻 |
| SIA 扩散势垒 $E_0^i$ | 0.05 eV | ⟨111⟩ 方向 1D 扩散 |
| 空位扩散势垒 $E_0^v$ | 1.495 eV | |
| 尝试频率 $\nu_0$ | $10^{12}$ s$^{-1}$ | |
| 复合半径 $R_{iv}$ | 0.445 nm ($\sqrt{2} a_0$, 3NN) | |
| 吸收跳跃数 $N_s$ | 1000 | 等效汇强度 |
| 模拟域 | $80 a_0 \times 80 a_0 \times 80 a_0$ | $N = 1{,}024{,}000$ 格点 |
| 温度范围 | 773–1073 K | 超晶格在 ≤1023 K 形成 |
| 剂量率范围 | $10^{-2}$–10 dpa/s | |
| 相变机制转变剂量率 (773 K) | ~0.6 dpa/s (解析模型) | |
| 相变机制转变剂量率 (873 K) | ~11 dpa/s (解析模型) | |

## Key Equations

**键能模型（1NN + 2NN）：**
$$E = \frac{1}{2} \sum_{\alpha=1}^{2} \sum_{j=1}^{N} \sum_{k=1}^{N_\alpha} \epsilon_\alpha^{jk}$$

**混合焓与梯度能系数参数化：**
$$E_{mix} = 8\epsilon_1^{mv} + 6\epsilon_2^{mv}, \quad \kappa = \frac{\epsilon_1^{mv} + \epsilon_2^{mv}}{a_0}$$

**Cahn-Hilliard 辐照方程（空位）：**
$$\frac{\partial c_v}{\partial t} = \nabla \cdot M_v \nabla \left(\frac{\delta F}{\delta c_v}\right) + P - k_s D_v c_v - k_{iv} c_v c_i$$

**Cahn-Hilliard 辐照方程（间隙原子）：**
$$\frac{\partial c_i}{\partial t} = \nabla \cdot D_i \nabla c_i + P - k_s D_i c_i - k_{iv} c_v c_i$$

**辐照条件下调幅分解判据：**
$$\frac{\partial^2 f}{\partial c_v^2} < -\sqrt{\frac{4\kappa Q}{M_v}}, \quad Q = k_{iv}c_i + k_s D_v + P$$

**稳态空位浓度（率理论）：**
$$c_v^{ss} = \frac{-k_s D_i D_v + \sqrt{(k_s D_i D_v)^2 + 4 k_{iv} P D_i D_v}}{2 k_{iv} D_v}$$

**调幅失稳与 $\partial^2 \bar{c}_v / \partial t^2 > 0$ 关联：**
$$\frac{\partial^2 \bar{c}_v}{\partial t^2} = -k_s D_v \frac{\partial \bar{c}_v}{\partial t} - k_{iv} \frac{\partial(c_v^0 c_i^0)}{\partial t} - \frac{\partial}{\partial t} \frac{1}{V}\int_V \frac{1}{2} k_{iv} \delta_v \delta_i \sigma_{k\lambda} \, dV$$

其中 $\sigma_{k\lambda} \leq 0$ 为 SIA 一维扩散引起的复合率降低因子。

## Related Work

- [[wiki/summaries/2025_Aagesen_PhaseTransformation_Superlattice|2025_Aagesen_PhaseTransformation_Superlattice]] — 同作者关于 Mo 中空洞超晶格的 AKMC 模拟，温度/剂量率对超晶格间距的影响
- [[wiki/summaries/2023_Zhang_Review_VoidBubbleSuperlattice_SelfOrganization|2023_Zhang_Review_VoidBubbleSuperlattice_SelfOrganization]] — 空洞/气泡超晶格自组织综述，提供实验与理论背景
- [[wiki/summaries/2016_Hu_GasBubbleSuperlatticeFormationPF|2016_Hu_GasBubbleSuperlatticeFormationPF]] — U-Mo 中气泡超晶格的相场模拟，对比形核与生长 vs 调幅分解
- [[wiki/summaries/2024_Aagesen_VacancyProductionPF|2024_Aagesen_VacancyProductionPF]] — Aagesen 同期关于空位产生相场模型的工作
- [[wiki/summaries/2023_Smith_EarlySelfOrganizationGBS|2023_Smith_EarlySelfOrganizationGBS]] — 气泡超晶格早期自组织行为的研究
- [[wiki/entities/GasBubbleSuperlattice|GasBubbleSuperlattice]] — 气泡超晶格（GBS）概念页，涵盖形成机制与材料体系
