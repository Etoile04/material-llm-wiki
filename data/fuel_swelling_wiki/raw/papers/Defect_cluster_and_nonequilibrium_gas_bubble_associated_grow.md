# Defect cluster and nonequilibrium gas bubble associated growth in irradiated UMo fuels – A cluster dynamics and phase field model

---

                                                                Journal of Nuclear Materials 542 (2020) 152441



                                                                Contents lists available at ScienceDirect


                                                          Journal of Nuclear Materials
                                                        journal homepage: www.elsevier.com/locate/jnucmat




Defect cluster and nonequilibrium gas bubble associated growth in
irradiated UMo fuels – A cluster dynamics and phase ﬁeld model
Shenyang Hu a,∗, Wahyu Setyawan a, Benjamin W. Beeler b,c, Jian Gan b, Douglas E Burkes a
a
  Paciﬁc Northwest National Laboratory, 902 Battelle Blvd., Richland, WA 99352, USA
b
  Idaho National Laboratory, PO Box 1625, MS 3740, Idaho Falls, ID 83415, USA
c
  North Carolina State University, 2500 Stinson Dr, Raleigh, NC 27607, USA




a r t i c l e            i n f o                        a b s t r a c t

Article history:                                        Irradiation examination shows that gas bubble swelling kinetics are much faster after irradiation-induced
Received 2 January 2020                                 recrystallization than that prior to recrystallization in U-10 wt% Mo alloy (UMo) fuels. These kinetics
Revised 28 June 2020
                                                        imply that gas bubbles in coarse grains and small recrystallized grains have different growth behav-
Accepted 29 July 2020
                                                        ior. For the ﬁrst time, researchers developed a phase-ﬁeld model of gas bubble evolution integrating
Available online 15 August 2020
                                                        microstructure-dependent cluster dynamics to study the gas bubble swelling behavior in the recrystal-
Keywords:                                               lization zone of UMo fuels. Generation, diffusion, reaction, sink, emission, and clustering of vacancies
UMo fuel                                                and interstitials are described by the cluster dynamics model while a phase-ﬁeld model is used to de-
Nonequilibrium gas bubble                               scribe the evolution of nonequilibrium gas bubbles including nucleation and growth. With the coupled
Gas bubble swelling                                     model, the effect of defect generation rate, clustering rate, interstitial emission, and sink rates on grain
Cluster dynamics and phase-ﬁeld model                   boundaries on the gas bubble evolution are systematically simulated. A set of model parameters (defect
                                                        generation rate, clustering rate, interstitial emission, and sink rates) is determined by comparing mea-
                                                        sured and simulated gas bubble swelling kinetics. The results demonstrate that interstitial clustering is
                                                        one of the important physical mechanisms that results in fast gas bubble swelling kinetics in the recrys-
                                                        tallization zone. The developed model can also be extended to study the associated growth of defect and
                                                        second-phase precipitates often observed in irradiated materials.
                                                                                                                          © 2020 Elsevier B.V. All rights reserved.




1. Introduction                                                                          a face-centered cubic (fcc) superlattice [7–9]. The gas bubble den-
                                                                                         sity is about 1 ~ 4 × 1024 /m3 . Atomistic simulations of equation
    U-10 wt% Mo alloys (UMo), with less than 20 wt% 235U en-                             of states for gas bubbles in UMo fuels show that internal pres-
richment, are considered a candidate for replacing highly en-                            sure inside the nano-sized Xe gas bubbles is on the order of a
riched 235U fuels currently used in high performance research                            few GPa [10,11] and the gas bubble superlattice generates a com-
and test reactors in the United States. Irradiation examination of                       pressive stress in the matrix [9]. The formation of interstitials and
UMo monolithic fuels showed that irradiation-induced recrystal-                          interstitial loops causes volume expansion of lattices. A compres-
lization dramatically speeds up the gas bubble swelling kinetics                         sive stress is not energetically favored for interstitial accumula-
[1–6]. Recrystallization reﬁnes grain sizes from several microme-                        tion and interstitial loop growth. The compressive stress associated
ter coarse grains to 20 0nm-30 0nm ﬁne grains. It implies that the                       with dense nano-sized gas bubbles prevents interstitial accumula-
gas bubbles in coarse grains and small recrystallized grains have                        tion and interstitial loop growth, which largely reduces the vacancy
different growth behavior. Fission reactions continuously generate                       concentration. The low vacancy concentration causes slow gas bub-
ﬁssion gas atoms, vacancies, interstitials, and their clusters. Gas                      ble growth kinetics in coarse grains. On the other hand, the grain
bubble growth requires both gas atoms and vacancies. Gas bub-                            size in the recrystallization zone is about 20 0nm-30 0nm [5]. In-
bles grow with absorption of vacancies and shrink with absorp-                           side these small grains, the gas bubble superlattice collapses, and
tion of interstitials. Therefore, vacancy and interstitial concentra-                    gas bubbles with uniform distribution and low density form in the
tions affect the gas bubble growth kinetics. In coarse grains, ex-                       recrystallization zone [8,12]. The small grain size and low gas bub-
periments and modeling show that nano-sized gas bubbles form                             ble density may release the stress in the matrix. Therefore, our hy-
                                                                                         pothesis for the faster gas bubble growth in recrystallization zone
    ∗
                                                                                         is that interstitial clustering is energetically favored, which results
        Corresponding author.
        E-mail address: Shenyang.hu@pnnl.gov (S. Hu).
                                                                                         in more vacancies available for the gas bubble growth.

https://doi.org/10.1016/j.jnucmat.2020.152441
0022-3115/© 2020 Elsevier B.V. All rights reserved.
2                                      S. Hu, W. Setyawan and B.W. Beeler et al. / Journal of Nuclear Materials 542 (2020) 152441


    Since gas bubbles are sinks for vacancies and interstitials, the                                eq1
                                                                                       defect i, Ci,de f is the equilibrium concentration of defect i on the
evolution of gas bubbles (such as nucleation and growth) changes                                                                                          e
                                                                                       sink, Di is diffusivity of defect, a is the lattice constant, and Si,de   is
                                                                                                                                                               f
the sink strength while defect concentrations affect the gas bubble
                                                                                       the local emission strength. The integration is on sinks (the red re-
evolution. Therefore, to describe the gas bubble evolution in irradi-
                                                                                       gion in Fig. 1(b)). After that, the absorption zone (the yellow region
ated UMo fuels, the model needs to take the defect clustering and
                                                                                       in Fig. 1(b)) is deﬁned where the minimum distance to sinks is less
gas bubble associated growth into account. In this work, we ex-
                                                                                       than l, and the total lattice of the absorption zone, Ntot , is calcu-
tended the cluster dynamics model to a microstructure-dependent
                                                                                       lated. Then, the emitted defects are uniformly distributed in the
cluster dynamics model for taking into account both steady-state
                                                                                       absorption zone by ξ˙i,de f = Ci /(t Ntot ). Fig. 1(b) shows the sinks
and evolving sinks. The generation, diffusion, reaction, sink, emis-
                                                                                       including grain boundaries, gas bubbles, and the emission zone on
sion, and clustering of vacancies and interstitials in a polycrys-
                                                                                       the plane A in Fig. 1(a). The red lines represent grain boundaries,
talline structure with evolving gas bubbles are described by a
                                                                                       red circles for gas bubbles, and the yellow regions are the absorp-
microstructure-dependent cluster dynamics model. A phase-ﬁeld
                                                                                       tion zones. The sinks change with the evolution of gas bubbles and
model was used to describe the gas bubble nucleation and growth
                                                                                       grain boundaries.
[13,14]. The information of defect clusters, defect ﬂuxes, and ﬁssion
                                                                                           Having described defects and microstructures, next we present
gas atom ﬂux obtained from cluster dynamics modeling is fed into
                                                                                       the cluster dynamics and phase-ﬁeld models.
the phase-ﬁeld model of gas bubble evolution while the gas bub-
ble structures from phase-ﬁeld modeling are used to update the                         2.1. Microstructure-dependent cluster dynamics
sinks in the cluster dynamics model. Integrating these two mod-
els enables us to study the effect of defect cluster evolution on                          In UMo fuels, 235U ﬁssion generates high-energy neutrons and
gas bubble growth and swelling mechanisms. The model can also                          ﬁssion fragments that cause radiation damage. The cluster dynam-
be extended to study the associated growth of defect and second                        ics model describes the evolution of gas atoms, vacancies, inter-
phase precipitates often observed in irradiated materials [15–19].                     stitials, and their clusters in polycrystalline structures with dis-
                                                                                       tributed gas bubbles. The generation of gas atoms, vacancies, and
2. Microstructure-dependent cluster dynamics and phase-ﬁeld                            interstitials are calculated with the ﬁssion product yields and the
model of gas bubble evolution                                                          kinetic energy distribution of the ﬁssion products. The details of
                                                                                       defect generation are described in next section. Grain boundaries,
     To describe the gas bubble evolution in the recrystallization                     gas bubbles, and dislocations are treated as sink and emission sites
zone, two sets of ﬁeld variables are used to describe the mi-                          of defects. According to the kinetic rate theory, with the assump-
crostructure. One set is the order parameters ηm (x, t) and χ (x, t).                  tion that 1) only single interstitial, vacancy, and gas atoms are mo-
ηm (x, t) describes the grain orientations and χ (x, t) describes the                  bile, and 2) mobile gas atoms only interact with existing gas bub-
gas bubbles. ηm (x, t) is equal to 1 inside grain m, and 0 outside the                 bles, the evolution of defect concentrations can be written as [20–
grain m. It varies from 0 to 1 across the grain boundaries. The or-                    23]:
der parameter χ (x, t) is equal to 1 inside gas bubbles and 0 outside                  dCi (x, t )
gas bubbles, and varies from 0 to 1 across the interface between                                   = ∇ [Di ∇ Ci (x, t ) + DiCi (x, t )∇ Ui /kB T ]
                                                                                           dt
gas bubble and matrix. The other set of ﬁeld variables is defect
concentrations Cli (n, x, t) and Cg (x, t). Cli (n, x, t) , which describe
                                                                                                     + G˙ i − αCi (x, t )C j (x, t ) + K lij (2 )C j (x, t )C2i (x, t )
