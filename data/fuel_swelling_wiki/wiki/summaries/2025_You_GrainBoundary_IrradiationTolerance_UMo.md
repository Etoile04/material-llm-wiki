# 晶界对U-Mo合金辐照容忍性的影响：缺陷演化与力学性能

## Metadata
- **Title**: The Effect of Grain Boundary on Irradiation Tolerance of U-Mo Alloy: Defect Evolution and Mechanical Properties
- **Authors**: Hang You, Xuelian Ou, Junjie Ai, Tengfei Ma, Xiaofeng Tian*
- **Year**: 2025
- **Journal**: Nuclear Instruments and Methods in Physics Research B 558 (2025) 165561
- **Affiliation**: 成都理工大学核技术与自动化工程学院
- **DOI**: 10.1016/j.nimb.2024.165561

## 摘要

本研究利用分子动力学（MD）方法系统研究了U-10 at.%Mo合金中两种对称倾斜晶界——Σ13(032)和Σ17(0̄41)——对辐照缺陷演化和力学性能的影响。模拟采用Smirnova开发的ADP势函数，U-21.6 at.%Mo（对应U-10 wt%Mo）模型。

关键发现：(1) 存活缺陷数量对温度和PKA-to-GB距离高度敏感。随温度从300 K升至900 K，Σ13 GB模型中间隙和空位分别减少43.5%和31.4%。(2) 晶界表现出间隙原子偏好吸收效应（bias absorption），导致体区空位浓度升高。(3) 间隙原子对结合能均为负值（-1.2至-2.2 eV），不利于间隙团簇形成，这与典型bcc金属不同。(4) 晶界吸收缺陷能力与应变宽度正相关——Σ13 GB（应变宽度10.224 Å）优于Σ17 GB（9.783 Å），尽管后者具有更高的晶界能。

辐照后拉伸模拟（30 keV PKA）表明：GB模型屈服应力损失更小（Σ13: 3.65% vs SC: 4.06%），但平均流动应力增幅更大（Σ17 GB: +33.31%），表明晶界有效增强了材料抗塑性变形能力。弹性模量在辐照前后几乎无变化。空位团簇尺寸随温度升高而减小，GB模型在抑制空位团簇形成方面优于SC模型。

## Key Equations

- **晶界能**：
$$E_{GB} = \frac{E_{t}^{GB} - n \cdot E_C}{2A}$$

- **晶界过剩自由体积**：
$$V_f = \frac{V_g - V_s}{2A}$$

- **间隙扩散系数（Einstein方程）**：
$$D = \frac{\langle r^2(t) \rangle}{2nt}$$

- **间隙迁移能（Arrhenius方程）**：
$$\ln(D) = D_0 \exp\left(-\frac{E_m}{k_B T}\right)$$

- **缺陷湮灭率**：
$$\eta = 1 - \frac{n_s}{n_p}$$

- **间隙对结合能**：
$$E_b(A,B) = E(A) + E(B) - [E(A+B) + E_N]$$

## 关键数据
| 参数 | Σ13(032) GB | Σ17(0̄41) GB |
|------|-------------|--------------|
| 倾转角 | 67.38° | 28.07° |
| 晶界能 | 0.1380 J/m² | 0.1680 J/m² |
| 应变宽度 | 10.224 Å | 9.783 Å |
| 过剩自由体积 | 0.2063 ų | 0.2218 ų |
| 间隙迁移能 | 0.349 eV | 0.375 eV |
| 原子数 | 374,616 | 410,256 |

## Related Work
- [[wiki/summaries/Mahbuba_GrainBoundary_Diffusion_Defect_AlphaU_MD|Mahbuba_GrainBoundary_Diffusion_Defect_AlphaU_MD]] — 同为MD研究晶界缺陷演化，材料体系互补（α-U vs U-Mo）
- [[wiki/summaries/2025_Atomistic_U-Mo_DefectEnergetics|2025_Atomistic_U-Mo_DefectEnergetics]] — U-Mo原子尺度缺陷能研究
- [[wiki/concepts/SwellingMechanisms|SwellingMechanisms]] — 晶界缺陷吸收影响辐照肿胀
- [[wiki/summaries/2020_Beeler_RadiationDrivenDiffusion_UMo|2020_Beeler_RadiationDrivenDiffusion_UMo]] — U-Mo辐照驱动扩散
- [[wiki/summaries/2018_Liang_3DPhaseFieldIntragranularBubbleUMo|2018_Liang_3DPhaseFieldIntragranularBubbleUMo]] — U-Mo气泡演化相场模拟
- [[wiki/entities/FuelAlloy|FuelAlloy]] — U-Mo合金属金属燃料合金体系
