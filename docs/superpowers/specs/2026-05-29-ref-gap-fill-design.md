# Ref-Gap-Fill 多智能体参考值补全系统 — Design Spec

> **For agentic workers:** This spec follows Superpowers brainstorming → writing-plans → subagent-driven-development workflow.

**Goal:** 构建多智能体协作系统，自动化势函数验证参考值补全，同时通过慢线持续积累知识库以减少未来缺口。

**Architecture:** 三级缓存查询 + 快慢线分离。势函数网站提交数据需求 → 数据库智能体三级缓存查询 → 未命中派发快线（搜索智能体搜索/提取）→ 慢线异步消化文献并回填缓存。数据库智能体负责组装完整数据集返回。

**Tech Stack:** OpenClaw agents + skills、PostgreSQL (reference_values)、Supabase (NFMD parameters)、MinerU (PDF 解析)、LLM (物性提取)、Zotero MCP (文献管理)、ontofuel (本体提取)、llm-wiki (知识库)

---

## 设计决策（已确认）

| # | 决策 | 选择 | 理由 |
|---|------|------|------|
| Q1 | 智能体映射 | 新建 nucpot-db + nucpot-librarian agent | main 专注调度，职责分离 |
| Q2 | 慢线触发 | 混合：快线标记 + cron 批量消化 | 不阻塞快线，批量效率高 |
| Q3 | 写入策略 | 分级：high 自动 / medium-low 标记 needs_review | 平衡自动化与数据质量 |
| Q4 | 数据存储 | 本地 PG 为主，慢线双写到 NFMD | 快线快写，慢线全面同步 |

---

## 1. 系统架构

### 1.1 智能体拓扑

```
main (调度者)
  │
  ├─ sessions_send → nucpot-db (数据库智能体)
  │                     │
  │                     ├─ 三级缓存查询 (同步)
  │                     │   L1: reference_values (本地 PG)
  │                     │   L2: NFMD parameters (Supabase)
  │                     │   L3: llm-wiki params + ontofuel 本体
  │                     │
  │                     ├─ 快线 (同步，有超时)
  │                     │   sessions_spawn → nucpot-librarian
  │                     │     ├─ 搜索 (Zotero → Semantic Scholar → Web)
  │                     │     ├─ 获取 (PDF 下载 → Zotero)
  │                     │     ├─ 解析 (MinerU → Markdown)
  │                     │     ├─ 提取 (LLM → RefValue JSON)
  │                     │     └─ 标记待消化 (写入 Zotero tag)
  │                     │
  │                     ├─ 慢线 (异步，cron 触发)
  │                     │   sessions_spawn → researcher (子 agent)
  │                     │     ├─ llm-wiki ingest (summary + params)
  │                     │     ├─ ontofuel extraction (本体更新)
  │                     │     └─ 回填 L1 + L2 + L3
  │                     │
  │                     └─ 验证 + 组装 DataSet → 返回 main
  │
  └─ 结果转交势函数验证服务
```

### 1.2 OpenClaw Agent 配置

需要新增 2 个 agent 到 `openclaw.json`：

#### nucpot-db（数据库智能体）

```jsonc
{
  "id": "nucpot-db",
  "skills": ["ref-gap-fill", "nfmd-db-ops", "nfmd-development"],
  "tools": {
    "profile": "minimal",
    "alsoAllow": [
      "exec", "process", "read", "write", "edit",
      "web_search", "web_fetch",
      "memory_search", "memory_get",
      "sessions_spawn", "sessions_yield", "subagents",
      "message", "llm-task",
      // NFMD Supabase
      "feishu_bitable_app", "feishu_bitable_app_table",
      "feishu_bitable_app_table_record",
      // 飞书通知
      "feishu_im_user_message",
      // 数据库 SSH
      "gateway"
    ]
  }
}
```

#### nucpot-librarian（搜索智能体）

```jsonc
{
  "id": "nucpot-librarian",
  "skills": ["librarian-search", "librarian-extract"],
  "tools": {
    "profile": "minimal",
    "alsoAllow": [
      "exec", "process", "read", "write", "edit",
      "web_search", "web_fetch",
      "memory_search", "memory_get",
      "browser",
      "image",
      "llm-task",
      "sessions_spawn", "sessions_yield", "subagents",
      "message"
    ]
  }
}
```

### 1.3 数据流

