# 📄 PDF Parsing Result

**File:** `/Volumes/openclaw记忆/Zotero_storage/storage/A8L8V29I/Beeler et al._2020_A improved equation of state for Xe gas bubbles in γU-Mo fuels.pdf`
**Backend:** `pipeline`
**Pages:** 0 to end
**Formula Recognition:** ❌ Disabled
**Table Recognition:** ✅ Enabled

---

# A improved equation of state for Xe gas bubbles in U-Mo fuels

Benjamin Beeler a, b, \* , Shenyang Hu c , Yongfeng Zhang b , Yipeng Gao

![](images/9a1e4b165dff4c72f889da39ffcaedc294526164aa88d824ec84f1956eb133af.jpg)

a North Carolina State University, Raleigh, NC, 27607, USA

b Idaho National Laboratory, Idaho Falls, ID, 83415, USA

c Pacific Northwest National Laboratory, Richland, WA, 99354, USA

## a r t i c l e i n f o

Article history:   
Received 11 July 2019   
Received in revised form   
2 December 2019   
Accepted 16 December 2019   
Available online 20 December 2019

## a b s t r a c t

A monolithic fuel design based on a UeMo alloy has been selected as the fuel type for conversion of the United States High-Performance Research Reactors (HPRRs). An issue with UeMo monolithic fuel is the large amount of swelling that takes place during operation. The accurate prediction of fuel evolution under irradiation requires implementation of correct thermodynamic properties into mesoscale and continuum level fuel performance modeling codes. However, the thermodynamic properties of the fission gas bubbles (such as the relationship among bubble size, equilibrium Xe concentration, and bubble pressure) are not well known. This work studies Xe bubbles in U-Mo from a diameter of 3 nm up gto 8.5 nm and from 400 K up to 700 K. The energetic relationship of Xe bubbles with regard to voids and Xe substitutional atoms is described. The transition is also determined for when a bubble becomes overpressurized. Finally, an equation of state is fit to the pressure as a function of molar volume and temperature.

Published by Elsevier B.V.

## 1. Introduction

The United States High-Performance Research Reactor (USHPRR) program targets replacing current highly enriched uranium (HEU) fuel in high power research reactors with low enriched uranium (LEU) fuel [1]. In order to achieve a reduced enrichment in these fuel types, there is the requirement for increased uranium density. One way this is achieved is by utilizing  stabilized uragnium alloys with 10 wt% or less alloy content. The fuel design being pursued under the USHPRR program is a uranium-molybdenum (UeMo) monolithic foil, with a zirconium (Zr) diffusion barrier in Al clad.

An issue with UeMo monolithic fuel is the large amount of swelling that takes place during operation [2]. Such swelling needs to be stable and predictable up to high fission densities. Research reactor fuel types based on UeMo are unique in their ability to stably retain fission gases to high fission densities, and as such there is a relatively high content of fission gas and of fission gas bubbles within the fuel matrix. The importance of swelling in addition to the unique fuel environment has led to a variety of experimental studies characterizing the swelling behavior in UeMo fuels [3e6] which has led to the development of a swelling correlation as a function of fission density from Argonne National Laboratory (ANL correlation) [7] and Idaho National Laboratory [8]. A 2015 post-irradiation examination (PIE) report [9] from Williams et al. showed higher swelling in Ue10Mo fuels at fission densities much lower than previously observed. This accelerated fuel swelling behavior could lead to early fuel failure and was not captured by the ANL correlation. As such, a more mechanistic fuel swelling model is needed in order to predict swelling behavior of UeMo fuels under both typical operating conditions, as well as transients, accident scenarios and different reactor environments.

Recently, substantial effort has been made on mesoscale models to predict the swelling behavior of UeMo fuels [10e17]. These models rely on phase-field and/or rate theory descriptions of microstructure evolution of material systems in order to model swelling on realistic timescales. These simulation methodologies include a number of parameters that are either fit to limited experimental data, calculated from lower length scale modeling methodologies, or assumed based on other material systems. However, the thermodynamic properties of the bubbles (such as the relationship among bubble size, equilibrium Xe concentration, and bubble pressure) are not well known. Implementation of correct thermodynamic properties into mesoscale and continuum level fuel performance modeling codes is crucial for the accurate prediction of fuel behavior under irradiation, particularly in regard

to swelling.

A number of molecular dynamics investigations have been performed targeted at elucidating fundamental Xe bubble properties in UeMo. Xiao et al. [18,19] studied UeMo-Xe bubbles of less than 2 nm in diameter, analyzing the pressure and induced swelling with increasing Xe content. They also modeled bubble coalescence as a function of temperature. They observed interesting effects such as a decrease in bubble pressure and Xe density with increasing number of Xe atoms present in the bubble. The origin of such anomalous effects is unclear. Recently, Hu, et al. developed an equation of state of Xe bubbles in UeMo at 500 K by determining Xe density and pressure [20]. They also studied dislocation emission from fission gas bubbles and suggested a possible cause of the face-centered cubic fission gas superlattice due to the anisotropic tensile stress surrounding the bubbles. However, this work was restricted to a single temperature and very small bubbles of diameter less than 2 nm. Although this is typically the size of bubbles found in the fission gas superlattice [7], after grain refinement the superlattice bubbles coalesce into larger bubbles, up to 1 m in diameter [9]. The inclusion of only small, highly presmsurized bubbles into an equation of state that governs all possible Xe bubble configurations excludes a significant amount of information. Therefore, it is valuable to extend the previous work that was performed to investigate much larger systems and a wider variety of Xe concentrations within bubbles in order to incorporate as much information as possible to facilitate mesoscale models of fission gas swelling and microstructural evolution in UeMo fuels.

