# Michel et al. (2022) - 燃料微观力学

**论文**: Fuel Micromech  
**期刊**: Journal of Nuclear Materials 572 (2022) 154034  
**作者**: B. Michel, M. Welland, N. Ofori-Opoku et al.

## 摘要

本文综述了核燃料微观力学建模的最新进展，涵盖了从原子尺度到宏观尺度的多尺度方法。文章首先介绍了UO₂燃料的弹塑性力学行为，包括基于晶体塑性理论建立的强化模型。作者通过分子动力学和离散位错动力学模拟，系统计算了UO₂中不同滑移系统之间的位错相互作用强化系数（共26个α系数），为晶体塑性模拟提供了关键参数。

在辐照损伤力学方面，文章描述了分子动力学模拟揭示的UO₂和MOX燃料中辐照损伤演化的五个阶段：(1)点缺陷产生，(2)点缺陷聚集成簇，(3)Frank位错环形核，(4)通过Shockley不全位错转化为完美位错环，(5)重组为林位错网络。弹性模量随辐照剂量变化呈现约13%体积模量下降和约17.5%剪切模量下降的趋势。

文章还讨论了裂变气体气泡压力的分子动力学研究、UO₂/Xe界面特性、相场晶体(PFC)方法在缺陷生成和断裂力学中的应用，以及多维燃料性能代码ALCYONE中微观-宏观耦合的FE²方法。特别强调了纳米孔隙率对弹性性能的表面/界面效应以及温度对气泡内压力和肿胀影响不大的重要发现。

## 关键参数

- UO₂杨氏模量E = 385 GPa，泊松比ν = 0.23
- 26个位错强化系数α₀'到α₂₀*
- 断裂韧度Gc ≈ 1 J/m²
- 辐照后体积模量下降~13%，剪切模量下降~17.5%

## Key Equations

$$\tau_c = \alpha \mu b \sqrt{\rho}$$

位错强化准则，其中α为强化系数，μ为剪切模量，b为Burgers矢量，ρ为林位错密度。

$$F[\rho] = \int (f_{ideal} + f_{excess} + f_{external}) dV$$

相场晶体(PFC)自由能泛函。

$$f_{excess} = -\frac{1}{2} \int \int \delta\rho(V) \cdot C(V, V'; \tau) \cdot \delta\rho(V') dV dV'$$

PFC过剩自由能密度。

## Related Work
- [[wiki/summaries/Ke_2023_MicrostructureModeling|Ke_2023_MicrostructureModeling]] — 核材料微观结构建模综述，涵盖多尺度方法
- [[wiki/summaries/Li_2017_PhaseFieldReview|Li_2017_PhaseFieldReview]] — 相场方法综述
- [[wiki/summaries/Hales_2016_BISON_TheoryManual|Hales_2016_BISON_TheoryManual]] — BISON燃料性能代码理论手册
- [[wiki/summaries/Michel_2022_FuelMicromech|Michel_2022_FuelMicromech]] — 同一论文的替代slug
- [[wiki/concepts/SwellingMechanisms|SwellingMechanisms]] — 纳米孔隙率对肿胀的影响
