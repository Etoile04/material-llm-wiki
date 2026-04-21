# Void nucleation, growth, and coalescence in irradiated metals

---

                                                              Journal of Nuclear Materials 378 (2008) 86–97



                                                             Contents lists available at ScienceDirect


                                                      Journal of Nuclear Materials
                                            journal homepage: www.elsevier.com/locate/jnucmat




Void nucleation, growth, and coalescence in irradiated metals
Michael P. Surh *, Jess B. Sturgeon 1, Wilhelm G. Wolfer
Lawrence Livermore National Laboratory, 7000 East Avenue, Livermore, CA 94551, USA



a r t i c l e        i n f o                          a b s t r a c t

Article history:                                      A novel computational treatment of dense, stiff, coupled reaction rate equations is introduced to study
Received 22 January 2008                              the nucleation, growth, and possible coalescence of cavities during neutron irradiation of metals. Radia-
Accepted 12 May 2008                                  tion damage is modeled by the creation of Frenkel pair defects and helium impurity atoms. A multi-
                                                      dimensional cluster size distribution function allows independent evolution of the vacancy and helium
                                                      content of cavities, distinguishing voids and bubbles. A model with sessile cavities and no cluster–cluster
                                                      coalescence can result in a bimodal ﬁnal cavity size distribution with coexistence of small, high-pressure
                                                      bubbles and large, low-pressure voids. A model that includes unhindered cavity diffusion and coalescence
                                                      ultimately removes the small helium bubbles from the system, leaving only large voids. The terminal void
                                                      density is also reduced and the incubation period and terminal swelling rate can be greatly altered by
                                                      cavity coalescence. Temperature-dependent trapping of voids/bubbles by precipitates and alterations
                                                      in void surface diffusion from adsorbed impurities and internal gas pressure may give rise to intermedi-
                                                      ate swelling behavior through their effects on cavity mobility and coalescence.
                                                                                                                        Ó 2008 Elsevier B.V. All rights reserved.




1. Introduction                                                                            At the least, simulations of early irradiation must account for
                                                                                       void nucleation and growth processes, since annihilation, aggrega-
    Irradiation of metals has long been known to culminate in mac-                     tion, and cluster ripening take place concurrently. Transient and
roscopic property changes including void swelling [1]. Characteris-                    steady-state swelling behavior due to these processes have been
tic stable voids and steady volumetric swelling develop for a range                    studied recently using a mean ﬁeld monomer aggregation model
of temperatures and ﬂuxes, independent of whether radiation                            [5–8]. However, only void reactions with vacancy or interstitial
bombardment damage occurs as disseminated Frenkel pairs or as                          monomers are included in these studies. This minimal model of
small defect clusters. This can occur whether or not helium is gen-                    void nucleation gives reasonable swelling behavior as a function
erated along with atomic displacements. In either case, small,                         of temperature and ﬂux [7,8], viz. an observed steady swelling rate
unstable voids, loops, and other defect clusters will develop almost                   around 1%/dpa in austenitic stainless steels and an important
immediately within the irradiated material. Their subsequent evo-                      ﬂux-effect on the measured incubation times [9,10]. While the
lution determines the ﬂuence required to create stable voids and                       results are encouraging, these calculations neglect many of the
achieve steady swelling; this so-called incubation dose includes                       processes believed to shape the microstructure. For example, the
most of the dependence on radiation environment [2–4]. The pro-                        generation and aggregation of helium impurities is not explicitly
cesses that govern microstructure evolution include thermally-                         modeled. Void diffusion, impingement, and direct void–void coa-
activated motion of small defect clusters, mutual impingement,                         lescence are excluded, thus the size-dependent void diffusion
and annihilation or coalescence reactions along with micro-chem-                       [11,12] is effectively set to zero in this model. (Void impingement
ical changes from nuclear transmutation and displacements or dif-                      via the expansion of adjacent cavities [13] is not considered here,
fusion of pre-existing impurities. Radiation simulations should                        as the mean ﬁeld approximation is most appropriate for a small
ideally encompass all of these processes. Typically, existing models                   volume fraction of voids.) Dislocation loop formation, migration,
have included only particular types of defects and reactions or                        and coalescence is not explicitly simulated either. The model [5–
have made other numerical approximations in order to obtain a                          8] can be considered to combine the production and biased diffu-
solution.                                                                              sion of small vacancy and interstitial clusters into effective gener-
                                                                                       ation and reaction rates for monomer species alone, but it is
                                                                                       unclear a priori how a coarse-grained treatment of these processes
                                                                                       affects microstructure evolution.
 * Corresponding author. Tel.: +1 9254222087.
                                                                                           It is now clear that this earlier model must presuppose a ready
   E-mail address: surh1@llnl.gov (M.P. Surh).                                         supply of gas impurity atoms (e.g., oxygen and helium [14]) to
 1
   Perceptive Software, Shawnee, KS 66226.                                             promote the formation of small voids from the radiation-induced,

0022-3115/$ - see front matter Ó 2008 Elsevier B.V. All rights reserved.
doi:10.1016/j.jnucmat.2008.05.009
                                                M.P. Surh et al. / Journal of Nuclear Materials 378 (2008) 86–97                                          87


supersaturated vacancy population. In practice, reasonable correc-                 where q are densities of reactant species m 6¼ n and the rate coef-
tions to void energies may reproduce the approximate void num-                     ﬁcients are
ber density observed in irradiated steel [8]. Ultimately, however,
                                                                                   Kðm; nÞ ¼ Z m;n Am;n Dm;n :                                           ð1Þ
crude models for the apportionment of impurities among the
defect clusters should be supplanted by a detailed accounting of                   Note that an additional factor of 1/2 may be required when m ¼ n,
multicomponent aggregation and coalescence reactions and their                     to prevent double-counting of unique pairs of identical reactant
inﬂuence on the non-equilibrium cluster size distribution. Such                    particles. This factor is not explicitly shown in the deﬁnition of K.
problems are widely addressed in the literature, including gelation,                   Microstructure defect species are limited here to self-intersti-
polymerization, and formation of aerosols and precipitates in solid                tials and vacancies, substitutional and interstitial helium, voids/
or ﬂuid media [15–31]. The numerical methods developed for such                    bubbles, and network dislocations. Vacancy and helium monomers
problems may also be fruitfully applied to radiation swelling. Here,               as well as clusters are characterized by their composition,
a hybrid numerical approach that can encompass the full range of                   n ¼ ðnvac ; nhel Þ, in a two dimensional space. Vacancies and intersti-
possible cluster compositions and cluster reactions in mean ﬁeld is                tials are also specially identiﬁed by ð1; 0Þ ¼ v and ð1; 0Þ ¼ i,
introduced, a Livermore Microstructure Evolution program, LiME.                    respectively; substitutional and interstitial helium by ð1; 1Þ ¼ vh
As a ﬁrst application, the method is applied to the nucleation and                 and ð0; 1Þ ¼ h; and network dislocations by d. Monomer densities
growth of voids with a two-component distribution of cluster com-                  evolve according to
positions, examining the evolution of helium–vacancy clusters                                  X
                                                                                   dqi
[14], while continuing to treat oxygen adsorption by simply reduc-                     ¼ gi           Kðm; iÞqm qi  Kðd; iÞqd qi ;
                                                                                   dt
ing the cavity surface energy by a constant (temperature-indepen-                             m62fh;ig

dent) factor. The method predicts realistic swelling behavior for                  dqh         X
                                                                                       ¼ gh           Kðm; hÞqm qh þ Kðvh; iÞqvh qi ;
ferritic steel in reactor environments.                                             dt        m62fh;ig
    As before, the void distribution function is partitioned into
                                                                                   dqv        X                X                 
overlapping regions [5], treating small clusters with the Master                       ¼ gv    Kðm; vÞqm qv þ    Kðm  v; vÞc½m  qm
                                                                                                                              v
Equation (ME domain) and large ones with Monte Carlo meth-                          dt        m                m
ods (MC domain). This allows self-consistent evolution of the                            þ Kðv2 ; iÞqv2 qi  Kðd; vÞqd qv þ ðKðd; vÞc½eq
                                                                                                                                     v Þqd ;
full void population with no truncation or coarse-graining of                                    X
                                                                                   dqvh
the size domain, no assumptions as to the critical void size or                         ¼ g vh     Kðm; vhÞqm qvh þ Kðv; hÞqv qh
                                                                                    dt
the nature of the nucleation process, and no approximations                                      m

for the overall nucleation rate or duration of the nucleation                                     þ ðKðvh; vÞcv½v2 h Þqv2 h þ Kðv2 h; iÞqv2 h qi :      ð2Þ
stage. The formation and evolution of dislocation loops is not
explicitly modeled; network dislocations and loops are already                     The vacancy–vacancy aggregation term, ðZ v;v Av;v Dv;v Þqv qv , within
                                                                                   the ﬁrst summation for dqv =dt in Eq. (2) includes that two vacancies
described by a single, time-dependent density parameter rather
than a detailed size distribution function [32]. However, the                      are consumed by the reaction, that there is a factor of 1/2 to prevent
                                                                                   double-counting of unique pairs of vacancies from the population
methods used for void evolution would be easily generalizable
to other defect species and reactions, provided that suitable                      qv , and that the relative diffusivity is twice Dv . The net rate is iden-
                                                                                   tical to that used in a previous study [5]. Similar considerations also
mean ﬁeld rate coefﬁcients are speciﬁed for their reaction rate
equations. In particular, future calculations will consider the                    apply to pairs of substitutional helium and to thermal dissociation
                                                                                   of vacancy dimers.
formation, unfaulting, and migration of dislocation loops; loop
coalescence and annihilation; and incorporation of loops in the                         Cluster (n 62 fv; vh; h; ig) densities evolve as
                                                                                              8
dislocation network.                                                                          < X                                  
                                                                                   dqn                                       dm;nm
    The remainder of this paper ﬁrst describes the coupled, stiff,                     ¼ gn þ             Kðm;nmÞqm qnm 1          ð1UðmnÞÞ
