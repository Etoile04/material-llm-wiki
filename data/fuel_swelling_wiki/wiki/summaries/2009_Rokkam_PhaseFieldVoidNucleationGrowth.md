# Phase Field Modeling of Void Nucleation and Growth in Irradiated Metals

## Metadata

| 字段 | 值 |
|------|------|
| **标题** | Phase field modeling of void nucleation and growth in irradiated metals |
| **作者** | Srujan Rokkam, Anter El-Azab, Paul Millett, Dieter Wolf |
| **年份** | 2009 |
| **期刊** | Modelling and Simulation in Materials Science and Engineering |
| **卷/页** | 17, 064002 (18pp) |
| **DOI** | 10.1088/0965-0393/17/6/064002 |
| **机构** | Florida State University; Idaho National Laboratory |
| **关键词** | 相场模型, 空洞形核, 空洞长大, 辐照金属, 空位过饱和, Cahn-Hilliard, Allen-Cahn |

---

## Physical Mechanisms

### 核心思想
本文提出了一种**唯象相场模型**，用于描述金属中空位过饱和条件下的空洞（void）形成与演化。该模型将空洞形成视为**空位从过饱和固溶体中脱溶析出**的过程，类似于沉淀析出。

### 双场描述
- **保守场** — 空位浓度场 $c_v(\mathbf{x}, t)$：描述空位在基体中的空间分布，遵循 Cahn-Hilliard 型动力学
- **非保守场** — 序参量 $\eta(\mathbf{x}, t)$：描述基体相（$\eta = 0$）与空洞相（$\eta = 1$）之间的长程序，遵循 Allen-Cahn 型动力学

### 空洞形成物理
1. **辐照产生空位**：高能粒子（中子）撞击原子产生初级碰撞原子（PKA），引发级联碰撞，产生大量空位-间隙原子对
2. **空位过饱和**：级联碰撞后剩余的空位使空位浓度远超热平衡值
3. **空洞形核**：空位聚集形成空洞胚胎（void embryo）
4. **空洞长大**：空洞通过吸收周围空位持续长大
5. **Ostwald 熟化**：大空洞以消耗小空洞为代价继续长大

### 辐照空洞形成的三个阶段
- **Stage I — 孕育期（Incubation）**：空位浓度积累，系统无空洞形成
- **Stage II — 形核期（Nucleation）**：小空洞核心稳定形成，空洞数量线性增长
- **Stage III — 长大期（Growth）**：已有空洞吸收空位长大，Ostwald 熟化与空洞合并发生，空洞数量减少

### 关键物理效应
- **Gibbs-Thomson 效应**：空洞的平衡尺寸取决于周围空位浓度梯度，小空洞在低过饱和度下会收缩
- **Denuded zone（贫化区）**：大空洞/自由表面附近因大量吸收空位，形成无空洞形核区域
- **Ostwald 熟化**：大空洞吸收小空洞释放的空位而长大

---

## Key Equations

### 1. 自由能泛函

$$\mathcal{F}[c_v, \eta] = N \int \left[ h(\eta)\psi_m(c_v) + w(c_v, \eta) + \kappa_v|\nabla c_v|^2 + \kappa_\eta|\nabla \eta|^2 + \psi_{el}(c_v, \eta) \right] dV$$

其中：
- $N$ = 单位体积格点数
- $h(\eta) = (\eta-1)^2(\eta+1)^2$ — 形状函数（基体中 $h=1$，空洞中 $h=0$）
- $\psi_m(c_v)$ — 空位缺陷自由能
- $w(c_v, \eta)$ — Landau 型双稳态势
- $\kappa_v, \kappa_\eta$ — 梯度能量系数
- $\psi_{el}$ — 弹性相互作用能（本文忽略）

### 2. 空位缺陷自由能

$$\psi_m(c_v) = E_v^f c_v + k_BT[c_v \ln(c_v) + (1-c_v)\ln(1-c_v)]$$

### 3. Landau 型双稳态项

$$w(c_v, \eta) = -A(c_v - c_v^0)^2 \eta(\eta+2)(\eta-1)^2 + B(c_v - 1)^2 \eta^2$$

双稳态设计：
- 能量井1：$c_v = c_v^0, \eta = 0$（基体相，热平衡空位浓度）
- 能量井2：$c_v = 1, \eta = 1$（空洞相，纯空位）

### 4. Cahn-Hilliard 方程（空位浓度场演化）

$$\frac{\partial c_v}{\partial t} = \nabla \cdot M_v \nabla \left[ h(\eta)\frac{\partial \psi_m}{\partial c_v} + \frac{\partial w}{\partial c_v} - 2\kappa_v \nabla^2 c_v \right] + \xi(\mathbf{x},t) + P_v(\mathbf{x},t)$$

