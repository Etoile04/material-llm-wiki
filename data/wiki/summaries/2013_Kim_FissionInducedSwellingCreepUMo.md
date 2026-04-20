# Metadata

- **Title**: Fission induced swelling and creep of U–Mo alloy fuel
- **Authors**: Yeon Soo Kim, G.L. Hofman, J.S. Cheon, A.B. Robinson, D.M. Wachs
- **Year**: 2013
- **Journal**: Journal of Nuclear Materials 437, 37–46
- **DOI**: 10.1016/j.jnucmat.2013.01.346
- **Institutions**: Argonne National Laboratory (USA), KAERI (Korea), Idaho National Laboratory (USA)

---

# Physical Mechanisms

## 1. 肿胀机制 (Swelling Mechanisms)

U–Mo 合金燃料的肿胀由两部分组成：

- **固态裂变产物引起的肿胀** (solid fission product swelling)：裂变产物原子积累导致体积增加
- **裂变气体气泡引起的肿胀** (fission gas bubble swelling)：裂变气体（Xe, Kr）聚集形成气泡

在研究堆中，辐照温度通常低于 250°C，此时：
- 裂变气体扩散主要由 **裂变增强扩散 (Fission Enhanced Diffusion, FED)** 主导
- 热激活气体扩散量很小
- 亚稳态 γ 相分解为 α + γ' 相的过程非常缓慢，裂变诱导扩散有效逆转 α + γ' → γ 相
- γ 相的气泡尺寸小，温度对肿胀的影响被测量不确定性掩盖

## 2. 裂变诱导蠕变机制 (Fission-Induced Creep)

- 裂变诱导蠕变是 **athermal**（非热激活）的
- 蠕变速率与裂变率和外加应力 **线性相关**
- 不同于热蠕变（应力指数 3–4），裂变诱导蠕变的应力指数为 1
- 驱动力：裂变产物引起的肿胀在燃料端部产生 **剪切应力 (shear stress)**，导致燃料质量沿宽度方向向中心转移

## 3. 质量转移机制 (Lateral Mass Transfer)

- 燃料箔端部被包壳封堵，肿胀产生的应力驱动燃料体积向低应力区（宽度中心）转移
- 燃料流动在箔厚度中心线处最大，在箔-包壳界面处最小（假设完美结合）
- 这种质量转移使得端部区域（裂变密度最高处）的实际测量肿胀低于预期值
- 这一机制使得 U–Mo 燃料能够达到高燃耗而不发生失效

## 4. 孔隙率效应

- 高燃耗下裂变气体孔隙率可超过 10%
- 孔隙率增强热蠕变速率（UO₂ 中 12% 孔隙率增加约 12% 蠕变速率）
- 对裂变诱导蠕变的影响较小（因为应力指数为 1，而非 3–4）

---

# Key Equations

## 肿胀公式

**燃料体积变化**（式 1）：
$$\left(\frac{\Delta V}{V_0}\right)_f = \frac{\Delta t_f}{t_f^0}$$

其中 Δt_f 为辐照后箔厚度变化，t_f^0 为原始箔厚度。

**肿胀-裂变密度关系**（式 3–4）：

低燃耗区（fd ≤ 3 × 10²¹ fissions/cm³）：
$$\left(\frac{\Delta V}{V_0}\right)_f = 5.0 \cdot f_d \quad (\%)$$

高燃耗区（fd > 3 × 10²¹ fissions/cm³）：
$$\left(\frac{\Delta V}{V_0}\right)_f = 15 + 6.3(f_d - 3) + 0.33(f_d - 3)^2 \quad (\%)$$

其中 f_d 为裂变密度，单位 10²¹ f/cm³。

## 蠕变速率公式（式 2）

$$\dot{\varepsilon}_c = A \cdot \sigma \cdot \dot{f}$$

其中：
- ε̇_c：等效蠕变应变率 (s⁻¹)
- A：蠕变速率系数 (cm³/MPa) — **U–10Mo 最佳拟合值：A = 500 × 10⁻²⁵ cm³/MPa**
- σ：等效应力 (MPa)
- ḟ：裂变率 (fissions/cm³·s)

