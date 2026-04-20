# Three-dimensional phase-field simulations of intragranular gas bubble evolution in irradiated U-Mo fuel

---

                                                          Computational Materials Science 145 (2018) 86–95



                                                            Contents lists available at ScienceDirect


                                                  Computational Materials Science
                                          journal homepage: www.elsevier.com/locate/commatsci




Three-dimensional phase-field simulations of intragranular gas bubble
evolution in irradiated U-Mo fuel
Linyun Liang ⇑, Zhi-Gang Mei, Yeon Soo Kim, Mihai Anitescu, Abdellatif M. Yacout
Argonne National Laboratory, 9700 South Cass Avenue, Argonne, IL 60439, USA



a r t i c l e       i n f o                          a b s t r a c t

Article history:                                     The evolution of fission gas bubbles in irradiated materials plays a critical role in the microstructural pro-
Received 27 September 2017                           cesses that leads to dimensional changes of U-Mo alloy fuels, e.g., fuel swelling. Although the intergran-
Received in revised form 28 December 2017            ular bubbles-induced fuel swelling has been long-discussed for U-Mo fuel, there are very few
Accepted 29 December 2017
                                                     computational studies of the formation of intragranular gas bubbles and its impact on fuel swelling. To
Available online 4 January 2018
                                                     this end, we develop a three-dimensional phase-field model to investigate the evolution of intragranular
                                                     gas bubbles in U-Mo fuel. Fission induced defect formation and annihilation processes, such as vacancy-
Keywords:
                                                     interstitial recombination, fission gas atom resolution, and interactions with dislocations and grain
Phase-field
Intragranular gas bubbles
                                                     boundaries are incorporated in the model. Simulations show that the intragranular gas bubbles can be
Fuel swelling                                        stabilized to certain sizes due to the balance between the generation and annihilation of defects. The
                                                     intragranular gas bubbles induced fuel swelling is predicted to be comparable to experimental measure-
                                                     ments. The effects of the irradiation and fuel fabrication conditions (i.e., fission rate, fuel grain size, and
                                                     mechanical work induced deformation) on the bubble evolution and the resultant swelling are investi-
                                                     gated. The current simulations provide a better understanding of intragranular gas bubble-induced swel-
                                                     ling and a solid foundation for the future study of the nucleation and growth of intergranular gas bubbles
                                                     and recrystallization in U-Mo fuel.
                                                                                                                                         Published by Elsevier B.V.




1. Introduction                                                                          Various types of fission gas bubbles have been observed in irra-
                                                                                     diated U-Mo alloy fuels. These gas bubbles can be categorized into
    Understanding and predicting fission-induced microstructural                     three types based on their morphology and location: (1) intragran-
changes in materials are of great importance to developing new                       ular bubbles – those inside fuel grains, usually of nanometer scale
fuels for both nuclear power and research reactors. U-Mo alloys                      and evenly distributed; (2) intergranular bubbles – those on grain
are under investigation as a candidate fuel for future high power                    boundaries, usually of micrometer scale; and (3) periphery bubbles
research reactors [1,2], because of their stable swelling behavior                   – those in the interaction layer of the fuel and Al matrix, usually
at moderate fission densities [3,4]. During the fission reactions of                 large and unevenly distributed [5]. The final morphology of gas
uranium-235, fission gas atoms, such as Xe, are generated at a rate                  bubbles is affected by several factors, such as types of fuel, fuel fab-
of about 0.25 atom per fission as a result of decay of primary fission               rication conditions, and operation conditions of reactors. Although
products. These fission gas atoms are almost insoluble in metallic                   fission gas bubbles have different morphologies, the initial stage of
fuels, and tend to accumulate in voids to form gas bubbles. The for-                 bubble formation is considered to be similar, starting as isolated
mation of fission gas bubbles can lead to serious dimensional                        fission gas atoms inside fuel grains. Therefore, understanding the
changes of nuclear fuels, e.g., fuel swelling, which can affect the                  mechanism of the nucleation and growth of intragranular bubbles
fuel performance and the long-term safety of reactors. Therefore,                    is critical to investigating the evolutions of other types of gas
understanding the mechanism of the nucleation and growth of fis-                     bubbles.
sion gas bubbles and their impact on fuel swelling plays a critical                      During fission events, incident irradiations produce isolated gas
role in the qualification of U-Mo fuel for high performance research                 atoms and Frenkel pairs. The generated vacancies and self-
reactors.                                                                            interstitial atoms (SIAs) in equal numbers can annihilate either
                                                                                     through their recombination to form perfect lattices or by interac-
                                                                                     tions with defect sinks such as dislocations, grain boundaries, or
 ⇑ Corresponding author.                                                             precipitates. The efficiency of vacancy/SIA absorption by different
   E-mail address: linyun@anl.gov (L. Liang).                                        sinks varies vastly because of the different sink strengths. The

https://doi.org/10.1016/j.commatsci.2017.12.061
0927-0256/Published by Elsevier B.V.
                                              L. Liang et al. / Computational Materials Science 145 (2018) 86–95                                                              87


relaxation volumes of SIAs in bcc alloys are typically much larger                2. Phase-field methodology
than those of vacancies, resulting in a higher rate of SIAs to interact
with edge dislocations than vacancies [6]. This property is the ori-                  To study the evolution of fission gas bubble in U-Mo fuel, we
gin of dislocation bias, and is the driving force for the formation of            chose three parameters as composition fields in the phase-field
vacancy clusters. The fission gas atoms can be easily trapped by                  model, namely, the concentrations of fission gas Xe cX ðr; tÞ, vacancy
vacancy clusters to form intragranular gas bubbles inside fuel                    cV ðr; tÞ, and SIA cI ðr; tÞ, which represent atoms or mole fractions at
grains. Subsequently, the growth of intragranular gas bubbles are                 position r and time t. The phase parameter gðr; tÞ is chosen to rep-
closely related to the effective diffusivities of fission gas atoms in            resent the gas bubble phase with g ¼ 1 and the matrix phase with
fuel grains. Generally, intragranular gas bubbles confined inside                 g ¼ 0. g changes continuously from 0 to 1 across the interface
fuel grains do not grow to an appreciable size. The phenomenon                    between the gas bubble and matrix. The total free energy of the
is attributed to the fission-induced gas atom re-solution process                 system can be described by
[7], in which small intragranular gas bubbles are partially or com-                                             Z h
                                                                                                                                                       jX                jV
pletely destroyed by close-passing fission fragments and some of                  FðcX ; cV ; cI ; g; eij Þ ¼         f chem ðcX ; cV ; cI ; g; TÞ þ        jrc X j2 þ
                                                                                                                                                             jrcV j2
                                                                                                                                                       2                 2
the gas atoms in the bubbles are resolved into the fuel matrix.
                                                                                                                 jI        jg                                  i
Therefore, the formation, growth, and dissolution of gas bubbles                                                þ jrcI j2 þ jrgj2 þ f elas cX ; cV ; cI ; g; eij dV;
                                                                                                                 2         2
in U-Mo fuel are closely related to the diffusion of point defects
                                                                                                                                                                   ð1Þ
and their reactions with defect aggregates.
    Computer simulation as a cost-effective method can provide                    where f chem is the chemical free energy density describing the com-
