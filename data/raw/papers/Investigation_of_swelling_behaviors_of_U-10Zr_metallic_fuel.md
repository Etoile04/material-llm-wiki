# Investigation of swelling behaviors of U-10Zr metallic fuel in the low temperature regime via a cavitational void swelling model

---

                                                               Journal of Nuclear Materials 564 (2022) 153665



                                                               Contents lists available at ScienceDirect


                                                          Journal of Nuclear Materials
                                                       journal homepage: www.elsevier.com/locate/jnucmat




Investigation of swelling behaviors of U-10Zr metallic fuel in the low
temperature regime via a cavitational void swelling model
Zhengyu Qian a, Xin Xie a, Yingjie Fu a, Di Yun a,b,∗, Wenbo Liu a, Xiankun Liu c, Qijie Feng c,
Haibing Guo c, Yong Sun c, Wei Zhou c, Xinfu He d, Jinli Cao d,e, Wenjie Li f
a
  School of Nuclear Science and Technology, Xi’an Jiaotong University, Xi’an, China, 710049
b
  State Key Laboratory of Multiphase Flow, Xi’an Jiaotong University, Xi’an, China, 710049
c
  Institute of Nuclear Physics and Chemistry, China Academy of Engineering Physics, Mian Yang, China, 621999
d
  Reactor Engineering Technology Research Division, China Institute of Atomic Energy, Beijing, China, 102413
e
  School of Materials and Science and Engineering, University of Science and Technology Beijing, Beijing, China, 100083
f
  Science and Technology on Reactor System Design Technology Laboratory, Nuclear Power Institute of China, Chengdu, China, 610213




a r t i c l e            i n f o                        a b s t r a c t

Article history:                                        The uranium zirconium (U-Zr) metallic nuclear fuel has long been considered as a promising candidate
Received 24 December 2021                               fuel type for fast breeder reactors. One of the key performance issues of the U-10Zr metallic fuel is its
Revised 27 February 2022
                                                        rather strong swelling, which would lead to signiﬁcant fuel cladding mechanical interaction (FCMI) at
Accepted 9 March 2022
                                                        relatively high fuel burn-ups. It is therefore imperative to understand the fuel swelling behaviors and
Available online 10 March 2022
                                                        the underlying physics mechanisms. Recently published experimental results of U-10Zr fuel swelling be-
Keywords:                                               haviors in a low temperature regime (40 0-60 0K) showed perceivable swelling of the in-pile irradiated
Uranium zirconium fuel                                  fuel. However, the underlying physics mechanism behind this swelling is not clear. In this work, we per-
Thermo-mechanical analysis                              formed in-depth analyses on the microstructural features of the irradiated fuel with metallography and
Fuel swelling                                           conducted a ﬁnite-element based simulation on a computational platform, COMSOL, to determine the
Rate theory                                             hydrostatic stress in the irradiated fuel. The spherical objects in the metallography result have been iden-
Cavitational void swelling
                                                        tiﬁed as cavities with relatively low ﬁssion gas pressure instead of equilibrium gas bubbles. A rate theory
                                                        code based on the cavitational void swelling model has been developed and the fuel swelling behaviors
                                                        of U-10Zr fuel in the low temperature regime have been assessed. The simulation results suggest a much
                                                        lower migration energy for vacancy diffusion in the metallic fuel compared to what is currently used,
                                                        and a new set of key parameters for the rate theory model were determined.
                                                                                                                             © 2022 Elsevier B.V. All rights reserved.




1. Introduction                                                                           irradiation data from past EBR-II and FFTF irradiations carried out
                                                                                          in U.S [6]. A semi-empirical swelling model was established based
    U-Zr metallic nuclear fuel has the characteristics of high ura-                       on these experimental data [8]. However, the situation at the low
nium atom density (and hence a harder neutron spectrum and a                              temperature regime (40 0K - 60 0K) is completely different due to
high conversion ratio), high thermal conductivity and good com-                           the lack of experimental data. Therefore, the fuel swelling behav-
patibility with cladding [1–4]. At the same time, the overall matu-                       iors at the low temperature regime are still largely unknown. In
rity and reliability of technology and economics of metallic fuel-                        addition, there are other applications, e.g. in a high ﬂux fast spec-
based fuel cycle are desirable [5]. These advantages make U-Zr                            trum research reactor currently in the design phase in China that
metal fuel a promising fast reactor fuel. However, there are a num-                       requires knowledge of swelling performance at the low tempera-
ber of issues from the fuel performance perspective that set lim-                         ture regime (40 0K - 60 0K), which is still a gap due to the lack of
itations to the wide use of U-Zr metallic fuels. One important is-                        experimental data. Recently, research performed at China Academy
sue is the signiﬁcant fuel swelling of metallic fuels that would post                     of Engineering Physics by the co-authors of this work provided im-
threats to fuel integrity via FCMI [6,7]. For the swelling of U-10Zr                      portant swelling behavior results for U-10Zr in the low tempera-
fuel at the high temperature regime (normal fast reactor operation                        ture regime [9]. This research showed that there was perceivable
temperature range for the fuel slug), there exists a large amount of                      volumetric swelling (∼12%) in U-10Zr at the irradiation tempera-
                                                                                          ture range of 450K - 560K (450K being the fuel slug outer radius
    ∗
                                                                                          temperature and 560K being the centerline temperature). In addi-
        Corresponding author at: 28 Xian Ning West Road, Xi’an 710049, China
                                                                                          tion, the metallographic examination of the cross-section of fuel
        E-mail address: diyun1979@xjtu.edu.cn (D. Yun).



https://doi.org/10.1016/j.jnucmat.2022.153665
0022-3115/© 2022 Elsevier B.V. All rights reserved.
Z. Qian, X. Xie, Y. Fu et al.                                                                              Journal of Nuclear Materials 564 (2022) 153665


materials used in the experiment pointed to the fact that there              particularly to shed lights on the future application of U-Zr metal-
existed a large number of very small spherical structures whose              lic fuels at low temperatures. The emergence of experimental fuel
nature remains to be determined.                                             swelling data and microstructural insights from the recent work in
    Since U-Zr metallic fuel was proposed as a fast reactor fuel             the low temperature regime [9] therefore opens a new opportunity
