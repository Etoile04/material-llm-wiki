# A model for the effect of the progression of irradiation-induced recrystallization from initiation to completion on swelling of UO2 and U–10Mo nuclear fuels

## Metadata

- **作者**: J. Rest (Argonne National Laboratory)
- **年份**: 2005
- **期刊**: Journal of Nuclear Materials
- **卷/页**: 346, 226–232
- **DOI**: 10.1016/j.jnucmat.2005.06.012
- **关键词**: irradiation-induced recrystallization, fission gas swelling, UO2, U-10Mo, grain subdivision, burnup

## Physical Mechanisms（物理机制）

### 辐照诱发再结晶 (Irradiation-Induced Recrystallization)

辐照诱发再结晶是核燃料中普遍观察到的现象，发生在 UO2、U-xMo、U3O8 等多种燃料中。

**驱动力**：辐照产生的 interstitial loops（间隙原子环）不断积累，在材料中产生内应力，导致晶格位移形式的应变。当体积应变能超过创建新表面所需的能量时，触发再结晶。

**过程**：
1. **形核阶段**：再结晶在原始晶界处优先形核（preexisting grain boundaries）
2. **扩展阶段**：再结晶前沿从晶界向晶粒中心推进，形成宽度为 δ 的无缺陷环形区域（defect-free annulus）
3. **完成阶段**：最终消耗整个原始晶粒，产生亚微米级新晶粒

**关键特征**：
- 再结晶导致亚微米级晶粒，加速裂变气体肿胀
- 短扩散距离、增加的晶界面积/体积比、更高的晶间气泡生长速率三者协同
- 再结晶的起始 fission density 与温度基本无关（athermal），对裂变率依赖极弱

### 裂变气体肿胀 (Fission Gas Swelling)

肿胀由两部分组成：
1. **未再结晶区**：晶内气泡（intragranular bubbles）+ 晶界气泡（intergranular bubbles）
2. **再结晶区**：原有晶界气泡 + 新晶界气泡 + 三叉晶界节点气泡（triple point bubbles）

再结晶后肿胀加速的原因：
- 再结晶晶粒尺寸（~0.2–0.5 μm）远小于原始晶粒（~4–9 μm）
- 大量三叉晶界节点成为极高效的气泡形核点
- 大部分生成的裂变气体到达晶界

## Key Equations（关键方程式）

### 再结晶形核浓度（Eq. 1）

再结晶核心浓度 C_rlx 与位错密度 ρ_d 的关系：

$$C_{rlx} = \frac{9(f(m)\rho_d)^{7/2}}{8\pi^6(C_A C_q)^7 F_d^{5/2}} \frac{\phi_c}{\alpha_p} \frac{2k}{\sqrt{3\pi b_v B_0 b}}$$

### 再结晶起始 fission density（Eq. 4）

$$F_d^x = \left[\frac{\alpha_p \rho_d}{\phi_c}\right]^{4/5} \left[\frac{2k}{3b_v D_0 b}\right]^{1/5} \frac{[f(m)]^{6/5} \exp[4(\varepsilon_v/2 - \varepsilon_i)/15kT]}{\pi^{9/5}(C_A C_q)^{12/5}}$$

### 简化起始 fission density（Eq. 5）

- **UO2**: $F_d^x = 4 \times 10^{24} (\dot{f})^{2/15}$ (m⁻³)
- **U-10Mo**: $F_d^x = 6 \times 10^{24} (\dot{f})^{2/15}$ (m⁻³)

### 晶格位移（Eq. 6）

$$\frac{\Delta a(t)}{a_0} = \pi b_v n_l(t) d_l^2(t) / 12$$

### 无缺陷环形区域宽度（Eq. 9）

$$\delta = \frac{2c_s h}{E(\Delta a/a_0)^2}$$

### 再结晶体积分数（Eq. 24）— 核心结果

$$V_r = 1 - \left[1 - \frac{96 c_s B_2 (F_d - F_d^x)}{d_g C_A C_q \sqrt{f(m)/(2\pi)}}\right]^3$$

- V_r 近似与 fission density 成正比，与晶粒尺寸成反比
- V_r(t) 与燃料温度无关

### 近似解（Eq. 25）

$$V_r \approx \frac{288 c_s B_2 (F_d - F_d^x)}{d_g C_A C_q \sqrt{f(t)/(2\pi)}}, \quad F_d \ll F_d^{max}$$

### 肿胀计算（Eq. 39）— 总肿胀

$$\left(\frac{\Delta V}{V}\right)_T = (1 - V_r)\left(\frac{\Delta V}{V}\right)_g + V_r \left(\frac{\Delta V}{V}\right)_{gx}$$

