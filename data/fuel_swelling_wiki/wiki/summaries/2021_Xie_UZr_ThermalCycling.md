# Xie et al. (2021) — U-10Zr热循环中微结构演变的原位中子衍射研究

## 基本信息
- **标题**: Microstructure Evolution of U–Zr System in A Thermal Cycling Neutron Diffraction Experiment: Extruded U–10Zr (wt. %)
- **期刊**: Journal of Nuclear Materials, 544, 152665
- **作者**: Yi Xie, Sven C. Vogel, Jason M. Harp, Michael T. Benson, Luca Capriotti
- **机构**: Idaho National Laboratory, Purdue University, Los Alamos National Laboratory, Oak Ridge National Laboratory
- **DOI**: 10.1016/j.jnucmat.2020.152665

## 研究概述

本文利用HIPPO飞行时间中子衍射仪，对1073 K热挤压制备的U-10Zr（wt.%）合金在热循环过程（303–1073 K，冷却时在873 K保温约9小时）中的微观结构演变进行了原位研究。通过Rietveld织构与晶体结构精修，系统分析了各相的织构和晶格参数随温度的演化规律。

## 主要发现

1. **β-U相缺失**: 在整个热循环过程中均未观察到β-U相的衍射峰，与公认的U-Zr平衡相图不符。按杠杆规则，在943–966 K温度区间应有约56–73 wt.%的β-U相，其中子衍射技术完全可探测到。这支持了Bauer相图而非Sheldon相图的适用性。

2. **相变滞后**: α-U→γ的相变在加热至943 K完成，而冷却时反向相变在923 K才发生，表现出显著的温度滞后。这归因于γ相中Zr原子需要重新分配（Zr在α-U中溶解度<1 at.%）才能形成α-U，导致该过程动力学迟缓。

3. **晶格参数与热膨胀**: α-U相在升温时沿b轴收缩、沿a和c轴膨胀，其余各相（δ-UZr₂、γ-(U,Zr)、α-Zr）在所有方向均膨胀。作者给出了各相晶格参数随温度变化的拟合公式及热膨胀系数张量。

4. **织构演化与变体选择**: 挤压态U-10Zr中(001)α和(110)γ晶面法线沿挤压方向强烈取向（~5 MRD和~2.7 MRD）。首次观察到α-U与γ-(U,Zr)之间的变体选择关系(001)α || (110)γ，热循环后织构完全恢复，表明无再结晶发生。较高挤压温度（1073 K vs 873 K）产生更强的织构。

5. **未观察到γ₁/γ₂两相分离**: 在整个温度范围内γ相衍射峰无分裂现象，不支持相图所示的γ₁+γ₂两相BCC固溶体。

## 关键方程

### δ-UZr₂晶格参数温度关系（303–873 K）
$$a(T) = 5.043 - 2.3236 \times 10^{-5} T + 7.186 \times 10^{-8} T^2$$
$$c(T) = 3.0552 + 3.8774 \times 10^{-5} T + 5.4406 \times 10^{-9} T^2$$

### α-U晶格参数温度关系（303–938 K）
$$a(T) = 2.8467 + 8.6442 \times 10^{-5} T$$
$$b(T) = 5.8583 - 2.6262 \times 10^{-5} T$$
$$c(T) = 4.9538 + 1.2784 \times 10^{-4} T$$

### α-U热膨胀系数张量
$$\boldsymbol{\alpha} = \begin{pmatrix} 3.0088 \times 10^{-5} & 0 & 0 \\ 0 & -4.489 \times 10^{-6} & 0 \\ 0 & 0 & 2.5607 \times 10^{-5} \end{pmatrix} \text{ K}^{-1}$$

### α-Zr晶格参数温度关系（303–1073 K）
$$a(T) = 3.2336 + 7.6084 \times 10^{-6} T + 6.9269 \times 10^{-9} T^2$$
$$c(T) = 5.1478 + 3.2301 \times 10^{-5} T + 1.1929 \times 10^{-8} T^2$$

## 对燃料性能的意义

α-U相的正交各向异性导致燃料肿胀不对称。挤压引入的织构（(001)α || 挤压方向）与相变过程中的变体选择共同维持了强烈的择优取向，使宏观热膨胀和辐照肿胀具有各向异性。β-U相的缺失意味着热循环无法消除挤压织构，这对燃料棒设计和性能预测具有重要影响。Zr重分配的迟缓动力学（低互扩散系数）解释了相变滞后现象。

## 关键词
U-10Zr, 挤压, 原位高温中子衍射, 织构, 晶格参数, 相变滞后, 变体选择

## Related Work
- [[wiki/summaries/2025_Williams_UZr_PhaseDiagram|2025_Williams_UZr_PhaseDiagram]] — U-Zr相图评估，本文实验支持Bauer相图而非Sheldon相图
- [[wiki/summaries/2021_Hirschhorn_CALPHAD_BISON_Redistribution|2021_Hirschhorn_CALPHAD_BISON_Redistribution]] — CALPHAD组元再分布模型，本文提供U-Zr相变温度和织构数据
- [[wiki/concepts/ConstituentRedistribution|ConstituentRedistribution]] — 本文相变滞后和织构数据对组元再分布建模有重要意义
- [[wiki/summaries/2020_Yao_AlphaOmega_U10Zr|2020_Yao_AlphaOmega_U10Zr]] — 同为U-10Zr显微组织研究，本文提供热循环相变数据
