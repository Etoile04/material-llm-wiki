# Ke (2023) - 核结构材料微观结构建模综述

**论文**: Microstructure Modeling for Nuclear Structural Materials  
**期刊**: Computational Materials Science 230 (2023) 112503  
**作者**: Jia-Hong Ke

## 摘要

本文综述了核结构材料微观结构建模的方法、应用和现状，重点讨论了导致辐照诱导硬化与脆化的微化学和微观结构特征的模拟。文章系统介绍了四种跨尺度方法：速率理论(rate theory)、团簇动力学(cluster dynamics)、相场(phase field)和动力学蒙特卡罗(kMC)模型。

在速率理论部分，文章讨论了点缺陷产生率、复合率、缺陷-尾闾交互作用的建模框架。团簇动力学部分涵盖了从平均场速率方程到空间分辨团簇动力学的发展，包括缺陷团簇形核、长大和被尾闾吸收的过程。相场部分介绍了WBM、KKS和Grand Potential三种主要模型框架在辐照损伤模拟中的应用，包括空洞生长、析出动力学和位错环演化。kMC部分讨论了从晶格kMC到k-ART等方法的进展。

文章特别强调了核结构材料（尤其是奥氏体不锈钢）基本热力学-动力学数据严重缺乏的问题，以及磁性激发对铁基合金相稳定性和缺陷-溶质相互作用的复杂影响。最后讨论了混合多尺度模型（空间分辨团簇动力学与相场耦合）和机器学习在核材料研究中的机遇。

## Key Equations

$$\frac{dC_i}{dt} = G_i - K_{iv}C_iC_v + \sum_j K_{js}C_j - K_{is}C_i$$

速率理论基本方程，描述点缺陷浓度随时间的演化。

$$f(c, \eta) = f_{chem}(c) + \sum_i \Delta g_i h(\eta_i) + \sum_{i,j} \kappa_{ij} \nabla \eta_i \cdot \nabla \eta_j$$

KKS相场自由能泛函，包含化学自由能、结构序参数和梯度能量项。

$$\frac{\partial \eta_i}{\partial t} = -L \frac{\delta F}{\delta \eta_i}$$

Allen-Cahn方程，描述序参数的时间演化。

## Related Work
- [[wiki/summaries/Li_2017_PhaseFieldReview|Li_2017_PhaseFieldReview]] — 相场方法综述，与本文互补
- [[wiki/summaries/Tonks_2018_PhaseFieldRadiationDamage|Tonks_2018_PhaseFieldRadiationDamage]] — 相场辐照损伤模拟
- [[wiki/concepts/RateTheoryFramework|RateTheoryFramework]] — 本文涵盖速率理论方法
- [[wiki/summaries/2008_Surh_VoidNucleationGrowthCoalescence|2008_Surh_VoidNucleationGrowthCoalescence]] — 速率理论空洞形核生长
- [[wiki/summaries/2023_Ke_MicrostructureModeling|2023_Ke_MicrostructureModeling]] — 同一论文的替代slug
