# Thermal Stability of Fission Gas Bubble Superlattice in Irradiated U–10Mo Fuel

## Metadata

| Field | Value |
|-------|-------|
| **Authors** | J. Gan, D.D. Keiser Jr., B.D. Miller, A.B. Robinson, D.M. Wachs, M.K. Meyer |
| **Year** | 2015 |
| **Journal** | Journal of Nuclear Materials |
| **Volume/Pages** | 464, 1–5 |
| **DOI** | 10.1016/j.jnucmat.2015.04.023 |
| **Affiliation** | Idaho National Laboratory, USA |
| **Fuel Type** | U–10Mo monolithic |
| **Sample** | Fuel plate L1F040 |

## Physical Mechanisms

### Gas Bubble Superlattice (GBS) Formation
- Fission gas bubbles (predominantly Xe, Xe/Kr ≈ 10) self-organize into a **3D ordered superlattice** within the bcc γ-phase U–Mo matrix
- The GBS has an **fcc structure** in the bcc host material — contradictory to ion irradiation GBS where lattice matches host
- GBS develops between irradiation temperatures of **0.15Tm and 0.35Tm** (from He-irradiated Mo studies, Lawson & Johnson 1998)
- For Mo: Tm = 2623°C, so GBS window = 161–741°C
- U–10Mo irradiation at 140°C = **0.29Tm** (within the window)

### Xe Mobility and Thermal Stability
- **Xe atomic radius: 2.15 Å** vs He: 0.3 Å — much larger strain energy in matrix
- Low Xe mobility in U–Mo is key to GBS thermal stability
- **Solid fission products (SFP) in solution** create large strain fields that increase the diffusion barrier for Xe
- No SFP precipitates found in U–Mo matrix filled with GBS — SFP remain dissolved

### Bubble Migration and Coalescence
- **Not observed** during heating up to 850°C
- No large bubble development or GBS bubble shrinkage detected

## Key Equations & Parameters

| Parameter | Value | Notes |
|-----------|-------|-------|
| U–10Mo melting point (Tm) | ~1175°C | From U–Mo phase diagram |
| Irradiation temperature (Tirr) | 140°C | Local fuel temperature |
| Tirr/Tm | 0.29 | Within GBS formation window (0.15–0.35Tm) |
| Max heating temperature (Tht) | 850°C | In-situ TEM heating |
| Tht/Tm | 0.78 | Highest annealing homologous temperature |
| Fission density (sample) | 3.5 × 10²¹ fissions/cm³ | Local fission density |
| Average bubble size (low fd) | 2 nm | At 1.41 × 10²¹ fissions/cm³ |
| Average bubble size (intermediate fd) | 3.1 nm | At 3.3 × 10²¹ fissions/cm³ |
| Bubble size (remnant GBS) | 3.6 nm | At 5.2 × 10²¹ fissions/cm³ |
| Superlattice constant | 12 nm | At 3.3 × 10²¹ fissions/cm³ |
| Superlattice constant (remnant) | 12 nm | At 5.2 × 10²¹ fissions/cm³ |
| GBS structure | fcc | In bcc U–Mo host |
| Xe/Kr ratio | ~10 | GBS predominantly Xe |
| Fission product kinetic energy | 169 MeV average | Per fission event |
| Fission fragment energy | ~90 MeV | Dominant radiation damage source |
| Xe atomic radius | 2.15 Å | Much larger than He (0.3 Å) |
| Heating ramp rate (RT–700°C) | ~10°C/min | |
| Hold at 700°C | ~34 min | |
| Heating ramp (700–850°C) | ~5°C/min | |
| Total heating time | ~90 min to 700°C + 34 min hold + ramp to 850°C | |
| TEM column pressure | (0.65–1.5) × 10⁻⁵ Pa | During heating |
| FIB-TEM sample size | ~10 × 15 μm² | |

### GBS Formation Window (Empirical Rule)

The gas bubble superlattice forms within a homologous temperature range:

$$0.15 T_m \leq T_{irr} \leq 0.35 T_m$$

