# Further development of the fission gas swelling model for U-10Mo fuels

---

                                                               Journal of Nuclear Materials 565 (2022) 153769



                                                              Contents lists available at ScienceDirect


                                                        Journal of Nuclear Materials
                                                      journal homepage: www.elsevier.com/locate/jnucmat




Further development of the ﬁssion gas swelling model for U-10Mo
fuels
Xiaobin Jian1, Feng Yan1, Xiangzhe Kong, Yong Li, Shurong Ding∗
Department of Aeronautics and Astronautics, Institute of Mechanics and Computational Engineering, Fudan University, Shanghai 200433, China




a r t i c l e           i n f o                        a b s t r a c t

Article history:                                       The irradiation swelling of U-10Mo fuels is one of the critical factors to affect the in-pile structural in-
Received 4 January 2022                                tegrity and dimensional stability of fuel plates. In this study, a mechanistic model of ﬁssion gas swelling
Revised 4 March 2022
                                                       for U-10Mo fuels is newly developed with a new evolution model of bubble density, considering the ﬁs-
Accepted 25 April 2022
                                                       sion gas diffusion behavior and the grain recrystallization. The developed theoretical frame is validated by
Available online 27 April 2022
                                                       comparing the predictions in this study with diverse experimental data quantitatively and qualitatively,
Keywords:                                              including the ﬁssion gas swelling, total irradiation swelling, the evolution rules of the bubble density and
Fission gas swelling                                   the bubble size, together with the thickness increments of fuel foil in a monolithic U-10Mo/Al fuel plates.
Fission-induced creep                                  The correlation of the irradiation creep with the ﬁssion-gas-swelling induced porosity for U-10Mo fuels
External pressure                                      is ﬁrstly considered in the simulation of irradiation-induced thermal-mechanical behaviors in Al-cladded
Bubble density                                         monolithic fuel plates, and a new creep coeﬃcient of dense U-10Mo fuels is identiﬁed as 180 × 10−22
Bubble size
                                                       mm3 /MPa. The research results indicate that the developed ﬁssion gas swelling model has a satisfac-
                                                       tory prediction ability, especially for higher burnup cases, and can describe the dominant dependences
                                                       of external pressure and temperature found in the related experiments. In addition, parametric studies
                                                       have been carried out to investigate the inﬂuences of temperature, external pressure and grain-boundary
                                                       diffusion enhancement factor on the related ﬁssion gas behaviors.
                                                                                                                           © 2022 Elsevier B.V. All rights reserved.




1. Introduction                                                                          ated by grain recrystallization process [5–7]. As a result, a porous
                                                                                         structure will be formed [8–10] to weaken the thermal-mechanical
    U-10Mo alloy is a promising fuel to replace highly-enriched ura-                     properties of fuels [11,12], including the thermal conductivity, elas-
nium fuels in research and test reactors, due to its high uranium                        tic parameters and fracture strength.
density, stable γ phase and low neutron absorption cross section                             It has been demonstrated that the combination of irradiation
[1,2]. The Al-cladded monolithic fuel plates have been proposed                          swelling and irradiation-assisted creep of U-10Mo fuel foils inten-
and investigated for application in high performance research re-                        siﬁes the mechanical interactions with the cladding, presented as
actors (HPRRs) [3] of United States, with the zirconium diffusion                        an increase of the plate thickness [13]. At higher ﬁssion densities,
barrier layer designed between the U-10Mo fuel foil and the alu-                         cracking of U-10Mo fuel foil near the Zr diffusion barrier layer has
minum alloy cladding. Their structural integrity and dimensional                         been observed in the post irradiation examinations [14], and the
stability should be ensured for the in-reactor safe operation, which                     intrinsic mechanisms have aroused extensive attention. The failure
depend on the stable and predictable irradiation swelling of U-                          of fuel foil is deemed to have intense correlations with the ﬁs-
10Mo fuels [4].                                                                          sion gas behavior and the irradiation-induced mechanical behav-
    In addition to the ﬁssion solid swelling, the involved ﬁssion gas                    ior. Above all, a mechanistic ﬁssion gas swelling model for U-10Mo
swelling of U-10Mo fuels is one of the critical factors to affect the                    fuels is necessary to be developed, for precise predictions of the
in-pile performances of fuel plates [4], which has complex mecha-                        deformations of U-10M fuel plates at high burnup and analysis of
nisms. During irradiation, the ﬁssion gas atoms diffuse to the grain                     the fuel failure mechanism. Currently, various ﬁssion gas swelling
boundaries and lead to the nucleation and growth of large gas bub-                       models have been established for U-Mo fuels [1,3,5,15–17], in-
bles, which results in the macroscale ﬁssion gas swelling, acceler-                      cluding the physics-based models and phenomenological empirical
                                                                                         models. The phenomenological empirical models are obtained with
                                                                                         the irradiation experimental results, which are generally described
  ∗
    Corresponding author.                                                                as simple functions of the ﬁssion density [1,3]. Kim’s model [1] has
    E-mail address: dingshurong@fudan.edu.cn (S. Ding).                                  been widely used to simulate the irradiation-induced mechanical
  1
    These authors contributed equally to this work.



https://doi.org/10.1016/j.jnucmat.2022.153769
0022-3115/© 2022 Elsevier B.V. All rights reserved.
X. Jian, F. Yan, X. Kong et al.                                                                                          Journal of Nuclear Materials 565 (2022) 153769


behaviors in dispersion fuels and monolithic fuels, established with          sidering the effect of external hydrostatic pressure. Above all, the
the examined gas bubble information in U-10Mo/Al dispersion fu-               average number of gas atoms in one bubble should be determined,
els. Recently, a new series of empirical models for the total irradi-         which depends on the diffusion behavior of the ﬁssion gas atoms
ation swelling have been reported [3], given as the up-bound and              within the grains. In this study, the critical physical mechanisms
low-bound ones to envelop plenty of experimental data from U-                 are taken into account in our theoretical frame. It should be men-
10Mo monolithic fuel plates over a range of irradiation conditions.           tioned that a new bubble density model is proposed to capture the
    It should be mentioned that the ﬁssion gas swelling of nuclear            non-monotonic variations as a function of the ﬁssion density, dis-
fuels depends on the temperature, external hydrostatic pressure               covered in several fuels through post-irradiation experiments. The
and ﬁssion rate [18–20]. The ﬁssion gas behavior of U-10Mo fuels              predicted magnitudes of bubble density are consistent with those
in plate-type elements will be inﬂuenced by the actual in-service             of similar U-Mo fuels. The related models will be introduced be-
conditions, where non-homogenous distributions of temperature,                low.
ﬁssion rate and mechanical equilibrium hydrostatic pressure gra-
dients appear [21,22]. Several mechanistic models have been pro-              2.1. The governing equations for the ﬁssion gas atom diffusion
posed and improved [5,15–17], with important physical mecha-
nisms involved, such as the ﬁssion gas atom diffusion within the                  Taking the U-10Mo fuel as a collection of spherical grains, the
equivalent spherical grains [23], the grain recrystallization effect          diffusion equation of ﬁssion gas atoms is expressed as [15]
[5–7], resolution of ﬁssion gas atoms in the intra-granular and                        2         
                                                                              ∂c       ∂ c 2 ∂c
inter-granular bubbles [17,24,25]. As far as we know, although the               = Dg      +        + Y f˙ − 16π fn Dg rg cg2 − 4π rb Dg cg cb + bnb cb
predicted ﬁssion gas swelling results could match some experi-                ∂t       ∂ r2 r ∂ r
mental data, the predictions of bubble density and bubble radius                                                                                                   (1)
have been several orders of magnitude lower than the related ex-
                                                                              where, c denotes the local concentration of the dissolved ﬁssion
perimental data [8,25]. Especially, the dominant effect of external
                                                                              gas atoms in atom/m3 , which varies with time t in s and radial co-
hydrostatic pressure cannot be well captured, found in some ex-
                                                                              ordinates r in m, Y is the value of gas yield per ﬁssion, f˙ is the
periments [19].
                                                                              ﬁssion rate in ﬁssion/(m3 •s), fn is the nucleation factor, rg depicts
    In this study, a mechanistic model of ﬁssion gas swelling for
                                                                              the radius of the single gas atom in m, cg is the volume-average
U-10Mo fuels is further developed, with the inter-granular bubble
                                                                              concentration of the dissolved gas atoms in atom/m3 , cb and nb are
