# 📄 PDF Parsing Result

**File:** `/Volumes/openclaw记忆/Zotero_storage/storage/X2H2JBFB/Aagesen et al._2022_Phase-field simulations of fission gas bubble growth and interconnection in U-(Pu)-Zr nuclear fuel.pdf`
**Backend:** `pipeline`
**Pages:** 0 to end
**Formula Recognition:** ❌ Disabled
**Table Recognition:** ✅ Enabled

---

ORIGINAL ARTICLE

Open Access

# Phase-field simulations of fission gas bubble growth and interconnection in U-(Pu)-Zr nuclear fuel

![](images/faecc2c6d63341fd0f33aeb879bcb5046dade832386af95abf7981dc75adff84.jpg)

Larry K. Aagesen1\* , Albert Casagranda2, Christopher Matthews3, Benjamin W. Beeler4   
and Stephen Novascone1

\*Correspondence: Larry.Aagesen@inl.gov 1Computational Mechanics and Materials Department, Idaho National Laboratory, P.O. Box 1625, Idaho Falls 83415, ID, USA Full list of author information is available at the end of the article

## Abstract

The growth and interconnection of fission gas bubbles in the hotter central regions of U-(Pu)-Zr nuclear fuel has been simulated with a phase-field model. The Cahn-Hilliard equation was used to represent the two-phase microstructure, with a single defect species. The volume fraction of the bubble phase and surface area of the bubble-matrix interface were determined during growth and interconnection. Surface area increased rapidly during the initial stages of growth, then slowed and finally decreased as bubble interconnection began and coarsening acted to reduce surface area. The fraction of the bubbles vented to a simulation domain boundary, fV, was quantified as a measure of the microstructure’s interconnectivity and plotted as a function of porosity p. The defect species diffusivity was varied; although changes in diffusivity significantly affected the microstructure, the plots of fV vs. p did not change significantly. The percolation threshold pc was calculated to be approximately 0.26, depending on the assumed diffusivity and using an initial bubble number density based on experimental observations. This is slightly smaller than the percolation threshold for continuum percolation of overlapping 3D spheres. The simulation results were used to parameterize two different engineering-scale swelling models for U-(Pu)-Zr in the nuclear fuel performance code BISON.

Keywords: Phase-field, Fission gas bubble, Uranium, Zirconium

## Introduction

Nuclear fuel based on the U-Zr and U-Pu-Zr systems has attracted renewed interest in recent years for new commercial designs and microreactors. Additionally, the U. S. Department of Energy’s planned fast-spectrum Versatile Test Reactor will use metallic fuel. Although reactors using this type of fuel have not yet been used for commercial energy production in the U. S., the concept of a fast-spectrum reactor fueled with U-(Pu)- Zr was extensively validated during the years of operation of the Experimental Breeder Reactor-II (EBR-II) (Walters 1999). Fuel for such reactor concepts has typically employed compositions of 10 wt. % Zr and Pu composition ranging from 0 to 26 wt. %.

Swelling is a major concern in U-(Pu)-Zr fuels compared with the pellet-form UO2 fuel used in current commerical light-water reactors. Cylindrical metallic fuel elements swell anisotropically with a bias in the radial direction, and can swell by 30% or more in-plane at burnups of ∼2% FIMA (fissions per initial metal atom) (Hofman et al. 1997). Swelling in metallic fuel is a complex phenomenon that strongly impacts fuel performance and lifetime. For example, reduction in thermal conductivity, fission gas release, and loss of fuel cladding integrity can all be linked to fuel swelling.

The local microstructure of U-(Pu)-Zr fuel has a significant impact on the swelling behavior in different regions. In U-10Zr (wt %), below 890 K, the microstructure is composed of the α phase (orthorhomic crystal structure) and the δ phase (ordered UZr2). Above 890 K, the microstructure is a mixture of γ phase (body-centered cubic) and either the α or β (tetragonal) phase. Although the exact transition temperatures and phase composition depend on Pu content, the following general trends have been observed. The presence of the γ phase appears to determine the local morphology of fission gas bubbles and resulting swelling behavior (Hofman et al. 1990). At lower temperatures, where the γ phase is not present, it appears that swelling in the α phase is a result of grain boundary and interphase tearing or cracking, forming irregularly-shaped void space that subsequently collects gaseous and solid fission products with increasing burnup (Angerman and Caskey Jr 1964; Pahl et al. 1990). In the hotter regions where the γ phase is present, the fission gas bubbles are quite large compared to those observed in UO2 fuel, with diameters on the order of tens of microns (Hofman et al. 1990). The morphology of individual bubbles is initially spherical and individual bubbles coalesce with adjacent bubbles as they grow. As these bubbles continue to grow, they eventually form a fully interconnected structure. When this interconnected structure connects to a free surface of the fuel slug, the gas within the bubbles is released from the fuel, and any further fission gas produced that reaches the bubbles will travel out of the fuel through this network rather than causing the existing bubbles to grow further. The porosity values at which this interconnection process begins and ends therefore determine when swelling terminates and when fission gas release begins. These trends were observed for a wide range of Pu content in EBR-II fuel (Hofman et al. 1990).

Due to the high importance of swelling to U-(Pu)-Zr fuel performance, significant effort has been invested in recent years to develop mechanistic models of swelling in the nuclear fuel performance code BISON (Novascone et al. 2019; Matthews and Unal 2019; Casagranda et al. 2020). These efforts have focused on the hotter central region of the fuel, where the microstructure is dominated by the γ phase and large fission gas bubbles. However, these engineering-scale mechanistic models require information on the progress of bubble interconnectivity as inputs, and these details are not well known. Such data is difficult and expensive to obtain from experimental observations. Although interconnection has been investigated for overlapping spheres using continuum percolation models (Pike and Seager 2007; Lorenz et al. 1993; Rintoul and Torquato 1997; Lorenz and Ziff 2001), such studies do not account for the morphological changes that occur after interconnection of bubbles. For example, after the bubble coalescence, the morphology tends toward elongated voids or larger spheres, rather than contacting or overlapping spheres, as the system is energetically driven to reduce surface area and therefore surface energy (Hofman et al. 1990). An alternative approach to experimental data or geometric percolation models to study interconnectivity in U-(Pu)-Zr fuel is the use of mesoscale simulation methods such as phase-field modeling. Such models intrinsically account for the effects of bulk and surface energy on microstructural evolution and therefore better capture the physics that determine morphology than geometric percolation models, and can provide a cost-effective, rapid alternative to experimental measurement.

Here, the growth and interconnection of fission gas bubbles in the hotter γ -phasedominated central regions of U-(Pu)-Zr fuel is simulated using a phase-field model, and the simulation results are used to determine parameters for two BISON models of gas bubble swelling. The structure of the paper is as follows. In Phase-field model of bubble growth and interconnection section, the details of the phase-field model and its parameterization are given. In Simulation results and analysis section, phase-field simulation results are presented, and microstructural features are analyzed to gain insight into the progress of bubble interconnection. The simulation results are analyzed to determine parameters for BISON modeling in Determination of parameters for BISON models of metallic fuel swelling section, and the results are compared with geometric percolation models in Discussion section. Finally, conclusions are drawn and directions for future work are suggested in Conclusions section.

