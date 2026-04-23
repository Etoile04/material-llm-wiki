# 材料知识库技能与工作流开发计划

> **版本**: v1.0  
> **日期**: 2026-04-21  
> **状态**: 执行中  
> **负责人**: Wenjie Li + Lily 🦀

---

## 一、项目目标

构建一套 **AI 驱动的材料知识库自动化体系**，实现从文献检索、PDF 解析、知识提取、参数校验到比对入库的全流程自动化，最终服务于核燃料性能代码的模型参数标定。

### 核心指标

| 指标 | 当前值 | 目标值 |
|------|--------|--------|
| 文献覆盖量 | 47 篇 | 100+ 篇 |
| 参数总量 | 1213 条 | 3000+ 条 |
| validate FAIL | 0 | 0 |
| 公式覆盖率 | 100% | 100% |
| 入库自动化 | 手动编排 | 一键触发 |
| 单篇入库耗时 | ~15 min（手动） | ~5 min（自动化） |

---

## 二、已完成工作（2026-04-20）

### Phase A：参数质量修复
- 补全 352 条空 ID（12 个文件）
- 补全缺失 `source_file`、`symbol` 字段
- 消除跨文件 ID 冲突（kim 系列前缀加年份）
- validate 脚本支持嵌套 JSON 和排除报告文件
- **效果**：FAIL 297 → **0**

### Phase B：Typed Value Schema
- 新增 `value_type` 字段，支持 scalar/range/expression/list 四种类型
- `normalize_typed_values.py`：批量迁移历史数据（1213 条）
- `validate_params.py`：支持 typed value 校验（range 检查上下界，expression 跳过数值校验）
- `compare_params.py`：支持范围比较、显式论文映射表
- SKILL.md 提取模板更新：新数据直接带 value_type
- **效果**：magnitude FAIL 16 → **0**，无需事后 normalize

### Phase C：公式覆盖修复
- 28 篇缺公式 summary 批量补充（4 子智能体并行，3 分钟完成）
- SKILL.md 新增公式强制要求：模型类论文必须含 `## Key Equations`
- MinerU 转换命令显式标注 `-f true -t true`
- **效果**：公式覆盖率 40% → **100%**

### Phase D：v2 同源验证
- 从 47 篇中选取 15 篇（覆盖 5 种文献类型），用改进后技能从头重跑
- **验证结果**：

| 指标 | v1 首次 | v2 改进技能 |
|------|---------|-----------|
| validate FAIL | 297 | **0** |
| 公式覆盖率 | 40% | **100%** |
| value_type 覆盖 | 0% | **100%**（直接产出） |
| normalize 迁移 | 1213 条 | **0 条** |
| 空参数文件 | 6 篇 | **0 篇** |

---

## 三、后续开发计划

### Phase 1.5：文献覆盖面扩展（2-3 周）

> **目标**：从 47 篇扩展到 100+ 篇，覆盖金属燃料辐照肿胀的主要文献
> **同时**：在实战中验证改进后技能的稳定性，收集改进点

#### 1.5.1 文献源梳理（第 1-2 天）

| 任务 | 方法 | 产出 |
|------|------|------|
| 梳理现有 Zotero 库中金属燃料文献 | `zotero_search_real_skill.py` | 文献清单 A |
| 搜索 U-Pu-Zr 肿胀经典文献 | web_search + Semantic Scholar | 文献清单 B |
| 搜索 U-Mo 肿胀近 5 年新文献 | web_search (2020-2026) | 文献清单 C |
| 检查已有 handbooks 数据 | handbooks/ 目录 | 文献清单 D |
| 去重合并 | 对比 v1 已有 47 篇 | **候选新增清单** |

**验收标准**：候选新增 ≥ 60 篇，覆盖以下空白区域：
- U-Pu-Zr 三元合金（目前仅 ~5 篇）
- 辐照蠕变（irradiation creep）
- FCCI（fuel-cladding chemical interaction）
- 燃料再结晶（recrystallization kinetics）
- 裂变气体释放（fission gas release）

