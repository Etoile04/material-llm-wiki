# U-(Pu)-Zr核燃料中裂变气体气泡生长与连通的相场模拟

## Metadata
| Field | Value |
|-------|-------|
| Authors | Larry K. Aagesen, Albert Casagranda, Christopher Matthews, Benjamin W. Beeler, Stephen Novascone |
| Year | 2022 |
| Journal | Journal of Nuclear Materials |
| DOI | 10.1007/s40565-022-01811-3 |

## Overview

本文使用Cahn-Hilliard方程相场模型模拟了U-(Pu)-Zr核燃料高温中心区域（γ相主导）裂变气体气泡的生长与连通（Interconnection）过程，并将模拟结果用于参数化BISON燃料性能代码中的两种工程级肿胀模型。

模型采用单一缺陷种（不溶性裂变气体原子如Xe及伴随空位），通过源项模拟裂变产生。基于实验观测设定初始气泡数密度 $N = 3 \times 10^{14}$ m⁻³，缺陷扩散系数在2-10 nm²/s范围内变化。模拟发现：气泡表面积在生长初期快速增加，随后因连通和粗化而减小；连通体积分数 $f_V$ 在孔隙率 $p \approx 0.25-0.30$ 范围内急剧增加。渗透阈值（Percolation Threshold） $p_c$ 约为0.26，略低于连续介质中重叠3D球的渗透阈值（0.2896）。扩散系数显著影响微观结构形态但对 $f_V$-$p$ 关系影响不大。

模拟结果为BISON代码提供了关键参数：简单肿胀模型（UPuZrGaseousEigenstrain）的连通起始孔隙率 $p_i = 0.263$、终止孔隙率 $p_t = 0.280$；粘塑性肿胀模型的连通函数参数 $p_{start} = 0.198$、$p_{end} = 0.327$。

## Key Equations

### Cahn-Hilliard方程（含源项）
$$\frac{\partial c}{\partial t} = \nabla \cdot (M \nabla \mu) + s$$

其中 $c$ 为归一化缺陷浓度，$M$ 为迁移率，$\mu = \delta F / \delta c$ 为化学势，$s$ 为源项。

### 总自由能
$$F = \int_V \left[ f_b(c) + \frac{\kappa}{2}|\nabla c|^2 \right] dV$$

其中双势阱函数 $f_b(c) = Wc^2(1-c)^2$，$W$ 为势垒高度，$\kappa$ 为梯度能系数。

### 化学势
$$\mu = \frac{\delta F}{\delta c} = W(2c - 1)(2c^2 - 2c + 1) - \kappa \nabla^2 c$$

### 源项
$$s = \dot{s}(1-g)(1-c)$$

其中 $g(c) = c^3(6c^2 - 15c + 10)$，限制新缺陷仅在基体相中产生。

### 孔隙率计算（考虑基体膨胀）
$$p = \frac{\tilde{V}}{V_0 + \tilde{V}} = \frac{V_f}{1 + V_f}$$

其中 $\tilde{V}$ 为气泡相体积，$V_0$ 为初始模拟域体积，$V_f = \tilde{V}/V_0$。

### 连通体积分数拟合函数
$$f_V(p) = \frac{1}{2}\left[1 + \text{erf}\left(\frac{p - p_{cen}}{\Delta}\right)\right]$$

### BISON简单肿胀模型
$$\frac{\Delta V}{V} = \frac{Y_{Xe} \dot{F} k_B T t}{N \cdot \frac{2\sigma}{r_{eq}} - p_{ext}}$$

### 界面参数关系
$$\delta = \sqrt{\frac{2\kappa}{W}}, \quad \sigma = \frac{\sqrt{2\kappa W}}{3}$$

由此得 $\kappa = \frac{3\sigma \delta}{2}$，$W = \frac{3\sigma}{2\delta}$。

## Physical Mechanisms

### 气泡生长与连通
裂变产生的缺陷扩散至气泡使其生长。当相邻气泡接触时发生合并（Coalescence），系统通过粗化（Coarsening）降低表面积和表面能。连通从孔隙率约25%开始，30%时所有气泡均与自由表面连通。

### 渗透阈值
连续相通道首次连接模拟域两端边界时的孔隙率定义为渗透阈值。本文 $p_c \approx 0.26$，低于重叠球模型（0.2896），因为本模型考虑了基体膨胀和粗化效应。

### 扩散系数效应
虽然扩散系数（2-10 nm²/s）显著影响微观结构形态（高扩散加速生长和粗化），但对渗透阈值影响不大，表明气泡连通过程可能由普适过程控制。

## Relationships
- [[PhaseFieldModeling]] — Cahn-Hilliard方程相场方法
- [[FuelAlloy]] — U-10Zr, U-(Pu)-Zr合金体系
- [[SwellingMechanisms]] — 气泡连通决定肿胀终止和气体释放开始
- [[FissionGasDiffusion]] — 缺陷扩散控制气泡生长速率
- [[CavitationalVoid]] — 气泡形核与生长的物理过程
