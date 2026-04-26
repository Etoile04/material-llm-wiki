# 螺旋十字形燃料（HCF）三维精细燃耗特性分析 (2025, Duan et al.)

## Metadata
- **Journal**: Annals of Nuclear Energy 219 (2025) 111505
- **Authors**: Qianni Duan, Wei Li, Kun Zhang, Junmei Wu, Zhifeng Li
- **Affiliation**: 西安交通大学 / 中国核动力研究设计院
- **Material System**: Helical Cruciform Fuel (HCF), 4.95% enriched UO₂
- **Method**: OpenMC Monte Carlo + CRAM 燃耗求解 + 非结构四面体网格
- **Key Topic**: HCF 3D 精细燃耗区域划分方法与燃耗特性分析

## Physical Mechanisms

1. **HCF 几何特征**：四瓣十字截面 + 轴向扭转，增大换热面积、促进交混流动。凹面与凸面连接慢化剂的周长不同，导致中子通量周向不均匀。
2. **燃耗区域划分方法**：2D 截面自由四边形网格 → 轴向扫掠形成六面体 → CAD 实体 → DAGMC 面网格，解决了传统 CSG 无法建模复杂几何的问题。
3. **周向燃耗不均匀性**：凸面功率密度显著高于凹面（初始差 40–110 W/cm³，寿期末差 110–180 W/cm³），且随燃耗加深而加剧。
4. **轴向中子通量展平**：寿期初轴向通量峰值明显，随燃耗推进逐渐展平。

## Key Equations

### 燃耗方程
$$\frac{dN_i(t)}{dt} = \sum_j \left[\int_0^\infty f_{j\to i} dE\,\sigma_j(E,t)\phi(E,t) + \lambda_{j\to i}\right]N_j(t) - \left[\int_0^\infty dE\,\sigma_i(E,t)\phi(E,t) + \sum_j \lambda_{i\to j}\right]N_i(t)$$

## Key Parameters

| 参数 | 值 |
|------|------|
| 燃料轴向长度 | 100 cm |
| 扭转螺距 | 100 cm（基准）|
| 线功率 | 350 W/cm |
| 粒子数/循环 | 100,000 |
| 初始富集度 | 4.95% |
| 燃耗深度（Z=62.5 凸面） | 72.8 MWd/kg（寿期末） |
| 燃耗深度（Z=62.5 凹面） | 54.25 MWd/kg（寿期末） |
| 凹凸面燃耗差 | ~18.55 MWd/kg |
| 不同螺距反应性差 | < 300 pcm |

## Relevance to Knowledge Base

本文提出的 3D 燃耗区域划分方法适用于任意异形燃料，为新型燃料设计的中子物理分析提供了通用方法。周向燃耗不均匀性的定量数据对热工水力和力学分析具有基础性意义。HCF 的链式反应持续时间更长，相比圆柱燃料具有明显经济优势。

## Related Work
- [[wiki/concepts/FuelPerformanceCodes|FuelPerformanceCodes]] — 燃耗分析是燃料性能分析的基础模块
- [[wiki/summaries/2025_Nelson_AcceleratedBurnup_FuelQualification|2025_Nelson_AcceleratedBurnup_FuelQualification]] — 加速燃耗方法学与燃料鉴定
- [[wiki/summaries/2025_Pizzocri_MultiFidelity_FuelPerformance|2025_Pizzocri_MultiFidelity_FuelPerformance]] — 多保真度燃料性能建模
- [[wiki/concepts/FissionGasReleaseModels|FissionGasReleaseModels]] — 燃耗分析中的裂变气体释放建模
