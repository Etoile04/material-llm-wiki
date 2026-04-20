# U-Mo单体燃料肿胀：研究堆条件下预测性肿胀关联式的建立

## Metadata
| Field | Value |
|-------|-------|
| Authors | A.B. Robinson, W.J. Williams, W.A. Hanson, B.H. Rabin, N.J. Lybeck, M.K. Meyer |
| Year | 2021 |
| Journal | Journal of Nuclear Materials |
| DOI | 10.1016/j.jnucmat.2020.152793 |
| Affiliation | Idaho National Laboratory (INL) |

## Overview

本文基于美国先进试验堆（ATR）中7项U-10Mo单体燃料辐照实验（AFIP-3/4/6MkII/7、RERTR-9/10/12），对74块燃料板的超过18,000个局部厚度数据点进行统计分析，建立了一个预测性肿胀关联式。研究采用辐照后轮廓测量法获取局部燃料板厚度变化，通过数据分箱（binning）降低散布、揭示内在肿胀趋势。

文章系统比较了四种拟合方法（线性、分段线性、二次、三次函数），最终推荐二次函数作为肿胀关联式：

$$\left(\frac{\Delta V}{V}\right)_f = 7.12 \times 10^{-42} \cdot f_d^2 + 2.58 \times 10^{-21} \cdot f_d$$

其中$f_d$为裂变密度（fissions/cm³）。分段线性模型虽R²最高，但拐点位置不稳定，且重结晶驱动的固相→气相裂变产物主导肿胀转变是渐进过程而非突变，因此不予推荐。二次模型同时提供了95%置信区间和预测区间，分别适用于反应堆安全分析和实验数据比较。

文章验证表明，该关联式与RERTR-12浸没密度法测得的板平均肿胀数据吻合良好。U-10Mo单体燃料在LEU设计可达裂变密度（~7.8×10²¹ fissions/cm³）范围内未出现失控肿胀（breakaway swelling）迹象。

## Key Equations

### 推荐肿胀关联式（Eq. 17）
$$\left(\frac{\Delta V}{V}\right)_f = 7.12 \times 10^{-42} \cdot f_d^2 + 2.58 \times 10^{-21} \cdot f_d$$

- $\left(\frac{\Delta V}{V}\right)_f$：总体积肿胀率（%）
- $f_d$：局部裂变密度（fissions/cm³）
- 物理含义：二次项捕捉气相裂变产物肿胀（重结晶后），线性项捕捉固相裂变产物肿胀

### 95%置信区间（Eq. 18-19，分箱数据）
$$\text{Upper} = 7.12 \times 10^{-42} \cdot f_d^2 + 2.58 \times 10^{-21} \cdot f_d + 1.52$$
$$\text{Lower} = 7.12 \times 10^{-42} \cdot f_d^2 + 2.58 \times 10^{-21} \cdot f_d - 1.52$$

### 体积肿胀定义（Eq. 1）
$$\left(\frac{\Delta V}{V}\right)_f = \frac{\Delta t_f}{t_{f0}} \times 100$$

- $\Delta t_f$：辐照后燃料厚度变化
- $t_{f0}$：制造态燃料厚度

### 局部燃料肿胀计算（Eq. 16）
$$\left(\frac{\Delta V}{V}\right)_f = \frac{(t_p - t_{ox}) - t_{p0}}{t_f - t_{Zr}} \times 100$$

- $t_p$：辐照后局部总板厚；$t_{ox}$：局部氧化层厚度；$t_{p0}$：辐照前局部板厚
- $t_f$：初始燃料箔厚度；$t_{Zr}$：名义Zr扩散层厚度

### Kim-Hofman肿胀模型（Eq. 11-12，对比用）
$$\left(\frac{\Delta V}{V}\right)_f = 1.2 \cdot f_d \quad (f_d < 3.0 \times 10^{21})$$
$$\left(\frac{\Delta V}{V}\right)_f = 3.6 + 0.8(f_d - 3.0) \quad (f_d \geq 3.0 \times 10^{21})$$

### Rest模型——固相裂变产物肿胀（Eq. 8）
$$\left(\frac{\Delta V}{V}\right)_s = -0.33 + 3.84 \times 10^{-21} \cdot f_d$$

### Rest模型——气相裂变产物肿胀（Eq. 9-10）
$$\left(\frac{\Delta V}{V}\right)_g = 0 \quad (f_d \leq 3 \times 10^{21})$$
$$\left(\frac{\Delta V}{V}\right)_g = -12.7 + 4.5 \times 10^{-21} \cdot f_d \quad (f_d > 3 \times 10^{21})$$

## Physical Mechanisms

### 肿胀机制分区
1. **低裂变密度区（$f_d < 2.5 \times 10^{21}$ fissions/cm³）**：固相裂变产物主导肿胀，速率约2-4% per 10²¹ fissions/cm³，线性增长，基本不依赖温度
2. **过渡区（$2.5-3.5 \times 10^{21}$ fissions/cm³）**：辐照诱发重结晶（grain refinement/subdivision）导致纳米气泡超晶格坍塌，气体迁移至新亚微米晶界，气相肿胀逐渐占主导
3. **高裂变密度区（$f_d > 3.5 \times 10^{21}$ fissions/cm³）**：微米级气泡生长，肿胀加速，非线性增长

### 裂变气体气泡超晶格（Fission Gas Bubble Superlattice）
- Xe和Kr在γ-U-Mo晶格上形成面心立方超晶格纳米气泡
- 气泡直径2-3 nm，晶格参数11-12 nm
- 稳定至$f_d \approx 3 \times 10^{21}$ fissions/cm³

### 约束条件下的肿胀行为
- 铝包壳的侧向和纵向约束将肿胀限制在板厚方向
- 辐照辅助蠕变导致燃料重定位，边缘约束区出现零厚度增长区

## Relationships

- [[SwellingMechanisms]] — 固相与气相裂变产物肿胀机制
- [[FissionGasBubble]] — 裂变气体气泡形核与生长
- [[GasBubbleSuperlattice]] — 纳米气泡超晶格结构
- [[Recrystallization]] — 辐照诱发重结晶/晶粒细化
- [[UMoMonolithicFuel]] — U-10Mo单体燃料设计
- [[IrradiationAssistedCreep]] — 辐照辅助蠕变与燃料重定位
- [[BreakawaySwelling]] — 失控肿胀行为
- [[FuelPerformanceCode]] — 燃料性能分析中的肿胀模型输入