form, a considerable amount of research has been conducted to                to carefully examine the fuel swelling mechanisms for U-Zr metal-
establish models to describe the fuel swelling behaviors, among              lic fuels.
which many were mechanistic models. Previous studies on mecha-                   Mechanistic kinetic rate theory models often suffer from a com-
nistic models for ﬁssion gas behaviors and swelling of U-Zr metal-           mon shortage of large uncertainties due to the use of a number
lic fuel can be divided into two major categories. In one category,          of parameters at the same time [17–19]. A central issue for the
researchers [10,11] attributed the ﬁssion gas release and swelling           application of such mechanistic models to a ﬁssion gas behaviors
of metallic fuel to the interconnection of gas bubbles on the grain          problem, which is inherently complex in nature, is therefore the
boundaries and the expansion of volume occupied by the gas bub-              determination of a small set of key parameters that signiﬁcantly
bles, respectively. In the other category, researchers [12] thought          inﬂuence the computational results. Speciﬁcally, in the case of U-
that the cavitational void swelling may be the main source of                Zr metallic fuels modeling, the greatest uncertainty may lie in the
swelling for U-Zr metallic fuels. The ﬁssion gas bubble swelling             migration energy of vacancy diffusion. When Rest established the
mechanism was derived from the widely accepted bubble growth                 cavitational void swelling model, there was neither relevant exper-
kinetics in ceramic fuels based on large amount of experimental              imental data nor today’s advanced multi-scale simulation technol-
investigations on microstructural features of irradiated ceramic fu-         ogy to help assess the vacancy migration energy of α -U, so there
els [10,11]. The cavitational void swelling mechanism was proposed           inevitably existed great uncertainty in this migration energy. The
mainly based on some peculiar structural features of U-Zr metallic           large vacancy diffusion migration energy used in Rest’s model led
fuels. Metallography and scanning electron microscope (SEM) ex-              to a huge difference of 6 orders of magnitude [12] in the diffusion
aminations revealed that the structures in irradiated U-Zr metallic          coeﬃcients between the high temperature and the low tempera-
fuel, particularly in the α -U phase zone, were the swirl worked             ture regimes. And this has resulted in a signiﬁcant difference in
tear-like porosities [12,13]. Depending on the ﬁndings on the mi-            fuel swelling between the high temperature and the low tempera-
crostructural level, Rest developed a model that accounted for the           ture regimes.
swelling of the α -U phase zone in U-Zr fuels by irradiation induced             In this work, we utilized ﬁnite element analysis to calculate the
ﬁssion gas bubble nucleated cavitational void swelling mechanism             hydrostatic stress in the metallic fuel samples irradiated in a prior
[12]. The cavitational void swelling mechanism is mainly derived             work and determined that the spherical objects found in the met-
from Mansur’s work [14]. Mansur proposed the concept of criti-               allographic examination of irradiated samples of U-Zr metallic fuel
cal cavity radius and pointed out that the cavity will grow by ab-           at the low temperature regime were spherical cavities with low gas
sorbing vacancies when the radius of the cavity is greater than the          pressure instead of equilibrium gas bubbles. Building upon these
critical radius. After years of continuous development, the cavity           ﬁndings, a rate theory model based on cavitational void swelling
swelling model has been applied to in ﬁelds. Emelyanova [15] used            mechanism was established, which can well simulate the swelling
the void swelling model to explore the irradiation swelling of ODS-          of U-Zr fuels at different temperature regimes. Combined with the
EUROFER steel. Griﬃths [16] applied it to the study of irradia-              density functional theory (DFT) and molecular dynamics (MD) cal-
tion swelling of austenitic stainless steel. These studies usually ap-       culation [20,21], we used a more reasonable vacancy migration en-
ply the void swelling model to structural metals and alloys, and             ergy and the change in such energy has resulted in a much bet-
Rest was the ﬁrst to employ this model in metallic nuclear fuels             ter agreement between calculation results and experimental data
and achieved good results. In this cavitational void swelling model,         at the low temperature regime while slightly improving the agree-
swelling kinetics transform from bubble swelling to void swelling            ment with experimental data on swelling at the high temperature
when the sizes of gas bubbles penetrate the threshold for further            regime. Sections 2 and 3 provide the detailed processes of deter-
cavitational void growth. As a result, stable cavities are formed and        mining the nature of the spherical objects in the metallographic
they grow larger in size by receiving net vacancy inﬂux. In the              results, and Section 4 gives a description of the model and demon-
past decades, both bubble swelling and cavitational void swelling            strates the comparison between experimental data and the calcu-
mechanisms have been adopted to predict fuel swelling of U-Zr                lation results of fuel swelling at different temperature regimes.
metallic fuels at the high temperature regime (80 0K -10 0 0K), and
they were both quite successful despite their rather apparent dif-           2. The low temperature irradiation of U-10Zr fuels
ferences from a modeling perspective. Therefore, it becomes imper-
ative to determine which mechanism is the true operating mecha-                 The irradiation experiment was performed in a research reac-
nism for the fuel swelling of metallic U-Zr fuels.                           tor operated by the Institute of Nuclear Physics and Chemistry in
    In traditional cognition, the swelling of U-10Zr fuel at low tem-        China. The full details of the irradiation experiment, which was
