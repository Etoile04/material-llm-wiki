# 空位和裂变气体气泡的空间分辨模型

## 元数据

| 字段 | 值 |
|------|-----|
| **标题** | A New Spatially Resolved Model for Defects and Fission Gas Bubbles in UO₂ |
| **作者** | L. Verma, L. Noirot, P. Maugis |
| **期刊** | Nuclear Instruments and Methods in Physics Research B 458 (2019) 151–158 |
| **年份** | 2019（接收 2018） |
| **Slug** | 2018_Verma_SpatiallyResolved_Defect_FGB_Model |
| **关键词** | 空间分辨模型, 裂变气体气泡, 空位扩散, 气泡聚并, Ostwald 熟化, UO₂, 定向迁移 |

## 中文摘要

本文提出了一种新的空间分辨模型，用于研究 UO₂ 中裂变气体气泡与点缺陷之间的相互作用。模型将模拟域离散为三类单元：0-cell（气泡内部）、1-cell（气泡-基体界面）、2-cell（固体基体），通过追踪每个单元的空位浓度 $C_v$ 和晶格原子浓度 $C_a$ 来模拟微观结构演化。

模型核心机制包括：(1) 基于菲克定律的空位扩散，采用 5 点差分（2D）或 7 点差分（3D）格式；(2) 气泡体积更新，考虑空位通量吸收和体积守恒修正；(3) 气泡中心迁移（非各向同性空位通量导致）；(4) 气泡重绘与聚并判据。

验证测试在 64×64 网格（256 nm × 256 nm 物理域）上进行，等温退火温度 1800°C。网格敏感性分析显示三种网格（64×64, 128×128, 256×256）的平均气泡半径相对偏差仅 1.5%。

关键演示：(1) 两气泡聚并——两个高压小气泡在空位过饱和条件下长大并合并为 19.7 nm 半径的大气泡；(2) Ostwald 熟化——大气泡以消耗小气泡为代价持续长大，小气泡消失；(3) 定向迁移——小气泡沿空位浓度梯度向大气泡迁移，验证了 Evans 提出的裂变气体释放机制。在 1 小时退火时间内，245 个小气泡中 32 个因聚并消失，平均半径从 0.72 nm 增长至 1.94 nm。

该模型为研究晶粒内气泡迁移及其对裂变气体释放的影响提供了定量工具。

## Related Work
- [[wiki/entities/FissionGasDiffusion|FissionGasDiffusion]] — 本文核心机制，裂变气体扩散与气泡演化
- [[wiki/concepts/GasBubbleCoalescence|GasBubbleCoalescence]] — 本文演示了气泡聚并和Ostwald熟化过程
- [[wiki/concepts/FissionGasReleaseModels|FissionGasReleaseModels]] — 本文模型可用于研究晶粒内气泡迁移对FGR的影响
- [[wiki/summaries/2011_Noirot_MARGARET|2011_Noirot_MARGARET]] — MARGARET代码的裂变气体模型，与本文同属UO₂裂变气体建模
- [[wiki/summaries/2011_Millett_PhaseFieldGasBubbleKinetics|2011_Millett_PhaseFieldGasBubbleKinetics]] — 裂变气体气泡动力学的相场模拟，与本文方法互补

## Key Equations

### 1. 空位扩散方程

$$\frac{\partial \tilde{C}_v}{\partial \tilde{t}} = \tilde{\nabla} \cdot \tilde{D}_v \nabla \tilde{C}_v$$

非量纲化后 $\tilde{D}_v = 1$。空位浓度以格点分数表示。

### 2. 固体单元空位浓度演化

$$\frac{C_v^{(p)}}{\Delta t} = \frac{D_v}{h^2} \sum_n \left[C_v^{(n)} - C_v^{(p)}\right]$$

其中 $h$ 为网格尺寸，$p$ 为当前单元，$n$ 为面邻居单元。

### 3. 界面单元空位浓度演化

$$\frac{C_a^{(p)}}{\Delta t} = \frac{D_v}{h^2} \sum_{n \in \text{2-cell neighbours}} \left[C_v^{(n)} - C_v^{eq}\left(\kappa^{(p)}, P_b^{(p)}\right)\right]$$

其中 $C_v^{eq}$ 取决于界面曲率 $\kappa$ 和气泡内压力 $P_b$。

### 4. 气泡平衡空位浓度

$$C_v^{eq} = C_{v,0} \exp\left(\frac{\gamma \Omega}{kT r} - \frac{P_b \Omega}{kT}\right)$$

其中 $\gamma$ 为表面能，$\Omega$ 为原子体积，$r$ 为气泡半径。

### 5. 气泡体积更新

$$V_b = V_b^{(0\text{-cells})} + \sum_{\text{interface cells}} (1 - C_a) V_{cell} + \alpha + V_{comp}$$

包含原子守恒修正 $\alpha$ 和补偿项 $V_{comp}$。

## 关键物理参数

| 参数 | 值 | 非量纲值 |
|------|-----|---------|
| 空位形成能 $\varepsilon_v$ | 2.47 eV | 2.47 |
| UO₂ 格点体积 $\Omega$ | 40.9 × 10⁻³⁰ m³ | 4.09 × 10⁻² |
| 空位扩散系数 $D_v$ | 1.62 × 10⁻¹² m²/s | 1 |
| 表面张力 $\gamma_0$ (1800°C) | 0.24518 J/m² | 1.532 |
| 网格尺寸 $h$ | 4 nm | 4 |
| 退火温度 | 1800°C | — |
| $kT$ | 2.86 × 10⁻²⁰ J | 0.1788 |
| 自扩散系数 $D_U$ | $6.5 \times 10^{-5} \exp(-5.6 \text{ eV}/kT)$ m²/s | — |
