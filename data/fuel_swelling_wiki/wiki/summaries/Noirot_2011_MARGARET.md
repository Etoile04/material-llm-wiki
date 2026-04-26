# Noirot (2011) - MARGARET裂变气体行为代码

**论文**: MARGARET: A comprehensive code for the description of fission gas behavior  
**期刊**: Nuclear Engineering and Design 241 (2011) 2099–2118  
**作者**: L. Noirot (CEA)

## 摘要

本文详细描述了MARGARET代码，一个综合性的裂变气体行为描述代码，用于模拟核燃料中稳定裂变气体（主要为Xe）的行为。代码将相关现象分为晶内和晶间两个尺度，并在燃料经历正常状态、部分重构(PRS)状态和高燃耗结构(HBS)状态时采用不同的方程组。

MARGARET的晶内模型描述了溶解态Xe的扩散、纳米气泡的形核与长大、沉淀泡的热诱发形核、孔隙的捕获和气体重溶。晶间模型处理了晶界气泡的形核、长大、连通和最终释放。Xe在UO₂中的扩散系数由三项组成：热扩散、混合扩散和纯辐照项。

代码采用了精细的物理模型：气泡内压力通过硬球(Carnahan-Starling)方程或Van der Waals方程计算；重溶频率基于Olander模型并考虑气泡尺寸效应；空位平衡浓度考虑静水压力和表面张力的影响。PRS状态模型实现了从正常结构到HBS的渐进过渡。文章通过61 GWd/tU的UO₂燃料验证了代码，计算与SEM/EPMA实验数据吻合良好。

## Key Equations

$$D_{Xe}^{th} = 5 \times 10^{-5} \exp(-45200/T_K) \text{ m}^2/\text{s}$$

$$D_{Xe}^{mix} = 6.95 \times 10^{-25} F \exp(-13870/T_K) \text{ m}^2/\text{s}$$

$$D_{Xe}^{ath} = 6 \times 10^{-40} F \text{ m}^2/\text{s}$$

Xe在UO₂中扩散系数的三个分量。

$$b_0 = 8 \times 10^{-24} r_e(cav) \cdot F \text{ s}^{-1}$$

重溶频率（Olander模型）。

$$D_U^{th} = 6.5 \times 10^{-5} \exp(-64902/T_K) \text{ m}^2/\text{s}$$

阳离子(U)热扩散系数。

$$\frac{dC_{brim}}{dt} = C_{brim0} \frac{df_r}{dt}$$

HBS区域rim气泡密度演化方程。

## Related Work
- [[wiki/concepts/FissionGasReleaseModels|FissionGasReleaseModels]] — MARGARET是裂变气体释放综合建模代码的典型代表
- [[wiki/concepts/RateTheoryFramework|RateTheoryFramework]] — 代码基于速率理论框架描述晶内/晶间气体行为
- [[wiki/summaries/2002_Bernard_FissionGasModel|2002_Bernard_FissionGasModel]] — 同为CEA裂变气体建模工作，与MARGARET一脉相承
- [[wiki/summaries/Bernard_2002_FissionGasModel|Bernard_2002_FissionGasModel]] — CEA裂变气体行为建模的平行工作
- [[wiki/summaries/2001_Rest_GRSIS_FissionGasMetallic|2001_Rest_GRSIS_FissionGasMetallic]] — 裂变气体释放与肿胀模型的对比参考
- [[wiki/summaries/VanUffelen_2019_FuelPerformanceReview|VanUffelen_2019_FuelPerformanceReview]] — 燃料性能建模综述，涵盖裂变气体行为代码
