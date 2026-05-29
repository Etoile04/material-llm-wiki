# 势函数验证参考值补全系统 — 阶段性进展总结

**项目代号**: ref-gap-fill  
**日期**: 2026-05-29  
**版本**: v0.1 (Design Phase Complete)

---

## 1. 项目背景

NucPot 势函数验证服务依赖 `reference_values` 表中的参考物性值（晶格常数、弹性常数、内聚能等）来校验分子动力学势函数的准确性。

**现状问题：**
- `reference_values` 表仅有 **23 条记录**，覆盖 5 个体系（U、Mo、Zr、Nb、U-Mo）
- 实际需覆盖 **14+ 体系 × 8+ 物性 ≈ 100+ 条**
- 手动补充效率低、不可持续
- 已有多个系统（NFMD 数据库、llm-wiki 知识库、ontofuel 本体）各自具备部分能力，但缺乏统一编排

---

## 2. 设计方案

### 2.1 核心架构：多智能体协作 + 快慢线分离

```
势函数验证服务 → 提交数据需求 (GapRequest)
        │
        ▼
数据库智能体 (nucpot-db)
  ├─ 三级缓存查询 (同步, ≤5s)
  │   L1: reference_values (本地 PG, 23条)
  │   L2: NFMD parameters (Supabase, 6981条)
  │   L3: llm-wiki params (14320条) + ontofuel 本体 (279属性)
  │
  ├─ 缓存命中 → 直接返回
  │
  └─ 未命中 → 派发快线
        │
        ▼
搜索智能体 (nucpot-librarian)
  搜索 (Zotero → Semantic Scholar → Web)
  获取 PDF → MinerU 解析 → LLM 提取
  返回物性值 + 标记文献待消化
        │
        ▼
数据库智能体验证 + 分级写入
  high confidence → 自动写入
  medium/low → 标记待审核
        │
        ▼
慢线 (异步, cron 每周)
  llm-wiki 深度消化 + ontofuel 本体提取
  → 回填三级缓存 → 提升未来命中率
```

### 2.2 关键设计决策

| 决策 | 选择 | 理由 |
|------|------|------|
| 智能体架构 | 新建专用 agent (nucpot-db + nucpot-librarian) | main 专注宏观调度，职责分离 |
| 慢线触发 | 混合：快线标记 + cron 批量消化 | 不阻塞快线，批量效率高 |
| 写入策略 | 分级：high 自动 / medium-low 标记待审核 | 平衡自动化与数据质量 |
| 数据存储 | 本地 PG 为主，慢线双写到 NFMD | 快线快写，慢线全面同步 |

---

## 3. 数据资产盘点

### 3.1 已有数据（可立即利用）

| 数据源 | 记录数 | 可映射到 reference_values | 状态 |
|--------|--------|--------------------------|------|
| reference_values (L1) | 23 | 23 (已就位) | ✅ 可用 |
| NFMD parameters (L2) | 6,981 | 估计 50-100 条 | ⚠️ 需中英文物性名映射 + 单位转换 |
| llm-wiki params (L3a) | 14,320 (458 篇) | 68 条已识别 | ⚠️ 全中文命名，需 adapter |
| ontofuel 本体 (L3b) | 140 classes, 279 props | ~20 条物性相关 | ⚠️ 缺 Cij 属性定义 |

**预估**：三级缓存打通后，reference_values 可从 23 条扩充至 **~150 条**。

### 3.2 已识别的 llm-wiki 可用参数（部分）

| 体系 | 物性 | 值 | 来源 |
|------|------|-----|------|
| U-7wt%Mo (BCC) | 晶格常数 | 0.343 nm | Hu 2016 |
| γ-U | C11 / C12 / C44 | 94 / 154 / 34 GPa | Mei 2016 |
| U-7Mo | C11 / C12 / C44 | 173 / 138 / 50 GPa | Mei 2016 |
| bcc Mo | C11 / C12 / C44 | 466 / 157 / 103 GPa | Mei 2016 |

> 注：llm-wiki 参数为中文命名（如"晶格常数"、"弹性常数"），需要 property-mapping.json 做中英文映射。

### 3.3 物性缺口全景