For U–10Mo ($T_m \approx 1175\,°C$): $T_{irr} \in [120, 375]\,°C$.

### Homologous Temperature

$$T_h = \frac{T}{T_m}$$

The paper's irradiation temperature: $T_h = 0.29$ (well within formation window). Maximum annealing temperature: $T_h = 0.78$ (GBS still stable).

### Bubble-Induced Swelling (Reconstructed)

For GBS with bubble radius $r_b$ and number density $N_b$:

$$\frac{\Delta V}{V} = \frac{4}{3}\pi r_b^3 N_b$$

With $r_b \approx 3.1\,\text{nm}$ and superlattice constant $a_{SL} = 12\,\text{nm}$ (fcc), $N_b = 4/a_{SL}^3 \approx 2.3 \times 10^{23}\,\text{m}^{-3}$, giving $\Delta V/V \approx 0.3\%$.

### Xe Diffusivity Activation

$$D_{Xe} = D_0 \exp\left(-\frac{E_m}{k_B T}\right)$$

The extremely low Xe mobility in U–10Mo is attributed to: (1) large Xe atomic radius (2.15 Å) causing high migration energy $E_m$, and (2) strain fields from dissolved solid fission products further increasing the effective barrier.

### Reference: Xe Mobility in Other Systems
- Xe in polycrystalline Al: **immobile below 260°C (0.57Tm)**, highly mobile at 290°C (0.60Tm) (Weber & Lieb 1989)
- Xe in U–10Mo: still low mobility at 700°C (0.67Tm) — suppressed by SFP in solution

### TTT Diagram for U–10Mo γ-Phase Stability
- γ-phase decomposition starts at ~5 h at 500°C
- γ-phase stable above 580°C (stable high-temperature bcc)

## Experimental Data

### In-Situ Heating TEM Experiment

| Temperature (°C) | Observation |
|-------------------|-------------|
| RT (before) | GBS well-ordered at zone [110] |
| 199 | GBS intact |
| 400 | GBS intact |
| 603 | GBS intact |
| 700–704 | GBS stable during 34 min hold |
| 793 | GBS intact |
| 850 (max) | GBS intact, then cooling |
| RT (after) | No significant change in lattice constant or bubble size |

### GBS Evolution with Fission Density (from prior work)

| Fission Density (10²¹ f/cm³) | Avg Bubble Size (nm) | Superlattice Constant (nm) | GBS Status |
|-------------------------------|-----------------------|---------------------------|------------|
| 1.41 | 2.0 | — | Developed |
| 3.3 | 3.1 | 12 | Well-developed, fcc structure |
| 5.2 | 3.6 | 12 | Remnant (majority collapsed, grain subdivision) |

## Model Description

This is primarily an **experimental paper** (in-situ heating TEM). No computational model is presented. However, key mechanistic insights relevant to modeling:

1. **GBS thermal stability is extraordinarily high** — stable up to 0.78Tm without coarsening
2. **Xe mobility is the controlling factor** — low Xe mobility in U–Mo due to large atomic size mismatch and SFP strain fields
3. **No coarsening model needed** at temperatures below ~850°C for U–10Mo GBS
4. GBS formation window: **0.15Tm ≤ T ≤ 0.35Tm** (empirical rule from ion irradiation studies)

## Key Findings

1. **Extraordinary thermal stability**: Xe GBS in U–10Mo remains stable up to 850°C (0.78Tm) — no bubble migration, coalescence, or lattice collapse
2. **No change after 34 min at 700°C**: bubble size and superlattice constant unchanged
3. **γ-phase (bcc) stability**: U–10Mo γ-phase remained stable through entire heating cycle (500–846°C for 80 min accumulated)
4. **SFP strain effect**: Solid fission products in solution likely suppress Xe diffusion, enhancing GBS stability beyond what ion irradiation data would predict
5. **Surface oxide effect**: Oxide layer on FIB-TEM sample may reduce surface sink strength, preserving Xe in near-surface region
6. **GBS collapse at high fission density**: At 5.2 × 10²¹ fissions/cm³, grain subdivision destroys most GBS, though remnant GBS persists

