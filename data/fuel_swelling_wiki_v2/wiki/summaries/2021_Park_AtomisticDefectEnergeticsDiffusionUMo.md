# γU 及 γU-Mo 合金中的缺陷能量学与扩散原子尺度研究

> Park, Beeler, Okuniewski (2021). An atomistic study of defect energetics and diffusion with respect to composition and temperature in γU and γU-Mo alloys. *J. Nucl. Mater.* 553, 152970.

## 摘要

本研究利用分子动力学（MD）模拟和嵌入原子方法（EAM）U-Mo-Xe势函数，系统计算了γU和γU-xMo（x = 7, 10, 12 wt.%）在400–1200 K范围内的空位（Vacancy）和自间隙原子（Self-Interstitial Atom, SIA）形成能。在γU中，空位形成能随温度升高从1.74 eV增至2.43 eV，而SIA形成能基本不随温度变化（0.90–1.08 eV）。在γU-xMo合金中，空位形成能随Mo含量增加而降低，SIA形成能随Mo含量增加而升高，表明U-Mo键弱于U-U键（混合焓为正）。由于空位形成能始终高于SIA形成能，γU和γU-xMo中的扩散主要由自间隙原子主导。

基于缺陷形成能计算了U和Mo的自扩散系数和互扩散系数（800–1200 K）。自扩散和互扩散系数均随Mo浓度增加而降低，与实验观测定性一致。U的自扩散系数为Mo的3–4倍。互扩散激活能在γU-7Mo中为0.79 eV，在γU-12Mo中增至1.07 eV，实验值约为1.86–1.91 eV。差异源于MD时间尺度限制和理想合金假设。

## Key Equations

$$E_{vac,\gamma U}^{f} = E_{vac} - \frac{N-1}{N} E_{ideal}$$

空位形成能。$E_{vac}$为含空位体系的势能，$N$为原子数，$E_{ideal}$为完美体系势能。

$$E_{self\text{-}i,\gamma U}^{f} = E_{self\text{-}i} - \frac{N+1}{N} E_{ideal}$$

自间隙原子形成能。$E_{self\text{-}i}$为含SIA体系的势能。

$$D_{self\text{-}D}^{U} = c_{vac} D_{vac}^{U} + c_{self\text{-}i} D_{self\text{-}i}^{U}$$

U原子自扩散系数。$c_{vac}$、$c_{self\text{-}i}$分别为空位和SIA的平衡浓度，$D_{vac}^{U}$、$D_{self\text{-}i}^{U}$分别为含空位/SIA体系中U的扩散率。

$$c_{vac} = \exp\left(\frac{\Delta S_{vac}^{f}}{k_B}\right) \exp\left(\frac{-E_{vac}^{f}}{k_B T}\right)$$

空位平衡浓度。$\Delta S_{vac}^{f}$为形成熵，$k_B$为玻尔兹曼常数，$T$为温度。

$$D_{inter\text{-}D}^{U\text{-}xMo} = X_U D_{self\text{-}D}^{Mo} + X_{Mo} D_{self\text{-}D}^{U}$$

Darken方程计算互扩散系数。$X_U$、$X_{Mo}$为U和Mo的原子分数。

$$D_{vac/self\text{-}i}^{U/Mo} = \frac{\sum_{i=1}^{N} \Delta r_i^2}{6t}$$

通过均方位移（MSD）计算扩散率。$\Delta r_i^2$为第$i$个原子的均方位移，$t$为模拟时间。
