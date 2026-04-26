# Phase-Field Modeling of Cavity Growth and Dislocation Climb

**论文**: Dabas et al. (2025), *Acta Materialia* 293, 121040
**DOI**: https://doi.org/10.1016/j.actamat.2025.121040
**关键词**: 相场、空腔、位错、空位扩散、弹性相互作用、辐照

## 摘要

本文提出了一种原创的相场模型，耦合空腔生长、位错攀移和空位扩散，自然地处理了物体间的弹性相互作用，并通过变分约束保证空位在空腔表面和位错核心交换时物质守恒。模型还提出了一种高效的谱方法，用于快速获得空位浓度场的稳态解。

模型引入三个场变量：空腔相场$\eta$（0=基体，1=空腔）、位错相场$\phi$（整数=位错环的攀移面数）、空位浓度场$c$。通过守恒场$\Psi = \eta + b\phi\delta(x-x_0) + c$保证物质守恒。动力学方程采用Allen-Cahn（$\eta$, $\phi$）和Cahn-Hilliard（$\Psi$）框架。

模型通过解析解验证：空腔收缩动力学与扩散控制理论的MSZ解一致，位错攀移速率与经典解吻合。应用于退火辐照铝样品的模拟，揭示了位错诱导弹性相互作用对空腔闭合动力学的非平凡效应。

## Key Equations

### 守恒场定义
$$\Psi(\mathbf{r}, t) = \eta(\mathbf{r}, t) + b\phi(y, z, t)\delta(x - x_0) + c(\mathbf{r}, t)$$

- $b$：伯格斯矢量幅值，$\delta$：Dirac函数约束位错在攀移面$x=x_0$

### 总自由能泛函
$$\mathcal{F} = \int_V \left[ f_{cav}(\eta) + f_{dis}(\phi) + f_{chem}(c, \eta) + f_{el}(\varepsilon_{ij}, \eta, \phi, c) \right] dV$$

### 空腔自由能密度
$$f_{cav}(\eta) = \frac{3\gamma}{4\xi} \cdot 16\eta^2(1-\eta)^2 + \xi|\nabla\eta|^2$$

- $\gamma$：各向同性表面能（J·m⁻²），$\xi$：漫表面宽度（m）

### 空位平衡浓度
$$c_0 = \exp\left(-\frac{E_f}{k_B T}\right)$$

### 空位扩散系数
$$D_v = D_0 \exp\left(-\frac{E_m}{k_B T}\right)$$

### 空腔收缩速率（局部平衡近似，2D）
$$v = \frac{-D_v \left(c_0 - c_\infty - \frac{M\gamma}{R}\right)}{R \ln(R_\infty / R)}$$

### Al中空位参数
- 形成能 $E_f = 0.67$ eV，迁移能 $E_m = 0.61$ eV
- 指前因子 $D_0 = 1 \times 10^{-5}$ m²·s⁻¹
- 原子体积 $\Omega = 16.6$ ų，弛豫体积 $V^* = -0.38\Omega$

## Related Work
- [[wiki/entities/PhaseFieldModeling|PhaseFieldModeling]] — 本文提出耦合空腔-位错-扩散的原创相场模型
- [[wiki/summaries/2022_Yun_CavitationalVoidSwelling|2022_Yun_CavitationalVoidSwelling]] — 空洞肿胀的率理论建模
- [[wiki/summaries/2022_Qian_CavitationalVoidSwellingU10Zr|2022_Qian_CavitationalVoidSwellingU10Zr]] — U-10Zr空洞肿胀模拟
- [[wiki/summaries/2024_Aagesen_VacancyProductionPF|2024_Aagesen_VacancyProductionPF]] — 空位产生的相场模型
- [[wiki/entities/CavitationalVoid|CavitationalVoid]] — 空腔生长与位错攀移的耦合建模
