# 材料知识库技能开发计划（含路线图）

> **版本**: v2.0  
> **日期**: 2026-04-23  
> **状态**: Phase 1.5 核心完成，Phase 2 进行中  
> **仓库**: https://github.com/Etoile04/material-llm-wiki  
> **负责人**: Wenjie Li + AI Agent

---

## 一、项目目标

构建一套 **AI 驱动的材料知识库自动化体系**，实现从文献检索、PDF 解析、知识提取、参数校验到比对入库的全流程自动化，最终服务于核燃料性能代码（JSRT 等）的模型参数标定。

### 核心指标

| 指标 | 初始值 | 当前值 | 目标值 |
|------|--------|--------|--------|
| 文献覆盖量 | 47 篇 | **107 篇** | 120+ 篇 |
| 参数总量 | 1213 条 | **1920 条** | 2500+ 条 |
| validate FAIL | 297 | **0** | 0 |
| 公式覆盖率 | 40% | **100%** | 100% |
| 入库自动化 | 手动编排 | **~95%** | 一键触发 |
| 单篇入库耗时 | ~15 min | **~3 min** | ≤ 5 min |
| DEAD_LINK | 99 | **0** | 0 |

---

## 二、已完成工作

### Phase A-D：质量修复（2026-04-20）✅

- **Phase A**：参数质量修复 — 补全 352 条空 ID，消除跨文件 ID 冲突，FAIL 297→0
- **Phase B**：Typed Value Schema — scalar/range/expression/list 四类型，magnitude FAIL 16→0
- **Phase C**：公式覆盖修复 — 28 篇缺公式 summary 批量补充，覆盖率 40%→100%
- **Phase D**：v2 同源验证 — 15 篇从头重跑，验证技能改进效果

### Phase 1.5：文献覆盖面扩展（2026-04-22 ~ 04-23）✅ 核心完成

**§1.5.1 文献源梳理**
- Zotero 全量扫描，135 篇去重，104 篇候选新增
- 本地 Zotero ~550 篇燃料相关 PDF 可用

**§1.5.2-1.5.3 批量 Ingest（5 批完成）**

| 批次 | 论文数 | 参数数 | 公式数 | 耗时 | 子智能体 |
|------|--------|--------|--------|------|---------|
| Batch 1 (U-Zr) | 5 | 121 | 11 | 58s | 单智能体 |
| Batch 2 (混合) | 8 | 88 | 21 | ~7min | 2 组并行 |
| Batch 3 (2025-2026) | 7 | 125 | 35 | ~7min | 2 组并行 |
| Batch 4 (高价值) | 8 | 129 | 23 | ~9min | 2 组并行 |
| Batch 5 (模型/综述) | 4 | 79 | — | ~6min | 3 组并行 |
| **合计** | **32** | **542** | **90** | — | **0 FAIL** |

**Phase 1.5 验收**：

| 指标 | 验收条件 | 当前值 | 状态 |
|------|---------|--------|------|
| 文献总量 | ≥ 100 | **107** | ✅ |
| 参数总量 | ≥ 2500 | **1920** | 🔄 77% |
| validate FAIL | 0 | **0** | ✅ |
| 公式覆盖率 | 100% | **100%** | ✅ |
| value_type 覆盖 | 100% | **100%** | ✅ |

**Lint 修复**：99 DEAD_LINK → 0，113 处全部修复

### Phase 2：自动化 Pipeline（2026-04-23）🔄 进行中

**已完成**：
- ✅ `ingest_single_v2.lobster` — 单篇入库（PDF→pdftotext→质量检查→报告）
- ✅ `ingest_single_full.lobster` — 单篇端到端（+validate+报告）
- ✅ `ingest_batch_v2.lobster` — 批量 PDF 转换
- ✅ `batch_convert.py` / `run_llm_ingest.py` / `write_ingest_output.py`
- ✅ SKILL.md §8 pipeline 操作文档
- ✅ 架构决策：Lobster 做编排+门禁，LLM 部分委托子智能体

