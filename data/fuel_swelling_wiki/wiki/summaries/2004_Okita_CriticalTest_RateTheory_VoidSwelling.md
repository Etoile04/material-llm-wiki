# 2004_Okita_CriticalTest_RateTheory_VoidSwelling

## 基本信息
- **标题**: A Critical Test of the Classical Rate Theory of Void Swelling
- **作者**: T. Okita, W.G. Wolfer
- **机构**: Lawrence Livermore National Laboratory (LLNL)
- **来源**: Journal of Nuclear Materials 327 (2004) 130–139
- **关键词**: 空洞肿胀、经典率理论、偏压因子、奥氏体钢、FFTF/MOTA辐照、温度依赖性

## 摘要

本文对经典率理论（classical rate theory）预测空洞肿胀的能力进行了系统性临界测试。实验采用高纯Fe-15Cr-16Ni三元奥氏体合金，在FFTF/MOTA装置中辐照，利用温度精确控制系统使所有样品处于极窄的温度范围内（365–593°C），同时获得超过两个数量级的剂量率变化（10⁻⁶–10⁻⁴ dpa/s）。

理论推导从单空位-单间隙原子速率方程出发，建立了包含复合、偏压驱动吸收和热发射的完整框架。核心结论为：(1) 在偏压主导温度区间（<550°C），空洞稳态肿胀率为~1%/dpa，且不依赖于剂量率，与实验观测完全一致；(2) 空洞肿胀率对空位迁移能$E_v$极度敏感，$E_v$从1.2变化到1.4 eV导致肿胀率变化约3个数量级；(3) 当$D_i \gg D_v$时，复合由空位迁移控制，低温下肿胀率与$\sqrt{\dot{F}}$（剂量率平方根）成正比，高温下与$\dot{F}$成正比；(4) 偏压因子比$Z_i^{disl}/Z_v^{disl}$的合理范围为1.1–2.0，与Tenbrink等的双离子辐照实验一致。

通过TEM测量空洞尺寸分布并结合率理论计算，发现$E_v = 1.3$ eV、偏压因子比~1.02–1.05时可最佳重现实验肿胀数据。本文为率理论在空洞肿胀预测中的适用性提供了关键实验验证。

## Key Equations

### 缺陷速率方程（Eq. 5-6）
$$\frac{dC_v}{dt} = \eta\dot{F} - \kappa D_v C_v C_i - D_v \sum_S N^S A^S Z_v^S (C_v - C_v^S)$$
$$\frac{dC_i}{dt} = \eta\dot{F} - \kappa D_v C_v C_i - D_i \sum_S N^S A^S Z_i^S C_i$$

其中$\kappa = 4\pi R_c (1/D_v + 1/D_i)^{-1} \sum 1/A^S$为复合系数，$\eta$为级联逃逸分数。

### 稳态缺陷浓度（Eq. 8-9）
$$D_v C_v = \langle Z_i \rangle W + D_v \langle C_v^S \rangle, \quad D_i C_i = \langle Z_v \rangle W$$

### 空洞生长速率（Eq. 15）
$$\frac{da}{dt} = Z_v^0 \left(\frac{\langle Z_i \rangle Z_i^0}{\langle Z_v \rangle Z_v^0} W - D_v [C_v^0 - \langle C_v^S \rangle]\right)$$

第一项为偏压驱动项（正比于W），第二项为热退火项。当$2\gamma/a > p_g$时热退火促进生长。

### 空位扩散系数（Eq. 16）
$$D_v = D_{v0} \exp(-E_v / kT), \quad D_{v0} = 1.286 \times 10^{-6} \text{ m}^2/\text{s}$$

### 肿胀率计算（Eq. 17）
$$\frac{1}{V}\frac{dV}{dt} = \sum_h 4\pi a_h^2 N_h \frac{da_h}{dt}$$

## 关键参数

| 参数 | 值 | 来源 |
|------|-----|------|
| $D_{v0}$ | 1.286×10⁻⁶ m²/s | Dimitrov & Dimitrov |
| $E_v$ | 1.28±0.17 eV (推荐1.3 eV) | 电阻率/正电子湮没 |
| $\eta$ | 0.1–0.2 | 级联模拟 |
| $Z_i^{disl}/Z_v^{disl}$ | 1.1–2.0 | Sniegowski & Wolfer |
| 稳态肿胀率 | ~1%/dpa | 实验观测 |
| 辐照温度 | 365–593°C | FFTF/MOTA |
| 剂量率范围 | 10⁻⁶–10⁻⁴ dpa/s | 多位置辐照 |

## Related Work
- [[wiki/entities/FFTF|FFTF]] — FFTF/MOTA irradiation facility used in this study
- [[wiki/concepts/RateTheoryFramework|RateTheoryFramework]] — this paper provides critical experimental validation of rate theory for void swelling
- [[wiki/concepts/SwellingMechanisms|SwellingMechanisms]] — bias-driven void swelling mechanism
- [[wiki/summaries/2008_Surh_VoidNucleationGrowthCoalescence|2008_Surh_VoidNucleationGrowthCoalescence]] — related void nucleation and growth modeling
- [[wiki/summaries/2024_Aagesen_VacancyProductionPF|2024_Aagesen_VacancyProductionPF]] — modern phase-field approach to void swelling
