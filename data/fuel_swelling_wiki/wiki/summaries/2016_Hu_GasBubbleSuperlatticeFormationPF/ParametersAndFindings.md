# Hu 2016 — Parameters, Key Findings & Relationships

**Source:** [[wiki/summaries/2016_Hu_GasBubbleSuperlatticeFormationPF|Hu 2016 Index]]

---

## Simulation Parameters (Table 1)

| Parameter | Value | Notes |
|-----------|-------|-------|
| Grid size ($dx$) | 0.52 nm | Resolves nano-sized bubbles |
| Temperature | 400 K | UMo fuel operating temperature |
| $D_{Xe} = D_{\text{Vac}}$ | $2.0\times10^{-20}$ m²/s | Isotropic diffusion |
| $D^* = D_{\text{Int}}/D_{Xe}$ | $10$–$10^6$ | **Key parameter** controlling superlattice formation |
| Gas bubble interfacial energy | 0.6 J/m² | |
| Grain boundary energy | 1.0 J/m² | |
| Equilibrium pressure (400 K) | ~1.2 GPa | For nanosized Xe bubbles (~1 nm) |
| Fission yield $Y$ | 0.25 | Xe atoms per fission |
| Fission rates | $1.34$–$6.03\times10^{21}$ fission/(m³·s) | |
| Resolution critical radius | 0.5 nm | |
| Resolution fraction $\delta$ | 0.2 | |

## Defect Properties

| Property | Value | Source |
|----------|-------|--------|
| Xe substitution formation energy | 5.549 eV | DFT |
| U vacancy formation energy | 1.08–2.6 eV | DFT/MD |
| U interstitial formation energy | 0.3–1.5 eV | |
| U interstitial migration barrier | ~0.1–0.25 eV | MD |
| U vacancy migration barrier | ~0.5 eV | MD |
| Stress-free strain: Xe | $\varepsilon_{Xe}^* = 0.05$ | |
| Stress-free strain: Vacancy | $\varepsilon_{\text{Vac}}^* = -0.005$ | |

---

## Key Findings

### 1. Primary Mechanism Identified
- **Fast 1-D SIA migration along ⟨110⟩** is the dominant mechanism
- Elastic interaction alone does NOT cause [[wiki/entities/GasBubbleSuperlattice|gas bubble alignment]]
- Critical diffusivity ratio: $D^* = D_{\text{Int}}/D_{Xe} \geq 10^4$ for short-range ordering; $\geq 10^5$ for long-range ordering
- FCC superlattice in BCC matrix: ⟨110⟩ alignment in 2D extends to FCC in 3D

### 2. Nucleation-and-Growth of Superlattice
- Ordering nucleates in small regions, grows, and merges
- Dislocations observed at domain boundaries (consistent with [[wiki/summaries/2015_Miller_TEMGasBubbleSuperlatticeU7Mo|Miller 2015 TEM]])
- Gas bubbles in ordered regions are more stable than in disordered regions

### 3. Effect of Fission Rate
- Higher fission rate → smaller superlattice constant (9.5 nm → 8.32 nm)
- Higher fission rate → higher bubble density
- Formation controlled by 1-D SIA migration, not fission rate directly

### 4. Effect of Applied Stress
- Compressive stress: reduces bubble size and superlattice constant, **accelerates** formation
- Tensile stress: increases bubble size and lattice constant, **delays** formation

### 5. Effect of Saturated Xe Concentration
- Critical $c_{Xe}^{\text{sat}} > 0.078$ required for superlattice formation
- Implies minimum grain size needed (smaller grains → insufficient Xe accumulation)

### 6. No Coarsening in Disordered Regions
- Radiation-induced resolution + SIA-bubble reactions prevent coarsening
- Narrow size distribution maintained without ordering
- Superlattice regions: bubbles are **larger and more stable**

---

## Relationships to Other Work

| Study | Relationship |
|-------|-------------|
| wiki/summaries/2015_Miller_TEMGasBubbleSuperlatticeU7Mo|Miller et al. (2015)]] | TEM observations used as experimental validation; superlattice collapse at ~$4.5\times10^{21}$ fiss/cm³ |
| wiki/summaries/2013_Kim_RecrystallizationFGBSwellingUMo|Kim & Hofman (2013)]] | Recrystallization & swelling model — superlattice collapse drives FGB swelling increase |
| Hu & Henager (2009) | Earlier wiki/entities/PhaseFieldModeling|phase-field]] model for void lattice formation; basis for first-passage MC |
| Heinisch & Singh (2003) | Kinetic MC showing 1-D SIA migration important for void lattices |
| Gan et al. (2010, 2012) | TEM observations of FCC gas bubble superlattice in UMo |
| Beeler et al. (2010–2013) | DFT calculations of defect properties in bcc U |
| Smirnova et al. (2012–2015) | MD simulations of U self-diffusion and cascade damage in UMo |
| wiki/summaries/2011_Millett_PhaseFieldGasBubbleKinetics|Millett et al. (2011)]] | Earlier wiki/entities/PhaseFieldModeling|phase-field]] model for gas bubble kinetics in nuclear fuels |
| MARMOT/BISON | Target implementation platform for large-scale 3D simulations |

---

## Broader Significance

- First [[wiki/entities/PhaseFieldModeling|phase-field model]] for gas bubble evolution in irradiated U metallic fuels
- Resolves long-standing question: elastic interaction vs. 1-D migration as superlattice cause → **1-D SIA migration wins**
- Connects atomistic (DFT/MD) results to mesoscale [[wiki/entities/PhaseFieldModeling|phase-field]] modeling
- Framework enables studying grain size effects on swelling kinetics through $c_{Xe}^{\text{sat}}$ concept

---

## See Also

- [[wiki/summaries/2016_Hu_GasBubbleSuperlatticeFormationPF/PhysicalMechanismsAndModel|Physical Mechanisms & Model Equations]]
- [[wiki/entities/GasBubbleSuperlattice|GasBubbleSuperlattice]]
- [[wiki/entities/PhaseFieldModeling|PhaseFieldModeling]]
- [[wiki/summaries/2018_Liang_3DPhaseFieldIntragranularBubbleUMo|Liang 2018 — 3D phase-field intragranular bubble model in UMo]]
