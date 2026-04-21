# Batch D 提取任务清单

> 日期: 2026-04-21
> 目标: 提取 raw/mineru 中剩余 9 篇文献（去重后）

## 文献列表

| # | 目录名 | 规范化 slug | 公式 | 主题 |
|---|--------|------------|------|------|
| 1 | 151846_f3c95453 | 2024_MURR_LEU_U10Mo_SwellingCreep | 🔄重转 | U-10Mo 肿胀+蠕变 |
| 2 | Atomistic simulation of cubic and tetragonal phases of U-Mo alloy_ structure and_06dff417 | 2025_Atomistic_U-Mo_DefectEnergetics | ✅ 28 | 原子模拟缺陷能 |
| 3 | Evidence of Xe-incorporation in the bubble superlattice in irradiated U-Mo fuel_d23dcebc | 2024_XeIncorporation_BubbleSuperlattice | ✅ 42 | 气泡超晶格 Xe |
| 4 | Fission_gas_bubble_nucleated_cavitational_swelling_of_alpha_phase_of_irradiated_UPuZr_fuel | 1993_Rest_CavitationalSwellingAlphaUPuZr | ✅ 16 | α相空穴肿胀 |
| 5 | Interdiffusion Between Zr Diffusion Barrier and U-Mo Alloy_6dfb90c4 | 2020_Xie_Interdiffusion_ZrUMo | ✅ 6 | 扩散/FCCI |
| 6 | Kim, Hofman, Cheon_2013_Recrystallization and fission-gas-bubble swelling of U-Mo fuel | 2013_Kim_Recrystallization_FGBSwelling_UMo | ✅ 30 | 再结晶+肿胀 |
| 7 | R.M. WILLARD_A.R. SCHMITT_1985_Irradiation Swelling, Phase Reversion, and Intergranular Cracking of U-10 wt % | 1985_Willard_SwellingPhaseReversion_U10Mo | 🔄重转 | 经典肿胀 |
| 8 | TRANSFORMATION CHARACTERISTICS OF U-Mo AND U-Mo-Ti ALLOYS_b2a56895 | 2024_Transformation_UMo_UMoTi | ✅ 42 | 相变 |
| 9 | Yun 等 - Investigation of swelling behaviors of U-10Zr meta | 2024_Yun_U10Zr_Swelling | 🔄重转 | U-Zr 肿胀 |

## 提取规范

- 按 SKILL.md ingest 流程执行
- Summary 200-400 词中文，模型类论文必须含 Key Equations
- 参数 JSON 带 value_type 字段
- validate FAIL 必须 = 0
- 公式覆盖率 100%（模型类论文）
