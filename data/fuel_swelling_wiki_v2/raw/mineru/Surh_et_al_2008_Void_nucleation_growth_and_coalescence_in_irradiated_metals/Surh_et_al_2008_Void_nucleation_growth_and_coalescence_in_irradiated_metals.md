# 📄 PDF Parsing Result

**File:** `/Volumes/openclaw记忆/Zotero_storage/storage/47XM5IHL/Surh et al. - 2008 - Void nucleation, growth, and coalescence in irradiated metals.pdf`
**Backend:** `pipeline`
**Pages:** 0 to end
**Formula Recognition:** ❌ Disabled
**Table Recognition:** ✅ Enabled

---

# Void nucleation, growth, and coalescence in irradiated metals

Michael P. Surh \*, Jess B. Sturgeon 1 , Wilhelm G. Wolfer

Lawrence Livermore National Laboratory, 7000 East Avenue, Livermore, CA 94551, USA

a r t i c l e i n f o

Article history: Received 22 January 2008 Accepted 12 May 2008

## a b s t r a c t

A novel computational treatment of dense, stiff, coupled reaction rate equations is introduced to study the nucleation, growth, and possible coalescence of cavities during neutron irradiation of metals. Radiation damage is modeled by the creation of Frenkel pair defects and helium impurity atoms. A multidimensional cluster size distribution function allows independent evolution of the vacancy and helium content of cavities, distinguishing voids and bubbles. A model with sessile cavities and no cluster–cluster coalescence can result in a bimodal final cavity size distribution with coexistence of small, high-pressure bubbles and large, low-pressure voids. A model that includes unhindered cavity diffusion and coalescence ultimately removes the small helium bubbles from the system, leaving only large voids. The terminal void density is also reduced and the incubation period and terminal swelling rate can be greatly altered by cavity coalescence. Temperature-dependent trapping of voids/bubbles by precipitates and alterations in void surface diffusion from adsorbed impurities and internal gas pressure may give rise to intermediate swelling behavior through their effects on cavity mobility and coalescence.

\- 2008 Elsevier B.V. All rights reserved.

## 1. Introduction

Irradiation of metals has long been known to culminate in macroscopic property changes including void swelling [1]. Characteristic stable voids and steady volumetric swelling develop for a range of temperatures and fluxes, independent of whether radiation bombardment damage occurs as disseminated Frenkel pairs or as small defect clusters. This can occur whether or not helium is generated along with atomic displacements. In either case, small, unstable voids, loops, and other defect clusters will develop almost immediately within the irradiated material. Their subsequent evolution determines the fluence required to create stable voids and achieve steady swelling; this so-called incubation dose includes most of the dependence on radiation environment [2–4]. The processes that govern microstructure evolution include thermallyactivated motion of small defect clusters, mutual impingement, and annihilation or coalescence reactions along with micro-chemical changes from nuclear transmutation and displacements or diffusion of pre-existing impurities. Radiation simulations should ideally encompass all of these processes. Typically, existing models have included only particular types of defects and reactions or have made other numerical approximations in order to obtain a solution.

At the least, simulations of early irradiation must account for void nucleation and growth processes, since annihilation, aggregation, and cluster ripening take place concurrently. Transient and steady-state swelling behavior due to these processes have been studied recently using a mean field monomer aggregation model [5–8]. However, only void reactions with vacancy or interstitial monomers are included in these studies. This minimal model of void nucleation gives reasonable swelling behavior as a function of temperature and flux [7,8], viz. an observed steady swelling rate around 1%/dpa in austenitic stainless steels and an important flux-effect on the measured incubation times [9,10]. While the results are encouraging, these calculations neglect many of the processes believed to shape the microstructure. For example, the generation and aggregation of helium impurities is not explicitly modeled. Void diffusion, impingement, and direct void–void coalescence are excluded, thus the size-dependent void diffusion [11,12] is effectively set to zero in this model. (Void impingement via the expansion of adjacent cavities [13] is not considered here, as the mean field approximation is most appropriate for a small volume fraction of voids.) Dislocation loop formation, migration, and coalescence is not explicitly simulated either. The model [5– 8] can be considered to combine the production and biased diffusion of small vacancy and interstitial clusters into effective generation and reaction rates for monomer species alone, but it is unclear a priori how a coarse-grained treatment of these processes affects microstructure evolution.

It is now clear that this earlier model must presuppose a ready supply of gas impurity atoms (e.g., oxygen and helium [14]) to promote the formation of small voids from the radiation-induced, supersaturated vacancy population. In practice, reasonable corrections to void energies may reproduce the approximate void number density observed in irradiated steel [8]. Ultimately, however, crude models for the apportionment of impurities among the defect clusters should be supplanted by a detailed accounting of multicomponent aggregation and coalescence reactions and their influence on the non-equilibrium cluster size distribution. Such problems are widely addressed in the literature, including gelation, polymerization, and formation of aerosols and precipitates in solid or fluid media [15–31]. The numerical methods developed for such problems may also be fruitfully applied to radiation swelling. Here, a hybrid numerical approach that can encompass the full range of possible cluster compositions and cluster reactions in mean field is introduced, a Livermore Microstructure Evolution program, LiME. As a first application, the method is applied to the nucleation and growth of voids with a two-component distribution of cluster compositions, examining the evolution of helium–vacancy clusters [14], while continuing to treat oxygen adsorption by simply reducing the cavity surface energy by a constant (temperature-independent) factor. The method predicts realistic swelling behavior for ferritic steel in reactor environments.

As before, the void distribution function is partitioned into overlapping regions [5], treating small clusters with the Master Equation (ME domain) and large ones with Monte Carlo methods (MC domain). This allows self-consistent evolution of the full void population with no truncation or coarse-graining of the size domain, no assumptions as to the critical void size or the nature of the nucleation process, and no approximations for the overall nucleation rate or duration of the nucleation stage. The formation and evolution of dislocation loops is not explicitly modeled; network dislocations and loops are already described by a single, time-dependent density parameter rather than a detailed size distribution function [32]. However, the methods used for void evolution would be easily generalizable to other defect species and reactions, provided that suitable mean field rate coefficients are specified for their reaction rate equations. In particular, future calculations will consider the formation, unfaulting, and migration of dislocation loops; loop coalescence and annihilation; and incorporation of loops in the dislocation network.

The remainder of this paper first describes the coupled, stiff, non-linear evolution equations for void nucleation, growth, and coalescence. It presents the microscopic rate theory model, gives an overview of the computational scheme, details the various numerical methods employed in the calculations, and makes a preliminary application to void nucleation in irradiated stainless steel. The simulations include vacancy, interstitial, and helium generation, aggregation and, annihilation, with or without cluster coalescence. The results are sensitive to the effects of absorbed impurity atoms on cavity surface energy. They also expose a substantial influence of small, unstable, mobile clusters on the formation of critical-sized voids via direct cluster–cluster coalescence. Realistic incubation and swelling behavior cannot be obtained over wide ranges of temperature and flux without including cluster mobility and coalescence.

## 2. Rate theory model

Allowable microstructure reactions (either defect aggregation or annihilation) are assumed to occur whenever two defects, m and n, come into contact. Within the mean field continuum approximation, the collision rate is proportional to their relative diffusivity, Dm;n, and effective collision cross-section, Am;n. As before [5,8], a bias factor Zm;n includes the effect of long-range interactions [33,34] on the binary reaction rates, Kðm; nÞqmqn, where q are densities of reactant species m 6¼ n and the rate coefficients are

$$
\tag{ð1Þ}
$$

Note that an additional factor of 1/2 may be required when m ¼ n, to prevent double-counting of unique pairs of identical reactant particles. This factor is not explicitly shown in the definition of K.

Microstructure defect species are limited here to self-interstitials and vacancies, substitutional and interstitial helium, voids/ bubbles, and network dislocations. Vacancy and helium monomers as well as clusters are characterized by their composition, n ¼ ðnvac; nhelÞ, in a two dimensional space. Vacancies and interstitials are also specially identified by ð1; 0Þ ¼ v and ð-1; 0Þ ¼ i, respectively; substitutional and interstitial helium by ð1; 1Þ ¼ vh and ð0; 1Þ ¼ h; and network dislocations by d. Monomer densities evolve according to