the concentrations of vacancy and interstitial clusters; li denotes a                                      
                                                                                                           MI
                                                                                                                                                   
cluster with defect i which could be vacancy or interstitial while                                     +             γili (m ) − Kili (m )Ci (x, t ) Cli (x, t )
l means cluster or loop, n is the number of defect i in the cluster                                        m=3
li, Cg (x, t) describes the concentration of ﬁssion gas atoms, and x, t                                − Kili (2 )Ci (x, t )C2i (x, t ) − Kili (1 )Ci2 (x, t )
are coordinate and time, respectively.
     A phase-ﬁeld model of grain growth [13] is used to generate
                                                                                                           
                                                                                                           MV
                                                                                                                  li                            
                                                                                                       −          γ j (m ) − K lij (m )Ci (x, t ) Cl j (x, t )
polycrystalline structures. The grain boundaries are deﬁned by a
                                   m0                                                                     m=3
shape function η (x, t ) = 2 m=1           (1 − ηm )2 , which has the value of
0 inside the grains and continuously varies to 1 at the center of                                      − Kili (2 )Ci (x, t )C2 j (x, t ) − S˙ i,gb (η, Ci (x, t ) )
grain boundaries. m0 is the total number of grains in the simula-                                      − S˙ i,bb (χ , Ci (x, t ) ) − S˙ i,dis (ρdis , Ci (x, t ) )
tion cell. Grain boundaries and gas bubbles are structural defects,                                                                           
                                                                                                       + ξ˙i,gb η, Ci (x, t ), Ci,gb
                                                                                                                                eq1
                                                                                                                                     (x, t )
which are sinks for vacancies and interstitials. The spatial distribu-
                                                                                                                                              
tion of sinks can be deﬁned by θ (x, t ) = η (x, t ) + χ 2 (x, t ). Fig. 1(a)                          + ξ˙i,bb η, Ci (x, t ), Ci,bb
                                                                                                                                eq1
                                                                                                                                     (x, t ) , i = j = I and V           (1)
shows the polycrystalline structure with cylindrical grains and dis-
tributed gas bubbles. At sinks of defects, when the defect concen-                     dCli (m, x, t )
tration is larger than the equilibrium concentration, the defect will                        dt
be emitted. In conventional rate theory the emitted defects will be
                                                                                         = Kili (m − 1 )Ci (x, t )Cli (m − 1, x, t ) + γ jli (m − 1 )Cli (x, t )
used to update the overall defect concentration inside grains. This                                                                                        
means that the emitted defects are uniformly distributed in the                             − Kili (m )Ci (x, t ) + K lij (m )C j (x, t ) + γ jli (m ) Cli (m, x, t )
matrix. However, in reality, for a given simulation time increment,    √                    +K lij (m + 1 )C j (x, t )Cli (m + 1, x, t ) − S˙ li,bb (m ), m = 2, 3, . . . , M
the distance of defect migration can be estimated by l = Dt ,
where D is diffusivity of defect and t is the time increment in the                   i = j = I and V, m and li st and for a cluster with m defects i,
simulation. So, if l is much smaller than the grain size, uniformly                   M = MI or MV                                                                       (2)
redistributing the emitted defects inside the grains is incorrect. The
                                                                                       where Ci (x, t) is the concentration of mobile single defect i, i = V
emission rate in the polycrystalline structure should be nonuni-
                                                                                       for single vacancy, i = I for single interstitial. Di is the diffusivity
form. In this work, to calculate defect emission, we deﬁne a defect
                                                                                       of defect i; Ui is the interaction energy between sink and defect
emission zone near sinks. We ﬁrst calculate the total amount of
                                                                                       i or chemical potential of defect on sinks; G˙ i denotes generation
defect i during the time increment t, which will be emitted from
                   e                 eq1                                             rate of vacancy, interstitial. α is a rate constant for the recombi-
sinks: Ci =          Si,def Di [Ci − Ci,def ]dV where Ci is concentration of                                                                         lj
                                                                                       nation between single vacancies and single interstitials; Ki is the
                 Sink
                                            S. Hu, W. Setyawan and B.W. Beeler et al. / Journal of Nuclear Materials 542 (2020) 152441                                         3




Fig. 1. (a) Polycrystalline structure with distributed gas bubbles, and (b) different regions on plane A: grain boundaries (red lines); gas bubbles (red circles); and absorption
zone (yellow).


capture coeﬃcient of mobile defect i by defect cluster mlj ; γi (m )
                                                                               lj          where Ebi (l j ) is the binding energy between defect i and cluster
is the emission coeﬃcient of mobile defect i by cluster m of defect                        mlj . The capture radius ri, lj is estimated by ri,l j = (ml j )1/3 rat + rat
j; S˙ i,de f is the sink rate of defect i on sinks (def) including grain                   and ri,l j = a ml j /(2π h ) for vacancy and interstitial clusters,
boundary (gb), gas bubble interface (bb), and dislocation network                          respectively. mlj is the total number of vacancies/interstitials in
                 eq1
(dis); and Ci,de f is the equilibrium concentration of defect i on sinks                   cluster lj and rat is the atom radius. h is the magnitude of Burgers
(def); ξ˙  i,de f is the emission rate of defect i from sink (def). ρ dis is               vector of interstitial loop in units of a.
the dislocation density. Clj (m, x, t) in Eq. (2) is the concentration of                      The      binding       energy     between       defect    i and   clus-
                                                                                                                                                                   f
defect cluster li, which has m defects j. S˙ li,bb (m ) is the sink rate of                ter mlj         is a function of cluster size Ebi (l j ) = Ei +
                                                                                                                                         √
cluster li at gas bubbles. MI and MV are the largest allowable sizes                       (E2bi − Eif )( 3 (ml j )2 − 3 (ml j − 1 )2 )/( 3 4 − 1 ). Eif and E2bi are
of interstitial and vacancy clusters, respectively. The evolution of
                                                                                           the formation energy of defect i and the binding energy between
ﬁssion gas atom concentration (Xe is considered in this work) in
                                                                                           defect i and 2i, respectively [21,26]. Zil j is the bias coeﬃcient,
UMo with distributed gas bubbles can written as
                                                                                           which also depends on the cluster size. S˙ li,bb is the sink rate
dCg (x, t )
            = ∇ [Dg ∇ Cg (x, t ) + DgCg (x, t )∇ Ug ] + G˙ g − S˙ g,bb              (3)    of cluster mlj at gas bubbles. The defect diffusivity Di and the
   dt                                                                                      chemical potential Ui of defect i on grain boundaries and/or gas
where Cg (x, t) is the concentration of Xe atoms, Dg is the diffu-                         bubbles are different from those in matrix. The spatially dependent
sivity of Xe; Ug is the interaction energy between sink and Xe or                          thermodynamic property of defect i is described as
chemical potential of defect on sinks; G˙ g denotes generation rate
of Xe, and S˙ g,bb is the sink rate of Xe at gas bubbles.                                      i =   0i +       i,def   θ ( ηm , χ )                                       (5)
    The evolution of the dislocations is described by a model simi-                        where        0i   is the property of defect i inside the grains, and
                                                                                                i, def θ (η m , χ ) is the difference of the property of defect i on
lar to the one developed by Stoller [24,25],
dρdis                                                                                      the structural defect from that inside grains.
      = 2π vli SBH − ρdis τli−1 + 2π rMI Cli (MI )τ −1 (MI ),         i=I           (4)        In conventional rate theory, the sink strength of defect i on a
 dt
                                                                                           structural defect is estimated at the steady state by calculating the
   The ﬁrst term in the right side describes the generation of
                                                                                           diffusion ﬂux of defect i to an isolated structural defect in the ma-
network dislocations by Bardeen-Herring source. The second term
                                                                                           trix. For instance, the reaction-controlled sink rate of distributed
represents the annihilation of climbing dislocations. vli is the climb
                                                                                           gas bubbles with average radius R and density ρ bb can be calcu-
velocity, SBH the density of Bardeen-Herring sources, and τ lj the
                                                                                           lated by 4π R2 Di ρbb ciYi,bb
                                                                                                                     s /a [16]. For a single gas bubble, the sink
mean lifetime before annihilation. The third term represents the
                                                                                           rate is written as
rate at which new dislocation line length is generated by the un-
fault of largest interstitial loops (interstitial clusters MI ). rMI is the                S˙ i,bb (x, t ) = Yi,sbb 4π R2 Di ci /a                                          (6)
radius of interstitial cluster of size MI . τ (MI ) is the time needed for                         s
the incorporation of the interstitial cluster MI into the dislocation                      where Yi,bb is the biases of gas bubbles for interstitials or vacancies,
network. The calculation of vli , SBH , τ lj and τ (MI ) is referred to the                and ci is the average concentration of defect i at gas bubble inter-
                                                                                                   s 4π R2 /a is the sink strength of a gas bubble with radius
                                                                                           face. Yi,bb
work [24].
                                                eq1                                                s
                                                                                           of R. Yi,bb depends on the type of defect i and gas bubble proper-
   Defect equilibrium concentration Ci,de f is calculated by
       f                        f                                                          ties such as the defect structures at the gas bubble interface and
exp(Ei,de f /kB T ) where Ei,de f is the formation energy of defect
                                                                                           gas pressure. A overpressure gas bubble generates a compressive
i on defect def. The rate constant α = Ziv (DI + DV )/a2 where a is                                                                                    s
                                                                                           stress around the gas bubble that causes an increase of YI,bb   (bias
the lattice constant, and Ziv is the combinatorial factor of vacancy                                                              s
                                                                                           of interstitials) and an decrease of YV,bb (bias of vacancies). For a
and interstitial. Rate constant Ki (m ) = 4π ri,l j Zil j Di / where
                                  lj
                                                                     is                    system that has a high sink density and multiple types of sinks,
the atom volume, ri, lj is the capture radius between defect i and                         or has evolving sinks such as evolving voids and/or gas bubbles in
cluster mlj ; emission rate γi (m ) = Ki (m − 1 )exp(−Ebi (l j )/kB T )
                                       lj          lj
                                                                                           nuclear fuels, the concentration ci around the gas bubbles is not
