# Phase-Field Simulation of Irradiated Metals: Part II — Gas Bubble Kinetics

## Metadata

| 字段 | 值 |
|------|-----|
| **标题** | Phase-field simulation of irradiated metals: Part II: Gas bubble kinetics |
| **作者** | Paul C. Millett, Anter El-Azab, Dieter Wolf |
| **年份** | 2011 |
| **期刊** | Computational Materials Science |
| **卷/页** | 50, 960–970 |
| **DOI** | 10.1016/j.commatsci.2010.10.032 |
| **机构** | Idaho National Laboratory; Florida State University; Argonne National Laboratory |
| **关键词** | Phase-field simulation, irradiation damage, gas bubble kinetics, grain boundary bubbles |

---

## Physical Mechanisms

### 1. 相场方法框架

本文是 Part I 的扩展，引入了裂变气体（fission gas）的生成、扩散和偏聚。模型基于 Cahn-Hilliard 自由能泛函，描述多晶金属中空位（vacancy）、自间隙原子（self-interstitial）和气体原子（gas atom）三种点缺陷在辐照条件下的演化。

核心思想：通过一个长程有序参数 g(r,t) 区分固相和气泡相，使两相可以采用不同的热力学和动力学描述。这与 Hu et al. [12] 的模型不同——后者省略了非保守有序参数。

### 2. 气泡形核与长大

- **均匀形核（Homogeneous nucleation）**：气体原子在基体中随机扩散、相遇并聚集，形成气泡核心
- **非均匀形核（Heterogeneous nucleation）**：气体原子被晶界（GB）、三叉结（TJ）等缺陷捕获，优先形核
- **气泡长大/收缩**：取决于空位和间隙原子向气泡表面的净通量——净空位吸收导致长大，净间隙吸收导致收缩
- **气泡内气体密度**：随气泡体积变化和气体原子流入量动态调整

### 3. 晶界气泡（Intergranular Bubbles）

- 晶界降低气体原子形成能，促进气体偏聚和优先形核
- 晶界上气泡呈透镜状（lenticular shape），三叉结处呈弯曲三角形
- 平衡形状由 Herring 关系控制，二面角 θ ≈ 120°
- 晶界气泡对晶界迁移产生 Zener 钉扎效应（Zener pinning）

### 4. 辐照演化三阶段

| 阶段 | 名称 | 特征 |
|------|------|------|
| Stage I | 孵育期（Incubation） | 缺陷浓度累积，无明显气泡 |
| Stage II | 形核与长大（Nucleation & Growth） | 气泡快速形核并长大，孔隙率呈 S 型曲线 |
| Stage III | 粗化（Coarsening） | 形核停止，大泡吞小泡 |

---

## Key Equations

### 总自由能泛函

$$F = N \int_V \left[ h(g) f^{solid}(c_a) + j(g) f^{bubble}(c_a) + f^{pc}(g, \phi_{1 \ldots P}) + f^{grad}(c_a, g, \phi_{1 \ldots P}) \right] dV$$

- $c_a$ = {c_v, c_i, c_g}：空位、间隙、气体浓度场
- $N$：单位体积晶格位数
- $g$：有序参数（g=0 固相，g=1 气泡相）
- $\phi_{1 \ldots P}$：晶粒取向有序参数

### 固相自由能

$$f^{solid} = E_v^f c_v + E_i^f c_i + E_g^f c_g + k_BT[c_v \ln c_v + c_i \ln c_i + c_g \ln c_g + (1-c_v-c_i-c_g)\ln(1-c_v-c_i-c_g)]$$

- 包含空位、间隙、气体的形成焓和构型熵
- 假设气体原子为替代式缺陷（substitutional defects）

### 气泡相自由能

$$f^{bubble} = \left[(c_v - 1)^2 + c_i^2\right] + \left[\mu_g^0 c_g + c_g k_BT \ln c_g + c_g k_BT \ln(k_BT)\right]$$

- 第一项：能量最小值在 c_v=1, c_i=0（纯空位气泡）
- 第二项：理想气体自由能（推导见 Appendix A）

### 多晶体自由能

$$f^{polycrystal}(g, \phi_{1 \ldots P}) = 3A\left(\sum_{k=1}^{P} \phi_k^2 + g^2\right)^2 - 4A\left(\sum_{k=1}^{P} \phi_k^3 + g^3\right)$$

- g=0（固相）：P 个能量井，{φ_k=1, 其余=0}
- g=1（气泡相）：所有 φ → 0（晶粒有序参数在气泡内消失）

### 梯度能量

$$f^{grad} = \sum \frac{\kappa_w}{2} |\nabla w|^2$$

- w 包含所有浓度场和有序参数场
- 贡献气泡表面能和晶界能

### 气体原子动力学方程（Cahn-Hilliard）

$$\frac{\partial c_g}{\partial t} = \nabla \cdot \left[ M_g \nabla \frac{1}{N} \frac{\delta F}{\delta c_g} \right] + \eta_g(r,t) + P_g(r,t)$$

