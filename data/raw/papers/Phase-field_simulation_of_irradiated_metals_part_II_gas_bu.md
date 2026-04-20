# Phase-field simulation of irradiated metals: part II: gas bubble kinetics

---

                                                                 Computational Materials Science 50 (2011) 960–970



                                                                   Contents lists available at ScienceDirect


                                                      Computational Materials Science
                                               journal homepage: www.elsevier.com/locate/commatsci




Phase-ﬁeld simulation of irradiated metals
Part II: Gas bubble kinetics
Paul C. Millett a,⇑, Anter El-Azab b, Dieter Wolf c
a
  Idaho National Laboratory, Idaho Falls, ID 83415, USA
b
  Florida State University, Tallahassee, FL 32310, USA
c
  Argonne National Laboratory, Argonne, IL 60439, USA



a r t i c l e           i n f o                              a b s t r a c t

Article history:                                             The phase-ﬁeld model developed in Part I of this work is expanded to include ﬁssion gas generation, dif-
Received 14 September 2010                                   fusion, and segregation within bubbles nucleated both homogeneously and heterogeneously along grain
Received in revised form 14 October 2010                     boundaries. Illustrative results are presented that characterize bubble growth and shrinkage, as well as
Accepted 27 October 2010
                                                             the bubble density, size and nucleation rate as a function of the irradiation conditions. Finally, intergran-
Available online 4 December 2010
                                                             ular bubble characteristics such as shape, pinning energy and bubble density are investigated.
                                                                                                                                Ó 2010 Elsevier B.V. All rights reserved.
Keywords:
Phase-ﬁeld simulation
Irradiation damage
Radiation damage




1. Introduction                                                                              to form clusters due to their insolubility in the solid [5]. This clus-
                                                                                             tering can initiate either by chance encounters of the wandering
    The accumulation of gaseous species in nuclear fuel and struc-                           gas atoms (i.e., homogeneous nucleation), or by gas-atom trapping
tural materials leads to deleterious microstructural changes that                            at microstructural segregation sites such as GBs (i.e., heteroge-
are of utmost concern to both ﬁssion and fusion reactor applica-                             neous nucleation). The subsequent growth or shrinkage of a gas
tions [1]. Inert gas elements – such as helium, xenon and krypton                            bubble is governed by the ﬂuxes of vacancies, interstitials, and
– are generated due to ﬁssion reactions in nuclear fuel [2,3]. In                            gas atoms to or away from the bubble surface [6]. Basically, the
addition, transmutation via (n,a) reactions in the metallic cladding                         time rate of change of the volume of a bubble is equal to the differ-
leads to helium production [4]. In general, the precipitation of gas-                        ence in the rates at which vacancies and interstitials are absorbed
eous species into gas-ﬁlled bubbles leads to volumetric swelling in                          at the bubble surface times the (atomic) volume carried by each of
both structural materials and fuels, as well as high-temperature                             these point defects [5]. In addition, gas-atom re-solution can limit
embrittlement and overall loss of mechanical strength in metallic                            bubble growth whereby ﬁssion fragments directly or indirectly
components [1]. The processes of nucleation, growth, migration,                              cause gas atoms to be lost from the bubble [7,8]. If, however, gas
and coalescence of gas-ﬁlled bubbles are all governed by (i) the dy-                         bubbles are located on sinks (such as GBs) that recollect the lost
namic production of point defects (i.e., vacancies, self-interstitials,                      gas atoms, they may grow indeﬁnitely to the point of interconnec-
and gas atoms) by irradiation and (ii) the pre-existing microstruc-                          tion, thus leading to rapid ﬁssion gas release to the exterior of the
tural features of the material (i.e., grain boundaries (GBs), disloca-                       material in the case of fuel [9]. Conversely, the existence of inter-
tion networks, and precipitates). Such features can themselves                               granular gas bubbles can, in turn, inﬂuence GB migration due to
evolve as a result of interaction with point defects. A precise under-                       Zener pinning [10], thus ultimately affecting the microstructural
standing of the inter-dependency of the point and extended de-                               evolution of the material.
fects, and their kinetics, as they relate to gas behavior still                                  In the current paper, we expand the phase-ﬁeld model devel-
remains a very important subject in the ﬁeld of nuclear reactor                              oped in Part I to include gas atom evolution, thus allowing investi-
materials.                                                                                   gations of bubble nucleation and growth in irradiated metals. This
    According to conventional nucleation theory, in the early stages                         phase-ﬁeld model is based on the dynamics of generation, diffu-
of irradiation, gas atoms diffuse throughout the crystal and begin                           sion and reactions of vacancies, gas atoms, and self-interstitials
                                                                                             (to be referred to merely as interstitials from here on) in a single
                                                                                             component, polycrystalline metal. A polycrystal phase-ﬁeld model
    ⇑ Corresponding author.                                                                  [11] is incorporated, thus capturing lenticular-shaped intergranu-
      E-mail address: paul.millett@inl.gov (P.C. Millett).                                   lar bubble formation as well as bubble-induced Zener pinning of

0927-0256/$ - see front matter Ó 2010 Elsevier B.V. All rights reserved.
doi:10.1016/j.commatsci.2010.10.032
                                                     P.C. Millett et al. / Computational Materials Science 50 (2011) 960–970                                                           961


GB migration. This model differs from that of Hu et al. [12], in that                      vacancies, interstitials, and gas atoms in the matrix; it is written
the order parameter g (introduced in Part I) differentiates the bub-                       in the form
bles from the solid, and allows different thermodynamic and ki-
netic descriptions to be applied to each phase throughout space.                           f solid ¼ Efv cv þ Efi ci þ Efg cg þ kB T½cv lnðcv Þ þ ci lnðci Þ þ cg lnðcg Þ
                                                                                                        þ ð1  cv  ci  cg Þ lnð1  cv  ci  cg Þ;                                  ð2Þ

2. Simulation approach                                                                     where Efv , Efi , and Efg are the vacancy, interstitial, and gas formation
                                                                                           energies, respectively, kB is Boltzmann’s constant, and T is the abso-
    In this model, we consider a polycrystalline metal in which bub-                       lute temperature. The entropic term in the brackets in Eq. (2) repre-
