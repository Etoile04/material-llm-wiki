# Yun et al. 2013 — GRASS-SST 在 U-Pu-Zr 金属燃料裂变气体行为模拟中的初步评估

**来源:** Yun, D., Rest, J., Hofman, G.L., Yacout, A.M. (2013). Journal of Nuclear Materials, 435, 153–163.

## 摘要

本文首次将 GRASS-SST（稳态与瞬态气体释放与肿胀）力学速率理论模型应用于 U-Pu-Zr 金属合金燃料的裂变气体行为模拟。该模型最初为 UO₂ 氧化物燃料开发，基于耦合非线性微分方程组描述裂变气体原子和气泡在晶内、晶面和晶棱处的浓度演化。

作者根据 U-Pu-Zr 燃料辐照后形成的三相区微观结构特征——外区 α-U 相（层状孔隙结构）、中间区（Zr 贫化区）和内区高温 γ-U 相——分别建模。α-U 区因密集的层状孔隙结构贡献了约 67–72% 的裂变气体释放，采用 2 μm 有效晶粒尺寸模拟其气体释放行为，结果与实验测量值（燃耗 >3 at.% HM 时约 70–80%）吻合良好。中间区和 γ-U 区通过 SEM 微观照片测量气泡尺寸分布进行验证，模拟与实验的气泡尺寸分布匹配良好，中间区气体致肿胀约 25%，γ-U 区约 35%。

参数敏感性研究表明：气体原子扩散系数显著影响气泡尺寸分布形态；静水应力升高导致气泡收缩和肿胀量显著降低（中间区）；双原子形核概率 Fn 影响气泡数密度和尺寸。γ-U 区的气体释放在 10 at.% HM 燃耗时仅约 0.3%，可忽略不计。作者强调，仅凭平均气泡尺寸无法有效约束参数空间，必须使用完整的气泡尺寸分布进行验证。

## Key Equations

### 气泡浓度演化方程

$$\frac{dC_i}{dt} = -a_i C_i^2 - b_i C_i + e_i$$

其中 $C_i$ 为第 $i$ 尺寸类气泡的浓度（数密度），$a_i$、$b_i$、$e_i$ 取决于各尺寸类的浓度：

$$a_i = a_i(C_i), \quad b_i = b_i(C_1, \ldots, C_N), \quad e_i = e_i(C_1, \ldots, C_N)$$

- $a_i$：第 $i$ 类气泡因同类合并而消失的速率
- $b_i$：第 $i$ 类气泡因与其他类合并及再溶解而消失的速率
- $e_i$：第 $i$ 类气泡因裂变气体产生、形核、合并和再溶解而增加的速率
- $N$ 为尺寸类总数

### 气体原子扩散系数

$$D_g = D_0 \exp\left(-\frac{Q}{kT}\right)$$

其中 $k = 1.987$ cal/(mol·K) 为气体常数。不同相区采用不同的 $D_0$ 和 $Q$ 值（见表），温度取各相区平均值。

### α-U 区气体释放等效模型

α-U 区的层状孔隙结构与氧化物燃料中晶界/晶棱连通孔隙的气体释放机制类似。通过采用小有效晶粒尺寸（~2 μm，接近层间距）将层状孔隙释放"等效"为晶棱气泡连通释放，从而复用 GRASS-SST 的氧化物燃料物理框架。

## 各相区关键参数

| 参数 | α-U 区 | 中间区 | γ-U 区 |
|------|--------|--------|--------|
| $D_0$ (cm²/s) | 2×10⁻³ | 7×10⁻⁴ | 1.1×10⁻⁴ |
| $Q$ (cal/mol) | 33,000 | 33,000 | 33,000 |
| $F_n$ | 1×10⁻⁵ | 1×10⁻⁸ | 0.001 |
| 晶粒尺寸 (μm) | 2 | 30 | 100 |
| 温度 (°C) | 600 | 650 | 727 |
| 气体释放 @10 at.% HM | ~67–72% | ~11% | ~0.3% |
| 气泡致肿胀 | — | ~25% | ~35% |

## 标签

`#GRASS-SST` `#kinetic_rate_theory` `#bubble_size_distribution` `#fission_gas_release` `#U-Pu-Zr` `#phase_zones` `#sensitivity_analysis` `#benchmarking`

## Related Work
- [[wiki/entities/UPuZrFuel|UPuZrFuel]] — fuel system modeled with three distinct phase zones
- [[wiki/concepts/RateTheoryFramework|RateTheoryFramework]] — GRASS-SST is a kinetic rate theory based model
- [[wiki/concepts/FissionGasReleaseModels|FissionGasReleaseModels]] — extends FGR modeling to metallic fuel
- [[wiki/summaries/1993_Rest_CavitationalSwellingAlphaUPuZr|1993_Rest_CavitationalSwellingAlphaUPuZr]] — Rest's earlier cavitational swelling model for α-U phase
- [[wiki/summaries/2022_Yun_CavitationalVoidSwelling|2022_Yun_CavitationalVoidSwelling]] — updated cavitational void swelling model
- [[wiki/summaries/2010_Karahan_FEAST_ThermoMechanical_MetallicFuel|2010_Karahan_FEAST_ThermoMechanical_MetallicFuel]] — FEAST-METAL, another metallic fuel FGR code
