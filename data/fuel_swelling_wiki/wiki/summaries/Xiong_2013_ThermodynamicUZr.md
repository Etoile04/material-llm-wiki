# Xiong 2013 - U-Zr热力学建模

## 基本信息
- **标题**: Thermodynamic modeling of the U–Zr system – A revisit
- **作者**: Wei Xiong, Wei Xie, Chao Shen, Dane Morgan
- **机构**: University of Wisconsin – Madison
- **期刊**: Journal of Nuclear Materials 443 (2013) 331–341
- **关键词**: CALPHAD, U-Zr, 热力学, 相图, 第一性原理

## 中文摘要

本文利用CALPHAD方法结合第一性原理计算，重新评估了U-Zr二元系统的热力学描述。模型对热容、活度、混合焓等热力学性质给出了良好的预测。模型预测的bcc和δ相形成焓与DFT+U第一性原理计算结果吻合良好。

U-Zr系统包含六个相：液相、γ(U,Zr)（bcc）、α(U)（正交）、β(U)（四方）、δ（AlB₂型六方结构）和α(Zr)（hcp）。液相和各无序固溶体相采用替代溶液模型描述，过剩Gibbs自由能用Redlich-Kister多项式表达。δ相采用亚点阵模型(Zr)₁(U,Zr)₂描述，其中A亚点阵优先被Zr占据，B亚点阵由U和Zr随机占据。

研究发现δ相的热力学描述受纯Zr在δ和α-hcp结构之间的能量差影响显著。本文评估的ΔE(Zr)=527.5 J/mol，远小于传统CALPHAD常用的5000 J/mol。δ相在66.7 at.% Zr处的形成焓预测为-1627.5 J/mol（298K），与DFT+U计算值(-579 J/mol)在实验不确定度(±10.1 kJ/mol)范围内一致。

本文计算了四个不变反应温度：γ→γ'+β(U)在966K，β(U)→α(U)+γ在935K，γ→α(U)+δ在890K，γ→δ+α(Zr)在879K。bcc固溶体的miscibility gap在960-1020K范围内形成。

与以往评估相比，本文对δ相同质异能范围、液相过剩熵和bcc混合焓的描述均有改进，展示了第一性原理结合CALPHAD方法在锕系合金系统热力学评估中的应用价值。

## Key Equations

1. **替代溶液Gibbs自由能**:
$$G_m^{\phi} = x_U G_U^{\phi} + x_{Zr} G_{Zr}^{\phi} + RT(x_U \ln x_U + x_{Zr} \ln x_{Zr}) + G_m^{ex,\phi}$$

2. **过剩Gibbs自由能 (Redlich-Kister)**:
$$G_m^{ex,\phi} = x_U x_{Zr} \sum_{i=0}^{n} {}^{i}L_{UZr}^{\phi}(x_U - x_{Zr})^i$$

3. **δ相Gibbs自由能**:
$$G_m^{\delta} = y_{U}^{II} G_{Zr:U}^{\delta} + y_{Zr}^{II} G_{Zr:Zr}^{\delta} + \frac{2}{3}RT(y_{U}^{II}\ln y_{U}^{II} + y_{Zr}^{II}\ln y_{Zr}^{II}) + y_{U}^{II}y_{Zr}^{II} L_{Zr:U,Zr}^{\delta}$$

4. **形成焓计算**:
$$E_{form}^{U_xZr_{1-x}} = E^0_{U_xZr_{1-x}} - xE^0_{\alpha(U)} - (1-x)E^0_{\alpha(Zr)}$$

## Related Work
- [[wiki/concepts/IrradiationDrivenVsIntrinsicDiffusion|IrradiationDrivenVsIntrinsicDiffusion]] — U-Zr体系热力学与扩散数据
- [[wiki/summaries/Lu_2018_CALPHAD_UFuels|Lu_2018_CALPHAD_UFuels]] — 铀燃料CALPHAD评估
- [[wiki/summaries/Turchi_2018_ThermodynamicDiffusion|Turchi_2018_ThermodynamicDiffusion]] — Nb-Ti-U-Zr合金热力学与扩散
- [[wiki/summaries/Zhou_2023_ThermoDiffDatabaseU|Zhou_2023_ThermoDiffDatabaseU]] — 铀基合金热力学与扩散数据库的扩展
- [[wiki/summaries/2020_Hirschhorn_UZr_DiffusionCouple_PF|2020_Hirschhorn_UZr_DiffusionCouple_PF]] — U-Zr扩散偶的相场模拟
- [[wiki/summaries/2025_Williams_UZr_PhaseDiagram|2025_Williams_UZr_PhaseDiagram]] — U-Zr相图评估