4                                                S. Hu, W. Setyawan and B.W. Beeler et al. / Journal of Nuclear Materials 542 (2020) 152441


uniform, the gas bubble size varies with time, and the system may                                are energetically unfavored sinks for interstitials. Once vacancies
never reach steady state. This instability can be demonstrated by                                and gas atoms reach gas bubbles they are absorbed immediately
the observed gas bubble swelling kinetics in UMo fuels, which in-                                by gas bubbles while interstitials are partially absorbed or emitted
crease with the increase of ﬁssion density [5]. Therefore, it is hard                            by gas bubbles. Three ﬁeld variables (i.e., Xe atom concentration
to calculate the sink rate using the rate theory Eq. (6).                                        Cgg , vacancy concentration CgV , and order parameter χ ) are used
   In our model, the gas bubble interface and grain boundary are                                 to describe the gas bubbles in the phase-ﬁeld model of nonequi-
implicitly described by θ1 (ηm , χ ) = η (x, t ) + 2(1 − χ (x, t )) . The
                                                                   2
                                                                                                 librium gas bubble evolution. The vacancy concentration CgV is dif-
temporal evolution of defect concentrations is obtained by solving                               ferent from CV in the cluster dynamics model. Vacancies, intersti-
the Eqs. (1)–(4) in the system with spatial distributed and evolv-                               tials, and their clusters sinking to gas bubbles (described by S˙ i,bb
ing sinks. The concentration near the gas bubble reﬂects the ef-                                 and S˙ l j,bb in the cluster dynamics model) generate a net change of
fect of all the coupling of the spatial dependent features of sinks                              vacancies inside the gas bubbles. CgV accounts for the net vacancy
mentioned above. We proposed a method to calculate the spatially                                 concentration inside gas bubbles.
dependent sink rate with the following assumptions: 1) all the de-                                  The Kim-Kim-Suzuki (KKS) model is used to describe the two-
fect absorption and emission take place inside the grain boundary                                phase equilibrium in UMo (i.e., matrix and void). According to the
and/or gas bubble interface zone, which is deﬁned by θ 1 (ηm , χ ),                              KKS model [30], the total free energy density of a system with va-
and 2) the sink rate inside the gas bubble interface zone can be                                 cancies and voids can be written as
calculated as                                                                                                      
                                                                                                 G = p(χ ) f b cvb + (1 − p(χ ) ) f m (cvm ) + wg(χ )                                 (8)
S˙ i,bb (x, t ) = Zi,s bb Di ci ,   θ 1 ( ηm , χ ) > 0                                 (7)
                                                                                                 where χ is the order parameter, which is zero in matrix and unity
         s
where Zi,bb  is the local sink strength. The total sink strength can                             in bubbles, p(χ ) = χ 3 (10 − 15χ + 6χ 2 ) is a monotonously chang-
be calculated by integrating the local sink strength Zi,bbs  over the                            ing function from p(0 ) = 0 to p(1 ) = 1, g(χ ) = 30χ 2 (1 − χ )2 is a
interface region (θ 1 (ηm , χ ) > 0) of the gas bubble. The local sink                           double-well potential, and w is the height of the double well po-
           s
strength Zi,bb can be estimated with the total sink strength to be                               tential.
              s 4π R2 /a from the rate theory. If the interface thickness                            fm and fb are the bulk free energy density of the matrix and
equal to Yi,bb                                                                                                                                           eq
                                                                                                 void, respectively. They are set to be f m = Am (cvm − cv )2 and f b =
of a gas bubble with radius R0 is H0 which is deﬁned by θ 1 (ηm ,                                                       eq
                                                                                                 Abv (cvb − 1 )2 where cv is the equilibrium concentration of vacancy
χ ) > 0, the volume of interface zone is approximately calculated
                                                                                                 in matrix. The total free energy F(CgV , χ ) of the system includes
by V0 = 4π R20 H0 . Zi,bb
                       s                             s
                             can be estimated by Zi,bb      s 4π R2 / (aV ) =
                                                        = Yi,bb   0      0
                                                                                                 chemical free energy and interfacial energy. It is deﬁned as
Yi,bb /(aH0 ).
  s
                                                                                                                                         κ
    Our model releases the effect of coupling the spatially depen-                               F (CgV , χ ) =         G CgV , χ +            ∇χ 2 d                                 (9)
dent features of sinks on the sink rate. Zi,bb    s    measures the average                                                                2
sink strength in the interface zone. For given the lattice constant
                                                                                                 where κ is a gradient coeﬃcient. Two model parameters w and κ
a and the thickness of interface zone H0 which is a model pa-
                                                                    s                            can be determined by the interfacial energy σ and interface thick-
rameter related to the grid size in the simulation cell, Zi,bb           only
                               s                           s                                     ness λ [14].
depends on the bias Yi,bb . As discussed above Yi,bb is a material
                                                                                                    Following the KKS model, the concentration of vacancies is
property that depends on defect structures at the interface and                                  written as follows:
the interaction between the interface and defect i and could be
assessed by atomistic simulations. The defect emission rate can                                 CgV = p(χ )cvb + (1 − p(χ ) )cvm                                                     (10)
be deﬁned as Si,bb e          e D c , θ (η , χ ) > 0 at the interface zone.
                         = Zi,bb  i i 1    m                                                         At each point in the system, local thermodynamic equilibrium
 e
Zi,bb  is the local emission strength which also can be described as                             is assumed
 e
Zi,bb      e / (aH ). Y e is the bias that depends on the interface en-
       = Yi,bb                                                                                         
                  0      i,bb                                                                    ∂ f b cvb   ∂ f m (cvm )
ergy between defect i and gas bubbles. The total emission Ci of                                           =                                                                         (11)
defect i from the emission zone, which is described in the pre-                                     ∂ cv
                                                                                                       b        ∂ cvm
vious section, is calculated with Si,bb    e . The absorption rate can be
                                                                                                     The evolution equations of gas bubbles are written as follows:
calculated by ξ˙          = Ci /(t Ntot ). In the rate theory, defect sink                                                                      
                                                                                                             DgV                                
                        i,de f
and emission rates at grain boundaries have similar expressions                                  ∂ CgV
                                                                                                       =∇            Gχ CgV ∇ χ + GCgV CgV ∇ CgV
as those at gas bubble and/or precipitate interface [27]. The same                                ∂t        GCgV CgV
method was used to calculate sink and emission rates at grain
                                                                                                                                    
                                                                                                                                    MV                        
                                                                                                                                                              MI
boundaries.                                                                                                 + S˙ V,bb − S˙ I,bb +         mS˙ l v,bb (m ) −         mS˙ li,bb (m )   (12)
                  s
   The biases (Yi,bb        e ) depend on the properties of sinks
                      and Yi,bb                                                                                                     m=2                       m=2
                                                                                                         
such as the misorientation angle of grain boundaries [27–29], co-
                                                                                                 ∂χ           ∂  κ  2 
herency of precipitate interface, and the pressure of gas bubbles. To                               =L −                ∇χ
investigate the effect of biases on gas bubble evolution we carried
                                                                                                 ∂t          ∂χ 2
                                                                                                                                                                      
out a parametric study by varying the biases.                                                                                               ∂ f m (cvm )
                                                                                                   + p (χ ) f m (cvm ) − f b cvb − cvm − cvb                  + wg χ
                                                                                                                                                                    (  )
                                                                                                                                                   ∂ cvm
2.2. Phase-ﬁeld model of gas bubble evolution
                                                                                                                                                                                     (13)
    Gas bubbles in irradiated nuclear fuels may not reach equilib-                              where DgV is diffusivity of vacancies and L is the interface mobil-
rium. This means that the gas concentration inside gas bubbles                                  ity. S˙ V,bb and S˙ I,bb are sink rates of vacancy and interstitial at gas
may be larger or smaller than the equilibrium concentration. For                                bubbles, respectively. S˙ l v,bb and S˙ li,bb are the sink rates of vacancy
example, the gas bubbles may become voids if the matrix has high                                and interstitial clusters at the gas bubbles.
vacancy concentration. In contrast, the gas bubble might be over-                                   It is assumed that all gas atoms, vacancy, and vacancy and in-
pressurized if the vacancy concentration is low in matrix. To de-                               terstitial clusters are absorbed by gas bubbles when they reach the
scribe the nonequilibrium gas bubbles, we assume that gas bubbles                               gas bubbles. The sink rate is calculated by S˙ i,bb = Si mCi χ /t, i =
are energetically favored sinks for vacancies and gas atoms, and                                V, I, l i, and l v. m is the number of defect cluster i. For interstitials,
                                       S. Hu, W. Setyawan and B.W. Beeler et al. / Journal of Nuclear Materials 542 (2020) 152441                         5


when their concentration on the gas bubble interface is larger than                   that the cluster dynamics model and phase ﬁeld model exchange
their equilibrium concentration, the interstitials are emitted as de-                 information through the simulation. Defect concentrations and the
scribed in cluster dynamics model.                                                    absorption of defects at gas bubbles from the cluster dynamics
    The gas phase inside gas bubbles is treated as a solution phase.                  simulation are used in nucleation and growth of gas bubbles in the
The free energy density of the gas phase is described as                              phase-ﬁeld model. The gas bubble structures obtained from phase-
               eq
                     2                                                               ﬁeld modeling is used to update the sink as well as defect con-
G1 = Abb Cgg − Cgg                                                         (14)       centrations in the cluster dynamics model. The integrated model
       eq                                                                             enables one to simulate defect and gas bubble-associated growth.
where Cgg is the equilibrium concentration of gas atoms which is
set to 0.45 [11]. The evolution of gas atom concentration is given
as                                                                                    2.5. Model parameters
                              
∂ Cgg (x, t )           ∂ G1
              = ∇ Dgg ∇       + S˙ g,bb                                    (15)       2.5.1. Calculation of defect generation during ﬁssion
    ∂t                  ∂ Cgg
                                                                                          To calculate the defect generation G˙ i , we need to know the ﬁs-