## Phase-field model of bubble growth and interconnection Model formulation

To simulate the growth and interconnection of a large number of bubbles, we employ the Cahn-Hilliard equation with a source term, with a single defect species representing insoluble fission gas atoms such as Xe and accompanying vacancies, and a simplified description of the system’s free energy. Although this formulation does not allow us to include physically-based chemical free energies for the matrix and bubble phases as in some other models of fission gas bubbles in nuclear fuel (Li et al. 2013; Hu et al. 2016; Aagesen et al. 2019; Aagesen et al. 2020; Xiao et al. 2020), it does allow us to capture the changes in morphology that occur as the bubbles interconnect and the microstructure coarsens, and to explore the competing effects of the source term and diffusion on the evolution of the microstructure.

It should also be noted that with this formulation, there is no barrier to nucleation because new bubbles can form via spinodal decomposition if the defect concentration in the matrix enters the spinodal region. Because new fission gas bubbles in nuclear fuel are expected to form by a nucleation and growth mechanism rather than spinodal decomposition, we choose parameters that do not allow formation of new bubbles, and instead seed an initial distribution of bubbles based on experimental observations, as discussed in Initial conditions section. This is equivalent to assuming one-off nucleation of the bubbles.

In formulating the model, we have assumed that the bubbles remain as equilibrium bubbles through the simulation, for which the gas pressure acting to expand the bubble is exactly balanced by the surface tension of the bubble-matrix interface (Olander 1976). There are no local variations in the stress state in the vicinity of equilibrium bubbles and the stress state remains that given by far-field conditions. Equilibrium bubbles are likely to be found when there is a high production rate of vacancies during steady-state operating conditions (when no rapid temperature changes occur that would cause sudden over- or under-pressurization of the bubbles) (Olander 1976). Assuming these conditions exist, as they typically would during normal at-power reactor operation, there are no local variations in the stress state on the length scale of the microstructure. We therefore neglect the influence of elastic energy on microstructural evolution in the model.

The total free energy of the system F is written as a function of the local normalized concentration (mole fraction) c of defects (fission gas atoms on lattice sites and vacancies):

$$
\tag{1}
$$

where the bulk free energy fb is a double well function given by

$$
\tag{2}
$$

and W is the height of the free energy barrier between minima. The gradient energy density is given by

$$
\tag{3}
$$

where κ is the gradient energy coefficient. With this formulation, the free energy has minima at normalized concentrations c = 0 (matrix phase) and c = 1 (bubble phase), and the interface between phases is represented by a smooth variation of c between these values. The time evolution of the system is given by the Cahn-Hilliard equation with the addition of a source term s:

$$
\tag{4}
$$

where M is the defect mobility and μ is the chemical potential, which is equal to the variational derivative of F with respect to c, δFδc : 8F.

$$
\tag{5}
$$

The source term s has the following form

$$
\tag{6}
$$

where h(c) = c3(6c2 − 15c + 10). This form limits the formation of new solute species atoms to the matrix only, since [ 1 − h(0)] = 1 and [ 1 − h(1)] = 0.

## Porosity calculation

One limitation of the model employed for the present study relative to nuclear fuel behavior is that the matrix phase transforms to the bubble phase as defects accumulate, and the size of the simulation domain remains constant. This is different from the physical process of bubble growth and swelling in nuclear fuel, where gas atoms and vacancies combine to form the bubble phase and simultaneously, interstitial atoms are deposited in the matrix phase, causing it to grow. To relate our results to the definitions of swelling and porosity used in engineering fuel performance calculations, we calculate the porosity p in the simulations as follows. The porosity is defined as the volume of the bubble phase divided by the total volume occupied (matrix plus bubbles). We approximate the effect of growth of the matrix phase due to interstitial deposition by assuming that for the purpose of the porosity calculation, the size of the total volume occupied grows by the same amount as the growth of the bubble phase (Olander 1976):

$$
\tag{7}
$$

where V is the volume of the bubble phase and V0 is the original volume of the simulation domain. Since Vf = V /V0,

$$
\tag{8}
$$

Thus, the size of the simulation domain does not change, but for the purposes of calculating porosity, it is assumed the simulation domain volume increases by the same amount as the volume of the bubble phase formed.

## Model parametrization

The model is parametrized as follows. The choice of characteristic interfacial thickness lint and interfacial energy σ are first used to determine W and κ. The equilibrium solution for the interfacial profile between the matrix and bubble phases is given by c = 1 [ 1 + tanh( x−x0δ )], where

$$
\tag{9}
$$

and x0 is the midpoint of the interface. lint = 2δ is a good approximation for the thickness of the interface. The interfacial energy can also be written as a function of κ and W :

$$
\tag{10}
$$

Equations (9) and (10) can be re-arranged to obtain

$$
\tag{11}
$$

and

$$
\tag{12}
$$

For consideration of fission gas bubbles in a U-Zr matrix phase, the interfacial energy is σ = 1.8 J/m2 (Beeler 2019). The interfacial thickness lint was chosen to be lint = 1.5 μm to adequately resolve the bubble phase in the initial conditions, as described in Initial conditions section. Using Eqs. (11) and (12), this results in κ = 4.05 × 10−6 J/m and W = 1.44 × 107 J/m3. These parameters were non-dimensionalized using energy density scale E∗ = W and length scale l ∗ = 1 μm, resulting in W¯ = 1 and κ¯ = 0.281, where the overbars indicate non-dimensional quantities.

The time evolution of the system is expected to be affected by the relative strengths of the source term and mobility of solute atoms in the matrix. However, we are considering the fission gas atoms and accompanying vacancies to be the solute species, and the diffusion coefficient of fission gas atoms in UZr has not been measured or calculated to our knowledge. Therefore, we set the time scale based on the production rate of the solute species and assume a reasonable order-of-magnitude estimate for the diffusion coefficient and resulting defect mobility M as follows. Based on the EBR-II reactor, which used U-(Pu)-Zr fuel, during typical operating conditions a burnup of 10% was reached in approximately 700 days (Miao et al. 2021), equivalent to a fission rate F˙ of 7.91 × 10−8 fissions/nm3/s. The Xe production rate SXe is given by SXe = yXeF˙ , where yXe = 0.2156 is the fission yield of Xe (International Atomic Energy Agency). Assuming a net vacancy production rate approximately 10 times larger than SXe (Aagesen et al. 2019), the total defect production rate S0 ≈ 2.4×10−7/nm3/s. To convert from the volumetric production rate to the units of mole fraction used in Eq. (4), we use s0 = VaS0, where Va = 0.02089 nm3 is the atomic volume of U atoms in the γ phase (Wilson and Rundle 1949), giving s0 ≈ 5 × 10−9/s. We choose time scale t∗ = 106 s and thus s¯0 = s0t ∗ = 5 × 10−3. It is assumed that due to the relatively low maximum burnup and resulting low depletion of fissile U/Pu, s0 remains constant throughout the simulation. For the defect diffusivity, we assume D = 2 nm2/s as a starting point, which is the same order of magnitude as the athermal (radiation-driven) defect diffusivity in UO2 (Aagesen et al. 2021). This value is non-dimensionalized using D¯ = Dt∗/(l ∗)2 = 2. The value of M¯ used in the Cahn-Hilliard equation is given by M¯ = D¯ / ∂2 ¯f∂c2 , which can be approximated as M¯ ≈ D¯ /2W¯ for small c. Equation (4) was solved in non-dimensional form.

