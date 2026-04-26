# Atom Probe Tomography of Segregation at Grain Boundaries and Gas Bubbles in Neutron Irradiated U-10 wt% Mo Fuel

## Metadata

- **Title:** Atom probe tomography of segregation at grain boundaries and gas bubbles in neutron irradiated U-10 wt% Mo fuel
- **Authors:** Maalavan Arivu, Andrew Hoffman, Mukesh Bachhav, Assel Aitkaliyeva, Yaqiao Wu, Brandon Miller, Dennis Keiser, Jian Gan, Haiming Wen
- **Year:** 2024
- **Journal:** Materials Letters, 365, 136414
- **DOI:** 10.1016/j.matlet.2024.136414
- **Affiliations:** Missouri S&T; GE Research; INL; University of Florida; Boise State University; CAES

## Physical Mechanisms

### Fission Product Segregation — Size-Dependent Behavior
Three distinct segregation behaviors observed:

1. **Sub-10 nm bubbles:** Only Xe enriched; no significant solid fission product (SFP) segregation
   - Xe partitioning coefficient: ~3 (bubble/matrix)
   - U concentration at core: ~50 at.%
   - Mo: no enrichment/depletion

2. **>10 nm bubbles:** Xe + all major fission products enriched
   - Xe partitioning coefficient: ~10 (bubble/matrix)
   - U concentration at core: <10 at.%
   - Mo: depleted toward center, enriched at interface
   - Te: highest concentration (~21 at.%) at 2–4 nm from interface
   - Nd: highest at interface, decreasing toward center

3. **Grain boundaries:** All fission products enriched EXCEPT I and Rb
   - U depleted: ~74 at.% (interior) → ~55 at.% (GB)
   - Mo: approximately unchanged across GB

### Denuded Zone Formation
- **Adjacent to large bubbles (>10 nm):** Free of sub-10 nm Xe bubbles
- **Adjacent to grain boundaries:** Similar denuded zone observed
- **Mechanism:** Point defects accumulate at bubble-matrix interface; interstitial emission mechanism annihilates vacancies several atomic layers away from GB/interface

### Segregation Kinetics
- Irradiation-dominated (vs thermally-driven) segregation behavior
- High point defect concentration from irradiation enhances diffusion
- At high fission densities, matrix becomes amorphous enabling rapid SFP diffusion
- Bubble formation precedes SFP accumulation; SFPs eventually influx into bubbles

## Key Equations

### Gibbs-Thomson Capillary Effect on Bubble Composition (reconstructed)

Equilibrium vacancy concentration at curved bubble-matrix interface:

$$c_v^{eq}(r) = c_v^{eq}(\infty) \exp\left(\frac{2\gamma \Omega}{r k_B T}\right)$$

where $\gamma$ is the surface energy, $\Omega$ is the atomic volume, $r$ is the bubble radius, and $T$ is temperature. This explains why sub-10 nm bubbles have different Xe partitioning (~3×) vs. larger bubbles (~10×) — smaller bubbles require higher gas pressure for equilibrium.

### Gas Pressure in Equilibrium Bubbles (reconstructed)

$$P = P_{ext} + \frac{2\gamma}{r}$$

For U-10Mo at irradiation temperature (~370 K centerline), smaller bubbles sustain higher internal pressures. This pressure difference drives the size-dependent segregation behavior: small bubbles retain higher U content (~50 at.%) while large bubbles expel U (<10 at.%).

### Vacancy Supersaturation-Driven Bubble Growth (reconstructed)

$$\frac{dr}{dt} = \frac{D_v \Omega}{r}\left(S_v - \frac{2\gamma \Omega}{r k_B T}\right)$$

where $D_v$ is the vacancy diffusivity, $S_v = (c_v - c_v^{eq})/c_v^{eq}$ is the vacancy supersaturation ratio. Irradiation-enhanced vacancy supersaturation drives bubble growth preferentially at sinks (GBs, large bubble interfaces).

### Denuded Zone Width — Interstitial Emission Mechanism (reconstructed)

Point defect accumulation at bubble-matrix interface annihilates vacancies via interstitial emission (Beyerlein et al., 2013):

$$L_d \approx \sqrt{\frac{D_v}{K_{iv} c_i}}$$

where $K_{iv}$ is the vacancy-interstitial recombination coefficient and $c_i$ is the interstitial concentration. This mechanism produces vacancy-free zones adjacent to both large bubbles (>10 nm) and grain boundaries.

### Xe Partitioning Coefficient (from experimental data)

$$k_p = \frac{C_{Xe}^{bubble}}{C_{Xe}^{matrix}}$$

| Bubble Size | $k_p$ | Core U (at.%) |
|-------------|-------|---------------|
| <10 nm | ~3 | ~50 |
| >10 nm | ~10 | <10 |

### Fission Gas Generation Rate (reconstructed)

$$\dot{Y}_{Xe} = y_{Xe} \cdot \dot{F}$$

where $y_{Xe}$ is the Xe fission yield (~0.25 atoms/fission for U-235) and $\dot{F}$ is the fission rate density (1.55 × 10¹⁴ fissions/cm³·s in this experiment).

## Parameters