### 再结晶区肿胀（Eq. 40）

$$\left(\frac{\Delta V}{V}\right)_{gx} = 4\pi R_{bx}^3 \left(\frac{C_b}{d_g} + \frac{C_{bx}}{d_{gx}} + \frac{1}{3d_{gx}^3}\right)$$

### 固态裂变产物肿胀

- **U-xMo**: $(\Delta V/V)_S = 0.014 \times BU$ (Eq. 42)
- **UO2**: 0.32%/10 GWd/tM

### 应变率（Eq. 15）

$$\dot{\varepsilon} = B_2 \dot{f} \sigma$$

### 缺陷前沿速度（Eq. 22）

$$v_{df} = \frac{48 c_s B_2}{C_A C_q} \sqrt{\frac{f(m)}{2\pi}} \dot{f}$$

## Parameters（参数数据）

### Table 1 — 计算所用参数

| 参数 | 值 | 参考文献 |
|------|------|------|
| b (gas atoms/fission) | 0.25 | Olander 1976 |
| n (grain-boundary diffusion enhancement) | 1.65 × 10⁻³ | Spino et al. |
| β₀ (resolution parameter) | 10⁻²³ m³ | Marlow & Kaznoff 1973 |
| D₀ (athermal diffusivity constant) | 1.2 × 10⁻³⁹ m⁵ | Matzke 1980 |
| r_g (gas-atom radius) | 0.216 nm | Olander 1976 |
| γ (surface tension) | 1 J/m² | Olander 1976 |
| b_v (van der Waals constant) | 8.5 × 10⁻²⁹ m³/atom | Olander 1976 |
| f_n (bubble nucleation factor) | 10² | Spino et al. |
| h_s (fitting parameter) | 0.6 | Spino et al. |
| B₂ (U-xMo) | 2 × 10⁻³⁴ m⁵/N | This work |
| B₂ (UO2) | 10⁻³⁴ m⁵/N | This work |
| d_gb (grain boundary width) | 2 × 10⁻⁹ m | Spino et al. |
| z (sites per gas-atom jump) | 4 | Spino et al. |

### 其他关键参数

- U-10Mo 再结晶起始：~45% burnup
- U-10Mo 再结晶完成：~70% burnup
- 再结晶晶粒尺寸 dgx：~0.2–0.5 μm（实验测量）
- B₂ 宏观估算（UO2 in-pile creep）：10⁻³¹ cm⁵/dyne
- U-10Mo 拟合值：2 × 10⁻²⁹ cm⁵/dyne

## Experimental Data（实验数据）

### U-10Mo 再结晶体积分数
- 40% burnup：再结晶开始
- 70% burnup：再结晶基本完成
- 与模型（Eq. 24, B₂ = 2×10⁻²⁹ cm⁵/dyne）吻合良好

### UO2 再结晶的晶粒尺寸依赖
- 数据来源：Nogita et al. (1997)
- 模型预测的 1/dg 依赖性与数据趋势一致
- 晶粒直径 10–70 μm 范围，再结晶体积分数 0.1–0.6

### U-xMo 肿胀行为（Fig. 3）
- 数据来源：Hofman, Finlay, Kim (RERTR 4&5, 2004)
- 模型在 dgx = 0.2 μm 和 dgx = 0.4 μm 两个值下与数据对比
- 肿胀从 ~15% 到 ~40%（对应 45–70 at% burnup）
- 模型成功捕捉跨越再结晶转变的肿胀趋势

### UO2 肿胀行为（Fig. 5）
- 数据来源：相对浸没密度测量（Spino et al.）
- dg = 7 μm, dgx = 0.2 μm
- B₂ = 10⁻²⁹ 和 2×10⁻²⁹ cm⁵/dyne 两个值
- burnup > 80 GWd/tM 时，B₂ 较小值更符合实验
- UO2 的 B₂ 约为 U-xMo 的一半

### 晶粒尺寸对肿胀的影响（Fig. 4）
- 比较了 dg = 4 μm 和 dg = 9 μm
- 考虑再结晶渐进过程 vs 同时再结晶的区别
- 渐进过程显著抑制肿胀（实线 vs 虚线）
- 原始晶粒越大，渐进效应越明显

## Key Findings（核心发现）