The model parameters used for simulations are summarized in Table 1. Because the value of D has not been determined, we varied the value of D used to investigate its effect on microstructural evolution, as discussed further in Effect of defect species diffusivity on microstructure section. The other model parameters were held fixed for the following reasons. κ and W are derived from the interfacial energy σ and chosen interface thickness lint using Eq. (11) and (12). The interface thickness is not expected to influence microstructural evolution as long as it is sufficiently small compared to the bubble size. The interfacial energy was determined using atomistic calculations; although the uncertainty associated with the most representative value σ = 1.8 J/m2 was not quantified, a value between 1.5 and 2 J/m2 will likely be applicable over the entire composition and temperature range of relevance for U-Zr fuel (Beeler 2019). Thus, the percentage variation of σ is expected to be very small relative to the possible variation in values of D; for these reasons, the values of κ and W were held constant for the simulations. Variations in the value of s0 have an equal but opposite impact on microstructural evolution as changes in D, in that a factor of m change in s0 has the same effect as a factor of 1 change in D; for this reason, the value of s0 was held constant for the simulations.

## Numerical implementation

Equations (4) and (5) were discretized as a coupled set of second-order equations using the MOOSE framework (Gaston et al. 2009; Permann et al. 2020). Hexahedral 3D mesh elements with linear Lagrange shape functions were used for spatial discretization. Mesh adaptivity was used, with three levels of refinement and a minimum element size of x y z 0.5 μm so that the element size in the interfacial regions is 1/3 of the interfacial width. Periodic boundary conditions were used in the y and z dimensions, while no-flux boundary conditions were used in the x direction to allow the boundary at x = Lx (where Lx is the simulation domain size in the x direction) to better represent a free surface. The second-order backward differentiation formula was used for time integration, and adaptive time stepping was used with the MOOSE IterationAdaptiveDT time stepper, with eight optimal nonlinear iterations and an iteration window of two (Hales et al. 2015). The simulations were run on 720 cores on the Lemhi cluster at Idaho National Laboratory.

Table 1 Parameters used for phase-field simulations
<table><tr><td>Parameter</td><td>Value</td></tr><tr><td>K</td><td>4.05 × 10-6 J/m</td></tr><tr><td>W</td><td>1.44 × 107 J/m³</td></tr><tr><td>D</td><td>1.33 to 10 nm²/s</td></tr><tr><td>s0</td><td>5×10-9s-1</td></tr></table>

## Initial conditions

Based on Fig. 2 of Bauer and Holland (1995), the number density of bubbles N in U-10Zr fuel at 1.3% burnup is estimated to be N = 3.0 × 1014/m3. To simulate the growth and interconnection of a reasonably large number of bubbles while still remaining computationally tractable, we choose a cuboidal simulation domain of size Lx = Ly = Lz = 72 μm, where Ly and Lz are the sizes of the simulation domain in the y and z directions. The simulation domain is in the range 0 ≤ x ≤ Lx, 0 ≤ y ≤ Ly, 0 ≤ z ≤ Lz. In the initial conditions, the total number of bubbles n = 112 to match the experimentally observed N for the simulation domain volume. The initial bubble radius is rbub = 3.4 μm, corresponding to an initial bubble volume fraction of 5%. (This value was chosen because it is significantly below the expected porosity interconnection threshold, but still large enough that the interfacial thickness and corresponding mesh size needed to resolve the initial bubbles do not increase computational requirements excessively; the simulation results are not expected to be sensitive to the exact value used for initial porosity.) The bubbles were placed randomly in the initial conditions with a minimum spacing of 10 μm between their centers. To investigate the effects of initial conditions on simulation results and obtain improved statistics, a total of 10 sets of initial random bubble positions were created by supplying a different seed to the random number generator that determines the initial bubble positions. Each of the 10 total sets of initial bubble positions are referred to as Configuration 1 – 10. The initial conditions for Configuration 1 are shown in Fig. 1a, with the isosurface of c = 0.5 shown.

## Simulation results and analysis

Simulation results for Configuration 1 for the case s0 = 5×10−9 s−1 and D = 2 nm2/s are shown in Fig. 1. At simulation time t = 2.53 × 107 s, all bubbles in the initial conditions are still independent; no bubbles have yet merged. At t = 5.06 × 107 s, the process of bubble merging and coalescence has begun. By t = 7.62 × 107 s, many of the bubbles have merged, and a continuous path through the bubble phase exists from the simulation domain boundary at x  0 μm and the boundary at x  72 μm, as discussed further later in this section.

## Effect of defect species diffusivity on microstructure

As discussed in Phase-field model of bubble growth and interconnection section, because the diffusion coefficients of defect species in U-Zr have not been determined, in this section the diffusivity D of the single defect species is varied to determine its effect on microstructural evolution. Comparisons of the microstructure for the cases D = 2 nm2/s and D = 10 nm2/s for Configuration 1 are shown in Fig. 2 for time t = 1.14 × 108 s. The microstructure of the case with D = 2 nm2/s (Fig. 2a) is qualitatively much finer than the case with D = 10 nm2/s (Fig. 2b). To better understand the differences in microstructure and the reasons for these differences, the microstructure for varying D is quantified in the remainder of this section.

The volume fraction of the bubble phase, Vf is shown as a function of time in Fig. 3 for s0 = 5 × 10−9 s−1 and varying D for Configuration 1. The defect species is deposited in the matrix phase and diffuses to the bubble phase, causing the bubble phase to grow. For the D = 1.33 nm2/s simulation, spinodal decomposition occurred in the matrix phase beginning at t = 3.65 × 107 s due to the simplified free energy used. Because this does not correctly represent the nucleation-controlled formation mechanism of bubbles as discussed in Model formulation section, this simulation was terminated and only the cases with D ≥ 2 nm2/s were considered further. For the remaining simulations, from t = 0 to t ≈ 6 × 107 s, the volume fraction of the bubble phase grows more quickly for the higherdiffusivity simulations. This is because the higher diffusivity allows the defect species to be transported more rapidly from where it is deposited in the matrix phase to the bubble phase, causing the bubble phase to grow faster. After t > 6 × 107 s, the volume fractions for the different diffusivity simulations become approximately equal for the remainder of the simulation time. This is because as the volume fraction of the bubble phase grows, the volume fraction of the matrix phase correspondingly shrinks, and the distance over which the deposited defect species must diffuse to reach the bubble phase decreases significantly. Thus, after t ≈ 6 × 107 s, the defect species mobility is not a significant cause of the differences in microstructure between the different diffusivity simulations.

