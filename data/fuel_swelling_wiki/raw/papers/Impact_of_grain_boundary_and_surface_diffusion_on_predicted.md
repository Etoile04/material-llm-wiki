# Impact of grain boundary and surface diffusion on predicted fission gas bubble behavior and release in UO2 fuel

---

                                                                   Journal of Nuclear Materials 594 (2024) 155032


                                                                      Contents lists available at ScienceDirect


                                                               Journal of Nuclear Materials
                                                           journal homepage: www.elsevier.com/locate/jnucmat




Impact of grain boundary and surface diﬀusion on predicted ﬁssion gas
bubble behavior and release in UO2 fuel
Md Ali Muntaha a , Sourav Chatterjee a , Sophie Blondel b , Larry Aagesen c , David Andersson d ,
Brian D. Wirth b,e , Michael R. Tonks a,∗
a
  Department of Materials Science and Engineering, University of Florida, Gainesville, FL 32611, USA
b
  Department of Nuclear Engineering, University of Tennessee, Knoxville, TN, 37996, USA
c
  Computational Mechanics and Materials, Idaho National Laboratory, Idaho Falls, ID 83415, USA
d
  MST-8, Los Alamos National Laboratory, Los Alamos, NM, 87545, USA
e
  Oak Ridge National Laboratory, Oak Ridge, TN, 37830, USA




A R T I C L E             I N F O                           A B S T R A C T

Keywords:                                                   In this work, we quantify the impact of grain boundary (GB) and surface diﬀusion on ﬁssion gas bubble evolution
Phase ﬁeld modeling                                         and ﬁssion gas release in UO2 nuclear fuel using simulations with a hybrid phase ﬁeld/cluster dynamics model.
MOOSE-Xolotl coupling                                       We begin with a comprehensive literature review of uranium vacancy and xenon atom diﬀusivity in UO2 through
Grain boundary and surface diﬀusion
                                                            the bulk, along GBs, and along surfaces. In our model we represent fast GB and surface diﬀusion using a
Fission gas release
                                                            heterogeneous diﬀusivity that is a function of the order parameters that represent bubbles and grains. We ﬁnd
                                                            that the GB diﬀusivity directly impacts the rate of gas release via GB transport, and that the GB diﬀusivity is
                                                            likely below 104 times the lower value from Olander and van Uﬀelen (2001). We also ﬁnd that the surface
                                                            diﬀusivity impacts bubble coalescence and mobility, and that the bubble surface diﬀusivity is likely below 10−4
                                                            times the value from Zhou and Olander (1984).




1. Introduction                                                                                    the third stage, gas ﬂows through interconnected TJ tunnels to release
                                                                                                   at free surfaces. Experimental evidence indicates that all three stages oc-
    In uranium dioxide (UO2 ) fuel pellets for light water reactors, ﬁs-                           cur concurrently, with signiﬁcant overlap between them [5]. However,
sion gases, primarily xenon (Xe) and krypton (Kr), are produced as                                 ﬁssion gas bubble evolution has never been directly observed during
byproducts of uranium nuclear ﬁssion. These ﬁssion gas atoms ex-                                   reactor operation so there are still many aspects of it that are not un-
hibit exceptionally low solubility within UO2 grains [1,2], resulting in                           derstood.
the formation of small intra-granular bubbles and larger intergranu-                                   Mesoscale simulations of ﬁssion gas bubbles provide an alternative
lar bubbles at grain boundaries (GBs) and triple junctions (TJs) [3,4].                            means of investigating their evolution, and the phase ﬁeld method has
The intergranular bubbles at GBs and TJs are of particular concern, as                             emerged as the most popular approach for such simulations [6–9].
their growth and interconnection create a percolated pathway for ﬁs-                               One limitation of the phase ﬁeld method is that it is too computa-
sion gases to be released from the fuel pellet to the fuel rod gap and                             tionally expensive to resolve the small intragranular bubbles and GB
plenum. There, the ﬁssion gas directly impacts fuel performance by in-                             bubble evolution in the same simulation. A recently developed model
creasing the plenum pressure and decreasing heat transport through the                             [10] overcame this limitation by coupling a phase ﬁeld model repre-
gap.                                                                                               senting GBs and intergranular bubble evolution with spatially resolved
    Fission gas release typically results from a three-stage process [3].                          cluster dynamics representing ﬁssion gas generation, diﬀusion, and in-
In the ﬁrst stage, gas atoms are generated within the bulk and are ei-                             tragranular bubble trapping. However, the original implementation of
ther trapped by intra-granular bubbles or diﬀuse to GBs. In the second                             this hybrid model did not consider fast ﬁssion gas diﬀusion along GBs
stage, GB bubbles nucleate, grow, and coalesce until interconnected                                and bubble surfaces, and neither has most other previous ﬁssion gas
bubble networks allow gas to ﬂow from GB bubbles to TJ tunnels. In                                 bubble phase ﬁeld models [6–8,11–15]. In addition, it simulated an in-


    * Corresponding author.
      E-mail address: michael.tonks@uﬂ.edu (M.R. Tonks).

https://doi.org/10.1016/j.jnucmat.2024.155032
Received 19 June 2023; Received in revised form 15 January 2024; Accepted 15 March 2024
Available online 21 March 2024
0022-3115/© 2024 Elsevier B.V. All rights reserved.
M.A. Muntaha, S. Chatterjee, S. Blondel et al.                                                                      Journal of Nuclear Materials 594 (2024) 155032


terior region of the fuel without a free surface, so it could not represent       well with the data surveyed by Turnbull. We use the Turnbull values as
ﬁssion gas release.                                                               a reference for the Xe GB diﬀusivity.
    In this work, we investigate the impact of fast diﬀusion along GBs                In general, defect diﬀusion is faster along GBs than in the bulk, due
and bubble surfaces on ﬁssion gas release using 2D and 3D simulations             to the additional free volume. Values for the GB diﬀusivity of U vacan-
with a modiﬁed version of the hybrid model from Kim et al. [10]. We               cies, shown in Fig. 1c, were again converted from U self diﬀusivities
modify it by adding fast GB and bubble surface diﬀusion and a free                measured from experiments and taken from molecular dynamics sim-
surface for ﬁssion gas release. The outline of this paper is as follows:          ulations. The GB U self diﬀusivity values come from data obtained in
ﬁrst, we provide a detailed literature review of the vacancy and ﬁssion           the 1960s, from Alcock et al. [18] and Yajima et al. [19], from 2000
gas diﬀusivities values for UO2 grains, GBs, and free surfaces; then, we          by Sabioni et al. [28], and from 2009 by Vincent et al. [29]. Molec-
summarize the hybrid model and discuss the enhancements we have                   ular dynamics simulations by Galvin et al. [30] were used to directly
made; ﬁnally, we present and discuss our 2D and 3D simulation results.            calculate the U vacancy GB diﬀusivity in UO2 . Liu et al. [31] used the
                                                                                  same approach as Galvin et al. to calculate diﬀusivities for twist, tilt,
2. Survey of U vacancy and gas atom diﬀusivity values in UO𝟐                      and random GBs. These calculated values fall within the range of the
                                                                                  experimental values. The majority of these sources report GB diﬀusiv-
                                                                                  ity data ranging from 10−15 m2 /s to 10−8 m2 /s at 𝑇 = 1600 K, which
    The diﬀusivities of U vacancies and gas atoms have a direct impact
                                                                                  is approximately four to eight orders of magnitude greater than that of
on the ﬁssion gas release behavior in UO2 . Thus, their values have been
                                                                                  the bulk U vacancy diﬀusivity from Auskern et al. [16].
measured in various experiments and calculated using simulation ap-
                                                                                      Unfortunately, there are very few data on the Xe GB diﬀusivity in
proaches. However, there is a large amount of scatter and uncertainty
                                                                                  UO2 . It was measured by Olander and Van Uﬀelen [32] and has been
in these values. In Fig. 1, we compare the bulk, GB, and surface dif-
                                                                                  calculated by molecular dynamics simulations by Liu et al. [31], as
fusivities from the literature for temperatures ranging from 1000 K to
                                                                                  shown in Fig. 1d. Olander and Van Uﬀelen [32] used trace-irradiated
2200 K. Note that we consider radiation enhancement for bulk Xe diﬀu-
                                                                                  UO2 samples to measure Xe transport and estimate the GB diﬀusivity.
sion but that we assume that radiation does not enhance GB and surface
                                                                                  However, due to the scatter in the bulk Xe diﬀusivity measurements,
diﬀusion. We assume this because diﬀusion along these interfaces is al-
                                                                                  they estimated two GB diﬀusivities, one using the upper bulk diﬀusivity
ready accelerated due to their defected structure and that additional
                                                                                  data [26], and one using the lower bulk diﬀusivity data [25]. Liu et al.
defects due to radiation are not likely to add signiﬁcant additional ac-
                                                                                  [31] computed GB data for twist, tilt, and random GBs using MD simula-
celeration at our temperatures of interest.
                                                                                  tions. There are large diﬀerences between the measured and simulated
    The values for the bulk diﬀusivity of U vacancies in UO2 , shown in           values, though the migration energy from the simulations is similar to
Fig. 1a, were obtained either by converting experimentally-measured               that from the upper measured values. The GB diﬀusivity ranges from
values for U self diﬀusion by dividing by their reported vacancy concen-          10−16 m2 /s to 10−9 m2 /s at 𝑇 = 1600 K. When compared to bulk dif-
tration or by atomic-scale simulations. The measurements by Auskern               fusivity data from Turnbull [24], xenon gas diﬀusivity at the GB was
and Belle [16], Schmitz and Lindner [17], Alcock et al. [18] and Yajima           found to be three to eight orders of magnitude higher.
et al. [19] were performed in the 1960s. Matzke [20] measured the dif-                U vacancy diﬀusion is also accelerated at surfaces. Values for U
fusivity in 1987, and obtained a value signiﬁcantly higher than all other         Vacancy diﬀusivity along surfaces were again converted from U self
values. In 1998, Sabioni et al. [21] used more modern approaches and              diﬀusivity values, and are shown in Fig. 1e. Numerous researchers have
obtained values very close to those from Schmitz and Lindner [17].                reported U vacancy diﬀusivity data along surfaces. Amato et al. [33],
Matthews et al. [22] used molecular dynamics simulations to calculate             Reynolds [34], Henney and Jones [35], and Maiya [36] employed mass
the vacancy diﬀusivity, resulting in an activation energy similar to that         transfer techniques (GB grooving and single scratch decay). Marlowe
from Schmitz and Linder [17] and Sabioni et al. [21] but with a smaller           and Kaznoﬀ [37] and Zhou and Olander [38] relied on tracer tech-
prefactor. Overall, there is a large range of values; for a reference tem-        niques. However, tracers can migrate from the surface into the interior
perature 𝑇 = 1600 K, the values range from 10−20 m2 /s to 10−13 m2 /s.            and it was suggested that this could be resulting in large underestima-
If the value from Matzke is eliminated as an outlier, the values still            tions of the surface diﬀusivities [39,40]. Ultimately, Zhou and Olander
vary by four orders of magnitude. This large variation is potentially due         [38] developed an approach that potentially avoids this issue. However,
to the strong impact of non-stoichiometry and oxygen partial pressure             the value from Zhou and Olander is much higher than the values from
on the U vacancy diﬀusivity [23] and to uncertainty in the reported               mass transfer techniques. At 𝑇 = 1600 K, the mass transfer techniques
vacancy concentrations used to convert from self diﬀusivities. Sabioni            give a value that is six orders of magnitude larger than the bulk U va-
et al. [21] observed a substantial eﬀect of stoichiometry on uranium              cancy diﬀusivity from Auskern et al. [16] and the Zhou and Olander
vacancy concentration. Their ﬁndings showed that the concentration                value is about twelve orders of magnitude larger.
for hypostoichiometric cases was around six orders of magnitude lower                 Due to the large variation in the surface and GB diﬀusivity values, it
compared to the stoichiometric case. For our calculation of uranium va-           is important to understand their impact on the ﬁssion gas behavior. Sim-
cancy diﬀusivity, we considered the stoichiometric concentration. The             ulations of the ﬁssion gas behavior that includes bulk, GB, and surface
values from Auskern et al. [16] fall in the middle of the range if we ne-         diﬀusion provide a useful means of studying these impacts. Therefore,
glect the value from Matzke, so we use it as a reference for the GB and           we conduct a parametric study in Section 5 using the hybrid model de-
surface diﬀusivity values.                                                        veloped by Kim et al. [10] to examine the inﬂuence of GB and surface
    The values for Xe diﬀusivity in single crystal UO2 , shown in Fig. 1b,        diﬀusivity on the microstructural evolution of ﬁssion gas bubbles and
