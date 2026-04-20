# 速率理论框架（Rate Theory Framework）

> 速率理论（Rate Theory）是描述金属燃料辐照肿胀的核心理论框架

## 基本方程

速率理论（Rate Theory）描述点缺陷（Point Defect）——空位（Vacancy）和间隙原子（Interstitial）——的产生、复合（Recombination）、扩散和吸收动力学：

### 缺陷产生

$$
G_v = G_i = F_{nf} \times \dot{f} \quad \text{（空位和间隙产生率）}
$$

- $F_{nf}$：每次裂变产生的弗伦克尔对（Frenkel Pair）数
- $\dot{f}$：裂变速率（Fission Rate），单位 fissions/m³/s

### 缺陷浓度演化

$$
\frac{dC_v}{dt} = G_v - K_{iv} \cdot C_v \cdot C_i - \sum_j D_v \cdot Z_{vj} \cdot \rho_j \cdot C_v + S_v
$$

$$
\frac{dC_i}{dt} = G_i - K_{iv} \cdot C_v \cdot C_i - \sum_j D_i \cdot Z_{ij} \cdot \rho_j \cdot C_i + S_i
$$

- $K_{iv}$：空位-间隙复合系数（Recombination Rate Coefficient）
- $Z_{vj}$, $Z_{ij}$：位错（Dislocation）/气泡（Bubble）/晶界（Grain Boundary）对空位/间隙的偏置因子（Bias Factor）
- $\rho_j$：各类缺陷汇（Sink）密度
- $D_v$, $D_i$：空位和间隙扩散系数（Diffusion Coefficient）

### 空洞生长速率

$$
\frac{dr}{dt} = \frac{D_v \cdot C_v - D_i \cdot C_i}{r} - \text{气体压力项}
$$

### 肿胀率

$$
\frac{dS}{dt} = \frac{4\pi}{3} \sum_k \frac{d(r_k^3)}{dt} \cdot N_k
$$

- $N_k$：空洞/气泡数密度（Number Density），单位 m⁻³

## 关键参数

| 参数 | 符号 | 典型值（U-Zr） | 来源 |
|------|------|----------------|------|
| 裂变气体原子产额 | $F_{nf}$ | 1.0×10⁻⁶ ~ 5.0×10⁻⁶ | 校准（Calibration） |
| 位错密度 | $\rho$ | 10¹³ ~ 10¹⁵ m⁻² | 校准 |
| 空位扩散系数指前因子 | $D_{v0}$ | ~1.38×10⁻⁸ m²/s | Rest 2006 |
| 空位迁移能 | $E_{vm}$ | ~0.34 eV | Rest 2006 |
| 间隙迁移能 | $E_{im}$ | ~0.1 eV | 估算 |
| 复合半径 | $r_0$ | ~1 nm | 理论 |

## 物理假设

1. **均场近似（Mean-Field Approximation）**：缺陷浓度在空间上均匀分布
2. **球形对称**：气泡（Bubble）/空洞（Void）为球形
3. **稳态近似（Steady-State Approximation）**：$dC/dt \approx 0$（长时间尺度）
4. **弗伦克尔对产生**：裂变同时产生等量空位和间隙原子

## 局限性

1. **不考虑空间异质性**：忽略晶界（Grain Boundary）、相界的影响
2. **无微观组织演化**：不能描述再结晶（Recrystallization）、晶粒长大
3. **参数不确定性**：许多参数需依赖实验校准（Calibration）
4. **低温区失效**：需修正为空穴型空洞肿胀（Cavitational Void Swelling）模型

## 扩展模型

### 空穴型空洞肿胀模型（Cavitational Void Swelling Model，Yun 2022）

- 适用于铀锆合金（U-10Zr）低温区（400–600 K）
- 空洞内气体压力低于平衡压力
- 修正了空位扩散参数（Vacancy Diffusion Parameter）

### FEAST 金属燃料模型（FEAST-METAL，Karahan 2013）

- 耦合热-力学分析
- 扩展至超高燃耗（Burnup）工况
- 集成裂变气体释放（Fission Gas Release）模型

### BISON 铀钚锆模型（BISON U-Pu-Zr Model，Aagesen 2020）

- 引入介观尺度参数输入
- 由相场模拟（Phase-Field Modeling）提供参数
- 按温度区间分区处理

## 相关文献

- Rest（1993）——裂变气体气泡形核空洞肿胀动力学
- Rest（2005）——辐照诱发再结晶对肿胀的影响
- Yun 等（2022）——铀锆合金空穴型空洞肿胀模型
- Aagesen 等（2020）——基于低长度尺度信息的 BISON 模型
