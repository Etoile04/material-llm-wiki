# 📄 PDF Parsing Result

**File:** `/Volumes/openclaw记忆/Zotero_storage/storage/6Y3TGGVS/Liang et al. - 2018 - Three-dimensional phase-field simulations of intragranular gas bubble evolution in irradiated U-Mo f.pdf`
**Backend:** `pipeline`
**Pages:** 0 to end
**Formula Recognition:** ❌ Disabled
**Table Recognition:** ✅ Enabled

---

# Three-dimensional phase-field simulations of intragranular gas bubble evolution in irradiated U-Mo fuel

![](images/62d2f14cbbfbabf16833b4592dc199e2cf14134f8f86ebb88f78efb4de306323.jpg)

Linyun Liang ⇑ , Zhi-Gang Mei, Yeon Soo Kim, Mihai Anitescu, Abdellatif M. Yacout

Argonne National Laboratory, 9700 South Cass Avenue, Argonne, IL 60439, USA

## a r t i c l e i n f o

Article history:   
Received 27 September 2017   
Received in revised form 28 December 2017   
Accepted 29 December 2017   
Available online 4 January 2018

Keywords:   
Phase-field   
Intragranular gas bubbles   
Fuel swelling

## a b s t r a c t

The evolution of fission gas bubbles in irradiated materials plays a critical role in the microstructural processes that leads to dimensional changes of U-Mo alloy fuels, e.g., fuel swelling. Although the intergranular bubbles-induced fuel swelling has been long-discussed for U-Mo fuel, there are very few computational studies of the formation of intragranular gas bubbles and its impact on fuel swelling. To this end, we develop a three-dimensional phase-field model to investigate the evolution of intragranular gas bubbles in U-Mo fuel. Fission induced defect formation and annihilation processes, such as vacancyinterstitial recombination, fission gas atom resolution, and interactions with dislocations and grain boundaries are incorporated in the model. Simulations show that the intragranular gas bubbles can be stabilized to certain sizes due to the balance between the generation and annihilation of defects. The intragranular gas bubbles induced fuel swelling is predicted to be comparable to experimental measurements. The effects of the irradiation and fuel fabrication conditions (i.e., fission rate, fuel grain size, and mechanical work induced deformation) on the bubble evolution and the resultant swelling are investigated. The current simulations provide a better understanding of intragranular gas bubble-induced swelling and a solid foundation for the future study of the nucleation and growth of intergranular gas bubbles and recrystallization in U-Mo fuel.

Published by Elsevier B.V.

## 1. Introduction

Understanding and predicting fission-induced microstructural changes in materials are of great importance to developing new fuels for both nuclear power and research reactors. U-Mo alloys are under investigation as a candidate fuel for future high power research reactors [1,2], because of their stable swelling behavior at moderate fission densities [3,4]. During the fission reactions of uranium-235, fission gas atoms, such as Xe, are generated at a rate of about 0.25 atom per fission as a result of decay of primary fission products. These fission gas atoms are almost insoluble in metallic fuels, and tend to accumulate in voids to form gas bubbles. The formation of fission gas bubbles can lead to serious dimensional changes of nuclear fuels, e.g., fuel swelling, which can affect the fuel performance and the long-term safety of reactors. Therefore, understanding the mechanism of the nucleation and growth of fission gas bubbles and their impact on fuel swelling plays a critical role in the qualification of U-Mo fuel for high performance research reactors.

Various types of fission gas bubbles have been observed in irradiated U-Mo alloy fuels. These gas bubbles can be categorized into three types based on their morphology and location: (1) intragranular bubbles – those inside fuel grains, usually of nanometer scale and evenly distributed; (2) intergranular bubbles – those on grain boundaries, usually of micrometer scale; and (3) periphery bubbles – those in the interaction layer of the fuel and Al matrix, usually large and unevenly distributed [5]. The final morphology of gas bubbles is affected by several factors, such as types of fuel, fuel fabrication conditions, and operation conditions of reactors. Although fission gas bubbles have different morphologies, the initial stage of bubble formation is considered to be similar, starting as isolated fission gas atoms inside fuel grains. Therefore, understanding the mechanism of the nucleation and growth of intragranular bubbles is critical to investigating the evolutions of other types of gas bubbles.

During fission events, incident irradiations produce isolated gas atoms and Frenkel pairs. The generated vacancies and selfinterstitial atoms (SIAs) in equal numbers can annihilate either through their recombination to form perfect lattices or by interactions with defect sinks such as dislocations, grain boundaries, or precipitates. The efficiency of vacancy/SIA absorption by different sinks varies vastly because of the different sink strengths. The relaxation volumes of SIAs in bcc alloys are typically much larger than those of vacancies, resulting in a higher rate of SIAs to interact with edge dislocations than vacancies [6]. This property is the origin of dislocation bias, and is the driving force for the formation of vacancy clusters. The fission gas atoms can be easily trapped by vacancy clusters to form intragranular gas bubbles inside fuel grains. Subsequently, the growth of intragranular gas bubbles are closely related to the effective diffusivities of fission gas atoms in fuel grains. Generally, intragranular gas bubbles confined inside fuel grains do not grow to an appreciable size. The phenomenon is attributed to the fission-induced gas atom re-solution process [7], in which small intragranular gas bubbles are partially or completely destroyed by close-passing fission fragments and some of the gas atoms in the bubbles are resolved into the fuel matrix. Therefore, the formation, growth, and dissolution of gas bubbles in U-Mo fuel are closely related to the diffusion of point defects and their reactions with defect aggregates.

Computer simulation as a cost-effective method can provide important information for the development of new materials. Various computational approaches have been used to study the behavior of gas bubbles in irradiated materials. Among those, phase-field method is a mesoscale approach that has been successfully applied to study the nucleation and growth of voids [8–11] and their migration [12–14], interstitial kinetics [15,16], crack propagation [17], gas bubble evolution [18–24], and recrystallization [25] in nuclear materials. In particular, Millett et al. [9,21] proposed a physics-based phase-field model to simulate the evolution of voids and gas bubbles in irradiated materials. Their model can capture the processes of point defect generation and recombination, and bubble nucleation and growth in the presence of grain boundaries. However, their simulations were performed in two dimensions, and several important defects reactions were ignored, such as fission-induced gas atom resolution, vacancy and SIA interaction with dislocations, and diffusion of gas atoms to grain boundaries. These defect reactions are important to the formation of the stable nanometer size gas bubble structures [7,21]. Although significant progress has been made, few phase-field models can reproduce the stable intragranular gas bubble structures under irradiation. One exception is a recent work by Hu et al. [26], in which a twodimensional phase-field model was developed to study the formation of gas bubble superlattice in U-Mo. However, it should be pointed out that the generation of fission gas was artificially turned off in order to maintain a saturated Xe concentration in their model.

