# Extended fuel swelling models and ultra high burn-up fuel behavior of U–Pu–Zr metallic fuel using FEAST-METAL

**Authors:** Aydın Karahan, Nathan C. Andrews (MIT)  
**Year:** 2013  
**Journal:** Journal of Nuclear Materials  
**Slug:** 2013_Karahan_FEAST_ExtendedSwelling_UPuZr

## English Summary (200-400 words)

This paper presents significant upgrades to the FEAST-METAL metallic fuel behavior code, focusing on improved fission gas swelling models, pressure sintering behavior, and ultra-high burn-up predictions for U-Pu-Zr metallic fuel. The key modeling improvements include: (1) replacing the constant-volume bubble grouping scheme with a constant-atom-number scheme in the GRSIS fission gas algorithm, where small and large bubble groups each contain a fixed number of gas atoms; (2) implementing phase-structure-dependent bubble morphology, with ellipsoidal bubbles in the (α+δ) dual phase, small spherical bubbles in the (β+γ) dual phase, and large spherical bubbles (up to ~10 μm) in the single γ phase; (3) adopting phase-dependent gas diffusion coefficients using activation energies from Gruber and Kramer (1987), with Tγ = 923 K as the single γ-phase transition temperature; and (4) introducing a correction factor C = 0.23 for dual-phase compressibility in the hot-pressing model, compared to C = 1.0 for single γ phase, significantly improving coupled fuel behavior predictions. The solid fission product swelling rate is updated from 1.5% to 1.2% per at.% burn-up (Hofman et al. 1997 best estimate). A probabilistic verification confirms the 10% gas swelling threshold for interconnected porosity formation remains valid across a wide range of bubble sizes (1.5–6 μm average diameter).

The code is benchmarked against EBR-II X425 and X430 assemblies, showing satisfactory agreement in clad hoop strain, fission gas release, and axial elongation. Ultra-high burn-up simulations (up to 36 at.%, ~500 dpa) of vented U-6Zr fuel with HT9 cladding at 60% smear density predict a peak clad hoop strain of 3% (1% void swelling + 2% irradiation creep), 95% fission gas release, 20% fuel axial elongation, and <20% clad wastage at peak clad temperatures below 550°C. The study recommends a porous, chemically stable buffer layer at the fuel-clad interface to mitigate FCCI and accommodate solid fission product swelling.

## 中文摘要 (200-400词)

本文对FEAST-METAL金属燃料行为程序进行了重大升级，重点改进了裂变气体肿胀模型、压力烧结行为和U-Pu-Zr金属燃料的超高压燃耗预测能力。主要建模改进包括：(1) 在GRSIS裂变气体算法中将恒定体积气泡分组方案替换为恒定原子数方案，大小气泡组各包含固定数量的气体原子；(2) 实现了相结构依赖的气泡形态学，(α+δ)双相区为椭球形气泡，(β+γ)双相区为小球形气泡，单γ相区为大球形气泡（最大约10 μm）；(3) 采用相依赖的气体扩散系数，使用Gruber和Kramer (1987)的活化能数据，单γ相转变温度Tγ = 923 K；(4) 在热压模型中引入双相压缩性修正因子C = 0.23（单γ相C = 1.0），显著改善了耦合燃料行为预测。固态裂变产物肿胀率从每at.%燃耗1.5%更新为1.2%（Hofman等1997最佳估计值）。概率验证确认10%气体肿胀阈值在宽气泡尺寸范围（1.5–6 μm平均直径）内对连通孔隙形成有效。

程序经EBR-II X425和X430组件验证，包壳环向应变、裂变气体释放和轴向伸长量与实验吻合良好。超高压燃耗模拟（最高36 at.%，约500 dpa）采用排气式U-6Zr燃料、HT9包壳、60%涂抹密度，预测峰值包壳环向应变为3%（1%空洞肿胀+2%辐照蠕变），裂变气体释放率95%，燃料轴向伸长20%，包壳峰值温度低于550°C时包壳损耗低于20%。研究建议在燃料-包壳界面设置多孔、化学稳定的缓冲层以缓解FCCI并容纳固态裂变产物肿胀。

## Related Work
- [[wiki/entities/FEASTMETALCode|FEASTMETALCode]] — this paper extends FEAST-METAL code capabilities
- [[wiki/entities/UPuZrFuel|UPuZrFuel]] — fuel system for ultra-high burnup simulations
- [[wiki/entities/HT9Cladding|HT9Cladding]] — cladding material in simulations
- [[wiki/summaries/2010_Karahan_FEAST_ThermoMechanical_MetallicFuel|2010_Karahan_FEAST_ThermoMechanical_MetallicFuel]] — original FEAST-METAL code paper
- [[wiki/concepts/FuelCladdingChemicalInteraction|FuelCladdingChemicalInteraction]] — FCCI mitigation via buffer layer proposal
