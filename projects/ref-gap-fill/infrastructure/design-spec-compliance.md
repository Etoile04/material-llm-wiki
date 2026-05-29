# Design Spec 符合性评估

> 评估日期: 2026-05-30 | 评估基准: `docs/superpowers/specs/2026-05-29-ref-gap-fill-design.md`

## 总体评分: 75% (A+B+D 完成, C 待实现)

---

## 逐节评估

### §1 系统架构 — 🟡 部分实现 (60%)

| 设计要求 | 实现状态 | 说明 |
|----------|---------|------|
| main 作为调度者 | ✅ | main agent 负责子智能体派发和协调 |
| nucpot-db 智能体 | ❌ | 未添加到 openclaw.json，当前由 main 代理执行 |
| nucpot-librarian 智能体 | ❌ | 未添加到 openclaw.json，当前由 subagent 代理执行 |
| 三级缓存查询 (L1→L2→L3) | ✅ | cache_query.py 完整实现 |
| 快线搜索+提取 | ✅ | librarian-search + librarian-extract 技能 |
| 慢线 (cron 触发) | ❌ | 未实现 cron job 和回填流程 |
| 验证 + 组装 DataSet | 🟡 | write_ref_value 实现质量门控，但无正式 DataSet 组装 |

### §2 三级缓存 — ✅ 完整实现 (95%)

| 设计要求 | 实现状态 | 说明 |
|----------|---------|------|
| L1: reference_values (本地 PG) | ✅ | cache_query.py + db_migrate.py |
| L2: NFMD parameters (Supabase) | ✅ | adapter_nfmd.py |
| L3a: llm-wiki params | ✅ | adapter_wiki.py |
| L3b: ontofuel 本体 | ✅ | adapter_ontology.py |
| property-mapping.json 12 物性 | ✅ | 12 物性全部覆盖，含范围校验 |
| 降级查询逻辑 | ✅ | L1→L2→L3 顺序，mockable |
| 查询接口 GapItem 输入 | ✅ | cache_query(element_system, phase, property) |

**偏差**: ontofuel 本体缺少 C11/C12/C44/C33 的 keys (设计规范中有 `ontofuel_keys: []`)，这是数据源限制而非代码问题。

### §3 快线设计 — ✅ 完整实现 (90%)

| 设计要求 | 实现状态 | 说明 |
|----------|---------|------|
| 搜索策略 (Zotero→S2→Web) | ✅ | librarian-search SKILL.md |
| 获取策略 (OA→非OA标记) | ✅ | librarian-search 包含获取流程 |
| MinerU 解析 | ✅ | librarian-extract 引用 MinerU |
| LLM 提取 Prompt | ✅ | librarian-extract 含完整 prompt 模板 |
| 质量门控 (5 项检查) | ✅ | write_ref_value.py |
| 分级写入 (high/medium/low) | ✅ | WriteStatus enum: WRITTEN_AUTO / WRITTEN_PENDING_REVIEW |
| 去重机制 | ✅ | (element_system, phase, property, method, source) 唯一 |

**偏差**: Zotero tag "pending-slowlane" 标记逻辑未实现 (属于慢线部分)。

### §4 慢线设计 — ❌ 未实现 (0%)

| 设计要求 | 实现状态 | 说明 |
|----------|---------|------|
| 慢线 cron job | ❌ | 未配置 |
| Zotero pending-slowlane 扫描 | ❌ | 未实现 |
| llm-wiki ingest 集成 | ❌ | 未集成 |
| ontofuel extraction 集成 | ❌ | 未集成 |
| 回填 L1+L2+L3 | ❌ | 未实现 |
| 清除 Zotero tag | ❌ | 未实现 |

### §5 接口协议 — 🟡 部分实现 (50%)

| 设计要求 | 实现状态 | 说明 |
|----------|---------|------|
| GapRequest schema | ❌ | 未定义正式 schema，通过函数参数传递 |
| GapList schema | 🟡 | gap_analyzer 输出 GapItem dataclass，非 JSON schema |
| SearchResult schema | ❌ | librarian 技能定义了输入输出格式，但无正式 JSON schema |
| DataSet schema | ❌ | 未实现正式组装和返回 |

**说明**: 当前实现是"脚本库"模式，各组件通过 Python 函数调用协作，而非设计规范中的 "JSON message passing via sessions_send" 模式。这对于 Phase A-D 的脚本层是合理的，但完整部署时需要 nucpot-db agent 实现 §5 的消息协议。

### §6 ref-gap-fill 技能设计 — ✅ 完成 (100%)

