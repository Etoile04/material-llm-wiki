# U-Zr相图的现代再评估

## Metadata
- **Title**: A Modern Reappraisal of the U-Zr Phase Diagram
- **Authors**: W.J. Williams, J. Lund, R.E. García, M.A. Okuniewski
- **Year**: 2025
- **Journal**: Journal of Nuclear Materials 603 (2025) 155378
- **Affiliation**: Purdue University / Idaho National Laboratory
- **DOI**: 10.1016/j.jnucmat.2024.155378

## 摘要

本文通过机器学习方法gibbs.ML，整合已发表的U-Zr体系实验数据，对历史上两派观点——Sheldon & Peterson（1980s，β-U稳定范围延伸至~60 at.% Zr）和Rough & Bauer（1950s，β-U仅稳定至~14 at.% Zr）——进行了系统性再评估，最终提出了新的U-Zr相图。

关键发现：现代原位中子衍射（ND）和差示扫描量热法（DSC）数据在14 at.% Zr以上从未观测到β-U相。在0-95 at.% Zr范围内共识别83个实验数据点用于约束相界。新相图的主要特征包括：(1) β-U稳定性被截断至6 at.% Zr；(2) 等温线位于884 K（611°C）和961 K（688°C）；(3) δ-UZr₂相界在823 K（550°C）下为66.5-80.2 at.% Zr；(4) γ-U-Zr偏混溶隙保留至1020 K；(5) α-U中Zr固溶度从室温的<1 at.%增至~953 K附近的4-5 at.%。

新相图的损失函数值为4.9%，对实验焓值和转变温度的偏差为：$\Delta H^U_\alpha$偏差0.4%、$\Delta H^U_\beta$偏差1.6%、$T_{m,\beta}$偏差0.0%，优于两份历史相图。该结果对依赖U-Zr相图的多物理场燃料性能模拟具有重要意义——任何假设β-U在14 at.% Zr以上存在的模型都需要重新评估。

## Key Equations

- **γ-U-Zr自由能（Redlich-Kister展开）**：
$$\Delta G^{(\gamma)}(c,T) = \Delta H^{(\gamma)}_U \frac{T}{T_{m,U}^{(\gamma)}}(1-c) + \Delta H^{(\gamma)}_{Zr} \frac{T}{T_{m,Zr}^{(\gamma)}} c + RT[c\ln c + (1-c)\ln(1-c)] + c(1-c)\sum_{i=0}^{2}\left(a_i^{(\gamma)} + b_i^{(\gamma)} T\right)(2c-1)^i$$

- **α-U / β-U 正则溶液模型**：
$$\Delta G^{(j)}(c,T) = \Delta H^{(j)}_U\frac{T}{T_{m,U}^{(j)}}(1-c) + \Delta H^{(j)}_{Zr}\frac{T}{T_{m,Zr}^{(j)}}c + RT[c\ln c + (1-c)\ln(1-c)] + c(1-c)\Omega^{(j)}$$

- **δ-U-Zr 亚晶格模型**：化合物能量形式，第一亚晶格优先填充Zr，第二亚晶格为U/Zr混合占据

- **损失函数**：
$$L = \sqrt{\sum_{i \in PD_t}\min_{j\in PD_p}\left(\frac{|c_i - c_j|}{\Delta c} + \frac{|T_i - T_j|}{\Delta T}\right)^8} + \sqrt{\sum_{i \in PD_p}\min_{j\in PD_t}\left(\frac{|c_i - c_j|}{\Delta c} + \frac{|T_i - T_j|}{\Delta T}\right)^8}$$

## 关键参数
| 参数 | 新相图值 | 单位 |
|------|---------|------|
| $\Omega^{(\gamma)}$ a₀ | 22077 | J/mol |
| $\Omega^{(\gamma)}$ a₁ | -22514 | J/mol |
| $T_{m,U}^{(\alpha)}$ | 998.7 | K |
| $\Delta H^{(\alpha)}_U$ | -7517 | J/mol |
| $\Omega^{(\alpha)}$ | 25345 | J/mol |
| $T_{m,U}^{(\beta)}$ | 1042 | K |
| $\Delta H^{(\beta)}_U$ | -4831 | J/mol |
| $\Omega^{(\beta)}$ | 32578 | J/mol |

## Related Work
- [[wiki/entities/U10ZrFuel|U10ZrFuel]] — U-Zr相图是U-Zr燃料性能分析的基础热力学数据
- [[wiki/summaries/2018_Lu_CALPHAD_UFuels|2018_Lu_CALPHAD_UFuels]] — 铀燃料CALPHAD热力学评估
- [[wiki/summaries/2018_Turchi_ThermodynamicDiffusion|2018_Turchi_ThermodynamicDiffusion]] — U-Zr热力学与扩散数据库
- [[wiki/summaries/Xiong_2013_ThermodynamicUZr|Xiong_2013_ThermodynamicUZr]] — U-Zr热力学评估
- [[wiki/summaries/2020_Yao_AlphaOmega_U10Zr|2020_Yao_AlphaOmega_U10Zr]] — U-10Zr的α/ω相变
- [[wiki/summaries/2016_Carmack_FCCI_MFF3_Metallography|2016_Carmack_FCCI_MFF3_Metallography]] — U-Zr燃料的金相分析
