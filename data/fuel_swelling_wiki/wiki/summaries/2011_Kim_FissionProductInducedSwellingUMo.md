# Fission Product Induced Swelling of U-Mo Alloy Fuel

## Metadata

| 字段 | 值 |
|------|------|
| 标题 | Fission product induced swelling of U–Mo alloy fuel |
| 作者 | Yeon Soo Kim, G.L. Hofman |
| 机构 | Argonne National Laboratory, IL 60439, USA |
| 期刊 | Journal of Nuclear Materials |
| 年份 | 2011 |
| 卷/页 | 419, 291–301 |
| DOI | 10.1016/j.jnucmat.2011.08.018 |
| 关键词 | U-Mo合金, 裂变产物肿胀, 气泡肿胀, 固体裂变产物, 分散燃料, 单片燃料 |
| 研究范围 | 裂变密度 ≤ 7×10²⁷ fissions/m³, 温度 < 250°C, Mo含量 7–10 wt% |

---

## Physical Mechanisms

### 1. 总体肿胀机制（Overall Fuel Swelling）

U-Mo合金燃料的裂变产物诱导肿胀由**两个主要贡献**组成：

- **固体裂变产物肿胀**（包括液态裂变产物和未形成气泡的气态裂变产物原子）：与裂变密度呈**线性关系**，由裂变铀原子与产生的固体裂变产物之间的体积差引起。
- **裂变气体气泡肿胀**：在低燃耗时较小，但在高裂变密度（>3×10²⁷ fissions/m³）时因**晶粒细化**（grain refinement / recrystallization）而显著增强。

### 2. 裂变气体气泡演化

#### 2.1 纳米气泡（Intragranular Nano-bubbles）
- TEM观察到的**晶内纳米气泡**，约2 nm大小，以超晶格（superlattice）形式排列，间距6–7 nm（Van den Berghe, 2.4×10²⁷ fissions/m³）
- 更高燃耗时（4.5×10²⁷ fissions/m³），气泡尺寸增大至3.5 nm，超晶格常数11.5 nm（Gan et al.）
- 纳米气泡体积分数：低燃耗时~1.3%，高燃耗时~5.9%
- 这些纳米气泡被视为**固体裂变产物肿胀**的一部分

#### 2.2 SEM可见气泡（Grain Boundary Bubbles）
- 大于0.1 μm的气泡首先在**晶界**上形成
- 晶粒细化（recrystallization）产生更多晶界，为气泡形核和长大提供场所
- 晶粒细化起始范围：2.5×10²⁷ – 3.5×10²⁷ fissions/m³（模型取代表值3×10²⁷）
- 高燃耗时气泡均匀占据整个燃料截面

### 3. γ相稳定性与Mo含量

- Mo合金化使U稳定在**γ相**（bcc结构），比α相（正交结构）更能以间隙方式容纳裂变产物
- γ相具有**各向同性**肿胀行为
- 最佳γ稳定Mo含量：**10 wt%**
- 低Mo含量（如U-4Mo）在辐照下转变为α+γ'两相平衡态，导致**高得多的肿胀率**
- 超过10 wt% Mo时，U₂Mo相（δ相）形成，肿胀率反而增加

### 4. 晶界Mo浓度均匀化

- 雾化（atomized）U-Mo粉末具有"偏析"凝固结构：晶界Mo含量较低（~17 at%），晶粒内部较高（~22 at%）
- 裂变增强扩散（FED）驱使Mo浓度均匀化，但完全均匀化需要~2000天
- 典型RERTR-3辐照条件（48 EFPD）下，晶粒中心与晶界Mo浓度差仍有2.5 at%
- **结论**：在整个辐照期间，晶界保持较低的Mo浓度，有利于气泡形核

### 5. 燃料形态影响

| 燃料形态 | 显微硬度 (DPH) | 特点 |
|----------|---------------|------|
| Atomized powder | 290 ± 50 | 偏析结构，最低硬度 |
| Machined powder | 350 ± 50 | 高位错密度，最易再结晶 |
| Foil | 300 ± 10 | 冷加工结构 |

