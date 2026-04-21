# Karahan 2013 — Physical Mechanisms (FEAST-METAL)

**Source:** [[wiki/summaries/2013_Karahan_FEAST_METAL_FuelSwelling|Karahan 2013 Index]]

---

## 1. Fission Gas Bubble Nucleation and Growth

Bubbles nucleate **isotropically** within the [[wiki/entities/FuelAlloy|U-Pu-Zr fuel]] matrix. This is valid because the fuel operates above half its melting point and phase boundaries are nearly uniformly distributed within grains.

Two bubble groups with **fixed number of gas atoms** (constant atom number grouping):
- **Small bubbles**: grow via [[wiki/entities/FissionGasDiffusion|gas diffusion]] and transition to large bubbles
- **Large bubbles**: dominant contributors to swelling

Bubble radius is calculated using the **Van der Waals equation** given hydrostatic stress and temperature.

## 2. Phase-Dependent Bubble Morphology

| Phase | Structure | Bubble Shape | Bubble Size |
|-------|-----------|-------------|-------------|
| **(α + δ) dual phase** (cold peripheral) | Stiff orthorhombic α | Ellipsoidal, along α/δ boundaries | ~7×7×1 μm |
| **(β + δ) dual phase** | Stiff tetragonal β precipitates | Spherical, small | ~3 μm |
| **Single γ phase** (BCC, high T) | Soft → large growth | Spherical | up to ~10 μm |

## 3. Open Porosity Formation (Fuel Fracture)

Above the **10% gas swelling threshold**, interconnected open porosity forms via:
- Probabilistic crack-length model: bubble coalescence creates cracks
- Critical crack length density criterion: **$1.5\times10^{13}$ m/m³** above **30 μm**
- Threshold robust across bubble diameter range 1.5–6 μm

## 4. Pressure Sintering of Open Porosity

Open porosity (at plenum pressure) is sintered under applied hydrostatic stress in creep-dependent form.
- Compressibility factor $\alpha$ depends on open porosity fraction
- **Dual phases are less compressible** than single γ phase: correction factor $C = 0.23$ vs. $C = 1.0$

## 5. Solid Fission Product Swelling

Continues after gas swelling saturates at **1.2% per at.% burnup** (Hofman et al. 1997). Open porosity is compressed by contact pressure to accommodate solid FP swelling.

## 6. Fuel-Cladding Mechanical Interaction (FCMI)

Contact pressure ensures fuel and clad displacement rates are identical. Clad strain comes mainly from:
- Irradiation creep
- Void swelling

## 7. Fuel-Cladding Chemical Interaction (FCCI)

Lanthanide attack on the clad inner surface, controlled by keeping peak clad temperature **below 550 °C**.

---

## See Also

- [[wiki/summaries/2013_Karahan_FEAST_METAL_FuelSwelling/KeyEquations|Key Equations & Parameters]]
- [[wiki/summaries/2013_Karahan_FEAST_METAL_FuelSwelling/ExperimentalData|Experimental Data & Benchmark Results]]
- [[wiki/entities/FuelAlloy|FuelAlloy]] — U-Pu-Zr metallic fuel properties
- [[wiki/entities/FissionGasDiffusion|FissionGasDiffusion]] — Phase-dependent gas diffusivity
- [[wiki/summaries/2001_Rest_GRSIS_FissionGasMetallic|Rest 2001 — GRSIS metallic fuel gas release model]]
