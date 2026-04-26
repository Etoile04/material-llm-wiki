# Wu et al. (2025) - T91 钢在 LBE 中双层氧化与流动腐蚀的格子玻尔兹曼相场模型

## Metadata
- **期刊**: Corrosion Science, 256 (2025) 113132
- **作者**: Jinyi Wu, Dan Sun, Zhenhua Chai, Dongke Sun
- **机构**: 东南大学; 中国核动力研究设计院; 华中科技大学
- **DOI**: 10.1016/j.corsci.2025.113132
- **关键词**: Phase-field, LBM, T91, Duplex oxide, LBE
- **材料**: T91 铁素体-马氏体钢 (Fe 90, Cr 9, Mo 1 wt.%)
- **工况**: T = 400-600°C, cO = 1×10-7-饱和 wt.%, vLBE = 0-2 m/s

## 模型方法

本文发展了耦合格子玻尔兹曼方法 (LBM) 的相场模型,模拟 T91 钢在氧控流动铅铋共晶 (LBE) 中的双层氧化过程。模型引入两个序参量:外层序参量 φ 描述 magnetite (Fe3O4)/LBE 界面演化,内层序参量 ξ 描述 Fe-Cr spinel/基体界面演化。通过定义无量纲过化学势 UO0 和 UFe0,将温度和氧浓度的影响纳入相变驱动力。LBM 用于离散求解相场方程和 Fe/O 化学势扩散方程,采用 D2Q9 格子模型。通过引入标度去除势 Rφ 量化 LBE 流动对外层磁铁矿的溶解/冲蚀效应,并拟合得到 Rφ 的半经验表达式。

模型使用 11 组实验工况(涵盖 COLIMESTA、CORRIDA、KYLIN II 等装置,T = 450-550°C,静态及流动条件)进行验证,结果表明模型在预测内外氧化层厚度方面优于现有的 Martinelli 模型和 Feng 等的模拟结果。

## 主要发现

1. 氧化层厚度遵循抛物线生长定律,与 Wagner 理论一致
2. 温度是控制双层氧化生长的主导因素--升高温度虽降低 UO0,但显著增大扩散系数,整体加速氧化
3. 氧浓度主要影响内层 spinel 生长;外层 magnetite 对氧浓度不敏感,但对流动冲蚀敏感
4. cO ≈ 1×10-6 wt.% 可平衡保护性氧化层形成与流动条件下的稳定性
5. 低氧浓度 (10-7 wt.%) + 高流速 (2 m/s) 下外层完全去除 (Rφ = 1.0)
6. 五年长期模拟表明 550°C 下内层 spinel 可达 ~99 μm

## Key Equations

### 广义相场演化
$$\tau_0 \frac{\partial \Psi}{\partial t} = -\frac{\delta \mathcal{F}}{\delta \Psi}, \quad \Psi = \phi, \xi \tag{1}$$

### 系统自由能(三部分)
$$\mathcal{F} = \int \left[ \frac{1}{2}f(\Psi) + \frac{1}{2}W^2(\nabla\Psi)^2 + \lambda g(\Psi) U^* \right] dV \tag{2}$$
其中 f(Ψ) 为双势阱函数,W 为界面厚度,λ=3.19 为耦合系数,g(Ψ) 为插值函数,U* 为无量纲化学势。

### 外层/内层序参量方程
$$\tau_0 \frac{\partial \phi}{\partial t} = W_0^2 \nabla^2 \phi + \phi(1-\phi^2) + \lambda(1-\phi^2)^2 (1-R_\phi) U_\phi \tag{3a}$$
$$\tau_0 \frac{\partial \xi}{\partial t} = W_0^2 \nabla^2 \xi + \xi(1-\xi^2) + \lambda(1-\xi^2)^2 U_\xi \tag{3b}$$
Rφ 为标度去除势 (0=静态, 1=外层完全去除)。