## 真实应变（式 5）

$$\varepsilon_{f,true} = \ln\left(1 + \frac{\Delta V}{V_0}\right)_f$$

---

# Parameters

## 材料力学参数

| 参数 | 数值 | 材料 | 来源 |
|------|------|------|------|
| Young's modulus | 66 GPa | AA6061 包壳 | [7] |
| Poisson's ratio | 0.34 | AA6061 包壳 | [7] |
| Yield strength | 280 MPa | AA6061（辐照硬化后） | [1] |
| Strain hardening exponent | 0.13 | AA6061-T6 | [8] |
| Young's modulus | 85 GPa | U–Mo 燃料 | [9] |
| Poisson's ratio | 0.34 | U–Mo 燃料 | [9] |

## 蠕变速率系数比较

| 燃料 | A (10⁻²⁵ cm³/MPa) | T/Tm | 来源 |
|------|---------------------|------|------|
| U (纯铀) | 800 | 0.3 | [14,17] |
| **U–10Mo** | **500** | **0.3** | **本研究** |
| MOX | 56 | 0.25 | [18] |
| UO₂ | 7 | 0.25 | [11,19,20] |
| UN | 3 | 0.3 | [21,22] |
| UC | 1 | 0.3 | [20] |

U–10Mo 的蠕变速率系数约为纯铀的一半，但远高于所有陶瓷铀燃料。

---

# Experimental Data

## 辐照实验条件

- **反应堆**: Advanced Test Reactor (ATR), Idaho National Laboratory
- **试验系列**: RERTR-6, -7, -8, -9A, -9B, -10, -12
- **板材尺寸**: 100 mm (长) × 25.4 mm (宽) × 1.4 mm (厚)
- **燃料箔尺寸**: 82.6 mm (长) × 19.0 mm (宽)
- **箔厚度**: 0.25 mm（标准）或 0.50 mm（部分样品）
- **合金成分**: U–10Mo（wt.%）和 U–12Mo
- **包壳材料**: Al 6061
- **结合工艺**: 摩擦搅拌焊 (FSW) 或热等静压 (HIP, 103 MPa, 560–580°C, 90 min)

## 关键样品数据（Table 1 摘要）

| Plate ID | 富集度 (%U-235) | U-235 燃耗 (%) | EFPD (天) | 裂变密度 (10²¹ f/cm³) | BOL 温度 (°C) |
|----------|-----------------|----------------|-----------|----------------------|---------------|
| L1F040 | 19.7 | 46 | 135 | 3.0 | 113 |
| L1F140 | 58.2 | 27 | 90 | 4.4 | 177 |
| H1P010 | 57.5 | 31 | 105 | 5.7 | 164 |
| L1P04A | 58.3 | 28 | 98 | 4.5 | 152 |
| L1P09T | 58.8 | 39 | 115 | 6.8 | 189 |
| L1P755 | 70.0 | 25 | 90 | 5.9 | 156 |

## 加载方式

- **Edge-on loading**: 板窄边朝向 ATR 堆芯，高功率边/低功率边功率比约 2.5 (HEU) 或 2 (LEU)
- **Face-on loading**: 板面朝向堆芯，宽度方向功率分布更均匀（L1P755）

## 肿胀测量

- 沿箔宽度方向每 0.5 mm 测量箔厚度
- 测量不确定度 ±2%
- 详细数据见 Table 2（14 块板材的测量值 vs 计算值对比）
- 关键观察：端部测量肿胀显著低于计算值，表明发生了质量转移

## 裂变气体气泡形貌

- L1P09T 样品：端部区域平均孔径 ~1.9 μm，峰值厚度区域 ~2.0 μm
- 气泡尺寸和数密度沿宽度方向数毫米内变化不大，排除气泡对端部肿胀降低的影响

---

# Key Findings