where Dgg is the diffusivity of gas atoms, and S˙ g,g is the sink rate                sion product yields and the kinetic energy distribution of the ﬁs-
of gas atoms calculated in cluster dynamics model. For large gas                      sion products. Fission product (FP) yields depend on the ﬁssioning
bubbles, it is reasonable to assume that gas atoms are conﬁned                        nuclide and the energy of the neutron causing the ﬁssion. Here,
inside gas bubbles once they are absorbed by the gas bubbles. To                      we evaluate the model for ﬁssion from 235    92
                                                                                                                                      U due to thermal neu-
apply this assumption in the model, Dgg is deﬁned as Dgg = Dgg0 χ 2 .                 trons (neutron energy=0.0253 eV), which is applicable for light-
Dgg is equal to Dgg0 inside the gas bubble, and equal to zero in                      water reactors (LWRs). Based on previous work of Setyawan et al.
the matrix. Dgg0 is the diffusivity of gas atoms inside gas bubbles,                  [31], we take the independent ﬁssion product yield (iFPY) from the
which should be much larger than that in the matrix.                                  JEFF 3.3 library to calculate the defect generation in this work. The
   One of merits of this work is that we developed a phase-ﬁeld                       distribution of the ﬁssion products and kinetic energies (Etot) as a
model of nonequilibrium gas bubble evolution in nuclear fuels. The                    function of atomic number can be found in the reference [31]. The
Eqs. (8)–(13) describe two-phase equilibrium (i.e. void and matrix                    18 elements listed in Table 1 make up almost 100% of the distri-
phases). Eqs. (14) and (15) describe the gas phase inside the void.                   bution. Every ﬁssion creates two ﬁssion products, one light ﬁssion
Eq. (15) only evolves inside the voids, which can be seen from                        product and one heavy ﬁssion product. The mass of the most prob-
the deﬁnition of the diffusivity Dgg . Dgg is zero outside voids. All                 able isotope in each element is taken as the mass of the element.
gas atoms inside the voids are from the sink term in Eq. (15),                        UMo fuels are currently developed for high performance research
which is calculated from the cluster dynamic model. The evolu-                        reactors. In high performance research reactor such as High Flux
tion Eq. (15) drives the gas concentration inside voids to reach a                    Isotope Reactor (HFIR) at Oak Ridge National Laboratory, the per-
uniform value (a solution phase). So, the nonequilibrium gas bub-                     centages of ﬁssions caused by neutrons in the thermal, intermedi-
ble model can describe the transition from the over-pressure gas                      ate, and fast neutron ranges are 83.03% (< 0.625 eV), 15.50% (0.625
bubble (high gas concentration) to the void-like gas bubble (low                      eV ~100 keV), and 1.48% (>100 keV) [32]. We calculated the ﬁssion
gas concentration), which completely depends on the ratio of gas                      product yields for neutron energy of 40keV. The calculation shows
atoms and vacancy inside the gas bubble.                                              that the sum of ﬁssion product yields from18 elements is less than
                                                                                      0.5% for neutron energy 0.0253 eV and 40keV.
2.3. Nucleation of gas bubbles                                                            Using Etot and the mass of the most probable isotope, the Stop-
                                                                                      ping and Range of Ions in Matter (SRIM) simulations are performed
    The concentration distributions of vacancies, interstitials, and                  to obtain the portion of the energy lost due to electronic stopping
their clusters are nonuniform because of inhomogeneous grain and                      (Eelectronic) and the energy that effectively causes damage via dis-
gas bubble structures. With the increase of local net vacancy con-                    placement cascade (Edamage), for each ﬁssion product. For SRIM
centration (single vacancy, single interstitial, and their clusters),                 simulations, the displacement threshold energy (Ed) of γ U from
the defects will collapse and form a void. Based on this assump-                      molecular dynamic (MD) cascade simulations [33] and the material
tion, a statistical method is used to introduce the nuclei of gas                     density of pure γ U are used. Norgett, Robinson, and Torrens (NRT)
bubbles. To do so, the total vacancy concentration, ctotM (x, t ) is cal-             formula of 0.4∗ Edamage/Ed is used to estimate the Frenkel pair
culated by summing all the defects (single vacancy, single intersti-                  generation per ﬁssion [34]. The results show that one 235  92
                                                                                                                                                    U ﬁssion
tial, and their clusters) at every N1 simulation step. The sum of                     generates about 14,825 Frenkel pairs in γ U. Since we do not have
vacancy concentration ctot in the matrix can calculated by integrat-                  the cascade data of U-10wt%Mo, the defect generation calculated in
ing ctotM (x, t ). The number of potential nucleation sites is deter-                 γ U is used in the simulations. Table 1 summarizes the Etot, Eelec-
mined by N2 = ctot /ccrt , where ccrt is the critical value of vacancy                tron, Edamage, and the number of Frenkel pairs for each FP.
concentration required for the formation of a nucleus. Then, posi-
tion xi , (i = 1, 2, . . . , N2 ) is chosen randomly; the total vacancy ctot1         2.5.2. Thermodynamic and kinetic properties of defects
at xi by integrating ctotM (x, t ) in a sphere with radius r1 ; and a                     Table 2 lists the model parameters used in the simulations.
spherical nucleus with radius rc is introduced if the total vacancy                   Very limited thermodynamic and kinetic properties of defects in
ctot1 is larger than the critical value ccrt . Inside the nucleus, the                U10Mo, which are needed in cluster dynamics and phase ﬁeld
order parameter χ is set to be 1.0, the radius rc is calculated by                    models, are available in the literature. The defect formation en-
[3ctot1 /(4π )]1/3 . N1 and ccrt are model parameters. For given model                ergies of U vacancy and interstitials are assessed from the data
parameters, r1 is estimated by DV N1 t . In the simulations, N1                      of DFT and MD simulations in U and UMo alloys [35-37]. Self-
and ccrt are set to be 50 0 0 and 1.0, respectively.                                  diffusivity of U is from MD simulations and experiments [38-41].
                                                                                      Xe diffusion is adopted from the rate theory model of gas bubble
2.4. Flow chart of cluster dynamics and phase ﬁeld model of gas                       swelling in UMo [5]. Capture radius, bias coeﬃcients, and model
bubble evolution                                                                      parameter of network dislocations are adopted from the cluster dy-
                                                                                      namic and rate theory models [21,23,24,27,42].
  Fig. 2 shows the ﬂow chart of cluster dynamics and phase ﬁeld                           The thermodynamic and kinetics properties such as chemical
model of nonequilibrium gas bubble evolution. The chart shows                         potential Ui of mobile defects on grain boundaries, binding energy
6                                  S. Hu, W. Setyawan and B.W. Beeler et al. / Journal of Nuclear Materials 542 (2020) 152441




                                          Fig. 2. Flow chart of the integrated cluster dynamics and phase-ﬁeld model.

                                  Table 1
                                  The most probable isotopes of ﬁssion products from 235  92 U due to thermal neutrons, the
                                  independent ﬁssion product yield (iFPY), total kinetic energy (Etot), electronic loss (Eelec-
                                  tron), and Edamage = Etot – Eelectron used in SRIM simulations to estimate the number
                                  of Frenkel pairs in γ U with displacement threshold energy Ed=35.6eV at 800K.

                                    Element      iFPY     Etot(MeV)     Eelectron(MeV)        Edamage(MeV)     Frenkel pairs
                                    86
                                    34 Se        0.042    101.3         98.362                2.938            1376.9
                                    87
                                    35 Br        0.051    101.2         98.117                3.083            1751.6
                                    90
                                    36 Kr        0.164    101.5         98.333                3.167            5829.3
                                    93
                                    37 Rb        0.112    101.2         97.840                3.360            4216.0
                                    94
                                    38 Sr        0.209    101.1         97.766                3.334            7816.4
                                    97
                                    39 Y         0.114    101.3         97.792                3.508            4504.4
                                    100
                                    40 Zr        0.180    101.4         97.536                3.864            7824.6
                                    102
                                    41 Nb        0.073    101.8         97.728                4.072            3319.2
                                    104
                                    42 Mo        0.041    101.2         97.172                4.028            1847.3
                                    130
                                    50 Sn        0.041    81.5          75.928                5.572            2555.1
                                    133
                                    51 Sb        0.073    78.8          73.052                5.748            4685.4
                                    134
                                    52 Te        0.180    77.5          71.641                5.859            11864.3
                                    136
                                    53 I         0.114    74.6          68.582                6.018            7726.5
                                    138
                                    54 Xe        0.209    71.9          66.289                5.611            13154.9
                                    141
                                    55 Cs        0.112    68.2          61.898                6.322            7931.9
                                    144
                                    56 Ba        0.164    64.8          58.330                6.470            11908.0
                                    146
                                    57 La        0.051    62.6          56.049                6.551            3721.8
                                    148
                                    58 Ce        0.042    60.2          53.491                6.709            3144.7
                                    SUM          1.969

                                  iFPY-weighted sum of Frenkel pairs = 14825.


among defect and defect clusters, chemical free energies of differ-                a pressured gas bubble than that in matrix, which prevents inter-
ent phases, and gas atom mobility inside gas bubbles are set up to                 stitials diffusing to gas bubbles. For gas bubbles with low pressure
reasonably capture the interaction among defects and phase sta-                    or voids, interstitials, like vacancies, should have lower chemical
bility. For instance, the diffusivity of vacancies and gas atoms in-               potential inside voids than that in the matrix.
side gas bubbles is set up to be large so that the concentrations                      The inhomogeneous chemical potentials of vacancy, gas atoms,
                                                                                                                                                     U
of vacancy and gas atoms quickly become uniform inside gas bub-                    and interstitials are assumed to be UV /kB T = [−2.eV/kB T ]χ 2 , k gT =
                                                                                                                                                        B
bles after the absorption at the gas bubble interface. In the sim-
                                                                                   [−2. keVT ]χ 2 , and UI /kB T = [2.eV/kB T ]χ 2 in the simulations. Biases
ulations, DVg = 100DV and Dgg0 = 100Dg were used. The chemical                            B