perature is almost negligible according to Rest [12]. This new dis-          performed by co-authors of this work, can be found elsewhere
covery [9] is quite on the contrary to the previous prediction by            [9] and are not repeated here. However, in order to maintain the
Rest. Both bubble growth kinetics and cavitational void swelling             integrity of this paper and for the ease of comprehension of the
mechanism are strongly dependent on temperature. The recent re-              modeling work presented herein, some important details of the ir-
search [9] showed that the swelling reached 12% at 0.5at% bur-               radiation experiment that are relevant to the modeling side of the
nup, and the swelling increased rapidly with burnup. In the pre-             work are re-introduced.
vious data about the EBR-II fuels [6], the swelling of fuel at the              U-10Zr fuel slugs were irradiated in a pool-type research reactor
high temperature regime is close to 10% at 0.4at% burnup, but the            (China Mianyang Research Reactor, CMRR). The maximum burn-
temperature difference between the two temperature regimes is                up of the tested fuels is about 0.7 at.%, including contributions
about 300K. Whether if the key swelling mechanism was bubble                 from both U-235 and U-238. The U-235 enrichment was increased
growth or cavitational void swelling, such a large temperature dif-          in order for the tested fuels to reach the intended burn-up in a
ference will pose a great impact on swelling, but the gap between            shorter period of time. The geometries of the irradiated fuel slugs
experimental data between the two temperature regimes is actu-               were the same, 5mm×15mm cylinders. The outer Zr-4 shell of the
ally quite small. Therefore, it is necessary to explore the swelling         test capsules were also cylinders of 10mm×35mm cylinders with
mechanism of U-Zr metallic fuels at the low temperature regime,              1 mm wall thickness. Two types of irradiation samples and cap-

                                                                         2
Z. Qian, X. Xie, Y. Fu et al.                                                                                                Journal of Nuclear Materials 564 (2022) 153665


                                                                                            of 0.25, to be 0.1375 at.% which corresponds to ﬁssion gas level of
                                                                                            4.9×1019 ﬁssion gas atoms/cm3 . If one assumes that all the ﬁssion
                                                                                            gas atoms are retained in the cavities, then the ﬁssion gas den-
                                                                                            sity inside the cavities is 6.13×109 ﬁssion gas atoms/spherical ob-
                                                                                            ject. At this size range of cavities, one can safely assume an ideal
                                                                                            gas law for the gaseous equation of state. Through applying the
                                                                                            ideal gas law, the inner pressure of the average cavity is estimated
                                                                                            to be about 3 MPa. As the equilibrium bubbles need to achieve a
                                                                                            force balance between the inner pressure and the surface tension
                                                                                            plus the hydrostatic stress, the hydrostatic stress is estimated to
                                                                                            be about a compressive 2.3 MPa (given that the surface energy of
                                                                                            U-10Zr fuel is 0.5 J/m2 [12]). Now, if one relaxes the assumption
                                                                                            that all ﬁssion gas atoms join the cavities and realize that only a
                                                                                            fraction of them join the cavities, the resulting estimated internal
                                                                                            pressure will have to be even lower than 2.3MPa. It then becomes
                                                                                            necessary to have a realistic estimate of the hydrostatic stress in
Fig. 1. Metallography image of as-irradiated U-10Zr fuel at the low temperature             the irradiated fuel in order to verify the nature of the spherical
regime (at a burn-up level of 0.55 at.%, selected small spherical cavities are marked       objects.
by red arrows).

                                                                                            3. Thermo-mechanical analysis after irradiation
sules were designed to investigate the free swelling (swelling with
                                                                                            3.1. Finite-element model via COMSOL multiphysics
no mechanical constraint) behavior and fuel-cladding interaction,
respectively. In this work, we focus on the set of tested fuel slugs
                                                                                                A thermo-mechanical model for the irradiated U-10Zr fuel has
with their capsules designed to evaluate the free swelling behav-
                                                                                            been established based on the ﬁnite-element computational plat-
iors. Pure aluminum powder loosely ﬁlled to 68% of the theoreti-
                                                                                            form of COMSOL Multiphysics (version 5.5) [22]. The geometry of
cal density with almost homogeneous porosity was chosen to ﬁll
                                                                                            the model is consistent with the geometry of the irradiation device
the gap between the inner slug and the outer capsule shell. This
                                                                                            where the U-10Zr fuel slug is surrounded by loose aluminum pow-
both allowed space to accommodate the fuel swelling and provided
                                                                                            der and a Zr-4 cladding [9]. A 2-dimensional axi-symmetric model
good thermal conduction in the gap. The temperature distribution
                                                                                            was applied to simulate the thermos-mechanical behaviors of the
was calculated via a ﬁnite-element based computer program and
                                                                                            fuel slug. The heat transfer boundary conditions were set to match
this calculated temperature proﬁled was used as the input to the
                                                                                            those from the Fluent calculation in the reference literature [9].
rate theory program developed in this work. The detailed temper-
                                                                                            Table 1 summarizes the thermo-physical properties used in this
ature distribution in the fuel is shown in section 3.
                                                                                            simulation. where P is the porosity in the fuel slug, and T is the
    Fuel dimension changes were measured with both cold neutron
                                                                                            temperature in K. Properties of Al-6061 powder were taken from
radiography and metallography after an extensive cooling period
                                                                                            the in-software library of COMSOL multiphysics but the thermal
after the irradiated fuel slugs were taken out of the reactor. Both
                                                                                            conductivity and elastic modulus were corrected with the porosity
radial and axial dimension changes were measured with cold neu-
                                                                                            effects [29,30]. The plasticity model, thermal creep and irradiation
tron radiography at four different burn-ups. Two tested fuel slugs
                                                                                            creep correlations have been taken from past literatures [31]. A
received different burn-up levels due to their different location in-
                                                                                            parabolic ﬁt to the volumetric swelling data measured from the ex-
side the reactor test channel. The lower burn-up fuel slug reached
                                                                                            periment has been used as the swelling correlation (as a function
a ﬁnal burn-up of 0.55 at.% while the higher burn-up fuel slug
                                                                                            of fuel burn-up) fed to the thermo-mechanical simulation. It needs
reached a ﬁnal burn-up of 0.7 at.%. All these data were then pro-
                                                                                            to be pointed out that the purpose of the thermo-mechanical mod-
cessed to estimate the fuel swelling behaviors which were then
                                                                                            eling performed here is to provide a reasonable estimate on the
used as validation data to the rate theory model presented in this
                                                                                            hydrostatic stress. Hence, the measured relationship between fuel
work. Both fuel specimens reached a volumetric swelling level of
                                                                                            swelling strains and fuel burn-ups were used as an input known
∼12%.
                                                                                            correlation. The detailed temperature proﬁle in the radial direction
    Metallography results were obtained on the mid-cross-section
                                                                                            calculated via COMSOL is shown in Fig. 2 and it agrees well with
