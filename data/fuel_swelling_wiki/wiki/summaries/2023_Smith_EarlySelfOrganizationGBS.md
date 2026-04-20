# Early Self-Organization of Fission Gas Bubble Superlattice Formation in Neutron-Irradiated Monolithic U-10Mo Fuels (2023, Smith et al.)

## Metadata
- **Journal**: Journal of Nuclear Materials, 578 (2023) 154358
- **DOI**: 10.1016/j.jnucmat.2023.154358
- **Material System**: U-10Mo (monolithic)
- **Method**: Experimental (TEM, STEM/EDS, EELS)
- **Key Topic**: Gas bubble superlattice (GBS) / self-organization / grain boundary effects

## Physical Mechanisms
1. **GBS self-organization**: Highly ordered 3D fcc defect superlattice forms in bcc U-Mo matrix under neutron irradiation
2. **GB-initiated ordering**: Bubble ordering preferentially initiates at grain boundaries, then extends toward grain interior
3. **Critical bubble size for ordering**: ~3 nm — bubbles below this size remain disordered
4. **Dislocation loop punching**: Over-pressurized bubbles may grow by emitting interstitial dislocation loops; threshold pressure independent of bubble size for bubbles >2 nm
5. **Bubble-denuded zones**: Regions near GBs with reduced vacancy supersaturation may lack bubbles (reported in U-7Mo but not clearly observed in U-10Mo monolithic)
6. **Fission product co-location**: Xe, Cs, Ba, La, Ce found in GBS; possible core-shell arrangement of Xe coated by Cs

## Key Equations & Parameters

> Reconstructed from domain knowledge. This is a purely experimental study (TEM); the following equations describe the physical processes observed.

### Gas Bubble Internal Pressure (Equilibrium)

$$P = \frac{2\gamma}{R} + \sigma_h$$

where:
- $R$: bubble radius (~2.6–5.7 nm in this study)
- $\gamma$: surface energy of U-Mo (~1 J/m²)
- $\sigma_h$: hydrostatic stress (compressive, from cladding restraint)

For $R = 3$ nm, $\gamma = 1$ J/m²: $P \approx 667$ MPa (without external stress), consistent with over-pressurized bubbles that can emit dislocation loops.

### Dislocation Loop Punching Threshold

$$P_{\text{punch}} = \frac{\mu b}{R} + \sigma_h$$

where:
- $\mu$: shear modulus of U-Mo
- $b$: Burgers vector ($\frac{a_0\sqrt{3}}{2}$ for bcc, $a_0 \approx 0.315$ nm)

The threshold pressure is approximately independent of bubble size for $R > 2$ nm, explaining why bubbles above ~3 nm can grow by loop punching.

### 1-D SIA Diffusion Theory for GBS Formation

$$\lambda_{\text{GBS}} = \left(\frac{2\Omega\dot{F}}{D_1 C_{\text{SIA}} \xi}\right)^{-1/2}$$

where:
- $\lambda_{\text{GBS}}$: GBS lattice parameter (~11 nm measured)
- $\dot{F}$: fission rate
- $D_1$: 1-D SIA diffusion coefficient
- $C_{\text{SIA}}$: SIA concentration
- $\xi$: sink strength

This is the theoretical basis from Hu et al. (2016) predicting fcc GBS in bcc U-Mo via 1-D SIA migration along $\langle 111 \rangle$ directions.

### Measured Parameters
- **GBS lattice parameter**: ~11 nm (measured at both fission densities)
- **Critical bubble sizes**:
  - Intragranular disordered: mean ~2.6 nm
  - GB semi-ordered: 3.5 nm (1.15×10²¹ f/cm³), 4.3 nm (1.30×10²¹ f/cm³)
  - Bubbles around pores (BAPs): 5.2 nm and 5.7 nm respectively
- **GBS saturation threshold**: 3–4.5 × 10²¹ fissions/cm³
- **GBS formation temperature**: <250°C (for U-Mo research/test reactors)
- **GBS spread from GB**: 30–107 nm (non-uniform, depends on GB sink strength)

## Experimental Data

### Irradiation conditions (MP-1 campaign, ATR reactor)
| Mini-plate | Midplane EOL fission density | Axial center EOL | Temperature |
|---|---|---|---|
| A2C171 (KGT-3629) | 1.13-1.29 × 10²¹ f/cm³ | 1.15 × 10²¹ f/cm³ | <200°C |
| A2C125 (KGT-3706) | 1.28-1.58 × 10²¹ f/cm³ | 1.30 × 10²¹ f/cm³ | <200°C |