potential of vacancy, interstitial, and gas atom inside the gas bub-               coeﬃcient of interstitial clusters Zli j , the sink rate constant of grain
                                                                                                s , the emission rate constant Z e , and the defect
                                                                                   boundaries Zi,gb
bles depends on the ratio of gas atom and vacancy or gas con-                                                                            i,bb
centration Cgg . Generally speaking, vacancies and gas atoms should                generation rate G are model parameters for studying their effect
have lower chemical potentials inside gas bubbles than those in                    on gas bubble evolution. In the literature, some experimental re-
the matrix, which drives vacancies and gas atoms diffusing to gas                  ports exist on the effect of ﬁssion rates on gas bubble swelling
bubbles. Interstitials should have a higher chemical potential inside              in UMo dispersion fuels [43,44], but no relative results for UMo
                                         S. Hu, W. Setyawan and B.W. Beeler et al. / Journal of Nuclear Materials 542 (2020) 152441                                7
                                                                                        Table 3
monolithic fuels. With the assumptions that Xe diffusivity, res-                        Model parameters used in the case studies.
olution and recrystallization kinetics are proportional to the ﬁs-                         Cases                                G        s
                                                                                                                                       Yi,gb      e
                                                                                                                                                Yi,bb       Zl0j
sion rate, simulations show that the gas bubble swelling depends
                                                                                           Defect generation rate               1000   3.0      0.08        2.4
heavily on ﬁssion density, but weakly on ﬁssion rate [45]. Further-                                                             2000
more, considering the factors that 1) gas bubble swelling modeling                                                              3000
in 3D is a computer time-consuming process and 2) the simula-                              Interstitial emission rate           3000   3.0      0.05        2.4
tions will focus on parametric studies, we used a high ﬁssion rate                                                                              0.06
3.29 × 1022 ﬁssions/s/m3 to accelerate the simulation and save the                                                                              0.08
computational cost.                                                                                                                             0.10
                                                                                           Defect sink rate                     3000   0.1      0.08        2.4
                                                                                                                                       0.3
3. Results                                                                                                                             1.0
                                                                                                                                       3.0
    The simulations start from a polycrystalline structure with                            Defect clustering rate               3000   3.0      0.08        0.6
cylindrical grains and distributed gas bubbles as shown in Fig. 1.                                                                                          1.2
The simulation cell has dimensions of 128l0 × 128l0 × 32l0 . The                                                                                            2.4
                                                                                                                                                            3.6
use of cylindrical grains is to save the simulation cost while cap-
turing grain boundary effect. To solve the Eqs. (1)–(4),(10),(11), and
(13), time, length, and energy are normalized by t ∗ = t/(D0 /l02 ),
x∗ = x/l0 , and kB T, respectively. D0 is the largest diffusivity of Di ,               which means four ﬁssions generate one gas atom. Emission, sink,
l0 is the characteristic length, and T is the absolute temperature.                     and clustering rates of defects depend on the interaction ener-
    The average grain size is about 300nm, which is similar to that                     gies among defects. The knowledge of the interaction energies in
observed in the recrystallization zone in UMo. The initial size dis-                    the UMo system is lacking. Therefore, parametric studies for the
tribution and density of gas bubbles are set to have the volumet-                       unknown model parameters are carried out in the simulations.
ric swelling 1.32% at ﬁssion density fd = 2.6 × 1027 (ﬁssion/m ) to
                                                                      3                 Table 3 lists the model parameters used in the case studies.
mimic the gas bubble microstructure just after the recrystalliza-
tion. Besides the given model parameters and properties listed in                       3.1. Effect of defect generation rate on gas bubble swelling
Table 2, some thermodynamic and kinetic properties are unknown
or have large uncertainty, f(e.g., the defect generation rate, cluster-                     For a given generation rate, G f˙0 , of Frenkel pairs per ﬁssion
ing rate, and the defect emission rate).                                                with G = 20 0 0 and the rest of the parameters shown in the ﬁrst
    In Section 2.5.1 the generation of Frenkel pairs per 235U ﬁs-                       row in Table 3, the evolution of CgV (x, t), the concentrations of in-
sion in γ U is estimated at about 14,825. The MD method has been                        terstitial CI (x, t), vacancy CV (x, t), and total concentration of gas
extensively used to simulate the defect evolution under energetic                       atoms Cg (x, t ) + Cgg (x, t ) on the plane A shown in Fig. 1(a) are pre-
cascades in metals [46–48]. It is found that 1) most generated                          sented in Fig. 3(a-d), respectively. The gray color in Fig. 3(a) repre-
Frenkel pairs annihilate during a very short period (within a few                       sents grain boundaries, which shows the iso-surface of η (x, t ) =
ps), and 2) the NRT formula of 0.4∗ Edamage/Ed overestimates the                        0.5. Light blue shows the iso-surface of vacancy concentration,
number of defects by a factor 3 ~ 4. For long time cascade de-                          CgV (x, t ) = 0.5, representing gas bubbles. The color bar in Fig. 3(a-
fect aging up to tens ns, Object kinetic Monte Carlo (OkMC) sim-                        d) presents the concentration of defects. The change in gas bub-
ulations in tungsten show that the number of defects further de-                        ble number and size show the nucleation, growth, and coalescing
creases. The amount of reduced defects depends on PKA energy                            of gas bubbles. Concentrations CI (x, t) and CV (x, t) in the matrix
and temperature [49]. The generation rate of defects can be calcu-                      are not uniform. Interstitial concentration in the interior of grains
lated by G˙ I = G˙ V = G f˙0 , where f˙0 is the ﬁssion rate. G is the num-              increases, then decreases, while vacancy concentration increases
ber of survived Frenkel pairs per ﬁssion during the simulation time                     with time. Both CI (x, t) and CV (x, t) inside gas bubbles are almost
increment t. G is a unknown model parameter.                                           zero because they recombine with vacancies CgV (x, t). The white
    Based on the MD and OkMC simulations of defect evolution                            circles show the interface of gas bubbles. It can be seen that there
G =10 0 0 ~ 30 0 0, which means less than 20% defects calculated                        is a depletion zone of interstitials and vacancies near the gas bub-
by NRT formula survive, and this should be a safe estimation.                           bles. Inside gas bubble CgV (x, t) is equal to 1 and gas atom concen-
The generation rate of gas atoms is calculated by G˙ g = 0.25 f˙0 ,                     tration Cgg (x, t) has a general tendency to decrease with time. The
                                                                                        color shows that the largest Cgg (x, t) is about 0.8, which is associ-
Table 2
                                                                                        ated with the nucleation stage of gas bubbles. Cgg (x, t) in large gas
Model parameters in the cluster dynamics model.                                         bubbles is also smaller than that inside small gas bubbles. These
                                                                                        results demonstrated that the developed model reasonably cap-
 Parameter          Value                            Parameter          Value
                                                                                        tures the defect-gas bubble associated growth in UMo fuels (i.e.,
 T                  453K                             ZIV                50              dynamic interaction between evolving gas bubbles (sinks) and de-
 rat                1.5A                             ZI, dis            1.25
                                                                                        fects).
                    2.1 × 10−29 m3                   ZV, dis            1.0
 a                  3.48A                            MI                 30                  The gas bubble swelling is calculated by
 DV                 1.83 × 10−19 m2 /s               MV                 10
 DI                 1.42 × 10−18 m2 /s               Eif                0.8eV           Sgb (t ) =     χ (x, t )d /V0                                       (16)
 Dg                 1.83 × 10−20 m2 /s               E2bi               0.5eV
 ρ dis0             1.0 × 1014 m−2                   Evf                1.61eV
   f
 Ei,gb              0.7eV                            E2bv               0.5eV
                                                                                        where the integration is over the simulation cell, and V0 is the vol-
 Evf,gb             0.8eV                            σ                  1.0J/m  2       ume of simulation cell. The effect of defect generation rates on gas
 D0                 1.42 × 10−18 m2 /s               l0                 12nm            bubble swelling is plotted in Fig. 4. The experimental data points
 f˙0                3.29 × 1022 ﬁssion/s/m3          λ                  36nm            [1] are shown by red circles in Fig. 4. As expected, the gas bubble
 Am                 10.75kB T                        Abv                0.91kB T        swelling kinetics increase as the generation rate of Frenkel pairs
 Abb                0.91kB T                         t                 0.101s
                                                                                        per ﬁssion increases because there are more vacancies available for
 h                  2                                Zlvj               1.0
 Zli j              1.25                             Zl j              42
                                                                                        gas bubble growth. However, the predicted gas bubble swelling ki-
                                                                                        netics are much slower than measured swelling kinetics, even us-
8                                             S. Hu, W. Setyawan and B.W. Beeler et al. / Journal of Nuclear Materials 542 (2020) 152441




Fig. 3. Evolution of defects and gas bubble. (a) gas bubble CgV (x, t), (b) interstitials CI (x, t), (c) vacancy CV (x, t) and (d) gas atom Cg (x, t ) + Cgg (x, t ). fd is the ﬁssion density
(ﬁssion/m3 ).




ing a large defect generation rate (30 0 0 Frenkel pairs per ﬁssion).                                The interface of gas bubbles is a two dimensional (2D) sink.
Although the swelling kinetics may reach the experimental data                                    In the simulations the interface thickness H0 which is deﬁned
as the defect generation rate further increases, 30 0 0 Frenkel pairs                             by θ 1 (ηm , χ ) > 0 is equal to l0 . l0 is the grid size of simula-
generation rate corresponds to 20% defect survive of defects calcu-                               tion cell. In reality, defects emit from a very thin interface layer.
lated by NRT formula, which is a high surviving rate after 0.1 sec-                               The layer thickness is about the lattice constant a. So the av-
ond aging according to MD and OkMC simulations [46,50]. There-                                                  e
                                                                                                  erage bias Yi,de   has a scale factor H0 /a for 3D sink, and a scale
                                                                                                                   f
