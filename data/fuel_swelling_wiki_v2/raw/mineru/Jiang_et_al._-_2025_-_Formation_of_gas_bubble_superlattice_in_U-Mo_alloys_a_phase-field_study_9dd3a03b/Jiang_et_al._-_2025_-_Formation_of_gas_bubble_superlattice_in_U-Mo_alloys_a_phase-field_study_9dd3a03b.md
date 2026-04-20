# 📄 PDF Parsing Result

**File:** `/Volumes/openclaw记忆/Zotero_storage/storage/RHPYCAFL/Jiang et al. - 2025 - Formation of gas bubble superlattice in U-Mo alloys a phase-field study.pdf`
**Backend:** `pipeline`
**Pages:** 0 to end
**Formula Recognition:** ❌ Disabled
**Table Recognition:** ✅ Enabled

---

# Formation of gas bubble superlattice in U-Mo alloys: A phase-field study☆

![](images/48bfe569a440966fffe498ca301379e9e31ab3ad36cbfc8edef220adf5431fb3.jpg)

Yanbo Jiang a , Shisen Gao a , Yongxiao La a , Wenbo Liu a,b,\*

a Department of Nuclear Science and Technology, Xi’an Jiaotong University, Xi’an 710049 China

b Shaanxi Key Laboratory of Advanced Nuclear Energy and Technology, Xi’an Jiaotong University, Xi’an 710049 China

## A R T I C L E I N F O

Keywords:   
Gas bubble superlattice   
Grain boundary   
U-Mo alloy   
Phase-field method

## A B S T R A C T

The impact of grain boundary (GB) on the formation and evolution of gas bubble superlattices (GBS) in U-Mo alloys under irradiation is critical for understanding the material behavior in nuclear environments. In this study, a phase-field model coupled Kim-Kim-Suzuki (KKS) model and explicit nucleation algorithm was developed to simulate GBS formation. The accumulation of vacancies and gas atoms led to bubble nucleation, with directional migration of interstitial atoms inducing a shadow effect and causing ordered bubble arrangements. The GBS exhibited stability, with bubble size and lattice constants remaining nearly constant at higher fission densities. The GB was shown to influence GBS formation significantly, with the surrounding region divided into a denuded zone and a peak zone. The width of the denuded zone is influenced by the GB properties. In this work, the relationship between the denuded zone width and the GB absorption strength was derived using a onedimensional steady-state vacancy diffusion equation. It was found that the denuded zone width increases with an increase in the GB absorption coefficient. The phase-field simulation results were consistent with theoretical predictions. These findings contribute to a better understanding of how GBs affect irradiation-induced microstructural changes in nuclear materials.

## 1. Introduction

The study of Uranium-Molybdenum (U-Mo) systems has gained significant attention due to their critical role in the development of advanced nuclear fuels. U-Mo alloys are widely considered promising candidates for high-performance nuclear reactors, (Snelgrove et al., 1997; Keiser et al., 2003), particularly in applications requiring highdensity fuels with excellent thermal conductivity, radiation tolerance, and dimensional stability (Kim and Hofman, 2011; Meyer et al., 2014; Van Den Berghe and Lemoine, 2014). Their use is especially relevant in research reactors, where enriched uranium fuels must meet strict performance and safety criteria while minimizing waste and proliferation risks. These demands have led to an increasing focus on understanding the microstructural evolution of U-Mo alloys under irradiation. However, the swelling due to fission gases of these metallic fuels has been found to be significantly more severe than that of mixed oxide fuels over time. Irradiation-induced swelling has emerged as a critical issue that must be addressed, primarily attributed to the nucleation and growth of fission gas bubbles produced during the fission process of uranium-235 (Ajantiwalay et al., 2020). The rate of production of gas atoms (Xe and

Kr) during fission far exceeds their solubility in the metallic fuel matrix. These gas atoms tend to diffuse and accumulate, leading to bubble formation. The presence of these bubbles can substantially alter the microstructure of the fuel, thereby compromising thermal conductivity and mechanical integrity. Consequently, a comprehensive understanding of the mechanisms governing the formation and evolution of irradiation-induced bubbles is essential, along with elucidating the impact on microstructural characteristics and irradiation conditions on bubble dynamics, in order to clarify the overall performance and safety of U-Mo fuels in high-power reactor applications.

The evolution of bubbles in U-Mo alloys is a highly complex process with the formation of gas bubble superlattices (GBS) observed during the early stages of irradiation. These superlattices, composed of orderly arranged bubbles, significantly influence the microstructural dynamics and swelling behavior of the fuel. Characterized by coherent arrangements within the U-Mo matrix, the bubble superlattices exhibit lattice parameters distinct from those of the underlying crystal structure. The diameters of the intragranular bubbles are approximately 1–3 nm, forming a superlattice with a fcc structure, while the bulk material displays a bcc structure. The lattice constants of these superlattices typically range from 7 to 12 nm (Gan et al., 2010; Van den Berghe et al., 2008; Miller et al., 2015). The mechanisms underlying the formation of GBS have been the subject of extensive research, with proposed explanations including the interactions between dislocation and cavity (Dubinko et al., 1986; Dubinko et al., 1989; Dubinko and Turkin, 1994), anisotropy of elastic constants (Stoneham, 1971; Willis, 1975; Yu and Lu, 2005), and anisotropic diffusion processes involving self-interstitial atom (SIA) (Woo and Frank, 1985; Walgraef et al., 1996; Heinisch and Singh, 2003; Evans, 2005; Hu et al., 2016). Given that the symmetry of the superlattices generally adheres to that of the primary lattice, onedimensional diffusion of SIAs is considered a promising primary cause of bubble superlattice formation. Therefore, investigating the onedimensional SIA diffusion and its interactions with microstructural features, such as grain boundary (GB), is crucial for understanding the formation and evolution of GBS.

In recent years, the formation of GBS in U-Mo alloys and their influencing factors have been extensively studied. However, due to the complexity of the physical mechanisms underlying bubble evolution and the fact that GBS only appear at low fission density, experimental investigation of the evolution of GBS structures is quite challenging. Numerical simulations, as an effective and cost-efficient research method, can provide guidance and theoretical support for experimental studies. The phase-field method, due to its capability to simulate the microstructural evolution of materials while accommodating multiphysics fields coupling, has been successfully applied in nuclear materials to investigate the nucleation and growth of void (Millett et al., 2009; Millett et al., 2011; Jiang et al., 2020; Rokkam et al., 2009), bubble evolution (Jiang et al., 2024; Jiang et al., 2022; Jiang et al., 2024; La et al., 2024; Millett et al., 2011; Lan et al., 2024); superlattice formation (Hu et al., 2016; Aagesen et al., 2021; Gao et al., 2018; Gao et al., 2022), thermal conductivity calculation (Bai et al., 2016; Liang et al., 2018; Lan et al., 2023; Jiang et al., 2025), and recrystallization (Jiang et al., 2025; Abdoelatef et al., 2019; Liang et al., 2017). Hu et al. developed a phase-field model combined with the Monte Carlo method to study the formation mechanisms of bubble superlattices (Hu et al., 2016). This model accounts for multiple physical processes and reveals that rapid one-dimensional migration of SIAs along the 〈1 1 0〉 direction in the body-centered cubic U matrix results in the alignment of bubbles along the same direction. This suggests that one-dimensional directional migration of SIA should be a primary mechanism for the observed GBS in U-Mo alloys. But the generation of fission gases is artificially suppressed to maintain a saturated concentration of xenon in their model. Aagesen et al. (Aagesen et al., 2021) derived a phase-field model from the largescale functional to simulate the formation of voids and bubble superlattices. Their model is capable of explaining the formation of superlattices through either nucleation and growth mechanisms or independent decomposition processes, quantifying the superlattice spacing as a function of model parameters. It was found that the superlattice spacing decreases with increasing flux of gas atoms, consistent with experimental observations. In our previous research (Jiang et al., 2024); the influence of GB absorption strength on bubble evolution was discussed. The absorption strength of defects by GBs is considered an inherent characteristic of GBs, independent of vacancy or gas atomic diffusion rate. The adsorption capacity of GBs significantly affects the width of the denuded zone and the distribution of defect concentration in the peak zone. Understanding this relationship is critical for elucidating the role of GBs in microstructural evolution and provides theoretical support for optimizing material performance.

