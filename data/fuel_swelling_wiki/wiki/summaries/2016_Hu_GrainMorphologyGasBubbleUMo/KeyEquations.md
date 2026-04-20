# Key Equations – 2016 Hu: Grain Morphology & Gas Bubble Swelling (3D Booth Model)

## Generalized Fission Gas Diffusion (3D Booth Model)

$$\frac{\partial c(\mathbf{r},t)}{\partial t} = \nabla \cdot D_g \nabla \mu(\mathbf{r},t) + Y\dot{f}(\mathbf{r},t) - 16\pi f_n D_g r_g c(\mathbf{r},t)^2 - 4\pi r_b(\mathbf{r},t) D_g c(\mathbf{r},t) c_b(\mathbf{r},t) + b n_b(\mathbf{r},t) c_b(\mathbf{r},t)$$

**Variables:**
- $c(\mathbf{r},t)$: concentration of dissolved gas atoms in matrix
- $\mu$: chemical potential of fission gas atoms
- $Y$: gas atom yield per fission (0.25 atoms/fission)
- $\dot{f}(\mathbf{r},t)$: spatially dependent fission rate
- $D_g = D_0 \dot{f}$: athermal diffusion coefficient
- $f_n$: nucleation factor (0.01–0.03)
- $r_b(\mathbf{r},t)$: intra-granular bubble radius
- $c_b(\mathbf{r},t)$: intra-granular bubble number density
- $b = b_0 \dot{f}$: radiation-induced resolution rate

## Intra-granular Bubble Density

$$\frac{\partial c_b(\mathbf{r},t)}{\partial t} = \frac{16\pi f_n D_g r_g c(\mathbf{r},t)^2}{n_b(\mathbf{r},t)} - \frac{b c_b(\mathbf{r},t)}{2}$$

## Gas Content per Bubble

$$\frac{\partial n_b(\mathbf{r},t)}{\partial t} = 4\pi r_b(\mathbf{r},t) D_g c(\mathbf{r},t) - \frac{b n_b(\mathbf{r},t)}{2}$$

## Modified Van der Waals Bubble EOS

$$\left(\frac{2\gamma}{r_b} + \frac{4}{3}\pi r_b^3 - h_s b_v n_b\right)^{-1} \cdot n_b kT = 1$$

Approximate solution for nanometer-scale bubbles:

$$r_b(\mathbf{r},t) \approx \left(\frac{3 h_s b_v n_b(\mathbf{r},t)}{4\pi}\right)^{1/3}$$

## Inter-granular Bubble Density (Wood-Kear)

$$C_b(t) = \left(\frac{8 z a K}{12^{1/3} \pi^2 \chi D_g d}\right)^{1/2}$$

- $\chi$: grain-boundary diffusion enhancement factor (range 15–125 for UMo)
- $a$: lattice constant; $z$: jump sites; $d$: grain boundary width

## Total Fractional Swelling

$$\frac{\Delta V(t)}{V} = \frac{1}{V}\left[\int_V \frac{4}{3}\pi r_b^3(\mathbf{r},t) c_b(\mathbf{r},t) dV + \frac{4}{3}\pi R_b^3(t) C_b(t) S + \int_V \varepsilon_0 c_g(\mathbf{r},t) dV\right]$$

Three contributions: intra-granular bubbles, inter-granular bubbles, dissolved gas atoms.

## See Also

- [[wiki/summaries/2016_Hu_GrainMorphologyGasBubbleUMo|Index: Grain Morphology Booth Model]]
- [[wiki/summaries/2016_Hu_GrainMorphologyGasBubbleUMo/ModelParameters|Model Parameters Table]]
- [[wiki/entities/RateTheory|RateTheory]] — rate-equation context for these ODEs
- [[wiki/summaries/2018_Liang_3DPhaseFieldIntragranularBubbleUMo|Liang 2018 Phase-Field]] — complementary PF formulation with similar EOS
- [[wiki/summaries/2015_Cui_MechanisticGaseousSwellingUMo|Cui 2015 Mechanistic Swelling]] — analytical swelling model comparison
