# ref-gap-fill — 参考值补全系统

> PARA: Project | 父项目: [NucPot](./README.md)

## 基本信息

- **类型**: 多智能体自动化系统
- **状态**: Design Phase Complete (v0.1) — 待专家审查
- **开始日期**: 2026-05-29
- **目标截止**: 2026-06-10 (预估 6-10 天实施)

## 问题陈述

NucPot 势函数验证服务依赖 `reference_values` 表，但仅 23 条记录覆盖 5 个体系。实际需 14+ 体系 × 8+ 物性 ≈ 100+ 条。手动补充不可持续。

## 设计方案

**多智能体协作 + 快慢线分离：**
- **数据库智能体** (nucpot-db): 三级缓存查询 + 编排
- **搜索智能体** (nucpot-librarian): 快线搜索/提取
- **慢线**: cron 每周消化文献，回填缓存

**三级缓存**: L1 reference_values (23条) → L2 NFMD (6981条) → L3 llm-wiki + ontofuel

## 文件索引

### 设计文档（本目录）

| 文件 | 说明 |
|------|------|
| `prd-ref-gap-fill.md` | 产品需求文档 v1.0 (22KB) |
| `ref-gap-fill-progress.md` | 阶段性进展总结 + 10 个待审查问题 (11KB) |
| `design-spec.md` | 详细设计规格，含消息 schema + 文件清单 (23KB) |

> 注：设计规格原始文件在 `docs/superpowers/specs/2026-05-29-ref-gap-fill-design.md`，此处为 PARA 归档副本。

### 关联技能文件（只读引用）

| 文件 | 说明 |
|------|------|
| `~/.openclaw/skills/ref-gap-fill/SKILL.md` | 现有技能 (待重构为编排协议) |
| `~/.openclaw/skills/ref-gap-fill/test-prompts.json` | darwin-skill 测试用例 |

### 关联代码/数据（只读引用）

| 文件 | 说明 |
|------|------|
| `projects/2026-Q2-database-platform/sql/current_schema_dump.sql` | NFMD schema |
| `skills/llm-wiki/pipeline/*.lobster` | 可复用的 Lobster 工作流 |
| `skills/llm-wiki/scripts/zotero_sync.py` | Zotero 同步脚本 |
| `workspace-extractor/src/ontofuel/` | ontofuel Python API |

## 关键决策

| # | 决策 | 选择 | 确认日期 |
|---|------|------|----------|
| Q1 | 智能体架构 | 新建 nucpot-db + nucpot-librarian | 2026-05-29 |
| Q2 | 慢线触发 | 混合：快线标记 + cron 批量 | 2026-05-29 |
| Q3 | 写入策略 | 分级：high auto / medium-low 待审 | 2026-05-29 |
| Q4 | 数据存储 | 本地 PG 为主，慢线双写 NFMD | 2026-05-29 |

## 实施计划

| 子项目 | 范围 | 预估 | 依赖 |
|--------|------|------|------|
| A: 基础设施 | property-mapping, cache-query, adapters, write-ref-value | 2-3d | 无 |
| B: 快线 | librarian-search/extract SKILL, nucpot-librarian agent | 2-3d | A |
| C: 慢线 | cron, llm-wiki + ontofuel 集成, 回填 | 1-2d | A |
| D: 编排集成 | ref-gap-fill SKILL 重构, nucpot-db agent, E2E 测试 | 1-2d | A+B+C |

**执行顺序: A → B/C 并行 → D**

## 可复用资产

详见 → [../resources/ref-gap-fill-reuse-audit.md]

## 里程碑

- [ ] M1: 基础设施就绪 (property-mapping + cache-query + adapters)
- [ ] M2: 快线跑通 (U-Mo BCC 缺口端到端)
- [ ] M3: 慢线上线 (cron + 消化 + 回填)
- [ ] M4: 系统集成 (reference_values 达 100+ 条)

## 下一步

1. 提交专家审查 → 收集反馈
2. 更新 spec
3. 按 Superpowers writing-plans 写实施计划
4. 按 subagent-driven-development 执行 Phase A
