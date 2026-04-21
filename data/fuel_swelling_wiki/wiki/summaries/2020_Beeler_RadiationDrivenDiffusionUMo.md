# 2020_Beeler_RadiationDrivenDiffusionUMo

## 基本信息
- **标题**: Radiation driven diffusion in γ U-Mo
- **作者**: Benjamin Beeler, Michael W.D. Cooper, Zhi-Gang Mei, Daniel Schwen, Yongfeng Zhang
- **机构**: NC State, INL, LANL, ANL, UW-Madison
- **来源**: Journal of Nuclear Materials, 2020
- **关键词**: 铀钼合金、分子动力学、扩散、研究堆、辐照、裂变气体

## 摘要

本文通过分子动力学（MD）模拟研究了U-Mo核燃料中U、Mo和Xe的辐照驱动扩散系数。针对U-Mo单芯块燃料在研究堆运行温度（150-350°C）下固有热扩散极为有限的问题，利用LAMMPS软件和Smirnova U-Mo-Xe EAM势函数，对80×80×80超胞（1,024,000原子）进行级联损伤模拟。

研究发现Xe的辐射驱动扩散系数显著高于U和Mo（约为2-3.5倍），这是因为Xe在级联热峰的局部熔化区域中扩散更快。温度对辐射驱动扩散的影响较小，在600 K范围内仅增加约2倍，可视为准非热过程。Mo含量升高会降低辐射驱动扩散系数，主要原因是Mo提高了合金熔点，减少了级联核心的局部熔化程度。

基于MSD与能量密度的线性关系，提出了包含固有扩散和辐射驱动扩散的总扩散系数表达式。U、Mo和Xe的固有-辐射扩散转变温度分别为600 K、650 K和800 K，表明在U-Mo燃料研究堆运行温度（400-600 K）范围内，辐射驱动扩散是主导机制。该数据可直接用于介观和连续尺度的燃料性能建模。

## Key Equations

### 辐射驱动扩散系数（Eq. 1）
$$
D_{rad} = \frac{0.05 \times \epsilon_B}{6} \times E_F \times \dot{F}
$$
- $0.05$: 弹性能量沉积份额（95%为电子能量损失）
- $\epsilon_B$: MSD对单位体积沉积能量的斜率 (m⁵/J)
- $E_F = 170$ MeV: 单次裂变事件碎片总动能
- $\dot{F}$: 体积裂变率 (fissions/m³·s)

### 简化辐照扩散系数（Eq. 2）
$$
D_{irr} = A \dot{F}
$$
- $A$: 综合系数，对U-10Mo在500 K：U: $1.97 \times 10^{-41}$, Mo: $2.01 \times 10^{-41}$, Xe: $5.07 \times 10^{-41}$

### 总扩散系数（Eq. 3-5）
$$
D_U = (1.28 \times 10^{-5}) \exp(-1.76/kT) + 1.97 \times 10^{-41} \times \dot{F}
$$
$$
D_{Mo} = (1.62 \times 10^{-5}) \exp(-1.97/kT) + 2.01 \times 10^{-41} \times \dot{F}
$$
$$
D_{Xe} = (1.28 \times 10^{-9}) \exp(-1.76/kT) + 5.07 \times 10^{-41} \times \dot{F}
$$
- 单位：m²/s（预指数），eV（激活能），m⁵·f⁻¹·s（辐射项）
- 裂变率假设：$\dot{F} = 5 \times 10^{20}$ f/m³·s

## 参数汇总
- 弹性能量沉积份额：5%
- Xe在U-Mo中辐射驱动扩散约为U/Mo的2-3.5倍
- 固有-辐射扩散转变温度：U 600K, Mo 650K, Xe 800K
- U-Mo热导率：23 W/m·K (500°C)
- 超胞规模：80×80×80 (1,024,000原子)
- PKA能量范围：10-24 keV
- 电子能量损失（70 MeV Xe碎片）：95%