1. **U–Mo 燃料箔端部的锥形 (tapering) 现象**：尽管端部裂变密度最高（肿胀应最大），实际测量肿胀显著低于预期，原因是裂变诱导蠕变驱动的横向质量转移。

2. **蠕变速率系数**：通过 ABAQUS FEA 拟合获得 U–10Mo 裂变诱导蠕变速率系数 A = 500 × 10⁻²⁵ cm³/MPa，介于纯铀和 MOX 之间，约为纯铀的一半。

3. **高燃耗能力的关键机制**：裂变诱导蠕变有效降低端部应力，使 U–Mo 合金燃料能在高燃耗下不发生失效。

4. **剪切应力演化**：随辐照进行（BOL → MOL → EOL），燃料-包壳界面剪切应力增加，驱动质量转移加速。

5. **蠕变对安全分析的影响**：在裂变密度 7 × 10²¹ f/cm³ 时，蠕变引起的额外箔厚度增加可达原始厚度的 25%，需要在热点计算和安全分析中考虑。

6. **温度效应可忽略**：在 110–190°C 的低且窄温度范围内，裂变诱导蠕变表现为 athermal 行为。

7. **各燃料板材一致性**：无论制造方式（FSW/HIP）、加载方式（edge-on/face-on）还是包壳厚度（对称/非对称），FEA 模拟均与实验数据合理一致。

8. **孔隙率对蠕变的影响**：高燃耗时孔隙率 >10% 可能增强蠕变速率，但本文采用简化常数系数，建议未来采用燃耗依赖的蠕变速率系数。

---

# Relationships to Other Work

## 直接引用关系

- **Kim & Hofman (2011)** [Ref 1]: 提供了 U–Mo 肿胀动力学关联式（本文式 3–4 的来源），以及辐照硬化数据
- **Hofman & Kim (2009)** [Ref 2]: 首次提出质量转移机制的解释
- **Dienst (1977)** [Ref 11]: 关于裂变诱导蠕变的综述，线性应力依赖的基础

## 蠕变速率系数对比

本文的核心贡献是将 U–10Mo 的蠕变速率系数定位在已知的铀燃料蠕变速率谱系中：
- 纯 U > **U–10Mo** > MOX >> UO₂ > UN > UC
- 表明金属燃料的裂变诱导蠕变速率远高于陶瓷燃料

## 后续影响

- 本文建立的蠕变速率系数被广泛用于 U–Mo 燃料行为的有限元模拟
- 质量转移机制的发现对理解 U–Mo 弥散燃料中颗粒变形和烧结现象具有重要意义
- 建议的燃耗依赖蠕变速率系数为后续研究指明方向

## 相关关键词

- U–Mo alloy fuel, monolithic fuel, fission induced creep, fuel swelling, lateral mass transfer, ABAQUS FEA, athermal creep, RERTR program

## Relationships

- [[wiki/entities/FuelAlloy|FuelAlloy]] — U-10Mo monolithic fuel foil swelling and creep behavior in RERTR tests are the focus
- [[wiki/concepts/SwellingMechanisms|SwellingMechanisms]] — solid FP swelling and fission-gas bubble swelling are decomposed; creep-driven mass transfer is a key mechanism
- [[wiki/entities/Recrystallization|Recrystallization]] — recrystallization threshold influences transition from linear to enhanced bubble swelling
- [[wiki/summaries/2011_Kim_FissionProductInducedSwellingUMo|2011_Kim_FissionProductInducedSwellingUMo]] — provides the swelling correlations (Eqs. 3-4) used in this FEA model
- [[wiki/summaries/2013_Kim_RecrystallizationFGBSwellingUMo|2013_Kim_RecrystallizationFGBSwellingUMo]] — companion paper on recrystallization-driven FGB swelling in the same RERTR dataset
- [[wiki/summaries/2021_Robinson_PredictiveSwellingUMoMonolithic|2021_Robinson_PredictiveSwellingUMoMonolithic]] — extends predictive swelling modeling for U-Mo monolithic fuel
- U