bles are considered to be clusters of vacancies that contain a ﬁnite                       sents the conﬁgurational entropy of a defect-disordered crystal,
amount of gas atoms. (The current model is an extension of our                             shown schematically in Fig. 1, consisting of sites that are occupied
previous work [13], which also considered single component met-                            either by a host atom, gas atom, vacancy, or a dumbbell self-inter-
als.) The phase-ﬁeld approach is based on expressing the total free                        stitial defect. Note that this equation assumes that the gas atoms
energy functional F of the heterogeneous material in terms of the                          are substitutional defects that occupy regular lattice sites, which is
free energy of each of its phases and interfaces. Consistent with                          typical of large ﬁssion gases.
the Cahn–Hilliard deﬁnition of free energy for a non-uniform sys-                              The free energy of the bubble phase is deﬁned as
tem [14], we describe the free energy functional of a polycrystal-                                   h                i
line solid consisting of both matrix and bubble phases, in terms                           f bubble ¼ ðcv  1Þ2 þ c2i
of the vacancy concentration ﬁeld cv, the interstitial concentration                                   h                                        i
ﬁeld ci, gas atom concentration ﬁeld cg, an order parameter ﬁeld g                                   þ log cg þ cg kB T ln cg þ cg kB T lnðkB TÞ :                                     ð3Þ
that distinguishes solid and void phases, and a set of order param-
eters /1?P that represent discrete crystallographic (grain)                                    The term in the ﬁrst set of brackets was presented in Part I, in
orientations                                                                               which an energy minimum is located precisely at cv = 1 and
       Z                                                                                   ci = 0. At this minimum, the free energy is exactly equal to zero.
                                                                                          The term in the second set of brackets is the free energy of the
F¼N       hðgÞf solid ðca Þ þ jðgÞf bubble ðca Þ þ f pc ðg; /1!P Þ
         V                                                                                 gas phase within a bubble according to the ideal gas law. Its deri-
                           
         grad
     þ f ðca ; g; /1!P Þ dV:                                                      ð1Þ      vation is given in Appendix A. Here, the free energy is described by
                                                                                           a gas concentration rather than the conventional gas pressure to be
    In this expression, ca represents the set of concentration ﬁelds                       consistent with the use of a concentration variable in the matrix.
(cv, ci, and cg), and N is the number of lattice sites per unit volume                     The use of the ideal gas law is perhaps not appropriate for bubbles
of the crystal and thus all terms under the integral sign represent                        with a high density of gas, in which case the Van der Waals equa-
free energy per lattice site. The ﬁrst three terms in the right-                           tion is more accurate [15], nevertheless, we make use of this deri-
hand-side correspond to the bulk system energy. The interfacial                            vation for the current work.
energy contributions, due to the bubble free surfaces and GBs,                                 To incorporate GBs and their mutual interactions with gas
are accounted for by the gradient term.                                                    bubbles into the model, we employ a conventional polycrystal
    The excess free energy of the solid due to point defects fsolid(ca)                    phase-ﬁeld model, in which a set of order parameters /1?P are
is derived in terms of the enthalpy and entropic contributions of                          used to deﬁne the set of crystallographic grain orientations. The
                                                                                           free energy of the polycrystalline material is deﬁned as

                                                                                                                                                     !2                            !
                                                                                                                                   X
                                                                                                                                   P                             X
                                                                                                                                                                 P
                                                                                           f   polycrystal
                                                                                                             ðg; /1;...;P Þ ¼ 3A         /2k þ   2
                                                                                                                                                 g         4A         /3k þ   3
                                                                                                                                                                               g   :   ð4Þ
                                                                                                                                   k¼1                           k¼1


                                                                                           For g = 0 (i.e., in the solid phase), this equation creates P energy
                                                                                           wells located at {uk=l = 1, uk–l = 0}. For g = 1 (i.e., in the bubble
                                                                                           phase), this equation has one energy well located at /1?P = 0, thus
                                                                                           all grain order parameters go to zero inside a bubble. We note that
                                                                                           this polycrystal model is qualitatively similar (the functional form
                                                                                           differs) to that of Moelans et al. [16] that captures the pinning of
                                                                                           GBs by particles; however, the current model allows for a dynami-
                                                                                           cally-evolving bubble phase. To our knowledge, this is the ﬁrst
                                                                                           phase-ﬁeld model explicitly taking into account dynamically-evolv-
                                                                                           ing gas bubbles interacting with planar defects, such grain
                                                                                           boundaries.
                                                                                               The gradient energy contribution, contributing primarily to gas
                                                                                           bubble free surface energies and GB energies, are accounted for by
                                                                                           the term
                                                                                                        X jw
                                                                                           f grad ¼                 jrwj2 ;                                                            ð5Þ
                                                                                                                2

                                                                                           where w represents the set of concentration ﬁelds (cv, ci, cg) and or-
                                                                                           der parameter ﬁelds (g,/1?P).
                                                                                               Following the standard procedure in the phase-ﬁeld approach,
Fig. 1. Schematic plot illustrating the quasi-lattice representation of vacancy, self-
interstitial, and gas atom defects. The conﬁgurational entropy of this system is
                                                                                           the kinetic equations for the spatial and temporal evolution of
included in Eq. (2), in which each lattice site can be occupied by either an atom, a       the gas concentration ﬁeld (in addition to the vacancy and intersti-
vacancy, a gas atom, or a dumbbell self-interstitial.                                      tial concentrations derived in Part I) has the form
962                                                P.C. Millett et al. / Computational Materials Science 50 (2011) 960–970

                    
@cg            1 dF
    ¼ r  Mg r         þ ng ðr; tÞ þ Pg ðr; tÞ:                                ð6Þ
@t             N dcg
      The gas atom mobility is deﬁned as
        Dg c g
Mg ¼           ;                                                               ð7Þ
        kB T
where Dg is the gas atom diffusivity in the matrix. We note that, for
a substitutional gas atom (as assumed in Eq. (2)), the gas mobility
should depend on cv in addition to cg. This paper does not account
for this point. Because these concentrations remain fairly dilute in
the solid, this approximation is valid to a ﬁrst order analysis. In
the bubble phase, the gas can be assumed to instantly equilibrate
when considering solid-state diffusion time scales. To account for
this, the gas concentration inside each bubble is evenly distributed
to provide a ﬂat proﬁle within each bubble. The gas concentration
within the bubbles will vary from bubble to bubble.
   Bubble re-solution due to ﬁssion-fragment bombardment [5] is
