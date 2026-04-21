# Phase 1.5 进展报告

**日期**: 2026-04-21  
**执行人**: Lily 🦀  
**状态**: 进行中

---

## 一、目标

Phase 1.5 的真实目标有两部分：

1. 扩展参数提取范围：从"燃料肿胀"单一方向 → **9 类材料参数全覆盖**
2. 扩展文献覆盖面：从早期 47 篇提升到 **100+ 篇候选/可入库文献池**，并优先补齐 4 个空白方向

---

## 二、执行过程

### Batch A：新论文 ingest（6 篇）

从 Zotero 新增 6 篇去重论文（原子模拟/扩散/相变方向）：

| 论文 | 主题 | 参数 | Key Equations |
|------|------|------|---------------|
| Park 2021 | U-Mo 缺陷能/扩散（原子模拟） | 9 | ✅ |
| Beeler 2021 | γU-Mo 辐照驱动扩散 | 10 | ✅ |
| Interdiffusion Zr/U-Mo | Zr 扩散阻挡层互扩散 | 10 | ✅ |
| Kr 离子辐照铀合金 | Kr 辐照微结构演化 | 10 | ✅ |
| U-Mo-Ti 相变特征 | 相变动力学 | 10 | ✅ |
| Xie 2020 | U 微结构/扩散行为 | 10 | ✅ |

### Batch B：已有论文参数补充（10 篇，+58 条新参数）

从已有知识库中补充提取非肿胀参数（扩散、激活能、热力学、弹性、辐照损伤等）。

### Batch C：全库参数分类标注（64 个文件，1198 条参数）

- 919 条旧参数从无 category → 重新分类到 9 类
- 所有参数 value_type 覆盖率 100%

### v1 → v2 迁移

将 v1 的 32 篇 summary + 43 个参数文件迁移到 v2，形成完整知识库。

---

## 三、当前质量状态

| 指标 | v1（Phase 1） | v2（Phase 1.5 后） | 变化 |
|------|--------------|-------------------|------|
| **文献数量** | 47 | **约 69** | Batch A-D 持续扩展 |
| **参数总量** | 1213 | **约 1385** | Batch D 后继续增长 |
| **参数类别** | 2 类 | **9 类** | ✅ 扩展 4.5 倍 |
| **validate FAIL** | 0 | **0** | ✅ 保持 |
| **公式覆盖率** | 100% | **100%** | ✅ 保持 |
| **value_type 覆盖** | 100% | **100%** | ✅ 保持 |
| **category 覆盖** | ~30% | **100%** | ✅ 全覆盖 |

### 参数类别分布

| 类别 | 数量 | 占比 |
|------|------|------|
| swelling | 445 | 37.1% |
| irradiation | 277 | 23.1% |
| bubble | 252 | 21.0% |
| fuel_performance | 179 | 14.9% |
| diffusion | 117 | 9.8% |
| elastic | 42 | 3.5% |
| thermodynamic | 35 | 2.9% |
| activation_energy | 10 | 0.8% |
| phase_transformation | 9 | 0.8% |

---

## 四、关键改进

### 4.1 技能层面
1. **SKILL.md**：新增 8 类参数提取范围规范
2. **validate_params.py**：修复 list 类型 magnitude 检查（支持 dict 值）
3. **参数 schema**：expression 类型强制使用 `value_expr` 字段

### 4.2 数据层面
1. **新论文覆盖**：原子模拟（Park 2021）、辐照扩散（Beeler 2021）、互扩散（Xie 2020）、相变（U-Mo-Ti）
2. **参数类别从 2 → 9**：覆盖了扩散、弹性、热力学等非肿胀参数
3. **全库分类标准化**：1198 条参数统一到 9 类体系

### 4.3 发现的问题
1. **Zotero PDF 去重**：11 个 PDF 实际只有 6 篇独立论文（需在 ingest 前去重）
2. **网络限制**：SSL 连接外部网站失败，无法批量下载新 PDF
3. **Batch B 子智能体运行时间短**（23s）——追加模式效率高但深度有限

---

## 五、当前新增进展（晚间更新）

### Batch D 已完成

新增完成 9 篇文献提取，并补充了以下代表性方向：

- U-10Mo 板型燃料肿胀/蠕变
- U-Mo 原子尺度缺陷能与扩散
- Xe incorporation / bubble superlattice
- Rest 1993 α-U / U-Pu-Zr 空穴肿胀
- Beeler 2020 辐照驱动扩散
- Qian 2022 U-10Zr 空穴肿胀
- Aagesen 2025 Mo 超晶格/空位组织
- Willard 1985 辐照肿胀与相回复

### MinerU 工作流修正

- `flash-extract` 作为首选方案（<10MB 且 <20 页）
- 大文件改用 `extract`
- Willard 1985 已验证 `extract` 可恢复公式质量
- 新增“目录名不可信，以正文标题为准”的预检查规则

## 六、下一步建议

### 短期（继续执行 Phase 1.5）
1. **继续外部搜索补文献空白**：
   - U-Pu-Zr 三元肿胀 / constituent redistribution
   - irradiation creep
   - FCCI
   - fission gas release / release rate theory
2. **形成候选新增清单**：至少再补 20 篇候选，其中 ≥10 篇可直接进入 ingest
3. **按主题分批 ingest**：优先 review / handbook / code-model / PIRT 文献
4. **保持门禁不退化**：validate FAIL = 0，公式覆盖率 = 100%

### 中期（Phase 2）
5. **Lobster Pipeline**：在技能稳定后搭建自动化 ingest pipeline
6. **与 Supabase 集成**：参数自动入库供查询

---

*最后更新：2026-04-21 23:15 GMT+8*