$$
\tag{ð2Þ}
$$

The vacancy–vacancy aggregation term, ðZv;vAv;vDv;vÞqvqv, within the first summation for dq =dt in Eq. (2) includes that two vacancies are consumed by the reaction, that there is a factor of 1/2 to prevent double-counting of unique pairs of vacancies from the population q , and that the relative diffusivity is twice Dv. The net rate is identical to that used in a previous study [5]. Similar considerations also apply to pairs of substitutional helium and to thermal dissociation of vacancy dimers.

Cluster (n 62 fv; vh; h; ig) densities evolve as

![](images/9f92646a2d957a82fc4a347075f29bd188c5a97aac6e77791622a069b9645d62.jpg)

in terms of any direct generation of clusters in the radiation damage cascade, g ; reactions of existing clusters with monomers (in brackets) that consume or create n-mers including thermal emission of vacancies, and cluster–cluster reactions (in the second set of brackets) that consume or create n-mers. Factors of 1/2 in the first and last summations prevent double-counting of indistinguishable reactant pairs, and dm;n ¼ dmv;nv dmh;nh where the right hand side consists of the usual Kronecker deltas, di;j ¼ 1 0 i 6¼ j . The primed summa- i ¼ j tion is restricted to all pairs of reactants with m; n - m 62 fv; vh; h; ig. Defects n - m (n - v, etc.) are restricted to the domain of allowed compositions by a step-function: UðnÞ ¼ UðnvÞUðnhÞ, where UðnÞ ¼ 0 n < 0 . 1 n P 0 Finally, clusters never undergo fragmentation in this model, only the thermal emission of single vacancies.

Radiation damage deposition is approximated by the creation of disseminated monomers (Frenkel pairs), so gn  0 for n 62 fv; vh; h; ig. In this case, g ¼ /n, in terms of the atomic displacement rate, /, and the damage production efficiency, n. The total helium production is gh þ gvh, with the ratio of interstitial to substitutional depending on the model. (Here, it is assumed that the helium is all deposited as substitutional defects.) Conservation of host atoms (including transmutation products) requires gv þ gvh  gi. Helium impurities are added with a temperature-independent, gradual activation of a-emitters. This is modeled for a Fe–Ni–Cr steel undergoing neutron bombardment according a two-step activation process, in analogy to the 58Ni(n,c) 59Ni(n,a) reaction. Model transmutation rates are treated as free parameters and are fit to the experimental helium content in HFIR-irradiated nickel [35,36]. The parameters are c, a, and d for the rates of (respectively) 58Ni(n,c), 59Ni(n,a), and the sum of all transmutations that consume 59Ni. In terms of the cumulative radiation dose in dpa, x ¼  /ðtÞdt (for radiation flux, /):

$$
\tag{ð4Þ}
$$

The 59Ni content, q59, is obtained from Eq. (4) by transforming to the eigenbasis, where qAðxÞ ¼ q58ðxÞ and qBðxÞ ¼ q59ðxÞ þ cc q58ðxÞ are solved, and then transforming back. The helium generation rate is given by

$$
\tag{ð5Þ}
$$

assuming that only 59Ni(n,a) produces a-particles. The fit parameters are c ¼ 0:0255, a ¼ 0:0711, and d ¼ 0:297 dpa-1 . Pristine type

Table 1 Model material parameters for type-316 stainless steel

316 stainless steel is approximately 14% nickel, with 68.08% of that 58Ni and with no naturally-occurring 59Ni. Other relevant materials parameters for type-316 stainless steel are listed in Table 1.

Non-interacting diffusion (independent random walks) implies Dm;n ¼ Dm þ Dn. Defect collision cross-sections are simply given by

$$
\tag{6Þ}
$$

in terms of radii for (spherical) defects, rn ¼ ð3nvXÞ 2 (except for interstitial monomers, where ri ¼ rh ¼ rv). For consistency with earlier work, cross-sections involving monomers are defined using the Burgers vector magnitude in place of a monomer radius.

Bias factors between voids and the four defect monomers are calculated from a mean field solution of the diffusion including stress-mediated interactions [34]. The infinite series describing the image interaction [37] is fit by a simple analytic form, while the modulus interaction [38] is treated analytically. The numerical results are tabulated for small voids and computed as needed for larger ones. Long range void–void interactions are presently neglected, so Zm;n ¼ 1 for m; n 62 fv; vh; h; ig. In principle, the effect of any long-range interactions or net drift velocities (e.g., from external stress or temperature gradients [39]) can be incorporated in the void–void reaction rates, so the mean field reaction kernel, K, has general applicability.

Thermal emission from vacancy clusters is evaluated by a detailed balance argument. Equating vacancy emission and absorption for the n-mer identifies the chemical potential, l½nv ¼ F½n - F½n-v , in terms of the n-mer and ðn - vÞ-mer (i.e., void minus one vacancy) free energies. Rewriting in terms of void internal energies, E, and the inert gas pressure, P:

$$
\tag{ð7Þ}
$$

<table><tr><td rowspan=1 colspan=1>Burgers vector b                                              a0/√2</td></tr><tr><td rowspan=1 colspan=1>Atomic volume Ω                                             /4Shear modulus μ                                              8.295 × 101° Pa</td></tr><tr><td rowspan=1 colspan=1>Poisson&#x27;sratio v                                               0.264</td></tr><tr><td rowspan=1 colspan=1>Damage production efficiency &amp;                                  0.1</td></tr><tr><td rowspan=1 colspan=1>Relaxation volume                                             -0.2 Ω</td></tr><tr><td rowspan=1 colspan=1>Migration energy Em                                           2.08 × 10-19 J</td></tr><tr><td rowspan=1 colspan=1>Formation energy Ef                                           2.88 × 10-19J</td></tr><tr><td rowspan=1 colspan=1>Formation entropy Sf                                           1.5 kg</td></tr><tr><td rowspan=1 colspan=1>Pre-exponential factor                                          1.29 × 10-6 m²/s</td></tr><tr><td rowspan=1 colspan=1>Shear polarizability                                            -2.4 × 10-18</td></tr><tr><td rowspan=1 colspan=1>Relaxation volume                                             1.50 Ω</td></tr><tr><td rowspan=1 colspan=1>Migration energy Em                                           0.320 × 10-19 J</td></tr><tr><td rowspan=1 colspan=1>Pre-exponential factor                                         1.29 × 10- m²/s</td></tr><tr><td rowspan=1 colspan=1>Shear polarizability                                            -2.535 × 10-17</td></tr><tr><td rowspan=1 colspan=1>Relaxation volume                                             0.60Ω</td></tr><tr><td rowspan=1 colspan=1>Migration energy Em                                           0.320 × 10-19 J</td></tr><tr><td rowspan=1 colspan=1>Pre-exponential factor                                          1.29 × 10-6 m²/s</td></tr><tr><td rowspan=1 colspan=1>Shear polarizability                                            -2.535 × 10-17</td></tr><tr><td rowspan=1 colspan=1>Relaxation volume                                             -0.2Ω</td></tr><tr><td rowspan=1 colspan=1>Migration energy Em                                           2.08 × 10-19 J</td></tr><tr><td rowspan=1 colspan=1>Pre-exponential factor                                          1.29 × 10-6 m²/s</td></tr><tr><td rowspan=1 colspan=1> Shear polarizability                                            -2.4 × 10-18</td></tr><tr><td rowspan=1 colspan=1>Relaxation volume                                             0</td></tr><tr><td rowspan=1 colspan=1>Surface energy γo(T = 0)                                        2.408 J/m²</td></tr><tr><td rowspan=1 colspan=1>Temperature derivative dyo/dT                                  0.440× 10-³ J/m²/K</td></tr><tr><td rowspan=1 colspan=1>Adsorption factor A                                            0.45-0.80</td></tr><tr><td rowspan=1 colspan=1>Migration energy Em                                           2.08 × 10-19 J</td></tr><tr><td rowspan=1 colspan=1>Pre-exponential factor                                         1.29 × 10- m²/s/n/3</td></tr><tr><td rowspan=1 colspan=1>Temperature T                                                300-700 C</td></tr></table>

