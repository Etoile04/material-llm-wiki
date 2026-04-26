# Metadata

- **标题**: Void nucleation, growth, and coalescence in irradiated metals
- **作者**: Michael P. Surh, Jess B. Sturgeon, Wilhelm G. Wolfer
- **年份**: 2008
- **期刊**: Journal of Nuclear Materials
- **卷/页**: 378, 86–97
- **DOI**: 10.1016/j.jnucmat.2008.05.009
- **机构**: Lawrence Livermore National Laboratory (LLNL)
- **关键词**: void swelling, cluster dynamics, rate theory, Monte Carlo, helium bubbles, irradiation

---

# Physical Mechanisms

## 辐照损伤基本过程

1. **Frenkel 对产生**: 中子辐照在金属中产生 disseminated Frenkel pairs（空位-自间隙原子对），损伤产生效率 η ≈ 0.1
2. **氦杂质生成**: 通过核嬗变反应（如 ⁵⁸Ni(n,γ)⁵⁹Ni(n,α)）逐步产生氦原子，氦以置换缺陷形式沉积
3. **缺陷聚集与湮灭**: 空位和间隙原子分别聚集形成 void/bubble 和位错环，同时发生复合

## 空洞形核机制

- **二维团簇分布**: 使用 (n_vac, n_hel) 二维组分空间描述 He-Vacancy 团簇，区分 void（高空位/氦比）和 bubble（高压平衡气泡）
- **形核路径**: 小团簇沿稳定平衡 bubble 线生长（积累氦的同时动态调整空位数），达到临界氦含量后转变为稳定 void
- **临界尺寸**: 在 500°C 下临界氦含量约 11 个氦原子；临界空位/氦组分约 (19, 11) 和 (94, 0)
- **表面能效应**: 吸附氧杂质降低空洞表面能（因子 K = 0.45–0.80），显著影响形核势垒和空洞密度

## 空洞长大机制

- **单体聚集模型**: void 通过吸收空位 monomer 长大，位错偏好（dislocation bias）驱动净空位流入
- **稳态肿胀率**: 约 0.8%/dpa（500°C，316 不锈钢），与奥氏体不锈钢实验观测一致
- **bimodal 分布**: 无 coalescence 时，小高压 bubble 和大低压 void 共存

## 空洞合并（Coalescence）

- **团簇扩散**: void 扩散系数 D_n = D_v / n_v^(4/3)，小团簇扩散快
- **合并效应**:
  - 优先消耗小而活泼的团簇
  - 最大 void 通过合并增大一个数量级
  - 低温：减少复合中心 → 加速大 void 形成 → 增强低温肿胀
  - 高温：大幅减少 bubble/void 总数 → 降低渐进肿胀率
  - 消除 bimodal 分布
- **终端空洞密度**: 700°C 时降至 4–5 × 10¹⁸ m⁻³

## 陷阱效应

- 团簇被析出物钉扎（pinning）阻碍扩散和合并，延长孕育期
- 完全固定模型（所有 ≥ dimer 的团簇不可移动）导致 bimodal 分布
- 实际材料中 trapping 和 coalescence 的竞争决定微观结构演化

---

# Key Equations

## 反应速率系数（Equation 1）

$$K(m, n) = Z_{m,n} \cdot A_{m,n} \cdot D_{m,n}$$

其中 Z 为 bias factor，A 为碰撞截面，D 为相对扩散系数。

## 单体密度演化（Equation 2）

空位、间隙原子、氦单体（间隙态和置换态）的密度演化方程，包含：
- 辐照产生项 g
- 与团簇的反应消耗项
- 热发射项
- 与位错的反应项

## 团簇密度演化（Equation 3）

一般团簇 (n_vac, n_hel) 的密度演化，包含：
- 辐照直接产生项 g_n
- 单体反应项（聚集 + 热发射空位）
- 团簇-团簇合并项（含 1/2 防止重复计数因子）
- step function U(n) 限制允许的组分范围

## 氦嬗变速率（Equations 4–5）

⁵⁸Ni → ⁵⁹Ni → ⁵⁶Ni + α 两步激活模型：
- c = 0.0255 dpa⁻¹（⁵⁸Ni 激活率）
- a = 0.0711 dpa⁻¹（⁵⁹Ni (n,α) 率）
- d = 0.297 dpa⁻¹（⁵⁹Ni 总消耗率）

