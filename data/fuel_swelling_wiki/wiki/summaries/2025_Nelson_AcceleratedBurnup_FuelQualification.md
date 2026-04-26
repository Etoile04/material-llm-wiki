# 加速燃耗辐照测试在加速燃料合格鉴定中的作用

## Metadata
- **Title**: Role of Accelerated Burnup Irradiation Testing in Support of Accelerated Fuel Qualification
- **Authors**: A. T. Nelson, D. Adorno Lopes, N. A. Capps, C. M. Petrie
- **Year**: 2025
- **Journal**: Nuclear Technology, DOI: 10.1080/00295450.2025.2481360
- **Affiliation**: Oak Ridge National Laboratory, Nuclear Energy and Fuel Cycle Division

## 摘要

本文系统阐述了加速燃耗（ABU）辐照测试在加速燃料合格鉴定（AFQ）框架中的角色与定位。作者首先回顾了核燃料合格鉴定的技术就绪水平（TRL 1-9）框架，将传统鉴定过程划分为概念化（TRL 1-3）、原型开发（TRL 4-6）和示范商用（TRL 7-9）三个阶段。

两种主要的ABU平台——ORNL的MiniFuel（利用HFIR高通量）和INL的FAST（利用高富集度+小尺寸）——均通过提高裂变率来加速燃耗积累。文章澄清了ABU与AFQ的关系：ABU是AFQ的一个组成部分，但不能替代整体积分辐照测试。ABU的核心价值在于早期阶段的分离效应测试，为热导率、肿胀、力学性能、裂变气体释放等关键模型提供数据支撑。

文章通过多个实例说明了ABU的当前应用和未来潜力，并总结了关键挑战：裂变率对扩散、微观结构演化和其他关键机制的影响仍需深入理解。特别是裂变速率变化可能改变温度梯度、裂变气体行为和燃料-包壳相互作用的演化路径，这些效应需要在将ABU数据外推至正常工况时进行校准。

## Key Equations

本文为综述/框架类论文，无核心物理模型公式。关键概念包括：

- **ABU加速因子**：$\text{ABU factor} = \frac{\dot{f}_{\text{test}}}{\dot{f}_{\text{reactor}}}$，即测试裂变速率与目标反应堆裂变速率之比
- **TRL推进逻辑**：ABU辐照主要服务于 TRL 2-5 阶段的材料模型开发

## 关键结论
1. ABU不能替代积分辐照，但可显著降低前期研发时间和成本
2. 裂变率效应（fission rate effect）是ABU方法学中最大的不确定性来源
3. MiniFuel和FAST两种平台互补，前者适合高通量分离效应测试，后者更接近真实几何条件

## Related Work
- [[wiki/entities/BISONCode|BISONCode]] — MiniFuel数据用于BISON燃料性能代码验证
- [[wiki/summaries/2025_Doyle_Swelling_FGR_U10Mo_U17Mo|2025_Doyle_Swelling_FGR_U10Mo_U17Mo]] — MiniFuel平台上U-Mo肿胀-FGR实验
- [[wiki/summaries/2025_Duan_3DBurnup_HelicalCruciformFuel|2025_Duan_3DBurnup_HelicalCruciformFuel]] — 精细燃耗分析方法
- [[wiki/concepts/FissionGasReleaseModels|FissionGasReleaseModels]] — 加速燃耗方法学中FGR模型的不确定性
- [[wiki/summaries/2016_Hales_BISON_TheoryManual|2016_Hales_BISON_TheoryManual]] — BISON理论框架