swelling correlated with the in-grain ﬁssion gas diffusion behavior
                                                                              the intra-granular bubble density in n/m3 and the gas atom num-
and grain recrystallization, with a new evolution model of bubble
                                                                              ber per bubble in atom/m3 , respectively, with the diffusion coef-
density involved. The obtained prediction results match well with
                                                                              ﬁcient Dg =D0 f˙ in m2 s−1 and the resolution rate of intra-granular
diverse experimental data, quantitatively and qualitatively, includ-
ing the ﬁssion gas swelling, total irradiation swelling, the evolution        bubbles b=b0 f˙ in s−1 .
rules of the bubble density and the bubble size, together with the               The evolution of intra-granular bubbles is described as [26]
thickness increments of a monolithic fuel foil. The effects of irradi-        d n b cb
                                                                                       = 16π fn Dg rg cg2 + 4π rb Dg cg cb − bnb cb                                (2)
ation conditions on the ﬁssion gas swelling, the bubble density and             dt
size are investigated, and the sensitivities to some critical model               Substituting Eq. (2) into Eq. (1) and denoting φ =c + nb cb yields
parameters are analyzed. It is noted that the correlation of the ir-
                                                                                       2          
radiation creep with the ﬁssion-gas-swelling induced porosity is              ∂φ       ∂ φ 2 ∂φ
                                                                                 = Dg       +        + Y f˙                                                        (3)
ﬁrstly considered in the simulation of irradiation-induced thermal-           ∂t       ∂ r2   r ∂r
mechanical behaviors in U-10Mo/Al monolithic fuel plates, and a
new creep coeﬃcient of dense U-10Mo fuels is identiﬁed.                          Considering the inter-granular resolution effect, the correspond-
                                                                              ing boundary conditions are adopted as
2. Model descriptions                                                         φ ( 0, t ) = 0
                                                                                                                                                                  (4)
                                                                              φ (rgr , t ) = b2DλNg
    As illustrated in Fig. 1, the grains of nuclear fuels are generally
regarded as spherical ones. The ﬁssion gas atoms will diffuse to-             where, rgr denotes the grain radius in m; b = b0 f˙ is the inter-
ward the grain boundary, and they could be trapped by the intra-              granular resolution rate in s−1 [27]; λ is the resolution depth in
granular and inter-granular bubbles. In the irradiation environ-              m and N is the equivalent surface concentration of the gas atoms
ments, the ﬁssion gas atoms in the bubbles are apt to re-dissolve             in the inter-granular bubbles in atom/m2 .
into the fuel matrix, due to the attack of high-energy fast neu-                  The conservation equation for the ﬁssion gas atoms is expressed
trons and the ﬁssion fragments. For the U-10Mo fuels in the dis-              as
persion fuel plates or monolithic fuel plates, grain recrystallization                  t                rgr
                                                                              4π rgr
                                                                                  3
                                                                                                                                        N
is demonstrated to occur, which will trigger the quick diffusion of                          Y f˙ dτ =           4π r 2 φ dr + 4π rgr
                                                                                                                                   2
                                                                                                                                                                   (5)
ﬁssion gas atoms to the grain boundary of ﬁne grains. It is noted                3      0                 0                             2
that the intra-granular bubbles are extremely small, which are dif-           where 4π rgr2 N indicates the gas atom contributions from the con-
                                                                                            2
ﬁcult to be identiﬁed by Scanning Electron Microscope (SEM) [7],              sidered grain to the inter-granular bubbles.
and their contributions could be considered in the ﬁssion solid                  It is noted that the analytical expressions for N (tˆ) and dNˆ have
                                                                                                                                            dt
swelling [1].                                                                 been obtained through Laplace transformation and inverse Laplace
    In fact, the experimental data of ﬁssion gas swelling are ob-             transformation by Cui et al. [15], wheretˆ = Dgt. With these ex-
tained with the identiﬁed number and size of inter-granular bub-              pressions, the values for the original grains, the ﬁne ones and the
bles by image processing of the microstructures of fuel particles in          shrunk ones can be calculated out at different time instants.
the U-10Mo dispersion fuel plates [7]. Therefore, a hypothesis that
the ﬁssion gas swelling only originates from the contribution of              2.2. The developed models for the bubble number and average gas
inter-granular bubbles is adopted in this study. Assuming that the            atom number per bubble
same bubble radius holds for all of the inter-granular bubbles at
a certain ﬁssion density, one can obtain their magnitudes at differ-             The number of all the inter-granular bubbles over the original
ent burnup levels through the modiﬁed Van Waals gas law by con-               grain is a critical parameter, and with it the average gas atom num-

                                                                          2
X. Jian, F. Yan, X. Kong et al.                                                                                                                  Journal of Nuclear Materials 565 (2022) 153769




                                                            Fig. 1. The sketch of behavior of ﬁssion gas atoms in a spherical grain.



ber and volumetric density of bubbles can be determined. A satu-                                         Hence, the average gas atom number in one bubble N̄atom can
ration of bubble density is observed in the ﬁssion density range                                      be obtained as
of 4.5-4.7 × 1027 ﬁssion/m3 for U-7Mo fuels, following with a re-                                                                                       2π rgr0
                                                                                                                                                            3
                                                                                                                                                                ·ηr
duction of bubble density at higher ﬁssion density levels [8]. Simi-                                             2π (1 − ηr )2/3 rgr0
                                                                                                                                  2
                                                                                                                                      · Cb Nb +            rgrx
                                                                                                                                                                    · Cbx Nbx
                                                                                                      N̄atom =                                                                           (10)
lar bubble evolution laws have also been reported in ceramic fuels                                                                 Nbubble1 +Nbubble2
[28]. For U-10Mo fuel, Jian et al. [29] have proposed a bubble den-
                                                                                                      where Nb and Nbx are the ﬁssion gas atom number per inter-
sity model, and the predictions are not in good agreement with
                                                                                                      granular bubble in the un-recrystallized region and ﬁne grains, re-
the experimental phenomena [8], and new development needs to
                                                                                                      spectively, deﬁned as [5]
be performed.                                                                                                                               
    The inter-granular bubbles are contributed by the un-                                                    N tˆ                      N tˆ 
                                                                                                                       rgr                       rgrx
recrystallized zone and the recrystallized zone. The numbers of                                       Nb =                      Nbx =                                                    (11)
                                                                                                                  Cb                       Cbx
bubbles from the un-recrystallized and recrystallized zones are de-
ﬁned as Nbubble1 and Nbubble2 , respectively, described as                                               It should be mentioned that the deﬁnition of Nbx here is differ-
                                                                                                      ent from that in Ref. [5].
Nbubble1 = 2π (1 − ηr )2/3 rgr0
                            2
                                · Cb · ηFd                                                  (6)          In Eqs. (7), (9) and (10), the volume fraction of the recrystallized
                                                                                                      zone is given as [5]
                2π rgr0
                    3
                        · ηr                                                                                                                                                    3
Nbubble2 =                        · Cbx · ηFd                                               (7)                              16γs B2 (Fd − Bux )        ( 1 − v/2 ) ( 1 − v )
                        rgrx                                                                          ηr =1 − 1 −                                                                        (12)
                                                                                                                                     rgr0                       2π
        
                1              Fd < Fd0                                                               where, γs is the surface tension in N/m, v is Poisson’s ratio, Bux in
ηFd =                                                                                       (8)       ﬁssion/m3 is the critical ﬁssion density dependent on ﬁssion rate
            (Fd0 /Fd )2        Fd ≥ Fd0
                                                                                                      [5], B2 is a parameter.
where, Fd represents the ﬁssion density in ﬁssions/m3 ;Fd0 =                                              It is noted that the form of (Fd0 /Fd )2 in Eq. (8) is adopted.
4.7 × 1027 ﬁssions/m3 , which has been ﬁtted out in this study,                                       This is consistent with the developed evolution model for the bub-
in order to make the calculated ﬁssion gas swelling results match                                     ble surface density of irradiated oxide fuels [31]. The experimental
well with the experimental results for U-10Mo fuel particles [8];                                     data of bubble density evolution for U-7Mo fuels [8] could also be
rgr0 depicts the radius of the original grain, and rgrx denotes that of                               described with this form. Besides, the obtained ﬁssion swelling re-
ﬁne grains; ηr represents the volume fraction of the recrystallized                                   sults could match well with the experimental results, as shown in
zone; with Cb and Cbx given as [5,26,30]                                                              Section 3. As a result, this form in Eq. (8) is reasonable and accept-
                                                                                                      able.
                                         1 / 2                                1 / 2
           8za dN                                           8za dN  
               dtˆ  rgr =(1−ηr )1/3 rgr0                         dtˆ   rgr =rgrx                      2.3. The model for the average bubble radius
