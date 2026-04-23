# Phase 2 — 知识库质量提升与自动化

**日期**: 2026-04-22  
**前置条件**: Phase 1.5 ✅ 已完成（1921 参数 / 72 摘要 / 120 raw）  
**预估工期**: 3-5 天

---

## 一、现状诊断

### 1.1 数据健康度

| 指标 | 数值 | 问题 |
|------|------|------|
| 摘要文件 | 72 | 8 篇缺参数 |
| 参数文件 | 71 | 7 篇缺摘要（slug 不匹配） |
| 概念页 | 3 | 严重不足（应有 15-20） |
| 实体页 | 8 | 不足（应有 12-15） |
| CLAUDE.md | 停留在 2026-04-19 | 未更新 Phase 1.5 成果 |
| Research Gaps | 6 条 | 3 条已被 Phase 1.5 解决但未关闭 |
| parameter_database_v2.json | 1001 条 | 落后于当前 1921 条（未同步） |
| literature_index.json | 103 条 | 可能过时 |

### 1.2 核心问题

1. **知识图谱稀疏**: concepts/ 只有 3 页，entities/ 只有 8 页，大量论文知识只存在 summary+parameters 中，没有被提炼和交叉关联
2. **slug 不一致**: 7 个参数文件与摘要文件 slug 不匹配（可能是 Batch D 重命名导致）
3. **聚合数据过时**: `parameter_database_v2.json` 停留在 1001 条，实际已有 1921 条
4. **Category 分布失衡**: fuel_performance 占 76%，需要重新审阅细分
5. **CLAUDE.md 过时**: Research Gaps 1/2/3 已解决但未关闭，Current Articles 未更新

---

## 二、Phase 2 目标

### 总体目标
从"文献堆积"升级到"知识提炼"——让知识库不仅是论文仓库，而是一个可查询、可推理、可交叉引用的结构化知识图谱。

### 交付标准

| # | 目标 | 验收条件 |
|---|------|---------|
| G1 | 数据一致性 | 所有 slug 一致，聚合数据同步 |
| G2 | 知识图谱充实 | concepts ≥ 15, entities ≥ 15 |
| G3 | Category 精细化 | fuel_performance 占比 < 50% |
| G4 | CLAUDE.md 更新 | Research Gaps / Open Questions / Current Articles 全部更新 |
| G5 | 自动化 pipeline | ingest 流程可通过 Lobster pipeline 一键执行 |

---

## 三、分阶段执行计划

### Phase 2.1: 数据一致性修复（预估 1-2 小时）

#### 2.1.1 Slug 不匹配修复
- 修复 7 个参数文件缺摘要的问题（重命名 slug 使其匹配）
- 补全 8 个摘要缺参数的问题（提取或标记为"无需参数"）
- 验证 1:1 映射

#### 2.1.2 聚合数据同步
- 重新生成 `parameter_database_v2.json`（从 71 个参数文件合并）
- 更新 `literature_index.json`（反映 Phase 1.5 新增的 17 篇）
- 更新 `wiki/index.md`（反映 72 篇摘要）

#### 2.1.3 CLAUDE.md 更新
- Current Articles: 更新到 72 summaries, 8 concepts, 8 entities
- Research Gaps: 关闭已解决的（#1 Redistribution, #3 FCCI），更新剩余
- Open Questions: 补充新问题
- Recent Activity: 记录 Phase 1.5 成果

---

### Phase 2.2: 知识图谱充实（预估 4-6 小时）

#### 2.2.1 概念页扩展（目标: 15+ 页）

从 Phase 1.5 四方向提炼概念：

**FCCI 方向**（新增 3 页）:
- `FuelCladdingChemicalInteraction.md` — FCCI 机理综述
- `LanthanideDiffusionInSteel.md` — 镧系元素在包壳中的扩散
- `EutecticFormationFuelCladding.md` — 燃料-包壳共晶形成

**FGR 方向**（新增 2 页）:
- `FissionGasReleaseModels.md` — FGR 模型对比（GRSIS / FEAST / BISON）
- `GasBubbleCoalescence.md` — 气泡聚合与连通

**Irradiation Creep 方向**（新增 2 页）:
- `IrradiationCreepMechanisms.md` — 辐照蠕变机理
- `CreepSwellingCoupling.md` — 蠕变-肿胀耦合

**Redistribution 方向**（新增 3 页）:
- `ConstituentRedistribution.md` — 组元再分布综述
- `SoretEffectInMetallicFuels.md` — 热扩散（Soret 效应）
- `PhaseFieldModelingRedistribution.md` — 再分布相场建模

