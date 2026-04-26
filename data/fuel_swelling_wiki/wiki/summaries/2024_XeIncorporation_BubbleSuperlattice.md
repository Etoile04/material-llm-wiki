# 2024_XeIncorporation_BubbleSuperlattice

**论文**: Formation of gas bubble superlattice in U-Mo alloys: A phase-field study
**作者**: Yanbo Jiang, Shisen Gao, Yongxiao La, Wenbo Liu (Xi'an Jiaotong University)
**期刊**: Journal of Nuclear Materials (2024)

## 摘要

本研究建立了耦合Kim-Kim-Suzuki（KKS）模型与显式形核算法的相场模型，模拟了U-7Mo合金中辐照诱导气泡超晶格（GBS）的形成与演化过程，重点研究了晶界（GB）对GBS形成的影响。模型考虑了空位、裂变气体原子和两类自间隙原子（SIA）的浓度场演化，通过SIA的各向异性一维扩散（沿[110]和[011]方向）产生的"阴影效应"来解释气泡有序排列机制。

主要发现：（1）在单晶模拟中，气泡直径约1.3 nm，晶格常数7-12 nm，与实验结果吻合良好（RMSE=0.276）；（2）晶界周围形成贫空位区和峰值区，GBS在峰值区内形成；（3）推导了一维稳态空位扩散方程，建立了贫空位区宽度与GB吸收系数的定量关系：$W_{dz} = \sqrt{(s_\nu - 2P_\nu)\lambda^2/(2P_\nu) + 2D_\nu(c_{\nu}^{eq} - c_{cr})/P_\nu}$；（4）贫空位区宽度随GB吸收系数增大而增大；（5）GB抑制气泡生长，有GB时气泡直径比无GB时小约0.5 nm。模拟温度473 K，裂变密度范围1-6×10²¹ fissions/cm³。

## Key Equations

### 1. 系统总自由能

$$F = \int_V \left[f_{chem} + f_{poly} + Wg(\eta) + f_{grad}\right] dV$$

- $f_{chem}$：化学自由能密度，$f_{poly}$：多晶能量密度，$Wg(\eta)$：双势阱函数，$f_{grad}$：梯度能密度

### 2. 缺陷演化方程（Cahn-Hilliard）

$$\frac{\partial c_\nu}{\partial t} = \nabla \cdot M_\nu \nabla \mu_\nu + P_\nu - K_{\nu i}c_\nu(c_1 + c_2) - S_\nu$$

$$\frac{\partial c_g}{\partial t} = \nabla \cdot M_g \nabla \mu_g + P_g$$

$$\frac{\partial c_1}{\partial t} = \nabla \cdot \left(\frac{D_1 c_1 \nabla \mu_1}{k_B T}\right) + P_1 - K_{\nu i}c_\nu c_1 - S_1$$

- $c_\nu, c_g, c_1, c_2$：空位、气体原子、两类SIA浓度
- $P_\nu, P_g$：空位和气体原子产生率
- $K_{\nu i}$：空位-间隙复合速率
- $S_\nu, S_1, S_2$：GB吸收项

### 3. 贫空位区宽度

$$W_{dz} = \sqrt{\frac{(s_\nu - 2P_\nu)}{2P_\nu}\lambda^2 + \frac{2D_\nu}{P_\nu}(c_\nu^{eq} - c_{cr})}$$

- $s_\nu$：GB吸收系数，$\lambda$：GB半宽度，$D_\nu$：空位扩散系数，$c_{cr}$：临界过饱和浓度

### 4. 形核概率

$$J(t) = k_1 \exp(-k_2/\Delta c_\nu)$$

- $k_1 = 10^{-3}$，$k_2 = 10^{-5}$，$\Delta c_\nu$：局部空位过饱和度

### 5. 表面能与界面厚度关系

$$\gamma_s = \frac{\sqrt{\kappa_\eta W}}{3\sqrt{2}}, \quad 2\lambda = 2.2\sqrt{2}\sqrt{\frac{\kappa_\eta}{W}}$$

- $\kappa_\eta = 2.45 \times 10^{-8}$ J/m，$W = 2.38 \times 10^9$ J/m³

## Related Work
- [[wiki/entities/GasBubbleSuperlattice|GasBubbleSuperlattice]] — 本研究核心主题，模拟U-7Mo中气泡超晶格的形成与演化
- [[wiki/summaries/2025_Jiang_GasBubbleSuperlatticePhaseField|2025_Jiang_GasBubbleSuperlatticePhaseField]] — 同一课题组后续的相场气泡超晶格研究
- [[wiki/summaries/2023_Smith_EarlySelfOrganizationGBS|2023_Smith_EarlySelfOrganizationGBS]] — GBS自组织早期行为的相场模拟
- [[wiki/summaries/2016_Hu_GasBubbleSuperlatticeFormationPF|2016_Hu_GasBubbleSuperlatticeFormationPF]] — Hu等人的相场气泡超晶格形成模型
- [[wiki/summaries/2025_Aagesen_PhaseTransformation_Superlattice|2025_Aagesen_PhaseTransformation_Superlattice]] — 超晶格形成中形核长大与调幅分解机制转变的AKMC研究
