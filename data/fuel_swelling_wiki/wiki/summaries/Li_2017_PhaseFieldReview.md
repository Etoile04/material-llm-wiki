# Li 2017 - 相场方法在预测辐照核材料微观结构与性能演化中的应用综述

**文献**: Y. Li, S. Hu, X. Sun, M. Stan, "A review: applications of the phase field method in predicting microstructure and property evolution of irradiated nuclear materials", npj Computational Materials 3:16 (2017).

## 摘要

本文系统综述了相场(PF)方法在预测辐照核材料微观结构演化及其对力学、热学和磁性能影响中的应用。核燃料和结构材料在强辐照和高温极端环境下发生复杂的微观结构变化，理解这些变化对先进核材料设计至关重要。

文章首先概述了辐照条件下缺陷演化的重要物理机制和模拟挑战。PF方法基于热力学基本定律和缺陷动力学，具有无需预先假设微观结构形态、无需显式追踪界面位置、可高效表示多物理多尺度过程等优势。PF模型按自由能构造分为四类：Model 1(CH)仅浓度场、Model 2(GL/AC)仅序参量场、Model 3(WBM)混合场同浓度、Model 4(KKS)混合场异浓度。

综述覆盖的辐照诱导微观结构演化现象包括：(1)气泡演化——包括气泡均匀/非均匀形核、辐射诱导溶解、弹性相互作用；(2)空洞形成与演化——在单晶和多晶金属中的形核和生长，空洞贫化区形成；(3)空洞/气泡超晶格形成——弹性相互作用和SIA一维迁移均可导致超晶格，当D_SIA/D_v > 5000时开始形成；(4)空洞迁移——温度梯度驱动，Soret效应，迁移速度与空洞半径成反比；(5)SIA位错环生长——盘状{100}位错环的强各向异性能描述；(6)氢化物析出——锆合金中γ-氢化物的形貌由界面能和弹性能最小化决定；(7)辐照诱导偏析和析出；(8)晶粒生长和再结晶。

文章还讨论了PF方法在预测微观结构-性能关系方面的应用，包括热导率退化、辐照肿胀和硬化。最后分析了PF方法的优势（定性定量描述复杂3D微观结构）和局限性（形核处理困难、参数获取挑战、大尺度计算需求）。

## Key Equations

系统总自由能泛函:
$$F = \int_V [f_{ch}(\mathbf{c}, \boldsymbol{\eta}) + f_{grad}(\mathbf{c}, \boldsymbol{\eta}) + f_{lr}(\mathbf{c}, \boldsymbol{\eta})] dV$$

梯度能量密度:
$$f_{grad}(\mathbf{c}, \boldsymbol{\eta}) = \sum_m \frac{\kappa_{c_m}}{2} (\nabla c_m)^2 + \sum_n \frac{\kappa_{\eta_n}}{2} (\nabla \eta_n)^2$$

Cahn-Hilliard方程(浓度场演化):
$$\frac{\partial c_i}{\partial t} = \nabla \cdot \sum_j M_{ij} \nabla \frac{\delta F}{\delta c_j} + \dot{g}_i + \dot{\gamma}_i + \dot{S}_i$$

Allen-Cahn方程(序参量演化):
$$\frac{\partial \eta_\rho}{\partial t} = -L_\rho \frac{\delta F}{\delta \eta_\rho} + \xi_\rho$$

缺陷产生率: $\dot{g}_i = G_{NRT}(1 - \Omega_R)(1 - \theta_i)$

空位-间隙复合率: $\dot{\gamma}_i = \mu_R D_{int} c_{vac} c_{int}$

缺陷汇吸收率: $\dot{S}_i = -k_i^2 D_i c_i$

## Related Work
- [[wiki/summaries/Ke_2023_MicrostructureModeling|Ke_2023_MicrostructureModeling]] — 核材料微观结构建模综述，与本文互补
- [[wiki/summaries/Tonks_2018_PhaseFieldRadiationDamage|Tonks_2018_PhaseFieldRadiationDamage]] — 相场辐照损伤
- [[wiki/summaries/2009_Rokkam_PhaseFieldVoidNucleationGrowth|2009_Rokkam_PhaseFieldVoidNucleationGrowth]] — 相场空洞形核生长
- [[wiki/concepts/RateTheoryFramework|RateTheoryFramework]] — PF方法与速率理论框架对比
- [[wiki/summaries/2022_Aagesen_PFBubbleInterconnection|2022_Aagesen_PFBubbleInterconnection]] — 相场气泡互连
- [[wiki/summaries/Li_2017_PhaseFieldReview|Li_2017_PhaseFieldReview]] — 同一综述的替代slug