Cb =                                                Cbx =                                   (9)
                 121/3 π ξ δ                                   121/3 π ξ δ
                                                                                                          Different from the treatment strategy in Refs. [5,15], the bub-
where, Cb and Cbx in n/m2 are the deﬁned grain-boundary bub-                                          bles are assumed to be spherical with an identical radius R̄ at an
ble concentrations of un-recrystallization region and ﬁne grains                                      instant, without differentiation of the bubble radii of the recrystal-
[5,26,30], respectively; z is the number of sites explored per gas-                                   lized and un-recrystallized zones. In fact, from the images of post-
atom jump; a3 /12 is the average volume of atom in m3 ; ξ is the                                      irradiation microstructures for the U-Mo fuels [1,10], one can see
grain-boundary diffusion enhancement factor; δ is the width of the                                    that the bubbles can be regarded as spherical ones with the same
boundary in m.                                                                                        radius at a certain ﬁssion density.

                                                                                                  3
X. Jian, F. Yan, X. Kong et al.                                                                                    Journal of Nuclear Materials 565 (2022) 153769


   The average bubble radius can be determined with the modiﬁed               Table 1
                                                                              Parameters used in calculations.
Van Waals gas law, given as
Pb 4π R̄3 /3 − hs bv N̄atom = N̄atom kT                          (13)          Parameter                           Value            Unit           Source

                                                                               Y                                   0.25             -              [32]
where, R̄ denotes the average bubble radius in m; Pb is the bubble             b0                                  2 × 10−24        m−3            [25]
pressure in Pa, T is the temperature in K, k is Boltzmann constant             fn                                  10−2             -              [26]
with a value of 1.38 × 10−23 J/K [28], hs is the ﬁtting parame-                rg                                  2.16 × 10−10     m              [32]
                                                                               b0 (un-recrystallization region)   4.0 × 10−26      m−3            this study
ter with a value of 0.6 [28], bv is the Van der Waals constant of
                                                                               b0 (ﬁne grain)                     1.9 × 10−25      m−3            this study
8.5 × 10−29 m3 /atom for Xe [15].                                              D0                                  1.0 × 10−40      m5             [25]
   As shown in Fig. 1, the bubble pressure is adopted as                       γ                                   1.0              N/m            [5]
                                                                              γs                                  1.0              N/m            [5]
           H p + 2γ /R̄ H p > 0                                                a                                   5.47 × 10−10     m              [26]
Pb =                                                             (14)
           2γ /R̄ H p ≤ 0                                                      z                                   4                -              [26]
                                                                               δ                                   2.0 × 10−9       m              [26]
where, γ denoted the surface tension of bubbles with a value of                rgr0                                3.5 × 10−6       m              [5]
1N/m [15]; H p depicts the external pressure in Pa. Eq. (14) implies           rgrx                                2.5 × 10−7       m              [5]
that when the external hydrostatic pressure is negative, the bubble            B2                                  10−34            m5 /N          [5]
                                                                               λ                                   2.5 × 10−8       m              [33]
pressure is considered to be balanced by the surface tension. If the
                                                                               ξ                                   2.0 × 107        -              this study
external hydrostatic pressure is positive, the bubble pressure will            Fd0                                 4.7 × 1027       ﬁssion/m3      this study
be enhanced.

2.4. The models for the ﬁssion gas swelling and the volumetric               3.1. Comparisons of the irradiation swelling, bubble density and
density of bubbles                                                           bubble radius evolutions

    Once the bubble number and average bubble radius are calcu-              3.1.1. The irradiation swelling results
lated out, the total bubble volume Vbubble in m3 can be obtained as              Fig. 2 (a) displays the predictions of ﬁssion gas swelling for
                                                                             the fuel particles in U-10Mo /Al dispersion fuel plates, together
                                   4
Vbubble = Nbubble1 +Nbubble2         π R̄3                       (15)        with some experimental data in Ref. [7]. The applied irradiation
                                   3
                                                                             conditions are chosen from Refs. [7,8], which are also marked in
    The current volume V of the originally considered grain is               Fig. 2 (a). One can ﬁnd that the predictions of ﬁssion gas swelling
V = 1 + SWsolid V0 + Vbubble                                     (16)        increase with the ﬁssion density, which are in general agreement
                                                                             with the available experimental data in Ref. [7]. Especially, the pre-
where, V0 is the initial grain volume in m3 , SWsolid    is the ﬁssion
                                                                             dicted ﬁssion gas swelling curve as a function of the ﬁssion den-
solid swelling, expressed as [1]
                                                                             sity appears in a downwards convex manner, which matches the
SWsolid = 0.04 × 10−27 Fd                                        (17)        characteristics of the experimental curves of irradiation swelling in
    The ﬁssion gas swelling can be obtained as                               some Refs. [4,36,37].
                                                                                 Fig. 2 (b) shows the predictions of total irradiation swelling
             Vbubble
SWgas =                                                          (18)        for U-10Mo fuel foils in U-10Mo monolithic fuel plates, which are
               V0                                                            compared with the experimental results of average swelling in
    The total irradiation swelling can be expressed as                       RERTR-12 campaign [14]. It should be mentioned that the fuel foil
                                                                             temperatures in the thickness direction are different, with higher
SW = SWsolid + SWgas                                             (19)
                                                                             magnitudes at the mid-plane of the fuel plate. For non-uniformly
    The average current porosity is                                          irradiated fuel plates, the fuel temperatures across the plate sur-
            Vbubble                                                          face also have a great divergence. So, the computational results for
poro =                                                           (20)        the two temperature values of 423 K and 473 K are given for com-
              V
                                                                             parison. One can see that the irradiation swelling results at higher
   The current quantity density of bubbles ρbubble in m−3 can be
                                                                             burnup will vary with the temperature, and become larger at a
also obtained as
                                                                             higher temperature value. This stems from the enhanced ﬁssion
              Nbubble1 +Nbubble2                                             gas swelling, as governed by Eq. (13).
ρbubble =                                                        (21)
                      V                                                          It can be seen that the predicted total irradiation swelling re-
                                                                             sults in this study are in good agreement with the experimental
3. Validation of the improved ﬁssion gas swelling model for                  data at different burnup levels [14]. The predictions in this study
U-10Mo fuels                                                                 locate in the range of the upper and lower bounds of total irradi-
                                                                             ation swelling proposed by Robison et.al [3]. At the ﬁssion densi-
    To authenticate the validity of the ﬁssion gas swelling model            ties lower than 4 × 1027 ﬁssion/m3 , the predictions in this study
for U-10Mo fuels developed above, various experimental results               are very close to those of Kim and Hofman [1]. At higher ﬁssion
are compared with the predictions in this study, including the ﬁs-           densities, the phenomenological empirical model of Kim and Hof-
sion gas swelling for U-10Mo fuel particles in dispersion fuel plates        man [1] will under-evaluate the ﬁssion gas swelling. The developed
[7], and the total irradiation swelling results for the U-10Mo fuel          mechanistic ﬁssion gas swelling model is demonstrated to have a
foils [14]. The predicted values of bubble porosity, bubble density          satisfactory prediction ability for the high ﬁssion density cases. Af-
and bubble radius are also analyzed, according to the experimen-             ter grain recrystallization, the ﬁssion gas atoms in the bubbles will
tal results for similar U-Mo fuels. Besides, the experimental data of        grow in quantity, which will lead to the sensitivities of the ﬁs-
the thickness increments of a U-10Mo monolithic fuel plate [34,35]           sion gas swelling to the temperature and external pressure [15].
are also employed for a comparison with the computation results,             If the post-irradiation annealing blister temperature needs to be
where different points in the considered path have experienced di-           predicted, or the failure mechanism of fuel foil is to be revealed,
verse irradiation histories and external hydrostatic pressures. The          it is necessary to adopt a precise mechanistic ﬁssion gas swelling
used model parameters are listed in Table 1.                                 model.

                                                                         4
X. Jian, F. Yan, X. Kong et al.                                                                                                 Journal of Nuclear Materials 565 (2022) 153769




Fig. 2. The evolution results of (a) the ﬁssion gas swelling SWgas for the fuel particles in U-10Mo/Al dispersion fuel plates and (b) the total irradiation swelling SW for the
fuel foils in U-10Mo/Al monolithic fuel plates.




                                      Fig. 3. (a) Bubble density and (b) bubble radius evolution results as a function of ﬁssion density.