**验收**：

| 指标 | 目标 | 当前 | 状态 |
|------|------|------|------|
| 单篇入库 | ≤ 5min | ~1-4min | ✅ |
| 批量 10 篇 | ≤ 30min | ~7min | ✅ |
| 自动化率 | ≥ 90% | ~95% | ✅ |
| 失败恢复 | 支持 | 部分 | 🔄 |

---

## 三、路线图（2026 Q2）

```
2026-04  ████████████████ Phase A-D + Phase 1.5 + Phase 2 核心
         │
         ├─ [DONE] Phase A-D 质量修复（04-20）
         ├─ [DONE] Phase 1.5 文献扩展 107 篇（04-22~23）
         ├─ [DONE] Phase 2 Lobster pipeline 验证（04-23）
         ├─ [DONE] Lint 修复 DEAD_LINK 清零（04-23）
         │
2026-05  ──────────────── Phase 1.5 收尾 + Phase 2 完善 + Phase 3 启动
         │
         ├─ [PLAN] Week 1 (05-01 ~ 05-07)
         │   ├─ Batch 6-8: 再入库 15-20 篇高参数密度论文 → 参数 2500+
         │   ├─ incremental-update.lobster 设计与验证
         │   └─ ORPHAN 页面修复（compile 交叉引用）
         │
         ├─ [PLAN] Week 2 (05-08 ~ 05-14)
         │   ├─ openclaw.invoke 集成（配置 gateway token）
         │   ├─ Lobster resume 失败续跑
         │   ├─ approve 交互审批（交互模式）
         │   └─ Phase 2 完整验收
         │
         ├─ [PLAN] Week 3 (05-15 ~ 05-21)
         │   ├─ Phase 3.1: Zotero MCP 自动同步
         │   ├─ Phase 3.2: Supabase 参数库集成
         │   └─ 参数查询 API 设计
         │
         └─ [PLAN] Week 4 (05-22 ~ 05-31)
             ├─ Phase 3.3: 定时巡检（validate/lint/备份）
             ├─ 旧 summaries 中文化翻译（47 篇）
             ├─ literature_index.json 清理（3637 条旧格式）
             └─ 知识库 v3.0 交付验收
```

### 里程碑

| 里程碑 | 日期 | 交付物 |
|--------|------|--------|
| M1: Phase 1.5 验收 | 2026-04-23 ✅ | 107 summaries, 1920 params |
| M2: 参数 2500+ | 2026-05-07 | 120+ summaries, 2500+ params |
| M3: Phase 2 验收 | 2026-05-14 | 完整自动化 pipeline |
| M4: Phase 3 验收 | 2026-05-31 | Supabase + Zotero + 定时巡检 |

---

## 四、技术架构

```
┌─────────────────────────────────────────────────────┐
│                    用户交互层                         │
│          Feishu DM / Web UI / CLI                    │
├─────────────────────────────────────────────────────┤
│                  编排层（Lobster）                     │
│    ingest-pipeline / incremental-update              │
│    PDF转换 → 质量检查 → LLM提取 → Validate → 报告     │
├─────────────────────────────────────────────────────┤
│                   技能层（llm-wiki）                   │
│  compile / ingest / query / lint / audit             │
│  validate / compare / scaffold                       │
├─────────────────────────────────────────────────────┤
│                   脚本层                              │
│  validate_params.py / compare_params.py              │
│  batch_convert.py / run_llm_ingest.py                │
│  normalize_typed_values.py / lint.py / scaffold.py   │
├─────────────────────────────────────────────────────┤
│                   数据层                              │
│  summaries/ (107) / parameters/ (95) / wiki/         │
│  concepts/ (15) / entities/ (15) / raw/              │
├─────────────────────────────────────────────────────┤
│                 外部集成                              │
│  Zotero MCP / MinerU / Supabase / GitHub             │
└─────────────────────────────────────────────────────┘
```