non-linear evolution equations for void nucleation, growth, and                     dt        :m2ðv;vh;hÞ                      2
coalescence. It presents the microscopic rate theory model, gives                           X
                                                                                                Kðm;nÞqm qn
an overview of the computational scheme, details the various                                m2ðv;vh;hÞ
numerical methods employed in the calculations, and makes a pre-
                                                                                          þKði;nþvÞqi qnþv Kði;nÞqi qn UðnvÞ
liminary application to void nucleation in irradiated stainless steel.                                                           
The simulations include vacancy, interstitial, and helium genera-                         þ Kðn;vÞcv½nþv qnþv  Kðnv;vÞc½n
                                                                                                                          v qn UðnvÞ
                                                                                            8
tion, aggregation and, annihilation, with or without cluster coales-                        <     X
cence. The results are sensitive to the effects of absorbed impurity                      þ                Kðm;nÞqm qn
atoms on cavity surface energy. They also expose a substantial
                                                                                            : m62ði;v;h;vhÞ
inﬂuence of small, unstable, mobile clusters on the formation of                                                                 
                                                                                            1 X0
critical-sized voids via direct cluster–cluster coalescence. Realistic                    þ      Kðm;nmÞqm qnm ð1UðmnÞÞ                              ð3Þ
                                                                                            2
incubation and swelling behavior cannot be obtained over wide
ranges of temperature and ﬂux without including cluster mobility                   in terms of any direct generation of clusters in the radiation damage
and coalescence.                                                                   cascade, g n ; reactions of existing clusters with monomers (in brack-
                                                                                   ets) that consume or create n-mers including thermal emission of
                                                                                   vacancies, and cluster–cluster reactions (in the second set of brack-
2. Rate theory model                                                               ets) that consume or create n-mers. Factors of 1/2 in the ﬁrst and
                                                                                   last summations prevent double-counting of indistinguishable reac-
    Allowable microstructure reactions (either defect aggregation                  tant pairs, and dm;n ¼ dmv ;nv dmh ;nh where
                                                                                                                             the right hand side consists
or annihilation) are assumed to occur whenever two defects, m                                                                 1 i¼j
                                                                                   of the usual Kronecker deltas, di;j ¼               . The primed summa-
and n, come into contact. Within the mean ﬁeld continuum                                                                      0 i 6¼ j
approximation, the collision rate is proportional to their relative                tion    is     restricted    to     all   pairs   of     reactants   with
diffusivity, Dm;n , and effective collision cross-section, Am;n . As be-           m; n  m 62 fv; vh; h; ig. Defects n  m (n  v, etc.) are restricted to
fore [5,8], a bias factor Z m;n includes the effect of long-range inter-           the domain of allowed compositions                by a step-function:
                                                                                                                              1 nP0
actions [33,34] on the binary reaction rates, Kðm; nÞqm qn ,                       UðnÞ ¼ Uðnv ÞUðnh Þ, where UðnÞ ¼                      . Finally, clusters
                                                                                                                              0 n<0
88                                                       M.P. Surh et al. / Journal of Nuclear Materials 378 (2008) 86–97


never undergo fragmentation in this model, only the thermal emis-                           316 stainless steel is approximately 14% nickel, with 68.08% of that
                                                                                            58
sion of single vacancies.                                                                     Ni and with no naturally-occurring 59Ni. Other relevant materials
    Radiation damage deposition is approximated by the creation of                          parameters for type-316 stainless steel are listed in Table 1.
disseminated monomers (Frenkel pairs), so g n  0 for n 62 fv;                                 Non-interacting diffusion (independent random walks) implies
vh; h; ig. In this case, g i ¼ /n, in terms of the atomic displacement                      Dm;n ¼ Dm þ Dn . Defect collision cross-sections are simply given by
rate, /, and the damage production efﬁciency, n. The total helium
                                                                                            Am;n ¼ 4pðr m þ r n Þ for m 62 fv; vh; h; ig and n 62 fv; vh; h; ig
production is g h þ g vh , with the ratio of interstitial to substitutional
depending on the model. (Here, it is assumed that the helium is all                         Am;n ¼ r m þ b for n 2 fv; vh; h; ig                                        ð6Þ
                                                                                                                                               qﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃﬃ
deposited as substitutional defects.) Conservation of host atoms                                                                                          2
                                                                                            in terms of radii for (spherical) defects, r n ¼ ð3n4vpXÞ (except for
(including transmutation products) requires g v þ g vh  g i . Helium                       interstitial monomers, where r i ¼ r h ¼ r v ). For consistency with ear-
impurities are added with a temperature-independent, gradual                                lier work, cross-sections involving monomers are deﬁned using the
activation of a-emitters. This is modeled for a Fe–Ni–Cr steel                              Burgers vector magnitude in place of a monomer radius.
undergoing neutron bombardment according a two-step activation                                   Bias factors between voids and the four defect monomers are
process, in analogy to the 58Ni(n,c)59Ni(n,a) reaction. Model trans-                        calculated from a mean ﬁeld solution of the diffusion including
mutation rates are treated as free parameters and are ﬁt to the                             stress-mediated interactions [34]. The inﬁnite series describing
experimental helium content in HFIR-irradiated nickel [35,36].                              the image interaction [37] is ﬁt by a simple analytic form, while
The parameters are c, a, and d for the rates of (respectively)                              the modulus interaction [38] is treated analytically. The numerical
58
   Ni(n,c), 59Ni(n,a), and the sum of all transmutations that con-                          results are tabulated for small voids and computed as needed for
sume 59Ni. In terms of the cumulative radiation dose in dpa,                                larger ones. Long range void–void interactions are presently ne-
     R
x ¼ /ðtÞdt (for radiation ﬂux, /):                                                          glected, so Z m;n ¼ 1 for m; n 62 fv; vh; h; ig. In principle, the effect
                                       
d        q58               c   0        q58                                                of any long-range interactions or net drift velocities (e.g., from
                   ¼                         :                                   ð4Þ        external stress or temperature gradients [39]) can be incorporated
dx       q59               þc d         q59
                                                                                            in the void–void reaction rates, so the mean ﬁeld reaction kernel, K,
The 59Ni content, q59 , is obtained from Eq. (4) by transforming to                         has general applicability.
                                                               c
the eigenbasis, where qA ðxÞ ¼ q58 ðxÞ and qB ðxÞ ¼ q59 ðxÞ þ cd q58 ðxÞ                        Thermal emission from vacancy clusters is evaluated by a de-
are solved, and then transforming back. The helium generation rate                          tailed balance argument. Equating vacancy emission and absorp-
is given by                                                                                                                                                      ½n
                                                                                            tion for the n-mer identiﬁes the chemical potential, lv ¼
dqHe                  c                                                                     F ½n  F ½nv , in terms of the n-mer and ðn  vÞ-mer (i.e., void minus
     ¼ aq59 ðxÞ ¼ a      q ð0Þ½edx  ecx                                      ð5Þ        one vacancy) free energies. Rewriting in terms of void internal
 dx                 c  d 58
                                                                                            energies, E, and the inert gas pressure, P:
assuming that only 59Ni(n,a) produces a-particles. The ﬁt parame-
                                                                                                  ½eq ðE E
                                                                                                           ½n   ½nv
                                                                                                                         P XÞ
ters are c ¼ 0:0255, a ¼ 0:0711, and d ¼ 0:297 dpa1. Pristine type                         c½n
                                                                                             v ¼ cv e                            :                                      ð7Þ



Table 1
Model material parameters for type-316 stainless steel
                                                                                                                                                                10
Bulk parameters:                                                               Lattice constant a0                                                3:639pﬃﬃﬃ 10     m
                                                                               Burgers vector b                                                   a0 = 2
                                                                               Atomic volume X                                                    a30 =4
                                                                               Shear modulus l                                                    8:295  1010 Pa
                                                                               Poisson’s ratio m                                                  0.264
                                                                               Damage production efﬁciency n                                      0.1
Vacancy parameters:                                                            Relaxation volume                                                  0.2 X
                                                                               Migration energy Em                                                2:08  1019 J
                                                                               Formation energy Ef                                                2:88  1019 J
                                                                               Formation entropy Sf                                               1.5 kB
                                                                               Pre-exponential factor                                             1:29  106 m2/s
                                                                               Shear polarizability                                               2:4  1018
Self-interstitial parameters:                                                  Relaxation volume                                                  1.50 X
                                                                               Migration energy Em                                                0:320  1019 J
                                                                               Pre-exponential factor                                             1:29  106 m2/s
                                                                               Shear polarizability                                               2:535  1017
Interstitial helium parameters:                                                Relaxation volume                                                  0.60 X
                                                                               Migration energy Em                                                0:320  1019 J
                                                                               Pre-exponential factor                                             1:29  106 m2/s
                                                                               Shear polarizability                                               2:535  1017
Substitutional helium parameters:                                              Relaxation volume                                                  0.2 X
                                                                               Migration energy Em                                                2:08  1019 J
                                                                               Pre-exponential factor                                             1:29  106 m2/s
                                                                               Shear polarizability                                               2:4  1018
Void parameters:                                                               Relaxation volume                                                  0
                                                                               Surface energy c0 ðT ¼ 0Þ                                          2.408 J/m2
                                                                               Temperature derivative dc0 =dT                                     0:440  103 J/m2/K
                                                                               Adsorption factor K                                                0.45–0.80
                                                                               Migration energy Em                                                2:08  1019 J
                                                                                                                                                                    4=3
                                                                               Pre-exponential factor                                             1:29  106 m2/s/nv
Environmental parameters:                                                      Temperature T                                                      300–700 C
                                                                               Flux /                                                             106 dpa/s
                                                   M.P. Surh et al. / Journal of Nuclear Materials 378 (2008) 86–97                                      89


