# Swelling Behavior Detection of Irradiated U-10Zr Alloy Fuel Using Indirect Neutron Radiography

## Metadata

| Field | Value |
|-------|-------|
| **Title** | Swelling behavior detection of irradiated U-10Zr alloy fuel using indirect neutron radiography |
| **Authors** | Yong Sun, He-yong Huo, Yang Wu, Jiangbo Li, Wei Zhou, Hai-bing Guo, Hang Li, Chao Cao, Wei Yin, Sheng Wang, Bin Liu, Qi-jie Feng, Bin Tang |
| **Year** | 2016 |
| **Journal** | Nuclear Instruments and Methods in Physics Research A, 837, 23–27 |
| **DOI** | 10.1016/j.nima.2016.08.059 |
| **Affiliation** | Institute of Nuclear Physics and Chemistry, CAEP; Key Laboratory of Neutron Physics, CAEP, Mianyang, China |
| **Keywords** | U-10Zr alloy, Indirect neutron radiography, Swelling behaviors |

---

## Physical Mechanisms

### Fuel Swelling in U-10Zr Alloy
- U-10Zr alloy (10 wt% Zr) is a candidate metallic fuel for fusion-fission hybrid energy system subcritical blankets.
- Under irradiation, fuel swells due to fission gas bubble formation and accumulation.
- Swelling manifests as both **radial** (diametral) and **axial** (longitudinal) dimensional changes.
- Radial and axial swelling behaviors are **anisotropic**: radial swelling rate exceeds axial swelling rate at higher burnup.
- Cladding constraint (Zr-4 shell in Type B samples) mechanically suppresses swelling.

### Indirect Neutron Radiography (INR)
- **Two-step method**: (1) expose neutron converter foil (In/Dy) in neutron beam with sample; (2) contact converter with imaging plate/film offline for second exposure.
- Suitable for **highly radioactive** samples where direct radiography is impractical.
- High-Z materials (U) strongly absorb neutrons; low-Z materials (Al, Al powder) are nearly transparent to cold neutrons.

---

## Key Equations

### Neutron Penetrability

$$P = \frac{I}{I_0} = \exp(-\Sigma \cdot d_{max})$$

Where:
- $I_0$ = incident neutron flux
- $I$ = transmitted neutron flux
- $\Sigma$ = total macroscopic cross section (cm⁻¹)
- $d_{max}$ = maximum sample thickness (cm)

**Calculated for U-10Zr fuel pin**: $\Sigma = 4.1$ cm⁻¹, $d_{max} = 0.5$ cm → $P = \exp(-4.093 \times 0.5) = 0.129$ (12.9% transmission)

### Swelling Rate

$$\text{Swelling Rate (\%)} = \frac{\Delta L}{L_0} \times 100$$

Where $\Delta L$ is the dimensional change and $L_0$ is the original dimension.

---

## Parameters

### Sample Parameters

| Parameter | Type A | Type B |
|-----------|--------|--------|
| Fuel pin dimensions | φ5 × 15 mm | φ5 × 15 mm |
| Cladding thickness | — | 1.0 mm |
| Sample shell | 1.0 mm (Zr-4) | 3.0 mm (Al) |
| Porous Al powder (radial) | 1.5 mm | 1.5 mm |
| Sample dimensions | φ10 × 37 mm | φ16 × 63 mm |
| Fuel composition | U-10 wt%Zr | U-10 wt%Zr |
| Nominal fuel density | 16.03 g/cm³ | 16.03 g/cm³ |
| Uranium loading per pin | 4.25 g | 4.25 g |
| Destination burnup | 0.1, 0.3, 0.5, 0.7 at% | 0.1, 0.3, 0.5, 0.7 at% |

### Neutron Beam Parameters

| Parameter | Value |
|-----------|-------|
| Facility | CMRR (China Mianyang Research Reactor) |
| Beam line | C1 cold neutron tube |
| Most probable neutron wavelength | 2.7 Å |
| L/D ratio | ~325 |
| Sample-converter distance | 5 mm |
| Reactor power during experiment | 15 MW |

### INR Imaging Parameters

| Parameter | Value |
|-----------|-------|
| Converter | 100 µm Indium metal foil, 100 × 100 mm |
| First exposure (neutron) | 1 hour |
| Second exposure (converter → film) | 4 hours |
| Film | Kodak AA400 |
| Digitization | Array-2905 film scanner |
| Resolution | 50 µm |