also come from experimental measurement and from simulations. Turn-               ﬁssion gas release in UO2 nuclear fuel.
bull [24] surveyed the available experimental data in 1982 and de-
veloped an overall ﬁt that includes intrinsic and radiation-enhanced              3. Model formulation
diﬀusion. The scatter of the data, shown in gray in Fig. 1b, is roughly
plus or minus one order of magnitude and is much less than the scatter                Our study is built upon the ﬁssion gas hybrid model [10] that pre-
in the U vacancy data. The intrinsic diﬀusivity measured by Davies and            dicts the evolution of both small intragranular bubbles and larger in-
Long [25] was used in Turnbull’s ﬁt, which varies signiﬁcantly from               tergranular bubbles, as well as GB migration. This is accomplished by
the intrinsic diﬀusivity value from Miekeley and Felix [26]. Matthews             coupling a spatially-resolved cluster dynamics model, implemented in
et al. [27] used a combination of density functional theory, molecular            the Xolotl code [41], with a phase ﬁeld model, implemented using the
dynamics, and cluster dynamics to obtain Xe diﬀusivity values that also           MARMOT code [42]. The cluster dynamics model in Xolotl represents
include intrinsic and radiation-enhanced diﬀusion and they compare                the generation of Xe gas atoms due to ﬁssion reactions, their diﬀu-

                                                                              2
M.A. Muntaha, S. Chatterjee, S. Blondel et al.                                                                          Journal of Nuclear Materials 594 (2024) 155032




Fig. 1. Diﬀusivity values for U vacancies and gas atoms in UO2 from the literature. Bulk values through the crystal lattice are shown in (a) and (b), along GBs in
(c) and (d), and vacancy diﬀusion along surfaces in (e). Experimental values are shown with solid lines, simulation values with dashed lines, and reference bulk
diﬀusivities are shown with black diamonds. The reference numbers for the sources of the data are shown in the legends.


sion through the fuel matrix, gas atom clustering, and re-solution of gas               We have made several enhancements to the hybrid model to enable
atoms within the grains due to radiation and ﬁssion fragment damage.                its use to investigate the impact of fast GB and bubble surface diﬀu-
The phase ﬁeld model in MARMOT includes GB evolution, intergran-                    sion on ﬁssion gas release. The coupling between MARMOT and Xolotl
ular bubble growth and coalescence, bubble migration, and gas atom                  is unchanged, but we made changes to the cluster dynamics model in
diﬀusion along grain boundaries. At each time step, MARMOT passes                   Xolotl and the phase ﬁeld model in MARMOT. In Xolotl, we modiﬁed
                                                                                    the boundary conditions to represent gas release from grains at free
updated GB and intergranular bubble surface positions to Xolotl and
                                                                                    surfaces and we modiﬁed the re-solution model. The cluster dynamics
Xolotl passes the rate of gas arriving at these interfaces into MARMOT.
                                                                                    model is brieﬂy summarized in Section 3.1 and then we discuss these
The codes are coupled using capabilities from the MOOSE framework                   changes. In MARMOT, we changed the diﬀusivities of U vacancies and
that MARMOT is based on [43]. The computational cost of coupling the                gas atoms along grain boundaries and at bubble surfaces to represent
codes is small in 2D simulations and the hybrid model scales well on                fast GB and surface diﬀusion, and we modiﬁed the boundary conditions
multiple processors. A more complete description of the hybrid model                to represent gas release from free surfaces. We summarize the phase
was provided by Kim et al. [10].                                                    ﬁeld model and discuss the changes in Section 3.2.

                                                                                3
M.A. Muntaha, S. Chatterjee, S. Blondel et al.                                                                            Journal of Nuclear Materials 594 (2024) 155032


3.1. Cluster dynamics model summary and changes                                   have been shown to have a large impact on the overall diﬀusion rates
                                                                                  [22,27]. These variables evolve according to partial diﬀerential equa-
   For the hybrid ﬁssion gas model, the cluster dynamics model in                 tions to minimize the overall grand potential of the system.
Xolotl is used to model the transport and clustering of ﬁssion gas atoms              The model uses the grand potential formulation originally presented
within the UO2 matrix. To simplify the model, it assumes that all ﬁs-             by Plapp [48] and it is described in detail in Kim et al. [10] and Aagesen
sion gas atoms are Xe, the most common gaseous ﬁssion product. It                 et al. [8]. Here, we provide a brief overview of the equations solved in
simpliﬁes the model by not directly representing vacancies but assum-             the model. The order parameters describing the grains and bubbles are
ing vacancies are present with Xe atoms and clusters. The formation               evolved according to the Allen-Cahn equation
and evolution of intragranular bubbles is represented by modeling the
                                                                                  𝜕𝜂𝑖      𝛿Ω
evolution of the concentrations of Xe atom clusters using the expression              = −𝐿     , with 𝑖 = 0, 1, ..., 𝑛,                                             (3)
                                                                                  𝜕𝑡       𝛿𝜂𝑖
𝜕𝐶𝑛
     = 𝐷𝑛 ∇2 𝐶𝑛 + 𝐹̇ 𝑦𝑛 − 𝑄(𝐶𝑛 ),                                  (1)            where 𝐿 is the order parameter mobility, Ω is the grand potential, and
 𝜕𝑡                                                                                𝛿
                                                                                     represents a variational derivative. Ω is written as function of the
where 𝐶𝑛 is the concentration of a cluster containing 𝑛 Xe atoms and              𝛿𝜂𝑖
                                                                                  local grand potential density [49]
𝐷𝑛 is the diﬀusion coeﬃcient of the cluster. The Xe production is a
function of the ﬁssion rate density 𝐹̇ and the ﬁssion yield 𝑦𝑛 of the                  ( (𝑁 (       ) 𝑁 𝑁               )
                                                                                          ∑ 𝜂𝑖4 𝜂𝑖2    ∑ ∑ 𝛾𝑖𝑗        1
cluster per ﬁssion. 𝑄(𝐶𝑛 ) describes the various reactions that impact            Ω=    𝑚       −    +          𝜂 𝜂 +
                                                                                                                 2 2

the cluster concentration. Xolotl solves the coupled reaction-diﬀusion
                                                                                     ∫
                                                                                          𝑖=0
                                                                                              4   2    𝑖=0 𝑗≠𝑖
                                                                                                               2 𝑖 𝑗 4
                                                                                         𝑉
equations using the ﬁnite diﬀerence method with implicit time integra-                                                 )                                            (4)
                                                                                              𝑁
tion, where the PETSc library [44] is used to solve the nonlinear system                   𝜅∑
                                                                                         +       |∇𝜂𝑖 | + ℎ𝑚 𝜔𝑚 + ℎ𝑏 𝜔𝑏 𝑑𝑉 ,
                                                                                                       2
of equations.                                                                              2 𝑖=0
    We assume that the single Xe atom is the only mobile cluster such
                                                                                  where 𝑚 is the free energy barrier coeﬃcient, 𝛾𝑖𝑗 is a model parameter
that 𝐷𝑛>1 = 0, based on the work performed by Perriot et al. [45] where
                                                                                  that inﬂuences the shape of the diﬀuse interface and intergranular bub-
migration energies were computed with empirical potential methods
                                                                                  ble contact angles, 𝜅 is the gradient energy coeﬃcient, ℎ𝑚 and ℎ𝑏 are
and the energy barriers were 1.5 eV and 2.1 eV higher for clusters of
                                                                                  switching functions that control matrix and bubble properties, respec-
two and three Xe atoms, respectively, than for a single Xe atom. We
                                                                                  tively, and 𝜔𝑚 and 𝜔𝑏 are the grand potential densities of the matrix
also assume that ﬁssions only yield single Xe atoms, such that 𝑦𝑛>1 = 0.
                                                                                  and bubble phases, respectively. The switching functions are deﬁned as
Three types of reactions are considered according to
                                                                                  [50]:
𝑄(𝐶𝑛 ) = (𝑘𝑛 𝐶𝑛 𝐶1 − 𝑘𝑛−1 𝐶𝑛−1 𝐶1 ) + (𝑘𝑒𝑚𝑖𝑡    𝑒𝑚𝑖𝑡
                                        𝑛 𝐶𝑛 − 𝑘𝑛+1 𝐶𝑛+1 )                                   ∑𝑁
                                                                                              𝑖=1 𝜂𝑖
                                                                                                   2
                                                                       (2)
           + (𝑘𝑟𝑒𝑠𝑜    𝑟𝑒𝑠𝑜                                                       ℎ 𝑚 = ∑𝑁                                                                          (5)
               𝑛 𝐶𝑛 − 𝑘𝑛+1 𝐶𝑛+1 )
                                                                                              𝑖=0 𝜂𝑖
                                                                                                   2

where the ﬁrst two terms represent absorption of a Xe atom to form
                                                                                  ℎ𝑏 = 1 − ℎ𝑚 .                                                                     (6)
a larger cluster Xe1 + Xe𝑛 → Xe𝑛+1 , the second two terms represent
Xe atom emission Xe𝑛 → Xe1 + Xe𝑛−1 where the rates are governed                   The grand potential densities of the matrix and bubble phase are given
by the binding energies, and the last two terms represent Xe atom re-             by [48,49]:
solution that is described by the same reaction equation as emission.
The reaction rate expressions for absorption and emission are described           𝜔𝑚 = 𝑓𝑚,𝑐ℎ𝑒𝑚 − 𝜇𝑔 𝜌𝑔 − 𝜇𝑣 𝜌𝑣 ,                                                    (7)
by Kim et al. [10].
                                                                                  𝜔𝑏 = 𝑓𝑏,𝑐ℎ𝑒𝑚 − 𝜇𝑔 𝜌𝑔 − 𝜇𝑣 𝜌𝑣 ,                                                    (8)
    Previously [10], re-solution was described using the heterogeneous
