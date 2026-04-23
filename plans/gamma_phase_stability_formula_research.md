# γ相辐照稳定性公式补充任务

**日期**: 2026-02-19 12:05
**状态**: 待处理
**优先级**: 高

---

## 当前状态

手册Section 5.3.2中已有框架公式：
```
T_stable > T_critical
T_critical = f(fission rate, Mo content)
```

提到了Willard-Schmitt关系，但缺少具体公式。

---

## 需要补充的内容

### 1. 临界裂变速率-温度关系公式

**目标**: 找到或推导出 T_critical 的具体表达式

**可能的形式**:
```
T_critical = T_0 - A × (fission_rate)^n

或者

fission_rate_critical = B × exp(-Q/(R×T))
```

**参数**:
- T_critical: γ相稳定临界温度 (K或°C)
- fission_rate: 裂变速率 (f/cm³·s 或类似单位)
- Mo含量: 合金成分影响

---

## 搜索策略

### 1. 文献搜索关键词
- "U-Mo gamma phase stability irradiation"
- "Willard Schmitt critical fission rate"
- "U-Mo phase diagram irradiation induced"
- "gamma phase decomposition suppression"

### 2. 数据源优先级
1. **U-Mo Handbook** (ANL-09/31) - Section 3 or Section 5
2. **Zotero库中的U-Mo文献**
3. **ORNL/ANL报告**
4. **Journal of Nuclear Materials**

---

## 行动计划

### 阶段1: 文献搜索 (15分钟)
- [ ] 在handbook_fulltext_extraction.json中搜索相关关键词
- [ ] 检查Zotero提取文件
- [ ] 查看手册Section 3 (U-Mo Phases)

### 阶段2: 公式提取 (10分钟)
- [ ] 从找到的文献中提取临界条件公式
- [ ] 记录参数定义和适用范围
- [ ] 标注参考文献

### 阶段3: 手册更新 (5分钟)
- [ ] 更新Section 5.3.2 γ相稳定性
- [ ] 添加具体公式和参数
- [ ] 添加数据来源引用

---

## 预期输出

```markdown
#### 5.3.2 γ相辐照稳定性

**临界裂变速率-温度关系** (Willard-Schmitt公式):

```
T_critical = T_0 - A × (φ)^n
```

**其中**:
- T_critical: γ相稳定临界温度 (K)
- T_0: 热力学临界温度 (K), ≈ 833K (560°C)
- φ: 裂变速率 (×10¹³ f/cm³·s)
- A: 材料常数
- n: 幂指数 (通常0.3-0.5)

**适用条件**:
- 温度范围: 300-600°C
- 裂变速率: 10¹²-10¹⁴ f/cm³·s
- Mo含量: 6-10 wt.%

**数据来源**: [参考文献]

**物理意义**:
- 高裂变速率可抑制γ相分解
- 辐照缺陷阻止原子扩散
- 临界条件决定γ相是否稳定
```

---

## 相关数据点

从手册Section 5.3.2已知：
- 临界燃耗: ~3×10²¹ f/cm³ (用于再结晶)
- γ相稳定区: >560°C (热力学条件)
- 辐照缺陷抑制分解 (定性描述)

**需要**: 量化裂变速率与温度的关系

---

## 成功标准

1. ✅ 找到具体公式（不是定性描述）
2. ✅ 参数定义清晰
3. ✅ 适用范围明确
4. ✅ 来源可追溯

---

*任务创建: 2026-02-19 12:05*
*负责人: AI Assistant*
*截止: 2026-02-19 13:00*
