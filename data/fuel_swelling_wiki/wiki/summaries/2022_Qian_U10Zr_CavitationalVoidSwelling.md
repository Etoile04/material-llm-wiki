# U-10Zr金属燃料低温区空化空洞肿胀行为研究

## 基本信息
- **作者**: Zhengyu Qian, Xin Xie, Yingjie Fu, Di Yun, Wenbo Liu 等
- **机构**: 西安交通大学核科学与技术学院, 中国工程物理研究院
- **年份**: 2022
- **期刊**: Journal of Nuclear Materials, 564, 153665
- **DOI**: 10.1016/j.jnucmat.2022.153665
- **材料**: U-10Zr金属燃料
- **关键词**: 铀锆燃料、热-力学分析、燃料肿胀、速率理论、空化空洞肿胀

## 摘要

本文针对U-10Zr金属燃料在低温区（400-600K）的肿胀行为开展了深入研究。基于中国工程物理研究院提供的堆内辐照实验数据（CMRR研究堆，最大燃耗~0.7 at.%），通过金相分析和有限元模拟确定了辐照燃料中的球形结构为低气压空腔（cavities）而非平衡气泡。

**实验结果**：U-10Zr燃料在低温区（450-560K）产生了可观的体积肿胀（~12% at 0.55 at.% burnup）。金相观察到大量球形空腔，平均直径约3 μm（1328个测量，均值2.98 μm，标准差0.988 μm），数密度约8×10⁹个/cm³。

**有限元分析**：通过COMSOL Multiphysics建立轴对称热-力学模型，计算得到辐照燃料中的静水应力约60-130 MPa（压应力），远高于基于气体原子密度估算的空腔内压（~2.3 MPa），排除了平衡气泡机制的可能性。

**速率理论模型**：基于Rest发展的空化空洞肿胀机制建立了改进的速率理论代码。关键改进在于采用了更低的空位迁移能——将空位扩散激活能从传统值大幅降低至**0.34 eV**（基于DFT计算，与文献一致），使低温区空位扩散系数比Rest模型高出3-4个数量级。改进后的模型能够同时很好地描述低温区和高温区（α-U相区）的燃料肿胀行为。

**参数敏感性分析**：验证了空位迁移能对计算结果的高度敏感性，0.34 eV是最优值。高温区（800-1000K）EBR-II燃料X423实验数据的验证表明，γ-U相区采用气泡长大动力学、α-U相区采用空化空洞肿胀动力学的组合模型能够很好地捕捉裂变气体释放和肿胀行为。

**对比验证**：尝试用气泡长大动力学模拟低温肿胀，即使将裂变气体扩散系数前置因子人为提高6个数量级，也只能得到~1.2%的肿胀（含固体裂变产物），远低于实验值~12%，证明低温区肿胀的主导机制是空化空洞肿胀而非气泡长大。

## Key Equations

### 1. 空位扩散系数
$$D_v = D_{v0} \exp\left(-\frac{E_m^v}{k_BT}\right)$$
- $D_{v0} = 1.0 \times 10^{-7}$ cm²/s；$E_m^v = 0.34$ eV

### 2. 间隙原子扩散系数
$$D_i = D_{i0} \exp\left(-\frac{E_m^i}{k_BT}\right)$$
- $D_{i0} = 1.0 \times 10^{-4}$ cm²/s；$E_m^i = 0.19$ eV

### 3. 裂变气体原子扩散系数
$$D_{fg} = D_{fg0} \exp\left(-\frac{E_m^{fg}}{k_BT}\right)$$
- $D_{fg0} = 1.2 \times 10^{-3}$ cm²/s；$E_m^{fg} = 1.16$ eV

### 4. U-10Zr热导率
$$k = (1-P)^{1.5} k_0, \quad k_0 = 11.7 + 1.33 \times 10^{-2}T + 9.38 \times 10^{-6}T^2$$
- P: 孔隙率；T: 温度(K)

### 5. U-10Zr弹性模量
$$E = 56 - 0.1158(T - 890) \text{ GPa}$$

### 6. 理想气体定律估算空腔内压
$$P_{cavity} = \frac{n_{gas} k_B T}{V_{cavity}} \approx 2.3\text{–}3 \text{ MPa}$$

### 7. 空穴生长速率（简化形式）
$$\frac{dr}{dt} \propto \frac{D_v C_v - D_i C_i}{r}$$

### 8. 临界空穴半径
$$r_c = \frac{2\gamma}{p_{gas} + \sigma_h}$$
其中 $\gamma$ 为表面能，$p_{gas}$ 为内部气体压力，$\sigma_h$ 为静水应力。

## 关键实验数据

| 参数 | 值 | 备注 |
|------|-----|------|
| 空穴平均直径 | ~3 μm | 金相测量（1328个空穴统计，均值2.98±0.988 μm） |
| 空穴数密度 | ~8×10⁹ cm⁻³ | 金相测量 |
| 静水应力 | 60–130 MPa（压） | COMSOL 有限元分析 |
| 体积肿胀 | ~12% @ 0.55 at.% | 低温辐照实验 |
| α/γ 相界温度 | 903 K | 高温区建模 |
| α相区体积分数 | 72.2% | 本文 |

## 关键模型参数

| 参数 | 值 | 来源 |
|------|-----|------|
| 空位形成能 $E_f^v$ | 1.77 eV | 本文DFT计算 |
| 空位迁移能 $E_m^v$ | 0.34 eV | 文献[20] DFT |
| 间隙原子迁移能 $E_m^i$ | 0.19 eV | 文献[20] DFT |
| 裂变气体迁移能 $E_m^{fg}$ | 1.16 eV | 文献[39] |
| 位错密度 | 7×10⁹ cm⁻² | 文献[12] |
| 气泡形核因子 | 1×10⁻⁵ | 文献[12] |
| 晶粒尺寸 | 1×10⁻³ cm | 本文TEM估算 |
| 相变温度 | 903K | 本文 |
| α相区体积分数 | 72.2% | 本文 |

## Related Work
- [[wiki/summaries/1993_Rest_CavitationalSwellingAlphaUPuZr|1993_Rest_CavitationalSwellingAlphaUPuZr]] — Rest空穴型空洞肿胀基础模型，本文建模基础
- [[wiki/summaries/1992_Rest_CavitationalSwellingAlphaUPuZr|1992_Rest_CavitationalSwellingAlphaUPuZr]] — Rest 1992 ASTM 会议论文，空腔肿胀理论雏形
- [[wiki/summaries/1993_Rest_VoidSwellingAlphaU|1993_Rest_VoidSwellingAlphaU]] — Rest α-U空洞肿胀模型，本文高温区验证数据参考
- [[wiki/summaries/2022_Yun_CavitationalVoidSwelling|2022_Yun_CavitationalVoidSwelling]] — 同期空穴型空洞肿胀研究（Yun组），方法互补
- [[wiki/summaries/2023_Development_formulation_physics_based_metallic_fuel|2023_Development_formulation_physics_based_metallic_fuel]] — BISON金属燃料模型，本文低温肿胀机制为BISON模型改进提供参考
- [[wiki/entities/CavitationalVoid|CavitationalVoid]] — 本文核心机制：空穴型空洞肿胀
- [[wiki/concepts/RateTheoryFramework|RateTheoryFramework]] — 本文使用的速率理论建模方法