![](images/2a4d816eb3c447daed08b1fdc2afc6bcf69d36c20fd5870aa2b4388db38e7bc8.jpg)  
(a) Initial conditions

![](images/d828b9061e3812938a0454a3d281a673394b44a6927923b4c921b44e81c44140.jpg)  
(b) t= 2.53 × 107s

![](images/175934b831f60e5c2c6a5fe23a7400e4f1849603061d67cb6192eda5d29059c9.jpg)  
(c) t = 5.06 × 107 s

![](images/78b0b42871471e9bd36ffd2ec910d1bb24b792a4f47978a0f92d04f0e5be936a.jpg)  
(d) t = 7.62 × 107 s

Fig. 1 Evolution of microstructure of Configuration 1 during simulation of gas bubble growth with s0 = 5 × 10−9 s−1 and D = 2 nm2/s. Simulation domain size is 72 μm ×72 μm ×72 μm. Isosurface of c = 0.5 is shown. a initial conditions. b the bubbles have grown but none have begun to merge. c bubble merging and coalescence has begun. d a continuous path through the bubble phase exists from the simulation domain boundary at x = 0 μm and the boundary at x = 72 μm  
![](images/fd6707494e7dd8b55e2066c17b0a024e52792d91d0c6d2701de583ae1aec38cc.jpg)  
(a)t=1.14 × 10°s,D=2 nm²/s

![](images/eee4efe3afe693ea833e1e5280fb9c42e0f6685c0749614468c163791f07236f.jpg)  
(b)t= 1.14× 108 s,D= 10 nm²/s  
Fig. 2 Comparison of microstructure for varying diffusivity D, for initial conditions of Configuration 1. Simulation domain size is 72 μm ×72 μm ×72 μm

![](images/106a3c14b42a8d88f53aa31c8d03c33d07ea58c087047a67667a01425fa21bba.jpg)  
Fig. 3 Volume fraction of the bubble phase, Vf , versus time for varying diffusivity (initial conditions of Configuration 1)

The microstructure of the bubble growth and interconnection simulations was also quantified by determining the surface area of the bubble-matrix interface, as shown in Fig. 4 for Configuration 1. The areas are plotted versus time for the varying diffusivity cases in Fig. 4a. For t < 5×107 s, the surface area of the high-diffusivity cases grows faster than the lower diffusivity cases. This is because the volume fraction of the high-diffusivity cases grows faster during this time, resulting in faster growth of the bubble surface area. At this early stage, the bubbles are relatively far from each other, and coarsening has not yet begun to significantly affect microstructural evolution. However, at t > 5 × 107 s, the area of the low-diffusivity simulations becomes larger than that of the higher diffusivity simulations, even though the volume fraction is very nearly equal for each case. This is due to the effect of coarsening, the process by which the system reduces its energy by reducing surface area and thus interfacial energy. Kinetically, this process is driven by the diffusion of the defect species from regions of high curvature to regions of low curvature caused by the Gibbs-Thomson effect. Higher diffusional mobility increases the rate of coarsening, and thus interfacial area is lower for the high-diffusivity cases at later times. The microstructural evolution is thus controlled by a competition between the strength of the source term and the mobility term.

![](images/7487ba3fb1d24a3724a1d69d43588099267c4c129daeaf4a84961037c5f533fc.jpg)

![](images/c3b3f8757c76d747aefce39e7cace468e2e86d4698ba2883bde5cf194fd3e25e.jpg)  
Fig. 4 Surface areas as a function of a time and b porosity (initial conditions of Configuration 1)

The surface area is plotted as a function of p in Fig. 4b. When plotted versus p, the surface area is constant for the different diffusivity simulations below p < 0.15. At these lower values, the bubbles grow uniformly and are spaced far enough apart that coarsening has not begun to affect microstructural evolution. However, when p > 0.15, the higher diffusivity simulations have a smaller surface area than the D = 2 case, indicating that as the bubbles have begun to interconnect, coarsening eliminates surface area more rapidly for the higher diffusivity simulations. This is the primary cause for the differences in microstructure between Fig. 2a and b.

Another aspect of the microstructure that is useful to characterize is the length scale or characteristic size of features in the system. This is helpful to ensure that the simulation domain size is large enough to obtain a statistically valid sample of the microstructure. To ensure the domain size is sufficiently large, the domain size should be significantly greater than the characteristic length scale of the system. The length scale of the microstructural features can be easily characterized early in the system’s evolution when the bubbles are isolated and have a spherical morphology, and can be characterized by bubble radius. However, when the bubbles grow and begin to impinge on one another, they become a highly interconnected structure, for which there is no well-defined radius. An alternative definition of the characteristic length scale that can be employed for highly interconnected structures is the inverse of the surface area of interface per unit volume, S−1 . This definition has been used previously as a characteristic length scale for the coarsening of bicontinuous microstructures (Kwon et al. 2007). S−1v is plotted versus p in Fig. 5, for varying defect diffusivity and initial conditions of Configuration 1. Although S−1v grows significantly during the simulated microstructural evolution, it remains an order of magnitude lower than Lx = 72 μm, indicating that the simulation domain size is large enough to obtain reasonable statistics for microstructural evolution.

![](images/39368f5def7ff4cb2baebf1d4bab3a1a3cf2d3779aeccc46f57af21b6aa3ba49.jpg)  
Fig. 5 Characteristic length scale S−1v for varying simulated diffusivities (initial conditions of configuration 1). S−1v remains an order of magnitude smaller than the simulation domain size Lx = 72 μm

## Effect of initial bubble number density

Although an estimate of N was obtained based on experimental data, this was only determined based on a single micrograph, giving the estimated value a high degree of uncertainty. The value of N at a particular location in the fuel is expected to depend strongly on the nucleation rate, which itself is a function of fission rate, gas diffusivity, Pu content, temperature, re-solution rate, and other factors (Olander 1976). To determine how strongly the bubble number density affects microstructural evolution and the rate of bubble interconnection, simulations of bubble growth with varying N were conducted with D = 2 nm2/s and s0 = 5 × 10−9 s−1. Simulations with 140 and 168 bubbles were performed, corresponding to N = 3.75 × 1014/m3 and N = 4.5 × 1014/m3, respectively. (Simulations with lower N resulted in spinodal decomposition of the matrix phase and thus are not further considered here.)

The number of bubbles versus time and porosity are shown in Fig. 6. For larger N, the rate of interconnection of bubbles was faster with respect to time, as would be expected. However, the trend was consistent even when plotted against porosity.

## Bubble venting and percolation

