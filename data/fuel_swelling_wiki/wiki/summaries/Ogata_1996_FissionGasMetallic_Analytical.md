# Ogata_1996_FissionGasMetallic_Analytical - 中文摘要

**论文标题**: Analytical model for fission gas release and swelling in metallic fast reactor fuels

**作者**: T. Ogata, M. Ishida, T. Tayama, T. Onose

**期刊/来源**: Journal of Nuclear Materials (1996)

## 摘要

本文提出了ALFUS（Analysis of LWR Fuel under Steady-state）代码中用于U-Zr合金燃料裂变气体行为分析的解析模型。该模型采用Booth等效球模型，将燃料晶粒近似为球形，通过求解气体原子在球内的扩散方程来计算裂变气体的产生、扩散和释放。

模型的核心是将复杂的偏微分扩散方程通过无量纲化转化为解析解形式。定义了两个关键无量纲参数：α=b·a²/D（描述重溶解与扩散的相对强度）和β=Y·ḟ·a²/D（描述气体产生与扩散的相对速率）。通过这些参数，可以解析地给出晶内气体浓度分布和气体释放分数的时间演化。

模型考虑了裂变气体在金属燃料中的特殊行为：极低的气体固溶度、辐照驱动的气体原子重溶解机制、以及气泡形核-生长-粗化的演化过程。气体肿胀通过气泡体积分数的增长来计算，与气体释放分数直接关联。

ALFUS模型在EBR-II快堆实验数据上进行了验证，覆盖了不同燃耗水平（最高约10 at%），结果表明解析模型能较好地预测裂变气体释放分数和气体肿胀率，适用于工程级的燃料性能分析。

## Related Work
- [[wiki/concepts/FissionGasReleaseModels|FissionGasReleaseModels]] — 本文提出金属燃料裂变气体释放的解析模型
- [[wiki/entities/EBR-II|EBR-II]] — 模型在EBR-II实验数据上验证
- [[wiki/summaries/2001_Rest_GRSIS_FissionGasMetallic|2001_Rest_GRSIS_FissionGasMetallic]] — 金属燃料裂变气体释放的对比模型
- [[wiki/summaries/1996_Ogata_FissionGasBehavior_MetallicFuel|1996_Ogata_FissionGasBehavior_MetallicFuel]] — 同作者同期关于金属燃料裂变气体行为的工作
- [[wiki/summaries/2013_Yun_GRASSSST_UPuZr|2013_Yun_GRASSSST_UPuZr]] — GRASS-SST裂变气体释放模型，可与解析模型对比

## Key Equations

- 有效扩散系数: $D = D_0 \\exp(-Q_D/RT)$, $D_0 = 1.5 \\times 10^{-6}$ m²/s, $Q_D = 177$ kJ/mol
- 无量纲参数: $\\alpha = ba^2/D$, $\\beta = Y\\dot{f}a^2/D$
- 气体释放分数: $F(t) = 1 - \\frac{6}{\\pi^2}\\sum_{n=1}^{\\infty} \\frac{1}{n^2} \\exp\\left(-\\frac{n^2\\pi^2 D t}{a^2}\\right)$
- 稳态气体浓度: $C_{ss} = Y\\dot{f}/b$
- 气泡内压: $p = \\frac{nkT}{4\\pi r^3/3}$
