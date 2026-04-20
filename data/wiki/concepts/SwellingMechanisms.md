# 肿胀机制概述（Swelling Mechanisms）

> 金属核燃料辐照肿胀的物理机制分类与综合描述

## 总览

金属核燃料（Metallic Nuclear Fuel）——包括铀锆合金（U-Zr）、铀钼合金（U-Mo）和铀钚锆合金（U-Pu-Zr）——的辐照体积肿胀由两个主要分量组成：

$$
\left(\frac{\Delta V}{V}\right)_{\text{总}} = \left(\frac{\Delta V}{V}\right)_{\text{固态}} + \left(\frac{\Delta V}{V}\right)_{\text{气体}}
$$

### 1. 固态裂变产物肿胀（Solid Fission Product Swelling）

- **贡献**：每原子百分数燃耗约 1% 体积肿胀率（ΔV/V）
- **机制**：Mo、Tc、Ru、Rh、Pd 等裂变产物原子在燃料基体（Matrix）中积累
- **特点**：
  - 与燃耗（Burnup）近似呈线性关系
  - 温度依赖性弱
  - 在整个辐照过程中持续贡献

### 2. 裂变气体肿胀（Fission Gas Swelling）

- **贡献**：主导肿胀（1 at.% 燃耗之后）
- **气体**：Xe（约 85%）和 Kr（约 15%）
- **机制**：气泡形核（Bubble Nucleation）→ 生长（Bubble Growth）→ 聚合（Bubble Coalescence）→ 互连（Bubble Interconnection）→ 释放
- **特点**：
  - 强温度依赖性
  - 非线性行为（气泡互连转折点）
  - 在突变点（Breakaway Point）发生急剧转变

## 肿胀阶段

### 第一阶段：初始肿胀（0–1 at.%）

- 辐照蠕变（Irradiation Creep）驱动燃料快速膨胀
- 肿胀率：约 1% ΔV/V per 0.1 at.%

### 第二阶段：气体肿胀主导（1–2 at.%）

- 裂变气体气泡（Fission Gas Bubble）形核与生长
- 肿胀率：约 6–10% ΔV/V per at.%

### 第三阶段：突变肿胀（ΔV/V 达 20–33%）

- 气泡互连，形成开放孔隙网络
- 裂变气体开始释放（Fission Gas Release）至气腔
- 燃料与包壳（Cladding）发生接触

### 第四阶段：约束肿胀（>2 at.%）

- 包壳约束限制进一步肿胀
- 气体释放降低肿胀率
- 稳态行为：约 1% ΔV/V per at.%

## 按材料体系分类

### 铀锆合金（U-10Zr）

- **低温区（400–600 K）**：空穴型空洞肿胀（Cavitational Void Swelling）
  - 空洞（Void）形核，而非平衡气泡（Bubble）
  - 气体压力（Gas Pressure）较低
  - 与 α 相（α-Phase，正交结构）相关
- **高温区（>600 K）**：裂变气体气泡肿胀（Fission Gas Bubble Swelling）
  - γ 相（γ-Phase，体心立方）稳定
  - 气泡平衡生长

### 铀钼合金（U-10Mo）

- γ 相稳定（体心立方结构，Body-Centered Cubic）
- 气泡超晶格（Gas Bubble Superlattice，GBS）形成
- 辐照诱发再结晶（Irradiation-Induced Recrystallization）加速肿胀
- 肿胀行为可预测性较好

### 铀钚锆合金（U-Pu-Zr）

- 肿胀行为与铀锆合金类似
- 固态裂变产物（Solid Fission Product）贡献更多（Pu 裂变）
- 燃料-包壳化学交互（Fuel-Cladding Chemical Interaction，FCCI）更为严重（镧系元素迁移）

## 与 JSRT 模型的关联

Jiao 速率理论模型（JSRT，Jiao's Swelling Rate Theory）聚焦于低温区的空穴型空洞肿胀（Cavitational Void Swelling），关键过程包括：

- 空位产生与复合（Vacancy Recombination）
- 空位向空洞偏聚（Vacancy Bias to Voids）
- 气泡辅助空洞形核（Bubble-Assisted Void Nucleation）
- 关键参数：$F_{nf}$（裂变气体原子产额）、$\rho$（位错密度，Dislocation Density）、$D_v$（空位扩散系数，Vacancy Diffusion Coefficient）

## 参考文献

- Hofman 等（1990）——铀钚锆燃料肿胀行为
- Rest（1993）——裂变气体气泡形核空洞肿胀动力学
- Yun 等（2022）——铀锆合金空穴型空洞肿胀模型
- Karahan & Buongiorno（2013）——FEAST 金属燃料扩展模型
