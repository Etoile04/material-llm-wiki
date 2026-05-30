# Ref-Gap-Fill Phase 2 — Implementation Plan

> 按 dev-pm M 级流程，Step 2 产出。

**Goal:** 实现慢线 + 部署 + 协议 + 可观测性，将 ref-gap-fill 完成度从 75% → 100%。

**Spec:** `docs/superpowers/specs/2026-05-30-ref-gap-fill-phase2-design.md`

---

## 执行顺序

```
批次 1 (并行): T14, T15, T16, T17, T18, T21
批次 2 (串行): T19, T20
批次 3 (串行): T22
批次 4 (验证): T23
```

---

## T14: ontofuel 本体扩展

- [ ] 写失败测试 `tests/test_ontology_elastic_constants.py`
- [ ] 在 ontofuel 本体中添加 ElasticConstant class + C11/C12/C44/C33 子类
- [ ] 更新 `scripts/adapter_ontology.py` 的 ontofuel_keys 映射
- [ ] 测试通过
- [ ] `git commit -m "feat(ref-gap-fill): extend ontofuel ontology with elastic constant classes"`

**文件：**
- 新建: `tests/test_ontology_elastic_constants.py`
- 修改: ontofuel 本体文件, `scripts/adapter_ontology.py`

**测试用例：**
1. test_elastic_constant_class_exists
2. test_c11_subclass_exists
3. test_c12_subclass_exists
4. test_c44_subclass_exists
5. test_c33_subclass_exists
6. test_adapter_ontology_maps_c11
7. test_adapter_ontology_maps_c12

---

## T15: slowlane_backfill.py

- [ ] 写失败测试 `tests/test_slowlane_backfill.py`
- [ ] 实现 `scripts/slowlane_backfill.py`
- [ ] 测试通过
- [ ] `git commit -m "feat(ref-gap-fill): add slowlane backfill logic for L1+L2 writeback"`

**文件：**
- 新建: `scripts/slowlane_backfill.py`, `tests/test_slowlane_backfill.py`

**功能：**
- `backfill_l1(extracted_values: list[dict]) -> BackfillResult` — 调用 write_ref_value 写入本地 PG
- `backfill_l2(extracted_values: list[dict]) -> BackfillResult` — 适配为 NFMD 格式，同步到 Supabase
- `run_slowlane_backfill(extracted_values: list[dict]) -> BackfillSummary` — L1+L2 统一回填

**测试用例：**
1. test_backfill_l1_writes_high_confidence
2. test_backfill_l1_skips_duplicates
3. test_backfill_l2_adapts_format
4. test_backfill_l2_skips_existing
5. test_run_slowlane_backfill_summary
6. test_empty_input_returns_empty

---

## T16: ref_logger.py

- [ ] 写失败测试 `tests/test_ref_logger.py`
- [ ] 实现 `scripts/ref_logger.py`
- [ ] 测试通过
- [ ] `git commit -m "feat(ref-gap-fill): add JSON request logger for observability"`

**文件：**
- 新建: `scripts/ref_logger.py`, `tests/test_ref_logger.py`

**功能：**
- `RefLogger(log_dir)` — 日志记录器
- `start_request(request) -> request_id` — 开始记录
- `record_cache_hit(level)` — 记录缓存命中
- `record_express_result()` — 记录快线结果
- `record_error(error)` — 记录错误
- `finish_request(duration, gaps_remaining)` — 完成记录，写入 JSON

**测试用例：**
1. test_start_request_creates_id
2. test_record_cache_hit_increments
3. test_record_express_result_increments
4. test_record_error_appends
5. test_finish_request_writes_json
6. test_finish_request_json_format
7. test_multiple_requests_same_day_append

---

## T17: message_schemas.py

- [ ] 写失败测试 `tests/test_message_schemas.py`
- [ ] 实现 `scripts/message_schemas.py`
- [ ] 测试通过
- [ ] `git commit -m "feat(ref-gap-fill): add GapRequest and DataSet message schemas"`

**文件：**
- 新建: `scripts/message_schemas.py`, `tests/test_message_schemas.py`

