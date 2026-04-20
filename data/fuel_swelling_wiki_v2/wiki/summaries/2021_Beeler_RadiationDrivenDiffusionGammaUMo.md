# γU-Mo中辐射驱动扩散（Radiation Driven Diffusion）

> Beeler, Cooper, Mei, Schwen, Zhang (2021). Radiation driven diffusion in γU-Mo. *J. Nucl. Mater.* 540, 152395.

## 摘要

本研究通过分子动力学模拟确定了U-Mo核燃料中U、Mo和Xe的辐射驱动扩散（Radiation Driven Diffusion, D₃）系数。利用Smirnova U-Mo-Xe EAM势函数和ZBL短程修正，在80×80×80超胞（1,024,000原子）中进行级联碰撞模拟。PKA能量范围为10–24 keV，温度范围为100–700 K，合金成分包括U-4Mo、U-7Mo、U-10Mo和U-15Mo（wt.%）。

研究发现Xe的均方位移（MSD）随能量密度的斜率显著高于U和Mo，表明Xe在级联核心的热峰区域扩散更快，这与液态U-Mo中Xe的快速扩散行为一致。辐射驱动扩散可视为近似非热（athermal）过程，温度从100 K升至700 K仅导致扩散系数增加约2倍（U/Mo）或1.5倍（Xe）。

通过MyTRIM计算确定裂变碎片仅有约5%的能量通过弹道方式沉积。基于εB系数和裂变率（5×10²⁰ fiss/m³·s），给出了包含本征扩散（D₁）和辐射驱动扩散（D₃）的完整扩散系数。在研究堆运行温度范围（400–600 K）内，辐射驱动扩散是U和Mo的主导机制（转变温度分别为600 K和650 K），而Xe在800 K以下由辐射驱动扩散主导。

## Key Equations

$$D_{rad} = \frac{0.05 \times \epsilon_B}{6} \times E_F \times \dot{F}$$

辐射驱动扩散系数。0.05为弹道能量沉积分数，$\epsilon_B$为MSD随能量密度的斜率（m⁴/eV），$E_F$=170 MeV为裂变碎片总动能，$\dot{F}$为裂变率（fiss/m³·s）。

$$D_{irr} = A \dot{F}$$

简化形式，$A$为与材料相关的系数。

$$D_U = (1.28 \times 10^{-5}) \exp(-1.76/k_BT) + 1.97 \times 10^{-41} \times \dot{F}$$

U的总扩散系数（本征+辐射驱动），单位m²/s。

$$D_{Mo} = (1.62 \times 10^{-5}) \exp(-1.97/k_BT) + 2.01 \times 10^{-41} \times \dot{F}$$

Mo的总扩散系数。

$$D_{Xe} = (1.28 \times 10^{-9}) \exp(-1.76/k_BT) + 5.07 \times 10^{-41} \times \dot{F}$$

Xe的总扩散系数。本征扩散项假设比U低4个数量级。