In this work, we develop a three-dimensional phase field model to study the gas bubble evolution in bcc U-Mo alloy with 7 wt.% Mo (U-7Mo) based on Millett et al.’s two-dimensional model. The large size difference between intragranular bubbles (size around 1.0–5.0 nm) and intergranular bubbles (size around 0.1–0.3 µm) makes simulating them simultaneously difficult because of the limitation of computing resources. In this work we focus on intragranular gas bubbles in U-Mo alloy fuel. The current model incorporates most of the key defect processes, including the defect production by fission, gas atoms reresolution, grain boundary sinks for gas atoms, vacancy-SIA recombination, and dislocation sinks for the vacancy and SIA. We develop a new free energy for gas bubble phases based on the van der Waals equation of state (vdW EOS). By including the critical defect annihilation and gas-atom resolution processes, we demonstrate that the stable intragranular gas bubble structure observed in experiments can be reproduced. The predicted fission gas bubble size distribution and bubble-induced swelling of U-Mo are in agreement with experimental measurements. We also investigate the influence of fabrication and irradiation conditions on the growth kinetics of intragranular gas bubbles and the resultant fuel swelling in U-Mo.

## 2. Phase-field methodology

To study the evolution of fission gas bubble in U-Mo fuel, we chose three parameters as composition fields in the phase-field model, namely, the concentrations of fission gas Xe cXðr; tÞ, vacancy cV r; t , and SIA cI r; t , which represent atoms or mole fractions at position r and time t. The phase parameter gðr; tÞ is chosen to represent the gas bubble phase with g  1 and the matrix phase with g 0. g changes continuously from 0 to 1 across the interface between the gas bubble and matrix. The total free energy of the system can be described by

$$
\tag{ð1Þ}
$$

where f chemis the chemical free energy density describing the composition and volume fraction of the equilibrium phases,jX, jV , jI, and jg are the gradient energy coefficients for Xe, vacancy, and SIA concentrations, and the phase parameter, respectively, f elas is the elastic energy density, eij is the strain, and T is the temperature. The first term in the volume integral represents the local contribution to the free energy from short-range chemical interactions. Four second derivative terms in the volume integral represent the interfacial properties. The last term in the volume integral represents the long-range elastic interactions.

The chemical free energy density describes the thermodynamic properties of the system by

$$
\tag{ð2Þ}
$$

where f and f are the free energy densities of the gas bubble and matrix, respectively, hðgÞ is an interpolation function with the form g3 6g2  15g  10 , g g is a double-well function with the form g2ð1 - gÞ 2 to promote the stable phases, and w is the potential barrier height.

In deriving the free energy of the matrix, the condition cX þ cV þ cI þ cM ¼ 1:0 (cM is the concentration of perfect lattice site) is always satisfied since we assume that the defects can occupy only the lattice sites. Thus, by adopting the ideal solution model, we can express the free energy of the matrix as

![](images/4f9ce8b3e3721ef8e5bc95ea4164a323ebe5bb9e4b8ef6afa8a8feeaae997770.jpg)

where E fX, E fV , and E fI are the formation energies of Xe, vacancy, and SIA in the matrix phase, respectively, and kB is the Boltzmann’s constant.

For the free energy of gas bubbles, the definition of the Xe atom concentration differs from that in the matrix. In bubbles, Xe atoms can occupy either lattice or non-lattice sites. The Xe concentration in the bubble is defined as cb NX=Vb, where NX is the number of Xe atoms in the bubble and V is the volume of the bubble. Based on this definition, the Xe EOS can be used to determine the free energy of gas bubble contributed by Xe accumulation. A detailed derivation of the Xe bubble free energy is given in the appendix. The free energy of the Xe bubble based on the vdW EOS is given by

$$
\tag{ð4Þ}
$$

where l and p0 are the chemical potential and the pressure at the reference state, respectively, and B0 is a constant related to the vdW constant, which can be obtained by fitting the experimental data.

Because of the different definitions of Xe concentration in the matrix and gas bubbles, we have to convert the Xe concentration to be consistent with the definition in the matrix. The definition of the Xe concentration can be written as cbX ¼ NX=Vb ¼ cX=Vsite, where NX is the number of Xe atoms per unit of volume and Vsite is the volume of lattice site of the host material. Thus, the free energy of the gas bubble is

$$
\tag{ð5Þ}
$$

where A and B are constants.

The governing equations describing the spatial and temporal evolutions of the phase parameter and the concentrations of Xe, vacancy, and SIA are

$$
\tag{ð6aÞ}
$$

$$
\tag{ð6bÞ}
$$

$$
\tag{ð6cÞ}
$$

$$
\tag{ð6dÞ}
$$

where \_ni (i = g, X, V, I) are the thermal induced fluctuations, and \_Pi (i = X, V, I) are the point defect production rates. The production rate of Xe is expressed as \_PX 2 1  g 2 f Ran, where fr is the KXfission rate, Ran is the random number uniformly between 0 and 1, the number 2 is used to account for the loss of concentration due to the introduction of the random number, is the volume of the lattice site of U-Mo, and is a constant.

KThe Frenkel pair production rate in the unit of displacement per atom (dpa) in the fuel can be related to the fission rate according to [27],

$$
\tag{ð7Þ}
$$

where d is a constant.

Gas-atom re-solution is a dynamic bubble shrinkage mechanism in which the fission gas atoms are knocked out from a bubble caused directly or indirectly by the fission fragments [28–30]. The observation that intragranular bubbles do not grow to appreciable sizes at low temperatures can be ascribed to the effect of irradiation-induced gas-atom re-solution [28,30,31]. There are two accepted mechanisms of the re-solution effect: one is the heterogeneous process which destroys entire bubbles in the path of fission fragments and in which all gas atoms in the bubble return to the matrix as single atoms; and the other is a homogeneous process which re-solves fission-gas atoms singly by scattering collisions with fission fragments and uranium recoils whose paths intersect the bubbles. Both mechanisms [7] agree that the intragranular bubbles rapidly grow to certain sizes; the bubbles are either dissolved (heterogeneous mechanism [29]) or stabilized (homogeneous mechanism [32]). We adopt the homogeneous mechanism in this work for simplifying the model. The fissioninduced gas resolution is written as R\_ re g2bcX, where b is the resolution rate and g2 is used to limit the gas resolution occurring only inside the gas bubble.

