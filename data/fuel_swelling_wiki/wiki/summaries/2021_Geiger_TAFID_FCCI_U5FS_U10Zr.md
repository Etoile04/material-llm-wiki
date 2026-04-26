# 2021_Geiger_TAFID_FCCI_U5FS_U10Zr

## Metadata
- **Title:** Thermodynamic Investigations of Fuel-Cladding Chemical Interaction in U-5Fs and U-10Zr Metallic Fuels with the TAF-ID
- **Authors:** E. Geiger, C. Guéneau, E.C. Corcoran, M.H.A. Piro
- **Journal:** Journal of Nuclear Materials 551 (2021) 152981
- **DOI:** 10.1016/j.jnucmat.2021.152981

## Summary (English)

This study evaluates the TAF-ID (Thermodynamics of Advanced Fuels – International Database) for predicting Fuel-Cladding Chemical Interaction (FCCI) phases in two irradiated metallic fuels: U-5Fs in SS316 cladding (540°C, 7.48% burn-up) and U-10Zr in HT9 cladding (615°C, 5.70% burn-up). Using Thermo-Calc v.2018b with TAF-ID v.10, equilibrium thermodynamic calculations were performed assuming a linear Fe diffusion profile from the cladding into the fuel. For U-10Zr, predicted phases include α-U, BCC#1/BCC#2 (U-Zr), λ-FeUZr, Fe₃U₃Zr₄, χ-FeUZr, FeU₆, ZrFe₂, UFe₂, FCC (Ce,Nd,La,Sr,Y,Pu), NdPd, and Fe₁₇Ln₂. For U-5Fs, predicted phases include α-U, FeU₆, UFe₂, NiZr, U₇Ni₉, HCP/FCC (Ce-Nd), NdPd, and Fe₁₇Ln₂. Calculations agree well with SEM-EDS experimental characterizations from Harp et al., confirming most observed phases. Limitations include the equilibrium assumption and missing binary assessments (Ni-Ce, Ni-Pd, Ni-Nd, Ce-Pd) in TAF-ID v.10. The work demonstrates TAF-ID's capability for FCCI modelling and suggests coupling thermodynamic with kinetic calculations for improved accuracy.

## 摘要（中文）

本研究评估了TAF-ID（先进燃料热力学国际数据库）在预测两种辐照金属燃料——U-5Fs/SS316包壳（540°C，燃耗7.48%）和U-10Zr/HT9包壳（615°C，燃耗5.70%）——燃料-包壳化学相互作用（FCCI）相的能力。采用Thermo-Calc v.2018b和TAF-ID v.10，假设Fe从包壳向燃料线性扩散，进行平衡热力学计算。U-10Zr预测相包括α-U、BCC#1/BCC#2、λ-FeUZr、Fe₃U₃Zr₄、χ-FeUZr、FeU₆、ZrFe₂、UFe₂、FCC（Ce,Nd,La,Sr,Y,Pu）、NdPd和Fe₁₇Ln₂。U-5Fs预测相包括α-U、FeU₆、UFe₂、NiZr、U₇Ni₉、HCP/FCC（Ce-Nd）、NdPd和Fe₁₇Ln₂。计算结果与Harp等的SEM-EDS实验表征吻合良好。局限包括平衡假设及TAF-ID v.10中缺少Ni-Ce、Ni-Pd、Ni-Nd、Ce-Pd等二元系评估。该工作展示了TAF-ID用于FCCI建模的能力，建议耦合热力学与动力学计算以提升精度。

## Key Findings
- TAF-ID accurately predicts most FCCI phases observed experimentally in both U-10Zr and U-5Fs fuels
- Key predicted phases: χ-FeUZr, UFe₂, FeU₆, FCC lanthanoid phase, Fe₁₇Ln₂
- Equilibrium assumption is a significant limitation; kinetic coupling needed
- Missing binary system assessments (Ni-Ce, Ni-Pd, Ce-Pd) limit prediction accuracy
- BCC miscibility gap in U-10Zr disappears below 597°C, relevant for post-irradiation characterization

## Tags
`TAF-ID`, `FCCI`, `metallic-fuel`, `U-10Zr`, `U-5Fs`, `thermodynamic-modelling`, `CALPHAD`, `Thermo-Calc`

## Related Work
- [[wiki/concepts/FuelCladdingChemicalInteraction|FuelCladdingChemicalInteraction]] — 本文核心主题：FCCI相的热力学预测
- [[wiki/summaries/2017_Matthews_FCCI_CriticalReview_UPuZr|2017_Matthews_FCCI_CriticalReview_UPuZr]] — FCCI综述，本文为FCCI热力学预测的具体实现
- [[wiki/summaries/2021_Hirschhorn_CALPHAD_BISON_Redistribution|2021_Hirschhorn_CALPHAD_BISON_Redistribution]] — CALPHAD方法在BISON中的应用，与本文TAF-ID热力学建模互补
- [[wiki/summaries/2016_Carmack_FCCI_MFF3_Metallography|2016_Carmack_FCCI_MFF3_Metallography]] — MFF-3 FCCI实验金相数据，本文引用Harp等实验数据进行验证
- [[wiki/summaries/Piro_2021_ThermodynamicFuelCodes|Piro_2021_ThermodynamicFuelCodes]] — 燃料热力学建模综述，本文TAF-ID方法的理论背景