Gas pressure is described with a non-ideal equation of state for helium versus density and temperature [40]. No volume relaxation is included (i.e., the void volume is n X). In the absence of surface-adsorbed impurity atoms, E½n is parametrized in terms of an effective surface energy, c½n , and the surface area of a spherical cavity of volume nvX

$$
\tag{ð8Þ}
$$

In the continuum limit, c½n approaches that of a flat, clean surface, c ðTÞ, while it approaches the results of atomic calculations in the limit of small voids [41]. This surface energy is then further reduced by an constant scale factor, K, to reflect the presence of adsorbed oxygen impurities [42] (see Table 1). Finally, the emission rate is obtained from c ½nv and the vacancy-cluster reaction parameters for the ðn - vÞ-mer. For straight, jogged dislocation segments, c ½dv ¼ c ½eqv , the thermal equilibrium concentration. Emission rate coefficients in Eq. (2) are represented as unary reactions, by including the defect-dependent c½n within the rate coefficient.

At some maximum density, an over-pressurized bubble would begin to emit self-interstitials via loop punching [40]. Such a possibility is not considered here; instead, an artificial constraint is imposed on the helium density in a reactant cluster, nh 6 2nv. Any reactions that would yield a higher-density are disallowed. Thermal dissociation of substitutional helium into a vacancy plus interstitial helium is similarly assumed to be energetically impossible at temperatures of interest. Note that self-interstitial and interstitial helium aggregation is excluded since interstitial loops are effectively part of the dislocation density model. Mixed interstitial clusters can develop in principle [43].

Void diffusivity Dn ¼ Dv=n4=3v for n ¼ ðnv; nhÞ. This gives both the correct monomer value and size-dependence for large cluster diffusion [11,12], although the activation energy for void migration should more properly be that for surface diffusion. This diffusivity takes no account of the effect of reversible pinning [44], or internal gas pressure on the migration [45], or radiation-enhanced diffusion [46], or, e.g., that vacancy dimer diffusion may be Dv ’ Dv. Trapping at dislocations and grain boundaries are not considered. Such features would be straightforward to incorporate in the future.

The dislocation model reproduces measured dislocation densities versus dose and temperature [32]. It includes separate source and annealing terms in terms of the biased flow of radiation-induced vacancies and interstitials. There is one adjustable parameter, l, representing a characteristic dislocation pinning length [32]. This is taken to be independent of the density of voids/bubbles in the matrix, because the pinning length in stainless steels is more determined by carbide precipitates than by the density of voids/ bubbles.

## 3. Numerical method

## 3.1. Overview

Once initial conditions for the microstructure and the temperature- and radiation-environment are fixed, the Master Eqs. (2) and 3) and the dislocation model [32] completely determine the void/ bubble size distribution function PðtÞ ¼ fqnðtÞg. These stiff, nonlinear coupled rate equations can be integrated numerically for a small number of species [18]. However, direct integration becomes impractical for a large domain of cluster sizes. Coarse-grained approximations group similar clusters together to reduce the number of distinct species [47], but even they are intractable for multidimensional distributions. Monte Carlo schemes for discrete coalescence events [16,21] can naturally encompass large voids of arbitrary composition; however, they are inefficient for simulating nucleation from sub-critical clusters. Here, the advantages of both rate equations and Monte Carlo methods are combined by partitioning the cluster composition domain into two overlapping regions. Separate sub-distributions are defined for each, labeled ME and MC for treatment by Master Equation and Monte Carlo, with P ¼ PME þ PMC. Such split distribution functions have been used before in a Fokker–Planck treatment of void growth [5]. Similar approaches are found in non-equilibrium chemistry [24,30] and plasma physics applications [48].

Each sub-distribution of P is composed of a set of discrete ensembles of identical clusters, represented by ðn; qÞ for the multi-dimensional cluster composition, n, and the paired ensemble density, q. The distribution PME ¼ fðn; qÞgME includes interstitials, i, and vacancy–helium clusters, n, with 0 6 nv 6 NMEv and 0 6 nh 6 NMEh . There is exactly one element for each ME species, for a total of NME. Only the densities of the ME elements evolve over time; the set of allowed compositions is fixed. A sparse, random set, fðn; qÞgMC, approximates PMC for all 0 6 nv; nh < 1. The total number of elements, NMC, is variable, and there may be none, one, or many MC elements (each with potentially different values of q) at a given composition coordinate n. Both the densities and the compositions of the MC elements evolve with time as defect– defect reactions occur. In essence, the elements of PMC also constitute so-called ‘macroparticles’, already in wide use for non-equilibrium plasma physics problems [49].

The various elements of the two sub-distributions are evolved using the most efficient method available. ME–ME reactions (i.e., those processes with reactants and product among the elements of PME) are evaluated in a continuum approximation, using the Master Equation [18]. Monomers can be treated separately by a quasi-stationary approximation or evolved along with the rest of the ME distribution through the coupled non-linear reaction rate equations. Discrete MC–MC reactions are performed stochastically using a Markov Monte Carlo procedure [16]. ME–MC cross-reactions are included using either the Markov Monte Carlo method or Poisson-distributed random walks [21,22] for PMC, and using average sink or source terms in the rate equations for PME. There are also procedures to transfer clusters between the two sub-distributions and to regulate the number of elements and their ensemble densities in PMC, in order to control statistical errors and computational cost. This combined algorithm is elaborate, so the different approaches for each of the various components are described in detail in the following sections.

The whole of the material microstructure is evolved over a time-step, s, by operator splitting into five stages. First, ME–MC reactions for rapidly evolving MC clusters (i.e., those with small nv) are included with a Markov chain method (Section 3.5). Second, the ME–MC reactions for the large, slowly-evolving clusters are evaluated by Poisson-distributed random walks in composition space; this encompasses each possible reaction with ME species (Section 3.5). Third, all MC–MC reactions are evaluated with the Markov Monte Carlo method. (Section 3.4) This completes the evolution of PMC over s. The fourth stage integrates the ME including the average source and sink terms from MC defects and dislocations (Section 3.2). This completes the evolution for the void/bubble P. At this point, clusters may be exchanged between PME and PMC, without affecting the instantaneous total P in any way (Section 3.3). This process may create new MC elements or eliminate existing ones, in order to control the growth of NMC versus time. Fifth and finally, dislocation evolution is performed using a previously-described model [32].

Overall numerical accuracy is monitored through the conservation of host and helium atoms. This must be carefully maintained in any void nucleation calculation. Obviously, a systematic imbalance could distort the swelling results, but even small, fluctuating numerical errors might potentially affect the predicted nucleation behavior. The incubation period represents a sort of barrier-crossing problem, involving nucleation of stable voids and concomitant, self-consistent changes in the vacancy/interstitial populations. In practice, a simulation must not spuriously affect the crossing into the steady-state; i.e., the associated numerical errors must not significantly promote or inhibit void nucleation.

By construction, the procedures in Sections 3.3 and 3.4 will always conserve the number of host and helium atoms and exactly treat the number of clusters. Operator splitting of the evolution equations between Sections 3.2 and 3.5 does cause first-order time-step errors, but these are conventionally controlled by adjusting the overall time-step, s. Numerical integration errors within Section 3.2 are similarly managed through the VODE tolerance parameters and the resulting internal time-steps [18]. Conservation errors are dominated by differences between the ME and MC treatment of reactions (see Section 3.5). In essence, the flux of ME particles to the MC clusters occurs continuously, while the MC clusters grow in discrete, stochastic jumps. The average rate of growth of an individual MC macroparticle necessarily equals the net influx of ME particles, but there are residual, random deviations from this trend. This corresponds to random discrepancies in the usual continuity equation, r\~ \~J ¼ dN=dt (i.e., conservation errors). Integrated over time, this Monte Carlo noise accumulates as a random walk with zero average expectation. In general, the magnitude of the RMS error can be controlled by adjusting NMC; it approaches zero as NMC ! 1. The relative error asymptotically approaches zero once steady swelling is achieved – i.e., the net vacancy and helium content increases linearly with time while the error grows only as ffiffit . Thus, the relative error tends to vanish over long times for the radiation swelling problem.