Free atoms diffuse towards the grain boundaries, where they can form intergranular bubbles. The diffused gas atoms can be described by a sink term \_SX 1 g 2 rgSgVXcX, where Sg is the grain boundary areas per unit volume, VX is the velocity of the gas atom, and rg is a rate constant [33].

When SIAs and vacancies encounters each other, they recombine and form a perfect lattice. Their recombination can be described by \_RVI mrcV cI, where mr is the recombination rate. To account for the faster recombination rate on the void surface, we define it as mr mb g2ms, where mb and msis the recombination rate in the bulk and on the surface, respectively. mb is given by 4priv DI DV = , where riv is the radius of the recombination vol-Xume and DV and DI are the diffusivities of vacancy and SIA, respectively [34].

Due to the unique nature of the stress field in the neighborhood of a dislocation line, the dislocation is an efficient sink for many atomic defects. Vacancies and SIAs approaching a dislocation can be permanently captured. Thus, the dislocation acts as a perfect sink for vacancies and SIAs. The sink terms can be described as \_Si k 2 Dici, where k 2 and k 2 are the sink strengths of dislocations for vacancies and SIAs [6]. They take the forms,

$$
\tag{ð8aÞ}
$$

$$
\tag{ð8bÞ}
$$

where ZV and ZI are the dislocation bias terms for vacancies and SIAs, respectively, and q is the dislocation density in the materials.

The motilities of the Xe, vacancy, and interstitial atoms can be described by

$$
\tag{ð9Þ}
$$

Due to the introduction of defects in the matrix, a lattice misfit can occur between the matrix and gas bubbles. The strain energy caused by the misfit can be described by elastic theory. If the variation of the stress-free lattice parameter, a, with respect to defect (vacancy and interstitial) concentrations is assumed to obey Vegard’s law, the local stress-free strain caused by the defect inhomogeneity in the matrix is given by [20]

$$
\tag{ð10Þ}
$$

where eX0 1=a da=dcX, eV0 1=a da=dcV , and eI0 1=a da=dcI are the expansion coefficients of the lattice parameter due to the introduction of gas atoms, vacancies, and SIAs, c eq0X ; c eq0V , and c eq0I are the equilibrium concentration of the Xe, vacancy, and selfinterstitial atoms, respectively, and dij is the Kronecker-delta function.

Similarly, the local stress-free strain caused by the defect inhomogeneity in the gas bubble is [20]

$$
\tag{ð11Þ}
$$

where the expansion coefficients of the lattice parameter eb0 is related to the introduction of gas bubbles.

Following Khachaturyan’s elastic theory [35], the elastic strain can be calculated by

$$
\tag{ð12Þ}
$$

where -eij is the homogeneous strain describing the macroscopic shape and volume change, which is defined such that R d ij r\* dV  0 and d kl r\* is a function of displacement as 1=2½@ukð r\* Þ=@rl þ @ulð r\* Þ=@rk [36]. The elastic energy density can be calculated by

$$
\tag{ð13Þ}
$$

where kijkl is the elastic constant tensor of the system. We assume the elastic constants for the gas bubble are the same as in the bulk U-Mo alloy [20].

Modeling the nucleation process is one of the greatest challenges in phase-field simulations. In this work, we explicitly introduce nuclei in the governing equation following the classical nucleation theory. The detailed procedure can be found in previous work [37,38].

## 3. Material properties

In order to study the bubble evolution in U-7Mo alloy, material properties, such as elastic constants, bubble surface energy, defects formation energies, reaction rates and defect diffusivities, are needed as input parameters for the phasefield simulations. Recently, Mei et al. [39] studied the elastic properties of U-7Mo alloy using density functional theory (DFT) calculations. So far, the surface energy, defect formation energies, and defect diffusivities in U-Mo alloys have not been studied yet. To this end, we studied the surface properties of U-7Mo alloy using DFT calculations. Four typical surfaces of bcc phase, namely, (1 0 0), (1 1 0), (1 1 1) and (2 1 1) surfaces, are considered. The most stable surface is predicted to be (1 1 0) with a surface energy of 1.81 J/m2 . Due to the complex atomic environment in the structure of U-7Mo alloy, the defect formation energy in the alloy is estimated by averaging the vacancy or interstitial formation energies of four independent configurations of U/Mo. The formation energies of vacancy and interstitial in U-7Mo alloy are predicted to be 1.12 eV and 1.48 eV, respectively. With a similar approach, the solution energy of Xe in U-7Mo matrix is predicted to be 6.95 eV. We note that both the defect formation energy and the Xe solution energy are presented as averaged results at the U and Mo lattice sites, because U and Mo are not distinguished in the current model. The diffusivities of U/Mo vacancy and SIA in U-7Mo alloy are predicted from the mean square displacement of defects calculated by molecular dynamics (MD) simulations. The calculated diffusivities show that SIAs diffuse significantly faster than vacancies in U-7Mo alloy. A detailed description of the calculations of the formation energy and diffusivity of defects in U-7Mo alloy using DFT and MD will be presented elsewhere. The Xe diffusivity in U-7Mo alloy is adopted from Rest’s work [40]. Table 1 presents the values of the principal parameters used in the current simulation.

The mobilities MX;I;V of point defects are related to their diffusivities DX;V;I by Eq. (9). Constants A and B in the free energy function in Eq. (5) are chosen to be 1:1  1010 J cm-3 and 2:3 1010 J cm-3 to ensure that the vacancy and SIA have identical and lower chemical potentials in the gas bubble and matrix phases, respectively. The gradient coefficients and potential height are determined by the surface energy of a gas bubble as shown in Table 1. The other parameters used include the lattice misfit strains, eX0 ¼ -0:006, eV0 ¼ 0:02, eI0 ¼ 0:02, and eb0 ¼ 0:003. The velocity of Xe can be obtained by ffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffiffi3kB T =mXp , where mx is the atomic mass of the Xe with the value of 2.17 10-25 kg. The currently used defect production rates are consistent with the typical average fission rate used for the in-pile test of U-Mo dispersion fuels [34,43].

In the simulations, a model size of 22.4 nm  22.4 nm  22.4 nm is used. The grid spacing is l ¼ 0:35 nm. Periodic boundary Dconditions are imposed on the simulation domain. A semiimplicit FFTW method is employed to solve the coupled Eqs. (6a)–(6d) [44].