This work studies Xe bubbles in U-Mo from a diameter of 3 nm gup to 8.5 nm and from 400 K up to 700 K. The energetic relationship of Xe bubbles with regard to voids and Xe substitutional atoms is described. The transition is also determined for when a bubble becomes over-pressurized. Finally, an equation of state is fit to the pressure as a function of molar volume and temperature.

## 2. Computational details

Molecular dynamics simulations are performed utilizing the LAMMPS [21] software package and the UeMo-Xe embedded atom method (EAM) interatomic potential [22]. This potential is capable of describing the body-centered cubic phase of UeMo alloys, and is presently the only potential capable of describing the UeMo-Xe ternary system. The potential is able to reproduce the stable structure, modulus of elasticity, room-temperature density and melting temperature of Ue10Mo. Additionally, this potential is able to reproduce a number of properties of pure Xe gas and facecentered cubic Xe. However, it is unknown the level of accuracy of the defect properties of Xe in UeMo with this potential, as no such experimental data is available, and the inherent mechanical instability in density functional theory simulations makes such examinations untenable. The authors would recommend validation of this potential with ab initio molecular dynamics simulations; however, such a study was beyond the scope of this project and additionally no such study of the kind has been performed.

A supercell of 40  40  40 body-centered cubic (bcc) unit cells (128,000 U atoms) is generated, and approximately 22% of U atoms are randomly switched to Mo atoms, yielding a Ue10Mo (10 wt percent) alloy in the bcc structure. Relaxation of the bulk system is performed in an NPT-ensemble, relaxing each x, y, and z component individually, with a damping parameter of 0.1. A Langevin thermostat in the Gronbech-Jensen-Farago [23,24] formalism is utilized with the damping parameter set to 0.01 ps. Temperatures of interest are 400 K, 500 K, 600 K and 700 K, which span the realistic operating temperatures for UeMo fuels [8]. The system is allowed to equilibrate for 200 ps at a given temperature, and subsequently a void is constructed by deleting a sphere of atoms from the center of the supercell. This void is relaxed for 200 ps under the same simulation conditions described above. Larger supercells were investigated in specific cases to ensure that no artifacts due to the size of the supercell were present in the simulations. No statistically significant changes to bubble energies or pressures were observed due to changes in the supercell size.

In order to analyze bubbles, two sets of simulations are performed: an NPT and an NVT ensemble. An NVT ensemble is utilized to mimic a bubble in a very large system that effectively exerts a resistive pressure on the bubble. This allows for the calculation of a Xe bubble pressure and a subsequent equation of state based on the density of the bubble. The NPT ensemble allows the system volume to change and to determine the transition between an underpressurized bubble, where the volume of the system is less than the equilibrium volume of a Ue10Mo alloy, to an over-pressurized bubble, where the volume of the system is greater than the equilibrium volume of a Ue10Mo alloy. The target pressure for the NPT ensemble is 0.

The generation of bubbles is performed by inserting Xe atoms into the void one at a time, while relaxation of the system is ongoing. For smaller bubbles, the insertion rate is as low as one Xe atom per 17.5 ps. For the largest voids/bubbles investigated, the insertion rate is higher, with one Xe atom inserted every 0.8 ps. This is modified according to the bubble size in order to ensure a similar rate of Xe to vacancy ratio change as a function of time. In order to track the bubble size, two atoms (one on either side of the void) are tracked throughout the simulation and the distance between the two atoms is classified as the diameter of the bubble. The pressure of the bubble is determined by computing the stress per atom on each of the Xe atoms in the system, summing the individual components of the stress tensor over all Xe atoms and finally dividing by the degrees of freedom (three) and the volume of the bubble.

Two unique formalisms of the equation of state (EOS) are fit to the molecular dynamics data, both of which will be discussed in greater detail below. A minimization script is utilized to fit the EOS for each functional form to the determined pressure and molar volume data from the molecular dynamics simulations. The data is input into the script, and the relative error is summed and utilized to optimize the EOS, iterating by providing a random step to each of the fitting coefficients and only accepting the iteration if the total relative error is reduced.

## 3. Results

3.1. Surface, formation and binding energies of voids and bubbles

In order to generate bubbles in the methodology outlined above, voids of varying size must be generated. This allows for the calculation of a void surface area as a function of radius, and the surface energy can be determined from equation (1)

$$
\tag{1}
$$

where E is the potential energy per atom of the system with a void, E is the potential energy per atom of the perfect crystal of UeMo, A is the total surface area of the void and N is the number of atoms in the system with a void. The void surface energy is shown in Fig. 1 as a function of void radius. It should be emphasized that all of these systems are random solid substitutional alloys of Ue10Mo in an NVT ensemble unless specifically mentioned otherwise. It can be observed that the void surface energy converges above a radius of 1.5 nm for all temperatures to a value of approximately 1.2 J/m2 . This is similar in magnitude to, albeit slightly lower than, the average surface energy for UeMo free surfaces as determined in

