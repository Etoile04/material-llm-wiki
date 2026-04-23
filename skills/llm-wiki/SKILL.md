---
name: llm-wiki
description: >-
  Build and maintain a Karpathy-style LLM knowledge base for nuclear materials research.
  Ingests raw sources (papers, PDFs, notes), compiles cross-linked concept/entity/summary
  pages, answers queries against the corpus, lints the graph for health, and processes
  human feedback via audit/. Use when (1) scaffolding a new knowledge base,
  (2) ingesting articles/papers/PDFs into raw/, (3) compiling or restructuring wiki
  articles, (4) answering questions against the wiki, (5) running lint passes,
  (6) processing human feedback from audit/.
---

# LLM Wiki — Nuclear Materials Knowledge Base

> Based on Karpathy's LLM Wiki pattern. Adapted for OpenClaw by Wenjie Li.

## Core Idea

Instead of RAG (re-retrieving raw docs every time), the LLM **compiles** raw sources into a persistent, cross-linked wiki. Knowledge compounds — every ingest, query, lint, and audit pass makes the wiki richer.

- **You** own: sourcing raw material, asking questions, steering direction, filing feedback.
- **LLM** owns: all writing, cross-referencing, filing, bookkeeping, and applying feedback.

Five operations: `compile`, `ingest`, `query`, `lint`, `audit`.

## Directory Layout

```
<wiki-root>/
├── CLAUDE.md              ← Schema: scope, conventions, current articles, gaps
├── log/                   ← Per-day operation log (one file per day)
│   └── YYYYMMDD.md
├── audit/                 ← Human feedback inbox
│   └── resolved/          ← Processed feedback
├── raw/                   ← Immutable source documents (LLM reads only)
│   ├── articles/          ← Web articles, notes
│   ├── papers/            ← Extracted paper text
│   └── refs/              ← Pointer files for external PDFs/binaries
├── wiki/                  ← LLM-generated knowledge (LLM writes)
│   ├── index.md           ← Master catalog
│   ├── concepts/          ← Concept/topic pages (<1200 words each)
│   ├── entities/          ← Materials, models, people, organizations
│   └── summaries/         ← Per-source summary pages (200-400 words)
├── parameters/            ← Structured parameter data (JSON)
└── outputs/
    └── queries/           ← Query answers (promote durable ones to wiki/)
```

## 语言规范

### 中文为主、英中对照

- **所有 wiki 页面**以中文撰写，英文术语首次出现时标注在括号中
- 例如：「裂变气体气泡（Fission Gas Bubble, FGB）在辐照初期...」
- **术语对照表**：`raw/terminology.md` — 所有页面必须使用统一翻译
- **参数符号**保持英文（如 $D_v$, $E_m$），描述用中文
- **文件名**保持英文（便于跨平台兼容），页面标题和内容用中文

### 格式示例

```markdown
# 再结晶（Recrystallization）

> 辐照诱发再结晶是指...

## 物理机制

裂变气体扩散（Fission Gas Diffusion）驱动...

## 关键参数

| 符号 | 数值 | 单位 | 材料 | 来源 |
|------|------|------|------|------|
| $\Phi_{rx}$ | 2-4×10²¹ | fissions/m³ | U-10Mo | [[wiki/summaries/2013_Kim_RecrystallizationFGBSwellingUMo|Kim 2013]] |
```

## Core Principles

### 1. Divide and Conquer

Single concept page = **400–1200 words**. When a topic exceeds this:
- Create subfolder: `wiki/concepts/<topic>/`
- Index page: `wiki/concepts/<topic>/index.md`
- Each aspect: `wiki/concepts/<topic>/<aspect>.md`

### 2. Mermaid for Diagrams, KaTeX for Formulas

- Flow/state/hierarchy diagrams → **mermaid** (never ASCII art)
- Formulas → **KaTeX**: inline `$f(x)$` or block `$$...$$`

### 3. Raw File Policy

- Small text files → copy to `raw/`
- Large PDFs (>10MB) → pointer file in `raw/refs/`:
  ```yaml
  ---
  kind: ref
  external_path: /path/to/file.pdf
  size: ~50 MB
  ---
  ```
- Wiki pages cite `[[raw/refs/<slug>]]` like any source

### 4. Audit is the Human Feedback Surface

- Humans file feedback → `audit/` directory
- AI processes feedback → moves to `audit/resolved/` with resolution notes
- Never delete audit files

## The Five Operations

### 1. `compile`

(Re)structure wiki content. Run after big ingests, when pages outgrow limits, or when index.md is stale.