Gas pressure is described with a non-ideal equation of state for he-                  nucleation from sub-critical clusters. Here, the advantages of both
lium versus density and temperature [40]. No volume relaxation is                     rate equations and Monte Carlo methods are combined by parti-
included (i.e., the void volume is nv X). In the absence of surface-ad-               tioning the cluster composition domain into two overlapping re-
sorbed impurity atoms, E½n is parametrized in terms of an effective                  gions. Separate sub-distributions are deﬁned for each, labeled ME
surface energy, c½n , and the surface area of a spherical cavity of                  and MC for treatment by Master Equation and Monte Carlo, with
volume nv X                                                                           P ¼ P ME þ P MC . Such split distribution functions have been used be-
                                                                                    fore in a Fokker–Planck treatment of void growth [5]. Similar ap-
                                  0:8
E½n ¼ c½n 4pr 2n ¼ Kc0 ðTÞ 1          4pr2n :                           ð8Þ        proaches are found in non-equilibrium chemistry [24,30] and
                                 nv þ 2
                                                                                      plasma physics applications [48].
In the continuum limit, c½n approaches that of a ﬂat, clean surface,                     Each sub-distribution of P is composed of a set of discrete
c0 ðTÞ, while it approaches the results of atomic calculations in the                 ensembles of identical clusters, represented by ðn; qÞ for the mul-
limit of small voids [41]. This surface energy is then further reduced                ti-dimensional cluster composition, n, and the paired ensemble
by an constant scale factor, K, to reﬂect the presence of adsorbed                    density, q. The distribution PME ¼ fðn; qÞgME includes interstitials,
oxygen impurities [42] (see Table 1). Finally, the emission rate is ob-               i, and vacancy–helium clusters, n, with 0 6 nv 6 N ME         v   and
                ½n
tained from cv and the vacancy-cluster reaction parameters for the                    0 6 nh 6 N MEh . There is exactly one element for each ME species,
ðn  vÞ-mer. For straight, jogged dislocation segments, cv ¼ cv ,
                                                                  ½d  ½eq
                                                                                      for a total of N ME . Only the densities of the ME elements evolve
the thermal equilibrium concentration. Emission rate coefﬁcients                      over time; the set of allowed compositions is ﬁxed. A sparse, ran-
in Eq. (2) are represented as unary reactions, by including the de-                   dom set, fðn; qÞgMC , approximates P MC for all 0 6 nv ; nh < 1. The
                    ½n
fect-dependent cv within the rate coefﬁcient.                                         total number of elements, N MC , is variable, and there may be none,
    At some maximum density, an over-pressurized bubble would                         one, or many MC elements (each with potentially different values
begin to emit self-interstitials via loop punching [40]. Such a pos-                  of q) at a given composition coordinate n. Both the densities and
sibility is not considered here; instead, an artiﬁcial constraint is                  the compositions of the MC elements evolve with time as defect–
imposed on the helium density in a reactant cluster, nh 6 2nv .                       defect reactions occur. In essence, the elements of PMC also consti-
Any reactions that would yield a higher-density are disallowed.                       tute so-called ‘macroparticles’, already in wide use for non-equilib-
Thermal dissociation of substitutional helium into a vacancy plus                     rium plasma physics problems [49].
interstitial helium is similarly assumed to be energetically impos-                       The various elements of the two sub-distributions are evolved
sible at temperatures of interest. Note that self-interstitial and                    using the most efﬁcient method available. ME–ME reactions (i.e.,
interstitial helium aggregation is excluded since interstitial loops                  those processes with reactants and product among the elements
are effectively part of the dislocation density model. Mixed inter-                   of PME ) are evaluated in a continuum approximation, using the
stitial clusters can develop in principle [43].                                       Master Equation [18]. Monomers can be treated separately by a
    Void diffusivity Dn ¼ Dv =n4=3
                                v  for n ¼ ðnv ; nh Þ. This gives both the            quasi-stationary approximation or evolved along with the rest of
correct monomer value and size-dependence for large cluster dif-                      the ME distribution through the coupled non-linear reaction rate
fusion [11,12], although the activation energy for void migration                     equations. Discrete MC–MC reactions are performed stochastically
should more properly be that for surface diffusion. This diffusivity                  using a Markov Monte Carlo procedure [16]. ME–MC cross-reac-
takes no account of the effect of reversible pinning [44], or internal                tions are included using either the Markov Monte Carlo method
gas pressure on the migration [45], or radiation-enhanced diffusion                   or Poisson-distributed random walks [21,22] for PMC , and using
[46], or, e.g., that vacancy dimer diffusion may be Dv2 ’ Dv . Trap-                  average sink or source terms in the rate equations for P ME . There
ping at dislocations and grain boundaries are not considered. Such                    are also procedures to transfer clusters between the two sub-dis-
features would be straightforward to incorporate in the future.                       tributions and to regulate the number of elements and their
    The dislocation model reproduces measured dislocation densi-                      ensemble densities in PMC , in order to control statistical errors
ties versus dose and temperature [32]. It includes separate source                    and computational cost. This combined algorithm is elaborate, so
and annealing terms in terms of the biased ﬂow of radiation-in-                       the different approaches for each of the various components are
duced vacancies and interstitials. There is one adjustable parame-                    described in detail in the following sections.
ter, l, representing a characteristic dislocation pinning length [32].                    The whole of the material microstructure is evolved over a
This is taken to be independent of the density of voids/bubbles in                    time-step, s, by operator splitting into ﬁve stages. First, ME–MC
the matrix, because the pinning length in stainless steels is more                    reactions for rapidly evolving MC clusters (i.e., those with small
determined by carbide precipitates than by the density of voids/                      nv ) are included with a Markov chain method (Section 3.5). Second,
bubbles.                                                                              the ME–MC reactions for the large, slowly-evolving clusters are
                                                                                      evaluated by Poisson-distributed random walks in composition
                                                                                      space; this encompasses each possible reaction with ME species
3. Numerical method                                                                   (Section 3.5). Third, all MC–MC reactions are evaluated with the
                                                                                      Markov Monte Carlo method. (Section 3.4) This completes the evo-
3.1. Overview                                                                         lution of P MC over s. The fourth stage integrates the ME including
                                                                                      the average source and sink terms from MC defects and disloca-
   Once initial conditions for the microstructure and the tempera-                    tions (Section 3.2). This completes the evolution for the void/bub-
ture- and radiation-environment are ﬁxed, the Master Eqs. (2) and                     ble P. At this point, clusters may be exchanged between PME and
3) and the dislocation model [32] completely determine the void/                      PMC , without affecting the instantaneous total P in any way (Sec-
bubble size distribution function PðtÞ ¼ fqn ðtÞg. These stiff, non-                  tion 3.3). This process may create new MC elements or eliminate
linear coupled rate equations can be integrated numerically for a                     existing ones, in order to control the growth of N MC versus time.
small number of species [18]. However, direct integration becomes                     Fifth and ﬁnally, dislocation evolution is performed using a previ-
impractical for a large domain of cluster sizes. Coarse-grained                       ously-described model [32].
approximations group similar clusters together to reduce the num-                         Overall numerical accuracy is monitored through the conserva-
ber of distinct species [47], but even they are intractable for multi-                tion of host and helium atoms. This must be carefully maintained
dimensional distributions. Monte Carlo schemes for discrete coa-                      in any void nucleation calculation. Obviously, a systematic imbal-
lescence events [16,21] can naturally encompass large voids of                        ance could distort the swelling results, but even small, ﬂuctuating
arbitrary composition; however, they are inefﬁcient for simulating                    numerical errors might potentially affect the predicted nucleation
90                                                       M.P. Surh et al. / Journal of Nuclear Materials 378 (2008) 86–97


behavior. The incubation period represents a sort of barrier-cross-                         void surface energies of 0.4 times c0 ðTÞ. The vacancy/interstitial er-
ing problem, involving nucleation of stable voids and concomitant,                          ror is calculated as the difference between the net integrated ﬂux
self-consistent changes in the vacancy/interstitial populations. In                         of interstitials to the dislocations and the net vacancy content in
practice, a simulation must not spuriously affect the crossing into                         all point defects and defect clusters. The former quantity is ob-
the steady-state; i.e., the associated numerical errors must not sig-                       tained from numerical integration of the rate theory equations,
niﬁcantly promote or inhibit void nucleation.                                               while the latter includes rate theory and Monte Carlo contribu-
    By construction, the procedures in Sections 3.3 and 3.4 will al-                        tions. This particular simulation includes up to N MC ’ 1500.
ways conserve the number of host and helium atoms and exactly                               Increasing N MC to 14 000 changes the overall vacancy content by
treat the number of clusters. Operator splitting of the evolution                           just 10 appm at a dose of 1 dpa, while the density of visible voids
equations between Sections 3.2 and 3.5 does cause ﬁrst-order                                (not shown in the ﬁgure) changes by 2%. Thus, the swelling behav-
time-step errors, but these are conventionally controlled by adjust-                        ior is not sensitive to the N MC -dependent error, i.e., the Monte Carlo
ing the overall time-step, s. Numerical integration errors within                           noise does not unduly promote or suppress nucleation.
Section 3.2 are similarly managed through the VODE tolerance
parameters and the resulting internal time-steps [18]. Conserva-                            3.2. ME–ME reactions
tion errors are dominated by differences between the ME and MC
treatment of reactions (see Section 3.5). In essence, the ﬂux of                                Small defect clusters develop at high concentrations under irra-
ME particles to the MC clusters occurs continuously, while the                              diation, and so they dominate the system of reactions. However,
MC clusters grow in discrete, stochastic jumps. The average rate                            they quickly reach a quasi-stationary distribution wherein further
of growth of an individual MC macroparticle necessarily equals                              reactions cause little change in their densities; i.e., the majority of
the net inﬂux of ME particles, but there are residual, random devi-                         their reactions subsequently cancel one another. Thus, it is much
ations from this trend. This corresponds to random discrepancies                            more efﬁcient to treat their net behavior in a continuum approxi-
in the usual continuity equation, r   ~ ~J ¼ dN=dt (i.e., conservation                     mation than to explicitly account for individual defect reaction
errors). Integrated over time, this Monte Carlo noise accumulates                           events. The ordinary differential equation solver, VODE, provides
as a random walk with zero average expectation. In general, the                             an optimized treatment of stiff, non-linear reaction equations
                                                                                                                qn
