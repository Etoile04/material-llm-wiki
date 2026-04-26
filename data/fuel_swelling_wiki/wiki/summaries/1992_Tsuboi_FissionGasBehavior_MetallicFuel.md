# Summary: 1992_Tsuboi_FissionGasBehavior_MetallicFuel

**Source:** Y. Tsuboi, T. Ogata, M. Kinoshita, H. Saito, Journal of Nuclear Materials 188 (1992) 312–318

## English

This paper presents a mechanistic model for fission gas swelling and release in metallic fuel, developed as part of the SESAME fuel performance code effort. The model couples intragranular gas migration (based on the modified OGRES model) with a grain boundary bubble coalescence and growth model. Intragranular behavior accounts for gas atom generation, diffusion, re-solution from bubbles, trapping by bubbles, and bubble nucleation. Grain boundary bubbles are classified into six classes by gas content; coalescence occurs through random and biased migration (temperature-gradient-driven). Closed bubbles (classes 1–5) contribute to swelling, while open bubbles (class 6) enable gas release. Swelling is calculated from bubble volumes equilibrated by internal gas pressure, surface tension, and external pressure. Gas release probability from closed to open bubbles is a function of local swelling (ΔV/V). A critical swelling parameter (Bᵥ = 0.07) limits open bubble swelling to model tunnel saturation. The model is validated against irradiated uranium metal annealing experiments at 1173 K under pressures of 0–100 MPa, showing good agreement with measured swelling and bubble size distributions. Key model parameters include: re-solution coefficient b = 10⁻⁶ s⁻¹, bubble generation coefficient k = 10⁻⁷ s⁻¹, gas atom diffusion Dg = 1.4×10⁻⁵ exp(−5200/RT) m²/s, surface diffusion Ds = 16.6 exp(−40Tm/RT) + 1.4×10⁻⁶ exp(−13Tm/RT) m²/s, surface tension γ = 0.8 N/m, and grain size 10 μm.

## 中文

本文提出了金属燃料裂变气体肿胀和释放的力学机理模型，作为SESAME燃料性能代码开发的一部分。模型将晶内气体迁移（基于改进的OGRES模型）与晶界气泡聚合生长模型相耦合。晶内行为考虑了气体原子产生、扩散、气泡再溶解、捕获和形核。晶界气泡按气体含量分为六个类别，通过随机迁移和偏压迁移（温度梯度驱动）发生聚合。闭合气泡（1–5类）贡献肿胀，开放气泡（第6类）实现气体释放。肿胀由气泡体积计算，气泡内部气体压力与表面张力和外部压力平衡。从闭合气泡到开放气泡的转变概率是局部肿胀（ΔV/V）的函数。临界肿胀参数（Bᵥ = 0.07）限制开放气泡肿胀以模拟隧道饱和。模型经铀金属在1173 K、0–100 MPa压力下退火实验验证，与实测肿胀和气泡尺寸分布吻合良好。关键参数包括：再溶解系数 b = 10⁻⁶ s⁻¹、气泡生成系数 k = 10⁻⁷ s⁻¹、气体原子扩散系数 Dg = 1.4×10⁻⁵ exp(−5200/RT) m²/s、表面扩散系数 Ds、表面张力 γ = 0.8 N/m、晶粒尺寸 10 μm。

**Keywords:** metallic fuel, fission gas, swelling, gas release, bubble coalescence, mechanistic model, grain boundary, re-solution, uranium

## Related Work
- [[wiki/entities/EBR-II|EBR-II]] — metallic fuel irradiation experiments providing validation data
- [[wiki/concepts/GasBubbleCoalescence|GasBubbleCoalescence]] — grain boundary bubble classification and coalescence mechanism central to this model
- [[wiki/summaries/1996_Ogata_FissionGasBehavior_MetallicFuel|1996_Ogata_FissionGasBehavior_MetallicFuel]] — ALFUS code extends similar bubble coalescence and gas release modeling to U-Zr fuel
- [[wiki/summaries/2010_Karahan_FEAST_ThermoMechanical_MetallicFuel|2010_Karahan_FEAST_ThermoMechanical_MetallicFuel]] — FEAST-METAL code uses GRSIS algorithm for fission gas behavior in metallic fuel
- [[wiki/concepts/FissionGasReleaseModels|FissionGasReleaseModels]] — this work contributes a mechanistic FGR model for metallic fuel