These artifact statistical fluctuations are relatively most important at low temperatures and especially during incubation, when NMC is small, defect annihilation dominates, and little net swelling occurs. For the situations considered here, stable cavities form naturally under the vacancy supersaturation and the essentially irreversible aggregation of helium. Thus, the added noise is relatively inconsequential. For example, the total vacancy content (net swelling) is shown in Fig. 1 along with the instantaneous error for a calculation without cluster coalescence at 10-6 dpa/s and 500 C, using void surface energies of 0.4 times c0ðTÞ. The vacancy/interstitial error is calculated as the difference between the net integrated flux of interstitials to the dislocations and the net vacancy content in all point defects and defect clusters. The former quantity is obtained from numerical integration of the rate theory equations, while the latter includes rate theory and Monte Carlo contributions. This particular simulation includes up to NMC ’ 1500. Increasing NMC to 14 000 changes the overall vacancy content by just 10 appm at a dose of 1 dpa, while the density of visible voids (not shown in the figure) changes by 2%. Thus, the swelling behavior is not sensitive to the NMC-dependent error, i.e., the Monte Carlo noise does not unduly promote or suppress nucleation.

![](images/0bf4a67fc50b2f9ebaa78502a6cb476c5cacaecb96fbf456fb28895131ff4d85.jpg)  
Fig. 1. The total vacancy content (a measure of the swelling) and the net vacancy/ interstitial conservation error are shown for c ¼ 0:4c ðTÞ, at T = 500 C, 10-6 dpa/s. The macroparticles reach NMC ’ 1500 at 1 dpa, at which point new ones are still forming.

## 3.2. ME–ME reactions

Small defect clusters develop at high concentrations under irradiation, and so they dominate the system of reactions. However, they quickly reach a quasi-stationary distribution wherein further reactions cause little change in their densities; i.e., the majority of their reactions subsequently cancel one another. Thus, it is much more efficient to treat their net behavior in a continuum approximation than to explicitly account for individual defect reaction events. The ordinary differential equation solver, VODE, provides an optimized treatment of stiff, non-linear reaction equations [18], given fn ¼ dqndt (Eqs. (2) and (3)) and the Jacobian, Jnm ¼ ofnoq dt m for all species. The computational cost increases rapidly with the number of coupled equations, hence the cluster domain is limited to 0 6 nvac 6 NMEvac and 0 6 nhel 6 NMEhel . Typically, NMEvac ¼ 10—100 and NMEhel ¼ 2—10. Some terms are excluded from the Master Equation so that all reaction products remain within this finite domain. Clusters with 0 6 nvac 6 NMEvac=2 and 0 6 nhel 6 NMEhel =2 may undergo any mutual reactions, but no other ME clusters may undergo any reactions. These latter clusters are frozen in size, so their density only increases as reaction products accumulate. Frozen clusters eventually transfer to the MC distribution as described in Section 3.3, after which they will undergo reactions according to the MC procedure.

With reaction constraints and separate ME and MC distributions, the vacancy Eq. (2) becomes

$$
\tag{ð9Þ}
$$

restricting the sums over n 2 ME to reactive defects. Eq. (1) also parametrizes unary vacancy emission reactions as the n-null reaction, Kðn; 0Þ ¼ Zn-v;vAn-v;vDn-v;vc ½n-vv . S includes the external source and sink terms for reactive elements of PME; it accounts for ME reactions with defects in PMC and with dislocations. Vacancy absorption at MC defects and dislocations is parametrized by Sv, and vacancy emission by S0. The vacancy sinks and sources include separate terms that either evolve slowly or rapidly with time. The coefficients are obtained in Section 3.5. The rest of Eq. (2) takes similar form, with sinks Si, Svh, or Sh. (Only vacancies can be thermally emitted from defect clusters, so S0 is the only source term.)

Operator splitting over the time-step, s, is such that external source and sink terms S are held constant as PME evolves. S is divided into terms that evolve slowly or rapidly with time. The bar indicates an average of the sink strength over the time-step, from t0 to t0 þ s, useful for rapidly evolving MC clusters, while slowlyevolving dislocations and large MC voids are simply evaluated at the beginning t0 (see also Section 3.5 for further details).

The constrained coalescence Eq. (3) becomes

$$
\tag{ð10Þ}
$$

for clusters m; n 2 ME, and n 62 fv; vh; h; ig. The primed summation excludes n - m 2 fv; vh; h; ig, since the monomer reactions are evaluated separately. S includes any reactions of the n-mer with the MC clusters and with dislocations. There are no reactions that consume frozen clusters, so their concentration increases with time.

A subset of the disallowed reactions would produce clusters that still lie within the ME domain. These have been excluded, for simplicity and to better resemble an earlier scheme for monomer aggregation [5]. Specifically, a homogeneous boundary condition is imposed on the Fokker–Planck equation in Ref. [5], at n ¼ NME . vac Clusters that grow to the boundary are removed from the Master Equation treatment and accumulated separately, during which time they are prevented from changing size. This is equivalent to keeping those NMEvac-sized clusters within PME but disabling all of their reactions. Frozen clusters are then intermittently transferred to PMC, where they are no longer constrained [5].

Ideally, the ME domain will encompass all non-zero generation terms, g , and include as many sub-critical or transient defect cluster species as possible. A relatively small domain of NME ’ 60, v NMEh ’ 4 is chosen here, reflecting the computational demands that coalescence imposes.

Similarly to [5], the solution is recorded at exponentiallyincreasing intervals, up to some smax. This time-step is irrelevant to the ME evolution itself, which advances by adaptive sub-steps. However, s controls errors from operator splitting of the evolution equations, and it governs the creation of MC elements, as described below.

Because the sink/source terms, S, are evaluated by a discrete MC method, they introduce a fictitious noise to the continuum rate equations. This partly manifests as step-function discontinuities in the sink strength over successive time-steps, which in turn causes transient relaxation in the concentrations of the ME species. The numerical solution tries to accurately follow the transients, potentially making the fully coupled, non-linear evolution inefficient, when large time-steps are otherwise possible. Rather than faithfully simulating these spurious transients at late times, it may be preferable to solve the monomer concentrations (Eqs. (2), (9), etc.) in the quasi-stationary approximation after any real transient behavior (due to the abrupt onset of irradiation or other changes in environmental parameters) has concluded. Eq. (10) for dimers and larger clusters may then be solved while holding the monomer concentrations fixed over the time-step. In practice, after a brief transient, the results are comparable to those obtained from the full, coupled, non-linear ME solution.

## 3.3. Transfer between ME and MC domains

A majority of the ME elements in a small multi-dimensional domain will lie near its boundary, and so the majority of the ME cluster species will be artificially frozen. The constraints on the defect clusters are only lifted after they are transferred to PMC. There are three desiderata to this transfer process. Foremost, it must minimize any systematic, constraint-induced errors, therefore the density of frozen clusters must be small compared to the rest of P.

Secondly, the MC computational cost must be controlled, therefore NMC must be kept small. Rather than increasing NMC at every opportunity, frozen clusters at n 2 ME are allowed to accumulate until exceeding a spawning threshold density, qMEn > qsp, as in [5]. At the end of that time-step, a portion of the accumulated density is removed from PME and transferred to a new element of PMC, incrementing NMC

$$
\tag{ð11Þ}
$$

with the ME and MC compositions coinciding. If the accumulated qMEn > qsp after each time-step, then the accumulating clusters are effectively never constrained. Finally, it is imperative to minimize any NMC-dependent Monte Carlo statistical error. Individual MC elements with the largest q will contribute the most to this error. Therefore, if qMEn  qsp at the end of a time-step, then DN > 1 new MC elements are created, as

$$
\tag{ð12Þ}
$$

