# Formation mechanism of gas bubble superlattice in UMo metal fuels: Phase-field modeling investigation

---

                                                             Journal of Nuclear Materials 479 (2016) 202e215



                                                            Contents lists available at ScienceDirect


                                                       Journal of Nuclear Materials
                                            journal homepage: www.elsevier.com/locate/jnucmat




Formation mechanism of gas bubble superlattice in UMo metal fuels:
Phase-ﬁeld modeling investigation
Shenyang Hu*, Douglas E. Burkes, Curt A. Lavender, David J. Senor, Wahyu Setyawan,
Zhijie Xu
Paciﬁc Northwest National Laboratory, P. O. Box 999, Richland, WA 99352, USA




a r t i c l e i n f o                                 a b s t r a c t

Article history:                                      Nano-gas bubble superlattices are often observed in irradiated UMo nuclear fuels. However, the for-
Received 29 October 2015                              mation mechanism of gas bubble superlattices is not well understood. A number of physical processes
Received in revised form                              may affect the gas bubble nucleation and growth; hence, the morphology of gas bubble microstructures
24 May 2016
                                                      including size and spatial distributions. In this work, a phase-ﬁeld model integrating a ﬁrst-passage
Accepted 6 July 2016
Available online 8 July 2016
                                                      Monte Carlo method to investigate the formation mechanism of gas bubble superlattices was devel-
                                                      oped. Six physical processes are taken into account in the model: 1) heterogeneous generation of gas
                                                      atoms, vacancies, and interstitials informed from atomistic simulations; 2) one-dimensional (1-D)
Keywords:
UMo metal fuels
                                                      migration of interstitials; 3) irradiation-induced dissolution of gas atoms; 4) recombination between
Gas bubble superlattice                               vacancies and interstitials; 5) elastic interaction; and 6) heterogeneous nucleation of gas bubbles. We
One-dimensional migration                             found that the elastic interaction doesn’t cause the gas bubble alignment, and fast 1-D migration of
Radiation effects                                     interstitials along 〈110〉 directions in the body-centered cubic U matrix causes the gas bubble alignment
Phase-ﬁeld method                                     along 〈110〉 directions. It implies that 1-D interstitial migration along [110] direction should be the
                                                      primary mechanism of a fcc gas bubble superlattice which is observed in bcc UMo alloys. Simulations
                                                      also show that ﬁssion rates, saturated gas concentration, and elastic interaction all affect the morphology
                                                      of gas bubble microstructures.
                                                                                                                        © 2016 Elsevier B.V. All rights reserved.




1. Introduction                                                                        irradiation produces vacancy and interstitial defects and their
                                                                                       clusters. Because the solubility of ﬁssion gas atoms is extremely low
    The development of metallic alloy fuels such as UMo dispersion                     in UMo fuels, the gas atoms segregate and form gas bubbles. Fission
fuels and monolithic UMo fuels is part of a global effort on nuclear                   gas bubble nucleation and growth are primarily responsible for the
non-proliferation, and low-enriched uranium fuels are being                            swelling in metallic fuels. Therefore, a fundamental understanding
developed by programs throughout the world [1]. In the United                          of the effect of microstructures and irradiation conditions on gas
States, the efforts are led by the Ofﬁce of Material Management and                    bubble nucleation and growth kinetics is important for developing
Minimization Reactor Conversion Program within the National                            mitigation strategies for the swelling of the fuels and the continued
Nuclear Security Administration. Although UMo fuels have the                           development of advanced fuels for use in high-speciﬁc-power/
advantage of high density, excellent irradiation performance, and                      neutron-ﬂux research and test reactors.
good thermal conductivity, swelling of these metallic fuels over                           Gas bubble structures have been examined in post-irradiation
time is known to be much more severe than mixed-oxide fuels. This                      samples of dispersion and monolithic UMo fuels at different
characteristic is an important design parameter because it not only                    ﬁssion densities [1e6]. Descriptions of some observed gas bubble
affects the thermal conductivity of the fuels but also the mechanical                  and grain microstructure features follow. First, intragranular gas
integrity of fuel structures. Nuclear reactions continuously generate                  bubbles are small, around 1e3 nm in diameter, and tend to form gas
ﬁssion gas atoms such as Xe and Kr, while ﬁssion fragment                              bubble superlattices. Second, the gas bubble superlattice is
                                                                                       coherent with the Ue7 wt%Mo fuel that has a body-centered cubic
                                                                                       (bcc) structure with a lattice constant of 0.343 nm while the gas
 * Corresponding author.                                                               bubble superlattice has a face-centered cubic (fcc) structure. The
   E-mail address: shenyang.hu@pnnl.gov (S. Hu).                                       lattice constant of fcc gas bubble superlattices is approximately

http://dx.doi.org/10.1016/j.jnucmat.2016.07.012
0022-3115/© 2016 Elsevier B.V. All rights reserved.
                                                 S. Hu et al. / Journal of Nuclear Materials 479 (2016) 202e215                                       203


7e12 nm. Third, with the increase of ﬁssion density, the density and               cause the emission of dislocation loops. Therefore, the high pres-
size of intragranular gas bubbles increases slightly. In contrast, the             sure inside gas bubbles makes the theoretical investigation and
density and size of intergranular gas bubbles increase with ﬁssion                 modeling difﬁcult. Three possible mechanisms that have been
density. Finally, when the ﬁssion density is larger than                           proposed to explain the formation of gas bubble superlattices are 1)
4.5  1021 ﬁss/cm3, the gas bubble superlattice inside small grains                elastic interaction between bubbles, 2) planar diffusion of host
begins to collapse, and recrystallization on grain boundaries takes                interstitial atoms, and 3) dislocation loop punching from over-
place and extends to the grain interior, producing a microstructure                pressurized bubbles [4,22e24]. However, the mechanism that
with grains ranging from 100 to 500 nm in size with large inter-                   dominates the formation of gas bubble superlattices, especially fcc
granular gas bubbles. As a result, swelling kinetics increase signif-              gas bubble superlattice in bcc UMo matrix, is still an open question.
icantly. It is expected that a number of material processes such as 1)             Furthermore, the effect of radiation conditions on the evolution
the heterogeneous generation of ﬁssion defects; 2) anisotropy of                   kinetics of gas bubble superlattices has not been quantitatively
diffusivity; 3) irradiation-induced dissolution of gas atoms; 4)                   investigated.
elastic interaction; and 5) the nucleation of gas bubbles may affect                   Gas bubble evolution in U-Mo metal fuel is a complicated pro-
the formation and evolution of gas bubble superlattices. Further-                  cess. The formation and growth of gas bubbles require continuous
more, initial microstructures (such as grain sizes, second-phase                   supplies of vacancies and gas atoms by diffusion while interstitials
particles, and dislocation density) and radiation conditions (such                 can hinder the nucleation and growth of gas bubbles through
as temperature and ﬁssion rate) also may affect the formation and                  recombination or annihilation reactions. Irradiation-induced
evolution of gas bubble superlattices. The microstructures of                      dissolution of gas atoms from gas bubbles also may affect the gas
intragranular gas bubbles including bubble size distribution and                   bubble evolution kinetics. Furthermore, internal pressure inside gas
overall saturated gas concentration affect the net ﬂux of gas atoms                bubbles is high, especially in small gas bubbles. The elastic inter-
to grain boundaries and kinetics of the intergranular gas bubble                   action among gas bubbles and the cladding constraint in mono-
and recrystallization, hence, the swelling kinetics.                               lithic fuels might be important for gas bubble nucleation as well as
    It is well known that the orientation of void and gas bubble                   growth kinetics. Thermodynamic and kinetic properties of UMo
superlattices in irradiated metals usually follows those of the host               alloys and defects including Xe, vacancies, and U interstitials in bcc
lattice. For this reason, 1-D migration of self-interstitial atom (SIAs)           U single crystals have been investigated by experiments [25e28]
along the close-packed crystallographic directions is believed to be               and theoretical simulations with density functional theory (DFT)
a prime factor in many studies of void lattice formation [7e18]. The               [29e33] and the molecular dynamics (MD) method [31,34e36]. The
molecular dynamics simulations of displacement cascades have                       results show that Xe substitution is stable; the dumbbell conﬁgu-
revealed that glissile clusters of self-interstitial crowdions are                 rations of U interstitials along [100] and [110] are energetically
formed directly in cascades and during defect evolution, and that                  favored; and the migration barrier of U interstitials is about 0.1 eV,
they migrate one-dimensionally along close-packed directions                       which is much smaller than that of vacancies (0.5 eV). The defect
with extremely low activation energies [19e21]. Occasionally, un-                  generation and spatial distribution during cascades in bcc U were
der various conditions, a crowdion cluster can change its Burgers                  simulated using MD methods [37,38]. The results show that most
vector and glide along a different close-packed direction. However,                surviving interstitials have dumbbell conﬁgurations along [100]
the detailed mechanism of void and gas bubble superlattice for-                    and [110]. Almost all the interstitials remain isolated and vacancies
mation is still not well understood. Heinisch and Singh [14]                       tend to cluster into polyhedral voids [38]. The equation of state of
developed a kinetic Monte Carlo method central to the produc-                      Xe gas phase also has been examined by experiments [39e41] and
tion bias model of irradiation damage and simulated the effect of                  atomistic simulations [42]. During the past decade, the phase-ﬁeld
one-dimensional migration of self-interstitial atoms (1-D SIAs) on                 approach has been applied to study microstructure evolutions in
the formation of void lattices. Their results demonstrated that both               irradiated materials such as gas bubble evolution in UO2 nuclear
1-D migration and Burgers vectors changes of SIA clusters are                      fuels [43,44], interstitial loop growth kinetics [45], and radiation-
important for the void lattice formation. A phase-ﬁeld model                       induced segregation and precipitation [46,47]. In the current
integrating ﬁrst passage Kinetic Monte Carlo method and irradia-                   work, a phase-ﬁeld model with thermodynamic and kinetic prop-
tion induced void nucleation demonstrated that 1-D migration of                    erties obtained from experiments and atomistic simulations was
SIAs, large mean free path of SIAs and randomly void nucleation are                developed to 1) examine the effect of microstructures, thermody-
important for the void lattice formation [18]. However, Evans [15]                 namic and kinetic properties of defects, elastic interactions, and
examined some of processes involved the in the alignment of                        radiation conditions on gas bubble evolution in irradiated UMo
voids by using a similar model proposed by Heinisch et al. [14]. His               nuclear fuels, and 2) study the gas bubble superlattice formation
results suggested that 1-D SIA transport of either the crowdions or                mechanism.
small interstitial clusters may cause the coalescence between                          The organization of this paper is described here. In Section 2, the
neighboring voids along the crystallographic directions and pre-                   phase-ﬁeld model of gas bubble evolution in the irradiated UMo
vent the precise void lattice formation. Recently, Semenov et al.                  alloys is described. The thermodynamic and kinetic properties used
[16,17] investigated the effect of system instability and symmetry-                in the simulations are assessed and discussed in Section 3. The
breaking on void lattice formation. They found that the presence                   parameters of the phase-ﬁeld model and simulation cell are listed
of a small amount of 1-D migrating SIAs with mean-free path                        in Section 4. The simulation results describing the effect of irradi-
comparable to the average distance between voids can bias the void                 ation conditions on gas bubble evolution kinetics and gas bubble
coarsening process, such that the non-aligned voids have a much                    structures are presented in Section 5. Conclusions and discussion
larger probability to shrink than the aligned ones.                                are given in Section 6.
    Unlike voids, there exists a high internal pressure inside nano-
