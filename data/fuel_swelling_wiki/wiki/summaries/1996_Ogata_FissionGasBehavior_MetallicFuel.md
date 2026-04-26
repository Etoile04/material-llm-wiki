# Summary: 1996_Ogata_FissionGasBehavior_MetallicFuel

**Source:** T. Ogata, M. Kinoshita, H. Saito, T. Yokoo, Journal of Nuclear Materials 230 (1996) 129–139

## English

This paper describes the ALFUS (ALoyed Fuel Unified Simulator) code for mechanistic simulation of gas release and deformation in U-Zr metallic fast reactor fuel. ALFUS integrates: (1) a stress-strain finite element model with anisotropic "tearing" strain from α-uranium grain/phase boundary cavitation; (2) a fission gas behavior model with 5-class grain boundary bubble coalescence, open pore formation, and gas release; (3) thermal models with sodium infiltration of open pores. The tearing model introduces anisotropic swelling in the low-temperature α-phase region (<600°C), with rate ktr = 12% ΔV/V₀/at.% up to BUlimit = 2.0 at.%, and anisotropy ratios {Rr, Rθ, Rz} = {0.5, 0.5, 0.0}. Creep and open pore volume decrease are coupled through a modified hot-press model. Gas release occurs via two paths: open pore formation at threshold swelling εsw = 0.20 (connected bubble onset) and εsw = 0.33 (breakaway), plus collision of gas atoms/bubbles with existing open pores. Key fitted parameters include: bubble diffusion adjustment factor Cadj = 20, open pore gas amount m₆ = 4.02×10⁻¹⁸ mol, and tearing rate 12%/at.%. Validation against EBR-II U-10Zr fuel pins (X423 and X419/X420/X421 assemblies) shows good agreement with slug axial elongation and fractional gas release data. The analysis reveals that open pore volume accommodates closed bubble swelling after slug-cladding contact, keeping FCMI negligible for ≤75% smear density. For >80% smear density, insufficient space prevents open pore formation, leading to significant FCMI — consistent with experimental cladding strain data.

## 中文

本文介绍了ALFUS（合金燃料统一模拟器）代码，用于力学机理模拟U-Zr金属快堆燃料的气体释放和变形行为。ALFUS整合了：（1）包含α-铀晶界/相界空洞化引起的各向异性"撕裂"应变的应力-应变有限元模型；（2）5类晶界气泡聚合、开放孔隙形成和气体释放的裂变气体行为模型；（3）考虑钠渗入开放孔隙的热工模型。撕裂模型在低温α相区（<600°C）引入各向异性肿胀，撕裂速率 ktr = 12% ΔV/V₀/at.%，上限燃耗 BUlimit = 2.0 at.%，各向异性比 {Rr, Rθ, Rz} = {0.5, 0.5, 0.0}。气体释放通过两条路径实现：开放孔隙在阈值肿胀 εsw = 0.20 时开始形成，εsw = 0.33 时完全贯通，以及气体原子/气泡与已有开放孔隙碰撞。关键拟合参数包括气泡扩散调节因子 Cadj = 20。经EBR-II U-10Zr燃料棒验证，与轴向伸长和气体释放数据吻合良好。分析表明，燃料芯块-包壳接触后开放孔隙容纳闭合气泡肿胀，使≤75%涂敷密度下FCMI可忽略。>80%涂敷密度时空间不足导致显著FCMI，与实验包壳应变数据一致。

**Keywords:** ALFUS, U-Zr, metallic fuel, fission gas release, swelling, FCMI, tearing strain, smear density, open pore, fast reactor

## Related Work
- [[wiki/entities/U10ZrFuel|U10ZrFuel]] — fuel system validated with EBR-II U-10Zr pins
- [[wiki/entities/EBR-II|EBR-II]] — irradiation data source for code validation
- [[wiki/concepts/FissionGasReleaseModels|FissionGasReleaseModels]] — ALFUS contributes a mechanistic FGR model for metallic fuel
- [[wiki/summaries/1992_Tsuboi_FissionGasBehavior_MetallicFuel|1992_Tsuboi_FissionGasBehavior_MetallicFuel]] — precursor SESAME model for metallic fuel fission gas behavior
- [[wiki/summaries/2010_Karahan_FEAST_ThermoMechanical_MetallicFuel|2010_Karahan_FEAST_ThermoMechanical_MetallicFuel]] — FEAST-METAL code with similar coupling of FGR and mechanics
- [[wiki/summaries/2013_Karahan_FEAST_ExtendedSwelling_UPuZr|2013_Karahan_FEAST_ExtendedSwelling_UPuZr]] — extended FEAST-METAL with improved swelling models