![](images/17ef20478397c940ef78ba6ed69d8b0a19b579af1676b90ef69dc0b7956121af.jpg)  
Fig. 1. Void surface energy as a function of radius for voids in Ue10Mo from 400 K to 700 K.

Ref. [25], which utilized an Angular-Dependent potential [26] capable of describing the UeMo system. It is expected that different interatomic potentials would yield different values for the void surface energy. However, this calculation gives confidence that voids are reaching a relaxed, converged state to provide a foundation for insertion of Xe atoms to create bubbles and that all void radii in this system yield a similar energetic landscape for analysis.

An example bubble is shown in Fig. 2. Atoms are progressively inserted into a void, leading to an increasing Xe to vacancy ratio as a function of simulation time, resulting in a highly pressurized Xe bubble at the end of the simulation. The maximum Xe/vacancy ratio obtained is approximately 0.5, which was observed to be sufficiently high to obtain a bubble pressure of a few GPa, which ensures investigation of all likely bubble pressures in these systems.

The bubble formation energy can be calculated by the following equation:

$$
\tag{2}
$$

where Ebub is the energy of the system with a bubble, Nvoid is the number of atoms in the system with a void, Esys is the energy of the bulk system (no voids or bubbles) and Nsys is the number of atoms in the bulk system. The energy per atom of Xe in its reference state is neglected in this calculation, as the energy is sufficiently small ( < 0.01 eV/at) to result in only statistically insignificant changes to formation energies. In order to compare different bubble sizes to one another, a relative bubble energy is defined as the bubble formation energy less the void formation energy. With this formalism, only the excess energy attributable to the Xe atoms and their subsequent influence on the energy of the system is analyzed. This allows for the investigation of energetic effects of Xe bubbles for different bubble sizes. The relative bubble energy at 500 K is shown in Fig. 3 for bubbles of diameter 3.1, 4.4, 5.8, 7.1 and 8.5 nm.

![](images/6c6b718c4e6c641f3120bf1f0089021a1d75130ed24f7683895e836aa1face18.jpg)  
Fig. 3. Relative bubble energy at 500 K as a function of Xe/vacancy ratio for bubbles of five unique sizes. Bubble diameters labeled, units in nm.

For all bubbles, there is a region below a Xe/vacancy ratio of 0.15 where additional Xe atoms inserted into the bubble produce no noticeable change in the relative bubble energy, which corresponds to a Xe molar volume of approximately 80 cm3 /mol. There can even exist a slight reduction in system energy due to Xe aiding in the faceting of the low pressure bubble. Above a Xe/vacancy ratio of approximately 0.15, the relative bubble energy displays a quadratic increase as a function of the Xe/vacancy ratio. The specific nature of the quadratic growth is dependent upon the bubble size, where a larger bubble displays a more rapid increase in relative bubble energy. This shows that it is much more difficult to obtain a high Xe/ vacancy ratio in large bubbles compared to small bubbles.

![](images/b75584a22f199e98174ffd25a91d9086143b326705c236ffa491e3a3351765a6.jpg)  
Fig. 2. A Xe bubble at 500 K with a diameter of 7.1 nm in Ue10Mo as a function of time. Starting from a void (a), to a Xe/vacancy ratio of 0.16 (b), and a Xe/vacancy ratio of 0.32 (c). Red atoms are U, blue atoms are Mo and green atoms are Xe.

Point defect formation energies and binding energies in Ue10Mo at 400 K. Units in eV.
<table><tr><td>Defect Type</td><td>Formation Energy</td><td>Binding Energy</td></tr><tr><td>Vacancy</td><td>1.6</td><td></td></tr><tr><td>Interstitial</td><td>1.1</td><td></td></tr><tr><td>Xe substitutional</td><td>6.1</td><td></td></tr><tr><td>Divacancy</td><td>2.1</td><td>-1.2</td></tr><tr><td>Xe sub-vac pair</td><td>7.4</td><td>-0.4</td></tr></table>

The energetic preference for adding or removing a Xe atom into an existing bubble can be investigated by looking at the binding energy of the nth Xe atom in a given bubble. The binding energy of the nth Xe atom in a given bubble can be defined as:

$$
\tag{3}
$$

where E(n) is the energy of a system with a bubble with n Xe atoms, E (n-1) is the energy of system with a bubble with n-1 Xe atoms, ESubXe is the formation energy of a Xe substitutional, and EVac is the formation energy of a monovacancy. The addition of a vacancy indicates the two systems of comparison with a fixed bubble size: 1) a bubble with m vacancies and n 1 Xe, and a substitutional Xe atom, 2) a bubble with m vacancies and n Xe, and a monovacancy in the lattice. The Xe substitutional reference state was chosen as this is the low energy defect configuration for Xe in Ue10Mo. This was the assumed configuration based on density functional theory calculations in pure bcc U [27]. However, specific calculations utilizing the interatomic potential were undertaken to verify this information. A simulation supercell of 1024 atoms (8  8x8 unit cells) was utilized to calculate the energy, at 400 K, of bcc U, bcc Mo and bcc Ue10Mo. Due to the large number of possible unique configurations of a random solid substitutional alloy, one thousand unique simulations were performed to calculate the energies of alloy systems and ensure converged energies. The formation energy of a Ue10Mo alloy was found to be 0.18 eV/at. Point defects investigated included vacancy, interstitial, divacancy, Xe substitutional, Xe interstitial and a Xe substitutional-vacancy pair. To account for the non-zero formation energy in point defect calculations, equation (4) was utilized,

