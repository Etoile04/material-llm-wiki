# Summary: Constituent Redistribution in U-Zr Fuels Using Quantitative Phase-Field Modeling

**Authors:** J. Hirschhorn, M.R. Tonks, A. Aitkaliyeva, C. Adkins (2019)  
**Journal:** Journal of Nuclear Materials 523, 143–156

## English Summary

Hirschhorn et al. developed a quantitative phase-field model for constituent redistribution in U-Zr fuels using the MARMOT code (MOOSE framework). Unlike previous studies using sharp-interface finite-difference approaches, this model employs diffuse interfaces with CALPHAD-derived thermodynamic descriptions and DICTRA atomic mobilities for the γ-phase. The model couples Cahn-Hilliard (conserved composition) and Allen-Cahn (non-conserved phase fraction) equations with heat generation and transport. Using Hofman et al.'s (1996) EBR-II PIE data from DP-81 and DP-11 as optimization and validation datasets, the model was optimized with only four parameters (D₀ᵝ, Mcᵞ, Q̃ᵦᵀ, MTᵞ) using DAKOTA. Diffusivities required enhancement (~10× for Mcᵞ, ~2.7× for D₀ᵝ), supporting irradiation-enhanced diffusion. Crucially, no modification of phase transition temperatures was needed. Sensitivity analysis revealed that β and γ kinetic parameters scale the magnitude of redistribution, while swelling (kswell) and sodium infiltration (kinfil) parameters influence the size, shape, and location of the Zr bathtub. Fuel surface temperature was the most influential parameter overall. The γ/b+γ interface mobility was particularly important in forming the Zr bathtub. The model confirmed that Q̃ᵞᵀ ≈ −50 to −100 kJ/mol, consistent with Hofman et al.'s estimate.

## 中文摘要

Hirschhorn等人使用MARMOT代码（MOOSE框架）开发了U-Zr燃料组元再分布的定量相场模型。与以往采用锐界面有限差分方法的研究不同，该模型采用弥散界面描述，结合CALPHAD热力学数据和DICTRA原子迁移率描述γ相动力学。模型耦合了Cahn-Hilliard方程（守恒组分）和Allen-Cahn方程（非守恒相分数）以及热生成与传输。以Hofman等人（1996）的EBR-II辐照后检验数据DP-81和DP-11分别为优化和验证数据集，使用DAKOTA仅优化四个参数（D₀ᵝ, Mcᵞ, Q̃ᵦᵀ, MTᵞ）即可达到与以往模型相当的精度。扩散系数需增强（Mcᵞ约10倍，D₀ᵝ约2.7倍），支持辐照增强扩散假说。关键发现是无需修改相变温度。敏感性分析表明β和γ相动力学参数控制再分布幅度，而肿胀（kswell）和钠渗入（kinfil）参数影响Zr浴缸的大小、形状和位置。燃料表面温度是影响最大的单一参数。γ/b+γ界面的移动性对Zr浴缸的形成特别重要。模型确认Q̃ᵞᵀ ≈ −50至−100 kJ/mol，与Hofman等人的估计一致。

## Key Parameters
- Fuel: U-10Zr wt% (DP-81, DP-11)
- Phase field: KKS formalism, interface width 500 μm, energy 0.5 J/m²
- Optimized: D₀ᵝ ×2.722, Mcᵞ ×9.981, Q̃ᵦᵀ ×0.617, MTᵞ ×1.395
- Q̃ᵞᵀ ≈ −50 to −100 kJ/mol
- Domain: 2170 μm radius, 1000 elements
- Phase mobility L = 2.5×10⁻¹⁰ m³/(J·s)

## Related Work
- [[wiki/concepts/ConstituentRedistribution|ConstituentRedistribution]] — 本文核心主题，U-Zr燃料组元再分布的相场建模
- [[wiki/concepts/PhaseFieldModelingRedistribution|PhaseFieldModelingRedistribution]] — 本文使用定量相场方法(Cahn-Hilliard/Allen-Cahn)建模组元再分布
- [[wiki/entities/PhaseFieldModeling|PhaseFieldModeling]] — 本文在MARMOT/MOOSE框架中实现相场模型
- [[wiki/summaries/1996_Hofman_TemperatureGradientRedistribution_UZr|1996_Hofman_TemperatureGradientRedistribution_UZr]] — 本文使用Hofman的EBR-II PIE数据(DP-81, DP-11)进行模型验证
- [[wiki/summaries/2015_Galloway_ConstituentRedistribution_UPuZr_BISON|2015_Galloway_ConstituentRedistribution_UPuZr_BISON]] — BISON中U-Pu-Zr组元再分布模型，与本文方法对比
- [[wiki/summaries/2020_Hirschhorn_UZr_DiffusionCouple_PF|2020_Hirschhorn_UZr_DiffusionCouple_PF]] — 同一作者组，U-Zr扩散偶的相场模拟
