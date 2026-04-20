# 裂变气体扩散（Fission Gas Diffusion）

> 金属核燃料中裂变气体（Xe、Kr）的扩散、迁移与气泡形核

## 定义

裂变气体扩散（Fission Gas Diffusion）描述惰性裂变产物（Fission Product, FP）（主要为 Xe 和 Kr）在燃料基体（matrix）中的输运过程，从生成点迁移至最终的气泡形核位点或释放至气腔（plenum）。

## 气体产生

### 产生速率
- **Xe**：约 0.25 原子/裂变（含量最高）
- **Kr**：约 0.03 原子/裂变
- **总气体产额**：约 0.28 气体原子/裂变

### 产生速率公式：
```
C_gen = Y_gas × F_dot  [atoms/m³/s]
```
其中：
- Y_gas = 气体产额（原子/裂变）
- F_dot = 裂变速率密度（fissions/m³/s）

## 扩散机制

### 晶内扩散（Intragranular Diffusion）

**有效扩散系数**（Speight 1969）：
```
D_eff = D_v × (1 + g_cloud / (4πr_b N_b D_v))
```

**温度依赖扩散系数**：
```
D = D_0 × exp(-E_m / kT)
```

| 气体 | D_0 (m²/s) | E_m (eV) | 温度范围 |
|------|-----------|----------|----------|
| Xe 在 γ-U 中 | ~10⁻⁶ – 10⁻⁴ | 1.0–2.5 | 200–800°C |
| Kr 在 γ-U 中 | ~10⁻⁵ | 1.5–2.0 | 200–800°C |
| Xe 在 U-10Mo 中 | ~10⁻⁵ | 1.0–2.0 | 200–600°C |

### 辐照增强扩散（Irradiation-Enhanced Diffusion）

**热扩散（Thermal Diffusion）**：高温（>600°C）占主导
```
D_th = D_0 × exp(-E_m / kT)
```

**非热扩散（Athermal Diffusion）**：低温（<400°C）占主导
```
D_ath = a² × F_dot^(1/2) × Ω / (8π × r_0)
```

**总有效扩散系数**：
```
D_total = D_th + D_ath
```

### 晶界扩散（Grain Boundary Diffusion）

- 沿晶界的快速输运通道
- 受辐照诱发偏析强化
- 对晶界气泡（intergranular bubble）生长和气体释放至关重要

## 气泡形核（Bubble Nucleation）

### 均质形核（Homogeneous Nucleation）
- 气体原子在过饱和溶液中成簇
- 需要临界团簇尺寸（通常 2–5 个原子）
- 低温下占主导

### 非均质形核（Heterogeneous Nucleation）
- 在缺陷位点（空位、位错、晶界）处形核
- 能量壁垒更低
- 高燃耗下占主导

### 形核率（Nucleation Rate）
```
J_nuc = Z × β* × N_0 × exp(-ΔG* / kT)
```
其中：
- Z = Zeldovich 因子（~10⁻²）
- β* = 气体原子吸收速率
- N_0 = 形核位点数量
- ΔG* = 临界自由能壁垒

## 气泡生长（Bubble Growth）

### 生长机制
1. **空位吸收**：气泡通过吸收空位而长大
2. **气体吸收**：Xe/Kr 原子附着到气泡表面
3. **聚合（Coalescence）**：相邻气泡合并
4. **Ostwald 粗化（Ostwald Ripening）**：大气泡以小气泡为代价长大

### 生长速率（速率理论）
```
dr/dt = (Ω / r) × [D_v × C_v - D_i × C_i - D_g × C_g × (P_eq - P_b) / (kT)]
```

## 关键参数

| 参数 | 数值 | 单位 | 来源 |
|------|------|------|------|
| Xe 原子半径 | 0.216 | nm | — |
| Xe 在 U-Mo 中的溶解能 | 1.5–3.0 | eV | 密度泛函理论（DFT） |
| 气泡平衡压力 | 2γ/r | Pa | Laplace 方程 |
| 表面能（U-Mo） | 1.0–1.5 | J/m² | 实验 |
| Xe-Xe 结合能 | 0.1–0.3 | eV | 密度泛函理论（DFT） |

## 相关条目
- [[wiki/entities/Recrystallization|再结晶]] — 改变扩散路径
- [[wiki/entities/GasBubbleSuperlattice|气泡超晶格]] — 有序气泡阵列
- [[wiki/entities/CavitationalVoid|空穴型空洞]] — 气体驱动的空洞形成
- [[wiki/entities/FuelAlloy|燃料合金]] — 基体成分影响扩散

## 主要参考文献
- Ronchi (1979)：MX 型燃料中的裂变气体肿胀
- Rest (2001)：金属燃料 GRSIS 裂变气体肿胀模型
- Ye (2023)：U-10Mo 肿胀的集成模拟
- Qian (2021)：UN 燃料的速率理论
