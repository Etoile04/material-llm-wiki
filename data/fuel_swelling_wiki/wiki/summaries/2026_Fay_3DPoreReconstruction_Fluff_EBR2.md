# EBR-II 燃料顶部 fluff 区 3D 孔隙结构 Micro-CT 重构 (2026, Fay et al.)

## Metadata
- **Journal**: Journal of Nuclear Materials 618 (2026) 156167
- **Authors**: Jake Fay, William Chuirazzi, Luca Capriotti, Fidelma Di Lemma, Cameron Howard, Mario Matos, Jie Lian
- **Affiliation**: Rensselaer Polytechnic Institute / Idaho National Laboratory
- **Material System**: U-19Pu-10Zr (EBR-II fuel pin X512-DP55)
- **Method**: Plasma-FIB 制样 + Micro-CT (260 nm/voxel) + EDS
- **Key Topic**: 首次 3D 重构 fluff 微观孔隙结构，验证蠕变驱动形成机制

## Physical Mechanisms

1. **Fluff 现象**：金属燃料柱顶部形成的多孔疏松结构，从几毫米到几厘米不等，富含易裂变原子，可能影响反应性。
2. **两种假说**：（a）**蠕变驱动**：燃料肿胀接触包壳后在顶部产生应力集中，加速蠕变导致碎裂；（b）**气体爆破**：裂变气体局部压力导致顶部爆破-融合循环。
3. **3D 孔隙分析支持蠕变机制**：fluff 内部孔隙分布与体燃料显著不同，微观尺度上孔隙率远高于体燃料且高度集中于少数大孔隙网络，符合蠕变加速孔隙生长的特征。

## Key Equations

### 孔隙率计算
$$\text{Porosity} = \frac{V_p}{V_p + V_S} \quad \text{(Eq. 1)}$$

### 球度
$$\text{Sphericity} = \frac{(36\pi V^2)^{1/3}}{SA} \quad \text{(Eq. 2)}$$

球度范围 0–1，1 为完美球体。小封闭孔隙趋向球形，大互连孔隙网络形状不规则。

## Key Parameters

| 参数 | 燃料体 | Fluff 整体 | Fluff 顶部 | Fluff 底部 |
|------|--------|-----------|-----------|-----------|
| 孔隙结构数 | 512 | 182 | 108 | 83 |
| 总孔隙率 | 15% | 36% | 32% | 8% |
| 开放孔隙率 | 77% | 98% | 97% | 87% |
| 最大孔隙网络体积 | 14,400 µm³ | 57,000 µm³ | 27,080 µm³ | 2,400 µm³ |
| 前5大孔隙占比 | 69% | 97% | 96% | 85% |

## Relevance to Knowledge Base

本文首次实现了 fluff 的 3D 微观孔隙表征，为理解金属燃料轴向肿胀和 fluff 形成机制提供了关键实验数据。95% 的 fluff 孔隙集中于单一巨大孔隙网络的发现，对燃料性能模拟中孔隙互连模型具有重要参考价值。

## Related Work
- [[wiki/entities/UPuZrFuel|UPuZrFuel]] — 材料体系为U-19Pu-10Zr
- [[wiki/entities/EBR-II|EBR-II]] — 燃料取自EBR-II辐照
- [[wiki/concepts/SwellingMechanisms|SwellingMechanisms]] — fluff形成与肿胀机制直接相关
- [[wiki/summaries/2020_Aagesen_BisonUPuZrSwellingLowerLengthScale|2020_Aagesen_BisonUPuZrSwellingLowerLengthScale]] — BISON U-Pu-Zr肿胀模型
- [[wiki/summaries/2018_Millett_ComputationalExperimentalPorosityMetallic|2018_Millett_ComputationalExperimentalPorosityMetallic]] — 金属燃料孔隙率计算与实验对比