Steps:
1. Read `CLAUDE.md`, `wiki/index.md`, target subtree
2. Split oversized pages (>1200 words)
3. Merge near-duplicates
4. Rebuild `wiki/index.md`
5. Log to `log/YYYYMMDD.md`

### 2. `ingest`

Add a new source. One source typically touches 5–15 wiki pages.

Steps:

#### 0. 源文件验证（Pre-ingest Check）
1. 读取 MD 文件前 50 行，提取论文标题
2. 与目录名/文件名对比
3. 如不匹配：以 MD 内容中的标题为准，更新 slug 为 `YYYY_Author_ShortTitle`
4. 记录不匹配到 `log/YYYYMMDD.md`

#### 1. PDF 转 Markdown（三层策略）

**优先级**: mineru-open-api > 本地 MinerU > pdftotext

```bash
# 方法 A: mineru-open-api flash-extract（推荐，免 token）
# 限制：<10MB 且 <20页，自动含公式+表格+OCR
mineru-open-api flash-extract "<pdf_path>" -o raw/papers/ --language en

# 大文件分页：
mineru-open-api flash-extract "<pdf_path>" -o raw/papers/ --language en --pages 1-20

# 方法 B: mineru-open-api extract（需 token，无限制）
# 适用于 >10MB 或 >20页，支持 VLM 模型
mineru-open-api extract "<pdf_path>" -o raw/papers/ --language en -f md

# 方法 C: 本地 MinerU（离线备选，需 HF 模型缓存）
~/.openclaw/workspace/.venv-mineru/bin/mineru -p "<pdf_path>" -o raw/papers/ -b pipeline -m auto -l en -f true -t true

# 方法 D: pdftotext（最后兜底，不保留公式格式）
pdftotext "<pdf_path>" raw/papers/<slug>.txt
```

**选择策略**:
| 条件 | 方法 |
|------|------|
| <10MB 且 <20页 | flash-extract（免 token）|
| >10MB 或 >20页 | extract（需 MINERU_TOKEN）|
| 网络不可用 | 本地 MinerU 或 pdftotext |

**Token 配置**: `~/.mineru/config.yaml` 或环境变量 `MINERU_TOKEN`

- 输出保存到 `raw/papers/` 或 `raw/mineru/<slug>/`
- 如果 PDF 已有对应 `.md` 且公式覆盖率 >70%，自动跳过
- 转换后验证公式覆盖率：`grep -c '\$\$' output.md`

**异常处理（实战经验）**：
1. **SSL / 网络失败**：MinerU 连接 HuggingFace 超时 → 跳过 MinerU，直接用 pdftotext 兜底，不要重试浪费等待时间
2. **pdftotext 后的公式补回**：pdftotext 会丢失所有公式。处理方式：
   - 在 summary 的 `## Key Equations` 章节中，通过论文 DOI + web_search 补回关键公式
   - 标记该论文为 `formula_source: doi_search`，区别于 MinerU 直接提取的 `formula_source: pdf`
3. **目录名预校验**：转换前先检查目录名是否与 PDF 实际标题匹配（昨发现 `Xie_2020` 实际是 Beeler 论文）。以 PDF 正文标题为准，不匹配时记录到 log 并修正 slug

#### 2. 读取源文件全文
- 读取 MD/TXT 文件全文
- ⚠️ pdftotext 文件前 200 行可能是元数据，跳过
- ⚠️ MinerU 输出中 `Formula Recognition: ❌ Disabled` 的需重新转换
3. 创建 `wiki/summaries/<slug>.md`（200-400 词中文摘要）
   - **⚠️ 模型类论文必须包含 `## Key Equations` 章节**
   - 公式用 LaTeX 格式（`$$...$$` 块级、`$...$` 行内）
   - 每个公式标注物理含义和变量说明
   - 如果源 MD 缺公式，用 web_search 搜索论文 DOI 获取
4. 创建/更新 `wiki/concepts/` 概念页
5. 创建/更新 `wiki/entities/` 实体页
6. 提取参数到 `parameters/<slug>.json`
   - **参数提取范围**（不限于肿胀，覆盖以下 8 类）：
     - 扩散系数（Diffusion Coefficient）：$D_v$, $D_i$, 互扩散系数
     - 激活能（Activation Energy）：$E_m$, $E_f$, 迁移/形成能
     - 热力学参数（Thermodynamic）：$ΔG$, $ΔH$, $ΔS$, 溶解度极限
     - 相变参数（Phase Transformation）：相变温度、相图数据、CALPHAD 参数
     - 弹性/力学性质：弹性常数、剪切模量、泊松比
     - 辐照损伤参数：空位形成能、间隙形成能、级联效率
     - 肿胀/气泡参数：肿胀率、气泡密度/尺寸、裂变气体释放率
     - 燃料性能：热导率、比热、密度
   - 每类参数都应提取，即使论文主题不是肿胀