important information for the development of new materials. Var-                  position and volume fraction of the equilibrium phases,jX , jV , jI ,
ious computational approaches have been used to study the behav-                  and jg are the gradient energy coefficients for Xe, vacancy, and
ior of gas bubbles in irradiated materials. Among those, phase-field              SIA concentrations, and the phase parameter, respectively, f elas is
method is a mesoscale approach that has been successfully applied                 the elastic energy density, eij is the strain, and T is the temperature.
to study the nucleation and growth of voids [8–11] and their                      The first term in the volume integral represents the local contribu-
migration [12–14], interstitial kinetics [15,16], crack propagation               tion to the free energy from short-range chemical interactions. Four
[17], gas bubble evolution [18–24], and recrystallization [25] in                 second derivative terms in the volume integral represent the inter-
nuclear materials. In particular, Millett et al. [9,21] proposed a                facial properties. The last term in the volume integral represents the
physics-based phase-field model to simulate the evolution of voids                long-range elastic interactions.
and gas bubbles in irradiated materials. Their model can capture                     The chemical free energy density describes the thermodynamic
the processes of point defect generation and recombination, and                   properties of the system by
bubble nucleation and growth in the presence of grain boundaries.
However, their simulations were performed in two dimensions,                      f chem ðcX ; cV ; cI ; g; TÞ ¼ hðgÞf b ðcX ; cV ; cI ; TÞ
and several important defects reactions were ignored, such as                                                    þ ½1  hðgÞf m ðcX ; cV ; cI ; TÞ þ wgðgÞ;                  ð2Þ
fission-induced gas atom resolution, vacancy and SIA interaction
with dislocations, and diffusion of gas atoms to grain boundaries.                where f b and f m are the free energy densities of the gas bubble and
These defect reactions are important to the formation of the stable               matrix, respectively, hðgÞ is an interpolation function with the form
nanometer size gas bubble structures [7,21]. Although significant                 g3 ð6g2  15g þ 10Þ, gðgÞ is a double-well function with the form
progress has been made, few phase-field models can reproduce
                                                                                  g2 ð1  gÞ2 to promote the stable phases, and w is the potential bar-
the stable intragranular gas bubble structures under irradiation.
                                                                                  rier height.
One exception is a recent work by Hu et al. [26], in which a two-
                                                                                      In deriving the free energy of the matrix, the condition
dimensional phase-field model was developed to study the forma-
                                                                                  cX þ cV þ cI þ cM ¼ 1:0 (cM is the concentration of perfect lattice
tion of gas bubble superlattice in U-Mo. However, it should be
                                                                                  site) is always satisfied since we assume that the defects can
pointed out that the generation of fission gas was artificially turned
                                                                                  occupy only the lattice sites. Thus, by adopting the ideal solution
off in order to maintain a saturated Xe concentration in their
                                                                                  model, we can express the free energy of the matrix as
model.
    In this work, we develop a three-dimensional phase field                      f m ðcX ; cV ; cI ; TÞ ¼ EXf cX þ EVf cV þ EIf cI þ kB TðcX lncX þ cV lncV þ cI lncI
model to study the gas bubble evolution in bcc U-Mo alloy with
                                                                                                          þ ð1  cX  cV  cI Þlnð1  cX  cV  cI ÞÞ;                        ð3Þ
7 wt.% Mo (U-7Mo) based on Millett et al.’s two-dimensional
model. The large size difference between intragranular bubbles
                                                                                  where EXf , EVf , and EIf are the formation energies of Xe, vacancy, and
(size around 1.0–5.0 nm) and intergranular bubbles (size around
0.1–0.3 µm) makes simulating them simultaneously difficult                        SIA in the matrix phase, respectively, and kB is the Boltzmann’s
because of the limitation of computing resources. In this work                    constant.
we focus on intragranular gas bubbles in U-Mo alloy fuel. The                         For the free energy of gas bubbles, the definition of the Xe
current model incorporates most of the key defect processes,                      atom concentration differs from that in the matrix. In bubbles,
including the defect production by fission, gas atoms re-                         Xe atoms can occupy either lattice or non-lattice sites. The Xe
resolution, grain boundary sinks for gas atoms, vacancy-SIA                       concentration in the bubble is defined as cbX ¼ N X =V b , where N X
recombination, and dislocation sinks for the vacancy and SIA.                     is the number of Xe atoms in the bubble and V b is the volume
We develop a new free energy for gas bubble phases based on                       of the bubble. Based on this definition, the Xe EOS can be used
the van der Waals equation of state (vdW EOS). By including                       to determine the free energy of gas bubble contributed by Xe
the critical defect annihilation and gas-atom resolution processes,               accumulation. A detailed derivation of the Xe bubble free energy
we demonstrate that the stable intragranular gas bubble structure                 is given in the appendix. The free energy of the Xe bubble based
observed in experiments can be reproduced. The predicted fission                  on the vdW EOS is given by
gas bubble size distribution and bubble-induced swelling of U-Mo                   b                                          b      kB T
are in agreement with experimental measurements. We also                          f X ðcbX Þ ¼ cbX l0 ðp0 Þ þ cbX kB TlncX þ cbX kB Tln
                                                                                                                                      p0
investigate the influence of fabrication and irradiation conditions                                                                                         
                                                                                                                                            cbX kB T
on the growth kinetics of intragranular gas bubbles and the resul-                             cbX kB Tlnð1  B cbX kB TÞ þ cbX kB TB0
                                                                                                                0
                                                                                                                                                          p0 ;               ð4Þ
tant fuel swelling in U-Mo.                                                                                                              1  B0 cbX kB T
88                                                        L. Liang et al. / Computational Materials Science 145 (2018) 86–95


where l0 and p0 are the chemical potential and the pressure at the                            described by a sink term S_ X ¼ ð1  gÞ2 r g Sg V X cX , where Sg is the
reference state, respectively, and B0 is a constant related to the vdW                        grain boundary areas per unit volume, V X is the velocity of the
constant, which can be obtained by fitting the experimental data.                             gas atom, and rg is a rate constant [33].
    Because of the different definitions of Xe concentration in the                              When SIAs and vacancies encounters each other, they recom-
matrix and gas bubbles, we have to convert the Xe concentration                               bine and form a perfect lattice. Their recombination can be
to be consistent with the definition in the matrix. The definition                            described by R_ VI ¼ mr cV cI , where mr is the recombination rate. To
of the Xe concentration can be written as cbX ¼ N X =V b ¼ cX =V site ,                       account for the faster recombination rate on the void surface, we
where NX is the number of Xe atoms per unit of volume and V site                              define it as mr ¼ mb þ g2 ms , where mb and ms is the recombination rate
is the volume of lattice site of the host material. Thus, the free                            in the bulk and on the surface, respectively. mb is given by
energy of the gas bubble is                                                                   4pr iv ðDI þ DV Þ=X, where r iv is the radius of the recombination vol-
                                               b                                              ume and DV and DI are the diffusivities of vacancy and SIA, respec-
f b ðcX ; cV ; cI ; TÞ ¼ AðcV  1Þ2 þ Bc2I þ f X ðcX Þ;                             ð5Þ
                                                                                              tively [34].
where A and B are constants.                                                                        Due to the unique nature of the stress field in the neighborhood
   The governing equations describing the spatial and temporal                                of a dislocation line, the dislocation is an efficient sink for many
evolutions of the phase parameter and the concentrations of Xe,                               atomic defects. Vacancies and SIAs approaching a dislocation can
vacancy, and SIA are                                                                          be permanently captured. Thus, the dislocation acts as a perfect
                                                                                              sink for vacancies and SIAs. The sink terms can be described as
@g     dF
   ¼ L þ n_ g ;                                                                  ð6aÞ        S_ i ¼ k Di ci , where k and k are the sink strengths of dislocations
                                                                                                      2               2       2
@t     dg                                                                                             i                           V          I
                                                                                              for vacancies and SIAs [6]. They take the forms,
                  