In this work, a phase-field model coupled Kim-Kim-Suzuki (KKS) model and explicit nucleation algorithm was developed to simulate the formation of GBS in U-Mo alloys with 7 wt% Mo (U-7Mo). Initially, the GBS formation and evolution process in a single crystal was simulated, and the bubble diameter and lattice constant of the GBS were compared with experimental results. Next, a structure containing GB was constructed to investigate the effect of GB on GBS formation. The relationship between the denuded zone width and the GB absorption strength was quantitatively derived using a one-dimensional steadystate vacancy diffusion equation. Additionally, simulations were conducted by modifying the GB absorption coefficient, and the results were compared with the theoretical predictions to explore the impact of defect absorption intensity by GB on the denuded zone width.

## 2. Phase-field model

Considering the formation and development of bubble superlattices in U-Mo alloys, this section proposes a mesoscale phase-field model that couples bubble nucleation theory with self-interstitial atom (SIA) directional migration. This phase-field model of irradiation bubble evolution, known as the KKS model, is developed based on the formula proposed by Kim et al (Kim et al., 1999). In this model, it is assumed that the pure material is the matrix phase, and the chemical substances considered in the model are vacancies at lattice positions, SIAs from the matrix, and gas atoms assumed to be located at interstitial positions in the matrix. Therefore, the model will introduce vacancy concentration cv(r,t) and gas atomic concentration cg(r,t). Based on the assumption that one-dimensional anisotropic diffusion of different SIAs leads to the formation of bubble superlattices (Hu et al., 2016); SIA with two different diffusion directions are introduced into the current model, one diffusing faster in the (Dubinko et al., 1986) direction and the other diffusing faster in the [01] direction, with concentrations given by c1(r,t) and c2(r,t), respectively. In addition, the non-conserved order parameter η is used to distinguish the differences between the matrix phase and the bubble phase, which smoothly vary from 1.0 in the bubble phase to 0.0 in the matrix phase. Referring to the hypothesis in Aagesen et al.’s work (Aagesen et al., 2021), the bubble phase is composed of vacancies and gas atoms, resulting in cv + cg = 1.0 and ci = 0.0 in the bubble phase, where ci(r,t) represents all two types of SIA. In order to consider the influence of GBs on the formation and evolution of bubble superlattice, based on Chen et al.’s work (Chen and Wei, 1994), a series of order parameters ϕi(r,t) was introduced in the model to represent grains, where ϕi = 1.0 in the i-th grain.

## 2.1. Total free energy

In the current phase-field model, the evolution of bubbles and grains in U-Mo alloy needs to be considered. The total free energy of the system can be understood as the sum of distinct energy contributions. The chemical free energy density accounts for the energy associated with the chemical composition in the system. The polycrystalline energy density reflects the energy related to the grain boundaries and crystallographic structure. The double well potential represents the energy barrier of phase transition. The gradient energy density represents the energy density of interface. The total free energy is described as:

$$
\tag{1}
$$

where fchem indicates the chemical free energy density, fpoly indicates the polycrystalline energy density and fgrad indicates the gradient energy density, respectively. The double well function is shown as g(η) = η2 (1- η) 2 and W is the potential height.

As in Aagesen’work (Bai et al., 2016), the chemical free energy density is composed of the free energy density of the matrix phase and the bubble phase, which is shown as:

$$
\tag{2}
$$

where f m is the chemical free energy density in the matrix phase and f b is in the bubble phase. h(η) is an interpolating function with h(η) = η3 (6η2 -15η+10) that ensures the energy density changes smoothly between the bubble phase to matrix phase from h(1) = 1 to h(0) = 0.

Referring to the work of Aagesen et al. (Aagesen et al., 2022), the free energy density of the matrix phase and the bubble phase can be approximated by a parabola, while ensuring that the chemical potential of each conserved field variable in the parabolic approximation is the same as that in the ideal solution model. The chemical free energy density in the matrix of U-Mo alloy is written as:

$$
\tag{3}
$$

$$
\tag{4}
$$

where kvm, kgm, kim, kvb , kgb and kib are the parabola curvatures, cvm,eq, cgm,eq and cim,eq are the equilibrium concentration of vacancy, gas atom and SIA in the matrix phase, cvb,eq, cgb,eq and cib,eq are the equilibrium concentration in the bubble phase, respectively.

Following the work of Tonks et al. (Tonks et al., 2015), the polycrystalline energy density is described as:

$$
\tag{5}
$$

where μ is the constant of polycrystalline energy density. aGB and as are the parameter of diffuse surface. The parameter aGB related to GBs is taken the value of 1.5 which is set to ensure the symmetry of the diffusion interface. And the parameter ab related to the bubble surface is determined by as = aGBγsurf /γGB where γGB is the GB energy and γsurf is the surface energy (Jiang et al., 2024).

The gradient energy density is written as:

$$
\tag{6}
$$

where κη and κϕ are the gradient energy coefficient of bubble surface and GB, with dimensions of energy per unit length.

## 2.2. KKS model description

In the KKS model, the total defect concentration is considered to be composed of the defect concentration of each phase (Aagesen et al., 2021). To simplify the representation, cn (n = v,g,i) is used here to represent the concentration of all point defects, which is described as:

$$
\tag{7}
$$

In this expression, the total defect concentration is linked to the defect concentration in each phase through an interpolation function. Furthermore, based on the assumption of thermodynamic equilibrium in the KKS model, the assumption that the chemical potentials of each component in the matrix phase and bubble phase are the same is applied, which is expressed by the following formula:

$$
\tag{8}
$$

where μn (n = v,g,i) represents the total chemical potential of each point defect concentration. The Newton-Raphson method is used to numerically solve Eqs. (7–8) to obtain the local defect concentrations in different phases and in each phase-field calculation step.

When applied at larger simulation scales, The KKS model has great advantages as it decouples the relationship between diffusion interface width and interfacial energy, making the phase-field parameters of the diffusion interface directly related to actual physical parameters. Referring to the work of Hu et al. (Hu et al., 2007), the height of the gradient energy coefficient kappa κη and the double well potential W are related to the surface energy γs and interface thickness 2λ of the material, as expressed below:

$$
\tag{9}
$$

$$
\tag{10}
$$

where the interface thickness 2λ = 10 nm was selected based on numerical stability considerations and the requirement to accurately capture the interface effects. The value of κη and W can be calculated by Eqs. (9–10) to be κη = 2.45 × 10-8 J/m and W = 2.38 × 109 J/m3 . In addition, the phase-field parameters of GBs are also directly related to physical parameters, which is expressed as (Moelans et al., 2008):

