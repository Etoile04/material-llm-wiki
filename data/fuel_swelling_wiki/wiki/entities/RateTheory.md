# 速率理论（Rate Theory）

> 核燃料中裂变气体行为建模的速率理论框架

## 定义

速率理论（Rate Theory, RT）（又称均场理论（Mean-Field Theory））通过耦合常微分方程描述缺陷和气泡浓度的平均时间演化，是大多数工程级燃料肿胀模型的基础框架。

## 核心方程

### 缺陷平衡方程

**空位浓度**：
```
dC_v/dt = G_v - K_iv × C_i × C_v - K_vb × C_v × N_b - D_v × C_v / (a²)
```

**间隙原子浓度**：
```
dC_i/dt = G_i - K_iv × C_i × C_v - K_ib × C_i × N_b
```

其中：
- $G_v$、$G_i$ = 空位/间隙原子产生速率
- $K_{iv}$ = 复合速率系数（recombination rate coefficient）
- $K_{vb}$、$K_{ib}$ = 缺陷-气泡吸收速率
- $N_b$ = 气泡数密度

### 气体原子平衡

**溶解态气体**：
```
dC_g/dt = Y_g × F_dot - K_gb × C_g × N_b - D_g × C_g × S_gb / V
```

**气泡内气体**：
```
d(C_g × N_b × V_b)/dt = K_gb × C_g × N_b
```

### 气泡生长

**气泡半径演化**：
```
dr/dt = (Ω/r) × [D_v × C_v - D_i × C_i + D_g × C_g / (2n_b)]
```

其中：
- $Ω$ = 原子体积（atomic volume）
- $n_b$ = 气泡内气体原子数

## 关键速率常数

### 复合速率
```
K_iv = 4π × r_0 × (D_v + D_i)
```

### 气泡吸收速率
```
K_vb = 4π × r_b × D_v × Z_v
K_ib = 4π × r_b × D_i × Z_i
```

其中 $Z_v$、$Z_i$ 为偏置因子（bias factor）（$Z_i > Z_v$，因为位错对间隙原子有偏好吸收）。

### 气体吸收速率
```
K_gb = 4π × r_b × D_g
```

## 模型变体

### 1. 简单速率理论（Simple Rate Theory, SRT）
- 单一气泡尺寸
- 均场近似
- 计算快速，可获得解析解

### 2. 团簇动力学（Cluster Dynamics, CD）
- 多尺寸类别
- 求解完整尺寸分布
- 精度更高，但计算量大

### 3. 耦合速率-相场方法（Coupled Rate-Phase-Field）
- 速率理论处理点缺陷
- 相场模型（Phase-Field Modeling）提供空间分辨率
- 两种方法优势互补（Ye 2023）

## 在金属燃料中的主要应用

| 模型 | 体系 | 参考文献 |
|------|------|----------|
| GRSIS 裂变气体肿胀模型 | U-Pu-Zr | Rest (2001) |
| Rest 模型 | α-U、α-U-Pu-Zr | Rest (1992, 1993) |
| FEAST 金属燃料模型 | U-Pu-Zr | Karahan (2013) |
| Ye 集成模型 | U-10Mo | Ye (2023) |
| Qian 模型 | UN | Qian (2021) |

## 关键参数

| 参数 | 数值 | 单位 | 来源 |
|------|------|------|------|
| 空位扩散指前因子 $D_{v0}$ | 1.38 × 10⁻⁸ | m²/s | 校准值 |
| 空位迁移能 | 0.34 | eV | 文献 |
| 位错偏置因子 | 1.02–1.10 | — | 理论 |
| 气泡再溶解速率（resolution rate） | 10⁻³ – 10⁻¹ | s⁻¹ | 依赖裂变速率 |

## 局限性

1. **无空间分辨率**：无法捕捉局部微观结构效应
2. **均场假设**：忽略尺寸分布效应
3. **依赖校准**：参数通常针对特定数据集调整
4. **相变问题**：无法自然捕捉再结晶起始

## 相关条目
- [[wiki/entities/PhaseFieldModeling|相场模拟]] — 速率理论的空间扩展
- [[wiki/entities/FissionGasDiffusion|裂变气体扩散]] — 速率理论中的输运机制
- [[wiki/entities/CavitationalVoid|空穴型空洞]] — 速率理论描述空洞演化
- [[wiki/entities/SwellingMechanisms|肿胀机制]] — 速率理论支撑机制性肿胀模型

## 主要参考文献
- Rest (1992)：空穴型肿胀速率理论
- Rest (2001)：GRSIS 模型
- Karahan (2013)：FEAST 实现
- Ye (2023)：耦合方法集成模拟