@cX            dF                                                                              2
                                                                                              kV ¼ Z V q;                                                          ð8aÞ
    ¼ r  MX r       þ n_ X þ P_ X  _Rre  _SX ;                                 ð6bÞ
@t             dcX
                                                                                               2
                                                                                            kI ¼ Z I q;                                                          ð8bÞ
@cV            dF
    ¼ r  MV r       þ n_ V þ P_ V  _RVI  _SV ;                                 ð6cÞ        where Z V and Z I are the dislocation bias terms for vacancies and
 @t            dcV
                                                                                              SIAs, respectively, and q is the dislocation density in the materials.
                                                                                               The motilities of the Xe, vacancy, and interstitial atoms can be
@cI            dF
    ¼ r  MI r       þ n_ I þ P_ I  R_ VI  S_ I ;                               ð6dÞ        described by
@t             dcI
                                                                                                      c i Di
                                                                                              Mi ¼           ; ði ¼ X; V; IÞ:                                       ð9Þ
where n_ i (i = g, X, V, I) are the thermal induced fluctuations, and                                 kB T
P_ i (i = X, V, I) are the point defect production rates. The production
                                                                                                 Due to the introduction of defects in the matrix, a lattice misfit
rate of Xe is expressed as P_ X ¼ 2ð1  gÞ2 KXf r Ran, where fr is the                        can occur between the matrix and gas bubbles. The strain energy
fission rate, Ran is the random number uniformly between 0 and                                caused by the misfit can be described by elastic theory. If the vari-
1, the number 2 is used to account for the loss of concentration                              ation of the stress-free lattice parameter, a, with respect to defect
due to the introduction of the random number, X is the volume of                              (vacancy and interstitial) concentrations is assumed to obey
the lattice site of U-Mo, and K is a constant.                                                Vegard’s law, the local stress-free strain caused by the defect inho-
    The Frenkel pair production rate in the unit of displacement per                          mogeneity in the matrix is given by [20]
atom (dpa) in the fuel can be related to the fission rate according to                                    h                                                  i
                                                                                                               eq0                 eq0                 eq0
                                                                                               ij ¼ e ðc X  c X Þdij þ e ðc V  c V Þdij þ e ðc I  c I Þdij ;
                                                                                              e0m                                                                  ð10Þ
                                                                                                     X0                  V0                  I0
[27],

              dpa f r
P_ V ¼ P_ I ¼    ¼ ;                                                                ð7Þ       where eX0 ¼ ð1=aÞda=dcX , eV0 ¼ ð1=aÞda=dcV , and eI0 ¼ ð1=aÞda=dcI
               s  d                                                                           are the expansion coefficients of the lattice parameter due to the
where d is a constant.                                                                        introduction of gas atoms, vacancies, and SIAs, ceq0       eq0       eq0
                                                                                                                                                   X ; c V , and c I
    Gas-atom re-solution is a dynamic bubble shrinkage mecha-                                 are the equilibrium concentration of the Xe, vacancy, and self-
nism in which the fission gas atoms are knocked out from a bubble                             interstitial atoms, respectively, and dij is the Kronecker-delta
caused directly or indirectly by the fission fragments [28–30]. The                           function.
observation that intragranular bubbles do not grow to appreciable                                Similarly, the local stress-free strain caused by the defect inho-
sizes at low temperatures can be ascribed to the effect of                                    mogeneity in the gas bubble is [20]
irradiation-induced gas-atom re-solution [28,30,31]. There are                                                 eq0
                                                                                               ij ¼ e ðc X  c X Þdij ;
                                                                                              e0b                                                                  ð11Þ
                                                                                                     b0
two accepted mechanisms of the re-solution effect: one is the
heterogeneous process which destroys entire bubbles in the path
                                                                                              where the expansion coefficients of the lattice parameter eb0 is
of fission fragments and in which all gas atoms in the bubble return
                                                                                              related to the introduction of gas bubbles.
to the matrix as single atoms; and the other is a homogeneous pro-
                                                                                                 Following Khachaturyan’s elastic theory [35], the elastic strain
cess which re-solves fission-gas atoms singly by scattering colli-
                                                                                              can be calculated by
sions with fission fragments and uranium recoils whose paths
intersect the bubbles. Both mechanisms [7] agree that the intra-                              eelij ¼ eij þ deij ðrÞ  ½hðgÞe0b
                                                                                                                              ij ðrÞ þ ð1  hðgÞÞeij ðrÞ;
                                                                                                                                                  0m
                                                                                                                                                                   ð12Þ
granular bubbles rapidly grow to certain sizes; the bubbles are
                                                                                              where eij is the homogeneous strain describing the macroscopic
either dissolved (heterogeneous mechanism [29]) or stabilized
(homogeneous mechanism [32]). We adopt the homogeneous                                        shape and volume change, which is defined such that
                                                                                              Rd *                        *
mechanism in this work for simplifying the model. The fission-                                  eij ð r ÞdV ¼ 0 and dekl ð r Þ is a function of displacement as
                                                                                                              *                       *
induced gas resolution is written as R_ re ¼ g2 bcX , where b is the res-                     1=2½@uk ð r Þ=@r l þ @ul ð r Þ=@r k  [36]. The elastic energy density can
                        2
olution rate and g is used to limit the gas resolution occurring                              be calculated by
only inside the gas bubble.
   Free atoms diffuse towards the grain boundaries, where they                                                       1
                                                                                              f elas ðcX ; eij Þ ¼     kijkl eelij eelkl ;                         ð13Þ
can form intergranular bubbles. The diffused gas atoms can be                                                        2
                                             L. Liang et al. / Computational Materials Science 145 (2018) 86–95                                                   89


where kijkl is the elastic constant tensor of the system. We assume              Table 1
the elastic constants for the gas bubble are the same as in the bulk             Materials properties of U-7Mo alloy used in the simulations.

U-Mo alloy [20].                                                                   Physical parameter                   Symbol      Value             Reference
   Modeling the nucleation process is one of the greatest chal-                    Temperature                          T           473 K             This work
lenges in phase-field simulations. In this work, we explicitly intro-              Lattice constant of U-7Mo            a           3.43  1010 m    This work
duce nuclei in the governing equation following the classical                      Surface energy                       r           1.81 J/m2         This work
nucleation theory. The detailed procedure can be found in previous                 Gradient coefficients                jX;V ;I;g   6.91  109 J/m   This work
                                                                                   Potential height                     w           7.73  109 J/m3   This work
work [37,38].
                                                                                   Vacancy formation energy             EVf         1.12 eV           This work
                                                                                   Interstitial formation energy        EIf         1.48 eV           This work
                                                                                   Xe solution energy                   EXf         6.95 eV           This work
                                                                                   Xe diffusivity                       DX          4.10  1017 m2   [40]
3. Material properties                                                                                                              s1
                                                                                   Interstitial diffusivity             DI          2.05  1014 m2   This work
                                                                                                                                    s1
    In order to study the bubble evolution in U-7Mo alloy,
                                                                                   Vacancy diffusivity                  DV          3.84  1017 m2   This work
material properties, such as elastic constants, bubble surface                                                                      s1
energy, defects formation energies, reaction rates and defect                      Kinetic coefficient                  L           9.04  108 m3    This work
diffusivities, are needed as input parameters for the phase-                                                                        J1 s1
field simulations. Recently, Mei et al. [39] studied the elastic                   Elastic constant                     C 11        173.0 Gpa         [39]
                                                                                   Elastic constant                     C 12        138.0 Gpa         [39]
properties of U-7Mo alloy using density functional theory
                                                                                   Elastic constant                     C 44        50.0 Gpa          [39]