7. 更新 `wiki/index.md`
8. 记录日志到 `log/YYYYMMDD.md`

**⚠️ PDF 转 Markdown 是必需步骤**：
- 所有 PDF 必须先转换为 Markdown，保存到 `raw/papers/`
- MinerU 路径：`/Users/lwj04/.openclaw/workspace/.venv-mineru/bin/mineru`
- **公式识别必须开启**: `-f true -t true`
- 大型 PDF（>10MB）MinerU 处理较慢，可用 pdftotext 先处理
- 批量处理：`BATCH_FILE=batch.json python3 scripts/batch_convert.py`

**⚠️ Summary 公式要求**：
- 涉及数理模型的论文，summary 必须包含 `## Key Equations` 章节
- 公式用 LaTeX 格式，标注物理含义
- 如果 MinerU 转换缺公式，用 web_search + DOI 补充
- 公式缺失是知识库质量的关键风险点

### 3. `query`

Answer a question grounded in the wiki.

Steps:
1. Read `wiki/index.md`
2. Read relevant pages + one level of wikilinks
3. If insufficient material, say so and suggest what to ingest
4. Synthesize answer with `[[Page Name]]` citations
5. Save to `outputs/queries/`
6. Promote durable answers to `wiki/concepts/`
7. Log

### 4. `lint`