sized gas bubbles. Experimental results show that the pressure of                  2. Description of multicomponent and multiphase phase-
Xe gas bubbles is about several GPa which depends on the gas                       ﬁeld model
bubble size and Xe concentration inside the gas bubble. Such a high
pressure might cause long range elastic interaction among gas                         In this work, we consider gas bubble evolution in bcc UMo
bubbles and gas bubble alignment to minimize the deformation                       nuclear fuels. Microstructure and defects in irradiated UMo fuels is
energy of the system. The over-pressured gas bubbles might also                    complicated. Mo usually depletes at grain boundaries and enriches
204                                                     S. Hu et al. / Journal of Nuclear Materials 479 (2016) 202e215


at the center of the grain because of congruent growth during so-
                                                                                                                X        ka
lidiﬁcation [48]. Depletion of Mo at grain boundaries may affect the                      fs ¼ f0 ðhÞ þ                       ðVha Þ2                                                (3)
stability of bcc UMo phase and lead to a phase transition from                                               a¼0;1;2;…;N
                                                                                                                         2
gamma U to alpha U [49,50]. Such an inhomogeneous Mo distri-
bution also may cause internal stresses because the bcc UMo lattice                                                                                            0                     1
constant is dependent on the Mo concentration. Furthermore, the                                          X                4                       X              X ga;b
                                                                                                                          ha       h2a                         @              2 2A
ﬁssion reaction of 235U generates different gas atoms including Xe,                       f0 ðhÞ ¼                 ma                       þ                               ha hb
                                                                                                     a¼0;1;2;…;N
                                                                                                                          4        2             a¼0;1;2;…;N
                                                                                                                                                                         2
Kr, and I. Meanwhile, the ﬁssion fragment cascade generates point                                                                                                  bsa
defects and defect clusters. To simplify the description of the sys-                                     1
                                                                                                     þ
tem without losing the physics, a uniform distribution of Mo was                                         4
assumed, which implies that the system has a single bcc phase and                                                                                                                    (4)
no internal stress; all ﬁssion gas atoms (Xe, Kr, I, …) were consid-
ered to be Xe atoms, and defect clusters generated by ﬁssion frag-                        where ma , ka and ga;b are model parameters determined by the
ment cascades were replaced by the same amount of point defects.                          properties of the interface between a andb phases. Parameters ma
We further assumed that two phases (i.e., the Xe gas phase and                            and ka are determined by interfacial energy and interface thickness
matrix bcc UMo phase) coexist, the ﬁssion center is a heteroge-                           while ga;b is determined by interfacial symmetry. For the case
neous nucleation site of gas bubbles because a large vacancy cluster                      ignoring the ga;b terms in equation (4), quantitative relationships
might form during the irradiation as shown in MD simulations [38],                        between these model parameters and interfacial properties can be
and interstitials with dumbbell conﬁgurations in 〈110〉 directions                         obtained by thin interface limit analysis [53,54]. Since the free
migrate along [110] directions while vacancies and Xe have                                energy in equation (4) has intercrossed terms ga;b , we use a nu-
isotropic diffusivity. With the assumptions described above, the gas                      merical method to determine the parameters ma and ka . Especially,
bubble microstructures in a polycrystalline UMo alloy can be                              we consider a one dimension problem with an interface of interest
uniquely described by the following phase-ﬁeld variables: 1) three                        (such as gas bubble/grain, and grain/grain interface). We optimize
concentration variables c ¼ fc1 ðr; tÞ; c2 ðr; tÞ; c3 ðr; tÞg presenting the              the model parameters ma and ka to ensure that the properties of
concentrations of U and Mo interstitials, vacancies, and Xe atoms,                        the interface including the interfacial energy and interface thick-
respectively; 2) one order-parameter variable h0 ðr; tÞ presenting                        ness are satisﬁed.
the distribution of gas bubbles that is equal to 1 inside a gas bubble                        Generally speaking, the diffusion of vacancies, interstitials, and
and 0 outside the gas bubble; and 3) a set of order parameters                            gas atoms and gas bubble evolution can be simulated by solving the
fh1 ðr; tÞ; h2 ðr; tÞ; ::::; hN ðr; tÞg presenting the grain orientations at              Cahn-Hilliard and Allan-Cahn equations, which are similar to
position r and time t. The multicomponent and multiphase free                             conventional phase-ﬁeld models [43]. However, both experiments
energy model was employed to describe the total free energy of the                        and MD simulations show that interstitials in UMo alloys have a
system Fðh0 ; h; cÞ [51e53] that is expressed as a function of the                        much larger diffusivity than that of vacancies [28,36,55]. With the
order-parameter ﬁeld h ¼ fh0 ðr; tÞ; h1 ðr; tÞ; h2 ðr; tÞ; ::::; hN ðr; tÞg               migration barriers, 0.1 eV for interstitials and 0.5 eV for vacancies in
and molar-fraction ﬁeld c ¼ fc1 ðr; tÞ; c2 ðr; tÞ; c3 ðr; tÞg:                            bcc UMo alloys, the diffusivities can be calculated, resulting in a
                                                                                          diffusivity of interstitials about ﬁve orders of magnitude larger than
                                                                                          that of vacancies at 400 K. The time step solving the diffusion
            Z                                                                             equations of vacancies, interstitials, and Xe atoms can be estimated
Fðh; cÞ ¼       ½fs ðhÞ þ fb ðh; cÞ þ felas ðh; cÞdV                          (1)        by Dt ¼ minðDx2 =DSIA ; Dx2 =DVac ; Dx2 =DXe Þ, where Dx is the grid
                                                                                          size in the simulation cell, and Di ði ¼ SIA; Vac; XeÞ is the diffusivity
            V
                                                                                          of a self-interstitial atom, vacancy, and Xe, respectively. Therefore,
where V is the volume of the system, fb is the chemical free energy                       the interstitial diffusivity will determine the time step in the sim-
density, fs is the gradient energy density representing interfacial                       ulations under the assumption that a vacancy and Xe have the same
energy, and felas is the elastic energy density associated with lattice                   diffusivity. A very small time step is required to solve the diffusion
mismatch of defects and applied stresses.                                                 equations because of the large diffusivity of interstitials, which
   The chemical free energy density in equation (1) is deﬁned as                          signiﬁcantly affects the numerical efﬁciency in phase-ﬁeld
                                                                                          modeling. Furthermore, the interstitials usually have very strong
                                                                                          anisotropic diffusivity. For example, both atomistic simulations and
          X                                                                               in situ transmission electron microscopy (TEM) results demon-
fb ¼                 ha fa ðca Þ                                               (2)        strate that interstitials with a dumbbell conﬁguration along 〈110〉
       a¼0;1;2;…;N                                                                        directions migrate along 〈110〉 directions in bcc Fe. Because density
                                                                                          functional theory and MD results show that both the formation
where fa ðca Þ is the chemical free energy of a phases. For example,                      energy for the dumbbell conﬁguration of U interstitials along 〈110〉
f0 ðc0 Þ is the free energy of the Xe gas phase, and                                      direction and migration barrier of interstitials are low, it is
fa ðca Þ; ða ¼ 1; 2; …; NÞ is the free energy of the matrix phase. We                     reasonable to assume that the U interstitial (SIA) migrates along
assumed that different phases at point r have different concentra-                        〈110〉 direction of bcc UMo similar to that in bcc Fe. The strong
tions,         but         the         same          chemical        potential            anisotropy of interstitial migration causes additional difﬁculty in
vfa ðca Þ=vca i ¼ vfb ðcb Þ=vcb i ; ða; b ¼ 0; 1; 2; …; N; and i ¼ 1; 2; 3Þ.              solving the diffusion equation. In our work, the phase-ﬁeld model
The term ha ðhÞ is a shape function that is related to the volume                         coupling a one-dimensional random walk model, ﬁrst developed to
fraction of a phase at point r. The concentration satisﬁes the                            simulate the void lattice formation [18], was extended to study the
                                    P
constraint equation c ¼                   ha ðhÞca . In addition, to correctly            gas bubble evolution with a large difference and strong anisotropy
                                   a¼0;1;…;N
                                                                                          of defects’ diffusivity. We used the ﬁrst-passage Monte Carlo
describe the equilibrium properties at a triple point of three                            method to describe the one-dimensional migration of interstitials
different phases such as a gas bubble and two different grains, the                       [18,56,57], and the phase-ﬁeld model is used to describe the evo-
                                           P
shape function is deﬁned as ha ðhÞ ¼ h2a = N      2
                                             r¼0 hr . The gradient                        lution of defects and microstructure.
energy density in equation (1) is given as                                                    The one-dimensional migration of interstitials was viewed as a
                                                           S. Hu et al. / Journal of Nuclear Materials 479 (2016) 202e215                                                205


random walk along speciﬁc directions. Considering an interstitial                                                pﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
from the position r0 ¼ 0 and time t0 ¼ 0, the probability that the                                                ZDSIA Dt
interstitial reaches the position r at time t is the solution of the                                                                00         00
                                                                                              p Drk0 ; Dt ¼                    p Drk ; Dt drk                            (7)
diffusion equation:
                                                                                                                  Drk0
                                                                                                                  00  
                                                                                              where Drk ¼ rk  rk0  is the distance between rk and rk0 , and
                                                                                                            00                                       00


                                                                                                   0
                                                                                              pðDrk ; DtÞ is the shadow area as shown in Fig. 1(b). In this case the
vpðr; tÞ       v2                                                                             summation over k in equation (6) runs from 1 to 6 because there is
         ¼ DSIA 2 pðr; tÞ                                                           (5)       no interstitial ﬂux to the point r from the sink side.
  vt           v r
                                                                                                 The second contribution is the generation of SIAs g_ SIA ðr; tÞDt,
with an initial condition pðr; 0Þ ¼ dð0; 0Þ; and boundary condition                           and the third contribution is the reaction between vacancies and
pðr ¼ ∞; tÞ ¼ 0. DSIA is the diffusivity of the interstitial, and d is the                    SIAs g_ SIA ðr; tÞDt. Therefore, the evolution equation of interstitials
Kronecker delta function. For a given SIA distribution, c1 ðr; tÞ at                          can be written as:
time t, the change of SIA concentration, Dc1 ðr; tÞ after a time step
Dt, includes three contributions. The ﬁrst contribution was asso-                             vc1
                                                                                                  ¼ Dc1 ðr; tÞ þ g_ SIA ðr; tÞ  _gSIA ðr; tÞ                            (8)