magnitude of the RMS error can be controlled by adjusting N MC ;                            [18], given fn ¼ ddt   (Eqs. (2) and (3)) and the Jacobian, J nm ¼ oofqn
                                                                                                                                                                   m
it approaches zero as N MC ! 1. The relative error asymptotically                           for all species. The computational cost increases rapidly with the
approaches zero once steady swelling is achieved – i.e., the net va-                        number of coupled equations, hence the cluster domain is limited
cancy and helium content
                     pﬃﬃ       increases linearly with time while the                       to 0 6 nvac 6 N ME                    ME                ME
                                                                                                            vac and 0 6 nhel 6 N hel . Typically, N vac ¼ 10—100 and
error grows only as t . Thus, the relative error tends to vanish over                       N ME
                                                                                              hel ¼ 2—10.  Some    terms  are  excluded  from   the  Master Equation
long times for the radiation swelling problem.                                              so that all reaction products remain within this ﬁnite domain.
    These artifact statistical ﬂuctuations are relatively most impor-                       Clusters with 0 6 nvac 6 N ME                         ME
                                                                                                                         vac =2 and 0 6 nhel 6 N hel =2 may undergo
tant at low temperatures and especially during incubation, when                             any mutual reactions, but no other ME clusters may undergo any
N MC is small, defect annihilation dominates, and little net swelling                       reactions. These latter clusters are frozen in size, so their density
occurs. For the situations considered here, stable cavities form nat-                       only increases as reaction products accumulate. Frozen clusters
urally under the vacancy supersaturation and the essentially irre-                          eventually transfer to the MC distribution as described in Section
versible aggregation of helium. Thus, the added noise is relatively                         3.3, after which they will undergo reactions according to the MC
inconsequential. For example, the total vacancy content (net swell-                         procedure.
ing) is shown in Fig. 1 along with the instantaneous error for a cal-                           With reaction constraints and separate ME and MC distribu-
culation without cluster coalescence at 106 dpa/s and 500 C, using                         tions, the vacancy Eq. (2) becomes

                                                                                            dqv
                                                                                                ¼ g v ðtÞ þ Kðv2 ; iÞqv2 ðtÞqi ðtÞ
                                                                                             dt
                                                                                                       X                                                 
                                                                                                                                                   1
                                                                                                  þ        ½Kðn; vÞqn ðtÞqv ðtÞ þ Kðn; 0Þqn ðtÞU NME  n
                10000
                                                                                                      n2ME
                                                                                                                                                   2
                            Total Vacancy                                                            Sfast
                                                                                                       v    þ Sslow
                                                                                                               v    ðt 0 Þ qv ðtÞ þ Sfast
                                                                                                                                     0    þ Sslow
                                                                                                                                             0    ðt0 Þ
                            Vacancy Error X1000
                8000
                                                                                                                                                                  ð9Þ

                                                                                            restricting the sums over n 2 ME to reactive defects. Eq. (1) also
                6000                                                                        parametrizes unary vacancy emission reactions as the n-null reac-
                                                                                                                                   ½nv
                                                                                            tion, Kðn; 0Þ ¼ Z nv;v Anv;v Dnv;v cv . S includes the external source

     N (appm)
                                                                                            and sink terms for reactive elements of PME ; it accounts for ME reac-
                4000                                                                        tions with defects in P MC and with dislocations. Vacancy absorption
                                                                                            at MC defects and dislocations is parametrized by Sv , and vacancy
                                                                                            emission by S0 . The vacancy sinks and sources include separate
                2000                                                                        terms that either evolve slowly or rapidly with time. The coefﬁ-
                                                                                            cients are obtained in Section 3.5. The rest of Eq. (2) takes similar
                                                                                            form, with sinks Si , Svh , or Sh . (Only vacancies can be thermally emit-
                   0                                                                        ted from defect clusters, so S0 is the only source term.)
                                                                                                Operator splitting over the time-step, s, is such that external
                        0       0.5           1                 1.5               2         source and sink terms S are held constant as P ME evolves. S is di-
                                           Dose (dpa)                                       vided into terms that evolve slowly or rapidly with time. The bar
                                                                                            indicates an average of the sink strength over the time-step, from
Fig. 1. The total vacancy content (a measure of the swelling) and the net vacancy/          t0 to t0 þ s, useful for rapidly evolving MC clusters, while slowly-
interstitial conservation error are shown for c ¼ 0:4c0 ðTÞ, at T = 500 C, 106 dpa/s.
The macroparticles reach N MC ’ 1500 at 1 dpa, at which point new ones are still
                                                                                            evolving dislocations and large MC voids are simply evaluated at
forming.                                                                                    the beginning t0 (see also Section 3.5 for further details).
                                                M.P. Surh et al. / Journal of Nuclear Materials 378 (2008) 86–97                                       91


   The constrained coalescence Eq. (3) becomes                                     changes in environmental parameters) has concluded. Eq. (10)
                                                                                   for dimers and larger clusters may then be solved while holding