$$
\tag{11}
$$

$$
\tag{12}
$$

where the GB thickness lGB was chosen to be 10 nm, and the value of κϕ and μ can be determined by Eqs. (11–12) to be κϕ = 3.75 × 10-9 J/m and μ = 3.00 × 108 J/m3 .

## 2.3. Evolution equations

A series of modified Cahn-Hilliard equations (Cahn, 1961) are employed to describe the spatial and temporal evolution of the concentrations of vacancy, gas atom and two types of SIAs, which are written as:

$$
\tag{13}
$$

$$
\tag{14}
$$

$$
\tag{15}
$$

$$
\tag{16}
$$

where Mv = Dv/kBT and Mg = Dg/kBT are the mobilities of vacancy and gas atom which are related to the diffusivity. D1 and D2 are the diffusion coefficients of two types of SIAs, respectively. According to the assumption of Aagesen (Aagesen et al., 2022), The diffusivities of the two SIAs with unit of nm2 /s are anisotropic and taken the tensorial form as:

$$
\tag{17}
$$

$$
\tag{18}
$$

Pv is the production rate of vacancies in the solid matrix. Referring to the phase-field model proposed by Liang et al (Liang et al., 2018). in irradiated U-Mo alloy, the vacancy production rate in the fuel can be related to the fission rate according to Pv = fr/δ, where fr is the fission rate and δ is a constant with a value of 5.12 × 102 in this work. In cascade collisions, the number of vacancies is equal to the number of SIAs generated by Frankel pairs. Therefore, assuming that collision cascades generate SIA species 1 and 2 with equal probability, their total generation rate must be equal to the total vacancy generation rate P1=P2= Pv/2. The generation rate of gas atom is expressed as Pg=(1- η) 2 ΛΩfr (Liang et al., 2018), where Ω is the volume of the U-Mo lattice and Λ is a constant. When SIAs and vacancies meet, they recombine and form a perfect lattice. Kvi is the rate of vacancy–interstitial recombination. Due to the unique properties of GBs, they serve as effective absorption traps for many atomic defects. Vacancies and SIAs near GBs can be permanently captured. Therefore, the absorption term for GBs needs to be added to the model and described as (Millett et al., 2009): S = s (1- Φ), S1 = s1(1-Φ), S2 = s2(1-Φ), where sv, s1 and s2 are the constant representing the strength of the vacancy and SIAs absorbed by GBs. An assumption is adopted that the absorption capacity of GB for SIA and vacancy is the same, with sv = s1 = s2. Φ takes the form Φ = (ϕi) 2 , that ensures Φ = 1.0 in the grain interior and Φ < 1.0 at the GBs.

All order parameters evolves by Allen-Cahn equations as (Cahn and Allen, 1977):

$$
\tag{19}
$$

$$
\tag{20}
$$

where Lη and Lϕ are the mobility of bubble surface and GB. A nondimensional grid spacing (x = l/l\*), time step (τ = t/t\*) are applied to numerical solution of the evolution equations. The reference length scale is l\* = 0.8 nm and time scale is t\* = 0.1 s during numerical implementation, and the grid size is x = 0.5, time step is τ = 0.01. In addition, under periodic boundary conditions, the forward Euler method in time and the finite difference method in space are applied to solve the Cahn Hilliard equation and Allen Cahn equation. The temperature selected for this simulation is 473 K, which is based on the typical operating conditions of uranium molybdenum fuel in nuclear reactors. Research within this temperature range is crucial for evaluating fuel performance. In addition, the parameters used in our analysis were derived from the work of Liang et al. (Liang et al., 2018), which employed the same simulated temperature.

## 2.4. Nucleation model

The nucleation process of irradiation-induced bubbles begins with the introduction of gas atoms and defects, such as vacancies generated during irradiation. Gas atoms diffuse through the material and are attracted to vacancies, forming gas-vacancy complexes that act as initial clusters. As these clusters grow, they may reach a subcritical nucleus state, which is thermodynamically unstable and must overcome a nucleation energy barrier to grow into stable bubbles. This barrier depends on factors like defect densities and microstructural features, such as GBs. Once the critical size is reached, the nucleus becomes stable, and the bubble grows by absorbing additional gas atoms and vacancies (Simmons et al., 2000). In present phase-field method, an explicit nucleation method is applied to introduce the discrete kernel of new bubble. Referring to the nucleation method in U-Mo alloy mentioned by Liang et al. (Liang et al., 2018); the nucleation probability of discrete regions as a function of simplified local nucleation probability can be calculated as:

$$
\tag{21}
$$

where k1 and k2 are the nucleation factors, and Δcv is the local supersaturation (Simmons et al., 2000).

In a discretized zone, the overall nucleation probability is shown as:

$$
\tag{22}
$$

where Δt is the time interval of the nucleation probability calculation. Calculate the nucleation probability of each supersaturated region with spatial features at each simulation time interval Δt, and perform the nucleation step. After calculating the probability, the location of nucleation can be determined. In addition, it is necessary to introduce a depletion zone of defects when introducing bubble cores to ensure concentration conservation. Specifically, the geometric shape of the bubble core is chosen to approximate the circular shape in a discrete lattice. The depletion zone around the nucleus is selected to have a width of approximately half its diameter. The depletion zone reduces the required number of components to provide the additional solute needed to form the bubble phase in the nucleus (Cahn, 1961). It is worth noting that the nucleation probability in the bubble is set to zero. Therefore, when calculating the nucleation probability, the nucleation probability of the formed bubbles and their depletion regions is almost zero, thus avoiding bubble overlap. All parameters of U-Mo alloy used in the present simulation are shown in Table 1.

## 3. Results

In this section, the formation and evolution of GBS in U-Mo alloy are discussed by the phase-field model proposed previously. In materials, interstitial atoms are those located in the gaps between the lattice sites. They do not occupy the normal lattice positions but instead occupy the void regions. The diffusion of these interstitial atoms is typically not random but rather directional, and it is considered to be the primary cause of GBS. Specifically, the formation of GBS can be explained by the shadow effect. The shadow effect refers to the phenomenon where, as interstitial atoms diffuse in a certain direction, existing bubbles block part of the migration path of the interstitial atoms, leading to the formation of depleted regions (i.e., regions with lower concentrations of interstitial atoms) in the areas obstructed by the bubbles. On the other hand, the regions not obstructed by the bubbles will form saturated regions (i.e., regions with higher concentrations of interstitial atoms). Therefore, the presence of bubbles affects the directional diffusion of interstitial atoms, intensifying the concentration differences of interstitial atoms across different regions. Due to the existence of different diffusion paths for interstitial atoms in the directional diffusion process, these atoms will form depleted regions in some areas and saturated regions in others. The bubble-blocking effect causes the interstitial depleted regions to appear periodically in different locations, leading to an alternating arrangement of depleted and saturated regions, as shown in Fig. 1, where red represents the bubbles and blue represents the depleted regions caused by the blocking of diffusion. This alternating arrangement itself has a certain periodicity, and the nucleation and growth of bubbles are more likely to occur in the depleted regions because these areas have fewer interstitial atoms, requiring less energy for bubble formation. As the bubbles continue to form and grow, they arrange according to the periodic distribution of the interstitial depleted regions. During the evolution process, bubbles such as those shown in areas B, C and D in Fig. 1 may appear outside of the lattice positions. However, influenced by the interstitial saturated regions, these bubbles will shrink over time as they absorb interstitial atoms, causing all the bubbles to become regular, similar to the one shown in position A. This process ultimately results in the formation of a bubble superlattice structure.