ciated with the one-dimensional migration of SIAs along the 12                                 vt
〈110〉 directions in a bcc crystal. It is usually true that SIAs cannot                            The microstructure evolution including gas bubbles and grains
penetrate through sinks such as voids, gas bubbles, and grain                                 is controlled by the time dependent Cahn-Hilliard equations [58]
boundaries so that SIAs accumulate on the interface of sinks when                             and Allen-Cahn equations [59]:
SIAs approach sinks. Fig. 1 schematically shows the probability that
                                                                                                                               !
interstitials at the point rk0 migrate to the position r at time Dt,                          vci      X       dF
where rk0 is one point on lines that pass through the point r and                                 ¼ V$   Mij V                     þ g_ i  _gi þ xi ;   ði ¼ 2; 3Þ    (9a)
                                                                                              vt              d cj
have one of the 12 〈110〉 directions. If both r and rk0 do not locate on                                j

sink interfaces as shown in Fig. 1(a), the change of SIA concentra-
tion at the point r resulting from one-dimensional migration of SIAs                          vhr       dF
can be calculated as                                                                              ¼ Lr     þ xr ;             r ¼ 0; 1; 2; :::; N                     (9b)
                                                                                               vt       dhr

                                                                                              where Mij and Lr are mobility coefﬁcients, and xi and xr are the
                                                                                              thermal ﬂuctuations. In equation (9a), g_ i is the generation rate of
                                                                                              defect i, and g_ i is the reaction rate that is proportional to diffusivity
               12 Z
                     Rk
               X    1  0   0                                                          and concentrations of defects. The g_ i and g_ i could be calculated by
Dc1 ðr; tÞ ¼         c r ; t p Drk ; Dt  pð0; DtÞd rk0  r drk0                              the same expressions in the rate theory [60,61]. A sink term of
                    6 1 k
               k¼1                                                                            defects can be added into equations (8) and (9a) to take the effect of
                     0
                                                                                    (6)       defects such as distributed dislocations on the accumulation of
                                                                                              interstitials and vacancies.
where pðDrk0 ; DtÞ and pð0; DtÞ are the solution of equation                   (5), k           By numerically solving these two groups of equations (8,9a and
represents runs for 12 different 〈110〉 directions,            D r 0 ¼ r 0  r  is the       b), we can obtain the spatial and temporal evolution of the phase-
                                                    pﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
                                                                  k      k
distance between rk0 and r, and Rk ¼p                                0
                                            ﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃDSIA Dt ; Rk Þ is the min-
                                          minð                                                ﬁeld       variables        of        c ¼ fc1 ðx; tÞ; c2 ðx; tÞ; c3 ðx; tÞg and
imum value of the mean free path DSIA Dt of an SIA during the                                 h ¼ fh0 ðx; tÞ; h1 ðx; tÞ; h2 ðx; tÞ; ::::; hN ðx; tÞg, and thus the micro-
time step Dt and R0k that is the distance between the point r and the                         structure evolution. In this generic phase-ﬁeld model, the chemical
surface of the nearest sink such as gas bubble and grain boundaries                           free energy density fb is a function of concentration and order-
along the kth direction. If r locates on a sink boundary, the proba-                          parameter ﬁelds, while the gradient energy density fs is described
bility pðDrk0 ; DtÞ in equation (6) is calculated by                                          by order-parameter ﬁelds shown in equations (2) and (3). The




                                             Fig. 1. Probability distribution of a random walker at Dt from initial position rk0 at t ¼ 0.
206                                               S. Hu et al. / Journal of Nuclear Materials 479 (2016) 202e215


unknown parameters, m, k and gr;s ðjr;s ; m     ~ Þ, are completely deter-
mined by the grain boundary and/or interface properties, and are
independent               of         the       concentration        ﬁelds
c ¼ fc1 ðx; tÞ; c2 ðx; tÞ; /; cM ðx; tÞg and chemical free energy fb. One
advantage of such a free energy formulation is that it is convenient
in determining model parameters, especially for a multiphase and
multicomponent system. The unknown model parameters can be
quantitatively determined once the grain boundary properties
including interface thickness, interfacial energy, and interface
symmetry are known [53,54]. Another advantage of such a model is
that the chemical free energy fa ðca Þ of different phases, which can
be obtained from atomistic simulations and phase diagram calcu-
lations, can be directly used as shown in equation (4). Therefore, the
model has potential application in simulating the concurrent evo-
lution of multiphases in a system; for example, the evolution of gas
bubbles, gamma, alpha, gamma prime phases, and grain growth in
UMo alloy fuel.
                                                                                    Fig. 2. Pressure and concentration inside Xe gas bubbles as a function of gas bubble
                                                                                    radius.
3. Thermodynamic and kinetic properties

3.1. Chemical free energies of matrix and gas phases                                has molar-fraction units. As the number of gas bubbles increase, the
                                                                                    internal pressure and concentration quickly decreases. In this work,
   Atomistic simulations show that Xe gas atoms are a substitu-                     we consider the evolution of nano-sized intragranular gas bubbles.
tional defect with formation energy of approximately 5.549 eV                       Equilibrium pressure and Xe concentration inside the nano-sized
[30,32]. The formation energy of U vacancies is about 1.08e1.38 eV                  gas bubbles at T ¼ 400 K are assumed to be 1:2 GPa and 0.6,
[30,32,35]. Stable U interstitials have a dumbbell conﬁguration                     respectively, and the equilibrium concentration of the vacancy in-
along the 〈100〉 and 〈110〉 directions. Their formation energies are                  side the gas bubble is 0.4. The unknown parameters in equation
0.5 eV and 0.55 eV, respectively. The ideal solution model is used to               (11) can be ﬁt using the equation of state and equal chemical po-
describe the excess chemical free energy of the matrix phase (U-                    tentials of matrix and gas phases at equilibrium concentrations.
Mo-Xe alloy) with vacancies and gas atoms. If the contribution of
interstitials is ignored the free energy of matrix phase reads as
                                                                                    3.2. Defect generation and gas bubble nucleation
fa ðcÞ ¼ Evf c2 þ Egf c3 þ kB T½c2 ln c2 þ c3 ln c3 þ ð1  c2  c3 Þlnð1
                                                                                        Defect generation and spatial distribution during displacement
          c2  c3 Þ;   a                                                          cascades in bcc U has been simulated using MD methods [37,38].
      ¼ 1:2; …; N                                                                   Fig. 3(a) shows the spatial distribution of defects due to a 50 keV
                                                                        (10)        primary knocked-on atom (PKA) cascade at 16 ps. It is found a large
                                                                                    vacancy cluster at the cascade center, a high-vacancy concentration
where Evf and Egf are the formation energies of U vacancies and                     zone next to the cascade center, and isolated interstitials away from
substantial Xe in gamma U, respectively; kB is Boltzmann’s con-                     the cascade center. The surviving Frenkel pair population was ﬁt by
                                                                                    NFP ¼ 4:839EPKA0:607 , where E
stant; and T is the absolute temperature.                                                                          PKA is the PKA energy. Experiments and
   The free energy of the gas bubble phase is described by a                        simulations show that the high energy particle cascade may cause
polynomial function as                                                              gas atom resolution from the gas bubbles within the cascade region
                                                                                    in UO2 [62e64]. The high energy PKAs destroy smaller gas bubbles
f0 ðcÞ ¼ A0 c22 þ A1 c2 þ A2 þ B0 c23 þ B1 c3 þ B2                      (11)        completely and bring a quasi-constant number of gas atoms into
                                                                                    resolution when they interact with larger bubbles. In the phase-
where Ai and Bi ði ¼ 0; 1; 2Þ are constants determined by the ther-                 ﬁeld model, different zones as shown in Fig. 3(b) are deﬁned to
modynamic properties of the system. The pressure-volume-                            describe the spatial distribution of defect generation g_ i in equation
temperature (P-V-T) relation of Xe has been studied from experi-                    (9a) and radiation-induced dissolution during a U235 ﬁssion event.
ments [39,41] and MD simulations [42]. For Xe gas bubbles, the                      A spherical vacancy cluster with N0 vacancies and a radius R0 is
modiﬁed equation of state can be described as                                       introduced at the cascade center. Xe atoms are generated at the
                                                                                    cascade center by U235 ﬁssion with a yield Y ¼ 0:25  0:3. The va-
                          
    2g        4pR3                                                                  cancies and Xe atoms diffuse and form a gas bubble nucleus. The
       þp           hs bv NR ¼ NR kB T                                 (12)
     R         3                                                                    region ðR0 < R < R1 Þ is deﬁned as a high-vacancy generation zone
                                                                                    with a generation rate g_ 2 ¼ ðNFP  N0 Þ=Vvac f_, where f_ and VVac are
where g is the interfacial energy of gas bubbles, p the local pressure,             the ﬁssion rate and the volume of the regionðR0 < R < R1 Þ. For
R the radius of the gas bubble, NR the number of gas atoms inside                   radiation-induced resolution, we assumed that the gas atoms in-
the gas bubble, and bv the resolution rate of gas atoms from the gas                side the gas bubbles within the region ðR < R2 Þ were fully or
bubble. The parameter hs can be determined by ﬁtting P-V-T inside                   partially dissolved into the matrix due to the ﬁssion segment
the gas bubble with the equation of state of Xe gas bubbles. Fig. 2                 cascade. If the gas bubble was smaller than a critical size, Rcrit
                                                                                                                                                    resol
                                                                                                                                                          , the
plots the internal pressure and Xe concentration as a function of                   gas bubble is assumed to be completely dissolved while the gas
gas bubble radius (R) for a givenp ¼ 0, g ¼ 0:6N=m2 , T ¼ 400 K, and                bubble be partially dissolved if the gas bubble size is larger than
hs ¼ 0:36. As can be seen, the internal pressure is approximately                   Rcrit
                                                                                     resol
                                                                                           . The parameter c is deﬁned as the fraction of total gas atoms
1:2GPa, and the Xe concentration is approximately 0.6 when the                      inside the gas bubbles that are dissolved. The resolved gas atoms
radii of the gas bubbles are a few nanometers. The Xe concentration                 are uniformly redistributed in a larger region ðR < R3 Þ. The
                                                            S. Hu et al. / Journal of Nuclear Materials 479 (2016) 202e215                                                         207




Fig. 3. (a) spatial distribution of defects due to a 50 keV PKA at 16 ps from MD cascade simulation at 1045 K in U alloys, (b) spatial distribution of defect generation and resolution
used in phase-ﬁeld model.