#### 1.5.2 批量 PDF 获取与转换（第 3-5 天）

| 任务 | 方法 | 注意事项 |
|------|------|---------|
| 获取 PDF | Zotero 导出 + 开放获取搜索 | 优先 OA，记录无法获取的 |
| MinerU 批量转换 | `mineru -f true -t true -l en -b pipeline` | 公式识别必须开启 |
| 转换质量检查 | grep `$$` 检查公式覆盖率 | < 70% 的需重转或用 pdftotext 兜底 |
| 建立 raw/ 目录 | 每个 PDF → `raw/mineru/<paper_name>/*.md` | 文件名规范化 |

**验收标准**：转换成功率 ≥ 90%，公式覆盖率 ≥ 70%（源 MD 级别）

#### 1.5.3 分批提取（第 6-14 天）

**策略**：每天处理 1 批（10-15 篇），分 3 个子智能体并行

| 批次 | 主题 | 预计篇数 | 时间 |
|------|------|---------|------|
| Batch 1 | U-Pu-Zr 经典 + 率理论 | 15 | Day 6 |
| Batch 2 | U-Mo 相场 + 气泡模型 | 15 | Day 7-8 |
| Batch 3 | 实验表征 + TEM/SEM | 15 | Day 9-10 |
| Batch 4 | 燃料性能代码 + 工程模型 | 15 | Day 11-12 |
| Batch 5 | 补漏 + 无法分类的 | 剩余 | Day 13-14 |

**每批执行流程**：
1. 子智能体并行 ingest（summary + parameters，按 SKILL.md 模板）
2. 运行 `validate_params.py` → FAIL 必须 = 0
3. 检查公式覆盖率 → 必须 100%
4. 抽样人工审查 2-3 篇质量
5. 如有问题，立即暂停修复后再继续

**质量控制关卡**：
- ⛔ validate FAIL > 0 → 暂停，修复后继续
- ⛔ 公式覆盖率 < 100% → 暂停，补充后继续
- ⛔ 参数文件为空 → 暂停，重新提取
- ⚠️ WARN > 30% → 记录，继续

#### 1.5.4 每日审查与改进记录（贯穿）

| 任务 | 频率 | 产出 |
|------|------|------|
| 统计当日入库量、validate 结果 | 每天 | `log/YYYYMMDD.md` |
| 记录遇到的问题和修复方式 | 每次 | 更新 SKILL.md 或脚本 |
| 抽样人工审查 | 每天 2-3 篇 | 审查笔记 |
| 更新 `CLAUDE.md` 术语表 | 按需 | 新增术语 |

#### 1.5.5 Phase 1.5 验收标准

| 指标 | 验收条件 |
|------|---------|
| 文献总量 | ≥ 100 篇 |
| 参数总量 | ≥ 2500 条 |
| validate FAIL | 0 |
| 公式覆盖率（summary 级） | 100% |
| value_type 覆盖 | 100% |
| 人工审查通过率 | ≥ 90% |

---

### Phase 2：自动化 Pipeline（2-3 周）

> **前置条件**：Phase 1.5 完成，技能稳定，入库流程标准化

#### 2.1 Lobster Ingest Pipeline

