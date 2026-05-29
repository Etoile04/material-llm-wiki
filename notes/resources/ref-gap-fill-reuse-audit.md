# ref-gap-fill 可复用资产审计

> PARA: Resource | 关联项目: [ref-gap-fill](../projects/nucpot/ref-gap-fill.md)

## 可直接复用（无需修改）

| 资产 | 位置 | 能力 | 复用于 |
|------|------|------|--------|
| ontofuel Python API | `workspace-extractor/src/ontofuel/` | Segmenter + Extractor + Merger + OntologyUpdater | 慢线 |
| llm-wiki batch_extract.py | `skills/llm-wiki/scripts/` | 去重、schema 验证、子 agent prompt 生成 | 慢线 |
| llm-wiki normalize_typed_values.py | `skills/llm-wiki/scripts/` | 单位/类型标准化 | 基础设施 |
| llm-wiki compare_params.py | `skills/llm-wiki/scripts/` | 单位换算因子表 | 基础设施 |
| llm-wiki zotero_sync.py | `skills/llm-wiki/scripts/` | Zotero→知识库同步、PDF 检测 | 慢线触发 |
| Lobster pipeline | `skills/llm-wiki/pipeline/*.lobster` | PDF→文本→质量检查 | 快线+慢线 |
| ref-gap-fill SKILL.md | `skills/ref-gap-fill/SKILL.md` | Step 1-7 完整流程 | 重构为编排协议 |
| 验证 API CRUD | ThinkStation `:8001/api/references` | reference_values 读写 | 基础设施 |
| NFMD RPC | Supabase `search_parameters` | 参数搜索 | L2 缓存 |

## 需要适配

| 资产 | 适配工作 | 工作量 |
|------|----------|--------|
| llm-wiki 68 条中文参数 | 中文名→英文映射 + 单位转换 | 小 |
| ontofuel 本体 | 新增 C11/C12/C44/C33 属性 | 小 |
| ref-gap-fill 提取 prompt | 追加 confidence + 分级逻辑 | 小 |

## 必须新建

| 资产 | 说明 |
|------|------|
| property-mapping.json | L1↔L2↔L3 物性名映射 |
| cache-query.py | 三级缓存统一查询 |
| write-ref-value.py | 分级写入 + 质量门控 |
| adapter-nfmd.py | NFMD → reference_values 转换 |
| nucpot-db / nucpot-librarian 配置 | openclaw.json agent 新增 |
| librarian-search / librarian-extract SKILL | 快线技能 |
| 慢线 cron job | 定时触发 |

## 数据资产

| 数据源 | 记录数 | 可映射 | 状态 |
|--------|--------|--------|------|
| reference_values (L1) | 23 | 23 | ✅ 可用 |
| NFMD parameters (L2) | 6,981 | ~50-100 | ⚠️ 需映射 |
| llm-wiki params (L3a) | 14,320 | 68 | ⚠️ 中文命名 |
| ontofuel 本体 (L3b) | 279 props | ~20 | ⚠️ 缺 Cij |

**预估**：三级缓存打通后 reference_values 可从 23 → ~150 条。

## 已确认的 llm-wiki 可用参数（部分）

| 体系 | 物性 | 值 | 来源 |
|------|------|-----|------|
| U-7wt%Mo (BCC) | 晶格常数 | 0.343 nm | Hu 2016 |
| γ-U | C11/C12/C44 | 94/154/34 GPa | Mei 2016 |
| U-7Mo | C11/C12/C44 | 173/138/50 GPa | Mei 2016 |
| bcc Mo | C11/C12/C44 | 466/157/103 GPa | Mei 2016 |