$$
\tag{4}
$$

where EalloyF is the total formation energy of an alloy of UeMo, and EdefF is the total formation energy of a UeMo alloy with a defect. Each of these total formation energies are calculated via equation (5)

$$
\tag{5}
$$

where ETot is the total energy of the system, EU is the energy per atom of bcc U, EMo is the energy per atom of bcc Mo, and NU and NMo are the number of U and Mo atoms in the system of interest, respectively. Subsequently, the Edef , which is the individual defect formation energy, can be calculated. The subsequent defect formation energies are presented in Table 1.

It should be noted that all defects are an average of both species, for example an interstitial could be either U or Mo, and this is an average over all 1000 unique simulations. The vacancy and interstitial defect energies are qualitatively coherent, based on what one would expect in bcc U [28], with a comparatively lower interstitial formation energy. The Xe substitutional energy is 6.1 eV. The Xe interstitial energy is omitted from this table, as it was observed that Xe interstitials transformed into a Xe substitutional and a matrix interstitial. There exists strong binding between individual vacancies (negative binding energy indicating attraction here) as well as a strong binding between Xe substitutionals and vacancies. The value of 6.1 eV for a Xe substitutional was utilized in equation (3).

![](images/1fdc078c8e852e1dfbef34a582c08e78e8d27bd5163fb9c1cc05eeb084979fa9.jpg)  
Fig. 4. Binding energy of the nth Xe atom in a bubble as a function of the Xe/vacancy ratio.

The binding energy of the nth Xe atom in a given bubble is shown in Fig. 4, for all bubble sizes investigated. It can be seen that the binding energy is negative for all Xe/vacancy ratios included in this study, illustrating that it is always favorable for a Xe atom to reside in a bubble, regardless of existing Xe/vacancy ratio, rather than to reside in the bulk UeMo alloy. The binding energy does grow less strong with increasing Xe/Vac ratio, as would be expected, but there is no observed scenario where it is energetically favorable for a Xe atom to reside in the bulk instead of as an atom in the bubble. Extrapolating a quadratic fit to a binding energy of zero yields a Xe/Vac ratio of 0.94, where it would be energetically unfavorable for a Xe atom to reside within the bubble. However, it is very likely that as Xe/Vac ratio increases, lattice deformation around the bubble will become dramatic, altering the binding energy behavior as a function of Xe content. It should also be noted that data for all bubble sizes is included in this graph as there is no observable difference in Xe binding energy as a function of Xe/Vac ratio for different bubble sizes.

## 3.2. Bubble pressurization transition

In order to determine the under-to over-pressurized transition, simulations in an NPT ensemble at 400 K are performed to allow the volume to change as a function of time. The equilibrium volume of a Ue10Mo alloy is determined prior to the introduction of a void and subsequent introduction of Xe atoms. A relaxed system with a void exhibits a reduced volume compared to the equilibrium system. As Xe is introduced into the void/bubble, the Xe exerts an outward force on the system. As progressively more Xe is added into the bubble, the pressure becomes significant enough to expand the bulk system and increase the supercell volume. This work defines the transition from under-to over-pressurized bubbles as the point where the volume of the system with a Xe bubble is equal to the equilibrium volume of a system with no void or bubble. Thus, at a lower than equilibrium Xe/vacancy ratio the system will have a slightly lower volume than the equilibrium system, and at a higher than equilibrium Xe/vacancy ratio the system will have a slightly higher volume than the equilibrium system. The results are shown in Fig. 5. The system becomes over-pressurized at different Xe/vacancy ratios depending upon the bubble diameter. For smaller bubbles, the transition occurs at a lower Xe/vacancy ratio. However, for the bubbles investigated, the range of variance for all bubble sizes is somewhat small. The transition occurs as early as a 0.13 Xe/ vacancy ratio for a bubble of diameter 3.1 nm, and as late as a 0.20 Xe/vacancy ratio for a bubble of diameter 8.5 nm. Proceeding the transition, the volume increase is related to the size of the bubble as well, as larger bubbles see significantly more rapid volume increase with a given increase in the Xe/vacancy ratio. The quantitative value of the relative volume as a function of Xe/vacancy ratio will change with changes in supercell size volume, but the qualitative relationships will not vary. Supercell size effects were investigated in limited cases to ensure the qualitative relationships held and that the transition point was converged.

![](images/24d93441d1a876bcfe4934f83024c514779bb5d42862470e39504902551b93a3.jpg)  
Fig. 5. The normalized volume of a system with a bubble as a function of Xe/vacancy ratio for five unique bubble sizes. Bubble diameters labeled, units in nm.

An equilibrium bubble can be understood as the bubble existing at the under-to over-pressurized transition. Typically the pressure of such a bubble is determined by satisfying the Young-Laplace equation, often denoted by equation (6),

$$
\tag{6}
$$

