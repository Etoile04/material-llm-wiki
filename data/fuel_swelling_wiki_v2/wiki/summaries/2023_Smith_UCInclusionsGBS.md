# The Role of UC Inclusions in the Development of Fission Gas Bubble Superlattice in U-10Mo Fuels (2023, Smith, Bawane, Salvato et al.)

## Metadata
- **Journal**: Journal of Nuclear Materials, 578, 154358 (2023) [Note: PDF text shows 154358; DOI refers to 154474]
- **DOI**: 10.1016/j.jnucmat.2023.154474
- **Authors**: Charlyne Smith, Kaustubh Bawane, Daniele Salvato, Mukesh Bachhav, Dennis Keiser, Brandon Miller, Jian Gan, Jan-Fong Jue, Dong Choe, Paul Gilbreath, William Hanson
- **Material System**: U-10Mo (monolithic)
- **Method**: Experimental (TEM, STEM/EDS, EELS, SAD)
- **Key Topic**: Gas bubble superlattice (GBS), UC inclusions, fission gas bubble ordering

## Physical Mechanisms

1. **Gas bubble superlattice (GBS)**: Self-organization of fission gas bubbles into ordered arrays in irradiated U-10Mo fuel. Driven by collective interaction between system components far from equilibrium.
2. **GBS self-organization initiates at grain boundaries (GB)**: Ordered bubbles first appear at GB, then extend toward grain interior. The rate of extension depends on GB sink strength.
3. **Bubble size categories**:
   - (1) Disordered intragranular bubbles
   - (2) Ordered bubbles at grain boundaries (critical size for ordering ~3 nm)
   - (3) Ordered bubble-adjacent-to-pores (BAPs) (critical size ~4.5 nm, saturation size)
4. **Dislocation loop punching**: When bubble gas pressure exceeds threshold, bubbles grow by pushing out interstitial dislocation loops. Required bubble pressure is independent of bubble size for bubbles > 2 nm diameter.
5. **Vacancy diffusion**: Primary mechanism for bubble growth on small scale. At high gas pressure, additional mechanisms (dislocation loop punching) activate.
6. **Bubble-denuded zones**: Regions near GBs absent of bubbles, due to vacancy diffusion to GB reducing vacancy supersaturation below nucleation threshold.

## Key Equations & Parameters

### Bubble Pressure and Surface Tension Equilibrium (reconstructed)

For a gas bubble in equilibrium with the surrounding matrix:

$$P_{gas} = P_{ext} + \frac{2\gamma}{r}$$

where $P_{gas}$ is the internal gas pressure, $P_{ext}$ is the external hydrostatic pressure, $\gamma$ is the surface energy, and $r$ is the bubble radius. For U-10Mo, $\gamma \approx 1.0$–$1.5$ J/m².

### Dislocation Loop Punching Criterion (reconstructed)

When bubble gas pressure exceeds the threshold for dislocation loop emission:

$$P_{gas} \geq \frac{2\gamma}{r} + \frac{Gb}{r}$$

where $G$ is the shear modulus of U-10Mo (~40 GPa) and $b$ is the Burgers vector (~0.28 nm). This mechanism activates for bubbles >2 nm diameter and drives growth beyond the vacancy-diffusion-limited regime.

### Vacancy Supersaturation and Bubble Growth Rate (reconstructed)

$$\frac{dr}{dt} = \frac{D_v \Omega}{r} \left( S_v - \frac{2\gamma \Omega}{r k_B T} \right)$$

where $D_v$ is the vacancy diffusivity, $\Omega$ is the atomic volume, $S_v = (c_v - c_v^{eq})/c_v^{eq}$ is the vacancy supersaturation ratio, and the second term is the Gibbs-Thomson capillary correction. At GBs, vacancy supersaturation is enhanced, enabling bubbles to reach the critical ordering size of ~3 nm.

### Gibbs-Thomson Effect at Bubble Surface (reconstructed)

Equilibrium vacancy concentration at bubble surface:

$$c_v^{eq}(r) = c_v^{eq}(\infty) \exp\left(\frac{2\gamma \Omega}{r k_B T}\right)$$

Small bubbles ($r < 3$ nm) have elevated equilibrium vacancy concentration, reducing net vacancy absorption and explaining why disordered intragranular bubbles remain small.

### Bubble-Denuded Zone Width (reconstructed)

Near a grain boundary acting as a vacancy sink:

$$L_d \approx \sqrt{D_v t}$$

where $L_d$ is the denuded zone width and $t$ is the irradiation time. Vacancy diffusion to GBs depletes the local vacancy supersaturation below the nucleation threshold, preventing bubble formation in the denuded zone.

### Key Parameters
- **GBS lattice parameter**: ~11 nm for both fission densities (1.15 and 1.30 × 10²¹ fissions/cm³)
- **Critical bubble size for ordering**: ~3 nm (at GB)
- **Bubble saturation size (BAPs)**: ~4.5 nm
- **Xe neutron absorption cross-section**: 2.7 × 10⁶ ± 0.1 barns
- **Fission densities studied**: 1.15 × 10²¹ and 1.30 × 10²¹ fissions/cm³

