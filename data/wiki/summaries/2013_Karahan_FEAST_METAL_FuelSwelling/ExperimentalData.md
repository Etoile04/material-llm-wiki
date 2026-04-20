# Karahan 2013 — Experimental Data & Benchmark Results (FEAST-METAL)

**Source:** [[wiki/summaries/2013_Karahan_FEAST_METAL_FuelSwelling|Karahan 2013 Index]]

---

## EBR-II Benchmark: X425 Assembly (U-19Pu-10Zr)

| Parameter | Value |
|---|---|
| Fuel composition | [[wiki/entities/FuelAlloy\|U-19Pu-10Zr]] |
| Cladding | HT9 |
| Fuel slug density | 15.8 g/cm³ |
| Fuel slug radius | 2.16 mm |
| Clad inner radius | 2.54 mm |
| Clad outer radius | 2.92 mm |
| Fuel smear density | 72.3% |
| Fuel active length | 34.3 cm |
| Plenum-to-fuel ratio | 1.0 |
| Peak linear heat rate | 40 kW/m |
| Peak clad temperature | 590 °C |
| Peak burnup | 18.9 at.% |
| Peak dose (EOL) | ~95 dpa |

## EBR-II Benchmark: X430 Assembly

| Parameter | Value |
|---|---|
| Fuel slug radius | 2.86 mm |
| Clad inner radius | 3.28 mm |
| Clad outer radius | 3.68 mm |
| Fuel smear density | 76% |
| Plenum-to-fuel ratio | 1.4 |
| Peak linear heat rate | 50 kW/m |
| Peak burnup | 11.6 at.% |
| Peak dose (EOL) | ~60 dpa |

## Benchmark Results

| Quantity | X425 | X430 |
|----------|------|------|
| Clad hoop strain | ~2.0% at 18.9 at.% ✓ | ~1.0% at 11.6 at.% ✓ |
| Fission gas release | ~80% at EOL ✓ | ~65% at EOL ✓ |
| Fuel axial elongation (calc.) | ~7.8% | ~7.1% |
| Fuel axial elongation (exp.) | 8.5±1.2% | 6.5* |

## Ultra-High Burnup Design (U-6Zr, Vented Fuel)

| Parameter | Value |
|---|---|
| Fuel composition | U-6Zr |
| Fuel slug density | 17 g/cm³ |
| Fuel slug radius | 3.0 mm |
| Fuel smear density | 60% |
| Peak linear heat rate | 50 kW/m |
| Peak clad temperature | 550 °C |
| Peak burnup | **36 at.%** |
| Peak dose (EOL) | ~500 dpa |

### Ultra-High Burnup Predictions

| Quantity | Predicted Value |
|----------|----------------|
| Peak clad hoop strain | **3%** (1% void + 2% creep) |
| Fission gas release | **95%** |
| Fuel axial elongation | **20%** |
| Clad wastage | <20% of clad thickness |

---

## Key Model Improvements

1. Bubble grouping: constant volume → **constant atom number**
2. Phase-dependent morphology (separate shapes/sizes per phase)
3. Phase-dependent [[wiki/entities/FissionGasDiffusion|gas diffusion]]: separate activation energies (52,000 vs. 28,500 cal/mol)
4. Ellipsoidal corrections for (α+δ) region
5. Pressure sintering: $C = 0.23$ for dual phases vs. $C = 1.0$ for γ
6. Solid FP swelling reduced from 1.5% to **1.2%/at.%**
7. Probabilistic verification: 10% gas swelling threshold confirmed for 1.5–6 μm bubbles

---

## Key Findings

1. Phase-dependent modeling significantly improves predictions
2. 10% gas swelling threshold is robust (probabilistic crack analysis)
3. Dual-phase sintering overestimated by previous models ($C = 0.23$ vs. $C = 1.0$)
4. X425 (72.3% smear) reached 18.9 at.% with no failure — most successful EBR-II assembly
5. X430 (76% smear) limited to 11.6 at.% — higher smear density → earlier FCMI
6. Ultra-high burnup (36 at.%) requires ~60% smear density to limit clad strain to ~3%
7. Peak clad temperature below 550 °C controls lanthanide migration and clad wastage

---

## See Also

- [[wiki/summaries/2013_Karahan_FEAST_METAL_FuelSwelling/PhysicalMechanisms|Physical Mechanisms]]
- [[wiki/summaries/2013_Karahan_FEAST_METAL_FuelSwelling/KeyEquations|Key Equations]]
- [[wiki/entities/FuelAlloy|FuelAlloy]] — U-Pu-Zr properties
- [[wiki/summaries/1990_Hofman_SwellingBehaviorUPuZr|Hofman 1990 — EBR-II swelling behavior]]
- [[wiki/summaries/2001_Rest_GRSIS_FissionGasMetallic|Rest 2001 — GRSIS gas release model]]