| 设计要求 | 实现状态 | 说明 |
|----------|---------|------|
| SKILL.md 重写为编排协议 | ✅ | 6.8KB, Phase 1-4 流程 |
| property-mapping.json | ✅ | 12 物性映射 |
| test-prompts.json | ❌ | 未创建 (非关键) |

### §7 文件清单 — ✅ 大部分完成 (90%)

| 设计要求 | 实现状态 |
|----------|---------|
| `data/property-mapping.json` | ✅ |
| `scripts/cache-query.py` | ✅ (命名 cache_query.py) |
| `scripts/adapter-nfmd.py` | ✅ (命名 adapter_nfmd.py) |
| `scripts/adapter-wiki.py` | ✅ (命名 adapter_wiki.py) |
| `scripts/adapter-ontology.py` | ✅ (命名 adapter_ontology.py) |
| `scripts/write-ref-value.py` | ✅ (命名 write_ref_value.py) |
| `librarian-search/SKILL.md` | ✅ |
| `librarian-extract/SKILL.md` | ✅ |
| `ref-gap-fill/SKILL.md` 重写 | ✅ |
| `scripts/gap_analyzer.py` | ✅ (设计规范未列出但实施计划中包含) |
| `scripts/db_migrate.py` | ✅ (设计规范未列出但实施计划中包含) |
| `openclaw.json` agent 配置 | ❌ |

**命名偏差**: 使用 snake_case 而非 kebab-case (Python 约定优先)。

### §8 错误处理 — 🟡 部分实现 (40%)

| 设计要求 | 实现状态 |
|----------|---------|
| L1 降级到 L2 | ✅ cache_query 顺序降级 |
| L2 降级到 L3 | ✅ |
| 搜索无结果标记 | ✅ librarian-search 输出 |
| PDF 获取失败标记 | ✅ librarian-extract 输出 |
| API 写入重试 | ❌ write_ref_value 当前不重试 |
| 慢线断点续传 | ❌ (慢线未实现) |
| 错误日志记录 | ❌ 无 data/ref-logs/ |

### §9 安全 — ✅ 实现 (85%)

| 设计要求 | 实现状态 |
|----------|---------|
| 遵循 nfmd-db-ops 安全规则 | ✅ (adapter 不直接写 NFMD) |
| 禁止 TRUNCATE/DROP | ✅ |
| 写入前去重 | ✅ write_ref_value |
| needs_review 列 | ✅ db_migrate 已添加 |

### §10 可观测性 — ❌ 未实现 (10%)

| 设计要求 | 实现状态 |
|----------|---------|
| 日志 (data/ref-logs/) | ❌ |
| 统计指标 | ❌ |
| 缓存命中率 | ❌ |
| 快线响应时间 | ❌ |

### §11 子项目分解 — 🟡 按计划执行 (75%)

| 子项目 | 设计要求 | 实际状态 |
|--------|---------|---------|
| A: 基础设施 | 3-4 天 | ✅ 1 天完成 |
| B: 快线 | 3-5 天 | ✅ 0.5 天完成 |
| C: 慢线 | 2-3 天 | ❌ 未开始 |
| D: 编排+验证 | 2-3 天 | ✅ 0.5 天完成 |

---

## 总结

### ✅ 已完成 (符合设计规范)
1. **三级缓存查询架构** — L1→L2→L3 完整实现，含降级逻辑
2. **12 物性映射** — property-mapping.json 完整覆盖
3. **3 个适配器** — NFMD/Wiki/Ontology 全部实现
4. **质量门控** — 范围检查 + 去重 + 分级写入
5. **快线技能** — 搜索+提取 SKILL.md
6. **编排协议** — ref-gap-fill SKILL.md 重写
7. **DB schema 迁移** — 已实际应用到 ThinkStation
8. **TDD 全流程** — 72 测试，零失败
9. **4 个设计决策** — 全部遵循

### ❌ 未完成 (偏离设计规范)
1. **慢线 (子项目 C)** — cron + Zotero tag + 回填完全未实现
2. **Agent 配置** — nucpot-db/nucpot-librarian 未添加到 openclaw.json
3. **消息协议** — §5 定义的 JSON schema 未正式实现
4. **可观测性** — 日志和统计指标未实现
5. **错误处理增强** — 写入重试、慢线断点续传未实现

### 📋 建议下一步
1. **实现慢线 (子项目 C)** — 这是设计规范的核心差异化特性
2. **添加 agent 配置** — openclaw.json 新增 nucpot-db + nucpot-librarian
3. **实现消息协议** — §5 JSON schema 标准化
4. **添加可观测性** — 日志记录 + 统计指标
5. **专家审查** — 提交当前进展给专家评审 M0.9
