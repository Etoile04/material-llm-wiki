# Piro 2021 - Thermodynamically Informed Nuclear Fuel Codes: A Review and Perspectives

**论文信息**: Piro, M.H.A. *Thermo* 2021, 1, 262–285.
**类型**: 综述论文
**关键词**: thermodynamics, nuclear fuel, fuel performance, CALPHAD, multi-physics

## 摘要

本文系统综述了热力学计算与核燃料程序耦合的研究进展，将燃料程序分为两类：Class I（研究开发类）和 Class II（工业安全分析类）。Class I 程序包括 COMSOL、AMP、BISON、MARMOT、ALCYONE 和 GERMINAL，用于机理探索和能力开发；Class II 程序包括 VICTORIA、MFPR、MELCOR、ASTEC 和 SOURCE，用于严重事故下的裂变产物释放预测。

文章详细讨论了多种热力学耦合策略：经验关联式（如 Lindemer-Besmann 方程）、查表法、以及直接耦合 Gibbs 能量最小化求解器（如 THERMOCHIMICA、OpenCalphad）。在 COMSOL 框架中，利用 CALPHAD 方法推导的 Gibbs 能量方程实现了 UO₂₊ₓ 和 MOX 燃料的非一致熔化相场模拟。BISON-THERMOCHIMICA 耦合实现了基于化学势梯度的氧扩散计算，避免了 Soret 效应修正。在 U-Pu-Zr 金属燃料方面，Poschmann 和 Hirschhorn 分别采用直接耦合和查表法处理 U/Zr 相互扩散，揭示了"浴缸"型 Zr 分布特征。

ALCYONE 通过 OpenCalphad 耦合使用 TAF-ID 数据库（含 210 个二元系和 76 个三元系），预测 PCI 过程中碘的化学形态。GERMINAL 利用热力学计算预测钠冷快堆 MOX 燃料中 JOG（Joint Oxyde Gaine）层的形成。MFPR 采用半理想化学近似处理溶解在萤石基体中的裂变产物。

文章指出了当前面临的主要挑战：(1) 有限元网格上直接耦合热力学求解器的计算开销显著增加；(2) 相场模拟中物种数大于元素数导致的欠定系统问题；(3) 非常规燃料（U-C-O、熔盐等）的热力学数据库尚不成熟；(4) 热力学软件的质量保证（SQA）缺乏公开报道。

未来方向包括：并行化热力学求解、简化耦合策略（如代表性节点插值）、YELLOWJACKET 开发（将 GEM 直接耦合至 MARMOT 相场程序），以及加强国际合作推进 TAF-ID 和 MEPHISTA 数据库建设。

## Related Work
- [[wiki/concepts/FuelPerformanceCodes|FuelPerformanceCodes]] — 综述了BISON、MARMOT等燃料性能代码的热力学耦合
- [[wiki/entities/BISONCode|BISONCode]] — BISON-THERMOCHIMICA耦合是本文重点讨论的案例
- [[wiki/summaries/Hales_2016_BISON_TheoryManual|Hales_2016_BISON_TheoryManual]] — BISON理论手册，与本文讨论的BISON热力学耦合直接相关
- [[wiki/summaries/Lu_2018_CALPHAD_UFuels|Lu_2018_CALPHAD_UFuels]] — CALPHAD在铀燃料中的应用，补充热力学建模基础
- [[wiki/summaries/Turchi_2018_ThermodynamicDiffusion|Turchi_2018_ThermodynamicDiffusion]] — 热力学与扩散数据汇编，为燃料代码提供输入
- [[wiki/summaries/VanUffelen_2019_FuelPerformanceReview|VanUffelen_2019_FuelPerformanceReview]] — 燃料性能代码综述

## 核心程序与应用

| 程序 | 类型 | 热力学耦合方式 | 应用场景 |
|------|------|----------------|----------|
| COMSOL | Class I | CALPHAD Gibbs能方程 | 燃料氧化、非一致熔化 |
| AMP | Class I | THERMOCHIMICA | 氧势径向分布 |
| BISON | Class I | THERMOCHIMICA/查表 | 氧扩散、U-Zr再分布 |
| MARMOT | Class I | 自动微分Gibbs能 | 介观组织演化 |
| ALCYONE | Class I | OpenCalphad/TAF-ID | PCI、裂变产物化学 |
| GERMINAL | Class I | OpenCalphad/TAF-ID | MOX燃料JOG形成 |
| VICTORIA | Class II | 内置数据库（26元素/288物种）| 严重事故裂变产物释放 |
| MFPR | Class II | Lindemer-Besmann方程 | 正常/事故工况 |
| MELCOR | Class II | VANESA/GEM | 严重事故进程 |
| ASTEC | Class II | 平衡常数关联式 | 严重事故源项 |
| SOURCE | Class II | ChemApp/RMCTT | CANDU事故源项 |