$$\frac{dq_{He}}{dx} = \frac{ac}{c-d} q_{58}(0) [e^{-dx} - e^{-cx}]$$

## 空洞自由能（Equation 8）

$$E[n] = K\sigma_0(T) \left(1 - \frac{0.8}{n_v + 2}\right) 4\pi r_n^2$$

K 为表面能降低因子（氧吸附效应），大 void 时趋近于 Kσ₀。

## 热发射率（Equation 7）

$$c_v^{eq}[n] = c_v^{[d]} \exp\left(-\frac{E[n] - E[n-v] - P\Omega}{kT}\right)$$

包含内能差和气体压力功的贡献。

## MC-MC 合并反应（Markov Monte Carlo）

反应间隔: $dt = -\ln(x)/R_N$，反应对选择概率正比于反应速率。

---

# Parameters

## 材料参数（Type-316 不锈钢）

| 参数 | 值 | 说明 |
|------|-----|------|
| 晶格常数 a₀ | 3.639 × 10⁻¹⁰ m | |
| Burgers 矢量 b | a₀√2/2 | |
| 原子体积 Ω | a₀³/4 | |
| 剪切模量 μ | 8.295 × 10¹⁰ Pa | |
| 泊松比 ν | 0.264 | |
| 损伤产生效率 η | 0.1 | |

## 空位参数

| 参数 | 值 |
|------|-----|
| 弛豫体积 | −0.2 Ω |
| 迁移能 E_m | 2.08 × 10⁻¹⁹ J (~1.3 eV) |
| 形成能 E_f | 2.88 × 10⁻¹⁹ J (~1.8 eV) |
| 形成熵 S_f | 1.5 k_B |
| 指数前因子 | 1.29 × 10⁻⁶ m²/s |

## 自间隙原子参数

| 参数 | 值 |
|------|-----|
| 弛豫体积 | 1.50 Ω |
| 迁移能 E_m | 0.320 × 10⁻¹⁹ J (~0.2 eV) |
| 指数前因子 | 1.29 × 10⁻⁶ m²/s |

## Void 参数

| 参数 | 值 |
|------|-----|
| 表面能 σ₀(T=0) | 2.408 J/m² |
| dσ₀/dT | 0.440 × 10⁻³ J/m²/K |
| 吸附因子 K | 0.45–0.80 |
| 迁移能 E_m | 2.08 × 10⁻¹⁹ J |
| 扩散系数 | (4/3) D_v / n_v^(4/3) |

## 环境参数

| 参数 | 值 |
|------|-----|
| 温度范围 | 300–700°C |
| 通量 | 10⁻⁶ dpa/s |

## 氦密度约束

nh ≤ 2nv（超过则禁止进一步反应，避免 loop punching）

---

# Experimental Data

## 模型验证

- **氦含量**: 模型参数拟合 HFIR 辐照镍中的实验氦含量数据 [35, 36]
- **肿胀率**: 500°C 下预测 0.8%/dpa，与奥氏体不锈钢实验值 ~1%/dpa 一致
- **位错密度**: 使用 Wolfer-Glasgow 模型 [32] 再现实验测量的位错密度-剂量-温度关系

## 关键计算结果

### 无 Coalescence 模型（σ = 0.75σ₀）

| 温度 | 肿胀行为 |
|------|---------|
| 300°C | 极低肿胀，大量小 bubble 作为复合中心 |
| 500°C | 稳态肿胀 ~0.8%/dpa，bimodal 分布 |
| 700°C | 空洞密度 7–8 × 10²⁰ m⁻³，较少 void 突破临界尺寸 |

### 有 Coalescence 模型

| 温度/条件 | 肿胀行为 |
|-----------|---------|
| 300°C, σ = 0.5σ₀ | 增强肿胀，减少复合中心 |
| 500°C, σ = 0.5σ₀ | 肿胀率 ~0.8%/dpa |
| 500°C, σ = 0.75σ₀ | 肿胀率仅 ~0.3%/dpa（50 dpa 时） |
| 700°C | 终端 void 密度 4–5 × 10¹⁸ m⁻³ |

### 表面能敏感性

- 300°C：可见空洞密度从 5 × 10²³ m⁻³（K=0.8）到 1 × 10²⁴ m⁻³（K=0.5）
- Coalescence 模型中 500°C 仍对 σ 敏感：0.3%/dpa（K=0.75）vs 0.8%/dpa（K=0.5）

---

# Key Findings