interstitial is assumed to be uniformly generated in an interstitial                          bubble due to ε*0 ðc3 Þ was approximated as P ¼ Bε*0 ðc3 Þ=3. Using the
generation zone ðR1 < R < R3 Þ. The generation rate, g_ 1 , is calculated                     equation of state of the Xe gas phase (a relationship P ¼ Pðc3 Þ be-
byg_ 1 ¼ NFP =VInt f_, where VInt is the volume of interstitial generation                    tween pressure and Xe concentration) [39,40] results in
zone ðR1 < R < R3 Þ. For given ﬁssion rate, the number of ﬁssion                              ε*0 ðc3 Þ ¼ 3Pðc3 Þ=B. With the stress-free strain ε*ij , the stress and
events during phase-ﬁeld simulation time step is calculated, and                              strain ﬁelds can be obtained by solving the mechanical equilibrium
the ﬁssion events and defects are randomly introduced into the                                equation vsij =vrj ¼ 0 [65].
simulation cell. Since the composition and order parameter ﬁelds
uniquely deﬁne the gas bubble location, the gas bubbles inside the                            3.4. Mobility of Xe, vacancy and interstitials
cascade zone can be identiﬁed, and radiation-induced resolution
can be calculated.                                                                               The effective diffusivity and activation energy of Xe in U alloys
                                                                                              was studied by measuring Xe release during post-irradiation
3.3. Elastic interaction                                                                      annealing [66]. The diffusivity of Xe was deduced to be
                                                                                                                                                            .
   It is expected that elastic interaction plays an important role in                         DXe ¼ 2:242  1011 expð  27000=RTÞ                        m2 s :                 (16)
gas bubble evolution because of the presence of a larger internal
                                                                                                  Xe diffusivity in irradiated U alloys also was described in a
pressure inside gas bubbles, especially for nano-sized gas bubbles.
                                                                                              function of the ﬁssion rate asDXe ¼ D0 f_, which was used in
The elastic interaction energy felas in equation (1) can be calculated
                                                                                              modeling Xe gas bubble swelling in UMo alloys [67]. In this equa-
as
                                                                                              tion, D0 is a constant of proportionality associated with the volume
       1                                                                                    affected by a ﬁssion spike. At T ¼ 400 K, which is around the
felas ¼ lijkl εij  ε*ij εkl  ε*kl                                               (13)        operation temperature of UMo nuclear fuels, the diffusivity calcu-
       2
                                                                                              lated by both models is approximately 1020 ðm2 =sÞ. Molecular
where lijkl is the elastic modulus tensor, εij is the total strain tensor,                    dynamics method was used to study the U self-diffusion in g U and
and ε*ij is the stress-free strain tensor associated with the lattice                         g UMo alloys [36,68] with EAM [35]and MEAM potentials [31]. The
mismatch of defects. If we assume that the variation of a stress-free                         assessment of U self-diffusion data from experiments [28,55] and
lattice parameter a of U alloys with vacancies and substantial Xe                             the atomistic simulations show that the migration barrier of va-
and U interstitials obey Vegard’s law, the local stress-free strain ε*ij is                   cancy and U interstitial are about 0.5 eV and 0.25 eV, respectively.
given by                                                                                      From the extrapolation of the self-diffusion coefﬁcients [36] at low
                                                                                              temperature T ¼ 400 K, the interstitial diffusivity is approximately
         X
         3
                                                                                              1015 ðm2 =sÞ    and     the     vacancy   diffusivity   is   approx-
ε*ij ¼         ε*k ck  ceq dij                                                   (14)
                         k                                                                    imately1020 ðm2 =sÞ. The results show that the diffusivities of va-
         k¼1
                                                                                              cancies and Xe atoms are similar while the interstitial diffusivity is
where ε*k ¼ 1=aðda=dck Þ is the composition expansion coefﬁcient of                           about ﬁve order magnitude larger than that of vacancies. For the
the lattice parameter, dij is the KroneckereDelta function, and ε*k is                        sake of simplicity, we assumed that the vacancy and Xe have the
estimated by the formation volume of defects that can be calculated                           same diffusivity DXe ¼ DVac ∝1020 ðm2 =sÞ in the simulations.
from atomistic simulations. However, inside the gas bubble,                                       The strong anisotropy of SIA diffusivity which is achieved by 1-D
Vegard’s law is no longer valid because of high vacancy and Xe                                and 2-D migration of the SIAs plays an important role in the
concentrations. In the current work, an effective composition                                 microstructure evolution in irradiated materials [8e11,14e18].
expansion coefﬁcient of the lattice parameter, ε*0 ðc3 Þ, inside the gas                      Although the experiments and MD simulations shows that the self-
bubble was deﬁned and the stress-free strain tensor is given as                               diffusivity of U interstitials in bcc UMo is much larger than that of
                                                                                              vacancies there is very limited data of U interstitial mobility
ε*ij ¼ ε*0 ðc3 Þdij h0 ðhÞ                                                        (15)        anisotropy in UMo alloys. It is unknown whether self interstitials
                                                                                              migrate along [111] or [110] directions and how Mo concentration
    The parameter ε*0 ðc3 Þ inside the gas bubble was calculated as                           affects the U interstitial conﬁguration and mobility. The formation
follows. First, the bulk modulus B of gas bubbles was assumed to be                           energies of U interstitials in bcc U single crystals at 0 K have been
the same as that of the matrix phase. The pressure inside the gas                             calculated by density functional theory (DFT) [30]. It is found that
208                                                         S. Hu et al. / Journal of Nuclear Materials 479 (2016) 202e215


the dumbbell conﬁgurations of U interstitials along [100] and [110]                           dumbbell. We can see that the ﬁnal number of [110] U dumbbells
are energetically favored. We studied the effect of Mo on the for-                            becomes thirteen. Analyzing the defect conﬁgurations, we found
mation energy and stable conﬁguration of a U dumbbell in U10 wt%                              that during the structure relaxation seven of ten initial [110] U
Mo alloy by using DFT. VASP [69,70] software is used to solve the                             dumbbell remains in the [110] dumbbell conﬁguration; three of ten
Kohn-Sham equations with plane-wave basis sets. Projector-                                    initial [110] U dumbbells transfer to [210] U dumbbells; two of ten
augmented-wave (PAW) [70,71] pseudo-potentials for U and Mo                                   initial [100] U dumbbells transfer to [110] U dumbbells; and four of
are taken from VASP’s library, in which the number of valence                                 ten initial [111] U dumbbells transfer to [110] U dumbbells. There
electrons is 14 and 6, respectively. Perdew-Burke-Ernzerhof (PBE)                             are only four of ten initial [100] U dumbbells remaining in the [100]
functionals [72] are employed for the electronic exchange-                                    dumbbell conﬁguration, and three of ten initial [111] U dumbbells
correlation energies. The plane-wave cutoff energy is taken to be                             remaining in the [111] U dumbbells. Some initial U [100] and [111]
253 eV. A Monkhorst-Pack [73] k-point grid of 4  4  4 is                                    dumbbells transfer to U [210], [311], [211], and [310] which depends
employed to sample the Brillouin zone. The stability of dumbbells                             on the local Mo distribution. The results in Fig. 4, also show that U-
are explored using a cubic simulation box of 4  4  4 supercell of                           U [110] dumbbell has the lowest formation energy, that is 0.204 eV.
the bcc unit cell. A random U-Mo alloy of ~20 at.% Mo is generated                                The DFT results clearly indicate that U-U[110] dumbbell is the
using the Monte Carlo special quasi-random structure (mcsqs)                                  most stable dumbbell conﬁguration in UMo alloys. In addition, the
technique [74] as implemented in the ATAT code [75]. A perfect                                instantaneous relaxation from several [111] and [100] initially ori-
(without defect) cell consists of 102 U and 26 Mo atoms. Subse-                               ented dumbbells to [110] dumbbells means that such rotation has
quently, 8 U sites and 2 Mo sites are selected. A dumbbell is con-                            no barrier. However, we cannot generalize that all rotations from
structed at one of these sites by adding a U interstitial atom, i.e. 8                        [111] and [100] to [110] are barrier-less. This is because in U-Mo
systems each with one U-U dumbbells and 2 systems each with one                               there exists lattice distortion, atoms are slightly displaced from a
Mo-U dumbbell. We explored [100], [110], and [111] dumbbell                                   perfect bcc lattice sites. It means that some other [111] and [100]
orientations for a total of 30 systems. The structures are then                               initially oriented dumbbells that remain in that orientation are
relaxed such that the coordinates of all atoms and the box volume                             stable not because of the symmetry constraint, but because of the
are optimized while maintaining cubic symmetry. The relaxation is                             local minimum in the potential energy landscape. In addition, as
stopped when the norm of the force on each atom is < 0.025 eV/Å                               can be seen from Fig. 4, dumbbells can stabilize in various other
and the external pressure acting on the box is < 0.5 kbar. At the end                         orientations such as [210], [310], [211], and [311]. Therefore it is
of the relaxations, a static calculation is performed to eliminate                            difﬁcult to obtain a deﬁnite picture of the migration pathways of
errors due to plane-wave basis incompleteness associated with                                 interstitial U in UMo without performing a dynamic simulation of
volume changes. The formation energy (Ef,db) of a dumbbell in this                            diffusion. At this moment, such simulation cannot be done within
alloy is calculated using                                                                     DFT framework.
                                                                                                  Since the pure bcc U is unstable at 0 K the DFT calculations of U
Ef $db ¼ Et;db  Et;alloy  Ecoh;bccU                                              (17)       migration energy has to be carried out in bcc UMo alloys, which
                                                                                              makes the DFT calculation difﬁcult as described above. Neverthe-
where Et,db is the total energy of the alloy with a dumbbell, Et,alloy is                     less, in the future we plan to perform DFT calculation to estimate
the total energy of the perfect alloy, Ecoh,bccU is the energy per atom                       the migration barrier for the 1D diffusion of [110] dumbbell along
of bcc U.                                                                                     [110] as well as the rotation barrier among different orientations.
   In the simulations, we ﬁnd that some initially generated U                                 But in the current work, we assumed that the large U interstitial
dumbbells are unstable. They will transfer to more stable defect                              diffusivity is attributed to the one-dimensional migration of 〈110〉 U
conﬁguration. Fig. 4 summaries the defects identiﬁed in the relaxed                           dumbbell along the [110] direction, and the effect of one-
system and their formation energy. We have ten initial U dumbbells                            dimensional migration of interstitials on gas bubble superlattice
along each [100], [110] and [111] directions for a total of 30                                formation was studied.

                                                                                              4. Parameters of phase-ﬁeld modeling

                                                                                                  The phase-ﬁeld model developed was a generic model that
                                                                                              considered gas bubble evolution under irradiation in three-
                                                                                              dimensional polycrystalline materials. The parameters used in
                                                                                              phase-ﬁeld simulations are listed in Table 1.
                                                                                                  Evolution equations (9a and b) together with the interstitial
                                                                                              evolution equation (8) and mechanical equilibrium equation were
                                                                                              numerically solved by a semi-implicit Fourier-spectral method [76].
                                                                                              In the current work, we have focused on investigating the effect of
                                                                                              thermodynamic properties and irradiation conditions on intra-
                                                                                              granular gas bubble evolution and exploring the formation mech-
                                                                                              anism of an intragranular gas bubble superlattice. The
                                                                                              microstructure of intragranular gas bubbles in a single crystal un-
                                                                                              der irradiation is described by three concentrationðc1 ; c2 ; c3 Þ and
                                                                                              two order parameter ðh0 ; h1 Þ ﬁelds. For inter- and intra-granular
                                                                                              gas bubbles in polycrystalline structures, we need to use more or-
                                                                                              der parameter ﬁelds ðh0 ; h1 ; ::::; hN Þ. All the model parameters are
                                                                                              same as that listed in Table 1. Because intragranular gas bubbles are
                                                                                              approximately a few nanometers in diameter, a very small grid size,