(DFT) calculations. So far, the surface energy, defect formation                   Resolution rate                      b           2.0  1025 fr    [41]
energies, and defect diffusivities in U-Mo alloys have not been                    Dislocation bias for vacancies       Zv          1.0               [6]
studied yet. To this end, we studied the surface properties of                     Dislocation bias for interstitials   Zi          1.025             [6]
                                                                                   Nucleation rate                      k1          1.0  103        This work
U-7Mo alloy using DFT calculations. Four typical surfaces of
                                                                                   Nucleation rate constant             k2          1.0  105        This work
bcc phase, namely, (1 0 0), (1 1 0), (1 1 1) and (2 1 1) surfaces,                 Velocity of Xe atom                  VX          300.08 m/s        This work
are considered. The most stable surface is predicted to be                         Frenkel pair rate constant           d           6.2               This work
(1 1 0) with a surface energy of 1.81 J/m2. Due to the complex                     Xe generation rate constant          K           0.25              [42]
atomic environment in the structure of U-7Mo alloy, the defect                     Rate constant for grain boundary     rg          2.4  102         This work
                                                                                      sink
formation energy in the alloy is estimated by averaging the
                                                                                   Radius of the recombination          riv         2.0  1010 m     [6]
vacancy or interstitial formation energies of four independent                        volume
configurations of U/Mo. The formation energies of vacancy                          Recombination rate on surface        vs          2vb               This work
and interstitial in U-7Mo alloy are predicted to be 1.12 eV
and 1.48 eV, respectively. With a similar approach, the solution
energy of Xe in U-7Mo matrix is predicted to be 6.95 eV. We                      4. Results and discussion
note that both the defect formation energy and the Xe solution
energy are presented as averaged results at the U and Mo                            In this section we present the phase-field simulation results of
lattice sites, because U and Mo are not distinguished in the                     intragranular gas bubble evolution and gas bubble-induced swel-
current model. The diffusivities of U/Mo vacancy and SIA in                      ling in irradiated U-Mo alloy fuel. Our simulation shows that the
U-7Mo alloy are predicted from the mean square displacement                      formation of a stable intragranular gas bubble structure observed
of defects calculated by molecular dynamics (MD) simulations.                    in U-Mo fuel is due to the dynamic equilibrium between defect
The calculated diffusivities show that SIAs diffuse significantly                generation and annihilation. In the following subsections, we dis-
faster than vacancies in U-7Mo alloy. A detailed description                     cuss the effects of fission rate, initial fuel grain size, and fuel fabri-
of the calculations of the formation energy and diffusivity of                   cation conditions on the evolution of intragranular gas bubbles and
defects in U-7Mo alloy using DFT and MD will be presented                        the resultant swelling in U-Mo fuel.
elsewhere. The Xe diffusivity in U-7Mo alloy is adopted from
Rest’s work [40]. Table 1 presents the values of the principal                   4.1. Stable intragranular gas bubble structure under irradiation
parameters used in the current simulation.
    The mobilities M X;I;V of point defects are related to their                    The evolution of fission-induced defect concentrations can be
diffusivities DX;V ;I by Eq. (9). Constants A and B in the free energy           obtained by solving the coupled equations (6a)–(6d). Typical irra-
function in Eq. (5) are chosen to be 1:1  1010 J cm3 and                       diation and fabricated conditions for U-Mo fuel are used in the
2:3  1010 J cm3 to ensure that the vacancy and SIA have identical              simulations, i.e., the fission rate, grain boundary density, and dislo-
and lower chemical potentials in the gas bubble and matrix phases,               cation density are fixed at 5:0  1020 m3 s1, 0.41 m1, and
respectively. The gradient coefficients and potential height are                 0.431015 m2, respectively [5,45]. The simulated phase parameter
determined by the surface energy of a gas bubble as shown in                     and point defect concentration profiles are shown in Fig. 1 at differ-
Table 1. The other parameters used include the lattice misfit                    ent irradiation times. Fission gas atoms and vacancies tend to accu-
strains, eX0 ¼ 0:006, eV 0 ¼ 0:02, eI0 ¼ 0:02, and eb0 ¼ 0:003. The             mulate and form gas bubbles, in which the equilibrium
                                       pﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
velocity of Xe can be obtained by        3kB T=mX , where mx is the              concentrations of vacancy, Xe, and SIA inside gas bubbles are about
atomic mass of the Xe with the value of 2.17  1025 kg. The cur-                1.0, 0.90, and 0.07, respectively. The average gas bubble pressure is
rently used defect production rates are consistent with the typical              about 1.3 GPa estimated by the vdW EOS Eq. (A.5), which is consis-
average fission rate used for the in-pile test of U-Mo dispersion                tent with the Xe gas pressure predicted by other phase field simu-
fuels [34,43].                                                                   lations [26]. The concentration of SIAs is considerably lower than
   In the simulations, a model size of 22.4 nm  22.4 nm  22.4                  that of vacancies inside gas bubbles because of the biased disloca-
nm is used. The grid spacing is Dl ¼ 0:35 nm. Periodic boundary                  tion sink. Although SIAs and vacancies are generated equally as
conditions are imposed on the simulation domain. A semi-                         Frenkel pairs during irradiation, their annihilation rates at disloca-
implicit FFTW method is employed to solve the coupled Eqs.                       tions are vastly different due to the difference in atomic diffusion
(6a)–(6d) [44].                                                                  radius [43]. More SIAs are annihilated at the dislocations leaving
90                                                      L. Liang et al. / Computational Materials Science 145 (2018) 86–95




                                  fd=0.10×1027 m-3            fd=0.20×1027 m-3               fd=0.38×1027 m-3                fd=3.0×1027 m-3
Fig. 1. Temporal evolution of (a) phase parameter; (b) vacancy; (c) Xe; (d) SIA concentrations in the irradiated U-Mo fuel. The isosurfaces of 0.7, 0.7, 0.5, and 0.1 were used for
plotting the phase parameter, vacancy, Xe, and SIA concentration profiles, respectively.




vacancies inside the grains. The accumulation of vacancies pro-                                 Experiments show that intragranular gas bubbles can form
vides room for large fission gas atoms to form stable gas bubbles.                          ordered superlattices in U-Mo dispersion fuels at low fission den-
Bubble growth is driven by the absorption of vacancies and gas                              sities [47,48]. Several potential mechanisms of the bubble super-
atoms. At the beginning of the irradiation, the size of the gas bub-                        lattice formation have been proposed: (1) elastic interaction
bles consistently grow with increasing fission time, while the num-                         between gas bubbles, (2) directional diffusion of SIAs, and (3) dis-
ber of gas bubbles increases. After a certain irradiation time, the                         location loop punching from overpressured bubbles. Recently, Hu
number of gas bubbles remains unchanged, while the bubble size                              et al. suggested that the directional diffusion of SIAs may be
increases very slowly. Small bubbles are dissolved due to fission-                          responsible for the gas bubble ordering structure [26]. However,
induced gas atom resolution and bubble coalescence. The bubble                              their simulation was performed in two-dimension, which may
coalescence occurs either through large bubbles swallowing small                            not reveal the true mechanism of the bubble superlattice forma-
bubbles or through atomic diffusion between bubbles. The simu-                              tion. Thus, due to the lack of a consensus on the formation mech-
lated gas bubbles appear to be randomly distributed in the irradi-                          anism of bubble superlattice, we assume the gas bubbles are
ated U-Mo fuel. The bubble migration is neglected in this model                             randomly distributed in U-Mo alloys.
because of its extremely low mobility at typical operation temper-                              The fuel swelling induced by fission gas bubbles can be esti-
atures of research reactors [46].                                                           mated by
    The evolution of gas bubbles in irradiated materials is inher-
                                                                                            DV V f  V 0
