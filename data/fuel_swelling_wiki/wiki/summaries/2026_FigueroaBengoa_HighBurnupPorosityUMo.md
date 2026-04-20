# Porosity, Swelling, and Composition Evolution in High-Burnup Monolithic U-Mo Fuel

## Metadata

- **Title:** Porosity, swelling, and composition evolution in high-burnup monolithic U-Mo fuel
- **Authors:** A. Figueroa Bengoa, Walter J. Williams, Daniel Murray, Brandon D. Miller, Maria A. Okuniewski
- **Year:** 2026
- **Journal:** Journal of Nuclear Materials, 618, 156165
- **DOI:** 10.1016/j.jnucmat.2025.156165
- **Affiliations:** Purdue University; Idaho National Laboratory

## Physical Mechanisms

### High-Burnup Porosity Evolution (Post-Recrystallization Regime)
- **Recrystallization completion:** Irradiation-induced recrystallization of U-10wt.%Mo completes between ~3–6 × 10²¹ fissions/cm³, producing nano-grained structure (~200–500 nm grain size)
- **Post-recrystallization porosity:** Increased grain boundary area and reduced diffusion path length for point defects cause enhanced porosity nucleation and growth from fission gas and vacancy accumulation at grain boundaries
- **Two-part primary swelling behavior:**
  1. Initial linear swelling rate (solid + gaseous fission products in superlattice)
  2. Increased second-order swelling rate from porosity accumulation after recrystallization

### Bimodal Porosity Distribution
- **First mode:** Centered at ~0.23 µm equivalent pore diameter (consistent across all fission densities)
- **Second mode:** Centered at ~0.98 µm (8.86 × 10²¹) to ~1.13 µm (9.05–9.36 × 10²¹ fissions/cm³)
- Small pores (<0.3 µm) increase in number density up to ~9.05 × 10²¹, then decrease (coalescence dominates)
- Large pores (>1.5 µm) increase monotonically with burnup
- Interconnected porosity (>2.55 µm) appears ~5 µm from diffusion barrier

### Delamination and Cracking
- Cracks propagate through interconnected porosity sublayer ~5 µm from Zr diffusion barrier
- Zr penetration into fuel does NOT arrest crack propagation
- Delamination correlates with regions of highest interconnected porosity

### Fission Product Distribution
- **Sr, Ba, Ce, Cs:** Precipitated inside pores
- **Nd:** Accumulated adjacent to (near) large pores
- Zr-fuel interaction layer shows Zr tendrils penetrating into fuel at high burnup

## Key Equations

### Robinson-Williams Swelling Model (reconstructed)

Local volumetric swelling as a function of fission density:

$$\frac{\Delta V}{V_0} = A \cdot F_D + B \cdot F_D^2$$

where $F_D$ is the local fission density (fissions/cm³) and $A$, $B$ are empirical coefficients. Experimental data from this study fall within or near the model prediction bounds at $F_D$ up to $9.39 \times 10^{21}$ f/cm³.

### Porosity Volume Fraction (from stereology)

$$V_v = \frac{A_p}{A_t} = \frac{\sum_{i} a_i}{A_t}$$

where $A_p$ is the total pore area, $A_t$ is the total measurement area, and $a_i$ is the area of individual pores. Measured by both image segmentation and ASTM E562 point counting methods.

### Schwartz-Saltykov Algorithm — 2D to 3D Conversion

Converts 2D sectional pore size distributions to 3D volume distributions:

$$N_v(D_j) = \frac{1}{\Delta D} \left[ n_j - \sum_{i=1}^{j-1} N_v(D_i) \cdot P(j-i) \cdot \Delta D \right]$$

where $N_v(D_j)$ is the number density of pores with diameter $D_j$, $n_j$ is the number of intersections in bin $j$, $\Delta D$ is the bin size (0.15 µm), and $P(j-i)$ is the probability kernel for a sphere of diameter $D_i$ producing a section of diameter $D_j$.

### Bimodal Porosity Distribution (from experimental data)

The pore size distribution is well-described by a bimodal model:

$$f(D) = w_1 \mathcal{N}(\mu_1, \sigma_1^2) + w_2 \mathcal{N}(\mu_2, \sigma_2^2)$$

| Mode | Center (µm) | Evolution |
|------|-------------|----------|
| Small pores | ~0.23 | Stable across all $F_D$ |
| Large pores | 0.98 → 1.13 | Shifts right with increasing $F_D$ |

### Post-Recrystallization Swelling Rate (reconstructed)

After recrystallization completion ($F_D > 6 \times 10^{21}$ f/cm³), enhanced grain boundary area ($A_{GB} \propto 1/d_{rx}$ where $d_{rx} \approx 200$–$500$ nm) accelerates porosity accumulation:

$$\frac{dV_v}{dF_D} = \frac{dV_v}{dF_D}\bigg|_{solid} + \frac{dV_v}{dF_D}\bigg|_{gas} + \frac{dV_v}{dF_D}\bigg|_{pore}$$

where the pore contribution term increases sharply due to reduced diffusion path lengths in the nano-grained recrystallized structure.