Parameters of U-Mo alloy used in the present phase-field simulation.
<table><tr><td>Physics parameter</td><td>Symbol</td><td>Value</td><td>Reference</td></tr><tr><td>Temperature</td><td>T</td><td>473K</td><td></td></tr><tr><td>Parabolic factor of matrix</td><td>k=k</td><td>6.00×1011 J/m</td><td>(Aagesen et al., 2022)</td></tr><tr><td>Parabolic factor of matrix</td><td>k</td><td>1.20 ×1011 J/m</td><td>(Aagesen et al., 2022)</td></tr><tr><td>Parabolic factorof bubble</td><td>k</td><td>1.20 ×101° J/m</td><td>(Aagesen et al., 2022)</td></tr><tr><td>Parabolic factor of bubble</td><td>K</td><td>2.40×1010 J/m</td><td>(Aagesen et al., 2022)</td></tr><tr><td>Parabolic factorof bubble</td><td>k</td><td>6.00 ×1011 J/m</td><td>(Aagesen et al., 2022)</td></tr><tr><td>Surface energy</td><td>Ys</td><td>1.81 J/m²</td><td>(Liang et al., 2018)</td></tr><tr><td>GB energy Diffusion coefficient of</td><td>YGB</td><td>0.5J/m²</td><td>(Hu et al., 2015)</td></tr><tr><td>vacancy</td><td>Dv</td><td>4.10 ×1017 m²/ S</td><td>(Liang et al., 2018)</td></tr><tr><td>Diffusion coefficient of gas atom</td><td>Dg</td><td>3.84×1017m²/ S</td><td>(Rest, 2010)</td></tr><tr><td>Constant of gas atom generation</td><td>A</td><td>0.25</td><td>(Spino et al., 2005)</td></tr><tr><td>Mobility of bubble surface</td><td>Ln</td><td>9.04×10m/ J/s</td><td>(Liang et al., 2018)</td></tr><tr><td>Mobility of GB</td><td>L</td><td>1.82 ×1014m/ J/s</td><td>(Liang et al., 2016)</td></tr><tr><td>Nucleation factor</td><td>k1</td><td>1×103</td><td>(Liang et al., 2018)</td></tr><tr><td>Nucleation factor</td><td>k2</td><td>1×10-5</td><td>(Liang et al., 2018)</td></tr></table>

![](images/cb115d4c0e82fa47befa5e7bfe5e4835f3ea94ebd8e809f8094c6bc77ea5f2ad.jpg)  
Fig. 1. Schematic diagram of shadow effect in GBS formation. A: Bubbles located on the superlattice sites. B: Bubbles not located on the superlattice sites. C: Small bubbles located in the shaded regions. D: Oversized bubbles located on the lattice sites.

In the present study, a 102.4 × 102.4 nm two-dimensional region was utilized to simulate the formation of GBS in U-Mo alloys. The initial defect concentration was set to the thermal equilibrium concentration. The formation of GBS in U-Mo is depicted in Fig. 2, corresponding to the fission densities of (a) 1, (b) 2, (c) 3, (d) 4, (e) 5 and (f) 6 × 1021 fiss/cm3 . The fluence values were chosen to represent the typical conditions under which gas bubble superlattice occurs (Aagesen et al., 2022; Liang et al., 2018). In the initial stages of irradiation, gas atoms, vacancies, and interstitial atoms were introduced into the system. As defects accumulated, bubbles began to nucleate. The nucleation of bubbles was modeled based on the nucleation model developed in the previous section. The probability of bubble nucleation was found to be related to the vacancy concentration, with the nucleation probability increasing as vacancies accumulated. At a fission density of 1 × 1021 fiss/cm3 , bubbles began to nucleate, although their size was very small at this stage. As defects continued to be introduced, existing bubbles absorbed vacancies and gas atoms, causing them to grow. Simultaneously, bubbles also shrank by absorbing interstitial atoms. At a fission density of 3 × 1021 fiss/cm3 , bubbles started to align and form a superlattice structure. At this point, due to the shadow effect, periodically arranged interstitial depleted regions were formed, leading to the periodic alignment of bubbles, which is consistent with experimental observations (Miller et al., 2015). However, irradiation-induced bubbles were also observed at non-lattice positions during this stage. This is because the difference between interstitial depleted and saturated regions was minimal at the early stages of irradiation, resulting in a nearly uniform nucleation probability across all lattice sites. As the fission density increased, the influence of bubbles on interstitial diffusion became more pronounced, amplifying the difference between the depleted and saturated regions. Bubbles located in the saturated regions shrank due to interstitial absorption, while bubbles in the depleted regions remained stable. After a fission density of 4 × 1021 fiss/cm3 , the GBS structure remained stable, with bubbles no longer changing significantly with further increases in fission density.

The GB plays a crucial role in the formation of GBS. Literature review

![](images/e2a5d52ed51fde316f0085d905bb7dd0fae5e732179e8d251ab860378ed05ca9.jpg)

Fig. 2. The morphology of the GBS for (a) 1, (b) 2, (c) 3, (d) 4, (e) 5 and (f) 6 × 1021 fiss/cm3.

indicates that during irradiation near GBs voids are formed early and the fission gases generated in these regions migrate to the intergranular bubbles, partially filling the developing voids (Ajantiwalay et al., 2020). During irradiation, the regions surrounding the GB can be divided into three distinct zones, as shown in Fig. 3. The first is the denuded zone, where the concentration of vacancies and interstitial atoms decreases to zero due to the GB’s absorption of these defects. The second is the peak zone, where the anisotropic migration of interstitial atoms occurs more rapidly than the isotropic diffusion of vacancies. As a result, interstitial atoms are more strongly influenced by the GB absorption. In this zone, a region with a significantly higher ratio of vacancies to interstitials compared to other parts of the grain is observed. Voids nucleate and grow most intensely in this peak zone (Millett et al., 2011) reaching high expansion values in the early stages of irradiation (Evans and Foreman, 1985), and GBS forms within this region. Moving inward towards the grain, the third zone is characterized by a reduced vacancy-to-interstitial ratio.

A bicrystal structure was constructed to investigate the influence of GB on the formation of GBS, as shown in Fig. 4, where the white region represents the GB. For simulation size considerations, a grid size of 204.8 × 204.8 nm was used in subsequent simulations. Due to the absorption of defects by the GB, the formation process of GBS is illustrated in Fig. 4, corresponding to the fission densities of (a) 1, (b) 2, (c) 3, (d) 4, (e) 5 and (f) 6 × 1021 fiss/cm3 . It can be observed that a denuded zone and a peak zone appear around the GB influenced by the GB. In the denuded zone, the defect concentration is zero, while in the peak zone, the defect concentration increases with the increase in fission density, leading to the nucleation and growth of bubbles. At a fission density of 3 × 1021 fiss/cm3 , bubbles begin to show a tendency to form a lattice arrangement. As the fission density increases, the bubble lattice in the GB peak zone stabilizes and persists.

The width of the denuded zone is an important characteristic influenced by the GB. It is well known that factors such as irradiation dose, temperature, dose rate (Konobeev et al., 1975), as well as the type and orientation of the GB (Han et al., 2012), can affect the width of this zone. Theoretically, as the GB’s absorption of defects increases, the width of the denuded zone should also increase. Therefore, simulations were conducted using GBs with different absorption coefficients to study the formation of GBS, as shown in Fig. 5, where the corresponding fission density is 6 × 1021 fiss/cm3 and the GB absorption coefficient are (a) sv = 0.04, (b) sv = 0.06 and (c) sv = 0.08. From the figures, it can be observed that, with the increase in the GB absorption, the location of

