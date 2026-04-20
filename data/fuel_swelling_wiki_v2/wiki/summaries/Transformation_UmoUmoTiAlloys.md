# 辐照诱发超晶格形成中的相变机制

> Aagesen, Zhang, Jiang, Gan (2025). Phase transformation mechanism in irradiation-induced superlattice formation. *Idaho National Laboratory, INL/EXT-25-82621.*

## 摘要

本研究利用原子动力学蒙特卡洛（AKMC）模拟，以钼（Mo）为模型材料，系统研究了辐照下空洞超晶格（Void Superlattice）形成的相变机制。模型基于SIA沿⟨111⟩方向的1D各向异性扩散，考虑Frenkel对的产生、空位-SIA复合和阱吸收。在80a₀×80a₀×80a₀的超胞中（1,024,000格点），模拟了773 K和873 K下10⁻²–10 dpa/s剂量率范围的超晶格形成。

关键发现：随剂量率增加，相变机制从**形核长大（Nucleation and Growth）**转变为**调幅分解（Spinodal Decomposition）**。低剂量率下（≤0.1 dpa/s），空位浓度随时间单调增加（凹向下），空洞随机形核后逐步对齐为有序超晶格。高剂量率下（≥1 dpa/s），空位浓度曲线出现凸向上区域（$\partial^2 \bar{c}_v/\partial t^2 > 0$），对应调幅不稳定性的发生，导致大量空洞同时形成并快速有序化。

速率理论解析模型成功解释了这一转变：辐照下空位浓度需要达到更高的临界值才能触发调幅分解。对于Mo等典型BCC金属，在常规辐照条件下超晶格形成以形核长大为主；镍（Ni）可能是实验观察机制转变的候选材料。

## Key Equations

$$k_j = \nu_0 \exp(-E_a^j / k_B T)$$

事件$j$的发生概率（倾向性）。$\nu_0$=10¹² s⁻¹为尝试频率，$E_a^j$为激活能。

$$E = \frac{1}{2}\sum_{\alpha=1}^{2}\sum_{j=1}^{N}\sum_{k=1}^{N_\alpha} \epsilon_\alpha^{jk}$$

系统总能量（成对键能模型）。$\alpha$为近邻壳层（1NN, 2NN），$\epsilon_\alpha^{jk}$为$j$-$k$键能。

$$E_{mix} = 8\epsilon_1^{mv} + 6\epsilon_2^{mv}$$

混合焓（eV/atom），由1NN和2NN键能参数化。

$$\kappa = \frac{\epsilon_1^{mv} + \epsilon_2^{mv}}{a_0}$$

梯度能系数（eV/nm），$a_0$=0.315 nm为Mo晶格常数。

$$k_s = \frac{2 \cdot dim}{N_s d_j^2}$$

阱强度。$dim$=3为维度，$N_s$=1000为吸收前跳跃次数，$d_j$=√3·a₀/2为跳跃距离。
