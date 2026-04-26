# 低燃耗 AFC 金属燃料合金辐照后检验

## 元数据

| 字段 | 值 |
|------|-----|
| **标题** | Postirradiation Examination Results of Selected AFC-3A and AFC-3B Metallic Fuel Alloys |
| **作者** | J.M. Harp, S. Chichester, L. Capriotti |
| **期刊** | Journal of Nuclear Materials 509 (2018) 377–391 |
| **年份** | 2018 |
| **Slug** | 2018_Harp_Postirradiation_AFC_MetalFuelAlloys |
| **关键词** | AFC-3, U-10Zr, U-10Mo, 辐照后检验, FGR, 光学显微镜, 伽马层析 |

## 中文摘要

本文报告了 AFC-3A 和 AFC-3B 实验中 8 根金属燃料棒的低燃耗辐照后检验（PIE）结果。实验在 ATR（先进试验反应堆）中辐照，包含多种合金和几何形状：实心和环形 U-10Zr（75% 涂抹密度）、实心 U-10Mo（75% 和 55% 涂抹密度），以及含 Pd 的 U-Zr 合金（用于抑制 FCCI）。

PIE 技术包括：中子射线照相、伽马能谱扫描及伽马发射计算机断层扫描（GECT）、尺寸检查、裂变气体释放（GASR 系统）、化学分析（ICP-MS 测定燃耗）、光学显微镜等。燃耗范围 2.1%-4.1% FIMA，峰值包壳温度 376-625°C。

关键发现：(1) 实心 U-10Zr 棒肿胀至填满燃料-包壳间隙，呈现经典的两区结构（Zr 重分布所致）；(2) 环形 U-10Zr 棒中 Zr 合金燃料基本填满环形间隙，而 Mo 合金燃料尺寸变化很小；(3) U-10Mo 燃料发生显著 FCCI，包壳减薄至 340 μm（原始 440 μm）；(4) 裂变气体释放 31%-71%，高涂抹密度和高燃耗棒释放率更高，与历史 ~70% 释放率一致；(5) GECT 揭示 Ce 在 g(U,Zr) 相转变区富集、Cs 向冷端迁移等裂变产物分布特征；(6) 低涂抹密度 U-10Mo 棒出现非对称肿胀和可能局部熔化。

## 关键实验数据

### 裂变气体释放

| 棒束 | 燃耗 (%FIMA) | Kr+Xe 释放 (%) |
|------|-------------|----------------|
| AFC-3A R1 | 2.2 | — |
| AFC-3A R2 | 4.1 | 62.3 |
| AFC-3A R4 | 3.3 | 37.0 |
| AFC-3A R5 | 2.5 | 31.0 |
| AFC-3B R1 | 2.6 | 57.6 |
| AFC-3B R2 | 3.8 | 70.0 |
| AFC-3B R4 | 2.1 | 70.6 |
| AFC-3B R5 | 2.4 | 48.7 |

### 燃耗测定方法

采用 ICP-MS 裂变产物监测-残余重原子技术：
$$BU = \frac{N_{fp} \cdot y_{fp}}{N_{fp} \cdot y_{fp} + N_{Act}} \times 100$$

可靠的监测同位素：La-139, Ce-140, Ce-142, Pr-141, Nd-145+Nd-146（来自 ENDF/B-VII.1 裂变产额）。

## 微结构观察

- **U-10Zr 实心棒**：肿胀填满间隙，经典两区结构，高燃耗下 FCCI 明显
- **U-10Mo 实心棒**：显著 FCCI（包壳减薄 100 μm），无组分重分布
- **U-10Mo 环形棒**：尺寸变化小，铀密度保持较好
- **低涂抹密度 U-10Mo**：非对称肿胀，大孔隙，可能局部过热
- **4wt% Pd U-Zr**：Pd 未有效抑制 FCCI

## Related Work
- [[wiki/concepts/FuelCladdingChemicalInteraction|FuelCladdingChemicalInteraction]] — 本文报告U-10Mo燃料的显著FCCI行为
- [[wiki/entities/U10ZrFuel|U10ZrFuel]] — 本文涵盖实心和环形U-10Zr燃料棒的PIE数据
- [[wiki/summaries/2018_Janney_MetallicFuelsHandbook|2018_Janney_MetallicFuelsHandbook]] — 金属燃料手册，汇总U-Zr和U-Mo燃料的辐照性能
- [[wiki/summaries/2016_Carmack_FCCI_MFF3_Metallography|2016_Carmack_FCCI_MFF3_Metallography]] — FFTF中金属燃料的PIE和FCCI研究，与本文ATR数据形成对比
- [[wiki/summaries/1996_Ogata_FissionGasBehavior_MetallicFuel|1996_Ogata_FissionGasBehavior_MetallicFuel]] — 金属燃料裂变气体行为，与本文FGR数据(31%-71%)对比
