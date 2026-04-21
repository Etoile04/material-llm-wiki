# Hu 2016 — Physical Mechanisms and Phase-Field Model

**Source:** [[wiki/summaries/2016_Hu_GasBubbleSuperlatticeFormationPF|Hu 2016 Index]]

---

## Primary Formation Mechanism

The dominant mechanism for [[wiki/entities/GasBubbleSuperlattice|gas bubble superlattice]] formation in bcc UMo is **fast 1-D migration of self-interstitial atoms (SIAs) along ⟨110⟩ directions**.

**Key insight:** Elastic interaction among gas bubbles alone does **not** cause alignment. The 1-D SIA migration is the essential driver — demonstrated by simulations with $D^* = D_{\text{Int}}/D_{Xe} = 10$ (no superlattice) vs. $D^* \geq 10^4$ (ordering appears).

### Mechanism Step-by-Step

1. Fission events generate vacancies, interstitials, and Xe gas atoms with heterogeneous spatial distributions (from MD cascade simulations)
2. Vacancy clusters at cascade centers serve as **heterogeneous nucleation sites** for gas bubbles
3. SIAs migrate 1-D along ⟨110⟩ dumbbell directions (activation barrier ~0.1–0.25 eV — very low)
4. **Non-aligned bubbles shrink preferentially** due to enhanced SIA absorption along crystallographic directions
5. Aligned bubbles survive → spatial ordering emerges
6. Ordered domains nucleate, grow, and merge; dislocations may form at domain boundaries (consistent with TEM)

### DFT Results on Interstitial Configurations

- U-U [110] dumbbell has the **lowest formation energy** (~0.204 eV) in U-10wt%Mo
- 13 of 30 initial configurations relax to [110] dumbbells
- Some [100] and [111] dumbbells spontaneously rotate to [110] (barrierless)

---

## Six Physical Processes in the Model

1. **Heterogeneous generation** of gas atoms, vacancies, and interstitials (MD cascade inputs)
2. **1-D migration of SIAs** along ⟨110⟩ directions (first-passage Monte Carlo method)
3. **Irradiation-induced dissolution** (resolution) of gas atoms from bubbles
4. **Recombination** between vacancies and interstitials
5. **Elastic interaction** among gas bubbles and defects
6. **Heterogeneous nucleation** of gas bubbles at cascade centers

---

## Key Equations

### Total Free Energy (Eq. 1)
$$F(\mathbf{h}, \mathbf{c}) = \int_V \left[f_s(\mathbf{h}) + f_b(\mathbf{h}, \mathbf{c}) + f_{\text{elas}}(\mathbf{h}, \mathbf{c})\right] dV$$

### Chemical Free Energy — Matrix Phase (Eq. 10)
$$f_a(\mathbf{c}) = E_v^f c_2^2 + E_g^f c_3^2 + k_B T\left[c_2\ln c_2 + c_3\ln c_3 + (1 - c_2 - c_3)\ln(1 - c_2 - c_3)\right]$$

Ideal solution with vacancy and Xe formation energies.

### Chemical Free Energy — Gas Bubble Phase (Eq. 11)
$$f_0(\mathbf{c}) = A_0 c_2^2 + A_1 c_2 + A_2 + B_0 c_3^2 + B_1 c_3 + B_2$$

### Xe Equation of State for Gas Bubble (Eq. 12)
$$\left(\frac{2\gamma}{R} + p\right)\left(\frac{4\pi R^3}{3} - \delta_s b_v N_R\right) = N_R k_B T$$

### Interstitial 1-D Migration Probability (Eq. 5)
$$\frac{\partial p(\mathbf{r}, t)}{\partial t} = D_{\text{SIA}} \frac{\partial^2}{\partial r_k^2} p(\mathbf{r}, t)$$

### Cahn-Hilliard / Allen-Cahn Evolution (Eqs. 9a–b)
$$\frac{\partial c_i}{\partial t} = \nabla \cdot \sum_j M_{ij} \nabla \frac{\delta F}{\delta c_j} + \dot{g}_i - \bar{g}_i + \xi_i$$

$$\frac{\partial h_r}{\partial t} = -L_r \frac{\delta F}{\delta h_r} + \xi_r$$

### Elastic Energy (Eq. 13)
$$f_{\text{elas}} = \frac{1}{2} l_{ijkl}(\varepsilon_{ij} - \varepsilon_{ij}^*)(\varepsilon_{kl} - \varepsilon_{kl}^*)$$

### Stress-Free Strain — Vegard's Law (Eq. 14)
$$\varepsilon_{ij}^* = \sum_{k=1}^3 \varepsilon_k^* (c_k - c_k^{\text{eq}}) \delta_{ij}$$

### Xe Diffusivity (Eq. 16)
$$D_{Xe} = 2.242 \times 10^{-11} \exp(-27000/RT) \quad [\text{m}^2/\text{s}]$$

---

## See Also

- [[wiki/summaries/2016_Hu_GasBubbleSuperlatticeFormationPF/ParametersAndFindings|Parameters, Findings & Relationships]]
- [[wiki/entities/GasBubbleSuperlattice|GasBubbleSuperlattice]]
- [[wiki/entities/PhaseFieldModeling|PhaseFieldModeling]]
- [[wiki/summaries/2015_Miller_TEMGasBubbleSuperlatticeU7Mo|Miller 2015 — TEM observations used as experimental basis]]