- 气体迁移率：$M_g = D_g c_g / (k_BT)$
- $\eta_g$：级联事件随机源项
- $P_g$：气体产生率

### 晶粒演化方程（Allen-Cahn）

$$\frac{\partial \phi_i}{\partial t} = -L_\phi \frac{\delta F}{\delta \phi_i}$$

### 孔隙率演化（Johnson-Mehl-Avrami 方程）

$$p = p_0 \left[1 - \exp(-k t^3)\right]$$

- $k = \frac{\pi}{3} \dot{R}^2 J$（2D 情况）
- $\dot{R}$：气泡半径增长率，$J$：形核率

### 理想气体状态方程

$$p = c_g k_BT$$

### 晶界处气体形成能降低

$$E_g^f = E_g^{f0} - U$$

- $U$：在晶粒内部 = 1.0，在晶界和三叉结处低至 0.5

---

## Parameters

### 缺陷形成能

| 参数 | 值 | 说明 |
|------|-----|------|
| $E_v^f$ | 0.8 eV | 空位形成能 |
| $E_i^f$ | 0.8 eV（Section 3）/ 1.5 eV（Section 4-5） | 间隙形成能 |
| $E_g^f$ | 0.8 eV（Section 3）/ 1.2 eV（Section 4-5） | 气体原子形成能 |
| $\mu_g^0$ | 0.4 eV | 气体参考化学势 |

### 扩散参数

| 参数 | 值 | 说明 |
|------|-----|------|
| $\tilde{D}_v$ | 1 | 无量纲空位扩散率 |
| $\tilde{D}_g$ | 1 | 无量纲气体扩散率 |
| $\tilde{D}_i$ | 4 | 无量纲间隙扩散率（Di > Dv，符合金属中的一般规律） |

### 温度与热力学

| 参数 | 值 |
|------|-----|
| $k_BT$ | 0.11 eV |
| $T$ | 1276 K |
| $c_v^{eq} = c_i^{eq}$ | 6.9 × 10⁻⁴ |

### 数值参数

| 参数 | 值 |
|------|-----|
| 网格间距 Δx | κ |
| 时间步 Δt | 0.001 s |
| 梯度能量系数 κ_v = κ_i = κ_g = κ_g = κ_φ | 1.0 eV·κ² |

### 复合率

| 参数 | 值 |
|------|-----|
| $R_{bulk}$ | 1.0 s⁻¹ |
| $R_{surf}$ | 5.0 s⁻¹ |

### 辐照参数

| 参数 | 值 |
|------|-----|
| 位移率 $K$ | 1.0 × 10⁻³ 或 2.3 × 10⁻³ dpa/s |
| 气体产生率 $P_{gas}$ | 0.0, 2.0 × 10⁻⁵, 1.0 × 10⁻⁴, 8.2 × 10⁻⁶ c_g/s |
| 间隙产生偏置 | 0.9（即 10% 更多空位） |

### 多晶模拟

| 参数 | 值 |
|------|-----|
| 晶粒数 $P$ | 40 |
| 平均晶粒直径 | 37 κ < d < 111 κ |
| 模拟域 | 6 μm × 6 μm，周期性边界 |
| 晶界能量/迁移率 | 各向同性 |

---

## Experimental Data

本文主要为计算模拟工作，无直接实验数据。但：

- **Fig. 10f**：对比了 UO₂ 中晶界气泡的显微图像（引自 Zacharie et al. [2], J. Nucl. Mater. 255 (1998) 85），定性验证了模拟得到的透镜状气泡形貌
- **气泡密度与尺寸随气体产率变化的趋势**与实验观测一致 [1]：气体产率增加 → 气泡密度增加、气泡尺寸减小

### 模拟验证结果

| 验证项 | 结果 |
|--------|------|
| 空洞内气体聚集（无净空位/间隙通量） | ✅ 气体浓度增加，气泡体积不变 |
| 过饱和空位条件下气泡长大 | ✅ 气泡体积增大，内部气体密度降低 |
| 过饱和间隙条件下气泡收缩 | ✅ 气泡体积减小，内部气体密度增加 |
| Zener 钉扎能 | ✅ 模拟与理论 2rγ_gb 一致 |
| 晶界气泡二面角 | ✅ 从 90° 指数趋近 ~120° |

---

## Key Findings

### 单晶模拟

1. **气泡演化三阶段**：孔隙率演化遵循 Johnson-Mehl-Avrami 方程，形核率可从模拟中提取并与理论预测吻合（相差不超过两倍）

2. **气体产率效应**：
   - 气体产率增加 → 形核率增加、气泡密度增加、气泡尺寸减小
   - 气体原子作为空位陷阱，提高自由能远离平衡，降低形核势垒

