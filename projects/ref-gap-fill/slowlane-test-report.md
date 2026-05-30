# 慢线功能测试报告

> 2026-05-30 | ref-gap-fill Phase 2 慢线端到端验证
> 测试环境: Mac Studio → ThinkStation (100.70.30.21) | nucpot-db:5432 | nfmd-postgres:15432

## 测试结果

| 测试 | 结果 | 说明 |
|------|------|------|
| S1.1 | ✅ PASS | backfill_l1 评估 + 真实 PG 写入 + 清理 |
| S1.2 | ✅ PASS | 应用层去重 + DB UNIQUE 双重保护 |
| S1.3 | ✅ PASS | high→AUTO, medium→PENDING, low 被评估 |
| S1.4 | ✅ PASS | adapter_nfmd 格式转换 + 无效物性拦截 |
| S1.5 | ✅ PASS | NFMD parameters INSERT/SELECT/DELETE |
| S1.6 | ✅ PASS | run_slowlane_backfill L1+L2 汇总 |
| S1.7 | ✅ PASS | RefLogger 全字段 + 快线兼容 |
| S1.8 | ✅ PASS | GapRequest/DataSet 序列化往返 |
| S1.9 | ✅ PASS | PG 23/23 + 慢线待写入 4/4 范围检查通过 |
| S2.1 | ✅ PASS | 慢线模拟全流程（评估→回填→日志） |
| S2.2 | ✅ PASS | 慢线写入→快线 L1 缓存命中 |

**11/11 全部通过**

## 关键发现

### F1: backfill_l1 是评估层，不直连 DB
- `write_ref_value()` 只做质量门控+去重+置信度决策，返回 WriteStatus
- 实际 PG 写入由慢线 agent 根据 WRITTEN_AUTO 状态手动执行 SQL
- 这是设计意图：agent 控制写入时机，模块只负责评估

### F2: NFMD parameters 表有 4 个 NOT NULL 字段
- `id`, `name`, `category`, `value_type` 必填
- `value_type` 所有现有值都是 `'scalar'`
- 慢线 L2 写入需填充这 4 个字段
- adapter_nfmd 当前不生成这些字段 → 需补充

### F3: S2.2 发现 U-Mo C12 已有值
- 快线写入前查询 U-Mo C12 返回 108.0（已有数据）
- 写入 105.0 后 query_l1 返回新值（匹配 element_system+phase+property，不匹配 source）
- 说明 query_l1 返回第一条匹配，多条同 property 不同 source 需注意

### F4: 置信度门控行为
- `write_ref_value`: high → WRITTEN_AUTO, 非 high → WRITTEN_PENDING_REVIEW
- low confidence 不会被拒绝，只是标记 needs_review
- 质量门控主要靠 passes_range_check，不靠 confidence 值

## ISSUES

无新增。

## 数据状态

- PG reference_values: 23 条（测试前后一致）
- NFMD parameters: 43 条（测试前后一致）
