# 参数数据比对报告 (v1 pdftotext vs v2 MinerU)

- **v1**: 982 条
- **v2**: 1006 条

## 统计摘要

| 类别 | 数量 |
|------|------|
| 匹配成功(值相同) | 241 |
| 新增参数 (v2独有) | 537 |
| 修正参数 (值不同) | 228 |
| 冲突参数 (差异>50%) | 43 |
| 缺失参数 (v1独有) | 513 |

## 冲突参数 (差异>50%)

| file | symbol/name | v1 | v2 | diff% |
|------|-------------|-----|-----|-------|
| 1985_Willard_SwellingPhaseReve | bu̇_critical | 8.8e11 | 2200000000000.0 | 150% |
| 1985_Willard_SwellingPhaseReve | bu̇_critical | 2.2e12 | 4800000000000.0 | 118% |
| 1985_Willard_SwellingPhaseReve | bu̇_critical | 4.8e12 | 9200000000000.0 | 92% |
| 1993_Rest_VoidSwellingAlphaU | dv0 | 2.0e-4 | 2e-08 | 100% |
| 1993_Rest_VoidSwellingAlphaU | em | 0.74 | 1.28 | 73% |
| 1993_Rest_VoidSwellingAlphaU | γ | 1.37 | 0.5 | 64% |
| 1993_Rest_VoidSwellingAlphaU | ρ | 7e13 | 20000000000000.0 | 71% |
| 2005_Rest_RecrystallizationSwe | γ | 0.5 | 1.0 | 100% |
| 2016_Sun_NeutronRadiographyU10 | λ | 5e-7 | 2.7 | 539999900% |
| 2016_Sun_NeutronRadiographyU10 | δ | 0.4 | 50.0 | 12400% |
| 2016_Sun_NeutronRadiographyU10 | σ | 1.8 | 4.1 | 128% |
| 2016_Sun_NeutronRadiographyU10 | p | 40 | 0.129 | 100% |
| 2021_Qian_RateTheoryUN | γ | 1.0 | 10.0 | 900% |
| 2021_Qian_RateTheoryUN | d | 1e-09 | 1.0 | 99999999900% |
| 2021_Qian_RateTheoryUN | b₀ | 2e-24 | 1e-18 | 49999900% |
| 2021_Qian_RateTheoryUN | b | 8.5e-32 | 0.02391 | 28129411764705880624057989201920% |
| 2021_Robinson_PredictiveSwelli | b | 0.02391 | 4e-21 | 100% |
| 2021_Zhang_EffectiveSwellingIn | k | 0.001 | 1.38e-23 | 100% |
| 2023_Ye_IntegratedSimulationU1 | fn | 0.0001 | 2e-07 | 100% |
| 2023_Ye_IntegratedSimulationU1 | z | 8 | 30000.0 | 374900% |
| 2023_Ye_IntegratedSimulationU1 | b₀ | 1e-18 | 2e-18 | 100% |
| 2023_Ye_IntegratedSimulationU1 | k | 0.0023 | 8.617e-05 | 96% |
| 2023_Ye_IntegratedSimulationU1 | ḟ | 6e+20 | 2.3 | 100% |
| 2023_Ye_IntegratedSimulationU1 | ḟ | 7.91e-08 | 2.4 | 3034133908% |
| 2026 - Porosity_ swelling_ and | $d_rx$ | 0.5 | 350.0 | 69900% |
| 2026 - Porosity_ swelling_ and | $t_foil$ | 0.0254 | 250.0 | 984152% |
| Aagesen - 2024 - Parameterizat | $2l$ | 1.5 | 10.0 | 567% |
| Aagesen et al._2022_Phase-fiel | $σ$ | 1.17 | 1.8 | 54% |
| Aagesen et al._2022_Phase-fiel | $lint$ | 10 | 1.5 | 85% |
| Casella et al_2017_Characteriz | $f_d$ | 2.68e21 | 4.32e+21 | 61% |
| Cui_et_al_2015_Modifications_a | a | 1.8e-20 | 5.47e-10 | 3038888888789% |
| Cui_et_al_2015_Modifications_a | z | 3e4 | 4 | 100% |
| Cui_et_al_2015_Modifications_a | f | 1e+20 | 6e+20 | 500% |
| Cui_et_al_2015_Modifications_a | b | 4e-21 | 2.5e-31 | 100% |
| Cui_et_al_2015_Modifications_a | p | 27.77 | 0 | 100% |
| Cui_et_al_2015_Modifications_a | p | 35.12 | 100 | 185% |
| hu_et_al_2016_effect_of_grain_ | f_n | 1e-05 | 0.02 | 199900% |
| hu_et_al_2016_effect_of_grain_ | z | 30000.0 | 8 | 100% |
| hu_et_al_2016_effect_of_grain_ | l | 101.47 | 50 | 51% |
| hu_et_al_2016_formation_mechan | γ | 10 | 0.6 | 94% |
| hu_et_al_2016_formation_mechan | p | 37.71 | 1.2 | 97% |
| muntaha_et_al_2024_impact_of_g | initial bubble count | 112 | 20 | 82% |
| muntaha_et_al_2024_impact_of_g | initial bubble radius | 3.4 | 480 | 14018% |

## 缺失参数 (v1独有，前50)