re-solution model [46] where a xenon bubble ejects an individual atom             where 𝑓𝑚,𝑐ℎ𝑒𝑚 and 𝑓𝑏,𝑐ℎ𝑒𝑚 are the chemical energy contributions of the
at a time. In this work, we use a diﬀerent approach to model re-solution          Helmholtz free energies of each phase and 𝜌𝑔 and 𝜌𝑣 are the densities
based on the Turnbull model described in Eqs. (2) and (16) of the work            (defects per unit volume) of gas atoms and vacancies, respectively.
by Pastore et al. [47]: the xenon bubble is fully re-solved in the lattice,           For all GBs (𝑖, 𝑗 > 0), 𝛾𝑖𝑗 = 3∕2 to ensure the order parameters are
leading to a higher concentration of mobile xenon in the grains and               symmetric across the interface [51]. The values of 𝛾0𝑗 and 𝛾𝑖0 (at bubble
larger amount of xenon moving to the GB for more realistic bubble                 surfaces) deﬁne the semi-dihedral angle that forms between a bubble
growth.                                                                           surface and a GB. Some researchers have found that the semi-dihedral
                                                                                  of intergranular bubbles in UO2 is around 50◦ [52], while others report
3.2. Phase ﬁeld model components and equations                                    that it ranges from 40◦ to 80◦ [53]. When 𝛾0𝑗 = 𝛾𝑖𝑗 = 3∕2, the semi-
                                                                                  dihedral angle is 60◦ degrees, which is within the experimental range,
    In the hybrid model, the phase ﬁeld method in MARMOT is used to               therefore we use a constant value 𝛾𝑖𝑗 = 𝛾 = 3∕2 in the model.
model GB migration, the interaction between GBs and gas bubbles, and                  The model parameters 𝐿, 𝑚, and 𝜅 can be related to measurable
intergranular bubble growth and coalescence. The phase ﬁeld model                 material properties, the GB energy 𝜎𝐺𝐵 and the interface mobility 𝑀𝑖𝑛𝑡 ,
formulation is similar to that described by Aagesen et al. [8] and it             and to the interfacial width 𝑙𝑖𝑛𝑡 to make the model quantitative [50]:
represents the evolving microstructure using variable ﬁelds. Grains are
represented by order parameters denoted as 𝜂1 , 𝜂2 , ..., 𝜂𝑛 . These order                   4 𝑀𝑖𝑛𝑡
                                                                                  𝐿𝐺𝐵 =             ,                                                               (9)
parameters have a value of 1 within corresponding grains, 0 in all                           3 𝑙𝑖𝑛𝑡
other grains, and they smoothly transition from 0 to 1 across GBs. Sim-                      6𝜎𝐺𝐵
ilarly, an additional order parameter 𝜂0 is designated to represent all                 𝑚=                                                                        (10)
                                                                                              𝑙𝑖𝑛𝑡
the bubbles. We also represent Xe atoms and U vacancies using their
                                                                                           3
respective chemical potentials: 𝜇𝑔 and 𝜇𝑣 . We assume Xe atoms are                      𝜅 = 𝜎𝐺𝐵 𝑙𝑖𝑛𝑡 .                                                            (11)
                                                                                           4
substitutional on the U lattice, such that there is a U vacancy associated
with each Xe atom. We neglect the vacancies and interstitials on the              The interface mobility 𝑀𝑖𝑛𝑡 = 𝑀𝐺𝐵 for interfaces with 𝜂0 = 0, where
                                                                                                     −𝑄
oxygen lattice and uranium interstitials since they migrate very quickly          𝑀𝐺𝐵 = 𝑀0 𝑒 𝑅𝑇 with the prefactor 𝑀0 and activation energy Q. For
compared to gas atoms and U vacancies and are therefore not rate lim-             bubble interfaces, where 𝜂0 > 0,
iting. Though we do not directly represent the interstitials, we capture
some of their eﬀects in the diﬀusivity values we use, since interstitials         𝑀𝑖𝑛𝑡 = 𝑀𝐺𝐵 (1 − 𝑔(𝜂0 )) + 𝑀𝑠 𝑔(𝜂0 ),                                            (12)

                                                                              4
M.A. Muntaha, S. Chatterjee, S. Blondel et al.                                                                                         Journal of Nuclear Materials 594 (2024) 155032

                                𝜂
where 𝑔(𝜂0 ) = tanh( 0 ). The value of the surface mobility 𝑀𝑠 was set to                     with a Xe atom transitions from two to four. Since the simulations in
                    0.2
be suﬃciently high such that the bubble surface migration is diﬀusion                         this work are carried out at 1600 K, it is assumed that 𝑠𝑣 = 4𝑠𝑔 in the
controlled.                                                                                   phase ﬁeld model [10].
   The chemical free energy densities of the matrix phase 𝑓𝑚,𝑐ℎ𝑒𝑚 and                              In the ﬁssion gas phase ﬁeld models described by Aagesen et al. [8]
the bubble phase 𝑓𝑏,𝑐ℎ𝑒𝑚 are approximated with parabolic functions [8]                        and Kim et al. [10], the vacancy and gas diﬀusivities were assumed to
that are functions of the gas and vacancy concentrations (𝑐𝑣 and 𝑐𝑔 ):                        be equal throughout the material. However, point defects diﬀuse faster
                                                                                              along GBs and surfaces than within grains. Therefore, we modify the
                      (               𝑓 )2           (          𝑓 )2
                                    −𝐸𝑣                       −𝐸𝑣                             phase ﬁeld model to make 𝐷𝑣 and 𝐷𝑔 functions of the order parameters
         1                                    1
𝑓𝑚,𝑐ℎ𝑒𝑚 = 𝑘𝑚             𝑐𝑣 − 𝑒 𝑘𝑏 𝑇         + 𝑘𝑚     𝑐𝑔 − 𝑒 𝑘𝑏 𝑇      ,           (13)       𝜂𝑖 :
         2 𝑣                                  2 𝑔
         1                     1                                                              𝐷𝑖 = 𝐷̃ 𝑏𝑢𝑙𝑘
                                                                                                      𝑖
                                                                                                           ℎ𝑏𝑢𝑙𝑘 + 𝐷̃ 𝐺𝐵
                                                                                                                      𝑖
                                                                                                                         ℎ𝐺𝐵 + 𝐷̃ 𝑠𝑢𝑟𝑓
                                                                                                                                  𝑖
                                                                                                                                       ℎ𝑠𝑢𝑟𝑓 ,                                 (21)
𝑓𝑏,𝑐ℎ𝑒𝑚 = 𝑘𝑏𝑣 (𝑐𝑣 − 𝑐𝑣𝑏,𝑒𝑞 )2 + 𝑘𝑏𝑔 (𝑐𝑔 − 𝑐𝑔𝑏,𝑒𝑞 )2 ,                              (14)
         2                     2
                                                                                              where 𝑖 = 𝑔 or 𝑣 and 𝐷̃ 𝑏𝑢𝑙𝑘
                                                                                                                        𝑖  , 𝐷̃ 𝐺𝐵      ̃𝑖
                                                                                                                                𝑖 , and 𝐷
                                                                                                                                          𝑠𝑢𝑟𝑓
                                                                                                                                               are the bulk, GB, and
where 𝑘𝑖𝑣 (for 𝑖 = 𝑚 or 𝑏) is the parabolic coeﬃcient for the phase with                      surface diﬀusivities used in the model, respectively. The interpolation
                                                                           𝑓   𝑓
respect to vacancies and 𝑘𝑖𝑔 with respect to gas and 𝐸𝑣 and 𝐸𝑔 are                            functions that distinguish between bulk, surface, and GBs are deﬁned
the formation energies of a U vacancy and a Xe gas atom on a U lat-                           as
tice site, respectively. The initial equilibrium composition of vacancies                                  𝑛 𝑛
                                              𝑏,𝑒𝑞            𝑏,𝑒𝑞                                         ∑ ∑
and gas atoms in the bubble phase are 𝑐𝑣 = 0.546 and 𝑐𝑔 = 0.454                                 ℎ𝑔𝑏 = 16                𝜂𝑖2 𝜂𝑗2 ,                                              (22)
[8]. These initial equilibrium concentration results in the minimization                                      𝑖=1 𝑗>𝑖
of the parabolic free energy (Eq. (14)), which corresponds to the mini-
                                                                                              ℎ𝑠𝑢𝑟𝑓 = 16𝜂02 (1 − 𝜂0 )2 ,                                                       (23)
mization of the Van der Waals free energy within the bubble phase. The
chemical potentials values are related to the concentrations according                        ℎ𝑏𝑢𝑙𝑘 = 1 − ℎ𝑔𝑏 − ℎ𝑠𝑢𝑟𝑓 ,                                                        (24)
to [8]:
                                                                                              and are illustrated in Fig. 2a. Fig. 2b shows the value of 𝐷𝑣 from
                                                                                              Eq. (21) across a 2D polycrystalline 30 μm by 30 μm domain with 20 ﬁs-
𝜇𝑔 = 𝑉𝑎 𝑘𝑚        𝑚,𝑒𝑞
         𝑔 (𝑐𝑔 − 𝑐𝑔    ),                                                          (15)                                           𝑣 = 100𝐷𝑣             𝑣            𝑣 .
                                                                                              sion gas bubbles and assuming 𝐷𝐺𝐵             𝑏𝑢𝑙𝑘
                                                                                                                                                 and 𝐷𝑠𝑢𝑟𝑓  = 1000𝐷𝑏𝑢𝑙𝑘
𝜇𝑣 = 𝑉𝑎 𝑘𝑚        𝑚,𝑒𝑞
         𝑣 (𝑐𝑣 − 𝑐𝑣    ),                                                          (16)           Due to the assumptions of our model, U vacancy and Xe surface
                                                                                              diﬀusivities are equal. As mentioned above, we assume gas atoms are
where 𝑉𝑎        = 0.0409 nm3 [54] is the atomic volume of a U atom in the                     substitutional such that there is a vacancy associated with every gas
UO2 crystal structure.                                                                        atom. Within a bubble, the model assumes that there is still a lattice, but
  The evolution of the chemical potentials 𝜇𝑔 and 𝜇𝑣 is deﬁned as [8]:                        that every site is occupied by either a vacancy or a gas atom residing in
                [                             𝑁
                                                              ]                               a vacancy. Since Xe is a gas at 1600 K, Xe atoms do not stay tied to one
𝜕𝜇𝑔        1                                  ∑ 𝜕𝜌𝑔 𝜕𝜂𝑖
       =            ∇.(𝐷𝑔 𝜒𝑔 ∇𝜇𝑔 ) + 𝑠𝑔 −                         ,                (17)       vacancy; rather, they move around throughout the void volume. Thus,
 𝜕𝑡        𝜒𝑔                                  𝑖=0
                                                     𝜕𝜂𝑖 𝜕𝑡                                   at the surface of a bubble there is no diﬀerence between a vacancy and a
                [                             𝑁
                                                              ]                               gas atom tied to a vacancy, making the Xe surface diﬀusivity equivalent
𝜕𝜇𝑣   1                                       ∑ 𝜕𝜌𝑣 𝜕𝜂𝑖
    =            ∇.(𝐷𝑣 𝜒𝑣 ∇𝜇𝑣 ) + 𝑠𝑣 −                            ,                (18)       to the vacancy surface diﬀusivity.
 𝜕𝑡   𝜒𝑣                                      𝑖=0
                                                     𝜕𝜂𝑖 𝜕𝑡                                       It is important to note that if measured values of the GB and surface
                                                                                              diﬀusivities are used in Eq. (21), the defect transport along the inter-
where 𝑠𝑔 and 𝑠𝑣 are the source terms for the production of Xe atoms
                                                                                              faces will be too large if the interface width 𝑙𝑖𝑛𝑡 is larger than the true