(axially) of the U-10Zr sample irradiated to 0.55 at.% burn-up.
                                                                                            that obtained by FLUENT in the reference literature [9].
Fig. 1 shows the metallography micro-image. There exists a large
amount of very small spherical structures (selectively marked by
red arrows in Fig. 1) whose nature is either ﬁssion gas bubble or                           3.2. Distribution of hydrostatic stress in the radial direction
cavity (where the internal ﬁssion gas pressure is relatively low).
In Section 1, we mentioned that the swelling mechanism for gas                                  One main difference between the heat transfer analysis in this
bubble and cavity is different. For the gas bubble growth kinet-                            work and that in the earlier work is the inclusion of porosity ef-
ics, the source of fuel swelling is gas atoms absorbed by bubbles,                          fect in the fuel slug. This has resulted in an increase in tempera-
but for the cavitational void swelling mechanism, the source is                             ture over time when porosity developed in the fuel slug. The max-
voids absorbed by cavities. It is therefore necessary to discrimi-                          imum temperature in the fuel slug (specimen P2-A4 in ref [9]) at
nate whether these structures are bubbles or cavities. The aver-                            0.55 at.% is 283°C, which is about 24°C higher than the maximum
age size of these structures has been measured to be about 3 μm                             temperature obtained by the equilibrium solution in reference [9].
in diameter (with 1328 cavities measured, mean diameter, 2.98μm,                            Fig. 3 demonstrates the distribution of hydrostatic stress along
and standard deviation, 0.988μm) and the number density was es-                             the radial direction in the mid-cross-section plane (middle height
timated to be about 8×109 objects/cm3 . It is diﬃcult to identify                           plane) of the fuel slug. It can be seen that due to the low tem-
the exact nature of these spherical objects. However, the internal                          perature of the fuel and hence the ineffectiveness of creep to re-
gas pressure may be quickly estimated. At 0.55 at.% burn-up, ﬁs-                            lieve the stress, the hydrostatic stress has been estimated to about
sion gas generated can be reliably estimated, by the ﬁssion yield                           60-130 MPa (compressive). Thus, there exists more than an order

                                                                                        3
Z. Qian, X. Xie, Y. Fu et al.                                                                                                  Journal of Nuclear Materials 564 (2022) 153665


                                  Table 1
                                  Thermo-physical properties of U-10Zr fuel and Zr-4 cladding used in the thermos-mechanical simulation.

                                    Property             Value                                                        Units       Source

                                    Fuel (U-10Zr)
                                    k                    (1-P)1.5 k0                                                  W/m/K       [23]
                                                         k0 =11.7+1.33×10− 2 T+9.38×10−6 T2
                                    Cp                   26.58+0.027(T-273.15)/206.3                                  J/kg/K      [24]
                                    E                    56-0.1158(T-890)                                             GPa         [25]
                                    αT                   1.76×10−5                                                    1/K         [26]
                                    ν                    0.33                                                                     [25]

                                    Cladding (Zr-4)

                                    k                    7.51 + 2.09 × 10−2 T − 1.45 × 10−5 T2 + 7.67 × 10−9 T3       W/m/K       [27]
                                    Cp                   286.5+0.1T                                                   J/kg/K      [27]
                                    E                    [9.9 × 105 − 566.9 × (T − 273.15)]× 9.8067 × 104             Pa          [28]




                                                                                               4. The rate theory model

                                                                                                   Through the analysis in Section 3, we determined that the small
                                                                                               spherical structures in the fuel are more likely to be cavities. It
                                                                                               means that the swelling of U-10Zr fuel mainly comes from the cav-
                                                                                               ities and the cavitational void swelling model developed by J. Rest
                                                                                               [12] can be used to capture the swelling behaviors at the low tem-
                                                                                               perature regime. A rate theory code that is based on the model
                                                                                               established by J. Rest [12] has been developed in this work to sim-
                                                                                               ulate the cavitational void swelling in U-10Zr fuel at both the low
                                                                                               temperature regime and the high temperature regime. The detailed
                                                                                               scheme of the rate theory model has been well described in the
                                                                                               work by J. Rest and will not be repeated here [12]. It is worth
                                                                                               noting that the cavitational void swelling in the α -U begins with
                                                                                               nucleation of gas bubbles and when the gas bubble penetrates
                                                                                               the threshold for further cavitational void growth, stable cavity is
                                                                                               formed and grows larger in size by receiving net vacancy inﬂux. In
                                                                                               the γ -U phase, however, the initial bubble nuclei keep absorbing
 Fig. 2. Distribution of temperature in the radial direction calculated via COMSOL.
                                                                                               ﬁssion gas atoms due to comparatively high ﬁssion gas diffusivity
                                                                                               because of the higher temperature. Therefore, it is the net inﬂux
                                                                                               of vacancies or ﬁssion gas atoms that set the swelling behaviors
                                                                                               different.


                                                                                               4.1. The swelling behavior of U-10Zr fuel at the low temperature
                                                                                               regime (400 – 600K)

                                                                                                   The research of China Academy of Engineering Physics provided
                                                                                               important swelling data in the low temperature regime to validate
                                                                                               the cavitational void swelling model. At the same time, the ex-
                                                                                               perimental data also pointed out that the early model [12] signiﬁ-
                                                                                               cantly underestimated the fuel swelling at low temperatures. This
                                                                                               is mainly because of the extremely low vacancy diffusion coeﬃ-
                                                                                               cient used in the model at the low temperature. For the cavita-
                                                                                               tional void swelling, the growth of cavities, which is derived by
                                                                                               accumulating vacancies, determines the fuel swelling. Such a low
Fig. 3. Distribution of hydrostatic stress in the radial direction on the mid cross sec-
                                                                                               diffusion coeﬃcient leads to almost zero cavity growth, which re-
tion plane of the fuel slug calculated via COMSOL (metallography region is marked
by the yellow window).                                                                         sulted in seriously underestimated fuel swelling at low tempera-
                                                                                               tures. As such, the fact that the swelling at the low temperature
                                                                                               regime is not much lower compared to that at the high tempera-