## Relevance to JSRT Model

### Direct Relevance
- **GBS stability regime**: Provides definitive experimental evidence that GBS in U–10Mo does not coarsen or collapse below 850°C — confirms that GBS-related swelling is stable during normal operation (<250°C)
- **Bubble size data**: Quantitative bubble sizes (2–3.6 nm) and superlattice constant (12 nm) at known fission densities for model calibration
- **No Ostwald ripening**: Absence of coarsening up to 0.78Tm suggests GBS bubble size may be modeled as irradiation-driven rather than thermally-driven

### Parameters for JSRT
- GBS bubble size: **2–3.6 nm** (fission density dependent)
- GBS lattice constant: **12 nm**
- Fcc superlattice in bcc host
- GBS formation window: **0.15–0.35 Tm**
- Xe/Kr ratio in bubbles: **~10**
- Critical fission density for GBS collapse: **~5.2 × 10²¹ fissions/cm³**

### Gaps / Limitations
- Single sample, single fission density (3.5 × 10²¹ f/cm³)
- FIB-TEM sample may not represent bulk behavior (surface effects, small volume)
- No quantitative Xe density in bubbles measured
- No bulk furnace annealing verification (acknowledged by authors)
- Temperature of specimen uncertain (thermocouple on furnace, not specimen)

## Relationships

- [[wiki/entities/GasBubbleSuperlattice|GasBubbleSuperlattice]] — thermal stability of the fcc gas bubble superlattice in bcc U-10Mo up to 850°C is the central finding
- [[wiki/entities/FuelAlloy|FuelAlloy]] — U-10Mo monolithic fuel plate (L1F040) is the subject material
- [[wiki/entities/FissionGasDiffusion|FissionGasDiffusion]] — low Xe mobility suppressed by solid fission product strain fields explains GBS stability
- [[wiki/summaries/2015_Miller_TEMGasBubbleSuperlatticeU7Mo|2015_Miller_TEMGasBubbleSuperlatticeU7Mo]] — companion TEM study on GBS structure and collapse in U-7Mo
- [[wiki/summaries/2016_Hu_GasBubbleSuperlatticeFormationPF|2016_Hu_GasBubbleSuperlatticeFormationPF]] — Hu's phase-field model explains the 1-D SIA migration mechanism for GBS formation
- [[wiki/summaries/2013_Kim_RecrystallizationFGBSwellingUMo|2013_Kim_RecrystallizationFGBSwellingUMo]] — GBS collapse at ~5×10²¹ f/cm³ coincides with recrystallization onset described by Kim (2013)

## Related Work
- [[wiki/summaries/2015_Miller_TEMGasBubbleSuperlatticeU7Mo|2015_Miller_TEMGasBubbleSuperlatticeU7Mo]] — companion TEM study on GBS structure and collapse in U-7Mo dispersion fuel
- [[wiki/summaries/2016_Hu_GasBubbleSuperlatticeFormationPF|2016_Hu_GasBubbleSuperlatticeFormationPF]] — phase-field model explaining the 1-D SIA mechanism for GBS formation
- [[wiki/summaries/2013_Kim_RecrystallizationFGBSwellingUMo|2013_Kim_RecrystallizationFGBSwellingUMo]] — GBS collapse at ~5×10²¹ f/cm³ coincides with recrystallization onset
- [[wiki/summaries/2023_Zhang_Review_VoidBubbleSuperlattice_SelfOrganization|2023_Zhang_Review_VoidBubbleSuperlattice_SelfOrganization]] — comprehensive review of void/bubble superlattice self-organization phenomena
- [[wiki/summaries/2024_Arivu_APTSegregationGasBubblesUMo|2024_Arivu_APTSegregationGasBubblesUMo]] — APT characterization of gas bubble segregation in U-Mo
- [[wiki/entities/GasBubbleSuperlattice|GasBubbleSuperlattice]] — central phenomenon: thermal stability of fcc superlattice in bcc U-10Mo
