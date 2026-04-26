# Di Lemma et al. (2021) — 金属燃料棒顶部燃料微观结构研究

**文献信息:** F.G. Di Lemma, K.E. Wright, L. Capriotti et al., *J. Nucl. Mater.* **544**, 152711 (2021)

**标签:** `微观结构` `瞬态行为` `FCCI` `EPMA` `U-Pu-Zr` `fluff结构` `EBR-II`

## 摘要

本文研究了EBR-II反应堆中经11 at.%燃耗辐照后，再经历30%超功率瞬态的U-19Pu-10Zr合金燃料棒（HT-9包壳）顶部的微观结构。样品取自燃料柱顶部（x/L≈0.95），该区域在EBR-II设计中是最先出现失效的位置。利用光学显微镜、SEM/EDS和EPMA等后辐照检验手段，系统分析了主元素重分布、相特征、裂变产物行为、化学形态及燃料-包壳化学相互作用（FCCI）。

**核心发现——"Fluff"结构的首次详细表征：** 金属燃料柱顶部常见的高度多孔低密度区域（称为"fluff"结构）在本研究中首次通过电子显微技术进行了详细分析。结果表明，该结构并非仅由裂变产物组成，而是包含主要燃料元素（U、Pu、Zr），其成分与初始制造成分相近（约65U-19Pu-10Zr wt.%），表明fluff形成可能发生在辐照早期、元素重分布之前。该区域孔隙面积分数超过40%，孔隙尺寸从~2 μm到>100 μm不等，并含有大量稀土裂变产物沉淀。

**温度分析：** 采用BISON有限元模拟表明，瞬态峰值温度约1100 K（燃料中心），包壳内壁约894 K，低于U-Pu系最低共晶相Pu₆Fe的熔点（<800 K），且瞬态持续时间仅315秒，不足以形成低熔点共晶相。

**FCCI分析：** 稀土元素渗透包壳深度最大约50 μm，Nd和Ce浓度最高。Pu是扩散进入包壳的主要锕系元素，渗透深度约15 μm。瞬态未显著加剧FCCI，与同设计参数的稳态辐照结果一致。未观察到低熔点相或裂纹。

**裂变产物：** 挥发性/半挥发性元素（Cs、I、Xe、Eu）因样品制备过程中Na的溶解/流失未能大量检测到。Cs以块状粒子形式零星分布。Eu在稀土沉淀中以微量元素形式存在。裂变气体Xe在Zr沉淀附近被检测到。稀土沉淀分为含Pd-Rh的RE₃(Pd,Rh)₂/RE₇(Pd,Rh)₃型和不含贵金属的纯RE型两类，Sm在内区（Region 1）含量高（>10 at.%），在外区（Region 3）含量低。

**结论：** 中等超功率瞬态未显著影响燃料性能。Fluff结构在试验条件下保持稳定，无燃料碎片脱落至腔室区域。

## 关键公式

本文为实验微观结构表征论文，未涉及数学模型或公式。主要依赖BISON有限元模拟进行温度预测，分析中使用的定量方法为EPMA（电子探针微分析）和ImageJ孔隙统计。

## 实验参数

| 参数 | 值 |
|------|-----|
| 燃料成分 | U-19Pu-10Zr (wt.%) |
| 包壳 | HT-9钢 (Fe-12Cr-0.2C) |
| 燃耗 | 11.1 at.% |
| 峰值线功率（稳态） | 53 kW/m |
| 预处理功率 | 41.7 kW/m, 24小时 |
| 瞬态功率 | 54.8 kW/m (32%超功率) |
| 瞬态持续时间 | 315秒 |
| 燃料中心峰值温度 | 1106 K (瞬态) |
| 包壳内壁峰值温度 | 894 K (瞬态) |
| 挤压密度 | 75% |
| 腔室/燃料体积比 | 2.1 |

## Related Work
- [[wiki/summaries/2023_Development_formulation_physics_based_metallic_fuel|2023_Development_formulation_physics_based_metallic_fuel]] — BISON金属燃料物理模型基线，本文使用BISON进行温度预测
- [[wiki/summaries/1990_Hofman_SwellingBehaviorUPuZr|1990_Hofman_SwellingBehaviorUPuZr]] — U-Pu-Zr肿胀经典实验，本文研究的燃料体系
- [[wiki/concepts/FuelCladdingChemicalInteraction|FuelCladdingChemicalInteraction]] — 本文分析了稀土元素渗透包壳的FCCI行为
- [[wiki/summaries/2026_Fay_3DPoreReconstruction_Fluff_EBR2|2026_Fay_3DPoreReconstruction_Fluff_EBR2]] — EBR-II fluff结构3D重建，直接关联本文首次详细表征的fluff结构
- [[wiki/summaries/2016_Carmack_FCCI_MFF3_Metallography|2016_Carmack_FCCI_MFF3_Metallography]] — MFF-3金属燃料FCCI金相分析，互补实验方法