not included in the current model. This process can conceivably be
including by adding a term that re-distributes ﬁssion gas from the
bubbles to the surrounding solid regions. The exclusion of ﬁssion
gas re-solution will result in higher bubble nucleation rates and
growth rates predicted by the simulations.
   The order parameter ﬁelds that deﬁne the distinct grain orien-
tations /i also evolve according to a set of Allen–Cahn equations
@/i ðr; tÞ       dF
           ¼ L/     ;                                                         ð8Þ
  @t             d/i
where L/ is the grain boundary mobility. In the present work, Eq. (6)
can be expressed in non-dimensional units following Part I leading
to
                     
@cg   ~  M
     ¼r       ~ 1 dF þ ~fð~r; ~tÞ þ P
           ~ gr                     ~ g ð~r; ~tÞ                               ð9Þ
@ t~            ~ dcg
                N
                   
         ~ ¼ l r is the dimensionless gradient operator. Energy is
where r
                                                                                         Fig. 2. Increase of gas concentration inside an initially-empty void surrounded by a
kept in units of eV. In all of the simulations below, the grid spacing                   solid with a supersaturated gas concentration. The top ﬁgures show the evolution of
is Dx = k, the time step is Dt = 0.001 s, and the gradient terms are                     (a) vacancy and (b) gas atom concentration ﬁelds. (c) Plots of the conserved
jv = ji = jg = jg = j/ = 1.0 eV k2.                                                      concentration ﬁelds, cv, ci, cg, along a cross-sectional slice through the centerline of
   In Sections 4 and 5 below, we vary the Frenkel pair production                        the bubble throughout time. The absorption of gas atoms into the void creates a
                                                                                         gradient in the gas concentration in the adjacent solid region.
rate and the gas atom production rate independently. In nuclear
reactor conditions, these two are coupled to some degree; how-
ever, we disregard this coupling which is more applicable to                             to observe any change in bubble size. For the simulations shown in
dual-beam ion irradiation. Varying these production rates inde-                          Figs. 2–4, the energies of formation of the vacancies and intersti-
pendently, as will be shown below, can lead to interesting results.                      tials in the crystal are taken as Efv ¼ Efi = 0.8 eV corresponding to
                                                                                         equilibrium intrinsic defect concentrations of ceq            eq
                                                                                                                                                 v ¼ ci = 6.9 
                                                                                            4
3. Gas bubble growth and shrinkage                                                       10 (the thermal energy in all simulations within this paper is ta-
                                                                                         ken as kBT = 0.11 eV, corresponding to a temperature of
    The size evolution of a gas bubble existing in a crystalline solid                   T = 1276 K). The gas atom defect energy in the solid is also taken
is governed by the ﬂux rate of vacancies and interstitials to its sur-                   as Efg = 0.8 eV. The reference chemical potential of the gas atoms
face. A net absorption of vacancies by the bubble will result in bub-                    in the gas phase is log = 0.4 eV throughout this paper (this value
ble growth, while conversely a net absorption of interstitials                           was arbitrarily chosen, with the condition that it be less than Efg ).
results in bubble shrinkage. Furthermore, the density of gas atoms                       The bulk recombination term is turned off (i.e., Rbulk = 0) so that
within the bubble will ﬂuctuate in time based on (i) the ﬂux of gas                      cv in the bulk remains constant, however surface recombination
atoms to the bubble and (ii) the change in the bubble volume itself.                     is activated by assigning a value of Rsurf = 5 s1. The supersatura-
In order to validate that the current model can appropriately cap-                       tion of the gas in the solid is Sg = 120 (this supersaturation is calcu-
ture bubble growth and shrinkage based on the vacancy and self-                          lated with the supposed ceq               f
                                                                                                                     g based on Eg , although there is no actual
interstitial concentrations in the surrounding solid, as well as the                     equilibrium concentration of impurity gas atoms in a crystal).
direct dependence of this on the bubble’s gas concentration, we                              Fig. 2a and b are contour plots that illustrate how the vacancy
have simulated three benchmark cases, which are described below.                         concentration (3a) and the gas atom concentration (3b) evolve in
    For the ﬁrst benchmark case, we have initialized the system to                       time. As can be seen, the gas concentration within the void in-
consist of a single void with a diameter of 20 k located at the center                   creases in time due to the diffusional ﬂux of gas atoms through
of the domain with periodic boundary conditions, as shown in                             the solid towards the bubble surface. The bubble volume, however,
Fig. 2a. Initially, the void itself contains no gas atoms, however,                      does not change in time due to the fact that there is not an excess
the surrounding solid does contain a ﬁnite concentration of gas                          quantity of vacancies or interstitials in the solid. Therefore, as more
atoms. The vacancy and interstitial concentrations in the solid                          gas atoms enter the bubble, which has a constant size, the gas den-
are at their equilibrium values, respectively, thus we do not expect                     sity in the bubble increases. This is shown quantitatively in Fig. 2c
                                                       P.C. Millett et al. / Computational Materials Science 50 (2011) 960–970                                                  963


which shows plots of the cv, ci, and cg concentration ﬁelds along a
cross-sectional slice through the centerline of the bubble through-
out time. In addition to the increase in gas concentration inside the
bubble, in the nearby solid, a gradient in gas concentration devel-
ops due to the depletion of gas atoms from the solid to the bubble.
This gradient drives an on-going ﬂux of gas atoms to the bubble
surface, which continues until the chemical potential of gas atoms
in the bubble equals that in the solid. The last snapshot in Fig. 2
does not correspond to the fully equilibrated system, i.e., more
time is needed before the gas concentration is done evolving (this
is also true of Figs. 3 and 4 below).
    The second benchmark case, shown in Fig. 3, consists of a gas
bubble that, initially, has a smaller diameter of 10 k. The initial va-
cancy concentration in the solid is supersaturated by Sv = 120. In
addition, the gas concentration in the bubble is initialized at a high
value corresponding to the case of an over-pressurized bubble. As
shown in Fig. 3a and b, the bubble grows in size due to the absorp-
tion of vacancies from the solid. Furthermore, as the bubble’s area
increases, the concentration of gas inside the bubble decreases. The
total concentration of gas is conserved, thus this decrease in bubble
gas concentration is solely due to the increase in bubble size, which
is in turn governed by the diffusional ﬂux of vacancies to the bub-
ble surface.
    Contrary to the above case of void growth in a supersaturated
