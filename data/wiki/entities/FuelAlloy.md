# 燃料合金（Fuel Alloy）

> 金属核燃料合金体系：成分、相结构与辐照行为

## 概述

金属核燃料（Metallic Nuclear Fuel）是为优化快堆和研究堆性能而设计的合金体系。主要体系包括铀钼合金（U-Mo）、铀锆合金（U-Zr）和铀钚锆合金（U-Pu-Zr），各体系具有不同的肿胀与辐照行为。

## 合金体系

### U-Mo 体系（U-7Mo 至 U-10Mo）

**成分范围**：7–10 wt% Mo  
**主要用途**：研究/试验堆燃料（低浓铀（LEU）转换）  
**晶体结构**：体心立方（BCC）（γ 相，亚稳态）

| 性质 | U-7Mo | U-10Mo |
|------|-------|--------|
| γ 相稳定性 | 一般 | 优异 |
| 肿胀率 | 较高 | 较低 |
| 裂变气体滞留 | 中等 | 良好 |
| 热导率 | ~20 W/(m·K) | ~15 W/(m·K) |

**主要特征**：
- Mo 在运行温度下稳定化 γ-U 相（体心立方）
- 辐照晶粒中形成气泡超晶格（Gas Bubble Superlattice, GBS）
- 再结晶（Recrystallization, RX）触发快速肿胀跃变
- 可制成单层燃料（monolithic fuel）或弥散燃料（dispersion fuel）形式

### U-Zr 体系（U-10Zr）

**成分**：10 wt% Zr  
**主要用途**：快堆燃料（金属燃料）  
**相结构**：多相（α-U、δ-UZr₂、γ-U）

**主要特征**：
- Zr 提高固相线温度，允许更高运行温度
- 成分再分配（Constituent Redistribution）：Zr 沿径向迁移
- 多相结构导致复杂的肿胀行为
- 燃料-包壳化学交互（Fuel-Cladding Chemical Interaction, FCCI）问题突出

### U-Pu-Zr 体系

**成分**：U-20Pu-10Zr、U-15Pu-10Zr（wt%）  
**主要用途**：快堆燃料（增殖）  
**相结构**：与 U-Zr 类似，但伴有 Pu 再分配

## 相行为

### 相图

**U-Mo**：
- 560°C 以下：γ-U（BCC）+ α-U（正交）+ U₂Mo（四方）
- 560–1280°C：γ 相区（BCC，亚稳态）
- Mo > 8 wt% 在运行温度下维持 γ 相

**U-Zr**：
- 620°C 以下：α-U + δ-UZr₂ + α-Zr
- 620–710°C：β-U + γ-U(Zr)
- 710°C 以上：γ 相区

### 辐照诱发相变
- U-Mo 互扩散层的非晶化
- 高燃耗下 U-Mo 中的 γ→α 相回转（Phase Reversion）
- U-Zr 中的相再分配（Zr 在中心和外周富集）

## 成分对肿胀的影响

### Mo 含量（U-xMo）
- Mo 含量越高 → γ 相稳定性越强 → 初始肿胀越低
- 但：Mo 含量越高 → 合金越硬 → 更多气泡形核位点
- LEU 应用最佳范围：7–10 wt%

### Zr 含量（U-xZr）
- Zr 含量越高 → 固相线越高 → 运行窗口越宽
- 但：Zr 含量越高 → 成分再分配越复杂 → 行为更难预测
- 标准：EBR-II/FFTF 应用采用 10 wt%

### Pu 含量（U-Pu-Zr）
- Pu 含量越高 → 功率密度越高 → 裂变气体越多
- Pu 影响相界和再分配模式
- 快堆燃料典型 Pu 含量：10–20 wt%

## 燃料-包壳交互

### 燃料-包壳化学交互（FCCI）
- **扩散偶**：燃料 ↔ 包壳（HT-9、D9、FeCrAlY）
- **镧系元素迁移**：Nd、Ce、La 向外周迁移
- **包壳腐蚀损耗（Cladding Wastage）**：包壳厚度减少 10–100 μm
- **温度依赖性**：速率随温度指数增大

### 燃料-包壳机械交互（FCMI）
- 肿胀引起的接触压力
- 包壳应变积累
- 间隙闭合时机对性能至关重要

## 相关条目
- [[wiki/entities/Recrystallization|再结晶]] — 相稳定性影响再结晶起始
- [[wiki/entities/GasBubbleSuperlattice|气泡超晶格]] — GBS 在稳定 γ 相中形成
- [[wiki/entities/CavitationalVoid|空穴型空洞]] — α 相肿胀机制

## 主要参考文献
- Rest (1992, 1993)：空穴型肿胀模型
- Karahan (2013)：FEAST 金属燃料肿胀模型
- Williams (2020)：U-Zr 肿胀评估 PIRT
- Hanson (2025)：U-10Mo 的稳定可预测肿胀