Equivalently, MC elements with large q may be split into identical macroparticles with smaller densities. The chosen values for s, qsp, and the functional dependence of DN on dq control the NMC-related statistical error and computational cost for a simulation. Typically, log2ðDNÞ ¼ Intðlog30ðdq=qspÞÞ.

For example, the distribution in Fig. 2 shows the production of many MC macroparticles containing 2–4 helium atoms; these react and form a plume that extends to nv ’ 100 (beyond the view of the figure). The ME domain used in this example also includes frozen cluster species with 5–9 helium; these species have not yet reached the threshold density. They eventually spawn MC elements, but at a much slower rate than for the near-critical sizes of 2–4 helium. Even at this early time, the total density of constrained ME clusters is small compared to the MC population so constraint errors are minimized.

Since q cannot be made arbitrarily small in practice, it is useful to add a second transfer mechanism. When a pre-existing MC element at n falls inside the frozen ME domain, the change:

$$
\tag{ð13Þ}
$$

leaves the total distribution unchanged. NMC remains constant, so the calculation remains tractable. In practice, the maximum amount dq 6 q is transferred until the receiving MC element reaches a cutoff density, qMCn þ dq 6 qmax (where typically, qmax ’ 2qsp to 10qsp.) The cutoff prevents over-weighting of individual Monte Carlo elements so as to control the statistical error.

At low temperatures, a very high density of small bubbles can coexist with a moderate density of large, low-pressure voids. Such distributions are most efficiently treated by making qmax sizedependent, so that the maximum macroparticle densities are high in the region of bubbles, but low in the region of voids. Macroparticles can freely wander between the two regions. Accordingly, if macroparticle A moves to a region where qA > qmax, it may be split into two identical parts; or if two MC elements at the same coordinate have qA þ qB < qmax, they may be united into one.

![](images/804f826e8ef1a200209e3d7129be2aaefab977644161bd6b6c809785989eadd6.jpg)  
Fig. 2. A portion of the void/bubble distribution for a model with mobile monomer defects and sessile clusters, c ¼ 0:8c0ðTÞ, at T = 300 C, 10-6 dpa/s, and 32  10-3 dpa. For reference, the largest void in the distribution contains 110 vacancies (not shown). The solid lines display the loci of stable and unstable equilibrium cluster compositions, based on average vacancy accumulation rates. This distribution has not been smoothed – the pixellated appearance reflects discrete cluster compositions.

In problems of reversible nucleation and growth, small MC clusters may shrink and disappear. It is computationally inefficient to follow unstable clusters by Monte Carlo methods. Accordingly, macroparticles of the smallest vacancy clusters (with both nvac < Nvac min < NME and nhel ¼ 0) are deleted at the end of each time-step and their density returned to the corresponding element of PME. (The numerical solution of the ME automatically accommodates any subsequent transients by adjusting its internal time-steps.) The minimum MC size should be large enough that macroparticles at the threshold only rarely shrink to monomer sizes during the interval s. It should also be far enough from NMEvac=2 that the cycle ME!MC!ME (involving creation of a new macroparticle, shrinkage of the constituent clusters, and transfer of that element back to PME) is infrequent. In practice, Nmin ¼ NME=4 is used, and these two criteria are accomodated by taking the largest possible NME. Helium clusters are never returned from MC to ME distribution; helium emission is not permitted, so the clusters will only grow along the helium axis.

In the examples considered here, all ME clusters are sub-critical for NMEvac ’ 60, so that newly-created MC particles frequently shrink and are annihilated. This is especially true at low temperatures, when the proliferation of small voids favors vacancy/interstitial recombination. Here, this ‘rare event problem’ for nucleation of stable voids from small vacancy clusters is at least improved from conventional kinetic Monte Carlo methods, where even the monomers would be treated stochastically.

Ultimately, direct application shows this mixed scheme is suitable for radiation damage calculations to high doses.

## 3.4. MC–MC reactions

Coalescence problems are frequently treated by a Markov Monte Carlo method [16]. A straightforward approach defines a finite volume, V, containing N (i.e., NMC) discrete clusters of sizes fng that stochastically evolve to a new N - 1 population fn0 g through the binary coalescence of any pair of particles. The average rate of reaction between the ith and jth particles is simply Kðni; njÞ=V2 per unit volume. The total rate of reaction of all N clusters is RN, where

$$
\tag{ð14Þ}
$$

and

$$
\tag{ð15Þ}
$$

in terms of the sum over reactions in the entire volume, V, assuming they are uncorrelated and occur in parallel. Ri N is proportional to the rate at which cluster i reacts with all other clusters. A stochastic sequence of discrete reactions may be constructed from these parameters. The random interval, dt, to the next reaction is obtained from a uniform variate, x 2 ð0; 1, as [50]:

$$
\tag{ð16Þ}
$$

The first cluster of the random reaction pair, i, is selected with a probability proportional to Ri;N, from y 2 ð0; 1 and

$$
\tag{ð17Þ}
$$

where R0  0. Finally, the reaction counterpart, j, is identified from z 2 ð0; 1 and

$$
\tag{ð18Þ}
$$

with Ri;0  0. This selects j with a probability proportional to 1 Kðni; njÞ=V. The procedure repeatedly selects new x, y, and z for the next event, increments the system time by (new, random, different) amount dt, performs the reaction i þ j, and recalculates R for the next iteration. This repeats until the elapsed time, P dt, exceeds the maximum time s. Since the last reaction falls outside the desired interval, it is discarded without being performed. The procedure may then be started anew for subsequent, regular time-steps, s. In effect, the overall algorithm employs stochastic sub-steps to evaluate MC–MC reactions during the fixed interval, s.The choice of two random numbers to select the pair, i; j, differs from the usual scheme, where the pair is selected from a single value. In either case, the search for i and j takes oðlog ðNÞÞ operations using the method of bisection [51]. However, separate selection of i and j makes it possible to record all Rm with oðNÞ storage space and a one-time computational effort of oðN2 Þ. Once i is determined, Ri;m may be tabulated with oðNÞ effort for all m, so the full matrix need not be stored. Finally, after i and j react, the Rm may be updated with oðNÞ effort by replacing only those terms involving the old clusters i and j with the results for a single new, coalesced cluster, and reindexing to account for the lost cluster. Since RN is an extensive quantity for a given total density, evolution of N particles over a finite interval requires oðN2 Þ effort and oðNÞ storage. Specifying the binary reaction rate coefficients, K, as a half-triangular matrix increases the efficiency marginally.This MC scheme has difficulty modeling widely varying concentrations of reactants (e.g., the monomer density is typically orders of magnitude higher than the large clusters for radiation damage). Also, N decreases after every coalescence, which increases the statistical noise. There are methods that preserve N [19,27]. However, other approaches make it possible to preserve N and encompass a wider range of densities at the same time. In the approach taken here, the discrete MC elements are macroparticles, widely used in, e.g., non-equilibrium simulations of plasma physics [49]. (This is distinct from related, ‘weighted particle’ schemes for coagulation [20,23,52].) Here, the jth macroparticle in the system consists of an ensemble of clusters all of the same composition ðnj; q Þ. Consistent with the Gillespie procedure, macroparticle reactions are evaluated discretely, so clusters in an ensemble react simultaneously but otherwise stochastically. However, here reactants will generally have different ensemble densities, qL < qH, which are independent of their sizes/ compositions, nL; nH. The lower-density macroparticle, L, reacts completely, leaving behind an unchanged portion qH - qL of clusters from the higher-density ensemble, H. The total cluster density declines, but N stays constant, and N-dependent errors remain steady over time.

Macroparticle reaction rates (analogous to Eq. (15)) are defined so as to reproduce the continuum limit as N ! 1. Pairs i and j, with q < q , react according to

$$
\tag{ð19Þ}
$$

at an average rate of Kðni; njÞqj.

Two macroparticles of the same density (qi ¼ qj ¼ q; i 6¼ j) react as

$$
\tag{ð20Þ}
$$

at an average rate of Kðni; njÞq. The product is simply split into two equal pieces so that N remains constant. Finally, the individual clusters within a single macroparticle ensemble may coalesce with one another, so there is also a unary reaction process