### Key observations
- At 1.15 × 10²¹ f/cm³: intragranular bubbles disordered; early GB ordering observed; SAD satellite spots not clearly resolved
- At 1.30 × 10²¹ f/cm³: more advanced GB ordering; SAD satellite spots clearly visible (higher ordering degree)
- Three bubble categories: (1) intragranular disordered, (2) ordered at GB, (3) ordered BAPs
- Fission products in GBS confirmed: Xe, Cs, Ba, La, Ce via STEM/EDS and EELS
- Xe signal spatially smaller than Cs signal in same location → possible Xe coated by Cs

## Model Description
- Purely experimental study using TEM characterization
- **FIB/SEM sample preparation**: TEM lamellae 20×10×0.1 μm from fuel midplane cross-sections
- **Characterization**: BF, HAADF, SAD patterns, STEM/EDS maps, EELS maps
- **EELS quantification**: Custom HyperSpy script with Hartree-Slater GOS parameterized model
- Irradiation performed in ATR; neutronics calculated with MCNP5 + ORIGEN2

## Key Findings
1. **GBS ordering initiates at grain boundaries** at low fission densities (1.15-1.30 × 10²¹ f/cm³), before full GBS formation at ~3 × 10²¹ f/cm³
2. **Critical bubble size for ordering is ~3 nm**: below this, bubbles remain disordered; above, they join the superlattice
3. **GBS spread from GB is non-uniform** (30-107 nm), suggesting dependence on GB type/sink strength
4. **Dislocation networks** observed in grain interiors on the side of GBS directional spread — possible role in bubble growth via loop punching
5. **GBS lattice parameter ~11 nm** at both fission densities (similar)
6. **GBS contains multiple fission products** (Xe, Cs, Ba, La, Ce), not exclusively Xe — first confirmation of non-Xe species in GBS
7. **BAPs (bubbles around pores) are larger** (~5-6 nm) and appear saturated, acting as strong gas sinks

## Relevance to JSRT Model
- **Critical size threshold**: The ~3 nm critical size for GBS ordering could inform bubble size thresholds in JSRT swelling rate calculations
- **GB-initiated bubble evolution**: Demonstrates that GBs serve as preferential nucleation/ordering sites — relevant for JSRT intergranular bubble modeling
- **Bubble size distribution data**: Three distinct bubble populations (disordered, GB-ordered, BAP) with measured sizes provide validation data for multi-size-group models
- **GBS as gas retention mechanism**: The superlattice can delay gas release and swelling — if U-Mo or similar fuels are in JSRT scope, GBS retention must be modeled
- **Low-temperature behavior**: Data at <200°C complements higher-temperature fuel data, relevant for JSRT temperature-dependent parameterization
- **Dislocation-bubble interaction**: Observed correlation between dislocation networks and bubble growth suggests additional transport mechanisms beyond simple diffusion

## Relationships

- [[wiki/entities/GasBubbleSuperlattice|GasBubbleSuperlattice]] — early-stage GBS self-organization at grain boundaries in U-10Mo is directly observed at ~1.15–1.30×10²¹ f/cm³
- [[wiki/entities/FuelAlloy|FuelAlloy]] — U-10Mo monolithic fuel fuel at very low fission density is the subject
- [[wiki/entities/FissionGasDiffusion|FissionGasDiffusion]] — GB-initiated bubble ordering and critical ~3 nm bubble size for GBS ordering are key findings
- [[wiki/summaries/2015_Miller_TEMGasBubbleSuperlatticeU7Mo|2015_Miller_TEMGasBubbleSuperlatticeU7Mo]] — Miller (2015) characterizes GBS saturation and collapse at higher fission densities
- [[wiki/summaries/2023_Smith_UCInclusionsGBS|2023_Smith_UCInclusionsGBS]] — companion paper from same group on UC inclusions in GBS
- [[wiki/summaries/2016_Hu_GasBubbleSuperlatticeFormationPF|2016_Hu_GasBubbleSuperlatticeFormationPF]] — Hu's phase-field model predicts the 1-D SIA mechanism for GBS formation being initiated
