# Characterization of Intergranular Fission Gas Bubbles in U-Mo Fuel

## Metadata

| 字段 | 值 |
|------|-----|
| 作者 | Y.S. Kim, G.L. Hofman, J. Rest |
| 年份 | 2008 |
| 机构 | Argonne National Laboratory (ANL) |
| 报告编号 | ANL-08/11 |
| DOI | 10.2172/929261 |
| 合金体系 | U-Mo (U-6Mo, U-7Mo, U-10Mo) |
| 燃料类型 | 弥散燃料 (dispersion fuel) / 单体燃料 (monolithic fuel) |
| 辐照实验 | RERTR-1, 2, 3, 5 |

## Physical Mechanisms

### 1. 晶间裂变气体气泡的形成与演化

U-Mo 合金燃料在辐照下裂变气体肿胀动力学呈现两个不同阶段：
- **预转变阶段 (pre-transition)**: 燃耗 < ~40 at% U-235 (LEU) 或裂变密度 < ~3×10²¹ fissions/cm³，气泡仅在晶界 (grain boundaries) 上出现
- **后转变阶段**: 气泡扩展到晶内区域，最终均匀分布于整个燃料截面

转变对应于 γ-U-Mo 的晶粒细化 (grain refinement/recrystallization) 现象。

### 2. 三种气泡类型（高燃耗时）

- **体气泡 (Bulk bubbles)**: 位于燃料颗粒内部，尺寸小，均匀分布
- **交叉气泡 (Intersection bubbles)**: 位于相邻燃料颗粒接触面，尺寸较大
- **边缘气泡 (Peripheral pores)**: 位于燃料颗粒边缘，尺寸大且不均匀分布，高燃耗时倾向于聚合成大规模气孔

### 3. 晶界作为气泡优先成核位置

- 雾化 U-Mo 粉末具有"胞状"凝固组织 (cellular solidification structure)
- 晶界区域 Mo 含量较低（~17 at%），晶粒内部较高（~22 at%）
- 低 Mo 含量区域更有利于气泡成核
- 通过扩散模型分析，辐照结束时的 Mo 浓度差异仍然存在（~2.5 at%），未完全均匀化

### 4. 晶界扩散增强机制

- 晶界处的气体原子扩散增强因子 ξ = 7×10³
- 此增强因子使得晶界成为气体原子的强汇 (strong sink)
- 晶界气泡成核率低于晶内

### 5. Sputtering Coalescence 机制

- 晶间气泡合并通过辐照诱发溅射聚并 (sputtering coalescence) 实现，无需气泡迁移
- 裂变碎片将气泡间材料中的原子击出，导致气泡逐渐合并
- 净原子流出速率与气泡体积分数相关

## Key Equations

### Mo 浓度均匀化 (Fick 扩散方程)

$$D = \frac{1}{3} f_r V$$

其中 $f_r$ 为裂变速率，$V$ 为裂变尖峰影响体积 (2.01×10⁻¹⁸ cm³)

### 晶界气泡密度转换（TKDH 模型）

晶粒建模为 Tetrakaidecahedron (TKDH)：