fore, other thermodynamic and kinetics might play an important                                   factor (H0 /a)2 for a one dimensional (1D) sink such as disloca-
role in gas bubble swelling in the recrystallization zone.                                       tions and interstitial loops. Fig. 5 shows the effect of interstitial
                                                                                                                               e
                                                                                                 emission rate or the bias Yi,bb  on gas bubble swelling. Increasing
                                                                                                 the emission rate results in more emission of interstitials from
3.2. Effect of interstitial emission rate on gas bubble swelling
                                                                                                 the gas bubble interface. As a result, the interstitial concentra-
                                                                                                 tion near the gas bubble decreases with the increase of Yi,bb e , and
       The normalized emission rate is described as
                                                                                               less vacancies are recombined with interstitials, hence, increasing
                                    Zi,e def Di l02 Ci − Ci,eqdef1                             the vacancy absorption by gas bubbles, the gas bubble growth,
ξ˙ ∗
 i,def η , Ci (x, t )
                    , Ci,eqdef
                            1
                            ( x, t ) =                                                           and swelling kinetics. When Yi,bbe  reaches 0.08, further increasing
                                                     D0
                         eq1
                                                                                              e
                                                                                                 Yi,bb does not affect the swelling kinetics. It indicates that all in-
       Yi,def Di l0 Ci − Ci,def
         e        2
                                     Yi,def (Di /D0 ) l02 /a2 Ci − Ci,eqdef
                                       e                                 1

    =                              =                                          ,                  terstitials arriving at gas bubbles are emitted and the interstitials
                 aH0 D0                               (H0 /a )                                   have an equilibrium concentration near the gas bubbles. The re-
θ 1 ( ηm , χ ) > 0                                                                   (17)        sults show that for the given model parameters listed in the sec-
                                                    S. Hu, W. Setyawan and B.W. Beeler et al. / Journal of Nuclear Materials 542 (2020) 152441                                         9




              Fig. 4. Effect of defect generation rates on gas bubble swelling.                    Fig. 6. Effect of interstitial and vacancy sink rate on grain boundaries on gas bubble
                                                                                                   swelling.



                                                                                                   sorbed by grain boundaries, it leads to grain growth. In contrast, if
                                                                                                   more vacancies than interstitials are absorbed by grain boundaries,
                                                                                                   that may result in the formation of voids. The defect concentration
                                                                                                   absorbed by grain boundaries can be calculated by
                                                                                                              t                   
                                                                                                   cIV,gb = ∫ S˙ I,gb − S˙ V,gb dt                                                 (19)
                                                                                                              0

                                                                                                   where t is the time.
                                                                                                       Fig. 7(a) shows the distribution of cIV, gb on the plane A for the
                                                                                                           S = 3.0 at ﬁssion density f = 8.04E + 27(ﬁssion/m3 ). It can
                                                                                                   case Yi,gb                             d
                                                                                                   be seen that cIV, gb on grain boundaries is larger than zero. A pos-
                                                                                                   itive value of cIV, gb means that more interstitials than vacancies
                                                                                                   are absorbed by grain boundaries. The effect of sink rates on cIV,gb
                                                                                                   along the line AA’ on the plane A are plotted in Fig. 7(b). Since the
                                                                                                   sink rate S˙ i,gb is proportional to the diffusivity Di , it is understand-
Fig. 5. Effect of interstitial emission rate from gas bubbles on gas bubble swelling.              able that cIV, gb increases with the increase of S˙ i,gb . As more intersti-
                                                                                                   tials sink to dislocations and grain boundaries, it is expected that
                                                                                                   more vacancies are left in the matrix. A high vacancy concentration
                                                                                                   should speed up the gas bubble swelling.
ond row in Table 3, increasing the interstitial emission rate on                                       The results in Fig. 6 show an opposite tendency. Notice that
gas bubble interface could not produce the measured swelling                                       the sink rate S˙ i,gb is also proportional to local defect concentration
kinetics.                                                                                                         eq1
                                                                                                   ci (x, t ) − Ci,gb . In the matrix, vacancy concentration is much higher
                                                                                                                                                                S
                                                                                                   than that of interstitials. Increasing sink rate coeﬃcient Yi,gb also
3.3. Effect of interstitial and vacancy sink rates on gas bubble
swelling                                                                                           increases the sink strength of vacancies on the grain boundaries.
                                                                                                   As a consequence, both interstitial and vacancy concentrations in
                                                                                                   the matrix decrease with the increase of sink rate coeﬃcient Yi,gbS .
   Interstitial and vacancy sink to grain boundaries. The normal-
ized sink rate is calculated by                                                                    The decrease of the gas bubble swelling kinetics shown in Fig. 7 is
                                      eq1
                                                                         eq1
                                                                                                  attributed to the decreasing vacancy concentration.
                    f i 0 i(
               s
              Zi,de  D l 2 c x, t ) − Ci,de f
                                                          s
                                                        Yi,de  D l 2 Ci − Ci,de
                                                              f i 0             f
S˙ i,de f =                                         =
                             D0                                  aH D                              3.4. Effect of interstitial clustering on gas bubble swelling
                                2 2         eq1
                                                                0 0
            s
          Yi,de   ( D i / D 0 ) l 0 / a Ci − C
                                                       , θ 1 ( ηm , χ ) > 0 .
                f                             i,de f
        =                                                                               (18)          Interstitials and vacancies form clusters which reduce the con-
                               (H0 /a )                                                            centrations of mobile vacancies and interstitials in the matrix. As a
   Fig. 6 shows the effect of sink rate at grain boundaries on gas                                 result, the defect clustering affects the gas bubble nucleation and
bubble swelling. It is interesting to ﬁnd that that when Yi,gbs < 1.0
                                                                                                   growth. The capture coeﬃcients of clusters depend on the interac-
                                                       s
the gas bubble swelling kinetics is independent of Yi,gb . But the gas                             tion energy between defect i and defect cluster lj. Assuming that
bubble swelling kinetics deviate from measured swelling kinetics                                   vacancy and interstitial clusters has a spherical and a loop shape,
                                     S . Therefore, adjusting the sink
with the increase of the sink rate Yi,gb                                                           respectively, the normalized capture coeﬃcients of mobile defect i
rate on grain boundaries could not produce the measured gas bub-                                   by defect cluster lj are calculated by
ble swelling kinetics.
                                                                                                                        4π rat Zvl j Dv l02
                                                                                                                              
                                                                                                                                                  1
   Interstitials and vacancies sinking to grain boundaries change                                  Kvl j∗ (m ) = Zl0j                         (m ) 3 + 1
their concentrations on grain boundaries as well as in matrix. We                                                         a3 Ha0 D0
assume that interstitials and vacancies on grain boundaries recom-                                                                                         1
bine immediately. Thus, if more interstitials than vacancies are ab-                                           = Zl0j 4π (rat /a )(Dv /D0 )Zvl j (m ) 3 + 1 /(H0 /a ),             (20)
10                                                 S. Hu, W. Setyawan and B.W. Beeler et al. / Journal of Nuclear Materials 542 (2020) 152441




     Fig. 7. (a) concentration cIV, gb of interstitial and vacancy absorbed on grain boundaries, and effect of sink rate coeﬃcient on cIV, gb along the AA’ line shown in Fig. 7(a).




                                                                                                   spectively. In Fig. 9a, it can be seen that the gas bubble density
                                                                                                   increases due to the gas bubble nucleation, and then decreases
                                                                                                   with gas bubble coalescence as the ﬁssion density increases. Ex-
                                                                                                   periments show a wide distribution of gas bubble size (100nm ~
                                                                                                   300nm) [2]. This implies gas bubble nucleation and coalescence
                                                                                                   take place. Fig. 9b shows that the average gas bubble size increases
                                                                                                   with the ﬁssion density increase. The drop of average gas bub-
                                                                                                   ble size around fd = 3.0 × 1027 (ﬁssions/m3 ) is because of rapid in-
                                                                                                   crease of gas bubble density associated with gas bubble nucleation.
                                                                                                   For different defect clustering rates, the average gas bubble size at
                                                                                                   high ﬁssion density has a slight difference. The predicted average
                                                                                                   gas bubble sizes, about 160nm at fd = 7.0 × 1027 (ﬁssions/m3 ), is
                                                                                                   in reasonable agreement with the average intergranular gas bub-
                                                                                                   ble size [2]. Fig. 9c shows the average Xe concentration inside
                                                                                                   the gas bubbles. The Xe concentration is the same as the ratio
                                                                                                   of Xe and vacancy inside the gas bubbles. It is clear that aver-
                                                                                                   age Xe concentration inside the gas bubble is much lower than
  Fig. 8. Effect of interstitial and vacancy clustering rate on gas bubble swelling.
                                                                                                   the equilibrium value (0.45), and decreases with the increase of
                                                                                                   ﬁssion density as well as the increase of clustering rate. The av-
                        2π ri,l j Di l02    i            √                                     erage ratio of Xe and vacancy inside gas bubbles is about 1:10
Kil j∗ (m ) = Zl0j                          Zl j + Z l j / 8π − Zil j /m0.35                      at fd = 7.0 × 1027 (ﬁssions/m3 ). It implies that the gas bubbles be-
                     a3 (H0 /a ) D0 2
                                                            Z
                                                                                                  come voids. All the information of gas bubble structure evolution
                                                2 2 i      √ l j − Zi
                                                              8π
                                                                                                   can be extracted from the simulations. However, systematic exper-
             = Zl0j 2   π (ri,l j /a )(Di /D0 ) l0 /a Zl j +       0.35
                                                                        lj
                                                                            /(H0 /a )2 ,           imental results of gas bubble structure evolution are required to
                                                                     m
                                                                                                   validate the model.
                                                                                       (21)            Gas bubble swelling is calculated by Eq. (16), which should be
                                                                                                   equivalent to the volume increase associated with absorbed inter-
where Zl0j is a scale value of bias coeﬃcient Zil j . The parameters
                                                                                                   stitials induced grain growth, the formation of interstitial and va-
Zvlj , Zilj , and Z lj [26] are listed in Table 2. Vacancy clusters are                           cancy clusters, and dislocation climb by absorbing defects. The ab-
2D sinks. Interstitial loops are 1D sinks. To calculate their cap-                                 sorbed interstitials on grain boundaries shown in Fig. 7(a) have a
                    l j∗         l j∗
