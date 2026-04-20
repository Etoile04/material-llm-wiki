# 相场模拟（Phase-Field Modeling）

> 金属核燃料中裂变气体气泡演化的相场模拟方法

## 定义

相场模拟（Phase-Field Modeling, PFM）是一种计算方法，通过连续序参量（order parameter）追踪微观结构演化，无需显式追踪界面。应用于核燃料时，可模拟气泡形核（bubble nucleation）、生长（growth）、聚合（coalescence）与互连（interconnection）。

## 数学框架

### 自由能泛函（Free Energy Functional）
```
F = ∫[f_c(c, η) + κ_c/2|∇c|² + Σ κ_η/2|∇η_i|²] dV
```
其中：
- $c$ = 浓度场（气体原子密度）
- $η_i$ = 序参量（气泡相标识符）
- $f_c$ = 体自由能密度
- $κ$ = 梯度能系数（gradient energy coefficient）

### 演化方程

**Cahn-Hilliard 方程**（守恒量，浓度场）：
```
∂c/∂t = ∇·[M∇(δF/δc)] + S_irr
```

**Allen-Cahn 方程**（非守恒量，序参量）：
```
∂η_i/∂t = -L(δF/δη_i)
```

其中：
- $M$ = 迁移率（mobility）
- $L$ = 动力学系数
- $S_{irr}$ = 辐照源项

### 辐照效应

**源项**：
```
S_gas = Y_gas × F_dot    （气体产生）
S_vac = Y_v × F_dot - k_iv C_i C_v  （空位产生-复合）
```

**级联效应**：位移级联（displacement cascade）产生富空位区，成为气泡形核位点。

## 主要应用

### 1. 气体气泡演化（Aagesen 2022, 2024）
- 晶内气泡生长与聚合
- 气泡尺寸分布演化
- 气泡互连阈值预测

### 2. 气泡超晶格形成（Hu 2016；Smith 2023）
- 有序气泡阵列的自组织
- 超晶格常数对辐照条件的依赖
- 稳定性分析

### 3. 再结晶模拟（Recrystallization Modeling）
- 辐照下的晶界迁移（grain boundary migration）
- 再结晶前沿传播
- 与气体气泡行为的耦合

### 4. 空洞肿胀（Void Swelling）（Rest 1992；Yun 2022）
- 空穴型空洞（cavitational void）形核与生长
- α-U 中的各向异性肿胀
- 空洞尺寸分布预测

## 校准参数

| 参数 | 典型值 | 单位 | 说明 |
|------|--------|------|------|
| 梯度能系数（κ） | 10⁻¹⁰ – 10⁻⁸ | J/m | 控制界面宽度 |
| 迁移率（M） | D_0/kT | m²/s | 与扩散系数相关 |
| 气泡表面能（γ） | 1.0–1.5 | J/m² | U-Mo 体系 |
| 空位形成能 | 1.5–2.0 | eV | U 基体 |
| Xe 溶解能 | 1.5–3.0 | eV | 在 U-Mo 中 |

## 模型层级

```
原子尺度（分子动力学 MD / 密度泛函理论 DFT）
    ↓  （提供参数）
相场模型（Phase-Field Model）
    ↓  （校准预测）
工程模型（Rest、Karahan）
    ↓  （燃料性能代码）
FEAST、BISON、ALFUS
```

## 相关条目
- [[wiki/entities/GasBubbleSuperlattice|气泡超晶格]] — 相场模型预测 GBS 形成
- [[wiki/entities/CavitationalVoid|空穴型空洞]] — 相场模型模拟空洞演化
- [[wiki/entities/Recrystallization|再结晶]] — 相场模型捕捉晶粒重构
- [[wiki/entities/RateTheory|速率理论]] — 相场模型在速率理论基础上增加空间分辨率

## 主要参考文献
- Aagesen (2022, 2024)：相场气泡生长与空位产生
- Hu (2016)：三维晶粒形貌对肿胀的影响
- Millett (2012)：辐照金属中气泡动力学的相场模型
- Liang (2013)：晶内气泡演化的三维相场模拟
- Rokkam (2007)：空洞形核与生长的相场模型
