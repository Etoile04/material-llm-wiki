# γU-Mo中辐射驱动扩散与Zr阻挡层互扩散

> Beeler, Cooper, Mei, Schwen, Zhang (2021). Radiation driven diffusion in γU-Mo. *J. Nucl. Mater.* 540, 152395.
> 
> **注**：本文聚焦U-Mo燃料体系中U、Mo和Xe的辐照扩散行为，结果可用于理解U-Mo/Zr扩散对中的互扩散问题。

## 摘要

U-Mo单片燃料采用Zr扩散阻挡层设计，燃料-包壳界面的互扩散行为直接影响燃料性能。本研究通过MD模拟确定了γU-Mo中U、Mo和Xe在辐照条件下的扩散系数，涵盖100–700 K温度范围和U-4Mo至U-15Mo成分范围。

在级联碰撞模拟中，Xe的均方位移显著高于U和Mo，归因于级联核心的热峰效应导致局部熔化和Xe的快速液态扩散。辐射驱动扩散为近似非热过程，温度影响可忽略。电子能量损失占裂变碎片总能量的~95%，仅~5%（8.5 MeV）以弹道方式沉积。

通过结合本征扩散（高温实验外推）和辐射驱动扩散，给出了适用于辐照条件的完整扩散系数。在研究堆运行温度（400–600 K）下，辐射驱动扩散是U和Mo的主导扩散机制。这些结果对U-Mo/Zr界面的辐照诱发互扩散建模具有重要意义。

## Key Equations

$$D_{rad} = \frac{0.05 \times \epsilon_B}{6} \times E_F \times \dot{F}$$

辐射驱动扩散系数。0.05为弹道沉积分数，$\epsilon_B$为MSD/能量密度斜率，$E_F$=170 MeV，$\dot{F}$为裂变率。

$$D_U = (1.28 \times 10^{-5}) \exp(-1.76/k_BT) + 1.97 \times 10^{-41} \times \dot{F}$$

$$D_{Mo} = (1.62 \times 10^{-5}) \exp(-1.97/k_BT) + 2.01 \times 10^{-41} \times \dot{F}$$

$$D_{Xe} = (1.28 \times 10^{-9}) \exp(-1.76/k_BT) + 5.07 \times 10^{-41} \times \dot{F}$$

U、Mo和Xe的总扩散系数（本征+辐射驱动），单位m²/s。