and U site vacancies, 𝐷𝑔 and 𝐷𝑣 are the diﬀusion coeﬃcient of the gas
                                                                                              width of such interfaces (on the order of 0.5 nm for GBs and 0.1 nm for
and vacancies, and 𝜒𝑔 and 𝜒𝑣 are the susceptibilities which are deﬁned
                                                                                              oxide surfaces). Typically, phase ﬁeld simulations use interface widths
as [8],
                                                                                              that are many of orders of magnitude larger than the true widths to re-
           ℎ𝑚           ℎ𝑏                                                                    duce the computational cost of resolving the diﬀuse interface. Thus, the
𝜒𝑔 =             +                                                                 (19)
       𝑉𝑎2 𝑘𝑚
            𝑔         𝑉𝑎2 𝑘𝑏𝑔                                                                 GB and surface diﬀusivities must be reduced. We derive an approach
                                                                                              for reducing the GB and surface diﬀusivities for large interface widths
           ℎ𝑚          ℎ𝑏
𝜒𝑣 =             +              .                                                  (20)       based on the Hart approximation for the eﬀective polycrystal diﬀusion
       𝑉𝑎2 𝑘𝑚
            𝑣         𝑉𝑎2 𝑘𝑏𝑣                                                                 coeﬃcient 𝐷𝑒𝑓 𝑓 [55]:
    The gas source term 𝑠𝑔 is computed by Xolotl and passed to the                                                  𝑤𝑖𝑛𝑡
phase ﬁeld model. 𝑠𝑔 = 0 within a grain or bubble (when an order pa-                          𝐷𝑒𝑓 𝑓 = 𝐷𝑏𝑢𝑙𝑘 +            (𝐷𝑖𝑛𝑡 − 𝐷𝑏𝑢𝑙𝑘 ),                                      (25)
                                                                                                                     𝐺
rameter equals 1). 𝑠𝑔 in the phase ﬁeld model is only used to pass gas                        where 𝑤𝑖𝑛𝑡 is the true interface width and 𝐺 is the average grain size.
from Xolotl to MARMOT; all of the gas production due to ﬁssion is rep-                        If we equate the Hart approximation for cases using the true interface
resented by Xolotl. 𝑠𝑔 > 0 at interfaces and its magnitude is equal to                        width and a larger interface width 𝑙𝑖𝑛𝑡 , we can solve for the reduced
the total amount of gas diﬀusing to this location from the neighboring                        interface diﬀusivity
grid points, divided by the time step size. Even though this results in a                                                 (         )
                                                                                                              𝑤𝑖𝑛𝑡            𝑤
gas concentration gradient at the GBs in MARMOT, it is more energet-                          𝐷̃ 𝑖𝑛𝑡 = 𝐷𝑖𝑛𝑡        + 𝐷𝑏𝑢𝑙𝑘 1 − 𝑖𝑛𝑡 .                                           (26)
ically favorable for the gas to diﬀuse to intergranular bubbles than to                                       𝑙𝑖𝑛𝑡             𝑙𝑖𝑛𝑡
diﬀuse into the grain center, so the amount of gas diﬀusion from GBs                          Note that a recent paper has presented alternative approaches for re-
into the grain centers in MARMOT is negligible. In the case of a mov-                         ducing the interface diﬀusivity [56] that are more complex than the
ing interface, where the given location was situated in the grain at the                      one we use here.
previous time step and is now within the GB, the total amount of xenon                           The values used in our simulations for the various model parameters
(mobile and in bubbles) at this location is added to the previous quan-                       are shown in Table 1. The table also provides the reference for where
tity, divided by the time step. The latter quantity corresponds to the GB                     the values were obtained.
sweeping eﬀect. Since Xolotl considers only gas atom clusters, it cannot
deﬁne the vacancy source term 𝑠𝑣 . Therefore, the vacancy source term                         4. Numerical methods
is a function of the gas source term. As Xe diﬀuses through UO2 , it oc-
cupies a defect cluster containing multiple U-vacancies [27]. At around                          In this work, we apply the hybrid ﬁssion gas model to investigate
1600 K during reactor operation, the number of U vacancies traveling                          the impact of the surface and GB diﬀusivities on ﬁssion gas release us-

                                                                                          5
M.A. Muntaha, S. Chatterjee, S. Blondel et al.                                                                            Journal of Nuclear Materials 594 (2024) 155032




Fig. 2. Demonstration of the spatially varying diﬀusivity that accounts for fast GB and surface diﬀusion, where (a) shows an illustration of ℎ𝑔𝑏 from Eq. (22) and
                                                                                                                            𝑣           𝑣          𝑣           𝑣
ℎ𝑠𝑢𝑟𝑓 from Eq. (23), and (b) shows the value of 𝐷𝑣 calculated using Eq. (21) throughout a 30 μm × 30 μm domain. Here, 𝐷𝐺𝐵       = 100𝐷𝑏𝑢𝑙𝑘  and 𝐷𝑠𝑢𝑟𝑓 = 1000𝐷𝑏𝑢𝑙𝑘 .
(For interpretation of the colors in the ﬁgure(s), the reader is referred to the web version of this article.)


                   Table 1
                   The parameters used for the phase ﬁeld model.
                   The reference that is the source of the value is
                   provided, where applicable.

                     Parameter       Value                Reference

                     T               1600 K
                     𝑀𝑜              2.14× 10−7 m4 /Js    [57]
                     𝑄               290 kJ/mol           [57]
                     𝛾𝑖𝑗             1.5                  [8]
                     𝑉𝑎              0.0409 nm3           [54]
                     𝜎𝐺𝐵             1.5 J/m2             [57]
                     𝑙𝑖𝑛𝑡            480 nm               [10]
                     𝑤𝐺𝐵             0.5 nm               [58]
                     𝑤𝑠              0.1 nm               [59]
                     𝑌𝑋𝑒             0.2156               [60]
                     𝐸𝑣𝑓             3 eV                 [14]
                     𝐸𝑔𝑓             4.66 eV              [27]
                     𝑐𝑣𝑏,𝑒𝑞          0.546                [8]
                     𝑐𝑔𝑏,𝑒𝑞          0.454                [8]
                     𝑘𝑚𝑔 = 𝑘𝑚𝑣       4.81×1011 J/m3       [14]
                     𝑘𝑏𝑔 = 𝑘𝑏𝑣       9×1011 J/m3          [14]
                     𝑀𝑠              5.616×10−18 m4 /Js   [8]
                     𝑆𝑣              4× 𝑆𝑔                [27]                       Fig. 3. The initial UO2 microstructure used in our simulations. The microstruc-
                                                                                     ture has 25 initial grains, with a 5 μm initial average grain size, and 20 inter-
                                                                                     granular bubbles with a 480 nm initial radius. Periodic boundary conditions
ing 2D polycrystal simulations. As described in Section 3, Xolotl uses the           are applied on the top and bottom, the right boundary has a zero ﬂux closed
implicit ﬁnite diﬀerence method, MARMOT uses the implicit ﬁnite ele-                 boundary condition, and the left boundary is considered a free surface.
ment method, and they are coupled using tools available in the MOOSE
framework [10]. In our investigation, we use a 24 μm by 24 μm poly-
crystal domain initially containing 25 grains with an average grain size             concentrations near the free surface that can temporarily occur around
of 5 μm. To avoid the need to model intergranular bubble nucleation,                 bubbles.
we begin the simulations with 20 circular bubbles with a 480 nm initial                  Adaptive time stepping is used in the simulations, where the initial
radius. The gas within the grains is initialized at zero. The initial grain          time step is 10 s and the maximum time step used in the simulations
and intergranular bubble structure is shown in Fig. 3.                               is 50,000 s. The time step size is increased or decreased from one time
    Both Xolotl and MARMOT use a uniform square grid with a distance                 step to the next to maintain an average of 20 nonlinear iterations in the
between ﬁnite diﬀerence grid points/ﬁnite element size of 120 nm.                    MARMOT solve. Larger diﬀusivities result in faster evolution that re-
First-order Lagrange elements are used in MARMOT. For the phase ﬁeld                 quires a smaller time step to resolve. Therefore, simulations with larger
model, a consistent interfacial width of 𝑙𝑖𝑛𝑡 = 480 nm is used. Regarding            GB and surface diﬀusivities require smaller time steps, and thus are
boundary conditions, the top and bottom boundaries are treated as pe-                more computationally expensive. This is demonstrated in Fig. 4 for a
riodic, and a zero ﬂux closed boundary condition is applied to the right             simulation at 𝑇 = 1600 K using the domain and initial conditions from
boundary for all variables. The left boundary is considered an open or               Fig. 3. The maximum time step used in the simulations decreases by
free surface. We represent the free surface in Xolotl using a Dirichlet              many orders of magnitude as we increase the surface diﬀusivity, which
boundary condition of zero for all cluster concentrations. We represent              has a large impact on the computational cost. Due to this eﬀect, we
it in the phase ﬁeld model using zero gradient boundary conditions for               shorten the simulation time used for the fastest surface diﬀusivity in-
the grain order parameters and Dirichlet boundary conditions for the                 vestigated in our simulations to reduce the computational cost.
other variables with values of 𝜂0 = 0, 𝜇𝑣 = 0, and 𝜇𝑔 = −0.023. The neg-                 As shown in Figs. 1a and 1b, the relationship between the bulk U
ative chemical potential boundary condition for the gas atoms was ﬁt                 vacancy and Xe diﬀusivity depends on the reference used for the U va-
to ensure that gas only leaves from the free surface and does not en-                cancy. The lower published values for U vacancy diﬀusivity are lower
ter. With 𝜇𝑔 = 0, gas enters in some cases due to small negative gas                 than the Xe diﬀusivity, while the Matzke [20] U vacancy diﬀusivity

                                                                                 6
M.A. Muntaha, S. Chatterjee, S. Blondel et al.                                                                             Journal of Nuclear Materials 594 (2024) 155032


                                                                                         5.1. Impact of GB diﬀusivity on ﬁssion gas release

                                                                                             To identify how GB diﬀusion impacts ﬁssion gas release, we carry
                                                                                         out a parametric study in which we ignore fast surface diﬀusion
                                                                                         (𝐷𝑠𝑢𝑟𝑓 = 𝐷𝑏𝑢𝑙𝑘 ) and carry out simulations at increasing values of GB
                                                                                         diﬀusivity. As shown in Figs. 1c and 1d, at 𝑇 = 1600 K the majority of
                                                                                         literature-reported GB diﬀusivity data for both U vacancies and Xe lie
                                                                                         between 10−15 m2 /s and 10−9 m2 /s, exhibiting a variation of up to six
                                                                                         orders of magnitude. Since the GB vacancy and Xe diﬀusivities range
                                                                                         across the same orders of magnitude, we simplify our parametric study
                                                                                         by assuming that they are equal. For the lowest GB diﬀusivity, we use
                                                                                                                                                          𝑔
                                                                                         the lower value from Olander and Van Uﬀelen [32] (labeled 𝐷𝐺𝐵,𝑙 ). We
                                                                                         then perform simulations with progressively higher GB diﬀusivities, in-
                                                                                         creasing by orders of magnitude up to six orders of magnitude higher
                                                                                                 𝑔
                                                                                         than 𝐷𝐺𝐵,𝑙 . Thus, our simulations roughly encompass the full range of
Fig. 4. The impact of high interface diﬀusivity on the time step size. The surface       literature-reported GB diﬀusivity.
diﬀusivity values are shown relative to the values from Zhou and Olander [38].               Note that due to this simplifying assumption that GB vacancy and
                                                                                         Xe diﬀusivities are equal, the vacancy and Xe diﬀusivities are assumed
                                                                                         to be equal for bulk, GB, and surface diﬀusion in our model. We assume