To understand how the interconnection of bubbles progresses and to provide a basis for parameterization of BISON models of swelling and fission gas release (Novascone et al. 2019; Matthews and Unal 2019; Casagranda et al. 2020; Olander 1976), the fraction of bubble volume connected to an external surface, fV , was calculated for the simulations as follows. Individual bubbles were identified as isolated regions where c > 0.5 using a recursive flood fill algorithm (Permann et al. 2016) and the volume of each such individual bubble was determined. A free surface is assumed to exist at the simulation domain boundary at x = 72 μm. For each bubble, it is determined whether or not it intersects that boundary, and fV is calculated as the volume of bubbles that intersect the free surface divided by the total bubble volume at each time step.

![](images/337ffa31b66704eb33c3031d1c900415dd5be058af741175c12ce17a01327e23.jpg)

(b)  
![](images/932eeb664b5d14ddc5c6f94463808b792c69a90811360a83b46924f57b59b39f.jpg)  
Fig. 6 Number of bubbles for varying initial bubble number density

fV is plotted as a function of porosity p for varying diffusivity cases in Fig. 7. fV is nonzero at the start of the simulation because some bubbles contact the free surface in the initial condition; however, their contribution is small. The increase in fV is slow until p ≈ 0.25. Past that point, fV increases rapidly until p ≈ 0.3. At p = 0.35, all bubbles are connected to a free surface for all configurations and parameters considered.

![](images/fa35237613b560ebb2247eb2e795a1ea53e7f25837e3c9c9848b4edb4f1f4609.jpg)  
(a) D=2 nm²/s

![](images/9ca08c2e5c6bc34876bd951f1f0781b3504c3c749172345438ca3421d5b0896f.jpg)

(b) D= 5 nm²/s  
![](images/179b3464f3cd3975b1460c83b70a66f2ab0171e4eeb01a1d84ce7ed22f6de72a.jpg)  
(c) D = 10 nm²/s  
Fig. 7 Fraction of total bubble volume connected to a free surface, fV , as a function of porosity p for varying diffusivity

To better quantify the progression of interconnectivty, the plots of fV versus p were fit using a function of the form

$$
\tag{13}
$$

where erf is the error function, pcen is the center of the distribution, and  is the characteristic width of the distribution. The choice of this functional form is motivated by its past use in modeling percolation phenomena (Rintoul and Torquato 1997; Brunini et al. 2011). As previously discussed, fV is non-zero in the initial conditions due to the initial random placement of the bubbles and non-zero initial bubble radius. To account for this, simulation data with p < 0.1 was excluded from the fit.

An example of simulated fV versus p data and the corresponding fV fit from it is shown in Fig. 8 for Configuration 1, D = 2 nm2/s, N = 3 × 1014/m3. In this case, pcen = 0.269 and  = 0.0392. With the exception of an early increase in fV at p ≈ 0.2, Eq. 13 appears to represent the data well. This early increase was not observed in all configurations.

A similar fit was performed for each configuration and set of simulation parameters considered. The mean of pcen and  for the 10 configurations and corresponding standard deviations are given in Table 2 for each set of simulation parameters considered. The mean values of pcen and  determined for the different diffusivity cases are close to each other, although in this case pcen for D = 5 nm2/s lies slightly outside of one standard deviation from the values determined for D = 2 and D = 10 nm2/s. However, due to the lack of an apparent trend with D and the effect of the relatively small number of samples used, we believe that D does not strongly influence pcen. The similarity of the values obtained for both pcen and  in spite of the differences in microstructure suggests that the interconnection process of initially spherical bubbles may be governed by a universal process that is independent of length scale evolution.

![](images/a3785861d75db9aaeeb03f133904399837df4c6144a40cdf2c1d91bb055ce261.jpg)  
Fig. 8 Fraction of total bubble volume that is connected to a free surface, fV , as a function of porosity p for M = 1, Configuration 1, and function fit to the data using Eq. (13)

Table 2 Mean pcen and  for the five initial condition configurations considered and corresponding standard deviations for each set of simulation parameters
<table><tr><td>D (nm2/s)</td><td>N(m-3)</td><td>Mean pcen</td><td>Std. dev. pcen</td><td>Mean △</td><td>Std. dev. △</td></tr><tr><td>2</td><td>3×1014</td><td>0.263</td><td>0.00522</td><td>0.0364</td><td>0.00922</td></tr><tr><td>5</td><td>3×1014</td><td>0.248</td><td>0.00738</td><td>0.0404</td><td>0.0127</td></tr><tr><td>10</td><td>3×1014</td><td>0.261</td><td>0.00905</td><td>0.0391</td><td>0.0126</td></tr><tr><td>2</td><td>3.75 × 1014</td><td>0.248</td><td>0.00477</td><td>0.0373</td><td>0.00664</td></tr><tr><td>2</td><td>4.5× 1014</td><td>0.244</td><td>0.00574</td><td>0.0328</td><td>0.00609</td></tr></table>

Although N = 3 × 1014/m3 is based on the best available experimental data, this value may vary due to temperature, Pu content, and other factors. Therefore, the effect of variation in N was also considered by simulating initial conditions with N = 3.75 × 1014/m3 and N = 4.5 × 1014/m3. As with the case of N = 3 × 1014/m3, 10 total configurations of initial conditions for the larger values of N were obtained by changing the seed in the random number generator used to determine initial bubble positions. As can be seen in Fig. 9, for the cases with larger N, the trends in fV versus p are similar to those observed for N = 3 × 1014/m3 in Fig. 7a, although for larger N, there appears to be less variation between the curves for each configuration. From the data of Table 2, there is also a decrease in pcen with increasing N, pointing to the need for further simulations with different N if improved experimental measurements of N become available.

In addition to fV , another useful quantity that can be determined from the simulations of bubble growth and interconnection is the percolation threshold, pc. The percolation threshold in this context is the porosity at which a continuous pathway through the bubble phase exists that connects the domain boundaries at x = 0 μm and x = 72 μm.

The mean value of pc for the 10 different configurations and its standard deviation are shown in Table 3 for each set of simulation parameters considered. Although the diffusivity of the defect species D is based on an order of magnitude estimate only, the data of Table 3 shows that the mean values of pc are very close to each other for the different diffusivities D = 2, 5, 10 nm2/s and constant N = 3 × 1014/m3. The total variation in mean pc for the different diffusivity cases is comparable to the standard deviation in each of the individual values (although it should be noted that a larger number of samples should ideally be considered when determining statistical quantities such as the standard deviation). Therefore, we conclude that although the defect species diffusivity does result in significant differences in the microstructure for different diffusivity, the resultant value of pc does not vary significantly with changes in D, at least for the range of values considered here.

![](images/ee7194e86d8fe4420a9f5db65144c1f51c96d18016cf0c8cc2560a9cb590f7be.jpg)  
(a) N = 3.75 × 1014/m³

![](images/b703c8b3f61ca1e601e5ad0c193ca3abdb3f82784e59549efc5ef38f57781649.jpg)  
(b) N = 4.5 ×1014/m³  
Fig. 9 Fraction of total bubble volume that is connected to a free surface, fV , as a function of porosity p for a N 3.75 1014/m3 and b N 4.5 1014/m3, with D 2 nm2/s