of magnitude difference between the simulation-provided hydro-                                 ture regime suggests a ﬂatter curve for the vacancy diffusion coef-
static stress and that estimated in the fuel by analysis of the gas                            ﬁcient across the low and high temperature regimes, and a smaller
atom number density per cavity (2.3 MPa). This throws the equi-                                value for the activation energy of vacancy diffusion becomes nec-
librium bubble scenario into major question. Moreover, it needs to                             essary.
be pointed out that when fuel temperature is relatively low, a large                               Based on the above analysis, we adjusted the parameters used
fraction of ﬁssion gas would be residing in the fuel matrix due to                             in the Rest’s work [12]. The key parameters used in our model to
effective gas bubble resolution together with the low ﬁssion gas                               interpret U-10Zr fuel swelling behaviors at the low temperature
diffusivity [32]. This would lead to a further decrease of already ex-                         regime are summarized in Table 2. Here, the formation energy and
tremely low hydrostatic stress estimated from the gas atom num-                                diffusion activation energy of vacancy are set to 1.77 and 0.34 eV,
ber density per cavity. As such, we conclude that the possibility of                           respectively. The values were obtained with 5×2×3 supercells uti-
the cavities being equilibrium gas bubbles is dim.                                             lizing the Vienna Ab initio Simulation Package (VASP) based on the

                                                                                           4
Z. Qian, X. Xie, Y. Fu et al.                                                                                                 Journal of Nuclear Materials 564 (2022) 153665


                      Table 2
                      Key Parameters for the Low Temperature Fuel Swelling Calculation.

                         Parameter                                                                 Value        Reference

                         Fuel axial length (mm)                                                    15.0         [9]
                         Fuel radius (mm)                                                          2.5          [9]
                         Pre-exponential factor for vacancy diffusion (cm2 •s−1 )                  1.0×10−7     This work
                         Migration energy for vacancy diffusion (eV)                               0.34         [20]
                         Formation energy for vacancy (eV)                                         1.77         This work
                         Pre-exponential factor for interstitial diffusion (cm2 •s−1 )             1×10−4       This work
                         Migration energy for interstitial diffusion (eV)                          0.19         [20]
                         Pre-exponential factor for ﬁssion gas atom diffusion coeﬃcient (cm2 /s)   1.2×10−3     [39]
                         Migration energy for ﬁssion gas atom diffusion (eV)                       1.16         [39]
                         Dislocation density (cm−2 )                                               7×109        [12]
                         Bubble nucleation factor in the bulk                                      1×10−5       [12]
                         Bubble nucleation factor on the phase boundaries                          1×10−5       [12]
                         Grain size (cm)                                                           1×10−3       This work, roughly estimated via TEM




             Fig. 4. Comparison between fuel swelling by simulation and by experimental measurements (a) specimen #10, (b) specimen #11 from reference [9].




density functional theory (DFT) [33–35], and they are also consis-
tent with previous literature results via DFT calculations [20]. An
activation energy of 0.19 eV is used for interstitial migration. This
value is adopted from the earlier DFT work as well [20]. The pre-
exponential factors for both vacancy and interstitial diffusion coef-
ﬁcients in the fuel were obtained in this work. The rationale for the
derivation of these values is that, if the model calculated swelling
behaviors compare well with experimental data at both the low
and the high temperature regimes, then these key parameters are
believed to be reasonable, given the additional pre-requisite that
they do not fall out of their normal expected range. The tempera-
ture distribution and the geometric information were obtained by
the ﬁnite-element analysis performed in Section 3.
    Fig. 4(a) and (b) compare the calculated fuel volumetric
swellings by the mechanistic model and the measured data from
the reactor irradiation experiments (specimen #10 and #11 in ref-
erence [9]). It is reasonable to believe that there is no ﬁssion gas
release in this irradiation experiment due to the low temperature
of the irradiated fuel and the relatively low ﬁnal burn-up that                            Fig. 5. Comparison between fuel swelling by simulation and experimental mea-
                                                                                           surements under different vacancy migration energies (ε F represents the vacancy
the fuel had reached. This is also consistent with the prediction
                                                                                           migration energy used in the present study).
results by our model. It can be observed that the trends of the
swelling curves are well in accordance with the experimental data.
At the same time, the calculated average cavity size is about 1.94
μm, reasonably close to that obtained from metallography result
(3 μm). To verify the rationality of the vacancy migration energy                          were adopted, reﬂected the high sensitivity of calculated swelling
selected in this work, a parameter sensitivity analysis were con-                          to this peculiar parameter. It, in fact, further provides support to
ducted. Fig. 5 shows the simulation results of the model with dif-                         the value of such parameter adopted in this work. It needs to be
ferent vacancy migration energies. It is not hard to ﬁnd that the                          pointed out that this, alone, cannot be a testimony to the valid-
vacancy migration energy selected in this work can well capture                            ity of the model and the corresponding parameters used herein.
the swelling of U-10Zr fuel at the low temperature regime. In addi-                        Besides the low temperature regime, the trends of both the ﬁs-
tion, the rather strong deviations of simulation results from the ex-                      sion gas release and the swelling curves in the high tempera-
perimental data, when other values of vacancy migration energies                           ture regime, which is the operation temperature regime for EBR-II

                                                                                       5
