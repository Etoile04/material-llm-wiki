# Integrated simulation of U-10Mo monolithic fuel swelling behavior

---

                                                               Journal of Nuclear Materials 583 (2023) 154542


                                                                  Contents lists available at ScienceDirect


                                                            Journal of Nuclear Materials
                                                       journal homepage: www.elsevier.com/locate/jnucmat




Integrated simulation of U-10Mo monolithic fuel swelling behavior
Bei Ye a, *, Aaron Oaks a, Shenyang Hu b, Benjamin Beeler c, d, Jeff Rest e, Zhi-Gang Mei a,
Abdellatif Yacout a
a
  Chemical and Fuel Cycle Technology Division, Argonne National Laboratory, 9700 S. Cass Ave. Lemont, IL 60439, USA
b
  Pacific Northwest National Laboratory, 902 Battelle Blvd, Richland, WA 99354, USA
c
  North Carolina State University, Raleigh, NC 27695, USA
d
  Idaho National Laboratory, 1955 N Fremont Ave, Idaho Falls, ID 83415, USA
e
  Independent consultant, Naperville, IL, USA




A R T I C L E I N F O                                    A B S T R A C T

Keywords:                                                A separate computational branch has been implemented within the DART (Dispersion Analysis Research Tool)
U-Mo fuel                                                computational code to simulate the swelling behavior of U-10Mo monolithic fuel under the operating conditions
Fuel performance modeling                                of high-power research and test reactors (RTRs). The monolithic branch of the DART code implements a
Fission gas behavior
                                                         mechanistic rate-theory-based fission-gas-behavior model for the calculation of fission gas swelling, as well as a
Fuel swelling
                                                         suite of thermal, physical, and mechanical models to consider various processes occurring in RTR fuels during
                                                         irradiation. To accurately simulate and eventually predict U-10Mo monolithic fuel irradiation behavior, the code
                                                         uses materials properties calculated with lower length-scale computational methods, such as gas atom diffusivity
                                                         and U-Mo surface energy from atomic simulations and grain-morphology-specific recrystallization kinetics
                                                         (recrystallized fuel volume fractions versus fission density) predicted using the phase-field method. The
                                                         remainder of the fission gas behavior parameters used in the model were calibrated with measured intergranular
                                                         bubble size distributions. With this integrated simulation approach, the swelling behavior of U-10Mo monolithic
                                                         fuel was simulated for various initial grain sizes at different operating conditions and compared with measured
                                                         data. Furthermore, because limited experimental data exist for parameter calibration, detailed sensitivity studies
                                                         for the important parameters used in the fission gas behavior model were performed to examine their impact on
                                                         both intergranular gas bubble morphology at low fission density, and on total porosity at high fission density.




1. Introduction                                                                              effects of various operational and microstructural parameters on the
                                                                                             swelling behavior of U-10Mo. Currently, a joint effort within the U.S. is
    U-Mo monolithic fuel is under development for converting highly                          ongoing across multiple universities and the national laboratory com­
enriched uranium (HEU, 235U > 20%) fuels currently used in high-power                        plex aimed at developing an integrated multi-scale simulation approach
research reactors (HPRR) in the United States to low enriched uranium                        for studying U-10Mo monolithic fuel performance [3]. This approach
(LEU, 235U < 20%) fuels [1,2]. The typical configuration of a monolithic                     incorporates engineering-scale fuel performance models [4,5] with
fuel plate is a thin U-10wt%Mo foil (~ 0.025 cm in thickness) bonded                         lower-scale and meso‑scale computational methods [6–8]. The devel­
with Zr interlayer diffusion barriers and encapsulated with Al alloy 6061                    opment of the monolithic branch of the DART (Dispersion Analysis
cladding by hot isostatic pressing (HIP). U-10wt%Mo (designated as                           Research Tool) [9–11] computational code is a part of this effort. This
U-10Mo) was selected as the fissile phase of this fuel because of its stable                 work describes the simulation scheme and capability of the DART
irradiation behavior and very-high uranium density, which can offset                         monolithic branch, results of calculations of U-10Mo swelling behavior
the loss in fuel enrichment without increasing fuel core volume [1]. One                     with different initial fuel grain sizes under various operating conditions,
of the requirements for U-10Mo monolithic fuel to be qualified is stable                     and sensitivity studies of main fission gas behavior parameters.
and predictable swelling behavior during irradiation [1,2]. Hence, it is                         The DART code was previously developed to simulate irradiation-
essential to develop a reliable simulation approach to evaluate the                          induced phenomena in dispersion fuels (U3Si2-Al and U-Mo/Al) [9,10,



    * Corresponding author.
      E-mail address: bye@anl.gov (B. Ye).

https://doi.org/10.1016/j.jnucmat.2023.154542
Received 27 January 2023; Received in revised form 25 May 2023; Accepted 26 May 2023
Available online 26 May 2023
0022-3115/Published by Elsevier B.V.
B. Ye et al.                                                                                                         Journal of Nuclear Materials 583 (2023) 154542


11]. A computational route for U-10Mo monolithic fuel has been added              it is almost impossible to obtain grain-size-specific recrystallization ki­
to DART since 2018 to separate its calculations from those of dispersion          netics from experiments, as it is extremely difficult to produce samples
fuel systems. In this monolithic branch, fission-gas-induced swelling,            that are composed of a single grain size. As an alternative solution,
one of the main causes of fuel swelling, is simulated using the GRASS             grain-size-specific recrystallization kinetics were predicted using the
(Gas Release and Swelling Subroutine) module [12], which is a                     phase field method [6] and implemented into DART.
rate-theory-based mechanistic fission-gas-behavior simulation module.                  The effects of operational parameters on fuel swelling are either
GRASS tracks bubble nucleation, re-solution, and growth processes both            difficult or expensive to study with experimental techniques because
within the grain and on grain boundaries (GBs) by solving a series of             many of these parameters are intricately interconnected. For instance,
non-linear differential equations. The output information includes not            fuel temperature is strongly dependent on the fission rate. On the other
only total porosity but also intra- and inter-granular bubble size distri­        hand, a well-designed and validated computational code is suitable for
butions at various locations (bulk, grain face, grain edge, and corner) [9,       separately studying and testing individual mechanisms proposed to
12]. Besides the GRASS module, the DART monolithic branch in­                     explain the complex irradiation behavior in fuels. The separate effects of
corporates a set of models for describing assorted physical, thermal, and         fission rate and fuel temperature are explored in this work.
mechanical processes occurring during irradiation, such as heat transfer               The following sections are organized as follows: The DART compu­
from the fuel plate center to coolant, fuel thermal conductivity degra­           tational methodology and primary models are described in Section 2, re-
dation, Al-cladding corrosion, etc. The modularized and parallelized              calibration results of fission-gas-behavior parameters and the associated
framework allows the code to simulate the irradiation behavior of a               sensitivity study in Section 3, U-Mo swelling behavior up to high fission
large-size fuel plate without compromising detailed descriptions of               density in Section 4, separate effects studies of operational parameters in
microstructural evolution.                                                        Section 5, and conclusions in Section 6.
    One of the key challenges in simulating fission-gas swelling with a
mechanistic model is to obtain the key material properties related to gas         2. DART code structure and primary models
bubble behavior [8,13], as many of them cannot be measured experi­
mentally with the currently available techniques. Some of the parame­                 This section describes the general code structure and primary models
ters can be calculated using atomic scale simulation methods. For the             of the DART monolithic branch, as well as the meshing scheme and the
parameters that do not have measurement data or atomic-scale simu­                recrystallization model in the GRASS module.
lation results, they are usually estimated by either fitting to measured
bubble morphology (e.g., gas bubble size distribution) or by borrowing            2.1. DART code structure
from other similar fuel systems where the data is available. The
fission-gas-behavior parameters used in the GRASS module were cali­                   The flowchart of the dispersion fuel branch in DART was described in
brated in a previous study [10], using the bubble size distributions              a previous publication [11]. The complete flowchart of the DART code
measured from irradiated U-10Mo dispersion fuel particles. This                   with the newly added monolithic fuel branch is displayed here to pro­
parameter set, however, needs recalibration because new atomic scale              vide an overview of the relationship between different calculation
calculation results have become available since the previous calibration          branches. As shown in the DART code flowchart of Fig. 1, the dispersion
– the surface energy of U-10Mo calculated using the density functional            and monolithic branches share the same peripheral models to simulate
theory (DFT) method [7], and the gas atom diffusivity calculated using            the heat transfer process from the centerline of the fueled zone to the
the molecular dynamics (MD) method [8]. When these parameters are                 coolant due to the similar laminated structures shared by these two types
updated, the remaining parameters need to be adjusted accordingly.                of fuels. At each time step, the code starts by calculating the thickness of
Furthermore, the previous study in Ref. [10] simulated fuel behavior at           the oxide layers caused by coolant corrosion and then proceeds to esti­
relatively low fission densities (< 3 × 1021 fissions/cm3). As the target         mate the temperatures on the oxide layer surface and at the
burnup of U-10Mo monolithic fuel may be higher than 7 × 1021 fis­                 oxide-cladding and cladding-fueled zone interfaces. The corrosion pro­
sions/cm3 in some reactors [2], it is of great interest to examine whether        cess of the coolant-side cladding surface is the same for both types of
the parameters calibrated using low-burnup measurement data can be                fuels and is described with oxide layer growth correlations [20,21]. The
applied to the high burnup regime. Therefore, recalibrating the                   implementation of the models in the thermal computational chain
fission-gas-behavior parameters and testing their applicability at high           (coolant temperature-cladding heat transfer, oxide layer growth, and
burnup have been carried out in this study.                                       heat transfer from fuel plate centerline to cladding surface) were
    Fuel swelling is closely related to its initial microstructure, such as       described in detail in Ref. [11] and have been benchmarked against the