ently a dynamic process, involving a balance between the growth                                ¼         ;                                                                   ð14Þ
                                                                                            V0     V0
and shrinkage mechanisms. At a constant temperature, the nucle-
ation and growth of gas bubbles are driven by the supersaturation                           where V0 is the initial volume of fuel and Vf is the final fuel volume
of point defects under irradiation. Gas bubbles can grow by absorb-                         with contribution from fission gas bubbles. Fig. 2 shows the calcu-
ing vacancies or shrink by either emitting vacancies or absorbing                           lated fuel swelling due to intragranular gas bubbles. The gas bubble
interstitials. Addition or emission of gas atoms can change the vol-                        induced fuel swelling increases rapidly at the beginning of the irra-
ume of bubbles, with the relative change depending on the ratio of                          diation, and then remains almost unchanged. These results clearly
gas atoms to vacancies in the bubble. The calculated size of the gas                        show that at the beginning of irradiation the defect concentrations
bubbles ranges from 2.7 nm to 3.8 nm at the equilibrium state.                              build up but the concentrations are too low either for recombina-
                                                      L. Liang et al. / Computational Materials Science 145 (2018) 86–95                                                  91




      Fig. 2. Intragranular bubble swelling as a function of fission density.             Fig. 3. Simulated gas bubble size distribution in U-Mo fuel. The calculated fission
                                                                                          density is 3.0  1027 m3.


tion or sinks to have an effect on the buildup. As fission time
increases, the buildup of defect concentrations start to level off                        bubbles can show very different behaviors due to various fission
when the production rate is compensated by the recombination                              rates. Recrystallization occurs in the metallic U-Mo fuel at high fis-
rate and sink reactions. Eventually, the production of defects is bal-                    sion densities, which destabilizes the stable intragranular gas bub-
anced by the defect annihilation due to the recombination of vacan-                       ble structure [49,50]. Thus, the fission rate is expected to have a
cies and SIAs and sink reactions on grain boundaries and                                  great impact on the evolution of intragranular gas bubbles and
dislocations. Therefore, a stable gas bubble structure can be                             the resultant fuel swelling.
achieved, which is beneficial for realizing a stable fuel swelling                            The predicted effect of fission rate on the intragranular gas bub-
behavior. However, the stable intragranular gas bubble structure                          ble swelling in the U-Mo fuel is shown in Fig. 4(a). Three fission
can be destroyed at high fission densities due to the recrystalliza-                      rates of 3.0  1020 m3 s1, 5.0  1020 m3 s1, and 7.0  1020
tion process starting at grain boundaries. As a result, the fission                       m3 s1 are used in the simulations. The intragranular gas bubble
gases are released from the intragranular bubbles and diffuse to                          swelling shows the highest value for the largest fission rate. As
the grain boundaries to form intergranular gas bubbles, which are                         shown in Eqs. (6), the local defect production rate is proportional
the major source of fuel swelling at high fission densities. Therefore,                   to fission rate. With an increased fission rate, the generation rates
it is technically important to retain fission gas atoms inside intra-                     of point defects increase. Moreover, the annihilation rate of defects
granular bubbles as stable gas bubble structure in order to decrease                      also increases due to the increased recombination, resolution, and
overall fuel swelling at high fission densities.                                          sink reactions as shown in Eqs. (6), which are proportional to the
    During irradiation, the major processes that affect the gas bub-                      defect concentrations. However, at the beginning of irradiation,
ble sizes are the nucleation of gas bubbles, the diffusion of gas                         the effect of annihilation on the defect concentrations is relatively
atoms into bubbles, and the fission-induced gas atom re-solution.                         small compared with the rapid generation of defect concentrations,
The differences in growth rates of bubbles with different sizes                           thus the net concentrations of defects increase rapidly at high fis-
result in a peak bubble size distribution. The position of the peak                       sion rate. This results in a high supersaturation of defect concentra-
in the bubble size distribution is determined by the balance                              tions, which reduces the incubation time of gas bubble formation.
between the flux of gas atoms diffusion in and out of bubbles. As                         After the formation of gas bubbles, the continuous increase of
more fission gases and vacancies are generated, their diffusion into                      vacancy and Xe gas concentrations further promotes the growth
the bubbles increases, and the gas bubbles continuously grow. In                          of gas bubbles, which leads to the increased gas bubble swelling.
contrast, the irradiation-induced gas resolution decreases the gas                        The production of defects eventually is balanced by their annihila-
concentration inside the bubbles and the grain boundary and dis-                          tion, which leads to a stable gas bubble swelling. Therefore,
location sinks decrease the defect concentrations, which make                             increasing fission rate can lead to the increased intragranular gas
the gas bubbles shrink. The simulated size distribution of intra-                         bubble swelling in the U-Mo fuel at early irradiation time.
granular gas bubbles in U-Mo is given in Fig. 3. The calculated fis-                          Fig. 4(b) shows the simulated size distribution of intragranular
sion density is 3.0  1027 m3. The average size of the simulated                         bubbles in U-Mo fuel at a fission density of 1.5  1027 m3. The
gas bubbles is about 3.2 nm, which is the typical size of intragran-                      average bubble size increases from 3.1 nm to 3.4 nm as the fission
ular gas bubbles observed in irradiated U-7Mo dispersion fuels                            rate increases from 3.0 to 7.0  1020 m3 s1. The peak of the bub-
[46–49]. The calculated gas bubble density is 2:40  1024 m3, in                         ble size distribution profile shifts to the larger size side when the
a good agreement with the intragranular bubble density measured                           fission rate increases. The reason is that the gas bubbles can grow
by experiments [48,49]. Therefore, the current simulations well                           faster by absorption of vacancies with a higher vacancy supersatu-
capture the evolution of intragranular gas bubbles in U-Mo fuel.                          ration or by bubble coalescence with a larger number of bubbles
    Since the intragranular gas bubble induced fuel swelling barely                       due to the higher vacancy production rate. These results are consis-
changes after a certain period of fission density, we simulate the                        tent with the recent experimental results performed in pure Mo
bubble swelling only for a fission density of 1.5  1027 m3 in the                       [46], in which the size of Xe bubbles increases with the increase
following work in order to save the computational time.                                   of ion flux. With a high fission rate, more Xe gas atoms are gener-
                                                                                          ated in the fuel because of its increased production rate, which
4.2. Fission rate effect                                                                  increases the nucleation rate of gas bubbles. As expected, we found
                                                                                          that the gas bubble density increases as fission rate increases. The
  Experiments have shown that the high fission rate can cause                             calculated stable gas bubble density is 2:05  1024 m3, 2:40 
more serious gas bubble swelling than low fission rate [49]. Gas                          1024 m3, and 2:67  1024 m3 for fission rates of 3.0  1020
92                                                  L. Liang et al. / Computational Materials Science 145 (2018) 86–95




                    Fig. 4. Simulated effect of fission rate on (a) intragranular gas bubble swelling and (b) bubble size distribution in U-Mo fuels.




m3 s1, 5  1020 m3 s1, and 7.0  1020 m3 s1 at a fission time                     the swelling caused by the intragranular gas bubbles in the small
of 35 days.                                                                             grain fuel decreases. We note, however, that the intergranular
                                                                                        gas bubble swelling should increase accordingly since more gas
4.3. Grain size effect                                                                  atoms diffuse to the grain boundaries in the small grain size fuel.
                                                                                           Fig. 5(b) shows the effect of initial fuel grain size on the distri-
    The grain size of the polycrystalline U-Mo fuel plays an impor-                     bution of intragranular gas bubble size in the U-Mo fuel up to a fis-
