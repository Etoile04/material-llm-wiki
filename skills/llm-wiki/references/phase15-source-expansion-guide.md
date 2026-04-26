# Phase 1.5 文献扩展指南

## 当前真实状态（2026-04-21）

- 已从早期 47 篇扩展到约 69 篇
- 参数总量约 1385 条
- Batch D 已完成 9 篇文献补充提取
- Willard 1985 已通过 `mineru-open-api extract` 成功转换，公式恢复良好
- 仍需继续扩展文献覆盖，而不是只做存量修补

## 当前空白方向

Phase 1.5 后半段优先补以下 4 个方向：

1. **U-Pu-Zr 三元金属燃料肿胀 / 组元再分布 / 重分布建模**
2. **辐照蠕变（irradiation creep）**
3. **FCCI（fuel-cladding chemical interaction）**
4. **裂变气体释放（fission gas release）与释放速率理论**

## 检索原则

### 1. 先补“领域骨架”，再补细节论文

优先顺序：

1. 综述 / handbook / PIRT / code model paper
2. 经典机制论文
3. 近 5 年高质量补充论文
4. 纯局部实验现象论文

### 2. 每个方向至少收集三层文献

- **综述层**：1-3 篇
- **经典模型层**：3-6 篇
- **近年进展层**：3-6 篇

### 3. 候选文献记录最少字段

每篇候选至少记录：

- title
- year
- topic
- source_url
- source_type（review / model / experiment / handbook）
- availability（oa / abstract / zotero-only / missing-pdf）
- priority（high / medium / low）
- notes

建议先写成 Markdown 表，后续再转结构化 JSON。

## 推荐检索模板

### U-Pu-Zr

- `U-Pu-Zr metallic fuel swelling review`
- `U-Pu-Zr constituent redistribution model`
- `U-Pu-Zr recrystallization swelling`
- `U-Pu-Zr FEAST-METAL swelling`
- `U-Pu-Zr BISON metallic fuel swelling`

### Irradiation creep

- `U-Mo irradiation creep fuel`
- `metal fuel irradiation creep review`
- `fission induced creep U-Mo`
- `irradiation creep metallic fuel model`

### FCCI

- `metal fuel FCCI review`
- `fuel cladding chemical interaction U-Pu-Zr`
- `U-Mo Al interaction irradiation review`
- `FCCI metallic fuel mechanistic model`

### Fission gas release

- `metallic fuel fission gas release model`
- `fission gas release rate theory metallic fuel`
- `U-Mo fission gas release model`
- `U-Pu-Zr fission gas release swelling`

## 候选筛选标准

优先入库：

- 与肿胀、气泡、再结晶、扩散、释放 directly relevant
- 含可提取参数、方程、模型结构
- 可形成新的 concept/entity page 支撑
- 与现有 69 篇相比有明显新增信息

降低优先级：

- 只做表征、几乎无可迁移参数
- 与已有论文高度重复
- 无 PDF、无足够摘要、无稳定来源

## 入库前检查

新增候选文献在进入 ingest 前先做：

1. **查询 `paper_registry.json`** — 按 DOI 精确匹配，按标题模糊匹配（>0.85）
2. 是否已在现有 summary / parameters 中出现
3. 是否与已有 raw/mineru 目录重复
4. 是否存在标题错配（目录名不可信，以正文标题为准）
5. 是否值得进入本轮 Phase 1.5 范围
6. **如果重复**: 使用已有 slug，追加参数到现有文件，禁止创建新 slug
7. **如果新论文**: 使用 `YYYY_FirstAuthor_ShortTitle` 格式创建 slug，注册到 paper_registry.json

## 本轮建议最低交付

- 每个空白方向至少补 5 篇候选
- 总新增候选至少 20 篇
- 其中至少 10 篇具备可直接进入 ingest 的 PDF 或稳定全文来源