value is several orders of magnitude larger than the Xe diﬀusivity. In                   they are the same for bulk diﬀusion because their values do not signif-
the models by Aagesen et al. [8] and Kim et al. [10], it was assumed                     icantly impact ﬁssion gas release when we include fast GB and surface
that bulk vacancy diﬀusivity was equal to the Xe atom diﬀusivity from                    diﬀusion. They are the same for surface diﬀusion because vacancies and
Turnbull [24], which simpliﬁed the model and improved the conver-                        Xe atoms are essentially the same at the surface of a bubble due to the
gence behavior. However, the impact of this assumption on the model                      assumptions of our model.
predictions was not investigated.                                                            As shown in Fig. 6a, the GB diﬀusivity has a large impact on the
    Here, we quantify the impact of the bulk U vacancy diﬀusivity on                     fractional gas release. As GB diﬀusivity increases, more gas travels along
the predicted ﬁssion gas release by simulating the ﬁssion gas release at                 the GBs and escapes from the free surface. The fractional release from
                                                                                         the Booth model is larger for all but the largest GB diﬀusivity because
temperature 𝑇 = 1600 K and ﬁssion rate 𝐹̇ = 1.09 × 1019 ﬁssions/(m3 s)
                                                                                         it assumes that all gas that arrives at GBs is released and intragranular
using the domain and initial condition shown in Fig. 3. When fast GB
                                                                                         bubble trapping is not included in the bulk Xe diﬀusivity we use in
and surface diﬀusion is not included, higher U vacancy diﬀusivity re-
                                                                                         the model. The fractional release is larger than from the Booth model
sults in increased gas release over time (Fig. 5a). However, when fast                                                         𝑔
                                                     𝑣 = 105 𝐷𝑣                          for the largest diﬀusivity of 106 𝐷𝐺𝐵,𝑙 due to a large amount of gas
GB and surface diﬀusion are included (we assume 𝐷𝐺𝐵             𝑏𝑢𝑙𝑘
                                                                     and
  𝑣            𝑣                                                                         sweeping during GB migration resulting in only a small fraction of the
𝐷𝑠𝑢𝑟𝑓 = 10 𝐷𝑏𝑢𝑙𝑘 ), the impact of U vacancy diﬀusivity becomes negli-
            7
                                                                                         gas remaining within the fuel.
gible (Fig. 5b). In other words, when fast GB and surface diﬀusion are                       The gas release becomes signiﬁcant enough to cause bubble col-
included, the bulk diﬀusivity does not signiﬁcantly impact ﬁssion gas                    lapse, reducing the number of bubbles (see Fig. 6b), for GB diﬀusivities
release and so we are safe to assume that the bulk U vacancy diﬀusiv-                    ≥ 104 𝐷𝐺𝐵,𝑙 . The number of grains decreases rapidly at the start of the
ity is the same as the bulk Xe diﬀusivity, as was done by Aagesen et                     simulations due to GB migration, as shown in Fig. 6c, until they are
al. [8] and Kim et al. [10]. For the purposes of our parametric investi-                 pinned by ﬁssion gas bubbles. For GB diﬀusivities ≤ 103 𝐷𝐺𝐵,𝑙 , the num-
gation, we use the Xe gas bulk diﬀusivity data from Turnbull et al. [24]                 ber of grains reaches 15 and does not decrease further, since the bubbles
based on the work by Robbe et al. [61], where the ﬁssion gas release                     do not evolve. For GB diﬀusivities ≥ 104 𝐷𝐺𝐵,𝑙 , bubble evolution allows
was found to be insensitive to whether diﬀusivity values from Turnbull                   for additional GB migration. For GB diﬀusivities ≥ 105 𝐷𝐺𝐵,𝑙 , bubble
et al. [24] or Matthews et al. [27] were used.                                           collapse results in signiﬁcant reduction in the number of grains. Yet,
                                                                                         as the number of grains goes down, the ﬁssion gas release slows. The
5. Results                                                                               faster diﬀusion and additional GB migration requires a smaller time
                                                                                         step, which results in larger wall time, as shown in Fig. 6d. The total
                                                                                         wall time (computational cost) is nearly four times greater with a GB
    Due to the large uncertainty in the surface and GB diﬀusivity values                 diﬀusivity of 106 𝐷𝐺𝐵,𝑙 than for 𝐷𝐺𝐵,𝑙 .
from the literature, it is important to investigate their impact on the ﬁs-                  The relationship between bubble collapse, grain growth, and ﬁssion
sion gas behavior. Thus, we carry out two parametric studies, one on                     gas release is more clear from a qualitative analysis of the microstruc-
the impact of the GB diﬀusivity on ﬁssion gas release and one on the im-                 ture evolution, shown in Fig. 7. For a GB diﬀusivity of 104 𝐷𝐺𝐵,𝑙 , the
pact of surface diﬀusivity. We use 2D simulations to reduce the overall                  two bubbles that disappear are the closest to the free surface and are
computational expense. In both studies, we compare the fractional gas                    connected to it by a GB. For a GB diﬀusivity of 105 𝐷𝐺𝐵,𝑙 , all of the
release over time from the left boundary. The fractional release is equal                bubbles near the free surface collapse, which allows additional grain
to the total gas released from the free surface divided by the total gas                 growth near the surface, reducing the number of GBs touching the free
produced. The total gas released is computed by integrating the bound-                   surface. As can be seen in Figs. 6a and 6c, the drop in the number of
ary gas ﬂux over the side area (assuming a depth in the third dimension                  grains to 14 that occurs around 10 days coincides with a decrease in
of 1 μm) and over time. The total gas produced includes the gas in the                   the ﬁssion gas release rate. A similar slowing of the gas release occurs
initial intergranular bubbles plus the gas produced over time, i.e. 𝐹̇ 𝑦𝑛 𝑡.             when the number of GBs touching the surface goes from four to three, at
We compare the fractional release from our simulations with that from                    around 40 days. For a GB diﬀusivity of 106 𝐷𝐺𝐵,𝑙 , rapid bubble collapse
the analytical Booth model [62] using the bulk Xe diﬀusivity from Turn-                  results in even more rapid grain growth that decreases the number of
bull [24] and assuming a grain radius equal to half the initial grain size               GBs touching the free surface, resulting in a slowing of the ﬁssion gas
from the simulations. We also compare the change in the number of                        release. After 60 days, the last intergranular bubble disappears and the
bubbles, the number of grains, and the total computational wall time.                    ﬁssion gas release reduces nearly to zero. Some release occurs due to re-
In addition to these quantitative metrics, we also qualitatively compare                 solution and emission from the small intragranular bubbles represented
the microstructure evolution over time.                                                  by Xolotl, but it is small compared to the gas release along the GBs.

                                                                                     7
M.A. Muntaha, S. Chatterjee, S. Blondel et al.                                                                          Journal of Nuclear Materials 594 (2024) 155032




Fig. 5. The impact of U-vacancy bulk diﬀusivity on ﬁssion gas release, where we consider the values from Matthews et al. [22], Matzke [20], and assuming it is
equal to the Xe diﬀusivity from Turnbull [24], as done by Aagesen et al. [8]. (a) shows the results for the homogeneous case when grain boundary and surface
diﬀusion are equal to bulk diﬀusion. (b) shows the results when grain boundary and surface diﬀusivity are signiﬁcantly greater than bulk diﬀusivity.




Fig. 6. The eﬀects of GB diﬀusivity on ﬁssion gas release, where (a) shows the fractional gas release over time from our simulations and from the Booth model, for
reference, (b) the number of bubbles, (c) the number of grains, and (d) the computational wall time. A homogeneous case with no fast GB diﬀusivity is shown for
reference.

   From the results of our parametric study, it is possible to draw some            grain size or less. In Fig. 8 we show the gas concentration in MARMOT
conclusions with regards to the correct Xe GB diﬀusivity. An analysis               at the end of our simulations carried out with diﬀerent GB diﬀusivities.
carried out by Olander and Van Uﬀelen [32] found that a Xe atom                     In our results, the gas depletion region, deﬁned as the region where
would be trapped after a migration distance along a GB equal to the                 the intergranular bubbles are shrinking due to loss of gas from the free

                                                                                8
M.A. Muntaha, S. Chatterjee, S. Blondel et al.                                                                              Journal of Nuclear Materials 594 (2024) 155032




                                                                                                                                                                     𝑔
Fig. 7. The impact of GB diﬀusivity on microstructure evolution. Snapshots of the microstructure are shown at diﬀerent times for GB diﬀusivity: (a) 104 × 𝐷𝐺𝐵,𝑙 ,
              𝑔                     𝑔
(b) 10 4
           × 𝐷𝐺𝐵,𝑙 , and (c) 104 × 𝐷𝐺𝐵,𝑙 . The times are selected for each snapshot to best illustrate the microstructure change with the diﬀerent GB diﬀusivities. The
simulation’s initial microstructure is shown in Fig. 3. Grains are shown in red, GBs in yellow, and bubbles in blue.




                                 Fig. 8. The Xe concentration in MARMOT across the domain after 100 days for the various GB diﬀusivities.


surface, is further than one grain size away from the free surface for GB                   Though Section 5.1 revealed a large impact of GB diﬀusivity on ﬁs-
                      𝑔
diﬀusivities ≥ 105 𝐷𝐺𝐵,𝑙 . Based on this analysis, we propose that the GB               sion gas release, this is not the case for surface diﬀusivity, as shown
                                     𝑔
diﬀusivity should be ≤ 104 𝐷𝐺𝐵,𝑙 .                                                      in Fig. 9a. The magnitude of the fractional release for all surface dif-
                                                                                        fusivities is smaller than for the two highest GB diﬀusivity values and
5.2. Impact of surface diﬀusivity on ﬁssion gas release                                 for the Booth model. The fractional release for all surface diﬀusivities
                                                                                        are larger than the four smallest GB diﬀusivity values. The release in-
    To identify how surface diﬀusion impacts ﬁssion gas release, we                                                                                        𝑣
                                                                                        creases with increasing surface diﬀusivity up to a value of 10−3 𝐷𝑠𝑢𝑟𝑓    .
                                                                                                                                                               ,𝑢
carry out a parametric study in which we ignore fast GB diﬀusion                                                    𝑣
                                                                                        For a diﬀusivity of 10−2 𝐷𝑠𝑢𝑟𝑓     , the gas release decreases after around
(𝐷𝐺𝐵 = 𝐷𝑏𝑢𝑙𝑘 ) and use increasing values of surface diﬀusivity. As shown                                                ,𝑢
in Fig. 1e, at 𝑇 = 1600 K the literature-reported U vacancy surface diﬀu-               45 days when depleted regions around bubbles near the free surface
sivity values range from 10−12 m2 /s to 10−3 m2 /s, showing a variation                 result in the nonphysical behavior of gas reentering the fuel.
                                                                                                                      𝑣
                                                                                            For diﬀusivities of 10−1 𝐷𝑠𝑢𝑟𝑓          𝑣
                                                                                                                               and 𝐷𝑠𝑢𝑟𝑓    , rapid bubble coalescence
of up to nine orders of magnitude. The value from Zhou and Olan-                                                            ,𝑢           ,𝑢
der [38] is the highest; therefore, our parametric study begins with the                and grain growth eliminates the GB paths for diﬀusion from bubbles to
Zhou and Olander surface diﬀusivity (labeled 𝐷𝑠𝑢𝑟𝑓𝑣      ) and decreases by
                                                      ,𝑢                                the free surface. This is because there is a large eﬀect of surface diﬀu-
