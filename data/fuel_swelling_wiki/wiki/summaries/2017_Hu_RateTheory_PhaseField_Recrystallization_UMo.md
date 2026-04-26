# 辐照诱导 UMo 燃料再结晶的率理论-相场耦合模型 (2017)

**Authors**: Shenyang Hu, Vineet Joshi, Curt A. Lavender
**Year**: 2017 | **Journal**: JOM 69(12), 2554–2562
**DOI**: 10.1007/s11837-017-2611-4
**Slug**: 2017_Hu_RateTheory_PhaseField_Recrystallization_UMo

## 中文摘要

本文提出了一种耦合空间依赖率理论与相场方法的辐照诱导再结晶模型，用于研究 UMo 核燃料中微观结构和辐照条件对再结晶动力学的影响。模型整合了晶内气泡与间隙环演化的率理论方程以及再结晶区域演化的相场模型。

率理论部分将 Xe 浓度、间隙原子浓度、晶内气泡密度/半径/含气量以及间隙环密度等场变量设为空间和时间相关函数，以研究非均匀微观结构对缺陷演化的影响。间隙原子扩散系数比 Xe 高约 5 个数量级，采用首次通过法（First Passage Method）求解一维扩散方程，显著提升了数值效率。

相场模型将再结晶视为在间隙环密度超过临界值处发生的二阶相变，仅需一个序参量 η(r,t) 描述粗晶与再结晶区之间的界面传播。自由能密度函数包含了间隙环密度的依赖关系，当间隙环密度增大时粗晶相失稳，驱动再结晶前沿从晶界向晶内推进。

一维双晶和二维多晶模拟结果表明：(1) 大晶粒中的再结晶启动早于小晶粒；(2) 再结晶体积分数随晶粒尺寸增大而降低；(3) 预测的再结晶动力学与实验结果一致；(4) 再结晶动力学可用修正 Avrami 方程描述，但其参数强烈依赖于晶粒尺寸。模型成功复现了晶粒尺寸对气泡密度、含气量和气泡半径的影响。主要局限是未包含再结晶区内的晶间气泡演化模型。

**与 JSRT 项目的关联**：本文的率理论-相场耦合策略展示了如何将率理论的点缺陷演化与宏观相变（再结晶）通过临界条件桥接，为金属燃料肿胀模型中考虑微观组织演变提供了方法论参考。首次通过法处理大扩散系数差异的思路值得借鉴。

## Key Equations

### 间隙原子演化
$$\frac{\partial c_{\text{int}}(\mathbf{r},t)}{\partial t} = \nabla \cdot D_{\text{int}} \nabla c_{\text{int}} + \dot{g}_{\text{int}}(\mathbf{r},t) - D_{\text{int}} Z_{iI1} \rho_{\text{loop}} c_{\text{int}} - D_{\text{int}} Z_{iI2} \rho_{\text{disl}} c_{\text{int}}$$

### 间隙环密度演化
$$\frac{\partial \rho_{\text{loop}}(\mathbf{r},t)}{\partial t} = \frac{2\pi D_{\text{int}} Z_{iI1} N c_{\text{int}}(\mathbf{r},t)}{|\mathbf{b}|}$$

### 相场再结晶方程
$$\frac{\partial \eta(\mathbf{r},t)}{\partial t} = -L \frac{\delta G(\eta, \rho_{\text{loop}})}{\delta \eta}$$

### 自由能密度
$$f = 4\eta^2(1-\eta)^2 - \bar{\rho}_0 \left(\eta^2 - \eta + 0.2\eta^3\right)$$

其中 $\bar{\rho}_0$ 为归一化间隙环密度，依赖临界间隙环密度 $\rho_{\text{crit}}$。

### 修正 Avrami 方程
$$V_{Rx} = 1 - \exp\left[-k(F_D - F_{D0})^n\right]$$

### 间隙原子净生成率
$$\dot{g}_{\text{int}}(\mathbf{r},t) = \gamma_0 \frac{d(c_b n_b)}{dt}$$

## 模型假设
- 空位浓度在基体中近似为零（被间隙原子复合和过压气泡快速消除）
- 间隙环在晶界处形核，核密度为常数 N
- 间隙原子以 [110] 哑铃构型沿 ⟨110⟩ 方向迁移（bcc UMo）
- 再结晶视为二阶相变，由局部间隙环密度驱动
- 再结晶区内晶内气泡不稳定，Xe 原子溶解并扩散

## Related Work
- [[wiki/entities/RateTheory|RateTheory]] — 本文将空间依赖率理论用于Xe/间隙原子/气泡演化
- [[wiki/entities/PhaseFieldModeling|PhaseFieldModeling]] — 本文用相场方法描述再结晶二阶相变
- [[wiki/entities/Recrystallization|Recrystallization]] — 本文核心现象，UMo燃料的辐照诱导再结晶
- [[wiki/summaries/2016_Hu_GrainMorphologyGasBubbleUMo|2016_Hu_GrainMorphologyGasBubbleUMo]] — 同一作者组，Booth扩展模型研究晶粒形态对气泡肿胀的影响
- [[wiki/summaries/2013_Kim_RecrystallizationFGBSwellingUMo|2013_Kim_RecrystallizationFGBSwellingUMo]] — UMo再结晶与气泡肿胀的实验关联研究
- [[wiki/summaries/2018_Liang_3DPhaseFieldIntragranularBubbleUMo|2018_Liang_3DPhaseFieldIntragranularBubbleUMo]] — UMo晶内气泡的三维相场模拟