Materials properties of U-7Mo alloy used in the simulations.
<table><tr><td>Physical parameter</td><td>Symbol</td><td>Value</td><td>Reference</td></tr><tr><td>Temperature</td><td>T</td><td>473K</td><td>This work</td></tr><tr><td>Lattice constant of U-7Mo</td><td>a</td><td>3.43× 10-10m</td><td>This work</td></tr><tr><td>Surface energy</td><td>0</td><td>1.81J/m²</td><td>This work</td></tr><tr><td>Gradient coefficients</td><td>Kx.V,n</td><td>6.91×10- J/m</td><td>This work</td></tr><tr><td>Potential height</td><td>W</td><td>7.73×10°J/m²</td><td>This work</td></tr><tr><td>Vacancy formation energy</td><td>E</td><td>1.12 eV</td><td>This work</td></tr><tr><td>Interstitial formation energy</td><td>E</td><td>1.48 eV</td><td>This work</td></tr><tr><td>Xe solution energy</td><td>E</td><td>6.95 eV</td><td>This work</td></tr><tr><td>Xe diffusivity</td><td>Dx</td><td>4.10 ×10-17m² s-1</td><td>[40]</td></tr><tr><td>Interstitial diffusivity</td><td>D</td><td>2.05 × 10-14 m² s-1</td><td>This work</td></tr><tr><td>Vacancy diffusivity</td><td>Dv</td><td>3.84× 10-17m² s-1</td><td>This work</td></tr><tr><td>Kinetic coefficient</td><td>L</td><td>9.04×10-m² J-1s-1</td><td>This work</td></tr><tr><td>Elastic constant Elastic constant</td><td>C11</td><td>173.0 Gpa</td><td>[39]</td></tr><tr><td>Elastic constant</td><td>C12</td><td>138.0 Gpa</td><td>[39]</td></tr><tr><td>Resolution rate</td><td>C44</td><td>50.0 Gpa</td><td>[39]</td></tr><tr><td></td><td>b</td><td>2.0 ×10-25 fr</td><td>[41]</td></tr><tr><td>Dislocation bias for vacancies</td><td>Zv</td><td>1.0</td><td>[6]</td></tr><tr><td>Dislocation bias for interstitials</td><td>Zi</td><td>1.025</td><td>[6]</td></tr><tr><td>Nucleation rate</td><td>k1</td><td>1.0×10-3</td><td>This work</td></tr><tr><td>Nucleation rate constant</td><td>k2</td><td>1.0 × 10-5</td><td>This work</td></tr><tr><td>Velocity of Xe atom</td><td>Vx</td><td>300.08 m/s</td><td>This work</td></tr><tr><td>Frenkel pair rate constant</td><td>δ</td><td>6.2</td><td>This work</td></tr><tr><td>Xe generation rate constant</td><td>4</td><td>0.25</td><td>[42]</td></tr><tr><td>Rate constant for grain boundary sink</td><td>rg</td><td>2.4×10²</td><td>This work</td></tr><tr><td>Radius of the recombination volume</td><td>riv</td><td>2.0× 10-10m</td><td>[6]</td></tr><tr><td>Recombination rate on surface</td><td>Us</td><td>2vb</td><td>This work</td></tr></table>

## 4. Results and discussion

In this section we present the phase-field simulation results of intragranular gas bubble evolution and gas bubble-induced swelling in irradiated U-Mo alloy fuel. Our simulation shows that the formation of a stable intragranular gas bubble structure observed in U-Mo fuel is due to the dynamic equilibrium between defect generation and annihilation. In the following subsections, we discuss the effects of fission rate, initial fuel grain size, and fuel fabrication conditions on the evolution of intragranular gas bubbles and the resultant swelling in U-Mo fuel.

## 4.1. Stable intragranular gas bubble structure under irradiation

The evolution of fission-induced defect concentrations can be obtained by solving the coupled equations (6a)–(6d). Typical irradiation and fabricated conditions for U-Mo fuel are used in the simulations, i.e., the fission rate, grain boundary density, and dislocation density are fixed at 5:0  1020 m-3 s -1 , 0.41 m-1 , and 0.431015 m-2 , respectively [5,45]. The simulated phase parameter and point defect concentration profiles are shown in Fig. 1 at different irradiation times. Fission gas atoms and vacancies tend to accumulate and form gas bubbles, in which the equilibrium concentrations of vacancy, Xe, and SIA inside gas bubbles are about 1.0, 0.90, and 0.07, respectively. The average gas bubble pressure is about 1.3 GPa estimated by the vdW EOS Eq. (A.5), which is consistent with the Xe gas pressure predicted by other phase field simulations [26]. The concentration of SIAs is considerably lower than that of vacancies inside gas bubbles because of the biased dislocation sink. Although SIAs and vacancies are generated equally as Frenkel pairs during irradiation, their annihilation rates at dislocations are vastly different due to the difference in atomic diffusion radius [43]. More SIAs are annihilated at the dislocations leaving vacancies inside the grains. The accumulation of vacancies provides room for large fission gas atoms to form stable gas bubbles. Bubble growth is driven by the absorption of vacancies and gas atoms. At the beginning of the irradiation, the size of the gas bubbles consistently grow with increasing fission time, while the number of gas bubbles increases. After a certain irradiation time, the number of gas bubbles remains unchanged, while the bubble size increases very slowly. Small bubbles are dissolved due to fissioninduced gas atom resolution and bubble coalescence. The bubble coalescence occurs either through large bubbles swallowing small bubbles or through atomic diffusion between bubbles. The simulated gas bubbles appear to be randomly distributed in the irradiated U-Mo fuel. The bubble migration is neglected in this model because of its extremely low mobility at typical operation temperatures of research reactors [46].

![](images/b591d3b603358d969b79ef2a4d47f03998c2e749c4de3324771018da15273a40.jpg)  
Fig. 1. Temporal evolution of (a) phase parameter; (b) vacancy; (c) Xe; (d) SIA concentrations in the irradiated U-Mo fuel. The isosurfaces of 0.7, 0.7, 0.5, and 0.1 were used for plotting the phase parameter, vacancy, Xe, and SIA concentration profiles, respectively.

The evolution of gas bubbles in irradiated materials is inherently a dynamic process, involving a balance between the growth and shrinkage mechanisms. At a constant temperature, the nucleation and growth of gas bubbles are driven by the supersaturation of point defects under irradiation. Gas bubbles can grow by absorbing vacancies or shrink by either emitting vacancies or absorbing interstitials. Addition or emission of gas atoms can change the volume of bubbles, with the relative change depending on the ratio of gas atoms to vacancies in the bubble. The calculated size of the gas bubbles ranges from 2.7 nm to 3.8 nm at the equilibrium state.