dqn
    ¼ g n ðtÞ                                                                      the monomer concentrations ﬁxed over the time-step. In practice,
 dt
         (                                                                       after a brief transient, the results are comparable to those obtained
                X                                     dm;nm
       þ               Kðm;nmÞqm ðtÞqnm ðtÞ 1               ð1UðmnÞÞ          from the full, coupled, non-linear ME solution.
           m2fv;vh;hg
                                                         2
                                            
            1                       1
       U NME ðnmÞ U NME m                                                      3.3. Transfer between ME and MC domains
            2                       2
            X                                        
                                             1                                         A majority of the ME elements in a small multi-dimensional
                     Kðm;nÞqm ðtÞqn ðtÞU NME n þ½Kði;n
         m2fv;vh;h;ig
                                             2                                     domain will lie near its boundary, and so the majority of the ME
                                                                                 cluster species will be artiﬁcially frozen. The constraints on the de-
                                                   1
       þvÞqi ðtÞqnþv ðtÞþKðnþv;0Þqnþv ðtÞU NME ðnþvÞ                             fect clusters are only lifted after they are transferred to PMC . There
                                                   2
                                                                                 are three desiderata to this transfer process. Foremost, it must
                                                        1
       ½Kði;nÞqi ðtÞqn ðtÞþKðn;0Þqn ðtÞUðnvÞU NME n                            minimize any systematic, constraint-induced errors, therefore
                                                        2                          the density of frozen clusters must be small compared to the rest
         (                                              !           !
                 X                              N ME
                                                             NME                   of P.
       þ                  Kðm;nÞqm ðtÞqn ðtÞU       n U        m
                                                 2            2                        Secondly, the MC computational cost must be controlled, there-
             m62fv;vh;h;ig
                                                                                   fore N MC must be kept small. Rather than increasing N MC at every
        1 X 0
       þ                Kðnm;mÞqnm ðtÞqm ðtÞð1UðmnÞÞ                           opportunity, frozen clusters at n 2 ME are allowed to accumulate
        2 m62fv;vh;h;ig
                                                                                   until exceeding a spawning threshold density, qME      n > qsp , as in
                            !           !)
             NME               NME                                                 [5]. At the end of that time-step, a portion of the accumulated den-
       U          ðnmÞ U        m                                              sity is removed from P ME and transferred to a new element of P MC ,
              2                  2
                                                                                   incrementing N MC
        Sfast
          n þSn
               slow
                    ðt0 Þ qn ðtÞ
                                                                                   ðn; qn ÞME ! ðn; qn  dqÞME þ ðn; dqÞMC                           ð11Þ
                                                                       ð10Þ
                                                                                   with the ME and MC compositions coinciding. If the accumulated
for clusters m; n 2 ME, and n 62 fv; vh; h; ig. The primed summation
excludes n  m 2 fv; vh; h; ig, since the monomer reactions are eval-
                                                                                   qME
                                                                                    n > qsp after each time-step, then the accumulating clusters are
                                                                                   effectively never constrained. Finally, it is imperative to minimize
uated separately. S includes any reactions of the n-mer with the MC
                                                                                   any NMC -dependent Monte Carlo statistical error. Individual MC ele-
clusters and with dislocations. There are no reactions that consume
                                                                                   ments with the largest q will contribute the most to this error.
frozen clusters, so their concentration increases with time.
                                                                                   Therefore, if qME
                                                                                                  n  qsp at the end of a time-step, then DN > 1
    A subset of the disallowed reactions would produce clusters
                                                                                   new MC elements are created, as
that still lie within the ME domain. These have been excluded,
for simplicity and to better resemble an earlier scheme for mono-                                                          MC
                                                                                                                         dq
mer aggregation [5]. Speciﬁcally, a homogeneous boundary condi-                    ðn; qn ÞME ! ðn; qn  dqÞME þ DN  n;                             ð12Þ
                                                                                                                         DN
tion is imposed on the Fokker–Planck equation in Ref. [5], at
n ¼ N ME
       vac . Clusters that grow to the boundary are removed from                   Equivalently, MC elements with large q may be split into identical
the Master Equation treatment and accumulated separately, during                   macroparticles with smaller densities. The chosen values for s,
which time they are prevented from changing size. This is equiva-                  qsp , and the functional dependence of DN on dq control the NMC -re-
lent to keeping those N ME vac -sized clusters within P
                                                        ME
                                                           but disabling           lated statistical error and computational cost for a simulation. Typ-
all of their reactions. Frozen clusters are then intermittently trans-             ically, log2 ðDNÞ ¼ Intðlog30 ðdq=qsp ÞÞ.
ferred to P MC , where they are no longer constrained [5].                             For example, the distribution in Fig. 2 shows the production of
    Ideally, the ME domain will encompass all non-zero generation                  many MC macroparticles containing 2–4 helium atoms; these react
terms, g n , and include as many sub-critical or transient defect clus-            and form a plume that extends to nv ’ 100 (beyond the view of the
ter species as possible. A relatively small domain of N ME      v  ’ 60,           ﬁgure). The ME domain used in this example also includes frozen
N ME
  h ’ 4 is chosen here, reﬂecting the computational demands that                   cluster species with 5–9 helium; these species have not yet
coalescence imposes.                                                               reached the threshold density. They eventually spawn MC ele-
    Similarly to [5], the solution is recorded at exponentially-                   ments, but at a much slower rate than for the near-critical sizes
increasing intervals, up to some smax . This time-step is irrelevant               of 2–4 helium. Even at this early time, the total density of con-
to the ME evolution itself, which advances by adaptive sub-steps.                  strained ME clusters is small compared to the MC population so
However, s controls errors from operator splitting of the evolution                constraint errors are minimized.
equations, and it governs the creation of MC elements, as described                    Since qsp cannot be made arbitrarily small in practice, it is use-
below.                                                                             ful to add a second transfer mechanism. When a pre-existing MC
    Because the sink/source terms, S, are evaluated by a discrete MC               element at n falls inside the frozen ME domain, the change:
method, they introduce a ﬁctitious noise to the continuum rate
equations. This partly manifests as step-function discontinuities                  ðn; qn ÞME þ ðn; qn ÞMC ! ðn; qn  dqÞME þ ðn; qn þ dqÞMC         ð13Þ
in the sink strength over successive time-steps, which in turn
causes transient relaxation in the concentrations of the ME species.               leaves the total distribution unchanged. N MC remains constant, so
The numerical solution tries to accurately follow the transients,                  the calculation remains tractable. In practice, the maximum amount
potentially making the fully coupled, non-linear evolution inefﬁ-                  dq 6 qn is transferred until the receiving MC element reaches a cut-
cient, when large time-steps are otherwise possible. Rather than                   off density, qMC
                                                                                                 n þ dq 6 qmax (where typically, qmax ’ 2qsp to 10qsp .)
faithfully simulating these spurious transients at late times, it                  The cutoff prevents over-weighting of individual Monte Carlo ele-
may be preferable to solve the monomer concentrations (Eqs. (2),                   ments so as to control the statistical error.
(9), etc.) in the quasi-stationary approximation after any real tran-                  At low temperatures, a very high density of small bubbles can
sient behavior (due to the abrupt onset of irradiation or other                    coexist with a moderate density of large, low-pressure voids. Such
92                                                    M.P. Surh et al. / Journal of Nuclear Materials 378 (2008) 86–97


                                                                                         3.4. MC–MC reactions
           10
                                                                Density
                                                                                            Coalescence problems are frequently treated by a Markov
                                                                    m 3
                                                                                         Monte Carlo method [16]. A straightforward approach deﬁnes a ﬁ-
                                                               10
                                                                    22
                                                                                         nite volume, V, containing N (i.e., N MC ) discrete clusters of sizes fng
                                                                    19                   that stochastically evolve to a new N  1 population fn0 g through
                                                               10
                                                                    16
                                                                                         the binary coalescence of any pair of particles. The average rate
                                                               10                        of reaction between the ith and jth particles is simply
                                                               10
                                                                    13
                                                                                         Kðni ; nj Þ=V 2 per unit volume. The total rate of reaction of all N clus-
     #He    5                                                       10                   ters is RN , where
                                                               10

                                                                                                X
                                                                                                i
                                                                                         Ri ¼           Rk;N                                                  ð14Þ
                                                                                                  k¼1


                                                                                         and

                                                                                                  X
                                                                                                  j
                                                                                                         1
                                                                                         Ri;j ¼            Kðni ; nk Þ=V                                      ð15Þ
            0                                                                                     k¼1
                                                                                                         2

                0                         25                               50            in terms of the sum over reactions in the entire volume, V, assuming
                                      # Vacancies                                        they are uncorrelated and occur in parallel. Ri;N is proportional to
                                                                                         the rate at which cluster i reacts with all other clusters. A stochastic
Fig. 2. A portion of the void/bubble distribution for a model with mobile monomer        sequence of discrete reactions may be constructed from these
defects and sessile clusters, c ¼ 0:8c0 ðTÞ, at T = 300 C, 106 dpa/s, and
                                                                                         parameters. The random interval, dt, to the next reaction is obtained
32  103 dpa. For reference, the largest void in the distribution contains 110
vacancies (not shown). The solid lines display the loci of stable and unstable
                                                                                         from a uniform variate, x 2 ð0; 1, as [50]:
equilibrium cluster compositions, based on average vacancy accumulation rates.
                                                                                         dt ¼  lnðxÞ=RN :                                                    ð16Þ
This distribution has not been smoothed – the pixellated appearance reﬂects
discrete cluster compositions.                                                           The ﬁrst cluster of the random reaction pair, i, is selected with a
                                                                                         probability proportional to Ri;N , from y 2 ð0; 1 and
                                                                                         Ri1     Ri
                                                                                              <y6    ;                                                        ð17Þ
distributions are most efﬁciently treated by making qmax size-                            RN      RN
dependent, so that the maximum macroparticle densities are high
                                                                                         where R0  0. Finally, the reaction counterpart, j, is identiﬁed from
in the region of bubbles, but low in the region of voids. Macropar-
                                                                                         z 2 ð0; 1 and
ticles can freely wander between the two regions. Accordingly, if
macroparticle A moves to a region where qA > qmax , it may be split                      Ri;j1     Ri;j
into two identical parts; or if two MC elements at the same coordi-                             <z6                                                           ð18Þ
                                                                                          Ri;N      Ri;N
nate have qA þ qB < qmax , they may be united into one.
    In problems of reversible nucleation and growth, small MC clus-                      with Ri;0  0. This selects j with a probability proportional to
                                                                                         1
ters may shrink and disappear. It is computationally inefﬁcient to                       2
                                                                                           Kðni ; nj Þ=V. The procedure repeatedly selects new x, y, and z for
follow unstable clusters by Monte Carlo methods. Accordingly,                            the next event, increments the system time by (new, random, dif-
macroparticles of the smallest vacancy clusters (with both                               ferent) amount dt, performs the reaction i þ j, and recalculates R
                                                                                                                                                       P
nvac < N min       ME
           vac < N vac and nhel ¼ 0) are deleted at the end of each                      for the next iteration. This repeats until the elapsed time,     dt, ex-
time-step and their density returned to the corresponding element                        ceeds the maximum time s. Since the last reaction falls outside the
of P ME . (The numerical solution of the ME automatically accommo-                       desired interval, it is discarded without being performed. The proce-
dates any subsequent transients by adjusting its internal                                dure may then be started anew for subsequent, regular time-steps,
time-steps.) The minimum MC size should be large enough that                             s. In effect, the overall algorithm employs stochastic sub-steps to
macroparticles at the threshold only rarely shrink to monomer                            evaluate MC–MC reactions during the ﬁxed interval, s.The choice
sizes during the interval s. It should also be far enough from                           of two random numbers to select the pair, i; j, differs from the usual
N ME
  vac =2 that the cycle ME!MC!ME (involving creation of a new                            scheme, where the pair is selected from a single value. In either
macroparticle, shrinkage of the constituent clusters, and transfer                       case, the search for i and j takes oðlog 2 ðNÞÞ operations using the
of that element back to PME ) is infrequent. In practice,                                method of bisection [51]. However, separate selection of i and j
Nmin ¼ NME =4 is used, and these two criteria are accomodated by                         makes it possible to record all Rm with oðNÞ storage space and a
taking the largest possible NME . Helium clusters are never returned                     one-time computational effort of oðN 2 Þ. Once i is determined, Ri;m
from MC to ME distribution; helium emission is not permitted, so                         may be tabulated with oðNÞ effort for all m, so the full matrix need
the clusters will only grow along the helium axis.                                       not be stored. Finally, after i and j react, the Rm may be updated with
    In the examples considered here, all ME clusters are sub-critical                    oðNÞ effort by replacing only those terms involving the old clusters i
for N ME
       vac ’ 60, so that newly-created MC particles frequently shrink                    and j with the results for a single new, coalesced cluster, and re-
and are annihilated. This is especially true at low temperatures,                        indexing to account for the lost cluster. Since RN is an extensive
when the proliferation of small voids favors vacancy/interstitial                        quantity for a given total density, evolution of N particles over a ﬁ-
recombination. Here, this ‘rare event problem’ for nucleation of                         nite interval requires oðN 2 Þ effort and oðNÞ storage. Specifying the
stable voids from small vacancy clusters is at least improved from                       binary reaction rate coefﬁcients, K, as a half-triangular matrix in-
conventional kinetic Monte Carlo methods, where even the mono-                           creases the efﬁciency marginally.This MC scheme has difﬁculty
mers would be treated stochastically.                                                    modeling widely varying concentrations of reactants (e.g., the
    Ultimately, direct application shows this mixed scheme is suit-                      monomer density is typically orders of magnitude higher than the
able for radiation damage calculations to high doses.                                    large clusters for radiation damage). Also, N decreases after every
                                                          M.P. Surh et al. / Journal of Nuclear Materials 378 (2008) 86–97                                            93


coalescence, which increases the statistical noise. There are meth-                          ðn; qn ÞMC ! ðm þ n; qn ÞMC                                            ð23Þ
ods that preserve N [19,27]. However, other approaches make it
possible to preserve N and encompass a wider range of densities                              as a discrete reaction with an average rate of Kðm; nÞqm . A stochas-
at the same time. In the approach taken here, the discrete MC ele-                           tic sequence of reactions at these average rates will approach the
ments are macroparticles, widely used in, e.g., non-equilibrium sim-                         continuum behavior of Eq. (22) in the limit N MC ! 1. A single reac-
ulations of plasma physics [49]. (This is distinct from related,                             tion can change a macroparticle size, cross-section, and reaction
‘weighted particle’ schemes for coagulation [20,23,52].) Here, the                           rate substantially, if m is comparable in size to n. Accordingly,
jth macroparticle in the system consists of an ensemble of clusters                          ME–MC reactions for such ‘small’ MC clusters n < n0 are included
all of the same composition ðnj ; qj Þ. Consistent with the Gillespie                        by the Markov Monte Carlo scheme described above, and the reac-
procedure, macroparticle reactions are evaluated discretely, so clus-                        tion parameters are immediately updated to reﬂect the change,
ters in an ensemble react simultaneously but otherwise stochasti-                            before evaluating the next reaction.
cally. However, here reactants will generally have different                                     Reaction events are randomly performed from the N MC  N ME
ensemble densities, qL < qH , which are independent of their sizes/                          matrix of reaction rates, at overall rate Q. If the next event occurs
compositions, nL ; nH . The lower-density macroparticle, L, reacts                           within the desired interval, the ith MC element is selected as a
completely, leaving behind an unchanged portion qH  qL of clus-                             reactant with probability Q i =Q , where
                                                                                                    X
ters from the higher-density ensemble, H. The total cluster density                          Qi ¼             Kðni ; mj Þqmj                                        ð24Þ
declines, but N stays constant, and N-dependent errors remain stea-                                   j
dy over time.
    Macroparticle reaction rates (analogous to Eq. (15)) are deﬁned                          for reactive elements mj 2 ME and
so as to reproduce the continuum limit as N ! 1. Pairs i and j, with                                X
                                                                                                    N MC

qi < qj , react according to                                                                 Q¼            Qi                                                       ð25Þ
                                                                                                    i¼1
ðni ; qi Þ þ ðnj ; qj Þ ! ðni þ nj ; qi Þ þ ðnj ; qj  qi Þ                      ð19Þ
                                                                                             The jth ME element is selected as a reactant with probability
at an average rate of Kðni ; nj Þqj .                                                        Kðni ; mj Þqmj =Q i . Finally, the time index is updated, the reaction is
   Two macroparticles of the same density (qi ¼ qj ¼ q; i 6¼ j) react                        performed, and Q is revised. This is analogous to the Markov proce-
as                                                                                           dure for MCMC reactions, except that the reaction matrix is full-
                                                                                             rectangular rather than half-triangular and that the rates are always
ðni ; qÞ þ ðnj ; qÞ ! ðni þ nj ; q=2Þ þ ðni þ nj ; q=2Þ                          ð20Þ        proportional to the density of the ME reactant.
                                                                                                 As for the corresponding evolution of P ME , the instantaneous
at an average rate of Kðni ; nj Þq. The product is simply split into two                     source/sink terms, Eq. (22), change after each discrete reaction
equal pieces so that N remains constant. Finally, the individual clus-                       event in PMC . This may happen multiple times during the interval
ters within a single macroparticle ensemble may coalesce with one                            s. It is not computationally practical to account for this variation
another, so there is also a unary reaction process                                           in detail (e.g., by evolving PME over each individual Markov sub-
ðni ; qi Þ ! ð2ni ; qi =2Þ;                                                      ð21Þ        step, dt). Instead, PME is updated by operator splitting; it is evolved
                                                                                             over the full time-step s only after all ME–MC and MC–MC reac-
which also proceeds at an average rate of Kðni ; ni Þqi . This possibility                   tions in PMC are performed. To minimize any convergence error
modiﬁes Eq. (15) to include a non-zero reaction rate for i ¼ j.                              for ﬁnite s, the instantaneous sink strength n < n0 can be replaced
   Macroparticle dynamics never corresponds to an atomistic sim-                             with a weighted time average over the interval
ulation for ﬁnite N. Instead, this is a distinct, approximative dis-                                                           "                          #
cretization of the continuum equations themselves, in the same                                             Z t0 þs                 X
                                                                                                   1
spirit as earlier approaches [5]. Again, PðtÞ is approximated here                           Sfast
                                                                                              m ¼                       dt             Kðm; nðtÞÞqm ðtÞ             ð26Þ
                                                                                                      s        t0              n2MC
by a sparse set of elements without arbitrarily imposing some                                                              "                                    #
coarse-graining of ﬁnite difference equations for the distribution.                                       1X                   X
                                                                                                    ¼               dt j           Kðm; nðt j1 ÞÞqm ðt j1 Þ       ð27Þ
Since the computational cost scales as oðN 2 Þ for a dense reaction                                       s     j              n
matrix, the method is also efﬁcient. This is especially advantageous
in higher dimensions, e.g., in describing helium–vacancy–impurity                            ﬁnally expressed as a sum over random sub-intervals, dt j , between
clusters.                                                                                    discrete reaction times, tj1 and t j as determined by Eq. (16).
                                                                                                 Such attention to detail is unnecessary for large MC clusters
3.5. ME–MC reactions                                                                         (and for network dislocations), where rapid reactions with highly
                                                                                             mobile defects (i.e., small m) do not substantially change the sink
    Additional schemes are required for treating reactions between                           strength over short intervals. Thus, it is sufﬁcient to update param-
ME and MC elements. In the continuum approximation, reaction                                 eters for the large n clusters at the end of each time-step. In this
with external entities, n 62 ME, introduces unary sink terms to                              case, MC clusters are evolved using a Poisson-distributed random
the rate equation for m 2 ME, cf. Eqs. (9) and (10)                                          variate, PðxÞ, [21,53] for the number of reactions that occurs during
               "                                #                                            s. These MC elements are only updated at t0 þ s, with all reactions
                 X
Sm ðtÞqm ðtÞ ¼     K ðm;nðtÞÞqn ðtÞþKðm;dÞqd ðtÞ qm ðtÞUðNME =2mÞ;                          accumulated in each of the N ME channels
                 n2MC                                                                                                                                         !
                                                                                                                           X
                                                                                 ð22Þ        ðn; qn Þ !             nþ             mP½sKðm; nÞqm ; qn :            ð28Þ
                                                                         MC                                                m2ME
where the summation includes all elements fðnðtÞ; qn ðtÞg at time
t and where Kðm; dÞ includes reactions with network dislocations.                            Eq. (28) is the discrete analogue of the Gaussian-distributed random
The sink term, S, is identically zero for constrained ME defects. At                         walk used previously [5].
present, Kðm; dÞ is only non-zero for m ¼ ð1; 0Þ; ð1; 0Þ and for va-                           The corresponding ME sink term n P n0 is
cancy emission Kð0; dÞ.
                                                                                                                    X
   The counterpart to Eq. (22) is expressed for n 2 MC in the mac-                           Sslow
                                                                                              m ðt 0 Þ ¼                Kðm; nðt 0 ÞÞqn ðt 0 Þ þ Kðm; dÞqd ðt0 Þ    ð29Þ
roparticle scheme by                                                                                            n2MC
94                                             M.P. Surh et al. / Journal of Nuclear Materials 378 (2008) 86–97


including the dislocation contribution, assuming that qd ðtÞ is slowly                       20
changing.
    Finally, discrete reactions could also be evaluated by a rejection
method, given a Majorant kernel Mðm; nÞ P Kðm; nÞ [52]. For
example, the reaction rates, M, can be evaluated on a coarse grid
of ni where all reactants ni 6 n 6 ni þ 1 are initially treated alike.
In a variant of this approach, M may be chosen to be a sum of prod-
ucts [23],
                                                                                                                                                   Density
Mðm; nÞ ¼ ~
          MðmÞ  ~
                 MðnÞ:                                                ð30Þ
                                                                                     # He    10                                                         m 3
It is then only required to evaluate N MC vectors, M, (of one or more                                                                               10
                                                                                                                                                         22

dimensions) and to take dot products. Either approach is easier than                                                                                     19
                                                                                                                                                    10
directly computing N MC ðNMC þ 1Þ=2 binary rate coefﬁcients for Eqs.
                                                                                                                                                         16
(14), (15). The Majorant kernel is selected to be easy to evaluate and                                                                              10
to predict a faster (or equal) event rate than the true system. To cor-                                                                             10
                                                                                                                                                         13

rect for any overestimate, the time index is updated according to                                                                                        10
                                                                                                                                                    10
the usual Markov Monte Carlo procedure, but the reaction is only
performed if a uniform variate, w 2 ð0; 1 also satisﬁes w 6
Kðm; nÞ=Mðm; nÞ. Thus, excess events predicted by M are rejected                              0
(with the required probability 1  K=M). At present, the full reaction
                                                                                                  0                             100                               200
rate coefﬁcients from Eq. (1) can be evaluated very efﬁciently, so
                                                                                                                           # Vacancies
this method is not employed here. However, this is expected to be
advantageous when biased cavity–cavity, cavity–loop, and loop–                    Fig. 3. A portion of the void/bubble distribution as in Fig. 2, but at T = 500 C,
loop reactions are included in the future.                                        106 dpa/s, and 16  103 dpa. The distribution has been smoothed for the large
                                                                                  clusters, where Monte Carlo data is increasingly sparse. The solid lines display the
                                                                                  stable and unstable equilibrium cluster compositions.
4. Results

4.1. Monomer aggregation model                                                               60

    A high density of trapping/recombination centers is believed to
delay the onset of void swelling [44,54,55]. Traps hinder void diffu-
sion and coalescence and prolong the incubation stage. The sim-
plest trapping model assumes that all dimers and larger clusters
are immobile: Dn  0 for all n 62 fv; vh; h; ig, so that the last two
summations in Eq. (3) are zero. If Eq. (2) is solved separately from
the remainder of the Master Equation (Eq. (3)) in a quasi-stationary                                                                              Density

                                                                                      # He
approximation, then that problem may be solved by existing meth-                             30                                                       m 3
ods [5,56]. However, here the problem is simply treated as a limit
                                                                                                                                                        19
case of Smoluchowski’s coagulation equation.                                                                                                       10
    Initial cluster populations are shown in Figs. 2–4 for type-316                                                                                     16
                                                                                                                                                   10
stainless steel irradiated to low doses at 106 dpa/s and 300, 500,
                                                                                                                                                        13
and 700 C. It is well-known that helium–vacancy clusters may be                                                                                    10
separated into distinct species (of equilibrium bubbles and stable                                                                                      10
or unstable voids), according to their size-dependent free energies.                                                                               10
Accordingly, the ﬁgures are marked with black lines where the net
average vacancy addition rate for the defect clusters approaches
                                                                                              0
zero. The leftmost black line in Figs. 2–4 represents a hard wall
for over-pressurized bubbles: by ﬁat, bubbles cannot reach densi-                                 0                           100                                 200
ties greater than two helium per vacant site. Here, this is imposed                                                       # Vacancies
by disallowing further reactions with helium- and self-interstitials.
                                                                                  Fig. 4. The full void/bubble distribution as in Fig. 3, but at T = 700 C. The curved
    Other lines separate clusters that add or lose vacancies on aver-             solid line locates the stable equilibrium bubbles; the critical void size is not visible
age. Small, over-pressurized bubbles tend to add vacancies until                  on this scale.
reaching the next line in the ﬁgures, where stable helium bubbles
are in dynamic equilibrium with the vacancy and interstitial pop-
ulation. (This approximates the line of bubbles with P ’ c=2r,                    which point they grow by adding vacancies in excess of helium,
which would be in equilibrium in the absence of a vacancy and                     forming a plume of rapidly-growing voids in the size distribution.
interstitial supersaturation.) The stability of these bubbles is re-                 Voids are here simply taken to be cavities with higher vacancy/
ﬂected by their elevated concentration in that region, especially                 helium ratio than any bubble species of the same helium content.
visible in Fig. 4. Stable bubbles tend to grow along the equilibrium              An approximately parabolic region under the black curves bounds
line as they accumulate helium, while adjusting their vacancy con-                a set of small, unstable voids that tend to lose vacancies and shrink
tent on average to remain in equilibrium. Finally, bubbles cannot                 back towards the equilibrium bubble conﬁguration. For example,
exceed some critical helium content – larger clusters are stable                  this ranges from the origin to vacancy/helium compositions of
voids that tend to add vacancies and grow to arbitrary size. This                 (19, 11) and (94, 0) in Fig. 3. The rightmost solid line identiﬁes
is seen in Fig. 3; there the clusters grow along the line of stable               the critical or unstable equilibrium void compositions; larger voids
bubbles until reaching a critical helium content (11 heliums), at                 tend to add net vacancies with time. Note that a percentage of
                                                         M.P. Surh et al. / Journal of Nuclear Materials 378 (2008) 86–97                                                      95


equilibrium bubbles in Fig. 3 are able to ﬂuctuate in vacancy con-                          lium mobility results in fewer cavities (7–81020 m3 at 700 C),
tent across the barrier of unstable voids. That is, they become sta-                        and a smaller density of bubbles escape to become stable voids
ble voids without having ﬁrst reached the critical helium content.                          and contribute to steady swelling.
Similarly, helium dimers are readily able to cross the barrier of
unstable voids in Fig. 2. Very large voids ultimately become neutral                        4.2. Cluster coalescence model
(unbiased) sinks, adding helium/vacancies at an average rate of
1:200 (based on anticipated asymptotic swelling of 1%/dpa and                                   The other simpliﬁed limit of defect trapping is to neglect it en-
model helium generation around 50 appm/dpa). Thus, voids ap-                                tirely and assume that clusters diffuse freely according to their
proach a line of constant composition.                                                      size. The predicted void size distribution changes signiﬁcantly
    Except for a brief transient at the onset of irradiation, the va-                       when coalescence is included. This is seen in Figs. 6 and 7, for
cancy monomer concentration decreases monotonically with time                               the same temperatures as in Figs. 2 and 3.
as the total sink strength of the microstructure rises with dose.                               Coalescence reactions continually, preferentially consume the
After a few dpa, production of a-particles also peaks, and the he-                          smaller, more mobile clusters. The largest voids grow an order of
lium monomer concentration also declines. During this extended                              magnitude larger through coalescence, making the distribution of
period, equilibrium bubbles continue to grow by adding helium,                              stable void sizes substantially broader than before. Very large voids
they continue to reach the critical size, and they continue to be-                          achieve such low diffusivities as to be effectively immobile; this re-
come voids. However, the critical size for equilibrium bubbles in-                          sults again in a terminal void population. At low temperatures, the
creases with time (as a function of declining qv ), and the rate of                         removal of small unstable or equilibrium defect clusters reduces
formation of new helium dimer nuclei and bubble growth rates de-                            the number of recombination centers, suppresses damage annihi-
crease (as a function of declining qh þ qhv ). This causes the rate of                      lation, and speeds the formation of large, stable voids. This en-
void formation to decrease gradually with time, giving a broad void                         hances low temperature swelling. At high temperatures, this
size distribution. Eventually, the larger stable bubbles become                             same coalescence of small clusters greatly reduces the total num-
TEM-visible, and the overall size distribution becomes bimodal.                             ber of helium bubbles and voids, so that the total void sink strength
    The time-dependent volumetric swelling for this model is                                is kept small and the asymptotic swelling rate is diminished com-
shown at a series of temperatures in Fig. 5. The low temperature                            pared to the monomer aggregation model (Fig. 8 versus Fig. 5,
system is initially dominated by large numbers of transient, unsta-                         respectively). Small clusters are absorbed as rapidly as new ones
ble vacancy clusters (Fig. 2) that serve as recombination centers                           form, which prevents the formation of a bimodal distribution of
and suppress swelling. So many defect centers form that helium/                             small equilibrium bubbles and large voids. These differences sug-
vacancy ratios are kept low, and helium plays a reduced role in                             gest that competition between trapping and coalescence of very
the initial evolution. As a result, the visible cavity density                              small (mostly TEM-invisible) clusters signiﬁcantly shapes the
(r > 0:5 nm) is sensitive to the surface energy parameter, c:                               microstructure in real irradiated materials.
qvis ¼ 5  1023 m3 for cðTÞ ¼ 0:8c0 ðTÞ and 1  1024 m3 for                                   When coalescence is included, the terminal void density and
cðTÞ ¼ 0:5c0 ðTÞ. Eventually, some vacancy clusters acquire signiﬁ-                         swelling rate remain sensitive to c up to 500 C. The predicted void
cant amounts of helium, and the system is ﬁlled with a high con-                            density at this temperature increases from 7  1019 m3 for
centration of small equilibrium bubbles. These function as                                  c ¼ 0:75c0 to 7  1020 m3 for c ¼ 0:5c0 . The swelling rate for the
recombination centers; they keep the vacancy supersaturation                                former case is only 0.3%/dpa at 50 dpa but reaches 0.8%/dpa for
low so that few, if any, bubbles grow into stable voids. They also                          the latter. This suggests that either the cavity surface energy is sub-
keep the asymptotic swelling rate small. At and above 500 C, swell-                         stantially smaller than the value for the clean metal or that the va-
ing is more a matter of helium bubble formation and growth to-                              cancy clusters have much smaller mobilities than are modeled
wards critical sizes (Figs. 3 and 4). The cavity density and
swelling rates are therefore insensitive to c. The steady swelling
rate of 0.8%/dpa at 500 C is consistent with void swelling in austen-
itic stainless steel [7,8]. At higher temperatures, the increased he-                                  10




                   25

                                T = 300 C
                                T = 500 C
                   20
                                T = 700 C

                                                                                                # He    5




    Swelling (%)
                   15



                   10



                    5
                                                                                                        0

                                                                                                            0                          100                               200
                   0
                        0   5          10      15        20        25         30                                                   # Vacancies
                                            Dose (dpa)
                                                                                            Fig. 6. A portion of the void/bubble distribution as in Fig. 2 (300 C), but including
Fig. 5. Volumetric swelling curves versus dose in the model that excludes void–             void coalescence and with cðTÞ ¼ 0:5c0 ðTÞ. The distribution has been smoothed for
void coalescence. The cavity surface energy is ﬁxed at cðTÞ ¼ 0:75c0 ðTÞ.                   the large clusters, where Monte Carlo data is sparse.
96                                                        M.P. Surh et al. / Journal of Nuclear Materials 378 (2008) 86–97


                                                                                             defect distribution. A Markov method for smaller clusters accu-
                  10
                                                                                             rately simulates rapid ﬂuctuations in size and in the reaction
                                                                                             parameters, and a Poisson-distributed random walk efﬁciently
                                                                                             treats the more gradual evolution of the largest clusters. Finally,
                                                                                             a macroparticle approach is introduced to encompass large differ-
                                                                                             ences in species densities in the Monte Carlo distribution.
                                                                                                 This hybrid scheme readily treats void/bubble evolution to high
                                                                                             cumulative ﬂuxes for temperatures and dose rates that are charac-
                                                                                             teristic of real reactor systems. Calculations demonstrate that void
     # He             5                                                                      coalescence provides an important channel for consolidating va-
                                                                                             cancy defects into large, stable voids, controlling the duration of
                                                                                             incubation and the terminal void density.
                                                                                                 It is expected that thermal and radiation-induced micro-chem-
                                                                                             ical evolution of solute and precipitate distributions will inﬂuence
                                                                                             the cluster mobility and thereby the macroscopic incubation and
                                                                                             steady-swelling behavior. Some degree of void/bubble trapping
                                                                                             seems to be required in order to obtain a bimodal bubble/void size
                                                                                             distribution, while some coalescence may be needed to give a real-
                      0
                                                                                             istically low terminal void density at higher temperature. The cav-
                                                                                             ity surface energy determines the barrier for nucleation of stable
                           0                   3500                           7000
                                                                                             voids and hence also affects the incubation behavior; this contribu-
                                           # Vacancies                                       tion becomes temperature- and time-dependent if oxygen is
Fig. 7. The full void/bubble distribution as in Fig. 4 (500 C), but including void–void
                                                                                             explicitly modeled. All of these effects can be addressed, in princi-
coalescence and with cðTÞ ¼ 0:5c0 ðTÞ.                                                       ple, by extensions of the method described here.
                                                                                                 These calculations also suggest the importance of additional,
                                                                                             competing processes that are not evaluated at present, such as
                      25
                                                                                             interstitial–interstitial aggregation or cluster annihilation from
                                                                                             void–dislocation reaction. The methods described here can be ex-
                               T = 300 C
                                                                                             tended to treat coalescence of loops as easily as voids, given a suit-
                               T = 500 C                                                     able binary reaction kernel. Such reactions should be included for
                      20
                               T = 700 C                                                     reasons of consistency, besides their likely contribution to tran-
                                                                                             sient and steady swelling behavior. They would be especially
                                                                                             important if radiation damage were introduced as a variety of



       Swelling (%)
                      15
                                                                                             pre-formed defect clusters. Based on the preliminary ﬁndings for
                                                                                             cavity coalescence, more general defect cluster reactions are
                                                                                             expected to have a signiﬁcant inﬂuence on radiation swelling
                      10                                                                     behavior.

                                                                                             Acknowledgements
                       5

                                                                                                This work performed under the auspices of the US Department
                                                                                             of Energy by Lawrence Livermore National Laboratory under Con-
                      0                                                                      tract DE-AC52-07NA27344. MPS acknowledges V.V. Bulatov for
                           0          10                 20                    30
                                            Dose (dpa)                                       an early introduction to Markov chain Monte Carlo methods, e.g.,
                                                                                             Ref. [57].
Fig. 8. Volumetric swelling curves versus dose in the model that includes void–void
coalescence. The cavity surface energy is set to cðTÞ ¼ 0:4c0 ðTÞ.
                                                                                             References

                                                                                              [1] C. Cawthorne, E. Fulton, Nature 216 (1967) 575.
here. The swelling behavior ﬁnally becomes insensitive to the sur-                            [2] F.A. Garner, W.G. Wolfer, J. Nucl. Mater. 122&123 (1984) 201.
face energy by 700 C. In this limit, coalescence reduces the termi-                           [3] T. Okita, T. Kamada, N. Sekimura, J. Nucl. Mater. 283–287 (2000) 220.
                                                                                              [4] T. Okita, T. Sato, N. Sekimura, F.A. Garner, L.R. Greenwood, J. Nucl. Mater. 307
nal void density to 4–51018 m3.
                                                                                                  (2002) 322.
                                                                                              [5] M.P. Surh, J.B. Sturgeon, W.G. Wolfer, J. Nucl. Mater. 325 (2004) 44.
5. Conclusions                                                                                [6] M.P. Surh, J.B. Sturgeon, W.G. Wolfer, J. Nucl. Mater. 328 (2004) 107.
                                                                                              [7] M. Surh, J. Sturgeon, W. Wolfer, J. Nucl. Mater. 336 (2005) 217.
                                                                                              [8] M.P. Surh, J.B. Sturgeon, W.G. Wolfer, J. Nucl. Mater. 328 (2004) 107.
    This paper introduces a mixed Master Equation/Monte Carlo                                 [9] F.A. Garner, in: B. Frost (Ed.), Materials Science and Technology: A
treatment of rate theory calculations in a mean ﬁeld continuum                                    Comprehensive Treatment, vol. 10A, VCH Verlagsgesellschaft mbH, 1998, p.
                                                                                                  419.
approximation. This enables ﬂexible treatment of the defect den-                             [10] T. Okita, T. Sato, N. Sekimura, F.A. Garner, in: Proceedings of the Fourth Paciﬁc
sity variables, using different algorithms to treat the various reac-                             Rim International Conference on Advanced Materials and Processing, vol.
tions as efﬁciently as possible. The approximately quasi-stationary                               PRICM-4, Aoba, Aramaki, Aoba-ku, Sendai, 2001.
                                                                                             [11] G.W. Greenwood, M.V. Speight, J. Nucl. Mater. 10 (1963) 140.
distribution of small, unstable or transient clusters is treated (as
                                                                                             [12] E. Gruber, J. Appl. Phys. 38 (1967) 243.
much as possible) by solving continuum rate equations. This elim-                            [13] L.K. Mansur, Nucl. Technol. 40 (1978) 5.
inates the need to evaluate rapid individual reactions that mostly                           [14] L.K. Mansur, W.A. Coghlan, J. Nucl. Mater. 119 (1983) 1.
                                                                                             [15] A.H. Marcus, Technometrics 10 (1968) 133.
cancel one another. Larger clusters are treated by Monte Carlo
                                                                                             [16] D. Gillespie, J. Atmos. Sci. 29 (1972) 1496.
methods, which treats clusters of arbitrary size and composition                             [17] A.A. Lushenko, Fizika Atmosfery i Okeana 14 (1978) 738.
without the need for a ﬁxed grid or artiﬁcial discretization of the                          [18] P. Brown, G. Byrne, A. Hindmarsh, SIAM J. Sci. Stat. Comput. 10 (1989) 1038.
                                                        M.P. Surh et al. / Journal of Nuclear Materials 378 (2008) 86–97                                                       97


[19] M. Smith, T. Matsoukas, Chem. Eng. Sci. 53 (1998) 1777.                               [39] G. Cottrell, J. Nucl. Mater. 302 (2002) 220.
[20] H. Babovsky, Monte Carlo Meth. Appl. 5 (1999) 1.                                      [40] W.G. Wolfer, Philos. Mag. A 58 (1988) 285.
[21] D. Gillespie, J. Chem. Phys. 114 (2000) 297.                                          [41] J. Adams, W. Wolfer, J. Nucl. Mater. 166 (1989) 235.
[22] D. Gillespie, J. Chem. Phys. 115 (2001) 1716.                                         [42] C.A. English, B.L. Eyre, J.W. Muncie, Philos. Mag. A 56 (1987) 453.
[23] A. Eibeck, W. Wagner, Ann. Appl. Probab. 11 (2001) 1137.                              [43] W.D. Wilson, Radiat. Eff. 78 (1983) 11.
[24] E.L. Haseltine, J.B. Rawlings, J. Chem. Phys. 117 (2002) 6959.                        [44] R.S. Nelson, J. Nucl. Mater. 19 (1966) 149.
[25] W.I. Friesen, T. Dabros, J. Chem. Phys. 119 (5) (2003) 2825.                          [45] E. Mikhlin, Phys. Status Solidi (a) 56 (1979) 763.
[26] I.I. Laurenzi, S.L. Diamond, Physical Review E 67 (2003) 051103–1.                    [46] D.E. Alexander, R.C. Birtcher, J. Nucl. Mater. 191–194 (1992) 1289.
[27] D. Mukherjee, C. Sonwane, M. Zacariah, J. Chem. Phys. 119 (2003) 3391.                [47] S.I. Golubov, A.M. Ovcharenko, A.V. Barashev, B.N. Singh, Philos. Mag. A 81 (3)
[28] A.H. Alexopoulos, A.I. Roussos, C. Kiparissides, Chem. Eng. Sci. 59 (2004) 5751.           (2001) 643.
[29] F. Filbet, P. Laurencot, SIAM J. Sci. Comput. 25 (6) (2004) 2004.                     [48] A. Solovyev, V. Terekhin, V. Tikhonchuk, L. Altgilgers, Phys. Rev. E 60 (1999)
[30] H. Salis, Y. Kaznessis, J. Chem. Phys. 122 (2005) 054103.1.                                7360.
[31] M. Kraft, Powder Particle 23 (2005) 18.                                               [49] C. Birdsall, A. Langdon, H. Okuda, in: B. Alder, S. Fernbach, M. Rotenberg (Eds.),
[32] W.G. Wolfer, B.B. Glasgow, Acta Metall. 33 (1985) 1997.                                    Methods in Computational Physics, vol. 9, Academic Press, New York, 1970, p.
[33] J.J. Sniegowski, W.G. Wolfer, in: J.W. Davis, D.J. Michel (Eds.), Proceedings of           241.
     Topical Conference on Ferritic Alloys for Use in Nuclear Energy Technologies,         [50] P. MacKeown, Stochastic Simulation in Physics, Springer-Verlag, Singapore,
     Snowbird, Utah, 1983, p. 579.                                                              1997.
[34] M.P. Surh, W.G. Wolfer, J. Comput. Aided Design 14 (2007) 419.                        [51] W.H. Press, B.P. Flannery, S.A. Teukolsky, W.T. Vetterling, Numerical Recipes:
[35] L. Greenwood, F. Garner, B. Oliver, M. Grossbeck, W.G. Wolfer, in: M.L.                    The Art of Scientiﬁc Computing, Cambridge University, 1986.
     Grossbeck, T.R. Allen, R.G. Lott, A.S. Kumar (Eds.), The Effects of Radiation on      [52] K. Sablefeld, S. Rogasinsky, A. Kolodko, A. Levykin, Monte Carlo Meth. Appl. 2
     Materials: 21st International Symposium, ASTM STP 1447, American Society                   (1996) 41.
     for Testing and Materials International, West Conshohocken, PA, 2003.                 [53] W.H. Press, B.P. Flannery, S.A. Teukolsky, W.T. Vetterling, Numerical Recipes:
[36] C. Schaldach, W. Wolfer, in: M.L. Grossbeck, T.R. Allen, R.G. Lott, A.S. Kumar             The art of Scientiﬁc Computing, Cambridge University, 1986.
     (Eds.), The Effects of Radiation on Materials:21st International Symposium,           [54] E.H. Lee, L.K. Mansur, J. Nucl. Mater. 141–143 (1986) 695.
     ASTM STP 1447, American Society for Testing and Materials International,              [55] E.H. Lee, L.K. Mansur, J. Nucl. Mater. 61 (1990) 733.
     West Conshohocken, PA, 2003.                                                          [56] M.F. Wehner, W.G. Wolfer, Philos. Mag. A 52 (1985) 189.
[37] F.C. Moon, Y.H. Pao, J. Appl. Phys. 38 (1967) 595.                                    [57] W. Cai, V. Bulatov, S. Yip, J. Comput.-Aided Mater. Design 6 (1999) 175.
[38] W.G. Wolfer, M. Ashkin, Scripta Metall. 7 (1973) 1175.
