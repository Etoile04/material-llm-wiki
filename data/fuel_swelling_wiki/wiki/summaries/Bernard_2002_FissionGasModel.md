# Bernard_2002_FissionGasModel - 中文摘要

**论文标题**: COPERNIC/FBR: A fuel performance code for the modeling of fission gas release in oxide and MOX fuels

**作者**: L.C. Bernard, C. Delafoy, P. Blanpain

**期刊/来源**: Journal of Nuclear Materials (2002)

## 摘要

本文介绍了核燃料性能分析程序COPERNIC中的裂变气体行为模型。该模型针对UO₂和MOX燃料在稳态和瞬态条件下的裂变气体释放行为进行建模。模型采用多尺度方法，同时描述晶内和晶界两个尺度的气体行为。

在晶内尺度，模型考虑了三种扩散机制：(1) 纯热激活扩散，(2) 辐照增强扩散，(3) 无热辐照扩散。裂变气体原子的扩散系数为三项之和。晶内气泡通过形核-生长-重溶解（resolution）机制演化，其中重溶解由裂变碎片与气泡的相互作用驱动。

在晶界尺度，气体原子通过体扩散到达晶界后，在晶界气泡中聚集。当晶界气泡达到饱和并互联形成通路时，气体释放到间隙。模型还考虑了高燃耗条件下高燃耗结构(HBS)的形成及其对气体行为的特殊影响。

模型在大量辐照实验数据（包括UO₂和MOX燃料）上进行了验证，覆盖了广泛的燃耗范围（最高超过70 GWd/tU），结果表明模型预测与实验数据吻合良好。

## Key Equations

- 有效扩散系数: $D_{eff} = D_{th} + D_{irr} + D_{ah} = 2.0 \\times 10^{-20} \\exp\\left(-\\frac{36800}{T}\\right) + 6.0 \\times 10^{-36} \\dot{F}^{0.5} \\exp\\left(-\\frac{36800}{T}\\right) + 5.0 \\times 10^{-39} \\dot{F}$
- 重溶解速率: $b = \\frac{4\\pi R_c^2 \\eta \\dot{F}}{N_n}$
- 气泡内压力(理想气体): $p = \\frac{nkT}{\\frac{4}{3}\\pi r^3 - nb}$
- 气体产额: $Y_{FG} = Y_{Xe} + Y_{Kr} \\approx 0.30$ atoms/fission


## Related Work
- [[wiki/concepts/FissionGasReleaseModels|FissionGasReleaseModels]] — COPERNIC裂变气体释放模型
- [[wiki/summaries/2002_Bernard_FissionGasModel|2002_Bernard_FissionGasModel]] — 同一论文的替代slug
- [[wiki/summaries/Hales_2016_BISON_TheoryManual|Hales_2016_BISON_TheoryManual]] — BISON理论手册包含裂变气体释放模型
- [[wiki/summaries/2011_Noirot_MARGARET|2011_Noirot_MARGARET]] — MARGARET裂变气体模型，同为法国燃料性能代码
- [[wiki/summaries/2001_Rest_GRSIS_FissionGasMetallic|2001_Rest_GRSIS_FissionGasMetallic]] — 金属燃料裂变气体模型对比
