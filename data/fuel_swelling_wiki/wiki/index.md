# 索引 — 金属燃料辐照肿胀（Metal Fuel Irradiation Swelling）

> 金属核燃料（U-Mo, U-Zr, U-Pu-Zr）辐照诱发肿胀的物理机制、建模方法和实验数据。

## 🔖 导航
- [[#物理概念]] · [[#知识实体]] · [[#文献摘要]] · [[#开放问题]]

## 物理概念（Concepts）

### 建模框架
- [[wiki/concepts/RateTheoryFramework|速率理论框架]] — 速率理论模型的数学框架
- [[wiki/concepts/SwellingModelComparison|肿胀模型对比]] — 各类肿胀模型的系统对比

### 物理机制
- [[wiki/concepts/SwellingMechanisms|肿胀机制概述]] — 所有肿胀机制的总览

## 知识实体（Entities）

### 物理现象
- [[wiki/entities/CavitationalVoid|空穴型空洞]] — 裂变气体形核驱动的空洞形成
- [[wiki/entities/GasBubbleSuperlattice|气泡超晶格]] — 辐照燃料中的有序气泡排列
- [[wiki/entities/Recrystallization|再结晶]] — 辐照诱发晶粒重构与肿胀转变
- [[wiki/entities/FissionGasDiffusion|裂变气体扩散]] — Xe/Kr 在燃料基体中的输运

### 材料体系
- [[wiki/entities/FuelAlloy|燃料合金]] — U-Mo、U-Zr、U-Pu-Zr 合金体系与相行为

### 计算方法
- [[wiki/entities/PhaseFieldModeling|相场模拟]] — 气泡演化的相场模拟方法
- [[wiki/entities/RateTheory|速率理论]] — 均场缺陷/气体演化框架

## 文献摘要（Summaries，按年代排序）

### 1970-1990年代 — 基础理论
- 1979 — [[wiki/summaries/1979_Ronchi_FissionGasSwellingMX_Fuels|Ronchi 1979]] — MX 型燃料裂变气体肿胀
- 1985 — [[wiki/summaries/1985_Willard_SwellingPhaseReversionU10Mo|Willard 1985]] — U-10Mo 辐照肿胀与相回转
- 1990 — [[wiki/summaries/1990_Hofman_SwellingBehaviorUPuZr|Hofman 1990]] — U-Pu-Zr 肿胀行为
- 1992 — [[wiki/summaries/1992_Rest_CavitationalSwellingAlphaUPuZr|Rest 1992]] — α-U-Pu-Zr 空穴型空洞肿胀模型
- 1993 — [[wiki/summaries/1993_Rest_VoidSwellingAlphaU|Rest 1993]] — α-U 空洞肿胀

### 2000年代 — 模型发展
- 2001 — [[wiki/summaries/2001_Rest_GRSIS_FissionGasMetallic|Rest 2001]] — 金属燃料 GRSIS 模型
- 2005 — [[wiki/summaries/2005_Rest_RecrystallizationSwellingUO2UMo|Rest 2005]] — 再结晶肿胀模型
- 2008 — [[wiki/summaries/2008_Kim_IntergranularFGBubblesUMo|Kim 2008]] — 晶界裂变气体气泡
- 2008 — [[wiki/summaries/2008_Surh_VoidNucleationGrowthCoalescence|Surh 2008]] — 空洞形核、生长与聚合
- 2009 — [[wiki/summaries/2009_Rokkam_PhaseFieldVoidNucleationGrowth|Rokkam 2009]] — 空洞相场模拟

### 2010年代 — 计算方法进展
- 2011 — [[wiki/summaries/2011_Kim_FissionProductInducedSwellingUMo|Kim 2011]] — 裂变产物诱发肿胀
- 2011 — [[wiki/summaries/2011_Millett_PhaseFieldGasBubbleKinetics|Millett 2011]] — 气泡动力学相场模拟
- 2013 — [[wiki/summaries/2013_Karahan_FEAST_METAL_FuelSwelling|Karahan 2013]] — FEAST 金属燃料模型
- 2013 — [[wiki/summaries/2013_Kim_FissionInducedSwellingCreepUMo|Kim 2013]] — 裂变诱发肿胀与蠕变
- 2013 — [[wiki/summaries/2013_Kim_RecrystallizationFGBSwellingUMo|Kim 2013b]] — 再结晶与裂变气体气泡肿胀
- 2015 — [[wiki/summaries/2015_Cui_MechanisticGaseousSwellingUMo|Cui 2015]] — 机制性气态肿胀模型
- 2015 — [[wiki/summaries/2015_Gan_ThermalStabilityGasBubbleSuperlattice|Gan 2015]] — 气泡超晶格热稳定性
- 2015 — [[wiki/summaries/2015_Miller_TEMGasBubbleSuperlatticeU7Mo|Miller 2015]] — U-7Mo 超晶格 TEM 表征
- 2016 — [[wiki/summaries/2016_Hu_GasBubbleSuperlatticeFormationPF|Hu 2016a]] — 超晶格形成相场模拟
- 2016 — [[wiki/summaries/2016_Hu_GrainMorphologyGasBubbleUMo|Hu 2016b]] — 晶粒形态与气泡肿胀
- 2016 — [[wiki/summaries/2016_Sun_NeutronRadiographyU10ZrSwelling|Sun 2016]] — U-10Zr 肿胀中子射线照相
- 2017 — [[wiki/summaries/2017_Casella_CharacterizationFissionGasBubblesU10Mo|Casella 2017]] — U-10Mo 裂变气体气泡表征
- 2018 — [[wiki/summaries/2018_Liang_3DPhaseFieldIntragranularBubbleUMo|Liang 2018]] — 3D 晶内气泡相场模拟
- 2018 — [[wiki/summaries/2018_Millett_ComputationalExperimentalPorosityMetallic|Millett 2018]] — 孔隙率计算与实验

### 2020年代 — 现代模型与验证
- 2019 — [[wiki/summaries/2019_Mohamed_MURRLEU10MoSwellingCreep|Mohamed 2019]] — MURR U-10Mo 肿胀与蠕变
- 2020 — [[wiki/summaries/2020_Aagesen_BisonUPuZrSwellingLowerLengthScale|Aagesen 2020]] — BISON U-Pu-Zr 下尺度改进
- 2020 — [[wiki/summaries/2020_Beeler_ImprovedEOSXeBubbleUMo|Beeler 2020]] — Xe 气泡改进状态方程
- 2020 — [[wiki/summaries/2020_Hu_DefectClusterGasBubbleUMo|Hu 2020]] — 缺陷团簇与气泡耦合生长
- 2020 — [[wiki/summaries/2020_Williams_PIRT_SwellingUZr|Williams 2020]] — U-Zr 肿胀 PIRT 分析
- 2021 — [[wiki/summaries/2021_Hilty_FissionGasBubblesThermalConductivity|Hilty 2021]] — 气泡对热导率的影响
- 2021 — [[wiki/summaries/2021_Qian_RateTheoryUN|Qian 2021]] — UN 燃料速率理论
- 2021 — [[wiki/summaries/2021_Robinson_PredictiveSwellingUMoMonolithic|Robinson 2021]] — U-10Mo 预测肿胀关联式（18000+ 数据点）
- 2021 — [[wiki/summaries/2021_Zhang_EffectiveSwellingInertMatrix|Zhang 2021]] — 惰性基体燃料有效肿胀
- 2022 — [[wiki/summaries/2022_Aagesen_PFBubbleInterconnection|Aagesen 2022]] — 气泡互连相场模拟
- 2022 — [[wiki/summaries/2022_Hanson_EMPIrESwellingAnalysis|Hanson 2022]] — EMPIrE 肿胀分析
- 2022 — [[wiki/summaries/2022_Jian_FissionGasSwellingModelU10Mo|Jian 2022]] — U-10Mo 裂变气体肿胀模型
- 2022 — [[wiki/summaries/2022_Yun_CavitationalVoidSwelling|Yun 2022]] — 空穴型空洞肿胀（JSRT 校准）
- 2023 — [[wiki/summaries/2023_Li_ElasticConstantsU10Mo|Li 2023]] — 辐照 U-10Mo 弹性常数
- 2023 — [[wiki/summaries/2023_Smith_EarlySelfOrganizationGBS|Smith 2023a]] — 超晶格早期自组织
- 2023 — [[wiki/summaries/2023_Smith_UCInclusionsGBS|Smith 2023b]] — UC 夹杂物与超晶格
- 2023 — [[wiki/summaries/2023_Ye_IntegratedSimulationU10Mo|Ye 2023]] — U-10Mo 集成模拟
- 2024 — [[wiki/summaries/2024_Aagesen_VacancyProductionPF|Aagesen 2024]] — 空位产生参数化
- 2024 — [[wiki/summaries/2024_Arivu_APTSegregationGasBubblesUMo|Arivu 2024]] — 气泡偏析 APT 表征
- 2024 — [[wiki/summaries/2024_Muntaha_GB_SurfaceDiffusion|Muntaha 2024]] — 晶界/表面扩散效应
- 2025 — [[wiki/summaries/2025_Hanson_StablePredictableSwellingU10Mo|Hanson 2025]] — 稳定可预测肿胀
- 2025 — [[wiki/summaries/2025_Jiang_GasBubbleSuperlatticePhaseField|Jiang 2025]] — 超晶格相场研究
- 2026 — [[wiki/summaries/2026_FigueroaBengoa_HighBurnupPorosityUMo|FigueroaBengoa 2026]] — 高燃耗孔隙率演化

## 开放问题

1. 为什么 JSRT 在 600K 预测肿胀为零？是物理真实还是模型假象？
2. U-10Mo 中正确的空位迁移能是多少？（文献值 0.34 eV vs 0.6 eV）
3. 如何建模再结晶 onset 处的肿胀转变？
4. U-Mo 参数能否通过简单标度传递给 U-Zr？
5. 非单调气泡密度行为的驱动力是什么？（Jian 2022）

## 术语对照

完整术语表见 [[raw/terminology|中英文术语对照表]]（160+ 条目）