vacancy ﬁeld, a system that is supersaturated with interstitials will




                                                                                             Fig. 4. Shrinkage of a bubble due to a supersaturated self-interstitial concentration
                                                                                             in the solid. The gas concentration in the bubble, which is initially under-saturated,
                                                                                             increases due to the decrease in bubble volume. The top ﬁgures show the evolution
                                                                                             of (a) vacancy and (b) gas atom concentration ﬁelds. (c) Plots of the conserved
                                                                                             concentration ﬁelds, cv, ci, cg, along a cross-sectional slice through the centerline of
                                                                                             the bubble throughout time.




                                                                                             drive a void to shrink in size due to the continual occupation of
                                                                                             empty lattice sites on the void surface by interstitials. This is essen-
                                                                                             tially identical to vacancy-interstitial recombination in the bulk, al-
                                                                                             beit the rate may be higher due to the unique structure of the free
                                                                                             surface. As mentioned in Part I, we consider the overall recombina-
                                                                                             tion term to have contributions from both the bulk and the free
                                                                                             surfaces. Fig. 4 shows the shrinkage of a bubble surrounded by a
                                                                                             solid containing a supersaturation of interstitials. The vacancy con-
                                                                                             centration in the bulk is initialized to equilibrium, where it roughly
                                                                                             remains throughout time (again, bulk recombination is turned off
                                                                                             in this simulation). As can be seen in Fig. 4b, as time progresses,
                                                                                             the interstitial ﬁeld becomes depleted adjacent to the bubble due
                                                                                             to surface recombination, which in turn shrinks the bubble. The
                                                                                             resultant gradient in ci drives more interstitials to the bubble sur-
                                                                                             face, where they continue to annihilate the vacancies that consti-
                                                                                             tute the bubble. Furthermore, the gas density in the bubble
                                                                                             increases in time due to the decreasing bubble size. The plots in
                                                                                             Fig. 4c illustrates the evolution in both cv, ci, and cg across the cen-
Fig. 3. Growth of a bubble due to a supersaturated vacancy concentration in the              terline of the bubble as it shrinks in time, indicating the gradient in
solid. The gas concentration in the bubble, which is initially over-saturated,               ci, the concurrent bubble shrinkage denoted by the vacancy ﬁeld, as
decreases due to the increase in bubble volume. The top ﬁgures show the evolution
of (a) vacancy and (b) gas atom concentration ﬁelds. (c) Plots of the conserved
                                                                                             well as the increasing gas density in the bubble.
concentration ﬁelds, cv, ci, cg, along a cross-sectional slice through the centerline of          The use of an order parameter g to deﬁne the bubble phase al-
the bubble throughout time.                                                                  lows us to distinguish the bubble and solid phases, and allows for
964                                                   P.C. Millett et al. / Computational Materials Science 50 (2011) 960–970


different conditions to apply in each region. For example, in the so-                        atoms from the solid. In the current section, we will investigate the
lid (where Eq. (2) applies), we assume gas atoms are substitutional,                         development and evolution of bubble microstructures during the
and the total vacancy, interstitial, gas, and atom concentrations                            on-going production of defects during irradiation. In these simula-
add up to one. However, in the bubble phase (where Eq. (3) ap-                               tions, the initial domain is entirely solid material, with the equilib-
plies), we assume gas atoms occupy off-lattice sites, hence the con-                         rium vacancy and interstitial concentrations (there is zero gas
centrations can add up to larger than one.                                                   concentration initially). The defect formation energies are assigned
                                                                                             values of Efv = 0.8 eV, Efi = 1.5 eV, and Efg = 1.2 eV; and the defect dif-
                                                                                             fusivities are assigned values of ~    Dv ¼ D ~ g ¼ 1, and ~
                                                                                                                                                        Di ¼ 4; in most
4. Gas bubble evolution during irradiation                                                   metals, Efi > Efv and Di > Dv, and in this section we assign these val-
                                                                                             ues accordingly, although the values do not correlate with a spe-
   The on-going production of point defects in irradiated materials                          ciﬁc material. Furthermore, the bulk recombination term is
eventually leads to the clustering of individual defect species, i.e.,                       turned on, Rbulk = 1 s1, in addition to the surface recombination
vacancies cluster to form voids and interstitials cluster to form dis-                       term that was solely activated in the simulations of Section 3.
location loops. We have veriﬁed in Part I that the current phase-                                Fig. 5 shows the evolution of g, cv, ci, and cg at progressive in-
ﬁeld model captures accurately the growth (shrinkage) rates of                               stances in time during an irradiation simulation. These vacancies
pre-existing voids due to the net ﬂuxes of vacancies (interstitials)                         and interstitials are produced stochastically in both space and time
to their free surfaces, without irradiation. In the previous section                         according to Part I. The gas production rate is assumed to by spa-
of this paper, we have veriﬁed that the gas concentration within                             tially uniform within the solid (g < 0.8) and Pgas has units of cg
a bubble is allowed to increase or decrease according to the shrink-                         per time. As seen in Fig. 5, the ongoing production of vacancies
age or growth of the bubble, as well as the absorption of excess gas                         and interstitials eventually leads to the nucleation of gas bubbles.




Fig. 5. Snapshots showing the nucleation and growth of bubbles in the presence of on-going cascades and gas production. The top-to-bottom rows represent the (a) g, (b) cv,
(c) ci, and (d) cg ﬁelds. During the simulation, an interstitial production bias of 0.9 is assumed (i.e., there are 10% more vacancies introduced into the system), the net effect of
which is similar to a dislocation bias. Within the voids, the vacancy concentration cv = 1, the interstitial concentration ci = 0, and the gas concentration varies.
                                                       P.C. Millett et al. / Computational Materials Science 50 (2011) 960–970                                                      965




Fig. 6. The evolution of (a), (d), (g) porosity, (b), (e), (h) bubble density, and (c), (f) average gas concentration inside the bubbles throughout time. The top row ((a), (b), (c))
represents a gas production rate of 1.0  104 cg/s, while the middle row ((d), (e), (f)) represents a gas production rate of 2.0  105 cg/s. In (g) and (h), the gas production rate
is zero. As shown in (i), for increasing gas production rate, the bubble density at the end of stage II increases while the average bubble size decreases. Also, as shown in (c) and
(f), the gas concentration within bubbles decreases during stage II (nucleation and growth) due to the relatively rapid bubble growth while the bubbles are still small.




