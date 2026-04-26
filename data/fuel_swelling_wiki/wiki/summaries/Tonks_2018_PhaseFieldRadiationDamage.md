# Tonks 2018 - How to Apply the Phase Field Method to Model Radiation Damage

**论文信息**: Tonks, M.R., Cheniour, A., Aagesen, L. *Computational Materials Science* 147 (2018) 353–362.
**类型**: 方法论文/教程
**关键词**: phase field method, radiation damage, computational nuclear materials

## 摘要

本文系统介绍了如何将相场方法应用于模拟辐照损伤引起的微观组织演化。相场方法适用于预测约100 nm至100 μm尺度、微秒至年级时间尺度的辐照诱发组织演化。

文章首先概述了相场方法的基本框架：使用保守浓度变量 $c_i$（描述缺陷或溶质浓度）和非保守序参数 $\eta_j$（描述相或晶粒等不同区域），通过最小化系统自由能泛函来驱动组织演化。自由能泛函包含局部自由能密度 $f^{loc}$、梯度能量密度 $f^{grad}$ 和附加能量 $f^{add}$（如弹性能）。浓度变量遵循 Cahn-Hilliard 方程，序参数遵循 Allen-Cahn 方程。迁移率与扩散系数的关系为 $M_i = D_i / (\partial^2 f^{loc} / \partial c_i^2)$。

对于缺陷自由能表示，文章讨论了理想溶液模型和化合物能量形式化（CEF），包括缺陷形成能 $E_i^f$、Boltzmann 熵项和缺陷间交互作用参数 $L_{ij}$。对于空洞相，使用抛物线形式 $f^V = \frac{1}{2}\epsilon_V(1-c_v)^2 + c_i^2$；对于间隙原子环，使用 $f^L = f_0 + A[c_v^2 + (1-c_i)^2]$。

文章详细比较了三种处理扩展缺陷的相场模型：(1) WBM模型（Wheeler-Boettinger-McFadden），直接插值两相自由能但体相自由能贡献界面能；(2) KKS模型（Kim-Kim-Suzuki），分别处理两相浓度且化学势相等，消除了体相自由能对界面能的贡献；(3) GP模型（Grand Potential），通过Legendre变换在化学势空间求解，与KKS等价但计算效率更高。

通过一维空洞生长算例（Cu，$E_f = 0.98$ eV/atom，$V^a = 1.16 \times 10^{-2}$ nm³/atom，$T = 500$ K，$D_v = 2000$ nm²/ms），对比了三种模型的预测结果和计算效率：WBM模型最快，GP模型耗时为WBM的1.96倍，KKS模型为2.14倍。KKS和GP模型给出几乎相同的空洞生长动力学，而WBM模型预测的界面位置偏前且生长时间约为KKS的两倍。

## Key Equations

### 自由能泛函
$$F = \int_\Omega \left[ f^{loc}(\mathbf{c}, \boldsymbol{\eta}, T) + f^{grad}(\nabla\mathbf{c}, \nabla\boldsymbol{\eta}) + f^{add} \right] dV$$

### 梯度能量密度
$$f^{grad} = \sum_i \frac{\kappa_i}{2}|\nabla c_i|^2 + \sum_j \frac{\kappa_j}{2}|\nabla\eta_j|^2$$

### 弹性能密度
$$f^{add} = \frac{1}{2}\sigma(\mathbf{c},\boldsymbol{\eta}) : (\varepsilon^{el} - \varepsilon^0(\mathbf{c},\boldsymbol{\eta}))$$

### Allen-Cahn方程（序参数演化）
$$\dot{\eta}_j = -L_j \frac{\delta F}{\delta \eta_j}$$

### Cahn-Hilliard方程（浓度演化）
$$\dot{c}_i = \nabla \cdot M_i \nabla \frac{\delta F}{\delta c_i}$$

### 迁移率与扩散系数关系
$$M_i = \frac{D_i}{\partial^2 f^{loc} / \partial c_i^2}$$

### 理想溶液自由能（单亚点阵）
$$G^s(\mathbf{c}) = \sum_i E_i^f c_i - k_b T \left[ \sum_i c_i \ln(c_i) + c_A \ln c_A \right] + \sum_{i,j-i} \sum_j c_i c_j L_{ij}$$

### 空洞自由能
$$f^V = \frac{1}{2}\left[ \epsilon_V(1-c_v)^2 + c_i^2 \right]$$

### WBM局部自由能
$$f^{loc} = h(\eta)f^s(\mathbf{c},T) + (1-h(\eta))f^d(\mathbf{c},T) + Wg(\eta)$$

### KKS浓度约束
$$c_i = h(\eta)c_{i,s} + (1-h(\eta))c_{i,d}$$

### 含源汇的Cahn-Hilliard方程
$$\dot{c}_i = \nabla \cdot M_i \nabla \frac{\delta F}{\delta c_i} + k_i - \sum_{i,j} K_{ij}c_ic_j - k_i^2 D_i c_i$$

### arcdpa存活缺陷份额
$$\text{arcdpa} = n(E) \cdot \text{dpa}$$

### 切换函数
$$h_3(\eta) = 3\eta^2 - 2\eta^3, \quad h_5(\eta) = \eta^3(6\eta^2 - 15\eta + 10)$$

### 能垒函数
$$g_2(\eta) = \eta(1-\eta), \quad g_4(\eta) = \eta^2(1-\eta)^2$$

## Related Work
- [[wiki/entities/PhaseFieldModeling|PhaseFieldModeling]] — 本文是相场方法应用于辐照损伤的系统性教程
- [[wiki/summaries/OECD_NEA_2015_MultiscaleModelling|OECD_NEA_2015_MultiscaleModelling]] — 多尺度模拟报告，涵盖相场方法
- [[wiki/summaries/Li_2017_PhaseFieldReview|Li_2017_PhaseFieldReview]] — 相场方法在核燃料中的应用综述
- [[wiki/summaries/2017_Hu_RateTheory_PhaseField_Recrystallization_UMo|2017_Hu_RateTheory_PhaseField_Recrystallization_UMo]] — 相场方法与速率理论耦合应用于U-Mo
- [[wiki/summaries/2024_Aagesen_VacancyProductionPF|2024_Aagesen_VacancyProductionPF]] — 相场方法模拟空位产生
