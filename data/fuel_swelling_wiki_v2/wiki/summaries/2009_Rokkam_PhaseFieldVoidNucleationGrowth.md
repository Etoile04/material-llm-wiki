# 辐照金属中空位形核与生长的相场建模

## Metadata
| Field | Value |
|-------|-------|
| Authors | Srujan Rokkam, Anter El-Azab, Paul Millett, Dieter Wolf |
| Year | 2009 |
| Journal | Modelling and Simulation in Materials Science and Engineering |
| DOI | 10.1088/0965-0393/17/6/064002 |

## Overview

本文提出了一个用于描述辐照金属中空位（Void）形核与生长的相场模型，首次在统一框架下耦合Cahn-Hilliard方程（守恒量：空位浓度场）和Allen-Cahn方程（非守恒量：相场序参量），实现了对空位形核和生长过程的连续模拟。

模型将空位过饱和条件下的空位相分离视为空位凝聚形成空洞相的过程。自由能泛函包含：理想空位溶液的焓熵贡献、Landau型双稳态势阱项（确保基体相和空洞相的能量极小值）以及梯度能项（描述界面性质）。模拟在二维域上进行，验证了以下经典物理行为：(1) Gibbs-Thomson效应——空位浓度随空洞曲率而变化；(2) Ostwald熟化——小空洞溶解、大空洞生长；(3) 自由表面附近的空洞贫化区（Denuded Zone）形成。

核心发现是成功再现了随机空位产生条件下的空位形核与生长全过程，识别出三个特征阶段：阶段I（孕育期）——空位浓度逐步增加至临界过饱和；阶段II（形核期）——空洞稳定核心大量形成，数量线性增长；阶段III（生长期）——现有空洞继续生长，Ostwald熟化和合并使空洞密度降低。空洞孔隙率演化符合KJMA方程（形核阶段）和线性Ostwald熟化方程（生长阶段）。本文为后续包含间隙原子和预存微观结构影响的更完整模型奠定了基础。

## Key Equations

### 自由能泛函
$$F = N \int_V \left[ h(\eta)\psi_m(c_v) + w(c_v, \eta) + \frac{\kappa_v}{2}|\nabla c_v|^2 + \frac{\kappa_\eta}{2}|\nabla \eta|^2 \right] dV$$

其中 $N$ 为单位体积格点数，$c_v$ 为空位浓度场，$\eta$ 为序参量（$\eta=0$基体，$\eta=1$空洞），$h(\eta)=(\eta-1)^2(\eta+1)^2$ 为插值函数，$\psi_m(c_v)$ 为缺陷自由能。

### 空位缺陷自由能
$$\psi_m(c_v) = c_v E_{fv} + k_B T [c_v \ln c_v + (1-c_v)\ln(1-c_v)]$$

其中 $E_{fv}$ 为空位形成能，$k_B$ 为玻尔兹曼常数，$T$ 为温度。

### Landau双稳态项
$$w(c_v, \eta) = A(c_v - c_{ov})^2(1-c_v)^2 \eta^2 + B(c_v - c_{ov})^2(1-c_v)^4 \eta^2$$

其中 $c_{ov} \approx \exp(-E_{fv}/k_BT)$ 为热平衡空位浓度，$A, B$ 为常数前因子。

### Cahn-Hilliard动力学方程（空位浓度演化）
$$\frac{\partial c_v}{\partial t} = \nabla \cdot \left( M_v \nabla \frac{\delta F}{\delta c_v} \right) + P_v$$

其中 $M_v$ 为空位迁移率，$P_v$ 为随机空位源项（模拟辐照产生）。

### Allen-Cahn动力学方程（相场演化）
$$\frac{\partial \eta}{\partial t} = -L \frac{\delta F}{\delta \eta}$$

其中 $L$ 为界面迁移率。

### 空洞生长幂律
$$\Delta R = \lambda t^n$$

模拟得到 $n = 0.5$（扩散控制生长），$\lambda$ 取决于过饱和度：过饱和比 $S_v = 100, 200, 300$ 时 $\lambda$ 分别为 0.268, 0.349, 0.412。

### KJMA方程（形核阶段孔隙率）
$$\rho(t) = \rho_e \left[1 - \exp(-k t^3)\right]$$

### Ostwald熟化方程（生长阶段孔隙率）
$$\rho(t) = \rho_0 + \frac{\rho_0}{\tau_1} t$$

## Physical Mechanisms

### 空位形核与生长三阶段
辐照下随机产生的空位逐步积累至临界过饱和（孕育期），随后在空间涨落触发下形成稳定空洞核心（形核期），最终空洞通过吸收空位持续生长（生长期），伴随Ostwald熟化和合并。

### Gibbs-Thomson效应
模拟中空洞表面的空位浓度随曲率而变化，小空洞具有较高的平衡空位浓度，导致其在过饱和度不足时溶解。

### 自由表面抑制形核
大空洞（模拟自由表面）通过大量吸收周围空位降低局部空位浓度至形核阈值以下，形成无空洞的贫化区。

## Relationships
- [[PhaseFieldModeling]] — 耦合Cahn-Hilliard/Allen-Cahn的相场方法学基础
- [[CavitationalVoid]] — 空位凝聚形成空洞的核心物理过程
- [[SwellingMechanisms]] — 空洞形成导致体积肿胀
- [[RateTheory]] — 与速率理论的经典结果（KJMA方程、Ostwald熟化）对比验证