- Machined粉末因更高的位错密度，在更低燃耗下发生晶粒细化，导致更高的气泡肿胀
- γ相退火（800°C, 70–100 h）粉末晶粒更大，晶界更少，气泡肿胀明显更小

---

## Key Equations

### 肿胀计算基础

**分散燃料肿胀转换公式**（Eq. 4）：
$$\left(\frac{\Delta V}{V_0}\right)_f = \left(\frac{\Delta t_p}{t_p^0} - \frac{t_p^0 - t_m^0}{t_p^0} \cdot \frac{1}{v_f^0}\right)$$

**单片燃料肿胀公式**（Eq. 5）：
$$\left(\frac{\Delta V}{V_0}\right)_f = \frac{\Delta t_f}{t_f^0}$$

### 裂变增强扩散系数

$$D = \frac{1}{12} f_r V^{5/3}$$

其中 $f_r$ 为裂变速率，$V$ 为裂变尖峰影响体积（2.01×10⁻²⁴ m³）

### Mo浓度均匀化方程（Fick方程，Eq. 1–3）

$$\frac{\partial C(x,t)}{\partial t} = D \frac{\partial^2 C(x,t)}{\partial x^2}$$

解析解（Bleiberg模型）：
$$C(x,t) = \frac{2}{L}\int_0^{L/2} C(x,0)dx + \frac{4}{L}\sum_{n=1}^{\infty}\left[\int_0^{L/2} C(x,0)\cos\frac{2n\pi x}{L}dx\right]\cos\frac{2n\pi x}{L}\exp\left(-\frac{4Dn^2\pi^2 t}{L^2}\right)$$

### 气泡体积分数（Eq. 8）

$$v_b = \frac{\pi \bar{x}_0^2}{4} \cdot \rho_{CS}$$

### 总体肿胀经验公式

**低燃耗区**（fd ≤ 3×10²⁷ fissions/m³）（Eq. 6）：
$$\left(\frac{\Delta V}{V_0}\right)_f = 5.0 f_d \quad (\%)$$

**高燃耗区**（fd > 3×10²⁷ fissions/m³）（Eq. 7）：
$$\left(\frac{\Delta V}{V_0}\right)_f = 15 + 6.3(f_d - 3) + 0.33(f_d - 3)^2 \quad (\%)$$

### 固体裂变产物肿胀（Eq. 13）

$$\left(\frac{\Delta V}{V_0}\right)_s = 4.0 f_d \quad (\%)$$

其中 $f_d$ 单位为 10²⁷ fissions/m³。

### 裂变气体气泡肿胀（Eq. 14–15）

**低燃耗区**（fd ≤ 3×10²⁷）：
$$\left(\frac{\Delta V}{V_0}\right)_g = 1.0 f_d \quad (\%)$$

**高燃耗区**（fd > 3×10²⁷）：
$$\left(\frac{\Delta V}{V_0}\right)_g = 3.0 + 2.3(f_d - 3) + 0.33(f_d - 3)^2 \quad (\%)$$

### 肿胀分解关系

$$\left(\frac{\Delta V}{V_0}\right)_s = \left(\frac{\Delta V}{V_0}\right)_f - \left(\frac{\Delta V}{V_0}\right)_g$$

$$\left(\frac{\Delta V}{V_0}\right)_g = \left(1 + \left(\frac{\Delta V}{V_0}\right)_s\right) \frac{(\Delta V/V)_g}{1 - (\Delta V/V)_g}$$

---

## Parameters

### 材料参数

| 参数 | 值 | 来源 |
|------|-----|------|
| 裂变尖峰影响体积 V | 2.01×10⁻²⁴ m³ | Kim & Hofman |
| 雾化U-10Mo平均晶粒尺寸 | 2–2.5 μm | Kim et al. [7] |
| 晶界层厚度 | 0.5 μm | 本文测量 |
| 晶粒内部Mo浓度 | ~22 at% | Kim et al. [7,8] |
| 晶界Mo浓度 | ~17 at% | Kim et al. [7,8] |
| 雾化粉末平均粒径 | ~70 μm | Kim et al. [6] |
| 固体裂变产物肿胀率 | 4.0% per 10²⁷ fissions/m³ | Eq. 13 |
| 低燃耗总体肿胀率 | 5.0% per 10²⁷ fissions/m³ | Eq. 6 |
| U-10Zr固体裂变产物肿胀率 | 1.2% per at% burnup | Hofman & Walters [20] |