where  is the surface energy and R is the radius of the bubble. gAlthough the Young-Laplace equation was formulated to describe the interface across fluids, it is commonly used to describe gas bubbles in solids. To verify if the Young-Laplace relationship holds for Xe bubbles in UeMo, the predicted equilibrium pressure from equation (6) is determined and compared to the computationally calculated equilibrium pressure using the Xe/vacancy ratio from

Predicted pressure based on Eq. (6), calculated pressure, and the subsequent difference. Units of pressure in GPa.
<table><tr><td>Diameter (nm)</td><td>Predicted</td><td>Calculated</td><td>Difference</td></tr><tr><td>3.1</td><td>1.39</td><td>0.24</td><td>1.15</td></tr><tr><td>4.4</td><td>1.07</td><td>0.31</td><td>0.77</td></tr><tr><td>5.7</td><td>0.82</td><td>0.43</td><td>0.38</td></tr><tr><td>7.1</td><td>0.65</td><td>0.43</td><td>0.22</td></tr><tr><td>8.5</td><td>0.55</td><td>0.43</td><td>0.13</td></tr></table>

![](images/ab2e9d797f3c825e25c7f984e25ae4a0205c96cfcdf38263b7c78f8552c7be1a.jpg)  
Fig. 6. Predicted bubble pressure from Eq. (6) minus the calculated pressure from molecular dynamics as a function of bubble size.

Fig. 5 where the normalized volume is 1. Interestingly, the results do not agree particularly well. The difference in the predicted versus calculated pressures as a function of bubble diameter is shown in Table 2. The difference in predicted versus calculated is most pronounced for small bubbles, however this difference is reduced as the bubble size increases. For all bubble sizes, the predicted pressure is greater than the calculated pressure. Thus, it is possible that the Young-Laplace equation does not hold for bubbles less than 10 nm in diameter in this system, however, it may apply for bubbles larger than 10 nm in diameter.

To verify this hypothesis, two larger bubbles were investigated to determine if the predicted and calculated equilibrium pressures converged as bubble size increases. In order to accommodate larger bubbles, a larger supercell (60  60  60, 432,000 atoms) is utilized. Bubbles with a 11.2 nm diameter and a 12.6 nm diameter are investigated in an NPT ensemble at 0 pressure and 400 K, with a comparable Xe/vacancy ratio rate of change to the previous bubbles included in this study. The results of this work are included in Fig. 6. As the bubble radius increases, the difference between predicted and calculated pressure continues to decrease, with each pressure converging to an identical value for large bubbles. An exponential function is fit to this data, (with an R2 value of 0.96), which shows that as bubble radius increases, the discrepancy between predicted and calculated equilibrium pressure exponentially decays. Given this information, we propose a modification to the Young-Laplace equation specifically for Xe bubbles in UeMo, although this relationship may hold for other gas bubbles in other material systems. The equilibrium pressure as a function of bubble radius should be defined by equation (7).

$$
\tag{7}
$$

where  equal 1.2 J/m2 (from Fig. 1), A equals 4.94 and B gequals 0.87 for the UeMo-Xe system. This equation decays to the Young-Laplace equation for bubble radii greater than 6 nm. It should be emphasized that this equation was not fit to data for bubbles smaller than 3 nm in diameter, and as such the authors make no conclusions regarding the validity of this expression for smaller bubbles. Additionally, it is possible that there exists a temperature dependence of this function, but since the surface energy does not vary over the temperature range of interest, it is assumed that the relationship denoted in equation (7) shows only

minimal variation.

## 3.3. Xe bubble equation of state in UeMo

The equation of state (EOS) can be determined by tracking the pressure inside the bubble and the bubble size as a function of the number of Xe atoms present in the bubble while the system is equilibrated in an NVT ensemble, which provides a pressure versus density relationship. This data can be fit to an EOS that provides a generalized function predicting the relationship between pressure, temperature and molar volume. In order to extend the applicability of the EOS, temperatures from 400 K to 700 K are analyzed, for all bubble sizes previously mentioned. No restrictions are imposed on the fitting parameters for each individual EOS.

## 3.3.1. Kaplun EOS

An EOS for Xe bubbles is taken from Kaplun [29], which was also utilized in the work of Hu [20],

$$
\tag{8}
$$

where R is the gas constant for Xe (8.314 J/mol-K [29]), T is the temperature in K, P is the pressure in MPa, v is the molar volume in cm3 /mol, and a, b, and c are fitting parameters. This EOS reduces to the well known van der Waals EOS when b c. It appears that Hu [20] mislabeled the fitting parameters in their equation, according to the units of the parameters. Hu et al. have confirmed that the correct EOS parameters from their work are a 259,780 J-cm3 / mol2 , b ¼ 18.928 cm3 /mol and c ¼ 280.658 cm3 /mol [20]. These parameters are utilized as the starting guess for the fitting procedure in this work to obtain an optimized EOS.

The subsequent fit, with and without molecular dynamics data, is shown in Fig. 7. An inlay is included for molar volumes from 20 to 100 cc/mol, to better illustrate the high pressure data. The data heavily overlaps and only shows minor differences as a function of temperature and as such the individual isotherms are difficult to distinguish. For clarity, the MD data is removed in Fig. 7b and the optimized EOS is displayed on a log/linear scale to emphasize the differences between the individual isotherms. The optimized coefficients for the equation of state are a 870912.08 J-cm3 / mol2 , b  27.133 cm3 /mol, c  88.987 cm3 /mol. Compared to the work of Hu, this is a significant decrease in the parameter a, a slightly larger value in b, and a substantial decrease in c. Although the work of Hu utilized the same interatomic potential as this work, the area of interest with regard to bubble properties was dramatically different. Hu investigated small bubbles, less than 2 nm in diameter, at high pressures, greater than 2 GPa and up to 8 GPa. They did not include bubbles with larger radii or low density Xe gas in their fitting. As such, it is expected that there would exist differences in the results for a fitted EOS.