Health check. Check:
- Dead wikilinks (`[[Target]]` where file doesn't exist)
- Orphan pages (no inbound links)
- Missing index entries
- Oversized pages (>1200 words)
- Stale parameters (not updated in >30 days)
- Audit shape (malformed files)
- Log consistency

### 5. `audit`

Process human feedback from `audit/`.

Steps:
1. List open audits
2. For each: read, locate target text, decide action (accept/partial/reject/defer)
3. Apply corrections to target files
4. Append resolution section, move to `audit/resolved/`
5. Log

### 6. `validate` — 参数质量验证

对 `parameters/` 目录下的 JSON 文件进行质量检查。

Steps:
1. 读取 `parameters/` 或指定目录下的所有 JSON 文件
2. 运行 `scripts/validate_params.py`
3. 检查项：
   - **量级合理性**（magnitude check）：支持 typed values，`scalar` 检查单值，`range` 检查上下界，`expression` 跳过数值校验
   - **单位一致性**（unit consistency）：同参数不同来源的单位是否可转换
   - **必填字段**（required fields）：id, symbol, unit, category, source_file，以及 typed value 所需字段
   - **ID 唯一性**（unique ID）：全局无重复
   - **重复检测**（duplication）：不同 ID 但相同 symbol+material+temperature 的记录
4. **typed value schema**：
   - `value_type: scalar|range|expression|list`
   - `scalar` → `value`
   - `range` → `value_min`, `value_max`
   - `expression` → `value_expr`
   - `list` → `values`
4. 输出三级报告：**pass** ✅ / **warn** ⚠️ / **fail** ❌
5. 对 fail 项给出具体修复建议
6. Log to `log/YYYYMMDD.md`

### 7. `compare` — 参数版本比对

对比两个参数目录（如 v1 和 v2），精确匹配论文级别变更。

Steps:
1. 读取两个参数目录（v1 和 v2）
2. 运行 `scripts/compare_params.py`
3. 按论文级别精确匹配（source_file + symbol + material + temperature）
4. 分类输出：
   - **匹配**（matched）：完全一致
   - **新增**（added）：v2 独有
   - **修正**（corrected）：同 ID 但值/单位不同
   - **冲突**（conflict）：匹配键相同但值差异超阈值
   - **缺失**（missing）：v1 有但 v2 无
5. 对冲突项标注差异原因：单位不同 / 条件不同 / 提取错误 / 疑似匹配错误
6. Log to `log/YYYYMMDD.md`

## `wiki/index.md` Format

```markdown
# Index — <Topic>

> One-sentence scope.

## 🔖 Navigation
- [[#Concepts]] · [[#Entities]] · [[#Summaries]] · [[#Open Questions]]

## Concepts
### <Category>
- [[concepts/Foo]] — one-line summary

## Entities
- [[entities/Bar]] — one-line summary

## Summaries (chronological)
- YYYY-MM-DD — [[summaries/slug]] — one-line summary

## Open Questions
- Q1: ...
```

## `log/` Format

- One file per day: `log/YYYYMMDD.md`
- H1 = date; H2 per entry: `## [HH:MM] <op> | <description>`
- Ops: compile, ingest, query, lint, audit, promote, split

## `CLAUDE.md` Format

The schema file. Contains:
- **Scope**: What this wiki covers
- **Naming conventions**: File naming rules
- **Current articles**: List of all wiki pages
- **Research gaps**: Topics needing more sources
- **Open questions**: Unresolved issues
- **Conventions**: Style rules, units, terminology

Read at the start of every session.

## Parameter Database

`parameters/` stores structured JSON extracted from sources. Each file is a JSON array of parameter objects.

### 必填字段 (Required Fields)

| 字段 | 类型 | 说明 |
|------|------|------|
| `id` | string | 全局唯一标识 |
| `name` | string | 参数英文名称 |
| `symbol` | string | 参数符号（支持 LaTeX，如 `$D_v$`）|
| `unit` | string | 单位（支持 SI 前缀自动换算）|
| `category` | string | 参数类别（见枚举值）|
| `source_file` | string | 来源文件路径 |
| `confidence` | string | 置信度：`high` / `medium` / `low` |

### category 枚举值

```
crystal_structure | elastic | mechanical | thermodynamic | thermal | physical | irradiation | diffusion | bubble | phase_transformation | surface_energy | microstructure | simulation
```

### 可选字段 (Optional Fields)

| 字段 | 类型 | 说明 | 示例 |
|------|------|------|------|
| `method` | string | 测量/计算方法 | `"XRD"`, `"TEM"`, `"EMTO-CPA"`, `"Tian model"` |
| `region` | string | 样品区域 | `"U-rich"`, `"Nb/Hf-rich"`, `"columnar grain"` |
| `subcategory` | string | 子类别（用于更精确的 validate 范围）| `"diffusion_coefficient"`, `"elastic_modulus"` |
| `note` | string | 备注说明 | 自由文本 |
| `temperature` | string | 温度条件 | `"773 K"`, `"400-800 K"` |
| `material` | string | 材料/合金体系 | `"U-10Mo"`, `"U-6Zr"` |
| `uncertainty` | string | 不确定度 | `"±50%"` |

### JSON 示例

```json
[
  {
    "id": "unique_id",
    "name": "Diffusion Coefficient",
    "symbol": "$D_v$",
    "value_type": "scalar",
    "value": 1.38e-8,
    "unit": "m²/s",
    "category": "diffusion",
    "subcategory": "diffusion_coefficient",
    "temperature": "400-800 K",
    "material": "U-10Mo",
    "method": "TEM",
    "source_file": "summaries/slug.md",
    "confidence": "high",
    "note": "Measured via tracer method"
  },
  {
    "id": "unique_id_2",
    "name": "Elastic Modulus",
    "symbol": "$E$",
    "value_type": "range",
    "value_min": 80,
    "value_max": 120,
    "unit": "GPa",
    "category": "mechanical",
    "subcategory": "elastic_modulus",
    "temperature": "298 K",
    "material": "U-10Mo",
    "method": "EMTO-CPA",
    "source_file": "summaries/slug2.md",
    "confidence": "medium"
  },
  {
    "id": "unique_id_3",
    "name": "Activation Energy",
    "symbol": "$Q$",
    "value_type": "expression",
    "value_expr": "1e-16 to 1e-9",
    "unit": "J",
    "category": "diffusion",
    "subcategory": "activation_energy",
    "temperature": "773 K",
    "material": "U-10Mo",
    "method": "Curtin parameter-free theory",
    "region": "U-rich",
    "source_file": "summaries/slug.md",
    "confidence": "low"
  }
]
```

### Typed Value Schema

`value_type` 字段指示值的类型：

| value_type | 必填字段 | 说明 |
|---|---|---|
| `scalar` | `value` | 单个数值（默认） |
| `range` | `value_min`, `value_max` | 数值范围 |
| `expression` | `value_expr` | 公式、文字描述或无法解析的表达式 |
| `list` | `values` (array) | 离散多个值 |

### 参数质量门禁（Parameter Quality Gate）

参数数据在进入 wiki 前需通过质量门禁：

1. **自动检查**：每次 `ingest` 操作后自动运行 `validate`
2. **报告级别**：
   - 全部 pass → 自动写入 `parameters/`
   - 存在 warn → 写入但标记待审查
   - 存在 fail → 阻断写入，返回修复建议
3. **版本比对**：参数更新时自动运行 `compare`，记录变更历史
4. **定期审计**：`lint` 操作包含参数完整性检查

## Use Cases

- **Research deep-dive** — reading papers on metal fuel swelling over weeks
- **Model parameter database** — structured extraction for model calibration
- **Writing companion** — building knowledge for academic papers
- **Team knowledge base** — shared understanding of fuel behavior

### 质量保障流程（Quality Assurance Workflow）

```
ingest → validate → (pass) → 写入 parameters/
                     → (fail) → 返回修复建议 → 人工审核 → 重新 ingest

参数更新 → compare(v1, v2) → 匹配/新增/修正/冲突/缺失
                                    → 冲突项 → 标注原因 → 人工裁定

textlint → validate + compare → 报告 → log/YYYYMMDD.md
```

**核心原则**：
- 自动检查优先，人工审核兜底
- 所有变更有据可查（log）
- 冲突不静默覆盖，必须标注并等待裁定

## 8. `pipeline` — Lobster 批量 Pipeline

使用 Lobster (OpenClaw typed shell pipeline) 自动化批量 ingest。

### 架构（混合模式）

```
Lobster pipeline 负责:  PDF 转换 → 质量检查 → Validate → 报告
子智能体负责:        Summary + Parameters 生成（需多步推理）
```

### 可用 Pipeline 文件

| 文件 | 用途 | 用法 |
|------|------|------|
| `pipeline/ingest_single_full.lobster` | 单篇完整入库 | `lobster run --file ... --args-json '{"PDF_PATH":"...","SLUG":"..."}'` |
| `pipeline/ingest_batch_v2.lobster` | 批量 PDF 转换 | `lobster run --file ...` |
| `pipeline/batch_convert.py` | 批量 pdftotext 转换 | `BATCH_FILE=batch.json python3 pipeline/batch_convert.py` |
| `pipeline/run_llm_ingest.py` | LLM ingest 包装 | 由 pipeline 或主智能体调用 |
| `pipeline/write_ingest_output.py` | 文件写入辅助 | 由 pipeline 调用 |

### 环境变量

```bash
WIKI_ROOT=/path/to/wiki      # 知识库根目录
BATCH_FILE=/path/to/batch.json # 批量论文列表
PDF_PATH=/path/to/paper.pdf   # 单篇 PDF
SLUG=YYYY_Author_ShortTitle   # 论文 slug
```

### 批量 Ingest 流程

1. **准备候选清单** (`batch.json`):
   ```json
   [{"filename":"...","pdf":"/abs/path.pdf","year":"2025","author":"...","size_kb":1000}]
   ```
2. **PDF 批量转换**: `BATCH_FILE=batch.json python3 pipeline/batch_convert.py`
3. **启动子智能体并行处理**: `sessions_spawn` 2 组 × 4-5 篇
4. **Validate**: `python3 scripts/validate_params.py <wiki-root>/`
5. **质量抽查**: 随机抽取参数文件检查 category/数值合理性

### Lobster .lobster 文件格式

YAML `steps` 结构，`command` 是 shell 命令，`stdin: $step.stdout` 做管道：

```yaml
name: my-pipeline
steps:
  - id: step1
    command: "python3 script.py"
  - id: step2
    command: "python3 process.py"
    stdin: $step1.stdout
```

**注意**: 多行 Python 在 YAML 中必须用单行+分号写法，`>-` 折叠会导致缩进错误。

### 性能基准

| 指标 | 目标 | 实测 |
|------|------|------|
| 单篇 PDF 转换 | < 10s | < 5s |
| 单篇 LLM ingest | < 5 min | ~1-4 min |
| 批量 8 篇（2 组并行）| < 30 min | ~7 min |
| Validate FAIL | 0 | 0 |
| 自动化率 | ≥ 90% | ~95% |

## Phase 1.5 扩展策略补充

当任务是“继续扩展文献覆盖”而不是“修补已有文献”时，优先执行：

1. 先识别当前空白方向（U-Pu-Zr / irradiation creep / FCCI / fission gas release）
2. 先做候选文献清单，再决定下载/转换/ingest
3. 优先找 review / handbook / code-model / PIRT 类型文献，先补领域骨架
4. 每次搜索后记录：标题、年份、主题、URL、可获取性、优先级、是否与现有库重复
5. 不要把“只清理仓库 / 只修 repo / 只改文档”误当成 Phase 1.5 进展

检索与扩展细则见：`references/phase15-source-expansion-guide.md`

## References

- `references/schema-guide.md` — CLAUDE.md template
- `references/article-guide.md` — Writing good wiki articles
- `references/log-guide.md` — Log file conventions
- `references/audit-guide.md` — Audit file format
- `references/phase15-source-expansion-guide.md` — Phase 1.5 source expansion playbook
- `pipeline/` — Lobster pipeline files for automated batch ingest
