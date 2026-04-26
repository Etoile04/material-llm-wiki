# Hales_2016_BISON_TheoryManual - 中文摘要

**论文标题**: BISON Theory Manual: The Equations Behind Nuclear Fuel Analysis (BISON Release 1.3)

**作者**: J.D. Hales, R.L. Williamson, S.R. Novascone, G. Pastore, B.W. Spencer, D.S. Stafford, K.A. Gamble, D.M. Perez, R.J. Gardner, W. Liu, J. Galloway, C. Matthews, C. Unal, N. Carlson

**期刊/来源**: INL/EXT-13-29930 Rev. 3, September 2016

## 摘要

BISON是美国爱达荷国家实验室(INL)开发的多维多物理场核燃料性能分析程序，基于MOOSE有限元框架。本理论手册详细记录了BISON中实现的所有物理模型和数学方程，涵盖UO₂、MOX、U₃Si₂、U-Pu-Zr金属燃料等多种燃料类型以及Zr合金包壳。

热学模型包括燃料热导率（考虑燃耗和孔隙率效应）、热膨胀和比热容。U-Pu-Zr金属燃料的热导率采用Billone模型，随Zr含量和温度变化。力学模型涵盖弹性、塑性、蠕变（热蠕变和辐照蠕变）以及燃料-包壳相互作用。

辐照行为模型包括：裂变气体释放（基于晶内扩散-气泡-重溶解机制）、辐照肿胀（固体FP肿胀和气体肿胀）、燃料密实化和重定位。对于U-Pu-Zr燃料，气体肿胀采用体积肿胀模型[VSwellingUPuZr]，气体释放通过孔隙率阈值触发。

Zr重分布模型是BISON金属燃料模块的核心之一。该模型基于Galloway等人的工作，考虑了相依赖的Fick扩散和Soret热扩散，在简化伪二元相图上求解耦合的热传导-扩散方程。模型改进了早期工作中溶解焓与相图的不一致性，引入了人工扩散项以稳定有限元求解。

## Key Equations

- Zr通量(单相): $J_{Zr} = c_0 D \\left(-\\nabla x_{Zr} + \\frac{x_{Zr}(1-x_{Pu}-x_{Zr})}{1-x_{Pu}} \\frac{Q^*}{RT^2} \\nabla T\\right)$
- 溶解度曲线: $X(T) = (1-x_{Pu})\\left[1 + \\left(\\frac{x_{Pu}-X_0}{X_0}\\right)\\exp\\left(\\frac{\\Delta H}{R}\\left(\\frac{1}{T}-\\frac{1}{T_0}\\right)\\right)\\right]^{-1}$
- 耦合方程: $\\rho c_p \\frac{\\partial T}{\\partial t} = \\nabla \\cdot k(x,T)\\nabla T + q(r,x)$, $\\frac{\\partial x}{\\partial t} = \\nabla \\cdot D(x,T)\\nabla x + \\nabla \\cdot S(x,T)\\nabla T$
- 间隙压力: $P = nRT/V$
- Dittus-Boelter: $Nu = 0.023 Re^{0.8} Pr^{0.4}$

## Related Work
- [[wiki/entities/BISONCode|BISONCode]] — 本文即BISON理论手册
- [[wiki/concepts/FuelPerformanceCodes|FuelPerformanceCodes]] — BISON属燃料性能分析程序
- [[wiki/summaries/2015_Galloway_ConstituentRedistribution_UPuZr_BISON|2015_Galloway_ConstituentRedistribution_UPuZr_BISON]] — BISON中U-Pu-Zr组元再分布模型
- [[wiki/summaries/2021_Paaren_AutomatedFuelPerformance_BISON_EBR2|2021_Paaren_AutomatedFuelPerformance_BISON_EBR2]] — BISON自动化燃料性能分析
- [[wiki/concepts/ConstituentRedistribution|ConstituentRedistribution]] — Zr重分布模型为BISON金属燃料核心
- [[wiki/summaries/2020_Aagesen_BisonUPuZrSwellingLowerLengthScale|2020_Aagesen_BisonUPuZrSwellingLowerLengthScale]] — BISON U-Pu-Zr肿胀模型