grain morphology and impurity content. For instance, initial grain size           MAIA fuel performance code developed at the French Alternative En­
impacts fuel swelling from three aspects: (1) the number of inter-                ergies and Atomic Energy Commission (CEA) [22].
granular gas bubble nucleation sites, (2) the travel distance for gas                 The two branches diverge from each other starting from the point at
atoms from the grain interior to boundaries, and (3) the kinetics of grain        which fueled zone calculations are performed. The Bruggeman model
subdivision – subdivided fuel volume fractions as a function of fission           [23] is currently applied to approximate the thermal conductivity of
density. The first two aspects have been modeled with GRASS, while the            irradiated U-Mo by treating it as a composite material consisting of
third aspect needs additional input. Irradiation-induced grain subdivi­           fission gas bubbles and U-Mo. A more accurate model for updating the
sion/refinement in U-Mo fuel, also referred to as “recrystallization” [14,        thermal conductivity of irradiated fuel is under development and will be
15], occurs at intermediate to high fission densities (> 2 × 1021 fis­            implemented when completed. Detailed models for the calculation of
sions/cm3) during which the fuel grain size decreases from tens of                fuel swelling in the monolithic branch are described below in Sections
micron to sub-micron. Consequently, the grain boundary area per unit              2.2 – 2.4.
volume increases and fuel swelling switches from a moderate and almost
linear behavior to a nonlinear accelerated rate [14–16]. The effect of            2.2. Fission gas behavior models in the GRASS module
initial grain size on grain subdivision was observed in neutron-irradiated
UO2 fuels. It was found that grain subdivision was less likely to occur in           The GRASS module was originally developed for predicting fission-
large-grain samples [17]. Because as-fabricated U-10Mo fuel foils                 gas behavior in oxide fuels used in Liquid Metal Fast Breeder Reactors
exhibit very heterogeneous grain morphology [18,19] with the grain                (LMFBRs) and Light Water Reactors (LWRs) [24,25]. It has been vali­
size range spanning from a few microns to over a hundred microns,                 dated against various experimental data [12]. GRASS includes models
grain-size-specific recrystallization kinetics are required to simulate           for intra- and intergranular fission-gas-bubble behavior as well as a
fission gas behavior during the grain subdivision process. Nevertheless,          mechanistic description of the role of grain-edge interlinked porosity in

                                                                              2
B. Ye et al.                                                                                                              Journal of Nuclear Materials 583 (2023) 154542




                                                       Fig. 1. Flowchart of the DART computational code.


releasing fission gasses to triple points (grain corners) [12]. Most of the           CXe− intra is solved through a set of coupled differential equations
primary physics models are the same as what were described in                         described later (Eqn. (7)) by taking into account the processes for gas
Ref. [12]. One main modification was made in the radiation-induced                    atoms getting trapped in and resolved from intragranular bubbles. The
bubble re-solution model to consider the bubble-size-dependent reso­                  values of fN ranging from 10− 7 to 10− 2 were proposed for UO2 in the
lution efficiency. The equations of the main physics models are listed                literature [13]. In this study, this parameter is treated as an adjustable
below to facilitate the discussions in later sections. In addition, the value         variable to be determined by fitting to measurement data. DXe is the total
ranges of key parameters in each model were determined based on                       gas atom diffusivity, composed of intrinsic (thermal) and
recent literature of U-Mo fuels.                                                      radiation-driven components [8]:
                                                                                                                 (       )
                                                                                              (           )         1.76
2.2.1. Gas bubble nucleation                                                          DXe = 1.28 × 10− 5 × exp −            + 5.07 × 10− 31 × f˙             (2)
                                                                                                                      kT
   For intragranular gas, the rate of bubble nucleation is
                               2
NR− intra = 16π⋅fN ⋅DXe ⋅rXe ⋅CXe− intra                                   (1)        where k = 8.617 × 10− 5 is the Boltzmann constant in eV/K, T is the fuel
                                                                                      temperature in K, and f˙ is the fission rate in cm− 3s− 1. The description of
where NR− intra is the intragranular bubble nucleation rate in cm− 3s− 1; fN          radiation-enhanced diffusion is recently published [26], and the results
is the nucleation factor, describing the probability that two gas atoms               suggest radiation-enhanced diffusion does not significantly contribute to
come together to form a dimer; DXe is the diffusivity of a Xe atom in U-              the total diffusion of Xe at the operating conditions of RTRs. The un­
Mo in cm2/s; rXe = 2.16×10− 8 cm is the Xe atom radius; CXe− intra is the Xe          certainty of not including this diffusion component in the swelling
atom concentration in U-Mo grains in cm− 3. This nucleation model as­                 simulation is examined in Section 4.2. Gas atoms have faster transport
sumes a dimer as the nucleus of gas bubbles, which is a reasonable                    on grain boundaries than in the lattice [27]. Hence, gas atom diffusivity
practical treatment for handling the mathematical complexity in the                   on grain boundaries is approximated with DXe multiplied with an
simulation [13]. Although it is not stated explicitly in Eqn. (1), NR− intra is       enhancement factor z. The z value for UO2 is in the range of 102 – 107,
dependent on the intragranular bubble population because CXe− intra is                according to the estimation in Ref. [27]. The z value is treated as an
not a constant but changes with the evolution of the intragranular                    adjustable parameter in this study.
bubble population throughout the irradiation period. The variation of                    For intergranular gas, the bubble nucleation rate is assumed to have

                                                                                  3
B. Ye et al.                                                                                                                 Journal of Nuclear Materials 583 (2023) 154542


a similar expression as that of intragranular gas:                                      more likely to be knocked out in smaller bubbles and (2) the probability
                                                                                        for knock-out atoms to be trapped back to bubbles increases with bubble
NR− inter = 16π                                 2
                  ⋅(fN ⋅fN− GB )⋅(DXe ⋅z)⋅rXe ⋅CXe−                          (3)
                                                    inter                               size. Therefore, rresol can be much smaller than λ, because of the trapping
                                                                                        effect of large bubbles. Both λ and rresol are handled as adjustable vari­
where NR− inter is the intergranular bubble nucleation rate in cm− 3s− 1;
                                                                                        ables and their values are determined in this study by fitting to experi­
fN− GB is the proportional factor to be multiplied with fN ; CXe− inter is the Xe
                                                                                        mental data. Eqn. (6) also indicates that the relative re-solution effect of
atom concentration on U-Mo grain boundaries in cm− 3. Similar to
                                                                                        intergranular bubbles is much smaller than that of intragranular bub­
CXe− intra , CXe− inter changes during irradiation and is solved through Eqn.
                                                                                        bles, given the larger size of intergranular bubbles. This inference is
(7) in the model. The amount of free gas atoms on grain boundaries is the
                                                                                        reasonable because grain boundaries have strong trapping effects. A
difference of the incoming flux of gas atoms from the grain interior, the
                                                                                        steep gas-atom concentration gradient is expected to exist next to grain
atoms released from intergranular bubbles due to radiation-induced re-
                                                                                        boundaries. Ejected gas atoms within the concentration gradient can be
solution, and the loss of gas atoms to intergranular bubbles by absorp­
                                                                                        absorbed by the grain boundaries immediately [37]. The step-function
tion. Compared to those that diffuse from the grain interior, the gas
                                                                                        form for Eqn. (6) will be further modified in the future to smooth the
atoms resolved from intergranular bubbles are not the main contributors
                                                                                        transition between the two bubble-size regimes.
to CXe− inter . Bubble nucleation on grain boundaries is much more rapid at
the beginning of irradiation, but it reaches saturation much earlier than
                                                                                        2.2.3. Gas bubble growth
that in lattice [28]. Therefore, fN− GB can be much smaller than 1.
                                                                                            The GRASS module consists of a set of coupled nonlinear differential
However, since the z factor can be a large number, the difference be­
                                                                                        equations for calculating the concentrations of gas atoms and bubbles in
tween NR− inter and NR− intra (the product of fN− GB and z) is much closer to 1
                                                                                        different sizes at various locations (bulk, grain face, grain edge, and
than fN− GB .
                                                                                        grain corner). These equations take the form of [12,38]:
2.2.2. Radiation-induced bubble re-solution                                             dCi
                                                                                            = − ai Ci Ci − bi Ci + ci (i = 1, …, N)                                    (7)
   Radiation-induced bubble re-solution model adopted in DART is                         dt

b = b0 ⋅f˙⋅R                                                                 (4)        where Ci is the number of bubbles in the i th size class per unit volume;
                                                                                        ai = ai (Ci ) represents the rate at which bubbles grow out of the i th size
where b0 is the bubble destruction probability, f˙ is the fission rate, and R           class because of coalescence with bubbles in the same class; bi = bi (C1 ,
is a piecewise function representing different re-solution modes for                    …, Ci− 1 , Ci+1 , …, CN ) represents the rate at which bubbles are lost from
small and large gas bubbles. Eqn. (4) assumes gas-atom re-solution from                 the i th size class because of coalescence with bubbles in other size
a bubble is isotropic and single gas-atoms are ejected [28]. This formula               classes and re-solution; and ci = ci (C1 , …, Ci− 1 , Ci+1 , …, CN ) represents
is applied to both intra- and inter-granular gas bubbles in the DART                    the rate at which bubbles are being added to the i th size class because of
calculations.                                                                           fission gas generation and gas atom release due to re-solution (for i = 1),
    b0 can be estimated with the interaction volume of a thermal spike                  bubble nucleation (for i = 2), bubble growth resulting from bubble
with bubbles [13,29]:                                                                   coalescence and diffusion of gas atoms into bubbles (for i > 2), and
                                                                                        bubble shrinkage due to irradiation-induced re-solution (for i > 2). Size
b0 = Z02 ⋅μff                                                                (5)
                                                                                        distributions of intra- and inter-granular bubbles are obtained by solving
                                                                                        the equations in Eqn. (7) for each type of bubble.
where Z0 is the radius of a thermal spike and μff is the recoil length of
                                                                                            Bubble growth is generally achieved through the mechanism of
fission fragments. Eqn. (5) was proposed to model the dynamic bubble
                                                                                        bubble coalescence. The process of gas atom diffusion into bubbles can
re-solution process in UO2 [13,30], presuming that partial or total vol­
                                                                                        also be understood as the coalescence between bubbles and gas atoms.
umes of a bubble are “chipped away” when it is transversed by a fission
                                                                                        The probability of an i bubble coalescing with a j bubble is [12]:
fragment, and the efficiency of this sputtering mechanism is related to
                                                                                                  (       )(        )    (      )2 ⃒     ⃒
the interaction distance between the fission fragment path and the                      Pij = 4π ri + rj Di + Dj + π ri + rj ⃒vj − vi ⃒                             (8)
bubble [31,32]. For UO2, Z0 is on the order of 1–7 nm [13] and μff on the
order of 6 µm [33]. Since the electrical resistance of U-Mo is much                     where Pij is the coalescence probability in cm3/s; ri and rj in cm are the
smaller than UO2 [34], the radius of a thermal spike in U-Mo is expected                average radius of the bubbles in the i th and j-th size classes, respec­
to be smaller than that in UO2 [29]. Therefore, although the dimension                  tively; Di and Dj in cm2/s are the average diffusivity for the bubbles in
of a thermal spike was estimated to be ~13 nm in U-Mo in Ref. [34], the                 the i th and j-th size classes, respectively, calculated based on the model
value of 1–7 nm is applied in this study as an estimation of Z0 . The recoil            in [39] and inversely proportional to bubble volume; and vi and vj in
length μff is ~5 µm, which is the stopping range of 80 MeV Xe in U-10Mo                 cm/s are the velocity of the i bubble and j bubble moving in a temper­
calculated using the SRIM software [35]. Based on the reasoning above,                  ature gradient, respectively. The first and second terms on the RHS
b0 is estimated to be on the order of 10− 18 cm3.                                       (right-hand side) of Eqn. (8) are the probability of bubble interaction
    The piecewise function R is a simplified version of the model pro­                  due to random motion [39] and biased migration (induced by a tem­
posed in Ref. [28]:                                                                     perature gradient), respectively [12]. As the fuel temperature difference
     ⎧                                                                                  (~10 ◦ C) across the fuel foil thickness is insignificant, the biased
     ⎪           1
     ⎨
            (             )3 r b ≤ λ                                                    migration is not the primary driving force for bubble interaction.
