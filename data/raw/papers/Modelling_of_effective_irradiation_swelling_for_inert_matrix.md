# Modelling of effective irradiation swelling for inert matrix fuels

---

                                                           Nuclear Engineering and Technology 53 (2021) 2616e2628



                                                              Contents lists available at ScienceDirect


                                                Nuclear Engineering and Technology
                                                  journal homepage: www.elsevier.com/locate/net


Original Article

Modelling of effective irradiation swelling for inert matrix fuels
Jing Zhang a, Haoyu Wang b, Hongyang Wei a, b, Jingyu Zhang a, Changbing Tang b,
Chuan Lu b, Chunlan Huang b, Shurong Ding a, *, Yuanming Li b, **
a
    Institute of Mechanics and Computational Engineering, Department of Aeronautics and Astronautics, Fudan University, Shanghai, 200433, China
b
    Science and Technology on Reactor System Design Technology Laboratory, Nuclear Power Institute of China, Chengdu, 610213, China




a r t i c l e i n f o                                   a b s t r a c t

Article history:                                        The results of effective irradiation swelling in a wide range of burnup levels are numerically obtained for
Received 2 December 2020                                an inert matrix fuel, which are veriﬁed with DART model. The ﬁssion gas swelling of fuel particles is
Received in revised form                                calculated with a mechanistic model, which depends on the external hydrostatic pressure. Additionally,
14 February 2021
                                                        irradiation and thermal creep effects are included in the inert matrix. The effects of matrix creep strains,
Accepted 22 February 2021
                                                        external hydrostatic pressure and temperature on the effective irradiation swelling are investigated. The
Available online 28 February 2021
                                                        research results indicate that (1) the above effects are coupled with each other; (2) the matrix creep
                                                        effects at high temperatures should be involved; and (3) ranged from 0 to 300 MPa, a remarkable
Keywords:
Inert matrix fuel
                                                        dependence of external hydrostatic pressure can be found. Furthermore, an explicit multi-variable
