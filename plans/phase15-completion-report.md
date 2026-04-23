# Phase 1.5 文献扩展 — 完成报告

**日期**: 2026-04-22  
**状态**: ✅ 已完成  
**执行时间**: ~8 小时（09:50–18:00）

---

## 一、目标回顾

Phase 1.5 的核心目标是**补齐 4 个空白方向**的文献覆盖，使知识库从以 U-Mo 肿胀为主扩展到覆盖金属燃料全栈关键物理过程：

1. FCCI（fuel-cladding chemical interaction）
2. FGR（fission gas release）
3. Irradiation creep（辐照蠕变）
4. Constituent redistribution（组元再分布）

---

## 二、完成情况

### 2.1 总量增长

| 指标 | Phase 1.5 前 | Phase 1.5 后 | 增量 |
|------|-------------|-------------|------|
| 总参数 | ~1,385 | **1,921** | +536 |
| 摘要文件 | ~55 | **72** | +17 |
| raw/mineru 目录 | ~103 | **120** | +17 |
| 参数 JSON 文件 | ~54 | **71** | +17 |

### 2.2 新增文献明细（17 篇）

#### 第一优先级（5 篇，175 参数）

| # | 文献 | 年份 | 方向 | 参数 |
|---|------|------|------|------|
| 1 | Matthews et al. — FCCI Critical Review of U-Pu-Zr | 2017 | FCCI | 40 |
| 2 | GRSIS — Fission gas release and swelling model | 2001 | FGR | 26 |
| 3 | Kim et al. — Fission-induced swelling and creep of U-Mo | 2013 | Irradiation Creep | 11 |
| 4 | Matthews et al. — Physics-based metallic fuel formulation (BISON) | 2023 | BISON/骨架 | 63 |
| 5 | Galloway et al. — Constituent redistribution in U-Pu-Zr (BISON) | 2015 | Redistribution | 35 |

#### 第二优先级（3 篇，96 参数）

| # | 文献 | 年份 | 方向 | 参数 |
|---|------|------|------|------|
| 6 | Hirschhorn et al. — Mechanistic multiscale FCCI model (BISON) | 2025 | FCCI | 31 |
| 7 | Karahan & Buongiorno — FEAST-METAL code | 2010 | BISON/Code | 35 |
| 8 | Karahan & Andrews — Extended swelling models (FEAST-METAL) | 2013 | Swelling/FGR | 30 |

#### 第三批扩展（9 篇，267 参数）

| # | 文献 | 年份 | 方向 | 参数 |
|---|------|------|------|------|
| 9 | Kim et al. — Constituent redistribution in U-Pu-Zr | 2004 | Redistribution | 29 |
| 10 | Hofman, Hayes & Petri — Temperature gradient driven redistribution in U-Zr | 1996 | Redistribution | 29 |
| 11 | Hirschhorn et al. — Phase-field modeling redistribution in U-Zr | 2019 | Redistribution | 29 |
| 12 | Hirschhorn, Tonks & Matthews — CALPHAD-informed redistribution (BISON) | 2021 | Redistribution | 40 |
| 13 | Carmack et al. — FCCI metallography (FFTF, MFF-3) | 2016 | FCCI | 47 |
| 14 | Geiger et al. — TAF-ID thermodynamic investigation of FCCI | 2021 | FCCI | 38 |
| 15 | Jian et al. — U-Mo irradiation creep, mesoscale | 2019 | Irradiation Creep | 14 |
| 16 | Tsuboi et al. — Mechanistic model of fission gas behavior | 1992 | FGR | 13 |
| 17 | Ogata et al. — Analytical study of fission gas behavior | 1996 | FGR | 16 |

### 2.3 四方向覆盖

| 方向 | 新增论文 | 既有论文 | 合计 | 状态 |
|------|---------|---------|------|------|
| FCCI | 4（Matthews, Hirschhorn 2025, Carmack, Geiger） | 0 | **4** | ✅ |
| FGR | 3（GRSIS, Tsuboi, Ogata） | 0 | **3** | ✅ |
| Irradiation Creep | 1（Jian 2019） | 4（Kim 2013, Mohamed, MURR 等） | **5** | ✅ |
| Redistribution | 5（Kim 2004, Hofman, Hirschhorn ×2, Galloway） | 1（Williams 2020） | **6** | ✅ |

---

## 三、质量改进

### 3.1 Category 标准化

- **问题**: 子智能体提取时使用了非标准 category 标签（composition, geometric, kinetic 等 40+ 种）
- **修复**: 全部映射到标准 9 类体系，覆盖 71 个 JSON 文件
- **结果**: 1921 条参数全部为标准 category

### 3.2 标准分类分布

| Category | 数量 | 占比 |
|----------|------|------|
| fuel_performance | 1,461 | 76.1% |
| diffusion | 153 | 8.0% |
| thermodynamic | 74 | 3.9% |
| irradiation | 54 | 2.8% |
| phase_transformation | 50 | 2.6% |
| bubble | 43 | 2.2% |
| swelling | 43 | 2.2% |
| elastic | 29 | 1.5% |
| activation_energy | 14 | 0.7% |

> 注：fuel_performance 占比高，是因为大量早期论文参数在映射时 default 到此类。Phase 2 可进一步细分。

### 3.3 数据完整性修复

- 修复 `2016_Hu_GasBubbleSuperlatticeFormationPF.json` 缺逗号导致的 JSON 损坏（36 参数）
- BISON 2023 的 63 条参数从 category=unknown 补全到标准分类

---

## 四、SKILL.md 更新

新增实战经验 3 条（异常处理）：

1. **SSL/网络失败** → 跳过 MinerU，直接 pdftotext
2. **pdftotext 后公式补回** → DOI + web_search，标记 `formula_source: doi_search`
3. **目录名预校验** → 转换前对比 PDF 标题，不匹配时修正 slug

---

## 五、未完成项

| 项目 | 说明 | 优先级 |
|------|------|--------|
| FCCI 2012（温度-燃耗关联） | 候选清单中，Zotero 无 PDF | 低 |
| U-Pu-Zr 1994（辐照性能综述） | 候选清单中，Zotero 无 PDF | 低 |
| BISON 2023 category 细化 | 当前粗粒度映射，可进一步按 equation 精细分类 | 低 |
| fuel_performance 占比过高 | 大量参数 default 到此类，需要人工审阅重分类 | 中 |

---

## 六、下一步（Phase 2 建议）

1. **Lobster Pipeline 自动化** — 将 ingest 流程固化为可复用 pipeline
2. **参数质量审阅** — 对 fuel_performance 类参数进行细分
3. **概念图生成** — 基于 summary + parameters 生成领域概念关系图
4. **查询接口** — 提供语义搜索 API 供下游使用
