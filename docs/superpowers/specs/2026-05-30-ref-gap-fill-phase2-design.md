# Ref-Gap-Fill Phase 2 — 慢线 + 部署 + 协议 + 可观测性 Design Spec

> 延续 Phase 1 (子项目 A+B+D)，完成 design spec 中剩余的子项目 C 及部署配置。
> 按 dev-pm M 级流程管理。

**Goal:** 实现慢线自动化、Agent 配置部署、消息协议标准化、最小可观测性日志系统，将 ref-gap-fill 从 75% 完成度提升到 100%。

**前置依赖:** Phase 1 已完成（72 tests, 8 scripts, 3 skills）。

---

## 设计决策（Phase 2 新增）

| # | 决策 | 选择 | 理由 |
|---|------|------|------|
| D005 | llm-wiki 集成 | agent 直接调用 SKILL.md 流程 | 保持灵活性，不重构 |
| D006 | ontofuel 集成 | 先扩展本体再集成 | 弹性常数是验证核心属性 |
| D007 | Agent 配置 | 本次配置到 openclaw.json | 验证完整架构 |
| D008 | 消息协议 | 轻量：GapRequest+DataSet 严格，中间用 dict | 避免过度工程 |
| D009 | 可观测性 | 最小：data/ref-logs/ JSON 日志 | 基础优先 |

---

## 1. 子项目 C：慢线实现

### 1.1 慢线 Cron Job

配置一个 cron job，每周一 09:00 CST 触发慢线流程。

```
慢线主 cron:
  名称: slowlane-weekly-ref-gap-fill
  调度: 0 9 * * 1 (Asia/Shanghai)
  target: isolated
  payload: agentTurn — 执行慢线流程（见 §1.2）
  delivery: announce
```

### 1.2 慢线流程

```
Slowlane Agent (isolated session):
  │
  ├─ 1. 扫描 Zotero pending-slowlane 标记文献
  │     工具：zotero-workflow-skills/zotero-search
  │     输出：待消化文献列表
  │
  ├─ 2. 对每篇文献执行 llm-wiki ingest
  │     工具：agent 调用 llm-wiki SKILL.md 流程
  │     步骤：PDF → MinerU → summary.md → parameters/*.json
  │
  ├─ 3. 对每篇文献执行 ontofuel extraction
  │     工具：ontofuel-extractor agent + ontology-driven-extraction skill
  │     步骤：提取 → individuals → 合并去重 → 本体增量更新
  │     注意：需先扩展 C11/C12/C44/C33 到 ontofuel 本体
  │
  ├─ 4. 回填三级缓存
  │     L1: 提取物性值 → write_ref_value.py → reference_values
  │     L2: 适配为 NFMD 格式 → sync 到 Supabase parameters
  │     L3a: summary + params → llm-wiki knowledge base (自动)
  │     L3b: individuals → ontofuel 本体 (自动)
  │
  └─ 5. 清除 Zotero pending-slowlane tag
        工具：zotero-workflow-skills/zotero-mcp
```

### 1.3 快线标记

快线（librarian-extract）处理完文献后，在 Zotero 中添加 tag `pending-slowlane`。这需要在 librarian-extract SKILL.md 中补充此步骤。

### 1.4 ontofuel 本体扩展

在 ontofuel 本体中添加弹性常数的 OWL class 和 properties：

```
新增 class: ElasticConstant
  ├─ 子类: ElasticConstantC11, ElasticConstantC12, ElasticConstantC44, ElasticConstantC33
  ├─ 属性: hasValue (float), hasUnit (string), hasTemperature (float)
  └─ 关联: belongsToSystem → MaterialSystem
```

### 1.5 新建文件

| 文件 | 用途 |
|------|------|
| `scripts/slowlane_backfill.py` | 慢线回填逻辑（L1+L2 写入） |
| `scripts/ref_logger.py` | JSON 日志记录器 |
| `scripts/message_schemas.py` | GapRequest + DataSet schema 定义 |
| `tests/test_slowlane_backfill.py` | 慢线回填测试 |
| `tests/test_ref_logger.py` | 日志记录器测试 |
| `tests/test_message_schemas.py` | 消息协议测试 |

### 1.6 修改文件

| 文件 | 修改 |
|------|------|
| `~/.openclaw/skills/librarian-extract/SKILL.md` | 补充 Zotero pending-slowlane tag 步骤 |
| `~/.openclaw/skills/ref-gap-fill/SKILL.md` | 补充慢线 section 的具体实现细节 |
| `scripts/adapter_ontology.py` | 更新 ontofuel_keys 映射（添加 C11/C12/C44/C33） |
| `~/.openclaw/openclaw.json` | 新增 nucpot-db + nucpot-librarian agent |

