# α-U 晶界自扩散与点缺陷 MD 模拟

## 元数据

| 字段 | 值 |
|------|-----|
| **标题** | Grain Boundary Self-Diffusion and Point Defect Interactions in α-U: A Molecular Dynamics Study |
| **作者** | S. Mahbuba, J. Yu, D. A. Lopes, B. Beeler, C. Deo |
| **期刊** | Journal of Nuclear Materials (预印本) |
| **年份** | ~2021 |
| **Slug** | Mahbuba_GrainBoundary_Diffusion_Defect_AlphaU_MD |
| **关键词** | α-U, 分子动力学, 晶界扩散, 点缺陷, 偏析能, Coble 蠕变, LAMMPS |

## 中文摘要

本文利用分子动力学（MD）模拟系统研究了 α-铀中六种对称倾斜晶界（STGB）与点缺陷（空位和间隙原子）的相互作用及沿晶界的自扩散行为。采用 Starikov 的 U-Mo 角依赖势（ADP），在 LAMMPS 中进行模拟。

晶界按取向分为三类：A 型（倾斜轴 [100]，剪切面 (001)）、B 型（倾斜轴 [001]，剪切面 (010)）、C 型（倾斜轴 [001]，剪切面 (100)），每类选取一个高能和一个低能晶界。

**点缺陷偏析**：间隙原子的偏析能始终高于空位。高能晶界对间隙原子的偏析能约为空位的 2 倍，低能晶界甚至达到 6 倍。偏析能与晶界能呈线性关系：间隙原子 2.99 eV/(J/m²)，空位 2.92 eV/(J/m²)。空位偏析存在约 0.4 J/m² 的晶界能阈值。加权平均偏析能为：间隙原子 0.91 eV，空位 0.52 eV。

**晶界扩散**：高能晶界扩散系数比低能晶界高约 4 倍，比体扩散快 10⁷-10¹³ 倍。高能 A2、C2 晶界呈现管道扩散（1D），低能晶界为面扩散（2D）。点缺陷的引入使高能晶界扩散率提高 1.45-1.5 倍。

**Coble 蠕变**：首次推导了 α-U 的 Coble 蠕变方程，激活能 0.221 eV。在金属燃料典型条件下（500-750 K, 5 MPa, 10-20 μm 晶粒），蠕变率为 1.68×10⁻⁶ 至 1.34×10⁻⁵ s⁻¹。

## Key Equations

### 1. 点缺陷形成能

$$E_f^{(r)}_{i/v} = E^{(n \pm 1)}_{(r)} - \frac{n \pm 1}{n} \times E_n$$

其中 $n$ 为无缺陷体系原子数，$E_n$ 为无缺陷体系势能。

### 2. 偏析能

$$E_s^{(r)}_{i/v} = E_f^{(r)}_{i/v} - E_f^{bulk}_{i/v}$$

正 $E_s$ 表示缺陷被吸引到晶界。

### 3. Einstein 扩散关系

$$D_{GB} = \frac{MSD_{GB}}{2dt}$$

其中 $d$ 为扩散维度，$MSD_{GB}$ 考虑晶界厚度修正：$MSD_{GB} = (l_{sb}/\delta) \times MSD_{sb}$。

### 4. 加权平均晶界扩散系数

$$D_{GB,A} = 7.05 \times 10^{-10} \exp\left(\frac{-0.272}{k_B T}\right) \text{ m}^2/\text{s}$$

$$D_{GB,B} = 7.92 \times 10^{-10} \exp\left(\frac{-0.248}{k_B T}\right) \text{ m}^2/\text{s}$$

$$D_{GB,C} = 1.44 \times 10^{-10} \exp\left(\frac{-0.124}{k_B T}\right) \text{ m}^2/\text{s}$$

### 5. Coble 蠕变方程

$$\dot{\varepsilon}_{Coble} = \frac{42|\Omega|\pi D_{GB}\delta}{k_B T d^3} \sigma$$

拟合形式：
$$\dot{\varepsilon}_{Coble} = \frac{\sigma}{T d^3} \times 3.269 \times 10^{-22} \exp\left(\frac{-0.221}{k_B T}\right) \text{ s}^{-1}$$

## 关键物理参数

| 参数 | 值 |
|------|-----|
| 温度范围 | 300-750 K |
| 间隙原子偏析能（加权平均） | 0.91 eV |
| 空位偏析能（加权平均） | 0.52 eV |
| 间隙原子交互长度 | 7.8 Å（加倍后 15.6 Å） |
| 空位交互长度 | 5.0 Å（加倍后 10.0 Å） |
| 晶界宽度 δ | 1.5-2.0 nm（取 1.6 nm） |
| 间隙原子缺陷体积 | 8.33 × 10⁻³⁰ m³ |
| 空位缺陷体积 | 13.67 × 10⁻³⁰ m³ |
| Coble 蠕变激活能 | 0.221 eV |
| 迁移能范围 | 0.09-0.626 eV |

## Related Work
- [[wiki/summaries/2025_You_GrainBoundary_IrradiationTolerance_UMo|2025_You_GrainBoundary_IrradiationTolerance_UMo]] — 同为MD研究晶界缺陷演化（U-Mo体系）
- [[wiki/concepts/IrradiationCreepMechanisms|IrradiationCreepMechanisms]] — 本文推导了Coble蠕变方程
- [[wiki/summaries/1993_Rest_VoidSwellingAlphaU|1993_Rest_VoidSwellingAlphaU]] — α-U空洞肿胀物理模型
- [[wiki/summaries/2020_Beeler_RadiationDrivenDiffusion_UMo|2020_Beeler_RadiationDrivenDiffusion_UMo]] — 辐照驱动扩散
- [[wiki/summaries/Mahbuba_GrainBoundary_Diffusion_Defect_AlphaU_MD|Mahbuba_GrainBoundary_Diffusion_Defect_AlphaU_MD]] — 同一论文的替代slug
