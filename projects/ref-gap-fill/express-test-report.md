# 快线功能测试报告

> 日期: 2026-05-30
> 环境: macOS (local) + ThinkStation PG (SSH)

## 测试结果汇总

| ID | 测试项 | 结果 | 备注 |
|----|--------|------|------|
| L2.1 | 缺口分析 vs 真实 PG | ✅ PASSED | 89 缺口 / 23 已填 / 112 目标，数量平衡 |
| L2.2 | L1 缓存命中/未命中 | ✅ PASSED | U BCC C11=119 命中，U-Zr C33 未命中 |
| L2.3 | L2 NFMD 缓存查询 | ⏭️ SKIPPED | SUPABASE_URL/KEY 未配置 |
| L2.4 | 真实写入 PG (受控) | ⚠️ PARTIAL | 写入+清理成功，但 PG 缺 UNIQUE constraint |
| L2.5 | L3A Wiki adapter | ✅ PASSED | adapter 可用且转换正确，knowledge/params 待慢线构建 |
| L2.6 | 全量范围校验 | ✅ PASSED | 23/23 条均在范围内 |
| L3.1 | 快线模式 A (纯缓存) | ✅ PASSED | 3/5 缓存命中，DataSet 正确 |
| L3.2 | 快线模式 C (U-Mo C44) | ✅ PASSED | L3A 知识库提取 C44=49.52 GPa，范围校验通过 |
| L3.3 | RefLogger 真实日志 | ✅ PASSED | JSON 日志完整，cache_hits.L1=3 |

**通过率: 7/9 (L2.3 skip + L2.4 partial = 符合方案预期)**

## 关键发现

### F1: PG 缺少 UNIQUE Constraint
- **问题:** `reference_values` 表没有 `(element_system, phase, property, method, source)` 的 unique constraint
- **影响:** 应用层 write_ref_value.py 有去重，但直接 SQL 写入可产生重复
- **建议:** 添加 UNIQUE constraint 或至少添加 UNIQUE INDEX

### F2: L3A 知识库数据丰富
- 本地 llm-wiki 参数库包含大量 U-Mo 弹性常数数据
- 4 个来源给出 C44 ≈ 42-50 GPa，一致性良好
- L3 cache 是快线的重要数据源

### F3: 网络搜索不稳定
- web_search 连续超时，web_fetch 也受阻
- 快线模式 C 的文献搜索功能受网络限制
- 建议: 快线优先查 L3A 本地知识库，网络搜索作为补充

### F4: cache_query L1 接口设计
- `query_l1()` 使用 `_mock_rows` kwarg 注入数据
- 生产使用时需通过 PG 连接获取数据
- 当前无 PG 连接池模块（L1 查询靠 SSH tunnel）

## 未覆盖项
- L2 缓存查询 (NFMD Supabase) — 需配置环境变量
- 真实 LLM 物性提取 (PDF → LLM) — 网络超时
- Agent 级编排 (nucpot-db → nucpot-librarian) — 需 agent 启动

## 结论
快线核心链路（缺口分析 → 缓存查询 → 质量门控 → 日志记录）在真实数据环境下功能正常。主要风险在网络搜索稳定性和 PG schema 完整性。
