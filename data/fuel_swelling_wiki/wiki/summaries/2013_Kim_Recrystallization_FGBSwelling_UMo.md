# 2013_Kim_Recrystallization_FGBSwelling_UMo

## 基本信息
- **标题**: Recrystallization and fission-gas-bubble swelling of U–Mo fuel
- **作者**: Yeon Soo Kim, G.L. Hofman, J.S. Cheon
- **机构**: Argonne National Laboratory; KAERI
- **来源**: Journal of Nuclear Materials, 2013
- **关键词**: U-Mo燃料、再结晶、裂变气泡肿胀、Avrami方程

## 摘要

本文建立了U-Mo合金燃料的再结晶动力学与裂变气泡（FGB）肿胀的半经验模型。高燃耗下U-Mo燃料发生辐照诱导再结晶，原始数微米晶粒细分为亚微米晶粒，大幅增加晶界面积，从而显著增强晶界FGB肿胀。

基于RERTR-1至RERTR-5辐照试验的20个样品SEM分析数据，再结晶动力学采用修正Avrami方程描述，以裂变密度替代时间作为驱动变量。模型参数包括：反应常数$K$（与Mo含量线性相关）、Avrami指数$n=2.6$、孕育裂变密度$F_0$（雾化粉1.67×10²¹ f/cm³，磨制粉1.38×10²¹ f/cm³）。磨制粉因冷加工缺陷较多，再结晶孕育期更短。

FGB肿胀模型将肿胀分为三个阶段：（1）再结晶前阶段——FGB仅在原始晶界形成，肿胀率$\Delta V/V_0 = 0.6 \times F$（%）；（2）再结晶阶段——肿胀率为两阶段的加权组合；（3）完全再结晶阶段——肿胀率最高，$\Delta V/V_0 = 2.2 \times F$（%）。累积FGB肿胀通过对裂变密度的积分获得，模型预测与实验数据一致性良好。该模型可预测Mo含量和制备工艺对FGB肿胀的影响，是对简单多项式肿胀模型的显著改进。

## Key Equations

### 修正Avrami方程（Eq. 1）
$$
V_{rx} = 1 - \exp\left[-K(F - F_0)^n\right]
$$
- $V_{rx}$: 再结晶体积分数，$K$: 反应常数，$F$: 裂变密度 (10²¹ f/cm³)
- $F_0$: 孕育裂变密度，$n$: Avrami指数 = 2.6

### 反应常数（Eq. 2）
$$
K = K_0 (1 - 0.1 \times x_{Mo})
$$
- $K_0 = 0.1$，$x_{Mo}$: Mo含量 (wt.%)

### 孕育裂变密度
- 雾化粉：$F_0 = 1.67 \times 10^{21}$ f/cm³
- 磨制粉：$F_0 = 1.38 \times 10^{21}$ f/cm³

### 再结晶前FGB肿胀率（Eq. 4）
$$
\left(\frac{\Delta V}{V_0}\right)_{g,0} = 0.6 \times F
$$
- $F$单位为 10²¹ f/cm³，肿胀率为百分比

### 完全再结晶FGB肿胀率（Eq. 5）
$$
\left(\frac{\Delta V}{V_0}\right)_{g,rx} = 2.2 \times F
$$

### 再结晶阶段FGB肿胀率（Eq. 7）
$$
\left(\frac{\Delta V}{V_0}\right)_g = \left(\frac{\Delta V}{V_0}\right)_{g,0} + V_{rx} \left[\left(\frac{\Delta V}{V_0}\right)_{g,rx} - \left(\frac{\Delta V}{V_0}\right)_{g,0}\right]
$$

### 累积FGB肿胀（Eq. 8-9）
$$
\frac{\Delta V}{V_0} = \int_0^F \left(\frac{\Delta V}{V_0}\right)_g dF
$$

### Avrami指数与体积再结晶模型比较（Eq. 12, 14）
$$
V_{rx} \approx \left(\frac{F - F_0}{F_{0.5} - F_0}\right)^{2.6}
$$
$$
V_{rx} \approx 1 - \exp\left(-0.1(F - F_0)^{2.6}\right)
$$

## 参数汇总
- Avrami指数 $n = 2.6$
- $K_0 = 0.1$
- 再结晶前肿胀率系数：0.6 %/(10²¹ f/cm³)
- 完全再结晶肿胀率系数：2.2 %/(10²¹ f/cm³)
- 再结晶完成裂变密度：~5×10²¹ f/cm³
- 完全再结晶FGB肿胀：~10.6-12.5%
- 晶粒尺寸：原始3-15 μm → 再结晶后 <1 μm
