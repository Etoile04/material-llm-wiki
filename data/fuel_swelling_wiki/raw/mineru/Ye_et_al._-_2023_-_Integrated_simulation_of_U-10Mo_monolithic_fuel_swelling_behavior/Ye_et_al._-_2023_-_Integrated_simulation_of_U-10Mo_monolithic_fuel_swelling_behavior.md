# 📄 PDF Parsing Result

**File:** `/Volumes/openclaw记忆/Zotero_storage/storage/JN4LYXFS/Ye et al. - 2023 - Integrated simulation of U-10Mo monolithic fuel swelling behavior.pdf`
**Backend:** `pipeline`
**Pages:** 0 to end
**Formula Recognition:** ❌ Disabled
**Table Recognition:** ✅ Enabled

---

# Integrated simulation of U-10Mo monolithic fuel swelling behavior

![](images/bb72759d0e37615a430e78c79bcdf21eb98d6885afdc578a6ad4ddd6e85a7c7b.jpg)

Bei Ye a,\* , Aaron Oaks a , Shenyang Hu b , Benjamin Beeler c,d , Jeff Rest e , Zhi-Gang Mei a , Abdellatif Yacout a

a Chemical and Fuel Cycle Technology Division, Argonne National Laboratory, 9700 S. Cass Ave. Lemont, IL 60439, USA

b Pacific Northwest National Laboratory, 902 Battelle Blvd, Richland, WA 99354, USA

c North Carolina State University, Raleigh, NC 27695, USA

d Idaho National Laboratory, 1955 N Fremont Ave, Idaho Falls, ID 83415, USA

e Independent consultant, Naperville, IL, USA

## A R T I C L E I N F O

Keywords:   
U-Mo fuel   
Fuel performance modeling   
Fission gas behavior   
Fuel swelling

## A B S T R A C T

A separate computational branch has been implemented within the DART (Dispersion Analysis Research Tool) computational code to simulate the swelling behavior of U-10Mo monolithic fuel under the operating conditions of high-power research and test reactors (RTRs). The monolithic branch of the DART code implements a mechanistic rate-theory-based fission-gas-behavior model for the calculation of fission gas swelling, as well as a suite of thermal, physical, and mechanical models to consider various processes occurring in RTR fuels during irradiation. To accurately simulate and eventually predict U-10Mo monolithic fuel irradiation behavior, the code uses materials properties calculated with lower length-scale computational methods, such as gas atom diffusivity and U-Mo surface energy from atomic simulations and grain-morphology-specific recrystallization kinetics (recrystallized fuel volume fractions versus fission density) predicted using the phase-field method. The remainder of the fission gas behavior parameters used in the model were calibrated with measured intergranular bubble size distributions. With this integrated simulation approach, the swelling behavior of U-10Mo monolithic fuel was simulated for various initial grain sizes at different operating conditions and compared with measured data. Furthermore, because limited experimental data exist for parameter calibration, detailed sensitivity studies for the important parameters used in the fission gas behavior model were performed to examine their impact on both intergranular gas bubble morphology at low fission density, and on total porosity at high fission density.

## 1. Introduction

U-Mo monolithic fuel is under development for converting highly enriched uranium (HEU, 235U > 20%) fuels currently used in high-power research reactors (HPRR) in the United States to low enriched uranium (LEU, 235U < 20%) fuels [1,2]. The typical configuration of a monolithic fuel plate is a thin U-10wt%Mo foil (\~ 0.025 cm in thickness) bonded with Zr interlayer diffusion barriers and encapsulated with Al alloy 6061 cladding by hot isostatic pressing (HIP). U-10wt%Mo (designated as U-10Mo) was selected as the fissile phase of this fuel because of its stable irradiation behavior and very-high uranium density, which can offset the loss in fuel enrichment without increasing fuel core volume [1]. One of the requirements for U-10Mo monolithic fuel to be qualified is stable and predictable swelling behavior during irradiation [1,2]. Hence, it is essential to develop a reliable simulation approach to evaluate the effects of various operational and microstructural parameters on the swelling behavior of U-10Mo. Currently, a joint effort within the U.S. is ongoing across multiple universities and the national laboratory complex aimed at developing an integrated multi-scale simulation approach for studying U-10Mo monolithic fuel performance [3]. This approach incorporates engineering-scale fuel performance models [4,5] with lower-scale and meso‑scale computational methods [6–8]. The development of the monolithic branch of the DART (Dispersion Analysis Research Tool) [9–11] computational code is a part of this effort. This work describes the simulation scheme and capability of the DART monolithic branch, results of calculations of U-10Mo swelling behavior with different initial fuel grain sizes under various operating conditions, and sensitivity studies of main fission gas behavior parameters.

The DART code was previously developed to simulate irradiationinduced phenomena in dispersion fuels (U3Si2-Al and U-Mo/Al) [9,10,

11]. A computational route for U-10Mo monolithic fuel has been added to DART since 2018 to separate its calculations from those of dispersion fuel systems. In this monolithic branch, fission-gas-induced swelling, one of the main causes of fuel swelling, is simulated using the GRASS (Gas Release and Swelling Subroutine) module [12], which is a rate-theory-based mechanistic fission-gas-behavior simulation module. GRASS tracks bubble nucleation, re-solution, and growth processes both within the grain and on grain boundaries (GBs) by solving a series of non-linear differential equations. The output information includes not only total porosity but also intra- and inter-granular bubble size distributions at various locations (bulk, grain face, grain edge, and corner) [9, 12]. Besides the GRASS module, the DART monolithic branch incorporates a set of models for describing assorted physical, thermal, and mechanical processes occurring during irradiation, such as heat transfer from the fuel plate center to coolant, fuel thermal conductivity degradation, Al-cladding corrosion, etc. The modularized and parallelized framework allows the code to simulate the irradiation behavior of a large-size fuel plate without compromising detailed descriptions of microstructural evolution.

One of the key challenges in simulating fission-gas swelling with a mechanistic model is to obtain the key material properties related to gas bubble behavior [8,13], as many of them cannot be measured experimentally with the currently available techniques. Some of the parameters can be calculated using atomic scale simulation methods. For the parameters that do not have measurement data or atomic-scale simulation results, they are usually estimated by either fitting to measured bubble morphology (e.g., gas bubble size distribution) or by borrowing from other similar fuel systems where the data is available. The fission-gas-behavior parameters used in the GRASS module were calibrated in a previous study [10], using the bubble size distributions measured from irradiated U-10Mo dispersion fuel particles. This parameter set, however, needs recalibration because new atomic scale calculation results have become available since the previous calibration – the surface energy of U-10Mo calculated using the density functional theory (DFT) method [7], and the gas atom diffusivity calculated using the molecular dynamics (MD) method [8]. When these parameters are updated, the remaining parameters need to be adjusted accordingly. Furthermore, the previous study in Ref. [10] simulated fuel behavior at relatively low fission densities (< 3 × 1021 fissions/cm3 ). As the target burnup of U-10Mo monolithic fuel may be higher than 7 × 1021 fissions/cm3 in some reactors [2], it is of great interest to examine whether the parameters calibrated using low-burnup measurement data can be applied to the high burnup regime. Therefore, recalibrating the fission-gas-behavior parameters and testing their applicability at high burnup have been carried out in this study.

Fuel swelling is closely related to its initial microstructure, such as grain morphology and impurity content. For instance, initial grain size impacts fuel swelling from three aspects: (1) the number of intergranular gas bubble nucleation sites, (2) the travel distance for gas atoms from the grain interior to boundaries, and (3) the kinetics of grain subdivision – subdivided fuel volume fractions as a function of fission density. The first two aspects have been modeled with GRASS, while the third aspect needs additional input. Irradiation-induced grain subdivision/refinement in U-Mo fuel, also referred to as “recrystallization” [14, 15], occurs at intermediate to high fission densities (> 2 × 1021 fissions/cm3 ) during which the fuel grain size decreases from tens of micron to sub-micron. Consequently, the grain boundary area per unit volume increases and fuel swelling switches from a moderate and almost linear behavior to a nonlinear accelerated rate [14–16]. The effect of initial grain size on grain subdivision was observed in neutron-irradiated UO2 fuels. It was found that grain subdivision was less likely to occur in large-grain samples [17]. Because as-fabricated U-10Mo fuel foils exhibit very heterogeneous grain morphology [18,19] with the grain size range spanning from a few microns to over a hundred microns, grain-size-specific recrystallization kinetics are required to simulate fission gas behavior during the grain subdivision process. Nevertheless, it is almost impossible to obtain grain-size-specific recrystallization kinetics from experiments, as it is extremely difficult to produce samples that are composed of a single grain size. As an alternative solution, grain-size-specific recrystallization kinetics were predicted using the phase field method [6] and implemented into DART.

The effects of operational parameters on fuel swelling are either difficult or expensive to study with experimental techniques because many of these parameters are intricately interconnected. For instance, fuel temperature is strongly dependent on the fission rate. On the other hand, a well-designed and validated computational code is suitable for separately studying and testing individual mechanisms proposed to explain the complex irradiation behavior in fuels. The separate effects of fission rate and fuel temperature are explored in this work.

The following sections are organized as follows: The DART computational methodology and primary models are described in Section 2, recalibration results of fission-gas-behavior parameters and the associated sensitivity study in Section 3, U-Mo swelling behavior up to high fission density in Section 4, separate effects studies of operational parameters in Section 5, and conclusions in Section 6.

## 2. DART code structure and primary models

This section describes the general code structure and primary models of the DART monolithic branch, as well as the meshing scheme and the recrystallization model in the GRASS module.

## 2.1. DART code structure

The flowchart of the dispersion fuel branch in DART was described in a previous publication [11]. The complete flowchart of the DART code with the newly added monolithic fuel branch is displayed here to provide an overview of the relationship between different calculation branches. As shown in the DART code flowchart of Fig. 1, the dispersion and monolithic branches share the same peripheral models to simulate the heat transfer process from the centerline of the fueled zone to the coolant due to the similar laminated structures shared by these two types of fuels. At each time step, the code starts by calculating the thickness of the oxide layers caused by coolant corrosion and then proceeds to estimate the temperatures on the oxide layer surface and at the oxide-cladding and cladding-fueled zone interfaces. The corrosion process of the coolant-side cladding surface is the same for both types of fuels and is described with oxide layer growth correlations [20,21]. The implementation of the models in the thermal computational chain (coolant temperature-cladding heat transfer, oxide layer growth, and heat transfer from fuel plate centerline to cladding surface) were described in detail in Ref. [11] and have been benchmarked against the MAIA fuel performance code developed at the French Alternative Energies and Atomic Energy Commission (CEA) [22].

