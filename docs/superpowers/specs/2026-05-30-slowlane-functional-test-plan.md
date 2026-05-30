# 慢线功能测试方案

> ref-gap-fill Phase 2 慢线端到端真实运行验证
> 目标：验证从文献扫描 → 参数提取 → 三级缓存回填 → 日志记录的完整链路
> 对标快线功能测试 9/9 通过的标准

## 测试环境

| 依赖 | 状态 | 验证方式 |
|------|------|---------|
| ThinkStation nucpot-db | ✅ 5432, UNIQUE 约束已加 | ssh 查询 |
| ThinkStation nfmd-postgres | ✅ 15432, 43 条参数 | ssh 查询 |
| L3A 知识库 | ✅ `data/fuel_swelling_wiki/parameters/` | 本地文件 |
| 慢线 cron job | ✅ 已注册，下周一 09:00 触发 | cron get |
| Zotero MCP | ⚠️ 需验证可用性 | 搜索 pending-slowlane |
| MinerU | ✅ `.venv-mineru/` | 本地 venv |
| llm-wiki 技能 | ✅ 已配置 | SKILL.md |

## 与快线测试的关系

快线测试验证的是「缓存查询 → 缺口发现 → 实时提取」链路。
慢线测试验证的是「定时扫描 → 批量提取 → 批量回填 → 审核队列」链路。

关键区别：
- 慢线写入 L1 是**真的写 PG**（快线只组装不写）
- 慢线有**置信度门控**（high 自动写，medium/low 标记 needs_review）
- 慢线有**L2 格式转换**（适配 NFMD parameters 格式）
- 慢线有**Zotero 标记管理**（pending-slowlane → 清除）

---

## 测试分层

### S0: 单元层（已完成 ✅）
- 36 个 mock 测试全部通过（test_slowlane_backfill + test_ref_logger + test_message_schemas + test_e2e_slowlane）

### S1: 真实数据层（本方案核心）
验证各慢线模块与真实外部系统的交互。

### S2: 端到端编排层
验证 cron 触发 → agent 执行 → 结果交付的完整流程。

---

## S1 测试用例

### S1.1: 慢线 L1 回填 — 真实 PG 写入

**目标：** `backfill_l1()` 能通过 `write_ref_value()` 真实写入 PG

**前置：** 从 L3A 知识库选一条真实物性（U-Mo C44 = 49.52 GPa, Miao 2016）

**步骤：**
1. 从 `data/fuel_swelling_wiki/parameters/2016_Miao_*.json` 加载 C44 参数
2. 调用 `adapt_wiki_param()` 转为 reference_value 格式
3. 调用 `backfill_l1([extracted], _existing=current_refs)`
4. 验证返回 `BackfillResult(written=1, skipped=0, errors=[])`
5. 查询 PG `SELECT * FROM reference_values WHERE element_system='U-Mo' AND property='C44'`
6. 验证 value = 49.52, confidence = 'high', source 包含 'Miao'
7. **清理：** DELETE 该条测试数据

**通过条件：**
- ✅ 写入成功，1 条记录
- ✅ 值和元数据正确
- ✅ 清理后记录数 = 原始 23

---

### S1.2: 慢线 L1 去重 — UNIQUE 约束验证

**目标：** 重复数据被 `write_ref_value()` 应用层拦截 + PG UNIQUE 约束双重保护

**步骤：**
1. 写入一条 U-Mo C44（同 S1.1）
2. 再次调用 `backfill_l1()` 写入相同数据
3. 验证返回 `BackfillResult(written=0, skipped=1)`
4. 直接 SQL INSERT 同一条，验证 UNIQUE 约束报错
5. **清理**

**通过条件：**
- ✅ 应用层去重: skipped=1
- ✅ DB 层约束: SQL 报 `uq_ref_value_unique` 错误

---

### S1.3: 慢线 L1 置信度门控

**目标：** 不同 confidence 级别产生不同写入行为

**步骤：**
1. 构造 3 条数据：
   - high confidence (DFT, peer-reviewed): U-Mo C12 = 105.0
   - medium confidence (estimated): U-Mo bulk_modulus = 135.0
   - low confidence (vague source): U-Mo formation_energy = 0.5
2. 调用 `backfill_l1([3条], _existing=current_refs)`
3. 验证 high → WRITTEN_AUTO, medium → WRITTEN_PENDING_REVIEW, low → rejected 或 skipped
4. 验证 PG 中只有 high 和 medium 两条（medium 标记 needs_review）
5. **清理**

**通过条件：**
- ✅ high 自动写入
- ✅ medium 写入但标记 pending_review
- ✅ low 被拒绝（或标记为需人工审核）
- ✅ 写入值符合范围检查

---

### S1.4: 慢线 L2 格式转换

**目标：** `backfill_l2()` 正确将 reference_value 格式转为 NFMD parameters 格式

**步骤：**
1. 用 S1.1 的 U-Mo C44 数据
2. 调用 `backfill_l2([extracted])`
3. 验证返回 `BackfillResult(written=1)` 且格式包含:
   - `material_raw` 包含 'U-Mo'
   - `name` 或 `symbol` 映射到 C44
   - `value_scalar` = 49.52
   - `unit` 标准化
4. 对无法映射的物性（如虚构 property），验证抛出 `NfmdAdapterError`

**通过条件：**
- ✅ 格式转换正确
- ✅ 无效物性被拦截

