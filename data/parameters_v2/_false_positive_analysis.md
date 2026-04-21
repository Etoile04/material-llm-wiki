# 假阳性根因分析与改进措施

> 日期：2026-04-20
> 事件：参数比对 v1 vs v2 报告 43 条冲突，审核后全部为假阳性

---

## 根因分析

### 直接原因：比对算法存在 5 个系统性缺陷

| # | 缺陷 | 影响数 | 严重性 |
|---|------|--------|--------|
| 1 | **跨论文匹配** | 20 | 🔴 严重 |
| 2 | **跨符号匹配** | 6 | 🔴 严重 |
| 3 | **v2 新增论文随机配对** | 8 | 🟡 中等 |
| 4 | **同符号多条件未精确配对** | 5 | 🟡 中等 |
| 5 | **科学计数法比较 bug** | 4 | 🟢 低 |

### 深层原因

#### 1. 缺少匹配键约束（根因 #1）
比对时只用 `symbol` 或 `name` 做全局匹配，没有限制在同一论文范围内。结果：
- Ye 2023 的 `fn=0.0001` 和 Hu 2016 的 `f_n=1e-05` 被配对
- Sun 2016 的 `λ`（中子波长）和另一个论文的 `λ`（热导率）被配对

**正确做法**：匹配键 = `source_file + symbol + material + temperature_range`

#### 2. 符号歧义未处理（根因 #2）
科学文献中大量参数使用通用符号（γ, σ, b, k, z 等），含义完全不同：
- `γ`：表面能？层错能？γ相？
- `b`：伯格斯矢量？气泡半径？肿胀系数？
- `k`：玻尔兹曼常数？热导率？缺陷产生率？

**正确做法**：匹配时必须结合 `name`/`name_en` 和 `category` 字段消歧

#### 3. 数值比较不归一化（根因 #5）
`2.0e-8` 和 `2e-08` 被认为不同，因为字符串比较而非数值比较。

#### 4. v1 文件名体系与 v2 不同
v1 文件名如 `1993_Rest_VoidSwellingAlphaU.json`，v2 文件名如 `Rest_1993_VoidSwellingAlphaU.json`。比对算法无法建立文件对应关系。

---

## 改进措施

### 1. 重写匹配算法（优先级 P0）

```python
def match_params(v1_records, v2_records):
    """精确匹配参数记录"""
    matches = []
    unmatched_v1 = []
    unmatched_v2 = []
    
    for v2 in v2_records:
        # 精确匹配键：论文 + 符号 + 材料 + 温度
        candidates = [
            v1 for v1 in v1_records
            if (
                normalize_symbol(v1['symbol']) == normalize_symbol(v2['symbol'])
                and normalize_name(v1.get('name_en','')) == normalize_name(v2.get('name_en',''))
                and v1.get('material','') == v2.get('material','')
                and ranges_overlap(v1.get('temperature_K'), v2.get('temperature_K'))
                # 关键：必须在同一论文范围内
                and same_paper(v1['source_file'], v2['source_file'])
            )
        ]
        
        if len(candidates) == 1:
            matches.append((v1, v2))
        elif len(candidates) == 0:
            unmatched_v2.append(v2)  # 新增参数
        else:
            # 多候选：选最接近的
            best = min(candidates, key=lambda c: temp_distance(c, v2))
            matches.append((best, v2))
    
    return matches, unmatched_v1, unmatched_v2
```

### 2. 建立论文映射表（优先级 P0）

```json
{
    "v1_to_v2_mapping": {
        "1979_Ronchi_FissionGasSwellingMX_Fuels": "Ronchi_1979_*",
        "1993_Rest_VoidSwellingAlphaU": "Rest_1993_*",
        ...
    }
}
```

### 3. 数值归一化（优先级 P1）

```python
def normalize_value(v):
    """统一数值表示"""
    if isinstance(v, (int, float)):
        return float(v)
    if isinstance(v, str):
        # 处理科学计数法、单位后缀等
        return float(v.replace('×10', 'e').replace('×10⁻', 'e-'))
```

### 4. 符号消歧规则（优先级 P1）

| 步骤 | 检查项 |
|------|--------|
| 1 | symbol 精确匹配 |
| 2 | name_en 包含匹配 |
| 3 | category 一致 |
| 4 | unit 量纲一致 |
| 5 | 数值量级合理性检查 |

### 5. 自动化质量门禁（优先级 P2）

在参数提取流程中加入：
- **量级检查**：同类参数偏离中位数 >3 个数量级 → 标记异常
- **单位一致性**：同类参数单位必须一致（如扩散系数统一 m²/s）
- **物理合理性**：如扩散系数应在 1e-20 ~ 1e-5 m²/s 范围

---

## 检查清单（未来比对时使用）

- [ ] 匹配键包含 source_file（论文级别约束）
- [ ] 匹配键包含 symbol + name_en（消歧）
- [ ] 匹配键包含 material + temperature（条件约束）
- [ ] 数值比较用 float 而非字符串
- [ ] v2 独有论文标记为"新增"而非"冲突"
- [ ] 差异 >1000% 的记录自动标记为"疑似匹配错误"
- [ ] 输出匹配详情（匹配了哪条 v1 → 哪条 v2），便于人工审核

---

## 教训

1. **符号 ≠ 参数**：`γ` 在不同上下文含义完全不同，不能仅靠符号匹配
2. **数值比较必须归一化**：`2.0e-8` = `2e-08` = `0.00000002`
3. **跨文件匹配是灾难性的**：47 篇论文的参数池做全局模糊匹配，假阳性率 100%
4. **"差异大"≠"有冲突"**：先验证匹配是否正确，再判断差异是否有意义
5. **输出可审核信息**：每次匹配应附带配对详情，让人类能快速验证