**通用**（新增 2 页）:
- `FuelPerformanceCodes.md` — BISON / FEAST-METAL / LIFE-METAL 对比
- `ParameterUncertaintyQuantification.md` — 参数不确定性

#### 2.2.2 实体页扩展（目标: 15+ 页）

**材料体系**（新增 3 页）:
- `UPuZrFuel.md` — U-Pu-Zr 三元合金
- `U10ZrFuel.md` — U-10Zr 合金
- `HT9Cladding.md` — HT9 包壳钢

**代码/工具**（新增 2 页）:
- `BISONCode.md` — BISON 燃料性能代码
- `FEASTMETALCode.md` — FEAST-METAL 代码

**实验设施**（新增 2 页）:
- `EBRII.md` — EBR-II 实验快堆
- `FFTF.md` — FFTF 快中子通量试验设施

---

### Phase 2.3: Category 精细化（预估 2-3 小时）

#### 2.3.1 问题分析
当前 fuel_performance 占 76%（1461/1921），原因：
- 大量早期参数 default 映射到此
- 一些参数应该属于更细分的类别

#### 2.3.2 执行策略
- 对 1461 条 fuel_performance 参数做二次分类
- 重点审查包含以下关键词的参数：
  - 含 "temperature" → thermodynamic
  - 含 "diffusion"/"D₀"/"D₀" → diffusion
  - 含 "stress"/"strain"/"creep" → elastic
  - 含 "gas"/"bubble"/"Xe"/"Kr" → bubble 或 swelling
  - 含 "phase"/"transform"/"α→γ" → phase_transformation
- 目标: fuel_performance 占比降到 < 50%

---

### Phase 2.4: 自动化 Pipeline（预估 3-4 小时）

#### 2.4.1 Lobster Pipeline 设计

```
┌─────────────┐    ┌──────────────┐    ┌─────────────┐    ┌──────────────┐
│ PDF Input    │───▶│ pdftotext    │───▶│ Summary     │───▶│ Parameters   │
│ (Zotero/ref) │    │ Conversion   │    │ Generation  │    │ Extraction   │
└─────────────┘    └──────────────┘    └─────────────┘    └──────────────┘
                                                                │
                                                                ▼
                                                        ┌──────────────┐
                                                        │ Category     │
                                                        │ Normalization│
                                                        └──────────────┘
```

#### 2.4.2 Pipeline Steps
1. **输入**: PDF 路径 + 元数据（标题/年份/主题）
2. **pdftotext**: 自动转换，保存 paper.md
3. **目录名校验**: 对比 PDF 标题，修正 slug
4. **Summary 生成**: 200-400 词中英双语
5. **参数提取**: 结构化 JSON，含标准 9 类 category
6. **质量检查**: 验证 JSON 合法、category 标准、slug 一致

#### 2.4.3 实现方式
- Lobster pipeline YAML 定义
- 每个 step 用 `sessions_spawn` 调用子智能体
- 批量处理：输入论文列表，输出完成报告
- 失败重试 + 跳过已存在

#### 2.4.4 SKILL.md 更新
- 新增 pipeline 使用说明
- 定义输入/输出 schema
- 添加批量处理示例

---

## 四、优先级排序

| 阶段 | 优先级 | 原因 |
|------|--------|------|
| Phase 2.1 数据一致性 | 🔴 高 | 后续工作依赖干净数据 |
| Phase 2.2 知识图谱 | 🔴 高 | 核心价值交付 |
| Phase 2.3 Category 精细 | 🟡 中 | 提升查询精度 |
| Phase 2.4 Pipeline | 🟡 中 | 加速后续 ingest |

---

## 五、成功标准

Phase 2 完成后，知识库应满足：

1. ✅ 71+ 参数文件与 72+ 摘要文件一一对应（slug 匹配）
2. ✅ `parameter_database_v2.json` 与实际参数文件一致（1921 条）
3. ✅ 15+ 概念页，覆盖 Phase 1.5 四方向
4. ✅ 15+ 实体页，覆盖材料/代码/设施
5. ✅ CLAUDE.md 反映最新状态
6. ✅ fuel_performance 占比 < 50%
7. ✅ Lobster pipeline 可复用

---

## 六、风险与缓解

| 风险 | 缓解 |
|------|------|
| Category 精细化可能引入错误 | 做前备份，按批次验证 |
| 知识图谱页质量不稳定 | 先写模板，再批量填充 |
| Pipeline 对异常 PDF 处理不足 | 复用 SKILL.md 已有异常处理经验 |