Table 3 Mean percolation threshold (pc) and mean porosity at which fV = 0.8 (p0.8) for the five initial condition configurations considered, and corresponding standard deviations, for each set of simulation parameters
<table><tr><td>D (nm²/s)</td><td>N(m-3)</td><td>Mean pc</td><td>Std. dev. pc</td><td>Mean po.8</td><td>Std. dev. po.8</td></tr><tr><td>2</td><td>3×1014</td><td>0.263</td><td>0.0101</td><td>0.280</td><td>0.00407</td></tr><tr><td>5</td><td>3×1014</td><td>0.254</td><td>0.00902</td><td>0.272</td><td>0.0103</td></tr><tr><td>10</td><td>3×1014</td><td>0.265</td><td>0.00922</td><td>0.283</td><td>0.0120</td></tr><tr><td>2</td><td>3.75 × 1014</td><td>0.246</td><td>0.00983</td><td>0.274</td><td>0.00435</td></tr><tr><td>2</td><td>4.5 × 1014</td><td>0.248</td><td>0.0145</td><td>0.265</td><td>0.00675</td></tr></table>

The effect of N on pc was also determined. As shown in Table 3, pc decreases with increasing N. Therefore, if future experimental data allows N to be better quantified, additional simulations using the more accurate values of N should be performed.

## Determination of parameters for BISON models of metallic fuel swelling

Recently, two physics-based models of swelling in U-(Pu)-Zr fuels have been implemented in BISON. In this section, parameters for these models are determined from the phasefield simulations described in Simulation results and analysis section.

## Determination of parameters for simple swelling model

The simpler of the two swelling models implemented recently is known in BISON as UPuZrGaseousEigenstrain. In this model, it is assumed that the number of bubbles is constant, the bubbles are all of the same size and are spherical in shape, the amount of gas in the matrix is negligible, the bubbles are in mechanical equilibrium with the solid, and the gas within the bubbles follows the ideal gas law. Under these assumptions, the swelling is given by Olander (1976)

$$
\tag{14}
$$

where k is the Boltzmann constant, T is the temperature in K, σ is the surface tension of the fuel-bubble interface, YXe is the gaseous fission product yield, F˙ is the fission rate density, t is time, and N is the number density of bubbles. With increasing burnup, the volumetric swelling increases by Eq. (14) until porosity is high enough to allow gas release. In the model, the number of atoms produced by fission that are added to the bubbles (and thus that contribute to swelling by Eq. 14) decreases linearly in a range controlled by the BISON model parameters interconnection initiating porosity, pi, and interconnection terminating porosity, pt. In the remainder of this section, we describe how pi and pt are determined from the phase-field simulations.

We assume that significant gas release cannot occur from the internal volume of the fuel to the free surface until the percolation threshold, pc, is reached. Based on this assumption pi should be set equal to the mean value of pc determined for a representative microstructure. The data for mean values of pc is shown in Table 3. As discussed in Bubble venting and percolation section, for N = 3×1014/m3, the values of pc for the different diffusivities considered are statistically indistinguishable. Therefore, we choose pc = 0.263 as a representative value from the D = 2 nm2/s case. Assuming pi = pc as previously discussed, the recommended value of pi for BISON simulations is 0.263.

To determine pt for BISON simulations, we use the fact that post-irradiation examination of EBR-II fuel rods showed that fission gas release plateaued at approximately 80% of the fission gas produced (Hofman et al. 1997). We therefore set pt to the porosity p at which fV = 0.8, which we refer to as p0.8. The mean and standard deviation of p0.8 for the different cases considered are also shown in Table 3. The mean value of p0.8 also does not vary strongly with D, so again using the D = 2 nm2/s case as representative, the recommended value of pt for BISON simulations is 0.280. (Similar to the trend observed in pc, the mean value of p0.8 decreases with increases in N.)

## Determination of parameters for viscoplastic swelling model

A new model for swelling due to fission gas bubbles was recently added to BISON (Matthews and Unal 2019). In this model, it is again assumed that the number of bubbles is constant, their size is uniform and shape is spherical. However, additional physics are considered beyond those used in the derivation of Eq. (14). The concentration of gas in the matrix and diffusion to the bubbles is considered, the hydrostatic stress in the fuel matrix surrounding the gas bubbles is accounted for, and the van der Waals equation of state is used for the fission gas within bubbles. In the model of Matthews and Unal (2019), the fraction of bubbles in a given volume element that are connected to an external surface is described by an interconnectivity function I(p), where p is the local porosity. In this section, we fit a function for I(p) based on the phase-field results of Simulation results and analysis section.

The plots of fV versus p describe the fraction of bubbles that are connected to an external surface and contain the information needed to determine I(p). Similar to Determination of parameters for simple swelling model section, we use the data for D = 2 nm2/s, N = 3 × 1014/m3 to determine I(p). The functional form for I(p) used in BISON is Matthews and Unal (2019)

$$
\tag{15}
$$

$$
\tag{16}
$$

where pstart is the interconnection initiating porosity and pend is the interconnection terminating porosity. Thus, the parameters to be determined are pstart and pend. To determine these values, a MATLAB script was written that varied pstart and pend to determine what values minimized the least-squares error between Eq. (15) and Eq. (13) with pcen = 0.263 and  = 0.0364. This resulted in pstart = 0.198 and pend = 0.327. A plot of the smooth step function I(p) with these parameters and Eq. (13) is shown in Fig. 10. The least-squares minimization process results in good agreement between Eq. (13) and (15) for the given parameters.

![](images/f8343ea90c22b8313a44545f6681ad7efdc472a26d97f82308b04de12abfbe31.jpg)  
Fig. 10 Comparison of I(p) (smooth step function of Eq. 15) and fV (Eq. 13) with parameters based on fit to phase-field simulations

## Discussion

In Simulation results and analysis section, the percolation behavior of spheres growing due to deposition of a defect species in the surrounding matrix was studied. Although the percolation behavior of this situation has not yet been determined to our knowledge, percolation of other geometries has been studied extensively in the past. In this section, the present simulations are compared to existing literature.

The previously studied geometry that is most similar the present simulation results is the continuum percolation of overlapping 3D spheres (Pike and Seager 2007; Lorenz et al. 1993; Rintoul and Torquato 1997; Lorenz and Ziff 2001). In such a model, spheres of uniform radius are randomly placed throughout a simulation domain, with overlapping allowed between spheres, and there is no curvature-driven coarsening of the sphere-matrix interface following sphere placement. Rintoul and Torquato determined the percolation threshold for this geometry to be pc = 0.2895 ± 0.0005 and determined critical exponents for the continuum system as expected from percolation theory (Rintoul and Torquato 1997). Lorenz and Ziff later found pc = 0.289573 ± 0.000002, in agreement with the previous value determined by Rintoul and Torquato but with reduced uncertainty. This value is slightly larger than the values for pc found in our simulations. The reason for this difference may be partially due to the fact that in our model, swelling is assumed to occur in the matrix surrounding the bubbles, as reflected in Eq. (8). Such swelling is not considered in continuum percolation models. It should also be noted that the value of the percolation threshold can be determined much more precisely for continuum percolation models than for the present growth simulations. This is because microstructural evolution does not occur with time in continuum percolation models, reducing computational requirements and therefore allowing a larger size and number of representative microstructures to be sampled.

