# Phase 1.5 候选文献清单（继续扩展）

更新日期：2026-04-21 23:18 GMT+8

目标：补齐 Phase 1.5 后半段的 4 个空白方向，并形成下一批可入库候选。

---

## A. U-Pu-Zr / 金属燃料性能骨架

| Priority | Type | Title | Year | Topic | URL | Notes |
|---|---|---:|---|---|---|---|
| high | model / code | Development and formulation of physics based metallic fuel models and comparison to integral irradiation data | 2023 | BISON metallic fuel baseline, swelling/FGR/FCCI | https://www.osti.gov/biblio/1960181 | 高价值骨架文献，可串联多个机制 |
| high | model | Extended fuel swelling models and ultra high burn-up fuel behavior of U–Pu–Zr metallic fuel using FEAST-METAL | 2013 | FEAST-METAL, swelling/FGR/FCCI | https://www.sciencedirect.com/science/article/abs/pii/S0029549313000435 | 已知重要骨架文献，应优先入库 |
| high | redistribution model | Modeling of constituent redistribution in U–Pu–Zr metallic fuel | 2006 | constituent redistribution | https://www.sciencedirect.com/science/article/abs/pii/S0022311506004120 | U-Pu-Zr 关键机制文献 |
| medium | irradiation performance | Irradiation performance of U-Pu-Zr metal fuels for liquid-metal-cooled reactors | 1994 | 性能综述 / 高燃耗表现 | https://www.osti.gov/servlets/purl/106470 | 适合作为历史性能背景 |
| medium | review | Status of performance and fabrication of metallic U-Pu-Zr fuel for the integral fast reactor | 1984 | fabrication + irradiation performance + compatibility | https://www.osti.gov/biblio/707411 | 经典背景综述 |
| medium | experiment | Steady-state irradiation testing of U-Pu-Zr fuel to >18% burnup | 1989 | burnup / gas release / swelling | https://www.osti.gov/biblio/7177201 | 与 FGR/肿胀关联强 |

---

## B. Irradiation creep

| Priority | Type | Title | Year | Topic | URL | Notes |
|---|---|---:|---|---|---|---|
| high | model / implementation | Irradiation Creep for U 10 Mo \| BISON | - | U-10Mo irradiation creep constitutive model | https://mooseframework.inl.gov/releases/bison/v2.0.0/source/materials/tensor_mechanics/U10MoCreepUpdate.html | 虽不是论文，但适合补模型公式和实现接口 |
| high | journal article | Fission induced swelling and creep of U–Mo alloy fuel | 2013 | U-Mo 蠕变与肿胀耦合 | https://www.osti.gov/biblio/1111062-fission-induced-swelling-creep-umo-alloy-fuel | 高优先级，直接命中空白 |
| medium | experiment/model | Effect of stress on microstructural evolution in U-Mo/Al dispersion fuel | - | stress + relocation + creep | https://www.osti.gov/pages/servlets/purl/1373747 | 与板型燃料相关 |
| medium | assessment | Thermo-mechanical performance assessment of selected plates from MP-1 low power experiments | 2018 | irradiation creep in plate fuel | https://www.osti.gov/biblio/1484449 | 可补工程模型侧 |
| medium | model context | Development and formulation of physics based metallic fuel models and comparison to integral irradiation data | 2023 | creep + FGR + swelling baseline | https://www.osti.gov/servlets/purl/1960181 | 与上面骨架文献重合，可合并处理 |

---

## C. FCCI

