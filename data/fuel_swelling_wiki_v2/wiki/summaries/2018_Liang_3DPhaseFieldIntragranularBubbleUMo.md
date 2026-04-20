# 辐照UMo燃料中晶内裂变气体气泡演化的三维相场模拟

## Metadata
| Field | Value |
|-------|-------|
| Authors | Linyun Liang, Zhi-Gang Mei, Yeon Soo Kim, Mihai Anitescu, Abdellatif M. Yacout |
| Year | 2018 |
| Journal | Journal of Nuclear Materials |
| DOI | 10.1016/j.jnucmat.2017.12.037 |

## Overview

本文开发了三维相场模型研究辐照U-Mo合金燃料中晶内裂变气体气泡（Intragranular Gas Bubble）的形成与演化，并预测了气泡引起的燃料肿胀。模型基于van der Waals状态方程（vdW EOS）构建了新的气泡相自由能函数，首次在相场框架中完整考虑了Frenkel对产生、空位-间隙原子复合、裂变诱导气体原子再溶解、晶界和位错吸收等关键缺陷反应过程。

模拟结果表明，晶内气泡可在缺陷产生与湮灭的动态平衡下稳定在纳米尺度（平均约3.2 nm），其尺寸分布和密度（约 $2.4 \times 10^{24}$ m⁻³）与实验观测一致。预测的晶内气泡肿胀在初始快速增加后趋于稳定，体现了燃料的稳定肿胀行为。系统研究了裂变速率、晶粒尺寸和轧制引入位错密度的影响：高裂变速率（$7.0 \times 10^{20}$ m⁻³s⁻¹）导致更大的气泡和更高的肿胀（约5%）；大晶粒（10.7 μm）增加晶内气泡肿胀但减少晶间气泡肿胀；高位错密度（$1.52 \times 10^{15}$ m⁻²）因位错偏压效应增强空位流入气泡而增加肿胀。这些发现为通过燃料制造工艺调控气泡形态和肿胀提供了理论依据。

## Key Equations

### 总自由能泛函
$$F = \int_V \left[ f_{chem} + \sum_{i=X,V,I} \frac{\kappa_i}{2}|\nabla c_i|^2 + \frac{\kappa_g}{2}|\nabla g|^2 + f_{elas} \right] dV$$

其中 $c_X, c_V, c_I$ 分别为Xe、空位、SIA浓度场，$g$ 为相参量（$g=1$气泡相，$g=0$基体相），$f_{chem}$ 为化学自由能密度。

### 基于vdW EOS的气泡自由能
$$f^{bubble} = A \ln(1 - Bc_b) + p_0 c_b$$

其中 $c_b$ 为气泡内Xe浓度，$A, B$ 为常数，$p_0$ 为参考态压力。由van der Waals方程拟合实验数据得到 $B = 23.97 \times 10^{-6}$ m³/mol。

### Frenkel对产生率
$$P_V = P_I = d \cdot \dot{f} \cdot (1-g)$$

其中 $d$ 为常数，$\dot{f}$ 为裂变速率，$(1-g)$ 限制缺陷仅在基体相中产生。

### 气泡演化控制方程（Cahn-Hilliard + Allen-Cahn耦合）
$$\frac{\partial g}{\partial t} = -L_g \frac{\delta F}{\delta g} + \xi_g$$
$$\frac{\partial c_i}{\partial t} = \nabla \cdot \left( M_i \nabla \frac{\delta F}{\delta c_i} \right) + S_i - R_i, \quad i = X, V, I$$

其中 $S_i$ 为源项（缺陷产生），$R_i$ 为汇项（复合、再溶解、晶界/位错吸收），$\xi_g$ 为热涨落。

### 肿胀计算
$$\frac{\Delta V}{V_0} = \frac{V_f - V_0}{V_0}$$

其中 $V_f$ 为包含气泡贡献的最终体积，$V_0$ 为初始体积。

## Physical Mechanisms

### 晶内气泡稳定化机制
辐照下缺陷产生（Frenkel对）与湮灭（复合+汇吸收）的动态平衡使气泡稳定在纳米尺度。裂变诱导再溶解过程不断将小气泡中的气体原子弹射回基体，抑制气泡过度生长。位错偏压（SIA被位错优先吸收）使更多空位流入气泡，促进气泡生长。

### 位错偏压效应
轧制引入的位错作为缺陷汇，对SIA的吸收速率高于空位（因SIA具有更大的弛豫体积）。高位错密度下，SIA浓度快速降低，空位-SIA复合减少，更多空位流向气泡，导致更大的气泡和更高的肿胀。

### 晶粒尺寸效应
晶界作为Xe原子的有效汇，小晶粒中Xe原子扩散到晶界的距离更短，导致晶内Xe浓度降低，晶内气泡尺寸和密度减小。大晶粒有利于将气体保留在晶内，减少晶间气泡肿胀和裂变气体释放。

## Relationships
- [[PhaseFieldModeling]] — 三维相场方法，基于vdW EOS的气泡自由能
- [[GasBubbleSuperlattice]] — 晶内气泡的有序排列结构（本文未直接模拟）
- [[FissionGasDiffusion]] — Xe扩散和再溶解决定气泡生长动力学
- [[FuelAlloy]] — U-7Mo合金体系
- [[SwellingMechanisms]] — 晶内气泡肿胀的稳定化行为
- [[Recrystallization]] — 高燃耗下晶内气泡结构破坏触发再结晶