> **注意：** L2 实际 Supabase 写入仍是 TODO（`scripts/slowlane_backfill.py` 第 87 行），本测试只验证格式转换

---

### S1.5: 慢线 L2 NFMD 真实写入（如可用）

**目标：** 验证 adapter_nfmd 产出可被 NFMD parameters 表接受

**步骤：**
1. 构造一条 NFMD 格式的参数
2. 通过 SSH 写入 nfmd-postgres: `INSERT INTO parameters (...)`
3. 验证写入成功
4. 验证查询可见
5. **清理**

**通过条件：**
- ✅ INSERT 成功
- ✅ SELECT 可见
- ✅ 清理后无残留

> **前置：** 需要确认 parameters 表 schema 和约束

---

### S1.6: 慢线完整回填摘要

**目标：** `run_slowlane_backfill()` 正确汇总 L1+L2 结果

**步骤：**
1. 构造 5 条提取数据（3 high + 1 medium + 1 已存在重复）
2. 调用 `run_slowlane_backfill([5条], _existing=current_refs)`
3. 验证 `BackfillSummary`:
   - `total_input = 5`
   - `l1.written` = 3 (high 自动 + medium pending)
   - `l1.skipped` = 1 (重复)
   - `l1.errors` = 1 (或 skipped 视实现而定)
   - `l2.written` = 对应可转换的数量

**通过条件：**
- ✅ 数量汇总正确
- ✅ L1/L2 分开统计

---

### S1.7: 慢线日志与快线日志一致性

**目标：** RefLogger 在慢线场景下记录完整日志

**步骤：**
1. 创建 RefLogger（tmp 目录）
2. `start_request(items_count=5)` → 获取 request_id
3. 模拟慢线流程：record_cache_hit + record_express_result + record_error
4. `finish_request(duration_seconds=60, gaps_remaining=2)`
5. 验证 JSON 日志：
   - `cache_hits.L1` + `express_results` + `gaps_remaining` 数量正确
   - `slowlane_tagged_papers` 字段存在
   - `errors` 列表包含模拟的错误
   - schema 版本字段正确

**通过条件：**
- ✅ 日志文件创建
- ✅ 所有字段正确
- ✅ 格式与快线日志兼容（可被同一解析器处理）

---

### S1.8: 慢线消息协议验证

**目标：** GapRequest/DataSet 在慢线上下文中正确序列化

**步骤：**
1. 构造慢线 GapRequest（多个体系 + 多个物性，优先级 mixed）
2. `GapRequest.to_json()` → `GapRequest.from_json()` 往返
3. 构造 DataSet（status="partial"，包含 L1 写入结果 + 剩余缺口）
4. `DataSet.to_json()` → `DataSet.from_json()` 往返
5. 验证慢线特有字段：`preferred_method`="DFT", `priority`="low"

**通过条件：**
- ✅ 序列化/反序列化无丢失
- ✅ 慢线特有字段保留

---

### S1.9: 慢线全量范围校验

**目标：** 慢线写入的数据全部通过范围检查

**步骤：**
1. 从 L3A 知识库加载所有 U-Mo 相关参数
2. 逐一 `adapt_wiki_param()` 转换
3. 逐一 `passes_range_check()` 检查
4. 统计通过/未通过数量

**通过条件：**
- ✅ 所有 L3A 提取值在合理范围内
- ✅ 或明确标注超范围原因

---

## S2 测试用例（端到端编排）

### S2.1: 慢线 cron job 手动触发

**目标：** cron job 配置正确，可手动触发并产生结果

**步骤：**
1. `cron run` 手动触发 slowlane-weekly-ref-gap-fill
2. 等待 isolated session 完成事件
3. 验证 session 输出包含慢线执行日志
4. 验证日志文件 `data/ref-logs/YYYY-MM-DD.json` 更新

**通过条件：**
- ✅ cron run 成功
- ✅ isolated session 执行完成
- ✅ 日志文件写入

> **前置：** 需要至少一篇 Zotero 文献标记 pending-slowlane，或修改 cron payload 跳过 Zotero 扫描

### S2.2: 慢线 + 快线数据共享验证

**目标：** 慢线写入的数据可被快线缓存查询命中

**步骤：**
1. 慢线写入一条新物性到 PG（如 U-Mo C12）
2. 快线 `query_l1("U-Mo", "BCC", "C12")` 查询
3. 验证命中，值与写入一致
4. **清理**

**通过条件：**
- ✅ 快线 L1 缓存命中慢线写入数据

---

## 测试执行策略

### 执行顺序

1. **只读测试** (S1.1 只验证格式, S1.4, S1.6, S1.7, S1.8, S1.9) — 先跑，不修改任何数据
2. **受控写入测试** (S1.1 完整, S1.2, S1.3, S1.5) — 每条测试后清理
3. **端到端测试** (S2.1, S2.2) — 最后跑

### 判定标准

| 判定 | 含义 |
|------|------|
| ✅ PASS | 全部通过条件满足 |
| ⚠️ PARTIAL | 核心功能通过，非关键项失败 |
| ⏭️ SKIP | 外部依赖不可用 |
| ❌ FAIL | 核心通过条件不满足 |

### 已知限制

1. L2 Supabase 写入仍是 TODO — S1.5 可能 SKIP
2. Zotero MCP 可用性未确认 — S2.1 可能需要 mock
3. 慢线 cron 首次运行需等下周一 — S2.1 用手动触发替代