| 优先级 | 体系 | 已有性质 | 缺失性质 | 缺口数 |
|--------|------|----------|----------|--------|
| P1 | U (BCC) | C11,C12,C44,lattice,vacancy_E | cohesive_E, bulk_modulus | 2 |
| P1 | Mo (BCC) | C11,C12,C44,lattice,vacancy_E | cohesive_E, bulk_modulus | 2 |
| P1 | Zr (BCC) | lattice,vacancy_E | C11,C12,C44,cohesive_E,bulk_modulus | 5 |
| P1 | Zr (HCP) | C11,C33,lattice | C12,C44,cohesive_E,bulk_modulus | 4 |
| P1 | Nb (BCC) | C11,C12,C44,lattice,vacancy_E | cohesive_E, bulk_modulus | 2 |
| P1 | U-Mo (BCC) | C11,C12,lattice | C44,cohesive_E,bulk_modulus,vacancy_E | 4 |
| P2 | U-Zr ~ U-Pu-Zr | 无 | 全部 | 8×5=40 |
| P3 | Fe, Cr, SiC | 无 | 全部 | ~16 |
| **总计** | | | | **~75 个缺口** |

---

## 4. 可复用资产审计

### 4.1 可直接复用（无需修改）

| 资产 | 能力 | 复用于 |
|------|------|--------|
| ontofuel Python API (`Segmenter`, `Extractor`, `Merger`, `Updater`) | 超长文档分割→LLM提取→合并→本体更新 | 慢线 |
| llm-wiki `batch_extract.py` | 去重、schema 验证、子 agent prompt 生成 | 慢线 |
| llm-wiki `normalize_typed_values.py` | 单位/类型标准化 | 基础设施 |
| llm-wiki `compare_params.py` | 单位换算因子表 (GPa↔MPa 等) | 基础设施 |
| llm-wiki `zotero_sync.py` | Zotero→知识库同步、PDF 检测 | 慢线触发 |
| llm-wiki Lobster pipeline (`ingest_single_v2.lobster`, `incremental_update.lobster`) | PDF→文本→质量检查的确定性流程 | 快线 Step 4 + 慢线 |
| ref-gap-fill 现有 SKILL.md | Step 1-7 完整流程、搜索策略、提取 prompt、单位换算表 | 重构为编排协议 |
| 验证 API CRUD (GET/POST/PATCH/DELETE) | reference_values 读写 | 基础设施 |
| NFMD RPC (`search_parameters`) | 参数搜索 | L2 缓存查询 |

### 4.2 需要适配

| 资产 | 适配工作 | 工作量 |
|------|----------|--------|
| llm-wiki 68 条中文参数 | 中文名→英文 property 映射 + 单位转换 | 小 |
| ontofuel 本体 | 新增 C11/C12/C44/C33 属性定义 | 小 |
| ref-gap-fill 提取 prompt | 追加 confidence 字段和分级逻辑 | 小 |

### 4.3 必须新建

| 资产 | 说明 |
|------|------|
| `property-mapping.json` | L1↔L2↔L3 物性名映射（核心基础设施） |
| `cache-query.py` | 三级缓存统一查询脚本 |
| `write-ref-value.py` | 分级写入 + 质量门控 |
| `adapter-nfmd.py` | NFMD → reference_values 格式转换 |
| nucpot-db / nucpot-librarian agent 配置 | openclaw.json 新增 |
| librarian-search / librarian-extract SKILL.md | 快线技能 |
| 慢线 cron job | 定时触发配置 |

---

## 5. 实施计划

### 5.1 子项目分解

| 子项目 | 范围 | 依赖 | 预估工期 |
|--------|------|------|----------|
| **A: 基础设施** | property-mapping.json, cache-query.py, adapter-nfmd.py, write-ref-value.py, DB schema 迁移 | 无 | 2-3 天 |
| **B: 快线** | librarian-search SKILL, librarian-extract SKILL, nucpot-librarian agent | A | 2-3 天 |
| **C: 慢线** | cron job, llm-wiki + ontofuel 集成, 回填机制 | A | 1-2 天 |
| **D: 编排集成** | ref-gap-fill SKILL.md 重构, nucpot-db agent, 端到端测试 | A+B+C | 1-2 天 |

**执行顺序：A → B/C 并行 → D**  
**总预估：6-10 天**（复用现有资产后比原计划节省约 40%）

### 5.2 里程碑