Z. Qian, X. Xie, Y. Fu et al.                                                                                            Journal of Nuclear Materials 564 (2022) 153665


    Table 3
    Key Parameters for the High Temperature Fuel Fission Gas Release and
    Swelling Calculation.

      Parameter                                Value         Reference

      Fuel axial length (mm)                   343.0         [6]
      Fuel radius (mm)                         2.83          [6]
      Peak cladding temperature (°C)           522           [6]
      Bubble nucleation factor in the bulk     1×10−5        [12]
      Peak linear power rate (W/cm)            427           [6]
      Grain size – γ zone (cm)                 5×10−3        [12]
      Irradiation enhanced bubble              1×10−29       [12]
      diffusivity (cm2 /s)
      Gas bubble re-solution constant (cm3 )   1×10−18       [12]




                                                                                     Fig. 7. Comparison between simulated ﬁssion gas release and experimental data for
                                                                                     U-10Zr [36].



                                                                                     up range between 0.65 at.% and 0.75 at.%. Since the α phase zone
                                                                                     occupies about 72.2% of the total fuel volume, its ﬁssion gas re-
                                                                                     lease behavior becomes dominant. The ﬁssion gas release demon-
                                                                                     strates an asymptotic behavior towards the release level of about
                                                                                     70%. Different from ﬁssion gas release, the trend of unrestrained
                                                                                     fuel swelling with burnup is relatively simple. At 0.65 at.% burn-
                                                                                     up, the total fuel swelling reached 25%, and this corresponds to
                                                                                     the burn-up region where ﬁssion gas release starts to show a sharp
                                                                                     increase. This is consistent with the common observations that ﬁs-
                                                                                     sion gas starts to release in high fraction when U-10Zr fuel swells
Fig. 6. Simulated fuel swelling and ﬁssion gas release at the high temperature
                                                                                     to an extent beyond 30% volumetric strain. These points show that
regime.                                                                              the results of the model are basically in accordance with the cur-
                                                                                     rent understanding of the U-10Zr fuel behaviors [6]. Fig. 7 com-
                                                                                     pares the ﬁssion gas release predicted by the model and the exper-
tested fuels, have to be consistent with experimental observations                   imental data [6]. It is perceivable that the simulated ﬁssion gas re-
as well. This will be demonstrated in the following section.                         lease matches the experimental data reasonably well. Fig. 8 shows
                                                                                     the axial distribution of fuel swelling under different burnup. It can
4.2. The swelling behavior of U-10Zr fuel at the high temperature                    be seen that the results of our model can effectively envelope ex-
regime (800 – 1000K)                                                                 perimental data points at the burn-up of 0.4 at.%, and also shows a
                                                                                     good agreement with data points at 0.9 at.% burn-up in both values
    Different from with the situation of the low temperature                         and trends. Generally speaking, the modiﬁed model can effectively
regime, there are more data that can be used to validate at the                      capture the behaviors of swelling and ﬁssion gas release of U-10Zr
high temperature regime, but the multiphase characteristics of U-                    fuel at the high temperature range.
10Zr fuel will greatly increase the diﬃculty of modeling. At such
temperature range, there will exist two difference phase regions (α                  4.3. The diffusion coeﬃcients and their effects on swelling
fuel zone and the γ fuel zone) and this makes it necessary to con-
sider the ﬁssion gas behaviors in different phase regions separately.                    In Sections 4.1 and 4.2, we demonstrated the swelling behavior
According to the temperature distribution calculated via the COM-                    of U-10Zr fuel at both the low and the high temperature regimes
SOL Multiphysics Finite Element platform, the fuel was divided into                  obtained by the modiﬁed model and the results of the model are
two regions and the phase boundary temperature was chosen to                         basically in accordance with the experimental data. Compared with
be 903K. In the γ phase zone, the gas bubble growth kinetics was                     the Rest’s model, we mainly change the vacancy and interstitial
used to model the ﬁssion gas release and fuel swelling, while the                    diffusion coeﬃcients, so it is necessary to compare these two pa-
bubble nucleated cavitational void swelling kinetics was adopted                     rameters between this work and prior works and Fig. 9 shows such
in the α phase zone. The fuel irradiation experiment parameters                      comparison. The parameters we used can well reﬂect the swelling
and the key parameters used for the mechanistic model for the γ                      of U-Zr metal fuel at both the high and the low temperature
phase zone are tabulated in Table 3. Parameters for the U-10Zr fuel                  regimes at the same time, while Rest’s model could not predict the
were taken from the published data for the EBR-II irradiation ex-                    swelling behaviors in the low temperature regime. From the Fig. 9,
periment X423 [6].                                                                   we can intuitively see that at the high temperature range the dif-
    Fig. 6 gives the fuel swelling and ﬁssion gas release predicted                  fusion coeﬃcients used in our model exhibited no differences with
by our mechanistic model. The results of the model are obtained                      those used by Rest, but at the low temperature range, the differ-
after comprehensively considering the ﬁssion gas behaviors in dif-                   ence between the diffusion coeﬃcients becomes signiﬁcant. This is
ferent phase regions. For the γ phase zone, there is nearly no ﬁs-                   mainly due to the fact that the migration energy used in our work
sion gas release until relatively high burn-up, while for the α phase                is much smaller and hence the diffusion coeﬃcient curve of va-
zone, ﬁssion gas release experiences an incubation period of about                   cancy becomes much ﬂatter. Therefore, the diffusion coeﬃcient is
0.65 at.% burn-up and then shows a sharp increase at the burn-                       about 3 to 4 orders of magnitude higher than that used by Rest at

                                                                                 6
Z. Qian, X. Xie, Y. Fu et al.                                                                                                  Journal of Nuclear Materials 564 (2022) 153665




         Fig. 8. Comparison between axial distribution of fuel swelling by simulation and by experimental measurements (a) 0.4 at.%, (b) 0.9 at.% fuel burn-ups [12].



                                                                                          comparison between swelling calculated by our work and that by
                                                                                          Rest’s is also included. The swelling reaches a peak value and then
                                                                                          sharply declines with increasing temperature, which is consistent
                                                                                          with prior works [18,19]. Due to the ﬂatter distribution of vacancy
                                                                                          diffusion coeﬃcient used in our model, fuel swelling remains at a
                                                                                          higher and detectable value at the temperature of 400K as com-
                                                                                          pared to Rest’s work. This ﬁgure also marks the key difference be-
                                                                                          tween the simulated U-10Zr swelling in this work and that in the
                                                                                          prior work by Rest in the temperature range of 40 0K - 80 0K. It
                                                                                          should to be noted that there is still uncertainty in the temper-
                                                                                          ature range between 60 0K and 80 0K due to lack of experimen-
                                                                                          tal data, and further research of an in-reactor irradiation of U-10Zr
                                                                                          fuel at the temperature range would be needed to further validate
                                                                                          the results obtained in this work.

                                                                                          4.4. The swelling behavior of U-10Zr fuel in the low temperature
                                                                                          regime with the gas bubble driven swelling model