ture coeﬃcients Kv (m ) and Ki (m ), scale factors H0 /a and (H0 /a)2                              concentration that is much higher than thermal equilibrium con-
should be applied, respectively. The effect of bias coeﬃcient Zl0j Zil j                           centration. If the absorbed interstitials cause grain growth, the vol-
of clusters on swelling kinetics is plotted in Fig. 8. It can be seen                              umetric swelling associated with the grain growth can be calcu-
that with the increase of Zlj0 , the gas bubble swelling kinetics in-                              lated by integrating the absorbed interstitial on the gain boundary.
creases and converges to measured swelling kinetics. If the inter-                                 Fig. 10 shows the effect of sink rates and clustering rates on grain
stitial clusters have a large clustering rate or growth rate, the pre-                             growth-induced swelling. It is found that the swelling rate asso-
dicted gas bubble swelling kinetics is in agreement with the mea-                                  ciated with grain growth gradually reach zero for all cases. This
sured swelling kinetics. Compared the effect of other thermody-                                    means that absorbed interstitials decrease with the ﬁssion density
namic and kinetic properties on the swelling kinetics, we conclude                                 increase or the increase of gas bubble and interstitial density. For
that the defect clustering plays an important role in fast gas bubble                              the cases that predicted gas bubble swelling kinetics in agreement
swelling kinetics in recrystallization zone in UMo fuels.                                          with experiment (Zl0j > 2.4), the total swelling associated with
    Fig. 9a, b, and c show the temporal evolution of gas bubble                                    grain growth is less than 0.002, which is much smaller than gas
structures including gas bubble density, average gas bubble size,                                  bubble swelling (0.25 at fd = 7.0 × 1027 (ﬁssions/m3 )). Therefore
and average ratio of Xe and vacancy inside the gas bubbles, re-                                    in the recrystallization zone, grain growth-induced the volumetric
                                           S. Hu, W. Setyawan and B.W. Beeler et al. / Journal of Nuclear Materials 542 (2020) 152441                                       11




Fig. 9. Evolution of gas bubble structures for different clustering rates. (a) gas bubble density, (b) average gas bubble size in diameter, and (c) the average ratio of Xe and
vacancy inside the gas bubbles.




                                                                                                                        S
Fig. 10. Effect of defect kinetic properties on swelling associated with grain growth. (a) defect sink rate coeﬃcient Yi,gb on grain boundaries, and (b) defect clustering rate
coeﬃcient Zl0j



swelling is negligible compared with volumetric swelling associ-                               From the simulations a set of model parameters is determined,
ated with gas bubble and interstitial clustering. In other words, the                                       s = 1.0, Y e = 0.08, and Z 0 = 2.4. With this set of
                                                                                          i.e., G=30 0 0, Yi,gb       i,bb              lj
defect clustering is one of main mechanisms that results in a fast                        model parameters, predicted gas bubble swelling kinetics in the re-
gas bubble swelling kinetics in the recrystallization zone.                               crystallization zone is in good agreement with the experimental
                                                                                          results. The evolution of gas bubble structures including gas bub-
4. Conclusions                                                                            ble density, gas bubble size, and the ratio of Xe and vacancy inside
                                                                                          gas bubble are also analyzed. The gas bubble structures are in rea-
   For the ﬁrst time, we developed a mesoscale model of defect                            sonable agreement with existing experimental data. However, the
cluster and nonequilibrium gas bubble associated growth by inte-                          model is based on assumptions of interstitial clustering and ran-
grating phase-ﬁeld and cluster dynamics approaches for investigat-                        dom gas bubble distribution in the recrystallization zone. Exper-
ing the effect of defect clustering on gas bubble swelling in poly-                       imental results including the stability of nano-sized intragranular
crystalline UMo under irradiation. With the model, the effect of de-                      gas bubbles, large gas bubble spatial distribution, and the stability
fect generation rate, clustering rate, interstitial emission and sink                     and evolution of interstitial loops in recrystallization zone are re-
rates on gas bubble evolution were systematically simulated. We                           quired to validate these assumptions. The simulations were accel-
found that 1) gas bubble swelling kinetics increases with the in-                         erated by using a very high ﬁssion rate (3.29 × 1022 ﬁssions/m3 )
crease of defect generation rate, interstitial emission rate from gas                     in order to reach the fuel operation time (several months) and to-
bubble interfaces, and defect clustering rate, but decreases with                         tal ﬁssion density (7.5 × 1027 ﬁssions/m3 ). To increase simulation
the increase of defect sink rate on grain boundaries; 2) swelling                         time step, which enables one to use a low ﬁssion rate (~ 5 × 1020
associated with grain growth is negligible compared with gas bub-                         ﬁssions/m3 ), an eﬃcient approach should be developed to deal
ble swelling; and 3) compared with the sink and emission of de-                           with the fast interstitial diffusion. Rate theory modeling shows that
fects from grain boundaries and interfaces, interstitial clustering                       the increase of resolution rate (which is proportional to the ﬁssion
and growth is the key mechanism for the rapid gas bubble growth                           rate) decreases the gas bubble swelling kinetics while the increase
observed in irradiated UMo.                                                               of ﬁssion rate increases the swelling kinetics [45]. Therefore, we
12                                            S. Hu, W. Setyawan and B.W. Beeler et al. / Journal of Nuclear Materials 542 (2020) 152441


need to further improve the model to handle the fast diffusion of                             [12] Y.B. Miao, K. Mo, B. Ye, L. Jamison, Z.G. Mei, J. Gan, B. Miller, J. Madden,
interstitials and take the gas atom resolution into account. In ad-                                J.S. Park, J. Almer, S. Bhattacharya, Y.S. Kim, G.L. Hofman, A.M. Yacout, High-en-
                                                                                                   ergy synchrotron study of in-pile-irradiated U-Mo fuels, Scr. Mater. 114 (2016)
dition, more systematic and consistent experimental data includ-                                   146–150.
ing the effect of grain size and morphology, ﬁssion rate, and 235U                            [13] L.Q. Chen, Phase-ﬁeld models for microstructure evolution, Annu. Rev. Mater.
inhomogeneity on gas bubble structures and swelling kinetics are                                   Res. 32 (2002) 113–140.
                                                                                              [14] Y.L. Li, S.Y. Hu, X. Sun, M. Stan, A review: applications of the phase ﬁeld
required for validating the model.                                                                 method in predicting microstructure and property evolution of irradiated nu-
    In summary, the simulations demonstrate the capability of the                                  clear materials, npj Comput. Mater. 3 (2017), doi:10.1038/s41524- 017- 0018- y.
developed model to study the effect of thermodynamic and kinetic                              [15] P.J. Maziasz, C.J. Mchargue, Microstructural evolution in annealed austenitic
                                                                                                   steels during neutron-irradiation, Int. Mater. Rev. 32 (4) (1987) 190–219.
properties on defect cluster and gas bubble associated growth,
                                                                                              [16] A.D. Brailsford, R. Bullough, Rate theory of swelling due to void growth in ir-
gas bubble structure evolution, and gas bubble swelling kinetics                                   radiated metals, J. Nucl. Mater. 44 (2) (1972) 121 +.
in polycrystalline UMo, and explore the swelling mechanisms. De-                              [17] G.R. Odette, R.E. Stoller, A theoretical assessment of the effect of microchemi-
                                                                                                   cal, microstructural and environmental mechanisms on swelling incubation in
fect and second-phase-precipitate-associated growth are often ob-
                                                                                                   austenitic stainless-steels, J. Nucl. Mater. 122 (1-3) (1984) 514–519.
served in irradiated materials. For example, voids form and grow                              [18] L.K. Mansur, Theoretical evaluation of a mechanism of precipitate-enhanced
on evolving precipitates. The developed model can be extended to                                   cavity swelling during irradiation, Philos. Mag. A 44 (4) (1981) 867–877.
study defect and second-phase-precipitate associated growth in ir-                            [19] H.R. Brager, J.L. Straalsund, Defect development in neutron-irradiated type-316
                                                                                                   stainless-steel, J. Nucl. Mater. 46 (2) (1973) 134–158.
radiated materials.                                                                           [20] L.K. Mansur, Theory and experimental background on dimensional changes in
                                                                                                   irradiated alloys, J. Nucl. Mater. 216 (1994) 97–123.
                                                                                              [21] D. Brimbal, L. Fournier, A. Barbu, Cluster dynamics modeling of the effect of
Declaration of Competing Interest                                                                  high dose irradiation and helium on the microstructure of austenitic stainless
                                                                                                   steels, J. Nucl. Mater. 468 (2016) 124–139.
                                                                                              [22] A.A. Kohnert, B.D. Wirth, Cluster dynamics models of irradiation damage ac-
    The authors declare that they have no known competing ﬁnan-                                    cumulation in ferritic iron. II. Effects of reaction dimensionality, J. Appl. Phys.
cial interests or personal relationships that could have appeared to                               117 (15) (2015).
inﬂuence the work reported in this paper.                                                     [23] A.A. Kohnert, B.D. Wirth, L. Capolungo, Modeling microstructural evolution in
                                                                                                   irradiated materials with cluster dynamics methods: A review, Comp. Mater.
                                                                                                   Sci. 149 (2018) 442–459.
                                                                                              [24] R.E. Stoller, Modeling dislocation evolution in irradiated alloys, Metallur. Trans.
Acknowledgement                                                                                    A 21 (7) (1990) 1829–1837.
                                                                                              [25] J. Bardeen, C. Herring, John Wiley and Sons, Inc, New York, 1952, p. 261.
   This work was supported by the U.S. Department of Energy, Na-                              [26] A.H. Duparc, C. Moingeon, N. Smetniansky-de-Grande, A. Barbu, Microstructure
                                                                                                   modelling of ferritic alloys under high ﬂux 1 MeV electron irradiations, J. Nucl.