The two branches diverge from each other starting from the point at which fueled zone calculations are performed. The Bruggeman model [23] is currently applied to approximate the thermal conductivity of irradiated U-Mo by treating it as a composite material consisting of fission gas bubbles and U-Mo. A more accurate model for updating the thermal conductivity of irradiated fuel is under development and will be implemented when completed. Detailed models for the calculation of fuel swelling in the monolithic branch are described below in Sections 2.2 – 2.4.

## 2.2. Fission gas behavior models in the GRASS module

The GRASS module was originally developed for predicting fissiongas behavior in oxide fuels used in Liquid Metal Fast Breeder Reactors (LMFBRs) and Light Water Reactors (LWRs) [24,25]. It has been validated against various experimental data [12]. GRASS includes models for intra- and intergranular fission-gas-bubble behavior as well as a mechanistic description of the role of grain-edge interlinked porosity in releasing fission gasses to triple points (grain corners) [12]. Most of the primary physics models are the same as what were described in Ref. [12]. One main modification was made in the radiation-induced bubble re-solution model to consider the bubble-size-dependent resolution efficiency. The equations of the main physics models are listed below to facilitate the discussions in later sections. In addition, the value ranges of key parameters in each model were determined based on recent literature of U-Mo fuels.

![](images/00a99b516a1e842a84d5458035185b2a49cbcca7c81a7a9f9a780917f619cc8c.jpg)  
Fig. 1. Flowchart of the DART computational code.

## 2.2.1. Gas bubble nucleation

For intragranular gas, the rate of bubble nucleation is

$$
\tag{1}
$$

where NR− intra is the intragranular bubble nucleation rate in cm− 3 s − 1 ; fN is the nucleation factor, describing the probability that two gas atoms come together to form a dimer; DXe is the diffusivity of a Xe atom in U-Mo in cm2 /s; rXe = 2.16×10− 8 cm is the Xe atom radius; CXe− intra is the Xe atom concentration in U-Mo grains in cm− 3 . This nucleation model assumes a dimer as the nucleus of gas bubbles, which is a reasonable practical treatment for handling the mathematical complexity in the simulation [13]. Although it is not stated explicitly in Eqn. (1), NR− intra is dependent on the intragranular bubble population because CXe− intra is not a constant but changes with the evolution of the intragranular bubble population throughout the irradiation period. The variation of

CXe− intra is solved through a set of coupled differential equations described later (Eqn. (7)) by taking into account the processes for gas atoms getting trapped in and resolved from intragranular bubbles. The values of fN ranging from 10− 7 to 10− 2 were proposed for UO in the literature [13]. In this study, this parameter is treated as an adjustable variable to be determined by fitting to measurement data. DXe is the total gas atom diffusivity, composed of intrinsic (thermal) and radiation-driven components [8]:

$$
\tag{2}
$$

where k = 8.617 × 10− 5 is the Boltzmann constant in eV/K, T is the fuel temperature in K, and ˙f is the fission rate in cm− 3 s − 1 . The description of radiation-enhanced diffusion is recently published [26], and the results suggest radiation-enhanced diffusion does not significantly contribute to the total diffusion of Xe at the operating conditions of RTRs. The uncertainty of not including this diffusion component in the swelling simulation is examined in Section 4.2. Gas atoms have faster transport on grain boundaries than in the lattice [27]. Hence, gas atom diffusivity on grain boundaries is approximated with DXe multiplied with an enhancement factor z. The z value for UO2 is in the range of 102 – 107 , according to the estimation in Ref. [27]. The z value is treated as an adjustable parameter in this study.

For intergranular gas, the bubble nucleation rate is assumed to have

a similar expression as that of intragranular gas:

$$
\tag{3}
$$

where NR− inter is the intergranular bubble nucleation rate in cm− 3 s − 1 ; fN− GB is the proportional factor to be multiplied with fN; CXe− inter is the Xe atom concentration on U-Mo grain boundaries in cm− 3 . Similar to CXe− intra, CXe− inter changes during irradiation and is solved through Eqn. (7) in the model. The amount of free gas atoms on grain boundaries is the difference of the incoming flux of gas atoms from the grain interior, the atoms released from intergranular bubbles due to radiation-induced resolution, and the loss of gas atoms to intergranular bubbles by absorption. Compared to those that diffuse from the grain interior, the gas atoms resolved from intergranular bubbles are not the main contributors to CXe− inter. Bubble nucleation on grain boundaries is much more rapid at the beginning of irradiation, but it reaches saturation much earlier than that in lattice [28]. Therefore, fN− GB can be much smaller than 1. However, since the z factor can be a large number, the difference between NR− inter and NR− intra (the product of fN− GB and z) is much closer to 1 than fN− GB.

## 2.2.2. Radiation-induced bubble re-solution

Radiation-induced bubble re-solution model adopted in DART is

$$
\tag{4}
$$

where b0 is the bubble destruction probability, ˙f is the fission rate, and R is a piecewise function representing different re-solution modes for small and large gas bubbles. Eqn. (4) assumes gas-atom re-solution from a bubble is isotropic and single gas-atoms are ejected [28]. This formula is applied to both intra- and inter-granular gas bubbles in the DART calculations.

b0 can be estimated with the interaction volume of a thermal spike with bubbles [13,29]:

$$
\tag{5}
$$

where Z0 is the radius of a thermal spike and μ is the recoil length of fission fragments. Eqn. (5) was proposed to model the dynamic bubble re-solution process in UO [13,30], presuming that partial or total volumes of a bubble are “chipped away” when it is transversed by a fission fragment, and the efficiency of this sputtering mechanism is related to the interaction distance between the fission fragment path and the bubble [31,32]. For UO2, Z0 is on the order of 1–7 nm [13] and μ on the order of 6 µm [33]. Since the electrical resistance of U-Mo is much smaller than UO2 [34], the radius of a thermal spike in U-Mo is expected to be smaller than that in UO2 [29]. Therefore, although the dimension of a thermal spike was estimated to be \~13 nm in U-Mo in Ref. [34], the value of 1–7 nm is applied in this study as an estimation of Z0. The recoil length μ is \~5 µm, which is the stopping range of 80 MeV Xe in U-10Mo calculated using the SRIM software [35]. Based on the reasoning above, b0 is estimated to be on the order of 10− 18 cm3 .

The piecewise function R is a simplified version of the model proposed in Ref. [28]:

$$
\tag{6}
$$

where rb is the bubble radius, λ is the gas-atom knock out distance, and rresol is the thickness of the annulus within which all gas-atoms are knocked out. The order of magnitude of λ, \~ 10 nm, is borrowed from the value for UO [30,36]. As suggested in Eqn. (6), when a gas bubble is struck by a fission fragment, all gas atoms are ejected if the bubble size is smaller than λ. However, for a large bubble, only the gas atoms in the outer shell of the bubble are ejected. Gover’s molecular dynamics study [30] on Xe-bubble re-solution in UO2 also suggests that (1) gas atoms are more likely to be knocked out in smaller bubbles and (2) the probability for knock-out atoms to be trapped back to bubbles increases with bubble size. Therefore, rresol can be much smaller than λ, because of the trapping effect of large bubbles. Both λ and rresol are handled as adjustable variables and their values are determined in this study by fitting to experimental data. Eqn. (6) also indicates that the relative re-solution effect of intergranular bubbles is much smaller than that of intragranular bubbles, given the larger size of intergranular bubbles. This inference is reasonable because grain boundaries have strong trapping effects. A steep gas-atom concentration gradient is expected to exist next to grain boundaries. Ejected gas atoms within the concentration gradient can be absorbed by the grain boundaries immediately [37]. The step-function form for Eqn. (6) will be further modified in the future to smooth the transition between the two bubble-size regimes.

## 2.2.3. Gas bubble growth

The GRASS module consists of a set of coupled nonlinear differential equations for calculating the concentrations of gas atoms and bubbles in different sizes at various locations (bulk, grain face, grain edge, and grain corner). These equations take the form of [12,38]:

$$
\tag{7}
$$

where Ci is the number of bubbles in the i th size class per unit volume; ai = ai(Ci) represents the rate at which bubbles grow out of the i th size class because of coalescence with bubbles in the same class; bi = bi(C1, …, Ci− 1, Ci+1, …, CN) represents the rate at which bubbles are lost from the i th size class because of coalescence with bubbles in other size classes and re-solution; and ci = ci(C1, …, Ci− 1, Ci+1, …, CN) represents the rate at which bubbles are being added to the i th size class because of fission gas generation and gas atom release due to re-solution (for i = 1), bubble nucleation (for i = 2), bubble growth resulting from bubble coalescence and diffusion of gas atoms into bubbles (for i > 2), and bubble shrinkage due to irradiation-induced re-solution (for i > 2). Size distributions of intra- and inter-granular bubbles are obtained by solving the equations in Eqn. (7) for each type of bubble.

Bubble growth is generally achieved through the mechanism of bubble coalescence. The process of gas atom diffusion into bubbles can also be understood as the coalescence between bubbles and gas atoms. The probability of an i bubble coalescing with a j bubble is [12]:

$$
\tag{8}
$$

where Pij is the coalescence probability in cm3 /s; ri and rj in cm are the average radius of the bubbles in the i th and j-th size classes, respectively; Di and Dj in cm2 /s are the average diffusivity for the bubbles in the i th and j-th size classes, respectively, calculated based on the model in [39] and inversely proportional to bubble volume; and vi and vj in cm/s are the velocity of the i bubble and j bubble moving in a temperature gradient, respectively. The first and second terms on the RHS (right-hand side) of Eqn. (8) are the probability of bubble interaction due to random motion [39] and biased migration (induced by a temperature gradient), respectively [12]. As the fuel temperature difference (\~10 ◦C) across the fuel foil thickness is insignificant, the biased migration is not the primary driving force for bubble interaction.

The size of the bubbles in the i th size class is calculated in GRASS at each time step using the current fuel temperature and stresses (including both hydrostatic stress and U-Mo surface energy) according to the hard sphere equation of state (EOS) developed by Ronchi [40], which was fitted to experimental data for argon, xenon, and krypton at high pressure.

