# Radiation Driven Diffusion in γ U-Mo

## 元数据

| 字段 | 内容 |
|------|------|
| **标题** | Radiation driven diffusion in γ U-Mo |
| **作者** | Benjamin Beeler, Michael W.D. Cooper, Zhi-Gang Mei, Daniel Schwen, Yongfeng Zhang |
| **期刊** | Journal of Nuclear Materials |
| **年份** | 2020 (published online 2 Oct 2020) |
| **DOI** | 10.1016/j.jnucmat.2020.152564 |

## 中文摘要

本文利用分子动力学（MD）模拟研究了γ相U-Mo合金中U、Mo和Xe在辐照条件下的扩散行为。U-Mo单体燃料是研究堆低浓化（LEU）转换的候选燃料，其运行温度较低（150–350 °C），在此温度范围内本征热扩散极为有限。因此，辐照驱动扩散（radiation driven diffusion, D₃）成为决定裂变气体肿胀速率和微观组织演化的关键因素。

作者采用Smirnova U-Mo-Xe EAM势函数，构建了102.4万原子的BCC超胞，对U-4Mo、U-7Mo、U-10Mo和U-15Mo（wt%）四种成分在100–700 K温度范围内进行了级联碰撞模拟。PKA能量范围为10–24 keV，每种条件进行40次独立模拟以获得统计显著的均方位移（msd）数据。通过MyTRIM程序确定电子能量损失份额，得出裂变事件中仅约5%的能量以弹道方式沉积。

主要发现：(1) Xe的辐照驱动扩散系数约为U和Mo的2.5倍，这与UO₂中Xe的行为截然不同；(2) 辐照驱动扩散可视为近似无热（athermal）过程，温度从100 K升至700 K仅使扩散增加约1.5–2倍；(3) Mo含量越低，辐照驱动扩散越强，这与低Mo合金熔点较低、级联核心更易发生局部熔化有关；(4) 在U-Mo研究堆运行温度范围（400–600 K）内，辐照驱动扩散远大于本征扩散，是主导扩散机制。论文最终给出了包含本征扩散和辐照驱动扩散的总扩散系数公式，可直接用于介观和连续介质燃料性能模拟。

## Key Parameters

| 参数名 | 值 | 单位 | 条件/备注 |
|--------|-----|------|-----------|
| 超胞尺寸 | 80×80×80 (1,024,000 atoms) | BCC unit cells | U-Mo合金 |
| Xe替代浓度 | ~1% (同时测试0.5%, 0.1%) | 原子分数 | 替代位，随机分布 |
| PKA能量范围 | 10–24 (步长2) | keV | U原子作为PKA |
| 每条件独立模拟数 | 40 | — | 不同随机PKA方向 |
| 级联模拟总时长 | 124.5 | ps | 分四段变时间步长 |
| NPT平衡时间 | 50 | ps | Langevin恒温器，阻尼0.01 ps |
| 裂变碎片总动能 | 170 | MeV | 单次裂变事件 |
| 弹道能量沉积份额 | 5% | — | U-Mo中，基于MyTRIM计算 |
| U-Mo热导率 | 23 | W/m·K | 500 °C |
| 裂变速率 | 5×10²⁰ | fiss/m³·s | 参考值 |
| ε_B (U, U-10Mo) | 1.39×10⁻⁴¹ | m⁵/eV·s | 500 K，Eq.(1)斜率 |
| ε_B (Mo, U-10Mo) | 1.42×10⁻⁴¹ | m⁵/eV·s | 500 K |
| ε_B (Xe, U-10Mo) | 3.58×10⁻⁴¹ | m⁵/eV·s | 500 K |
| U本征扩散指前因子 | 1.28×10⁻⁵ | m²/s | 拟合Huang 2013高温数据 |
| U本征扩散激活能 | 1.76 | eV | 拟合Huang 2013高温数据 |
| Mo本征扩散指前因子 | 1.62×10⁻⁵ | m²/s | 拟合Huang 2013高温数据 |
| Mo本征扩散激活能 | 1.97 | eV | 拟合Huang 2013高温数据 |
| Xe本征扩散指前因子 | 1.28×10⁻⁹ | m²/s | 假设比U低4个量级 |
| Xe本征扩散激活能 | 1.76 | eV | 假设与U相同 |
| A系数 (U, U-10Mo, 500K) | 1.97×10⁻⁴¹ | m⁵/fiss | D_irr = A·Ḟ |
| A系数 (Mo, U-10Mo, 500K) | 2.01×10⁻⁴¹ | m⁵/fiss | — |
| A系数 (Xe, U-10Mo, 500K) | 5.07×10⁻⁴¹ | m⁵/fiss | — |
| 本征→辐照扩散转变温度(U) | ~600 | K | — |
| 本征→辐照扩散转变温度(Mo) | ~650 | K | — |
| 本征→辐照扩散转变温度(Xe) | ~800 | K | — |
| U-15Mo熔点(势函数预测) | ~1600 | K | 二维固液界面演化验证 |
| U-4Mo熔点(势函数预测) | ~1500 | K | 二维固液界面演化验证 |
| ZBL样条截止距离 | 1–2 | Å | 短程修正 |