R=            rb − rresol                                                (6)                The size of the bubbles in the i th size class is calculated in GRASS at
     ⎪
     ⎩  1 −                  rb > λ
                   rb                                                                   each time step using the current fuel temperature and stresses (including
                                                                                        both hydrostatic stress and U-Mo surface energy) according to the hard
where rb is the bubble radius, λ is the gas-atom knock out distance, and                sphere equation of state (EOS) developed by Ronchi [40], which was
rresol is the thickness of the annulus within which all gas-atoms are                   fitted to experimental data for argon, xenon, and krypton at high
knocked out. The order of magnitude of λ, ~ 10 nm, is borrowed from                     pressure.
the value for UO2 [30,36]. As suggested in Eqn. (6), when a gas bubble is
struck by a fission fragment, all gas atoms are ejected if the bubble size is           2.2.4. Gas-atom migration path from the grain interior to boundaries
smaller than λ. However, for a large bubble, only the gas atoms in the                     The models in GRASS assume that gas-atom generation occurs within
outer shell of the bubble are ejected. Gover’s molecular dynamics study                 grains as fission products. Gas atoms and bubbles migrate to grain
[30] on Xe-bubble re-solution in UO2 also suggests that (1) gas atoms are               boundaries through diffusion induced by a concentration gradient and a

                                                                                    4
B. Ye et al.                                                                                                          Journal of Nuclear Materials 583 (2023) 154542


temperature gradient. The gas-atom migration process from grain inte­             thermal and power calculations and is usually adapted from the settings
rior to boundaries consists of a series of intragranular trapping and             in neutronics calculations. This level of calculation is executed outside of
irradiation-induced re-solution processes. The flux of gas-atom diffusion         the GRASS module. Level-2 (k node) and level-3 (p node) meshing are set
arriving at grain boundaries is solved using Speight’s model from                 up inside each (x, z) node to facilitate GRASS calculations. K nodes
Ref. [41]. The derivation details are presented in Ref. [12] and the result       (Fig. 3(c)) represent different initial grain sizes. Four k nodes were set up
is listed here:                                                                   in this study to represent the four initial grain sizes: 1.34 µm, 4.36 µm,
                  {[                  ]0.5            }                           8.5 µm, and 17 µm, which were used in the phase-field calculations of U-
        (       )
RgI = 3 CI − Cg ⋅
                          DXe b
                                           − 2
                                               DXe b
                                                                        (9)       10Mo recrystallization kinetics described in Section 2.4. The volume of
                                                                                  each k node within a (x, z) node is defined as:
                     2
                    a (b + g)(t − t0 )       a (b + g)

           g
where RI is the rate of fission-gas-atom diffusion to the grain boundaries;       V(x,z,k) = Δx⋅Δz⋅fk ⋅y                                                      (10)
CI is the gas-atom concentration in the grain at the beginning of the time
step t0 ; Cg is the gas-atom concentration at the grain-boundary location;        where Δx and Δz are the dimensions of the (x, z) node in the x and z
a is grain radius; DXe is gas atom diffusivity in Eqn. (2); g is the proba­       directions, respectively; fk is the volume fraction of the kth type of grain;
bility of a gas atom in solution being captured by a bubble per second,           and y is the thickness of the fuel foil.
which is proportional to the coalescence probability between single gas               Each k node is further divided into multiple segments (denoted as p
atoms and bubbles in all size classes (P1j in Eqn. (8)); and b is the re-         nodes) with equal volume (V(x,y,k,p) = V(x,z,k) /p) to track the progression
solution probability, defined in Eqn. (4).                                        of grain subdivision, as shown in Fig. 3(d). The fission-gas-behavior
    When the grain-face coverage by intergranular bubbles reaches                 equations described in Section 2.2 are solved for each p node. At each
saturation, gas atoms diffuse from grain faces to grain edges. The satu­          time step, the number of p nodes that become recrystallized is deter­
ration criteria (FaceCovMax), based on an ideal situation in which the            mined according to the grain-size-specific recrystallization kinetics in
grain faces are occupied by equal-size, close-packed, round, and                  Section 2.4. Once a p node becomes recrystallized, its grain size will
touching bubbles, gives the maximum areal coverage per unit area of               change from the initial grain size to the recrystallized grain size (0.5 μm)
grain boundary as 0.907 [12]. In reality, intergranular bubbles are               and maintain this grain size until the end of irradiation. In this study, the
lenticular in shape and have a size distribution. Hence, the value of             number of p nodes is set to 50. The amount of p nodes is selected to
FaceCovMax can be less than 0.907. The sensitivity of this parameter on           enable the code to satisfactorily replicate the phase-field-calculated
swelling calculation results will be described in Section 4. A schematic          recrystallization kinetics described in Section 2.4 without consuming
showing the intergranular bubble morphology evolution with fission                excessive computational resources. Note that neither k nodes nor p
density is depicted in Fig. 2.                                                    nodes represent actual spatial locations within the fuel foil, as the rate
    The GRASS calculation for the gas-atom diffusion from grain faces to          theory method used for simulating fission gas behaviors is a mean-field-
grain edges is based on the model developed in Ref. [42]. The rate of             theory method. These meshes were set up in order to properly track
gas-atom diffusion to the edges is a function of both gas-atom diffusiv­          fission gas behavior in grains that start with different initial grain sizes
ities in lattice and on grain boundaries, and grain morphology. In this           and undergo the recrystallization process at different times during
study, grains with the same size are approximated with identical tetra­           irradiation.
kaidecahedrons. Based on this geometry, the effective distance that gas               In order to ease the computational burden of solving multiple sets of
atoms must travel before encountering an edge can be estimated. Gas               differential equations simultaneously for each of hundreds or even
atoms on edges stay trapped until an interconnected tunnel forms to               thousands of nodes, the DART code was extended with MPI (Message
allow gas atoms to migrate to the triple points (grain corners), shown in         Passing Interface)-based data communication subroutines, so that data
Fig. 2. Tunnels of open porosity along the grain edges have been                  could be passed between nodes consistently as needed. A load-balancing
observed in UO2 fuels [43]. Although no direct observation of tunnel              subroutine was added to determine the number of processes allocated to
formation in U-Mo has been made yet, the gas atom transport mecha­                a computational run and to distribute the parallel load as evenly as
nism in U-Mo from the grain interior to the triple points is assumed to be        possible. Currently, the GRASS module that performs the swelling cal­
analogous to that in UO2, as both materials maintain their crystalline            culations over the level-1 mesh elements was modified to run the cal­
structure during irradiation up to high fission densities. The probability        culations for each time step in parallel and to redistribute the results
of pore interlinkage is estimated using percolation theory [44] and is a          when complete. Further development in the parallelization calculation
function of grain size and the grain-edge bubble size distribution [12].          scheme to extend the parallel computation to level-2 and level-3 mesh
The criterion for pore tunnel formation is established using fuel swelling        elements is underway.
due to grain-edge bubbles. The threshold value of fuel swelling due to
edge bubbles (LinkSwell) is ~ 0.07 for UO2 [12] and is treated as an              2.4. Grain subdivision process
adjustable variable in this study.
                                                                                     In this study, recrystallization kinetics for four grain sizes (1.34 µm,
                                                                                  4.36 µm, 8.5 µm, and 17 µm) were calculated using a set of two-
2.3. Meshing scheme and parallelization                                           dimensional (2D) polycrystalline structures in a phase-field model [6]
                                                                                  which gives a more realistic representation of the material than a
  A three-level meshing scheme is implemented in DART. Level-1                    one-dimensional structure. The predicted recrystallization kinetics are
meshing ((x, z) node), shown in Fig. 3(a) and (b), is defined for                 displayed in Fig. 4, showing an apparent grain-size dependency.




                            Fig. 2. Schematic of intergranular gas bubble morphology and its evolution with fission density (FD).

                                                                              5
B. Ye et al.                                                                                                                Journal of Nuclear Materials 583 (2023) 154542




Fig. 3. Schematic of (a) the (x, z) meshing grid of a monolithic fuel plate, (b) side view of the plate, (c) k nodes within a (x, z) node, and (d) p nodes inside each k
node to track the progression of recrystallization.


                                                                                       dispersion fuel particles (average grain size: ~ 4.5 µm) [14], the
                                                                                       calculated recrystallization kinetics are within the uncertainty range of
                                                                                       the measurement data.
                                                                                           Fig. 5 depicts how grain subdivision is simulated in DART. At each
                                                                                       time step, the code determines whether a p node undergoes recrystalli­
                                                                                       zation by comparing the current recrystallized volume fraction with the
                                                                                       supposed value predicted with the recrystallization kinetics in Fig. 4. If
                                                                                       the current value is lower than the supposed value, more p nodes will
                                                                                       become recrystallized until the former becomes very close to the latter.
                                                                                       When a p node becomes recrystallized, its average grain diameter is
                                                                                       assumed to reduce to 0.5 µm. Microstructural characterization of irra­
                                                                                       diated U-7Mo fuel particles shows that the subdivided grain size is in a
                                                                                       range of 0.1 – 1 μm with a peak value of ~0.3 μm [46]. Thus, the
                                                                                       assumed 0.5 µm as the subdivided grain size is reasonable. A future
                                                                                       study will include the subdivided grain size as an adjustable parameter
                                                                                       in parameter optimization. The processes of gas atom migration from the
                                                                                       grain interior to the corners in the recrystallized zone are simulated
                                                                                       using the updated grain size.

                                                                                       3. Calibration of fission-gas-behavior parameters
Fig. 4. Recrystallization kinetics calculated with the phase-field method for
grain sizes 1.34 µm, 4.36 µm, 8.5 µm, and 17 µm, compared with the mea­                   Calibration of fission-gas-behavior parameters in DART was per­
surement data collected from U-10Mo dispersion fuel particles with an average          formed by fitting to intergranular bubble size distributions measured
grain size of ~ 4.5 µm. The “measurement” data is from Ref. [14].                      from samples irradiated to low fission densities, prior to the onset of
                                                                                       recrystallization. The reasons for using this specific type of data are