## 2.2.4. Gas-atom migration path from the grain interior to boundaries

The models in GRASS assume that gas-atom generation occurs within grains as fission products. Gas atoms and bubbles migrate to grain boundaries through diffusion induced by a concentration gradient and a temperature gradient. The gas-atom migration process from grain interior to boundaries consists of a series of intragranular trapping and irradiation-induced re-solution processes. The flux of gas-atom diffusion arriving at grain boundaries is solved using Speight’s model from Ref. [41]. The derivation details are presented in Ref. [12] and the result is listed here:

$$
\tag{9}
$$

where Rg is the rate of fission-gas-atom diffusion to the grain boundaries; CI is the gas-atom concentration in the grain at the beginning of the time step t0; Cg is the gas-atom concentration at the grain-boundary location; a is grain radius; DXe is gas atom diffusivity in Eqn. (2); g is the probability of a gas atom in solution being captured by a bubble per second, which is proportional to the coalescence probability between single gas atoms and bubbles in all size classes (P1j in Eqn. (8)); and b is the resolution probability, defined in Eqn. (4).

When the grain-face coverage by intergranular bubbles reaches saturation, gas atoms diffuse from grain faces to grain edges. The saturation criteria (FaceCovMax), based on an ideal situation in which the grain faces are occupied by equal-size, close-packed, round, and touching bubbles, gives the maximum areal coverage per unit area of grain boundary as 0.907 [12]. In reality, intergranular bubbles are lenticular in shape and have a size distribution. Hence, the value of FaceCovMax can be less than 0.907. The sensitivity of this parameter on swelling calculation results will be described in Section 4. A schematic showing the intergranular bubble morphology evolution with fission density is depicted in Fig. 2.

The GRASS calculation for the gas-atom diffusion from grain faces to grain edges is based on the model developed in Ref. [42]. The rate of gas-atom diffusion to the edges is a function of both gas-atom diffusivities in lattice and on grain boundaries, and grain morphology. In this study, grains with the same size are approximated with identical tetrakaidecahedrons. Based on this geometry, the effective distance that gas atoms must travel before encountering an edge can be estimated. Gas atoms on edges stay trapped until an interconnected tunnel forms to allow gas atoms to migrate to the triple points (grain corners), shown in Fig. 2. Tunnels of open porosity along the grain edges have been observed in UO2 fuels [43]. Although no direct observation of tunnel formation in U-Mo has been made yet, the gas atom transport mechanism in U-Mo from the grain interior to the triple points is assumed to be analogous to that in UO2, as both materials maintain their crystalline structure during irradiation up to high fission densities. The probability of pore interlinkage is estimated using percolation theory [44] and is a function of grain size and the grain-edge bubble size distribution [12]. The criterion for pore tunnel formation is established using fuel swelling due to grain-edge bubbles. The threshold value of fuel swelling due to edge bubbles (LinkSwell) is \~ 0.07 for UO2 [12] and is treated as an adjustable variable in this study.

## 2.3. Meshing scheme and parallelization

A three-level meshing scheme is implemented in DART. Level-1 meshing ((x, z) node), shown in Fig. 3(a) and (b), is defined for thermal and power calculations and is usually adapted from the settings in neutronics calculations. This level of calculation is executed outside of the GRASS module. Level-2 (k node) and level-3 (p node) meshing are set up inside each (x, z) node to facilitate GRASS calculations. K nodes (Fig. 3(c)) represent different initial grain sizes. Four k nodes were set up in this study to represent the four initial grain sizes: 1.34 µm, 4.36 µm, 8.5 µm, and 17 µm, which were used in the phase-field calculations of U-10Mo recrystallization kinetics described in Section 2.4. The volume of each k node within a (x, z) node is defined as:

$$
\tag{10}
$$

where Δx and Δz are the dimensions of the (x, z) node in the x and z directions, respectively; fk is the volume fraction of the kth type of grain; and y is the thickness of the fuel foil.

Each k node is further divided into multiple segments (denoted as p nodes) with equal volume (V(x,y,k,p) = V(x,z,k)/p) to track the progression of grain subdivision, as shown in Fig. 3(d). The fission-gas-behavior equations described in Section 2.2 are solved for each p node. At each time step, the number of p nodes that become recrystallized is determined according to the grain-size-specific recrystallization kinetics in Section 2.4. Once a p node becomes recrystallized, its grain size will change from the initial grain size to the recrystallized grain size (0.5 μm) and maintain this grain size until the end of irradiation. In this study, the number of p nodes is set to 50. The amount of p nodes is selected to enable the code to satisfactorily replicate the phase-field-calculated recrystallization kinetics described in Section 2.4 without consuming excessive computational resources. Note that neither k nodes nor p nodes represent actual spatial locations within the fuel foil, as the rate theory method used for simulating fission gas behaviors is a mean-fieldtheory method. These meshes were set up in order to properly track fission gas behavior in grains that start with different initial grain sizes and undergo the recrystallization process at different times during irradiation.

In order to ease the computational burden of solving multiple sets of differential equations simultaneously for each of hundreds or even thousands of nodes, the DART code was extended with MPI (Message Passing Interface)-based data communication subroutines, so that data could be passed between nodes consistently as needed. A load-balancing subroutine was added to determine the number of processes allocated to a computational run and to distribute the parallel load as evenly as possible. Currently, the GRASS module that performs the swelling calculations over the level-1 mesh elements was modified to run the calculations for each time step in parallel and to redistribute the results when complete. Further development in the parallelization calculation scheme to extend the parallel computation to level-2 and level-3 mesh elements is underway.

## 2.4. Grain subdivision process

In this study, recrystallization kinetics for four grain sizes (1.34 µm, 4.36 µm, 8.5 µm, and 17 µm) were calculated using a set of twodimensional (2D) polycrystalline structures in a phase-field model [6] which gives a more realistic representation of the material than a one-dimensional structure. The predicted recrystallization kinetics are displayed in Fig. 4, showing an apparent grain-size dependency.

![](images/d3d606f556a2f7a423b8d3bc19664a0987b1dbd6eee6d5d19aad5aed868de0fb.jpg)  
Fig. 2. Schematic of intergranular gas bubble morphology and its evolution with fission density (FD).

![](images/b6b015373a5ee1c86eed64b85386c81d37c57868a195e12e85f9b8b013f68046.jpg)  
Fig. 3. Schematic of (a) the (x, z) meshing grid of a monolithic fuel plate, (b) side view of the plate, (c) k nodes within a (x, z) node, and (d) p nodes inside each k node to track the progression of recrystallization.

![](images/28f0e15b7e7b2c13625066934b243281c6fa2168fe92733b19c76d8da3f73dd0.jpg)  
Fig. 4. Recrystallization kinetics calculated with the phase-field method for grain sizes 1.34 µm, 4.36 µm, 8.5 µm, and 17 µm, compared with the measurement data collected from U-10Mo dispersion fuel particles with an average grain size of \~ 4.5 µm. The “measurement” data is from Ref. [14].

Larger-size grains have lower volume fractions of recrystallized fuel at a given fission density. Similar grain size effect has been observed in high burnup UO2 fuel pellet [45]. The effects of aspect ratio and fission rate on recrystallization are not studied explicitly in these simulations. Compared with the experimental data collected from irradiated U-10Mo dispersion fuel particles (average grain size: \~ 4.5 µm) [14], the calculated recrystallization kinetics are within the uncertainty range of the measurement data.

Fig. 5 depicts how grain subdivision is simulated in DART. At each time step, the code determines whether a p node undergoes recrystallization by comparing the current recrystallized volume fraction with the supposed value predicted with the recrystallization kinetics in Fig. 4. If the current value is lower than the supposed value, more p nodes will become recrystallized until the former becomes very close to the latter. When a p node becomes recrystallized, its average grain diameter is assumed to reduce to 0.5 µm. Microstructural characterization of irradiated U-7Mo fuel particles shows that the subdivided grain size is in a range of 0.1 – 1 μm with a peak value of \~0.3 μm [46]. Thus, the assumed 0.5 µm as the subdivided grain size is reasonable. A future study will include the subdivided grain size as an adjustable parameter in parameter optimization. The processes of gas atom migration from the grain interior to the corners in the recrystallized zone are simulated using the updated grain size.

## 3. Calibration of fission-gas-behavior parameters

Calibration of fission-gas-behavior parameters in DART was performed by fitting to intergranular bubble size distributions measured from samples irradiated to low fission densities, prior to the onset of recrystallization. The reasons for using this specific type of data are explained as follows:

(1) The bubble size distribution carries more information indicating the underlying mechanisms of fission gas behavior than averaged bubble size and total porosity [47];

![](images/650146c883c26e1407bff3420d5d3d476d25e99a9565b063a2a895b926a82b33.jpg)  
Fig. 5. Schematics of how the recrystallization process is tracked in DART.

(2) Data obtained prior to recrystallization contain information closer to the early stage of bubble formation and evolution, without the influence of grain refinement.

The applicability of the fission-gas-behavior parameters calibrated with low-burnup data to the systems irradiated to high burnup is verified in Section 4 by comparing computational results to the U-10Mo monolithic fuel swelling correlation developed based on measured data [16].

## 3.1. Calculation setup and input parameters

The data measured from three miniature-size U-10Mo/Al dispersion fuel plates irradiated in the Advanced Test Reactor (ATR) were used for the calibration. These plates were irradiated in the RERTR-5 test to relatively low fission densities and no recrystallization was observed in these plates [48]. Moreover, although these plates are dispersion fuels, in which the fuel phase exists as particles embedded in an Al matrix, the fuel phase material is U-10Mo, which is the same as that in monolithic plates. No difference in material properties related to fission gas behavior is expected, which ensures the validity of applying this set of data for calibration. Calibration using the measured data from recently completed monolithic fuel tests will be performed when the data becomes available. The ATR operating conditions and the irradiation parameters of these three plates, as well as the input parameters for the calibration calculations, are listed in Tables 1 and 2, respectively. Important thermal property data are listed in Table 1 as well. The thickness of the coolant-side oxidation layer formed on the plate surface is assumed to be a constant of 5 µm based on the observations of fuel plates irradiated in the ATR [10]. For all calculations in this work, the hydrostatic pressure used in the equation of state of gas bubbles is assumed to be the coolant pressure. The study of the effect of coolant pressure on fission gas bubble growth is ongoing, using the DART code integrated with a FEM (Finite Element Method)-based mechanical analysis module, and the results will be described in a future study.