Equivalent spherical model                              mathematic model is established for the effective irradiation swelling, as a function of particle volume
Effective irradiation swelling                          fraction, temperature, external hydrostatic pressure and fuel particle ﬁssion density, which can well
Hydrostatic pressure                                    reproduce the ﬁnite element results. The mathematic model for the current volume fraction of fuel
Irradiation and thermal creep                           particles can help establish other effective performance models.
                                                        © 2021 Korean Nuclear Society, Published by Elsevier Korea LLC. This is an open access article under the
                                                                                        CC BY-NC-ND license (http://creativecommons.org/licenses/by-nc-nd/4.0/).




1. Introduction                                                                            swelling is complex. The ﬁssion gas swelling is closely dependent
                                                                                           on the gas atom diffusion within the fuel grain. After a critical
   Inert matrix fuel elements are widely used in research and test                         ﬁssion density, grain recrystallization occurs, which accelerates
reactors [1,2], which also have a promising application prospect in                        ﬁssion gas swelling [14e18]. Moreover, the ﬁssion gas swelling is
advanced future nuclear reactors [3,4] and in the aspects of disposal                      affected by external hydrostatic pressure [19e22], so the irradiation
of nuclear wastes [5]. Simultaneously, different inert matrix com-                         and thermal creep strains [23e25] in the inert metal matrix have an
posite fuel pellets are proposed to burn plutonium and some other                          impact on the ﬁssion gas swelling of fuel particles, because the
minor actinides extracted from the spent fuels [6,7]. These inert                          creep relaxing effects will change the mechanical interactions be-
matrix fuel pellets are expected to be loaded in current light water                       tween the fuel particles and the matrix. It should be noted that the
reactors with extended burnup, because these composite fuels have                          irradiation swelling of fuel particles will contribute to the volu-
higher thermal conductivity than the traditional homogeneous UO2                           metric variations of composite fuel pellets, which will exert in-
and can reach high burnup [8e10]. Additionally, inert matrix fuels                         ﬂuences on the thermo-mechanical interactions [14,26] between
have shown good performances under transient conditions [7,11].                            the fuel pellets and the cladding. To better understand the
   In the extreme environments of nuclear reactors, the nuclear                            irradiation-induced thermo-mechanical behavior of inert matrix
fuel particles undergo irradiation swelling due to the accumulation                        fuel elements and implement optimized design, it is critical to
of solid and gaseous ﬁssion products [6,12,13]. The irradiation                            predict the effective irradiation swelling of inert matrix nuclear
swelling induced by solid ﬁssion products can be a linear function                         fuels. The effective irradiation swelling refers to the homogenized
of ﬁssion density [14]. However, the mechanism of ﬁssion gas                               swelling under the irradiation environments.
                                                                                               Owing to the fact that the irradiation experiments are time-
                                                                                           consuming with high cost and hard to be examined in situ, it is
                                                                                           very necessary to develop the theoretical models and numerical
  * Corresponding author.
                                                                                           simulation methods to obtain the effective irradiation swelling of
 ** Corresponding author.
     E-mail addresses: dingshurong@fudan.edu.cn (S. Ding), lym_npic@126.com                inert matrix fuels [27e29]. Inert matrix nuclear fuels tend to
(Y. Li).                                                                                   contain massive fuel particles [6,30], and it is difﬁcult to simulate

https://doi.org/10.1016/j.net.2021.02.019
1738-5733/© 2021 Korean Nuclear Society, Published by Elsevier Korea LLC. This is an open access article under the CC BY-NC-ND license (http://creativecommons.org/
licenses/by-nc-nd/4.0/).
J. Zhang, H. Wang, H. Wei et al.                                                                             Nuclear Engineering and Technology 53 (2021) 2616e2628


the irradiation-induced thermo-mechanical coupling behavior of a                     2.2. Veriﬁcations
whole fuel element or fuel assembly with the interactions between
the fuel particles and matrix involved. Thus, an effective way is to                 2.2.1. Veriﬁcation of the equivalent spherical model
homogenize the inert matrix fuels and study its effective properties                     The effective irradiation swelling of the considered inert matrix
[31e34]. Both the theoretical models and numerical methods have                      fuels can be obtained directly through the volumetric variation of
been performed to acquire the effective irradiation swelling of                      the ﬁnite element model. The effective irradiation swelling can be
some dispersion nuclear fuels [14,26,30,35,36]. DART model [26,36]                   expressed as
is an effective tool to calculate the effective irradiation swelling of
                                                                                                          3
Al-based dispersion nuclear fuels. But the creep and work hard-                      DV       V  V0       r
ening effects of the matrix were not explicitly taken into account,                       ¼          ¼        1                                               (1)
                                                                                     V0         V0        r0
and small-deformation assumption was performed [26]. Simulta-
neously, the intergranular gas atom resolution effect and the hy-                    where V is the post-irradiation spherical volume, V0 is the initial
drostatic pressure on the external surface of matrix due to the                      spherical volume, r is the post-irradiation outer spherical radius,
mechanical interactions inside matrix and among particles should                     r0 is the initial outer spherical radius, shown in Fig. 1.
be further incorporated.                                                                  The initial outer radius is known, which varies with the initial
    In this study, the modelling of effective irradiation swelling for               particle volume fraction. The ﬁssion density and the corresponding
PuO2/Zr inert matrix fuels [7,11] is implemented, with the obtained                  post-irradiation outer spherical radius can be obtained from the FE
ﬁssion gas swelling results of fuel particles validated, and the                     results. So, the effective irradiation swelling at different ﬁssion
effective irradiation swelling results veriﬁed with DART model.                      densities can be calculated.
Then, a multi-variable function for effective irradiation swelling is                     To ensure the computation precision and efﬁciency, the sensi-
developed. The ﬁnite element model includes the grain recrystal-                     tivity of mesh density is investigated ﬁrst for the ﬁnite element
lization of fuel particles and the external-hydrostatic-pressure                     model under the conditions that the initial particle volume fraction
dependence of particle ﬁssion gas swelling coupled with the ma-                      is 20%, the internal temperature is 573 K and the external pressure
trix creep effects. The effects of external hydrostatic pressure,                    is 0 MPa. Three mesh cases are considered, having 256, 3400 and
temperature and matrix creep on the effective irradiation swelling                   7267 elements respectively, as shown in Fig. 2. The obtained
are investigated.                                                                    effective volume swelling results are given in Fig. 3. The maximum
                                                                                     relative error of the results between Mesh2 and Mesh3 is 0.52%.
2. Finite element modelling                                                          Hence, results of effective irradiation swelling have converged with
                                                                                     Mesh 2, and therefore Mesh 2 is adopted in the following studies. It
   To obtain the effective irradiation swelling results of the                       is noted that the ﬁnite element results displayed in the following
considered inert matrix fuels under different conditions, ﬁnite                      are all tested to be converged.
element simulations are implemented with the commercial                                   Regarding the effective properties of the considered inert
software ABAQUS. In this section, the representative ﬁnite                           matrix fuels, cubic RVE models with different particle arrange-
element model will be presented, in which the mechanical                             ment were established in the previous study [30]. In order to
constitutive relations for the fuel particles and matrix are deﬁned                  verify the applicability of the developed equivalent spherical
with the user-deﬁned subroutines, based on the stress update                         model in this study, FE simulations for three cases with different
algorithms in our previous studies [27,37]. In the three-                            particle arrangements are also performed, including simple cubic
dimensional constitutive relation for the fuel particles, the total                  (SC), body-centered cubic (BCC) and face-centered cubic (FCC),
strains contain the contributions of elasticity, plasticity and irra-                and the particle radius of 0.05 mm is assumed to be the same for
diation swelling. The thermo-mechanical property models in                           each case. It can be observed from Fig. 4 that the FE results of
Refs. [12,16,17,34,38,39] are adopted in this study. The models of                   effective irradiation swelling for different models match well
elastic constants, plasticity and creep strain rate in Refs. [13,40]                 with each other, which demonstrates that the equivalent spher-
are taken into account for matrix.                                                   ical model can be used for calculating the effective irradiation
                                                                                     swelling for inert matrix fuels.
2.1. The ﬁnite element model

    Assuming that the PuO2 fuel particles are periodically distrib-
uted in a large matrix, an equivalent spherical model is considered                  2.2.2. Veriﬁcation of the swelling models
as the representative volume element (RVE), with a particle radius                       The ﬁssion gas swelling model of fuel particles is vitally
of 0.05 mm and a matrix shell. Since the RVE describes all the meso-                 important for calculating the effective irradiation swelling of inert
structure information of inert matrix fuels, the effective irradiation               matrix fuels. In order to validate the gas swelling model used in
swelling can be calculated by the ﬁnite element (FE) analysis via a                  this study, the obtained results are compared with experimental
RVE. Finally, 1/8 fraction of the RVE is selected as the ﬁnite element               results. As is known that in the reactor irradiation environments
model, allowing for the symmetry of RVE, shown as Fig. 1. Once the                   the UO2 pellets can form high burnup structure in the rim zone,
initial particle volume fraction fv0 is set, the initial outer radius r0 of          where grain recrystallization occurs [38]. In Fig. 5, the experi-
the equivalent spherical model can be calculated as shown in                         mental results for the rim-zone ﬁssion gas swelling [41e43] are
Table 1.                                                                             displayed.
    The symmetric boundary conditions are applied on the surfaces                        The external hydrostatic pressure on the rim zone surface is
of x ¼ 0, y ¼ 0 and z ¼ 0. The constant pressure condition is applied                relatively low. The corresponding temperature is about
to the outside of the equivalent sphere in consideration of the in-                  500 Ke900 K [41], and the as-fabricated grain size is about
ternal mechanical interactions of inert matrix fuels. A uniform,                     5mme15mm[44]. So the external hydrostatic pressure is set as zero,
steady-state temperature is assumed in the ﬁnite element model.                      the temperature as 800 K and the as-fabricated grain size as 7mm. In
The temperature is ranged from 473 K to 773 K. The ﬁssion rate in                    this study, with the external hydrostatic pressure considered, the
the fuel particle is set as 1  1020 ﬁssions/(m3$s) and the fast                     radius of intergranular bubbles is calculated with the Van der Waal
neutron ﬂux is set as 2.01568  1011 n/(mm2$s) in this study [27].                   gas equation [38,39], expressed as
                                                                              2617
J. Zhang, H. Wang, H. Wei et al.                                                                                            Nuclear Engineering and Technology 53 (2021) 2616e2628




                                                                        Fig. 1. The equivalent spherical model.



Table 1
Initial particle volume fraction and the equivalent spherical radius.

  Initial particle volume fraction   Initial outer radius of equivalent sphere/mm

  10%                                0.1077
  20%                                0.0855
  30%                                0.0747
  40%                                0.0679




                                   !
    2g            4pR3b
       þ Ph              hs bv Nb       ¼ Nb kT                                    (2)
    Rb             3

where, 2g=Rb is the bubble surface tension in Pa, Ph is the external
hydrostatic pressure in Pa, Rb is the radius of the intergranular
bubbles in m, hs is the ﬁtting parameter to make the Van der Waals
equation equivalent to the hard-sphere equation of state, bv is the
Van der Waal gas constant of Xe in m3, Nb is the average number of                                     Fig. 3. The sensitivity of effective irradiation swelling to the meshes.
gas atoms in each bubble, k ¼ 1.38  1023J/K is the boltzmann
constant and T is temperature in K. The above model parameters
can be found in Refs. [38,39].
                                                                                                 irradiation swelling of dispersion fuels, which takes into account
   The comparison between the obtained simulation results and
                                                                                                 the volumetric variation of inert matrix fuels from three aspects:
experimental results is shown in Fig. 5. It can be observed that the
                                                                                                 the contribution of matrix swelling induced by chemical reaction of
results in this study agree well with the experimental ones, which
                                                                                                 fuel particles with matrix, accumulation of ﬁssion products and
validate the gaseous swelling model used here. Furthermore, the
                                                                                                 irradiation-enhanced sintering.
obtained results for an external hydrostatic pressure of 50 MPa can
                                                                                                     For the considered inert matrix fuel in this study, there is no
be found in Fig. 5, and it can be known that hydrostatic pressure has
                                                                                                 occurrence of chemical reaction during irradiation. It should be also
a considerable effect on gaseous swelling, especially at high
                                                                                                 mentioned that the fuel particles are assumed to be dense, so the
burnup.
                                                                                                 irradiation-enhanced sintering effect is not considered here. Then,
   DART model [26,35,36] is a useful tool to calculate the effective




                                                                    Fig. 2. The models for three mesh cases.

                                                                                          2618
J. Zhang, H. Wang, H. Wei et al.                                                                                         Nuclear Engineering and Technology 53 (2021) 2616e2628




                                                                                              Fig. 6. The comparison of the results calculated according to DART model with the
                                                                                              obtained results in this study.
                Fig. 4. Comparison of FE results with different models.


                                                                                              the results with matrix creep effect match well with the results
                                                                                              from Eq. (3), respectively. It should be mentioned that the absolute
                                                                                              volume variation of particle in Eq. (3) is not directly obtained from
                                                                                              DART model. Meanwhile, it is demonstrated that our results satisfy
                                                                                              the basic relation of Eq. (3) in DART model. Additionally, the ﬁssion
                                                                                              gas swelling results of fuel particles are validated in this study, as
                                                                                              shown in Fig. 5. So, the effective treatment in this study can be
                                                                                              veriﬁed. Meanwhile, it can be obtained that it is necessary to
                                                                                              consider matrix creep effect because the results at ﬁssion density of
                                                                                              4.3  1027ﬁssions/m3 with matrix creep effect is about 13.3% higher
                                                                                              than the ones without matrix creep effect.

                                                                                              3. Inﬂuence factors on effective irradiation swelling

                                                                                              3.1. Effects of hydrostatic pressure

                                                                                                  During irradiation, there are mechanical interactions between
                                                                                              the fuel particles and matrix because of the particle irradiation
                                                                                              swelling. Thus, external forces exist at the outside of equivalent
                                                                                              sphere. The external forces will change with the ﬁssion density. It
Fig. 5. The comparison of the simulation results in this study with the experimental
                                                                                              can be known from Section 2.2.2 that the gaseous swelling is
results for the ﬁssion gas swelling of fuel particles.                                        affected by particle hydrostatic pressure. Therefore, the effective
                                                                                              swelling of inert matrix fuels is also affected by external hydrostatic
                                                                                              pressure. It should be noted that the effective irradiation swelling is
the effective swelling of DART model can be simpliﬁed as                                      dominated by the particle hydrostatic pressure Hpf (identical to Ph
                                                                                              in Eq. (2)) on the outside of fuel particles with the external pressure
DV       V  V0 DVf                                                                           applied on the matrix set as Hp, as depicted in Fig. 7.
     ¼         ¼                                                                (3)
V0         V0    V0                                                                               When the inert matrix fuel is homogenized, the mechanical
                                                                                              interaction between the fuel particles and matrix can't be taken
where, V is the post-irradiation total volume of inert matrix fuel, V0                        into account. So, the model of particle hydrostatic pressure Hpf
is the initial total volume of inert matrix fuel, DVf is the absolute                         should be studied. Then the model can be used to calculate the
volume variation of particle and DV represents the absolute volume                            ﬁssion gas swelling of fuel particles directly. The hydrostatic pres-
variation of inert matrix fuel.                                                               sure Hp0 is deﬁned as the particle hydrostatic pressure when the
    Based on Eq. (3), the effective irradiation swelling can be                               external hydrostatic pressure on the outside of equivalent sphere is
calculated utilizing the current particle volume obtained in this                             zero, as illustrated in Fig. 8. The particle hydrostatic pressure Hp0
study. Fig. 6 gives the results obtained according to Eq.(3) and the                          evolves with increasing ﬁssion density. Firstly, the simulation is
simulation results in this study, with the initial particle volume                            carried out under the condition that there is no pressure on the
fraction of 20%, the temperature of 700 K and the external hydro-                             external surface of matrix. During irradiation, the interaction be-
static pressure of 0 MPa. The simulation results with and without                             tween the fuel particle and matrix happens because of particle
matrix creep effect are simultaneously displayed in Fig. 6. The ef-                           irradiation swelling, and the fuel particle is subjected to a hydro-
fects of irradiation hardening and strain hardening effects in the                            static pressure of Hp0, which can be determined by the FE compu-
matrix plasticity model are both considered in the simulations. One                           tation. Fig. 9 depicts the calculation results of hydrostatic pressure
can see that the simulation results without matrix creep effect and                           Hp0 at different temperatures and different initial particle volume
                                                                                       2619
J. Zhang, H. Wang, H. Wei et al.                                                                                             Nuclear Engineering and Technology 53 (2021) 2616e2628




                                                          Fig. 7. The hydrostatic pressure Hpf on a fuel particle surface.




                                                         Fig. 8. The hydrostatic pressure Hp0 on a fuel particle surface.




Fig. 9. The FEM results and ﬁtted results of hydrostatic pressure Hp0 as a function of
                                                                                                Fig. 10. The particle hydrostatic pressures Hpf under different external hydrostatic
temperature and initial particle volume fraction at the certain ﬁssion density of
                                                                                                pressures.
6  1027ﬁssions/m3.


                                                                                                the external surface of the matrix, the particle hydrostatic pressures
fractions. It can be found that Hp0 at the certain ﬁssion density of
                                                                                                of Hpf at different ﬁssion densities have been obtained by FE cal-
6  1027ﬁssions/m3 gradually decreases with the increase of tem-
                                                                                                culations, as depicted in Fig. 10. The considered initial particle
perature and initial particle volume fraction. When the tempera-
                                                                                                volume fraction is 20% and the temperature is 573 K. One can
ture is higher than 573 K, the hydrostatic pressure Hp0 drops
                                                                                                observe that the particle hydrostatic pressure will increase from
sharply. When the temperature is higher than 673 K, the hydro-
                                                                                                zero to a stable value at the ﬁssion density of 1  1027ﬁssions/m3,
static pressure keeps decreasing at yet a much slower rate. These
                                                                                                after which the pressure magnitudes vary slightly. The stable value
evolution traits are related to the creep effects in the matrix, as
                                                                                                of hydrostatic pressure Hp0 is ~400 MPa. It should be indicated that
analyzed in Section 3.3.
                                                                                                the results in Fig. 9 represent the stable values under different
   When different hydrostatic pressure levels of Hp is applied on
                                                                                                conditions. Besides, the stable results of hydrostatic pressures Hpf

                                                                                         2620
J. Zhang, H. Wang, H. Wei et al.                                                                                          Nuclear Engineering and Technology 53 (2021) 2616e2628


are approximately equal to the sum of Hp0 and Hp, namely as Eq. (4),                                Under the condition that the initial particle volume fraction is
which is also true for all the cases in this study.                                             20%, it can be found from Fig. 9 that the stable hydrostatic pressure
                                                                                                Hp0 at 573 K and 673 K are about 430 MPa and 85 MPa respectively.
                                                                                                So, the stable particle hydrostatic pressures Hpf at 573 K for
Hpf z Hp þ Hp0                                                                     (4)
                                                                                                Hp ¼ 200 MPa and 673 K for Hp ¼ 300 MPa will become 630 MPa
    One can know that the external hydrostatic pressure Hp will                                 and 385 MPa. Because the ﬁssion gas swelling of fuel particles will
inﬂuence the particle hydrostatic pressure Hpf. As a result, the                                be hardly lessened by the particle hydrostatic pressure Hpf when its
ﬁssion gas swelling of fuel particles and also the effective irradia-                           magnitude exceeds 300 MPa, the phenomena in Fig. 11 can be
tion swelling will be affected by Hp. In a nuclear reactor, the                                 explained.
external hydrostatic pressures (the hydrostatic pressures for the                                   Simultaneously, one can see from Fig. 11 that the effective
homogenized pellets) in inert matrix fuels change continuously                                  irradiation swelling values are close to each other for all the cases at
with the internal interactions within the inert matrix fuel parts and                           the ﬁssion density lower than 2  1027ﬁssions/m3, which indicates
the interactions between the fuel pellet/meat and the cladding. So,                             that the ﬁssion gas swelling of fuel particle will play an important
the effective irradiation swelling under different external hydro-                              role at higher ﬁssion densities. Thus, the ﬁssion gas swelling of fuel
static pressures should be investigated. The results of effective                               particles only depends on the stable value of particle hydrostatic
irradiation swelling under different external hydrostatic pressures                             pressure. When the stable particle external pressure Hp0 is deter-
Hp are shown in Fig. 11, respectively for two temperature cases of                              mined, the magnitudes of Hpf can be calculated by Eq. (4). The stable
573 K and 673 K. The initial particle volume fractions are all                                  hydrostatic pressure Hp0 is dominantly dependent on the variables
considered as 20%.                                                                              of temperature and initial particle volume fraction, whose func-
    By comparing Fig. 11(a) and (b), it can be seen that the effective                          tional relations are ﬁtted, given as



                                                                                  
        8
         0:0625fv0 2 þ 0:04775fv0  0:01237 T 2 þ 54:375fv0 2  39:4865fv0 þ 9:54425 T
        >
        >                                                    
        >
        >
        >
        < þ  7686:3125fv0 2 þ 4371:05475fv0  618:28387          ; 473K  T < 673K
Hp0 ¼                                                                                                                                                                   (5)
     >
     >
     >
     >  0:015fv0 2  0:0209fv0 þ 0:00905 T 2 þ  27:44fv0 2 þ 34:9264fv0  14:3988 T
     >
     :                                                     
          þ 12323:185fv0 2  14618:2511fv0 þ 5767:38495         ; 673K  T < 773K




irradiation swelling decreases more slightly with the external hy-                              where, Hp0 is in MPa, fv0 is the initial particle volume fraction and T
drostatic pressure in Fig. 11(a). When temperature is 573 K, the                                is temperature in K.
effective irradiation swelling for the case of Hp ¼ 200 MPa is 4.07%                                The comparisons of calculation results with the ﬁtting results for
lower than that for Hp ¼ 0 MPa at the ﬁssion density of 1.47  1028                             the cases with different initial particle volume fractions and
ﬁssions/m3. Meanwhile, the effective irradiation swelling decreases                             different temperatures are also exhibited in Fig. 9. The maximum
signiﬁcantly with the increase of external pressure until the                                   difference between the ﬁtting results and the calculated results is
external hydrostatic pressure reaches 200 MPa in Fig. 11(b).                                    50 MPa, and the maximum relative error is about 7%. The error is
Compared to the case of Hp ¼ 0, the effective irradiation swelling for                          within the acceptable range, since the effective irradiation swelling
Hp ¼ 200 MPa is reduced by ~15.77% at the ﬁssion density of                                     is not very sensitive to the particle hydrostatic pressure, especially
1.47  1028 ﬁssions/m3. Afterwards, the effective irradiation                                   at high pressure levels.
swelling decreases slowly after the external hydrostatic pressure
exceeds 200 MPa. Compared to the case of Hp ¼ 200 MPa, the
                                                                                                3.2. Effects of temperature
effective irradiation swelling for Hp ¼ 300 MPa is only ~3.54% lower
at the ﬁssion density of 1.47  1028 ﬁssions/m3.
                                                                                                   In a nuclear reactor core, the temperatures of fuel particles vary




                          Fig. 11. The effective irradiation swelling under different external hydrostatic pressures Hp at (a) T ¼ 573 K and (b) T ¼ 673 K.

                                                                                         2621
J. Zhang, H. Wang, H. Wei et al.                                                                                 Nuclear Engineering and Technology 53 (2021) 2616e2628


                                                                                          magnitudes occur near the particle/matrix interface because the
                                                                                          intensive particle/matrix interaction takes place here. From
                                                                                          Fig. 13(a)e(d), it can be found that the effective creep strains in-
                                                                                          crease with temperature. The maximum strain at 473 K is 0.044,
                                                                                          while the maximum value at 773 K is 0.341, which increases by
                                                                                          674.4%.
                                                                                              The creep strains of the matrix will relieve the stresses of the
                                                                                          matrix, and also affect the interaction between the matrix and
                                                                                          particle. Thereby, it will affect the particle hydrostatic pressure and
                                                                                          the ﬁssion gas swelling of fuel particles. Fig. 14 compares the results
                                                                                          of hydrostatic pressure Hp0 at different temperatures for the cases
                                                                                          with and without considering matrix creep. At 473 K, the effect of
                                                                                          matrix creep is weak, and the differences of Hp0 is slight. As the
                                                                                          temperature increases, the differences become more distinct. At
                                                                                          773 K, Hp0 is reduced by 92.6% with creep considered, compared to
                                                                                          the no creep case. It can also be found that Hp0 sharply decreases
                                                                                          from 573 K to 673 K for the case with creep considered, on account
                                                                                          of the creep strains of matrix which is enhanced obviously with the
                                                                                          temperature in this range so that the stresses of the matrix are
                                                                                          lessened.
       Fig. 12. The effective irradiation swelling under different temperatures.              Fig. 15 compares the effective irradiation swelling at different
                                                                                          temperatures for the cases with and without considering matrix
with their locations and irradiation conditions. The effective irra-                      creep. The results at 473 K and 573 K are close to each other,
diation swelling of the considered inert matrix fuels also give a rise                    because the creep effect is weak at these two temperatures and Hp0
with temperature, as can be found in Section 3.1. Thus, the effects of                    are similar with each other, as can be seen from Fig. 14. The effective
irradiation temperature on the effective irradiation swelling should                      irradiation swelling results with creep are larger than those
be investigated in detail. Fig. 12 displays the effective irradiation                     without creep at 673 K, and the maximum relative difference is
swelling results at different temperatures. The external hydrostatic                      9.24%. The effective irradiation swelling with creep at 773 K in-
pressure is set as100 MPa and the initial particle volume fraction is                     creases by 15.34% at the considered maximum ﬁssion density than
designated as 20%.                                                                        the one without creep. The variations of effective irradiation
    From 473 K to 573 K, the effective irradiation swelling increases                     swelling are consistent with the particle hydrostatic pressures in
slightly, because the temperature is relatively low and the particle                      Fig. 14.
hydrostatic pressure Hpf is high. From 573 K to 673 K, the effective                          It can be known that the matrix creep can cause stress relaxation
irradiation swelling increases more signiﬁcantly. This results from                       and affect the effective irradiation swelling of the considered inert
the sharp decrease of particle hydrostatic pressure, which is caused                      matrix fuels, especially under high temperatures and high ﬁssion
by the matrix creep. When the temperature is higher, the matrix                           densities. It can be concluded that the matrix creep needs to be
creep will be larger, and the stress relaxation effect will be                            considered in developing effective irradiation swelling model, so
enhanced. From 673 K to 773 K, the effective irradiation swelling                         that the obtained model can be used for an arbitrary, steady-state
continues to rise up because of further decrease of particle hydro-                       case.
static pressure. It should be noted that the results in Fig. 12 are                           The results of matrix shell thickness with and without creep
obtained with an assumption of constant external hydrostatic                              contribution are compared in Fig. 16(a). With the enhancement of
pressure Hp. If Hp is also lowered, the effective irradiation swelling                    creep effect, the matrix shell thickness becomes smaller, and the
will be correspondingly enlarged.                                                         maximum difference between the results with and without the
    It can also be seen that the effective irradiation swelling accel-                    creep contribution is about 2.82% at 773 K. It can be observed that
erates after the critical ﬁssion density of grain recrystallization.                      the matrix shell thickness all decrease with the ﬁssion density. It
With the increase of ﬁssion density, the coupling effects of hydro-                       should be mentioned that the deformations of the matrix are
static pressure and temperature appear more signiﬁcantly. The                             mainly induced by the plasticity strains for the case without creep.
evolution phenomenon of effective irradiation swelling under                              Because the stress of matrix is larger without the stress relaxing
different temperatures is also consistent with the evolution of                           effects of creep, which induces the occurring of plasticity strain.
intergranular bubble radius revealed by Eq. (2).                                          From Fig. 16(b), one can ﬁnd that the volume of the matrix remains
                                                                                          the same, because the deformations of plasticity and creep will
3.3. Effects of matrix creep                                                              make no contributions to the volumetric variations.

    The ﬁssion product induced swelling leads to the stress and                           3.4. Fitting models for effective irradiation swelling and current
deformation in the matrix. The resultant creep strains in the matrix                      particle volume fraction
will also result in its stress evolutions, simultaneously affect the
mechanical interactions between the fuel particles and the matrix.                           As mentioned previously, the effective irradiation swelling is
Hence, the ﬁssion gas swelling of fuel particles tends to be                              deﬁned as the ratio of the absolute volume variation to the initial
increased.                                                                                volume of the ﬁnite element model. In fact, the absolute volume
    Fig. 13 gives the effective creep strain results of matrix at                         variation consists of two contributions from the matrix and fuel
different temperatures at the ﬁssion density of 1.47  1028 ﬁssions/                      particle, as depicted in Fig. 17. One can ﬁnd that the effective irra-
m3. For all the cases, the external hydrostatic pressure is set as                        diation swelling is dominated by the contribution from the fuel
100 MPa and the initial particle volume fraction is equal to the same                     particle. Especially, when the ﬁssion density is greater than
value of 20%. It can be seen that the effective creep strains gradually                   ~3  1027ﬁssions/m3, the contribution ratio of the fuel particle
decrease from the inside to the outside of matrix. The maximum                            reaches almost 100%. It is noted that the results in Fig. 17 are
                                                                                   2622
J. Zhang, H. Wang, H. Wei et al.                                                                                          Nuclear Engineering and Technology 53 (2021) 2616e2628




                       Fig. 13. The effective creep strain contour plots of matrix at different temperatures at the ﬁssion density of 1.47  1028 ﬁssions/m3.



                                                                                              matrix volume variation despite their effects on the particle volume
                                                                                              increase.
                                                                                                 So, the effective irradiation swelling of the considered inert
                                                                                              matrix fuels can be calculated as

                                                                                              DV       Vf  Vf 0 Vf 0 Vf  Vf 0
                                                                                                   ¼            ¼                                                           (6)
                                                                                              V0          V0      V0     Vf 0

                                                                                              where Vf is the post-irradiation particle volume in the ﬁnite
                                                                                              element model, Vf0 is the initial particle volume, V0 is the initial
                                                                                              total volume of the ﬁnite element model, and DV represent the
                                                                                              absolute volume variation of the ﬁnite element model. Eq. (6) can
                                                                                              also be expressed as

                                                                                              DV           DVf
                                                                                                   ¼ fv0                                                                    (7)
                                                                                              V0           Vf 0

                                                                                              where fv0 is the initial particle volume fraction, and DVf is the ab-
                                                                                              solute volume variation of the fuel particle part in the ﬁnite
Fig. 14. Hydrostatic pressure Hp0 under the condition of with and without matrix
                                                                                              element model, andDVf =Vf 0 is the irradiation swelling of fuel par-
creep considered.
                                                                                              ticle.DVf =Vf 0 mainly results from the ﬁssion gas swelling and
                                                                                              ﬁssion solid swelling, which can be outputted with the state vari-
obtained for the case with the initial particle volume fraction of                            ables in the ﬁnite element simulations.
20%, the temperature of 473 K and the external hydrostatic pressure                               Fig. 18(a)e(c) depict the comparison of the effective irradiation
of 100 MPa. For the other investigated cases, the effective irradia-                          swelling results obtained by Eq. (1) with the ones calculated by Eq.
tion swelling also originates from the contribution of fuel particles,                        (7) under different conditions. The results agree well with each
because the deformations of plasticity and creep will result in no                            other. It indicates that the effective irradiation swelling satisﬁes Eq.
                                                                                              (7). Once the fuel particle swelling is known, the effective swelling




                                                                                       2623
J. Zhang, H. Wang, H. Wei et al.                                                                                             Nuclear Engineering and Technology 53 (2021) 2616e2628




                              Fig. 15. The comparison of effective irradiation swelling at different temperatures with and without creep considered.




    Fig. 16. (a) The comparison of matrix shell thickness with and without creep considered and (b) the volume of matrix with creep considered at different temperatures.



                                                                                             matrix nuclear fuels, as long as the contribution of the matrix
                                                                                             volume variation can be neglected.
                                                                                                 The effective irradiation swelling is intensively related to the
                                                                                             irradiation swelling of fuel particles. In this study, a ﬁtting mathe-
                                                                                             matical model for the irradiation swelling of PuO2 fuel particles is
                                                                                             also developed. The total irradiation swelling of fuel particles in-
                                                                                             cludes the ﬁssion solid and gas swelling, described as

                                                                                                                   !              !
                                                                                             DVf            DVf            DVf
                                                                                                    ¼                  þ                                                       (8)
                                                                                             Vf 0           Vf 0           Vf 0
                                                                                                                   s              g

                                                                                                The ﬁssion solid swelling is proportional to ﬁssion density and
                                                                                             can be calculated as

                                                                                                      !
                                                                                              DVf
                                                                                                            ¼ 2:5  1029 $Fd                                                  (9)
                                                                                               Vf 0
                                                                                                        s

                                                                                             where, Fd depicts the ﬁssion density in ﬁssions/m3.
            Fig. 17. The proportion of particle and matrix volume change.                       Importantly, a multi-variable coupling model for the ﬁssion gas
can be obtained. It can also be known that Eq. (7) can be used to                            swelling of PuO2 fuel particles is obtained as a function of external
calculate the effective irradiation swelling of many kinds of inert                          hydrostatic pressure, temperature, initial particle volume fraction
                                                                                             and ﬁssion density, expressed as
                                                                                      2624
J. Zhang, H. Wang, H. Wei et al.                                                                                          Nuclear Engineering and Technology 53 (2021) 2616e2628




                    "                                                      #
                           7      2          4
                  8 2  10  Hpf  1:3  10  Hpf þ 0:034  ðT  473Þ þ 1 
                  >
                  >                     50
                  >
                  >
                  >
                  > h                                              
                  >
                  >
                  >
                  >
                  >   9:17914  1030 þ 3:81476  1030  0:99099Hpf  Fd
                  >
                  >
                  >
                  >                               i
                  >
                  >
         !        >
                  > 0:00152  0:0011  0:98876Hpf                 Fd  Fdx
                  >
                  <
  DVf
              ¼                                                                                                                                                                (10)
  Vf 0            >
                  >
                  > "                                                             #
          g       >
                  >
                  >    2  107  Hpf 2  1:3  104  Hpf þ 0:034
                  >
                  >                                                   ðT  473Þ þ 1 
                  >
                  >                         25
                  >
                  >
                  >
                  > h                                                   
                  >
                  >
                  >
                  >   1:64365  1029 þ 1:55406  1029  0:99073Hpf  Fd
                  >
                  >
                  :
                                                     i
                    0:00544  0:02763  0:98794Hpf                   Fd > Fdx




where, Hpf is the particle hydrostatic pressure in MPa, with                                  thermal-mechanical behavior in homogenized fuel pellets; T is the
Hpf ¼ Hp0 þHp, and Hp denotes the external hydrostatic pressure,                              temperature in K, Fd is ﬁssion density in ﬁssions/m3. The critical
namely the hydrostatic pressure obtained from calculation of the                              ﬁssion density is dependent on ﬁssion rate, which can be described




Fig. 18. Veriﬁcation of the effective irradiation swelling under (a) external hydrostatic pressure HP ¼ 100 MPa, (b) different temperatures and (c) different initial particle volume
fractions.

                                                                                       2625
J. Zhang, H. Wang, H. Wei et al.                                                                                             Nuclear Engineering and Technology 53 (2021) 2616e2628




Fig. 19. Veriﬁcation of the ﬁtting mathematical model for the ﬁssion gas swelling of PuO2 particles under (a) different temperatures and (b) different particle hydrostatic pressures.



asFdx ¼ 4  1024 ðf_Þ2=15 .f_ is the ﬁssion rate in ﬁssions/(m3s).                            other effective thermo-mechanical performances, such as the
    In fact, the contribution of matrix creep is also implicitly                               effective thermal conductivity, it is necessary to obtain the math-
involved, which relies on the temperature, the ﬁssion density, the                             ematical model for the current volume fraction of inert matrix
external hydrostatic pressure et al. and is coupled with the irradi-                           fuels. According to the deﬁnition of particle volume fraction, with
ation swelling of fuel particles. The comparison of ﬁnite element                              the irradiation swelling of fuel particles known, the current particle
calculation results and ﬁtting model results for the ﬁssion gas                                volume fraction can be obtained as
swelling of PuO2 fuel particles under different temperatures and                                                            !
different particle hydrostatic pressures are shown in Fig. 19. One                                                     DV
                                                                                                           fv0 1 þ Vf 0f
can conclude that the ﬁtting model results match well with the                                        Vf
computation ones on the whole. When the ﬁssion density of fuel                                 fv ¼      ¼          DV
                                                                                                                                                                                (11)
                                                                                                      V    1 þ fv0 $ Vf 0f
particles is near the critical ﬁssion density, the relative error can
reach 10%. The relative error is below 5% at higher ﬁssion densities.
                                                                                                                                                                  DV
As mentioned in the previous section, the contribution of ﬁssion                               where fv0 is the initial particle volume fraction and Vf 0f is the irra-
gas swelling of fuel particles is remarkable at high ﬁssion densities.                         diation swelling of fuel particles. The update particle volume Vf can
Consequently, the ﬁtting mathematical model is acceptable.                                     be calculated as
    Once the basic inﬂuencing variables are known, the irradiation
                                                                                                                   !
swelling of fuel particles in the considered inert matrix fuels can be                                   DVf
quickly calculated by the ﬁtting mathematical model. Subsequently,                             Vf ¼             þ 1 Vf 0                                                        (12)
                                                                                                         Vf 0
the effective irradiation swelling can be obtained according to Eq.
(7).                                                                                              Similarly, the current fuel volume V can be obtained as
    Apparently, the current volume fraction of fuel particles will                                                     !                     !
change with the increase of ﬁssion density. In order to obtain the                                         DVf                     DVf           Vf 0
                                                                                               V ¼ fv0            þ 1 V0 ¼ fv0             þ1                                   (13)
                                                                                                           Vf 0                     Vf 0         fv0

                                                                                                   which depends on the irradiation swelling of fuel particles, and
                                                                                               the initial particle volume and volume fraction.
                                                                                                   To ensure the correctness of Eq. (11), the ﬁnite element calcu-
                                                                                               lation results and the results calculated by the formula under the
                                                                                               temperature of 573 K, the initial particle volume fraction of 20%,
                                                                                               and the matrix external pressure Hp of 0 MPa are plotted in Fig. 20.
                                                                                               One can ﬁnd that the results obtained by two routes are in good
                                                                                               agreement, which indicates that Eq. (11) can be used to update the
                                                                                               particle volume fraction.


                                                                                               4. Conclusions

                                                                                                  In this study, a ﬁtting mathematic model for the effective irra-
                                                                                               diation swelling is developed, and a model of current particle vol-
                                                                                               ume fraction is also proposed, which is veriﬁed with the ﬁnite
                                                                                               element results. The effective irradiation swelling of the considered
                                                                                               inert matrix fuels is demonstrated to depend mainly on the irra-
                                                                                               diation swelling of fuel particles, as long as the contribution of
           Fig. 20. Veriﬁcation of current particle volume fraction formula.                   matrix volume variation can be neglected. The gaseous swelling
                                                                                        2626
J. Zhang, H. Wang, H. Wei et al.                                                                                          Nuclear Engineering and Technology 53 (2021) 2616e2628


model of fuel particle and FE model results of effective irradiation                           [6] L.V. Duyn, Evaluation of the Mechanical Behavior of a Metal Matrix Dispersion
                                                                                                   Fuel for Plutonium Burning, Georgia Institute of Technology: A thesis for the
swelling are veriﬁed through making comparison with experi-
                                                                                                   Degree Master of Science in Mechanical Engineering, 2003.
mental results and DART model. Through ﬁnite element analysis,                                 [7] A. Savchenko, L. Konovalov, A. Vatulin, A. Morozov, V. Orlov, O. Uferov,
the effects of external hydrostatic pressure, temperature and ma-                                  S. Ershov, A. Laushkin, G. Kulakov, S. Maranchak, Z. Petrova, Dispersion type
trix creep on the effective irradiation swelling are investigated. The                             zirconium matrix fuels fabricated by capillary impregnation method, J. Nucl.
                                                                                                   Mater. 362 (2e3) (2007) 356e363.
conclusions can be drawn as follows.                                                           [8] A.M. Savchenko, A.V. Vatulin, A.V. Morozov, et al., Inert matrix fuel in
                                                                                                   dispersion type fuel elements, J. Nucl. Mater. 352 (1e3) (2006) 372e377.
   (1) The effective irradiation swelling of the considered inert                              [9] E.A.C. Neeft, K. Bakker, R.P.C. Schram, et al., The EFTTRA-T3 irradiation
                                                                                                   experiment on inert matrix fuels, J. Nucl. Mater. 320 (1e2) (2003) 106e116.
       matrix fuels decreases with the increase of external hydro-                            [10] A.M. Savchenko, I.I. Konovalov, A.V. Vatulin, E.M. Glagovsky, New concept of
       static pressure, which is dominantly inﬂuenced when the                                     designing Pu and MA containing fuel for fast reactors, J. Nucl. Mater. 385 (1)
       particle hydrostatic pressure is lower than 300 MPa. This is                                (2009) 148e152.
                                                                                              [11] A.M. Savchenko, A.V. Vatulin, E.M. Glagovsky, I.I. Konovalov, A.V. Morozov,
       attributed to the fact that the intergranular bubble radius                                 A.V. Kozlov, S.A. Ershov, V.A. Mishunin, G.V. Kulakov, V.I. Sorokin,
       depends on the particle hydrostatic pressure. For the con-                                  A.P. Simonov, Z.N. Petrova, V.V. Fedotov, Main results of the development of
       ditions with the initial particle volume fraction of 20%, the                               dispersion type IMF at A.A. Bochvar Institute, J. Nucl. Mater. 396 (1) (2010)
                                                                                                   26e31.
       temperature of 673 K and the ﬁssion density of 1.47  1028                             [12] M. Suzuki H S, Light water reactor fuel analysis code, 2005. FEMAXI-6 (Ver.1)
       ﬁssions/m3, the results indicate that the effective irradiation                             [Z].
       swelling for particle hydrostatic pressure of 285 MPa is                               [13] A. MATPRO, Handbook of Materials Properties for Use in the Analysis of Light
                                                                                                   Water Reactor Fuel Rod Behavior, 1978.
       reduced by ~15.77% compared to the case of 85 MPa.
                                                                                              [14] Y.S. Kim, G.Y. Jeong, J.M. Park, A.B. Robinson, Fission induced swelling of UMo/
   (2) The effective irradiation swelling of the considered inert                                  Al dispersion fuel, J. Nucl. Mater. 465 (2015) 142e152.
       matrix fuels increases with temperature. From 573 K to                                 [15] Y.M. Zhao, J.Y. Zhang, S.R. Ding, A new method for solving the ﬁssion gas
       673 K, the effective swelling increases by~10.9% at the ﬁssion                              diffusion equations with time varying diffusion coefﬁcient and source term
                                                                                                   considering recrystallization of fuel grains, Nuclear Materials and Energy 20
       density of 1.47  1028 ﬁssions/m3 under the condition that                                  (2019) 100686.
       the external hydrostatic pressure is 100 MPa and the initial                           [16] J. Rest, A model for ﬁssion-gas-bubble behavior in amorphous uranium sili-
       particle volume fraction is 20%. The contribution from the                                  cide compounds, J. Nucl. Mater. 325 (2e3) (2004) 107e117.
                                                                                              [17] J. Rest, Application of a mechanistic model for radiation-induced amorph-
       intergranular bubble radius will be enlarged at higher tem-                                 ization and crystallization of uranium silicide to recrystallization of UO2,
       peratures. Simultaneously, the enhanced matrix creep                                        J. Nucl. Mater. 248 (1997) 180e184.
       lessens the particle hydrostatic pressure.                                             [18] A. Leenaers, W. Van Renterghem, S. Van den Berghe, High burn-up structure
                                                                                                   of U(Mo) dispersion fuel, J. Nucl. Mater. 476 (2016) 218e230.
   (3) The matrix creep can reduce the mechanical interaction be-                             [19] Y. Cui, S.R. Ding, Z.T. Chen, Y.Z. Huo, Modiﬁcations and applications of the
       tween the matrix and fuel particles, and the weakened                                       mechanistic gaseous swelling model for UMo fuel[J], J. Nucl. Mater. 457 (2015)
       constraint effect accelerates the ﬁssion gas swelling of fuel                               157e164.
                                                                                              [20] X. Tian, X.Z. Kong, F. Yan, S.R. Ding, Hydrostatic pressure effect of ﬁssion gas
       particles. The matrix shell thickness decreases, and its                                    swelling in UMo/Al dispersion fuel plate, Atomic Energy Sci. Technol. 51 (11)
       circumference size increases to accommodate the enlarged                                    (2017) 2062e2068.
       fuel particle, but the matrix volume remains the same. The                             [21] Y.B. Miao, A. Kyle, David Andersson Gamble, et al., Gaseous swelling of U3Si2
                                                                                                   during steady-state LWR operation: a rate theory investigation, Nucl. Eng.
       effect of creep on the effective irradiation swelling can be
                                                                                                   Des. 322 (2017) 336e344.
       enhanced, which is induced by its coupling correlations with                           [22] M.C. Paraschiv, A. Paraschiv, V.V. Grecu, On the nuclear oxide fuel densiﬁca-
       the temperature and the hydrostatic pressure within fuel                                    tion, swelling and thermal re-sintering, J. Nucl. Mater. 302 (2) (2002)
       particles.                                                                                  109e124.
                                                                                              [23] Y.S. Kim, G.L. Hofman, J.S. Cheon, A.B. Robinson, D.M. Wachs, Fission induced
                                                                                                   swelling and creep of UeMo alloy fuel, J. Nucl. Mater. 437 (1e3) (2013)
Declaration of competing interest                                                                  37e46.
                                                                                              [24] G.Y. Jeong, Y.S. Kim, D. Sohn, Mechanical analysis of UMo/Al dispersion fuel,
                                                                                                   J. Nucl. Mater. 466 (2015) 509e521.
   The authors declare that they have no known competing                                      [25] Z.H. Xing, S.H. Ying, Study on the irradiation swelling of U3Si2-Al dispersion
ﬁnancial interests or personal relationships that could have                                       fuel, Atomic Energy Sci. Technol. 35 (1) (2001) 15e19.
appeared to inﬂuence the work reported in this paper.                                         [26] J. Rest, et al., The DART Dispersion Analysis Research Tool: A Mechanistic
                                                                                                   Model for Predicting Fission-Product-Induced Swelling of Aluminum Disper-
                                                                                                   sion Fuels, Argonne National Laboratory, 1995.
Acknowledgement                                                                               [27] X. Gong, Y.M. Zhao, S.R. Ding, A new method to simulate the micro-thermo-
                                                                                                   mechanical behaviors evolution in dispersion nuclear fuel elements, Mech.
                                                                                                   Mater. 77 (2014) 14e27.
   The authors are very grateful for the supports of National Nat-                            [28] Q.M. Wang, X.Q. Yan, S.R. Ding, Y.Z. HUO, Research on the interfacial behaviors
ural Science Foundation of China (No. 11772095), the support of the                                of plate-type dispersion nuclear fuel elements, J. Nucl. Mater. 399 (1) (2010)
National Key Research and Development Program of China                                             41e54.
                                                                                              [29] Q.M. Wang, Y. Cui, S.R. Ding, Y.Z. HUO, Simulation of the coupling behaviors of
(2016YFB0700103) and the supports of the foundation from Sci-                                      particle and matrix irradiation swelling and cladding irradiation growth of
ence and Technology on Reactor System Design Technology                                            plate-type dispersion nuclear fuel elements, Mech. Mater. 43 (4) (2011)
Laboratory.                                                                                        222e241.
                                                                                              [30] W. CAI, Y.M. ZHAO, X. GONG, S.R. DING, Y.Z. HUO, Calculation simulation of
                                                                                                   equivalent irradiation swelling for dispersion nuclear fuel, Atomic Energy Sci.
References                                                                                         Technol. 49 (3) (2015) 502e510.
                                                                                              [31] Y.M. Zhao, X. Gong, S.R. Ding, Y.Z. Huo, A numerical method for simulating the
 [1] A.N. Holden, Dispersion Fuel Elements, Gordon and Breach Science Publishers                   non-homogeneous irradiation effects in full-sized dispersion nuclear fuel
     Inc, New York, 1967.                                                                          plates, Int. J. Mech. Sci. 81 (2014) 174e183.
 [2] J.L. Kloosterman, P.M.G. Damen, Reactor physics aspects of plutonium burning             [32] M.L. Liu, Y.H. Lee, Dasari V. Rao, Development of effective thermal conduc-
     in inert matrix fuels, J. Nucl. Mater. 274 (1999) 112e119.                                    tivity model for particle-type nuclear fuels randomly distributed in a matrix,
 [3] C. Lombardi, L. Luzzi, E. Padovani, et al., Thoria and inert matrix fuels for a               J. Nucl. Mater. 508 (2018) 168e180.
     sustainable nuclear power, Prog. Nucl. Energy 50 (8) (2008) 944e953.                     [33] Z. Hashin, Analysis of composite materials-a survey, Appl. Mech 50 (1983)
 [4] W.J. Carmack, M. Todosow, M.K. Meyer, K.O. Pasamehmetoglu, Inert matrix                       481e505.
     fuel neutronic, thermal-hydraulic, and transient behavior in a light water               [34] P S. In Sanchez-Palencia E Z A E. Homogenization Techniques for Composites
     reactor, J. Nucl. Mater. 352 (2006) 276e284.                                                  Media, Springer-Verlag, Berlin, 1987.
 [5] Xin Gong, Shurong Ding, Yunmei Zhao, Yongzhong Huo, Lin Zhang,                           [35] J. Rest, DART model for irradiation-induced swelling of uranium silicide
     Yuanming Li, Effects of irradiation hardening and creep on the thermo-                        dispersion, Fuel Elements 126 (1998) 88e101.
     mechanical behaviors in inert matrix fuel elements, Mech. Mater. 65 (2013)               [36] B. Ye, J. Rest, A Description of the Mechanistic DART-THERMAL Dispersion
     110e123.                                                                                      Fuel Performance Code and Application to Irradiation Behavior Analysis of U-

                                                                                       2627
J. Zhang, H. Wang, H. Wei et al.                                                                                           Nuclear Engineering and Technology 53 (2021) 2616e2628

     Mo/Al, 2013.                                                                                  describe the evolution of the high burnup structure, J. Nucl. Mater. 456 (2015)
[37] Y.M. Zhao, X. Gong, Y. Cui, S.R. Ding, Simulation of the ﬁssion-induced                       174e181.
     swelling and creep in the CERCER fuel pellets, Mater. Des. 89 (2016) 183e195.            [42] J. Spino, A.D. Stalios, H. Santa Cruz, D. Baron, Stereological evolution of the rim
[38] J. Rest, A model for the effect of the progression of irradiation-induced                     structure in PWR-fuels at prolonged irradiation: dependencies with burn-up
     recrystallization from initiation to completion on swelling of UO2 and U-                     and temperature, J. Nucl. Mater. 354 (2006) 66e84.
     10Mo nuclear fuels, J. Nucl. Mater. 346 (2005) 226e232.                                  [43] J. Noirot, L. Desgranges, J. Lamontagne, Detailed characterisations of high
[39] J. Spino, J. Rest, W. Goll, C.T. Walker, Matrix swelling rate and cavity volume               burn-up structures in oxide fuels, J. Nucl. Mater. 372 (2008) 318e339.
     balance of UO2 fuels at high burn-up, J. Nucl. Mater. 346 (2005) 131e144.                [44] B. Roostaii, H. Kazeminejad, S. Khakshournia, Inﬂuence of porosity formation
[40] J.D. Hales, R.L. Williamson, S.R. Novascone, et al., BISON Theory Manual the                  on irradiated UO2 fuel thermal conductivity at high burnup, J. Nucl. Mater.
     Equations behind Nuclear Fuel Analysis, Idaho National Laboratory, 2016.                      479 (2016) 374e381.
[41] Martin Lemes, Alejandro Soba, Alicia Denis, An empirical formulation to




                                                                                       2628