tant role in the evolution of intragranular gas bubbles. Grain                          sion density of 1.5  1027 m3. The peak of the bubble size
boundary acts as sinks for the fission gas atoms, which can assist                      distribution profile shifts to the larger size side when the fuel grain
in suppressing or controlling the gas bubble formation. Therefore,                      size increases. The calculated average bubble size increases from
we study the effect of grain size on the evolution of intragranular                     3.0 nm to 3.5 nm when the grain size increases from 3.2 µm to
gas bubbles.                                                                            10.7 µm. This can be understood by considering the nucleation
    Since the grain boundary is not directly modeled in this work,                      and growth of gas bubbles. In the small grain size fuel, more Xe
the simulation of grain size effect is realized by considering the                      atoms diffuse to the grain boundaries forming intergranular gas
grain boundary density in the reaction term in Eq. (6b). For a sam-                     bubbles and leaving less Xe atoms in the bulk, resulting in fewer
ple with fixed volume, increasing grain size can lead to decreased                      nucleation sites and a lower nucleation rate. Therefore, for a small
density of grain boundaries. Three scenarios with grain boundary                        grain size fuel both the size and the number of gas bubbles
densities of 0.65 µm1, 0.38 µm1, and 0.19 µm1, are considered,                       decrease. The calculated gas bubble density increases from
which correspond respectively to the grain size of 3.2 µm, 5.4                          2:31  1024 m3 to 2:49  1024 m3 with the grain size increasing
µm, and 10.7 µm estimated from an analytical expression [5].                            from 3.2 µm to 10.7 µm.
These grain sizes are within the typical size range observed in U-                         As the initial grain size of a fuel decreases, the intragranular gas
Mo fuels. Fig. 5(a) shows the effect of grain size on the kinetics                      bubbles induced fuel swelling decreases while the intergranular
of intragranular gas bubble swelling. The fuel with the smallest                        gas bubble swelling increases. Since the contribution of intergran-
grains show the lowest swelling. For fuels with reduced grain size,                     ular gas bubble to fuel swelling is usually much larger than intra-
the concentration of gas atoms decreases because of the increased                       granular bubbles, especially at high fission densities [3,48,51],
grain boundary sink reactions. Additionally, the small grains                           reducing the intergranular gas bubble swelling and containing
reduce the diffusion distance of gas atoms from grain interior to                       more intragranular gas bubbles within fuel grains by increasing
grain boundary, thus increasing the probability of Xe atoms sinking                     grain size is an effective way to reduce the overall gas bubble swel-
to the grain boundary to form intergranular gas bubbles. Therefore,                     ling. Another benefit of using large fuel grains is to reduce the




                     Fig. 5. Simulated effect of grain size on (a) intragranular gas bubble swelling and (b) bubble size distribution in U-Mo fuels.
                                                      L. Liang et al. / Computational Materials Science 145 (2018) 86–95                                      93


fission gas release. In a system including bubbles, grains, and grain                     5. Conclusions
boundaries, the Xe gas atoms release from the fuel matrix by single
atom diffusion to grain boundaries, where Xe gas atoms diffuse                                We presented three-dimensional phase-field simulations of the
more slowly inside fuel grain than on grain boundary. Thus, more                          evolution of intragranular gas bubbles in the irradiated U-Mo fuel.
Xe gas atoms release in the small grain fuel because of increased                         The fission-induced microstructural change in U-Mo fuel was sim-
grain boundary densities. These results demonstrate the possibility                       ulated by incorporating several critical processes, radiation-
of tuning bubble morphology and density in irradiated fuel mate-                          induced defects production, vacancy and self-interstitial atom
rials through grain size modification.                                                    recombination, gas atom resolution, and defect sinks at grain
                                                                                          boundaries and dislocations. The current phase-field model can
                                                                                          capture the core behavior of stable intragranular gas bubble forma-
4.4. Effect of rolling induced dislocations                                               tion in U-Mo under irradiation. The simulated gas bubble size dis-
                                                                                          tribution, bubble density, and fuel swelling agree with the
    The rolling process used in the fabrication of U-Mo fuel plate                        experimental data. We systematically studied the effect of fission
can create a high density of the dislocation network, which can                           rate, fuel grain size, and rolling-induced dislocation on the evolu-
have a great impact on the microstructural evolution of a fuel.                           tion of intragranular gas bubbles. High fission rate leads to large
For example, experiments have showed that the bubble super-                               gas bubbles and high bubble density and therefore high swelling.
lattice is missing in the U-Mo dispersion fuel when the initial                           Increasing the initial grain size of a fuel can increase the intragran-
density of dislocation is high although the exact mechanism is                            ular gas bubbles swelling while decrease the intergranular gas
still unclear [50]. Therefore, the rolling process can have a high                        bubble swelling. Considering the significance of intergranular gas
impact on the evolution of gas bubbles.To study the effect of                             bubble swelling especially at high fission densities, the large grains
rolling-induced dislocations on the evolution of intragranular                            are beneficial for reducing the overall bubble swelling. We also
gas bubbles, we introduced three initial dislocation densities                            found that increased dislocation densities because of the rolling
in the U-Mo fuel. These dislocation densities are within the typ-                         process in the fuel fabrication can lead to an increased intragranu-
ical range observed for U-Mo dispersion fuels. Fig. 6(a) shows                            lar gas bubble swelling. Our study shows that the fuel fabrication
that the intragranular gas bubble induced swelling in U-Mo                                and irradiation conditions may be used to control the bubble-
fuels with different initial dislocation densities. At the same fis-                      induced swelling in U-Mo fuel.
sion density of 1.5  1027 m3 ,  the gas bubble swelling increases
from about 2.8% to 5.9% when the initial dislocation density                              Acknowledgments
increases from 0:10  1015 m2 to 1:52  1015 m2. For a fuel
with high initial dislocation density, the defect-dislocation reac-                           This work was supported by the U.S. Department of Energy,
tions consume both vacancies and SIAs, however the SIA concen-                            National Nuclear Security Administration (NNSA), Office of Mate-
tration decreases much faster than the vacancy concentration                              rial Management and Minimization (NA-23) Reactor Conversion
does because of the biased sink strength. As a consequence, the                           Program, and by the U.S. Department of Energy, Office of Science,
recombination rate of vacancy and SIA decreases. More vacancies                           under contract DE-AC02-06CH11357. Use of the Center for Nanos-
flow to voids so both bubble growth and swelling are enhanced                             cale Materials, an Office of Science user facility, was supported by
at high dislocation density compared with the ones at low initial                         the U.S. Department of Energy, Office of Science, Office of Basic
dislocation density [52]. As shown in Fig. 6(b), at a fission den-                        Energy Sciences, under Contract No. DE-AC02-06CH11357. We also
sity of 1.5  1027 m3, the average bubble size in U-Mo fuel                              acknowledge use of Blues, a high-performance computing cluster
increases from 3.1 nm to 3.4 nm and the peak of gas bubble dis-                           operated by the Laboratory Computing Resource Center at Argonne
tribution also shifts to the larger bubble size side as the initial                       National Laboratory. In addition, this manuscript benefited from
dislocation    density        increases      from      0:10  1015      m2      to       insightful discussion with Dr. Jeff Rest.
          15    2
