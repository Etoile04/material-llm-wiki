# UN燃料裂变气体释放与肿胀的动力学速率理论建模

## Metadata
| Field | Value |
|-------|-------|
| Authors | Zhengyu Qian, Wenbo Liu, Rui Yu, Yujie Tao, Di Yun, Long Gu |
| Year | 2021 |
| Journal | Journal of Nuclear Materials |
| DOI | 10.1016/j.jnucmat.2021.153088 |

## Overview

本文基于经典动力学速率理论框架，建立了氮化铀（UN）燃料裂变气体行为和肿胀的力学模型。模型基于GRASS-SST和FASTGRASS代码框架，采用气泡尺寸分组方法，通过一组耦合的非线性微分方程描述燃料中不同位置（晶内、晶面、位错、晶棱）的裂变气体原子和气泡浓度演化。

通过日本JOYO实验堆的辐照数据对模型进行了验证。主要贡献包括：（1）提出了适合UN燃料模拟的新Xe扩散系数 $D_g = 4.05 \times 10^{-3}\exp(-2.15 \times 10^5 / RT)$ cm²/s；（2）确定UN燃料的形核因子 $F_N = 10^{-4}$ 和再溶解常数 $b_0 = 10^{-18}$ cm³；（3）揭示了再溶解效应是气泡尺寸双峰分布的主要驱动力。

模型预测的燃料肿胀为7.19%，裂变气体释放率为5.28%，晶内气体保留比例为80.5%，与实验数据（6.7%、5.2%、80%）吻合良好。研究表明再溶解使小尺寸气泡增多、中尺寸气泡减少、大尺寸气泡先增后减，导致双峰分布的形成。

## Key Equations

### 气泡尺寸分组
$$N_i = m \cdot N_{i-1}$$

$N_i$ 为第$i$组气泡中的气体原子数，$m=2$ 为倍增因子（即每级包含 $2^i$ 个气体原子）。

### 晶内气体原子浓度演化
$$\frac{dC_g}{dt} = -F_N C_g^2 + \text{capture terms} - g_o(t) - \text{sweeping} + \eta \dot{f} + \sum_{i=1}^{I} b_i C_{f,i}$$

各项分别代表形核损失、气泡捕获损失、向晶界扩散、晶界扫过、裂变产生、以及从气泡的再溶解。

### 气泡再溶解强度
$$b_i = \frac{b_0 \dot{f}}{(R_i + \delta)(R_i + d)}$$

$b_0$ 为再溶解常数，$d$ = 1 nm 为允许气体原子逃逸的表面层厚度，$\delta$ = 0.4 nm 为再溶解原子返回气泡的扩散层厚度。

### 裂变气体释放率
$$FGR = \frac{1}{N_{total}}\left(P_A N_{gf} \text{vent} + P_I \text{edge vent} + \text{long-range}\right)$$

### 燃料肿胀
$$S = \frac{4\pi}{3}\left(\sum_i C_{f,i} R_i^3 + \sum_i C_{e,i} R_i^3 + C_g R_g^3\right)$$

### 气泡半径（van der Waals模型）
由 $P(4\pi R^2 - BN_i) = N_i k_B T$ 和 $P = 2\gamma/R + P_h$ 联立求解，其中 $B = 8.5 \times 10^{-32}$ m³，$\gamma = 10$ N/m，$P_h = 10^7$ N/m²。

## Physical Mechanisms

1. **气泡尺寸分组法**：将气泡按包含的气体原子数分组（2的幂次），避免单一平均气泡尺寸的简化
2. **再溶解驱动的双峰分布**：再溶解使小气泡增多（新形核）、中气泡减少、大气泡因弱再溶解效应而增长
3. **扩散系数与肿胀的耦合**：增大扩散系数同时减少晶内气体（降低肿胀）和增加气泡合并概率（增大肿胀），两种效应相互抵消
4. **晶内气体高保留率**：UN燃料中80%的裂变气体保留在晶内，仅5%释放，15%在晶界

## Relationships
- [[RateTheory]] — 动力学速率理论框架
- [[RateTheoryFramework]] — 速率方程的数学框架
- [[FissionGasDiffusion]] — Xe气体在UN中的扩散
- [[SwellingMechanisms]] — 裂变气体驱动的燃料肿胀
- [[FuelAlloy]] — UN氮化物燃料体系