To set up the calculations, a (x, z) node that has the dimensions of the miniature-size plates irradiated in the RERTR tests was simulated. Four k nodes were defined within the (x, z) node, and each of them has the initial grain size of 1.34 µm, 4.36 µm, 8.5 µm, and 17 µm, respectively. For each calculation, a grain size distribution (volumetric fraction of each grain size) is required.

## 3.2. Calibration results

The optimized set of fission-gas-behavior parameters, listed in Table 3, were either obtained through atomic-scale simulation or selected by fitting the calculated intergranular bubble size distributions with measurement data. The bounding limits of each fitted parameter were taken from the literature and are described in Section 2.2. The parameter values obtained in a previous study are also listed in the table for the purpose of comparison.

Table 1  
Input parameters for the calibration of fission-gas-behavior parameters in DART.
<table><tr><td>Parameter</td><td>Value</td><td>References</td></tr><tr><td>Coolant conditions</td><td>Inlet temperature:51℃ coolant pressure: 2.7 Mpa coolant velocity:14.5 m/s</td><td>[49]</td></tr><tr><td>Node dimensions</td><td>8.26 cm (H)× 2 cm (W)× 0.105 cm (T) Fuel foil thickness = 0.0254</td><td>[50,51]</td></tr><tr><td>Coolant-side oxidation layer thickness</td><td>cm 5μm</td><td>[10]</td></tr><tr><td>Coolant-side oxidation layer</td><td>2.25W/m·K</td><td>[52]</td></tr><tr><td>thermal conductivity Cladding thermal conductivity</td><td>167W/m·K</td><td>[53]</td></tr><tr><td>Unirradiated U-10Mo thermal conductivity</td><td>11.2 W/mK</td><td>[2]</td></tr></table>

As seen in Table 3, some parameters have quite different values from those of the previous study [10]. A lot of the parameter values in the previous study were adopted from UO2. Since then, some key parameter values of U-Mo have been obtained through atomic-scale simulations. Considering the lattice and structure differences between UO2 and U-Mo, it is expected that the re-calibrated values can be different from the original set. For example, the surface energy used in this study was calculated using the DFT method, much more accurate than the estimated value in the original set, as well as the linear coefficient of radiation-driven gas atom diffusivity and activation energy for intrinsic gas atom diffusion. As many of the parameters are interrelated, when some of them are updated, the rest need to be adjusted accordingly. For future fuel performance modeling, it is recommended to use the parameter set obtained in this study.

The comparisons between the fitted and measured intergranular bubble size distributions are presented in Fig. 6 for all three plates, in which the calibrated and measured peak bubble sizes agree reasonably well with each other. For each plate comparison in Fig. 6, two sets of calculation results are presented, generated by setting single grain sizes (100 vol% for the interested grain size and 0 vol% for the other grain sizes) of 4.36-µm and 8.5-µm, respectively. These two grain sizes were employed for the comparison because they are close to the observed fuel grain sizes listed in Table 2. The calculated bubble size distributions on grain faces are plotted in Fig. 6.

The primary criterion of the calibration is to obtain the best match between the peak positions of calibrated and measured intergranularbubble-size distributions for both grain sizes in all three plates. The differences in bubble densities are less important in comparison with the peak bubble size, because the experimental limitations, such as undulating sample surface and limited number of images to obtain good counting statistics, etc., can lead to large uncertainties in bubble density. For instance, the uncertainties for the measured data in Fig. 6 are ± 10% near the peak position and ± 50% at both ends of the distributions [48]. Besides the measurement uncertainties, many other sources can contribute to the peak bubble density differences. An apparent one is related to the density conversion process. The experimental data was initially measured as linear bubble density (number of bubbles per unit grain boundary length), while the calculation results were expressed as volume densities. For comparison purposes, both experimental and calculated quantities were converted to areal density. To achieve the best accuracy of density conversion, it is required that the bubbles are homogeneously distributed in the material [54]. Such an ideal condition does not exist in the fuel plates used for calibration. Moreover, other assumptions applied for the conversions, such as the shape of grains and packing patterns of bubbles, may not reflect reality well. All these uncertainty factors, taken together, contribute to the deviation of the converted density from the data. The results in Fig. 6 show that the calculated peak bubble densities are 2 – 3 times higher than the measured data. Considering the uncertainties described above, this discrepancy is deemed acceptable.

Besides the bubble size distributions, the calibrated parameter set was also verified by comparing calculated and measured average bubble diameters, visible porosities, and swelling as shown in Fig. 7. A cutoff diameter of 100 nm was applied when estimating the average bubble diameters and visible porosities using calculated bubble size distributions, which is consistent with the resolution limit of the scanning electron micrographs (SEM) used for bubble measurement [48]. The average bubble size and visible porosity were therefore calculated according to the equations below:

$$
\tag{11}
$$

Table 2  
Characteristics of three miniature U-10Mo/Al dispersion fuel plates irradiated in the RERTR-5 test, used for fission-gas-parameter calibration [48].
<table><tr><td>Plate ID</td><td>Fission density (fissions/cm)</td><td>Avg.fission rate (fissions/cm·s)</td><td>Temperature (C)</td><td>If recrystallized?</td><td>Initial grain size (um)</td><td>Avg.bubble diameter (um)</td></tr><tr><td>V6018G</td><td>2.31×1021</td><td>2.3×1014</td><td>121</td><td>No</td><td>4.9±2.0</td><td>0.14</td></tr><tr><td>V6019G</td><td>2.91×1021</td><td>2.9×1014</td><td>142</td><td>No</td><td>8.5±3.6</td><td>0.16</td></tr><tr><td>V8005B</td><td>2.41×1021</td><td>2.4×1014</td><td>170</td><td>No</td><td>8.1±4.5</td><td>0.16</td></tr></table>

Table 3

Optimized value set of calibrated key fission-gas-behavior parameters.
<table><tr><td>Parameter</td><td>Description</td><td>Unit</td><td>Best value obtained</td><td>Ref.</td><td>Bounding limits</td><td>Ref.</td><td>Value in previous calibration [10]</td></tr><tr><td>D0</td><td>Linear coefficient of radiation-driven gas atom diffusivity</td><td>cm5</td><td>5×10-31</td><td>[8]</td><td>N/A</td><td></td><td>8×10-29</td></tr><tr><td>Q</td><td>Activation energy for intrinsic gas atom diffusion</td><td>cal</td><td>40,559</td><td>[8]</td><td>N/A 10²-107</td><td></td><td>33,000</td></tr><tr><td>2</td><td>GB diffusion enhancement factor</td><td>N/A</td><td>3×104</td><td>This work</td><td></td><td>[27]</td><td>1×104</td></tr><tr><td>fn</td><td>The probability that two intragranular gas atoms come together and form a di-atom bubble nucleus</td><td>N/A</td><td>2×107</td><td>This work</td><td>10-7-10-2</td><td>[13]</td><td>3×10-8</td></tr><tr><td>fn-GB</td><td>Adjustment factor for bubble nucleation probability on GB</td><td>N/A</td><td>6×10-10</td><td>This work</td><td>can be&lt;1</td><td>[28]</td><td>6×10-7</td></tr><tr><td>Yu10Mo</td><td>Surface energy of U-10Mo</td><td>dyn/</td><td>1850</td><td>[7]</td><td>N/A</td><td></td><td>200</td></tr><tr><td>b</td><td>The probability fora bubble interacting with fission</td><td>cm cm³</td><td>2×10-18</td><td>This</td><td>on the order of</td><td>Refs. Of</td><td>7×10-18</td></tr><tr><td></td><td>fragments</td><td></td><td></td><td>work</td><td>10-18</td><td>Eqn. (5)</td><td></td></tr><tr><td>虽</td><td>The gas-atom knock out distance from bubbles</td><td>cm</td><td>5×10-7</td><td>This</td><td>~1×10-6</td><td>[30,36]</td><td>1 ×10-6</td></tr><tr><td></td><td></td><td></td><td></td><td>work</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Tresol</td><td></td><td></td><td></td><td></td><td>&lt;1×10-6</td><td></td><td></td></tr><tr><td></td><td>The destructed outer-shell thickness of bubbles</td><td>cm</td><td>3×10-9</td><td>This</td><td></td><td>Refs. Of</td><td>N/A</td></tr><tr><td></td><td></td><td></td><td></td><td>work</td><td></td><td>Eqn. (6)</td><td></td></tr></table>

![](images/678da93ea0e2cad4629b42476cd9a62807801986d57fbc0ab092aa03b3bc8155.jpg)

![](images/b808ec3a8dcd4242268e22cf1cf9669e9e3ca831c79338a0897ec72d936775a1.jpg)

![](images/c4eae310339201bb334d7ca51f53a8f8993e0f9067c73b38ee3ee80a40862f0b.jpg)  
Fig. 6. Comparisons of measured and calibrated intergranular bubble size distributions in plates (a) V6018G, (b) V6019G, and (c) V8005B.

![](images/bc5a13b52b213792e6f6ec6f00c9928c36fc4fbbd32a9e08ba267c288fb43bfa.jpg)

![](images/2a634c5f392b522fa43b60ded5ee0a6cfafe0f2e299966cd9fdaa690f213a006.jpg)

![](images/ab27c3251d713cadf510db5ca37a18e16cda7e11008e9a354b3fbb01368ec20c.jpg)  
Fig. 7. Comparison of measured and calibrated (a) bubble diameter, (b) visible porosity, and (c) U-Mo swelling. The measured data are from Ref. [48].

$$
\tag{12}
$$

where ¯d is the average bubble diameter in cm, pvisible is the percent visible porosity, and Ci in 1/cm3 and ri in cm are the number density and average radius of the bubbles in the size classes whose bubble radii are larger than 50 nm, respectively. Since the intragranular bubble size (2–3 nm in diameter) is much smaller than 100 nm, the contribution from intragranular bubbles to eqn. (11) and (12) was excluded. The experimental average bubble diameter, visible porosity, and swelling were reported in Ref. [48].

Fuel swelling includes the contributions from both gaseous and solid fission products. The swelling due to fission gasses is calculated through the summation of all bubble volumes, and solid-fission-product swelling is proportional to fission density and expressed as [55]:

