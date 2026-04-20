# 匹配审核报告

审核日期: 2026-04-20
审核人: Lily (subagent)

---

## 1. 2021_Qian → Hilty_et_al_2021 匹配错误

**结论: ❌ 确认匹配错误**

- v1 `2021_Qian_RateTheoryUN`: Qian 等人关于 UN 燃料的速率理论模型
- v2 `Hilty_et_al_2021`: Hilty 等人关于 UO2 中裂变气泡对热导率的影响

这是两篇完全不同的论文（不同作者、不同材料、不同主题）。原比对算法因相似度 0.49（极低）仍强行匹配，是错误的。

**正确映射:**
- `2021_Qian_RateTheoryUN` → `2021_Qian_RateTheoryUN`（v2 中存在同名文件，exact match）
- `2021_Hilty_FissionGasBubblesThermalConductivity` → `Hilty_et_al_2021_Impact_of_fission_gas_bubbles_on_thermal_conductivity_of_UO2`

---

## 2. Miller 2015 第15-17行参数对比差异（3条疑似错误）

**结论: ⚠️ 非匹配错误，是行对齐问题**

论文映射 `2015_Miller_TEMGasBubbleSuperlatticeU7Mo` → `miller_et_al_2015_...` 是正确的。

但 v1 和 v2 的参数按行号对齐时出现了错位：

| 行号 | v1 参数 | v1 值 | v2 参数 | v2 值 |
|------|---------|-------|---------|-------|
| #15 | Xe solution energy in UO₂ | ~9.5 eV/atom | fission density for grain subdivision onset | 4.5e21 fiss/cm³ |
| #16 | Xe solubility at 2.4 at.% Xe | ~20 kJ/mol | fission density for monolithic fuel swelling transition | 7e21 fiss/cm³ |
| #17 | cold-worked metal recrystallization threshold | ~20 J/mol | fission density for fully ordered superlattice | 1.3e21 fiss/cm³ |

**原因**: v1 按 TEM 观察到的物理参数排序（溶解能、溶解度等），v2 按辐照条件排序（裂变密度阈值）。两边对同一论文提取了不同侧重点的参数，且排序方式不同，导致行对齐时比较了不相关的参数。

**建议**: 后续比对应改为按参数名称/语义匹配，而非按行号对齐。

---

## 总结

| 问题 | 类型 | 严重程度 |
|------|------|---------|
| Qian → Hilty 误匹配 | 论文映射错误 | 🔴 高 |
| Miller 3条参数差异 | 行对齐问题（非映射错误） | 🟡 中 |