- 截面气泡密度：$\rho_{CS} = \frac{2(1+\sqrt{2})}{7} \cdot \frac{6}{d} \cdot \rho_L$ (Eq. 9)
- 表面气泡密度：$\rho_S = \frac{2}{\sqrt{3}} \cdot (\rho'_L)^2$ (Eq. 14)
- 测量修正因子：$\rho'_L = 1.32 \rho_L$ (截面测量值比真实值低约32%)

### 体积气泡密度

$$\rho_V = \frac{9(1+\sqrt{2/3})}{8d} \cdot \rho_S$$

### 气泡体积分数

$$v_b = \frac{4}{3}\pi x_0^3 \cdot \rho_V$$

或

$$v_b = \frac{\pi}{4} x_0^2 \cdot \rho_{CS}$$

### 总肿胀

$$\left(\frac{\Delta V}{V_0}\right)_{total} = 6 \times 10^{-21} F_d$$

其中 $F_d$ 为裂变密度 (fissions/cm³)

### 机理模型核心方程

- **气体原子扩散系数**: $D_g = D_0 \dot{f}$ (Eq. 29)
- **再溶解速率**: $b = b_0 \dot{f}$ (Eq. 30)
- **晶内气泡密度稳态解**: $c_b^0 = \frac{f_n c_g}{16 \pi D_g r_b^0}$ (Eq. 34)
- **晶界气泡浓度 (Wood-Kear)**: $C_b = 8\pi \left(\frac{z a K}{12 D_g \xi \delta}\right)^{2/3}$ (Eq. 40)
- **肿胀分数**: $\frac{\Delta V}{V} = \frac{4\pi r_b^3 c_b}{3} + \frac{4\pi R_b^3 C_b}{3} \cdot \frac{6}{d_g} + \frac{a^3 c_g}{d_g}$ (Eq. 47)

## Parameters

### 辐照条件范围

| 参数 | 范围 |
|------|------|
| 辐照温度 | 66–191°C |
| 裂变速率 | 2.3–7.0 × 10¹⁴ f/cm³·s |
| 燃耗 | 30–49 at% U-235 |
| 裂变密度 | ~2.0–3.1 × 10²¹ f/cm³ |
| 辐照时长 | 48–116 天 |

### 材料参数

| 参数 | 值 |
|------|-----|
| 晶粒尺寸 (as-atomized) | 2–8 μm |
| 晶粒尺寸 (γ-annealed) | 10–24 μm |
| 晶界宽度 | ~0.5 μm |
| 晶界 Mo 含量 | ~17 at% |
| 晶粒内部 Mo 含量 | ~22 at% |
| 晶界扩散增强因子 ξ | 7×10³ |
| 气泡成核因子 $f_n$ | ~10⁻⁴ (vacancy concentration) |

### 关键数据点

| 参数 | 典型值 |
|------|--------|
| 平均气泡直径 | 0.09–0.18 μm |
| 气泡密度/晶界长度 ρ_L | 1.18–1.96 × 10⁴ cm⁻¹ |
| 气泡密度/截面面积 ρ_CS | 0.17–0.92 × 10⁸ cm⁻² |
| 气泡密度/晶粒表面 ρ_S | 5.0–13.6 × 10⁸ cm⁻² |
| 气泡体积分数 v_b | 0.1–3.2% |

## Experimental Data

### 13 个测试板的完整实验数据

| Plate ID | 燃料 | 制备方式 | 燃耗 (at%U-235) | 裂变速率 (10¹⁴) | 温度 (°C) | 平均气泡径 (μm) | ρ_L (10⁴ cm⁻¹) | 晶粒尺寸 (μm) | v_b (%) |
|----------|------|---------|-----------------|-----------------|-----------|----------------|----------------|-------------|---------|
| Z03 | U-10Mo | atomized, γ-annealed | 32 | 5.3 | 121 | 0.09 | 1.96 | 23.6 | 0.1 |
| Y01 | U-10Mo | machined, γ-annealed | 30 | 4.8 | 109 | 0.09 | 1.79 | 10.1 | 0.2 |
| V002 | U-10Mo | atomized | 39 | 3.8 | 66 | 0.15 | 1.30 | 4.9 | 1.0 |
| A003 | U-10Mo | machined | 40 | 3.8 | 68 | 0.18 | 1.41 | 3.2 | 2.3 |
| V07 | U-10Mo | atomized | 30 | 5.1 | 122 | 0.13 | 1.34 | 6.5 | 0.6 |
| V03 | U-10Mo | atomized | 38 | 6.3 | 149 | 0.16 | 1.36 | 7.3 | 0.8 |
| S03 | U-6Mo | atomized | 39 | 7.0 | 158 | 0.18 | 1.18 | 3.6 | 1.7 |
| A6008H | U-10Mo | atomized | 49 | 3.1 | 177 | 0.17 | 1.43 | 5.3 | 1.3 |
| R6007F | U-7Mo | atomized | 37 | 2.4 | 185 | 0.16 | 1.39 | 6.2 | 0.9 |
| V6019G | U-10Mo | atomized | 49 | 2.9 | 142 | 0.16 | 1.36 | 7.6 | 0.7 |
| V6018G | U-10Mo | atomized | 35 | 2.3 | 121 | 0.14 | 1.32 | 5.2 | 0.8 |
| V8005B | U-10Mo | atomized | 37 | 2.4 | 170 | 0.16 | 1.37 | 8.1 | 0.7 |
| A8002L | U-10Mo | machined | 48 | 2.9 | 191 | 0.18 | 1.35 | 3.9 | 1.8 |

### 气泡尺寸分布特征

- 所有测试板的气泡尺寸分布呈**准正态分布 (quasi-normal)**
- 气泡按尺寸分为 7 组进行统计
- 测量不确定性：气泡尺寸 ±10%，端部 bins ±50%，中间 bins ±10%

## Key Findings

### 1. 晶界是气泡优先成核位置

SEM 观察明确证实，在预转变阶段（燃耗 < ~40 at% U-235），所有可观察的气泡均位于晶界。晶内气泡仅在 TEM 分辨率下（~0.002 μm）可见，远小于 SEM 分辨率（~0.02 μm）。

### 2. γ 退火显著影响气泡行为

- γ 退火（800°C, 70-100 小时）消除了胞状结构，晶粒显著长大（2 μm → 10-24 μm）
- 退火板的气泡尺寸更小（0.09 μm vs 0.14-0.18 μm）
- 退火板的单位晶界长度气泡密度更高
- 晶界扩散增强因子对退火板约为 as-fabricated 板的 1/6

### 3. 气泡密度与燃耗无关

在预转变阶段，单位晶界长度的气泡密度 (ρ_L) 基本不随裂变密度变化，表明气泡成核在早期即达到饱和。

### 4. 气泡体积分数随燃耗增加

在裂变密度 3×10²¹ f/cm³ 时，气泡体积分数达到 ~2%。但这远小于总肿胀量，说明大量裂变气体仍以原子溶解态或 SEM 不可分辨的小气泡形式存在。

### 5. 晶间气泡肿胀贡献很小

在预转变阶段，晶间裂变气体气泡对总肿胀的贡献很小（~2%），远小于固体裂变产物肿胀。这意味着大部分裂变气体仍在原子固溶体中或纳米级气泡中。

### 6. TKDH 模型验证成功

Tetrakaidecahedron 晶粒模型计算的晶界长度与直接测量值吻合良好，验证了该模型的适用性。

### 7. 机理模型与实验一致

基于解析解的晶间气泡形成动力学模型计算的气泡尺寸分布与测量分布一致，但模型对气体原子扩散系数和再溶解率等参数敏感。

## Relationships to Other Work

### 关联文献

- **Bleiberg [4,5]**: α+γ' → γ 相反转分析，用于推导 Mo 浓度均匀化模型
- **Speight [11]**: 扩散到晶界的气体分数近似公式 (Eq. 38)
- **Wood & Kear [12]**: 晶界气泡成核机制
- **比利时 TEM 研究 [6]**: 证实晶内 ~0.002 μm 气泡均匀存在

### 与肿胀模型的关系

- 本报告的预转变阶段数据为建立机理肿胀模型提供了基础
- 转变点 (~3×10²¹ f/cm³) 后的现象涉及再结晶，需要更复杂的模型
- 边缘大气孔形成是潜在的性能限制因素

### 对后续工作的意义

1. 为 U-Mo 燃料性能评估提供了关键的预转变气泡数据
2. 确定了关键材料参数（扩散系数、再溶解率）需要更精确的测量
3. 晶界扩散增强因子 ξ = 7×10³ 可作为后续模型校验基准
4. 气泡体积分数的多种计算方法（ρ_S, ρ_CS, 直接测量）提供了交叉验证手段

---

*数据来源: Kim et al., ANL-08/11, 2008. DOI: 10.2172/929261*

## Relationships

- [[wiki/entities/FuelAlloy|FuelAlloy]] — U-Mo (U-6Mo, U-7Mo, U-10Mo) alloy fuel is the subject; grain boundary composition and structure are central
- [[wiki/entities/FissionGasDiffusion|FissionGasDiffusion]] — grain boundary diffusion enhancement factor ξ = 7×10³ and gas atom diffusion kinetics are key findings
- [[wiki/entities/Recrystallization|Recrystallization]] — grain refinement transition at ~3×10²¹ f/cm³ triggers intragranular bubble formation post-transition
- [[wiki/concepts/SwellingMechanisms|SwellingMechanisms]] — pre-transition intergranular bubble swelling is quantified as a small but important contribution
- [[wiki/summaries/2005_Rest_RecrystallizationSwellingUO2UMo|2005_Rest_RecrystallizationSwellingUO2UMo]] — Rest's recrystallization-swelling model is complementary
- [[wiki/summaries/2011_Kim_FissionProductInducedSwellingUMo|2011_Kim_FissionProductInducedSwellingUMo]] — Kim (2011) builds directly on these RERTR data to construct empirical swelling correlations
