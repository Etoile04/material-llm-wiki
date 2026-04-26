# 1993_Rest_CavitationalSwellingAlphaUPuZr

## 基本信息
- **标题**: Fission Gas Bubble Nucleated Cavitational Swelling of the Alpha-Uranium Phase of Irradiated U-Pu-Zr Fuel
- **作者**: J. Rest
- **机构**: Argonne National Laboratory
- **来源**: ASTM STP 1175, Effects of Radiation on Materials: 16th International Symposium, 1993
- **关键词**: 肿胀、金属燃料、空腔、裂变气泡、临界半径、空位形核

## 摘要

本文提出了U-Pu-Zr金属燃料中α-U相的裂变气泡形核空化肿胀模型。在快堆中间温度区间（<662°C），α-U相的肿胀机制与非裂变材料中的空洞肿胀类似：裂变气泡在晶界/相界上形核并长大，当气泡半径超过由偏压驱动空位通量决定的临界半径后，气泡转变为空洞并以偏压驱动方式持续长大。

模型基于单空位和单间隙原子的速率理论，将晶界裂变气泡作为空洞形核核心，避免了复杂的缺陷相互作用计算。核心方程描述了空腔生长速率（Eq. 1），包含空位/间隙原子扩散系数、捕获效率和热发射项。临界半径（Eq. 8）由偏压驱动空位流入与热空位流出的平衡条件确定。

GRASS-SST和FASTGRASS计算表明，在673 K辐照温度下，U-19Pu-10Zr燃料中晶界气泡半径在约0.1 at.%燃耗时超过临界半径，标志着从气泡驱动生长向偏压驱动空洞生长的转变，这与实验观察到的肿胀和气体释放孕育期一致。肿胀峰值出现在约773 K。模型参数包括：空位形成能1.23 eV、迁移能0.74 eV、扩散预指数$2.0 \times 10^{-4}$ m²/s、表面能1.37 J/m²、复合半径$2 \times 10^{-10}$ m。

## Key Equations

### 空腔生长速率（Eq. 1）
$$
\frac{dr_c}{dt} = \frac{\Omega}{r_c} \left[ D_v (Z_v^c C_v - C_v^0(r_c)) - D_i Z_i^c C_i \right]
$$
- $r_c$: 空腔半径，$\Omega$: 原子体积，$D_v, D_i$: 空位/间隙原子扩散系数
- $Z_v^c, Z_i^c$: 空腔对空位/间隙原子的捕获效率
- $C_v, C_i$: 空位/间隙原子浓度，$C_v^0(r_c)$: 空腔附近的热空位浓度

### 热空位浓度（Eq. 2-3）
$$
C_v^0(r_c) = C_v^0 \exp\left(\frac{2\gamma}{r_c} - P_g\right)\frac{\Omega}{kT}
$$
$$
C_v^0 = \exp(-E_f / kT)
$$
- $\gamma$: 表面能，$P_g$: 气泡内气体压力，$E_f$: 空位形成能

### 缺陷平衡浓度（Eq. 6）
$$
C_v = \left(\frac{K}{4\pi r_{iv}(D_v + D_i)}\right)^{1/2}
$$
- $K$: Frenkel对产生速率，$r_{iv}$: 复合体积半径

### 临界半径（Eq. 8）
$$
r_c^{crit} = \frac{2\gamma \Omega}{kT \ln(Z_d^v / Z_d^i)}
$$
- $Z_d^v, Z_d^i$: 位错对空位/间隙原子的捕获效率比

## 参数汇总
- 空位形成能 $E_f = 1.23$ eV
- 空位迁移能 $E_m = 0.74$ eV
- 扩散预指数 $D_0 = 2.0 \times 10^{-4}$ m²/s
- 表面能 $\gamma = 1.37$ J/m²
- 原子体积 $\Omega = 4.09 \times 10^{-29}$ m³
- 复合半径 $r_{iv} = 2 \times 10^{-10}$ m
- 肿胀峰值温度 ~773 K
- 临界转变燃耗 ~0.1 at.%

## Related Work
- [[wiki/entities/CavitationalVoid|CavitationalVoid]] — this paper's core mechanism: fission gas bubble nucleated cavitational swelling
- [[wiki/entities/UPuZrFuel|UPuZrFuel]] — fuel system modeled in this work
- [[wiki/concepts/RateTheoryFramework|RateTheoryFramework]] — model based on single vacancy and interstitial rate theory
- [[wiki/summaries/2013_Yun_GRASSSST_UPuZr|2013_Yun_GRASSSST_UPuZr]] — applies GRASS-SST (successor to this framework) to U-Pu-Zr fuel
- [[wiki/summaries/2022_Yun_CavitationalVoidSwelling|2022_Yun_CavitationalVoidSwelling]] — modern update to cavitational void swelling modeling
- [[wiki/summaries/2022_Qian_CavitationalVoidSwellingU10Zr|2022_Qian_CavitationalVoidSwellingU10Zr]] — extends cavitational swelling model to U-10Zr