1:52  10      m     . The gas bubble density also increases from
1:78  1024 m3 to 2:85  1024 m3 with increasing initial dislo-                         Appendix A. Derivation of the free energy of a gas bubble
cation density. Therefore, the rolling process during fuel fabrica-
tion can play an important role in controlling the gas bubble                                 The general expression of the Gibbs free energy of a gas bubble
size and density in U-Mo fuel.                                                            is expressed as




                   Fig. 6. Simulated effect of dislocation density on (a) intragranular gas bubble swelling and (b) bubble size distribution in U-Mo fuels.
94                                                      L. Liang et al. / Computational Materials Science 145 (2018) 86–95

                        Z p
                                                                                            cbX þ cV þ cI þ cm – 1:0                                                                 ðA:12Þ
GðpÞ ¼ Gðp0 Þ þ                 V b dp;                                          ðA:1Þ
                           p0
                                                                                               We have to relate these two definitions in order to make them
where p is the pressure, Vb is the gas bubble volume, and G(p0) is the                      consistent with each other. The definition of Xe concentration in
Gibbs free energy at the reference state p0.                                                the gas bubble can be written as
   The state of equation for a nonideal gas can be expressed as
                                                                                                    n      n       n 1               1
                                                                                            cbX ¼      ¼         ¼             ¼ cX        :                                         ðA:13Þ
pV b                                                                                                V b NV V site Nsite V site      V site
      ¼ 1 þ B0 p þ C 0 p2 þ    ;                                              ðA:2Þ
nkB T
                                                                                            where Nv is the number of vacancy inside the bubble, and Vsite is the
where B0 and C 0 are constants, n is the number of gas atoms, and kB                        volume of the lattice site. Next, for each bubble the number of
is a Boltzmann constant, T is the temperature.                                              vacancy equals the number of sites, and the lattice parameter of
    For a nonideal gas, the Gibbs free energy is                                            U-7Mo is assumed to be 3.43 1010 m. Thus,
                          
                        Z p                       
                            1                                                                           1                 1
GðpÞ ¼ Gðp0 Þ þ     nkB T     þ B0 þ C 0 p þ    dp                                       cbX ¼ cX          ¼ cX                   :                                               ðA:14Þ
                            p                                                                          V site                      3
                 p0
                                                                                                                 ð3:43  1010 Þ
                          p
     ¼ Gðp0 Þ þ nkB T ln þ B0 ðp  p0 Þ þ C 0 ðp2  p20 Þ þ    :              ðA:3Þ         The reference state is consistent with the state that we calculate
                         p0
                                                                                            for the formation energy of defects in DFT calculations. Thus, the
   We assume that the state of equation of a nonideal gas has the                           reference pressure p0 is also derived at the same state,
form,
                                                                                                        c X V 1 kB T
pV b                                                                                        p0 ¼             site
                                                                                                                             ;                                                       ðA:15Þ
      ¼ 1 þ B0 p:                                                                ðA:4Þ              1  B0 cX V 1site kB T
nkB T
  We can rewrite it by defining the Xe concentration in the gas                             where B0 is a fitting constant and can be fitted from the experimen-
bubble as cbX ¼ n=V b ,                                                                     tal data. In this paper, we use the data derived from the equation of
                                                                                            state from Xiao et al.’s work [53]. The equation of state is
         cbX kB T                                                                                            
p¼                    :                                                          ðA:5Þ           RT        c      a
      1  B0 cbX kB T                                                                       p¼       1þ          2;                                                                 ðA:16Þ
                                                                                                 Vb     Vb  b   Vb
     Then, the free energy of the gas bubble is expressed as
                                                                                            where constant a, b, and c are 259,780 J cm3/mol2, 23.9276 cm3/
                                            kB T
                                                  cbX kB Tlnð1  B0 cbX kB TÞ
                               b
f ðpÞ ¼ f ðp0 Þ þ cbX kB TlncX þ cbX kB Tln                                                 mol, and 55.6583 cm3/mol, respectively. We use the Van de Waals
                                             p0
                                                                                          state equation to fit Eq. (A.16) in order to obtain the constant B0 .
                           cbX kB T                                                         The fitted result gives B0 =kB T ¼ 23:9687  106 m3/mol (see Fig. A1).
        þ cbX kB TB0                    p 0 :                                   ðA:6Þ
                       1  B0 cbX kB T                                                         Therefore, based on the Xe atoms in the DFT calculation cell, the
     The reduced Van de Waals equation is                                                   reference pressure is calculated as follows.

pðV b  nbÞ ¼ nkB T:                                                             ðA:7Þ                  c X V 1 kB T
                                                                                            p0 ¼             site
                                                                                                                             ¼ 6:53  106 Pa                                         ðA:17Þ
                                                          0                                         1  B0 cX V 1site kB T
   Thus, the Van de Waals constant is b ¼ B kB T. The free energy
equation can be rewritten as                                                                                                     2                                                          3
                                                                                                                                         c X V 1 kB T
                                                                                                                                               site                                     !
                            b              kB T                    b                                                  1          6         0
                                                                                                                                       1B cX V 1 kB T
                                                                                                                                                                        1
                                                                                                                                                                   cX V site kB T         7
f ðpÞ ¼ cbX l0 þ cbX kB TlncX þ cbX kB Tln       cbX kB Tlnð1  bcX Þ                      f ðpÞ ¼ f ðp0 Þ þ cX            kB T 6                       þ B0                         p0 7
                                                                                                                                 4ln
                                                                                                                                               site
                                            p0                                                                       V site                    p0               1  B0 cX V 1 kB T        5
                                !                                                                                                                                           site
                  cbX kB T
        þ cbX b           b
                             p0 :                                               ðA:8Þ
                                                                                                                                                                                     ðA:18Þ
                 1  bcX
   To calculate the p0 inside the bubble, we first clarify the defini-                      plot in Fig. A2 the free energy as a function of cX .
tion of the gas concentration inside the matrix and gas bubble.                                The equilibrium concentration is cX ¼ 0:017, which corresponds
                                                                                            to the pressure 2:79  106 Pa.
     (1) In the matrix, the Xe, vacancy, and SIA atoms can occupy
         only one lattice site. Thus the concentration at every site sat-
         isfies the condition

         cX þ cV þ cI þ cm ¼ 1:0:                                                ðA:9Þ
     The definition of the Xe concentration in the matrix is
                 NXe
         cX ¼          :                                                     ðA:10Þ
                 Nsite
     (2) In the bubble, although the vacancy and interstitial atoms
         keep their definition as in the matrix, the Xe concentration
         is different. Based on the definition of the concentration in
         the state of equation, the Xe concentration in the bubble is
                 n
         cbX ¼      :                                                        ðA:11Þ
                 Vb
   Therefore, the condition (A.9) is not satisfied at every site inside                     Fig. A1. Comparison of fitting curve with the original data. The original data are
