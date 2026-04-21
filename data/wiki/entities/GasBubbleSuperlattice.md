# 气泡超晶格（Gas Bubble Superlattice）

> 气泡超晶格（Gas Bubble Superlattice, GBS）是 U-Mo 合金中观察到的独特自组织现象

## 定义

在辐照铀钼合金（U-Mo）中，纳米级裂变气体气泡（Fission Gas Bubble, FGB）（~2–8 nm）自发形成**面心立方（FCC）超晶格**结构，与基体体心立方（BCC）γ-U(Mo) 相相干。

## 特征参数

| 参数 | 值 | 来源 |
|------|------|------|
| 气泡直径 | 2–8 nm | 透射电子显微镜（TEM） |
| 超晶格常数 | ~10–15 nm | TEM |
| 超晶格类型 | FCC（沿 BCC ⟨110⟩ 方向） | TEM/SAED |
| 形成裂变密度 | 1–3 × 10²¹ f/cm³ | 多文献 |
| 饱和裂变密度 | 3–4.5 × 10²¹ f/cm³ | Miller 2015 |
| 崩溃裂变密度 | >4.5 × 10²¹ f/cm³ | Miller 2015 |

## 形成机制

### 1. 自组织理论
- 间隙原子（interstitial）沿 ⟨110⟩ 方向一维迁移
- 产生"阴影效应"（shadow effect）
- 导致气泡沿 ⟨110⟩ 方向有序排列

### 2. 形核过程
- 气泡优先在**晶界（Grain Boundary, GB）**和 **UC/U-Mo 相界**处形核
- 临界完全有序气泡尺寸：~3 nm
- 从晶界向晶内扩展

### 3. 稳定性
- 高热稳定性（加热至 700°C 仍保持稳定）
- 高辐照稳定性（饱和前维持有序）
- 崩溃与再结晶（Recrystallization, RX）相关

## 对肿胀的影响

### 正面
- GBS 可有效储存裂变气体，**抑制肿胀**
- 有序排列降低气泡互连（bubble interconnection）概率
- 裂变密度 < 4.5×10²¹ f/cm³ 时有效控制肿胀

### 负面
- GBS 崩溃后肿胀加速
- 再结晶导致大量新气泡形核位点产生
- 高燃耗时肿胀不可控

## 贫化区（Denuded Zone）

晶界附近存在气泡贫化区：
- 宽度随晶界吸收系数增大而增宽
- 由一维空位扩散方程解析推导
- 影响局部肿胀分布

## 模型

### 相场模型（Phase-Field Modeling）（Hu 2016；Jiang 2025）
- KKS 模型 + 显式形核算法
- 弹性相互作用不导致气泡对齐
- 一维间隙迁移是主要机制

### 团簇动力学（Cluster Dynamics）（Hu 2020）
- 耦合缺陷团簇动力学
- 间隙团簇是快速肿胀动力学的重要机制

## 与 U-Zr 的区别

U-Zr 燃料中**未观察到** GBS：
- U-Zr 在运行温度下为 α + δ 两相
- 不具备稳定的 BCC γ 相
- 肿胀机制不同（空穴型空洞肿胀（Cavitational Void Swelling）vs. 气体气泡肿胀）

## 参考文献
- Hu et al. (2016) — GBS 形成机制
- Miller et al. (2015) — GBS 的 TEM 表征
- Gan et al. (2015) — GBS 的热稳定性
- Smith et al. (2023) — 早期自组织
- Jiang et al. (2025) — 含晶界的相场研究
- Smith et al. (2023) — UC 夹杂物的作用