```
GapRequest (JSON)
  │
  ▼
nucpot-db: 三级缓存查询
  │
  ├─ 全部命中 → 组装 DataSet 返回（≤ 5s）
  │
  ├─ 部分命中 → 已有数据 + GapList
  │
  └─ 全部未命中 → GapList = GapRequest
        │
        ▼
nucpot-db: sessions_spawn → nucpot-librarian
  │
  │  nucpot-librarian 内部流程:
  │  1. 搜索 (Zotero → S2 → Web) → 候选文献
  │  2. 获取 PDF → 存入 Zotero → 本地路径
  │  3. 解析 (MinerU) → Markdown
  │  4. 提取 (LLM) → RefValue JSON
  │  5. 标记待消化 (Zotero tag: "pending-slowlane")
  │
  ▼
nucpot-db: 验证提取结果
  │
  ├─ quality gate: range check + dedup + source required
  │
  ├─ confidence=high → 直接写入 reference_values
  ├─ confidence=medium/low → 写入 reference_values (needs_review=true)
  │
  ▼
组装 DataSet 返回
```

---

## 2. 三级缓存

### 2.1 缓存层级

| 级别 | 数据源 | 位置 | 查询方式 | 预期命中率 |
|------|--------|------|----------|-----------|
| L1 | `reference_values` 表 | ThinkStation PG `nucpot` | SQL `SELECT` | 20-30%（初始数据少） |
| L2 | NFMD `parameters` 表 | Supabase `100.65.135.2:54321` | SQL via SSH tunnel | 30-40%（6981 条记录） |
| L3 | llm-wiki params + ontofuel 本体 | 本地文件 | `memory_search` + JSON scan | 10-15% |

### 2.2 查询逻辑

```python
def cache_query(gap: GapItem) -> Optional[RefValue]:
    # L1: 直接查 reference_values
    result = query_local_pg(
        "SELECT * FROM reference_values "
        "WHERE element_system = %s AND property = %s AND phase = %s",
        [gap.element_system, gap.property, gap.phase]
    )
    if result:
        return adapt_l1(result)

    # L2: 查 NFMD parameters（通过 property-mapping 映射）
    mapping = load_property_mapping()
    nfmd_names = mapping.get_nfmd_names(gap.property)
    for name in nfmd_names:
        result = query_supabase(
            "parameters", 
            {"material_raw": f"ilike.%{gap.element_system}%",
             "name": f"ilike.%{name}%"}
        )
        if result:
            return adapt_nfmd_to_ref(result, gap)

    # L3: llm-wiki params + ontofuel 本体
    # L3a: llm-wiki parameters JSON
    wiki_params = search_wiki_params(gap.element_system, gap.property)
    if wiki_params:
        return adapt_wiki_to_ref(wiki_params, gap)

    # L3b: ontofuel 本体 individuals
    onto_props = query_ontology(gap.element_system, gap.property)
    if onto_props:
        return adapt_ontology_to_ref(onto_props, gap)

    return None  # 未命中，加入 GapList
```

### 2.3 物性映射表

文件路径: `data/property-mapping.json`

