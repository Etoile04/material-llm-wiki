# ref-gap-fill — 参考值补全系统

> PARA: Project | 父项目: [NucPot](./README.md)

## 基本信息

- **类型**: 多智能体自动化系统
- **状态**: ✅ **项目关闭** — 219 条参考值入库，134/134 测试通过
- **开始日期**: 2026-05-29
- **关闭日期**: 2026-05-30

## 架构概览

```
验证服务 → GapRequest → nucpot-db (三级缓存 + 编排)
                              ├─ L1: reference_values (PG, 23条) → HIT: 返回
                              ├─ L2: NFMD parameters (15432, 43条) → HIT: 返回
                              ├─ L3: llm-wiki + ontofuel → HIT: 返回
                              └─ 全 MISS → 快线 (nucpot-librarian)
                                    搜索→提取→分级写入

慢线 (cron 每周一 09:00):
  Zotero 扫描 → llm-wiki ingest → ontofuel 提取 → 三级缓存回填
```

## 完成状态

| 里程碑 | 状态 | 说明 |
|--------|------|------|
| M1: 基础设施 | ✅ | 12 物性映射, 三级缓存, 6 适配器, 质量门控 |
| M2: 快线跑通 | ✅ | 9/9 功能测试通过, U-Mo C44 端到端验证 |
| M3: 慢线上线 | ✅ | 11/11 功能测试通过, cron 每周一触发 |
| M4: 全量覆盖 | ✅ | 219 条，38 个(体系,相)组合，14 体系 |

## 测试结果

- **单元测试**: 108/108 通过 (Phase 1: 72 + Phase 2: 36)
- **快线功能测试**: 9/9 通过
- **慢线功能测试**: 11/11 通过
- **PG UNIQUE 约束**: 已添加 `uq_ref_value_unique`

## 文件索引

### 项目管理 (projects/ref-gap-fill/)

| 文件 | 说明 |
|------|------|
| `STATE.json` | 项目状态机 |
| `DECISIONS.md` | 9 个设计决策 (D001-D009) |
| `WORK_LOG.md` | 每日工作日志 |
| `ISSUES.md` | 已知问题跟踪 |
| `SIGNALS.md` | 信号采集配置 |
| `README.md` | 项目说明 |
| `express-test-report.md` | 快线测试报告 |
| `slowlane-test-report.md` | 慢线测试报告 |

### 设计文档 (docs/superpowers/)

| 文件 | 说明 |
|------|------|
| `specs/2026-05-29-ref-gap-fill-design.md` | 详细设计规格 |
| `specs/2026-05-30-ref-gap-fill-phase2-design.md` | Phase 2 设计 |
| `specs/2026-05-30-express-functional-test-plan.md` | 快线测试方案 |
| `specs/2026-05-30-slowlane-functional-test-plan.md` | 慢线测试方案 |
| `plans/2026-05-30-ref-gap-fill-phase2-implementation.md` | Phase 2 实施计划 |

### 代码 (scripts/ + tests/)

| 文件 | 说明 |
|------|------|
| `scripts/property-mapping.json` | 12 物性映射 + 范围 |
| `scripts/gap_analyzer.py` | 缺口分析 |
| `scripts/cache_query.py` | 三级缓存查询 |
| `scripts/adapter_*.py` | 6 个适配器 (nfmd/wiki/ontology) |
| `scripts/write_ref_value.py` | 分级写入 |
| `scripts/db_migrate.py` | PG schema |
| `scripts/slowlane_backfill.py` | 慢线回填 |
| `scripts/ref_logger.py` | 日志记录 |
| `scripts/message_schemas.py` | 消息协议 |
| `tests/test_*.py` | 14 个测试文件, 108 tests |

## 关键决策

| # | 决策 | 选择 | 状态 |
|---|------|------|------|
| D001 | 智能体架构 | nucpot-db + nucpot-librarian | ✅ 已验证 |
| D002 | 慢线触发 | 快线标记 + cron 批量 | ✅ cron 已注册 |
| D003 | 写入策略 | 分级 (high/medium/low) | ✅ 已验证 |
| D004 | 数据存储 | 本地 PG + 慢线双写 NFMD | ✅ 双写验证 |
| D005 | llm-wiki 集成 | 直接调用 agent | ⏳ 待首次运行 |
| D006 | ontofuel 扩展 | 先扩展再集成 | ✅ C11/C12/C44/C33 |
| D007 | Agent 配置 | 本次配置 | ✅ openclaw.json |
| D008 | 消息协议 | 轻量 (GapRequest+DataSet 严格) | ✅ 已验证 |
| D009 | 可观测性 | 最小 JSON 日志 | ✅ ref_logger |

## 下一步（项目已关闭）

1. ~~专家审查~~ → 功能测试已替代
2. ~~等待慢线 cron 首次运行~~ → cron 保持运行，下周一 09:00 自动触发
3. ~~MP 数据写入 PG~~ → 107 条已写入（2026-05-30）
4. 如需扩展：添加 thermal_expansion, melting_point, density, specific_heat 四个物性
5. 如需迁移：将 ref-gap-fill 代码迁移到独立 NucPot 仓库
