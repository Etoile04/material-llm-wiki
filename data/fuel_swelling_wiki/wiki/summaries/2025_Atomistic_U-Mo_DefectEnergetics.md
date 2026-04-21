# 2025_Atomistic_U-Mo_DefectEnergetics

**论文**: An atomistic study of defect energetics and diffusion with respect to composition and temperature in γU and γU-Mo alloys
**作者**: Gyuchul Park, Benjamin Beeler, Maria A. Okuniewski (Purdue University / NC State / INL)
**期刊**: Journal of Nuclear Materials 549 (2021) 152970

## 摘要

本研究采用分子动力学（MD）模拟，利用EAM U-Mo-Xe嵌入原子势（Smirnova et al.开发），系统计算了γU及γU-xMo（x=7, 10, 12 wt.%）合金中空位和自间隙原子的形成能，以及自扩散和互扩散系数随温度和成分的变化关系。模拟温度范围为400-1200 K，使用LAMMPS软件包，体系包含2000个原子（10×10×10超胞），采用NPT系综和Langevin恒温器。

主要发现：（1）γU中空位形成能（1.74-2.43 eV）始终高于自间隙原子形成能（0.90-1.08 eV），与DFT计算一致；（2）在γU-xMo中，空位形成能随Mo含量增加而降低，而自间隙原子形成能随Mo含量增加而升高，二者差距缩小；（3）800 K以下U和Mo的扩散可忽略不计；（4）自扩散和互扩散系数均随Mo浓度增加而降低，与实验结果定性一致；（5）自间隙原子主导扩散过程，其平衡浓度远高于空位浓度。计算结果可作为介观和工程尺度燃料性能模型的输入参数。

## Key Equations

### 1. EAM势函数总能量

$$E_{total} = \frac{1}{2}\sum_{i<j}\phi_{ij}(r_{ij}) + \sum_i F\left(\sum_{j\neq i}\rho_i(r_{ij})\right)$$

- $\phi_{ij}$：对势项，$r_{ij}$为原子间距
- $F$：嵌入能，$\rho_i$为背景电子密度

### 2. 空位形成能（γU）

$$E_{vac,\gamma U}^f = E_{vac} - \frac{N-1}{N}E_{ideal}$$

### 3. 自间隙原子形成能（γU）

$$E_{self-i,\gamma U}^f = E_{self-i} - \frac{N+1}{N}E_{ideal}$$

- $N$：无缺陷体系原子数，$E_{ideal}$、$E_{vac}$、$E_{self-i}$分别为完美、含空位、含自间隙原子体系的势能

### 4. 自扩散系数

$$D_{self-D}^U = c_{vac}D_{vac}^U + c_{self-i}D_{self-i}^U$$

$$D_{self-D}^{Mo} = c_{vac}D_{vac}^{Mo} + c_{self-i}D_{self-i}^{Mo}$$

### 5. 缺陷平衡浓度

$$c_{vac} = \exp\left(\frac{\Delta S_{vac}^f}{k_B}\right)\exp\left(\frac{-E_{vac}^f}{k_BT}\right)$$

### 6. Darken互扩散方程

$$D_{inter-D}^{U-xMo} = X_U D_{self-D}^{Mo} + X_{Mo} D_{self-D}^U$$

## 关键数据

| 合金 | 温度(K) | $D_{self-D}^U$ (m²/s) | $D_{self-D}^{Mo}$ (m²/s) | $Q_{inter-D}$ (eV) |
|---|---|---|---|---|
| γU-7Mo | 1200 | 5.89×10⁻¹¹ | 1.56×10⁻¹¹ | 0.79 |
| γU-10Mo | 1200 | 2.38×10⁻¹¹ | 7.18×10⁻¹² | 0.84 |
| γU-12Mo | 1200 | 2.44×10⁻¹² | 8.05×10⁻¹³ | 1.07 |