```jsonc
{
  "version": 1,
  "mappings": [
    {
      "ref_property": "lattice_constant",
      "ref_unit": "angstrom",
      "nfmd_names": ["lattice parameter", "lattice constant", "a0", "lattice parameter a"],
      "nfmd_symbols": ["a", "a0", "a_lat"],
      "ontofuel_keys": ["latticeConstant"],
      "range": {"min": 2.0, "max": 6.5}
    },
    {
      "ref_property": "cohesive_energy",
      "ref_unit": "eV/atom",
      "nfmd_names": ["cohesive energy"],
      "nfmd_symbols": ["E_coh", "E_c"],
      "ontofuel_keys": [],
      "range": {"min": -10.0, "max": 0.0}
    },
    {
      "ref_property": "C11",
      "ref_unit": "GPa",
      "nfmd_names": ["elastic constant C11", "C11"],
      "nfmd_symbols": ["C11", "c11"],
      "ontofuel_keys": [],
      "range": {"min": 10, "max": 600}
    },
    {
      "ref_property": "C12",
      "ref_unit": "GPa",
      "nfmd_names": ["elastic constant C12", "C12"],
      "nfmd_symbols": ["C12", "c12"],
      "ontofuel_keys": [],
      "range": {"min": 5, "max": 400}
    },
    {
      "ref_property": "C44",
      "ref_unit": "GPa",
      "nfmd_names": ["elastic constant C44", "C44"],
      "nfmd_symbols": ["C44", "c44"],
      "ontofuel_keys": [],
      "range": {"min": 5, "max": 400}
    },
    {
      "ref_property": "C33",
      "ref_unit": "GPa",
      "nfmd_names": ["elastic constant C33", "C33"],
      "nfmd_symbols": ["C33", "c33"],
      "ontofuel_keys": [],
      "range": {"min": 10, "max": 600}
    },
    {
      "ref_property": "bulk_modulus",
      "ref_unit": "GPa",
      "nfmd_names": ["bulk modulus", "isothermal bulk modulus"],
      "nfmd_symbols": ["B", "K", "B0"],
      "ontofuel_keys": [],
      "range": {"min": 10, "max": 400}
    },
    {
      "ref_property": "vacancy_formation_energy",
      "ref_unit": "eV",
      "nfmd_names": ["vacancy formation energy"],
      "nfmd_symbols": ["E_vf", "E_vac"],
      "ontofuel_keys": [],
      "range": {"min": 0.5, "max": 5.0}
    },
    {
      "ref_property": "formation_energy",
      "ref_unit": "eV/atom",
      "nfmd_names": ["formation energy", "enthalpy of formation"],
      "nfmd_symbols": ["E_f", "ΔH_f"],
      "ontofuel_keys": ["formationEnergy"],
      "range": {"min": -2.0, "max": 2.0}
    },
    {
      "ref_property": "surface_energy",
      "ref_unit": "J/m²",
      "nfmd_names": ["surface energy"],
      "nfmd_symbols": ["γ", "E_surf"],
      "ontofuel_keys": [],
      "range": {"min": 0.5, "max": 5.0}
    },
    {
      "ref_property": "melting_point",
      "ref_unit": "K",
      "nfmd_names": ["melting point", "melting temperature"],
      "nfmd_symbols": ["T_m", "T_melt"],
      "ontofuel_keys": ["meltingPoint"],
      "range": {"min": 300, "max": 4500}
    },
    {
      "ref_property": "thermal_conductivity",
      "ref_unit": "W/m·K",
      "nfmd_names": ["thermal conductivity"],
      "nfmd_symbols": ["κ", "k", "λ"],
      "ontofuel_keys": ["thermalConductivity"],
      "range": {"min": 0.1, "max": 500}
    }
  ]
}
```

---

## 3. 快线设计

### 3.1 搜索智能体 (nucpot-librarian)

**搜索策略（按优先级）：**

1. **Zotero 本地库** — `zotero-ontology-research` 技能，关键词 + 语义搜索
2. **llm-wiki 已有摘要** — `memory_search`，可能已消化过的文献包含目标物性
3. **Semantic Scholar API** — `web_fetch` 调用 S2 API，筛选含物性数据的论文
4. **Web 搜索** — `web_search`，兜底

**搜索 query 生成模板：**

```
"{element_system} {phase} {property} {preferred_method}"
"{element_system} elastic constants {method} first principles"
"{element_system} lattice parameter DFT"
```

**获取策略：**

1. Zotero 已有 PDF → 直接用本地路径
2. OA 论文 → Semantic Scholar PDF URL → `exec: wget`
3. 非 OA → 标记为 `access_blocked`，通知 nucpot-db 请求人工协助
4. 每篇获取的文献都存入 Zotero（如果不在）

### 3.2 提取流程

```
PDF → MinerU 解析 → Markdown (保留表格和公式)
                        │
                        ▼
              LLM 提取 Prompt → RefValue JSON
                        │
                        ▼
              单位标准化 + 范围检查
                        │
                        ▼
              标记 confidence (high/medium/low)
                        │
                        ▼
              标记 Zotero tag: "pending-slowlane"
```

**LLM 提取 Prompt：**

```
System: 你是核材料物性数据提取专家。从文献内容中提取指定体系的物性参考值。

目标体系：{element_system}
目标相：{phase}
目标性质：{properties}
温度条件：{temperature_k} K

要求：
1. 每个性质提取所有可用值（不同方法/条件的分别列出）
2. 包含：value, unit, method, temperature, source_location
3. 数值保留原文精度，不做近似
4. 未给出的字段设为 null
5. 标注置信度：
   - high：明确表格/正文数值
   - medium：图表估算
   - low：间接推算

输出 JSON 数组，每个元素包含：
element_system, phase, property, value, unit, uncertainty,
temperature, method, source, source_doi, confidence, extraction_note
```

### 3.3 质量门控