### 辐照条件参数

| 参数 | 范围 |
|------|------|
| 燃料温度 | 66–199°C（BOL） |
| Mo含量 | 6–12 wt% |
| U-235富集度 | 19.5–58.8% |
| 总辐照时间 | 48–257 EFPD |
| 裂变密度范围 | 2.0–7.0 ×10²⁷ fissions/m³ |
| 晶粒细化起始裂变密度 | 2.5–3.5 ×10²⁷ fissions/m³ |
| 裂变速率 | ~6×10²⁰ fissions/m³/s（用于均匀化计算） |

---

## Experimental Data

### 单片燃料肿胀数据（Table 3）

| 测试 | 样品 | 初始箔厚度 (mm) | 裂变密度 (10²⁷ f/m³) | 总体肿胀 (%) |
|------|------|-----------------|---------------------|-------------|
| RERTR-6 | L1F040 | 0.25 | 3.0 | 13 |
| RERTR-6 | L1F100 | 0.25 | 3.0 | 17 |
| RERTR-6 | L2F030 | 0.5 | 2.6 | 12 |
| RERTR-7 | L1F140 | 0.25 | 4.4 | 25 |
| RERTR-7 | L1F120 | 0.25 | 4.8 | 28 |
| RERTR-7 | L2F040 | 0.5 | 2.7 | 13 |
| RERTR-8 | H1P010* | 0.25 | 5.4 | 44 |
| RERTR-9 | L1F34T | 0.25 | 7.0 | 42 |
| RERTR-9 | L1P05A | 0.25 | 6.3 | 30 |
| RERTR-9 | L1P04A | 0.25 | 5.1 | 25 |
| RERTR-9 | L1F26C | 0.25 | 6.0 | 34 |
| RERTR-9 | L1F32C | 0.25 | 5.8 | 32 |
| RERTR-9 | L1P09T | 0.25 | 6.8 | 43 |

*U-12Mo，其余为U-10Mo

### 气泡肿胀分析数据（Table 4 部分关键数据）

| 样品 | 裂变密度 (10²⁷ f/m³) | 平均气泡直径 (μm) | 气泡密度 (个/μm²) | 气泡肿胀 (%) | 固体FP肿胀 (%) |
|------|---------------------|-------------------|-------------------|-------------|---------------|
| Z03 (γ退火) | 2.2 | 0.09 | 0.31 | 0.2 | 10.8 |
| Y01 (γ退火) | 2.0 | 0.09 | 0.35 | 0.2 | 9.8 |
| V002 (雾化) | 2.9 | 0.15 | 0.68 | 1.4 | 13.1 |
| A003 (机加工) | 3.0 | 0.18 | 1.06 | 3.1 | 11.9 |
| V6019G (雾化) | 3.1 | 0.16 | 1.00 | 2.3 | 13.3 |
| A8002L (机加工) | 3.0 | 0.18 | 1.26 | 3.7 | 11.3 |
| V6001M (雾化) | 4.8 | – | – | 10.2 | 17.2 |
| V6022M (雾化) | 5.5 | – | – | 13.3 | 19.5 |
| A6002H (机加工) | 5.7 | – | – | 14.8 | 19.6 |

**关键观察**：机加工粉末样品的气泡肿胀始终高于雾化粉末样品（相同辐照条件下对比）。

---

## Key Findings

1. **两阶段肿胀行为**：低燃耗时肿胀主要由固体裂变产物主导（线性），高燃耗时（>3×10²⁷ fissions/m³）裂变气体气泡肿胀因晶粒细化而显著增强（二次方增长）。

2. **固体裂变产物肿胀是线性的**：与裂变密度成正比，速率为4.0% per 10²⁷ fissions/m³，与燃料类型基本无关。