![](images/83223f5080cc1b8096f3efbc3302bd969ffbaad450833e3cfda43cb1ae46d4f5.jpg)

Considering the fitted parameters, emphasis should be drawn to the negative magnitude of the a parameter. In the original van der Waals formalism, the a/v2 term was included to provide for intermolecular attraction. Typical values of a are positive [29], indicating net attraction between molecules and a reduction in the overall pressure. However, in this study, the a parameter is negative, indicating additional repulsion leading to an increase in the pressure of the system. This could potentially be due to the fact that these are generally high pressure systems, or this could be an aspect of the interaction of the Xe gas with the UeMo matrix. Kaplun states that their derivation of a modified van der Waals EOS loses applicability in regimes of high pressure and density, and they only compare to Xe pressures of 5 MPa and below, which would be considered extremely low for this work. Regardless, at very low gas densities, the a/v2 term vanishes and this equation converges to the ideal gas law. Thus, although the magnitude of a is atypical for isolated gases, it is deemed representative of high pressure Xe bubbles in UeMo in this work.

The accuracy of the EOS fit can be quantified in a number of ways. A root-mean squared deviation (RMSD) is likely not the best metric, due to the large range of pressures in the data set covering multiple orders of magnitude. Thus, it can be better to gauge accuracy via a normalized RMSD (NRMSD), which is defined by dividing the RMSD by the range (the difference of the maximum and minimum) of the dataset, or via a total relative error, which is the summation of the relative error of each individual data point divided by the total number of data points. Both metrics will be used here, with emphasis placed on total relative error. The NRMSD of the optimized Kaplun EOS compared to the MD data is 6.5% and the total relative error is 10.3%. Considering that the pressure in this dataset varies over 3 orders of magnitude and the temperature varies over 300 K, this is considered excellent agreement. The NRMSD of the previously optimized EOS from Hu calculated with respect to the MD data in this work is 9.8% and the total relative error is 16.5%. Thus, using the relative error as the standard measure of accuracy, this represents approximately a 6% improvement over the most finely calibrated EOS for Xe bubbles in UeMo in the literature, as well as a dramatic expansion on the range of applicability, with respect to bubble size, pressure and temperature.

b)  
![](images/7fbb6c86f32abe02fbf4a8b92d253b77d4848e618db5243067e34574cde49d69.jpg)  
Fig. 7. An equation of state (EOS) based on a modified van der Waals equation from Kaplun for Xe bubbles in Ue10Mo from 400 K to 700 K (a) compared to molecular dynamics data and (b) without molecular dynamics data.

## 3.3.2. Virial EOS

Due to the atypical nature of the a parameter in 3.3.1, an additional equation of state formalism was utilized to investigate the possibility of alternate functional forms better representing the molecular dynamics data. A virial equation of state is utilized, expanded to the third order with respect to volume and the second order with respect to temperature, as is shown in equation (9),

$$
\tag{9}
$$

where A ¼ 1, and B, C and D are temperature dependent Taylor series of 1/T (B ¼ b0 þ b1/T þ b2/T2 , C ¼ c0 þ c1/T þ c2/T2 and D ¼ d0 þ d1/T  d2/T2 ), leading to nine unique fitting parameters. The virial equation is a general function relating pressure, molar volume and temperature that can be directly derived from statistical mechanics [30].

The subsequent fit, with and without molecular dynamics data, is shown in Fig. 8. An inlay is included for molar volumes from 20 to 100 cc/mol. The MD data is removed in Fig. 8b and the optimized EOS is displayed on a log/linear scale to emphasize the differences between the individual isotherms. The optimized coefficients are shown in Table 3. The NRMSD of the optimized Virial EOS compared to the MD data is 5.7% and the total relative error is 9.0%. This is an increase in accuracy over the modified van der Waals EOS from this work by 1.3% and from Hu by 7.5%, utilizing total relative error to judge accuracy. Thus, the virial EOS provides the most accurate description of molecular dynamics information in this work and is put forth as the most accurate EOS available for description of Xe bubbles in UeMo over this temperature and pressure range. However, comparable accuracy is achieved with the modified van der Waals EOS and the reader is encouraged to utilize their preferred functional form.

![](images/668c3c823aea096e8cbc1e91a4867d7cd55967473194c19d8ff8ce1cfc373406.jpg)

Virial equation of state (Eq. (9)) parameters for Xe bubbles in UeMo.
<table><tr><td>Parameter</td><td>Value</td></tr><tr><td>b</td><td>197.229 cm/mol</td></tr><tr><td>b1</td><td>120307.145 cm-K/mol</td></tr><tr><td>b</td><td>60.555 cm²-K²/mol</td></tr><tr><td>Co</td><td>-22038.723 cm/mol2</td></tr><tr><td>C1</td><td>2292.793 cm-K/mol2</td></tr><tr><td>C2</td><td>-117.564 cm-K²/mol²</td></tr><tr><td>do</td><td>1030015.045 cm/mol</td></tr><tr><td>d1</td><td>-5.200 cm-K/mol</td></tr><tr><td>d</td><td>-280.677cm-K²/mol²</td></tr></table>