| 里程碑 | 交付物 | 预期效果 |
|--------|--------|----------|
| M1: 基础设施就绪 | property-mapping + cache-query + adapters | 三级缓存可查询，L2/L3 数据可通过 API 写入 L1 |
| M2: 快线跑通 | librarian 搜索+提取 U-Mo 缺口 | 首次端到端自动化补全参考值 |
| M3: 慢线上线 | cron + 消化 + 回填 | 知识库持续积累，缓存命中率逐步提升 |
| M4: 系统集成 | 完整多智能体编排 | reference_values 达到 100+ 条 |

---

## 6. 消息接口协议

所有智能体间通信使用 JSON，通过 OpenClaw `sessions_send` / `sessions_spawn` 传递：

| 消息 | 方向 | 关键字段 |
|------|------|----------|
| `GapRequest` | 验证服务 → nucpot-db | element_system, phase, properties[], preferred_method, priority |
| `GapList` | nucpot-db → nucpot-librarian | 缓存未命中的缺口列表 + 已命中数据 |
| `SearchResult` | nucpot-librarian → nucpot-db | 提取结果 (value, unit, method, source, confidence) + 处理的文献 + 失败缺口 |
| `DataSet` | nucpot-db → 验证服务 | 完整/部分数据集 + 缓存命中统计 + 剩余缺口 |

---

## 7. 质量保障

| 维度 | 措施 |
|------|------|
| 数据准确性 | 范围检查（lattice 2-6Å, Cij 10-600GPa）+ 多源交叉验证 |
| 数据追溯 | 每条记录必须有 source (作者/年份/期刊) + DOI |
| 写入安全 | 去重检查 + 分级写入 (high auto / medium-low 待审) + nfmd-db-ops 安全规则 |
| 系统可靠 | 快线失败不阻塞返回 partial DataSet + 慢线断点续传 |
| 可观测性 | 每次 GapRequest 记录日志 (命中率/耗时/来源) + 缓存命中率统计 |

---

## 8. 待专家审查事项

### 8.1 技术方案

1. **三级缓存设计是否合理？** L1 (reference_values) → L2 (NFMD) → L3 (llm-wiki + ontofuel)，这个优先级顺序是否符合实际数据质量和可靠性？
2. **物性映射表 (property-mapping.json) 是否完整？** 当前覆盖 12 种物性，是否需要补充？
3. **LLM 提取的准确性如何保障？** 当前方案依赖 prompt engineering + 范围检查 + confidence 分级，是否需要更严格的验证机制（如人工抽检比例）？
4. **ontofuel 本体扩展的优先级？** 缺少 C11/C12/C44/C33 属性定义，是否应在 Phase A 中一并解决还是后续单独处理？

### 8.2 数据策略

5. **DFT vs 实验值的优先级？** 势函数验证主要对比 DFT 值，但实验值作为交叉验证。是否需要区分存储和展示？
6. **L2 (NFMD) 数据质量是否足够？** NFMD 中部分参数来源不明确（如 "Experiment" 无具体引用），直接映射到 reference_values 是否需要额外的质量过滤？
7. **llm-wiki 参数的中文命名问题？** 68 条可用参数全是中文命名，adapter 映射可能引入歧义。是否应在 llm-wiki 层面就改用英文命名？

### 8.3 工程实施

8. **智能体数量是否合适？** 当前设计 3 个角色（nucpot-db / nucpot-librarian / researcher），是否需要进一步拆分或合并？
9. **慢线频率？** 每周一次是否合适？是否应根据缺口数量动态调整？
10. **与验证服务的集成方式？** 当前验证服务 (FastAPI) 通过 API 读写 reference_values，势函数网站智能体是否需要独立 agent？

---

## 9. 产出物索引

| 文件 | 说明 |
|------|------|
| `docs/prd-ref-gap-fill.md` | 产品需求文档 (初版) |
| `docs/superpowers/specs/2026-05-29-ref-gap-fill-design.md` | 详细设计规格 (含消息 schema、文件清单、错误处理) |
| `docs/ref-gap-fill-progress.md` | 本文件 — 阶段性进展总结 |
| `~/.openclaw/skills/ref-gap-fill/SKILL.md` | 现有 ref-gap-fill 技能 (待重构) |
| `~/.openclaw/skills/ref-gap-fill/test-prompts.json` | darwin-skill 测试用例 |

---

## 10. 下一步

1. **专家审查**：本文件提交审查，收集反馈
2. **更新 spec**：根据审查意见修改设计规格
3. **实施 Phase A**：按 Superpowers writing-plans 写详细实施计划，subagent-driven-development 执行
4. **端到端验证**：以 U-Mo BCC 缺口作为首个测试 case