Larger-size grains have lower volume fractions of recrystallized fuel at a             explained as follows:
given fission density. Similar grain size effect has been observed in high
burnup UO2 fuel pellet [45]. The effects of aspect ratio and fission rate                 (1) The bubble size distribution carries more information indicating
on recrystallization are not studied explicitly in these simulations.                         the underlying mechanisms of fission gas behavior than averaged
Compared with the experimental data collected from irradiated U-10Mo                          bubble size and total porosity [47];




                                            Fig. 5. Schematics of how the recrystallization process is tracked in DART.

                                                                                   6
B. Ye et al.                                                                                                               Journal of Nuclear Materials 583 (2023) 154542


   (2) Data obtained prior to recrystallization contain information                    parameter values obtained in a previous study are also listed in the table
       closer to the early stage of bubble formation and evolution,                    for the purpose of comparison.
       without the influence of grain refinement.                                          As seen in Table 3, some parameters have quite different values from
                                                                                       those of the previous study [10]. A lot of the parameter values in the
    The applicability of the fission-gas-behavior parameters calibrated                previous study were adopted from UO2. Since then, some key parameter
with low-burnup data to the systems irradiated to high burnup is veri­                 values of U-Mo have been obtained through atomic-scale simulations.
fied in Section 4 by comparing computational results to the U-10Mo                     Considering the lattice and structure differences between UO2 and
monolithic fuel swelling correlation developed based on measured data                  U-Mo, it is expected that the re-calibrated values can be different from
[16].                                                                                  the original set. For example, the surface energy used in this study was
                                                                                       calculated using the DFT method, much more accurate than the esti­
3.1. Calculation setup and input parameters                                            mated value in the original set, as well as the linear coefficient of
                                                                                       radiation-driven gas atom diffusivity and activation energy for intrinsic
    The data measured from three miniature-size U-10Mo/Al dispersion                   gas atom diffusion. As many of the parameters are interrelated, when
fuel plates irradiated in the Advanced Test Reactor (ATR) were used for                some of them are updated, the rest need to be adjusted accordingly. For
the calibration. These plates were irradiated in the RERTR-5 test to                   future fuel performance modeling, it is recommended to use the
relatively low fission densities and no recrystallization was observed in              parameter set obtained in this study.
these plates [48]. Moreover, although these plates are dispersion fuels,                   The comparisons between the fitted and measured intergranular
in which the fuel phase exists as particles embedded in an Al matrix, the              bubble size distributions are presented in Fig. 6 for all three plates, in
fuel phase material is U-10Mo, which is the same as that in monolithic                 which the calibrated and measured peak bubble sizes agree reasonably
plates. No difference in material properties related to fission gas                    well with each other. For each plate comparison in Fig. 6, two sets of
behavior is expected, which ensures the validity of applying this set of               calculation results are presented, generated by setting single grain sizes
data for calibration. Calibration using the measured data from recently                (100 vol% for the interested grain size and 0 vol% for the other grain
completed monolithic fuel tests will be performed when the data be­                    sizes) of 4.36-µm and 8.5-µm, respectively. These two grain sizes were
comes available. The ATR operating conditions and the irradiation pa­                  employed for the comparison because they are close to the observed fuel
rameters of these three plates, as well as the input parameters for the                grain sizes listed in Table 2. The calculated bubble size distributions on
calibration calculations, are listed in Tables 1 and 2, respectively.                  grain faces are plotted in Fig. 6.
Important thermal property data are listed in Table 1 as well. The                         The primary criterion of the calibration is to obtain the best match
thickness of the coolant-side oxidation layer formed on the plate surface              between the peak positions of calibrated and measured intergranular-
is assumed to be a constant of 5 µm based on the observations of fuel                  bubble-size distributions for both grain sizes in all three plates. The
plates irradiated in the ATR [10]. For all calculations in this work, the              differences in bubble densities are less important in comparison with the
hydrostatic pressure used in the equation of state of gas bubbles is                   peak bubble size, because the experimental limitations, such as undu­
assumed to be the coolant pressure. The study of the effect of coolant                 lating sample surface and limited number of images to obtain good
pressure on fission gas bubble growth is ongoing, using the DART code                  counting statistics, etc., can lead to large uncertainties in bubble density.
integrated with a FEM (Finite Element Method)-based mechanical                         For instance, the uncertainties for the measured data in Fig. 6 are ± 10%
analysis module, and the results will be described in a future study.                  near the peak position and ± 50% at both ends of the distributions [48].
    To set up the calculations, a (x, z) node that has the dimensions of the           Besides the measurement uncertainties, many other sources can
miniature-size plates irradiated in the RERTR tests was simulated. Four k              contribute to the peak bubble density differences. An apparent one is
nodes were defined within the (x, z) node, and each of them has the                    related to the density conversion process. The experimental data was
initial grain size of 1.34 µm, 4.36 µm, 8.5 µm, and 17 µm, respectively.               initially measured as linear bubble density (number of bubbles per unit
For each calculation, a grain size distribution (volumetric fraction of                grain boundary length), while the calculation results were expressed as
each grain size) is required.                                                          volume densities. For comparison purposes, both experimental and
                                                                                       calculated quantities were converted to areal density. To achieve the
3.2. Calibration results                                                               best accuracy of density conversion, it is required that the bubbles are
                                                                                       homogeneously distributed in the material [54]. Such an ideal condition
    The optimized set of fission-gas-behavior parameters, listed in                    does not exist in the fuel plates used for calibration. Moreover, other
Table 3, were either obtained through atomic-scale simulation or                       assumptions applied for the conversions, such as the shape of grains and
selected by fitting the calculated intergranular bubble size distributions             packing patterns of bubbles, may not reflect reality well. All these un­
with measurement data. The bounding limits of each fitted parameter                    certainty factors, taken together, contribute to the deviation of the
were taken from the literature and are described in Section 2.2. The                   converted density from the data. The results in Fig. 6 show that the
                                                                                       calculated peak bubble densities are 2 – 3 times higher than the
                                                                                       measured data. Considering the uncertainties described above, this
Table 1
                                                                                       discrepancy is deemed acceptable.
Input parameters for the calibration of fission-gas-behavior parameters in DART.
                                                                                           Besides the bubble size distributions, the calibrated parameter set
  Parameter                          Value                          References         was also verified by comparing calculated and measured average bubble
  Coolant conditions                 Inlet temperature: 51⁰C        [49]               diameters, visible porosities, and swelling as shown in Fig. 7. A cutoff
                                     coolant pressure: 2.7 Mpa                         diameter of 100 nm was applied when estimating the average bubble
                                     coolant velocity: 14.5 m/s
                                                                                       diameters and visible porosities using calculated bubble size distribu­
  Node dimensions                    8.26 cm (H) × 2 cm (W) ×       [50,51]
                                     0.105 cm (T)                                      tions, which is consistent with the resolution limit of the scanning
                                     Fuel foil thickness = 0.0254                      electron micrographs (SEM) used for bubble measurement [48]. The
                                     cm                                                average bubble size and visible porosity were therefore calculated ac­
  Coolant-side oxidation layer       5 μm                                              cording to the equations below:
                                                                    [10]
    thickness
                                                                                            ∑
  Coolant-side oxidation layer       2.25 W/m⋅K                     [52]                       2Ci ri
    thermal conductivity                                                               d̄ = ∑         (ri > 50 nm)                                             (11)
                                                                                                 ci
  Cladding thermal conductivity      167 W/m⋅K                      [53]
  Unirradiated U-10Mo thermal        11.2 W/m⋅K                     [2]
    conductivity


                                                                                   7
B. Ye et al.                                                                                                                                             Journal of Nuclear Materials 583 (2023) 154542


Table 2
Characteristics of three miniature U-10Mo/Al dispersion fuel plates irradiated in the RERTR-5 test, used for fission-gas-parameter calibration [48].
  Plate ID      Fission density (fissions/cm3)     Avg. fission rate (fissions/cm3•s)      Temperature (⁰C)      If recrystallized?          Initial grain size (µm)      Avg. bubble diameter (µm)
                         21                                 14
  V6018G        2.31×10                            2.3 × 10                                121                   No                          4.9±2.0                      0.14
  V6019G        2.91×1021                          2.9 × 1014                              142                   No                          8.5±3.6                      0.16
  V8005B        2.41×1021                          2.4 × 1014                              170                   No                          8.1±4.5                      0.16




Table 3
Optimized value set of calibrated key fission-gas-behavior parameters.
  Parameter       Description                                                       Unit         Best value        Ref.         Bounding limits               Ref.           Value in previous
                                                                                                 obtained                                                                    calibration [10]

  D0              Linear coefficient of radiation-driven gas atom diffusivity       cm5          5 × 10− 31        [8]          N/A                                          8 × 10− 29
  Q               Activation energy for intrinsic gas atom diffusion                cal          40,559            [8]          N/A                                          33,000
  z               GB diffusion enhancement factor                                   N/A          3 × 104           This         102 – 107                     [27]           1 × 104
                                                                                                                   work
                                                                                                          − 7                         − 7          − 2
  fn              The probability that two intragranular gas atoms come             N/A          2 × 10            This         10          – 10              [13]           3 × 10− 8
                  together and form a di-atom bubble nucleus                                                       work
  fn-GB           Adjustment factor for bubble nucleation probability on GB         N/A          6 × 10− 10        This         can be ≪ 1                                   6 × 10− 7
                                                                                                                                                              [28]
                                                                                                                   work
  γU10Mo          Surface energy of U-10Mo                                          dyn/         1850                           N/A                                          200
                                                                                                                   [7]
                                                                                    cm
  b0              The probability for a bubble interacting with fission             cm3          2 × 10   − 18
                                                                                                                   This         on the order of               Refs. Of       7 × 10− 18
                  fragments                                                                                        work         10− 18                        Eqn. (5)
  λ               The gas-atom knock out distance from bubbles                      cm           5 × 10− 7         This         ~ 1 × 10− 6                   [30,36]        1 × 10− 6
                                                                                                                   work
  rresol          The destructed outer-shell thickness of bubbles                   cm           3 × 10− 9         This         < 1 × 10− 6                   Refs. Of       N/A
                                                                                                                   work                                       Eqn. (6)




               Fig. 6. Comparisons of measured and calibrated intergranular bubble size distributions in plates (a) V6018G, (b) V6019G, and (c) V8005B.



                                                                                                 8
B. Ye et al.                                                                                                             Journal of Nuclear Materials 583 (2023) 154542




      Fig. 7. Comparison of measured and calibrated (a) bubble diameter, (b) visible porosity, and (c) U-Mo swelling. The measured data are from Ref. [48].

                   ∑ 4π                                                              bubble density per unit length of grain boundaries to volumetric density