## 4. Conclusions

This work investigated Xe bubbles in U-Mo from a diameter of g3 nm up to 8.5 nm and from 400 K up to 700 K. The energetic relationship of Xe bubbles with regard to voids and Xe point defects is described. The relative energy of a bubble increases quadratically as a function of Xe/vacancy ratio, with larger bubbles exhibiting a more rapid increase in energy. The binding energy of Xe atoms is negative, indicating attraction, for all bubbles and all Xe/vacancy ratios investigated. This shows that the energy of a Xe atom in the UeMo lattice is sufficiently high, such that Xe will always want to reside in the bubble, regardless of bubble pressure investigated in this work. The under-to over-pressurized transition for bubbles is determined. This transition is below a Xe/vacancy ratio 0.2 for all bubbles in this work. A modification of the Young-Laplace equation is suggested to determine the equilibrium volume pressure of Xe bubbles in UeMo. Finally, two distinct equations of state were fit to the pressure as a function of molar volume and temperature for Xe in UeMo bubbles. The virial EOS variant represents an improvement in accuracy and extended applicability compared to a

b)  
![](images/69db649f2a62ac770c156fed92185620c2422877b86732b647b79ddb059ab361.jpg)  
Fig. 8. An equation of state (EOS) based on a virial expansion for Xe bubbles in Ue10Mo from 400 K to 700 K (a) compared to molecular dynamics data and (b) without molecular dynamics data.

previously developed EOS.

The knowledge that the Xe/vacancy ratio depends on the bubble size and optimally decreases with increasing bubble diameter is valuable, in that the assumption is typically made of a constant Xe/ vacancy ratio, regardless of bubble size. Also, the examined Xe/ vacancy ratios in this study are somewhat lower than the previous estimate of fission gas densities in bubbles in UeMo, although the pressures are similar in magnitude. A modification to the Young-Laplace equation will dramatically modify the suggested equilibrium state for small fission gas bubbles. The information provided in this work regarding bubble energetics, under-to over-pressurization transition, and an updated equation of state for Xe bubble in Ue10Mo can be directly utilized to improve the fidelity of mesoscale models that describe fission gas induced swelling in UeMo fuels.

## CRediT authorship contribution statement

Benjamin Beeler: Conceptualization, Methodology, Software, Formal analysis, Investigation, Writing - original draft, Project administration, Visualization. Shenyang Hu: Conceptualization, Methodology, Validation, Writing - review & editing. Yongfeng Zhang: Conceptualization, Methodology, Writing - review & editing, Supervision. Yipeng Gao: Conceptualization, Methodology, Writing - review & editing.

## Acknowledgement

This work was supported by the U.S. Department of Energy, Office of Material Management and Minimization, National Nuclear Security Administration, under DOE-NE Idaho Operations Office Contract DE-AC07-05ID14517. This manuscript has been authored by Battelle Energy Alliance, LLC with the U.S. Department of Energy. The publisher, by accepting the article for publication, acknowledges that the U.S. Government retains a nonexclusive, paid-up, irrevocable, worldwide license to publish or reproduce the published form of this manuscript, or allow others to do so, for U.S. Government purposes. This research made use of the resources of the High Performance Computing Center at Idaho National Laboratory, which is supported by the Office of Nuclear Energy of the U.S. Department of Energy and the Nuclear Science User Facilities.

## Appendix A. Supplementary data

Supplementary data related to this article can be found at https://doi.org/10.1016/j.jnucmat.2019.151961.

## References

[1] J. Snelgrove, G. Hofman, M. Meyer, C. Trybus, T. Weincek, Development of very-high density low enriched uranium fuels, Nucl. Eng. Des. 178 (1997) 119.

[2] G. Hofman, L. Walters, T. Bauer, Metallic fast reactor fuels, Prog. Nucl. Energy 31 (1997) 83.

[3] J. Rest, G. Hofman, Y. Kim, Analysis of intergranular fission-gas bubble-size distributions in irradiated uranium-molybdenum alloy fuel, J. Nucl. Mater. 385 (2009) 563.

[4] Y. Kim, G. Hofman, J. Rest, G. Shevlyakov, Characterization of Intergranular

Fission Gas Bubbles in U-Mo Fuel, Argonne National Laboratory, 2008. Tech. Rep. ANL-08/11.

[5] M. Meyer, G. Hofman, S. Hayes, C. Clark, T. Wiencek, J. Snelgrove, R. Strain, K. Kim, Low-temperature irradiation behavior of uranium-molybdenum alloy dispersion fuel, J. Nucl. Mater. 304 (2002) 221.

[6] Y. Kim, G. Hofman, J. Cheon, A. Robinson, D. Wachs, Fission induced swelling and creep of u-mo alloy fuel, J. Nucl. Mater. 437 (2013) 37.

[7] Y. Kim, G. Hofman, Fission product induced swelling of u-mo alloy fuel, J. Nucl. Mater. 419 (2011) 291.

