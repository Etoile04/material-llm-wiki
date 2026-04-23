# Phase 1.5 进展报告

**日期**: 2026-04-21 ~ 2026-04-22  
**执行人**: Lily 🦀  
**状态**: ✅ 已完成

---

## 一、目标

Phase 1.5 的真实目标有两部分：

1. 扩展参数提取范围：从"燃料肿胀"单一方向 → **9 类材料参数全覆盖**
2. 扩展文献覆盖面：从早期 47 篇提升到 **100+ 篇候选/可入库文献池**，并优先补齐 4 个空白方向

---

## 二、执行过程

### Batch A：新论文 ingest（6 篇）

从 Zotero 新增 6 篇去重论文（原子模拟/扩散/相变方向）：

| 论文 | 主题 | 参数 | Key Equations |
|------|------|------|---------------|
| Park 2021 | U-Mo 缺陷能/扩散（原子模拟） | 9 | ✅ |
| Beeler 2021 | γU-Mo 辐照驱动扩散 | 10 | ✅ |
| Interdiffusion Zr/U-Mo | Zr 扩散阻挡层互扩散 | 10 | ✅ |
| Kr 离子辐照铀合金 | Kr 辐照微结构演化 | 10 | ✅ |
| U-Mo-Ti 相变特征 | 相变动力学 | 10 | ✅ |

### Batch B：新论文 ingest（6 篇，继续）

| 论文 | 主题 | 参数 |
|------|------|------|
| Hu 2016 | 气泡超晶格相场模拟 | 36 |
| Williams 2020 | PIRT 评估肿胀和组元再分布 | 8 |
| Willard 1985 | 金属燃料肿胀综述 | 25 |
| Hofman 1990 | U-Pu-Zr 肿胀行为综述 | 13 |
| Beeler (Xie) 2020 | γU 辐照损伤分子动力学 | 10 |
| Ke 2020 | U-Mo 合金辐照微观结构演化 | 10 |

### Batch C：新论文 ingest（6 篇）

| 论文 | 主题 | 参数 |
|------|------|------|
| Bai 2021 | U-Mo 辐照蠕变分子动力学 | 12 |
| Ye 2021 | U-Mo 蠕变实验+MD | 15 |
| Mohamed 2019 | MURR LEU-U10Mo 肿胀蠕变 | 14 |
| Talamo 2020 | MCNP 辐照 U-Mo | 10 |
| 2024 MURR | LEU U-10Mo 肿胀蠕变实验 | 15 |
| Jiang 2025 | 气泡超晶格相场模拟 | 12 |

### Batch D：参数补全（9 篇存量论文补充提取）

对已有 raw/mineru 但缺少 parameters 的存量论文补充参数提取：

| 论文 | 新增参数 |
|------|---------|
| Bragg-Sitton 2009 | 10 |
| Park 2021 | 8 |
| Rest 7 papers | ~50 |

### Batch E（4/22）：Phase 1.5 四方向补齐（17 篇）

#### 第一优先级（5 篇，175 参数）

| 论文 | 方向 | 参数 |
|------|------|------|
| Matthews 2017 FCCI Critical Review | FCCI | 40 |
| GRSIS 2001 FGR model | FGR | 26 |
| Kim 2013 Swelling+Creep | Irradiation Creep | 11 |
| BISON 2023 physics-based formulation | BISON/骨架 | 63 |
| Galloway 2015 Redistribution (BISON) | Redistribution | 35 |

#### 第二优先级（3 篇，96 参数）

| 论文 | 方向 | 参数 |
|------|------|------|
| Hirschhorn 2025 Multiscale FCCI | FCCI | 31 |
| Karahan 2010 FEAST-METAL | BISON/Code | 35 |
| Karahan 2013 Extended swelling | Swelling/FGR | 30 |

#### 第三批扩展（9 篇，267 参数）

| 论文 | 方向 | 参数 |
|------|------|------|
| Kim 2004 Redistribution experiment | Redistribution | 29 |
| Hofman 1996 Temperature gradient redistribution | Redistribution | 29 |
| Hirschhorn 2019 Phase-field redistribution | Redistribution | 29 |
| Hirschhorn 2021 CALPHAD redistribution (BISON) | Redistribution | 40 |
| Carmack 2016 FCCI metallography | FCCI | 47 |
| Geiger 2021 TAF-ID FCCI thermodynamics | FCCI | 38 |
| Jian 2019 U-Mo irradiation creep mesoscale | Irradiation Creep | 14 |
| Tsuboi 1992 Fission gas behavior | FGR | 13 |
| Ogata 1996 Fission gas behavior | FGR | 16 |

---

## 三、最终成果

| 指标 | Phase 1 前 | Phase 1.5 后 | 增量 |
|------|-----------|-------------|------|
| 总参数 | ~476 | **1,921** | +1,445 |
| 摘要文件 | ~47 | **72** | +25 |
| raw/mineru 目录 | ~47 | **120** | +73 |
| 参数 JSON | ~47 | **71** | +24 |
| Category 体系 | 无 | **9 类** | +9 |

### 四方向覆盖

| 方向 | 论文数 | 状态 |
|------|--------|------|
| FCCI | 4 | ✅ |
| FGR | 3 | ✅ |
| Irradiation Creep | 5 | ✅ |
| Redistribution | 6 | ✅ |

---

## 四、质量改进

1. ✅ Category 标准化：71 个 JSON 文件全部映射到 9 类
2. ✅ JSON 损坏修复：Hu 2016 文件
3. ✅ SKILL.md 异常处理补充（SSL/pdftotext/目录名校验）
4. ✅ Subagent 模型切换到 zai/glm-5-turbo

---

## 五、详细完成报告

→ `plans/phase15-completion-report.md`

---

## 六、下一步

→ Phase 2：Lobster Pipeline 自动化 + 参数质量审阅