Experiments show that intragranular gas bubbles can form ordered superlattices in U-Mo dispersion fuels at low fission densities [47,48]. Several potential mechanisms of the bubble superlattice formation have been proposed: (1) elastic interaction between gas bubbles, (2) directional diffusion of SIAs, and (3) dislocation loop punching from overpressured bubbles. Recently, Hu et al. suggested that the directional diffusion of SIAs may be responsible for the gas bubble ordering structure [26]. However, their simulation was performed in two-dimension, which may not reveal the true mechanism of the bubble superlattice formation. Thus, due to the lack of a consensus on the formation mechanism of bubble superlattice, we assume the gas bubbles are randomly distributed in U-Mo alloys.

The fuel swelling induced by fission gas bubbles can be estimated by

$$
\tag{ð14Þ}
$$

where V0 is the initial volume of fuel and Vf is the final fuel volume with contribution from fission gas bubbles. Fig. 2 shows the calculated fuel swelling due to intragranular gas bubbles. The gas bubble induced fuel swelling increases rapidly at the beginning of the irradiation, and then remains almost unchanged. These results clearly show that at the beginning of irradiation the defect concentrations build up but the concentrations are too low either for recombination or sinks to have an effect on the buildup. As fission time increases, the buildup of defect concentrations start to level off when the production rate is compensated by the recombination rate and sink reactions. Eventually, the production of defects is balanced by the defect annihilation due to the recombination of vacancies and SIAs and sink reactions on grain boundaries and dislocations. Therefore, a stable gas bubble structure can be achieved, which is beneficial for realizing a stable fuel swelling behavior. However, the stable intragranular gas bubble structure can be destroyed at high fission densities due to the recrystallization process starting at grain boundaries. As a result, the fission gases are released from the intragranular bubbles and diffuse to the grain boundaries to form intergranular gas bubbles, which are the major source of fuel swelling at high fission densities. Therefore, it is technically important to retain fission gas atoms inside intragranular bubbles as stable gas bubble structure in order to decrease overall fuel swelling at high fission densities.

![](images/34dff8e7f8353b2634a50cabc79defbb7de9dc2362a0e544735e7479c601e554.jpg)  
Fig. 2. Intragranular bubble swelling as a function of fission density.

During irradiation, the major processes that affect the gas bubble sizes are the nucleation of gas bubbles, the diffusion of gas atoms into bubbles, and the fission-induced gas atom re-solution. The differences in growth rates of bubbles with different sizes result in a peak bubble size distribution. The position of the peak in the bubble size distribution is determined by the balance between the flux of gas atoms diffusion in and out of bubbles. As more fission gases and vacancies are generated, their diffusion into the bubbles increases, and the gas bubbles continuously grow. In contrast, the irradiation-induced gas resolution decreases the gas concentration inside the bubbles and the grain boundary and dislocation sinks decrease the defect concentrations, which make the gas bubbles shrink. The simulated size distribution of intragranular gas bubbles in U-Mo is given in Fig. 3. The calculated fission density is 3.0 1027 m-3 . The average size of the simulated gas bubbles is about 3.2 nm, which is the typical size of intragranular gas bubbles observed in irradiated U-7Mo dispersion fuels [46–49]. The calculated gas bubble density is 2:40 1024 m-3 , in a good agreement with the intragranular bubble density measured by experiments [48,49]. Therefore, the current simulations well capture the evolution of intragranular gas bubbles in U-Mo fuel.

Since the intragranular gas bubble induced fuel swelling barely changes after a certain period of fission density, we simulate the bubble swelling only for a fission density of 1.5 1027 m-3 in the following work in order to save the computational time.

## 4.2. Fission rate effect

Experiments have shown that the high fission rate can cause more serious gas bubble swelling than low fission rate [49]. Gas bubbles can show very different behaviors due to various fission rates. Recrystallization occurs in the metallic U-Mo fuel at high fission densities, which destabilizes the stable intragranular gas bubble structure [49,50]. Thus, the fission rate is expected to have a great impact on the evolution of intragranular gas bubbles and the resultant fuel swelling.

![](images/bf5ed0d7955b28e4f6d838802b508179f74a6f18822592c41b7e70aec29e6b60.jpg)  
Fig. 3. Simulated gas bubble size distribution in U-Mo fuel. The calculated fission density is 3.0 1027 m-3 .

The predicted effect of fission rate on the intragranular gas bubble swelling in the U-Mo fuel is shown in Fig. 4(a). Three fission rates of 3.0 1020 m-3 s-1 , 5.0 1020 m-3 s-1 , and 7.0 1020 m-3 s-1 are used in the simulations. The intragranular gas bubble swelling shows the highest value for the largest fission rate. As shown in Eqs. (6), the local defect production rate is proportional to fission rate. With an increased fission rate, the generation rates of point defects increase. Moreover, the annihilation rate of defects also increases due to the increased recombination, resolution, and sink reactions as shown in Eqs. (6), which are proportional to the defect concentrations. However, at the beginning of irradiation, the effect of annihilation on the defect concentrations is relatively small compared with the rapid generation of defect concentrations, thus the net concentrations of defects increase rapidly at high fission rate. This results in a high supersaturation of defect concentrations, which reduces the incubation time of gas bubble formation. After the formation of gas bubbles, the continuous increase of vacancy and Xe gas concentrations further promotes the growth of gas bubbles, which leads to the increased gas bubble swelling. The production of defects eventually is balanced by their annihilation, which leads to a stable gas bubble swelling. Therefore, increasing fission rate can lead to the increased intragranular gas bubble swelling in the U-Mo fuel at early irradiation time.

Fig. 4(b) shows the simulated size distribution of intragranular bubbles in U-Mo fuel at a fission density of 1.5  1027 m-3 . The average bubble size increases from 3.1 nm to 3.4 nm as the fission rate increases from 3.0 to 7.0  1020 m-3 s -1 . The peak of the bubble size distribution profile shifts to the larger size side when the fission rate increases. The reason is that the gas bubbles can grow faster by absorption of vacancies with a higher vacancy supersaturation or by bubble coalescence with a larger number of bubbles due to the higher vacancy production rate. These results are consistent with the recent experimental results performed in pure Mo [46], in which the size of Xe bubbles increases with the increase of ion flux. With a high fission rate, more Xe gas atoms are generated in the fuel because of its increased production rate, which increases the nucleation rate of gas bubbles. As expected, we found that the gas bubble density increases as fission rate increases. The calculated stable gas bubble density is 2:05 1024 m-3 , 2:40 1024 m-3 , and 2:67 1024 m-3 for fission rates of 3.0 1020 m-3 s-1 , 5  1020 m-3 s-1 , and 7.0  1020 m-3 s-1 at a fission time of 35 days.

![](images/f08dcccf2a9adc468e263301ccd19e02212d0ca8f050718bcd743cd9ed2518cb.jpg)

