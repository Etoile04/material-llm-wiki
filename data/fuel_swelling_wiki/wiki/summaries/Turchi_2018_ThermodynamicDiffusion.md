# Turchi 2018 - Nb-Ti-U-Zr合金的热力学、扩散和物理性能

**文献**: P. E. A. Turchi, "Thermodynamic, Diffusion, and Physical Properties of Nb-Ti-U-Zr Alloys", LLNL-TR-752282, June 2018.

## 摘要

本报告系统汇编了Nb-Ti-U-Zr合金体系的热力学、扩散和物理性能数据，为相场建模(PFM)等多尺度模拟提供关键输入参数。报告覆盖四个二元体系(Nb-Ti, Nb-Zr, Ti-Zr, Nb-U)的相图和CALPHAD热力学参数、液相和bcc固相的原子迁移率数据库，以及Nb-Zr合金的弹性常数。

热力学部分提供了各二元系的Redlich-Kister相互作用参数，包括液相、bcc相、hcp相和ω相的模型参数。通过CALPHAD方法预测了各体系的平衡和亚稳相图，包括T0曲线和溶解度间隙。Nb-Ti体系的bcc亚稳溶解度间隙临界温度约为511°C(50 at.% Ti处)，Nb-Zr体系的bcc溶解度间隙临界温度约为977°C(41.4 at.% Zr处)。

扩散部分采用Liu等人的预测方程计算了液相自扩散和杂质扩散系数，并汇编了bcc相的原子迁移率参数(Q = a + RT ln(b)形式)。液相扩散模型基于Goldsmith原子半径和熔点温度，K₀参数考虑了固相结构类型(bcc=1, hcp=2, fcc=3)。固相扩散参数基于DICTRA评估，覆盖Nb-Ti, Nb-Zr, Nb-U, Ti-Zr四个二元体系。

弹性常数部分采用Wang等人的CALPHAD模型，给出了Nb-Zr合金C₁₁、C₁₂、C₄₄随温度和成分变化的多项式表达式，并由此计算体积模量、剪切模量、杨氏模量和泊松比。报告还包含纯元素Nb、Ti、U、Zr的基本物理性能数据表，以及液态金属粘度的Kaptay统一方程计算结果。

## Key Equations

液相扩散系数预测方程:
$$D_{A,B} = D_0 \frac{d_B}{d_A} \exp\left[-0.17 \cdot T_{Melt} \cdot (16 + K_0) / T\right]$$

原子迁移率Redlich-Kister展开:
$$\Delta G_i = c_A Q_i^A + c_B Q_i^B + c_A c_B {}^0Q_i^{A,B} + c_A c_B (c_A - c_B) {}^1Q_i^{A,B}$$

弹性常数成分依赖:
$$C_{lm} = x_{Nb} {}^0C_{lm}^{Nb} + x_{Zr} {}^0C_{lm}^{Zr} + x_{Nb} x_{Zr} \sum_p {}^pC_{lm}^{Nb,Zr} (x_{Zr} - x_{Nb})^p$$

体积模量: $B = (C_{11} + 2C_{12}) / 3$

## Related Work
- [[wiki/concepts/IrradiationDrivenVsIntrinsicDiffusion|IrradiationDrivenVsIntrinsicDiffusion]] — 汇编了热力学扩散数据与原子迁移率参数
- [[wiki/summaries/Lu_2018_CALPHAD_UFuels|Lu_2018_CALPHAD_UFuels]] — 铀燃料CALPHAD热力学建模，与本文互补
- [[wiki/summaries/Xiong_2013_ThermodynamicUZr|Xiong_2013_ThermodynamicUZr]] — U-Zr体系热力学CALPHAD评估
- [[wiki/summaries/Zhou_2023_ThermoDiffDatabaseU|Zhou_2023_ThermoDiffDatabaseU]] — 铀基合金热力学与扩散数据库的扩展
- [[wiki/summaries/Piro_2021_ThermodynamicFuelCodes|Piro_2021_ThermodynamicFuelCodes]] — 热力学与燃料代码耦合综述
