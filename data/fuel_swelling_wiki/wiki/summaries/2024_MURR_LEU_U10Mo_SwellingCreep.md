# 2024_MURR_LEU_U10Mo_SwellingCreep

**论文**: Fuel Swelling and Creep Analysis for a MURR LEU U-10Mo Monolithic Plate
**作者**: Walid Mohamed, Hee Seok Roh, John Stillman, Erik Wilson (Argonne National Laboratory)
**来源**: ANL/RTR/TM-18/19, March 2019

## 摘要

本研究采用有限元方法（ABAQUS）分析了密苏里大学研究堆（MURR）低浓铀U-10Mo单片燃料板（plate 23）在辐照条件下的热力学行为。研究重点评估了燃料板厚度方向的肿胀和蠕变引起的最大厚度增量，以确保冷却剂通道在寿期末（EOL）仍有足够间隙用于热移除。

研究采用三种燃料肿胀关联式：Kim肿胀关联式、排除AFIP-6 MKII数据的肿胀关联式、以及包含AFIP-6 MKII数据的95%上置信限（UCL）关联式，分别配合四个蠕变速率系数（750、500、250、5 × 10⁻²⁵ cm³/MPa-fission）进行组合分析。结果表明：蠕变速率系数在250-750范围内变化对净板厚增量影响不显著；最大板厚增量为0.083 mm（95% UCL关联式+蠕变系数250-750）；所有工况下燃料芯体的等效应力均低于屈服应力（805 MPa@150°C），未发生塑性变形。plate 23最大裂变密度为2.62×10²⁷ fissions/m³，辐照时间2873小时。

## Key Equations

### 1. Kim 肿胀关联式（分段线性）

$$\Delta V/V(\%) = 5.0 \cdot fd \quad (fd \leq 3 \times 10^{27} \text{ fissions/m}^3)$$

$$\Delta V/V(\%) = 15.0 + 6.3 \cdot (fd - 3) \quad (fd > 3 \times 10^{27} \text{ fissions/m}^3)$$

- $\Delta V/V$：总体积肿胀百分比
- $fd$：裂变密度（× 10²⁷ fissions/m³）
- 基于 RERTR-6 至 RERTR-9 辐照数据拟合

### 2. 排除 AFIP-6 MKII 肿胀关联式

$$\Delta V/V(\%) = -0.80 + 6.09 \cdot fd - 0.71 \cdot fd^2$$

- $fd$：裂变密度（× 10²⁷ fissions/m³）
- 基于 18,675 个局部厚度测量数据（排除 AFIP-6 MKII）

### 3. 95% UCL 肿胀关联式（含 AFIP-6 MKII）

$$\Delta V/V(\%) = -1.25 + 7.13 \cdot fd - 0.68 \cdot fd^2$$

- 最保守估计，代表极端工况

### 4. 辐照蠕变模型

$$\dot{\varepsilon}_{cr} = A \cdot \sigma \cdot \dot{f}$$

- $\dot{\varepsilon}_{cr}$：蠕变应变速率（1/s）
- $A$：辐照蠕变速率系数（cm³/MPa-fission）
- $\sigma$：等效应力（MPa）
- $\dot{f}$：裂变密度率（fissions/cm³·s）
- Kim et al. 确定 $A = 500 \times 10^{-25}$ cm³/MPa-fission

## 关键结果

| 肿胀关联式 | EOL肿胀应变(FEA) | 最大板厚增量(mm) |
|---|---|---|
| Kim | 13.1% | 0.051 |
| 排除AFIP-6 MKII | 14.5% | 0.055 |
| 95% UCL含AFIP-6 MKII | 20.7% | 0.083 |