Fig. 4. DFT formation energy of U interstitial defect in various ﬁnal dumbbell conﬁg-
urations in U-Mo random alloys (~20 at.% Mo). The data are collected from 30 con-
                                                                                              dx ¼ 5:2  1010 m, was used in the simulations to capture the
ﬁgurations in which initially there are 10 conﬁgurations for each [100], [110], and [111]     morphology of nano-sized gas bubbles. We performed intra-
orientation.                                                                                  granular gas bubble evolution in a three-dimensional simulation
                                               S. Hu et al. / Journal of Nuclear Materials 479 (2016) 202e215                                              209

Table 1
Parameters used in the simulations.

 Characteristic length                                      l0                                                          0:52 nm
 Grid size                                                  dx ¼ dy ¼ dz                                                0:52 nm
 Temperature                                                T                                                           400 K
 Diffusivity of Xe and vacancy                              DXe ¼ DVac                                                  2:0  1020 m2 =s
 Mobility                                                   Mii ¼ DXe =ðkB TÞ; i ¼ 2; 3                                 1:8
                                                            Mij ¼ 0:0; isj
 Mobility of interstitial                                   DInt ¼ D* DXe                                               D* ¼ 10; 103 ; 104 ; 105 ; 106
 Interfacial energy of gas bubble                           g                                                           0:6 J=m2
 Grain boundary energy                                      gGB                                                         1:0 J=m2
 Gradient coefﬁcient                                        k0 =ðkB Tl20 Þ                                              0:04
 Gradient coefﬁcient                                        ka =ðkB Tl20 Þ; a ¼ 1; 2; …; N                              0:04
 Coefﬁcient                                                 m0 =ðkB TÞ                                                  0:067
 Coefﬁcient                                                 ma =ðkB TÞ; a ¼ 1; 2; …; N                                  0:067
 Coefﬁcient                                                 g0;a =ðkB TÞ; a ¼ 1; 2; …; N                                0:15
 Coefﬁcient                                                  ga;b =ðkB TÞ;                                              0:25
                                                             a; b ¼ 1; 2; …; N; asb
                                                                                                                         P a*
 Free energy function                                       fa =ðkB TÞ; a ¼ 0; 1; 2; …; N                                               a
                                                                                                                              Ai ðci  ci eq Þ2
                                                                                                                        i¼2;3
 Elastic energy                                             felas =ðkB TNV Þ                                            1l* ðε  ε* Þðε  ε* Þ
                                                                                                                        2 ijkl ij    ij   ij    ij
 Coefﬁcient                                                 Aia*                                                         A1*             1*
                                                                                                                          1 ¼ 159:4; A2 ¼ 53:1;
                                                                                                                         A2*
                                                                                                                          1  ¼ 0:3; A 2*
                                                                                                                                      2  ¼  0:1
 Equilibrium concentration                                    a                                                           1
                                                            ci eq                                                        c2eq ¼ 6:0  107 ;
                                                                                                                          1
                                                                                                                         c3eq ¼ 4:0  107 ;
                                                                                                                          2           2
                                                                                                                        c2eq ¼ 0:6; c3eq ¼ 0:4
 Interface mobility                                         La l20 =DXe                                                 50
 Elastic constant                                           Cij* ¼ Cij =ðkB TNV Þ;                                        *
                                                                                                                         C11 ¼ 1504:28
                                                                                                                          *
                                                            NV ¼ 4:75  1028 atom=m3                                     C12 ¼ 271:88 [32]
                                                                                                                          *
                                                                                                                         C44 ¼ 244:35
 Stress free strain                                         ε*ij                                                         εXe*
                                                                                                                          ii   ¼ 0:05; εVac*
                                                                                                                                        ii   ¼ 0:005
                                                                                                                         εInt*
                                                                                                                          ii   ¼ 0:0
 Time                                                       DXe t=l20                                                   1:5  103
 Fission rate                                               f_                                                           1:34  1021 ; 2:68  1021 ;
                                                                                                                         4:02  1021 ; 6:03  1021
                                                                                                                         fission=ðm3 sÞ
 Reaction rate                                              g_ i ¼ g12 DSIA c1 c2                                       g12 ¼ 1:4  1019 =m2
                                                            i ¼ 1; 2
 Fission Yield                                              Y                                                           0:25
 Saturated Xe concentration                                 csat   sat
                                                             2 ¼ cXe
                                                                                                                        0:108; 0:098; 0:088
                                                                                                                        0:078
 Applied strain                                             εappl:                                                      0:015; 0:0075
                                                             ii
                                                                                                                        0:0075; 0:015
 Radiation zones                                            R*i ¼ Ri =l0                                                R*0 ¼ 1:0; R*10 ¼ 8:0;
                                                                                                                        R*1 ¼ 3:0; R*2 ¼ 9:6;
                                                                                                                        R*3 ¼ 12:0
 Defect generation per ﬁssion                               NFP                                                         50 in 3D
                                                                                                                                 [38]
                                                                                                                        5 in 2D
 Vacancy cluster                                            N0                                                          2
 Resolution rate                                            c                                                           0:2
 Critical radius of resolution                              Rcrit                                                       0:5 nm
                                                             resol
 Formation energy of defects                                Eif                                                          f
                                                                                                                        EVac ¼ 1:08  2:6 eV[36]
                                                                                                                         f                  f
                                                                                                                        EInt ¼ 0:3  1:5 eVEXe ¼ 5:549 eV[29]




cell and intergranular gas bubble evolution in a bicrystal with a                   a three-dimensional simulation cell because the gas bubble is a
parallel code and 24 processors. However, to achieve a speciﬁed                     cylinder in two dimensions while it is a sphere in three dimensions.
ﬁssion density, large computer resources are needed to simulate                     The ratio between the two-dimensional and three-dimensional
gas bubble evolution in a three-dimensional representative vol-                     volume fraction ðV2D =V3D Þ can be calculated by3a=ð4RÞ, where a
ume. More efﬁcient and scalable numerical methods are required to                   is the superlattice constant and R is the gas bubble radius. If
perform large scale three-dimensional (3D) simulations. Therefore,                  a ¼ 8nm andR ¼ 1nm, then V2D =V3D ¼ 6. Considering this fact, high
in the current work, the simulations of gas bubble evolution were                   ﬁssion rates and ﬁssion densities were used in the two-dimensional
performed in a two-dimensional, 256dx  256dx simulation cell.                      simulations. In addition, we believe that the intragranular gas
The model can be implemented in Idaho National Laboratory’s                         bubbles quickly reach a quasi-static state in which the average gas
MARMOT and BISON fuel performance code [77,78], which has                           bubble size and overall gas storage inside grains remains constant.
efﬁcient scalable numerical methods, for large scale gas bubble                     In the current work, a saturated Xe concentration, csatXe , to present
microstructure evolution simulations in 3D and polycrystalline                      the quasi-static state has been introduced, where csat
                                                                                                                                         Xe is deﬁned as
materials.                                                                          the average Xe concentration inside the grain that includes Xe
    For a given gas bubble superlattice constant, the volume fraction               atoms in the matrix as well as inside the gas bubbles. The saturated
of gas bubbles in a two-dimensional cell is much higher than that in                Xe concentration could be estimated from the gas bubble structure
210                                                     S. Hu et al. / Journal of Nuclear Materials 479 (2016) 202e215


observed in experiments. For a fcc gas bubble superlattice with a                          vacancies and interstitials, and elastic interaction are the same in
lattice constant 10 nm, gas bubble radius 1 nm, and Xe concen-                             the following simulations, except when speciﬁcally noted.
tration 0.6 inside the gas bubbles, the overall Xe concentration is
can be calculated which is about 0.05. Considering the difference                          5.1. Effect of interstitial mobility on gas bubble structure
between two and three-dimensions discussed in section, we set up
the saturated Xe concentration to be around 0.098 in the simula-                               For a given Xe and vacancy diffusivity, gas bubble evolution was
tions. The parameter csatXe may depend on the grain size and ﬁssion                        systematically simulated by varying the mobility of one-
rate. For example, csat
                    Xe  in coarser grains should be larger than that in                    dimensional migration of interstitials. The ﬁssion rate
ﬁner grains. In the current work, we studied the effect ofcsat
                                                             Xe , elastic                  f_ ¼ 2:68  1021 fission=ðm 3 sÞ was used. The saturated Xe concen-
interaction, ﬁssion rate, and interstitial mobility anisotropy on gas                      tration was set to becsat
                                                                                                                   Xe ¼ 0:098, and the ratio of interstitial and Xe
bubble structure evolution.                                                                diffusivity D* ¼ DInt =DXe varied from 10 to 106. Fig. 5 presents the
                                                                                           gas bubble microstructure at time t ¼ 114.6days. The color bar
5. Simulation results                                                                      denotes the Xe concentration. It can be clearly seen that when
                                                                                           D* ¼ DInt =DXe < 104 , the spatial distribution of gas bubbles is
    The ordering of bubbles has been observed to develop subse-                            random as shown in Fig. 5(a).