$$
\tag{ð21Þ}
$$

which also proceeds at an average rate of Kðni; niÞqi. This possibility modifies Eq. (15) to include a non-zero reaction rate for i ¼ j.

Macroparticle dynamics never corresponds to an atomistic simulation for finite N. Instead, this is a distinct, approximative discretization of the continuum equations themselves, in the same spirit as earlier approaches [5]. Again, PðtÞ is approximated here by a sparse set of elements without arbitrarily imposing some coarse-graining of finite difference equations for the distribution. Since the computational cost scales as oðN2 Þ for a dense reaction matrix, the method is also efficient. This is especially advantageous in higher dimensions, e.g., in describing helium–vacancy–impurity clusters.

## 3.5. ME–MC reactions

Additional schemes are required for treating reactions between ME and MC elements. In the continuum approximation, reaction with external entities, n 62 ME, introduces unary sink terms to the rate equation for m 2 ME, cf. Eqs. (9) and (10)

$$
\tag{ð22Þ}
$$

where the summation includes all elements fðnðtÞ; qnðtÞgMC at time t and where Kðm; dÞ includes reactions with network dislocations. The sink term, S, is identically zero for constrained ME defects. At present, Kðm; dÞ is only non-zero for m ¼ ð1; 0Þ; ð-1; 0Þ and for vacancy emission Kð0; dÞ.

The counterpart to Eq. (22) is expressed for n 2 MC in the macroparticle scheme by

$$
\tag{ð23Þ}
$$

as a discrete reaction with an average rate of Kðm; nÞqm. A stochastic sequence of reactions at these average rates will approach the continuum behavior of Eq. (22) in the limit NMC ! 1. A single reaction can change a macroparticle size, cross-section, and reaction rate substantially, if m is comparable in size to n. Accordingly, ME–MC reactions for such ‘small’ MC clusters n < n0 are included by the Markov Monte Carlo scheme described above, and the reaction parameters are immediately updated to reflect the change, before evaluating the next reaction.

Reaction events are randomly performed from the NMC  NME matrix of reaction rates, at overall rate Q. If the next event occurs within the desired interval, the ith MC element is selected as a reactant with probability Qi=Q, where

$$
\tag{ð24Þ}
$$

for reactive elements mj 2 ME and

$$
\tag{ð25Þ}
$$

The jth ME element is selected as a reactant with probability Kðni; mjÞqm =Q i. Finally, the time index is updated, the reaction is performed, and Q is revised. This is analogous to the Markov procedure for MCMC reactions, except that the reaction matrix is fullrectangular rather than half-triangular and that the rates are always proportional to the density of the ME reactant.

As for the corresponding evolution of PME, the instantaneous source/sink terms, Eq. (22), change after each discrete reaction event in PMC. This may happen multiple times during the interval s. It is not computationally practical to account for this variation in detail (e.g., by evolving PME over each individual Markov substep, dt). Instead, PME is updated by operator splitting; it is evolved over the full time-step s only after all ME–MC and MC–MC reactions in PMC are performed. To minimize any convergence error for finite s, the instantaneous sink strength n < n0 can be replaced with a weighted time average over the interval

$$
\tag{ð26Þ}
$$

$$
\tag{ð27Þ}
$$

finally expressed as a sum over random sub-intervals, dtj, between discrete reaction times, tj-1 and tj as determined by Eq. (16).

Such attention to detail is unnecessary for large MC clusters (and for network dislocations), where rapid reactions with highly mobile defects (i.e., small m) do not substantially change the sink strength over short intervals. Thus, it is sufficient to update parameters for the large n clusters at the end of each time-step. In this case, MC clusters are evolved using a Poisson-distributed random variate, PðxÞ, [21,53] for the number of reactions that occurs during s. These MC elements are only updated at t0 þ s, with all reactions accumulated in each of the N channels

$$
\tag{ð28Þ}
$$

Eq. (28) is the discrete analogue of the Gaussian-distributed random walk used previously [5].

The corresponding ME sink term n P n0 is

$$
\tag{ð29Þ}
$$

including the dislocation contribution, assuming that qdðtÞ is slowly changing.

Finally, discrete reactions could also be evaluated by a rejection method, given a Majorant kernel Mðm; nÞ P Kðm; nÞ [52]. For example, the reaction rates, M, can be evaluated on a coarse grid of ni where all reactants ni 6 n 6 ni þ 1 are initially treated alike. In a variant of this approach, M may be chosen to be a sum of products [23],

$$
\tag{ð30Þ}
$$

It is then only required to evaluate NMC vectors, M, (of one or more dimensions) and to take dot products. Either approach is easier than directly computing NMCðNMC þ 1Þ=2 binary rate coefficients for Eqs. (14), (15). The Majorant kernel is selected to be easy to evaluate and to predict a faster (or equal) event rate than the true system. To correct for any overestimate, the time index is updated according to the usual Markov Monte Carlo procedure, but the reaction is only performed if a uniform variate, w 2 ð0; 1 also satisfies w 6 Kðm; nÞ=Mðm; nÞ. Thus, excess events predicted by M are rejected (with the required probability 1 - K=M). At present, the full reaction rate coefficients from Eq. (1) can be evaluated very efficiently, so this method is not employed here. However, this is expected to be advantageous when biased cavity–cavity, cavity–loop, and loop– loop reactions are included in the future.

## 4. Results

## 4.1. Monomer aggregation model

A high density of trapping/recombination centers is believed to delay the onset of void swelling [44,54,55]. Traps hinder void diffusion and coalescence and prolong the incubation stage. The simplest trapping model assumes that all dimers and larger clusters are immobile: Dn  0 for all n 62 fv; vh; h; ig, so that the last two summations in Eq. (3) are zero. If Eq. (2) is solved separately from the remainder of the Master Equation (Eq. (3)) in a quasi-stationary approximation, then that problem may be solved by existing methods [5,56]. However, here the problem is simply treated as a limit case of Smoluchowski’s coagulation equation.

Initial cluster populations are shown in Figs. 2–4 for type-316 stainless steel irradiated to low doses at 10-6 dpa/s and 300, 500, and 700 C. It is well-known that helium–vacancy clusters may be separated into distinct species (of equilibrium bubbles and stable or unstable voids), according to their size-dependent free energies. Accordingly, the figures are marked with black lines where the net average vacancy addition rate for the defect clusters approaches zero. The leftmost black line in Figs. 2–4 represents a hard wall for over-pressurized bubbles: by fiat, bubbles cannot reach densities greater than two helium per vacant site. Here, this is imposed by disallowing further reactions with helium- and self-interstitials.

Other lines separate clusters that add or lose vacancies on average. Small, over-pressurized bubbles tend to add vacancies until reaching the next line in the figures, where stable helium bubbles are in dynamic equilibrium with the vacancy and interstitial population. (This approximates the line of bubbles with P ’ c=2r, which would be in equilibrium in the absence of a vacancy and interstitial supersaturation.) The stability of these bubbles is reflected by their elevated concentration in that region, especially visible in Fig. 4. Stable bubbles tend to grow along the equilibrium line as they accumulate helium, while adjusting their vacancy content on average to remain in equilibrium. Finally, bubbles cannot exceed some critical helium content – larger clusters are stable voids that tend to add vacancies and grow to arbitrary size. This is seen in Fig. 3; there the clusters grow along the line of stable bubbles until reaching a critical helium content (11 heliums), at which point they grow by adding vacancies in excess of helium, forming a plume of rapidly-growing voids in the size distribution.

![](images/b5fccc4616100799398e503c8425ee5f801a92e654013ab3ad641c3dc7ff8b15.jpg)  
Fig. 3. A portion of the void/bubble distribution as in Fig. 2, but at T = 500 C, 10-6 dpa/s, and 16  10-3 dpa. The distribution has been smoothed for the large clusters, where Monte Carlo data is increasingly sparse. The solid lines display the stable and unstable equilibrium cluster compositions.

![](images/463fa73ac4bcd92d7197672d19e63ca9673e88b1d0e97582b124f55ff747a6a8.jpg)  
Fig. 4. The full void/bubble distribution as in Fig. 3, but at T = 700 C. The curved solid line locates the stable equilibrium bubbles; the critical void size is not visible on this scale.