![](images/4dba9439f62b70b1a36011ff173a1f2e9956101586babda66d5f62273534ddb7.jpg)

![](images/634434a333a7bb85972aaa862228e95ea1451dad284f03e62f669cd9be312a26.jpg)  
Bubble Superlattice (\~50nm)

![](images/2630c6dab80ed804e8b9143ba0e5ff0faf3effe061e81e785245845928ddc153.jpg)  
Grain interior

Fig. 3. Schematic diagram of GBS formation around GBs.

bubble formation shifts further away from the GB.

## 4. Discussion

## 4.1. Model validation

In the previous section, a phase-field model was developed to simulate the formation of GBS in U-Mo alloys, as shown in Fig. 6. Further, it was necessary to conduct a quantitative analysis of the simulation results to validate the proposed model. Therefore, the bubble diameter and lattice constant measured in experiments on GBS were used for model validation. In our simulations, bubble sizes were determined using the connected region labeling method, and lattice constant was measured by calculating the distance between the bubbles. The 4- point connected region labeling method works by identifying and labeling distinct regions of connected elements within a grid or lattice. In this method, a point is classified as part of a connected region if it shares at least one edge or corner with another point in the region. For 2D grids, a point can be connected to its four neighbors, which are examined in succession. If a point belongs to a previously identified region, it is labeled accordingly. Otherwise, a new label is assigned. This method is particularly useful for determining the size of clusters, such as bubbles in the simulation, by counting the number of points within each labeled region.

The average bubble diameter as a function of fission density was plotted in Fig. 6, as indicated by the red points. It can be seen that as bubble nucleation and growth occur, the bubble radius increases. The growth of bubbles can be attributed to the accumulation of vacancies and gas atoms, which are incorporated into existing bubbles, leading to their enlargement. At a fission density of 1 × 1021 fiss/cm3 , the bubble diameter is approximately 1.3 nm. As the fission density increases, the bubble diameter stabilizes after 3 × 1021 fiss/cm3 . The bubble diameters measured experimentally at different fission densities were also plotted in Fig. 6. To evaluate the agreement between the simulation results and the experimental data, RMSE (Root Mean Square Error) was calculated. Since the x-coordinates (fission density) of the simulation and experimental data do not match exactly, interpolation was applied to align them to the same x-coordinates before performing the calculation.

RMSE = ∑ni=1 ( ysim,i − yʹexp,i )2 /n , where ysim is the simulation data and y’exp is the interpolated experimental data. The RMSE was calculated to be 0.276, indicating a good agreement between the simulation and experimental results (Van den Berghe et al., 2008; Miller et al., 2015; Leenaers et al., 2016; Gan et al., 2014). As bubbles continue to absorb defects, their growth rate slows down. Due to the shadow effect, a large number of interstitial atoms diffuse within the GBS, which reduces the number of vacancies available for bubble absorption, thereby limiting further growth. Consequently, after reaching a certain fission density, the bubbles in the superlattice structure stabilize, and their size remains constant.

The lattice constant is also an important characteristic of GBS. Fig. 7 shows the variation of the lattice constant with fission density. In the early stages of irradiation, no lattice constant can be measured without GBS. The lattice constants measured experimentally at different fission densities are also plotted in Fig. 7, and The RMSE was calculated to be 0.302 shown a good agreement between the simulation and experimental data (Van den Berghe et al., 2008; Miller et al., 2015; Leenaers et al., 2016; Gan et al., 2014). The lattice constant decreases slightly as fission density increases, which may be related to the growth of bubbles. However, the relationship between the lattice constant and fission density appears to be minimal overall. According to previous reports, the gas appm/dpa ratio may be the decisive factor in determining the lattice constant. Harrison et al. (Harrison et al., 2017) emphasized the importance of the He appm/dpa ratio as a descriptor for bubble lattice formation. In their study on bubble lattice formation in tungsten under

Fig. 4. The morphology of the GBS with a GB for (a) 1, (b) 2, (c) 3, (d) 4, (e) 5 and (f) 6 × 1021 fiss/cm3.

![](images/e1ea6a7a6b72594a6a19851e2325a7222b01f6a27bfb49aa080574d8584057a2.jpg)

Fig. 5. The morphology of the GBS with a GB under 6 × 1021 fiss/cm3 for (a) sv = 0.04, (b) sv = 0.06 and (c) sv = 0.08.

He implantation at a temperature of approximately 0.2 Tm, the authors used different He energies to achieve an He appm/dpa ratio ranging from 500 to 40000. The bubble lattice adapted to different implantation conditions, and as the He appm/dpa ratio decreased, both the bubble diameter and lattice constant increased. As a result, the lattice constant remains relatively unchanged even at higher fission densities, since the gas appm/dpa ratio governs how bubbles form and influence the material microstructure. This suggests that the lattice constant is primarily determined by the gas appm/dpa ratio overshadowing the direct effects of fission density on the lattice constant.

## 4.2. The effect of GB

GBs play a significant role in the formation of GBS, and the underlying mechanisms can be attributed to their ability to absorb and influence the distribution of defects. To study the impact of GBs on GBS formation, a system containing GBs was constructed as shown in Fig. 4. With increasing fission density, bubbles were observed to form progressively on both sides of the GB and align into a superlattice arrangement under the influence of the directionally diffusing interstitial atoms. Throughout this process, the bubble size increased gradually until reaching a stable state, which was consistent with the GBS formation process observed in systems without GB. The average bubble diameter as a function of fission density is shown as red dots in Fig. 8. During the early stages of irradiation, the bubble size increased rapidly. However, when the fission density exceeded 3 × 1021 fiss/cm3 , the bubble size exhibited minimal further growth. This stabilization can be explained by the decreasing availability of defects, particularly vacancies, as discussed previously. The fitted curve, shown as a solid black line in Fig. 8, follows the equation y = 3.82–5.79 × exp(− x/1.32). The fitting results indicate that the bubble diameter in the GBS near the GB reaches a maximum value 3.82 nm, beyond which it approaches this limit with increasing fission density. The simulation results align well with the fitting curve, providing further validation of the model and the observed trends. It is worth noting that although both Fig. 6 and Fig. 8 show the variation of bubble diameter with fission density in GBS, Fig. 6 shows the simulation results of a single crystal without GBs, while Fig. 8 reflects the influence of GBs on the system. The presence of GB inhibits the growth of bubbles, resulting in smaller bubble diameters in Fig. 8 compared to Fig. 6, with a difference of approximately 0.5 nm at the same fission density.

![](images/27f19c402fe8b9b8dcfd174014ec21bb0cd301001090062f4efd0e0c47066a31.jpg)  
Fig. 6. The variation of bubble diameter with fission density and comparison with experimental data.

![](images/1ad7b23c3c271e6fb7e1e4e94b8d0fe56c489eb66c41a6fccd8bae283ef085bf.jpg)  
Fig. 7. The variation of lattice parameter with fission density and comparison with experimental data.