3.1.2. The results of bubble density, bubble radius, current porosity                     recrystallization zone (in Fig. 4), the bubble density rises to the
and bubble pressure                                                                       maximum and then decreases. When the ﬁssion density exceeds
    In addition to the ability to predict the ﬁssion gas swelling, the                    5 × 1027 ﬁssion/m3 , the bubble radius increases linearly with the
developed mechanistic model system can also simultaneously ob-                            ﬁssion density. Actually, the ﬁssion-density dependent factor ηFd
tain the results of bubble density, bubble radius, current porosity                       adopted in this study can be interpreted as the effect of bubble
and bubble pressure. The corresponding prediction results of bub-                         coarsening [8]. It should be mentioned that the model for the bub-
ble density and bubble radius are shown in Fig. 3. One can ﬁnd                            ble density evolutions has been developed in Ref. [29], in which
that the predicted curves as a function of ﬁssion density are con-                        two constants are adopted to modify the obtained grain-boundary
sistent with the evolution rules represented by the experimental                          bubble concentration. So, the predicted bubble density there could
data of U-7Mo fuels [8]. The magnitude orders of bubble density                           not reﬂect the decrease of the bubble density after a maximum.
and bubble radius are the same to those of U-7Mo fuels [8]. In Ref.                           One can see the predicted results of current porosity and bub-
[8], it has been mentioned that the evolution law of bubble size for                      ble pressure in Fig. 4. As shown in Fig. 4 (a), the average porosity
U-10Mo fuels is similar to U-7Mo fuels, and the bubble densities                          is less than 5% before recrystallization. With the increase of ﬁssion
for different fuels all present an evolution trait of decrease after an                   density, the average porosity increases rapidly, which can reach
increase to the maximum value. The comparisons in Fig. 3 further                          ∼18% when the recrystallization process is completed. The current
demonstrate the effectiveness of the developed mechanistic model                          porosity curve can be approximately divided into two linear stages.
system in this study.                                                                     Generally, the macroscale strength of a material decreases as the
    The predicted bubble density before grain recrystallization is                        porosity increases [38,39]. A four-point bend tests for irradiated
hardly changed, with the bubble radius growing continuously to                            U-10Mo fuel foils [11] indicated that the bending strengths were
a size of 0.1 um at the beginning of recrystallization, as shown                          much lower than the tensile strengths of un-irradiated U-10Mo fu-
in Fig. 3 (a) and (b). During this stage, the bubbles locate nearby                       els [40], even at low ﬁssion density levels. The substantial decline
the initial grain boundary. From the microstructure image of atom-                        in the bending strength may be related to the locally enhanced
ized U-Mo particles in Ref. [37], the bubble number can be seen                           porosity, in spite of the extremely small average porosity, which
to almost un-vary, and the enlargement of the bubble size domi-                           needs to be investigated in the future.
nates. After grain recrystallization, the bubble density will increase                        In addition, the irradiation embrittlement of the U-10Mo fuel
quickly and the bubble sizes vary slightly. With the spread of the                        may also degrade the strength of the material, because the failure

                                                                                      5
X. Jian, F. Yan, X. Kong et al.                                                                                           Journal of Nuclear Materials 565 (2022) 153769




                                  Fig. 4. (a) Porosity and (b) bubble pressure evolution results as a function of ﬁssion density.


appears to have a evident trait of brittle fracture [11]. The U-10Mo
fuel foil is prone to failure because of high porosity, pore pressure
and low strength at high burnup [41]. Fig. 4 (b) exhibits the evo-
lution results of bubble pressure. It is noted that the evolution law
of bubble pressure is opposite to the bubble radius. At the initial
stage of burnup, the bubble pressure can reach ∼60 MPa, which
decreases with the ﬁssion density due to the growth of bubble size.

3.2. The thickness increment results of the fuel foil in a U-10Mo/Al
monolithic fuel plate

    The ﬁssion gas swelling model is introduced into the ﬁnite el-
ement analysis of the thermal-mechanical behavior in a U-10Mo
monolithic fuel plate. The irradiation-induced creep of U-10Mo fu-
els is also a critical factor to affect the thickness increments of
                                                                                    Fig. 5. Flow chart of stress-update algorithm for the integration points of the fuel
the fuel foil in the monolithic fuel plates [4,13]. The creep defor-
                                                                                    foil elements in a time increment.
mations will cause the stress relaxation of the U-10Mo fuel foil,
which will affect the hydrostatic-pressure dependent ﬁssion gas                     dimensional incremental constitutive relations and stress update
swelling. The deformation analysis of the U-10Mo monolithic fuel                    algorithms similar to those in Ref. [22]. Fig. 5 shows the ﬂow chart
plates has been performed in Refs. [13,21,35], with the same form                   of stress-update algorithm for the fuel foil in a time increment.
of U-10Mo creep rate model, expressed as ε˙ cr = Aσ f˙ . In order to                Combining the information in Fig. 6 with that in Ref. [22], one can
match the experimental data, different values of the creep rate co-                 know the coupling scheme between the ﬁssion-gas-swelling model
eﬃcient A have been identiﬁed without considering the effect of                     and the three-dimensional mechanical constitutive relation.
porosity [13,21,35]. However, the porosity dependence of the fuel                       A ﬁssion density distribution across the plate width is adopted
creep rate is signiﬁcant [42], especially for the case of high poros-               as that in Fig. 6 (a), based on Refs. [34,35]. The ﬁssion rates are
ity. From the results in Section 3.1, it can be seen that the porosity              obtained with the ﬁssion density divided by the total irradiation
of U-10Mo fuels could reach a high level, which indicates that the                  days of 98. It should be mentioned that the uncertainty exists in
inﬂuence of porosity on the creep rate cannot be ignored.                           the calculated ﬁssion rate with MCNP [44], so the ﬁssion rates near
    In this study, a modiﬁed creep rate model is employed to study                  the two width-direction ends are adjusted in this study. It can be
the irradiation-induced thermal-mechanical behavior in a U-10Mo                     found that the ﬁssion density exceeds 10.0 × 1027 ﬁssion/m3 at the
monolithic fuel plate, expressed as [43]                                            highly-irradiated region.
ε˙ cr = A 1 + 1250 poro2 σ f˙                                           (22)            Fig. 7 shows the thickness increment results of the U-10Mo fuel
                                                                                    foil across the plate width, including the experimental data in Refs.
where, the parameter A in mm3 /MPa needs to be recognized by                        [34,35] and the predictions in this study. Good agreement between
the experimental data, and the porosity is correlated with the ﬁs-                  the simulation results and the experimental data can be observed,
sion gas swelling in Eq. (20); ε˙ cr in s−1 depicts the equivalent creep            which validates the developed swelling and creep models. It is
strain rate;σ denotes the von Mises stress in MPa; f˙ is the ﬁssion                 noted that the parameter A in Eq. (22) is identiﬁed as 180 × 10−22
rate in ﬁssion/(mm3 •s).                                                            mm3 /MPa, which corresponds to the creep coeﬃcient of dense U-
    The fuel plate L1P04A in RERTR-9 campaign is chosen for pre-                    10Mo. It should be pointed out that the experiment data are de-
diction of the thickness increments of the fuel foil [35]. The de-                  rived from Refs. [34,35]. The supplied experimental data in these
tailed information of the ﬁnite element model can be found in                       two references have some differences from each other. In Fig. 7,
Appendix, including the geometric model, the mesh grid and the                      the experimental data in Region 1 adopt those in Ref. [34], and the
other thermal-mechanical properties. It is noted that the user-                     experimental data in Region 2 use the average values of those in
deﬁned subroutines of UMAT and UMATHT in the commercial soft-                       Refs. [34,35].
ware ABAQUS are used to deﬁne the thermo-mechanical constitu-                           One can ﬁnd that the predictions in this study match perfectly
tive relations for the cladding and fuel foil, based on the three-                  with the experimental data, with much better coincidence degrees

                                                                                6
