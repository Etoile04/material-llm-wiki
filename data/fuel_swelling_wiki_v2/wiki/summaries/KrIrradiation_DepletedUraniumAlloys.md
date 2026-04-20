# U-Mo合金中气体气泡超晶格形成：相场研究（含晶界效应）

> Jiang, Gao, La, Liu (2025). Formation of gas bubble superlattice in U-Mo alloys: A phase-field study. *J. Nucl. Mater.* (西安交通大学).

## 摘要

本研究开发了耦合Kim-Kim-Suzuki (KKS)模型和显式形核算法的相场模型，模拟U-7Mo合金中裂变气体气泡超晶格（Gas Bubble Superlattice, GBS）的形成与演化。模型考虑空位浓度$c_\nu$、气体原子浓度$c_g$以及两种沿不同⟨110⟩方向一维扩散的自间隙原子（SIA）浓度$c_1$、$c_2$。SIA的各向异性一维扩散产生"阴影效应"，导致气泡沿特定方向有序排列，形成fcc结构的气泡超晶格（基体为bcc结构），晶格常数7–12 nm，气泡直径1–3 nm，与实验观测一致。

研究首次系统考察了晶界（GB）对GBS形成的影响。GB将周围区域分为贫化区（denuded zone）和峰值区。通过一维稳态空位扩散方程推导了贫化区宽度与GB吸收强度的关系：$w_{dz} = \sqrt{D_\nu/s_\nu}$，即贫化区宽度随GB吸收强度增大而增加。相场模拟结果与理论预测一致。

模拟温度为473 K（典型研究堆运行温度），界面厚度10 nm。SIA扩散系数张量取对角形式，主方向扩散系数为10 nm²/s。空位产生率与裂变率关系为$P_\nu = f_r/\delta$，$\delta = 512$。

## Key Equations

$$F = \int_V \left[ f_{chem} + f_{poly} + W g(\eta) + f_{grad} \right] dV$$

系统总自由能。$f_{chem}$为化学自由能密度，$f_{poly}$为多晶能量密度，$W g(\eta)$为双势阱函数（$g(\eta)=\eta^2(1-\eta)^2$），$f_{grad}$为梯度能密度，$\eta$为气泡序参量。

$$\frac{\partial c_\nu}{\partial t} = \nabla \cdot M_\nu \nabla \mu_\nu + P_\nu - K_{\nu i} c_\nu(c_1+c_2) - S_\nu$$

空位浓度演化方程（Cahn-Hilliard型）。$M_\nu=D_\nu/k_BT$为空位迁移率，$P_\nu$为空位产生率，$K_{\nu i}$为空位-SIA复合速率，$S_\nu$为GB吸收项。

$$\frac{\partial c_1}{\partial t} = \nabla \cdot \left(\frac{D_1 c_1 \nabla \mu_1}{k_B T}\right) + P_1 - K_{\nu i} c_\nu c_1 - S_1$$

SIA浓度演化方程。$D_1$为各向异性扩散系数张量。

$$w_{dz} = \sqrt{\frac{D_\nu}{s_\nu}}$$

晶界贫化区宽度。$D_\nu$为空位扩散系数，$s_\nu$为GB吸收强度。

$$J(t) = k_1 \exp(-k_2 / \Delta c_\nu)$$

气泡形核率。$k_1$、$k_2$为形核因子，$\Delta c_\nu$为局部空位过饱和度。