| Priority | Type | Title | Year | Topic | URL | Notes |
|---|---|---:|---|---|---|---|
| high | critical review | Fuel-Cladding Chemical Interaction in U-Pu-Zr Metallic Fuels: A Critical Review | 2017 | FCCI review | https://www.osti.gov/biblio/1523231 | 这个方向最值得先入库 |
| high | mechanistic model | Improvement of mechanistic fuel-cladding chemical interaction modeling in BISON | 2025? | BISON FCCI model | https://www.osti.gov/servlets/purl/2477151/ | 近年模型文献，优先级高 |
| high | technical report | Temperature and Burnup Correlated FCCI in U-10Zr Metallic Fuel | 2012 | FCCI correlation | https://www.osti.gov/biblio/1055966/ | 可提参数与相关式 |
| medium | classic compatibility | Fuel/cladding compatibility in high-burnup U-19 Pu-10 Zr/HT-9 clad fuel at elevated temperatures | 1991 | compatibility / eutectic / cladding thinning | https://www.osti.gov/biblio/6982511 | 经典 FCCI 机理 |
| medium | out-of-pile program | Out-of-pile experiments performed in the U. S. Fuel Cladding Chemical Interaction (FCCI) Program | 1976 | FCCI 实验 program | https://www.osti.gov/biblio/5854941 | 历史背景支撑 |
| medium | additive mitigation | Alloying additions are introduced into U-Zr fuel in order to bind lanthanides... | - | lanthanide mitigation / Pd additive | https://www.osti.gov/servlets/purl/1631115 | 对 mitigation 策略有价值 |

---

## D. Fission gas release (FGR)

| Priority | Type | Title | Year | Topic | URL | Notes |
|---|---|---:|---|---|---|---|
| high | mechanistic model | Fission gas release and swelling model of metallic fast reactor fuel | 2001 | GRSIS / FGR + swelling | https://www.sciencedirect.com/science/article/abs/pii/S0022311500007182 | 必入，FGR 骨架文献 |
| high | precursor / technical report | GRSIS program to predict fission gas release and swelling behavior of metallic fast reactor fuel | 1999 | GRSIS technical baseline | https://www.osti.gov/etdeweb/biblio/20010563 | 与 2001 论文形成前后对应 |
| high | code description | A new code for predicting the thermo-mechanical and irradiation behavior of metallic fuels in sodium fast reactors | 2010 | FEAST-METAL + GRSIS + FCCI | https://www.osti.gov/etdeweb/biblio/21363701 | 强骨架文献 |
| medium | coupled simulation | Fully-Coupled Metallic Fuel Performance Simulations using BISON | 2015 | metallic FGR + redistribution | https://www.osti.gov/biblio/1213497 | 工程实现侧 |
| medium | broad review | Development and formulation of physics based metallic fuel models and comparison to integral irradiation data | 2023 | retained gas / release trend / UPuZr | https://www.osti.gov/servlets/purl/1960181 | 可兼作 U-Pu-Zr 与 FGR 骨架 |

---

## 下一批建议优先顺序

### 第一优先级（建议先 ingest）

1. Fuel-Cladding Chemical Interaction in U-Pu-Zr Metallic Fuels: A Critical Review (2017)
2. Fission gas release and swelling model of metallic fast reactor fuel (2001)
3. Fission induced swelling and creep of U–Mo alloy fuel (2013)
4. Development and formulation of physics based metallic fuel models... (2023)
5. Modeling of constituent redistribution in U–Pu–Zr metallic fuel (2006)

### 第二优先级

6. Extended fuel swelling models and ultra high burn-up fuel behavior of U–Pu–Zr metallic fuel using FEAST-METAL (2013)
7. Improvement of mechanistic fuel-cladding chemical interaction modeling in BISON
8. Temperature and Burnup Correlated FCCI in U-10Zr Metallic Fuel
9. A new code for predicting the thermo-mechanical and irradiation behavior of metallic fuels in sodium fast reactors (2010)
10. Irradiation performance of U-Pu-Zr metal fuels for liquid-metal-cooled reactors (1994)

## 建议动作

- 先为上述前 5 篇确认 PDF 可获取性
- 对可获取 PDF 立即进入 MinerU / pdftotext 转换
- 对代码文档类来源（如 BISON 页面）可直接走 article ingest，而非 PDF 流程