---

## 2. Agent 配置

### 2.1 nucpot-db（数据库智能体）

```json
{
  "id": "nucpot-db",
  "name": "核势数据库",
  "skills": ["ref-gap-fill", "nfmd-db-ops"],
  "model": {"primary": "zai/glm-5-turbo"}
}
```

工具权限：exec, read, write, edit, web_search, web_fetch, memory_search, memory_get, sessions_spawn, sessions_yield, subagents, message, llm-task, gateway

### 2.2 nucpot-librarian（搜索智能体）

```json
{
  "id": "nucpot-librarian",
  "name": "文献管理员",
  "skills": ["librarian-search", "librarian-extract", "mineru-pdf"],
  "model": {"primary": "zai/glm-5-turbo"}
}
```

工具权限：exec, read, write, edit, web_search, web_fetch, memory_search, memory_get, browser, image, llm-task, sessions_spawn, sessions_yield, subagents, message

---

## 3. 消息协议

### 3.1 GapRequest Schema

```python
@dataclass
class GapRequest:
    schema_version: str = "ref-gap-fill/GapRequest/v1"
    request_id: str = ""       # uuid4
    timestamp: str = ""        # ISO-8601
    items: list[GapRequestItem] = field(default_factory=list)

@dataclass
class GapRequestItem:
    element_system: str        # required
    phase: str = ""            # optional
    properties: list[str] = field(default_factory=list)  # required
    preferred_method: str = "any"  # DFT | experimental | any
    temperature_k: int = 0
    priority: str = "normal"   # high | normal | low
```

### 3.2 DataSet Schema

```python
@dataclass
class DataSet:
    schema_version: str = "ref-gap-fill/DataSet/v1"
    request_id: str = ""
    status: str = ""           # complete | partial | failed
    stats: DataSetStats = field(default_factory=DataSetStats)
    data: list[dict] = field(default_factory=list)  # RefValue dicts
    gaps: list[dict] = field(default_factory=list)   # remaining gaps

@dataclass
class DataSetStats:
    total_requested: int = 0
    from_cache: int = 0
    from_express: int = 0
    gaps_remaining: int = 0
```

---

## 4. 可观测性

### 4.1 JSON 日志格式

每次 GapRequest 处理完成后，写入 `data/ref-logs/YYYY-MM-DD.json`：

```json
{
  "request_id": "uuid",
  "timestamp": "ISO-8601",
  "items_requested": 5,
  "cache_hits": {"L1": 2, "L2": 1, "L3": 0},
  "express_results": 1,
  "gaps_remaining": 1,
  "duration_seconds": 145,
  "slowlane_tagged_papers": 2,
  "errors": []
}
```

### 4.2 RefLogger API

```python
class RefLogger:
    def __init__(self, log_dir: str = "data/ref-logs"): ...
    def start_request(self, request: GapRequest) -> str: ...
    def record_cache_hit(self, level: str): ...
    def record_express_result(self): ...
    def record_error(self, error: str): ...
    def finish_request(self, duration: float, gaps_remaining: int): ...
```

---

## 5. Task 分解

按 TDD 要求，每个 Task 先写测试再写实现。

| Task | 内容 | 依赖 | 预估 | 可并行 |
|------|------|------|------|--------|
| T14 | ontofuel 本体扩展 (C11/C12/C44/C33) | 无 | 0.5d | ✅ |
| T15 | slowlane_backfill.py | 无 | 0.5d | ✅ |
| T16 | ref_logger.py | 无 | 0.5d | ✅ |
| T17 | message_schemas.py | 无 | 0.5d | ✅ |
| T18 | librarian-extract SKILL.md 补充 tag | 无 | 0.25d | ✅ |
| T19 | ref-gap-fill SKILL.md 补充慢线实现 | T15 | 0.25d | ❌ |
| T20 | adapter_ontology.py 更新 keys | T14 | 0.25d | ❌ |
| T21 | openclaw.json agent 配置 | 无 | 0.25d | ✅ |
| T22 | 慢线 cron job 注册 | T15, T19 | 0.25d | ❌ |
| T23 | 端到端慢线测试 | T15-T22 | 0.5d | ❌ |

**执行分组：**
- 批次 1 (并行): T14, T15, T16, T17, T18, T21
- 批次 2 (串行): T19, T20
- 批次 3 (串行): T22
- 批次 4 (验证): T23