Voids are here simply taken to be cavities with higher vacancy/ helium ratio than any bubble species of the same helium content. An approximately parabolic region under the black curves bounds a set of small, unstable voids that tend to lose vacancies and shrink back towards the equilibrium bubble configuration. For example, this ranges from the origin to vacancy/helium compositions of (19, 11) and (94, 0) in Fig. 3. The rightmost solid line identifies the critical or unstable equilibrium void compositions; larger voids tend to add net vacancies with time. Note that a percentage of equilibrium bubbles in Fig. 3 are able to fluctuate in vacancy content across the barrier of unstable voids. That is, they become stable voids without having first reached the critical helium content. Similarly, helium dimers are readily able to cross the barrier of unstable voids in Fig. 2. Very large voids ultimately become neutral (unbiased) sinks, adding helium/vacancies at an average rate of 1:200 (based on anticipated asymptotic swelling of 1%/dpa and model helium generation around 50 appm/dpa). Thus, voids approach a line of constant composition.

Except for a brief transient at the onset of irradiation, the vacancy monomer concentration decreases monotonically with time as the total sink strength of the microstructure rises with dose. After a few dpa, production of a-particles also peaks, and the helium monomer concentration also declines. During this extended period, equilibrium bubbles continue to grow by adding helium, they continue to reach the critical size, and they continue to become voids. However, the critical size for equilibrium bubbles increases with time (as a function of declining q ), and the rate of formation of new helium dimer nuclei and bubble growth rates decrease (as a function of declining qh þ qhv). This causes the rate of void formation to decrease gradually with time, giving a broad void size distribution. Eventually, the larger stable bubbles become TEM-visible, and the overall size distribution becomes bimodal.

The time-dependent volumetric swelling for this model is shown at a series of temperatures in Fig. 5. The low temperature system is initially dominated by large numbers of transient, unstable vacancy clusters (Fig. 2) that serve as recombination centers and suppress swelling. So many defect centers form that helium/ vacancy ratios are kept low, and helium plays a reduced role in the initial evolution. As a result, the visible cavity density (r > 0:5 nm) is sensitive to the surface energy parameter, c: q ¼ 5  1023 m-3 for cðTÞ ¼ 0:8c ðTÞ and 1  1024 m-3 for cðTÞ ¼ 0:5c ðTÞ. Eventually, some vacancy clusters acquire significant amounts of helium, and the system is filled with a high concentration of small equilibrium bubbles. These function as recombination centers; they keep the vacancy supersaturation low so that few, if any, bubbles grow into stable voids. They also keep the asymptotic swelling rate small. At and above 500 C, swelling is more a matter of helium bubble formation and growth towards critical sizes (Figs. 3 and 4). The cavity density and swelling rates are therefore insensitive to c. The steady swelling rate of 0.8%/dpa at 500 C is consistent with void swelling in austenitic stainless steel [7,8]. At higher temperatures, the increased helium mobility results in fewer cavities (7–81020 m-3 at 700 C), and a smaller density of bubbles escape to become stable voids and contribute to steady swelling.

![](images/07b85a190eb7618c9ba3b8d7e722f7c16c52282c5a49e8a0caed198a96de995d.jpg)  
Fig. 5. Volumetric swelling curves versus dose in the model that excludes void– void coalescence. The cavity surface energy is fixed at cðTÞ ¼ 0:75c0ðTÞ.

## 4.2. Cluster coalescence model

The other simplified limit of defect trapping is to neglect it entirely and assume that clusters diffuse freely according to their size. The predicted void size distribution changes significantly when coalescence is included. This is seen in Figs. 6 and 7, for the same temperatures as in Figs. 2 and 3.

Coalescence reactions continually, preferentially consume the smaller, more mobile clusters. The largest voids grow an order of magnitude larger through coalescence, making the distribution of stable void sizes substantially broader than before. Very large voids achieve such low diffusivities as to be effectively immobile; this results again in a terminal void population. At low temperatures, the removal of small unstable or equilibrium defect clusters reduces the number of recombination centers, suppresses damage annihilation, and speeds the formation of large, stable voids. This enhances low temperature swelling. At high temperatures, this same coalescence of small clusters greatly reduces the total number of helium bubbles and voids, so that the total void sink strength is kept small and the asymptotic swelling rate is diminished compared to the monomer aggregation model (Fig. 8 versus Fig. 5, respectively). Small clusters are absorbed as rapidly as new ones form, which prevents the formation of a bimodal distribution of small equilibrium bubbles and large voids. These differences suggest that competition between trapping and coalescence of very small (mostly TEM-invisible) clusters significantly shapes the microstructure in real irradiated materials.

When coalescence is included, the terminal void density and swelling rate remain sensitive to c up to 500 C. The predicted void density at this temperature increases from 7  1019 m-3 for c ¼ 0:75c0 to 7  1020 m-3 for c ¼ 0:5c0. The swelling rate for the former case is only 0.3%/dpa at 50 dpa but reaches 0.8%/dpa for the latter. This suggests that either the cavity surface energy is substantially smaller than the value for the clean metal or that the vacancy clusters have much smaller mobilities than are modeled

![](images/4cee43295a0c84a79a03809d4b7871642040d343b96b7e6bebed0fcea473b999.jpg)  
Fig. 6. A portion of the void/bubble distribution as in Fig. 2 (300 C), but including void coalescence and with cðTÞ ¼ 0:5c ðTÞ. The distribution has been smoothed for the large clusters, where Monte Carlo data is sparse.

![](images/9a6f5db8fd9549b74fafd37984e5e214128d0482288c80b96d347d6145c3d8e1.jpg)  
Fig. 7. The full void/bubble distribution as in Fig. 4 (500 C), but including void–void coalescence and with cðTÞ ¼ 0:5c0ðTÞ.

![](images/78c513010e9a17e4eac3b053a810274a027f0a4988b2531d636a0d2fb144b5bf.jpg)  
Fig. 8. Volumetric swelling curves versus dose in the model that includes void–void coalescence. The cavity surface energy is set to cðTÞ ¼ 0:4c0ðTÞ.

here. The swelling behavior finally becomes insensitive to the surface energy by 700 C. In this limit, coalescence reduces the terminal void density to 4–51018 m-3 .

## 5. Conclusions

This paper introduces a mixed Master Equation/Monte Carlo treatment of rate theory calculations in a mean field continuum approximation. This enables flexible treatment of the defect density variables, using different algorithms to treat the various reactions as efficiently as possible. The approximately quasi-stationary distribution of small, unstable or transient clusters is treated (as much as possible) by solving continuum rate equations. This eliminates the need to evaluate rapid individual reactions that mostly cancel one another. Larger clusters are treated by Monte Carlo methods, which treats clusters of arbitrary size and composition without the need for a fixed grid or artificial discretization of the defect distribution. A Markov method for smaller clusters accurately simulates rapid fluctuations in size and in the reaction parameters, and a Poisson-distributed random walk efficiently treats the more gradual evolution of the largest clusters. Finally, a macroparticle approach is introduced to encompass large differences in species densities in the Monte Carlo distribution.

This hybrid scheme readily treats void/bubble evolution to high cumulative fluxes for temperatures and dose rates that are characteristic of real reactor systems. Calculations demonstrate that void coalescence provides an important channel for consolidating vacancy defects into large, stable voids, controlling the duration of incubation and the terminal void density.

It is expected that thermal and radiation-induced micro-chemical evolution of solute and precipitate distributions will influence the cluster mobility and thereby the macroscopic incubation and steady-swelling behavior. Some degree of void/bubble trapping seems to be required in order to obtain a bimodal bubble/void size distribution, while some coalescence may be needed to give a realistically low terminal void density at higher temperature. The cavity surface energy determines the barrier for nucleation of stable voids and hence also affects the incubation behavior; this contribution becomes temperature- and time-dependent if oxygen is explicitly modeled. All of these effects can be addressed, in principle, by extensions of the method described here.