quent to an initial random distribution of bubbles in the matrix                               When the interstitial diffusivity is about four orders of magni-
[11]. In our simulations, gas bubbles with an average density of                           tude larger than that of Xe diffusivity, short-range ordering of gas
4:4  1016 =m2 and average radius of R:0     g ¼ 2l0 were randomly                         bubbles is observed in the regions marked by the white lines in
introduced into the simulation 256l0  256l0 cell. The gas and va-                         Fig. 5(b). As interstitial diffusivity increases, long-range gas bubble
cancy concentrations inside the gas bubbles were set to the equi-                          ordering takes place as shown in Fig. 5(c and d). It should be
librium concentration 0.6 and 0.4, respectively. The initial                               pointed out that the elastic interaction was taken into account in
concentrations of Xe atoms, vacancies and interstitials in the matrix                      the simulations. The gas bubble microstructure in Fig. 5(a) dem-
are input parameters in the simulations. The thermal equilibrium                           onstrates that the elastic interaction does not cause the formation
concentrations of these defects are very low which can be esti-                            of the gas bubble superlattice. Therefore, we can conclude that the
mated from the formation energy Ef the defect. The formation                               fast one-dimensional migration of interstitials is the primary
energies of U vacancy and interstitial in bcc U are about 1.0 eV and                       mechanism for gas bubble superlattice formation. Fig. 6 presents
0.5 eV [30], respectively. Their thermal equilibrium concentrations                        the gas bubble temporal evolution for the case D* ¼ 106 . Checking
can be estimated by expðEf =kB TÞ. It is about 2:5  1013 and 5:0                       the gas bubble evolution inside region A marked by the dashed-line
107 at 400 K, respectively. However, the defect concentration in                          circle, we ﬁnd that gas bubble ordering takes place through
radiated material should be much larger than its’ solubility/or                            continuous gas bubble nucleation, resolution, migration, and
thermal equilibrium concentration. A rate theory model [79] shows                          growth processes. It is clear that ordering of gas bubbles ﬁrst occurs
that the radiation-induced equilibrium concentration dominates                             in some small regions, and then the ordered regions grow and
completely over the thermal one at temperatures below 0:5Tm,                               merge with one another to form the superlattice. The gas bubbles
where Tm is the melting temperature. In Ni under electron radiation                        inside ordered regions are relatively stable compared to those in-
with 1 MeV energy and 1:0  1019 e=cm2 ﬂux, the predicted steady                           side disordered regions. Continuous attachment of gas bubbles in
state vacancy concentration is larger than1:0  105 while the                             disordered regions to ordered regions causes growth of the ordered
thermal equilibrium concentration is about 1:0  1013 at0:3Tm .                           region. All gas bubbles in small ordered regions have the same
Since there is no data of defect concentrations at steady state in                         structure and orientation, but they may shift among one another by
irradiated UMo alloys, we assumed that the concentrations of Xe,                           some distance. When they merge, a dislocation of gas bubbles in-
vacancies, and interstitials in the matrix be 1.0  105. For a given                      side the superlattice may form, which is marked by “⊥” in Fig. 6(c
ﬁssion rate, f_, and saturated Xe concentration, csat
                                                    Xe , the simulation                    and d). Such dislocations also are observed in TEM images of gas
randomly introduced ﬁssion events and generated vacancies, in-                             bubble superlattices [2,4,6,80]. Therefore, we conclude that for-
terstitials, and Xe atoms according to their generation rates and the                      mation of gas bubble superlattices occurs through a nucleation and
spatial proﬁle of defect distribution described in the previous sec-                       growth process.
tion. After the overall Xe concentration reaches csat    Xe , the ﬁssion                       A comparison of gas bubble superlattices from experiments and
event will only generate vacancies and interstitials and turn off the                      simulations are presented in Fig. 7. Experiments show that the gas
Xe generation to maintain the saturated Xe concentration in the                            bubble superlattice has a fcc structure. From the TEM images in
simulation cell. The initial conditions, heterogeneous nucleation of                       Fig. 7(b), the lattice constant of the superlattice is approximately
gas bubbles, radiation-induced resolution, reaction between                                11.44 nm, and the average gas bubble size in diameter is




                       Fig. 5. Effect of interstitial diffusivity on gas bubble microstructures. (a) D* ¼ 10, (b) D* ¼ 104 , (c) D* ¼ 105 , (d) D* ¼ 106 .
                                                            S. Hu et al. / Journal of Nuclear Materials 479 (2016) 202e215                                                        211




                      Fig. 6. Temporal evolution of gas bubbles for the caseD* ¼ 106 . (a) t ¼ 64.2 days, (b) t ¼ 81.0days, (c) t ¼ 97.8days, (d) t ¼ 114.6days.




Fig. 7. (a) Superlattice of ﬁssion gas bubbles oriented at zone [001] simulated with D* ¼ 106 at t ¼ 114.6days (3:98  2028 fission=m3 ) and (b) TEM images showing the superlattice
of ﬁssion gas bubble observed in a U-7Mo particle with oriented at zone [011] and [001] (ﬁssion density 3:2  2027 fission=m3 and average ﬁssion rate2:7  2020 fission=m3 s, and peak
temperature T ¼ 109 C). The spaces of plane “A”, “B” “C” are 5:75nm; 6:55nm; and 5:72nm; respectively, and the average gas bubble diameter is approximately 3.5 nm [80].




                                            Fig. 8. The evolution of gas bubble size distributions (a) for D* ¼ 10 and (b) for D* ¼ 106.
212                                                         S. Hu et al. / Journal of Nuclear Materials 479 (2016) 202e215


approximately 3.5 nm. Fig. 7(a) shows the gas bubble superlattice                              form superlattices for all ﬁssion rates considered in this work,
predicted from the simulation. It can be seen that gas bubbles                                 which implies that superlattice formation is controlled by the fast
uniformly align along 〈110〉 directions. The unit cell of the super-                            one-dimensional migration of interstitials (D* ¼ 106 ), not the
lattice in two dimensions consists of three sites; that is, (0.0 0.0                           ﬁssion rate. However, by analyzing the evolution of gas bubbles and
0.0), (0.5 0.5 0.0), (0.5 0.5 0.0). Extending this lattice to three di-                       superlattice structure, we found that the ﬁssion rate affects the
mensions yields a fcc lattice. The predicted superlattice shown in                             superlattice formation kinetics and the superlattice constant as
Fig. 7(a) is a fcc structure and the same orientation as that in the                           well as the saturated Xe concentration. A higher ﬁssion rate causes
TEM image with oriented zone [001] if we remove the second {001}                               more rapid Xe accumulation, resulting in superlattice formation
[43] gas bubble layer. Therefore, simulations conﬁrm that gas                                  earlier compared to a lower ﬁssion rate. The white square in Fig. 9,
bubbles form a fcc gas bubble superlattice if U interstitials migrate                          which covers the 3  3 perfect superlattice shown in Fig. 9(a),
in one dimension along 〈110〉 directions in the bcc UMo matrix. The                             shows some representative superlattices under different ﬁssion
lattice constant of the superlattice is about 8.9 nm as shown in                               rates. The results demonstrate that the superlattice constant de-
Fig. 7(a). The lattice constant of the superlattice in two-dimensional                         creases from 9.5 nm to 8.32 nm when the ﬁssion rate increases from
simulations could be different from that in a real three-dimensional                           1.34  1021 to 6.03  1021 (ﬁssion/m3s). The reason, why the
system due to different Xe concentrations. However, the simulation                             superlattice constant decreases as the ﬁssion rate increases, could
result is in reasonable agreement with the experimental result (i.e.,                          be that a higher ﬁssion rate causes more gas bubble nucleation sites
11.44 nm).                                                                                     and a higher gas bubble nucleation rate due to the higher resolution
    Fig. 8 shows the evolution of gas bubble size distributions for                            of gas atoms from existing gas bubbles and a higher Xe generation
two extreme cases, D* ¼ 10 andD* ¼ 106 . These two cases have                                  rate. We also observed that the volume fraction of superlattice re-
similar initial gas bubble size distribution. From the size distribu-                          gion decreases with the increase of ﬁssion rates for a given satu-
tion evolution, we can see that, for both cases, the smallest sized                            rated Xe concentration. For the ﬁssion rate 1.34  1021 shown in
gas bubbles are the same. These small bubbles are the gas bubble                               Fig. 9(a), the gas bubble structure is close to a perfect superlattice
nuclei continuously formed by radiation-induced resolution and                                 when the saturated Xe concentration reaches 0.098. Simulations
nucleation. For the case with large interstitial diffusivity, the largest                      with higher saturated Xe concentrations demonstrated that a per-
gas bubble size increased slightly as the ﬁssion density increased.                            fect gas bubble superlattice forms under the ﬁssion rate 6.03  1021
No gas bubble coarsening was observed. The radiation-induced
resolution and shrinkage induced by the reaction between inter-
stitial and gas bubbles result in a narrow size distribution. Finally,
for the case with small interstitial diffusivity, gas bubble coarsening
does take place and causes a decrease in the gas bubble number and
a continuous increase in the radius of the largest gas bubble. The
simulations demonstrate that the uniform and small intragranular
gas bubbles observed in UMo are attributed to not only radiation-
induced resolution, but also to the reaction between fast one-
dimensional migration of interstitials and gas bubbles.


5.2. Effect of ﬁssion rates on gas bubble structures

   We used four ﬁssion rates,f_ ¼ 1:34  1021 ; 2:68  1021 ;
4:02  1021 ; and 6:03  1021 ðfission=m3 sÞ, to examine the effect
on gas bubble superlattice formation. In the simulations, the
interstitial diffusivity was set as D* ¼ 106 . The initial overall Xe
concentration was 0.078, and the saturated Xe concentration is
assumed to be 0.098. The remaining parameters were the same as
those used in Section 5.1. At different ﬁssion rates, the system will
take different times to reach the saturated Xe concentration. The
gas bubble microstructures at time t ¼ 54days, which is calculated                             Fig. 10. Evolution of total gas bubble number for different ﬁssion rates. The time in the
from the initial state, are shown in Fig. 9. We found that gas bubbles                         horizontal axis is taken into account from the initial state with Xe concentration 0.078.




Fig. 9. The effect of ﬁssion rates on the formation of gas bubble superlattices. (a) 1:34  1021 ðfission=m3 sÞ, (b) 2:68  1021 ðfission=m3 sÞ, (c) 4:02  1021 ðfission=m3 sÞ, and (d)
6:03  1021 ðfission=m3 sÞ.
                                                              S. Hu et al. / Journal of Nuclear Materials 479 (2016) 202e215                                                        213


                                                                                                bubble superlattice obtained in phase-ﬁeld simulations. The results
                                                                                                discussed in Section 5.1 demonstrate that the elastic interaction
                                                                                                among gas bubbles and substantial diffusive Xe, U vacancies, and U
                                                                                                interstitials do not play an important role in the formation of gas
                                                                                                bubble superlattices. However, metallic nuclear fuel or fuel parti-
                                                                                                cles are embedded in metal cladding materials. Fuel swelling may
                                                                                                cause a large stress ﬁeld. Evidence of large creep deformation
                                                                                                caused by fuel swelling has been observed in monolithic UMo fuels
                                                                                                [81]. In addition, the heterogeneous Mo distribution inside the
                                                                                                grain also may generate a stress ﬁeld. In this section, the effect of
                                                                                                applied stresses associated with the deformation of matrix on gas
                                                                                                bubble evolution is examined. Four different strains,
                                                                                                 appl:                                                          appl
                                                                                                εii    ¼ 0:015 0:0075 0:0075 and 0:015 ði ¼ 1; 2Þ; and ε33 ¼ 0,
                                                                                                are applied to the simulation cell, which mimics the constraint of
                                                                                                fuel cladding. In the simulations, the interstitial diffusivity is set to
                                                                                                be D* ¼ 106 . The initial overall Xe concentration is 0.078, and the
                                                                                                saturated Xe concentration is assumed to be 0.098. The ﬁssion rate
                                                                                                is set at 4.02  1021 (ﬁssion/m3s). The remaining parameters are the
                                                                                                same as those discussed in Section 5.1. Fig. 12 shows the gas bubble
                                                                                                structures. It can be seen that the gas bubble superlattice forms
