# Hirschhorn et al. 2020 — 利用定量相场建模重新审视 U-Zr 扩散偶实验

> **论文**: Reexamination of a U-Zr diffusion couple experiment using quantitative phase-field modeling and sensitivity analysis
> **期刊**: Journal of Nuclear Materials 529 (2020) 151929
> **作者**: Jacob Hirschhorn, Michael Tonks, Assel Aitkaliyeva, Cynthia Adkins
> **DOI**: 10.1016/j.jnucmat.2019.151929

## 摘要

本文基于 Kim-Kim-Suzuki (KKS) 相场公式建立了 U-Zr 二元合金 β（四方相）和 γ（体心立方相）的定量相场模型，用于重新审视 Petri 和 Dayananda 发表的 U-Zr 扩散偶实验数据。扩散偶由纯 U（β 相）与 U-20Zr（γ 相，名义 at%）组成，在 750°C 下退火 16.5 小时。

模型采用 Cahn-Hilliard (CH) 方程描述 Zr 原子分数的守恒演化，Allen-Cahn 方程描述 γ 相分数的非守恒演化。通过 DAKOTA 优化工具拟合了 β 和 γ 相的 CH 迁移率（$M_\beta$ 和 $M_\gamma$），以多项式形式表示，其与实验成分分布的拟合 $R^2 = 0.989$。通过 Boltzmann-Matano (BM) 分析计算了互扩散系数分布，模拟得到的 β 和 γ 相平均有效互扩散系数分别为 $67 \times 10^{-15}$ 和 $33 \times 10^{-15}$ m²/s，与实验值 60 和 $30 \times 10^{-15}$ m²/s 吻合良好。

敏感性分析表明：(1) 动力学参数（CH 迁移率）远比界面能（$\sigma$）更具影响力；(2) γ 相动力学参数的影响大于 β 相，这与 γ 相较宽的溶解度范围和扩散限制行为有关；(3) 用户定义参数（相迁移率 $L$、界面宽度 $\ell$）可选取使模型主要响应实验数据。研究结论指出成分依赖性对于准确描述 β 和 γ 相的扩散行为至关重要，建议优先收集相动力学数据。

## Key Equations

1. **Cahn-Hilliard 方程**（守恒场 $c$ 的演化）：
   $$\frac{\partial c}{\partial t} = \nabla \cdot M \nabla \frac{\delta F}{\delta c}$$
   其中 $M$ 为 CH 迁移率，$F$ 为自由能泛函。

2. **Allen-Cahn 方程**（相场 $\gamma$ 的演化）：
   $$\frac{\partial \gamma}{\partial t} = -L \frac{\delta F}{\delta \gamma}$$
   其中 $L$ 为相迁移率。

3. **CH 迁移率分解**：
   $$M = (1-h) M_\beta + h M_\gamma$$
   $$M_\beta = c_\beta(1-c_\beta)[8 \times 10^{-19} c_\beta^2 + 1 \times 10^{-23}]$$
   $$M_\gamma = c_\gamma(1-c_\gamma)[1.1 \times 10^{-1}(0.186 - c_\gamma)^{24} + 1 \times 10^{-22}]$$

4. **界面参数与自由能关系**：
   $$\kappa = \frac{3\sigma\ell}{a}, \quad w = \frac{6a\sigma}{\ell}$$
   其中 $\sigma = 1$ J/m²，$\ell = 10$ μm，$a = 2.94$。

5. **互扩散系数（BM 分析）**：
   $$\tilde{D} = -\frac{1}{2t} \frac{\int_{c_L}^{c(x)} (x - x_M) dc}{dc/dx}\bigg|_{c(x)}$$

## 相关页面

- [[wiki/summaries/2020_Hirschhorn_UZr_DiffusionCouple_PF|Hirschhorn 2019 组分再分布]]
- [[wiki/entities/PhaseFieldModeling|相场建模]]
- [[wiki/concepts/ConstituentRedistribution|组分再分布]]

## 参数提取

→

## Related Work
- [[wiki/summaries/2019_Hirschhorn_PhaseFieldRedistribution_UZr|2019_Hirschhorn_PhaseFieldRedistribution_UZr]] — 同一作者的U-Zr组分再分布相场模型
- [[wiki/summaries/2021_Hirschhorn_CALPHAD_BISON_Redistribution|2021_Hirschhorn_CALPHAD_BISON_Redistribution]] — 后续工作将CALPHAD与BISON耦合用于组分再分布
- [[wiki/summaries/2018_Turchi_ThermodynamicDiffusion|2018_Turchi_ThermodynamicDiffusion]] — U-Zr热力学与扩散系数的CALPHAD评估
- [[wiki/summaries/1996_Hofman_TemperatureGradientRedistribution_UZr|1996_Hofman_TemperatureGradientRedistribution_UZr]] — U-Zr温度梯度驱动再分布的早期实验
- [[wiki/concepts/ConstituentRedistribution|ConstituentRedistribution]] — 组分再分布机制的概念综述
- [[wiki/concepts/SoretEffectInMetallicFuels|SoretEffectInMetallicFuels]] — Soret效应驱动的Zr迁移机制 