$$
\tag{13}
$$

wher e  ΔVV0  solid i s the percent swelling due to solid fission products, and FD is the fission density in 1021 fissions/cm3 .

As shown in Fig. 7(a), the calculated bubble sizes are slightly smaller than the measured data for these plates (differences ≤ 25%), which is consistent with the differences in bubble size distributions shown in Fig. 6 and can be explained with the uncertainties associated with measurements. Fig. 7(b) shows that although calculated visible porosities are generally higher than the measured quantities, the difference between calculated and direct measurement data is small. Directly measured porosity is only available for plate V6019G, and the other measurement data were derived based on the conversion from the bubble density per unit length of grain boundaries to volumetric density [48]. As explained earlier, such conversion may introduce notable errors in the resultant porosity. This can be demonstrated with the difference between the derived and direct measured values of plate V6019G. Considering the uncertainties associated with derived data, the agreement between calculated and measured data in Fig. 7(b) is satisfactory. For the comparison of total swelling shown in Fig. 7(c), the calculated values are close to the measured data (differences ≤ 15%). The overall agreement exhibited in Fig. 7 confirms that the parameter value set in Table 3, when applied to the models detailed in Section 2.2, can be used to describe fission gas behavior in U-10Mo irradiated at conditions similar to those listed in Tables 1 and 2.

It is also revealed in both Figs. 6 and 7 that the bubbles in the 8.5-µmgrain fuel have a larger size and correspondingly a lower bubble density than those in the 4.36-µm-grain fuel. These differences in bubble characteristics are due to lower grain boundary area per unit fuel volume in the larger-grain case, i.e., a reduced number of intergranular bubble nucleation sites.

## 3.3. Sensitivity studies of the calibrated parameter set

As many of the parameter values in Table 3 are not directly measurable, the uncertainties of the fitted values are unknown, as are their combined effects on the calculated bubble characteristics and fuel swelling. Therefore, it is necessary to perform sensitivity studies on the calibrated parameter set to examine how the uncertainties in individual parameters impact outputs qualitatively and quantitatively. The singlevariable approach was taken in this work because it is practical and straightforward to detect whether a gas-behavior mechanism functions as expected. The sensitivity studies were carried out on both the intergranular bubble size distribution at a low fission density, described in this section, and on fuel swelling up to a high fission density, described in Section 4.2. The variation ranges for the sensitivity study were chosen according to the optimized value and bounding limits in Table 3. For some parameters, the variation ranges are slightly larger than the bounding limits, but still in their vicinity, to test the response of the model with relatively extreme values.

For sensitivity studies on bubble size distribution, the intergranular bubble size distributions for 4.36-µm grains using data from plate V6018G, irradiated to 2.31×1021 fissions/cm3 , were calculated and compared within a range of values of each parameter.

Fig. 8 shows the sensitivity study results of two diffusion-related parameters: linear coefficient of radiation-driven gas atom diffusivity D0 and grain-boundary diffusion enhancement factor z. The value of D0 was computed through MD simulations, and the sensitive study presented here aimed to investigate the potential uncertainty of missing the component of radiation-enhanced diffusion in Eqn. (2). D0 universally impacts the diffusivities of all gas atoms in the system, while the z factor only changes gas atom diffusivity on GBs. The results in Fig. 8 show that increasing either D0 or z values led to similar changes in intergranular bubble morphology: the peaks of intergranular bubble size distribution moving toward the right, the profiles becoming flatter, and more gas atoms staying at the GBs (shown in the breakdown of gas atom distribution in the system in the insets of Fig. 8). Nevertheless, the reasons underlying the bubble morphology changes are slightly different when varying D0 or z. In the case of increasing D0, the gas migration process from the grain to the GBs was directly enhanced, according to Eqn. (9), while a larger z value may lead to more rapid formation of large bubbles on GBs.

Both the bubble nucleation probability fn and the adjustment factor for the nucleation probability on grain boundaries fn-GB were investigated for their effects on intergranular-bubble formation and growth behavior. The results shown in Fig. 9 demonstrate that increasing either fn or fn-GB shifts the bubble size distribution profiles toward the left side, i.e., reducing the peak intergranular bubble size, although to a different extent. Intergranular bubble size distributions are less sensitive to the variation of fn than to that of fn-GB, within the parameter ranges examined here. Increasing fn inflated the gas-bubble nucleation probabilities both in the lattice and on grain boundaries but had a relatively stronger effect on intragranular bubbles. Consequently, the number of gasses impinging on GBs was reduced because gas atoms generated from fission reactions were more readily trapped in the intragranular bubbles, which balanced out the effect of increased nucleation probability on GBs and resulted in the relatively stuporous feedback of intergranular bubble behavior to the change of fn. On the other hand, fn-GB strongly impacted the nucleation process of intergranular bubbles but had less of a direct influence on the incoming gas atom flux to GBs compared to fn, particularly when the intergranular bubbles were small. Accordingly, a lot more but smaller bubbles can form on GBs with a higher nucleation rate, as shown in Fig. 9(b). This trend continues with irradiation because large bubbles more easily trap gas atoms than the small bubbles.

![](images/c151d6ab8958c609830cff673ad271697276fd90e9bda82117b7874ea1872693.jpg)

The other important parameters investigated are b0, λ, and rresol, all of which are related to the bubble re-solution process. b0 is the probability that a bubble interacts with fission fragments and impacts all gas bubbles in the system. For larger values of b0, gas atoms are more likely to be knocked out from existing bubbles by a transverse fission fragment, and more gas atoms become available (before the system achieves a new equilibrium state) for nucleating new bubbles. In this case, more bubbles can nucleate but are difficult to grow, as presented in Fig. 10(a).

The gas-atom knock out distance from bubbles λ is applied in Eqn. (6) as an approximate cut-off threshold for separating different bubble destruction modes as a function of bubble size. Fig. 10(b) shows that the results do not change when λ varies from 5 × 10− 7 cm to 5 × 10− 6 cm. This is because of two facts: (1) the bubble destruction mode remains the same for all intragranular bubbles, as they are smaller than 5 × 10− 7 cm; and (2) the increase of λ only slightly promotes the re-solution of small intergranular bubbles (\~ 0.1% of total gas atoms in bubbles), and as such, the influence on results is negligible. However, reducing this variable to 5 × 10− 8 cm significantly decreased the size and density of intergranular bubbles because the destruction efficiency of intragranular bubbles was greatly enhanced, and most gas atoms stayed in solution (inset in Fig. 10(b)), which slowed down the gas atom migration process to GBs through the trapping-re-solution process. The smaller λ also prevented the establishment of a large population of intergranular bubbles.

rresol is the thickness of the destructed bubble annulus when a bubble is larger than λ (see Eqn. (6)). The variation in rresol only impacts intergranular bubbles, as the majority of the intragranular bubbles are smaller than λ (peak intragranular bubble radius: \~ 1 nm). Fig. 10(c) shows that intergranular bubble characteristics are sensitive to rresol. A thicker r (5 × 10− 9 cm vs. 3 × 10− 9 cm) made it difficult for intergranular bubbles to grow, and more gas atoms were knocked out.

For a complex computational code like DART, the sensitivity study performed in this work only covers a subset of the assumptions and parameter values applied in the code. The current results help to inform whether the models function as expected and provide information on the primary parameters that impact the results. However, a complete understanding of the uncertainties of the model inputs has not yet been obtained. For example, as discussed in a previous study [10], calibrated fission-gas-parameter values, like the set listed in Table 3, are not unique. Other combinations of parameter values may also yield satisfactory calibration results because some of the underlying mechanisms impacting the processes of fission gas bubble formation and growth counteract each other, yet the interval of parameter values within which equivalent results can be achieved is not quantified. Moreover, the sensitivity study performed here assumes independence between the tested variables, which may not be the case for some variables. It is also possible that the perturbation of two or more parameters simultaneously can, due to interactions between models, cause variation in the results greater than that of varying individual parameters alone. Therefore, a global multivariate sensitivity study designed to explore the multi-dimensional space of parameter values is required and is currently ongoing.

![](images/80c1a00ae2ec206428a6a9c72680ee4934bf521231cdc80d1779b02ad4b2df8d.jpg)  
Fig. 8. Sensitivity study results for the parameters related to the gas-atom diffusion process: (a) D0 and (b) z. The insets show the breakdown of gas atoms located in bulk, on grain faces, and on grain edges. The calculations were performed using the input parameters of V6018G and a grain size of 4.36 µm. The results calculated using the optimized values in Table 3 are presented in both figures: “D0 = 5.07×10− 31′′ in (a) and “z = 3 × 104′′ in (b), respectively.

![](images/8c9f094859822f28000435e4160392464457be522653676cfc7cdd762b4e1d70.jpg)

![](images/5a2f1776cbcd921fc9aa2e465ef485a37f4a495be6e475ec501314f981f9f16b.jpg)  
Fig. 9. Sensitivity study results for the parameters related to the bubble nucleation process: (a) fn and (b) fn-GB. The insets show the breakdown of gas atoms located in bulk, on grain faces, and on grain edges. The calculations were performed using the input parameters of V6018G and a grain size of 4.36 µm. The results calculated using the optimized values in Table 3 are presented in both figures: “fn = 2 × 10− 6′′ in (a) and “fn-GB = 6 × 10− 10′′ in (b), respectively.

## 4. U-10Mo swelling behavior up to high fission density

Using the fission-gas-behavior parameters calibrated in the previous section, the U-10Mo swelling behavior up to high fission density was simulated with DART. The simulation results in this section reveal the grain size effect on U-10Mo swelling by comparing the calculated swelling for four grain sizes, and the effect of key fission-gas-behavior parameters on the U-10Mo swelling behavior up to high fission density. Additionally, the total and constituent porosity evolutions in a 17- µm fuel were plotted to exemplify fission gas atom distribution and migration among different locations during irradiation and the impact of the grain subdivision process on fission gas behavior.

## 4.1. Calculated U-10Mo swelling for different grain sizes

