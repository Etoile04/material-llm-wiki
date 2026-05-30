# 快线功能测试方案

> ref-gap-fill 快线端到端真实运行验证（非 mock）
> 目标：验证从缺口分析到数据写入的完整链路

## 测试环境

| 依赖 | 状态 | 验证方式 |
|------|------|---------|
| ThinkStation PG | ✅ 可达，23 条现有数据 | `ssh z203@100.70.30.21` |
| 验证 API | ✅ `https://verify.nucpot.dpdns.org/api/references` | curl 200 |
| NFMD Supabase | ❌ 无本地 env var | L2 查询用 API 模拟或跳过 |
| Zotero MCP | ⚠️ 需确认可用性 | `zotero-workflow-skills` |
| MinerU | ✅ `.venv-mineru/` 存在 | 本地 Python |
| LLM (物性提取) | ✅ zai/glm-5.1 | image/pdf 工具 |

## 测试分层

### L0: 单元层（已完成 ✅）
- 108 个 mock 测试全部通过
- 覆盖所有模块接口和边界条件

### L1: 模块集成层（已完成 ✅）
- test_e2e_umo.py — U-Mo BCC mock 全流程
- test_integration.py — 跨组件兼容性
- test_e2e_slowlane.py — 慢线集成

### L2: 真实数据层（本方案重点）
验证各模块与真实外部系统的交互。

### L3: 端到端编排层
验证 agent 级别的完整编排流程。

---

## L2 测试用例

### L2.1: 缺口分析 vs 真实 PG 数据
**目标：** gap_analyzer 产出的缺口与 PG 实际数据一致
**步骤：**
1. 从 API 拉取当前 23 条 reference_values
2. 运行 `gap_analyzer.compute_gaps(targets, existing)`
3. 验证缺口列表中不包含已存在的 (element_system, phase, property) 组合
4. 验证缺口总数 = 目标总数 - 已填数（14 × 12 = 168 目标，23 已填 → ~145 缺口）
5. 验证优先级排序正确（P1 的排在前面）

**通过标准：** 缺口数量与手动计算一致，无假阳性/假阴性

### L2.2: L1 缓存查询 vs 真实 PG
**目标：** cache_query L1 能从真实 PG 查到数据
**步骤：**
1. 选择一条已知存在于 PG 的记录（如 U BCC C11 = 119.0 GPa）
2. `cache_query("U", "BCC", "C11")` → 应命中 L1
3. 选择一条不存在的记录（如 U-Zr BCC C33）
4. `cache_query("U-Zr", "BCC", "C33")` → 应返回 None
5. 验证命中结果的数据完整性（value, unit, source 非 None）

**通过标准：** 已有数据命中，不存在的返回 None

### L2.3: L2 缓存查询 vs NFMD
**目标：** cache_query L2 从 NFMD Supabase 查询
**步骤：**
1. 确认 NFMD 连接配置可用（需 SUPABASE_URL + SUPABASE_KEY）
2. 查询已知 NFMD 中的参数（如 U-10Zr 的密度）
3. 验证 adapter_nfmd.py 转换格式正确
4. 若 Supabase 不可用，标记 skip 并记录

**通过标准：** 格式转换正确，或 skip 并记录原因

### L2.4: 写入真实 PG（受控）
**目标：** write_ref_value 能写入真实 PG 并去重
**步骤：**
1. 写入一条全新的测试值（element_system="TEST-Ni", phase="FCC", property="C11", value=250.0）
2. 验证写入成功，状态 WRITTEN_AUTO
3. 再次写入相同记录 → 验证返回 DUPLICATE
4. 写入超范围值（C11 = -999）→ 验证返回 REJECTED
5. **清理：** DELETE 测试数据

**通过标准：** 写入/去重/拒绝行为正确，测试数据已清理

### L2.5: L3A Wiki 查询（如可用）
**目标：** cache_query L3A 从 llm-wiki 知识库查询
**步骤：**
1. 检查 llm-wiki sessions 索引是否可用
2. 查询已知知识库中的参数
3. 验证 adapter_wiki.py 转换正确
4. 若索引不可用，标记 skip

**通过标准：** 格式转换正确，或 skip 并记录