- $M_v = D_v / k_BT$ — 空位迁移率
- $\xi$ — 热涨落
- $P_v$ — 辐照空位源项（随机）

### 5. Allen-Cahn 方程（序参量演化）

$$\frac{\partial \eta}{\partial t} = -L\left[ \frac{\partial h}{\partial \eta}\psi_m + \frac{\partial w}{\partial \eta} - 2\kappa_\eta \nabla^2 \eta \right] + \zeta(\mathbf{x},t)$$

- $L$ — 界面迁移率

### 6. 空洞表面速度

$$v_n = -\frac{\partial \eta / \partial t}{|\nabla \eta|}_{\eta=0.5}$$

### 7. 无量纲化
- 长度尺度：$\ell = \sqrt{\kappa_\eta / k_BT}$
- 时间尺度：$\tau = \ell^2 / D_v$
- 无量纲参数：$\tilde{E}_v^f = E_v^f / k_BT$, $\tilde{A} = A/k_BT$, $\tilde{B} = B/k_BT$, $\tilde{\kappa}_v = \kappa_v/\kappa_\eta$, $\tilde{\kappa}_\eta = 1$

---

## Parameters

### 模型参数（无量纲）

| 参数 | 符号 | 值 | 说明 |
|------|------|------|------|
| 空位迁移率 | $\tilde{M}_v$ | 1 | 无量纲 |
| 界面迁移率 | $\tilde{L}$ | 1 | 无量纲 |
| 梯度能量系数 | $\tilde{\kappa}_\eta$ | 1 | $\tilde{\kappa}_v = \tilde{\kappa}_\eta/2$ |
| 梯度能量系数 | $\tilde{\kappa}_v$ | 0.5 | |
| 约化空位形成能 | $\tilde{E}_v^f$ | 9.09 | $= E_v^f / k_BT$ |
| Landau 系数 | $\tilde{A}$ | 9.09 | |
| Landau 系数 | $\tilde{B}$ | 9.09 | |

### 对应物理参数

| 参数 | 值 | 说明 |
|------|------|------|
| 温度 $T$ | ≈ 1276 K | |
| 空位形成能 $E_v^f$ | 1 eV | |
| 热平衡空位浓度 $c_v^0$ | ≈ $1.13 \times 10^{-4}$ | $= \exp(-E_v^f/k_BT)$ |

### 数值参数

| 参数 | 值 |
|------|------|
| 时间步长 $\Delta\tilde{t}$ | $5 \times 10^{-5}$ |
| 网格（形核模拟） | 128 × 128, $\Delta\tilde{x} = 1$ |
| 网格（其他测试） | 256 × 256, $\Delta\tilde{x} = 0.5$ |
| 边界条件 | 周期性 |

### 辐照源参数

| 参数 | 值 | 说明 |
|------|------|------|
| $P_v^{casc}$ | 0.1, 0.25 | 级联空位产生速率（无量纲） |

---

## Experimental Data

本文为纯计算建模工作，无实验数据。但模型结果与经典理论进行了对比验证：

### KJMA 方程拟合（Stage II 形核期）
$$\rho = \rho_e[1 - \exp(-kt^3)]$$

| 参数 | $P_v^{casc} = 0.25$ | $P_v^{casc} = 0.1$ |
|------|------|------|
| $\rho_e$ | 0.278 | 0.259 |
| $k$ | $1.72 \times 10^{-4}$ | $7.93 \times 10^{-5}$ |

### Ostwald 熟化拟合（Stage III 长大期）
$$\rho = \rho_0(1 + t/\tau_1)$$

| 参数 | $P_v^{casc} = 0.25$ | $P_v^{casc} = 0.1$ |
|------|------|------|
| $\rho_0$ | 0.1885 | 0.1516 |
| $\tau_1$ | 230.05 | 371.73 |

### 形核速率
$$n_{void} = Jt$$

| $P_v^{casc}$ | 形核率 $J$ |
|------|------|
| 0.25 | 2.22 |
| 0.1 | 1.04 |

### Ostwald 熟化空洞数量衰减
$$n_{void} = n_0(1 + t/\tau_2)^{-m}$$

| 参数 | $P_v^{casc} = 0.25$ | $P_v^{casc} = 0.1$ |
|------|------|------|
| $n_0$ | 53.45 | 178.28 |
| $\tau_2$ | 331.15 | 34.92 |
| $m$ | 0.926 | 0.673 |

### 空洞生长幂律
$$\Delta R = \lambda t^n$$
- 指数 $n = 0.5$（扩散控制生长）
- $\lambda$ 值：$S_v = 100$: 0.268, $S_v = 200$: 0.349, $S_v = 300$: 0.412

