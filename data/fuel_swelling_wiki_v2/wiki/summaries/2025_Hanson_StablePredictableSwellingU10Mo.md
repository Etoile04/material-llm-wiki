# 微结构验证的低浓铀单体U-10Mo燃料小型板的稳定可预测肿胀行为

## Metadata
| Field | Value |
|-------|-------|
| Authors | William A. Hanson, Daniele Salvato, Adam B. Robinson, Nancy J. Lybeck, Jan-Fong Jue, Tammy L. Trowbridge, Jatuporn Burns, Fidelma G. Di Lemma, Charlyne A. Smith, Margaret A. Marshall, Dennis D. Keiser Jr., Jeffrey J. Giglio, James I. Cole |
| Year | 2025 |
| Journal | Journal of Nuclear Materials |
| DOI | 10.1016/j.jnucmat.2025.155401 |

## Overview

本文报道了Mini-Plate 1（MP-1）辐照实验的肿胀行为与微观组织演化结果，这是低浓铀（LEU）单体U-10Mo板型燃料合格化程序中首次对商业制造的小型燃料板进行的辐照考验。MP-1实验包含74块Al-6061包壳小型板，其中34块商业制造板（C-plates，含均匀化退火）和8块INL基准板（B-plates，无均匀化退火），辐照于ATR（先进试验堆）中。LP（低功率）厚燃料板峰值功率5-10 kW/cm³，燃耗0.63-3.15×10²¹ fissions/cm³；MP（中功率）薄燃料板峰值功率20-35 kW/cm³，燃耗2.52-6.11×10²¹ fissions/cm³。

通过对约47,000个局部肿胀-裂变密度数据点的分析，发现MP-1燃料肿胀行为与Robinson等人（2020）建立的U-10Mo肿胀模型预测基本一致，绝大部分数据点落在95%预测带内。统计检验发现C板和B板肿胀行为存在可检测的差异：B板在所有测试裂变密度下肿胀量略高于C板。光学显微镜和SEM分析表明，这种差异主要归因于B板缺乏均匀化退火导致Mo成分不均匀，形成了α-U-Mo分解相，在低裂变密度下即诱发辐照辅助再结晶产生微米级晶粒，增加了裂变气体气泡沉淀位置，从而使肿胀向更低裂变密度偏移。相反，C板初始微观组织均匀，遵循典型的U-10Mo演化路径：低裂变密度下裂变气体以FCC气泡超晶格（Gas Bubble Superlattice）形式储存于晶内，中等裂变密度开始晶粒细化，高裂变密度下形成高燃耗结构（HBS）。两种制造方式的燃料均未观察到裂变气体孔隙互连或失稳肿胀（breakaway swelling）迹象。

## Key Equations

### 1. 燃料体积肿胀分数（完整形式）

$$S = \frac{(t_{\text{post}} - t_{\text{pre}}) - 2t_{\text{ox}}}{t_{\text{foil}} + 2t_{\text{Zr}}} \times 100\%$$

其中：$t_{\text{post}}$为辐照后板厚，$t_{\text{pre}}$为辐照前板厚，$t_{\text{ox}}$为辐照后氧化层厚度，$t_{\text{foil}}$为轧制Zr扩散障后燃料芯体厚度，$t_{\text{Zr}}$为单侧Zr扩散障厚度。由于板型燃料几何约束（轴向和横向受限），板厚变化直接关联体积肿胀。

### 2. 简化肿胀计算公式

$$S = \frac{t_{\text{post}} - t_{\text{pre}}}{t_{\text{foil}} + 2t_{\text{Zr}}} \times 100\%$$

当氧化层厚度在测量分辨率范围内可忽略时使用。MP-1实验中涡流探针验证氧化层厚度在BONA4INL测量台±3μm分辨率内。

### 3. Robinson经验肿胀模型（二次拟合，过原点约束）

$$S(f) = A \cdot f + B \cdot f^2$$

其中$f$为裂变密度（fissions/cm³），$A$和$B$为经验拟合系数。该模型基于约18,000个历史肿胀数据对建立，经MP-1约47,000个数据点验证，95%预测带能覆盖MP-1数据散布范围。

## Physical Mechanisms

1. **裂变气体超晶格（FGB Superlattice）**：低裂变密度（<3×10²¹ fissions/cm³）下，裂变气体以FCC有序气泡超晶格形式储存于γ-U-Mo晶粒内部，不贡献宏观肿胀。

2. **晶界裂变气体气泡沉淀**：原始晶界作为缺陷陷阱，微米级裂变气体气泡在晶界优先形核和长大，是肿胀的主要来源。

3. **晶粒细化与高燃耗结构（HBS）形成**：中等裂变密度（>3×10²¹ fissions/cm³）下，气泡超晶格崩塌，晶粒从原始晶界开始细化，新亚晶界上产生额外裂变气体孔隙，形成HBS。

4. **Mo成分不均匀性对肿胀的影响**：非均匀化B板中存在低Mo区，分解为α-U-Mo相，在辐照下通过辐照辅助再结晶转变为γ-U-Mo相，形成微米级晶粒带。这些额外晶界在低裂变密度下即提供裂变气体沉淀位点，使肿胀向更低裂变密度偏移。

5. **制造工艺的影响**：均匀化退火消除Mo成分偏析，使燃料微观组织演化遵循预期路径，略降低肿胀量。非均匀化制造导致统计上可检测但量值较小的肿胀增加。

## Relationships

- [[wiki/entities/GasBubbleSuperlattice|GasBubbleSuperlattice]] — FCC气泡超晶格在低裂变密度下储存裂变气体
- [[wiki/entities/Recrystallization|Recrystallization]] — 辐照辅助再结晶导致晶粒细化
- [[wiki/entities/FuelAlloy|FuelAlloy]] — U-10Mo合金体系，含Zr扩散障
- [[wiki/entities/CavitationalVoid|CavitationalVoid]] — 晶界裂变气体孔隙作为肿胀来源
- [[wiki/entities/FissionGasDiffusion|FissionGasDiffusion]] — 裂变气体从晶内向晶界输运
- Robinson et al. 2020 肿胀模型作为基准比较对象
- AFIP-6MKII实验数据主导了历史模型在高燃耗区间的行为，可能受Mo不均匀性影响
- AFIP-7和AFIP-3BZ数据与MP-1 C板行为一致，支持均匀化微观组织的有效性