Fig. 11. Distribution of pressurep ¼ ðsxx þ syy þ szz Þ in unitC44 . The pressure inside the    under both tensile and compressive applied strain, and the volume
gas bubble is about 1 GPa.                                                                      fraction of gas bubble superlattice in four different applied strains
                                                                                                are very similar. Therefore, we conclude that the applied strain does
                                                                                                not affect the formation of the gas bubble superlattice. However,
(ﬁssion/m3s) when the saturated Xe concentration reaches 0.12.
                                                                                                analyzing the superlattice evolution, we ﬁnd that the applied strain
This implies that the saturated Xe concentration for the formation
                                                                                                does affect the superlattice structure as well as the formation ki-
of gas bubble superlattices increases as the ﬁssion rate increases.
                                                                                                netics. A compressive stress (i.e., a negative applied strain) results
Fig. 10 plots the temporal evolution of total number of gas bubbles
                                                                                                in the reduction of average gas bubble size and the superlattice
inside the simulation cell. Because a higher ﬁssion rate causes
                                                                                                constant. In contrast, the average gas bubble size and lattice con-
higher resolution and nucleation rates, as expected, we found that
                                                                                                stant of the superlattice increase as the tensile stress increases. We
the total gas bubble number (or gas bubble density) increases as the
                                                                                                also found that the applied stress affects the kinetics of the
ﬁssion rate increases. For the lower ﬁssion rate case of 1.34  1021
                                                                                                superlattice. A compressive stress accelerates the formation of
(ﬁssion/m3s), the gas bubble density almost reaches the ideal value
                                                                                                superlattice while a tensile stress delays the formation of
(392) of a perfect superlattice with a lattice constant of 9.5 nm. This
                                                                                                superlattice.
also is conﬁrmed by the perfect superlattice shown in Fig. 9(a). For
the higher ﬁssion rate 6.03  1021 (ﬁssion/m3s), the average gas
bubble density is close to the ideal value (578) of a perfect super-                            5.4. Effect of gas saturation on gas bubble structures
lattice with a lattice constant of 8.2 nm. However, many small gas
bubbles with a low gas concentration are present, which is asso-                                     The simulations in previous sections assumed that the saturated
ciated with irradiation-induced nucleation. The average gas bubble                              Xe concentration was constant at 0.098. However, the saturation
size in the disordering region is much smaller than that in the                                 concentration may depend on the grain size and ﬁssion rate. For
ordering region, which means that a high saturated Xe concentra-                                ﬁne grains, the defects including vacancy, Xe, and interstitials have
tion is required to form the perfect superlattice.                                              short diffusion paths to grain boundaries. The saturated Xe con-
                                                                                                centration in ﬁne grains will be lower than that in coarse grains. In
5.3. Effect of applied stresses on gas bubble structures                                        this section, we investigate the effect of saturated Xe concentration
                                                                                                on gas bubble superlattice formation. Four different concentrations,
   As described previously, a high pressure is present inside nano-                             csat
                                                                                                 Xe ¼ 0:078; 0:088; 0:098 and 0:108, are used to examine the effect
sized gas bubbles. Fig. 11 presents the pressure distribution in a gas                          of Xe saturated concentration on gas bubble evolution. In the




Fig. 12. The effect of applied strain on gas bubble structure. (a)εappl
                                                                   ii
                                                                        ¼ 0:015, (b) εappl
                                                                                       ii
                                                                                            ¼ 0:0075, (c) εappl
                                                                                                            ii
                                                                                                                 ¼ 0:0075, (d) εappl
                                                                                                                                ii
                                                                                                                                     ¼ 0:015. The lattice constant is about 8:36nm under
εappl
 ii
      ¼ 0:015. The  lattice constant is about 9:5nm  under εappl
                                                             ii
                                                                  ¼   0:015.
214                                                    S. Hu et al. / Journal of Nuclear Materials 479 (2016) 202e215




              Fig. 13. The effect of Xe saturated concentrations on gas bubble structure. (a)csat             sat              sat                  sat
                                                                                              Xe ¼ 0:108, (b)cXe ¼ 0:098, (c) cXe ¼ 0:088, and (d) cXe ¼ 0:078.




simulations the interstitial diffusivity is set to be D* ¼ 106 . The                     constant observed in the experiments. The reason is that in 2D the
initial overall Xe concentration is 0.078. The ﬁssion rate is set to be                  gas bubble actually has cylindrical morphology. However, in 3D the
4.02  1021 (ﬁssion/m3s). The remaining parameters are the same                          gas bubbles are isolated spheres. If the gas bubble radius, the
as those discussed in Section 5.1. For a smaller saturated Xe con-                       concentration of Xe inside the gas bubbles, and superlattice con-
centration, the system will reach the saturated state at an earlier                      stant in 2D and 3D are the same, we know that more Xe and va-
time. The gas bubble structures at time t ¼ 114.6days are presented                      cancies are needed to form the cylindrical gas bubble in 2D than the
in Fig. 13. We found that the volume fraction of the superlattice                        isolated spherical gas bubbles in 3D. In addition, the stress ﬁeld
decreases with the decrease of Xe saturated concentration from                           around the gas bubbles in two dimensions is different from those in
Figure 13(a) to Figure 13(d). For the case csat  Xe ¼ 0:078, the gas                     three dimensions. These differences may affect gas bubble evolu-
bubbles have a random distribution in space and no ordering oc-                          tion kinetics, but do not necessarily affect the mechanism of
curs. Therefore, a critical Xe concentration, which is larger than                       superlattice formation and trends of gas bubble evolution predicted
0.078, is required to form the superlattice. The result implies that                     in the simulations. Regarding fcc gas bubble superlattice, it is hard
the superlattice can only form in sufﬁciently coarse grains where                        to tell FCC and BCC structure in two dimensions. However, our
the Xe concentration may be larger than the critical value.                              simulation demonstrates that if U interstitial fast migrates along
Analyzing the gas bubble microstructure evolution, it is interesting                     〈110〉 directions it will cause gas bubbles uniformly align along
to ﬁnd that no coarsening occurs in disordered regions although                          〈110〉 directions. We can image that if gas bubbles uniformly align
the gas bubble density is high, and the average size of gas bubbles                      along 〈110〉 directions in three dimensions the gas bubbles have a
in superlattice regions are larger than those in disordered regions.                     fcc superlattice structure. Therefore, our simulations indirectly
                                                                                         demonstrate that U interstitial fast migration along 〈110〉 directions
6. Conclusions and discussion                                                            results in the formation of fcc gas bubble superlattice in bcc UMo
                                                                                         alloys. To verify the conclusion, we have to perform three dimen-
    In this work, a phase-ﬁeld model of gas bubble evolution in                          sional (3D) simulations which require an efﬁcient and scalable
irradiated U metallic fuels was developed for the ﬁrst time. The                         numerical method to solve the phase-ﬁeld equations. We examined
model enables the investigation of interstitial one-dimensional                          the formation energies of 30 dumbbell conﬁgurations in U-Mo
migration, elastic interactions among gas bubbles, defects and                           random alloys (20 at%Mo) using DFT. The results clearly indicate
cladding constraints, and radiation conditions on gas bubble evo-                        that U-U [110] dumbbell is the most stable dumbbell conﬁguration.
lution and superlattice formation kinetics. The simulation reveals                       The instantaneous relaxation from several [111] and [110] initially
that the elastic interaction doesn’t cause the gas bubble alignment                      oriented dumbbells to [110] dumbbells means that such rotation
while the fast one-dimensional interstitial migration along 〈110〉                        has no barrier. However, it is difﬁcult to obtain a quantitative pic-
directions in a bcc U matrix results in gas bubble alignment along                       ture of the migration pathways of interstitials U in UMo without
〈110〉 directions. The gas bubble alignment along 〈110〉 implies the                       performing a dynamic simulation of diffusion. A quantitative
formation of fcc gas bubble superlattice which is observed in bc                         phase-ﬁeld simulation relies on accurate thermodynamic and ki-
UMO alloys. The simulations also show that 1) the superlattice                           netic properties of the system. Because of the lack of the thermo-
constant decreases with the increase of ﬁssion rate and compres-                         dynamic properties of UMo alloys, the simulations used in this
sive stress; 2) a critical Xe concentration is required to form the                      work employed a number of assumptions, including the interstitial
superlattice, implying that a critical grain size exists for the for-                    diffusivity, the equation of state of gas bubbles, interfacial energy,
mation of gas bubble superlattice; and 3) no coarsening of gas                           and lattice mismatch of defects. These properties could be esti-
bubbles in disordered regions occurs as a result of radiation-                           mated using atomistic simulations. The simulations show that the
induced resolution and nucleation. The gas bubbles in disordered                         saturated Xe concentration will importantly affect the superlattice
regions have much larger mobility than those in ordered regions or                       formation. To study the effect of grain size on the saturated Xe
the superlattice. The simulation results demonstrate the predictive                      concentration, the simulations need to consider the concurrent
capability of the phase-ﬁeld model developed. However, a semi-                           evolution of intergranular and intragranular gas bubbles. Therefore,
implicit Fourier-spectral method used in the current simulations,                        improvements to both numerical methods and thermodynamic
which is accurate and efﬁcient for a small simulation cell, is not an                    models are needed for quantitative simulations.
efﬁcient and scalable numerical method and limits performing
large scale simulations. Therefore, all simulations in the current                       Acknowledgements
work were performed in two dimensions. In two-dimensional (2D)
simulations, much larger overall defect concentrations and ﬁssion                          The work described in this article was performed by Paciﬁc
rates are required to reproduce a gas bubble size and superlattice                       Northwest National Laboratory, which is operated by Battelle for
                                                           S. Hu et al. / Journal of Nuclear Materials 479 (2016) 202e215                                                        215


the U.S. Department of Energy (DOE) under Contract DE-AC05-                                  [37] X.F. Tian, H.X. Xiao, R. Tang, C.H. Lu, Nucl. Instrum. Methods B 321 (2014)
                                                                                                  24e29.
76RL01830. This study was supported by DOE’s National Nuclear
                                                                                             [38] Y.B. Miao, B. Beeler, C. Deo, M.I. Baskes, M.A. Okuniewski, J.F. Stubbins, J. Nucl.
Security Administration, Ofﬁce of Material Management and                                         Mater. 456 (2015) 1e6.
Minimization Reactor Conversion Program. The authors also thank                              [39] C. Ronchi, J. Nucl. Mater. 96 (1981) 314e328.
the EMSL computer support.                                                                   [40] J.Y. Oh, Y.H. Koo, J.S. Cheon, B.H. Lee, D.S. Sohn, J. Nucl. Mater. 372 (2008)
                                                                                                  89e93.
                                                                                             [41] J.W. Harrison, J. Nucl. Mater. 31 (1969), 99-&.