six orders of magnitude in increments of one order of magnitude.                        sivity on number of bubbles (Fig. 9b) and number of grains (Fig. 9c). An

                                                                                    9
M.A. Muntaha, S. Chatterjee, S. Blondel et al.                                                                           Journal of Nuclear Materials 594 (2024) 155032




Fig. 9. The impact of surface diﬀusivity on ﬁssion gas release, where (a) shows the fractional gas release over time from our simulations and from the Booth model,
(b) the quantity of bubbles, (c) the number of grains, and (d) the computational wall time.


increase in the surface diﬀusivity results in an increase in bubble mobil-           bubble structures that have been shown to form on grain faces are an
ity, which leads to greater bubble coalescence with neighboring bubbles              inherently 3D structure that we cannot observe in our 2D simulations.
and less pinning of GBs by bubbles. The increase in the computational                Therefore, we have performed an additional study on the impact of sur-
wall time is even more dramatic for the high surface diﬀusivities than               face diﬀusivity on the evolution and coalescence of GBs and bubbles
for the GB diﬀusivities, with the total wall time to simulate 50 days                using 3D simulations. The computational cost of 3D simulations can
                                 𝑣
with a surface diﬀusivity of 𝐷𝑠𝑢𝑟𝑓      being 300 times longer than the
                                     ,𝑢                                              be quite high, so we use a reduced domain size of 9 μm by 9 μm by
                                                                  𝑣
wall time to simulate 100 days with a surface diﬀusivity of 10−6 𝐷𝑠𝑢𝑟𝑓    .
                                                                       ,𝑢            9 μm with 5 initial grains and 320 gas bubbles with initial radius 384
                                                                                     nm, randomly distributed on the GB faces. The initial mean grain size
    A qualitative analysis of the microstructure evolution is even more              is approximately 5 μm. We also only model 75 minutes at 𝑇 = 1600 K
important to understand the impact of surface diﬀusivity than for the                with a ﬁssion rate 𝐹̇ = 1.09 × 1019 ﬁssions/(m3 s). Since bubble coales-
GB diﬀusivity. The evolution in the microstructure for diﬀerent surface              cence happens independently of ﬁssion gas release, we carry out the 3D
diﬀusivities is shown in Fig. 10. Initial grain growth occurs even with
                                                                                     simulations without a free surface. We maintain the same physical and
lower values of surface diﬀusivity, as it did for the smaller GB diﬀusiv-
                                                                                     model parameters as in the 2D analysis, except for the absence of the
ity cases. No additional microstructure evolution occurred for surface
                    𝑣                                            𝑣                   free surface. As our 2D analysis shows that surface diﬀusivity does not
diﬀusivity ≤ 10−5 𝐷𝑠𝑢𝑟𝑓 ,𝑢
                           . With a surface diﬀusivity of 10−4 𝐷𝑠𝑢𝑟𝑓 ,𝑢
                                                                        , the
                                                                                     impact ﬁssion gas release, our 3D analysis focuses solely on gas-bubble
number of bubbles goes down by one due to bubble coalescence rather
                                                            𝑣                        evolution. We carry out two 3D simulations, each with a GB diﬀusivity
than bubble collapse. For surface diﬀusivities ≥ 10−3 𝐷𝑠𝑢𝑟𝑓    ,𝑢
                                                                  , bubbles                                                                     𝑣
                                                                                     of 𝐷𝐺𝐵,𝑙 and one with a surface diﬀusivity of 10−4 𝐷𝑠𝑢𝑟𝑓       ,𝑢
                                                                                                                                                       and one of
are dragged together by GBs, resulting in additional coalescence. The                  𝑣
coalescence further reduces GB pinning and enables additional grain                  𝐷𝑠𝑢𝑟𝑓 ,𝑢 .
growth. At the end of the simulation, only three grains remain for                       The microstructure evolution in the 3D simulations is shown in
       𝑣                                         𝑣           𝑣                                                                      𝑣
                                                                                     Fig. 11. With a surface diﬀusivity of 10−4 𝐷𝑠𝑢𝑟𝑓      , most bubbles remain
10−2 𝐷𝑠𝑢𝑟𝑓 ,𝑢
              and only two remain for 10−1 𝐷𝑠𝑢𝑟𝑓   ,𝑢
                                                      and 𝐷𝑠𝑢𝑟𝑓 ,𝑢
                                                                    and the                                                             ,𝑢
remaining bubbles get quite large.                                                   at grain faces, with very few connecting to grain edges. In contrast, with
                                                                                                                 𝑣
                                                                                     a surface diﬀusivity of 𝐷𝑠𝑢𝑟𝑓      , rapid bubble coalescence occurs. Bub-
    The amount of bubble coalescence and grain growth that occurs                                                    ,𝑢
when the surface diﬀusivity ≥ 10−3 𝐷𝑠𝑢𝑟𝑓𝑣      seems inconsistent with the           bles initially located at grain faces eventually connect to grain edges or
                                            ,𝑢
percolated intergranular bubbles structures that have been observed                  triple junctions due to enhanced surface diﬀusivity. This movement re-
in irradiated nuclear fuel (e.g. in [52]). However, the interconnected               sults in the formation of isolated triple junction bubbles after just 45

                                                                                10
M.A. Muntaha, S. Chatterjee, S. Blondel et al.                                                                                   Journal of Nuclear Materials 594 (2024) 155032




Fig. 10. The impact of surface diﬀusivity on microstructure evolution. Snapshots of the microstructure are shown at diﬀerent times for the entire range of surface
                                    𝑣                      𝑣                        𝑣                        𝑣                       𝑣
diﬀusivity values: (a) 𝐷𝑆 = 10−4 𝐷𝑠𝑢𝑟𝑓 ,𝑢
                                          , (b) 𝐷𝑆 = 10−3 𝐷𝑠𝑢𝑟𝑓 ,𝑢
                                                                   , (c) 𝐷𝑆 = 10−2 𝐷𝑠𝑢𝑟𝑓 ,𝑢
                                                                                            , (d) 𝐷𝑆 = 10−1 𝐷𝑠𝑢𝑟𝑓 ,𝑢
                                                                                                                     , and (e) 𝐷𝑆 = 𝐷𝑠𝑢𝑟𝑓 ,𝑢
                                                                                                                                             . The times are selected for each
snapshot to best illustrate the microstructure change with the diﬀerent surface diﬀusivities. The initial microstructure of the simulation is shown in Fig. 3. Grains
are shown in red, GBs in yellow, and bubbles in Blue.


minutes. This rate of bubble coalescence is much faster than what is                      provide an opportunity to highlight some diﬀerences between the 2D
observed in experiments. White [52] suggests that elongated bubbles                       and 3D bubble evolution. The largest diﬀerence is in the TJ behavior in
would not be present in UO2 if morphological relaxation took place un-                    the simulation with a surface diﬀusivity of 10−4 𝐷𝑠𝑢𝑟𝑓 𝑣      . The TJs in 2D
                                                                                                                                                     ,𝑢
der surface diﬀusion-limited conditions. Our 3D results are consistent                    simulations are points, while in 3D they are lines. This allows bubbles to
with White’s suggestion. Based on the results from our 2D and 3D sim-                     encounter them more often. Once a bubble contacts a triple junction, it
ulations, we suggest that a reasonable bubble surface diﬀusivity for U                    stays in contact, eventually contracting to form an isolated TJ bubble.
                     𝑣
vacancies is ≤ 10−4 𝐷𝑠𝑢𝑟𝑓    .
                          ,𝑢                                                              We also see more bubble coalescence on grain faces in 3D, since the
   Though the purpose of these small 3D simulations is to investigate                     grain faces are planes instead of lines and so it is easier for intergranular
the impact of the surface diﬀusivity on bubble coalescence, they also                     bubbles to come into contact.

                                                                                     11
M.A. Muntaha, S. Chatterjee, S. Blondel et al.                                                                        Journal of Nuclear Materials 594 (2024) 155032




                                                                                                                                                      𝑣
Fig. 11. Impact of surface diﬀusion on microstructure evolution in a 9 μm by 9 μm by 9 μm 3D domain. The evolution with a surface diﬀusivity of 10−4 𝐷𝑠𝑢𝑟𝑓 ,𝑢
                                                                                                                                                              is
                         𝑣
shown in (a) and with 𝐷𝑠𝑢𝑟𝑓 ,𝑢
                               in (b).


6. Discussion                                                                      note that our 2D simulations only consider one mechanism for ﬁssion
                                                                                   gas release: the transport of gas along GBs to the free surface. While
    Based on our 2D simulation results and on the ﬁnding from Olander              this mechanism is present in actual fuel, it is likely not the dominant
and Van Uﬀelen [32] that gas will only diﬀuse along GBs for about                  mechanism for ﬁssion gas release. It is commonly assumed that ﬁs-
one grain size before trapping, we suggest that a reasonable value for             sion gas release primarily occurs due to the three stages discussed in
the Xe GB diﬀusivity would range from the lower value from Olander                 the introduction. However, the interconnection of grain face bubbles
and Van Uﬀelen and up to four orders of magnitude larger. In addition,             and the formation of grain edge tunnels cannot be captured in our 2D
due to our use of 2D simulations that eﬀectively represent a columnar              simulations. GB diﬀusivity will have a much smaller impact on these
grain structure that would have fewer GBs touching the free surface                mechanisms.
than a true 3D structure, we are underestimating the release due to GB
                                                                                       Our 2D simulations indicate that surface diﬀusivity does not have
diﬀusion. Therefore, the true upper bound for the GB diﬀusivity may
                                                                                   a large impact on ﬁssion gas release. However, as mentioned above,
be even smaller. This covers the full range of the two values presented
                                                                                   our simulations only consider gas release via gas transport along GBs.
by Olander and Van Uﬀelen, and is below the GB diﬀusivity values
calculated using MD [31]. Thus, we suggest there may be some aspect                Surface diﬀusion will have a large impact on ﬁssion gas release via
of the GB structures used in the MD simulations that is resulting in Xe            interconnected grain face and grain edge porosity. Large surface dif-
diﬀusion that is too fast.                                                         fusivity would result in rapid bubble coalescence that would prevent
    Our results indicate that the GB diﬀusivity has a large impact on              the formation of interconnected bubble networks, as shown by our 3D
ﬁssion gas release, as shown in Fig. 6a. However, it is important to               simulations in Fig. 11.

                                                                              12
M.A. Muntaha, S. Chatterjee, S. Blondel et al.                                                                                  Journal of Nuclear Materials 594 (2024) 155032


    Based on our 2D and 3D simulation results, we suggest that a rea-                 CRediT authorship contribution statement
sonable bubble surface diﬀusivity for U vacancies is four orders of
magnitude below the value from Zhou and Olander [38] or less. Thus,                       Md Ali Muntaha: Investigation, Software, Visualization, Writing
we recommend surface diﬀusivities similar to those obtained using mass                – original draft, Data curation, Formal analysis, Validation. Sourav
transport methods [33,35–37] or lower. However, more information re-                  Chatterjee: Software, Supervision, Writing – review & editing. Sophie
garding surface diﬀusivity of ﬁssion gas bubbles is needed.                           Blondel: Methodology, Software, Writing – review & editing. Larry
    White and Tucker [52] found that assuming surface diﬀusion-                       Aagesen: Supervision, Writing – review & editing. David Andersson:
limited conditions [52] would result in rapid bubble coalescence, in                  Conceptualization, Funding acquisition, Project administration, Writ-
contrast to the elongated bubble structures observed in their fuel char-              ing – review & editing. Brian D. Wirth: Conceptualization, Funding
acterization. Our results are also consistent with this ﬁnding. This sug-             acquisition, Methodology, Project administration, Supervision, Writing
gests that bubble surfaces may behave diﬀerently than the free surfaces               – review & editing. Michael R. Tonks: Conceptualization, Funding ac-
used to measure surface diﬀusion. This is consistent with discrepancies               quisition, Methodology, Project administration, Resources, Supervision,
between the measured surface to GB energy ratios (for free surfaces)                  Writing – review & editing.
and the bubble semi-dihedral angles that are observed in irradiated fuel.
The surface to GB energy ratio is typically found to be around two [53],              Declaration of competing interest
yet semi-dihedral angles in fuel indicate energy ratios ranging from 0.6
to 0.8.                                                                                   The authors declare that they have no known competing ﬁnancial
    Since gas bubble surfaces exhibit distinct behavior, it is crucial to             interests or personal relationships that could have appeared to inﬂuence
investigate the diﬀerences between UO2 free surfaces and gas bubble                   the work reported in this paper.
surfaces. One potential approach would be to conduct MD simula-
tion studies focused on bubble surfaces to understand surface diﬀusion                Data availability
around these areas. Existing experimental studies measuring surface dif-
fusivity in UO2 focus on free surfaces rather than gas bubble surfaces.                   The MOOSE input ﬁles used to generate the simulation results in
Approaches that focus on the gas bubble surfaces or bubble mobility                   this paper can be obtained from the authors upon reasonable request.
are needed. For example, an in-situ Xe-implantation experiment in UO2
could be carried out to observe bubble evolution and measure the ki-                  Acknowledgements
netics of bubble coalescence, providing insight into gas bubble surface
diﬀusivity.                                                                               We express our gratitude for the high-performance computing re-
    Finally, the 2D simulations carried out in this work have provided                sources provided by the University of Florida’s HiPerGator clusters,
initial insights into the importance of considering GB and surface diﬀu-              which facilitated the execution of computationally intensive 2D simula-
sion in phase ﬁeld models of ﬁssion gas bubble evolution. This behavior               tions. Additionally, we acknowledge the support from leadership-class
has not been considered in past phase ﬁeld models of ﬁssion gas release               computers, such as INL Sawtooth [63], for running 3D large scale sim-
[7,8,10–15], but here we have shown the large impact it has on the                    ulations.
transport of gas atoms along GBs and on the bubble mobility, which                        This material is based upon work supported by the joint project on
impacts both bubble coalescence and bubble pinning of GBs. Future 3D                  Simulation of Fission Gas funded by the U.S. Department of Energy
                                                                                      Oﬃce of Nuclear Energy and U.S. Department of Energy Scientiﬁc Dis-
simulations with free surfaces are needed that consider GB and surface
                                                                                      covery through Advanced Computing (SciDAC) through the grant DOE
diﬀusion to investigate grain face bubble interconnection, grain edge
                                                                                      DE-SC0018359 at the University of Tennessee.
tunnel formation, and to understand all three stages of ﬁssion gas re-
lease.
                                                                                      References

7. Conclusion                                                                          [1] D.R. Olander, Fundamental Aspects of Nuclear Reactor Fuel Elements, Department
                                                                                           of Nuclear Engineering, U.C. Berkeley, 1976, https://doi.org/10.2172/7343826,
                                                                                           https://www.osti.gov/biblio/7343826.
    In this study, we utilized the hybrid phase ﬁeld/cluster dynamics                  [2] D.G. Cacuci, Handbook of Nuclear Engineering, Springer, New York, NY, 2010.
model developed by Kim et al. [10] to investigate the impact of fast GB                [3] M. Tonks, D. Andersson, R. Devanathan, R. Dubourg, A. El-Azab, M. Freyss, F. Igle-
and surface diﬀusion on ﬁssion gas bubble and GB evolution, as well                        sias, K. Kulacsy, G. Pastore, S. Phillpot, M. Welland, Unit mechanisms of ﬁssion
                                                                                           gas release: current understanding and future needs, J. Nucl. Mater. 504 (2018)
as ﬁssion gas release, which has been typically neglected in mesoscale                     300–317.
ﬁssion gas models. Our review of bulk, GB, and surface diﬀusivity val-                 [4] J. Rest, M. Cooper, J. Spino, J. Turnbull, P. Van Uﬀelen, C. Walker, Fission gas
ues for U vacancies and Xe in UO2 showed signiﬁcant uncertainty due                        release from uo2 nuclear fuel: a review, J. Nucl. Mater. 513 (2019) 310–345.
to the large range of values. Thus, we carried out parametric studies on               [5] I. Zacharie, S. Lansiart, P. Combette, M. Trotabas, M. Coster, M. Groos, Thermal
                                                                                           treatment of uranium oxide irradiated in pressurized water reactor: swelling and
the impact of GB and surface diﬀusivity on ﬁssion gas behavior using a
                                                                                           release of ﬁssion gases, J. Nucl. Mater. 255 (1998) 85–91.
modiﬁed version of the hybrid model. Our parametric study on the im-                   [6] S. Hu, C.H. Henager Jr., H.L. Heinisch, M. Stan, M.I. Baskes, S.M. Valone, Phase-
pact of GB diﬀusivity found that it had a large impact on the ﬁssion gas                   ﬁeld modeling of gas bubbles and thermal conductivity evolution in nuclear fuels,
release in our 2D domain. The results indicated that the GB diﬀusivity is                  J. Nucl. Mater. 392 (2) (2009) 292–300.
               𝑔             𝑔                                                         [7] P.C. Millett, M.R. Tonks, S. Biner, L. Zhang, K. Chockalingam, Y. Zhang, Phase-ﬁeld
likely ≤ 104 𝐷𝐺𝐵,𝑙 , where 𝐷𝐺𝐵,𝑙 is the lower grain boundary diﬀusivity
                                                                                           simulation of intergranular bubble growth and percolation in bicrystals, J. Nucl.
value rerported by Olander and Van Uﬀelen [32]. Our parametric study                       Mater. 425 (1) (2012) 69–76.
on the impact of surface diﬀusivity found that it had a large impact                   [8] L.K. Aagesen, D. Schwen, M.R. Tonks, Y. Zhang, Phase-ﬁeld modeling of ﬁssion
on bubble coalescence and GB migration. Our 2D and 3D results indi-                        gas bubble growth on grain boundaries and triple junctions in 𝑈 𝑂2 nuclear fuel,
                                                   𝑣
cate that the surface diﬀusivity is likely ≤ 10−4 𝐷𝑠𝑢𝑟𝑓             𝑣
                                                           , where 𝐷𝑠𝑢𝑟𝑓    is             Comput. Mater. Sci. 161 (2019) 35–45.
                                                        ,𝑢               ,𝑢            [9] A.A. Prudil, M.J. Welland, N. Ofori-Opoku, Modelling the growth and evolution of
the surface diﬀusivity value reported by Zhou and Olander [38]. The                        statistically signiﬁcant populations of intergranular ﬁssion gas bubbles by ipm, J.
bubble evolution in the 3D simulations is also distinct from what is ob-                   Nucl. Mater. 566 (2022) 153777, https://doi.org/10.1016/j.jnucmat.2022.153777,
served in our 2D simulations, especially at TJs. However, additional                       https://www.sciencedirect.com/science/article/pii/S0022311522002641.
                                                                                      [10] D. Kim, S. Blondel, D. Bernholdt, P. Roth, F. Kong, D. Andersson, M. Tonks, B. Wirth,
experiments and atomistic simulation results are needed to reduce the
                                                                                           Modeling mesoscale ﬁssion gas behavior in 𝑈 𝑂2 by directly coupling the phase ﬁeld
uncertainty on the GB and surface diﬀusivities in UO2 and 3D simula-                       method to spatially resolved cluster dynamics, Mater. Theory 6 (7) (2022), https://
tions are needed to further explore the ﬁssion gas behavior.                               doi.org/10.1186/s41313-021-00030-8.


                                                                                 13
M.A. Muntaha, S. Chatterjee, S. Blondel et al.                                                                                             Journal of Nuclear Materials 594 (2024) 155032


[11] P. Millett, M.R. Tonks, Application of phase-ﬁeld modeling to irradiation eﬀects in         [39] W. Robertson, Surface diﬀusion of oxides (a review), J. Nucl. Mater. 30 (1969)
     materials, current opinion in solid state, Mater. Sci. 15 (2011) 125–143.                        36–49.
[12] P.C. Millett, Percolation on grain boundary networks: application to ﬁssion gas re-         [40] D. Olander, Interpretation of tracer surface diﬀusion experiments on UO2 — roles
     lease in nuclear fuels, Comput. Mater. Sci. 53 (1) (2012) 31–36.                                 of gas and solid transport processes, J. Nucl. Mater. 96 (1981) 243–254.
[13] P.C. Millett, M.R. Tonks, S. Biner, Grain boundary percolation modeling of ﬁssion           [41] S. Blondel, D.E. Bernholdt, K.D. Hammond, L. Hu, D. Maroudas, B.D. Wirth, Bench-
     gas release in oxide fuels, J. Nucl. Mater. 424 (1–3) (2012) 176–182.                            marks and tests of a multidimensional cluster dynamics model of helium implanta-
[14] Y. Li, S. Hu, R. Montgomery, F. Gao, X. Sun, Phase-ﬁeld simulations of intragranular             tion in tungsten, Fusion Sci. Technol. 71 (1) (2017) 84–92.
     ﬁssion gas bubble evolution in 𝑈 𝑂2 under post-irradiation thermal annealing, Nucl.         [42] M. Tonks, D. Gaston, P. Millett, D. Andrs, P. Talbot, An object-oriented ﬁnite element
     Instrum. Methods Phys. Res. B 303 (2013) 62–67.                                                  framework for multiphysics phase ﬁeld simulations, Comput. Mater. Sci. 51 (2012)
[15] Z. Xiao, Y. Wang, S. Hu, Y. Li, S.-Q. Shi, A quantitative phase-ﬁeld model of gas                20–29.
     bubble evolution in uo2, Comput. Mater. Sci. 184 (2020) 109867, https://doi.org/            [43] D.R. Gaston, C.J. Permann, J.W. Peterson, A.E. Slaughter, D. Andrš, Y. Wang, M.P.
     10.1016/j.commatsci.2020.109867.                                                                 Short, D.M. Perez, M.R. Tonks, J. Ortensi, et al., Physics-based multiscale coupling
[16] A. Auskern, J. Belle, Uranium ion self diﬀusion in 𝑈 𝑂2 , J. Nucl. Mater. 3 (1961)               for full core nuclear reactor simulation, Ann. Nucl. Energy 84 (2015) 45–54.
     311–319.                                                                                    [44] S. Balay, S. Abhyankar, M.F. Adams, S. Benson, J. Brown, P. Brune, K. Buschelman,
[17] F. Schmitz, R. Lindner, Diﬀusion of heavy elements in nuclear fuels: actinides in                E. Constantinescu, L. Dalcin, A. Dener, V. Eijkhout, J. Faibussowitsch, W.D. Gropp,
     𝑈 𝑂2 , J. Nucl. Mater. 17 (1966) 259–269.                                                        V. Hapla, T. Isaac, P. Jolivet, D. Karpeev, D. Kaushik, M.G. Knepley, F. Kong, S.