![](images/be627366dc1f8b3e5fea2651c1d42fab65e606f7c8c6b2f58010471da794a285.jpg)  
Fig. 4. Simulated effect of fission rate on (a) intragranular gas bubble swelling and (b) bubble size distribution in U-Mo fuels.

## 4.3. Grain size effect

The grain size of the polycrystalline U-Mo fuel plays an important role in the evolution of intragranular gas bubbles. Grain boundary acts as sinks for the fission gas atoms, which can assist in suppressing or controlling the gas bubble formation. Therefore, we study the effect of grain size on the evolution of intragranular gas bubbles.

Since the grain boundary is not directly modeled in this work, the simulation of grain size effect is realized by considering the grain boundary density in the reaction term in Eq. (6b). For a sample with fixed volume, increasing grain size can lead to decreased density of grain boundaries. Three scenarios with grain boundary densities of 0.65 µm-1 , 0.38 µm-1 , and 0.19 µm-1 , are considered, which correspond respectively to the grain size of 3.2 µm, 5.4 µm, and 10.7 µm estimated from an analytical expression [5]. These grain sizes are within the typical size range observed in U-Mo fuels. Fig. 5(a) shows the effect of grain size on the kinetics of intragranular gas bubble swelling. The fuel with the smallest grains show the lowest swelling. For fuels with reduced grain size, the concentration of gas atoms decreases because of the increased grain boundary sink reactions. Additionally, the small grains reduce the diffusion distance of gas atoms from grain interior to grain boundary, thus increasing the probability of Xe atoms sinking to the grain boundary to form intergranular gas bubbles. Therefore, the swelling caused by the intragranular gas bubbles in the small grain fuel decreases. We note, however, that the intergranular gas bubble swelling should increase accordingly since more gas atoms diffuse to the grain boundaries in the small grain size fuel.

Fig. 5(b) shows the effect of initial fuel grain size on the distribution of intragranular gas bubble size in the U-Mo fuel up to a fission density of 1.5 1027 m-3 . The peak of the bubble size distribution profile shifts to the larger size side when the fuel grain size increases. The calculated average bubble size increases from 3.0 nm to 3.5 nm when the grain size increases from 3.2 µm to 10.7 µm. This can be understood by considering the nucleation and growth of gas bubbles. In the small grain size fuel, more Xe atoms diffuse to the grain boundaries forming intergranular gas bubbles and leaving less Xe atoms in the bulk, resulting in fewer nucleation sites and a lower nucleation rate. Therefore, for a small grain size fuel both the size and the number of gas bubbles decrease. The calculated gas bubble density increases from 2:31  1024 m-3 to 2:49  1024 m-3 with the grain size increasing from 3.2 µm to 10.7 µm.

As the initial grain size of a fuel decreases, the intragranular gas bubbles induced fuel swelling decreases while the intergranular gas bubble swelling increases. Since the contribution of intergranular gas bubble to fuel swelling is usually much larger than intragranular bubbles, especially at high fission densities [3,48,51], reducing the intergranular gas bubble swelling and containing more intragranular gas bubbles within fuel grains by increasing grain size is an effective way to reduce the overall gas bubble swelling. Another benefit of using large fuel grains is to reduce the fission gas release. In a system including bubbles, grains, and grain boundaries, the Xe gas atoms release from the fuel matrix by single atom diffusion to grain boundaries, where Xe gas atoms diffuse more slowly inside fuel grain than on grain boundary. Thus, more Xe gas atoms release in the small grain fuel because of increased grain boundary densities. These results demonstrate the possibility of tuning bubble morphology and density in irradiated fuel materials through grain size modification.

![](images/2874ca330de167279e6555231904332d32677c635afd25e9fe699e362f4f561d.jpg)

![](images/3fef4443de50e1e668f2cb6404cd481cb4ede8b7be729477bea75ef604ed4068.jpg)  
Fig. 5. Simulated effect of grain size on (a) intragranular gas bubble swelling and (b) bubble size distribution in U-Mo fuels.

## 4.4. Effect of rolling induced dislocations

The rolling process used in the fabrication of U-Mo fuel plate can create a high density of the dislocation network, which can have a great impact on the microstructural evolution of a fuel. For example, experiments have showed that the bubble superlattice is missing in the U-Mo dispersion fuel when the initial density of dislocation is high although the exact mechanism is still unclear [50]. Therefore, the rolling process can have a high impact on the evolution of gas bubbles.To study the effect of rolling-induced dislocations on the evolution of intragranular gas bubbles, we introduced three initial dislocation densities in the U-Mo fuel. These dislocation densities are within the typical range observed for U-Mo dispersion fuels. Fig. 6(a) shows that the intragranular gas bubble induced swelling in U-Mo fuels with different initial dislocation densities. At the same fission density of 1.5  1027 m-3, the gas bubble swelling increases from about 2.8% to 5.9% when the initial dislocation density increases from 0:10 1015 m-2 to 1:52 1015 m-2 . For a fuel with high initial dislocation density, the defect-dislocation reactions consume both vacancies and SIAs, however the SIA concentration decreases much faster than the vacancy concentration does because of the biased sink strength. As a consequence, the recombination rate of vacancy and SIA decreases. More vacancies flow to voids so both bubble growth and swelling are enhanced at high dislocation density compared with the ones at low initial dislocation density [52]. As shown in Fig. 6(b), at a fission density of 1.5  1027 m-3 , the average bubble size in U-Mo fuel increases from 3.1 nm to 3.4 nm and the peak of gas bubble distribution also shifts to the larger bubble size side as the initial dislocation density increases from 0:10 1015 m-2 to 1:52  1015 m-2 . The gas bubble density also increases from 1:78  1024 m-3 to 2:85  1024 m-3 with increasing initial dislocation density. Therefore, the rolling process during fuel fabrication can play an important role in controlling the gas bubble size and density in U-Mo fuel.

## 5. Conclusions

We presented three-dimensional phase-field simulations of the evolution of intragranular gas bubbles in the irradiated U-Mo fuel. The fission-induced microstructural change in U-Mo fuel was simulated by incorporating several critical processes, radiationinduced defects production, vacancy and self-interstitial atom recombination, gas atom resolution, and defect sinks at grain boundaries and dislocations. The current phase-field model can capture the core behavior of stable intragranular gas bubble formation in U-Mo under irradiation. The simulated gas bubble size distribution, bubble density, and fuel swelling agree with the experimental data. We systematically studied the effect of fission rate, fuel grain size, and rolling-induced dislocation on the evolution of intragranular gas bubbles. High fission rate leads to large gas bubbles and high bubble density and therefore high swelling. Increasing the initial grain size of a fuel can increase the intragranular gas bubbles swelling while decrease the intergranular gas bubble swelling. Considering the significance of intergranular gas bubble swelling especially at high fission densities, the large grains are beneficial for reducing the overall bubble swelling. We also found that increased dislocation densities because of the rolling process in the fuel fabrication can lead to an increased intragranular gas bubble swelling. Our study shows that the fuel fabrication and irradiation conditions may be used to control the bubbleinduced swelling in U-Mo fuel.

