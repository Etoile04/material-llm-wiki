# Karahan 2013 — Key Equations & Parameters (FEAST-METAL)

**Source:** [[wiki/summaries/2013_Karahan_FEAST_METAL_FuelSwelling|Karahan 2013 Index]]

---

## Fission Gas Diffusion Coefficient (Phase-Dependent)

**Dual phase** ($T < T_6$, where $T_6 = 923\,\text{K}$ for U-19Pu-10Zr):

$$D_g = 1.0 \times 10^{-4} \exp\!\left(-\frac{52{,}000}{RT}\right) \quad [\text{m}^2/\text{s}]$$

**Single γ phase** ($T > T_6$):

$$D_g = 0.3 \times 10^{-8} \exp\!\left(-\frac{28{,}500}{RT}\right) \quad [\text{m}^2/\text{s}]$$

where $R = 1.987\,\text{cal/(mol·K)}$.

## Pressure Sintering Compressibility Factor

$$\alpha = \begin{cases}
0 & \text{if } \varepsilon_{\text{opn}} = 0 \\
C \times \tfrac{1}{6} \times \varepsilon_{\text{opn}} \times 0.1^{1.5} & \text{if } 0 < \varepsilon_{\text{opn}} < 0.1 \\
C \times \tfrac{1}{6} & \text{if } \varepsilon_{\text{opn}} > 0.1
\end{cases}$$

- $C = 1.0$ (single γ phase)
- $C = 0.23$ (dual phases)

## Solid Fission Product Swelling Rate

- **Best estimate: 1.2% per at.% burnup** (corrected from previous 1.5%)
- Corrected proportionally to heavy metal density for non-reference compositions

## Anisotropic Fuel Axial Deformation

$$\Delta r_{\text{gap}} = (1 - f) \times \Delta r_{\text{gap},0}$$

where $f$ is an anisotropy factor (function of Pu content and $q'/D$ ratio).

---

## Bubble Group Parameters (Table 1)

| Phase Structure | Small Bubble Atoms | Small Bubble Shape | Large Bubble Atoms | Large Bubble Shape |
|---|---|---|---|---|
| (α + δ) | $3.7\times10^6$ | ~0.2×0.2×0.05 μm, ellipsoidal | $9.8\times10^9$ | ~7×7×1 μm, ellipsoidal |
| (β + δ) | $2.0\times10^6$ | ~0.15 μm, spherical | $5.4\times10^9$ | ~3 μm, spherical |
| Single γ | $7.5\times10^7$ | ~0.5 μm, spherical | $2.0\times10^{11}$ | ~10 μm, spherical |

## Open Porosity Formation Parameters

| Parameter | Value |
|-----------|-------|
| Open porosity formation coefficient | 0.4 |
| Open porosity surface area correction factor | 0.3 |
| Gas swelling threshold for open porosity | 10% |

---

## See Also

- [[wiki/summaries/2013_Karahan_FEAST_METAL_FuelSwelling/PhysicalMechanisms|Physical Mechanisms]]
- [[wiki/summaries/2013_Karahan_FEAST_METAL_FuelSwelling/ExperimentalData|Experimental Data & Benchmark Results]]
- [[wiki/entities/FissionGasDiffusion|FissionGasDiffusion]]
- [[wiki/summaries/1979_Ronchi_FissionGasSwellingMX_Fuels|Ronchi 1979 — MX fuel swelling physics]]