1. **统一理论框架**：UO2 和 U-10Mo 的再结晶起始、扩展和气泡肿胀可用同一理论描述，仅需调整材料属性参数
2. **再结晶体积分数**（Eq. 24）是本文的核心贡献：V_r 近似正比于 (Fd - Fdx)，反比于 dg，与温度无关
3. **再结晶渐进效应**：再结晶从晶界向晶粒中心逐步推进，而非瞬间完成。这一渐进过程显著抑制肿胀——与"瞬时全部再结晶"相比，肿胀率更低
4. **B₂ 参数差异**：UO2 的微观蠕变参数 B₂ 约为 U-xMo 的一半，反映了两种材料的力学性质差异
5. **三叉晶界节点**：再结晶产生的大量三叉晶界节点是极高效的气体陷阱，每个节点都形成气泡
6. **UO2 固态裂变产物肿胀**约为 U-xMo 的 3 倍（0.32%/10 GWd/tM vs 0.014×BU）

## Relationships to Other Work（与其他工作的关系）

### 前续工作
- **Rest (2004), J. Nucl. Mater. 326, 175** [Ref.1]：再结晶起始模型的理论基础，本文 Eq. 1-5 的修正版本来源
- **Rest (2003), J. Nucl. Mater. 321, 305** [Ref.2]：晶粒细分加速裂变气体肿胀的机制研究
- **Rest & Hofman (2000), J. Nucl. Mater. 277, 231** [Ref.4]：位错胞尺寸模型（Eq. 19）

### 实验数据来源
- **Nogita et al. (1997), J. Nucl. Mater. 248, 196** [Ref.7]：UO2 再结晶体积分数与晶粒尺寸关系
- **Hofman, Finlay, Kim (2004), RERTR 4&5** [Ref.10]：U-xMo 肿胀数据
- **Spino et al.** [Ref.8]：UO2 浸没密度数据、气泡参数

### 后续工作
- 作者在文末提到正在准备再结晶晶粒尺寸 dgx 的理论计算（submitted to J. Nucl. Mater., July 2005）
- 本模型为预测高 burnup 下 UO2 和 U-Mo 合金燃料的肿胀行为提供了分析工具

## Relationships

- [[wiki/entities/Recrystallization|Recrystallization]] — irradiation-induced recrystallization from initiation to completion is the central mechanism modeled
- [[wiki/concepts/SwellingMechanisms|SwellingMechanisms]] — recrystallization-enhanced fission gas swelling via grain subdivision is quantified
- [[wiki/entities/FuelAlloy|FuelAlloy]] — U-10Mo and UO2 fuels are the subject materials
- [[wiki/entities/FissionGasDiffusion|FissionGasDiffusion]] — triple-point bubble formation and intergranular gas bubble growth after recrystallization are key
- [[wiki/summaries/2008_Kim_IntergranularFGBubblesUMo|2008_Kim_IntergranularFGBubblesUMo]] — Kim (2008) provides experimental data on intergranular bubble evolution in U-Mo
- [[wiki/summaries/2011_Kim_FissionProductInducedSwellingUMo|2011_Kim_FissionProductInducedSwellingUMo]] — grain refinement threshold and its effect on swelling enhancement is further quantified
- [[wiki/summaries/2013_Kim_RecrystallizationFGBSwellingUMo|2013_Kim_RecrystallizationFGBSwellingUMo]] — extends recrystallization-swelling coupling in U-Mo fuel

### 相关模型
- **Olander (1976)**：核燃料基本物理参数、in-pile 蠕变数据
- **Wood & Kear (1983), J. Nucl. Mater. 118, 320** [Ref.9]：晶界气泡形核假设
- **Hanson & Kuhlmann-Wilsdorf (1986)** [Ref.5]：位错胞最低能量构型

---

*生成日期: 2026-04-19 | 知识提取自 PDF 全文*

## Related Work
- [[wiki/summaries/2008_Kim_IntergranularFGBubblesUMo|2008_Kim_IntergranularFGBubblesUMo]] — Kim (2008) 提供了 U-Mo 晶间气泡的实验数据，验证了本文再结晶-肿胀耦合预测
- [[wiki/summaries/2011_Kim_FissionProductInducedSwellingUMo|2011_Kim_FissionProductInducedSwellingUMo]] — Kim (2011) 在本文框架基础上建立了 U-Mo 肿胀的经验关联，量化了晶粒细化阈值
- [[wiki/summaries/2013_Kim_RecrystallizationFGBSwellingUMo|2013_Kim_RecrystallizationFGBSwellingUMo]] — 延伸了本文的再结晶-肿胀耦合模型在 U-Mo 燃料中的应用
- [[wiki/entities/Recrystallization|Recrystallization]] — 辐照诱发再结晶及其对肿胀的增强效应是本文的核心主题
- [[wiki/summaries/1985_Willard_SwellingPhaseReversionU10Mo|1985_Willard_SwellingPhaseReversionU10Mo]] — Willard 早期观察到 U-10Mo 的相变和 γ 稳定性问题，与本文再结晶物理相关