### L2.6: 范围校验 vs property-mapping.json
**目标：** 验证所有 property-mapping.json 的范围与真实物理值一致
**步骤：**
1. 对每条现有 PG 记录，用 range check 验证
2. 检查是否有现有值超范围（可能是 mapping 定义过窄）
3. 列出所有超范围的记录

**通过标准：** 无超范围记录，或超范围记录有合理解释

---

## L3 测试用例

### L3.1: 快线模式 A — 纯缓存补全
**目标：** 仅用缓存补全，不调用搜索
**步骤：**
1. 发送 GapRequest 包含 5 个缓存应命中的物性
2. 运行 Phase 1 (缺口分析) + Phase 2 (缓存查询) + Phase 4 (验证)
3. 验证返回 DataSet.status = "partial"
4. 验证 stats.from_cache > 0
5. 验证 data 中的值与 PG 原始数据一致

**通过标准：** 缓存命中正确，无搜索调用，返回完整 DataSet

### L3.2: 快线模式 C — 单体系精准补全
**目标：** 指定 U-Mo BCC C44 的完整流程
**步骤：**
1. 发送 GapRequest: element_system="U-Mo", phase="BCC", property="C44"
2. Phase 2: 缓存查询（PG 无此记录 → MISS）
3. Phase 3: **手动提供测试文献**（已知含 C44 的论文 DOI 或 PDF）
4. 执行 librarian-extract 流程：PDF → MinerU → LLM 提取
5. 验证提取值合理（C44 应在 30-150 GPa 范围内）
6. 验证 write_ref_value 写入 PG
7. **清理：** 删除测试写入的记录

**通过标准：** 提取值合理且成功写入，或文献搜索失败时有明确错误报告

### L3.3: RefLogger 真实日志
**目标：** 验证 RefLogger 在真实流程中正确记录
**步骤：**
1. 运行一次完整的模式 A 流程
2. 验证 `data/ref-logs/$(date +%F).json` 被创建
3. 验证 JSON 格式正确，包含所有必需字段
4. 验证 request_id、timestamp、cache_hits 与实际运行一致

**通过标准：** 日志文件存在且内容可解析

---

## 执行计划

| 序号 | 测试 | 前置条件 | 预估耗时 | 风险 |
|------|------|---------|---------|------|
| 1 | L2.1 缺口分析 | PG 可达 | 2min | 低 |
| 2 | L2.2 L1 缓存 | PG 可达 | 2min | 低 |
| 3 | L2.3 L2 缓存 | Supabase env | 3min | 中（env 未配置）|
| 4 | L2.4 真实写入 | PG 可写 | 3min | 低（有清理）|
| 5 | L2.5 Wiki 查询 | llm-wiki 索引 | 2min | 中 |
| 6 | L2.6 范围校验 | PG 数据 | 1min | 低 |
| 7 | L3.1 模式 A | PG 可达 | 5min | 低 |
| 8 | L3.2 模式 C | 文献+PG | 10min | 高（LLM 提取不确定性）|
| 9 | L3.3 日志 | L3.1 完成 | 1min | 低 |

**总预估：** 30 min

### 执行顺序
1. 先跑 L2.1-L2.2（只读，零风险）
2. L2.6 范围校验（只读）
3. L2.4 真实写入（有清理步骤）
4. L2.3 / L2.5（可能 skip）
5. L3.1 模式 A（编排层）
6. L3.3 日志验证
7. L3.2 模式 C（最后，风险最高）

---

## 失败处理

| 失败场景 | 处理 |
|---------|------|
| PG 不可达 | 跳过所有 L1/写入测试，记录到 ISSUES.md |
| NFMD env 未配置 | L2.3 skip，不影响其他测试 |
| LLM 提取值超范围 | 记录提取结果，不写入 PG，人工审核 |
| Zotero MCP 不可用 | L3.2 使用预下载的 PDF |
| 测试数据清理失败 | 记录到 ISSUES.md，标记为手动清理项 |

## 通过标准

- L2: 4/6 以上通过（L2.3/L2.5 允许 skip）
- L3: L3.1 必须通过，L3.3 必须通过
- L3.2: 提取成功 OR 有明确失败报告
- 无测试数据残留（PG 中无 TEST-* 记录）