pvisible = 100 ×          Ci ri3 ⋅(ri > 50 nm)                           (12)
                      3                                                              [48]. As explained earlier, such conversion may introduce notable errors
                                                                                     in the resultant porosity. This can be demonstrated with the difference
where d̄ is the average bubble diameter in cm, pvisible is the percent visible       between the derived and direct measured values of plate V6019G.
porosity, and Ci in 1/cm3 and ri in cm are the number density and                    Considering the uncertainties associated with derived data, the agree­
average radius of the bubbles in the size classes whose bubble radii are             ment between calculated and measured data in Fig. 7(b) is satisfactory.
larger than 50 nm, respectively. Since the intragranular bubble size (2–3            For the comparison of total swelling shown in Fig. 7(c), the calculated
nm in diameter) is much smaller than 100 nm, the contribution from                   values are close to the measured data (differences ≤ 15%). The overall
intragranular bubbles to eqn. (11) and (12) was excluded. The experi­                agreement exhibited in Fig. 7 confirms that the parameter value set in
mental average bubble diameter, visible porosity, and swelling were                  Table 3, when applied to the models detailed in Section 2.2, can be used
reported in Ref. [48].                                                               to describe fission gas behavior in U-10Mo irradiated at conditions
    Fuel swelling includes the contributions from both gaseous and solid             similar to those listed in Tables 1 and 2.
fission products. The swelling due to fission gasses is calculated through               It is also revealed in both Figs. 6 and 7 that the bubbles in the 8.5-µm-
the summation of all bubble volumes, and solid-fission-product swelling              grain fuel have a larger size and correspondingly a lower bubble density
is proportional to fission density and expressed as [55]:                            than those in the 4.36-µm-grain fuel. These differences in bubble char­
( )
  ΔV                                                                                 acteristics are due to lower grain boundary area per unit fuel volume in
            = 4.0 × FD                                                   (13)        the larger-grain case, i.e., a reduced number of intergranular bubble
   V0 solid
                                                                                     nucleation sites.
         ( )
where      V0 solid is the percent swelling due to solid fission products, and
           ΔV
                                                                                     3.3. Sensitivity studies of the calibrated parameter set
FD is the fission density in 1021 fissions/cm3.
    As shown in Fig. 7(a), the calculated bubble sizes are slightly smaller              As many of the parameter values in Table 3 are not directly
than the measured data for these plates (differences ≤ 25%), which is                measurable, the uncertainties of the fitted values are unknown, as are
consistent with the differences in bubble size distributions shown in                their combined effects on the calculated bubble characteristics and fuel
Fig. 6 and can be explained with the uncertainties associated with                   swelling. Therefore, it is necessary to perform sensitivity studies on the
measurements. Fig. 7(b) shows that although calculated visible poros­                calibrated parameter set to examine how the uncertainties in individual
ities are generally higher than the measured quantities, the difference              parameters impact outputs qualitatively and quantitatively. The single-
between calculated and direct measurement data is small. Directly                    variable approach was taken in this work because it is practical and
measured porosity is only available for plate V6019G, and the other                  straightforward to detect whether a gas-behavior mechanism functions
measurement data were derived based on the conversion from the                       as expected. The sensitivity studies were carried out on both the

                                                                                 9
B. Ye et al.                                                                                                                Journal of Nuclear Materials 583 (2023) 154542


intergranular bubble size distribution at a low fission density, described             resulted in the relatively stuporous feedback of intergranular bubble
in this section, and on fuel swelling up to a high fission density,                    behavior to the change of fn. On the other hand, fn-GB strongly impacted
described in Section 4.2. The variation ranges for the sensitivity study               the nucleation process of intergranular bubbles but had less of a direct
were chosen according to the optimized value and bounding limits in                    influence on the incoming gas atom flux to GBs compared to fn, partic­
Table 3. For some parameters, the variation ranges are slightly larger                 ularly when the intergranular bubbles were small. Accordingly, a lot
than the bounding limits, but still in their vicinity, to test the response of         more but smaller bubbles can form on GBs with a higher nucleation rate,
the model with relatively extreme values.                                              as shown in Fig. 9(b). This trend continues with irradiation because
     For sensitivity studies on bubble size distribution, the intergranular            large bubbles more easily trap gas atoms than the small bubbles.
bubble size distributions for 4.36-µm grains using data from plate                         The other important parameters investigated are b0 , λ, and rresol , all
V6018G, irradiated to 2.31×1021 fissions/cm3, were calculated and                      of which are related to the bubble re-solution process. b0 is the proba­
compared within a range of values of each parameter.                                   bility that a bubble interacts with fission fragments and impacts all gas
     Fig. 8 shows the sensitivity study results of two diffusion-related               bubbles in the system. For larger values of b0 , gas atoms are more likely
parameters: linear coefficient of radiation-driven gas atom diffusivity                to be knocked out from existing bubbles by a transverse fission fragment,
D0 and grain-boundary diffusion enhancement factor z. The value of D0                  and more gas atoms become available (before the system achieves a new
was computed through MD simulations, and the sensitive study pre­                      equilibrium state) for nucleating new bubbles. In this case, more bubbles
sented here aimed to investigate the potential uncertainty of missing the              can nucleate but are difficult to grow, as presented in Fig. 10(a).
component of radiation-enhanced diffusion in Eqn. (2). D0 universally                      The gas-atom knock out distance from bubbles λ is applied in Eqn. (6)
impacts the diffusivities of all gas atoms in the system, while the z factor           as an approximate cut-off threshold for separating different bubble
only changes gas atom diffusivity on GBs. The results in Fig. 8 show that              destruction modes as a function of bubble size. Fig. 10(b) shows that the
increasing either D0 or z values led to similar changes in intergranular               results do not change when λ varies from 5 × 10− 7 cm to 5 × 10− 6 cm.
bubble morphology: the peaks of intergranular bubble size distribution                 This is because of two facts: (1) the bubble destruction mode remains the
moving toward the right, the profiles becoming flatter, and more gas                   same for all intragranular bubbles, as they are smaller than 5 × 10− 7 cm;
atoms staying at the GBs (shown in the breakdown of gas atom distri­                   and (2) the increase of λ only slightly promotes the re-solution of small
bution in the system in the insets of Fig. 8). Nevertheless, the reasons               intergranular bubbles (~ 0.1% of total gas atoms in bubbles), and as
underlying the bubble morphology changes are slightly different when                   such, the influence on results is negligible. However, reducing this
varying D0 or z. In the case of increasing D0, the gas migration process               variable to 5 × 10− 8 cm significantly decreased the size and density of
from the grain to the GBs was directly enhanced, according to Eqn. (9),                intergranular bubbles because the destruction efficiency of intra­
while a larger z value may lead to more rapid formation of large bubbles               granular bubbles was greatly enhanced, and most gas atoms stayed in
on GBs.                                                                                solution (inset in Fig. 10(b)), which slowed down the gas atom migration
     Both the bubble nucleation probability fn and the adjustment factor               process to GBs through the trapping-re-solution process. The smaller λ
for the nucleation probability on grain boundaries fn-GB were investi­                 also prevented the establishment of a large population of intergranular
gated for their effects on intergranular-bubble formation and growth                   bubbles.
behavior. The results shown in Fig. 9 demonstrate that increasing either                   rresol is the thickness of the destructed bubble annulus when a bubble
fn or fn-GB shifts the bubble size distribution profiles toward the left side,         is larger than λ (see Eqn. (6)). The variation in rresol only impacts inter­
i.e., reducing the peak intergranular bubble size, although to a different             granular bubbles, as the majority of the intragranular bubbles are
extent. Intergranular bubble size distributions are less sensitive to the              smaller than λ (peak intragranular bubble radius: ~ 1 nm). Fig. 10(c)
variation of fn than to that of fn-GB, within the parameter ranges exam­               shows that intergranular bubble characteristics are sensitive to rresol . A
ined here. Increasing fn inflated the gas-bubble nucleation probabilities              thicker rresol (5 × 10− 9 cm vs. 3 × 10− 9 cm) made it difficult for inter­
both in the lattice and on grain boundaries but had a relatively stronger              granular bubbles to grow, and more gas atoms were knocked out.
effect on intragranular bubbles. Consequently, the number of gasses                        For a complex computational code like DART, the sensitivity study
impinging on GBs was reduced because gas atoms generated from fission                  performed in this work only covers a subset of the assumptions and
reactions were more readily trapped in the intragranular bubbles, which                parameter values applied in the code. The current results help to inform
balanced out the effect of increased nucleation probability on GBs and                 whether the models function as expected and provide information on the




Fig. 8. Sensitivity study results for the parameters related to the gas-atom diffusion process: (a) D0 and (b) z. The insets show the breakdown of gas atoms located in
bulk, on grain faces, and on grain edges. The calculations were performed using the input parameters of V6018G and a grain size of 4.36 µm. The results calculated
using the optimized values in Table 3 are presented in both figures: “D0 = 5.07×10− 31′′ in (a) and “z = 3 × 104′′ in (b), respectively.

                                                                                  10
B. Ye et al.                                                                                                                  Journal of Nuclear Materials 583 (2023) 154542




Fig. 9. Sensitivity study results for the parameters related to the bubble nucleation process: (a) fn and (b) fn-GB. The insets show the breakdown of gas atoms located in
bulk, on grain faces, and on grain edges. The calculations were performed using the input parameters of V6018G and a grain size of 4.36 µm. The results calculated
using the optimized values in Table 3 are presented in both figures: “fn = 2 × 10− 6′′ in (a) and “fn-GB = 6 × 10− 10′′ in (b), respectively.