The existence of the denuded zone arises from the fact that the vacancy concentration is lower directly adjacent to the GBs, due to the annihilation of excess vacancies within the GB. This phenomenon is a direct result of the vacancy absorption by the GB, where they are effectively removed from the bulk region. In the bulk region, as the supersaturation of vacancies continually increases over time due to the irradiation source term, voids begin to nucleate once a critical vacancy concentration is reached. The width of the denuded zone can therefore be defined as the region adjacent to the GB where the vacancy concentration does not exceed the critical nucleation threshold. This critical concentration is essential for void formation, as it dictates the point at which voids begin to nucleate and grow. To account for this phenomenon in a model, the one-dimensional steady-state diffusion equation is employed within GB. Considering the equilibrium of vacancy diffusion, generation and annihilation processes within GB, this equation can be described as:

![](images/0519f69262a678867da0a76ac0fe28c61345651e2bb1ea40b04ec4085f6a8fce.jpg)  
Fig. 8. Simulation results and fitting line of bubble diameter variation with fission density.

$$
\tag{23}
$$

where x is the distance from the middle of GB to the semi-infinite solid. sv/2 is approximately equal to Sv in the GB. Using the boundary conditions cv = cveq (x = 0) and dcv/dx = 0 (x = 0), the functional solution of vacancy concentration with x can be written as:

$$
\tag{24}
$$

As a result, the vacancy concentration at the boundary of the GB at position λ can be calculated as cGB. The region adjacent to GB that does not exceed the critical vacancy concentration can be defined as a denuded zone. The behavior of vacancies in this region can be considered using a one-dimensional steady-state diffusion equation as follows (Millett et al., 2009):

$$
\tag{25}
$$

Appling the boundary conditions cv = cGB (x = 0) and dcv/dx = 0 (x = W ), the vacancy concentration as a function of x can be obtained:

$$
\tag{26}
$$

where Wdz is the width of the denuded zone, and λ is the half width of GB. Assuming that the vacancy concentration at the edge of the denuded zone is the critical saturation concentration ccr, such that:

$$
\tag{27}
$$

After simplifying:

$$
\tag{28}
$$

The relationship between the width of denuded zone and absorption coefficient sv can be obtained. From the formula, it can be seen that sv has a minimum value for the occurrence of denuded zones, and only when the GB absorption coefficient is greater than this value will the denuded zone appear. Assuming that the critical supersaturation concentration of vacancies is 0.01, the one-dimensional vacancy distribution perpendicular to the GB direction for different GB absorption coefficients sv is shown in Fig. 9. It can be observed that within the GB, the vacancy concentration increases toward the GB edge. Additionally, the vacancy concentration at the GB edge increases as s increases. This is because vacancies within the GB tend to diffuse toward the GB edge to maintain equilibrium with a higher GB absorption strength. Further, in the direction from the GB edge towards the interior of the grain, the vacancy concentration decreases continuously until it reaches the critical supersaturation concentration. At this point, the derivative of the vacancy concentration with respect to position becomes zero, indicating a steady-state condition. The distance from the GB edge to this point is considered the width of the denuded zone. As shown in the figure, the width of the denuded zone also increases as the absorption coefficient sv increases.

According to Eq. (28), the denuded zone width as a function of the GB absorption coefficient sv can be quantitatively calculated, as shown by the black solid line in Fig. 10. It can be observed that the denuded zone width increases with increasing sv, which is attributed to the enhanced absorption of defects by the GB. However, as s continues to increase, the rate of increase in denuded zone width diminishes, suggesting the possible existence of a limit to the vacancy denuded zone. The formation of GBS around the GB was simulated using the developed phase-field model with varying sv values, as shown in Fig. 5. The simulation results indicate that the denuded zone width around the GB increases with increasing s . By statistically analyzing the distance of bubbles from the GB, the denuded zone width under steady-state conditions was obtained as a function of sv, represented by the blue dots in Fig. 10. The simulation results show good agreement with the calculated values.

Additionally, the effect of the GB absorption coefficient on bubble diameter is shown by the red dashed line in Fig. 10, where the average bubble diameter is plotted for different s values when the GBS reaches stability at a fission density of 6 × 1021 fiss/cm3 . It can be observed that as sv increases, the bubble diameter also increases. This can likely be attributed to the stronger vacancy segregation near the GB at higher sv, which leads to a higher supersaturation of vacancies. However, the bubble diameter stabilizes with further increases in s . This stabilization can be explained by the saturation of vacancy supersaturation levels, which limits further growth of bubbles. It is worth mentioning that simply modeling GB as vacancy absorption sink is an idealized approach, mainly to reduce model complexity and focus on the core mechanism of research. Future work aims to further explore the relationship between the GB absorption coefficient and GB properties. Such an investigation could bridge the gap between lower-scale simulations and practical engineering applications by enabling predictions of GBS formation around specific GBs based on their properties. By understanding and quantifying how GB characteristics influence the absorption and evolution of gas bubbles, this research has the potential to translate atomistic and mesoscale findings into actionable insights for the design and optimization of materials in irradiation environments.

![](images/fe960f3163db093eaef8b6da4a2efdd83e1047ad26d4aebdf99b5fcb90ef028a.jpg)  
Fig. 9. One-dimensional vacancy distribution perpendicular to the GB direction for different GB absorption coefficients sv.

![](images/6dd389ceae50151ba425c41c3068c596ece1de88db7f864a52502eda0919279d.jpg)  
Fig. 10. The variation of denuded zone width and bubble diameter with GB absorption coefficient sv.

## 5. Conclusions

A coupled KKS model and an explicit nucleation algorithm were successfully implemented in a phase-field model to simulate the formation of GBS in U-Mo alloys. Additionally, the impact of the GB absorption strength on the denuded zone width was systematically investigated. The primary conclusions are summarized as follows:

(1) The developed phase-field model was applied to simulate the formation and evolution of GBS in U-Mo alloys. With increasing fission density, vacancies and gas atoms were observed to accumulate in the matrix, leading to the bubble formation. The shadow effect caused by the one-dimensional directional migration of interstitial atoms resulted in the ordered arrangement of bubbles in the matrix. The formed GBS exhibited irradiationinduced stability, as further increases in fission density led to minimal changes in bubble radius and lattice constant. The simulated bubble diameters and lattice constants were in good agreement with experimental measurements.

(2) GBs were found to play a significant role in the formation and evolution of GBS. A structure containing a GB was constructed, and the validated model was employed to study the influence of the GB on GBS formation. Simulation results indicated that regions near the GB could be divided into distinct zones during irradiation. The first zone was the denuded zone, characterized by defect depletion. The second was the peak zone, where GBS primarily formed. During the formation process, bubble diameters initially increased but later stabilized in the vicinity of the GB.

(3) The absorption strength of GB for defects was shown to influence the width of the denuded zone. A quantitative relationship between the GB absorption coefficient sv and the denuded zone width was obtained through a one-dimensional steady-state diffusion equation. It was found that the denuded zone width increased with higher absorption strength, due to enhanced vacancy absorption at the GB which drives defect migration to maintain equilibrium. Simulations incorporating varying sv values were conducted, and the results were consistent with the calculations. As the GB absorption strength increased, bubble diameters within the surrounding GBS initially increased but eventually saturated.

## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Acknowledgements

This work was supported by the Joint Fund of the National Natural Science Foundation of China and the China Academy of Engineering Physics (NSAF Joint Fund) (Grants No. U2130105) and the Innovative Scientific Program of China National Nuclear Corporation (CNNC).

## Data availability

Data will be made available on request.

## References