### Chemical Composition of GBS
- **Primary gas**: Xe (Xe:Kr ratio ~9:1)
- **Additional fission products in GBS**: Cs, Ba, La, Ce
- **Spatial relationship**: Xe signal appears smaller than Cs signal at same location → possible core-shell arrangement (Xe coated by Cs)

## Experimental Data

| Parameter | Value (1.15 × 10²¹ f/cm³) | Value (1.30 × 10²¹ f/cm³) |
|-----------|---------------------------|---------------------------|
| GBS lattice parameter | ~11 nm | ~11 nm |
| Bubble ordering at GB | Early-stage preferential ordering | More clearly resolved SAD satellite spots |
| SAD satellite spots | Not as clearly resolved | Clear presence → higher ordering |
| Dislocation networks | Present (BF and HAADF) | Present (BF and HAADF) |
| Fission products detected | Xe, Cs, Ba, La, Ce | Xe, Cs, Ba, La, Ce |

### Key Observations
- **TEM/STEM imaging**: BF and HAADF micrographs show intragranular dislocation networks
- **STEM/EDS mapping**: Strongest signals from Xe, Ba, and Cs
- **EELS**: Confirms Xe inside GBS bubbles; also detects Cs, Ba, La, Ce inside GBS
- **Bubble size distribution**: Overlap between disordered intragranular and ordered GB bubbles at ~3 nm; transition from GB to BAPs at ~4.5 nm
- **UC inclusions**: Present in microstructure; interaction with GBS formation discussed in context of heterogeneous nucleation

## Model Description

This is primarily an **experimental characterization study**. No mechanistic model is developed, but the observations provide critical data for validating models:

1. **GBS formation sequence**: Disordered intragranular → ordered at GB → ordered BAPs
2. **Self-organization theory**: Collective interaction between bubbles drives system far from equilibrium
3. **Void superlattice vs. GBS**: Similar drivers for self-organization, but bubble mechanics are more complicated due to additional interactions (dislocation loop punching, gas interstitial effects)
4. **GB characteristics influence**: Coincident site lattice (CSL) boundaries may show different bubble nucleation behavior than random high-angle GBs

## Key Findings

1. **Three bubble size categories** identified: disordered intragranular (~<3 nm), ordered GB (~3–4.5 nm), and ordered BAPs (~>4.5 nm).
2. **GBS self-organization begins at grain boundaries** where critical bubble size for ordering is ~3 nm.
3. **GBS lattice parameter ~11 nm** at both fission densities studied, suggesting bubble saturation size is not dependent on fission density.
4. **Higher fission density** (1.30 × 10²¹) shows higher degree of ordering (clearer SAD satellite spots).
5. **GBS is not exclusively Xe-filled**: Contains Cs, Ba, La, Ce fission products; Cs may coat Xe in core-shell arrangement.
6. **Dislocation networks** present in microstructure may contribute to bubble growth via dislocation loop punching.
7. **No clear bubble-denuded zones** observed in monolithic U-10Mo (unlike U-7Mo dispersion fuel).
8. **Ordered bubble spread from GB** has directional preference toward large dislocation lines and nodes.
9. **UC inclusions** may serve as heterogeneous nucleation sites or influence GBS development.

## Relevance to JSRT Model

- **Bubble ordering physics**: Understanding GBS self-organization provides insights into bubble interaction mechanisms relevant to swelling models.
- **Critical size thresholds**: The ~3 nm ordering threshold and ~4.5 nm saturation threshold provide validation data for bubble growth models.
- **GB-initiated swelling**: Confirms that bubble growth initiates at boundaries — consistent with Rest's cavitational swelling model where boundary bubbles reach critical size first.
- **Dislocation loop punching**: Relevant for understanding cavity growth beyond simple vacancy diffusion — may need to be incorporated in advanced JSRT implementations.
- **Multi-component gas composition**: GBS contains multiple fission products, not just Xe — may affect equation of state parameters in swelling models.
- **Limited direct relevance**: This study focuses on U-10Mo rather than U-Zr/U-Pu-Zr, and on gas bubble superlattice rather than cavitational void swelling. However, the bubble growth physics and critical size concepts are transferable.

## Relationships

- [[wiki/entities/GasBubbleSuperlattice|GasBubbleSuperlattice]] — UC inclusions as heterogeneous nucleation sites for GBS formation and multi-component gas composition are the new findings
- [[wiki/entities/FuelAlloy|FuelAlloy]] — U-10Mo monolithic fuel microstructure with UC inclusions is the subject material
- [[wiki/entities/FissionGasDiffusion|FissionGasDiffusion]] — Xe, Cs, Ba, La, Ce co-location in GBS may affect effective EOS and gas transport
- [[wiki/summaries/2023_Smith_EarlySelfOrganizationGBS|2023_Smith_EarlySelfOrganizationGBS]] — companion paper from same group on early-stage GBS self-organization
- [[wiki/summaries/2015_Miller_TEMGasBubbleSuperlatticeU7Mo|2015_Miller_TEMGasBubbleSuperlatticeU7Mo]] — previous TEM study of GBS in U-7Mo at higher fission densities
- [[wiki/summaries/2016_Hu_GasBubbleSuperlatticeFormationPF|2016_Hu_GasBubbleSuperlatticeFormationPF]] — phase-field model for GBS formation mechanism is complementary