primary parameters that impact the results. However, a complete un­                     irradiation data of monolithic U-10Mo fuels in Fig. 11. All calculated
derstanding of the uncertainties of the model inputs has not yet been                   swelling curves stay within the vicinity of the swelling correlation. As
obtained. For example, as discussed in a previous study [10], calibrated                such, taking into consideration that current calculations were performed
fission-gas-parameter values, like the set listed in Table 3, are not                   with simplifying assumptions, such as constant fission rate and limited
unique. Other combinations of parameter values may also yield satis­                    representation of grain morphology (no consideration of grain shape
factory calibration results because some of the underlying mechanisms                   effect), etc., the calculated results shown in Fig. 11 are deemed
impacting the processes of fission gas bubble formation and growth                      reasonable.
counteract each other, yet the interval of parameter values within which                    As shown in Fig. 11, the 1.34-µm fuel has a different trend in swelling
equivalent results can be achieved is not quantified. Moreover, the                     from other grain-size cases at high fission densities – the slope of its
sensitivity study performed here assumes independence between the                       swelling curve decreased after ~ 4.3 × 1021 fissions/cm3. This is because
tested variables, which may not be the case for some variables. It is also              the grain refinement process has completed at this fission density in this
possible that the perturbation of two or more parameters simultaneously                 fuel. From this point onward, the swelling increase induced by fission
can, due to interactions between models, cause variation in the results                 gasses became similar to that which occurred before grain refinement.
greater than that of varying individual parameters alone. Therefore, a                  At fission densities higher than ~ 5.1 × 1021 f/cm3, the swelling of the
global multivariate sensitivity study designed to explore the                           1.34-µm fuel appears lower than those of other grain sizes. Whether this
multi-dimensional space of parameter values is required and is currently                swelling trend of ultra-small grain size is true is not yet tested experi­
ongoing.                                                                                mentally, because all in-pile-tested fuels have mixed grain sizes, and
                                                                                        their average grain sizes are much larger than 1.34 µm. On the other
4. U-10Mo swelling behavior up to high fission density                                  hand, the recent test of U-7Mo/Al dispersion fuel [56] did not show
                                                                                        conclusive evidence of the advantage of larger grain in reducing
    Using the fission-gas-behavior parameters calibrated in the previous                swelling. More detailed investigations, both experimental and compu­
section, the U-10Mo swelling behavior up to high fission density was                    tational, are needed to verify the swelling behavior of ultra-small grains.
simulated with DART. The simulation results in this section reveal the
grain size effect on U-10Mo swelling by comparing the calculated                        4.2. Sensitivity study on fuel swelling behavior up to high fission density
swelling for four grain sizes, and the effect of key fission-gas-behavior
parameters on the U-10Mo swelling behavior up to high fission den­                          Three main parameters related to bubble nucleation (fn), re-solution
sity. Additionally, the total and constituent porosity evolutions in a 17-              (b0 ), and growth (D0) processes, respectively, were tested for their
µm fuel were plotted to exemplify fission gas atom distribution and                     impact on fission gas swelling behavior up to high fission density. All
migration among different locations during irradiation and the impact of                calculations were conducted using a single grain size of 8.5 µm and a
the grain subdivision process on fission gas behavior.                                  constant fission rate of 5.94 × 1014 fissions/cm3⋅s.
                                                                                            Fig. 12(a) presents total porosities as a function of fission density
4.1. Calculated U-10Mo swelling for different grain sizes                               calculated by varying D0 values, keeping other parameters unchanged.
                                                                                        The comparison results show that the elevated D0 value boosted bubble
    U-10Mo swelling behavior up to high fission density was calculated                  growth throughout the entire irradiation and resulted in a higher
using a constant fission rate of 5.94 × 1014 fissions/cm3/s for four grain              porosity, which is 5.1% higher for D0 = 5.07 × 10− 30 cm5 at the final
sizes: 1.34 µm, 4.36 µm, 8.5 µm, and 17 µm. The average fuel centerline                 fission density than that of the optimized D0 value (5.07 × 10− 31 cm5).
temperatures were maintained at ~150◦ C throughout the irradiation for                  This is because, as demonstrated in Fig. 8(a), global bubble growth was
all cases by slightly altering coolant inlet temperatures. Fuel swelling as             promoted with an increased D0 and a larger population of gas atoms was
a function of fission density is illustrated in Fig. 11. Generally, the fuels           able to reach GBs. On the other hand, reducing the value of D0 by one
with larger grains have less swelling. The curves exhibit a clear transi­               order of magnitude did not significantly suppress bubble growth. The
tion in swelling rate at around 3 × 1021 – 3.5 × 1021 fissions/cm3,                     differences between the results of D0 = 5.07 × 10− 32 cm5 and those of
becoming steeper after passing the transition fission densities due to the              5.07 × 10− 31 cm5 are less than 2%. In this case, although fewer gas
inception of grain subdivision. Calculated swelling values were                         atoms initially migrated to the grain boundaries, more gas atoms, pre­
compared with the swelling correlation developed based on in-pile                       viously residing in bulk, were swept to grain boundaries upon the

                                                                                   11
B. Ye et al.                                                                                                                      Journal of Nuclear Materials 583 (2023) 154542




Fig. 10. Sensitivity study results for the parameters related to radiation-induced re-solution processes: (a) b0 , (b) λ, and (c) rresol . The insets show the breakdown of
gas atoms located in bulk, on grain faces, and on grain edges. The calculations were performed using the input parameters of V6018G and a grain size of 4.36 µm. The
results calculated using the optimized values in Table 3 are presented in all figures: “b0 = 2 × 10− 18′′ in (a), “λ = 5 × 10− 7cm” in (b), and “rresol = 3 × 10− 9 cm” in (c),
respectively.


                                                                                           occurrence of recrystallization. However, if the D0 value was reduced to
                                                                                           a very small value, bubble nucleation and growth can be severely
                                                                                           restrained. Consequently, the bubble coverage on grain boundaries
                                                                                           would be insufficient to form channels required to transport gas atoms to
                                                                                           grain corners. As the corner bubbles are the main contributors to total
                                                                                           porosity at high fission densities, much lower porosity is expected, as
                                                                                           demonstrated by the result of D0 = 5.07 × 10− 36 cm5 in Fig. 12(a).
                                                                                               The sensitivity study results for b0 are presented in Fig. 12(b). When
                                                                                           b0 is reduced, existing bubbles are less likely to be destroyed or shrunk
                                                                                           due to irradiation-induced re-solution. At the same time, more gas atoms
                                                                                           are able to diffuse to the grain boundaries from the interior, as shown in
                                                                                           Fig. 10(a). These two factors combined and gave rise to a higher porosity
                                                                                           with a lower b0 . Note that the accelerated increase in porosity at high
                                                                                           fission densities shown in the result of b0 = 2 × 10− 19 was due to a
                                                                                           continuous gas atom flux to grain corners subsequent to recrystalliza­
                                                                                           tion, indicating that the calculated swelling behavior entered an un­
                                                                                           stable regime. Hence, it is deduced that, when using the selected
                                                                                           parameter set in Table 3, a threshold value of b0 exists between 2 ×
Fig. 11. U-10Mo swelling as a function of fission density for 4 grain sizes,
                                                                                            10− 19 and 2 × 10− 18, beyond which a continuous flux of gas from the
compared with the U-10Mo monolithic fuel swelling correlation from Ref. [16].
                                                                                           grain face/edge to the grain corners will occur.

                                                                                      12
B. Ye et al.                                                                                                               Journal of Nuclear Materials 583 (2023) 154542




                    Fig. 12. Sensitivity study for (a) D0, (b) b0 , and (c) fn howing their impact on total porosity up to high fission density.


    The comparison shown in Fig. 12(c) indicates that total porosity is
insensitive to the nucleation factor fn within the tested parameter range.
This result is consistent with the comparison of intergranular bubble size
distributions when varying fn in Fig. 9(a). A closer examination of where
the gas atoms resided within the system revealed that the gas atom
population partitions (bulk, face, and corner gas populations) are close
for most of the cases tested here. For instance, between the cases of fn =
2 × 10− 8 and fn = 2 × 10− 1, ~ 5% difference was found for the bulk and
face populations and < 0.5% difference for the corner populations at the
end of irradiation. On the other hand, reducing the nucleation rate to an
extremely small value (2 × 10− 12) can lead to the formation of channels
on the grain boundaries, through which gas atoms can continuously flow
into the grain corners. The exact threshold value of fn for creating a
continuous gas flow from grain faces to corners will be determined using
a high-throughput approach of parameter optimization.
    Besides the three main global fission-gas-behavior parameters, the
effect of the saturation criteria (FaceCovMax) on fuel swelling was
investigated (shown in Fig. 13). As mentioned in Section 2.2, the value
of FaceCovMax = 0.907, used in the current parameter set, was esti­
mated based on an ideal bubble packing situation, and therefore may not
be achieved in all cases. The calculation results obtained using two
                                                                                     Fig. 13. Sensitivity study for FaceCovMax, showing its effect on fuel swelling
lower values, 0.507 and 0.707, show that U-Mo swelling is sensitive to
                                                                                     up to high fission density.
this parameter at high fission densities. This behavior is as expected, as
FaceCovMax is the parameter used to gage the possibility of bubble
interconnection on grain faces. The larger FaceCovMax value is, the
more difficult for bubble interconnection and channel formation to

                                                                                13
B. Ye et al.                                                                                                                Journal of Nuclear Materials 583 (2023) 154542


occur. Since the actual bubble packing fraction probably deviates from                 network-based algorithms.
the ideal situation, a value less than 0.907 should be utilized for future                 Calculation results also show that fuel swelling after recrystallization
parameter optimization.                                                                is susceptible to subdivided grain size. In this study, a value of 0.5 µm
   The sensitivity study in this section was aimed at exploring the                    was applied to all calculations. Predicted fuel swelling will reduce when
variation of fission gas swelling at high fission density induced by the               the subdivided grain size is decreased from 0.5 µm. This is because with
uncertainties of the key fission-gas-behavior parameters. The results                  the increase of grain boundary area per unit volume, associated with the
provide guidelines for future parameter optimization, which is ongoing                 decrease of subdivided grain size, the bubble interlinkage probability at
by utilizing high throughput computation combined with neural                          grain boundaries lowers, given that the supply of gas atom from bulk to




Fig. 14. Comparison of the porosities for the 1st and 50th p-nodes (nodes that are set up for tracking the grain subdivision process) in a 17-µm fuel: (a) evolution of
total porosity and intergranular bubble morphology and (b) evolution of constituent porosities (bulk, face, edge, and corner bubbles).

                                                                                  14
B. Ye et al.                                                                                                              Journal of Nuclear Materials 583 (2023) 154542


grain boundaries is fixed. Subsequently, less gas atoms flow into the               with the current understanding of fission gas swelling in U-Mo fuels
triple conjunction points and make the corner bubbles harder to grow,               [14–16].
which are the main contributors to the total porosity after recrystalli­               Furthermore, the calculated bubble morphology at high burnup is
zation (Section 4.3). Adjustments will be made to the subdivided grain              consistent with the observations in irradiated U-Mo fuel plates. In a U-
size in the planned optimization study by taking into account the                   10Mo monolithic fuel plate irradiated to 9.8 × 1021 fission/cm3, an
measured data of the subdivided grain size and its correlation with                 extremely high burnup as it is beyond 100% 235U burnup based on LEU
predicted fuel swelling.                                                            (typical enrichment of 19.75%), Gan et al. [59] observed a high con­
                                                                                    centration of small random bubbles in recrystallized grains, whose size,