Fig. 9. Comparison between diffusion coeﬃcients of vacancy and interstitial ob-
tained in this work and those from a prior work by J. Rest [12].                              The previous sections showed that the cavitational-void
                                                                                          swelling model can predict the swelling of U-10Zr fuel in different
                                                                                          temperature ranges under the premise of modiﬁed vacancy and in-
                                                                                          terstitial diffusion coeﬃcients. But many prior works adopted the
                                                                                          ﬁssion gas bubble growth mechanism (which has been widely used
                                                                                          for oxide fuels [37,38]) as the main contributing mechanism for
                                                                                          the fuel swelling of U-Zr/U-Pu-Zr type metallic fuels [10,11]. It be-
                                                                                          comes necessary at this point to use the bubble growth kinet-
                                                                                          ics to model U-10Zr fuel swelling at the low temperature regime.
                                                                                          Consequently, we made an attempt to capture the fuel swelling
                                                                                          behaviors at the low temperature regime with the gas bubble
                                                                                          growth model. The key parameters are the same with those from
                                                                                          Table 2 and 3. However, the resulting fuel swelling at 0.55 at.%
                                                                                          burn-up of the fuel, which is 1.2% including solid ﬁssion prod-
                                                                                          uct induced swelling, is very small. This is mainly because of the
                                                                                          rather small diffusion coeﬃcient for ﬁssion gas atoms in the low
                                                                                          temperature regime. Of course, we can adjust the diffusion coef-
                                                                                          ﬁcient of gas atoms similar to what we did in the cavitational-
                                                                                          void swelling model, but only when the pre-exponential factor of
                                                                                          ﬁssion gas diffusion coeﬃcient is artiﬁcially raised by as much
Fig. 10. Calculated U-10Zr fuel cavitational void swelling with respect to tempera-
ture (the curve beyond 903K is hypothetical due to the phase change to γ -U and
                                                                                          as six orders of magnitude, which is unreasonably high, can 10%
the resulting different swelling mechanism).                                              fuel swelling be obtained. By changing other key parameters such
                                                                                          as the bubble re-solution factor or the bubble nucleation factor
                                                                                          while holding the ﬁssion gas diffusion coeﬃcient, the resulting
the low temperature region (500 – 600k). This difference becomes                          fuel swelling did not exceed 1.5%, including solid ﬁssion product
the key factor in boosting the cavity growth kinetics and hence the                       induced swelling. Therefore, we believe that it is diﬃcult to ob-
cavitational fuel swelling in the low temperature regime.                                 tain the swelling behaviors of U-10Zr fuel in the low temperature
   Void swelling versus temperature curve usually takes a bell                            regime using the gas bubble growth model if the key parameters
shape and the swelling reaches a maximum at certain tempera-                              were to be set to be within a reasonable range physics wise. From
ture before it decreases due to higher annihilation rate of defects                       the above we conclude that bubble growth kinetics is not suitable
at high temperatures. Fig. 10 illustrates the trend of U-10Zr fuel                        for the simulation of fuel swelling of U-10Zr fuel at the low tem-
swelling with respect to temperature, and at the same time the                            perature regime, because even if some unreasonably set parame-

                                                                                      7
Z. Qian, X. Xie, Y. Fu et al.                                                                                     Journal of Nuclear Materials 564 (2022) 153665


ters were used (which is not allowed in rate theory simulations            Acknowledgements
in general), we cannot use bubble growth kinetics to obtain fuel
swelling close to that observed in the experiments. However, we                This research was also supported by the National Natural Sci-
can use reasonable parameters to describe the fuel swelling at the         ence Foundation of China (Grant No. 11675126, Grant No. 11705255
low temperature regime through cavitational void swelling model,           and Grant No. 11405153). Financial support provided by the NSAF
which also shows that cavity swelling is the main swelling mech-           Joint Fund (No. U2130105) and the CNNC Innovation Project at
anism at this low temperature regime.                                      Xi’an Jiaotong University are also acknowledged.

                                                                           References
5. Conclusions
                                                                            [1] L.C. Walters, B.R. Seidel, J.H. Kittel, Nucl. Technol. 65 (1984) 179.
    In this work, an in-depth analysis of the swelling data and met-        [2] R.G. Pahl, D.L. Porter, D.C. Crawford, L.C. Walters, J. Nucl. Mater. 188 (1992) 3.
                                                                            [3] G.L. Hofman, L.C. Walters, T.H. Bauer, Prog. Nucl. Energy 31 (1997) 83.
allography results of U-10Zr metal fuels irradiated in the low tem-         [4] D.C. Crawford, D.L. Porter, S.L. Hayes, J. Nucl. Mater. 371 (2007) 202.
perature regime (40 0 – 60 0K) was carried out, and the main con-           [5] W.J. Carmack, D.L. Porter, Y.I. Chang, S.L. Hayes, M.K. Meyer, D.E. Burkes,
clusions are as follows:                                                        C.B. Lee, T. Mizuno, F. Delage, J. Somers, J. Nucl. Mater. 392 (2009) 139.
                                                                            [6] T. Ogata, Chapter 3.01, Comprehensive Nuclear Materials, Elsevier, 2012.
                                                                            [7] G.L. Hofman, R.G. Pahl, C.E. Lahm, D.L. Porter, Metall. Trans. A, 21A (1990) 517.
1) From the metallography results, spherical cavities with an av-           [8] M.C. Billone, Y.Y. Liu, E.E. Gruber, T.H. Hughes, J.M. Kramer, Proc. Int. Conf. Re-
   erage size of 3 μm (in diameter) were observed. The number                   liable Fuels for Liquid Metal Reactors, Tucson, Arizona, September 7-11 (1986).
   density of the cavities was about 8×109 cavities/cm3 .                   [9] H. Guo, W. Zhou, Y. Sun, D. Qian, J. Ma, J. Leng, H. Huo, S. Wang, Nucl. Engr.
                                                                                Tech. 49 (2017) 734.