U-10Mo swelling behavior up to high fission density was calculated using a constant fission rate of 5.94 × 1014 fissions/cm3 /s for four grain sizes: 1.34 µm, 4.36 µm, 8.5 µm, and 17 µm. The average fuel centerline temperatures were maintained at \~150◦C throughout the irradiation for all cases by slightly altering coolant inlet temperatures. Fuel swelling as a function of fission density is illustrated in Fig. 11. Generally, the fuels with larger grains have less swelling. The curves exhibit a clear transition in swelling rate at around 3 × 1021 – 3.5 × 1021 fissions/cm3 , becoming steeper after passing the transition fission densities due to the inception of grain subdivision. Calculated swelling values were compared with the swelling correlation developed based on in-pile irradiation data of monolithic U-10Mo fuels in Fig. 11. All calculated swelling curves stay within the vicinity of the swelling correlation. As such, taking into consideration that current calculations were performed with simplifying assumptions, such as constant fission rate and limited representation of grain morphology (no consideration of grain shape effect), etc., the calculated results shown in Fig. 11 are deemed reasonable.

As shown in Fig. 11, the 1.34-µm fuel has a different trend in swelling from other grain-size cases at high fission densities – the slope of its swelling curve decreased after \~ 4.3 × 1021 fissions/cm3 . This is because the grain refinement process has completed at this fission density in this fuel. From this point onward, the swelling increase induced by fission gasses became similar to that which occurred before grain refinement. At fission densities higher than \~ 5.1 × 1021 f/cm3 , the swelling of the 1.34-µm fuel appears lower than those of other grain sizes. Whether this swelling trend of ultra-small grain size is true is not yet tested experimentally, because all in-pile-tested fuels have mixed grain sizes, and their average grain sizes are much larger than 1.34 µm. On the other hand, the recent test of U-7Mo/Al dispersion fuel [56] did not show conclusive evidence of the advantage of larger grain in reducing swelling. More detailed investigations, both experimental and computational, are needed to verify the swelling behavior of ultra-small grains.

## 4.2. Sensitivity study on fuel swelling behavior up to high fission density

Three main parameters related to bubble nucleation (fn), re-solution (b0), and growth (D0) processes, respectively, were tested for their impact on fission gas swelling behavior up to high fission density. All calculations were conducted using a single grain size of 8.5 µm and a constant fission rate of 5.94 × 1014 fissions/cm3 ⋅s.

Fig. 12(a) presents total porosities as a function of fission density calculated by varying D0 values, keeping other parameters unchanged. The comparison results show that the elevated D value boosted bubble growth throughout the entire irradiation and resulted in a higher porosity, which is 5.1% higher for D0 = 5.07 × 10− 30 cm5 at the final fission density than that of the optimized D value (5.07 × 10− 31 cm5 ). This is because, as demonstrated in Fig. 8(a), global bubble growth was promoted with an increased D0 and a larger population of gas atoms was able to reach GBs. On the other hand, reducing the value of D0 by one order of magnitude did not significantly suppress bubble growth. The differences between the results of D0 = 5.07 × 10− 32 cm5 and those of 5.07 × 10− 31 cm5 are less than 2%. In this case, although fewer gas atoms initially migrated to the grain boundaries, more gas atoms, previously residing in bulk, were swept to grain boundaries upon the occurrence of recrystallization. However, if the D0 value was reduced to a very small value, bubble nucleation and growth can be severely restrained. Consequently, the bubble coverage on grain boundaries would be insufficient to form channels required to transport gas atoms to grain corners. As the corner bubbles are the main contributors to total porosity at high fission densities, much lower porosity is expected, as demonstrated by the result of D0 = 5.07 × 10− 36 cm5 in Fig. 12(a).

![](images/551034c6d384628dc8e03146e95ca9665500b366ade34bd2f0c31135c7b2d9b8.jpg)

![](images/642a70cbeed4f6b6a1d2e0be1ac6555410c6c8710b625bf2e5f00f78a44b1355.jpg)

![](images/abd89fe84e0af8fdb1234a4ae34eb6d9e963003ce51357894a6e5f5c4e294844.jpg)  
Fig. 10. Sensitivity study results for the parameters related to radiation-induced re-solution processes: (a) b0, (b) λ, and (c) rresol. The insets show the breakdown of gas atoms located in bulk, on grain faces, and on grain edges. The calculations were performed using the input parameters of V6018G and a grain size of 4.36 µm. The results calculated using the optimized values in Table 3 are presented in all figures: “b0 = 2 × 10− 18′′ in (a), “λ = 5 × 10− 7 cm” in (b), and “rresol = 3 × 10− 9 cm” in (c), respectively.

![](images/55d36a3e24e2018586970770f04096022c2243dae3f86fe9ff8ef89c5e0bd290.jpg)  
Fig. 11. U-10Mo swelling as a function of fission density for 4 grain sizes, compared with the U-10Mo monolithic fuel swelling correlation from Ref. [16].

The sensitivity study results for b0 are presented in Fig. 12(b). When b0 is reduced, existing bubbles are less likely to be destroyed or shrunk due to irradiation-induced re-solution. At the same time, more gas atoms are able to diffuse to the grain boundaries from the interior, as shown in Fig. 10(a). These two factors combined and gave rise to a higher porosity with a lower b0. Note that the accelerated increase in porosity at high fission densities shown in the result of b0 = 2 × 10− 19 was due to a continuous gas atom flux to grain corners subsequent to recrystallization, indicating that the calculated swelling behavior entered an unstable regime. Hence, it is deduced that, when using the selected parameter set in Table 3, a threshold value of b0 exists between 2 × 10− 19 and 2 × 10− 18, beyond which a continuous flux of gas from the grain face/edge to the grain corners will occur.

![](images/07a8de60ee8a39dcb66b9ec3452062dc7c0e34db5ca90944bacc464f6ab2b89d.jpg)

![](images/63bb8db97de9fbbaffed8d574a33903ebce92d6d54bb447f66fee8e11066d931.jpg)

![](images/260c3a80c2ecc13c0ad62bcab881ee7f19746f80ef955a901df690fc02586b1e.jpg)  
Fig. 12. Sensitivity study for (a) D0, (b) b0, and (c) fn howing their impact on total porosity up to high fission density.

The comparison shown in Fig. 12(c) indicates that total porosity is insensitive to the nucleation factor fn within the tested parameter range. This result is consistent with the comparison of intergranular bubble size distributions when varying fn in Fig. 9(a). A closer examination of where the gas atoms resided within the system revealed that the gas atom population partitions (bulk, face, and corner gas populations) are close for most of the cases tested here. For instance, between the cases of fn = 2 × 10− 8 and fn = 2 × 10− 1 , \~ 5% difference was found for the bulk and face populations and < 0.5% difference for the corner populations at the end of irradiation. On the other hand, reducing the nucleation rate to an extremely small value (2 × 10− 12) can lead to the formation of channels on the grain boundaries, through which gas atoms can continuously flow into the grain corners. The exact threshold value of fn for creating a continuous gas flow from grain faces to corners will be determined using a high-throughput approach of parameter optimization.

Besides the three main global fission-gas-behavior parameters, the effect of the saturation criteria (FaceCovMax) on fuel swelling was investigated (shown in Fig. 13). As mentioned in Section 2.2, the value of FaceCovMax = 0.907, used in the current parameter set, was estimated based on an ideal bubble packing situation, and therefore may not be achieved in all cases. The calculation results obtained using two lower values, 0.507 and 0.707, show that U-Mo swelling is sensitive to this parameter at high fission densities. This behavior is as expected, as FaceCovMax is the parameter used to gage the possibility of bubble interconnection on grain faces. The larger FaceCovMax value is, the more difficult for bubble interconnection and channel formation to occur. Since the actual bubble packing fraction probably deviates from the ideal situation, a value less than 0.907 should be utilized for future parameter optimization.

![](images/95f422ca3b48da736c6879cf83e0f3e0874333389a61e0a8af7407b6d97e01df.jpg)  
Fig. 13. Sensitivity study for FaceCovMax, showing its effect on fuel swelling up to high fission density.

The sensitivity study in this section was aimed at exploring the variation of fission gas swelling at high fission density induced by the uncertainties of the key fission-gas-behavior parameters. The results provide guidelines for future parameter optimization, which is ongoing by utilizing high throughput computation combined with neural

network-based algorithms.

Calculation results also show that fuel swelling after recrystallization is susceptible to subdivided grain size. In this study, a value of 0.5 µm was applied to all calculations. Predicted fuel swelling will reduce when the subdivided grain size is decreased from 0.5 µm. This is because with the increase of grain boundary area per unit volume, associated with the decrease of subdivided grain size, the bubble interlinkage probability at grain boundaries lowers, given that the supply of gas atom from bulk to grain boundaries is fixed. Subsequently, less gas atoms flow into the triple conjunction points and make the corner bubbles harder to grow, which are the main contributors to the total porosity after recrystallization (Section 4.3). Adjustments will be made to the subdivided grain size in the planned optimization study by taking into account the measured data of the subdivided grain size and its correlation with predicted fuel swelling.

(a)  
![](images/e2adde62660ce665e21ef4bd0760542577913f05557ddfc56151920ad79effb4.jpg)

![](images/f2b1b5b6b294559052764f9c14b047c090c293e7c8d4609c59b37f76b07f287d.jpg)

![](images/c5b03ef67c5509d000fe862c8c38ebafaf920d04bcfb6befbafd5fde51779798.jpg)

![](images/1a8ae58f88c5f8a288757d8fde92fb3fb35b2ebc8d9bc5c5a7a0e643bb711d17.jpg)

(b)  
![](images/09e7c1d77aa7eb37c8abd3ef23221820e9c72cf4bd8843e325c9081ff39b9bd6.jpg)

![](images/0e0ff384c8f4b15a75ba39bac6e62eb471c5f22d3765ef9e684dac703a611990.jpg)

![](images/925120550aa61cdaf0ab2d171efc03d4f72b01e6d34fe91a69e5d628f3d36e5d.jpg)

![](images/113dd0b2b692d5318902fa2d12f325e982de8324c9b17092360c80409b06fe8d.jpg)  
Fig. 14. Comparison of the porosities for the 1st and 50th p-nodes (nodes that are set up for tracking the grain subdivision process) in a 17-µm fuel: (a) evolution of total porosity and intergranular bubble morphology and (b) evolution of constituent porosities (bulk, face, edge, and corner bubbles).

## 4.3. Evolution of porosities with fission density