Snelgrove, J.L., Hofman, G.L., Meyer, M.K., 1997. Development of very-high-density lowenriched-uranium fuels. Nucl. Eng. Des. 178, 119–126. https://doi.org/10.1016/ S0029-5493(97)00217-3.

Keiser, D.D., Hayes, S.L., Meyer, M.K., 2003. High-density, low-enriched uranium fuel for nuclear research reactors. Metals Mater. Soc. 55, 55–58. https://doi.org/10.1007/ s11837-003-0031-0.

Kim, Y.S., Hofman, G.L., 2011. Fission product induced swelling of U–Mo alloy fuel. J. Nucl. Mater. 419, 291–301. https://doi.org/10.1016/j.jnucmat.2011.08.018.

Meyer, M.K., Gan, J., Jue, J.F., 2014. Irradiation performance of U-Mo monolithic fuel. Nucl. Eng. Technol. 46, 169–182. https://doi.org/10.5516/NET.07.2014.706.

Van Den Berghe, S., Lemoine, P., 2014. Review of 15 years of high-density low-enriched UMo dispersion fuel development for research reactors in Europe. Nucl. Eng. Technol. 46, 125–146. https://doi.org/10.5516/NET.07.2014.703.

Ajantiwalay, T., Smith, C., Keiser, D.D., 2020. A critical review of the microstructure of U-Mo fuels. J. Nucl. Mater. 540, 152386. https://doi.org/10.1016/j. jnucmat.2020.152386.

Gan, J., Keiser, D.D., Wachs, D.M., 2010. Transmission electron microscopy characterization of irradiated U-7Mo/Al-2Si dispersion fuel. J. Nucl. Mater. 396 (2–3), 234–239.

Van den Berghe, S., Van Renterghem, W., Leenaers, A., 2008. Transmission electronmicroscopy investigation of irradiated U-7 wt% Mo dispersion fuel. J. Nucl. Mater. 375, 340–346. https://doi.org/10.1016/j.jnucmat.2007.12.006.

Miller, B.D., Gan, J., Keiser Jr., D.D., 2015. Transmission electron microscopy characterization of the fission gas bubble superlattice in irradiated U-7 wt%Mo dispersion fuels. J. Nucl. Mater. 458, 115–121. https://doi.org/10.1016/j. jnucmat.2014.12.012.

Dubinko, V.I., Slezov, V.V., Tur, A.V., 1986. The theory of gas bubble lattice. Radiat. Eff. Defects Solids 100 (1–2), 85–104. https://doi.org/10.1080/00337578608208738.

Dubinko, V.I., Tur, A.V., Turkin, A.A., 1989. A mechanism of formation and properties of the void lattice in metals under irradiation. J. Nucl. Mater. 161 (1), 57–71. https:// doi.org/10.1016/0022-3115(89)90462-5.

Dubinko, V.I., Turkin, A.A., 1994. Self-organization of cavities under irradiation. Appl. Phys. A 58 (1), 21–34. https://doi.org/10.1007/BF00331513.

Stoneham, A.M., 1971. Theory of regular arrays of defects - Void lattice. J. Phys. F. 1 (6), 778–784. https://doi.org/10.1088/0305-4608/1/6/311.

Willis, J.R., 1975. Interaction of gas-bubbles in an anisotropic elastic solid. J. Mech. Phys. Solids 23 (2), 129–138. https://doi.org/10.1016/0022-5096(75)90022-8.

Yu, H.C., Lu, W., 2005. Dynamics of the self-assembly of nanovoids and nanobubbles in solids. Acta Mater. 53 (6), 1799–1807. https://doi.org/10.1016/j. actamat.2004.12.029.

Woo, C.H., Frank, W., 1985. A theory of void-lattice formation. J. Nucl. Mater. 137 (1), 7–21. https://doi.org/10.1016/0022-3115(85)90044-3.

Walgraef, D., Lauzeral, J., Ghoniem, N.M., 1996. Theory and numerical simulations of defect ordering in irradiated materials. PhysRevB 53 (22), 14782–14794. https:// doi.org/10.1103/PhysRevB.53.14782.

Heinisch, H.L., Singh, B.N., 2003. Kinetic Monte Carlo simulations of void lattice formation during irradiation. Phil. Mag. 83 (31–34), 3661–3676. https://doi.org/ 10.1080/14786430310001605416.

Evans, J.H., 2005. Simulations of the effects of 1-D interstitial diffusion on void lattice formation during irradiation. Phil. Mag. 85 (11), 1177–1190. https://doi.org/ 10.1080/14786430512331325606.

Hu, S.Y., Burkes, D.E., Lavender, C.A., Senor, D.J., Setyawan, W., Xu, Z.J., 2016. Formation mechanism of gas bubble superlattice in UMo metal fuels: phase-field modeling investigation. J. Nucl. Mater. 479, 202–215.

Millett, P.C., El-Azab, A., Rokkam, S., 2009. Void nucleation and growth in irradiated polycrystalline metals: a phase-field model. Modelling Simul. Mater. Sci. Eng. 17, 064003. https://doi.org/10.1088/0965-0393/17/6/064003.

Millett, P.C., El-Azab, A., Rokkam, S., 2011. Phase-field simulation of irradiated metals: Part I: Void kinetics. Comput. Mater. Sci. 50, 949–959. https://doi.org/10.1016/j. commatsci.2010.10.034.

Jiang, Y.B., Liu, W.B., Li, W.J., 2020. Phase-field simulation of the interaction between intergranular voids and grain boundaries during radiation in UO2. Comput. Mater. Sci., 110176 https://doi.org/10.1016/j.commatsci.2020.110176.

Rokkam, S., El-Azab, A., Millett, P., 2009. Phase field modeling of void nucleation and growth in irradiated metals. Modelling Simul. Mater. Sci. Eng. 17 (6), 064002. https://doi.org/10.1088/0965-0393/17/6/064002.

Jiang, Y.B., Sun, Z., Wang, D., 2024. Effects of grain boundaries on the evolution of radiation-induced bubbles in polycrystalline tungsten: a phase-field simulation. J. Nucl. Mater. 588, 154757. https://doi.org/10.1016/j.jnucmat.2023.154757.

Jiang, Y.B., Xin, Y., Liu, W.B., 2022. Phase-field simulation of radiation-induced bubble evolution in recrystallized U-Mo alloy. Nucl. Eng. Technol. 54, 226–233. https://doi. org/10.1016/j.net.2021.07.034.

Jiang, Y.B., La, Y.X., Liu, X.X., 2024. Effect of grain size on irradiation-induced bubble evolution in high burn-up UO2: a phase-field study. J. Nucl. Mater. 601, 155312. https://doi.org/10.1016/j.jnucmat.2024.155312.

La, Y.X., Jiang, Y.B., Lan, X., 2024. Phase-field simulation of fission bubbles formation in composite ceramic nuclear fuel. Nucl. Eng. Des. 428, 113485. https://doi.org/ 10.1016/j.nucengdes.2024.113485.

Millett, P.C., El-Azab, A., Wolf, D., 2011. Phase-field simulation of irradiated metals: Part II: gas bubble kinetics. Comput. Mater. Sci. 50, 960–970. https://doi.org/10.1016/j. commatsci.2010.10.032.

Lan, X., Jiang, Y.B., Sun, D., 2024. Three-dimensional phase-field simulation of intergranular bubble evolution in UO2 during irradiation. Nucl. Eng. Des. 416, 112766. https://doi.org/10.1016/j.nucengdes.2023.112766.

