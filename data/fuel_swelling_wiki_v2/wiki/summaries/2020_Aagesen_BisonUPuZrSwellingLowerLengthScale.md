# 基于低尺度模拟改进BISON U-Pu-Zr燃料肿胀模型

## Metadata
| Field | Value |
|-------|-------|
| Authors | Larry K. Aagesen, Andrea M. Jokisaari, Jia-Hong Ke |
| Year | 2020 |
| Journal | INL Technical Report (INL/EXT-20-59990) |
| DOI | N/A (INL报告) |

## Overview

本文报告了爱达荷国家实验室（INL）在FY20期间利用低尺度模拟方法改进BISON燃料性能程序中U-Pu-Zr金属燃料肿胀模型的工作。研究涵盖三个尺度层次：

**高温区γ相气体肿胀与互连（相场模拟）**：采用Cahn-Hilliard方程模拟裂变气体气泡的生长与互连过程，在72 μm³计算域中系统研究了缺陷迁移率M和气泡数密度N对渗透阈值的影响。通过五组不同初始构型的统计分析，确定了两个BISON肿胀模型的关键参数：对UPuZrGaseousEigenstrain模型，互连起始孔隙率$p_i = 0.262$，终止孔隙率$p_t = 0.279$；对ADFissionGasViscoplasticityStressUpdateBase模型，起始孔隙率$p_{start} = 0.2026$，终止孔隙率$p_{end} = 0.3219$。

**低温区α相孔隙演化（晶体塑性有限元）**：利用MARMOT程序中的晶体塑性模型，模拟了含孔隙多晶α-铀在辐照和塑性变形下的孔隙演化。研究表明，辐照诱导的晶体生长本征应变是孔隙体积增大和形状各向异性化的主要驱动力，而塑性变形对孔隙体积和几何形状影响很小。

**Xe团簇早期成核（团簇动力学）**：基于Xolotl代码建立了Xe团簇与空位团簇耦合的团簇动力学模型，在1000 K下模拟了Xe气泡的早期成核与生长过程。敏感性分析表明，Xe溶解度、Xe团簇界面能和空位迁移势垒是影响Xe团簇演化的关键参数。

## Key Equations

### 气泡体积分数与肿胀（UPuZrGaseousEigenstrain模型）

$$\Delta V / V = \frac{kT}{\sigma} Y_{Xe} \dot{F} t / N$$

其中$k$为玻尔兹曼常数，$T$为温度（K），$\sigma$为燃料-气泡界面表面张力，$Y_{Xe}$为气态裂变产物产额，$\dot{F}$为裂变率密度，$t$为时间，$N$为气泡数密度。

### 互连分数拟合函数

$$f_V = \frac{1}{2}\left[1 + \text{erf}\left(\frac{p - p_{cen}}{\sqrt{2}\Delta}\right)\right]$$

其中$p$为局部孔隙率，$p_{cen}$为分布中心，$\Delta$为特征宽度。该函数描述了连通到自由表面的气泡体积分数随孔隙率的变化。

### 互连函数（BISON平滑阶跃函数）

$$I(p) = 1 - 6x^5 + 15x^4 - 10x^3, \quad x = \frac{p - p_{start}}{p_{end} - p_{start}}$$

该三阶Hermite插值函数用于在BISON中控制肿胀终止和气体释放开始。

### 辐照生长本征应变（α-铀）

$$\varepsilon^\beta = \frac{\partial \varepsilon^\beta}{\partial \beta} \cdot \beta$$

其中$\beta$为燃耗（FIMA），生长系数$G_{[100]} = -420$，$G_{[010]} = 420$，$G_{[001]} = 0$（423 K下）。单晶沿[100]收缩、[010]生长、[001]不变。

### Xe团簇主方程

$$\frac{df_n}{dt} = J_{p \to n} - J_{n \to q}$$

$$J_{p \to n} = \omega^+_{p,n} f_p - \omega^-_{n,p} f_n$$

其中$f_n$为尺寸$n$的Xe团簇数密度，$\omega^+$和$\omega^-$分别为吸附和发射反应速率系数。

### 团簇自由能

$$G_n = n \mu_d + 4\pi r_n^2 \sigma$$

其中$\mu_d$为团簇相化学势，$\sigma$为界面能，第一项为体贡献，第二项为界面贡献。

## Physical Mechanisms

### 高温γ相气体肿胀
- 裂变气体（Xe）在γ相中溶解度极低，快速形核形成气泡
- 气泡为球形，直径可达数十微米
- 气泡生长至互连后释放气体，肿胀终止
- 互连过程可用渗透理论描述，渗透阈值$p_c \approx 0.26$

### 低温α相肿胀
- α-铀单晶在辐照下发生各向异性生长（[100]收缩、[010]伸长）
- 晶体生长产生的本征应变导致孔隙体积增大和各向异性拉长
- 塑性变形不是孔隙演化的主要驱动力
- 孔隙呈拉长状，边缘不规则

### Xe团簇早期演化
- Xe单原子通过空位辅助机制扩散至团簇
- 空位浓度非平衡态由辐照产生、位错阱和复合过程共同决定
- Xe团簇数密度在$\sim 5 \times 10^4$ s后饱和，平均半径持续增长至7-8 nm（$10^6$ s）
- 团簇粗化现象不明显，因裂变持续提供Xe原子源

## Relationships

- [[FuelAlloy]] — U-Pu-Zr合金体系，γ相（BCC）高温区、α相（正交）低温区
- [[CavitationalVoid]] — 高温气泡互连与低温孔隙形成机制
- [[GasBubbleSuperlattice]] — Xe气泡在γ相中的分布
- [[FissionGasDiffusion]] — Xe通过空位辅助机制扩散
- [[PhaseFieldModeling]] — 相场模拟气泡生长与互连
- [[RateTheory]] — 团簇动力学作为速率理论的延伸
- [[SwellingMechanisms]] — 高温气体肿胀vs低温辐照生长驱动肿胀
- [[Recrystallization]] — 温度相关的相变对肿胀行为的影响
