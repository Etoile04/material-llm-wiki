# U-Mo合金燃料的裂变产物诱导肿胀

## Metadata
| Field | Value |
|-------|-------|
| Authors | Y.S. Kim, G.L. Hofman |
| Year | 2011 |
| Journal | Journal of Nuclear Materials |
| DOI | 10.1016/j.jnucmat.2011.08.022 |

## Overview

本文基于RERTR项目辐照数据（裂变密度达$7 \times 10^{27}$ fissions/m³），建立了U-Mo合金燃料的总肿胀、裂变气体气泡肿胀和固体裂变产物肿胀的经验关联式。通过单层燃料板的厚度变化测量总肿胀，通过SEM断口图像分析量化气泡体积分数，最后通过差值获得固体裂变产物肿胀。

核心发现是：在低温（<250°C）下，U-Mo燃料肿胀几乎与温度无关（athermal），主要由裂变密度决定。总肿胀由两步模型描述：低裂变密度时以固体裂变产物肿胀为主（线性关系），当裂变密度超过$\sim 3 \times 10^{27}$ fissions/m³时，晶粒细化（重结晶）导致气泡肿胀加速。

_atomized powder（雾化粉末）与machined powder（机加工粉末）的肿胀行为不同：机加工粉末因更高的位错密度而在更低燃耗时发生晶粒细化，导致更高的气泡肿胀。γ相退火粉末由于晶粒较大、晶界较少，气泡肿胀明显更低。

## Key Equations

### 单层板燃料肿胀计算
$$(\Delta V/V_0)_f = \Delta t_f / t_f$$

$\Delta t_f$ 为辐照后燃料箔厚度变化，$t_f$ 为原始厚度。

### 总肿胀经验关联（低裂变密度，<3×10²⁷ f/m³）
$$(\Delta V/V_0)_f = 3.3 + 2.7(f_d - 3)$$

### 总肿胀经验关联（高裂变密度，≥3×10²⁷ f/m³）
$$(\Delta V/V_0)_f = 17.5 + 5.2(f_d - 3)$$

$f_d$ 为裂变密度，单位 $10^{27}$ fissions/m³，肿胀单位%。

### 固体裂变产物肿胀
$$(\Delta V/V_0)_s = 3.3 f_d$$

### 气泡肿胀（低裂变密度）
$$(\Delta V/V_0)_g = 0 \quad (f_d < 3)$$

### 气泡肿胀（高裂变密度）
$$(\Delta V/V_0)_g = 14.2(f_d - 3)$$

### 气泡体积分数
$$v_b = \frac{\pi}{4} x_0^2 q_{CS}$$

$x_0$ 为平均气泡尺寸，$q_{CS}$ 为单位截面积气泡数密度。

### Fick方程（Mo均匀化模型）
$$\frac{\partial C_{Mo}}{\partial t} = D \frac{\partial^2 C_{Mo}}{\partial x^2}$$

$D = \frac{1}{12}\dot{f}_r V^{5/3}$，$V = 2.01 \times 10^{-24}$ m³。

## Physical Mechanisms

1. **两步肿胀模型**：低燃耗线性肿胀（固体裂变产物）→ 高燃耗加速肿胀（气泡生长 + 晶粒细化）
2. **晶粒细化阈值**：裂变密度 $2.5\text{--}3.5 \times 10^{27}$ f/m³，以$3 \times 10^{27}$为代表值
3. **Athermal肿胀**：低温下气体原子扩散依赖裂变增强扩散而非热激活扩散
4. **粉末类型效应**：机加工粉末位错密度更高→更早晶粒细化→更高气泡肿胀
5. **晶界Mo偏析**：雾化粉末的晶界Mo含量低于晶内，促进气泡形核

## Relationships
- [[SwellingMechanisms]] — 两步肿胀模型
- [[Recrystallization]] — 晶粒细化驱动的肿胀转变
- [[FuelAlloy]] — U-Mo合金（7-10 wt% Mo）
- [[FissionGasDiffusion]] — 裂变增强扩散
- [[CavitationalVoid]] — 气泡肿胀贡献