2) The distribution of the hydrostatic stress in the metallic fuel         [10] Y. Tsuboi, T. Ogata, M. Kinoshita, H. Saito, J. Nucl. Mater. 188 (1992) 312.
   was obtained by a ﬁnite-element based thermo-mechanical                 [11] C.B. Lee, D.H. Kim, Y.H. Jung, J. Nucl. Mater. 288 (2001) 29.
   analysis. Combined with the experimental data, the results sug-         [12] J. Rest, J. Nucl. Mater. 207 (1993) 192.
                                                                           [13] W.R. McDonell, ANS Trans. 15 (1972) 185 Proc. Int. Conf. on Physical Metal-
   gest that the spherical objects observed via metallography were
                                                                                lurgy of Reactor Fuel Element, eds. J.E. Harris and E.C. Sykes (The Metallurgical
   cavities with low gas pressure instead of equilibrium gas bub-               Society, London, 1975) p. 266.
   bles.                                                                   [14] L.K. Mansur, W.A. Coghlan, J. Nucl. Mater. 119 (1983) 1.
3) Employing a kinetic rate theory method, U-10Zr metallic fuel            [15] O. Emelyanova, A. Gentils, V.A. Borodin, J. Nucl. Mater. 545 (2021) 152724.
                                                                           [16] M. Griﬃths, J. Ramos-Nervi, L. Greenwood, J. Nuclear Eng. 2 (4) (2021)
   swelling behaviors in both the low temperature regime and the                484–515.
   high temperature regime (α -U zone in the EBR-II fuel temper-           [17] J. Rest, G.L. Hofman, Y.S. Kim, J. Nucl. Mater. 385 (2009) 563–571.
   ature regime) were modeled. It was shown that using a much              [18] J. Rest, J. Nucl. Mater. 407 (2010) 55–58.
                                                                           [19] Z. Qian, W. Liu, R. Yu, Y. Tao, D. Yun, L. Gu, J. Nucl. Mater. 556 (2021) 153188.
   lower migration energy for vacancy diffusion (0.34 eV, accord-          [20] G.-Y. Huang, B. Wirth, J. Phys. Condens. Matter 23 (2011) 205402.
   ing to our DFT calculation, and consistent with results from            [21] B. Beeler, Y. Zhang, M. Okuniewski, C. Deo, J. Nuclear Mater. 508 (2018) 181.
   previous literature) compared to an earlier work could well de-         [22] COMSOL Multiphysics User’s Guide manual, COMSOL Inc., www.comsol.com.
                                                                           [23] H. Savage, J. Nucl. Mater. 25 (1968) 249.
   scribe the fuel swelling behaviors at both temperature regimes          [24] T. Kobayashi, et al., Nucl. Technol. 89 (1990) 183.
   when a cavitational void swelling model is applied for the α -U         [25] A. Karahan, Ph. D. Thesis, Massachusetts Institute of Technology, 2009.
   zone.                                                                   [26] L. Leibowitz, R.A. Blomquist, Int. J. Thermophys. 9 (1988) 873.
                                                                           [27] S.D. Yu, S. Xu, Nucl. Engr. Design 216 (2002) 165.
4) The EBR-II fuel swelling and ﬁssion gas release behaviors were          [28] E.F. Fisher, C.J. Renken, Physical Rev. 135 (1964) 482.
   well captured when a gas bubble growth model was applied                [29] D. Yun, A.M. Yacout, M. Stan, T.H. Bauer, A.E. Wright, J. Nucl. Mater. 448 (2014)
   for the γ -U phase of EBR-II irradiated U-10Zr fuels. Several im-            129.
                                                                           [30] Y. Gao, Master’s Thesis of Xi’an Jiaotong University (2018).
   portant parameters for the rate theory model have been de-
                                                                           [31] E.E. Gruber, J.M. Kramer, Proc. 13th Int. Symp. (Part-I) Radiation Induced
   termined based on comparisons between the simulation results                 Changes in Microstructure, ASTM-STP-955 (1987) 432.
   and experimental data.                                                  [32] D.R. Olander, Fundamentals of Nuclear Reactor Fuel Elements, Energy Res. De-
                                                                                velopment Administration (1976) (Chapter 13).
                                                                           [33] G. Kresse, J. Furthmüller, Phys. Rev. B 54 (16) (1996) 11169.
Declaration of Competing Interest                                          [34] G. Kresse, J. Hafner, Phys. Rev. B 47 (1) (1993) 558.
                                                                           [35] G. Kresse, J. Furthmüller, Comp. Mater. Sci. 6 (1) (1996) 15.
                                                                           [36] R.G. Pahl, R.S. Wisner, M.C. Billone, G.L. Hofman, In Proceedings of the Int. Fast
    The authors declare that they have no known competing ﬁnan-                 Reactor Safety Meeting, Snowbird, UT (1990) 129 Vol. IV.
cial interests or personal relationships that could have appeared to       [37] M.S. Veshchunov, J. Nucl. Mater. 277 (20 0 0) 67.
                                                                           [38] Pekka Lösönen, J. Nucl. Mater. 304 (2002) 29.
inﬂuence the work reported in this paper.                                  [39] T. Ogata, M. Kinoshita, H. Saito, T. Yokoo, J. Nucl. Mater. 230 (1996) 129.


CRediT authorship contribution statement

    Zhengyu Qian: Conceptualization, Methodology, Investigation,
Writing – original draft. Xin Xie: Methodology, Investigation.
Yingjie Fu: Conceptualization, Methodology, Investigation. Di Yun:
Conceptualization, Methodology, Writing – review & editing, Su-
pervision, Funding acquisition. Wenbo Liu: Methodology, Investi-
gation, Funding acquisition. Xiankun Liu: Investigation. Qijie Feng:
Investigation. Haibing Guo: Investigation. Yong Sun: Investigation.
Wei Zhou: Investigation, Funding acquisition. Xinfu He: Conceptu-
alization, Methodology. Jinli Cao: Investigation. Wenjie Li: Writing
– review & editing, Supervision, Funding acquisition.




                                                                       8