The percolation of 2D disks growing by a nucleation and growth mechanism has been studied using phase-field simulations (Brunini et al. 2011). The physics of this mechanism are more similar to the present simulation than the previously discussed continuum percolation of overlapping spheres, although the lack of 3D results in Brunini et al. (2011) limits the ability to make direct comparisons with the present simulations. Another difference between Brunini et al. (2011) and the present simulations is that in Brunini et al. (2011), a fixed amount of defects was introduced into a supersaturated matrix in the initial conditions of each simulation, whereas in the present simulations, there are no defects in the matrix in the initial conditions, and defects are added by a source term. Nevertheless, Brunini et al. (2011) found pc 0.661 0.003 for nucleation and growth of 2D disks. This is slightly lower than the value obtained for continuum percolation modeling of uniform overlapping 2D disks, pc 0.6764 0.0009 (Lorenz et al. 1993). Thus, for both 2D and 3D geometries, nucleation and growth-type models where coarsening occurred simultaneously with growth resulted in lower values of pc than continuum percolation models.

## Conclusions

In this work, the growth and interconnection of fission gas bubbles in the hotter central region of U-(Pu)-Zr nuclear fuel was simulated using a Cahn-Hilliard model, with a single defect species that was generated uniformly throughout the fuel matrix with a source term. Because the diffusion coefficients of the relevant defect species in U-(Pu)-Zr have not been fully determined, the defect species diffusivity in the Cahn-Hilliard model was varied parametrically with constant initial bubble number density and source term strength to determine its effect on microstructure. Higher defect diffusivity simulations initially had a more rapid increase in bubble volume fraction and bubble surface area with time, as the higher diffusivity allowed defects to diffuse from the matrix where they are generated to the bubbles more rapidly. However, once the bubbles began to interconnect, the surface area of the higher diffusivity simulations decreased relative to lower diffusivity simulations, as the higher defect diffusivities allowed coarsening to proceed more rapidly. A characteristic length scale of the inverse of the surface area per unit volume, S−1v , was determined for the varying diffusivity simulations; S−1v remained significantly smaller than the dimensions of the simulation domain in each case, increasing confidence that the simulation domain is large enough to obtain reasonable statistics.

The fraction of bubbles vented to an external surface of the simulation domain, fV , was also quantified for simulations with varying diffusivities and for five different initial bubble position configurations. The increase in fV occurred mostly between porosity p ≈ 0.25 and p ≈ 0.3 for each simulation. The percolation threshold was also determined for these simulations. Mean values for differing diffusivity cases were in the range of 0.254 to 0.265. Thus, although the microstructures for different diffusivity cases had significantly different morphologies, the interconnection and percolation properties remained similar to each other. The effect of varying initial bubble number density N was also considered. Increasing values of N did appear to cause interconnection to happen at lower porosities, as quantified by trends in the plots of fV versus p and by the calculated values of pc.

The simulation results were analyzed to parameterize engineering-scale models of fuel swelling and gas release in the fuel performance code BISON. For the simpler swelling model UPuZrGaseousEigenstrain, the interconnection initiating porosity was determined to be pi = 0.263, and the interconnection terminating porosity was determined to be pt = 0.280. For the viscoplastic swelling model (Matthews and Unal 2019), the parameters of the interconnection function I(p) of Eq. (15) were determined to be pstart = 0.198 and pend = 0.327.

The simulation results were also compared to existing percolation models. The previously studied geometry that is most similar to the present simulations is the continuum percolation of overlapping 3D spheres. The percolation threshold for this configuration is slightly larger than the values of percolation threshold found for our simulations. In addition to the difference in morphology, this difference may also be partially due to the manner in which porosity is determined in our simulations, where swelling of the surrounding fuel matrix is assumed as bubbles grow. Such swelling is not considered in continuum percolation models.

Based on the present results, future experimental work should focus on determining the characteristics of the bubble population at the early stages of swelling, particularly the bubble number density at low burnup. The size distribution of bubbles in the early stages may also be used to determine whether the assumption of one-off nucleation, as used in these simulations, is valid, or whether a model that includes simultaneous nucleation and growth should be used for future work. Finally, as further increases in computational power are available, improvements in code efficiency are made, and defect parameters such as diffusion coefficients become available, future phase-field simulations should shift to a more physical model that includes vacancies and gas atoms as independent defect species.

## Acknowledgments

This work was funded by the Department of Energy Nuclear Energy Advanced Modeling and Simulation program. This manuscript has been authored by Battelle Energy Alliance, LLC under Contract No. DE-AC07-05ID14517 with the US Department of Energy. Los Alamos National Laboratory, an affirmative action/equal opportunity employer, is operated by Triad National Security, LLC, for the National Nuclear Security Administration of the U.S. Department of Energy under Contract No. 89233218CNA000001. The United States Government retains and the publisher, by accepting the article for publication, acknowledges that the United States Government retains a nonexclusive, paid-up, irrevocable, world-wide license to publish or reproduce the published form of this manuscript, or allow others to do so, for United States Government purposes.

## Authors’ contributions

Larry Aagesen: Conceptualization, Methodology, Software, Validation, Writing- original draft. Albert Casagranda: Conceptualization, Methodology, Writing- Review and Editing. Christopher Matthews: Conceptualization, Methodology, Writing- Review and Editing. Benjamin Beeler: Conceptualization, Methodology, Writing- Review and Editing. Stephen Novascone: Conceptualization, Methodology, Writing- Review and Editing, Funding Acquisition. All authors read and approved the final manuscript.

## Funding

This work was funded by the Department of Energy Nuclear Energy Advanced Modeling and Simulation program.

## Availability of data and materials

The MOOSE framework was used to carry out the simulations in this work. The MOOSE framework is open-source and available at mooseframework.inl.gov. Due to export control restrictions, the raw data from the simulations cannot be shared via open repository. The data may be made available to interested parties (subject to export control and other restrictions) by contacting the authors.

## Declarations

## Competing interests

The authors declare that they have no competing interests.

## Author details

1Computational Mechanics and Materials Department, Idaho National Laboratory, P.O. Box 1625, Idaho Falls 83415, ID, USA. 2TerraPower, LLC, 15800 Northup Way, Bellevue 98008, WA, USA. 3Materials Science and Technology Division, Los Alamos National Laboratory, P.O. Box 1663, Los Alamos 87545, NM, USA. 4Department of Nuclear Engineering, North Carolina State University, Raleigh 27965, NC, USA.

## References

L. K. Aagesen, D. A. Andersson, B. W. Beeler, M. W. D. Cooper, K. A. Gamble, Y. Miao, G. Pastore, M. R. Tonks, Phase-field simulations of intergranular fission gas bubble behavior in U3Si2 nuclear fuel. J. Nucl. Mater. 152415, 541 (2020)