4.3. Evolution of porosities with fission density                                   ~ 2 nm in diameter, is similar to the intragranular bubble size (2.4 nm in
                                                                                    diameter at 7 × 1021 fission/cm3) predicted here. Gan et al. also
    In order to understand the fission gas behavior during irradiation,             observed that large bubbles are mostly located at the triple junction of
particularly at high burnup, the evolution of the total and constituent             grains while the boundaries of the subdivided grains are relatively clean
porosities for the case of 17-µm fuel were plotted in Fig. 14. Porosity             from bubbles. Such characteristics agree with the calculation results
evolutions were compared for the 1st and 50th p-nodes because the                   presented in Fig. 14(b), in which corner porosity surpasses face and edge
grain subdivision process occurred in the 1st p-node but not in the 50th            porosities at high fission density. The calculated corner bubble size of ~
p-node during irradiation. The impact of the grain subdivision process              400 nm in diameter at 7 × 1021 fission/cm3 is also consistent with the
on fission gas behavior can be clearly demonstrated from this                       observed bubble size in both Refs. [46] and [59], a few hundred nano­
comparison.                                                                         meters to one micron for the bubbles at triple points. The correspon­
    The total porosity evolution in the 17-µm fuel is exhibited in Fig. 14          dence between the calculated results and the experimental observations
(a), together with the schematics showing intergranular bubble mor­                 supports the plausibility of the current model in simulating fission gas
phologies at different development stages. As grain subdivision did not             behavior in U-Mo fuels up to high fission densities.
occur in the 50th p-node, the total porosity of this p-node grew stably
and smoothly throughout the simulated irradiation and is mainly                     5. Effects of operating conditions on U-Mo fuel swelling
composed of bulk (intragranular) porosity. The total-porosity growth of
the 1st p-node overlapped with that of the 50th p-node before grain                     In order to examine the fission rate (FR) effect on U-Mo fuel swelling,
subdivision, but it leaped to a value that is almost 4 times higher when            calculations were performed for three constant fission rates: 8.92 ×
grain subdivision occurred. This is because, upon the occurrence of grain            1014, 5.94 × 1014, and 2.97 × 1014 fissions/cm3/s, representing the
subdivision (~ 2.6 × 1021 fissions/cm3), all bulk gas atoms were swept              high, medium, and low FRs in the RERTR-12 plates, respectively [50,
to grain boundaries, which greatly promoted intergranular bubble                    51]. A grain size of 8.5 µm was used in all calculations. The comparison
growth. The gas sweeping phenomenon was observed in UO2 [57,58].                    of the calculated fuel swelling, presented in Fig. 15, shows that the
Although it needs further confirmation in U-Mo, its plausibility could be           swelling behavior of these three cases was very similar at low fission
valid due to the fact that both fuels maintain their crystalline structure          densities and started to deviate at ~3 × 1021 fissions/cm3 when the
up to high burnup and their similar evolution process of grain                      recrystallization process began. The discrepancies between the three
subdivision.                                                                        curves grew larger with the increase of fission density.
    After this one-off event, the gas atoms that once conglomerated grain               In order to understand the trends observed in Fig. 15, it is important
faces were eventually absorbed by the corner bubbles, and intragranular             to examine the correlation between the calculation results and the
bubbles started to form again. As a result, the total porosity of the 1st p-        variations of the FR-related fission-gas-behavior parameters and oper­
node dropped to a stable value within a short period and continued to               ating conditions. Both gas atom diffusion and bubble re-solution are
grow gradually throughout the remainder of the irradiation. As the                  enhanced by a similar order of magnitude when FR increases, according
porosity used to calculate fission gas swelling is the averaged total po­           to Eqs. (2) and (4), respectively. These two fission-gas-behavior pro­
rosities of all 50 p-nodes, the contribution of the porosity impulses that          cesses have competing effects on bubble formation and growth. Hence,
are associated with the occurrence of grain subdivision was smoothed                increasing gas atom diffusivity and bubble re-solution rate at the same
out, and the averaged total porosity curve ascended in a stair-like                 time may not necessarily change the fuel swelling behavior. The simu­
manner with fission density, which can be further smoothed out using                lation results in Fig. 16(a) demonstrate that if FR and fuel temperature
a larger number of p-nodes.                                                         remained the same, increasing both D0 and b0 by one order of magnitude
    Breaking down the total porosity into the components at various
locations can reveal additional information on total porosity evolution,
as well as the distribution and migration path of gas atoms. Fig. 14(b)
illustrates the constituent porosity evolutions within the system at the
locations of bulk, grain face, grain edge, and grain corner, respectively.
When there was no grain subdivision, almost all gas atoms resided
within the grain interior, and the bulk porosity was the primary
contributor to the total porosity. When grain subdivision took place, the
bulk porosity was reduced to zero due to the gas atom sweeping
mechanism, while the face and edge porosities surged to sharp peaks
(see the 1st p-node curves in Fig. 14(b)). The face and edge porosities
were reduced thereafter as some of these gas atoms continued to migrate
to corners, and some were knocked out from bubbles due to radiation-
induced re-solution. The profile of corner-porosity evolution is close to
a step function. Although gas atoms continued to diffuse into or to be
knocked out from corner bubbles, the size and density of these bubbles
were stable after grain subdivision. This is because the corner bubbles
are large enough to become insensitive to the small variations in the gas
atom population within the bubbles. Note that, at this stage, the corner            Fig. 15. U-10Mo swelling as a function of fission density calculated with grain
porosity replaced the bulk porosity to become the major contributor to              size = 8.5 µm for a variation of constant fission rates: 8.92 × 1014, 5.94 × 1014,
the total porosity. The calculated porosity evolution in Fig. 14 agrees             and 2.97 × 1014 fissions/cm3⋅s.

                                                                               15
B. Ye et al.                                                                                                           Journal of Nuclear Materials 583 (2023) 154542




Fig. 16. U-10Mo swelling as a function of fission density calculated with grain size = 8.5 µm and constant fission rate = 5.94 × 1014 fissions/cm3/s showing the
effects of (a) the combination of D0 and b0 and (b) fuel temperature.


barely changed fuel swelling. Therefore, the increase of fuel swelling              that a higher fuel temperature or fission rate leads to increased swelling.
with FR may be related to fuel temperature because fuel temperature has             Further examination by isolating the variation of fuel temperature from
a positive correlation with FR. Following this line of reasoning, calcu­            that of radiation-enhanced gas behavior (gas diffusion and irradiation-
lations were performed by varying fuel temperature solely while keep­               induced re-solution) revealed that the fission rate effect is primarily
ing D0 and b0 unchanged. The results in Fig. 16(b) demonstrated that a              due to the temperature effect on bubble size but not the variances of gas
difference of 34 ◦ C resulted in a change of fuel swelling from 45.7 to             atom diffusivity and bubble re-solution rate.
54.5% at 6 × 1021 fissions/cm3.                                                         This work demonstrates that the updated DART code can be used to
    The results in Fig. 16 explained that the apparent fission rate effect          study U-10Mo monolithic fuel irradiation behavior as a function of
shown in Fig. 15 was actually a fuel temperature effect and was not                 initial microstructure and operating parameters. For future work, global
caused by the variances in gas-atom diffusivity or bubble re-solution               sensitivity studies of the calibrated fission-gas-behavior parameters will
rate. It is worth pointing out that the fuel temperature effect described           be performed, as well as exploring the effects of additional parameters,
here was not due to the increased thermal diffusion of gas atoms, which             e.g., coolant pressure, within the operating envelope of USHPRRs.
is negligible compared to the radiation-driven diffusion. Instead, it was           Additionally, with more characterization data being collected from the
because of the positive correlation between bubble volume and tem­                  recent tests, further verification and potential adjustments of the fission-
perature as described in the equation of state. This temperature effect is          gas-behavior parameters by including experimental data from different
stronger for large bubbles, which explains why the difference in swelling           burnup regimes has been planned.
grows larger with fission density in Fig. 16(b).
                                                                                    CRediT authorship contribution statement
6. Conclusions
                                                                                       Bei Ye: Conceptualization, Methodology, Formal analysis, Investi­
    A computational branch has been added into the DART fuel perfor­                gation, Writing – review & editing, Resources. Aaron Oaks: Method­
mance code to simulate U-10Mo monolithic fuel swelling behavior                     ology, Resources. Shenyang Hu: Conceptualization, Methodology,
during irradiation. This computational branch uses a rate-theory-based              Investigation, Writing – review & editing. Benjamin Beeler: Concep­
mechanistic model (the GRASS module) to describe fission gas                        tualization, Methodology, Formal analysis, Investigation, Writing – re­
behavior in U-10Mo. As such, the potential effects of initial grain                 view & editing, Resources. Jeff Rest: Conceptualization, Methodology,
morphology and operating conditions on fuel swelling can be captured.               Formal analysis, Investigation, Writing – review & editing. Zhi-Gang
Detailed studies were performed to improve the accuracy and reliability             Mei: Conceptualization, Methodology, Investigation, Writing – review
of the fission-gas-behavior model. In addition, phase-field-predicted U-            & editing. Abdellatif Yacout: Writing – review & editing, Resources.
10Mo grain-subdivision kinetics for various grain sizes was imple­
mented in order to describe fission gas behavior at high burnup.
                                                                                    Declaration of Competing Interest
    A few material properties were provided by atomic-scale simulation
methods, but many of the parameters used in the fission-gas-behavior
                                                                                        The authors declare the following financial interests/personal re­
model were calibrated using measured fission gas bubble characteris­
                                                                                    lationships which may be considered as potential competing interests:
tics observed at low burnup (prior to grain subdivision), and their
                                                                                        Bei Ye reports financial support was provided by US Department of
applicability to the calculations up to high fission density was tested and
                                                                                    Energy.
verified. Sensitivity studies for the important fission-gas-behavior pa­
rameters revealed that the implemented models behave as expected and
                                                                                    Data availability
the impact of the uncertainties of these parameters is understandable.
    The calculated swelling results for the fuels with an initial grain size
                                                                                       Data will be made available on request.
of 1.34 µm, 4.36 µm, 8.5 µm, or 17 µm bounded the U-10Mo swelling
correlation developed based on experimental data, demonstrating that
the fission-gas-behavior model and the associated parameter set used in
                                                                                    Acknowledgments
this study can reasonably describe U-10Mo swelling behavior up to high
fission density. These results also indicated that larger grains lead to a
                                                                                      This work was supported by the U.S. Department of Energy, National
lower swelling rate.
                                                                                    Nuclear Security Administration (NNSA), Office of Material Manage­
    The parametric studies on fission rate and fuel temperature showed
                                                                                    ment and Minimization (NA-23) Reactor Conversion Program. The work

                                                                               16