**功能：**
- `GapRequest` dataclass — 输入 schema
- `GapRequestItem` dataclass — 输入条目
- `DataSet` dataclass — 输出 schema
- `DataSetStats` dataclass — 输出统计
- `to_json()` / `from_json()` 序列化
- 验证逻辑：required fields, property name validation

**测试用例：**
1. test_gap_request_item_requires_element_system
2. test_gap_request_generates_uuid
3. test_gap_request_serializes_to_json
4. test_data_set_status_must_be_valid
5. test_data_set_stats_defaults
6. test_from_json_roundtrip
7. test_invalid_property_name_rejected

---

## T18: librarian-extract SKILL.md 补充 tag

- [ ] 编辑 `~/.openclaw/skills/librarian-extract/SKILL.md`
- [ ] 在提取流程末尾添加 Zotero pending-slowlane tag 步骤
- [ ] 无需 pytest（技能文件）
- [ ] `git commit -m "docs(ref-gap-fill): add slowlane tagging step to librarian-extract"`

**修改内容：**
在 Step 4 去重检查后添加：
```
### Step 4.5: 慢线标记
对每篇成功提取的文献，在 Zotero 中添加 tag "pending-slowlane"。
此 tag 供慢线 cron 扫描，触发深度消化流程。
工具：zotero-workflow-skills/zotero-mcp
```

---

## T19: ref-gap-fill SKILL.md 补充慢线实现

- [ ] 编辑 `~/.openclaw/skills/ref-gap-fill/SKILL.md`
- [ ] 在慢线 section 补充具体的 Python 调用示例
- [ ] 无需 pytest
- [ ] `git commit -m "docs(ref-gap-fill): detail slowlane implementation in SKILL.md"`

**依赖：** T15 (slowlane_backfill.py)

---

## T20: adapter_ontology.py 更新 keys

- [ ] 写失败测试
- [ ] 更新 `scripts/adapter_ontology.py` 的 ontofuel_keys 映射（C11/C12/C44/C33）
- [ ] 更新 `data/property-mapping.json` 的 ontofuel_keys 字段
- [ ] 测试通过
- [ ] `git commit -m "feat(ref-gap-fill): add C11/C12/C44/C33 keys to ontology adapter"`

**依赖：** T14 (ontofuel 本体扩展)

---

## T21: openclaw.json agent 配置

- [ ] 备份当前 openclaw.json
- [ ] 在 agents.list 中添加 nucpot-db 和 nucpot-librarian
- [ ] 验证配置格式正确（json lint）
- [ ] 无需 pytest（配置文件）
- [ ] `git commit -m "feat(ref-gap-fill): add nucpot-db and nucpot-librarian agent configs"`

**文件：**
- 修改: `~/.openclaw/openclaw.json`

---

## T22: 慢线 cron job 注册

- [ ] 注册慢线周 cron job
- [ ] 验证 job 创建成功
- [ ] 记录 job ID 到 STATE.json
- [ ] `git commit -m "feat(ref-gap-fill): register slowlane weekly cron job"`

**依赖：** T15, T19

**Cron 配置：**
```json
{
  "name": "slowlane-weekly-ref-gap-fill",
  "schedule": {"kind": "cron", "expr": "0 9 * * 1", "tz": "Asia/Shanghai"},
  "sessionTarget": "isolated",
  "payload": {
    "kind": "agentTurn",
    "message": "慢线周任务：扫描 Zotero 中 pending-slowlane 标记的文献...",
    "timeoutSeconds": 600
  },
  "delivery": {"mode": "announce"}
}
```

---

## T23: 端到端慢线测试

- [ ] 写 `tests/test_e2e_slowlane.py`
- [ ] 模拟完整慢线流程：提取 → 回填 L1+L2 → 日志记录
- [ ] 测试通过
- [ ] 全量测试 `pytest tests/ -v` 确认无回归
- [ ] `git commit -m "test(ref-gap-fill): add end-to-end slowlane test"`

**依赖：** T15-T22 全部完成

**测试用例：**
1. test_slowlane_extracts_and_backfills_l1
2. test_slowlane_extracts_and_backfills_l2
3. test_slowlane_logs_request
4. test_slowlane_handles_empty_input
5. test_slowlane_skips_duplicates
6. test_message_schemas_in_slowlane_context
