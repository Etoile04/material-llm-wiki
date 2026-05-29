# ref-gap-fill — 参考值补全系统

**Project**: NucPot Phase 4 子项目
**Status**: 🟡 设计完成，待专家审查
**Priority**: P1 (阻塞验证服务质量)
**Started**: 2026-05-29
**Target**: 2026-06-10
**One-liner**: 多智能体协作系统，自动化补全势函数验证所需的 100+ 条参考物性值

## Milestones

- [x] M0: 现有 ref-gap-fill 技能基线评估 (9 维 rubric) — 2026-05-29
- [x] M0.5: 可复用资产盘点 + 架构设计 — 2026-05-29
- [x] M0.7: PRD v1.0 + 设计 spec — 2026-05-29
- [x] M0.8: PARA 整理归档 — 2026-05-29
- [ ] M0.9: 专家审查通过 — ~2026-06-02
- [ ] M1: 基础设施就绪 (property-mapping + cache-query + adapters) — ~2026-06-04
- [ ] M2: 快线跑通 (U-Mo BCC 端到端) — ~2026-06-06
- [ ] M3: 慢线上线 (cron + 消化 + 回填) — ~2026-06-08
- [ ] M4: 系统集成 (reference_values 达 100+ 条) — ~2026-06-10

## Progress Log

### 2026-05-29
- ref-gap-fill 技能基线评估完成（严重短板：失败模式编码 3/10、检查点设计 2/10）
- 现有技能生态盘点：ontofuel-extraction、ontology-driven-extraction、llm-wiki、nfmd-db-ops 等
- 多智能体协作架构设计：nucpot-db (数据库/编排) + nucpot-librarian (搜索/提取) + researcher (慢线消化)
- 快慢线分离设计：快线搜索→提取、慢线 llm-wiki + ontofuel 消化
- PRD v1.0 撰写完成 (22KB)
- Superpowers brainstorming 逐个确认 4 个关键决策：
  - Q1: 新建专用 agent (非复用 main)
  - Q2: 混合触发 (快线标记 + cron 批量)
  - Q3: 分级写入 (high auto / medium-low 待审)
  - Q4: 本地 PG 为主，慢线双写 NFMD
- 详细设计 spec 完成 (23KB)：消息 schema + 文件清单 + 错误处理 + 安全规则
- 可复用资产审计：9 项直接复用 + 3 项需适配 + 7 项新建，预估节省 40% 工期
- 数据资产盘点：L1 23条 / L2 6981条 / L3a 14320条(68条可用) / L3b 279属性
- PARA 整理归档完成 (notes/projects/nucpot/ + notes/resources/)
- 阶段性进展总结撰写完成，已发送给用户

## Decisions

| Date | Decision | Rationale |
|------|----------|-----------|
| 2026-05-29 | 新建 nucpot-db + nucpot-librarian agent | main 专注调度，职责分离 |
| 2026-05-29 | 混合触发（快线标记 + cron） | 不阻塞快线，批量效率高 |
| 2026-05-29 | 分级写入（high auto / medium-low 待审） | 平衡自动化与数据质量 |
| 2026-05-29 | 本地 PG 为主，慢线双写 NFMD | 快线快写，慢线全面同步 |
| 2026-05-29 | 不用 Lobster 硬编码 pipeline | 快慢线并行、缓存命中跳步，需要灵活编排 |

## Blockers

- 专家审查反馈 → 决定是否修改架构设计
- ontofuel 本体缺少 C11/C12/C44/C33 属性定义 → 需在 Phase A 中扩展

## Key Files

| File | Description |
|------|-------------|
| `docs/prd-ref-gap-fill.md` | PRD v1.0 (22KB) |
| `docs/superpowers/specs/2026-05-29-ref-gap-fill-design.md` | 详细设计 spec (23KB) |
| `docs/ref-gap-fill-progress.md` | 阶段性进展总结 (含 10 个待审查问题) |
| `notes/projects/nucpot/ref-gap-fill.md` | PARA 项目索引页 |
| `notes/resources/ref-gap-fill-reuse-audit.md` | 可复用资产审计 |
| `~/.openclaw/skills/ref-gap-fill/SKILL.md` | 现有技能 (待重构) |