In order to understand the fission gas behavior during irradiation, particularly at high burnup, the evolution of the total and constituent porosities for the case of 17-µm fuel were plotted in Fig. 14. Porosity evolutions were compared for the 1st and 50th p-nodes because the grain subdivision process occurred in the 1st p-node but not in the 50th p-node during irradiation. The impact of the grain subdivision process on fission gas behavior can be clearly demonstrated from this comparison.

The total porosity evolution in the 17-µm fuel is exhibited in Fig. 14 (a), together with the schematics showing intergranular bubble morphologies at different development stages. As grain subdivision did not occur in the 50th p-node, the total porosity of this p-node grew stably and smoothly throughout the simulated irradiation and is mainly composed of bulk (intragranular) porosity. The total-porosity growth of the 1st p-node overlapped with that of the 50th p-node before grain subdivision, but it leaped to a value that is almost 4 times higher when grain subdivision occurred. This is because, upon the occurrence of grain subdivision (\~ 2.6 × 1021 fissions/cm3 ), all bulk gas atoms were swept to grain boundaries, which greatly promoted intergranular bubble growth. The gas sweeping phenomenon was observed in UO2 [57,58]. Although it needs further confirmation in U-Mo, its plausibility could be valid due to the fact that both fuels maintain their crystalline structure up to high burnup and their similar evolution process of grain subdivision.

After this one-off event, the gas atoms that once conglomerated grain faces were eventually absorbed by the corner bubbles, and intragranular bubbles started to form again. As a result, the total porosity of the 1st pnode dropped to a stable value within a short period and continued to grow gradually throughout the remainder of the irradiation. As the porosity used to calculate fission gas swelling is the averaged total porosities of all 50 p-nodes, the contribution of the porosity impulses that are associated with the occurrence of grain subdivision was smoothed out, and the averaged total porosity curve ascended in a stair-like manner with fission density, which can be further smoothed out using a larger number of p-nodes.

Breaking down the total porosity into the components at various locations can reveal additional information on total porosity evolution, as well as the distribution and migration path of gas atoms. Fig. 14(b) illustrates the constituent porosity evolutions within the system at the locations of bulk, grain face, grain edge, and grain corner, respectively. When there was no grain subdivision, almost all gas atoms resided within the grain interior, and the bulk porosity was the primary contributor to the total porosity. When grain subdivision took place, the bulk porosity was reduced to zero due to the gas atom sweeping mechanism, while the face and edge porosities surged to sharp peaks (see the 1st p-node curves in Fig. 14(b)). The face and edge porosities were reduced thereafter as some of these gas atoms continued to migrate to corners, and some were knocked out from bubbles due to radiationinduced re-solution. The profile of corner-porosity evolution is close to a step function. Although gas atoms continued to diffuse into or to be knocked out from corner bubbles, the size and density of these bubbles were stable after grain subdivision. This is because the corner bubbles are large enough to become insensitive to the small variations in the gas atom population within the bubbles. Note that, at this stage, the corner porosity replaced the bulk porosity to become the major contributor to the total porosity. The calculated porosity evolution in Fig. 14 agrees with the current understanding of fission gas swelling in U-Mo fuels [14–16].

Furthermore, the calculated bubble morphology at high burnup is consistent with the observations in irradiated U-Mo fuel plates. In a U-10Mo monolithic fuel plate irradiated to 9.8 × 1021 fission/cm3 , an extremely high burnup as it is beyond 100% 235U burnup based on LEU (typical enrichment of 19.75%), Gan et al. [59] observed a high concentration of small random bubbles in recrystallized grains, whose size, \~ 2 nm in diameter, is similar to the intragranular bubble size (2.4 nm in diameter at 7 × 1021 fission/cm3 ) predicted here. Gan et al. also observed that large bubbles are mostly located at the triple junction of grains while the boundaries of the subdivided grains are relatively clean from bubbles. Such characteristics agree with the calculation results presented in Fig. 14(b), in which corner porosity surpasses face and edge porosities at high fission density. The calculated corner bubble size of \~ 400 nm in diameter at 7 × 1021 fission/cm3 is also consistent with the observed bubble size in both Refs. [46] and [59], a few hundred nanometers to one micron for the bubbles at triple points. The correspondence between the calculated results and the experimental observations supports the plausibility of the current model in simulating fission gas behavior in U-Mo fuels up to high fission densities.

## 5. Effects of operating conditions on U-Mo fuel swelling

In order to examine the fission rate (FR) effect on U-Mo fuel swelling, calculations were performed for three constant fission rates: 8.92 × 1014, 5.94 × 1014, and 2.97 × 1014 fissions/cm3 /s, representing the high, medium, and low FRs in the RERTR-12 plates, respectively [50, 51]. A grain size of 8.5 µm was used in all calculations. The comparison of the calculated fuel swelling, presented in Fig. 15, shows that the swelling behavior of these three cases was very similar at low fission densities and started to deviate at \~3 × 1021 fissions/cm3 when the recrystallization process began. The discrepancies between the three curves grew larger with the increase of fission density.

In order to understand the trends observed in Fig. 15, it is important to examine the correlation between the calculation results and the variations of the FR-related fission-gas-behavior parameters and operating conditions. Both gas atom diffusion and bubble re-solution are enhanced by a similar order of magnitude when FR increases, according to Eqs. (2) and (4), respectively. These two fission-gas-behavior processes have competing effects on bubble formation and growth. Hence, increasing gas atom diffusivity and bubble re-solution rate at the same time may not necessarily change the fuel swelling behavior. The simulation results in Fig. 16(a) demonstrate that if FR and fuel temperature remained the same, increasing both D0 and b0 by one order of magnitude barely changed fuel swelling. Therefore, the increase of fuel swelling with FR may be related to fuel temperature because fuel temperature has a positive correlation with FR. Following this line of reasoning, calculations were performed by varying fuel temperature solely while keeping D0 and b0 unchanged. The results in Fig. 16(b) demonstrated that a difference of 34 ◦C resulted in a change of fuel swelling from 45.7 to 54.5% at 6 × 1021 fissions/cm3 .

![](images/e7dd8edef4c1bace58c13aa931a976845429d0c91437127ea49a530c4f4e2ac8.jpg)  
Fig. 15. U-10Mo swelling as a function of fission density calculated with grain size = 8.5 µm for a variation of constant fission rates: 8.92 × 1014, 5.94 × 1014, and 2.97 × 1014 fissions/cm3 ⋅s.

![](images/282cc8c89f30f0c14ae9bd3fb91cf2ffadfc366486b761deb7c3f77d5437fc10.jpg)

![](images/1e33cdcea8bd5b94c40fa548af31d59536d51398b252906d98bcb797fec4dd71.jpg)  
Fig. 16. U-10Mo swelling as a function of fission density calculated with grain size = 8.5 µm and constant fission rate = 5.94 × 1014 fissions/cm3 /s showing the effects of (a) the combination of D0 and b0 and (b) fuel temperature.

The results in Fig. 16 explained that the apparent fission rate effect shown in Fig. 15 was actually a fuel temperature effect and was not caused by the variances in gas-atom diffusivity or bubble re-solution rate. It is worth pointing out that the fuel temperature effect described here was not due to the increased thermal diffusion of gas atoms, which is negligible compared to the radiation-driven diffusion. Instead, it was because of the positive correlation between bubble volume and temperature as described in the equation of state. This temperature effect is stronger for large bubbles, which explains why the difference in swelling grows larger with fission density in Fig. 16(b).

## 6. Conclusions

A computational branch has been added into the DART fuel performance code to simulate U-10Mo monolithic fuel swelling behavior during irradiation. This computational branch uses a rate-theory-based mechanistic model (the GRASS module) to describe fission gas behavior in U-10Mo. As such, the potential effects of initial grain morphology and operating conditions on fuel swelling can be captured. Detailed studies were performed to improve the accuracy and reliability of the fission-gas-behavior model. In addition, phase-field-predicted U-10Mo grain-subdivision kinetics for various grain sizes was implemented in order to describe fission gas behavior at high burnup.

A few material properties were provided by atomic-scale simulation methods, but many of the parameters used in the fission-gas-behavior model were calibrated using measured fission gas bubble characteristics observed at low burnup (prior to grain subdivision), and their applicability to the calculations up to high fission density was tested and verified. Sensitivity studies for the important fission-gas-behavior parameters revealed that the implemented models behave as expected and the impact of the uncertainties of these parameters is understandable.

The calculated swelling results for the fuels with an initial grain size of 1.34 µm, 4.36 µm, 8.5 µm, or 17 µm bounded the U-10Mo swelling correlation developed based on experimental data, demonstrating that the fission-gas-behavior model and the associated parameter set used in this study can reasonably describe U-10Mo swelling behavior up to high fission density. These results also indicated that larger grains lead to a lower swelling rate.

The parametric studies on fission rate and fuel temperature showed that a higher fuel temperature or fission rate leads to increased swelling. Further examination by isolating the variation of fuel temperature from that of radiation-enhanced gas behavior (gas diffusion and irradiationinduced re-solution) revealed that the fission rate effect is primarily due to the temperature effect on bubble size but not the variances of gas atom diffusivity and bubble re-solution rate.

This work demonstrates that the updated DART code can be used to study U-10Mo monolithic fuel irradiation behavior as a function of initial microstructure and operating parameters. For future work, global sensitivity studies of the calibrated fission-gas-behavior parameters will be performed, as well as exploring the effects of additional parameters, e.g., coolant pressure, within the operating envelope of USHPRRs. Additionally, with more characterization data being collected from the recent tests, further verification and potential adjustments of the fissiongas-behavior parameters by including experimental data from different burnup regimes has been planned.

## CRediT authorship contribution statement

Bei Ye: Conceptualization, Methodology, Formal analysis, Investigation, Writing – review & editing, Resources. Aaron Oaks: Methodology, Resources. Shenyang Hu: Conceptualization, Methodology, Investigation, Writing – review & editing. Benjamin Beeler: Conceptualization, Methodology, Formal analysis, Investigation, Writing – review & editing, Resources. Jeff Rest: Conceptualization, Methodology, Formal analysis, Investigation, Writing – review & editing. Zhi-Gang Mei: Conceptualization, Methodology, Investigation, Writing – review & editing. Abdellatif Yacout: Writing – review & editing, Resources.

## Declaration of Competing Interest

The authors declare the following financial interests/personal relationships which may be considered as potential competing interests:

Bei Ye reports financial support was provided by US Department of Energy.