L. K. Aagesen, S. Biswas, W. Jiang, D. A. Andersson, M. W. D. Cooper, C. Matthews, Phase-field simulations of fission gas bubbles in high burnup UO2 during steady-state and LOCA transient conditions. J. Nucl. Mater. 153267, 557 (2021)

L. K. Aagesen, D. Schwen, M. R. Tonks, Y. F. Zhang, Phase-field modeling of fission gas bubble growth on grain boundaries and triple junctions in UO2 nuclear fuel. Comput. Mater. Sci. 161, 35–45 (2019)

C. L. Angerman, G. R. Caskey Jr, Swelling of uranium by mechanical cavitation. J. Nucl. Mater. 13(2), 182–196 (1964)

T. H. Bauer, J. W. Holland, In-Pile Measurement of the Thermal Conductivity of Irradiated Metallic Fuel. Nucl. Technol. 110(3), 407–421 (1995)

B. W. Beeler, Atomistic calculations of material parameters for swelling and redistribution models in U-Zr fuel, Report INL/EXT-19-54798. (Idaho National Laboratory, Idaho Falls, 2019)

V. E. Brunini, C. A. Schuh, W. C. Carter, Percolation of diffusionally evolved two-phase systems. Phys. Rev. E. 021119, 83 (2011)

A. Casagranda, L. K. Aagesen, J.-H. Ke, W. Jiang, J. D. Hales, A. Toptan, K. A. Gamble, X.-Y. Liu, S. R. Novascone, C. Matthews, D. S. Stafford, Summary of BISON milestones - NEAMS FY20 report. Report INL/EXT-20-60002. (Idaho National Laboratory, Idaho Falls, 2020)

D. Gaston, C. Newman, G. Hansen, D. Lebrun-Grandié, MOOSE: A parallel computational framework for coupled systems of nonlinear equations. Nucl. Eng. Des. 239, 1768–1778 (2009)

J. D. Hales, K. A. Gamble, B. W. Spencer, S. R. Novascone, G. Pastore, W. Liu, D. S. Stafford, R. L. Williamson, D. M. Perez, R. J. Gardner, BISON users manual. Technical Report INL/MIS-13-30307, Rev. 3, Idaho National Laboratory, September 2015., (2015)

G. L. Hofman, R. G. Pahl, C. E. Lahm, D. L. Porter, Swelling behavior of U-Pu-Zr fuel. Metall. Trans. A. 21(2), 517–528 (1990)

G. L. Hofman, L. C. Walters, T. H. Bauer, Metallic fast reactor fuels. Prog. Nucl. Energy. 31(1-2), 83–110 (1997)

S. Hu, D. E. Burkes, C. A. Lavender, D. J. Senor, W. Setyawan, Z. Xe, Formation mechanism of gas bubble superlattice in UMo metal fuels: Phase-field modeling investigation. J. Nucl. Mater. 479, 202–215 (2016)

International Atomic Energy Agency, Chain fission yields. https://www-nds.iaea.org/sgnucdat/c1.htm. Accessed 13 Apr 2017

Y. Kwon, K. Thornton, P. W. Voorhees, Coarsening of bicontinuous structures via nonconserved and conserved dynamics. Phys. Rev. E. 021120, 75 (2007)

Y. Li, H. Shenyang, R. Montgomery, F. Gao, X. Sun, Phase-field simulations of intragranular fission gas bubble evolution in UO2 under post-irradiation thermal annealing. Nucl. Instrum. Methods Phys. Res. Sect. B Beam Interact. Mater. Atoms. 303, 62–67 (2013)

B. Lorenz, I. Orgzall, H.-O. Heuer, Universality and cluster structures in continuum models of percolation with two different radius distributions. J. Phys. A Math. Gen. 26, 4711–4722 (1993)

C. D. Lorenz, R. M. Ziff, Precise determination of the critical percolation threshold for the three-dimensional “Swiss cheese” model using a growth algorithm. J. Chem. Phys. 114(8), 3659–3661 (2001)

C. Matthews, C. Unal, Initial implementation of a bubble-surface force-balance fission gas behavior algorithm for metallic nuclear fuel into BISON. Technical Report LA-UR-19-31814. (Los Alamos National Laboratory, Los Alamos, 2019)

Y. Miao, A. Oaks, A. M. Yacout, C. Matthews, S. R. Novascone, FY21 progress report on BISON metallic fuel model development and V&V using EBR-II legacy data. Report ANL/CFCT-21/19. (Argonne National Laboratory, Lemont, 2021)

S. R. Novascone, A. Casagranda, L. K. Aagesen, B. W. Beeler, W. Jiang, A. M. Jokisaari, D. J. McDowell, A. D. Lindsay, J. B. Tompkins, G. Pastore, A. X. Zabriskie, D. Schwen, R. L. Williamson, B. W. Spencer, A. E. Slaughter, Y. Miao, A. Oaks, A. M. Yacout, C. Matthews, D. S. Stafford, Summary of BISON milestones and activities - NEAMS FY19 report. Report INL/EXT-19-55699. (Idaho National Laboratory, Idaho Falls, 2019)

D. R. Olander, Fundamental Aspects of Nuclear Reactor Fuel Elements. (Technical Information Center, Office of Public Affairs, Energy Research and Development Administration, 1976)

R. G. Pahl, D. L. Porter, C. E. Lahm, G. L. Hofman, Experimental studies of U-Pu-Zr fast reactor fuel pins in the Experimental Breeder Reactor-II. Metall. Trans. A. 21(7), 1863–1870 (1990)

C. J. Permann, D. R. Gaston, D. Andrš, R. W. Carlsen, F. Kong, A. D. Lindsay, J. M. Miller, J. W. Peterson, A. E. Slaughter, R. H. Stogner, R. C. Martineau, MOOSE: Enabling massively parallel multiphysics simulation. SoftwareX. 11, 100430 (2020)

C. J. Permann, M. R. Tonks, B. Fromm, D. R. Gaston, Order parameter re-mapping algorithm for 3D phase field model of grain growth using FEM. Comput. Mater. Sci. 115, 18–25 (2016)

G. E. Pike, C. H. Seager, Percolation and conductivity: A computer study. I. Phys. Rev. B. 10(2), 1421–1434 (2007)

M. D. Rintoul, S. Torquato, Precise determination of the critical threshold and exponents in a three-dimensional continuum percolation model. J. Phys. A: Math. Gen. 30, L585—L592 (1997)

L. C. Walters, Thirty years of fuels and materials information from EBR-II. J. Nucl. Mater. 270(1), 39–48 (1999)

A. S. Wilson, R. E. Rundle, The structures of uranium metal. Acta Crystallogr. 2, 126–127 (1949)

Z. Xiao, Y. Wang, S. Hu, Y. Li, S.-Q. Shi, A quantitative phase-field model of gas bubble evolution in UO2. Comput. Mater. Sci. 109867, 184 (2020)

## Publisher’s Note

Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.