3. **气泡内气体浓度动态**：
   - Stage II（快速长大期）：c_g 下降（空位流入速率 > 气体流入速率）
   - Stage III（粗化期）：c_g 逐渐回升并趋于稳定
   - 高位移率下 c_g 更低（形核更早，系统气体浓度更低）

4. **形核率对位移率依赖性**：
   - 高位移率下，形核率对气体产率的依赖性较弱（形核在气体浓度较低时已开始）

### 多晶模拟

5. **晶界优先形核**：晶界处气体形成能降低 → 气体偏聚 → 优先形核

6. **晶界气泡形状**：
   - 晶界面上：透镜状（lenticular）
   - 三叉结处：弯曲三角形
   - 晶粒内部：圆形

7. **晶粒尺寸效应**：
   - 孔隙率和形核率对晶粒尺寸不敏感
   - 晶粒尺寸增大 → 晶界气泡直径增大、晶界气泡间距减小、晶界覆盖率增加
   - 原因：大晶粒 → 晶界密度低 → 相同孔隙率下气泡更密集于少数晶界

8. **模型创新**：首次在相场模型中显式考虑动态演化的气泡与晶界的相互作用（Zener 钉扎 + 平衡形状）

---

## Relationships to Other Work

### 前置工作
- **Part I** (Millett et al.): 同期论文，建立了纯金属辐照损伤的相场模型基础（空位/间隙动力学、空洞形核长大）
- **Millett et al. (2009)** [13]: 先前的单组分金属气泡模型

### 相关相场模型
- **Hu et al. (2009)** [12]: UO₂ 裂变气体行为的相场模型，但缺少非保守有序参数 g
- **Moelans et al. (2005)** [16]: 多晶体相场模型，捕获颗粒对晶界的钉扎
- **Chen & Yang (1994)** [11]: 多晶体相场模型框架

### 理论基础
- **Cahn-Hilliard (1958)** [14]: 非均匀系统自由能
- **Zener/Smith (1948)** [10]: Zener 钉扎理论
- **Herring (1951)** [19]: 二面角平衡关系
- **Olander (1985)** [5]: 核反应堆燃料基础理论

### 实验参考
- **Zacharie et al. (1998)** [2]: UO₂ 晶界气泡显微图像
- **Trinkaus & Singh (2003)** [1]: 辐照材料中惰性气体行为综述

### 后续影响
- 本文模型为辐照条件下核燃料（UO₂）和结构材料的气泡演化模拟提供了相场框架
- 可扩展至 Van der Waals 气体状态方程、气泡再溶解（re-solution）等物理过程

## Relationships

- [[wiki/entities/PhaseFieldModeling|PhaseFieldModeling]] — extends the Cahn-Hilliard + Allen-Cahn phase-field framework to include gas atom kinetics in polycrystalline metals
- [[wiki/entities/FissionGasDiffusion|FissionGasDiffusion]] — gas atom generation, diffusion, and grain boundary segregation are the new physical elements added
- [[wiki/entities/GasBubbleSuperlattice|GasBubbleSuperlattice]] — intragranular homogeneous nucleation of gas bubbles is a precursor to superlattice ordering
- [[wiki/summaries/2009_Rokkam_PhaseFieldVoidNucleationGrowth|2009_Rokkam_PhaseFieldVoidNucleationGrowth]] — Part I of this work; void-only phase-field model is the foundation
- [[wiki/summaries/2018_Liang_3DPhaseFieldIntragranularBubbleUMo|2018_Liang_3DPhaseFieldIntragranularBubbleUMo]] — Liang (2018) extends 3D phase-field bubble modeling in U-Mo
- [[wiki/concepts/SwellingMechanisms|SwellingMechanisms]] — bubble nucleation, growth, and coarsening stages in polycrystalline fuel are simulated

## Related Work
- [[wiki/summaries/2009_Rokkam_PhaseFieldVoidNucleationGrowth|2009_Rokkam_PhaseFieldVoidNucleationGrowth]] — Part I predecessor; void-only phase-field model without gas atom kinetics
- [[wiki/summaries/2018_Liang_3DPhaseFieldIntragranularBubbleUMo|2018_Liang_3DPhaseFieldIntragranularBubbleUMo]] — extends this 2D framework to 3D with re-solution, dislocation bias, and elastic strain in U-Mo
- [[wiki/summaries/2016_Hu_GasBubbleSuperlatticeFormationPF|2016_Hu_GasBubbleSuperlatticeFormationPF]] — related phase-field model for gas bubble superlattice formation via 1-D SIA migration
- [[wiki/summaries/2020_Hu_DefectClusterGasBubbleUMo|2020_Hu_DefectClusterGasBubbleUMo]] — extends defect-gas bubble interaction modeling in U-Mo
- [[wiki/concepts/RateTheoryFramework|RateTheoryFramework]] — rate-theory underpinnings of the Cahn-Hilliard defect evolution equations
- [[wiki/concepts/GasBubbleCoalescence|GasBubbleCoalescence]] — Stage III coarsening behavior captured by the phase-field model