| 检查 | 规则 | 不通过处理 |
|------|------|-----------|
| 数值范围 | 对照 `property-mapping.json` 中的 range | 标记 `needs_review` |
| 单位一致性 | 同一 property 必须可转换为标准单位 | 自动转换或标记 |
| 来源追溯 | 必须有 source（作者/年份/期刊） | 拒绝写入 |
| 去重 | `(element_system, phase, property, method, source)` 唯一 | 跳过已存在记录 |
| confidence | high/medium/low | high→自动写入，medium/low→标记 `needs_review` |

### 3.4 写入策略

```python
def write_ref_value(extracted: RefValue, config: WriteConfig):
    # 质量门控
    if not passes_quality_gate(extracted):
        return WriteResult(status="rejected", reason=gate_failure_reason)
    
    # 去重检查
    if exists_in_reference_values(extracted):
        return WriteResult(status="duplicate", note="skipped")
    
    # 分级写入
    if extracted.confidence == "high":
        insert_reference_value(extracted, needs_review=False)
        return WriteResult(status="written_auto")
    else:
        insert_reference_value(extracted, needs_review=True)
        return WriteResult(status="written_pending_review")
```

### 3.5 nucpot-librarian 技能

需要创建两个技能文件：

**`librarian-search/SKILL.md`** — 搜索 + 获取
**`librarian-extract/SKILL.md`** — 解析 + 提取

---

## 4. 慢线设计

### 4.1 触发机制

1. **快线标记** — nucpot-librarian 处理完文献后，在 Zotero 中添加 tag `pending-slowlane`
2. **cron 定时** — 每周触发一次（建议周一 09:00 CST），nucpot-db 扫描 Zotero 中带 `pending-slowlane` tag 的文献
3. **手动触发** — main 通过 `sessions_send` 向 nucpot-db 发送慢线启动指令

### 4.2 慢线流程

```
nucpot-db (cron 或手动触发)
  │
  ├─ 扫描 Zotero pending-slowlane 文献
  │
  ├─ sessions_spawn → researcher (子 agent)
  │     │
  │     ├─ llm-wiki ingest:
  │     │   PDF → summary.md → parameters/*.json
  │     │   validate_params.py 质量检查
  │     │
  │     ├─ ontofuel extraction:
  │     │   PDF → 章节 → LLM 提取 → individuals
  │     │   → 合并去重 → 本体增量更新
  │     │
  │     └─ 返回提取结果
  │
  ├─ 回填三级缓存:
  │   L1: 提取的物性值 → reference_values
  │   L2: 提取的物性值 → NFMD parameters (via nfmd-db-ops)
  │   L3a: summary + params → llm-wiki knowledge base (自动)
  │   L3b: individuals → ontofuel 本体 (自动)
  │
  └─ 清除 Zotero pending-slowlane tag
```

### 4.3 慢线 Cron 配置

```jsonc
{
  "name": "slowlane-weekly-digest",
  "schedule": {
    "kind": "cron",
    "expr": "0 9 * * 1",
    "tz": "Asia/Shanghai"
  },
  "sessionTarget": "isolated",
  "payload": {
    "kind": "agentTurn",
    "message": "慢线周任务：扫描 Zotero 中 pending-slowlane 标记的文献，依次用 llm-wiki ingest 和 ontofuel extraction 消化，提取的物性值回填到 reference_values 和 NFMD。遵循 ref-gap-fill 技能中的慢线流程。完成后清除标记并报告。",
    "toolsAllow": ["exec", "read", "write", "edit", "web_search", "web_fetch", "memory_search", "memory_get", "message", "sessions_spawn", "sessions_yield"]
  }
}
```

### 4.4 慢线回填 L2 (NFMD) 的数据格式

慢线产出的参数需要适配 NFMD `parameters` 表的 schema：

```jsonc
{
  "id": "uuid-string",
  "name": "elastic constant C11",
  "name_zh": "弹性常数 C11",
  "symbol": "C11",
  "category": "elastic_properties",
  "value_type": "scalar",
  "value_scalar": 286.0,
  "unit": "GPa",
  "material_raw": "U-Mo",
  "temperature_k": 0,
  "method": "DFT (PBE)",
  "confidence": "high",
  "source_file": "summaries/hu-2016-jnm.md"
}
```

---

## 5. 接口协议

### 5.1 消息 Schema

所有智能体间通信使用 JSON，通过 `sessions_send` / `sessions_spawn` 传递。

#### GapRequest