---

## 五、待解决问题

| 问题 | 优先级 | 计划时间 |
|------|--------|---------|
| 参数冲刺 1920→2500 | 高 | 05-01~05-07 |
| ORPHAN 页面修复（~20 篇） | 中 | 05-01~05-07 |
| `incremental-update.lobster` 设计 | 中 | 05-01~05-07 |
| `openclaw.invoke` 需 gateway token | 中 | 05-08~05-14 |
| Lobster resume 失败续跑 | 中 | 05-08~05-14 |
| literature_index.json 清理（3637条） | 低 | 05-22~05-31 |
| 旧 summaries 中文化翻译（47篇） | 低 | 05-22~05-31 |

---

## 六、风险与缓解

| 风险 | 概率 | 影响 | 缓解措施 |
|------|------|------|---------|
| MinerU 转换质量不稳定 | 中 | 公式缺失 | pdftotext 兜底 + 事后公式补充 |
| LLM 提取参数格式错误 | 中 | JSON 解析失败 | validate 门禁 + 格式修复子智能体 |
| PDF 无法获取 | 中 | 文献缺口 | 记录缺口清单，优先 OA 文献 |
| 子智能体并发限制 | 低 | 批量耗时 | 控制并发 ≤ 4，错峰执行 |
| Zotero API 变更 | 低 | 搜索失败 | 本地缓存 + 手动导入备选 |

---

## 七、仓库文件清单

```
skills/llm-wiki/
├── SKILL.md                          # 技能主文档（20KB）
├── pipeline/
│   ├── ingest_single_v2.lobster      # 单篇入库 MVP
│   ├── ingest_single_full.lobster    # 单篇完整入库
│   └── ingest_batch_v2.lobster       # 批量 PDF 转换
├── scripts/
│   ├── batch_convert.py              # 批量 PDF→TXT
│   ├── run_llm_ingest.py             # LLM 子智能体包装
│   ├── write_ingest_output.py        # 文件写入辅助
│   ├── validate_params.py            # 参数校验（17KB）
│   ├── compare_params.py             # 参数比对
│   ├── normalize_typed_values.py     # 类型归一化
│   ├── lint.py                       # 死链/孤立页检查
│   ├── scaffold.py                   # 知识库脚手架
│   ├── schema_input.json             # 输入 schema
│   └── schema_parameter.json         # 参数 schema
├── references/
│   ├── article-guide.md              # 摘要写作指南
│   ├── audit-guide.md                # 审计指南
│   ├── log-guide.md                  # 日志格式指南
│   ├── schema-guide.md               # Schema 说明
│   └── phase15-source-expansion-guide.md  # 文献扩展指南
└── plans/
    └── llm-wiki-development-plan.md  # 本文档
```

---

## 八、GitHub 提交历史

| Commit | 日期 | 说明 |
|--------|------|------|
| `d4e5a9f` | 04-23 | 清理冗余文件（v1 pipeline + 重复 schema） |
| `fb1af31` | 04-23 | 同步 pipeline 文件 |
| `ad52fa6` | 04-23 | Phase 1.5 Batch 4-5 + lint 修复 |
| `21f109b` | 04-23 | 修复 lint.py 崩溃 |
| `8cfda4b` | 04-23 | 移除硬编码路径，修复 write_ingest_output.py |
| `aa6d2b9` | 04-23 | 改进 validate 范围检查 |
| `fff6dc4` | 04-23 | 添加缺失 schema 文件 |
| `50ae032` | 04-23 | Lobster pipeline 批量入库自动化 |
| `5b56edf` | 04-22 | Zotero MCP 集成 + schema 约束 |
| `15f6717` | 04-22 | validate 单位感知 + lint 锚点修复 |
| `f31f029` | 04-21 | Quick start + MIT license |
| `d742e15` | 04-21 | 公开仓库结构 |

---

*最后更新：2026-04-23 22:40 CST*