## Data availability

Data will be made available on request.

## Acknowledgments

This work was supported by the U.S. Department of Energy, National Nuclear Security Administration (NNSA), Office of Material Management and Minimization (NA-23) Reactor Conversion Program. The work has been created by UChicago Argonne, LLC, Operator of Argonne National Laboratory (“Argonne”). Argonne, a U.S. Department of Energy Office of Science laboratory, is operated under Contract No. DE-AC02- 06CH11357. The U.S. Government retains for itself, and others acting on its behalf, a paid-up nonexclusive, irrevocable worldwide license in said article to reproduce, prepare derivative works, distribute copies to the public, and perform publicly and display publicly, by or on behalf of the Government.

## References

[1] M.K. Meyer, J. Gan, J.F. Jue, D.D. Keiser, E. Perez, A. Robinson, D.M. Wachs, N. Woolstenhulme, G.L. Hofman, Y.S. Kim, Nucl. Eng. Technol. 46 (2) (2014) 169–181.

[2] B. Rabin, M. Meyer, J. Cole, I. Glagolenko, G. Hofman, W. Jones, J.-F. Jue, D. Keiser Jr., Y. Kim, C. Miller, G. Moore, H. Ozaltun, F. Rice, A. Robinson, J. Smith, D. Wachs, W. Williams, N. Woolstenhulme, Preliminary report on U-Mo monolithic fuel for research reactors, INL/EXT-17-40975, Rev (2017) 1.

[3] B. Beeler, et al., Microstructural-level fuel performance modeling of U-Mo monolithic fuel, INL/EXT-20-60591, Rev 0 (2020).

[4] H. Ozaltun, P.G. Medvedev, B.H. Rabin, in: Proceedings of the 26th International Conference on Nuclear Engineering, July 22-26, London, England, 2018.

[5] H. Ozaltun, B.H. Rabin, in: Proceedings of the ASME International Mechanical Engineering Congress and Exposition, Nov. 9-15, Pittsburg, PA, USA, 2018.

[6] S. Hu, V. Joshi, C.A. Lavender, JOM 69 (2017) 12.

[7] Z. Mei, L. Liang, A.M. Yacout, Comput. Mater. Sci. 142 (2018) 355–360.

[8] B. Beeler, M.W.D. Cooper, Z. Mei, D. Schwen, J. Nucl. Mater. 543 (2021), 152568.

[9] J. Rest, “The DART dispersion analysis research tool: a mechanistic model for predicting fission-product-induced swelling of aluminum dispersion fuels,” ANL-95/36 (1995).

[10] B. Ye, J. Rest, Y.S. Kim, G. Hofman, B. Dionne, Nucl. Technol. 191 (2014) 27–40.

[11] B. Ye, G.L. Hofman, A. Leenaers, A. Bergeron, V. Kuzminov, S. Van den Berghe, Y. S. Kim, H. Wallin, J. Nucl. Mater. 499 (2018) 191–203.

[12] J. Rest, “GRASS-SST: a comprehensive mechanistic model for the prediction of fission-gas behavior in UO2-base fuels during steady-state and transient conditions,” NUREG/CR-0202, ANL-78-53 (1978).

[13] D.R. Olander, D. Wongsawaeng, J. Nucl. Mater. 354 (2006) 94–109.

[14] Y.S. Kim, G.L. Hofman, J.S. Cheon, J. Nucl. Mater. 436 (2013) 14–22.

[15] A. Leenaers, W. Van Renterghem, S. Van den Berghe, J. Nucl. Mater. 476 (2016) 218–230.

[16] A.B. Robinson, W.J. Williams, W.A. Hanson, B.H. Rabin, N.J. Lybeck, M.K. Meyer, J. Nucl. Mater. 544 (2021), 152703.

[17] K. Nogita, K. Une, M. Hirai, K. Ito, K. Ito, Y. Shirai, J. Nucl. Mater. 248 (1997) 196–203.

[18] D.J. Edwards, C.H. Henager Jr., R.M. Ermi, D. Burkes, A.L. Scheme-Kohm, D. J. Senor, N.R. Overman, Characterization of U-Mo Foils For AFIP-7, Pacific Northwest National Laboratory, 2012. PNNL-21990.

[19] J. Jue, D. Keiser, Jr., J. Madden, T. Trowbridge, A. Winston, “Characterization summary report on grain size and Mo distribution in monolithic U-Mo fuels,” INL/ LTD-18-515170 (2018).

[20] Y.S. Kim, G.L. Hofman, A.B. Robinson, J.L. Snelgrove, N. Hanan, J. Nucl. Mater. 378 (2008) 220–228.

[21] Y.S. Kim, H.T. Chae, S. Van den Berghe, A. Leenaers, V. Kuzminov, A.M. Yacout, J. Nucl. Mater. 529 (2020), 151926.

[22] S. Valance, A. Monnier, H. Palancher, B. Ye, A. Yacout, in: Proceedings of RRFM 2019 meeting, 2019. Jordan, Mar. 24th –28th.

[23] D.A.G. Bruggeman, Ann. Phys. 24 (1935) 636–664 [7].

[24] V.Z. Jankus, R.W. Weeks, Nucl. Eng. Des. 18 (1) (1972) 83–96.

[25] V.Z. Jankus, 2nd Int. Conf. Structural Mechanics in Reactor Technology, Vol. VI, Part A, Suppl. D2/5, Berlin, Germany, September 10-14, 1973.

[26] G. Park, B. Beeler, M.A. Okuniewski, J. Nucl. Mater. 574 (2023), 154137.

[27] D.R. Olander, P. Van Uffelen, J. Nucl. Mater. 288 (2001) 137–147.

[28] J. Rest, J. Nucl. Mater. 321 (2003) 305–312.

[29] R.S. Nelson, J. Nucl. Mater. 31 (1969) 153–161.

[30] K. Gover, C.L. Bishop, D.C. Parfitt, S.E. Lemehov, M. Verwerft, R.W. Grimes, J. Nucl. Mater. 420 (2012) 282–290.

[31] J.A. Turnbull, J. Nucl. Mater. 38 (1971) 203–212.

[32] J.A. Turnbull, C.A. Friskney, J.R. Findlay, F.A. Johnson, A.J. Walter, J. Nucl. Mater. 107 (1982) 168–184.

[33] K. Govers, S.E. Lemehov, M. Verwerft, J. Nucl. Mater. 374 (2008) 461–472.

[34] M.L. Bleiberg, L.J. Jones, B. Lustman, J. Appl. Phys. 27 (1956) 1270–1283.

[35] J.F. Ziegler, Nucl. Instrum. Methods Phys. Res. B. 219-220 (2004) 1027–1036.

[36] D.R. Orlander, “Aspects of nuclear reactor fuel elements,” TID-26711-PI-ERDA (1976).

[37] J. Rest, G.L. Hofman, Y.S. Kim, J. Nucl. Mater. 385 (2009) 563–571.

[38] J. Rest, J. Nucl. Mater. 402 (2010) 179–185.

[39] E.E. Gruber, J. Appl. Phys. 38 (1967) 243–250.

[40] C. Ronchi, J. Nucl. Mater. 96 (1981) 314–328.

[41] M.V. Speight, Nucl. Sci. Eng. 37 (1969) 180–185.

[42] J.C. Fisher, J. Appl. Phys. 22 (1951) 74–77.

[43] J.A. Turnbull, M.O. Tucker, Phil. Mag. 30 (1974) 47.

[44] K. Maschke, H. Overhof, P. Thomas, Phys. Status Solidi (b) 60 (1973) 563.

[45] K. Nogita, K. Une, M. Hirai, K. Ito, K. Ito, Y. Shirai, J. Nucl. Mater. 248 (1997) 196.

[46] D. Jadernas, J. Gan, D. Keiser, J. Madden, M. Bachhav, J. Jue, A. Robinson, J. Nucl. Mater. 509 (2018) 1–8.

[47] J. Rest, Ed.R.J.M. Konings, T. Allen, R.E. Stoller, Comprehensive Nuclear Materials (2021). United States: N.

[48] Y.S. Kim, G.L. Hofman, J. Rest, “Characterization of intergranular fission gas bubbles in U-Mo Fuel,” ANL-08/11, Argonne National Laboratory (2008).

[49] C.J. Stanley, F.M. Marshall, in: Proc. of the 16th International Conference on Nuclear Engineering, 2008. Orlando, FL, May 11-15.

[50] D.M. Perez, M.A. Lillo, G.S. Chang, N.E. Woolstenhulme, G.A. Roth, D.M. Wachs, “RERTR-12 Insertion 1 Irradiation Summary Report,” INL/EXT-11-24101, Idaho National Laboratory (2012).

[51] D.M. Perez, G.S. Chang, D.M. Wachs, G.A. Roth, “RERTR-12 Insertion 2 Irradiation Summary Report,” INL/EXT-12-27085, Idaho National Laboratory (2012).

[52] J.C. Griess, H.C. Savage, J.L. English, “Effect of heat flux on the corrosion of aluminum by water, Part IV Tests relative to the advanced test reactor and correlation with previous results,” ORNL-3541(1964), Oak Ridge National Laboratory.

[53] ASM material data sheet http://asm.matweb.com/search/SpecificMaterial.asp? bassnum=MA6061T6.

[54] L.A. Santalo, Integral Geometry and Geometric Probability, Addison-Westly, London, 1976, p. 404.

[55] Y.S. Kim, G.L. Hofman, J. Nucl. Mater. 419 (2011) 291–301.

[56] W.A. Hanson, A.B. Robinson, N.J. Lybeck, J.W. Nielsen, B. Ye, Z. Mei, D.D. Keiser, L.M. Jamison, G.L. Hofman, A.M. Yacout, A. Leenaers, B. Stepnik, I.Y. Glagolenko, J. Nucl. Mater 564 (2022), 153683.

[57] J. Spino, J. Rest, W. Goll, C.T. Walker, J. Nucl. Mater. 346 (2005) 131–144.

[59] J. Gan, B.D. Miller, D.D. Keiser Jr., J.F. Jue, J.W. Madden, A.B. Robinson, H. Ozaltun, G. Moore, M.K. Meyer, J. Nucl. Mater. 492 (2017) 195–203.

[58] K. Nogita, K. Une, Nucl. Instrum. Methods Phys. Res., Sect. B 91 (1994) 301–306.