### Irradiation Conditions
| Parameter | Value |
|-----------|-------|
| Fuel | U-10 wt% Mo (γ-BCC) |
| Reactor | ATR (INL) |
| Fission density | 2.68 × 10²¹ fissions/cm³ |
| Fission rate | 1.55 × 10¹⁴ fissions/cm³·s |
| End-of-life centerline temperature | 94.2°C |

### APT Parameters
| Parameter | Value |
|-----------|-------|
| Instrument | CAMECA LEAP 4000X HR |
| Laser mode | 20 K, 20–50 pJ, 200 kHz, 0.5–1% detection |
| Voltage mode | 45 K, 20% pulse fraction, 200 kHz |
| Analysis software | IVAS 3.8.4 |
| Xe isoconcentration surfaces | 6.7 at.% (large bubble), 5.5 at.% (GB), 2.4 at.% (small bubbles) |

### Compositional Data
| Feature | U (at.%) | Mo | Xe partitioning |
|---------|----------|-----|-----------------|
| Matrix | ~75 | — | ~3.5 |
| Small bubble (<10 nm) core | ~50 | unchanged | ~3× |
| Large bubble (>10 nm) core | <10 | depleted | ~10× |
| Grain boundary | ~55 | unchanged | enriched |

## Experimental Data

### Key Findings
1. **Size-dependent segregation:** First successful APT characterization of sub-10 nm bubbles in irradiated U-Mo — they behave differently from larger bubbles
2. **Denuded zones** identified around both >10 nm bubbles and grain boundaries — both act as effective sinks for irradiation-induced defects
3. **Irradiation vs thermal segregation:** GB segregation dominated by irradiation kinetics, not thermal equilibrium (contrasts with Devaraj et al. 2018 annealing study)
4. **Xe partitioning:** Strongly size-dependent (~3 for small, ~10 for large bubbles)
5. **Te peak position:** Maximum at 2–4 nm from large bubble interface (not at center) — suggests surface/interface segregation behavior

### Methodological Notes
- APT laser mode may cause sample heating — verified by voltage mode comparison
- Trajectory aberrations possible due to different evaporation fields of Xe bubbles vs matrix
- APT analytical sensitivity: ~1 appm (vs 10% relative uncertainty for STEM-EDS)

## Relationships to Other Work

- **Gan et al. (2017):** Previous STEM-EDS work on bubble segregation — APT provides higher sensitivity and quantitative data
- **Gan et al. (2014):** Bubble superlattice collapse and large bubble formation — consistent with observations
- **Miller et al. (2015):** Sub-10 nm bubble characterization unsuccessful previously — current study succeeds
- **Devaraj et al. (2018):** GB segregation in thermally annealed U-Mo — opposite behavior (U enrichment, Mo depletion) indicates irradiation-dominated kinetics
- **Beyerlein et al. (2013):** Interstitial emission mechanism for denuded zone formation — cited as theoretical basis

## Relationships

- [[wiki/entities/FuelAlloy|FuelAlloy]] — U-10 wt% Mo γ-BCC alloy fuel at 2.68×10²¹ f/cm³ is characterized by APT
- [[wiki/entities/FissionGasDiffusion|FissionGasDiffusion]] — size-dependent Xe partitioning and fission product segregation in gas bubbles are the key findings
- [[wiki/entities/GasBubbleSuperlattice|GasBubbleSuperlattice]] — sub-10 nm bubbles (GBS scale) and larger >10 nm bubbles show distinct chemistry
- [[wiki/concepts/SwellingMechanisms|SwellingMechanisms]] — irradiation-dominated segregation kinetics and denuded zone formation inform bubble growth models
- [[wiki/summaries/2015_Miller_TEMGasBubbleSuperlatticeU7Mo|2015_Miller_TEMGasBubbleSuperlatticeU7Mo]] — Miller (2015) first characterized GBS; this APT study provides chemical composition data
- [[wiki/summaries/2023_Smith_EarlySelfOrganizationGBS|2023_Smith_EarlySelfOrganizationGBS]] — companion experimental work on early GBS self-organization at similar fission densities

## Related Work
- [[wiki/summaries/2023_Smith_UCInclusionsGBS|2023_Smith_UCInclusionsGBS]] — 同期Smith的EELS研究也发现GBS中含多元素，与本文APT结果互补
- [[wiki/summaries/2015_Miller_TEMGasBubbleSuperlatticeU7Mo|2015_Miller_TEMGasBubbleSuperlatticeU7Mo]] — 首次GBS TEM表征，本文APT克服了其纳米气泡成分表征的技术瓶颈
- [[wiki/summaries/2023_Zhang_Review_VoidBubbleSuperlattice_SelfOrganization|2023_Zhang_Review_VoidBubbleSuperlattice_SelfOrganization]] — GBS综述，本文的尺寸依赖偏聚行为为其提供新的实验数据
- [[wiki/summaries/2025_Hanson_StablePredictableSwellingU10Mo|2025_Hanson_StablePredictableSwellingU10Mo]] — MP-1肿胀验证，本文的气泡化学成分数据可帮助理解肿胀行为的微观机理
- [[wiki/concepts/SwellingMechanisms|SwellingMechanisms]] — 尺寸依赖的Xe偏聚(<10 nm: 3×, >10 nm: 10×)对气泡生长模型有重要约束意义