X. Jian, F. Yan, X. Kong et al.                                                                                                  Journal of Nuclear Materials 565 (2022) 153769




         Fig. 6. (a) The distribution of ﬁssion density in the width direction of U-10Mo fuel foil at the irradiation time of 98 days and (b) the sketch of output path.




                                                                                           can be explained by the results of external hydrostatic pressure in
                                                                                           Fig. 8 (b). In the part from ∼2 to ∼17 mm, the values of hydrostatic
                                                                                           pressure are close to 0MPa. So, the corresponding predictions of
                                                                                           bubble radius and ﬁssion gas swelling mainly depend on the gas
                                                                                           atoms in the bubbles, which have a positive correlation with the
                                                                                           ﬁssion density.
                                                                                               In the part from 0 to ∼2 mm, the hydrostatic pressures reach
                                                                                           ﬁrstly an extremely large value of ∼113 MPa, then decrease quickly
                                                                                           to a small magnitude of ∼11 MPa at the location with a distance of
                                                                                           0.10462 mm away from the path origin, then maintain at a pres-
                                                                                           sure level of ∼20 MPa, and then decrease toward zero. So, the ﬁs-
                                                                                           sion gas swelling at the path origin reaches a value of ∼7% de-
                                                                                           spite of a very large ﬁssion density, then rises fast to ∼32% because
                                                                                           of the relatively large ﬁssion density and low external pressure
                                                                                           there, and then decreases to a local minimum, and subsequently
                                                                                           increases to a larger value due to the competition of the ﬁssion
                                                                                           density and external pressure. One can see that an external pres-
Fig. 7. The results of thickness increment of the U-10Mo fuel foil along Path 1 as         sure of ∼113 MPa can make the ﬁssion gas swelling reduce from a
shown in Fig. 6(b).
                                                                                           value of more than 32% to ∼7%. This is consistent with the report
                                                                                           in Ref. [19] that a ﬁssion gas swelling of ∼18% can vanish under
                                                                                           the external pressure of ∼40 MPa. This demonstrates that the cur-
than those in Refs. [13,21,35]. On one hand, the mechanistic                               rently developed ﬁssion gas swelling model can well capture the
ﬁssion gas swelling model and creep rate model for U-10Mo fuels                            external-pressure dependence.
are more reasonable, as presented above. The predicted results                                 In our previous studies [21,29], the predictions of ﬁssion gas
of bubble density and radius conform to reality, as analyzed in                            swelling are not very sensitive to the external pressure, because
Section 3.1. As a result, the external-pressure dependence of the                          the pressure H p in Eq. (14) has a weaker contribution than that
ﬁssion gas swelling is hopeful to be better captured. The coupling                         from the surface tension, owing to the lowered bubble radius pre-
of the ﬁssion gas swelling and creep is ﬁrstly reﬂected for U-10Mo                         dictions by several orders of magnitude. It should be mentioned
fuels, so the bubble-induced porosity can be correlated with the                           that the predicted ﬁssion gas swelling results in Ref. [21] differ
creep rate in real time. The critical physical mechanisms have been                        from those in Fig. 8 (a), in the aspects of the distribution trait
involved in the developed swelling and creep rate models, so the                           and the magnitudes. The predictions of external pressure in Ref.
irradiation-induced mechanical behavior deserves to be simulated                           [21] also have some discrepancies from those in this study, with
more precisely. On the other hand, the irradiation conditions                              negative values in the middle region there. These differences stem
adopted in this study are different with the ones used in Refs.                            from the adopted ﬁssion gas swelling and creep models. In fact,
[13,21,35]. In view of the uncertainties in the calculated ﬁssion                          the mechanical ﬁelds are also inﬂuenced greatly, which will be in-
rate with respect to the initial conﬁguration of the reactor core,                         vestigated in the future work.
especially for those data near the edges, the currently adopted                                From Fig. 8, it can be known that the conditions of external
ﬁssion density distribution in Fig. 6 (a) can be acceptable. It can                        hydrostatic pressure in the central region of fuel foil are similar to
be also understood as that the actual ﬁssion density distribution                          those of fuel particles in U-10Mo/Al dispersion fuels [45], so the
has been distinguished.                                                                    predictions from empirical models in Ref. [1] can agree well with
    Fig. 8 (a) displays the distribution of ﬁssion gas swelling along                      those of fuel foils in the central region of monolithic fuel plates.
the width direction of U-10Mo fuel foil. One can ﬁnd that the                              It is noted that the conditions of external hydrostatic pressure
curve part from ∼2 to ∼17 mm is consistent with the variation                              in the other regions have obvious differences. So, in this sense,
trait of ﬁssion density curve in Fig. 6 (a). While, the results in the                     the general predictions from the empirical models of irradiation
other parts are not positively correlated with the ﬁssion density,                         swelling are possible to have deviations from reactivity in the
especially in the vicinity of the two path ends. These predictions                         monolithic fuels.

                                                                                       7
X. Jian, F. Yan, X. Kong et al.                                                                                                     Journal of Nuclear Materials 565 (2022) 153769




                             Fig. 8. The distributions of (a) the ﬁssion gas swelling and (b) the external hydrostatic pressure along the fuel foil width.




                                  Fig. 9. The evolution results of (a) the ﬁssion gas swelling and (b) bubble radius under different temperatures.



4. Effects of model parameters and irradiation conditions on                                  effect of temperature before initiation of recrystallization is pre-
ﬁssion gas swelling                                                                           dicted to be more notable in this study. From Eqs. (13) and (14),
                                                                                              one can know that the temperature effects can be really reﬂected
    The irradiation temperatures are usually non-uniform within                               when the actual magnitude order of the bubble radius is taken into
the fuel plate. The induced local in-homogeneities in the irradi-                             account. In the previous studies [5,15], the predictions of ﬁssion
ation swelling, thermal expansion and creep deformations will                                 gas swelling were matched with the experimental data, by using
trigger the complex mechanical interactions among the fuel foil                               very large values of bubble density and very small values of bub-
or the fuel particles, the metal matrix and the cladding. One                                 ble radius. So, the pore pressure resulting from the surface tension
can know that the external pressures within the fuels will vary                               is ampliﬁed by several orders of magnitude. Hence, the tempera-
with the locations and ﬁssion density. For different fuels, the                               ture effect cannot be precisely captured.
critical model parameters, such as the grain boundary diffusion                                   It is noted that the bubble density is not affected by tempera-
enhancement factor in Eq. (9) will be different. In order to better                           ture, and the bubble radius is governed by the modiﬁed Van Waals
understand the ﬁssion gas behaviors of U-10Mo fuels or the other                              gas law. So, the increase of ﬁssion gas swelling with the irradi-
fuels, the inﬂuences of the irradiation temperatures, the external                            ation temperature stems from the expansion of bubble size. As
pressures and the grain boundary diffusion enhancement factors                                shown in Fig. 9(b), the bubble radius seems to have no very dom-
will be analyzed in this section.                                                             inant variation. With a temperature increase from 323 to 473 K,
                                                                                              the bubble radius at the ﬁssion density of 8.64 × 1027 ﬁssion/m3
4.1. Effects of irradiation temperature                                                       has an enlargement of ∼16%. However, the corresponding ﬁssion
                                                                                              gas swelling has an increase of ∼57%. In general, the ﬁssion gas
   Fig. 9 (a) gives the evolution results of ﬁssion gas swelling un-                          swelling is considered to be un-sensitive to the irradiation temper-
der different irradiation temperatures. It can be seen that the ﬁs-                           ature at the range lower than 250 °C [7]. From the predictions in
sion gas swelling increases with the irradiation temperature. The                             this study, it can be recognized that the temperature effect should
absolute differences are gradually enlarged with an increase of ﬁs-                           be well considered. Therefore, it is very important to maintain a
sion density. When the temperature rises from 323 to 423 K, the                               good heat transfer performance of the reactor core. Thus, the ﬁs-
ﬁssion gas swelling increases by ∼37% at the ﬁssion density of                                sion gas swelling and the related porosity can be restrained in the
8.64 × 1027 ﬁssion/m3 . Compared to the results in Ref. [15], the                             acceptable ranges.

                                                                                          8
X. Jian, F. Yan, X. Kong et al.                                                                                                     Journal of Nuclear Materials 565 (2022) 153769




    Fig. 10. Comparison results of ﬁssion gas swelling with previous study [29].              Fig. 12. Comparison of the ﬁssion gas swelling predictions for different hydrostatic
                                                                                              pressures using different models.

    The distinct temperature effect of ﬁssion gas swelling has not                            from 2.5 to 10 MPa. Once the hydrostatic pressure is higher than
