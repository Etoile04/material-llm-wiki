# Yao et al. 2020 — α-U and ω-UZr₂ in Neutron Irradiated U-10Zr Annular Metallic Fuel

**文献**: Yao, T., Capriotti, L., Harp, J.M., et al. *Journal of Nuclear Materials*, 2020.  
**DOI**: 10.1016/j.jnucmat.2020.152377  
**实验堆**: ATR (Idaho National Laboratory), 燃料棒编号 AFC-3A R4  
**燃耗**: 3.3% FIMA | **包壳**: HT-9 | **初始成分**: U-10Zr (wt.%)  
**燃料设计**: 环形燃料，55%涂覆密度，氦气结合（无钠结合）

## 摘要

本文通过透射电子显微镜（TEM）对中子辐照后的环形U-10Zr金属燃料进行了系统的显微组织表征。燃料在ATR堆辐照至3.3% FIMA后，原始U-10Zr双相组织发生显著重构，分离为外环α-U区和中心UZr₂₊ₓ区。α-U区形成大量相互连通的裂变气孔（最大约200 μm），为裂变气体释放至燃料棒气腔提供了快速通道，有效抑制了进一步肿胀。而中心UZr₂₊ₓ区由于发生辐照诱导调幅分解，形成约5 nm尺度的成分涨落纳米畴结构，这些大量的相界面作为有效的空位湮灭位错汇，使裂变气泡尺寸仅为α-U区的约1/20（约10 μm）。两相界面区域主要由四方晶系Zr₂Si（空间群I4/mcm，a = 6.58 Å, c = 5.37 Å）组成。包壳-燃料界面发现Fe渗透深度约200 μm，形成U₆Fe金属间化合物。燃料中心温度经BISON模型估计约为900°C，外围U区约700°C。该环形燃料设计通过向内肿胀机制有效避免了燃料-包壳机械相互作用（FCMI），验证了以氦气结合替代钠结合的可行性。

## 关键发现

### 相鉴定
- **外环区（U富集）**: 单相α-U，Zr贫化至约3–7 at.%，裂变气孔相互连通
- **中心区（Zr富集）**: UZr₂₊ₓ相，bcc基体中嵌有ω相纳米颗粒；靠近相边界处为调幅分解微结构（约5 nm畴尺寸）
- **两相边界**: 多晶Zr₂Si（四方晶系，含晶间U）

### Fe渗透
- 包壳附近成分U-3Zr-13Fe (at.%)，形成U₆Fe与α-U共格生长，深度约200 μm
- 渗透沿α-U特定晶体学方向进行

### Zr皮层（Zr Rind）
- 燃料中心侧：双层结构，主层Zr₂Si + 副层α-Zr（六方）
- 包壳侧：面心立方（fcc）结构，晶格常数约0.467 nm，接近ZrN（0.456 nm），含N和O杂质

### 裂变气孔差异机制
α-U区与UZr₂₊ₓ区裂变气孔尺寸相差约20倍，主要归因于UZr₂₊ₓ调幅分解产生的纳米畴界面充当空位-间隙原子复合湮灭中心，截断了向气泡供应空位的通道。

## 关键方程与模型

本文为实验表征论文，未提出新的本构方程或理论模型。引用的主要模型包括：

1. **BISON燃料性能模型** [35]：用于燃料温度预测
   - 燃料中心线温度 ~900°C，外围U区 ~700°C

2. **Rest (1993) 裂变气体气泡形核空洞肿胀动力学** [34]：
   - 裂变气体原子沿α-U高角度晶界或α-U/δ-UZr₂相界面聚集形核
   - 气泡生长受基体中裂变气体原子和空位扩散控制

3. **调幅分解判据**（引自Yao et al. 2020 [33,40]）：
   - 离子辐照U-50Zr合金在0.2 dpa、550°C下观察到成分涨落，波长20–40 nm
   - 中子辐照下畴尺寸约5 nm，可能与级联尺寸和辐照诱导混合效应有关

4. **U-Zr相图关键温度** [11]：
   - $\delta\text{-UZr}_2 \rightarrow \gamma\text{-(U,Zr)}$ 相变温度：约610°C
   - bcc → ω → δ 相变路径（淬火条件下停留在ω相）

## 对金属燃料肿胀模拟的意义

- α-U相：裂变气孔快速形核、生长并连通，~3% FIMA时气体释放率约77–90%，此后肿胀速率显著降低
- UZr₂₊ₓ相：调幅分解纳米微结构有效抑制裂变气泡生长，该效应在现有肿胀模型中未被显式考虑
- 环形燃料向内肿胀机制为高燃耗（>20% FIMA）设计提供了重要参考

## 标签

`TEM` `PIE` `环形燃料` `α-U` `ω-UZr₂` `调幅分解` `裂变气孔` `Zr重分布` `FCCI` `ATR`

## Related Work
- [[wiki/summaries/1993_Rest_CavitationalSwellingAlphaUPuZr|1993_Rest_CavitationalSwellingAlphaUPuZr]] — 本文引用的裂变气体气泡形核空洞肿胀动力学基础模型
- [[wiki/summaries/2021_Paaren_AutomatedFuelPerformance_BISON_EBR2|2021_Paaren_AutomatedFuelPerformance_BISON_EBR2]] — BISON燃料性能建模，本文使用BISON进行温度预测
- [[wiki/entities/CavitationalVoid|CavitationalVoid]] — α-U区裂变气孔形核与空洞肿胀机制
- [[wiki/summaries/2018_Harp_Postirradiation_AFC_MetalFuelAlloys|2018_Harp_Postirradiation_AFC_MetalFuelAlloys]] — AFC系列辐照后检验，同ATR实验背景
- [[wiki/summaries/2016_Sun_NeutronRadiographyU10ZrSwelling|2016_Sun_NeutronRadiographyU10ZrSwelling]] — U-10Zr肿胀中子射线照相研究，互补实验方法