```jsonc
{
  "schema": "ref-gap-fill/GapRequest/v1",
  "request_id": "uuid-v4",
  "timestamp": "ISO-8601",
  "caller": "main",
  "items": [
    {
      "element_system": "U-Mo",        // required
      "phase": "BCC",                   // optional, inferred if null
      "properties": [                   // required, from property-mapping.json
        "lattice_constant", "C11", "C12", "C44", "cohesive_energy"
      ],
      "preferred_method": "DFT",        // DFT | experimental | any
      "temperature_k": 0,               // optional, default 0
      "priority": "high"                // high | normal | low
    }
  ]
}
```

#### GapList

```jsonc
{
  "schema": "ref-gap-fill/GapList/v1",
  "request_id": "uuid-v4",
  "parent_request_id": "uuid-v4",
  "cached_results": [ /* RefValue[] — 缓存命中的数据 */ ],
  "gaps": [
    {
      "element_system": "U-Mo",
      "phase": "BCC",
      "property": "C44",
      "preferred_method": "DFT",
      "temperature_k": 0,
      "priority": "high"
    }
  ]
}
```

#### SearchResult

```jsonc
{
  "schema": "ref-gap-fill/SearchResult/v1",
  "gap_list_id": "uuid-v4",
  "status": "complete" | "partial" | "failed",
  "results": [
    {
      "element_system": "U-Mo",
      "phase": "BCC",
      "property": "C44",
      "value": 73.0,
      "unit": "GPa",
      "uncertainty": null,
      "temperature": 0,
      "method": "DFT (PBE)",
      "source": "Hu et al., 2016, J. Nucl. Mater.",
      "source_doi": "10.1016/j.jnucmat.2016.xxxxx",
      "confidence": "high",
      "extraction_note": "Table 3, Row 5"
    }
  ],
  "papers_processed": [
    {
      "doi": "10.1016/j.jnucmat.2016.xxxxx",
      "title": "...",
      "stored_in_zotero": true,
      "pdf_path": "/path/to/pdf",
      "slowlane_tagged": true
    }
  ],
  "failed_gaps": [
    {
      "element_system": "U-Pu-Zr",
      "property": "C44",
      "reason": "no_papers_found" | "access_blocked" | "extraction_failed"
    }
  ]
}
```

#### DataSet

```jsonc
{
  "schema": "ref-gap-fill/DataSet/v1",
  "request_id": "uuid-v4",
  "status": "complete" | "partial" | "failed",
  "stats": {
    "total_requested": 5,
    "from_cache": 3,
    "from_express": 1,
    "gaps_remaining": 1
  },
  "data": [
    {
      "element_system": "U-Mo",
      "phase": "BCC",
      "property": "lattice_constant",
      "value": 3.39,
      "unit": "angstrom",
      "method": "DFT (PBE)",
      "source": "Smirnov 2014, JNM",
      "source_doi": "10.xxxx",
      "confidence": "high",
      "cache_level": "L1",
      "needs_review": false
    }
  ],
  "gaps": [
    {
      "element_system": "U-Mo",
      "phase": "BCC",
      "property": "C44",
      "status": "no_papers_found",
      "note": "快线未找到相关文献，建议慢线关注"
    }
  ]
}
```

---

## 6. ref-gap-fill 技能设计

### 6.1 技能文件结构

```
~/.openclaw/skills/ref-gap-fill/
  SKILL.md                    # 编排协议（重写）
  test-prompts.json           # darwin-skill 测试用例
  data/
    property-mapping.json     # 物性映射表
```

### 6.2 SKILL.md 核心内容

技能不再是 monolithic pipeline，而是**编排协议**：

1. **接收 GapRequest** — 解析需求清单
2. **三级缓存查询** — L1 → L2 → L3
3. **生成 GapList** — 未命中的缺口
4. **派发快线** — `sessions_spawn` → nucpot-librarian
5. **等待结果** — `sessions_yield`
6. **验证 + 分级写入** — 质量门控 + confidence 分级
7. **组装 DataSet** — 缓存数据 + 快线数据
8. **返回** — 给调用者

快线和慢线的具体流程分别在 `librarian-search`、`librarian-extract` 技能中定义。

---

## 7. 文件清单

### 7.1 新建文件