3. **温度无关性**：在250°C以下，U-Mo合金肿胀表现为**athermal**（非热激活），主要由裂变增强扩散（FED）控制。温度效应被FED与裂变碎片气泡重溶之间的相互抵消所掩盖。

4. **晶粒细化是关键机制**：辐照损伤和裂变产物积累导致γ-U-Mo晶粒细化（recrystallization），产生新的晶界作为气泡形核和生长的场所。

5. **燃料形态影响**：机加工粉末因高位错密度更早发生再结晶，气泡肿胀更高；γ相退火粉末因晶粒更大，气泡肿胀更低。

6. **无breakaway肿胀**：在整个研究范围内（≤7×10²⁷ fissions/m³），裂变气体气泡仍然小而稳定，没有出现失控肿胀迹象。

7. **Mo含量的重要性**：Mo含量低于~7 wt%时，γ相不稳定，转变为α+γ'导致各向异性和更高的肿胀率。

---

## Relationships to Other Work

### 前驱工作
- **Rest et al. (2009)** [1]：U-Mo中晶界裂变气体气泡演化的机制模型，裂变密度至3×10²⁷ fissions/m³
- **Hofman & Walters (1994)** [20]：U-10Zr合金固体裂变产物肿胀估计（1.2% per at% burnup）
- **Bleiberg (1956, 1959)** [9,10]：α+γ' → γ相反转分析，为晶界均匀化模型提供基础

### 引用的TEM观察
- **Van den Berghe et al. (2007)** [17]：TEM观察到U-7Mo中2 nm纳米气泡超晶格，间距6–7 nm
- **Gan et al. (2010)** [18]：TEM观察到更高燃耗下3.5 nm纳米气泡，超晶格常数11.5 nm

### 后续影响
- 本文的经验肿胀公式成为U-Mo燃料性能分析的标准参考
- 两阶段肿胀模型（固体FP + 气泡）被广泛用于U-Mo分散燃料和单片燃料设计
- 晶粒细化阈值（~3×10²⁷ fissions/m³）成为预测肿胀行为转变的关键参数

### 相关体系对比
| 燃料体系 | 固体FP肿胀率 | 特点 |
|----------|-------------|------|
| U-10Mo | 4.0% per 10²⁷ f/m³ | athermal, <250°C |
| U-10Zr | ~1.2% per at% burnup | 液态Na间隙 |
| U-4Mo | 远高于U-10Mo | γ相不稳定，α+γ'转变 |

---

## Notes

- 本文数据主要基于U-10Mo，但模型可扩展至Mo含量7–10 wt%的U-Mo合金
- 肿胀测量误差主要来自初始箔厚度不确定度（±5 μm → ±2%肿胀误差）
- 所有辐照实验在ATR（Advanced Test Reactor）中进行
- 箔厚度测量不确定度：±0.005 mm

## Relationships

- [[wiki/entities/FuelAlloy|FuelAlloy]] — U-Mo alloy fuel (7–10 wt% Mo) swelling data and empirical correlations are the core contribution
- [[wiki/entities/Recrystallization|Recrystallization]] — grain refinement at ~3×10²⁷ fissions/m³ triggers the transition to enhanced bubble swelling
- [[wiki/concepts/SwellingMechanisms|SwellingMechanisms]] — two-component swelling model (solid FP + fission gas bubble) is the key framework
- [[wiki/entities/FissionGasDiffusion|FissionGasDiffusion]] — fission-enhanced diffusion controls Mo homogenization and bubble nucleation at grain boundaries
- [[wiki/summaries/2008_Kim_IntergranularFGBubblesUMo|2008_Kim_IntergranularFGBubblesUMo]] — the pre-transition intergranular bubble data from Kim (2008) feeds directly into this model
- [[wiki/summaries/2015_Cui_MechanisticGaseousSwellingUMo|2015_Cui_MechanisticGaseousSwellingUMo]] — Cui (2015) develops a mechanistic model building on the empirical framework here
- [[wiki/concepts/SwellingModelComparison|SwellingModelComparison]] — empirical correlations here serve as benchmarks for comparison with mechanistic models