---

## Experimental Data

### Swelling Rates vs. Burnup

**Type A samples** (no cladding on fuel pin, Zr-4 shell):

| Burnup (at%) | Radial Swelling Rate (%) | Axial Swelling Rate (%) |
|:---:|:---:|:---:|
| 0.1 | ~0 | ~0 |
| 0.3 | ~1–2 | ~0–0.5 |
| 0.5 | ~4–5 | ~1 |
| 0.7 | **>10** | **~2** |

**Type B samples** (1.0 mm cladding, Al shell):

| Burnup (at%) | Max Swelling Rate (%) |
|:---:|:---:|
| 0.1 | ~0 |
| 0.3 | ~0.5 |
| 0.5 | ~1.0 |
| 0.7 | **~1.75** |

### Key Observations
- **Sample No. 5** (Type A, 0.5% burnup): Fuel pin edge spread; gray value analysis suggests fuel broke through and expanded into Al powder shell.
- **Sample No. 11** (Type A, 0.7% burnup): Anatomized and verified by metallurgical microscopy — confirmed fuel pin edge spreading consistent with INR results.
- Swelling is detectable by INR when burnup ≥ 0.5% for Type A.

---

## Key Findings

1. **INR is effective for irradiated U-10Zr fuel**: Indirect neutron radiography successfully detected swelling in highly radioactive U-10Zr fuel pins with residual dose too high for direct methods.

2. **Swelling increases with burnup**: Both radial and axial swelling rates increase with increasing burnup (0.1–0.7 at%).

3. **Anisotropic swelling**: Radial swelling rate significantly exceeds axial swelling rate, especially at higher burnup. At 0.7 at% burnup, Type A showed >10% radial vs ~2% axial swelling.

4. **Cladding suppresses swelling**: Type B samples (with 1.0 mm cladding) showed dramatically lower swelling (max 1.75%) compared to Type A (unc lad fuel pin, >10%) at same burnup, demonstrating mechanical constraint effect.

5. **Fuel-cladding interaction**: At 0.5% burnup (Type A), evidence of fuel pin rupture and material expansion into surrounding Al powder shell.

6. **INR resolution**: 50 µm spatial resolution achieved, sufficient to quantify swelling dimensions.

7. **Validation**: Metallurgical microscopy of cross-sectioned sample No. 11 confirmed INR swelling observations.

---

## Relationships to Other Work

- **U-Zr alloy fuel development**: Builds on work by Jovanovic (1970) on uranium alloy phase growth, Meyer et al. (1999) on advanced fuel development, Eckelmeyer (1990) on beta-phase retention in U alloys.
- **Neutron radiography of nuclear fuel**: Extends techniques from Craft et al. (2015, INL) on neutron radiography of irradiated fuel, Lehmann et al. (2003) on non-destructive fuel analysis, and Wei et al. (2015) on indirect neutron radiography at CARR.
- **Fusion-fission hybrid energy systems**: Connected to Shi & Peng (2010) blanket neutronics design for hybrid reactors.
- **Complementary to metallographic methods**: INR provides non-destructive alternative to destructive cross-sectioning traditionally used for swelling assessment.
- **Future work**: Authors propose using imaging plates instead of film for shorter exposure, lower activation, and linear response.

## Relationships

- [[wiki/entities/FuelAlloy|FuelAlloy]] — U-10Zr metallic alloy fuel swelling behavior under irradiation is characterized
- [[wiki/concepts/SwellingMechanisms|SwellingMechanisms]] — anisotropic radial vs. axial swelling and cladding constraint effects are measured non-destructively
- [[wiki/summaries/1990_Hofman_SwellingBehaviorUPuZr|1990_Hofman_SwellingBehaviorUPuZr]] — Hofman's work on anisotropic swelling in U-Pu-Zr fuel provides context for U-Zr behavior
- [[wiki/summaries/2020_Williams_PIRT_SwellingUZr|2020_Williams_PIRT_SwellingUZr]] — comprehensive PIRT on U-Zr swelling phenomena relevant to the same fuel system
- [[wiki/summaries/2020_Aagesen_BisonUPuZrSwellingLowerLengthScale|2020_Aagesen_BisonUPuZrSwellingLowerLengthScale]] — BISON modeling of U-Pu-Zr swelling provides modeling context
