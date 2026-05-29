# ISSUES — ref-gap-fill 参考值补全系统

## Active

### I1: ontofuel 本体缺少弹性常数属性
- **严重度**: Medium
- **描述**: ontofuel 本体有 279 个 datatype properties，但缺少 C11/C12/C44/C33 弹性常数的定义
- **影响**: L3b 缓存无法查询弹性常数，影响 75% 的物性缺口
- **计划**: Phase A 中扩展本体，添加 4 个 datatypeProperty

### I2: llm-wiki 参数全中文命名
- **严重度**: Medium
- **描述**: llm-wiki 的 68 条可用参数全是中文命名（如"晶格常数"、"弹性常数"）
- **影响**: property-mapping.json 需要额外的中文→英文映射层，可能引入歧义
- **待决策**: 是否在 llm-wiki 层面就改用英文命名（影响面大），还是仅做 adapter

### I3: NFMD 数据质量参差不齐
- **严重度**: Low
- **描述**: NFMD 部分参数来源不明确（如 source_file 为 "Experiment" 无具体引用）
- **影响**: L2 缓存命中后仍需质量过滤，不能直接映射
- **计划**: adapter-nfmd.py 中增加 source 完整性检查

### I4: reference_values 表缺少 needs_review 列
- **严重度**: Low (Phase A 开始时解决)
- **描述**: 分级写入策略需要 `needs_review` 布尔列，当前表不存在
- **计划**: Phase A 第一步 ALTER TABLE 添加

## Resolved

(none yet)
