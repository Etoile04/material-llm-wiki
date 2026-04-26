# 2010_Karahan_FEAST_ThermoMechanical_MetallicFuel

**Title:** A new code for predicting the thermo-mechanical and irradiation behavior of metallic fuels in sodium fast reactors

**Authors:** Aydın Karahan, Jacopo Buongiorno (MIT)

**Journal:** Journal of Nuclear Materials 396 (2010) 283–293

**DOI:** 10.1016/j.jnucmat.2009.11.022

---

## English Summary

FEAST-METAL is a new FORTRAN-90 engineering code developed at MIT for predicting the steady-state and transient thermo-mechanical behavior of U-Zr and U-Pu-Zr metallic fuel pins in sodium fast reactors. The code couples multiple modules: (1) fission gas release and swelling using the GRSIS mechanistic bubble-tracking algorithm, where bubbles are classified into small (<0.5 μm), large (~10 μm), and open pores, with gas release triggered at 10% matrix swelling; (2) fuel constituent redistribution via thermo-transport theory, modeling radial Zr migration driven by temperature gradients across α, δ, β, and γ phase regions; (3) fuel-clad chemical interaction (FCCI) using a precipitation-kinetics diffusion model with separate treatments for steady-state lanthanide diffusion (D₀ = 1350 m²/s, Q = 300 kJ/mol) and transient eutectic formation (D₀ = 4.2×10⁶ m²/s, Q = 400 kJ/mol); (4) 1D mechanical analysis with anisotropic fuel slug deformation and hot-pressing model; and (5) a constrained diffusional cavity growth model for intergranular creep-fracture of HT9 cladding during transients. The code was validated against EBR-II irradiation data (X425, X430, X447 assemblies) and furnace transient tests, showing good agreement for clad strain, FGR, clad wastage, and failure time predictions across burnups of 2–19 at.% and peak clad temperatures of 550–820°C.

## 中文摘要

FEAST-METAL 是麻省理工学院开发的 FORTRAN-90 工程分析程序，用于预测钠冷快堆中 U-Zr 和 U-Pu-Zr 合金燃料棒的稳态及瞬态热工力学行为。该程序耦合了多个模块：（1）基于 GRSIS 气泡追踪算法的裂变气体释放与肿胀模型，气泡分为小泡（<0.5 μm）、大泡（~10 μm）和开孔隙三类，基体肿胀达 10% 时触发气体释放；（2）基于热传输理论的燃料组元再分布模型，模拟 Zr 在 α、δ、β、γ 相区间的径向迁移；（3）基于沉淀动力学扩散模型的燃料-包壳化学相互作用（FCCI）模型，稳态镧系元素扩散（D₀=1350 m²/s, Q=300 kJ/mol）和瞬态共晶形成分别处理；（4）含各向异性燃料棒变形和热压模型的 1D 力学分析；（5）基于约束扩散腔生长模型的 HT9 包壳晶间蠕变断裂模型。程序经 EBR-II 辐照数据（X425、X430、X447 组件）和炉内瞬态试验验证，在 2–19 at.% 燃耗和 550–820°C 峰值包壳温度范围内，包壳应变、裂变气体释放率、包壳损耗和破断时间预测与实验数据吻合良好。

## Key Models

| Module | Model Type | Key Parameters |
|--------|-----------|----------------|
| Fission Gas Release + Swelling | GRSIS bubble tracking | Gas diffusion: Q=52000 cal/gmol, D₀=2.3×10⁻³ m²/s; Open porosity threshold: 10% |
| Constituent Redistribution | Thermo-transport theory | Phase-dependent Zr diffusion + heat of transport |
| Steady-state FCCI | Precipitation kinetics | D₀L=1350 m²/s, QL=300 kJ/mol, lanthanide solubility in clad: 0.1 |
| Transient FCCI | Precipitation kinetics | D₀Fe=4.2×10⁶ m²/s, QFe=400 kJ/mol |
| Mechanical Analysis | 1D LIFE algorithm | Solid FP swelling: 1.5%/at.%; Isotropic swelling assumption |
| Clad Creep Fracture | Constrained cavity growth | CDF + diffusional cavity model; critical radius lookup table for HT9 |

## Related Work
- [[wiki/entities/FEASTMETALCode|FEASTMETALCode]] — this paper introduces the FEAST-METAL code
- [[wiki/entities/EBR-II|EBR-II]] — EBR-II X425/X430/X447 assemblies used for validation
- [[wiki/entities/HT9Cladding|HT9Cladding]] — cladding material with FCCI and creep fracture models
- [[wiki/concepts/FuelCladdingChemicalInteraction|FuelCladdingChemicalInteraction]] — FCCI model with lanthanide diffusion
- [[wiki/summaries/2013_Karahan_FEAST_ExtendedSwelling_UPuZr|2013_Karahan_FEAST_ExtendedSwelling_UPuZr]] — extended version with improved swelling models
- [[wiki/summaries/1996_Ogata_FissionGasBehavior_MetallicFuel|1996_Ogata_FissionGasBehavior_MetallicFuel]] — ALFUS code, a predecessor for metallic fuel modeling