been predicted previously for U-10Mo fuels. As shown in Fig. 10,                              100 MPa, the ﬁssion gas swelling will be less than 5.1%. As shown
the predictions of ﬁssion gas swelling at two temperature values                              in Fig. 12, the reported effect of external pressure in the experi-
are obtained with the model established in this study and that                                mental research [19] has been simulated in this study, which can-
in Ref. [29], respectively. It should be mentioned that the model                             not be captured with the previous ﬁssion gas swelling model [29].
in Ref. [29] is similar as those in Refs. [5,15]. One can ﬁnd that                            In Ref. [29], the effect of external hydrostatic pressure is slight be-
the temperature dependence of ﬁssion gas swelling before recrys-                              fore recrystallization, which results from the ampliﬁed bubble den-
tallization disappears in the results calculated with the model in                            sity. When the hydrostatic pressure increases from 2.5 to 100 MPa,
Ref. [29]. At the end of the investigated burnup, the deviation of                            the reduction of ﬁssion gas swelling reaches ∼30% using the model
ﬁssion gas swelling from 323 to 423 K in this study can reach                                 in Ref. [29], which is much smaller than the predicted value of
∼60%, but only about ∼30% when using the model in Ref. [29].                                  ∼85% in this study. From these predictions, one can recognize that
Simultaneously, distinct differences appear in the, respectively                              the external pressure has a prominent inﬂuence on the ﬁssion gas
predicted results at higher burnup levels, for the temperature case                           swelling. If the U-10Mo fuel particles are dispersed in a matrix
of 473 K. It is noted that the gas swelling curve predicted with                              with the ability of providing enough constraining forces, the ﬁs-
the model in Ref. [29] presents an unsmooth feature at the ﬁssion                             sion gas swelling of fuel particles can be restrained greatly. In the
density close to 8 × 1027 ﬁssion/m3 , after this ﬁssion density a                             current U-10Mo/Al dispersion fuel plates, considerable ﬁssion gas
linear relation appears. In fact, this appearance is induced by the                           swelling has been examined [7], which is induced by the weak-
deﬁnition of Nbx there.                                                                       ened constraint capability of the matrix, because of its chemical
                                                                                              reactions with the fuel particles.
4.2. Effects of external hydrostatic pressure                                                     As mentioned in Section 3.2, the developed models in this
                                                                                              study can capture the effect of external pressure, which is at-
   The effects of external pressure can be found from Fig. 11. The                            tributed to the objective consideration of the magnitude orders of
evolution results of ﬁssion gas swelling under four different hydro-                          the bubble density and bubble radius. For these reasons, the ac-
static pressures indicate that the ﬁssion gas swelling will be well                           tual effect cannot be well predicted in Refs. [15,46], although the
inhibited even under a low hydrostatic pressure of 10 MPa. At the                             correlation of external pressure has been considered. From the cur-
ﬁssion density of 8.64 × 1027 ﬁssion/m3 , the ﬁssion gas swelling                             rently developed theoretical frame in Section 2, one can know that
has a reduction of ∼46% with the external pressure increasing                                 the external pressure does not affect the evolution results of bub-




                              Fig. 11. The evolution results of (a) the ﬁssion gas swelling and (b) bubble radius under different hydrostatic pressures.


                                                                                          9
X. Jian, F. Yan, X. Kong et al.                                                                                                Journal of Nuclear Materials 565 (2022) 153769




     Fig. 13. The evolution results of (a)the ﬁssion gas swelling, (b) bubble density and (c) bubble radius with different grain boundary diffusion enhancement factors.



ble density. Similar to the analysis in Section 4.1, the variations of                        As shown in Fig. 13 (a), the ﬁssion gas swelling increases with
bubble size under different external pressures will contribute to                         the grain boundary diffusion enhancement factors, with an in-
the change in the ﬁssion gas swelling. As depicted in Fig. 11 (b),                        crease of ∼29% when the grain boundary diffusion enhancement
the bubble size is sensitive to the external pressure in the range                        factor is enlarged 5 times of 1 × 107 . It should be mentioned that
from 2.5 to 50 MPa, and then decreases slowly with the further                            the grain boundary diffusion enhancement factor of U-10Mo fuels
increase of external pressure. At the ﬁssion density of 8.64 × 1027                       is re-identiﬁed to obtain a new bubble density model according to
ﬁssion/m3 , the bubble radius decreases from ∼0.32 to ∼0.19 um,                           the experimental data [8], which are different from those in our
while the corresponding ﬁssion gas swelling has a signiﬁcant re-                          previous studies. It is noted that the value of 2 × 107 adopted
duction from ∼33% to ∼7%. It can be obtained that the bubble size                         in this study is much larger than the one used in Refs. [5,15],
has a great inﬂuence on the ﬁssion gas swelling.                                          so that the predicted bubble density can have the same order of
                                                                                          magnitude as those of similar U-Mo fuels [8]. It can be found
4.3. Effect of grain boundary diffusion enhancement factor and F_d0                       from Fig. 13 (a) that the ﬁssion gas swelling will increase with the
                                                                                          decrease of grain boundary diffusion enhancement factor. Differ-
   The grain boundary diffusion enhancement factors in Eq. (9) di-                        ent from the inﬂuence mechanisms of temperatures and external
rectly relate to the bubble density. It is reported that the density                      pressures, the grain boundary diffusion enhancement factors will
of ﬁssion-gas induced bubbles in UO2 fuels is one order of mag-                           change both the bubble density and the bubble size, as shown in
nitude lower than the one found in U-Mo fuels, and the bubble                             Fig. 13 (b) and (c), which are governed by Eqs. (6), (7) and (9).
sizes of the former fuels are much larger [8,28]. It implies that the                         It can be found from Fig. 13 (b) that the bubble density de-
grain boundary diffusion enhancement factors for UO2 fuels will                           creases with the increase of grain boundary diffusion enhancement
be larger than those for U-Mo fuels, which are diverse for different                      factor, while the inﬂuences will become weaker and weaker in the
ﬁssile materials. A region of Molybdenum-depletion existed in the                         investigated range of this study. With the grain boundary diffu-
fuel foil nearby the interface with the cladding, and the ﬁssion gas                      sion enhancement factor enlarged from 1 × 107 to 4 × 107 , the
swelling there was enhanced [14,47]. This might result from the                           maximum bubble density reduces from ∼7 to ∼3.5 um−3 . When
varied grain boundary diffusion enhancement factors in different                          the factor increases from 4 × 107 to 6 × 107 , the maximum bub-
U-Mo fuels. Hence, it is necessary to investigate the effects of                          ble density has a slight reduction of ∼0.6 um−3 . Due to that the
grain boundary diffusion enhancement factor on the ﬁssion gas                             total ﬁssion gas atoms in all the inter-granular bubbles have no
behaviors.                                                                                difference for the four cases of grain boundary diffusion enhance-

                                                                                     10
X. Jian, F. Yan, X. Kong et al.                                                                                                 Journal of Nuclear Materials 565 (2022) 153769




                                  Fig. 14. (a) Bubble density and (b) ﬁssion gas swelling evolution results as a function of ﬁssion density.

ment factor, the average ﬁssion gas atoms in a bubble is higher                           thickness deformations of fuel foils are obtained, and match well
for a smaller bubble density. Based on Eq. (13), the corresponding                        with diverse experimental data, validating the effectiveness of the
bubble size will become larger, as shown in Fig. 13 (c). With the                         ﬁssion gas swelling model. The effects of temperature, external
dominant inﬂuences of bubble radius, as analyzed in the previous                          hydrostatic pressure and grain boundary enhancement factor on
sections, the ﬁssion gas swelling grows with the grain boundary                           the ﬁssion gas behaviors are analyzed. The main conclusions are
diffusion enhancement factor despite the decrease of the bubble                           as follows:
density. Thus, higher grain boundary diffusion enhancement fac-
                                                                                          (1) The predictions of ﬁssion gas swelling and total irradiation
tors for UO2 fuels will lead to enhanced ﬁssion gas swelling in the
                                                                                              swelling for U-10Mo fuels are in good agreement with exper-
rim regions of fuel pellets [28] or fuel particles in dispersion fu-
                                                                                              imental data, and the evolution traits and magnitude orders
els [48], especially at high temperature conditions. At present, the
                                                                                              of bubble density and bubble size are similar with the post-
relationship between grain boundary diffusion enhancement factor
                                                                                              irradiation experimental results of U-7Mo alloy.
and the material composition is not clear. More experimental data
                                                                                          (2) The thickness increment predictions of the U-10Mo fuel foil in
will be needed for the further researches. It should be mentioned
                                                                                              a U-10Mo/Al monolithic fuel plate are consistent with the mea-