The top-to-bottom rows in Fig. 5 correspond to the g, cv, ci, and cg                          and average gas concentration within the bubbles (cg ) at regular
contour plots at progressive instances in time (the contour inter-                            intervals in time. This data is shown in Fig. 6. We vary two key
vals are indicated on the left side of the ﬁgure). As the voids nucle-                        parameters in this set of simulations: (i) the cascade-induced dis-
ate and grow, the interstitial concentration inside the voids is                              placement rate (taking on values of either K = 2.3  103 dpa/s or
reduced to zero, while the vacancy concentration evolves to a value                           K = 1.0  103 dpa/s), and (ii) the gas production rate (taking on
of one. The gas concentration in the solid and within the bubbles                             values of Pgas = 0.0, 2.0  105, and 1.0  104 cg/s).
varies from bubble to bubble and throughout the solid based on                                   The top row of Fig. 6 depicts the overall porosity (Fig. 6a), the
the local history of cascades and the spatial proximity of nearby                             bubble density (Fig. 6b), and the average gas concentration within
bubbles. The production bias mentioned above ensures that a high-
er net ﬂux of vacancies compared to interstitials arrives at the bub-                         Table 1
ble surfaces, thus allowing bubble growth. During the intermediate                            Values of k from Eq. (10) from ﬁtting to the data shown in Fig. 6 and calculated from
                                                                                              Eq. (11) for varying dpa rates and gas production rates. Also shown are the gas bubble
stages, the processes of bubble nucleation and growth are occur-
                                                                                              nucleation rates.
ring simultaneously while the bubble density is still low. In the lat-
ter stages, when the bubble density has increased, nucleation                                    K (dpa/s)       Pgas (cg/s)   k (ﬁt) (s3)   k (calculated) (s3)    J (k2 s1)

ceases and the evolution is controlled by growth and coarsening.                                 1.0  10   3
                                                                                                                 0.0           1.55  10 7
                                                                                                                                              1.28  10 7
                                                                                                                                                                      1.22  105
As we show below, the gas concentration within the bubbles also                                                  2.0  105    2.97  107    1.83  107             1.75  105
                                                                                                                 1.0  104    2.40  107    3.38  107             3.23  105
evolves with time according to the production rate of gas atoms
as well as the average bubble growth rate.                                                       2.3  103      0.0           4.97  107    3.21  107             3.07  105
                                                                                                                 2.0  105    4.60  107    3.48  107             3.32  105
   In order to quantify the bubble microstructure throughout the
                                                                                                                 1.0  104    8.46  107    3.65  107             3.49  105
simulation, we have calculated the porosity, void number density,
966                                              P.C. Millett et al. / Computational Materials Science 50 (2011) 960–970




Fig. 7. (a) The nucleation rate of gas bubbles increases with increasing gas production rate for both displacement rates. This effect is more dramatic for the lower
displacement rate (K = 1.0  103 dpa/s). (b) The average gas concentration within the bubbles decreases with increasing bubble diameter.




the bubbles (Fig. 6c) for a gas production rate of 1.0  104 cg/s.                    III, however, cg begins to increase gradually and eventually levels
The porosity versus time plot (Fig. 6a) reveals that the bubble                        off. This trend occurs for both displacement rates, however the
kinetics can be subdivided into three distinct regimes: stage I                        magnitude of cg is lower for the higher displacement rate
(incubation), stage II (nucleation and growth), and stage III (coars-                  (K = 2.3  103 dpa/s) due to the fact that nucleation occurs earlier
ening). This evolution is similar to our previous simulations in Part                  when the overall gas concentration is lower.
I. During stage II, the porosity follows an S-shaped curve character-                       The middle row of Fig. 6 displays similar results, although for a
istic of the Johnson–Mehl–Avarami equation [17]                                        lower gas production rate, 2.0  105 cg/s. The results are qualita-
      h             i                                                                tively similar to the higher gas production rate, with the exception
                   3
p ¼ po 1  exp kt      ;                                                  ð10Þ        that the nucleation rates have decreased for both displacement
                                                                                       rates. In addition, the cg values are generally lower, which is to
where po is the porosity at the end of stage II, and k is a constant                   be expected for a lower gas production rate. On the bottom row,
characteristic of the nucleation kinetics in the system, which for a                   Fig. 6g and h shows the porosity and bubble density evolution
2D domain, is deﬁned as                                                                for the case of zero gas production. We see again that the bubble
                                                                                       nucleation rates have decreased relative to the cases in which
      p _2                                                                             gas is produced.
k¼        R J:                                                             ð11Þ
      3                                                                                     In Fig. 6i, the bubble density and the average bubble diameter
     In this equation, R_ is the void radius growth rate and J is the                  are plotted as a function of gas production rate. These values are
nucleation rate. The dashed lines in Fig. 6a, d, and g within the                      taken at the end of stage II, when nucleation ceases. We see a gen-
stage II regimes represent ﬁts of the data to Eq. (10). For                            eral trend of increasing bubble density and decreasing bubble
K = 2.3  103 dpa/s, these ﬁts yield values of k = 4.97  107,                       diameter with increasing gas production rate. This is in agreement
4.60  107, and 8.46  107 s3 for Pgas = 0.0, 2.0  105, and                       with experimental observations [1]. The generally-accepted expla-
1.0  104 cg/s, respectively. For K = 1.0  103 dpa/s, these ﬁts                     nation for this is that gas atoms act as trapping sites for vacancies,
yield values of k = 1.55  107, 2.97  107, and 2.40  107 s3                      and therefore they represent nucleation sites for bubbles. In our
for Pgas = 0.0, 2.0  105, and 1.0  104 cg/s, respectively. This data               simulations, the presence of gas atoms increases the free energy
is displayed in Table 1.                                                               of the solid phase further away from equilibrium. Therefore, a
     The bubble nucleation rates, J, are obtained from Fig. 6b, e, and                 smaller thermal ﬂuctuation, or cascade event, is required to create
