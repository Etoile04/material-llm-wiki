# 辐照诱导超晶格形成中的相变机制研究（钼）

## 基本信息
- **作者**: Larry K. Aagesen, Yongfeng Zhang, Chao Jiang, Jian Gan
- **机构**: Idaho National Laboratory, University of Wisconsin
- **年份**: 2025
- **期刊**: (INL报告)
- **DOI**: 待确认
- **材料**: BCC钼 (Mo)
- **关键词**: 空位超晶格、动力学蒙特卡洛、调幅分解、形核长大、1D间隙原子扩散

## 摘要

本文通过原子动力学蒙特卡洛（AKMC）模拟和速率理论分析模型，系统研究了辐照条件下BCC钼中空位超晶格形成的相变机制转变。研究采用SPPARKS代码实现AKMC模拟，假设自间隙原子（SIA）沿⟨111⟩方向进行1D各向异性扩散。

**核心发现**：随着辐照剂量率的增加，空位超晶格的相变机制从**形核长大**（nucleation and growth）转变为**调幅分解**（spinodal decomposition）。在低剂量率（10⁻²~10⁻¹ dpa/s）下，空位团簇随机形核后逐渐对齐排列，符合形核长大机制；在高剂量率（1~10 dpa/s）下，出现平均空位浓度随时间的二阶导数∂²c̄ᵥ/∂t² > 0的区域，对应调幅不稳定性驱动的超晶格形成。

**理论分析**：基于Cahn-Hilliard理论的速率方程分析表明，∂²c̄ᵥ/∂t² > 0的唯一原因是调幅不稳定性引起的复合速率降低。非辐照条件下调幅分解判据∂²f/∂cᵥ² < 0在辐照条件下修正为∂²f/∂cᵥ² < -√(4κQ/Mᵥ)，其中Q = kᵢᵥcᵢ + kₛDᵥ + P。

**温度效应**：升高温度使调幅分解的临界剂量率增大。773K时转变剂量率约0.6 dpa/s，873K时升至约11 dpa/s。超晶格间距λ随温度升高而增大（773K时3.15 nm，1023K时6.3 nm），但模拟预测值低于实验值。

**材料对比**：分析表明在常规离子辐照条件下（10⁻² dpa/s），镍（Ni）是在超晶格形成温度窗口内唯一可能实验观察到相变机制转变的金属。对于钼，1173K离子辐照实验中的转变剂量率约3400 dpa/s，远超实验条件。

## Key Equations

### 1. 系统总能量（对势模型）
$$E = \frac{1}{2}\sum_{\alpha=1}^{2}\sum_{j=1}^{N}\sum_{k=1}^{N_\alpha}\epsilon_\alpha^{jk}$$
- $E$: 系统总能量；$\alpha$: 近邻壳层(1=1NN, 2=2NN)；$\epsilon_\alpha^{jk}$: 键能

### 2. 混合焓与梯度能系数
$$E_{mix} = 8\epsilon_1^{mv} + 6\epsilon_2^{mv}, \quad \kappa = \frac{\epsilon_1^{mv} + \epsilon_2^{mv}}{a_0}$$
- $E_{mix}$: 混合焓(3.0 eV/atom)；$\kappa$: 梯度能系数(2.41 eV/nm)

### 3. 空位/间隙原子演化方程（Cahn-Hilliard + 速率理论）
$$\frac{\partial c_v}{\partial t} = \nabla \cdot M_v \nabla\left(\frac{\delta F}{\delta c_v}\right) + P - k_s D_v c_v - k_{iv} c_v c_i$$
$$\frac{\partial c_i}{\partial t} = \nabla \cdot D_i \nabla c_i + P - k_s D_i c_i - k_{iv} c_v c_i$$
- $M_v = D_v/(k_BT)$: 空位迁移率；$P$: 缺陷产生速率；$k_s$: 尾闾强度；$k_{iv}$: 复合速率常数

### 4. 辐照下调幅分解临界条件
$$\frac{2\omega}{V_a} - \frac{k_BT}{V_a}\frac{1}{c_v^{crit}(1-c_v^{crit})} = \sqrt{\frac{4\kappa Q}{M_v}}$$
- $c_v^{crit}$: 调幅分解临界空位浓度；$\omega$: 规则溶液参数

### 5. 稳态空位浓度
$$c_v^{ss} = \frac{-k_s D_i D_v + \sqrt{(k_s D_i D_v)^2 + 4k_{iv}PD_i D_v}}{2k_{iv}D_v}$$
- 当 $c_v^{ss} > c_v^{crit}$ 时发生调幅分解

## 参数表（Table 1）

| 参数 | 值 | 单位 |
|------|-----|------|
| $E_{mix}$ | 3.0 | eV |
| $\kappa$ | 2.41 | eV/nm |
| $\epsilon_1^{mv}$ | 0.36047 | eV |
| $\epsilon_2^{mv}$ | 0.01938 | eV |
| $a_0$ | 0.315 | nm |
| $E_0^i$ (SIA迁移能) | 0.05 | eV |
| $E_0^v$ (空位迁移能) | 1.495 | eV |
| $\nu_0$ | 10¹² | s⁻¹ |
| $R_{iv}$ (复合距离) | 0.445 | nm |
| $N_s$ (尾闾吸收跳数) | 1000 | - |