These calculations also suggest the importance of additional, competing processes that are not evaluated at present, such as interstitial–interstitial aggregation or cluster annihilation from void–dislocation reaction. The methods described here can be extended to treat coalescence of loops as easily as voids, given a suitable binary reaction kernel. Such reactions should be included for reasons of consistency, besides their likely contribution to transient and steady swelling behavior. They would be especially important if radiation damage were introduced as a variety of pre-formed defect clusters. Based on the preliminary findings for cavity coalescence, more general defect cluster reactions are expected to have a significant influence on radiation swelling behavior.

## Acknowledgements

This work performed under the auspices of the US Department of Energy by Lawrence Livermore National Laboratory under Contract DE-AC52-07NA27344. MPS acknowledges V.V. Bulatov for an early introduction to Markov chain Monte Carlo methods, e.g., Ref. [57].

## References

[1] C. Cawthorne, E. Fulton, Nature 216 (1967) 575.

[2] F.A. Garner, W.G. Wolfer, J. Nucl. Mater. 122&123 (1984) 201.

[3] T. Okita, T. Kamada, N. Sekimura, J. Nucl. Mater. 283–287 (2000) 220.

[4] T. Okita, T. Sato, N. Sekimura, F.A. Garner, L.R. Greenwood, J. Nucl. Mater. 307 (2002) 322.

[5] M.P. Surh, J.B. Sturgeon, W.G. Wolfer, J. Nucl. Mater. 325 (2004) 44.

[6] M.P. Surh, J.B. Sturgeon, W.G. Wolfer, J. Nucl. Mater. 328 (2004) 107.

[7] M. Surh, J. Sturgeon, W. Wolfer, J. Nucl. Mater. 336 (2005) 217.

[8] M.P. Surh, J.B. Sturgeon, W.G. Wolfer, J. Nucl. Mater. 328 (2004) 107.

[9] F.A. Garner, in: B. Frost (Ed.), Materials Science and Technology: A Comprehensive Treatment, vol. 10A, VCH Verlagsgesellschaft mbH, 1998, p. 419.

[10] T. Okita, T. Sato, N. Sekimura, F.A. Garner, in: Proceedings of the Fourth Pacific Rim International Conference on Advanced Materials and Processing, vol. PRICM-4, Aoba, Aramaki, Aoba-ku, Sendai, 2001.

[11] G.W. Greenwood, M.V. Speight, J. Nucl. Mater. 10 (1963) 140.

[12] E. Gruber, J. Appl. Phys. 38 (1967) 243.

[13] L.K. Mansur, Nucl. Technol. 40 (1978) 5.

[14] L.K. Mansur, W.A. Coghlan, J. Nucl. Mater. 119 (1983) 1.

[15] A.H. Marcus, Technometrics 10 (1968) 133.

[16] D. Gillespie, J. Atmos. Sci. 29 (1972) 1496.

[17] A.A. Lushenko, Fizika Atmosfery i Okeana 14 (1978) 738.

[18] P. Brown, G. Byrne, A. Hindmarsh, SIAM J. Sci. Stat. Comput. 10 (1989) 1038.

[19] M. Smith, T. Matsoukas, Chem. Eng. Sci. 53 (1998) 1777.

[20] H. Babovsky, Monte Carlo Meth. Appl. 5 (1999) 1.

[21] D. Gillespie, J. Chem. Phys. 114 (2000) 297.

[22] D. Gillespie, J. Chem. Phys. 115 (2001) 1716.

[23] A. Eibeck, W. Wagner, Ann. Appl. Probab. 11 (2001) 1137.

[24] E.L. Haseltine, J.B. Rawlings, J. Chem. Phys. 117 (2002) 6959.

[25] W.I. Friesen, T. Dabros, J. Chem. Phys. 119 (5) (2003) 2825.

[26] I.I. Laurenzi, S.L. Diamond, Physical Review E 67 (2003) 051103–1.

[27] D. Mukherjee, C. Sonwane, M. Zacariah, J. Chem. Phys. 119 (2003) 3391.

[28] A.H. Alexopoulos, A.I. Roussos, C. Kiparissides, Chem. Eng. Sci. 59 (2004) 5751.

[29] F. Filbet, P. Laurencot, SIAM J. Sci. Comput. 25 (6) (2004) 2004.

[30] H. Salis, Y. Kaznessis, J. Chem. Phys. 122 (2005) 054103.1.

[31] M. Kraft, Powder Particle 23 (2005) 18.

[33] J.J. Sniegowski, W.G. Wolfer, in: J.W. Davis, D.J. Michel (Eds.), Proceedings of Topical Conference on Ferritic Alloys for Use in Nuclear Energy Technologies, Snowbird, Utah, 1983, p. 579.

[32] W.G. Wolfer, B.B. Glasgow, Acta Metall. 33 (1985) 1997.

[34] M.P. Surh, W.G. Wolfer, J. Comput. Aided Design 14 (2007) 419.

[35] L. Greenwood, F. Garner, B. Oliver, M. Grossbeck, W.G. Wolfer, in: M.L. Grossbeck, T.R. Allen, R.G. Lott, A.S. Kumar (Eds.), The Effects of Radiation on Materials: 21st International Symposium, ASTM STP 1447, American Society for Testing and Materials International, West Conshohocken, PA, 2003.

[36] C. Schaldach, W. Wolfer, in: M.L. Grossbeck, T.R. Allen, R.G. Lott, A.S. Kumar (Eds.), The Effects of Radiation on Materials:21st International Symposium, ASTM STP 1447, American Society for Testing and Materials International, West Conshohocken, PA, 2003.

[37] F.C. Moon, Y.H. Pao, J. Appl. Phys. 38 (1967) 595.

[38] W.G. Wolfer, M. Ashkin, Scripta Metall. 7 (1973) 1175.

[39] G. Cottrell, J. Nucl. Mater. 302 (2002) 220.

[40] W.G. Wolfer, Philos. Mag. A 58 (1988) 285.

[41] J. Adams, W. Wolfer, J. Nucl. Mater. 166 (1989) 235.

[42] C.A. English, B.L. Eyre, J.W. Muncie, Philos. Mag. A 56 (1987) 453.

[43] W.D. Wilson, Radiat. Eff. 78 (1983) 11.

[44] R.S. Nelson, J. Nucl. Mater. 19 (1966) 149.

[45] E. Mikhlin, Phys. Status Solidi (a) 56 (1979) 763.

[46] D.E. Alexander, R.C. Birtcher, J. Nucl. Mater. 191–194 (1992) 1289.

[47] S.I. Golubov, A.M. Ovcharenko, A.V. Barashev, B.N. Singh, Philos. Mag. A 81 (3) (2001) 643.

[48] A. Solovyev, V. Terekhin, V. Tikhonchuk, L. Altgilgers, Phys. Rev. E 60 (1999) 7360.

[49] C. Birdsall, A. Langdon, H. Okuda, in: B. Alder, S. Fernbach, M. Rotenberg (Eds.), Methods in Computational Physics, vol. 9, Academic Press, New York, 1970, p. 241.

[50] P. MacKeown, Stochastic Simulation in Physics, Springer-Verlag, Singapore, 1997.

[51] W.H. Press, B.P. Flannery, S.A. Teukolsky, W.T. Vetterling, Numerical Recipes: The Art of Scientific Computing, Cambridge University, 1986.

[52] K. Sablefeld, S. Rogasinsky, A. Kolodko, A. Levykin, Monte Carlo Meth. Appl. 2 (1996) 41.

[53] W.H. Press, B.P. Flannery, S.A. Teukolsky, W.T. Vetterling, Numerical Recipes: The art of Scientific Computing, Cambridge University, 1986.

[54] E.H. Lee, L.K. Mansur, J. Nucl. Mater. 141–143 (1986) 695.

[55] E.H. Lee, L.K. Mansur, J. Nucl. Mater. 61 (1990) 733.

[56] M.F. Wehner, W.G. Wolfer, Philos. Mag. A 52 (1985) 189.

[57] W. Cai, V. Bulatov, S. Yip, J. Comput.-Aided Mater. Design 6 (1999) 175.