---

## Key Findings

1. **模型成功再现 Gibbs-Thomson 效应**：空洞的平衡尺寸取决于周围空位浓度，高过饱和度下长大，低过饱和度下收缩。对于初始半径 ≈ 11.48 的空洞，约 5 倍过饱和度维持其平衡尺寸。

2. **Ostwald 熟化**：双空洞系统中，大空洞吸收空位长大，小空洞发射空位缩小，符合经典 Ostwald 熟化行为。

3. **Denuded zone 再现**：大空洞表面附近因大量吸收空位形成低浓度区，抑制新空洞形核，与辐照材料中自由表面/晶界附近的贫化区实验观测一致。

4. **三阶段空洞动力学**：成功模拟了完整的 孕育期→形核期→长大期 过程，空隙率和空洞密度演化与 KJMA 理论和 Ostwald 熟化理论定量吻合。

5. **辐照源强度效应**：更强的空位产生率缩短孕育期、增加形核率、提高最终空隙率。

6. **空洞生长幂律**：空洞半径增长遵循 $R \propto t^{0.5}$，与扩散控制生长一致。

---

## Relationships to Other Work

### 理论基础
- **Cahn & Hilliard** [17,18] — 梯度能量项，spinodal decomposition 理论
- **Allen & Cahn** [19] — 反相界理论，非保守场动力学
- **KJMA 理论** [22-24] — 形核动力学对比
- **经典形核理论** — 空洞形核率计算
- **反应速率理论** — 点缺陷平均浓度

### 相关相场模型
- **Millett et al.** — 同团队后续工作，多晶金属中空洞形核与长大（引入晶界）
- **Singer-Loginova & Singer** — 相场技术综述
- **Ahmed et al.** — 孔隙率对陶瓷晶粒长大的相场模拟

### 模型局限性（作者自述）
1. 未考虑间隙原子（interstitials）的作用
2. 模型参数未与具体材料性质匹配，仅用于验证模型
3. 忽略弹性效应 $\psi_{el}$
4. 仅二维模拟
5. 需要与 sharp-interface 模型进行渐近分析对比

### 后续扩展方向
1. 引入间隙原子物种
2. 参数标定：通过匹配 sharp-interface 模型确定 $L$、$A$、$B$ 等参数
3. 考虑晶界和沉淀相/基体界面对空洞形核长大的影响
4. 应力/温度梯度驱动下空洞迁移

## Relationships

- [[wiki/entities/CavitationalVoid|CavitationalVoid]] — void nucleation, Gibbs-Thomson stabilization, Ostwald ripening, and denuded-zone formation are modeled
- [[wiki/entities/PhaseFieldModeling|PhaseFieldModeling]] — the Cahn-Hilliard + Allen-Cahn dual-field phase-field framework is the central methodology
- [[wiki/concepts/RateTheoryFramework|RateTheoryFramework]] — phase-field results are benchmarked against classical nucleation and rate-theory predictions
- [[wiki/summaries/2008_Surh_VoidNucleationGrowthCoalescence|2008_Surh_VoidNucleationGrowthCoalescence]] — companion cluster-dynamics study of void nucleation, growth, and coalescence
- [[wiki/summaries/2011_Millett_PhaseFieldGasBubbleKinetics|2011_Millett_PhaseFieldGasBubbleKinetics]] — Millett (2011) extends this phase-field framework to include fission gas atom species
- [[wiki/summaries/2024_Aagesen_VacancyProductionPF|2024_Aagesen_VacancyProductionPF]] — later phase-field work on vacancy production and void evolution builds on this foundation

## Related Work
- [[wiki/summaries/2008_Surh_VoidNucleationGrowthCoalescence|2008_Surh_VoidNucleationGrowthCoalescence]] — Surh 用团簇动力学方法研究相同问题，是本文相场方法的对照
- [[wiki/summaries/2011_Millett_PhaseFieldGasBubbleKinetics|2011_Millett_PhaseFieldGasBubbleKinetics]] — Millett 在本文框架基础上扩展至包含裂变气体原子物种
- [[wiki/summaries/2024_Aagesen_VacancyProductionPF|2024_Aagesen_VacancyProductionPF]] — 后续相场工作，在空位产生和空洞演化方面延续了本文的方法论
- [[wiki/entities/PhaseFieldModeling|PhaseFieldModeling]] — 本文的 Cahn-Hilliard + Allen-Cahn 双场相场框架是相场建模方法的重要应用
- [[wiki/entities/CavitationalVoid|CavitationalVoid]] — 空洞形核、Ostwald 熟化和贫化区形成是本文模拟的核心物理