## Key Equations

### 1. 辐照驱动扩散系数

$$D_{\text{rad}} = \frac{0.05 \times \epsilon_B}{6} \times E_F \times \dot{F}$$

- $D_{\text{rad}}$: 辐照驱动扩散系数 [m²/s]
- $0.05$: U-Mo中弹道能量沉积份额（无量纲）
- $\epsilon_B$: 均方位移随能量密度变化的斜率 [m⁵/(eV·s)]
- $E_F = 170$ MeV: 单次裂变事件裂变碎片总动能
- $\dot{F}$: 裂变速率 [fiss/(m³·s)]

### 2. 简化辐照扩散系数

$$D_{\text{irr}} = A \cdot \dot{F}$$

- $D_{\text{irr}}$: 辐照扩散贡献 [m²/s]
- $A$: 物种和成分相关的系数 [m⁵/fiss]，由 $\epsilon_B$ 和弹道份额确定
- $\dot{F}$: 裂变速率 [fiss/(m³·s)]

### 3. 铀总扩散系数（本征 + 辐照驱动）

$$D_U = (1.28 \times 10^{-5}) \times \exp(-1.76 / kT) + 1.97 \times 10^{-41} \times \dot{F}$$

- 第一项: 本征扩散 $D_1$（Arrhenius形式），指前因子单位 m²/s，激活能单位 eV
- 第二项: 辐照驱动扩散 $D_3$
- $k$: 玻尔兹曼常数，$T$: 温度 [K]

### 4. 钼总扩散系数

$$D_{Mo} = (1.62 \times 10^{-5}) \times \exp(-1.97 / kT) + 2.01 \times 10^{-41} \times \dot{F}$$

- 物理含义同上，Mo的激活能（1.97 eV）高于U（1.76 eV）

### 5. 氙总扩散系数

$$D_{Xe} = (1.28 \times 10^{-9}) \times \exp(-1.76 / kT) + 5.07 \times 10^{-41} \times \dot{F}$$

- 本征Xe扩散指前因子假设比U低4个量级，激活能与U相同
- 辐照驱动项系数最大，反映Xe在弹道混合中迁移更快

## Related Work

- [[wiki/summaries/2020_Beeler_ImprovedEOSXeBubbleUMo|2020_Beeler_ImprovedEOSXeBubbleUMo]] — 同一作者同期工作，提供U-Mo中Xe气泡状态方程，与本扩散系数配合用于肿胀模拟
- [[wiki/summaries/2016_Hu_GasBubbleSuperlatticeFormationPF|2016_Hu_GasBubbleSuperlatticeFormationPF]] — 介尺度相场模型研究U-Mo中气泡超晶格形成，需扩散参数作为输入
- [[wiki/summaries/2018_Liang_3DPhaseFieldIntragranularBubbleUMo|2018_Liang_3DPhaseFieldIntragranularBubbleUMo]] — 三维相场模拟U-Mo晶内气泡演化，直接受益于本扩散数据
- [[wiki/entities/FissionGasDiffusion|FissionGasDiffusion]] — 裂变气体扩散概念框架，本文将 D₃ 机制从 UO₂ 推广至金属燃料
- [[wiki/summaries/2020_Beeler_ImprovedEOSXeBubbleUMo|2013_Huang_Interdiffusion_IntrinsicDiffusion_UMo]] — Huang 2013 高温互扩散实验数据，本文的本征扩散 Arrhenius 参数来源于此
- [[wiki/summaries/2006_Rest_UMoFuelsHandbook|2006_Rest_UMoFuelsHandbook]] — U-Mo燃料手册，提供热导率等物性参考数据