h, in which the dashed lines are linear ﬁts representing the quasi-                    a nucleation event.
steady-state nucleation regime. They yield nucleation rates of                              In addition to an increase in bubble density with increasing gas
J = 1.22  105 k2s1 (Pgas = 0.0), 1.75  105 k 2s1 (Pgas = 2.0                  production rate, the bubble nucleation rates (or the slopes of
105), and 3.23  105 k2s1 (Pgas = 1.0  104) for K = 1.0                         Fig. 6b, e, and h) also increase with increasing gas production rate.
103 dpa/s; and J = 3.07  105 k2s1 (Pgas = 0.0), 3.32  105                       This is shown in Fig. 7a for both displacement rates. Interestingly,
k2s1 (Pgas = 2.0  105), and 3.49  105 k2s1 (Pgas = 1.0                        the dependency of J (as well as the bubble density and bubble size)
104) for K = 2.3  103 dpa/s. Please see Table 1. Taking into con-                   on the gas production rate is higher for the lower displacement
sideration the bubble growth rate of 0.1 k/s (obtained from mea-                       rate. This is evident by the larger absolute values of the slopes
surements on the smallest voids in the simulations), the                               in Figs. 6i and 7a for K = 1.0  103 dpa/s, relative to K = 2.3 
analytical values of k are obtained from Eq. (11). For                                 103 dpa/s. Conceivably, this is perhaps due to the fact that bubble
K = 2.3  103 dpa/s, they are k = 3.21  107, 3.48  107, and                       nucleation initiates early for the higher displacement rate, when
3.65  107 s3 for Pgas = 0.0, 2.0  105, and 1.0  104 cg/s,                       the gas concentration is smaller.
respectively. For K = 1.0  103 dpa/s, they are k = 1.28  107,                           In Fig. 7b, the average gas concentration within the bubbles, cg ,
1.83  107, and 3.38  107 s3 for Pgas = 0.0, 2.0  105, and                       is plotted as a function of the bubble diameter. This data is for a gas
1.0  104 cg/s, respectively. All of these values are within a factor                 production rate of 2.0  105 cg/s and a displacement rate of
of two of the ﬁtted values obtained from Fig. 6a, d, and g.                            K = 2.3  103 dpa/s. For these conditions, cg decreases monotoni-
     Fig. 6c shows the average gas concentration inside the bubbles                    cally with increasing bubble size. This result is in accord with the
(cg ) as a function of time (this value is averaged over all the bub-                 data shown in Fig. 6f, in which cg decreases with time. As men-
bles in the domain). Interestingly, during the stage II regime, in                     tioned earlier, this decrease in cg with increasing bubble size is ex-
which the bubble growth rate is highest, the gas density decreases                     plained by a higher ﬂux of vacancies than gas atoms to the growing
from the initial value at the very onset of nucleation. This decrease                  bubbles. Had the gas production rate been considerably higher
occurs due to a faster bubble absorption rate of vacancies com-                        than the rate of increase in vacancy supersaturation (taking into
pared to gas atoms. Thus, the gas density decreases. During stage                      consideration vacancy-interstitial recombination), this trend may
                                                     P.C. Millett et al. / Computational Materials Science 50 (2011) 960–970                                              967


actually differ; although in this work we did not simulate such
conditions.


5. Intergranular gas bubbles

    Extended microstructural defects such as GBs and dislocations
strongly affect bubble structure evolution in irradiated materials
due to their role as point defect sinks, as well as the inherent fact
that impurity atom formation energies are lower at these features
compared to the bulk. It is commonly believed that GBs act as
heterogeneous nucleation sites for ﬁssion-gas bubbles; this being
widely supported by many experimental observations of intergran-
ular bubbles that are many times larger than their intragranular
counterparts [2,3,18]. As intergranular bubbles grow to micron-
sizes and larger, their migration and coalescence on the GB faces,
edges, and corners leads ultimately to an interconnected porosity
that allows rapid ﬁssion gas release to the exterior of the material
[2,3]. In addition, due to the triple junctions between bubble free
surfaces and the GB, the inherent bubble shape is lenticular rather
than spherical in order to minimize the interfacial energies of GB
and free surfaces. Furthermore, the presence of intergranular
bubbles effectively pins GB migration, according to the Zener drag
theory [10]. As we show below, the current model is able to capture
these important distinctions of intergranular bubble physics.
    Fig. 8 shows the interaction of a single GB with a stationary
bubble that does not evolve (i.e., change shape) in time. (Here,
the concentration ﬁelds and the g-ﬁeld are not updated in time;
only the /-ﬁelds representing grains 1 and 2 are solved for in time).
In Fig. 8a, the equilibrium GB shapes are shown for different rela-                        Fig. 9. Evolution of the shape of a gas bubble on a GB from circular to lenticular
tive positions of the bubble. We see that, for this stationary bubble,                     (equilibrium) due to the GB energy. The (a) /, (b) cv, and (c) cg ﬁelds are shown
the GB always intersects the bubble surface at a 90° angle. (Note                          throughout the evolution. (d) The dihedral angle, h, evolves exponentially from 90°
that in these ﬁgures, the GB is not made to migrate across the do-                         to approximately 120°.

main, rather the initial position of the GB is changed from left to
right). In Fig. 8b, the pinning energy that the bubble exerts on                           sults obtained from simulation, and the dashed line corresponds
the GB is plotted as a function of bubble radius. This pinning en-                         to the theory, showing a close agreement. This result is entirely
ergy is the difference between the system shown in the center of                           due to the interaction in the free energy term of Eq. (4) between
Fig. 8a and that shown on the far left of Fig. 8a. According to Zener                      the order parameter representing the bubbles, g, and the order
[10,16], it is equal to the amount of GB that is eliminated by the                         parameters representing the grains, /.
presence of the bubble multiplied by the GB energy. For 2D, this                               With veriﬁcation that the current model accurately captures the
is equal to 2rrgb. The data points in Fig. 8b correspond to the re-                        pinning effect of a gas bubble on a GB, we now focus on the inﬂu-
                                                                                           ence of a GB on the shape of a gas bubble. As mentioned above, an
                                                                                           intergranular bubble will assume a lenticular shape due to the Her-
                                                                                           ring relation [19] governing the dihedral angles existing at the tri-
                                                                                           ple junction between the free surfaces and the GB. To verify that
                                                                                           we correctly capture this, we have performed a simulation of a
                                                                                           bicrystal with a single, initially-circular gas bubble residing on
                                                                                           the GB. As shown in Fig. 9a, the bubble evolves from a circular
                                                                                           shape to a lenticular shape as time progresses. Fig. 9b and c illus-
                                                                                           trates that the vacancy and gas atom concentrations, respectively,
                                                                                           evolve accordingly. The evolution of the triple junction angle, h, is
                                                                                           shown versus time in Fig. 9b, illustrating an exponential approach
                                                                                           from h = 90° to h  120°.
                                                                                               With the above analysis of the interaction between pre-existing
                                                                                           gas bubbles and GBs, we now focus on bubble nucleation and
                                                                                           growth in polycrystalline microstructures. Here, we re-activate
                                                                                           the irradiation terms. Fig. 10 illustrates the nucleation and growth
                                                                                           of intergranular gas bubbles due to the ongoing production of Fren-
                                                                                           kel pair defects and gas atoms. The simulation domain is again
                                                                                           periodic in both directions (lx = ly = 6 lm) and contains 40 grains
                                                                                           (i.e., P = 40 in Eq. (4), with isotropic GB properties, including energy
                                                                                           and mobility) with an average diameter of d = 1.1 lm. The gas