Aagesen, L.K., Biswas, S., Jiang, W., 2021. Phase-field simulations of fission gas bubbles in high burnup UO2 during steady-state and LOCA transient conditions. J. Nucl. Mater. 557, 153267. https://doi.org/10.1016/j.jnucmat.2021.153267.

Gao, Y., Zhang, Y.F., Schwe, D., 2018. Formation and self-organization of void superlattices under irradiation: a phase field study. Material 1, 78–88. https://doi. org/10.1016/j.mtla.2018.04.003.

Gao, Y.P., Jokisaari, A.M., Aagesen, L., 2022. The effect of elastic anisotropy on the symmetry selection of irradiation-induced void superlattices in cubic metals. Comput. Mater. Sci. 206, 111252. https://doi.org/10.1016/j. commatsci.2022.111252.

Bai, X.M., Tonk, M.R., Zhang, Y.F., 2016. Multiscale modeling of thermal conductivity of high burnup structures in UO2 fuels. J. Nucl. Mater. 470, 208–215. https://doi.org/ 10.1016/j.jnucmat.2015.12.028.

Liang, L.Y., Kim, Y.S., Mei, Z.G., 2018. Fission gas bubbles and recrystallization-induced degradation of the effective thermal conductivity in U-7Mo fuels. J. Nucl. Mater. 511, 438–445. https://doi.org/10.1016/j.jnucmat.2018.09.054.

Lan, X., Jiang, Y.B., La, Y.X., 2023. Calculation of the effective thermal conductivity of porous polycrystalline U-10Mo alloy based on phase-field simulation. Nucl. Eng. Des. 413, 112552. https://doi.org/10.1016/j.nucengdes.2023.112552.

Jiang, Y.B., Shen, W.L., La, Y.X., 2025. Phase-field simulation of recrystallization and calculation of the effective thermal conductivity of polycrystalline UO2. Ann. Nucl. Energy. 211, 110918. https://doi.org/10.1016/j.anucene.2024.110918.

Abdoelatef, M.G., Badry, F., Schwen, D., 2019. Mesoscale modeling of high burn-up structure formation and evolution in UO . Metals Mater. Soc. 71, 4817–4828. https://doi.org/10.1007/s11837-019-03830-z.

Liang, L., Mei, Z.G., Yacout, A.M., 2017. Fission-induced recrystallization effect on intergranular bubble-driven swelling in U-Mo fuel. Comput. Mater. Sci. 138, 16–26. https://doi.org/10.1016/j.commatsci.2017.06.013.

Kim, S.G., Kim, W.T., Suzuki, T., 1999. Phase-field model for binary alloys. PhysRevE 60 (6), 7186–7197. https://doi.org/10.1103/PhysRevE.60.7186.

Chen, L.Q., Wei, Y., 1994. Computer simulation of the domain dynamics of a quenched system with a large number of nonconserved order parameters: the grain-growth kinetics. PhysRevB 50, 15752. https://doi.org/10.1103/PhysRevB.50.15752.

Aagesen, L.K., Jokisaari, A., Schwen, D., 2022. A phase-field model for void and gas bubble superlattice formation in irradiated solids. Comput. Mater. Sci. 215, 111772. https://doi.org/10.1016/j.commatsci.2022.111772.

Tonks, M.R., Zhang, Y., Butterfield, A., 2015. Development of a grain boundary pinning model that considers particle size distribution using the phase field method. Modelling Simul. Mater. Sci. Eng. 23, 045009.

Hu, S.Y., Murray, J., Weiland, H., 2007. Thermodynamic description and growth kinetics of stoichiometric precipitates in the phase-field approach. Calphad. 31, 303–312. https://doi.org/10.1016/j.calphad.2006.08.005.

Moelans, N., Blanpain, B., Wollants, P., 2008. Quantitative analysis of grain boundary properties in a generalized phase field model for grain growth in anisotropic systems. PhysRevB. 78, 024113. https://doi.org/10.1103/PhysRevB.78.024113.

Cahn, J.W., 1961. On spinodal decomposition. Acta Mater. 9, 795–801. https://doi.org/ 10.1016/0001-6160(61)90182-1.

Liang, L.Y., Mei, Z.G., Kim, Y.S., 2018. Three-dimensional phase-field simulations of intragranular gas bubble evolution in irradiated U-Mo fuel. Comput. Mater. Sci. 145, 86–95. https://doi.org/10.1016/j.commatsci.2017.12.061.

Cahn, J.W., Allen, S.M., 1977. A microscopic theory for domain wall motion and its experimental verification in Fe-Al alloy domain growth kinetics. Le Journal De Physique Colloques 38, C7–C51. https://doi.org/10.1051/jphyscol:1977709.

Simmons, J.P., Shen, C., Wang, Y., 2000. Phase field modeling of simultaneous nucleation and growth by explicitly incorporating nucleation events. Scripta. Mater. 43, 935–942. https://doi.org/10.1016/S1359-6462(00)00517-0.

Hu, S.Y., Casella, A.M., Lavender, C.A., 2015. Assessment of effective thermal conductivity in U-Mo metallic fuels with distributed gas bubbles. J. Nucl. Mater. 462, 64–76. https://doi.org/10.1016/j.jnucmat.2015.03.039.

Rest, J., 2010. An analytical study of gas-bubble nucleation mechanisms in uraniumalloy nuclear fuel at high temperature. J. Nucl. Mater. 402, 179–185. https://doi. org/10.1016/j.jnucmat.2010.05.022.

Spino, J., Rest, J., Goll, W., Walker, C.T., 2005. Matrix swelling rate and cavity volume balance of UO2 fuels at high burn-up. J. Nucl. Mater. 346, 131–144. https://doi.org/ 10.1016/j.jnucmat.2005.06.015.

Liang, L., Mei, Z.G., Kim, Y.S., 2016. Mesoscale model for fission-induced recrystallization in U-7Mo alloy. Comput. Mater. Sci. 124, 228–237. https://doi.org/ 10.1016/j.commatsci.2016.07.033.

Evans, J.H., Foreman, A.J.E., 1985. Some implications of anisotropic self-interstitial diffusion on void swelling in metals. J. Nucl. Mater. 137, 1–6. https://doi.org/ 10.1016/0022-3115(85)90043-1.

Konobeev, Y.V., Subbotin, A.V., Bykov, V.N., 1975. Grain boundary void denuded zone in irradiated metals. Phys. Stat. Sol. (a) 29, K121. https://doi.org/10.1002/ pssa.2210290246.

Han, W.Z., Demkowicz, M.J., Fu, E.G., 2012. Effect of grain boundary character on sink efficiency. Acta. Mater. 60, 6341–6351. https://doi.org/10.1016/j. actamat.2012.08.009.

Leenaers, A., Van Renterghem, W., Van den Berghe, S., 2016. High burn-up structure of U(Mo) dispersion fuel. J. Nucl. Mater. 476, 218–230. https://doi.org/10.1016/j. jnucmat.2016.04.035.

Gan, J., Miller, B.D., Keiser Jr, D.D., 2014. Microstructural characterization of irradiated U–7Mo/Al–5Si dispersion fuel to high fission density. J. Nucl. Mater. 454, 434–445. https://doi.org/10.1016/j.jnucmat.2014.08.052.

Harrison, R.W., Greaves, G., Hinks, J.A., 2017. Engineering selforganising helium bubble lattices in tungsten. Sci. Rep. 7 (1), 7724. https://doi.org/10.1038/s41598-017- 07711-w.