B. Ye et al.                                                                                                                              Journal of Nuclear Materials 583 (2023) 154542


has been created by UChicago Argonne, LLC, Operator of Argonne Na­                             [22] S. Valance, A. Monnier, H. Palancher, B. Ye, A. Yacout, in: Proceedings of RRFM
                                                                                                    2019 meeting, 2019. Jordan, Mar. 24th –28th.
tional Laboratory (“Argonne”). Argonne, a U.S. Department of Energy
                                                                                               [23] D.A.G. Bruggeman, Ann. Phys. 24 (1935) 636–664 [7].
Office of Science laboratory, is operated under Contract No. DE-AC02-                          [24] V.Z. Jankus, R.W. Weeks, Nucl. Eng. Des. 18 (1) (1972) 83–96.
06CH11357. The U.S. Government retains for itself, and others acting                           [25] V.Z. Jankus, 2nd Int. Conf. Structural Mechanics in Reactor Technology, Vol. VI,
on its behalf, a paid-up nonexclusive, irrevocable worldwide license in                             Part A, Suppl. D2/5, Berlin, Germany, September 10-14, 1973.
                                                                                               [26] G. Park, B. Beeler, M.A. Okuniewski, J. Nucl. Mater. 574 (2023), 154137.
said article to reproduce, prepare derivative works, distribute copies to                      [27] D.R. Olander, P. Van Uffelen, J. Nucl. Mater. 288 (2001) 137–147.
the public, and perform publicly and display publicly, by or on behalf of                      [28] J. Rest, J. Nucl. Mater. 321 (2003) 305–312.
the Government.                                                                                [29] R.S. Nelson, J. Nucl. Mater. 31 (1969) 153–161.
                                                                                               [30] K. Gover, C.L. Bishop, D.C. Parfitt, S.E. Lemehov, M. Verwerft, R.W. Grimes,
                                                                                                    J. Nucl. Mater. 420 (2012) 282–290.
References                                                                                     [31] J.A. Turnbull, J. Nucl. Mater. 38 (1971) 203–212.
                                                                                               [32] J.A. Turnbull, C.A. Friskney, J.R. Findlay, F.A. Johnson, A.J. Walter, J. Nucl.
 [1] M.K. Meyer, J. Gan, J.F. Jue, D.D. Keiser, E. Perez, A. Robinson, D.M. Wachs,                  Mater. 107 (1982) 168–184.
     N. Woolstenhulme, G.L. Hofman, Y.S. Kim, Nucl. Eng. Technol. 46 (2) (2014)                [33] K. Govers, S.E. Lemehov, M. Verwerft, J. Nucl. Mater. 374 (2008) 461–472.
     169–181.                                                                                  [34] M.L. Bleiberg, L.J. Jones, B. Lustman, J. Appl. Phys. 27 (1956) 1270–1283.
 [2] B. Rabin, M. Meyer, J. Cole, I. Glagolenko, G. Hofman, W. Jones, J.-F. Jue,               [35] J.F. Ziegler, Nucl. Instrum. Methods Phys. Res. B. 219-220 (2004) 1027–1036.
     D. Keiser Jr., Y. Kim, C. Miller, G. Moore, H. Ozaltun, F. Rice, A. Robinson,             [36] D.R. Orlander, “Aspects of nuclear reactor fuel elements,” TID-26711-PI-ERDA
     J. Smith, D. Wachs, W. Williams, N. Woolstenhulme, Preliminary report on U-Mo                  (1976).
     monolithic fuel for research reactors, INL/EXT-17-40975, Rev (2017) 1.                    [37] J. Rest, G.L. Hofman, Y.S. Kim, J. Nucl. Mater. 385 (2009) 563–571.
 [3] B. Beeler, et al., Microstructural-level fuel performance modeling of U-Mo                [38] J. Rest, J. Nucl. Mater. 402 (2010) 179–185.
     monolithic fuel, INL/EXT-20-60591, Rev 0 (2020).                                          [39] E.E. Gruber, J. Appl. Phys. 38 (1967) 243–250.
 [4] H. Ozaltun, P.G. Medvedev, B.H. Rabin, in: Proceedings of the 26th International          [40] C. Ronchi, J. Nucl. Mater. 96 (1981) 314–328.
     Conference on Nuclear Engineering, July 22-26, London, England, 2018.                     [41] M.V. Speight, Nucl. Sci. Eng. 37 (1969) 180–185.
 [5] H. Ozaltun, B.H. Rabin, in: Proceedings of the ASME International Mechanical              [42] J.C. Fisher, J. Appl. Phys. 22 (1951) 74–77.
     Engineering Congress and Exposition, Nov. 9-15, Pittsburg, PA, USA, 2018.                 [43] J.A. Turnbull, M.O. Tucker, Phil. Mag. 30 (1974) 47.
 [6] S. Hu, V. Joshi, C.A. Lavender, JOM 69 (2017) 12.                                         [44] K. Maschke, H. Overhof, P. Thomas, Phys. Status Solidi (b) 60 (1973) 563.
 [7] Z. Mei, L. Liang, A.M. Yacout, Comput. Mater. Sci. 142 (2018) 355–360.                    [45] K. Nogita, K. Une, M. Hirai, K. Ito, K. Ito, Y. Shirai, J. Nucl. Mater. 248 (1997) 196.
 [8] B. Beeler, M.W.D. Cooper, Z. Mei, D. Schwen, J. Nucl. Mater. 543 (2021), 152568.          [46] D. Jadernas, J. Gan, D. Keiser, J. Madden, M. Bachhav, J. Jue, A. Robinson, J. Nucl.
 [9] J. Rest, “The DART dispersion analysis research tool: a mechanistic model for                  Mater. 509 (2018) 1–8.
     predicting fission-product-induced swelling of aluminum dispersion fuels,” ANL-           [47] J. Rest, Ed.R.J.M. Konings, T. Allen, R.E. Stoller, Comprehensive Nuclear Materials
     95/36 (1995).                                                                                  (2021). United States: N.
[10] B. Ye, J. Rest, Y.S. Kim, G. Hofman, B. Dionne, Nucl. Technol. 191 (2014) 27–40.          [48] Y.S. Kim, G.L. Hofman, J. Rest, “Characterization of intergranular fission gas
[11] B. Ye, G.L. Hofman, A. Leenaers, A. Bergeron, V. Kuzminov, S. Van den Berghe, Y.               bubbles in U-Mo Fuel,” ANL-08/11, Argonne National Laboratory (2008).
     S. Kim, H. Wallin, J. Nucl. Mater. 499 (2018) 191–203.                                    [49] C.J. Stanley, F.M. Marshall, in: Proc. of the 16th International Conference on
[12] J. Rest, “GRASS-SST: a comprehensive mechanistic model for the prediction of                   Nuclear Engineering, 2008. Orlando, FL, May 11-15.
     fission-gas behavior in UO2-base fuels during steady-state and transient                  [50] D.M. Perez, M.A. Lillo, G.S. Chang, N.E. Woolstenhulme, G.A. Roth, D.M. Wachs,
     conditions,” NUREG/CR-0202, ANL-78-53 (1978).                                                  “RERTR-12 Insertion 1 Irradiation Summary Report,” INL/EXT-11-24101, Idaho
[13] D.R. Olander, D. Wongsawaeng, J. Nucl. Mater. 354 (2006) 94–109.                               National Laboratory (2012).
[14] Y.S. Kim, G.L. Hofman, J.S. Cheon, J. Nucl. Mater. 436 (2013) 14–22.                      [51] D.M. Perez, G.S. Chang, D.M. Wachs, G.A. Roth, “RERTR-12 Insertion 2 Irradiation
[15] A. Leenaers, W. Van Renterghem, S. Van den Berghe, J. Nucl. Mater. 476 (2016)                  Summary Report,” INL/EXT-12-27085, Idaho National Laboratory (2012).
     218–230.                                                                                  [52] J.C. Griess, H.C. Savage, J.L. English, “Effect of heat flux on the corrosion of
[16] A.B. Robinson, W.J. Williams, W.A. Hanson, B.H. Rabin, N.J. Lybeck, M.K. Meyer,                aluminum by water, Part IV Tests relative to the advanced test reactor and
     J. Nucl. Mater. 544 (2021), 152703.                                                            correlation with previous results,” ORNL-3541(1964), Oak Ridge National
[17] K. Nogita, K. Une, M. Hirai, K. Ito, K. Ito, Y. Shirai, J. Nucl. Mater. 248 (1997)             Laboratory.
     196–203.                                                                                  [53] ASM material data sheet http://asm.matweb.com/search/SpecificMaterial.asp?
[18] D.J. Edwards, C.H. Henager Jr., R.M. Ermi, D. Burkes, A.L. Scheme-Kohm, D.                     bassnum=MA6061T6.
     J. Senor, N.R. Overman, Characterization of U-Mo Foils For AFIP-7, Pacific                [54] L.A. Santalo, Integral Geometry and Geometric Probability, Addison-Westly,
     Northwest National Laboratory, 2012. PNNL-21990.                                               London, 1976, p. 404.
[19] J. Jue, D. Keiser, Jr., J. Madden, T. Trowbridge, A. Winston, “Characterization           [55] Y.S. Kim, G.L. Hofman, J. Nucl. Mater. 419 (2011) 291–301.
     summary report on grain size and Mo distribution in monolithic U-Mo fuels,” INL/          [56] W.A. Hanson, A.B. Robinson, N.J. Lybeck, J.W. Nielsen, B. Ye, Z. Mei, D.D. Keiser,
     LTD-18-515170 (2018).                                                                          L.M. Jamison, G.L. Hofman, A.M. Yacout, A. Leenaers, B. Stepnik, I.Y. Glagolenko,
[20] Y.S. Kim, G.L. Hofman, A.B. Robinson, J.L. Snelgrove, N. Hanan, J. Nucl. Mater.                J. Nucl. Mater 564 (2022), 153683.
     378 (2008) 220–228.                                                                       [57] J. Spino, J. Rest, W. Goll, C.T. Walker, J. Nucl. Mater. 346 (2005) 131–144.
[21] Y.S. Kim, H.T. Chae, S. Van den Berghe, A. Leenaers, V. Kuzminov, A.M. Yacout,            [58] K. Nogita, K. Une, Nucl. Instrum. Methods Phys. Res., Sect. B 91 (1994) 301–306.
     J. Nucl. Mater. 529 (2020), 151926.                                                       [59] J. Gan, B.D. Miller, D.D. Keiser Jr., J.F. Jue, J.W. Madden, A.B. Robinson,
                                                                                                    H. Ozaltun, G. Moore, M.K. Meyer, J. Nucl. Mater. 492 (2017) 195–203.




                                                                                          17