| 文件 | 用途 | 所属子项目 |
|------|------|-----------|
| `data/property-mapping.json` | 物性映射表 (L1↔L2↔L3) | A |
| `scripts/cache-query.py` | 三级缓存统一查询脚本 | A |
| `scripts/adapter-nfmd.py` | NFMD parameters → reference_values 适配器 | A |
| `scripts/adapter-wiki.py` | llm-wiki params → reference_values 适配器 | A |
| `scripts/adapter-ontology.py` | ontofuel individuals → reference_values 适配器 | A |
| `scripts/write-ref-value.py` | 分级写入脚本 (质量门控 + 去重) | A |
| `~/.openclaw/skills/librarian-search/SKILL.md` | 搜索+获取技能 | B |
| `~/.openclaw/skills/librarian-extract/SKILL.md` | 解析+提取技能 | B |
| `~/.openclaw/skills/ref-gap-fill/SKILL.md` | 重写为编排协议 | D |

### 7.2 修改文件

| 文件 | 修改内容 | 所属子项目 |
|------|----------|-----------|
| `openclaw.json` | 新增 nucpot-db + nucpot-librarian agent | D |

### 7.3 现有文件（只读引用）

| 文件 | 用途 |
|------|------|
| `~/.openclaw/skills/nfmd-db-ops/SKILL.md` | 数据库安全规则 |
| `~/.openclaw/skills/nfmd-development/SKILL.md` | NFMD 开发规则 |
| `~/.openclaw/workspace-extractor/src/ontofuel/` | ontofuel Python API |
| `~/.openclaw/workspace/skills/SKILL.md` | llm-wiki 技能 |

---

## 8. 错误处理

| 错误场景 | 处理方式 |
|----------|----------|
| L1 查询失败 (PG 不可达) | 降级到 L2，记录告警 |
| L2 查询失败 (Supabase 不可达) | 降级到 L3，记录告警 |
| 快线搜索无结果 | 标记 `no_papers_found`，返回 partial DataSet |
| PDF 获取失败 (非 OA) | 标记 `access_blocked`，通知 main 请求人工 |
| PDF 解析失败 | 降级到 pdftotext，仍失败则标记 `parse_failed` |
| LLM 提取空结果 | 标记 `extraction_failed`，不写入空数据 |
| API 写入失败 | 重试 1 次，仍失败记录错误日志 |
| 慢线 cron 超时 | 标记当前文献处理中断，下次 cron 从断点续传 |

---

## 9. 安全

- 所有 NFMD 数据库操作遵循 `nfmd-db-ops` 技能安全规则
- 禁止 TRUNCATE / DROP TABLE / 无 WHERE 的 DELETE
- 写入前必须去重检查
- `needs_review=true` 的数据不在验算中使用（API 查询时默认 `WHERE needs_review = false OR needs_review IS NULL`）
- 需要给 reference_values 表新增 `needs_review` 列（BOOLEAN DEFAULT false）

```sql
ALTER TABLE reference_values ADD COLUMN needs_review BOOLEAN DEFAULT false;
```

---

## 10. 可观测性

### 10.1 日志

每次 GapRequest 处理记录到 `data/ref-logs/YYYY-MM-DD.json`：

```jsonc
{
  "request_id": "uuid",
  "timestamp": "ISO-8601",
  "items_requested": 5,
  "cache_hits": { "L1": 2, "L2": 1, "L3": 0 },
  "express_results": 1,
  "gaps_remaining": 1,
  "duration_seconds": 145,
  "slowlane_tagged_papers": 2
}
```

### 10.2 统计指标

- 缓存命中率（按 L1/L2/L3 分别统计）
- 快线平均响应时间
- 慢线每周消化文献数
- reference_values 总记录数趋势
- needs_review 待审核数量

---

## 11. 子项目分解

按 Superpowers brainstorming 要求，本系统分解为 4 个独立子项目，每个有完整的 spec → plan → implementation 周期：

| 子项目 | 范围 | 依赖 | 预估 |
|--------|------|------|------|
| **A: 基础设施** | property-mapping.json, cache-query.py, 3 个 adapter, write-ref-value.py, DB schema 迁移 | 无 | 3-4 天 |
| **B: 快线** | librarian-search SKILL.md, librarian-extract SKILL.md, nucpot-librarian agent 配置 | A | 3-5 天 |
| **C: 慢线** | cron job 配置, 慢线流程集成 (llm-wiki + ontofuel + 回填) | A | 2-3 天 |
| **D: 编排层** | ref-gap-fill SKILL.md 重写, nucpot-db agent 配置, openclaw.json 更新, 端到端测试 | A + B + C | 2-3 天 |

**执行顺序：A → B/C 并行 → D**

A 是基础设施，B 和 C 都依赖 A 但彼此独立可并行，D 依赖前三者做最终集成。