| file | symbol/name | value |
|------|-------------|-------|
| 1979_Ronchi_FissionGasSwelling | d_s | 4.9e-4*exp(-35000/T + Kp) |
| 1979_Ronchi_FissionGasSwelling | c₀ | 4π*d*q*f/b' |
| 1979_Ronchi_FissionGasSwelling | k_j | 4π*n_j*D_g |
| 1979_Ronchi_FissionGasSwelling | x | sqrt(6*D_b*t) |
| 1979_Ronchi_FissionGasSwelling | τ₀ | 1e6–1e8 |
| 1979_Ronchi_FissionGasSwelling | u | 1e-12 |
| 1979_Ronchi_FissionGasSwelling | n | 1e18–1e19 |
| 1979_Ronchi_FissionGasSwelling | ε̇ | K*σₑⁿ*exp(-ΔH/RT) |
| 1985_Willard_SwellingPhaseReve | d_r | 0.6e-18 to 1.4e-18 |
| 1985_Willard_SwellingPhaseReve | bu̇_critical | 9.2e12 |
| 1985_Willard_SwellingPhaseReve | fission rate range in experime | 2.5e12–8.0e12 |
| 1985_Willard_SwellingPhaseReve | gammatizing heat treatment | 1650°F for 24 hr |
| 1985_Willard_SwellingPhaseReve | partially transformed heat tre | 900°C for 100 hr |
| 1990_Hofman_SwellingBehaviorUP | incubation burnup before rapid | 0.3 |
| 1990_Hofman_SwellingBehaviorUP | rapid swelling interval | 1.0 |
| 1990_Hofman_SwellingBehaviorUP | δd/d | 16 |
| 1990_Hofman_SwellingBehaviorUP | δl/l | 3 |
| 1992_Rest_CavitationalSwelling | peak cavitational swelling tem | 773 |
| 1992_Rest_CavitationalSwelling | drc/dt | Ω/(4πRc²) × [ZcDvCv - Z_DiCi - ZvDvCv0(Rc)] |
| 1992_Rest_CavitationalSwelling | cv0(rc) | Cv0*exp[-(Pg - 2γ/Rc)*Ω/kT] |
| 1992_Rest_CavitationalSwelling | cv | [Ω/(4π*riv*Dv)]^(1/2) × K^(1/2) |
| 1992_Rest_CavitationalSwelling | rc | 2γ / [Pg + kT*ln((1-Z)*Cv/Cv0)] |
| 1993_Rest_VoidSwellingAlphaU | dv0 | 2.0e-8 |
| 1993_Rest_VoidSwellingAlphaU | em | 1.28 |
| 1993_Rest_VoidSwellingAlphaU | ρ | 2e13 |
| 1993_Rest_VoidSwellingAlphaU | δv/v | 50 |
| 1993_Rest_VoidSwellingAlphaU | drc/dt | Ω/(4πRc²) × [kvcDvCv - ki_cDiCi - kvcDvCv0(Rc)] × Cc |
| 1993_Rest_VoidSwellingAlphaU | cv0(rc) | Cv0*exp[-(Pg - 2γ/Rc - σ)*Ω/kT] |
| 1993_Rest_VoidSwellingAlphaU | dcgb/dt | -16πFbRb²DgbCb²/Cb - 4πRb²DgbCgCb - jg(t) + βf + BCbCgb |
| 1993_Rest_VoidSwellingAlphaU | dcgf/dt | -16πFfRf²DgfCf²/Cf - 4πRfDgfCfCf + jg(t) - ṙgf |
| 1993_Rest_VoidSwellingAlphaU | dcv/dt | ½Kf - kv²DvCv - αCvCi |
| 1993_Rest_VoidSwellingAlphaU | dci/dt | ½Kf - ki²DiCi - αCvCi |
| 1993_Rest_VoidSwellingAlphaU | kvc | 4πRcCc*(1 + k*Rc) |
| 1993_Rest_VoidSwellingAlphaU | kvd | Zvd*ρ |
| 1993_Rest_VoidSwellingAlphaU | kid | Zid*ρ |
| 1993_Rest_VoidSwellingAlphaU | ac | π*Rc²*Cc*f(Rc) |
| 2001_Rest_GRSIS_FissionGasMeta | r_b1 | 0.5 |
| 2001_Rest_GRSIS_FissionGasMeta | r_b2 | 2.5 |
| 2001_Rest_GRSIS_FissionGasMeta | r_b3 | 12.5 |
| 2001_Rest_GRSIS_FissionGasMeta | d_g0 | 9.5e-8 |
| 2001_Rest_GRSIS_FissionGasMeta | q_g | 32000 |
| 2001_Rest_GRSIS_FissionGasMeta | d_s0 | 9.5e-5 |
| 2001_Rest_GRSIS_FissionGasMeta | q_s | 32000 |
| 2001_Rest_GRSIS_FissionGasMeta | bubble-1 nucleation constant | 1e-20 |
| 2001_Rest_GRSIS_FissionGasMeta | e_gbi | 1.0 |
| 2001_Rest_GRSIS_FissionGasMeta | s_th | 0.2 |
| 2001_Rest_GRSIS_FissionGasMeta | δv/v | 0.2 |
| 2001_Rest_GRSIS_FissionGasMeta | d_bi | 3*a0^4/(2π*rbi^4)*Ds |
| 2005_Rest_RecrystallizationSwe | n | 1.65e-3 |
| 2005_Rest_RecrystallizationSwe | f_d^x | 4e24*(ḟ)^(2/15) |

> 共 513 条