## Acknowledgments

This work was supported by the U.S. Department of Energy, National Nuclear Security Administration (NNSA), Office of Material Management and Minimization (NA-23) Reactor Conversion Program, and by the U.S. Department of Energy, Office of Science, under contract DE-AC02-06CH11357. Use of the Center for Nanoscale Materials, an Office of Science user facility, was supported by the U.S. Department of Energy, Office of Science, Office of Basic Energy Sciences, under Contract No. DE-AC02-06CH11357. We also acknowledge use of Blues, a high-performance computing cluster operated by the Laboratory Computing Resource Center at Argonne National Laboratory. In addition, this manuscript benefited from insightful discussion with Dr. Jeff Rest.

## Appendix A. Derivation of the free energy of a gas bubble

The general expression of the Gibbs free energy of a gas bubble is expressed as

![](images/1c56d3963198267439eff0cb0509679d3aff2338046f5a89317c0e9f89d8ad1e.jpg)

![](images/184583d5ed1f87f28800b1e245c1720149988ccbfa52b1a1aaf23286865f1764.jpg)  
Fig. 6. Simulated effect of dislocation density on (a) intragranular gas bubble swelling and (b) bubble size distribution in U-Mo fuels.

$$
\tag{ðA:1Þ}
$$

where p is the pressure, Vb is the gas bubble volume, and G(p0) is the Gibbs free energy at the reference state p0.

The state of equation for a nonideal gas can be expressed as

$$
\tag{ðA:2Þ}
$$

where B0 and C0 are constants, n is the number of gas atoms, and kB is a Boltzmann constant, T is the temperature.

For a nonideal gas, the Gibbs free energy is

$$
\tag{ðA:3Þ}
$$

We assume that the state of equation of a nonideal gas has the form,

$$
\tag{ðA:4Þ}
$$

We can rewrite it by defining the Xe concentration in the gas bubble as cb n=Vb,

$$
\tag{ðA:5Þ}
$$

Then, the free energy of the gas bubble is expressed as

$$
\tag{ðA:6Þ}
$$

The reduced Van de Waals equation is

$$
\tag{ðA:7Þ}
$$

Thus, the Van de Waals constant is b ¼ B0 kBT. The free energy equation can be rewritten as

$$
\tag{ðA:8Þ}
$$

To calculate the p0 inside the bubble, we first clarify the definition of the gas concentration inside the matrix and gas bubble.

(1) In the matrix, the Xe, vacancy, and SIA atoms can occupy only one lattice site. Thus the concentration at every site satisfies the condition

$$
\tag{ðA:9Þ}
$$

The definition of the Xe concentration in the matrix is

$$
\tag{ðA:10Þ}
$$

(2) In the bubble, although the vacancy and interstitial atoms keep their definition as in the matrix, the Xe concentration is different. Based on the definition of the concentration in the state of equation, the Xe concentration in the bubble is

$$
\tag{ðA:11Þ}
$$

Therefore, the condition (A.9) is not satisfied at every site inside the gas bubble and

$$
\tag{ðA:12Þ}
$$

We have to relate these two definitions in order to make them consistent with each other. The definition of Xe concentration in the gas bubble can be written as

$$
\tag{ðA:13Þ}
$$

where Nv is the number of vacancy inside the bubble, and Vsite is the volume of the lattice site. Next, for each bubble the number of vacancy equals the number of sites, and the lattice parameter of U-7Mo is assumed to be 3.43 10-10 m. Thus,

$$
\tag{ðA:14Þ}
$$

The reference state is consistent with the state that we calculate for the formation energy of defects in DFT calculations. Thus, the reference pressure p0 is also derived at the same state,

$$
\tag{ðA:15Þ}
$$

where B0 is a fitting constant and can be fitted from the experimental data. In this paper, we use the data derived from the equation of state from Xiao et al.’s work [53]. The equation of state is

$$
\tag{ðA:16Þ}
$$

where constant a, b, and c are 259,780 J cm3 /mol2 , 23.9276 cm3 / mol, and 55.6583 cm3 /mol, respectively. We use the Van de Waals state equation to fit Eq. (A.16) in order to obtain the constant B0 . The fitted result gives B0 =kBT  23:9687  10-6 m3 /mol (see Fig. A1).

Therefore, based on the Xe atoms in the DFT calculation cell, the reference pressure is calculated as follows.

$$
\tag{ðA:17Þ}
$$

$$
\tag{ðA:18Þ}
$$

plot in Fig. A2 the free energy as a function of cX.

The equilibrium concentration is cX ¼ 0:017, which corresponds to the pressure 2:79 106 Pa.

![](images/79b17b86a839cc560c2519a459950b5e4292e3c87873462e1c592dfaa66c509f.jpg)  
Fig. A1. Comparison of fitting curve with the original data. The original data are taken from [40].

![](images/81525a80349eaf16a7f877e7de602a877b5f1e2860023e49c8ce99dc95eeccb7.jpg)  
Fig. A2. Bubble free energy as a function of Xe concentration. The insert figure shows the enlargement of dash circle areas.

## References

[1] J.L. Snelgrove, G.L. Hofman, M.K. Meyer, C.L. Trybus, T.C. Wiencek, Nucl. Eng. Des. 178 (1997) 119–126.

[2] D.D. Keiser, S.L. Hayes, M.K. Meyer, C.R. Clark, Jom-J. Miner. Metals Mater. Soc. 55 (2003) 55–58.

[3] Y.S. Kim, G.L. Hofman, J. Nucl. Mater. 419 (2011) 291–301.

[4] G.L. Hofman, Y.S. Kim, Nucl. Eng. Technol. 37 (2005) 299–308.

[5] Y.S. Kim, G.L. Hofman, J. Rest, Argonne National Laboratory, Argonne National Laboratory, 2008.

[6] J. Rest, J. Nucl. Mater. 207 (1993) 192–204.

[7] D.R. Olander, D. Wongsawaeng, J. Nucl. Mater. 354 (2006) 94–109.

[8] S. Hu, C.H. Henager Jr., J. Nucl. Mater. 394 (2009) 155–159.

[9] P.C. Millett, A. El-Azab, S. Rokkam, M. Tonks, D. Wolf, Comput. Mater. Sci. 50 (2011) 949–959.