References                                                                                   [42] H.X. Xiao, C.S. Long, Chin. Phys. B 23 (2014).
                                                                                             [43] S.Y. Hu, C.H. Henager, H.L. Heinisch, M. Stan, M.I. Baskes, S.M. Valone, J. Nucl.
 [1] Y.S. Kim, G.L. Hofman, J. Nucl. Mater. 419 (2011) 291e301.                                   Mater. 392 (2009) 292e300.
 [2] J. Gan, D.D. Keiser, B.D. Miller, A.B. Robinson, J.F. Jue, P. Medvedev,                 [44] P.C. Millett, A. El-Azab, D. Wolf, Comp. Mater. Sci. 50 (2011) 960e970.
     D.M. Wachs, J. Nucl. Mater. 424 (2012) 43e50.                                           [45] S.Y. Hu, C.H. Henager, Y.L. Li, F. Gao, X. Sun, M.A. Khaleel, Model. Simul. Mater.
 [3] D.D. Keiser, J.F. Jue, A.B. Robinson, P. Medvedev, J. Gan, B.D. Miller,                      Sci. Eng. 20 (2012).
     D.M. Wachs, G.A. Moore, C.R. Clark, M.K. Meyer, M.R. Finlay, J. Nucl. Mater. 425        [46] A. Badillo, P. Bellon, R.S. Averback, Model. Simul. Mater. Sci. Eng. 23 (2015).
     (2012) 156e172.                                                                         [47] X.H. Guo, S.Q. Shi, Q.M. Zhang, X.Q. Ma, J. Nucl. Mater. 378 (2008) 110e119.
 [4] B.D. Miller, J. Gan, J.D.D. Keiser, A.B. Robinson, J.F. Jue, J.W. Madden,               [48] A.J. Clarke, K.D. Clarke, R.J. McCabe, C.T. Necker, P.A. Papin, R.D. Field,
     P.G. Medvedev, J. Nucl. Mater. 458 (2015) 115e121.                                           A.M. Kelly, T.J. Tucker, R.T. Forsyth, P.O. Dickerson, J.C. Foley, H. Swenson,
 [5] Y.S. Kim, G.L. Hofman, J.S. Cheon, J. Nucl. Mater. 436 (2013) 14e22.                         R.M. Aikin, J.D.E. Dombrowski, J. Nucl. Mater. 465 (2015) 784e792.
 [6] S. Van den Berghe, W. Van Renterghem, A. Leenaers, J. Nucl. Mater. 375 (2008)           [49] V.P. Sinha, P.V. Hegde, G.J. Prasad, G.K. Dey, H.S. Kamath, J. Alloy Compd. 506
     340e346.                                                                                     (2010) 253e262.
 [7] J.H. Evans, Nature 229 (1971), 403-&.                                                   [50] V.P. Sinha, P.V. Hegde, G.J. Prasad, G.K. Dey, H.S. Kamath, J. Alloy Compd. 491
 [8] J.H. Evans, J. Nucl. Mater. 119 (1983) 180e188.                                              (2010) 753e760.
 [9] P.B. Johnson, F. Lawson, Nucl. Instrum. Methods B 243 (2006) 325e334.                   [51] S.G. Kim, W.T. Kim, T. Suzuki, Phys. Rev. E 60 (1999) 7186e7197.
[10] P.B. Johnson, D.J. Mazey, Nature 276 (1978) 595e596.                                    [52] J. Heulens, B. Blanpain, N. Moelans, Acta Mater. 59 (2011) 3946e3954.
[11] P.B. Johnson, D.J. Mazey, J. Nucl. Mater. 218 (1995) 273e288.                           [53] N. Moelans, B. Blanpain, P. Wollants, Phys. Rev. Lett. 101 (2008).
[12] K. Krishan, Radiat. Eff. Defects 66 (1982) 121e155.                                     [54] N. Moelans, B. Blanpain, P. Wollants, Phys. Rev. B 78 (2008).
[13] S.J. Zinkle, B.N. Singh, J. Nucl. Mater. 283 (2000) 306e312.                            [55] Y. Adda, A. Kirianenko, J. Nucl. Mater. 1 (1959) 120e126.
[14] H.L. Heinisch, B.N. Singh, Philos. Mag. 83 (2003) 3661e3676.                            [56] D. Schwen, R.S. Averback, J. Nucl. Mater. 402 (2010) 116e123.
[15] J.H. Evans, Philos. Mag. 85 (2005) 1177e1190.                                           [57] T. Opplestrup, V.V. Bulatov, G.H. Gilmer, M.H. Kalos, B. Sadigh, Phys. Rev. Lett.
[16] A.A. Semenov, C.H. Woo, J. Nucl. Mater. 382 (2008) 96e102.                                   97 (2006).
[17] A.A. Semenov, C.H. Woo, W. Frank, Appl. Phys. A-Mater. 93 (2008) 365e377.               [58] J.W. Cahn, Acta Metall. Mater. 9 (1961) 795e801.
[18] S.Y. Hu, C.H. Henager, J. Nucl. Mater. 394 (2009) 155e159.                              [59] J.W. Cahn, S.M. Allen, J. de Phys. 38 (1977) C7eC51.
[19] Y.N. Osetsky, A. Serra, V. Priego, F. Gao, D.J. Bacon, Diffus. Mech. Cryst. Mater.      [60] C.H. Woo, B.N. Singh, Philos. Mag. A 65 (1992) 889e912.
     527 (1998) 49e58.                                                                       [61] S.I. Golubov, A.V. Barashev, R.E. Stoller, Comprehensive Nuclear Materials,
[20] D.J. Bacon, F. Gao, Y.N. Osetsky, J. Nucl. Mater. 276 (2000) 1e12.                           2012.
[21] Y.N. Osetsky, F. Gao, D.J. Bacon, Microstruct. Process. Irradiat. Mater. 540            [62] K. Govers, C.L. Bishop, D.C. Parﬁtt, S.E. Lemehov, M. Verwerft, R.W. Grimes,
     (1999) 691e696.                                                                              J. Nucl. Mater. 420 (2012) 282e290.
[22] P.B. Johnson, K.J. Stevens, R.W. Thomson, Nucl. Instrum. Methods B 62 (1991)            [63] R.S. Nelson, J. Nucl. Mater. 31 (1969), 153-&.
     218e227.                                                                                [64] D.R. Olander, D. Wongsawaeng, J. Nucl. Mater. 354 (2006) 94e109.
[23] W.G. Wolfer, Philos. Mag. A 58 (1988) 285e297.                                          [65] S.Y. Hu, L.Q. Chen, Acta Mater. 49 (2001) 1879e1890.
[24] W.G. Wolfer, Philos. Mag. A 59 (1989) 87e103.                                           [66] R. Munze, O. Hladik, S.A. Marei, S. Elbayoumy, M. Elgarhy, J. Radioanal. Chem.
[25] D.E. Burkes, C.A. Papesch, A.P. Maddison, T. Hartmann, F.J. Rice, J. Nucl. Mater.            45 (1978) 141e146.
     403 (2010) 160e166.                                                                     [67] J. Rest, J. Nucl. Mater. 407 (2010) 55e58.
[26] R.M. Hengstler, L. Beck, H. Breitkreutz, C. Jarousse, R. Jungwirth, W. Petry,           [68] D.E. Smirnova, A.Y. Kuksin, S.V. Starikov, J. Nucl. Mater. 458 (2015) 304e311.
     W. Schmid, J. Schneider, N. Wieschalla, J. Nucl. Mater. 402 (2010) 74e80.               [69] G. Kresse, J. Furthmuller, Phys. Rev. B 54 (1996) 11169e11186.
[27] K. Huang, D.D. Keiser, Y.H. Sohn, Metall. Mater. Trans. A 44A (2013) 738e746.           [70] G. Kresse, D. Joubert, Phys. Rev. B 59 (1999) 1758e1775.
[28] S.J. Rothman, L.T. Lloyd, A.L. Harkness, T Am. I Min. Met. Eng. 218 (1960)              [71] P.E. Blochl, Phys. Rev. B 50 (1994) 17953e17979.
     605e607.                                                                                [72] J.P. Perdew, K. Burke, M. Ernzerhof, Phys. Rev. Lett. 77 (1996) 3865e3868.
[29] B. Beeler, B. Good, S. Rashkeev, C. Deo, M. Baskes, M. Okuniewski, J. Nucl.             [73] H.J. Monkhorst, J.D. Pack, Phys. Rev. B 13 (1976) 5188e5192.
     Mater. 425 (2012) 2e7.                                                                  [74] A. van de Walle, P. Tiwary, M. de Jong, D.L. Olmsted, M. Asta, A. Dick, D. Shin,
[30] B. Beeler, B. Good, S. Rashkeev, C. Deo, M. Baskes, M. Okuniewski, J. Phys-                  Y. Wang, L.Q. Chen, Z.K. Liu, Calphad 42 (2013) 13e18.
     Condens. Mater. 22 (2010).                                                              [75] A. van de Walle, M. Asta, G. Ceder, Calphad 26 (2002) 539e553.
[31] B. Beeler, C. Deo, M. Baskes, M. Okuniewski, J. Phys-Condens. Mater. 24 (2012).         [76] L.Q. Chen, J. Shen, Comput. Phys. Commun. 108 (1998) 147e158.
[32] B. Beeler, C. Deo, M. Baskes, M. Okuniewski, J. Nucl. Mater. 433 (2013)                 [77] M.C. Teague, B.S. Fromm, M.R. Tonks, D.P. Field, Jom-Us 66 (2014) 2569e2577.
     143e151.                                                                                [78] J.D. Hales, M.R. Tonks, K. Chockalingam, D.M. Perez, S.R. Novascone,
[33] A. Landa, P. Soderlind, P.E.A. Turchi, J. Nucl. Mater. 414 (2011) 132e137.                   B.W. Spencer, R.L. Williamson, Comp. Mater. Sci. 99 (2015) 290e297.
[34] D.E. Smirnova, A.Y. Kuksin, S.V. Starikov, V.V. Stegailov, Z. Insepov, J. Rest,         [79] V.I. Dubinko, Radiat. Eff. Defect S 160 (2005) 85e97.
     A.M. Yacout, Model. Simul. Mater. Sci. Eng. 21 (2013).                                  [80] J. Gan, D.D. Keiser, D.M. Wachs, A.B. Robinson, B.D. Miller, T.R. Allen, J. Nucl.
[35] D.E. Smirnova, S.V. Starikov, V.V. Stegailov, J. Phys-Condens. Mater. 24 (2012).             Mater. 396 (2010) 234e239.
[36] D.E. Smirnova, A.Y. Kuksin, S.V. Starikov, V.V. Stegailov, Phys. Met. Metallogr.        [81] Y.S. Kim, G.L. Hofman, J.S. Cheon, A.B. Robinson, D.M. Wachs, J. Nucl. Mater.
     116 (2015) 445e455.                                                                          437 (2013) 37e46.