Fig. 8. (a) GB pinning due to a stationary bubble (that does not evolve in time). (b)      atom formation energy is reduced in the GBs by the following
The pinning energy is equal to the GB energy, gb, multiplied by the length (for 2D) of
the missing GB segment corresponding to the bubble diameter. The open circles
                                                                                           equation
represent values calculated from the model and the dashed line is the theory               f ¼ Ef  U;
according to Zener [10].
                                                                                           Eg    g                                                                      ð12Þ
968                                                  P.C. Millett et al. / Computational Materials Science 50 (2011) 960–970


where the factor U is deﬁned in Part I and is equal to 1.0 in the                           dEfg = 1.2 eV, and the recombination rates are Rbulk = 1.0 s1 and
grain interiors and as low as 0.5 in the GBs and triple junctions.                          Rsurf = 5.0 s1.
This results in preferential segregation of the gas atoms to the                                Fig. 10 shows sequential snapshots of the preferential nucle-
GB regions. The formation energies are Efv = 0.8 eV, Efi = 1.5 eV, an-                      ation of bubbles on GB and TJ regions, resulting from the enhanced




Fig. 10. (a)–(d) Snapshots throughout time of the nucleation and growth of intergranular gas bubbles in a polycrystalline grain structure, while (e) is a close-up view. Bubbles
existing on GBs are lenticular shaped, whereas bubbles on triple junctions have a curved triangular shape. (f) A microscopy image of intergranular bubbles in UO2 taken from
[2].




Fig. 11. Characteristics of intergranular gas bubbles for different grain sizes. The (a) porosity, (b) bubble density, and (c) gas concentration within the bubbles does not vary
substantially for the different grain sizes. However, as the grain size increases, the (d) average bubble diameter increases, the (e) average GB bubble spacing decreases, and the
(f) GB bubble coverage increases. (The data for (d), (e), and (f) are taken at the end of the simulations, t = 800 s).
                                            P.C. Millett et al. / Computational Materials Science 50 (2011) 960–970                                                 969


gas atom concentration at these extended defects. As can be seen                  turn, dictated by this change in bubble size, as well as by the ﬂux
in the close-up view in Fig. 10e, bubbles existing on GBs are lentic-             of gas atoms to the bubble.
ular shaped, whereas bubbles on TJs have a curved triangular                          In single crystal simulations, the porosity evolved in three dis-
shape. In Fig. 10f, a micrograph image of intergranular bubbles in                tinct stages during irradiation: stage I (incubation), stage II (nucle-
UO2 (taken from Ref. [2]) illustrates the qualitative similarities be-            ation and growth), and stage III (coarsening). The bubble
tween the bubble structures in terms of the relative size of the                  nucleation rate is shown to increase with increasing displacement
bubbles with respect to the grain size, as well as the bubble shapes.             rate as well as gas production rate. Increasing gas production rate
Also note that, in the simulations, bubbles within the grain interi-              is also shown to increase the bubble density and decrease the bub-
ors have also begun to nucleate, although their shapes remain cir-                ble size. Furthermore, at the early stages of bubble growth, the gas
cular, as would be expected.                                                      density within the bubbles (cg ) decreases due to a higher ﬂux of
    In Fig. 11, we analyze the intergranular bubble characteristics               vacancies, compared to gas atoms, to the bubble surfaces.
for various grain sizes. The top row, Fig. 11a–c shows the porosity,                  In polycrystal simulations, the gas atom formation energy is de-
bubble density, and cg throughout time for an average grain size                 creased within the GB and triple junction regions, leading to pref-
between 37 k < d < 111 k. Each of these simulations are run                       erential segregation and heterogeneous nucleation at these
with identical irradiation conditions of K = 1.0  103 dpa/s and                 features. During intergranular bubble growth, the bubbles retain
Pgas = 8.2  106 cg/s. We observe that the porosity, bubble density,             their equilibrium lenticular shapes on GB planes, and curved trian-
and cg do not vary substantially with the changing grain size (the               gular shapes on triple junctions. As the grain size is increased, the
exception is the smallest grain size, d = 37 k, in which the increase             porosity and nucleation rates remain constant; however, the aver-
in porosity has a slightly slower rate, although bubble nucleation                age bubble size and GB bubble coverage increase, while the aver-
rate is similar to the other grain sizes). The average gas concentra-             age GB bubble spacing decreases.
tion inside the bubbles (Fig. 11c) grows most rapid at the onset of
nucleation, and saturates at the later stages, in a very similar man-             Acknowledgements
ner for each grain size. Furthermore, the bubble nucleation rates,
obtained from Fig. 11b, do not vary substantially with grain size.                   This work was supported through the INL Laboratory Directed
    However, when we plot the average GB bubble diameter                          Research and Development program under DOE Idaho Operations