[18] G. Alcock, R. Hawkins, A. Hills, P. McNamara, A study of cation diﬀusion in stoi-                Kruger, D.A. May, L.C. McInnes, R.T. Mills, L. Mitchell, T. Munson, J.E. Roman, K.
     chiometric uo2 using x-ray spectrometry, in: International Atomic Energy Agency.                 Rupp, P. Sanan, J. Sarich, B.F. Smith, S. Zampini, H. Zhang, H. Zhang, J. Zhang,
     Thermodynamics: Proceedings of the Symposium on... Held in Vienna, vol. 2, 1965,                 PETSc/TAO users manual, Tech. Rep. ANL-21/39 - Revision 3.19, Argonne National
     pp. 57–62.                                                                                       Laboratory, 2023.
[19] S. Yajima, H. Furuya, T. Hirai, Lattice and grain-boundary diﬀusion of uranium in           [45] R. Perriot, C. Matthews, M.W. Cooper, B.P. Uberuaga, C.R. Stanek, D.A. Andersson,
     𝑈 𝑂2 , J. Nucl. Mater. 20 (1966) 162–170.                                                        Atomistic modeling of out-of-pile xenon diﬀusion by vacancy clusters in uo2, J.
[20] H. Matzke, Atomic transport properties in UO2 and mixed oxides (U, Pu)O2, J.                     Nucl. Mater. 520 (2019) 96–109, https://doi.org/10.1016/j.jnucmat.2019.03.050,
     Chem. Soc. Faraday Trans. 2 (83) (1987) 1121–1142, https://doi.org/10.1039/                      https://www.sciencedirect.com/science/article/pii/S0022311518316751.
     F29878301121.                                                                               [46] W. Setyawan, M.W. Cooper, K.J. Roche, R.J. Kurtz, B.P. Uberuaga, D.A. Andersson,
[21] A. Sabioni, W. Ferraz, F. Millot, First study of uranium self-diﬀusion in 𝑈 𝑂2 by                B.D. Wirth, Atomistic model of xenon gas bubble re-solution rate due to thermal
     SIMS, J. Nucl. Mater. 257 (1998) 180–184.                                                        spike in uranium oxide, J. Appl. Phys. 124 (7) (2018) 075107.
[22] C. Matthews, R. Perriot, M.W. Cooper, C.R. Stanek, D.A. Andersson, Cluster dynam-           [47] G. Pastore, N. Militello, S. Blondel, B.D. Wirth, Single-size and cluster dynam-
     ics simulation of uranium self-diﬀusion during irradiation in 𝑈 𝑂2 , J. Nucl. Mater.             ics modeling of intra-granular ﬁssion gas bubbles in uo2, J. Nucl. Mater. 583
     527 (2019).                                                                                      (2023) 154453, https://doi.org/10.1016/j.jnucmat.2023.154453, https://www.
[23] D. Andersson, P. Garcia, X.-Y. Liu, G. Pastore, M. Tonks, P. Millett, B. Do-                     sciencedirect.com/science/article/pii/S0022311523002210.
     rado, D. Gaston, D. Andrs, R. Williamson, R. Martineau, B. Uberuaga, C. Stanek,             [48] M. Plapp, Uniﬁed derivation of phase-ﬁeld models for alloy solidiﬁcation from a
     Atomistic modeling of intrinsic and radiation-enhanced ﬁssion gas (xe) diﬀusion                  grand-potential functional, Phys. Rev. E 84 (3) (2011) 031601.
     in uo2±x: implications for nuclear fuel performance modeling, J. Nucl. Mater.               [49] L.K. Aagesen, Y. Gao, D. Schwen, K. Ahmed, Grand-potential-based phase-ﬁeld
     451 (1) (2014) 225–242, https://doi.org/10.1016/j.jnucmat.2014.03.041, https://                  model for multiple phases, grains, and chemical components, Phys. Rev. E 98 (2018)
     www.sciencedirect.com/science/article/pii/S0022311514001664.                                     023309.
[24] J. Turnbull, C. Friskney, J. Findlay, F. Johnson, A. Walter, The diﬀusion-coeﬃcients        [50] N. Moelans, A quantitative and thermodynamically consistent phase-ﬁeld interpola-
     of gaseous and volatile species during the irradiation of uranium-dioxide, J. Nucl.              tion function for multi-phase systems, Acta Mater. 59 (3) (2011) 1077–1086.
     Mater. 107 (1982) 168–184.                                                                  [51] N. Moelans, B. Blanpain, P. Wollants, Quantitative analysis of grain boundary prop-
[25] D. Davies, G. Long, The emission of xenon-133 from lightly irradiated uranium diox-              erties in a generalized phase ﬁeld model for grain growth in anisotropic systems,
     ide spheroids and powders, Tech. Rep., United Kingdom Atomic Energy Authority.                   Phys. Rev. B 78 (2008), https://doi.org/10.1103/PhysRevB.78.024113.
     Research Group. Atomic Energy Research Establishment, Harwell, Berks, England               [52] R. White, M. Tucker, The development of grain-face porosity in irradiated oxide
     (United Kingdom), 1963, https://www.osti.gov/biblio/4660737.                                     fuel, J. Nucl. Mater. 325 (2004) 61–77.
[26] W. Miekeley, F. Felix, Eﬀect of stoichiometry on diﬀusion of xenon in uo2, J. Nucl.         [53] E. Hodkin, The ratio of grain boundary energy to surface energy of nuclear ceramics
     Mater. 42 (3) (1972) 297–306, https://doi.org/10.1016/0022-3115(72)90080-3,                      as determined from pore geometries, J. Nucl. Mater. 88 (1) (1980) 7–14.
     https://www.sciencedirect.com/science/article/pii/0022311572900803.                         [54] M. Idiri, T.L. Bihan, S. Heathman, J. Rebizant, Behavior of actinide dioxides un-
[27] C. Matthews, R. Perriot, M.W. Cooper, C.R. Stanek, D.A. Andersson, Cluster dynam-                der pressure 𝑈 𝑂2 and 𝑇 ℎ𝑂2 , Phys. Rev. B 70 (2004), https://doi.org/10.1103/
     ics simulation of xenon diﬀusion during irradiation in 𝑈 𝑂2 , J. Nucl. Mater. 540                PhysRevB.70.014113.
     (2020).                                                                                     [55] R.W. Balluﬃ, S.M. Allen, W.C. Carter, Kinetics of Materials, John Wiley & Sons,
[28] A. Sabioni, W. Ferraz, F. Millot, Eﬀect of grain-boundaries on uranium and oxygen                2005.
     diﬀusion in polycrystalline 𝑈 𝑂2 , J. Nucl. Mater. 278 (2000) 364–369.                      [56] P.-C.A. Simon, L.K. Aagesen, C. Jiang, W. Jiang, J.-H. Ke, Mechanistic calculation of
[29] E. Vincent-Aublant, J.-M. Delaye, L.V. Brutzel, Self-diﬀusion near symmetrical tilt              the eﬀective silver diﬀusion coeﬃcient in polycrystalline silicon carbide: application
     grain boundaries in UO2 matrix: a molecular dynamics simulation study, J. Nucl.                  to silver release in agr-1 triso particles, J. Nucl. Mater. 563 (2022) 153669.
     Mater. 392 (2009) 114–120.                                                                  [57] M. Tonks, P.-C. Simon, J. Hirschhorn, Mechanistic grain growth model for fresh and
[30] C.O. Galvin, A. Chakraborty, A.D.R. Andersson, L. Capolungo, M.W.D. Cooper, De-                  irradiated 𝑈 𝑂2 nuclear fuel, J. Nucl. Mater. 543 (2021), https://doi.org/10.1016/j.
     velopment of a creep model informed by lower-length scale simulations to simulate                jnucmat.2020.152576.
     creep in doped uo2, Tech. Rep., Materials Science and Technology Division, Los              [58] T. Yao, K. Mo, D. Yun, S. Nanda, A.M. Yacout, J. Lian, Grain growth and pore
     Alamos National Laboratory, Los Alamos, New Mexico 87545, USA, 2023, https://                    coarsening in dense nano-crystalline 𝑈 𝑂2+𝑥 fuel pellets, J. Am. Ceram. Soc. 100
     www.osti.gov/biblio/1962764.                                                                     (2017) 2651–2658, https://doi.org/10.1111/jace.14780.
[31] X.-Y. Liu, C. Galvin, M. Cooper, A. Andersson, Molecular dynamics simulations of            [59] R. Hall, M. Mortimer, D. Mortimer, Surface energy measurements on 𝑈 𝑂2 – a critical
     ﬁssion gas xenon (xe) diﬀusion at uo2 grain-boundaries, Tech. Rep., Los Alamos                   review, J. Nucl. Mater. 148 (1987) 237–256.
     National Lab. (LANL), Los Alamos, NM (United States, 2023, https://doi.org/10.              [60] A.L. Nichols, D.L. Aldama, M. Verpelli, Chain ﬁssion yields, International Atomic
     2172/1969379, https://www.osti.gov/biblio/1969379.                                               Energy Agency, 13-Apr-2017, https://www-nds.iaea.org/sgnucdat/c1.htm.
[32] D. Olander, V. Uﬀelen, On the role of grain boundary diﬀusion in ﬁssion gas release,        [61] P. Robbe, T. Casey, C. Matthews, M.W.D. Cooper, S. Blondel, G. Pastore, D.-U. Kim,
     J. Nucl. Mater. 288 (2001) 137–147.                                                              M.A. Muntaha, M. Tonks, B. Wirth, A.D.R. Andersson, H. Najm, Calibration of the
[33] I. Amato, R. Colombo, G. Grappiolo, Grain boundary grooving in uranium dioxide,                  diﬀusivity predictions of centipede using approximate Bayesian computation and
     Solid State Commun. 4 (1966) 237–239.                                                            applications in nyx (engineering scale) and xolotl-marmot (meso-scale) simulations,
[34] G.L. Reynolds, The surface self-diﬀusion of uranium dioxide, J. Nucl. Mater. 24                  Tech. Rep., Los Alamos National Lab. (LANL), Los Alamos, NM (United States), 2021,
     (1967) 69–73.                                                                                    https://doi.org/10.2172/1845228, https://www.osti.gov/biblio/1845228.
[35] J. Henney, J. Jones, Surface-diﬀusion studies on 𝑈 𝑂2 and MgO, J. Mater. Sci. 3             [62] A. Booth, A method of calculating ﬁssion gas diﬀusion from UO2 fuel and its appli-
     (1968) 158–164.                                                                                  cation to the X-2-f loop test, Canadian Report CRDC 721, 1957.
[36] P. Maiya, Surface diﬀusion, surface free energy, and grain-boundary free energy of          [63] S.J. Parker, M.W. Anderson, Nuclear science user facilities high performance com-
     uranium dioxide, J. Nucl. Mater. 40 (1) (1971) 57–65.                                            puting: Fy 2022 annual report, Tech. Rep., Idaho National Lab. (INL), Idaho Falls,
[37] M. Marlowe, A. Kaznoﬀ, Tracer study of the surface diﬀusivity of 𝑈 𝑂2 , J. Nucl.                 ID (United States), 2023, https://www.osti.gov/biblio/1964106.
     Mater. 25 (1968) 328–333.
[38] S. Zhou, D. Olander, Tracer surface diﬀusion on uranium dioxide, Surf. Sci. 136
     (1984) 82–102.




                                                                                            14