tional Nuclear Security Administration Oﬃce of Material Manage-                                    Mater. 302 (2-3) (2002) 143–155.
ment and Minimization, under DE-AC07-05ID14517. Paciﬁc North-                                 [27] G.S. Was, Fundamentals of Radiation Materials Science, Metal and Alloys,
west National Laboratory is a multiprogram national laboratory op-                                 Springer, New York, 2007.
                                                                                              [28] T.S. Duh, J.J. Kai, F.R. Chen, L.H. Wang, Numerical simulation modeling on the
erated by Battelle Memorial Institute for the U.S. Department of                                   effects of grain boundary misorientation on radiation-induced solute segrega-
Energy under DE-AC05-76RL01830. Computations were performed                                        tion in 304 austenitic stainless steels, J. Nucl. Mater. 294 (3) (2001) 267–273.
on the Constance cluster at Paciﬁc Northwest National Laboratory.                             [29] L.D. Xia, Y.Z. Ji, W.B. Liu, H. Chen, Z.G. Yang, C. Zhang, L.Q. Chen, Radiation
                                                                                                   induced grain boundary segregation in ferritic/martensitic steels, Nucl. Eng.
                                                                                                   Technol. 52 (1) (2020) 148–154.
                                                                                              [30] S.G. Kim, W.T. Kim, T. Suzuki, Phase-ﬁeld model for binary alloys, Phys. Rev. E
Supplementary materials                                                                            60 (6) (1999) 7186–7197.
                                                                                              [31] W. Setyawan, M.W.D. Cooper, K.J. Roche, R.J. Kurtz, B.P. Uberuaga, D.A. Ander-
   Supplementary material associated with this article can be                                      sson, B.D. Wirth, Atomistic model of xenon gas bubble re-solution rate due to
                                                                                                   thermal spike in uranium oxide, J. Appl. Phys. 124 (7) (2018).
found, in the online version, at doi:10.1016/j.jnucmat.2020.152441.                           [32] c. Xoubi, R.T. Primm III, Modeling of the high ﬂux isotope reactor cycle 400,
                                                                                                   ORNL/TM-2004/251, Technical Report (1996) http://www.osti.gov/bridge.
                                                                                              [33] B. Beeler, Y. Zhang, M. Okuniewski, C. Deo, Calculation of the displacement
References                                                                                         energy of α and γ uranium, J. Nucl. Mater. 508 (2018) 181–194.
                                                                                              [34] M.J. Norgett, M.T. Robinson, I.M. Torrens, Proposed method of calculating dis-
 [1] Y.S. Kim, G.L. Hofman, Fission product induced swelling of U-Mo alloy fuel, J.                placement dose-rates, Nucl. Eng. Des. 33 (1) (1975) 50–54.
     Nucl. Mater. 419 (1-3) (2011) 291–301.                                                   [35] B. Beeler, B. Good, S. Rashkeev, C. Deo, M. Baskes, M. Okuniewski, First princi-
 [2] J. Rest, Evolution of ﬁssion-gas-bubble-size distribution in recrystallized                   ples calculations for defects in U, J. Phys. Condens. Matter 22 (50) (2010) 1–7.
     U-10Mo nuclear fuel, J. Nucl. Mater. 407 (1) (2010) 55–58.                               [36] B. Beeler, C. Deo, M. Baskes, M. Okuniewski, First principles calculations of
 [3] M. Meyer, B. Rabin, J. Cole, I. Glagolenko, W. Jones, J.-F. Jue, D.K. Jr., C. Miller,         the structure and elastic constants of alpha, beta and gamma uranium, J. Nucl.
     G. Moore, H. Ozaltun, F. Rice, A. Robinson, J. Smith, D. Wachs, W. Williams,                  Mater. 433 (1-3) (2013) 143–151.
     N. Woolstenhulme, Preliminary Report on U-Mo Monolithic Fuel for Research                [37] K.R. Lund, K.G. Lynn, M.H. Weber, M.A. Okuniewski, Vacancy formation en-
     Reactors, 2017.                                                                               thalpy in polycrystalline depleted uranium, 16th international conference on
 [4] M.K. Meyer, J. Gan, J.F. Jue, D.D. Keiser, E. Perez, A. Robinson, D.M. Wachs,                 positron annihilation (Icpa-16) 443 (2013).
     N. Woolstenhulme, G.L. Hofman, Y.S. Kim, Irradiation Performance of U-Mo                 [38] D.E. Smirnova, A.Y. Kuksin, S.V. Starikov, V.V. Stegailov, Atomistic modeling of
     Monolithic Fuel, Nucl. Eng. Technol. 46 (2) (2014) 169–182.                                   the self-diffusion in gamma-U and gamma-U-Mo, Phys. Met. Metallogr. 116 (5)
 [5] Y.S. Kim, G.L. Hofman, J.S. Cheon, Recrystallization and ﬁssion-gas-bubble                    (2015) 445–455.
     swelling of U-Mo fuel, J. Nucl. Mater. 436 (1-3) (2013) 14–22.                           [39] S.J. Rothman, L.T. Lloyd, A.L. Harkness, Self-diffusion in gamma uranium, Trans.
 [6] S.Y. Hu, D. Burkes, C.A. Lavender, V. Joshi, Effect of grain morphology on gas                Am. I Min. Met. Eng. 218 (4) (1960) 605–607.
     bubble swelling in UMo fuels - A 3D microstructure dependent Booth model,                [40] Y. Adda, A. Kirianenko, Abaissement des coeﬃcients dautodiffusion de lura-
     J. Nucl. Mater. 480 (2016) 323–331.                                                           nium en phase-gamma par des additions de molybdene, de zirconium ou de
 [7] J. Gan, D.D. Keiser, B.D. Miller, A.B. Robinson, D.M. Wachs, M.K. Meyer, Thermal              niobium, J. Nucl. Mater. 6 (1) (1962) 135–136.
     stability of ﬁssion gas bubble superlattice in irradiated U-10Mo fuel, J. Nucl.          [41] K. Huang, D.D. Keiser, Y.H. Sohn, Interdiffusion, Intrinsic Diffusion, Atomic Mo-
     Mater. 464 (2015) 1–5.                                                                        bility, and Vacancy Wind Effect in gamma(bcc) Uranium-Molybdenum Alloy,
 [8] J. Gan, B.D. Miller, D.D. Keiser, J.F. Jue, J.W. Madden, A.B. Robinson, H. Ozal-              Metall. Mater. Trans. A 44A (2) (2013) 738–746.
     tun, G. Moore, M.K. Meyer, Irradiated microstructure of U-10Mo monolithic                [42] J.H. Ke, H.B. Ke, G.R. Odette, D. Morgan, Cluster dynamics modeling of Mn-Ni-Si
     fuel plate at very high ﬁssion density, J. Nucl. Mater. 492 (2017) 195–203.                   precipitates in ferritic-martensitic steel under irradiation, J. Nucl. Mater. 498
 [9] S.Y. Hu, D.E. Burkes, C.A. Lavender, D.J. Senor, W. Setyawan, Z.J. Xu, Formation              (2018) 83–88.
     mechanism of gas bubble superlattice in UMo metal fuels: Phase-ﬁeld model-               [43] A. Leenaers, Y. Parthoens, G. Cornelis, V. Kuzminov, E. Koonen, S. Van den
     ing investigation, J. Nucl. Mater. 479 (2016) 202–215.                                        Berghe, B. Ye, G.L. Hofman, J. Schulthess, Effect of ﬁssion rate on the mi-
[10] H.X. Xiao, C.S. Long, X.F. Tian, S.J. Li, Atomistic simulations of the small xenon            crostructure of coated UMo dispersion fuel, J. Nucl. Mater. 494 (2017) 10–19.
     bubble behavior in U-Mo alloy, Mater. Des. 74 (2015) 55–60.                              [44] A. Leenaers, W. Van Renterghem, S. Van den Berghe, High burn-up structure
[11] S.Y. Hu, W. Setyawan, V.V. Joshi, C.A. Lavender, Atomistic simulations of ther-               of U(Mo) dispersion fuel, J. Nucl. Mater. 476 (2016) 218–230.
     modynamic properties of Xe gas bubbles in U10Mo fuels, J. Nucl. Mater. 490               [45] B. Beelera, J. Colea, W. Frazierb, Y. Gao, I. Glagolenkoa, G. Hofmanc, S.Y. Hu,
     (2017) 49–58.                                                                                 V. Joshib, C. Lavendar, N. Lombardob, Z.G. Mei, G. Parkd, K. Vernere, A. Ya-
                                           S. Hu, W. Setyawan and B.W. Beeler et al. / Journal of Nuclear Materials 542 (2020) 152441                                          13


     coutc, B. Ye, Y.F. Zhang, Microstructural-level fuel performance modeling of          [49] G. Nandipati, W. Setyawan, H.L. Heinisch, K.J. Roche, R.J. Kurtz, B.D. Wirth, Dis-
     U-Mo monolithic fuel, INL Sci. Rep. (2019).                                                placement cascades and defect annealing in tungsten, Part II: Object kinetic
[46] K. Nordlund, S.J. Zinkle, A.E. Sand, F. Granberg, R.S. Averback, R. Stoller,               Monte Carlo simulation of tungsten cascade aging, J. Nucl. Mater. 462 (2015)
     T. Suzudo, L. Malerba, F. Banhart, W.J. Weber, F. Willaime, S.L. Dudarev,                  338–344.
     D. Simeone, Improving atomic displacement and replacement calculations with           [50] G. Nandipati, W. Setyawan, H.L. Heinisch, K.J. Roche, R.J. Kurtz, B.D. Wirth, Dis-
     physically realistic damage models, Nat. Commun. (2018) 9.                                 placement cascades and defect annealing in tungsten, Part III: The sensitivity
[47] C. Bjorkas, K. Nordlund, Comparative study of cascade damage in Fe simulated               of cascade annealing in tungsten to the values of kinetic parameters, J. Nucl.
     with recent potentials, Nucl. Instrum. Meth. B 259 (2) (2007) 853–860.                     Mater. 462 (2015) 345–353.
[48] C. Bjorkas, K. Nordlund, S. Dudarev, Modelling radiation effects using the ab-i-
     nitio based tungsten and vanadium potentials, Nucl. Instrum. Meth. B 267 (18)
     (2009) 3204–3208.
