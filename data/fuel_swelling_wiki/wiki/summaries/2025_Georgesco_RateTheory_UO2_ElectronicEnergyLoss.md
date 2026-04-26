# UO₂ 辐照效应率理论模型：电子能量损失的影响 (2025)

**Authors**: A. Georgesco, J.-P. Crocombette, G. Gutierrez, C. Onofri, M. Khafizov
**Year**: 2025 | **Journal**: Journal of Nuclear Materials 604, 155493
**DOI**: 10.1016/j.jnucmat.2024.155493
**Slug**: 2025_Georgesco_RateTheory_UO2_ElectronicEnergyLoss

## 中文摘要

本文发展了一个简化的率理论（RT）模型，基于单点缺陷（单体）的时间演化来研究 UO₂ 中电子能量损失对核损伤的影响。模型仅考虑间隙型位错环的形核与长大，用环密度和平均尺寸两个参量表征。

模型包含四个单体浓度演化方程（氧间隙/空位、铀间隙/空位），考虑缺陷产生、复合、薄膜表面吸收和位错环吸收等机制。扩散系数遵循 Arrhenius 定律。双亚晶格模型是本文的特色：氧亚晶格为快扩散通道，铀亚晶格为慢扩散通道，位错环通量由两者共同决定而非仅取决于最快扩散种。位错环通过双间隙团簇（2UI + 4OI）形核或碰撞级联内直接产生（ε 机制）。

首先用 0.39 MeV Xe 和 4 MeV Au 离子在 93、298、873 K 的六组实验数据标定核能量损失主导条件下的模型参数。拟合得到的迁移能为：E_m(UI)=2.55 eV, E_m(OI)=0.825 eV, E_m(VO)=1.6 eV, E_m(VU)=3.9 eV。结果表明：873 K 时环演化主要由单体扩散驱动；93 K 和 298 K 时扩散影响极小，级联内形核主导演化。

对 6 MeV Si 单束辐照数据（强电子能量损失），模型需在扩散系数中添加非热分量 D_ath = 7.5×10⁻²³ cm²/s 才能拟合，表明电子激发/电离效应可增强缺陷扩散且与温度无关。对 Xe+Si 双束辐照数据，模型需将有效温度升高 615 K，表明 Si 离子热峰引起的局部加热影响 Xe 预生成缺陷。

**与 JSRT 项目的关联**：虽然研究对象为 UO₂ 陶瓷燃料，但本文的率理论框架（单体演化→团簇形核→位错环长大/消失）与金属燃料裂变气体气泡模型结构相似。双亚晶格扩散通量的处理方法和不同温度区间主导机制的识别思路具有方法论借鉴价值。非热扩散分量的引入为考虑辐照增强扩散效应提供了定量途径。

## Key Equations

### 单体浓度演化（以氧间隙为例）
$$\frac{dC_{Oi}}{dt} = G_O - 2\sqrt{36D_{Oi} + 96D_{VO}} C_{VO} C_{Oi} - \frac{2D_{Oi} C_{Oi}}{L} - 2\pi r_0 j_{Li} \cdot 2\pi R_L N_L - 2j_{ii}$$

### 双间隙团簇形成通量
$$j_{ii} = \frac{\Omega_0 Z^2_{2,Ui} D_{Ui} C^2_{Ui} Z^2_{2,Oi} D_{Oi} C^2_{Oi}}{a^2 (2Z^2_{2,Ui} D_{Ui} C^2_{Ui} + Z^2_{2,Oi} D_{Oi} C^2_{Oi})}$$

### 位错环通量（间隙侧）
$$j_{Li} = \frac{1}{8R_L}\left(\frac{r_0}{R_L \ln(r_0/R_L)}\right) \times \frac{D_{Ui} C_{Ui} D_{Oi} C_{Oi}}{2D_{Ui} C_{Ui} + D_{Oi} C_{Oi}}$$

### 环密度与平均尺寸演化
$$\frac{dN_L}{dt} = j_{ii} + \varepsilon(G_O + G_U) - \tau N_L^2 R_L^2$$
$$\frac{dR_L}{dt} = \frac{2\pi r_0 L}{3\Omega_0 b} j_i$$

### 非热扩散系数
$$D = D_{ath} + D_0 \exp\left(-\frac{E_m}{k_B T}\right), \quad D_{ath} = 7.5 \times 10^{-23} \text{ cm}^2/\text{s}$$

## 材料参数

| 参数 | 值 | 来源 |
|------|-----|------|
| $E_m$(UI) | 2.55 eV | 拟合 |
| $E_m$(OI) | 0.825 eV | 拟合 |
| $E_m$(VO) | 1.6 eV | 拟合 |
| $E_m$(VU) | 3.9 eV | 设定 |
| $D_0$(UI) | 0.01 cm²/s | 文献 |
| $D_0$(OI) | 0.01 cm²/s | 文献 |
| $D_0$(VO) | 0.02 cm²/s | 文献 |
| $D_0$(VU) | 0.65 cm²/s | 文献 |
| ε | 20 | 拟合 |
| τ₀ | 5.5×10⁻⁷ cm/s | 拟合 |
| $E_a$(loop disappearance) | 2.8 eV | 拟合 |

## Related Work
- [[wiki/concepts/RateTheoryFramework|RateTheoryFramework]] — 本文基于单点缺陷率理论建模缺陷演化
- [[wiki/summaries/2021_Qian_RateTheoryUN|2021_Qian_RateTheoryUN]] — 率理论应用于核燃料缺陷建模
- [[wiki/summaries/2023_Ke_MicrostructureModeling|2023_Ke_MicrostructureModeling]] — 燃料微观结构的多尺度率理论建模
- [[wiki/summaries/2025_MilenaPerez_Oxidation_CrDoped_UO2|2025_MilenaPerez_Oxidation_CrDoped_UO2]] — 同为UO₂燃料的辐照后行为研究
- [[wiki/entities/RateTheory|RateTheory]] — 率理论框架用于缺陷产生-复合-扩散过程