[8] M. Meyer, B. Rabin, J. Cole, I. Glagolenko, W. Jones, J.-F. Jue, J.D. Keiser, C. Miller, G. Moore, H. Ozaltun, F. Rice, A. Robinson, J. Smith, D. Wachs, W. Williams, N. Woolstenhulme, Preliminary Report on U-Mo Monolithic Fuel for Research Reactors, Idaho National Laboratory, 2017. Tech. Rep. INL/EXT-17-40975.

[9] W. Williams, F. Rice, A. Robinson, M. Meyer, B. Rabin, Afip-6 Mkii Postirradiation Examination Summary Report, Idaho National Laboratory, 2015. Tech. Rep. INL/LTD-15-34142.

[10] L. Liang, Y. Kim, Z.-G. Mei, L. Aagesen, A. Yacout, Fission gas bubbles and recrystallization-induced degradation of the effective thermal conductivity in u-7mo fuels, J. Nucl. Mater. 511 (2018) 438.

[11] L. Liang, Z.-G. Mei, Y. Kim, M. Anitescu, A. Yacout, Three-dimensional phasefield simulations of intragranular gas bubble evolution in irradiated u-mo fuel, Comput. Mater. Sci. 145 (2018) 86.

[12] L. Liang, Z.-G. Mei, A. Yacout, Fission-induced recrystallization effect on intergranular bubble-driven swelling in u-mo fuel, Comput. Mater. Sci. 138 (2017) 16.

[13] L. Liang, Z.-G. Mei, Y. Kim, B. Ye, G. Hofman, M. Anitescu, A. Yacout, Mesoscale model for fission-induced recrystallization in u-7mo alloy, Comput. Mater. Sci. 124 (2016) 228.

[14] B. Ye, G. Hofman, A. Leenaers, A. Bergeron, V. Kuzminov, S.V. den Berghe, Y. Kim, H. Wallin, A modelling study of the inter-diffusion layer formation in u-mo/al dispersion fuel plates at high power, J. Nucl. Mater. 499 (2018) 191.

[15] S. Hu, V. Joshi, C. Lavender, A rate-theoryephase-field model of irradiationinduced recrystallization in umo nuclear fuels, J. Occup. Med. 69 (2017) 2554.

[16] S. Hu, D. Burkes, C. Lavender, V. Joshi, Effect of grain morphology on gas bubble swelling in umo fuels e a 3d microstructure dependent booth model, J. Nucl. Mater. 480 (2016) 323.

[17] S. Hu, D. Burkes, C. Lavender, D. Senor, W. Setyawan, Z. Xu, Formation mechanism of gas bubble superlattice in umo metal fuels: phase-field modeling investigation, J. Nucl. Mater. 479 (2016) 202.

[18] H.-X. Xiao, R. Tang, X.-F. Tian, C.-S. Long, Molecular dynamics simulation of xe behavior in u-mo alloys fuel, Chin. Phys. Lett. 31 (2014), 047101.

[19] H.-X. Xiao, C.-S. Long, X.-F. Tian, S. Li, Atomistic simulations of the small xenon bubble behavior in uemo alloy, Mater. Des. 74 (2015) 55.

[20] S. Hu, W. Setyawan, V. Joshi, C. Lavender, Atomistic simulations of thermodynamic properties of xe gas bubbles in u10mo fuels, J. Nucl. Mater. 490 (2017) 49.

[21] S. Plimpton, Fast parallel algorithms for short-range molecular dynamics, J. Comput. Phys. 117 (1995) 1e19.

[22] D. Smirnova, A. Kuksin, S. Starikov, V. Stegailov, Z. Insepov, J. Rest, A. Yacout, A ternary eam interatomic potential for u-mo alloys with xenon, Model. Simul. Mater. Sci. Eng. 21 (2013), 035011.

[23] N. Gronbech-Jensen, O. Farago, A simple and effective verlet-type algorithm for simulating Langevin dynamics, Mol. Phys. 111 (2013) 983.

[24] N. Gronbech-Jensen, N. Hayre, O. Farago, Application of the g-jf discrete-time thermostat for fast and accurate molecular simulations, Comput. Phys. Commun. 185 (2014) 524.

[25] B. Beeler, Y. Zhang, Y. Gao, An atomistic study of grain boundaries and surfaces in gamma u-mo, J. Nucl. Mater. 507 (2018) 248.

[26] D. Smirnova, A. Kuksin, S. Starikov, V. Stegailov, Atomistic modeling of the self-diffusion in gamma u and gamma u-mo, Phys. Met. Metallogr. 116 (2015) 445.

[27] B. Beeler, C. Deo, M. Baskes, M. Okuniewski, Atomistic investigations of intrinsic and extrinsic point defects in bcc uranium, Effects Radiat Nuc Mater: STP 1547 25 (2012) 231.

[28] B. Beeler, B. Good, S. Rashkeev, C. Deo, M. Baskes, M. Okuniewski, First principles calculations for defects in U, J. Phys. Condens. Matter 22 (2010), 505703.

[29] A. Kaplun, A. Meshalkin, Thermodynamic validation of the form of unified equation of state for liquid and gas, High Temp. 41 (2003) 319.

[30] H.K. Onnes, Expression of state of gases and liquids by means of series, KNAW Proceedings 4 (1902) 125.