## Related Work
- [[wiki/entities/HT9Cladding|HT9Cladding]] — T91为铁素体-马氏体包壳钢，与HT9同属FM钢
- [[wiki/summaries/2025_Wu_LBM_PhaseField_DuplexOxide_T91|2025_Wu_LBM_PhaseField_DuplexOxide_T91]] — 耦合格子玻尔兹曼的相场模型
- [[wiki/summaries/Li_2017_PhaseFieldReview|Li_2017_PhaseFieldReview]] — 相场方法综述，涵盖相场建模方法论
- [[wiki/summaries/2016_Carmack_FCCI_MFF3_Metallography|2016_Carmack_FCCI_MFF3_Metallography]] — 包壳与燃料化学相互作用相关
- [[wiki/concepts/FuelCladdingChemicalInteraction|FuelCladdingChemicalInteraction]] — 氧化层生长与燃料-包壳化学行为相关

### Fe/O 无量纲化学势扩散方程
$$\frac{\partial U_{Fe}}{\partial t} = \nabla \cdot M_{Fe}(\phi', \xi') \nabla U_{Fe} - \frac{\partial \xi}{\partial t} U_{Fe} \tag{4a}$$
$$\frac{\partial U_O}{\partial t} = \nabla \cdot M_O(\phi', \xi') \nabla U_O - \frac{\partial \phi}{\partial t} U_O \tag{4b}$$

### 扩散迁移率
$$M_{Fe}(\phi', \xi') = U_{Fe}^0 \left[ D_{Fe}^{mag} \frac{1+\phi'}{2} + D_{Fe}^{sp} \frac{1+\xi'}{2} \right] \tag{5a}$$
$$M_O(\phi', \xi') = U_O^0 \left[ D_O^{mag} \frac{1+\phi'}{2} + D_O^{sp} \frac{1+\xi'}{2} \right] \tag{5b}$$

### LBE 氧浓度控制窗口
$$\lg c_{O}^{LBE,min} = 0.7725 - \frac{7171}{T} \tag{6a}$$
$$\lg c_{O}^{LBE,max} = 2.25 - \frac{4125}{T} \tag{6b}$$

### 氧过化学势
$$U_{O0} = \frac{\lg c_O^* - 0.7725 + 7171/T}{1.4775 + 3046/T} \tag{7}$$

### 铁过化学势
$$U_{Fe0} = \frac{12500\left[(1-X_{Fe}^*)^2 - (1-X_{Fe}^{min})^2\right] + 8.314T \ln(X_{Fe}^*/X_{Fe}^{min})}{-12500(1-X_{Fe}^{min})^2 + 8.314T \ln(1/X_{Fe}^{min})} \tag{8}$$

### LBM 离散方程
$$g_i(\mathbf{x}+\mathbf{e}_i \delta x, t+\delta t) = g_i(\mathbf{x},t) - \frac{1}{\tau_\Psi}\left[g_i(\mathbf{x},t) - g_i^{eq}(\mathbf{x},t)\right] + w_i Q_\Psi(\mathbf{x},t) \frac{\delta t}{\tau_0} \tag{9}$$
$$g_i^{eq}(\mathbf{x},t) = w_i \Psi(\mathbf{x},t) \tag{10}$$
$$\tau_\Psi(\mathbf{x},t) = \frac{W_0^2}{\tau_0 c_s^2 \delta t} + \frac{1}{2} \tag{11}$$
$$Q_\Psi \text{ 含 } \phi, \xi \text{ 的源项} \tag{12}$$
$$h_i(\mathbf{x}+\mathbf{e}_i \delta x, t+\delta t) = h_i(\mathbf{x},t) - \frac{1}{\tau_U}\left[h_i(\mathbf{x},t) - h_i^{eq}(\mathbf{x},t)\right] + \frac{1}{\tau_U} Q_i(\mathbf{x},t)\delta t \tag{13}$$
$$\tau_U = \frac{D_{max}}{\delta x^2/\delta t} + \frac{1}{2}, \quad h_i^{eq} \text{ 含迁移率 } \bar{M} \tag{14}$$
$$Q_i \text{ 为扩散源项} \tag{15}$$

### 标度去除势半经验公式
$$R_\phi = \min\left( 72.558 \exp\left(-\frac{11568}{T}\right) \left[-\lg(c_O)\right]^{5.699} v_{LBE}^{0.875}, \; 1.0 \right) \tag{17}$$
