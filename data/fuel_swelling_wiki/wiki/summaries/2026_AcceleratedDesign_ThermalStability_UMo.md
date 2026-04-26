# γ-U-Mo 金属核燃料加速设计与热稳定性优化 (2026, Sun et al.)

## Metadata
- **Journal**: Journal of Alloys and Compounds 1056 (2026) 186570
- **Authors**: Dan Sun, Xin Wang, Rui Li, Chuan Mo, Keyu Ren, Yi Wang, Linna Feng, Wenjie Li
- **Affiliation**: 中国核动力研究设计院 / 中国工程物理研究院材料研究所
- **Material System**: U-Mo-Nb-Ti-V-Zr 六元合金体系
- **Method**: 机器学习（SVC-RBF, Gaussian Process）、DSC、XRD、自适应设计框架
- **Key Topic**: 数据驱动方法加速搜索高热稳定性单相 γ-U-Mo 合金

## Physical Mechanisms

1. **不连续析出（DP）反应**：γ-U-Mo 亚稳相沿晶界发生 γ→α+γ_b 分解，随后 γ_b→γ′(U₂Mo)，产物具有各向异性肿胀和辐照性能恶化。
2. **热稳定性与电子结构关联**：通过 Pauling 电负性均值 χ_P、Allen 电负性失配 δχ_A、有效构型熵 Λ 三个描述符可预测热稳定性。
3. **Hume-Rothery 规则的量化推广**：Λ = ΔS_c/δr² 表征错配熵与构型熵的竞争关系，是固溶体形成和热滞后的关键参数。
4. **Mo 当量筛选**：MoE = 1.0Mo + 1.13Nb + 2.42V + 1.86Ti + 1.1Zr，8 < MoE ≤ 27 时可避免 γ₀、α′、α″ 等亚稳相。

## Key Equations

### 组分特征加权平均
$$X = f_U X_U + f_{Mo} X_{Mo} + f_{Nb} X_{Nb} + f_{Zr} X_{Zr} + f_{Ti} X_{Ti} + f_V X_V \quad \text{(Eq. 1)}$$

### Landau 型自由能模型
$$F(T, \varepsilon) = \frac{1}{2}A(T - T_P^*)\varepsilon^2 + \frac{1}{4}\varepsilon^4 + \frac{1}{6}\varepsilon^6 \quad \text{(Eq. 2)}$$

其中 $T_P^* = T_P + \beta^2/(2A\alpha)$，ε 为序参量，β 和 α 分别反映掺杂原子与基体原子的弹性模量和局域应变。

### Mo 当量公式
$$\text{MoE} = 1.0\text{Mo} + 1.13\text{Nb} + 2.42\text{V} + 1.86\text{Ti} + 1.1\text{Zr} \quad (\text{wt}\%)$$

### 有效构型熵
$$\Lambda = \frac{\Delta S_c}{\delta r^2}$$

H 类合金范围：4 < Λ < 7，1.52 < χ_P < 1.58，1.8 < δχ_A < 3.3。

## Key Results

- 经三轮迭代筛选，发现 **10 种**单相 γ 合金在 RT–1000°C 无相变、铀密度 > 13 gU/cm³
- **3 种合金**（S41: U-87.9Mo-9.5Nb-2.6, S47: U-88.2Mo-8.4Ti-0.6V-2.8, S55: U-90.3Mo-7.7Nb-2）在 450°C/5天老化后无 DP 反应，优于 U-10wt%Mo（450°C/100h DP>66%）
- SVC-RBF 模型训练误差 10.9–17.1%，测试集表现最优

## Relevance to Knowledge Base

本文建立了 U-Mo 基合金热稳定性的定量预测框架，Landau 型模型为理解相变温度与合金元素的关系提供了物理基础。筛选出的新型合金成分对金属燃料设计具有直接指导意义。

## Related Work
- [[wiki/summaries/Lu_2018_CALPHAD_UFuels|Lu_2018_CALPHAD_UFuels]] — U-Mo基合金CALPHAD热力学评估
- [[wiki/summaries/2025_Zhang_ML_UraniumAlloy_CorrosionScreening|2025_Zhang_ML_UraniumAlloy_CorrosionScreening]] — 同为ML辅助铀合金设计筛选
- [[wiki/summaries/2025_Hanson_StablePredictableSwellingU10Mo|2025_Hanson_StablePredictableSwellingU10Mo]] — U-10Mo肿胀稳定性
- [[wiki/entities/FuelAlloy|FuelAlloy]] — U-Mo合金属金属燃料
- [[wiki/summaries/2025_Oberbauer_ThermalDiffusion_UMoX|2025_Oberbauer_ThermalDiffusion_UMoX]] — U-Mo热扩散与相稳定性