1. **混合 ME/MC 方法**: 提出 LiME（Livermore Microstructure Evolution）程序，结合 Master Equation 和 Monte Carlo 方法处理 stiff、非线性的耦合反应速率方程，无需截断或粗粒化尺寸域
2. **二维团簇分布**: (n_vac, n_hel) 分布函数允许独立追踪空位和氦含量，区分 void 和 bubble
3. **Coalescence 的重要性**:
   - 无 coalescence：bimodal 分布（小 bubble + 大 void 共存）
   - 有 coalescence：小 bubble 被消除，仅剩大 void，终端 void 密度降低
   - 显著影响孕育期和终端肿胀率
4. **表面能的关键作用**: 氧吸附降低表面能（K = 0.45–0.80）直接影响形核势垒，coalescence 模型中 500°C 仍对表面能敏感
5. **Trapping vs. Coalescence 竞争**: 实际材料的肿胀行为由小团簇（多为 TEM 不可见）的 trapping 和 coalescence 之间的竞争决定
6. **低温肿胀增强**: Coalescence 消除复合中心，在低温下反而增强肿胀

---

# Relationships to Other Work

## 前序工作（同一团队）

- **Surh et al. (2004)** [5–8]: 前期 monomer aggregation 模型，仅考虑 void 与单体反应，预测 ~1%/dpa 肿胀率
- **Wolfer & Glasgow (1985)** [32]: 位错密度演化模型，本文直接采用

## 相关理论

- **Mansur & Coghlan (1983)** [14]: He-Vacancy 团簇模型基础
- **Greenwood & Speight (1963)** [11], **Gruber (1967)** [12]: void 尺寸依赖扩散理论
- **Gillespie (1972, 2000, 2001)** [16, 21, 22]: Markov Monte Carlo 方法基础

## 实验关联

- **Cawthorne & Fulton (1967)** [1]: 首次发现 void swelling
- **Garner & Wolfer (1984)** [2]: 孕育剂量概念
- **Greenwood et al. (2003)** [35]: HFIR 辐照镍中氦含量数据

## 后续扩展方向（文中指出）

- 位错环的形成、unfaulting、迁移和合并
- 氧杂质的显式建模（替代恒定表面能降低因子）
- 可逆钉扎对空洞迁移率的影响
- 内部气体压力对表面扩散的影响
- 辐照增强扩散
- 间隙-间隙聚集和 void-位错反应

## Relationships

- [[wiki/entities/CavitationalVoid|CavitationalVoid]] — void nucleation, growth, and coalescence kinetics are the core subject using LiME cluster dynamics
- [[wiki/concepts/RateTheoryFramework|RateTheoryFramework]] — the mixed Master Equation/Monte Carlo approach is an advanced rate-theory implementation
- [[wiki/entities/FissionGasDiffusion|FissionGasDiffusion]] — helium-vacancy cluster formation and void nucleation paths are modeled in detail
- [[wiki/summaries/2009_Rokkam_PhaseFieldVoidNucleationGrowth|2009_Rokkam_PhaseFieldVoidNucleationGrowth]] — Rokkam's phase-field model addresses the same void nucleation and growth problem with a different methodology
- [[wiki/summaries/1993_Rest_VoidSwellingAlphaU|1993_Rest_VoidSwellingAlphaU]] — Rest's rate-theory void swelling model is a related foundational approach
- [[wiki/concepts/SwellingModelComparison|SwellingModelComparison]] — cluster dynamics vs. phase-field vs. rate-theory comparisons are enabled by this work

## Related Work
- [[wiki/summaries/2009_Rokkam_PhaseFieldVoidNucleationGrowth|2009_Rokkam_PhaseFieldVoidNucleationGrowth]] — Rokkam 用相场方法处理相同问题（空洞形核与长大），是本文团簇动力学方法的补充
- [[wiki/summaries/1993_Rest_VoidSwellingAlphaU|1993_Rest_VoidSwellingAlphaU]] — Rest 的速率理论空腔肿胀模型是本文 LiME 方法的简化先驱
- [[wiki/entities/CavitationalVoid|CavitationalVoid]] — 空洞形核、长大和合并是本文的核心物理主题
- [[wiki/concepts/GasBubbleCoalescence|GasBubbleCoalescence]] — 本文系统量化了空洞合并对微观结构演化和终端肿胀率的影响
- [[wiki/concepts/RateTheoryFramework|RateTheoryFramework]] — LiME 的混合主方程/Monte Carlo 方法是速率理论的高级实现