that the differences of ﬁssion gas swelling behaviors in different
                                                                                              sured data, thanks to the new ﬁssion gas swelling model and
fuels possibly stem from diverse swelling mechanisms, which de-
                                                                                              the porosity-dependent irradiation creep model.
serve deep researches.
                                                                                          (3) Compared to the previous results in the references, the effects
    It should be mentioned that the values of Fd0 in Eq. (8) have
                                                                                              of temperature, hydrostatic pressure and grain-boundary en-
some uncertainties, for U-10Mo fuels fabricated with different pro-
                                                                                              hancement factor on the ﬁssion gas swelling are predicted to
cessing parameters. The effects of this parameter should be inves-
                                                                                              be more signiﬁcant, even before the recrystallization initiation.
tigated. Fig. 14 gives the evolution results of bubble density and
ﬁssion gas swelling for four values of Fd0 . From Fig. 14 (a), it can
be found that the evolutions of bubble density are similar with                           Declarations of Competing Interest
each other before the saturation of bubble density. When Fd0 is
relatively small, the bubble density will start to reduce earlier. Un-                        We declare that no conﬂict of interest exits in our manuscript
der the same burnup larger than 4.0 × 1027 ﬁssion/m3 , the bub-                           entitled Further development of the ﬁssion gas swelling model for
ble density decreases with the reduction of Fd0 . From Fig. 14 (b),                       U-10Mo fuels. Manuscript is approved by all authors for publi-
one can ﬁnd the ﬁssion gas swelling has a tendency to rise as                             cation. I would like to declare on behalf of my co-authors that
Fd0 decreases, having an increase of ∼13% at the ﬁssion density of                        the work described was original research that has not been pub-
8.64 × 1027 ﬁssion/m3 , after a reduction of Fd0 from 5.0 × 1027                          lished previously, and not under consideration for publication else-
ﬁssion/m3 to 4.0 × 1027 ﬁssion/m3 . It can be obtained that the ﬁs-                       where, in whole or in part. All the authors listed have approved the
sion gas swelling is relatively insensitive to the value of Fd0 in the                    manuscript that is enclosed.
considered range.
    It should be mentioned that this value of Fd0 in Eq. (8) has been                     CRediT authorship contribution statement
ﬁtted out to be 4.7 × 1027 ﬁssion/m3 , in order to make the calcu-
lated ﬁssion gas swelling results match well with the experimental                            Xiaobin Jian: Software, Validation, Formal analysis, Investiga-
results for U-10Mo fuel particles. This value is close to the mea-                        tion, Data curation, Writing – original draft, Visualization. Feng
surement of U-7Mo dispersion fuel particles [8], which demon-                             Yan: Methodology, Software, Validation, Investigation. Xiangzhe
strates that the corresponding values of these two fuels are close                        Kong: Methodology, Validation. Yong Li: Methodology, Valida-
to each other.                                                                            tion. Shurong Ding: Conceptualization, Methodology, Software, Re-
                                                                                          sources, Writing – review & editing, Supervision, Project adminis-
5. Conclusions                                                                            tration.

   In this study, a mechanistic model of ﬁssion gas swelling for                          Acknowledgment
U-10Mo fuels is developed with a new evolution model of bubble
density involved, considering the ﬁssion gas diffusion behavior                              The authors thank for the supports of National Natural Science
and the grain recrystallization. The evolution rules of the ﬁssion                        Foundation of China (No. 12132005, 12102094, 12135008), the sup-
swelling, bubble density and the bubble size, together with the                           ports of the foundation from Science and Technology on Reactor

                                                                                     11
X. Jian, F. Yan, X. Kong et al.                                                                                                       Journal of Nuclear Materials 565 (2022) 153769




                                               Fig. A.1. The sketch of ﬁnite element geometric model and boundary conditions.



System Design Technology Laboratory. This study is also sponsored                              [13] F. Yan, X. Jian, S. Ding, Effects of UMo irradiation creep on the thermo-me-
by Shanghai Sailing Program (21YF1402200).                                                          chanical behavior in monolithic UMo/Al fuel plates, J. Nucl. Mater. 524 (2019)
                                                                                                    209–217.
                                                                                               [14] F. Rice, W. Williams, A. Robinson, et al., RERTR-12 Post-Irradiation Examination
Appendix A. Appendix title                                                                          Summary Report. Idaho National Laboratory Report INL/EXT-14-33066, 2015.
                                                                                                    https://www.osti.gov/biblio/1173078.
                                                                                               [15] Y. Cui, S. Ding, Z. Chen, et al., Modiﬁcations and applications of the mechanistic
(1) Finite element geometric model and boundary conditions                                          gaseous swelling model for UMo fuel, J. Nucl. Mater. 457 (2015) 157–164.
                                                                                               [16] J. Rest, Modeling of ﬁssion-gas-induced swelling of nuclear fuels, Compress.
   The fuel plate L1P04A is chosen to study the thickness incre-                                    Nucl. Mater. 3 (2012) 579–627.
                                                                                               [17] J. Rest, An analytical study of gas-bubble nucleation mechanisms in urani-
ments of fuel foil during irradiation. The geometric dimensions of
                                                                                                    um-alloy nuclear fuel at high temperature, J. Nucl. Mater. 402 (2010) 179–
the fuel plate can be obtained from Ref. [35]. In order to improve                                  185.
the calculation eﬃciency, a region of the central part of the fuel                             [18] T. Ogata, T. Yokoo, Development and validation of ALFUS: an irradiation be-
                                                                                                    havior analysis code for metallic fast reactor fuels, Nucl. Technol. 1 (1999)
plate is intercepted as a ﬁnite element model in this study, as
                                                                                                    113–123.
shown in Fig. A.1. The boundary conditions are also given in the                               [19] A.T. Churchman, R.S. Barnes, A.H. Cottrell, Effects of heat and pressure on the
ﬁgure.                                                                                              swelling of irradiation uranium, J. Nucl. Eng. 7 (1958) 88–96.
                                                                                               [20] M.M. Hall, J.E. Flinn, Stress state dependence of in-reactor creep and swelling.
(2) Material properties                                                                             part 2: experimental results, J. Nucl. Mater. 396 (2010) 119–129.
                                                                                               [21] X. Jian, F. Yan, X. Kong, et al., Effects of U-Mo irradiation creep coeﬃcient on
   As for the U-10Mo fuel foil, except for the models of the ir-                                    the mesoscale mechanical behavior in U-Mo/Al monolithic fuel plates, Nucl.
                                                                                                    Mater. Energy 21 (2019) 100706.
radiation swelling and ﬁssion-induced creep given in Section 2,                                [22] X. Kong, X. Tian, F. Yan, et al., Thermo-mechanical behavior simulation cou-
the mechanical constitutive models including the elastic properties                                 pled with the hydrostatic-pressure-dependent grain-scale ﬁssion gas swelling
dependent on irradiation-induced porosity, the thermal expansion                                    calculation for a monolithic UMo fuel plate under heterogeneous neutron irra-
                                                                                                    diation, Open Eng. 8 (2018) 243–260.
can be found in Ref. [29].                                                                     [23] M. Speight, A calculation on the migration of ﬁssion gas in material exhibiting
   As for the Aluminum alloy cladding, the models for the elastic                                   precipitation and re-solution of gas atoms under irradiation, Nucl. Sci. Eng. 37
performances [35], the thermal expansion [49] and the irradiation                                   (1969) 180–185.
                                                                                               [24] J. Rest, G.L. Hofman, Y.S. Kim, Analysis of intergranular ﬁssion-gas bubble-size
hardening plastic behavior [13] are considered. The thermal creep                                   distributions in irradiated uranium-molybdenum alloy fuel, J. Nucl. Mater. 385
rate model is also adopted, which can be found in Ref. [50].                                        (2009) 563–571.
   The thermal conductivities for U-10Mo [12,51] and Al alloy                                  [25] J. Rest, Evolution of ﬁssion-gas-bubble-size distribution in recrystallized
                                                                                                    U-10Mo nuclear fuel, J. Nucl. Mater. 407 (2010) 55–58.
cladding [49] are adopted to calculate the temperature ﬁelds of
                                                                                               [26] J. Spino, J. Rest, W. Goll, et al., Matrix swelling rate and cavity volume balance
fuel plates.                                                                                        of UO2 fuels at high burn-up, J. Nucl. Mater. 346 (2005) 131–144.
                                                                                               [27] J. Rest, A model for ﬁssion-gas-bubble behavior in amorphous uranium silicide