(Fig. 11d), the average spacing on the GB lines (Fig. 11e), and the               Ofﬁce contract no. DE-AC07-051D14517V. We also acknowledge
GB bubble coverage (percentage of GB length occupied by bubbles)                  support from two DOE programs: the Energy Frontier Research
(Fig. 11f), we see clear trends in each with respect to the grain size.           Center (EFRC) for Materials Science of Nuclear Fuel and the Nuclear
With increasing grain size, the intergranular bubble diameter in-                 Energy Modeling and Simulation (NEAMS) program (Cetin Unal as
creases, the intergranular bubble spacing decreases, and the GB                   Fuels IPSC program lead). In addition, this manuscript beneﬁted
bubble coverage increases. Considering that the porosity is basi-                 from technical discussions with Michael Tonks (INL) and Srujan
cally equal for each grain size at the end of the simulations, these              Rokkam (FSU).
trends can be rationalized by the fact that the total GB density is
lower for the larger grain size. Therefore, for the same porosity                 Appendix A. Free energy of ideal gas
and overall bubble density, and considering that virtually all bub-
bles reside on the GBs, bubbles should be closer spaced and larger                   The free energy of the gas phase with respect to the gas concen-
for larger grain sizes. This, in turn, results in a higher GB coverage            tration is derived below. We start with the total Gibb’s free energy
of bubbles.                                                                       [20] assuming an ideal gas law
    Interestingly, it appears that in the polycrystal specimens, the
nucleation stage has yet to saturate, yielding only the ﬁrst half of              Gðp; TÞ ¼ ngo þ nRT ln p;                                                      ðA1Þ
an S-shaped curve (Fig. 11a). We have observed that at about the
                                                                                  where p is the pressure, n is the number moles, go is a reference mo-
time that nucleation ceases on the GBs, nucleation events begin
                                                                                  lar chemical potential, and R is the universal gas constant. This
to occur in the grain interiors. So, the system as a whole does not
                                                                                  equation can be re-written to obtain a volumetric energy density
decelerate the porosity development. Eventually, nucleation in                                                              
both the grain interiors and the GBs will stop, at which time the                                    n                  nAv
                                                                                  gðp; TÞ ¼          bub
                                                                                                         Av log þ        bub
                                                                                                                              kB T ln p;                          ðA2Þ
system will truly enter a coarsening stage.                                                     V                   V
                                                                                  where Av is Avogadro’s number, Vbub is the volume of the bubble,
                                                                                  and log is a reference atomic chemical potential of the gas. In terms
                                                                                  of gas concentration, the equation is now written as
6. Conclusions
                                                                                  gðp; TÞ ¼ cg log þ cg kB T ln p:                                                ðA3Þ
    The phase-ﬁeld model presented here extends our previous
model in Part I for pure metals by incorporating ﬁssion gas atoms                     Using the ideal gas law, the gas pressure is equal to
in a manner that distinguishes their point defect energetics and
                                                                                                   
                                                                                            nAv
kinetics in the solid and gas bubble phases. This is accomplished                 p¼          bub
                                                                                                     kB T ¼ cg kB T;                                              ðA4Þ
                                                                                          V
by the use of a long-range order parameter, g(r,t), that spatially dif-
ferentiates the two phases throughout the simulation domain. This                 and by substituting (A4) into (A3), we arrive at
is a key feature that distinguishes the current model with a previ-
                                                                                  f b ðcg Þ ¼ log cg þ cg kB T ln cg þ cg kB T lnðkB TÞ:                          ðA5Þ
ous phase-ﬁeld model [12] for ﬁssion gas behavior in irradiated
materials, in which a non-conserved order parameter is omitted.
In addition, the g-ﬁeld in the current model allows for a proper                  References
interaction between gas bubbles and GBs in terms of the GB pin-
ning energies and the equilibrium bubble shapes.                                   [1] H. Trinkaus, B.N. Singh, J. Nucl. Mater. 323 (2003) 229.
    The rate of bubble growth or shrinkage, in the bulk or on GBs, is              [2] I. Zacharie, S. Lansiart, P. Combette, M. Trotabas, M. Coster, M. Groos, J. Nucl.
                                                                                       Mater. 255 (1998) 85.
controlled solely by the ﬂux of vacancies and interstitials to the                 [3] S.B. Fisher et al., J. Nucl. Mater. 306 (2002) 153.
bubble surfaces. The gas concentration within the bubbles is, in                   [4] H. Ullmaier, Nucl. Fusion 24 (1984) 1039.
970                                                 P.C. Millett et al. / Computational Materials Science 50 (2011) 960–970


 [5] D.R. Olander, Fundamental Aspects of Nuclear Reactor Fuel Elements (US-DOE,          [14] J.W. Cahn, J.E. Hilliard, J. Chem. Phys. 28 (1958) 258.
     1985).                                                                               [15] L.D. Landau, E.M. Lifshitz, Statistical Physics, third ed., Elsevier, Burlington, MA,
 [6] K. Morishita, R. Sugano, J. Nucl. Mater. 353 (2006) 52.                                   1980.
 [7] J.A. Turnbull, J. Nucl. Mater. 38 (1971) 203.                                        [16] N. Moelans, B. Blanpain, P. Wollants, Acta Mater. 53 (2005) 1771.
 [8] M.H. Wood, J. Nucl. Mater. 82 (1979) 264.                                            [17] R.W. Ballufﬁ, S.M. Allen, W.C. Carter, Kinetics of Materials, Wiley, Hoboken,
 [9] J. Rest, J. Nucl. Mater. 321 (2003) 305.                                                  2005.
[10] C. Smith, Trans. Metall. Soc. AIME 175 (1948) 15.                                    [18] S. Fréchard, M. Walls, M. Kociak, J.P. Chevalier, J. Henry, D. Gorse, J. Nucl. Mater.
[11] L.Q. Chen, Y. Yang, Phys. Rev. B 50 (1994) 15752.                                         393 (2009) 102.
[12] S. Hu, C.H. Henager, H.L. Heinisch, M. Stan, M.I. Baskes, S.M. Valone, J. Nucl.      [19] C. Herring, in: The Physics of Powder Metallurgy, McGraw-Hill, New York,
     Mater. 392 (2009) 292.                                                                    1951, pp. 143–179.
[13] P.C. Millett, S. Rokkam, A. El-Azab, D. Wolf, Mod. Sim. Mater. Sci. Eng. 17          [20] D.R. Gaskell, DR Introduction to Metallurgical Thermodynamics, second ed.,
     (2009) 064003.                                                                            Hemisphere, Publishing Corporation, 1981.