the gas bubble and                                                                          taken from [40].
                                                           L. Liang et al. / Computational Materials Science 145 (2018) 86–95                                                           95


                                                                                               [18] S. Hu, C.H. Henager Jr., H.L. Heinisch, M. Stan, M.I. Baskes, S.M. Valone, J. Nucl.
                                                                                                    Mater. 392 (2009) 292–300.
                                                                                               [19] S. Hu, Y. Li, X. Sun, F. Gao, R. Devanathan, C.H. Henager Jr., M.A. Khaleel, Int. J.
                                                                                                    Mater. Res. 101 (2010) 515–522.
                                                                                               [20] Y. Li, S. Hu, R. Montgomery, F. Gao, X. Sun, Nucl. Instrum. Meth. Phys. Res. Sect.
                                                                                                    B (Beam Interactions with Materials and Atoms) 303 (2013) 62–67.
                                                                                               [21] P.C. Millett, A. El-Azab, D. Wolf, Comput. Mater. Sci. 50 (2011) 960–970.
                                                                                               [22] P.C. Millett, M.R. Tonks, S.B. Biner, L. Zhang, K. Chockalingam, Y. Zhang, J. Nucl.
                                                                                                    Mater. 425 (2012) 130–135.
                                                                                               [23] P.C. Millett, M. Tonks, S.B. Biner, J. Appl. Phys. 111 (2012).
                                                                                               [24] S. Hu, A.M. Casella, C.A. Lavender, D.J. Senor, D.E. Burkes, J. Nucl. Mater. 462
                                                                                                    (2015) 64–76.
                                                                                               [25] L. Liang, Z.G. Mei, Y.S. Kim, B. Ye, G. Hofman, M. Anitescu, A.M. Yacout, Comput.
                                                                                                    Mater. Sci. 124 (2016) 228–237.
                                                                                               [26] S.Y. Hu, D.E. Burkes, C.A. Lavender, D.J. Senor, W. Setyawan, Z.J. Xu, J. Nucl.
                                                                                                    Mater. 479 (2016) 202–215.
                                                                                               [27] J. Rest, G.L. Hofman, ANL/ET/PP–84776, 1994.
                                                                                               [28] J.A. Turnbull, R.M. Cornell, J. Nucl. Mater. 41 (1971) 156–160.
                                                                                               [29] J.A. Turnbull, J. Nucl. Mater. 38 (1971) 203–212.
                                                                                               [30] M.H. Wood, J. Nucl. Mater. 82 (1979) 264–270.
                                                                                               [31] J. Rest, J. Nucl. Mater. 321 (2003) 305–312.
Fig. A2. Bubble free energy as a function of Xe concentration. The insert figure               [32] R.S. Nelson, J. Nucl. Mater. 25 (1968) 227–232.
                                                                                               [33] J. Rest, A.W. Cronenberg, J. Nucl. Mater. 150 (1987) 203–225.
shows the enlargement of dash circle areas.
                                                                                               [34] J. Rest, G.L. Hofman, J. Nucl. Mater. 210 (1994) 187–202.
                                                                                               [35] A.G. Khachaturyan, Theory of Structural Transformations in Solids, Wiley, New
                                                                                                    York, 1983.
References                                                                                     [36] S.Y. Hu, L.Q. Chen, Acta Mater. 49 (2001) 1879–1890.
                                                                                               [37] L. Liang, Z.-G. Mei, A.M. Yacout, Comput. Mater. Sci. 138 (2017) 16–26.
 [1] J.L. Snelgrove, G.L. Hofman, M.K. Meyer, C.L. Trybus, T.C. Wiencek, Nucl. Eng.            [38] J.P. Simmons, C. Shen, Y. Wang, Scripta Mater. 43 (2000) 935–942.
     Des. 178 (1997) 119–126.                                                                  [39] Z.-G. Mei, L. Liang, Y.S. Kim, T. Wiencek, E. O’Hare, A.M. Yacout, G. Hofman, M.
 [2] D.D. Keiser, S.L. Hayes, M.K. Meyer, C.R. Clark, Jom-J. Miner. Metals Mater. Soc.              Anitescu, J. Nucl. Mater. 473 (2016) 300–308.
     55 (2003) 55–58.                                                                          [40] J. Rest, J. Nucl. Mater. 402 (2010) 179–185.
 [3] Y.S. Kim, G.L. Hofman, J. Nucl. Mater. 419 (2011) 291–301.                                [41] J. Rest, J. Nucl. Mater. 407 (2010) 55–58.
 [4] G.L. Hofman, Y.S. Kim, Nucl. Eng. Technol. 37 (2005) 299–308.                             [42] J. Spino, J. Rest, W. Goll, C.T. Walker, J. Nucl. Mater. 346 (2005) 131–144.
 [5] Y.S. Kim, G.L. Hofman, J. Rest, Argonne National Laboratory, Argonne National             [43] L. Pagano, A.T. Motta, R.C. Birtcher, J. Nucl. Mater. 244 (1997) 295–304.
     Laboratory, 2008.                                                                         [44] L.Q. Chen, J. Shen, Comput. Phys. Commun. 108 (1998) 147–158.
 [6] J. Rest, J. Nucl. Mater. 207 (1993) 192–204.                                              [45] Y.B. Miao, K. Mo, B. Ye, L. Jamison, Z.G. Mei, J. Gan, B. Miller, J. Madden, J.S. Park,
 [7] D.R. Olander, D. Wongsawaeng, J. Nucl. Mater. 354 (2006) 94–109.                               J. Almer, S. Bhattacharya, Y.S. Kim, G.L. Hofman, A.M. Yacout, Scripta Mater.
 [8] S. Hu, C.H. Henager Jr., J. Nucl. Mater. 394 (2009) 155–159.                                   114 (2016) 146–150.
 [9] P.C. Millett, A. El-Azab, S. Rokkam, M. Tonks, D. Wolf, Comput. Mater. Sci. 50            [46] D. Yun, M.A. Kirk, P.M. Baldo, J. Rest, A.M. Yacout, Z.Z. Insepov, J. Nucl. Mater.
     (2011) 949–959.                                                                                437 (2013) 240–249.
[10] A. El-Azab, K. Ahmed, S. Rokkam, T. Hochrainer, Curr. Opin. Solid State Mater.            [47] B.D. Miller, University of Wisconsin-Madison, University of Wisconsin-
     Sci. 18 (2014) 90–98.                                                                          Madison, 2010.
[11] T. Hochrainer, A. El-Azab, Philos. Mag. 95 (2015) 948–972.                                [48] B.D. Miller, J. Gan, D.D. Keiser Jr., A.B. Robinson, J.F. Jue, J.W. Madden, P.G.
[12] S.Y. Hu, C.H. Henager Jr., Acta Mater. 58 (2010) 3230–3237.                                    Medvedev, J. Nucl. Mater. 458 (2015) 115–121.
[13] Y. Li, S. Hu, X. Sun, F. Gao, C.H. Henager Jr., M. Khaleel, J. Nucl. Mater. 407           [49] J. Gan, D.D. Keiser, B.D. Miller, A.B. Robinson, J.F. Jue, P. Medvedev, D.M. Wachs,
     (2010) 119–125.                                                                                J. Nucl. Mater. 424 (2012) 43–50.
[14] L. Zhang, M.R. Tonks, P.C. Millett, Y. Zhang, K. Chockalingam, B. Biner, Comput.          [50] J. Gan, B.D. Miller, D.D. Keiser, A.B. Robinson, J.W. Madden, P.G. Medvedev, D.
     Mater. Sci. 56 (2012) 161–165.                                                                 M. Wachs, J. Nucl. Mater. 454 (2014) 434–445.
[15] Y. Li, S. Hu, C.H. Henager Jr., H. Deng, F. Gao, X. Sun, M.A. Khaleel, J. Nucl. Mater.    [51] J. Gan, D.D. Keiser, B.D. Miller, A.B. Robinson, D.M. Wachs, M.K. Meyer, J. Nucl.
     427 (2012) 259–267.                                                                            Mater. 464 (2015) 1–5.
[16] S. Hu, C.H. Henager Jr., Y. Li, F. Gao, X. Sun, M.A. Khaleel, Model. Simul. Mater.        [52] J. Rest, G.L. Hofman, I.I. Konovalov, A.A. Maslov, ANL/ET/CP-97352, 1998.
     Sci. Eng. 20 (2012) 015011.                                                               [53] H.-X. Xiao, C.-S. Long, Chinese Phys. B 23 (2014) 020502.
[17] S.B. Biner, S.Y. Hu, Acta Mater. 57 (2009) 2088–2097.
