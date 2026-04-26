# 2021_Poschmann_MassTransport_Interdiffusion

**标题**: Thermochemically-informed Mass Transport Model for Interdiffusion of U and Zr in Irradiated U-Pu-Zr Fuel with Fission Products

**作者**: Max Poschmann, Markus H.A. Piro, Theodore M. Besmann, Kevin T. Clarno, Srdjan Simunovic

**期刊**: Journal of Nuclear Materials (2021)

**DOI**: 待补充

**标签**: MODEL, diffusion, interdiffusion, U-Pu-Zr, BISON, Thermochimica, chemical-potential, fission-products, constituent-redistribution

---

## 摘要

本文提出了一种基于热化学驱动力（广义化学势梯度）的金属燃料U-Zr组元再分配新模型，并将裂变产物的化学效应纳入考虑。与传统的Fickian扩散+Soret项方法不同，该模型以化学势梯度 $\nabla\mu_k$ 作为扩散驱动力，利用热化学求解器Thermochimica实时计算各相的化学势、相分数和组成。模型与燃料性能程序BISON耦合，对U-19Pu-10Zr燃料棒在1.9% FIMA燃耗下的Zr径向再分配进行了模拟，成功再现了EBR-II X419实验中T179燃料棒的Zr耗竭区（"浴缸"剖面）。

关键发现：（1）裂变产物通过稳定γ相的不溶混间隙（miscibility gap）显著增强了U-Zr互扩散迁移率，使Zr耗竭区扩大至燃料半径的约18%（不含裂变产物时约14%）；（2）裂变产物的积累使Zr-U化学势差梯度降低约0.4%，对扩散驱动力有轻微抑制；（3）基于热化学计算的等效热输运系数 $Q^*$ 在γ相中仅为25–50 kJ/mol，远低于先前文献假定的-200 kJ/mol，且具有显著的温度和成分依赖性；（4）该方法仅需有限的输运系数参数集，无需针对各相分别设定热输运常数和相边界参数。

## Key Equations

### 1. Gibbs能最小化拉格朗日函数

$$L = \frac{G}{RT} - \sum_{j=1}^{C} \tilde{\Gamma}_j (b_j - b_j^m)$$

- $G$: 系统总Gibbs自由能，$R$: 理想气体常数，$T$: 绝对温度
- $\tilde{\Gamma}_j$: 组元 $j$ 的无量纲化学势，$b_j$: 组元 $j$ 的克原子数
- $C$: 系统组元数，$m$: GEM迭代索引

### 2. 摩尔通量与漂移速度

$$J_k = \nu_k \, n_k$$

- $J_k$: 组元 $k$ 的摩尔通量 [mol/(m²·s)]，$\nu_k$: 平均漂移速度 [m/s]
- $n_k$: 组元 $k$ 的体积摩尔密度 [mol/m³]

### 3. Einstein关系 — 机械迁移率

$$M_k = \frac{D_k}{RT}$$

- $M_k$: 机械迁移率 [mol·m²/(J·s)]，$D_k$: 扩散系数 [m²/s]

### 4. Arrhenius扩散系数

$$D_k = D_0 \, e^{-Q/(RT)}$$

- $D_0$: 指前因子 [m²/s]，$Q$: 激活能 [J/mol]

### 5. 化学势梯度驱动力

$$F_k = -\nabla\mu_k$$

$$J_k = -M_k \, n_k \, \nabla\mu_k$$

- 以化学势梯度（而非浓度梯度）作为扩散驱动力的核心方程

### 6. 广义化学势展开

$$d\mu = \frac{\partial\mu}{\partial x_k}dx_k + \frac{\partial\mu}{\partial T}dT + \frac{\partial\mu}{\partial P}dP$$

$$\mathbf{F}_k = -\frac{\partial\mu}{\partial x_k}\nabla x_k - \frac{\partial\mu}{\partial T}\nabla T - \frac{\partial\mu}{\partial P}\nabla P$$

- 自动包含浓度梯度、温度梯度（Soret效应）和压力梯度的贡献

### 7. 等效热输运系数

$$Q^* = \frac{\partial\mu}{\partial x_k} \cdot \frac{T}{x_k(1-x_k)}$$

- 将化学势对组成的偏导数与传统热输运系数 $Q^*$ 联系起来
- γ相计算值约25–50 kJ/mol，远低于文献值-200 kJ/mol

### 8. 守恒方程（FEM实现）

$$\frac{\partial n_k}{\partial t} + \nabla\cdot\left(-M_k \, n_k \, \nabla\mu_{gk}\right) = 0$$

### 9. U-Zr互扩散驱动力

$$F_k^{Zr} = -\nabla(\mu_{Zr} - \mu_{U}), \quad F_k^{U} = -\nabla(\mu_{U} - \mu_{Zr})$$

- 基于Zr原子与U原子互换时系统Gibbs能变化

## 扩散参数（Table 1）

| 相 | $D_0$ [m²/s] | $Q$ [kJ/mol] | 来源 |
|---|---|---|---|
| αU | $1.35 \times 10^{-1}$ | 170 | Galloway 2015 |
| αZr | $1.50 \times 10^{-1}$ | 275 | Horváth 1984 |
| γ | $10^{-1.62-8.05x_{Zr}+9.13x_{Zr}^2}$ | $128-107x_{Zr}+174x_{Zr}^2$ | Hofman 1996, Galloway 2015 |

注：表中参数在本文中被统一放大3000倍以匹配实验观测。

## 与本项目的关系

本文提供了一个基于化学势梯度的U-Zr互扩散建模框架，相比传统Fickian+Soret方法减少了经验参数数量。该模型可用于金属燃料肿胀模拟程序中组元再分配模块的参考，特别是在处理多相系统中扩散驱动力计算时。化学势梯度自动包含温度效应（Soret项），无需单独标定热输运系数。

## Related Work
- [[wiki/concepts/ConstituentRedistribution|ConstituentRedistribution]] — 本文核心主题：U-Pu-Zr组元再分布建模
- [[wiki/summaries/2021_Hirschhorn_CALPHAD_BISON_Redistribution|2021_Hirschhorn_CALPHAD_BISON_Redistribution]] — CALPHAD查找表方法实现组元再分布，与本文化学势梯度方法形成方法论对比
- [[wiki/summaries/1996_Hofman_TemperatureGradientRedistribution_UZr|1996_Hofman_TemperatureGradientRedistribution_UZr]] — Hofman经典温度梯度再分布实验，本文引用的扩散参数来源
- [[wiki/summaries/2021_Paaren_AutomatedFuelPerformance_BISON_EBR2|2021_Paaren_AutomatedFuelPerformance_BISON_EBR2]] — 本文模型与BISON耦合，EBR-II燃料棒验证
- [[wiki/concepts/SoretEffectInMetallicFuels|SoretEffectInMetallicFuels]] — 本文计算的等效热输运系数Q*直接关联Soret效应