### Pore Coalescence Criterion (reconstructed)

When pore number density of small pores (<0.3 µm) decreases after $F_D \approx 9.05 \times 10^{21}$ f/cm³ while large pores continue growing:

$$\frac{dN_{small}}{dF_D} < 0 \quad \text{(coalescence dominates)}$$

$$\frac{dN_{large}}{dF_D} > 0 \quad \text{(growth dominates)}$$

This signals the transition from nucleation-dominated to coalescence-dominated porosity evolution.

## Parameters

### Irradiation Conditions
| Parameter | Value |
|-----------|-------|
| Fuel composition | U-10wt.%Mo |
| Enrichment | 70% ²³⁵U |
| Reactor | ATR (Idaho National Laboratory) |
| Irradiation cycles | 3 cycles, 137.2 days total |
| Average plate fission density | 7.71 × 10²¹ fissions/cm³ |
| Peak fission density | 9.39 × 10²¹ fissions/cm³ |
| As-fabricated grain size | ~10 µm |
| Recrystallized grain size | ~200–500 nm |
| Fuel foil thickness | ~250 µm |
| Zr barrier thickness | ~25 µm |

### Porosity Data (FIB-cuboid specimens)
| Fission Density (fissions/cm³) | Porosity Vv (%) | Avg Pore Size (µm) | Number Density (pores/µm²) |
|-------------------------------|-----------------|---------------------|---------------------------|
| 8.86 × 10²¹ | 27.77 ± 0.51 | 0.45 ± 0.01 | 0.97 ± 0.05 |
| 9.05 × 10²¹ | 35.12 ± 1.54 | 0.40 ± 0.01 | 1.19 ± 0.03 |
| 9.36 × 10²¹ | 37.71 ± 0.44 | 0.49 ± 0.02 | 0.98 ± 0.03 |

### Point Counting Validation
| Specimen | Segmentation Vv (%) | Point Counting Vv (%) |
|----------|---------------------|----------------------|
| 8.86 × 10²¹ | 28.53 | 29.84 ± 1.24 |
| 9.36 × 10²¹ | 36.84 | 33.76 ± 0.36 |

## Experimental Data

### Key Findings
1. **Porosity plateaus** at burnups > 6 × 10²¹ fissions/cm³ (volume fraction stabilizes), while **pore size grows linearly** with fission density
2. **Bimodal porosity** evolves differently: small pore mode stable at ~0.23 µm; large pore mode shifts from 0.98 to 1.13 µm
3. **Interconnected porosity sublayer** at ~5 µm from diffusion barrier is the primary crack propagation path
4. Local swelling measurements fall within or near Robinson-Williams model prediction bounds
5. First systematic study of **bimodal porosity progression** in fully recrystallized high-burnup monolithic U-Mo fuel

### Zr Diffusion Barrier Interaction
- Multi-layered interaction structure dissipates during irradiation
- At 9.8 × 10²¹ fissions/cm³: U-Zr₂ sublayer becomes discontinuous (Zr penetrates fuel)
- Zr tendrils extend into fuel visible in all three high-burnup specimens

## Relationships to Other Work

- **AFIP-6-MkII experiment:** Previous porosity data above recrystallization regime, but suspect due to uneven Mo distribution
- **U-7wt.%Mo dispersion fuel:** Similar porosity behavior studied, but not directly comparable due to matrix-fuel interactions
- **Robinson-Williams model:** Local swelling predictions validated against new high-burnup data
- **Jian et al. (2022):** Mechanistic swelling model — current data provides high-burnup validation
- **Gan et al. (2017):** Nano-bubble superlattice collapse and recrystallization onset consistent with observations
- **S-µCT studies:** Zr penetration observations corroborated

## Relationships

- [[wiki/entities/FuelAlloy|FuelAlloy]] — high-burnup monolithic U-10Mo fuel porosity and swelling at 8.86–9.36×10²¹ f/cm³ are the subject
- [[wiki/entities/Recrystallization|Recrystallization]] — recrystallization completes at ~3–6×10²¹ f/cm³; post-recrystallization bimodal porosity evolution is the main finding
- [[wiki/concepts/SwellingMechanisms|SwellingMechanisms]] — bimodal porosity distribution evolution, interconnected porosity sublayer, and delamination mechanisms are characterized
- [[wiki/concepts/SwellingModelComparison|SwellingModelComparison]] — Robinson-Williams model prediction bounds are validated against new high-burnup data
- [[wiki/summaries/2021_Robinson_PredictiveSwellingUMoMonolithic|2021_Robinson_PredictiveSwellingUMoMonolithic]] — empirical model whose bounds are validated here at highest burnups
- [[wiki/summaries/2022_Jian_FissionGasSwellingModelU10Mo|2022_Jian_FissionGasSwellingModelU10Mo]] — mechanistic swelling model that this high-burnup data validates/challenges
- [[wiki/summaries/2025_Hanson_StablePredictableSwellingU10Mo|2025_Hanson_StablePredictableSwellingU10Mo]] — MP-1 stable swelling study; this provides higher burnup data beyond MP-1 range