[10] A. El-Azab, K. Ahmed, S. Rokkam, T. Hochrainer, Curr. Opin. Solid State Mater. Sci. 18 (2014) 90–98.

[11] T. Hochrainer, A. El-Azab, Philos. Mag. 95 (2015) 948–972.

[12] S.Y. Hu, C.H. Henager Jr., Acta Mater. 58 (2010) 3230–3237.

[13] Y. Li, S. Hu, X. Sun, F. Gao, C.H. Henager Jr., M. Khaleel, J. Nucl. Mater. 407 (2010) 119–125.

[14] L. Zhang, M.R. Tonks, P.C. Millett, Y. Zhang, K. Chockalingam, B. Biner, Comput. Mater. Sci. 56 (2012) 161–165.

[15] Y. Li, S. Hu, C.H. Henager Jr., H. Deng, F. Gao, X. Sun, M.A. Khaleel, J. Nucl. Mater. 427 (2012) 259–267.

[16] S. Hu, C.H. Henager Jr., Y. Li, F. Gao, X. Sun, M.A. Khaleel, Model. Simul. Mater. Sci. Eng. 20 (2012) 015011.

[17] S.B. Biner, S.Y. Hu, Acta Mater. 57 (2009) 2088–2097.

[18] S. Hu, C.H. Henager Jr., H.L. Heinisch, M. Stan, M.I. Baskes, S.M. Valone, J. Nucl. Mater. 392 (2009) 292–300.

[19] S. Hu, Y. Li, X. Sun, F. Gao, R. Devanathan, C.H. Henager Jr., M.A. Khaleel, Int. J. Mater. Res. 101 (2010) 515–522.

[20] Y. Li, S. Hu, R. Montgomery, F. Gao, X. Sun, Nucl. Instrum. Meth. Phys. Res. Sect. B (Beam Interactions with Materials and Atoms) 303 (2013) 62–67.

[21] P.C. Millett, A. El-Azab, D. Wolf, Comput. Mater. Sci. 50 (2011) 960–970.

[22] P.C. Millett, M.R. Tonks, S.B. Biner, L. Zhang, K. Chockalingam, Y. Zhang, J. Nucl. Mater. 425 (2012) 130–135.

[23] P.C. Millett, M. Tonks, S.B. Biner, J. Appl. Phys. 111 (2012).

[24] S. Hu, A.M. Casella, C.A. Lavender, D.J. Senor, D.E. Burkes, J. Nucl. Mater. 462 (2015) 64–76.

[25] L. Liang, Z.G. Mei, Y.S. Kim, B. Ye, G. Hofman, M. Anitescu, A.M. Yacout, Comput. Mater. Sci. 124 (2016) 228–237.

[26] S.Y. Hu, D.E. Burkes, C.A. Lavender, D.J. Senor, W. Setyawan, Z.J. Xu, J. Nucl. Mater. 479 (2016) 202–215.

[27] J. Rest, G.L. Hofman, ANL/ET/PP–84776, 1994.

[28] J.A. Turnbull, R.M. Cornell, J. Nucl. Mater. 41 (1971) 156–160.

[29] J.A. Turnbull, J. Nucl. Mater. 38 (1971) 203–212.

[30] M.H. Wood, J. Nucl. Mater. 82 (1979) 264–270.

[31] J. Rest, J. Nucl. Mater. 321 (2003) 305–312.

[32] R.S. Nelson, J. Nucl. Mater. 25 (1968) 227–232.

[33] J. Rest, A.W. Cronenberg, J. Nucl. Mater. 150 (1987) 203–225.

[34] J. Rest, G.L. Hofman, J. Nucl. Mater. 210 (1994) 187–202.

[35] A.G. Khachaturyan, Theory of Structural Transformations in Solids, Wiley, New York, 1983.

[36] S.Y. Hu, L.Q. Chen, Acta Mater. 49 (2001) 1879–1890.

[37] L. Liang, Z.-G. Mei, A.M. Yacout, Comput. Mater. Sci. 138 (2017) 16–26.

[38] J.P. Simmons, C. Shen, Y. Wang, Scripta Mater. 43 (2000) 935–942.

[39] Z.-G. Mei, L. Liang, Y.S. Kim, T. Wiencek, E. O’Hare, A.M. Yacout, G. Hofman, M. Anitescu, J. Nucl. Mater. 473 (2016) 300–308.

[40] J. Rest, J. Nucl. Mater. 402 (2010) 179–185.

[41] J. Rest, J. Nucl. Mater. 407 (2010) 55–58.

[42] J. Spino, J. Rest, W. Goll, C.T. Walker, J. Nucl. Mater. 346 (2005) 131–144.

[43] L. Pagano, A.T. Motta, R.C. Birtcher, J. Nucl. Mater. 244 (1997) 295–304.

[44] L.Q. Chen, J. Shen, Comput. Phys. Commun. 108 (1998) 147–158.

[45] Y.B. Miao, K. Mo, B. Ye, L. Jamison, Z.G. Mei, J. Gan, B. Miller, J. Madden, J.S. Park, J. Almer, S. Bhattacharya, Y.S. Kim, G.L. Hofman, A.M. Yacout, Scripta Mater. 114 (2016) 146–150.

[46] D. Yun, M.A. Kirk, P.M. Baldo, J. Rest, A.M. Yacout, Z.Z. Insepov, J. Nucl. Mater. 437 (2013) 240–249.

[47] B.D. Miller, University of Wisconsin-Madison, University of Wisconsin-Madison, 2010.

[48] B.D. Miller, J. Gan, D.D. Keiser Jr., A.B. Robinson, J.F. Jue, J.W. Madden, P.G. Medvedev, J. Nucl. Mater. 458 (2015) 115–121.

[49] J. Gan, D.D. Keiser, B.D. Miller, A.B. Robinson, J.F. Jue, P. Medvedev, D.M. Wachs, J. Nucl. Mater. 424 (2012) 43–50.

[50] J. Gan, B.D. Miller, D.D. Keiser, A.B. Robinson, J.W. Madden, P.G. Medvedev, D. M. Wachs, J. Nucl. Mater. 454 (2014) 434–445.

[51] J. Gan, D.D. Keiser, B.D. Miller, A.B. Robinson, D.M. Wachs, M.K. Meyer, J. Nucl. Mater. 464 (2015) 1–5.

[52] J. Rest, G.L. Hofman, I.I. Konovalov, A.A. Maslov, ANL/ET/CP-97352, 1998.

[53] H.-X. Xiao, C.-S. Long, Chinese Phys. B 23 (2014) 020502.