References                                                                                          compounds, J. Nucl. Mater. 325 (2004) 107–117.
                                                                                               [28] J. Spino, A.D. Stalios, H. Santa Cruz, et al., Stereological evolution of the rim
                                                                                                    structure in PWR-fuels at prolonged irradiation: dependencies with burn-up
 [1] Y.S. Kim, G.L. Hofman, Fission product induced swelling of U-Mo alloy fuel, J.
                                                                                                    and temperature, J. Nucl. Mater. 354 (2006) 66–84.
     Nucl. Mater. 419 (2011) 291–301.
                                                                                               [29] X. Jian, X. Kong, S. Ding, A mesoscale stress model for irradiated U-10Mo
 [2] D.E. Burkes, A.J. Casella, A.M. Casella, Measurement of ﬁssion gas release from
                                                                                                    monolithic fuels based on evolution of volume fraction/radius/internal pres-
     irradiated UMo dispersion fuel samples, J. Nucl. Mater. 478 (2016) 365–374.
                                                                                                    sure of bubbles, Nucl. Eng. Technol. 51 (2019) 1575–1588.
 [3] A.B. Robinson, W.J. Williams, W.A. Hanson, et al., Swelling of U-Mo monolithic
                                                                                               [30] M.H. Wood, K.L. Kear, On the in-pile nucleation and growth of grain-boundary
     fuel: developing a predictive swelling correlation under research reactor con-
                                                                                                    bubbles, J. Nucl. Mater. 118 (1983) 320–324.
     ditions, J. Nucl. Mater. 544 (2021) 152703.
                                                                                               [31] R.J. White, The development of grain-face porosity in irradiated oxide fuel, J.
 [4] M.K. Meyer, J. Gan, J.F. Jue, et al., Irradiation performance of U-Mo monolithic
                                                                                                    Nucl. Mater. 325 (2004) 61–77.
     fuel, Nucl. Eng. Technol. 46 (2014) 169–182.
                                                                                               [32] D.R. Olander, Fundamental Aspects of Nuclear Reactor Fuel Elements, Technical
 [5] J. Rest, A model for the effect of the progression of irradiation-induced re-
                                                                                                    Information Center, Oﬃce of Public Affairs, 1976.
     crystallization from initiation to completion on swelling of UO2 and U-10Mo
                                                                                               [33] Y. Cui, S.R. Ding, Y.Z. Huo, An eﬃcient numerical method for intergranular ﬁs-
     nuclear fuels, J. Nucl. Mater. 346 (2005) 226–232.
                                                                                                    sion gas evolution under transient with piecewise boundary resolution, J. Nucl.
 [6] L. Liang, Z. Mei, A.M. Yacout, Fission-induced recrystallization effect on inter-
                                                                                                    Mater. 1-3 (2013) 570–578.
     granular bubble-driven swelling in U-Mo fuel, Comput. Mater. Sci. 138 (2017)
                                                                                               [34] S.J. Miller, H. Ozaltun, Evaluation of U10Mo Fuel Plate Irradiation Behavior Via
     16–26.
                                                                                                    Numerical and Experimental Benchmarking, IMECE2012, Houston, Texas, USA,
 [7] Y.S. Kim, G.L. Hofman, J.S. Cheon, Recrystallization and ﬁssion-gas-bubble
                                                                                                    2012.
     swelling of U-Mo fuel, J. Nucl. Mater. 436 (2013) 14–22.
                                                                                               [35] Y.S. Kim, G.L. Hofman, J.S. Cheon, et al., Fission induced swelling and creep of
 [8] D. Salvato, A. Leenaers, S. Van den Berghe, et al., Pore pressure estimation in
                                                                                                    U-Mo alloy fuel, J. Nucl. Mater. 437 (2013) 37–46.
     irradiated UMo, J. Nucl. Mater. 510 (2018) 472–483.
                                                                                               [36] T. Winter, C. Deo, Comparison of ﬁssion gas swelling models for amorphous
 [9] A.M. Casella, D.E. Burkes, P.J. MacFarlan, et al., Characterization of ﬁssion gas
                                                                                                    U3Si2 and crystalline UO2, Ann. Nucl. Energy 100 (2017) 31–41.
     bubbles in irradiated U-10Mo fuel, Mater. Charact. 131 (2017) 459–471.
                                                                                               [37] A. Leenaers, W. Van Renterghem, S. Van den Berghe, High burn-up structure
[10] J. Gan, B.D. Miller, D.D. Keiser, et al., Irradiated microstructure of U-10Mo
                                                                                                    of U(Mo) dispersion fuel, J. Nucl. Mater. 476 (2016) 218–230.
     monolithic fuel plate at very high ﬁssion density, J. Nucl. Mater. 492 (2017)
                                                                                               [38] A. Falkowska, A. Seweryn, A. Tomczyk, Fatigue life and strength of 316L sin-
     195–203.
                                                                                                    tered steel of varying porosity, Int. J. Fatigue 111 (2018) 161–176.
[11] J.L. Schulthess, W.R. Lloyd, B. Rabin, et al., Mechanical properties of irradiated
                                                                                               [39] V. Vu, B. Tran, B. Le, et al., Prediction of the relationship between strength
     U-Mo alloy fuel, J. Nucl. Mater. 515 (2019) 91–106.
                                                                                                    and porosity of pervious concrete: a micromechanical investigation, Mech. Res.
[12] D.E. Burkes, A.M. Casella, A.J. Casella, et al., Thermal properties of U-Mo alloys
                                                                                                    Commun. 118 (2021) 103791.
     irradiated to moderate burnup and power, J. Nucl. Mater. 464 (2015) 331–341.


                                                                                          12
X. Jian, F. Yan, X. Kong et al.                                                                                                    Journal of Nuclear Materials 565 (2022) 153769


[40] D.E. Burkes, R. Prabhakaran, T. Hartmann, et al., Properties of DU-10wt% Mo            [46] J. Zhang, H. Wang, H. Wei, et al., Modelling of effective irradiation swelling for
     alloys subjected to various post-rolling heat treatments, Nucl. Eng. Des. 240               inert matrix fuels, Nucl. Eng. Technol. 53 (2021) 2616–2628.
     (2010) 1332–1339.                                                                      [47] D. Keiser, J. Jue, B. Miller, et al., Observed changes in as-fabricated U-10Mo
[41] P.G. Medvedev, H. Ozaltun, A.B. Robinson, et al., Shutdown-induced tensile                  monolithic fuel microstructures after irradiation in the advanced test reactor,
     stress in monolithic miniplates as a possible cause of plate pillowing at very              JOM 69 (2017) 2538–2545.
     high burnup, Nucl. Eng. Des. 328 (2018) 161–165.                                       [48] E.A.C. Neeft, K. Bakker, R.L. Belvroy, et al., Mechanical behaviour of macro-dis-
[42] S.L. Hayes, J.K. Thomas, K.L. Peddicord, Development of a creep rate porosity               persed inert matrix fuels, J. Nucl. Mater. 317 (2003) 217–225.
     correction factor, Mater. Lett. 9 (1990) 435–442.                                      [49] H. Ozaltun, M.H. Herman Shen, P. Medvedev, Assessment of residual stresses
[43] W. Dienst, Irradiation induced creep of ceramic nuclear fuels, J. Nucl. Mater.              on U10Mo alloy based monolithic mini-plates during hot isostatic pressing, J.
     65 (1977) 1–8.                                                                              Nucl. Mater. 419 (2011) 76–84.
[44] D.M. Perez, M.A. Lillo, G.S. Chang, et al. RERTR-9 Irradiation Summary Re-             [50] X. Jian, S. Ding, Thermal creep effects of aluminum alloy cladding on the ir-
     port. Idaho National Laboratory Report INL/EXT-10-18421, 2011. https://digital.             radiation-induced mechanical behavior in U–10Mo/Al monolithic fuel plates,
     library.unt.edu/ark:/67531/metadc833664/.                                                   Nucl. Eng. Technol. 52 (2020) 802–810.
[45] G.Y. Jeong, Y.S. Kim, L.M. Jamison, et al., Effect of stress evolution on mi-          [51] J. Rest, Y.S. Kim, G.L. Hofman, et al. U-Mo Fuels Handbook. Argonne National
     crostructural behavior in U-Mo/Al dispersion fuel, J. Nucl. Mater. 487 (2017)               Laboratory Report ANL-09/31, 2009. https://www.osti.gov/biblio/1335129.
     265–279.




                                                                                       13