```
┌─────────────────────────────────────────────────────────────┐
│                    ingest-pipeline.lobster                   │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐               │
│  │ 1. Scan  │───▶│ 2. MinerU│───▶│ 3. Extract│              │
│  │  PDFs    │    │  Convert │    │  Params   │              │
│  └──────────┘    └──────────┘    └─────┬────┘               │
│       │                                │                     │
│       │ 增量检测                        │                     │
│       ▼                                ▼                     │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐               │
│  │ 6. Report│◀───│ 5. Compare│◀───│ 4. Validate│             │
│  │  & Commit│    │  v1 vs v2│    │  Quality  │──▶ ⏸️ 审批    │
│  └──────────┘    └──────────┘    └──────────┘               │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

**节点说明**：

| 节点 | 功能 | 输入 | 输出 | 失败策略 |
|------|------|------|------|---------|
| 1. Scan | 检测新 PDF（增量） | PDF 目录 | 新文件列表 | 跳过空列表 |
| 2. MinerU | PDF → Markdown（含公式） | PDF 文件 | `.md` 文件 | pdftotext 兜底 |
| 3. Extract | 子智能体提取 summary + 参数 | `.md` 文件 | summary + JSON | 重试 1 次 |
| 4. Validate | 运行 validate_params.py | JSON 文件 | 通过/失败报告 | ⏸️ 暂停审批 |
| 5. Compare | 运行 compare_params.py | v1 + v2 目录 | 比对报告 | 跳过（无 v1 时） |
| 6. Report | 生成报告 + git commit | 全部产出 | Markdown 报告 | 必须成功 |

**人工审批节点**：
- validate FAIL > 0：暂停，展示失败详情，人工决定修复或跳过
- MinerU 转换失败 > 10%：暂停，检查环境
- 抽样审查不通过：暂停，批量修复

#### 2.2 增量更新 Workflow

```
incremental-update.lobster
├── 输入：Zotero collection URL 或 PDF 目录
├── 检测：哪些文献尚未入库
├── 执行：ingest-pipeline（仅处理新增）
└── 输出：增量比对报告
```

#### 2.3 验收标准

| 指标 | 验收条件 |
|------|---------|
| 单篇入库耗时 | ≤ 5 分钟（从 PDF 到 validated JSON） |
| 批量 10 篇耗时 | ≤ 30 分钟 |
| 自动化率 | ≥ 90%（人工仅审批） |
| 失败恢复 | 支持从失败节点续跑 |

---

### Phase 3：高级集成（2-4 周）

> **前置条件**：Phase 2 完成，pipeline 稳定运行

#### 3.1 Zotero MCP 集成

| 功能 | 描述 |
|------|------|
| 自动同步 | Zotero 新增文献 → 自动触发 ingest |
| 全文搜索 | 从 Zotero 搜索文献，支持语义/关键词 |
| 标签管理 | 自动为入库文献打标签 |
| PDF 自动下载 | Zotero 有 PDF 的自动拉取 |

#### 3.2 Supabase 参数库集成

| 功能 | 描述 |
|------|------|
| 参数入库 | validated JSON → Supabase 表 |
| 查询接口 | API 查询参数（按材料/温度/类别） |
| 版本管理 | 参数变更记录 |
| 数据可视化 | 参数分布图表 |

#### 3.3 定时巡检

| 功能 | 频率 | 描述 |
|------|------|------|
| 全库 validate | 每周日 | 检查参数质量退化 |
| 文献更新检查 | 每周一 | 检测 Zotero 新增文献 |
| Lint | 每两周 | 死链/孤立页检查 |
| 备份 | 每月 | 知识库快照 |

---

## 四、技术架构

```
┌─────────────────────────────────────────────────┐
│                   用户交互层                      │
│          Feishu DM / Web UI / CLI               │
├─────────────────────────────────────────────────┤
│                  编排层（Lobster）                 │
│    ingest-pipeline / incremental-update          │
├─────────────────────────────────────────────────┤
│                   技能层（llm-wiki）               │
│  compile / ingest / query / lint / audit         │
│  validate / compare                              │
├─────────────────────────────────────────────────┤
│                   脚本层                          │
│  validate_params.py / compare_params.py          │
│  normalize_typed_values.py / lint.py             │
├─────────────────────────────────────────────────┤
│                   数据层                          │
│  summaries/ / parameters_v2/ / wiki/ / raw/      │
├─────────────────────────────────────────────────┤
│                 外部集成                          │
│  Zotero MCP / MinerU / Supabase / GitHub        │
└─────────────────────────────────────────────────┘
```

---

## 五、里程碑与时间线

```
2026-04    ████████ Phase A-D (已完成)
2026-04-21 ▶ Phase 1.5 开始
2026-05-05 ├─ 1.5.1 文献梳理 (2天)
2026-05-07 ├─ 1.5.2 PDF转换 (3天)
2026-05-14 ├─ 1.5.3 分批提取 (9天)
2026-05-14 └─ 1.5.4 验收 → 进入 Phase 2
2026-05-15 ▶ Phase 2 开始
2026-05-22 ├─ 2.1 Lobster Pipeline (1周)
2026-05-29 ├─ 2.2 增量更新 (3天)
2026-05-31 └─ 2.3 验收 → 进入 Phase 3
2026-06-01 ▶ Phase 3 开始
2026-06-15 ├─ 3.1 Zotero集成 (1周)
2026-06-22 ├─ 3.2 Supabase集成 (1周)
2026-06-28 └─ 3.3 验收 → 交付
```

---

## 六、风险与缓解

| 风险 | 概率 | 影响 | 缓解措施 |
|------|------|------|---------|
| MinerU 转换质量不稳定 | 中 | 公式缺失 | pdftotext 兜底 + 事后公式补充 |
| LLM 提取质量波动 | 中 | 参数不准 | validate 门禁 + 抽样人工审查 |
| PDF 无法获取 | 中 | 文献缺口 | 记录缺口清单，优先 OA 文献 |
| 子智能体并发限制 | 低 | 批量耗时 | 控制并发 ≤ 4，错峰执行 |
| Zotero API 变更 | 低 | 搜索失败 | 本地缓存 + 手动导入备选 |

---

## 七、进展报告

### 7.1 Phase 1.5 进展（2026-04-22 ~ 04-23）

#### §1.5.1 文献源梳理 ✅ 完成

- Zotero "Metal fuel" collection 及 10 个子 collection 全部扫描
- 去重后 **135 篇**，已入库 31 篇，新增候选 **104 篇**（远超 60 篇目标）
- 产出：`plans/phase1.5-candidate-list.md`（18KB）
- 本地 Zotero 实际可用 PDF：~550 篇燃料相关

#### §1.5.2-1.5.3 批量 Ingest ✅ 进行中（3 批完成）

| 批次 | 论文数 | 参数数 | 公式数 | 耗时 | Validate |
|------|--------|--------|--------|------|----------|
| Batch 1 (U-Zr) | 5 | 121 | 11 | 58s | 0 FAIL |
| Batch 2 (混合) | 8 | 88 | 21 | ~7min | 0 FAIL |
| Batch 3 (2025-2026) | 7 | 125 | 35 | ~7min | 0 FAIL |
| **合计** | **20** | **334** | **67** | — | **0 FAIL** |

#### §1.5.5 Phase 1.5 验收标准检查

| 指标 | 验收条件 | 当前值 | 状态 |
|------|---------|--------|------|
| 文献总量 | ≥ 100 篇 | **95** | 🔄 差 5 篇 |
| 参数总量 | ≥ 2500 条 | **1841** | 🔄 差 659 |
| validate FAIL | 0 | **0** | ✅ |
| 公式覆盖率 | 100% | **100%** | ✅ |
| value_type 覆盖 | 100% | **100%** | ✅ |
| 人工审查通过率 | ≥ 90% | **100%** | ✅ |

---

### 7.2 Phase 2 进展（2026-04-23）

#### §2.1 Lobster Ingest Pipeline ✅ 已验证

**完成内容**：
1. ✅ Lobster `.lobster` 文件格式研究（YAML steps 结构）
2. ✅ `ingest_single_v2.lobster` — 单篇 MVP（PDF→pdftotext→质量检查→报告）
3. ✅ `ingest_single_full.lobster` — 单篇端到端（+validate+报告）
4. ✅ `ingest_batch_v2.lobster` — 批量 PDF 转换
5. ✅ `batch_convert.py` — 批量转换脚本
6. ✅ `run_llm_ingest.py` — LLM 子智能体包装
7. ✅ `write_ingest_output.py` — 文件写入辅助
8. ✅ SKILL.md 新增 §8 pipeline 操作文档
9. ✅ 已推送到 GitHub（commit `50ae032`）

**架构决策**：
- 采用**混合模式**：Lobster 负责 PDF 转换 + 校验 + 报告，LLM 部分委托子智能体
- 原因：`openclaw.invoke` 需要 CLAWD_URL+CLAWD_TOKEN（未配置），且 `llm_task.invoke` 仅支持无状态 JSON 输出
- `approve` 门禁在非交互模式下暂用 validate 报告替代

**§2.2 增量更新 Workflow** — ⏳ 未启动

尚未设计 `incremental-update.lobster`。当前增量检测通过 Python 脚本（文件名匹配 + slug 去重）实现。

#### §2.3 Phase 2 验收标准检查

| 指标 | 验收条件 | 当前值 | 状态 |
|------|---------|--------|------|
| 单篇入库耗时 | ≤ 5 min | **~1-4 min** | ✅ |
| 批量 10 篇耗时 | ≤ 30 min | **~7 min (8篇)** | ✅ |
| 自动化率 | ≥ 90% | **~95%** | ✅ |
| 失败恢复 | 支持从失败节点续跑 | **部分**（Lobster resume 未集成） | 🔄 |

---

### 7.3 知识库现状（2026-04-23 15:00）

| 指标 | Phase A-D 结束时 | Phase 1.5+2 当前值 | 变化 |
|------|-----------------|----------------|------|
| 文献覆盖量（summaries） | 67 | **95** | +28 |
| 参数文件 | 67 | **91** | +24 |
| 参数条数 | ~1213 | **1841** | +628 |
| Wiki 页面（概念+实体） | 30 | **30** | — |
| KaTeX 块级公式 | ~100 | **454** | +354 |
| Raw papers | — | **71** | — |
| Validate FAIL | 0 | **0** | ✅ |

### 7.4 待解决问题

| 问题 | 优先级 | 状态 |
|------|--------|------|
| 75 个 lint issues（DEAD_LINK + ORPHAN） | 中 | Phase 1.5 完成后统一修复 |
| literature_index.json 旧格式（3637条缺 required_fields） | 中 | 待清理 |
| 47 篇旧 summaries 中文化翻译 | 低 | 长期任务 |
| `openclaw.invoke` 需 CLAWD_URL+CLAWD_TOKEN | 低 | gateway 未配置 token |
| Lobster resume（失败续跑） | 中 | Phase 2 完善项 |
| `incremental-update.lobster` | 中 | Phase 2 下一步 |

### 7.5 下一步计划

**Phase 1.5 收尾**（~1天）：
- [ ] 再跑 1 批（~5 篇），达到 100 篇验收线
- [ ] 修复 75 个 lint issues

**Phase 2 完善**（~3天）：
- [ ] 设计 `incremental-update.lobster`
- [ ] 集成 `openclaw.invoke`（需配置 gateway token）
- [ ] 实现 Lobster resume 失败续跑
- [ ] 添加 `approve` 交互审批（交互模式）

---

## 八、当前仓库与交付物

| 交付物 | 位置 | 状态 |
|--------|------|------|
| llm-wiki 技能 | `skills/llm-wiki/` | ✅ 已完成 |
| Lobster Pipeline | `skills/llm-wiki/pipeline/` | ✅ 已完成 |
| 知识库（95 篇） | `data/fuel_swelling_wiki/` | 🔄 Phase 1.5 进行中 |
| v2 验证集（15 篇） | `data/fuel_swelling_wiki_v2/` | ✅ 已完成 |
| GitHub 仓库 | `Etoile04/material-llm-wiki` | ✅ 已推送 |
| 开发计划 | `plans/llm-wiki-development-plan.md` | ✅ 本文档 |

---

*最后更新：2026-04-23 15:07 CST*
