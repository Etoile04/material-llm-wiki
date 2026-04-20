# Models for effective elastic constants of irradiated U-10Mo fuels with distributed fission gas bubbles

---

                                                                  Journal of Nuclear Materials 579 (2023) 154359



                                                                 Contents lists available at ScienceDirect


                                                              Journal of Nuclear Materials
                                                        journal homepage: www.elsevier.com/locate/jnucmat




Models for effective elastic constants of irradiated U-10Mo fuels with
distributed ﬁssion gas bubbles
Yong Li a, Guochen Ding a, Zhexiao Xie a, Jing Zhang a, Xiaobin Jian a, Shurong Ding a,∗,
Yuanming Li b
a
    Institute of Mechanics and Computational Engineering Department of Aeronautics and Astronautics, Fudan University, Shanghai, China
b
    Science and Technology on Reactor System Design Technology Laboratory, Nuclear Power Institute of China, Chengdu, China




a r t i c l e            i n f o                         a b s t r a c t

Article history:                                         The multi-scale related models for the effective elastic constants of porous U-10Mo fuels under the ir-
Received 15 October 2022                                 radiation conditions are developed with the proposed multi-level homogenization method. The grain re-
Revised 23 January 2023
                                                         crystallization effects are taken into account, with ﬁssion gas bubbles (FGBs) distributed in the external
Accepted 27 February 2023
                                                         bubble-contained region of Representative Volume Element (RVE). Performing theoretical analysis and
Available online 10 March 2023
                                                         numerical simulation, the effective elastic performances are ﬁrstly obtained for the bubble-contained re-
Keywords:                                                gion, and then are volumetrically averaged with those of the internal no-bubble region. The effective
Irradiated U-10Mo fuels                                  elastic constants of irradiated U-10Mo fuels determined in this study agree well with some available ex-
Fission gas bubbles                                      perimental data in the references. The research results indicate that: (1) the effective elastic constants
Recrystallization                                        of porous U-10Mo fuels are hardly affected by the pore pressure, mainly depending on the macroscopi-
Effective elastic constants                              cally average porosity; (2) the theoretically derived model for the effective bulk modulus is the same as
Homogenization theory
                                                         the degraded Mori-Tanaka model, with the inclusion phase there regarded as bubbles having zero elas-
Numerical simulation
                                                         tic constants. The developed models correlate the elastic constants of irradiated U-10Mo fuels with their
                                                         continuously varying porous structures, which lay a foundation for modeling the multi-scale irradiation-
                                                         induced thermo-mechanical coupling behaviors.
                                                                                                                           © 2023 Elsevier B.V. All rights reserved.




1. Introduction                                                                              control rods. Macroscopic elastic constants of irradiated U-10Mo
                                                                                             fuels vary with the increase of ﬁssion density. According to the
   U-10Mo alloy with high-temperature γ -phase has been a                                    post-irradiation examination of RERTR-12 and AFIP-6 MK Ⅱ irra-
promising nuclear fuel for converting some of the research and test                          diation campaign, Schulthess and Lloyd et al. [3] observed that the
reactors from high-enriched uranium to low-enrich uranium (LEU),                             effective Young’s modulus of U-10Mo fuels in LIP773 specimens is
due to its advantages of high uranium density, low neutron cap-                              in the range of 57∼65 GPa at the ﬁssion density of 3.3 × 1027
ture cross-section, high thermal conductivity, and good irradiation                          ∼3.4 × 1027 ﬁssion/m3 , while the Young’s modulus of the un-
stability [1,2]. To qualify U-10Mo fuels as alternative LEU fuels for                        irradiated U-10Mo is ∼85 GPa [7].
Research and Test Reactors, much research about processing tech-                                 The elastic constants of irradiated U-10Mo fuels depend on the
nology, thermo-physical properties, and irradiation performance of                           evolving microstructure induced by ﬁssion events. During irradi-
U-10Mo fuels designed as U10Mo/Al dispersion fuels and U-10Mo                                ation, the ﬁssion gas atoms are generated continuously and dif-
monolithic fuels have been performed [3–6].                                                  fuse towards the grain boundary, resulting in the formation of
   Elastic constants are important physical properties of nuclear                            FGBs. FGBs formed by ﬁssion gas atoms are a signiﬁcant problem,
fuels, as they are directly related to the mechanical and geometric                          as they change the U-10Mo fuels to porous structures, degrade
stability of fuel elements. For any nuclear fuels, it is essential to                        the thermo-mechanical properties, and swell the fuels [3,8,9].
keep the structural integrity and geometric stability to avoid the                           The examinations of TEM and SEM demonstrated that the FGBs
leakage of ﬁssion products and the channel block of coolant and                              in U-Mo fuels distributed themselves in intra-granular form and
                                                                                             inter-granular form [4,10,11]. TEM images of intra-granular bubbles
                                                                                             showed that ﬁssion gas atoms could be arranged into an ordered
    ∗
        Corresponding author.                                                                nano-bubble FCC lattice, as a superlattice in the BCC crystal lat-
        E-mail address: dingshurong@fudan.edu.cn (S. Ding).                                  tice of the U-Mo matrix. Typical intra-granular bubble sizes are


https://doi.org/10.1016/j.jnucmat.2023.154359
0022-3115/© 2023 Elsevier B.V. All rights reserved.
Y. Li, G. Ding, Z. Xie et al.                                                                                     Journal of Nuclear Materials 579 (2023) 154359


2∼6 nm in diameter and the distance between the intra-granular
bubbles is in the 4∼12 nm range [11]. Thus, the intra-granular
bubbles of ﬁssion gas in nm-size could be regarded as solid pre-
cipitates in the U-Mo matrix. FGBs of irradiated U-Mo fuels ob-
served by SEM are located in the grain boundary area and named
inter-granular bubble. The diameter of inter-granular bubbles is
about 0.1∼1 μm [12]. With the increase of ﬁssion density, recrys-
tallization occurs at intermediate ﬁssion densities, with the orig-
inal large grains subdivided into ﬁne grains. The recrystallization
initiates near the grain boundary and propagates toward the inner
part with the increase of ﬁssion density, until the whole grain are
consumed [13]. The reﬁned grains present higher grain boundary               Fig. 1. Microstructures of the irradiated U-10Mo fuels by SEM (a) during recrystal-
density and shorten gas diffusion distances to grain boundaries.             lization (b) after recrystallization [10].
Therefore, recrystallization accelerates the formation and growth
of FGBs [14], and separates the irradiated U-10Mo fuels into the
bubble-contained region and the no-bubble region.                            where, Lhomi jkl
                                                                                              denotes the components of effective stiffness tensor;
    The irradiated U-10Mo fuels could be regarded as composite               σ̄i j and ε̄kl are the volume-averaged stress components and elastic
materials consisting of U-10Mo matrix and inter-granular FGBs                strain components over the RVE domainV , expressed as
full-ﬁlled with ﬁssion gas atoms. According to homogenization the-                         
                                                                                       1
ory, the macroscopic effective mechanical properties of composite            σ̄i j =               σi j dV                                                  (2)
                                                                                       V       V
materials can be obtained via the volumetric average of the meso-
                                                                                           
scopic mechanical variables, termed as mean-ﬁeld method [15,16].                       1
To calculate the mesoscopic mechanical variables, the RVE includ-
                                                                             ε̄i j =               εi j dV                                                  (3)
                                                                                       V   V
ing mesoscopic components and all structural information should
                                                                             where, σi j and εi j are the additional local stress components and
be chosen, and the mechanical behaviors of each part should be
                                                                             elastic strain components of the RVE induced by the external
known [17]. The mean-ﬁeld method for effective elastic perfor-
                                                                             forces.
mances can be carried out with analytical methods and numerical
                                                                                 The irradiated U-10Mo fuels can be regarded as heterogeneous
simulation. Different analytical models for effective elastic prop-
                                                                             materials consisting of the U-10Mo skeleton and the FGBs full-
erties of composites have been proposed by researchers [18–24].
                                                                             ﬁlled with ﬁssion gas atoms. During recrystallization, the U-10Mo
Finite element (FE) computations have also been used to obtain
                                                                             fuels could be divided into the no-bubble region and the bubble-
the effective elastic behavior of composites or porous materials
                                                                             contained region, as shown in Fig. 1(a). While the recrystallization
[25,26]. Some semi-empirical relations of effective elastic constants
                                                                             is ﬁnished, the FGBs distribute in the U-10Mo fuels uniformly, as
to porosity for porous materials are also proposed to ﬁt the experi-
                                                                             shown in Fig. 1(b) [10]. The local volume fraction of the FGBs in
mental results [3,27]. However, the effective elastic constants of ir-
                                                                             the bubble-contained region is denoted as fbc , also termed as lo-
radiated U-10Mo fuels with distributed FGBs still need to be stud-
                                                                             cal porosity. The macroscopic volume fraction of the FGBs for the
ied, considering its special irradiation phenomena and the contin-
                                                                             whole irradiated U-10Mo fuels denoted as fbm , termed as macro-
uous evolution of the FGBs in the irradiated U-10Mo fuels during
                                                                             scopic porosity, is expressed as
recrystallization. Different from the general porous materials, dis-
tinct bubble-contained region and no bubble region appear before                       Vc fbc
                                                                             fbm =            = ηbc fbc                                                     (4)
completion of grain recrystallization, and pore pressures result in                     V
the existence of initial stresses.                                           where, Vc is the volume of the bubble-contained region; ηbc is the
    In this study, the effective elastic constants of irradiated U-          volume fraction of the bubble-contained region; V is the sum vol-
10Mo fuels with distributed FGBs are studied based on homoge-                ume of the no-bubble region and the bubble-contained region.
nization theory. A multi-level homogenization method is proposed                 To obtain the effective elastic constants of irradiated U-10Mo
considering the distribution feature of the FGBs during recrystal-           fuels, the RVE representing the microscopic information should be
lization. Different RVEs of equivalent spherical model and random            selected. Fig. 2 shows the multi-level homogenization process for
distribution model are selected to determine the independent ef-             the irradiated U-10Mo fuels during recrystallization. In the ﬁrst-
fective elastic constants of the irradiated U-10Mo fuels. The effec-         level homogenization, the bubble-contained region is homogenized
tive bulk modulus is theoretically derived according to the elas-            to an isotropic material. Then the homogenized bubble-contained
tic solution of the equivalent spherical model. The effective shear          region and no-bubble region are homogenized to an isotropic ma-
modulus is calculated by the effective bulk modulus and the effec-           terial further. Thus, this multi-level homogenization method is im-
tive Young’s modulus, while the latter is obtained by FE method              plemented for the irradiated U-10Mo fuels during recrystallization.
based on the random distribution model. The effective elastic con-           While the recrystallization is ﬁnished, the FGBs are assumed to be
stants determined in this study are compared with other effective            homogeneously distributed in all the U-10Mo matrix, and only the
elastic constants models and some available experimental data in             ﬁrst-level homogenization is needed to obtain the effective elastic
the references. At last, the effective elastic constants models re-          constants of the irradiated U-10Mo fuels. Two types of RVE includ-
lated to the macroscopic porosity are developed for the irradiated           ing the equivalent spherical model and random distribution model
U-10Mo fuels.                                                                are selected to determine the effective elastic constants of the irra-
                                                                             diated U-10Mo fuels as shown in Fig. 2. The shapes of the FGBs and
2. A multi-level homogenization method for modeling of                       the no-bubble regions are approximately spherical in this study.
effective elastic constants of irradiated fuels
                                                                             3. Determination of the effective elastic constants for the
    According to the homogenization theory, the homogenized elas-            bubble-contained region
tic constitutive relation for heterogeneous materials is deﬁned as
                                                                                In the ﬁrst-level homogenization, the FGBs are considered to be
σ̄i j = Lhom
         i jkl ε̄kl                                               (1)        distributed in the U-10Mo skeleton uniformly and randomly. The

                                                                         2
Y. Li, G. Ding, Z. Xie et al.                                                                                                      Journal of Nuclear Materials 579 (2023) 154359




                                Fig. 2. The sketch of bubble-contained region and no-bubble region and the multi-level homogenization.




Fig. 3. Schematics of the RVE used to determine the bulk modulus of the bubble-contained region: (a) the effective spherical model subjected to bubble pressure and
external pressure, which can be superposed by (b) a model subjected to the bubble pressure as the reference conﬁguration, and (c) a model subjected to the external
hydrostatic pressure. The black dotted lines represent the boundaries of the FGBs and U-10Mo skeleton before the application of the external hydrostatic pressure.



bubble-contained region is regarded as a macroscopically isotropic                    where, R1 and R2 are the radius of the FGBs and the RVE respec-
material. The elastic constants of U-10Mo are taken from Ref. [7].                    tively.
The surfaces of FGBs or pores are subjected to pressures, which de-                       The effective bulk modulus can be obtained by solving the
pend on the bubble volume and the moles of contained ﬁssion gas                       stress and elastic strain ﬁelds of the RVE under the uniform exter-
atoms, obeying the modiﬁed Van der Waal gas law [29]. Two types                       nal hydrostatic pressure. As shown in Fig. 3(a), the external hydro-
of RVE are selected to determinate the effective bulk modulus and                     static pressure Hp is applied on the outer surface S2 of the RVE. The
the effective shear modulus of the bubble-contained region.                           mechanical interaction between the FGBs and the U-10Mo skeleton
                                                                                      on the interface S1 is Pb , corresponding to the bubble pressure of
3.1. Theoretical analysis of effective bulk modulus for the                           FGBs. The global coordinate system is located at the center of the
bubble-contained region                                                               equivalent spherical model. The deformation of the RVE subjected
                                                                                      to the bubble pressure and the external hydrostatic pressure can
  According to the homogenization theory, the effective bulk                          be considered as a combination of two components. Elastic defor-
modulus of a heterogeneous material is expressed as                                   mation caused by the bubble pressure as shown in Fig. 3(b). Elastic
       σ̄ii /3                                                                        deformation caused by the external hydrostatic pressure as shown
K̄ =                                                                        (5)
        ε̄kk                                                                          in Fig. 3(c). To obtain the effective elastic volumetric strain caused
where σ̄ii /3 and ε̄kk are the volumetrically averaged effective hy-                  by the external hydrostatic pressure, the conﬁguration shown in
drostatic stress and effective elastic strain of the RVE caused by                    Fig. 3(b) is regarded as the reference conﬁguration. As mentioned
the external hydrostatic pressure.                                                    above, initial stresses exist in the irradiated fuels. The elastic me-
   For the bubble-contained region composed of the U-10Mo                             chanical responses are corresponding to the additional stresses and
skeleton and the FGBs, the equivalent spherical model in Fig. 3 is                    elastic strains due to the external forces.
selected as RVE to determine the effective bulk modulus, similar as                       The term σ̄ii /3 can be expressed as
                                                                                                                             
that in Ref. [28]. The radius ratio of the FGBs and RVE depends on                                1                       1
                                                                                      σ̄ii /3 =            σ̄ii /3 dV +            σ̄ii /3 dV                                (7)
the local porosity, expressed as                                                                  V   Vm                  V   Vb
R31                                                                                   where, Vm and Vb correspond to the volumes of the U-10Mo skele-
      = fbc                                                                 (6)
R32                                                                                   ton and the FGBs, respectively, and V is the total volume of the

                                                                                  3
Y. Li, G. Ding, Z. Xie et al.                                                                                                                                         Journal of Nuclear Materials 579 (2023) 154359


RVE. It is noted that these stresses are the stress increments in-                                                              induced bubble volume variation can be ignored, so the superim-
duced by the external pressures. Here, the FGBs can be assumed                                                                  position treatment is acceptable.
as an equivalent solid media bearing spherical stresses (negative                                                                  Substituting Eq. (16) to Eq. (15) yields
values of hydrostatic pressure).                                                                                                                                                        
                                                                                                                                     1                           1                      1
   As xi,k = δik , therefore                                                                                                    ε̄kk =      n 1k u 1r n 1k d S +      −n1k u1r n1k dS +     n u 2r n 2k d S
                                                                                                                                     V S1                        V S1                   V S2 2k
                                                        
               1                                  1                                                                                    u 2r
σ̄ii /3 =                    σik xi,k dV +                         σik xi,k dV                                        (8)           =3                                                               (17)
              3V       Vm                        3V           Vb                                                                       R2
where, xi is the coordinate components of material points inside                                                                    For the equivalent spherical model with uniform hydrostatic
the RVE.                                                                                                                        pressure boundary condition, its effective elastic volumetric strain
   Neglecting body forces, the equilibrium differential equations                                                               is 3 times of the average radial strain.
are expressed as σik,k = 0. Applying the divergence theorem to                                                                      Thus, the effective bulk modulus of the RVE is
Eq.(8), the effective hydrostatic stress can be calculated as                                                                             −H p
                                                                                                                             K̄ =                                                                          (18)
σ̄            1
                                 σ          1
                                                                          σ         1
                                                                                                               σ                        3 u 2r /R2
     ii /3 = 3V        s1 n1k ik x1i d S + 3V                 s1 −n1k ik x1i d S + 3V                  s2 n2k ik x2i d S
                                                                                                                                According to the elastic solution of u2r given in Appendix B,
               1                                 1                                1
         =                   T1i x1i dS +                    T1i x1i dS +                     T2i x2i dS                       the effective bulk modulus of the bubble-contained region is de-
              3V        s1                      3V       s1                      3V       s2
                                                                                                                                termined as
                                                                                                                      (9)
                                                                                                                                                 2E (1 − fbc )
                                                                                                                                K̄bc =
where, n1k and n2k are the normal components of S1 and S2 re-                                                                           6 ( 1 − 2v ) + 3 fbc (1 + v
                                                                                                                                                                    )
spectively.                                                                                                                                                                                                   (19)
                                                                                                                                                       fbc
   x1i and x2i are the coordinate components of material points on                                                              =K 1−
                                                                                                                                                     1 −v ) (  bc )
                                                                                                                                              1 − 3(1+  v 1− f
the surfaces S1 and S2 respectively, which can be expressed as
x1i = R1 n 1i                                                                                                                   where, E is the Young’s modulus of the dense U-10Mo skeleton
                                                                                                                    (10)
x2i = R2 n 2i                                                                                                                   with the value of 85,0 0 0 MPa; v is the Poisson’s ratio of the U-
                                                                                                                                10Mo skeleton with the value of 0.34. The inﬂuences of the ﬁssion
T1i is the surface force of the FGBs on the surface S1 , given as                                                              solid products and the intra-granular FGBs on the elastic constants
T1’ i = −Pb n1i                                                                                                     (11)        of the U-10Mo skeleton are ignored [7].
                                                                                                                                    It should be mentioned that the variation of bubble pres-
T1i and T2i are the surface forces of the U-10Mo skeleton on the                                                                sure after applying the external hydrostatic pressure is slight, as
surfaces S1 and S2 , expressed as                                                                                               demonstrated in Appendix B. Consequently, the above superposi-
 T1i = Pb n1i                                                                                                                   tion method can be adopted, and the effective bulk modulus of
                                                                                                                    (12)        porous U-10Mo fuels is independent of bubble pressure. Simulta-
T2i = −H p n2i
                                                                                                                                neously, it is found from Appendix A that no energy dissipation oc-
       Substituting Eqs. (10)∼(12) into Eq. (9) yields                                                                          curs during the homogenization of the RVE. Furthermore, the stress
                                                                                                      
                  PR                                  Pb R1                                    H p R2                           and strain results calculated with the RVE are equal to those with
σ ii /3 = − b 1                       n1i n1i dS +                        n1i n1i dS −                         n2i n2i dS
                                                                                                                                the RVE placed in the inﬁnite effective medium, as pointed out in
                  3V             s1                    3V            s1                         3V        s2
                        H p R2                                                                                                  Ref. [30]. Thus, it can be obtained that the homogenization model-
          =−                            4π R22 = −H p                                                               (13)        ing in this study conforms to the basic conditions of the homoge-
                  3 × 43 π R32
                                                                                                                                nization theory and the generalized self-consistent theory [31,32].
   So, the effective hydrostatic pressure of the equivalent spherical
model is equal to the external hydrostatic pressure applied to the                                                              3.2. Modeling of the effective shear modulus for the bubble-contained
model, unrelated to the bubble pressure. While the bubble pres-                                                                 region
sure is balanced by the surrounding U-10Mo skeleton.
   The term ε̄kk is expressed as                                                                                                   As the effective shear modulus can’t be determined by the
                                                                                                                              equivalent spherical model, we will obtain the effective shear mod-
          1                             1
ε̄kk =                 εkk dV +                  εkk dV                                                             (14)        ulus based on the inter-relationships between different elastic con-
          V    Vm                       V   Vb                                                                                  stants. For the macroscopic isotropic materials, the effective shear
where, εkk depicts the additional elastic volumetric strain ﬁeld                                                                modulus can be calculated byḠ = 3K̄ Ē . The effective Young’s mod-
                                                                                                                                                                           9K̄ −Ē
caused by the external hydrostatic pressure.                                                                                    ulus is usually determined by the FE simulation of uniaxial load-
   Using geometric equation εi j = 12 (ui, j + u j,i ), and applying the                                                        ing based on RVE [33,34]. Then, combined with the effective bulk
divergence theorem to Eq.(14) yields                                                                                            modulus in Section 3.1, the effective shear modulus can be ac-
                                       
         1     1                   1       1                                                                                quired.
ε̄kk =             uk,k + uk,k dV +             uk,k + uk,k dV
         V Vm 2                    V Vb 2                                                                        (15)        3.2.1. Finite element model for performing uniaxial tension
         1                    1                   1
       =      n 1k u 1k d S +      −n1k u1k dS +        n u dS                                                                      To obtain the effective Young’s modulus, a 3D ﬁnite element
         V S1                 V S1                V S2 2k 2k
                                                                                                                                model with FGBs distributed in the U-10Mo matrix randomly is
where, u1k and u2k are the displacement components of material                                                                  considered as RVE shown in Fig. 4. The RVE contains twenty-ﬁve
points on the surfaces S1 and S2 respectively, which can be ex-                                                                 FGBs, and the calculated effective Young’s modulus are approxi-
pressed as                                                                                                                      mately isotropy in the simulation. The FGBs full-ﬁlled with ﬁs-
                                                                                                                                sion gas atoms could be considered as an equivalent solid to im-
u 1k = u 1r n 1k
                                                                                                                    (16)        plement the FE simulation [34,35]. The equivalent constitutive re-
u 2k = u 2r n 2k
                                                                                                                                lations and elastic constants of the equivalent solid given in Ref.
where, u1r = R1 − R1 and u2r = R2 − R2 are the radial displacement                                                            [35] are adopted. The bubble pressure balanced by the surround-
of material points on the surfaces S1 and S2 caused by the external                                                             ing U-10Mo skeleton before uniaxial tension is ignored in the sim-
hydrostatic pressure, respectively. In fact, the elastic deformation                                                            ulation. Displacement δx is applied on the upper surface in the

                                                                                                                            4
Y. Li, G. Ding, Z. Xie et al.                                                                                            Journal of Nuclear Materials 579 (2023) 154359




                                                                                         Fig. 6. The mesh grid of the FE model (a) U-10Mo skeleton (b) the FGBs.




   Fig. 4. The FE model with FGBs randomly distributed in the U-10Mo matrix.




                                                                                     Fig. 7. Effective stress component in x direction and normalized volume of FGBs
                                                                                     evolution results during uniaxial tension.



                                                                                        In the ﬁnite element analysis, the effective strain component in
                                                                                     x direction can be expressed as
                                                                                             δx
                                                                                     ε̄x =                                                                       (22)
                                                                                             a
                                                                                     where, a is the edge length of the RVE shown in Fig. 4.
                 Fig. 5. The diagram of periodic boundary conditions.                   In the ﬁnite element analysis, the effective stress component in
                                                                                     x direction can be calculated as

x direction to result in the elastic deformation of the RVE. As                      σ x = fm σ m
                                                                                                x + f bc σ x
                                                                                                           b

                                                                                               n m m m                     n b
the RVE with randomly distributed FGBs is asymmetric in geom-                                        σ V
                                                                                                  i=1 x,i i
                                                                                                                                   σ
                                                                                                                                   b
                                                                                                                                       Vb
                                                                                                                               j=1 x, j j
etry, displacement constraints are applied to guarantee the peri-                        = n m             n b       + n m         nb                        (23)
odic boundary conditions. The displacement constraints can be ex-
                                                                                                     Vm +
                                                                                                  i=1 i       j=1
                                                                                                                     b
                                                                                                                    Vj        V m + j=1
                                                                                                                           i=1 i
                                                                                                                                          V jb
pressed as                                                                           where, nm and nb are the total element numbers of the U-10Mo
u j+ − u j− = U j − U 0                                                  (20)        skeleton part and the FGBs part (equivalent solid media); σx,i
                                                                                                                                                m and


where, j = 1, 2, 3;u j+ and u j− denote the displacement vectors                     σx,b j are the integration point stress of the ith U-10Mo skeleton ele-
of arbitrary two corresponding points n j+ and n j− on the oppos-                    ment and jth FGBs element along x direction, respectively; Vim and
ing surfaces; U 0 and U j denote the displacement vectors of master                  V jb are the element volume of the ith U-10Mo skeleton element
nodes N 0 and N j . The master nodes and corresponding points are                    and the jth FGBs element, respectively; fm and fbc are the volume
shown in Fig. 5.                                                                     fractions of the U-10Mo skeleton elements and the FGBs elements
    Commercial software ABAQUS is used to realize the FE solution.                   respectively, which can be expressed as
The mesh grid of the U-10Mo skeleton and the FGBs are shown in                                      n m
                                                                                                         Vm
                                                                                                     i=1 i
Fig. 6 with 69,305 C3D10 elements, and the mesh convergence has                      f m = n m          n b
been veriﬁed.                                                                                     V + j=1
                                                                                               i=1 i
                                                                                                    m
                                                                                                              V jb
                                                                                                  n b
                                                                                                         Vb
3.2.2. The results of effective young’s modulus                                      fbc =
                                                                                                      j=1 j
                                                                                              n m m n b                                                        (24)
    Based on the homogenization theory, the effective Young’s                                     V + j=1 V jb
                                                                                               i=1 i
modulus can be expressed as
                                                                                         Fig. 7 gives the contributions of effective stress component in
       σ̄x                                                                           x direction together with the normalized volumes of FGBs during
Ē =                                                                      (21)
       ε̄x                                                                           uniaxial tension. The normalized volume of FGBs is deﬁned as the
where, σ̄x and ε̄x is the effective stress component and effective                   ratio of current FGBs volume to that before uniaxial tension. It can
elastic strain component in x direction.                                             be observed that the volumes of FGBs are scarcely changed dur-

                                                                                 5
Y. Li, G. Ding, Z. Xie et al.                                                                                                    Journal of Nuclear Materials 579 (2023) 154359


                                                                                          Table 1
                                                                                          The effective bulk moduli for the cases with the same macroscopic porosities
                                                                                          and different local porosities.

                                                                                                                    Local porosity       Volume
                                                                                                                    in the               fraction of the   Effective bulk
                                                                                                                    bubble-              bubble-           modulus
                                                                                            Macroscopic             contained            contained         calculated by
                                                                                            porosity f bm           region f bc          regionηbc         Eq.(26) /GPa

                                                                                            0.05                    0.2                  0.25              75.7
                                                                                                                    0.1                  0.5               76.1
                                                                                                                    0.05                 1                 76.1
                                                                                            0.10                    0.25                 0.4               65.0
                                                                                                                    0.2                  0.5               65.4
                                                                                                                    0.1                  1                 65.9
                                                                                            0.20                    0.25                 0.8               49.5
                                                                                                                    0.2                  1                 49.9




                                                                                         4. Determination of the effective elastic constants for overall
                                                                                         U-10Mo fuels
Fig. 8. Comparison of effective shear modulus with different local porosity calcu-
lated in this study and those by the effective shear modulus models in references.
                                                                                             In the second-level homogenization, the bubble-contained re-
                                                                                         gion is considered as the homogenized matrix phase with the ef-
ing uniaxial tension simulation, implying that the change in bub-                        fective elastic constants determined by Eq. (19) and (25). The no-
ble pressure can be neglected and the obtained effective Young’s                         bubble region is treated as the inclusion phase. The overall U-10Mo
modulus is also independent of bubble pressure. As a result, it is                       fuel is homogenized to an isotropic material. Similar to the ho-
reasonable that the nominal Young’s modulus and shear modulus                            mogenization operation of bubble-contained region, the equivalent
of equivalent solid media are considered to be zero. As shown in                         spherical model and random distribution model are adopted to de-
Fig. 7, the effective stress component in x direction of the RVE                         termine the effective elastic constants of overall U-10Mo fuels con-
is only contributed by the U-10Mo skeleton part. The effective                           sisting of the no-bubble region and the bubble-contained region.
Young’s modulus of the RVE for the case of fbc = 15% is about
62.90 GPa, 74% of the Young’s modulus of the U-10Mo skeleton.                            4.1. Models for the effective bulk modulus of overall U-10Mo fuels

                                                                                             As shown in Section 3.1, the effective bulk modulus of equiva-
3.2.3. Models for effective shear modulus                                                lent spherical model is determined by the relationship of the exter-
    Cases with different volume fraction of FGBs are simulated to                        nal hydrostatic pressure and the radial displacement caused by the
calculate the effective Young’s modulus of the bubble-contained re-                      external hydrostatic pressure. For the U-10Mo fuels comprising the
gion. The effective shear modulus of the bubble-contained region                         no-bubble region and the bubble-contained region, the same theo-
are determined by the effective bulk modulus calculated by Eq.(19)                       retical analysis method can be adopted. The radial displacement of
and the effective Young’s modulus calculated by the FE simulation.                       the corresponding equivalent spherical model (seen in Fig. 2) is de-
    Fig. 8 presents the effective shear modulus of the bubble-                           rived in Appendix B. According to the elastic solution of the radial
contained region calculated in this study, together with values cal-                     displacement, the effective bulk modulus for the overall U-10Mo
culated by the models in the Refs. [22–24,26]. The detailed expres-                      fuels is expressed as
sions of the models are given in Appendix D. According to the
above analysis, the bulk modulus and Young’s modulus of FGBs                                         1 + v̄bc + 2(1 − 2v̄bc )K̄bc /K ηbc + 2(1 − 2v̄bc )(1 − ηbc )
                                                                                         K̄ = K̄bc
can be regarded as zero. Thus, the shear modulus of the inclusion                                  ηbc (1 + v̄bc ) + (1 − ηbc )(1 + v̄bc )K̄bc /K + 2(1 − 2v̄bc )K̄bc /K
phase is set as zero in the Mori-Tanaka model [23,24] and Dilute                                  ⎡                                ⎤
model [24]. It can be noted that the effective shear modulus in this                                       (1 − ηbc ) K/K̄bc − 1
study is in good agreement with the results obtained with Mori-                            = K̄bc ⎣1 +          1+v̄bc               ⎦
Tanaka model [23,24] and Power-law model [22]. The maximum                                              1+              η K/K̄bc − 1
                                                                                                             3 (1−v̄bc ) bc
relative difference between the results in this study and those of                                                                                                          (26)
the Mori-Tanaka model is less than 1.53%. In the range of low
porosity, the results obtained with Dilute model [24] and Expo-                                             3K̄bc −2Ḡbc
                                                                                         where, v̄bc =                     is the effective Poisson’s ratio of bubble-
                                                                                                            6K̄bc +2Ḡbc
nential model [22] agree well with the results in this study. With
                                                                                         contained region.
the rise of porosity, the deviations of Dilute model and Exponen-
                                                                                            The local porosity can be obtained with the model in Ref. [36].
tial model results increase, while the former predicts larger val-
                                                                                         The effective bulk moduli for the cases with the same macro-
ues and the later predicts smaller values. The Ramakrishnan model
                                                                                         scopic porosities and different local porosities are compared in
[26] predicts smaller values of effective shear modulus throughout
                                                                                         Table 1. It can be noted that the obtained effective bulk moduli
the considered porosity range.
                                                                                         are close. Thus, the effective bulk modulus of overall U-10Mo fuels
    So, the effective shear modulus of the bubble-contained region
                                                                                         is mainly dominated by the macroscale porosity. Assuming homo-
can be evaluated by the Mori-Tanaka model according to the local
                                                                                         geneous distribution of the FGBs in the overall U-10Mo fuels, with
porosity, expressed as
                                                                                         the macroscopic porosity fbm the effective bulk modulus of irradi-
                                                                                       ated U-10Mo fuels during recrystallization can be calculated as
                                fbc
Ḡbc = G 1 −                      ν)
                                                                            (25)                                                    
                    1 − 215(4(1−5
                                −ν ) (
                                       1 − fbc )                                                                      fbm
                                                                                         K̄ = K 1 −                                                                         (27)
                                                                                                               1 −v ) (  bm )
                                                                                                        1 − 3(1+  v 1− f
    The nominal shear modulus of FGBs is considered as zero.

                                                                                     6
Y. Li, G. Ding, Z. Xie et al.                                                                                                  Journal of Nuclear Materials 579 (2023) 154359


                                                                                          Table 2
                                                                                          Cases with different volume fraction of the bubble-contained region and differ-
                                                                                          ent local porosity to calculate the effective shear modulus.

                                                                                            Volume fraction of the      Local porosity in the
                                                                                            bubble-contained            bubble-contained             Macroscopic
                                                                                            region ηbc                  region f bc                  porosity f bm

                                                                                            0.00                        0.00                         0.00
                                                                                            0.85                        0.10                         0.085
                                                                                            0.85                        0.25                         0.212
                                                                                            1.00                        0.10                         0.10
                                                                                            1.00                        0.25                         0.25




Fig. 9. Comparison of the results of effective bulk modulus for the overall U-10Mo
fuels calculated by different models.



    The macroscopic porosity is used for the porosity or inclusion
volume fraction in the models given in Appendix D. The bulk mod-
ulus of the inclusion phase is considered as zero. Fig. 9 gives the
comparison of the obtained effective bulk modulus for the over-
all U-10Mo fuels by Eq.(27) with those from different models in
the references. It should be mentioned that the degenerated Mori-
Tanaka model [23,24] with the elastic constants set as zero is the
same as Eq. (27), leading to the same results. It is found that Di-
lute model [24] overestimate the values. While, the Ramakrish-
nan model [26] underestimate the values of effective bulk modu-
lus throughout the considered macroscopic porosity range, and the                        Fig. 10. Comparison of effective shear modulus for the overall U-10Mo fuels in this
                                                                                         study with those from different models in the references.
differences are enlarged with the increase of macroscopic poros-
ity. These differences might be caused by the adopted calcula-
tion method, where the external pressure of the porous solid is
ampliﬁed with 1/(1 − fbm ) to act as the pressure applied on the
outer surface of the RVE (same as that in Fig. 3). As conﬁrmed in                        with the results obtained in this study. As a result, the effective
Section 3.1, the external hydrostatic pressure of the RVE should be                      shear modulus for the overall U-10Mo fuels is demonstrated to rely
equal to the external pressure of the porous solid. The ampliﬁca-                        mainly on the macroscopic porosity.
tion of the pressure on the RVE would duplicate the effect of the                            It can be obtained that the effective bulk modulus and effective
macroscopic porosity, needing to be removed. So, the effective bulk                      shear modulus of irradiated U-10Mo fuels during irradiation can be
modulus obtained by the Ramakrishnan model [26] is actually re-                          determined by the macroscopic porosity and the elastic constants
duced with the factor of (1 − fbm ).                                                     of the U-10Mo skeleton as follows:
                                                                                                                          
                                                                                                           fbm                         1+v
                                                                                         K̄ = K 1 −                    ,          α=
4.2. Modeling of the effective shear modulus for overall U-10Mo fuels                               1 − α (1 − fbm )                 3 (1 − v )
                                                                                                                                                                     (28)
                                                                                                          fbm                        2 ( 4 − 5ν )
    Similar to the solution strategy of the effective shear modu-                        Ḡ = G 1 −                    ,          β=
lus for the bubble-contained region, a 3D FE model with the no-
                                                                                                    1 − β (1 − fbm )                 15(1 − ν )
bubble region randomly distributed in the bubbles-contained re-                              According to the inter-relationships between different effective
gion randomly is considered here. The boundary conditions are the                        elastic constants, the effective Young’s modulus and the Poisson’s
same as those shown in Section 3.2.1, while the FGBs part is occu-                       ratio are given by
pied by the no-bubble region, and the matrix are occupied by the
homogenized bubble-contained region. The overall effective shear                                                3E (1 − fbm )
                                                                                         Ē =                                                   ,
modulus is calculated based on the FE results of the overall effec-                             2(1 + v )(1 + bg fbm ) + (1 − 2v )(1 + bk fbm )
tive Young’s modulus and the overall effective bulk modulus deter-                            (1 + v)(1 + bg fbm ) − (1 − 2v)(1 + bk fbm )
mined by Eq. (26).                                                                       v̄ =                                                ,                         (29)
                                                                                             2(1 + v )(1 + bg fbm ) + (1 − 2v )(1 + bk fbm )
    Different cases with varied volume fractions of the bubble-
                                                                                                  1+v             8 − 10v
contained region and local porosity are investigated, as listed in                       bk =              , bg =
                                                                                              2 ( 1 − 2v )         7 − 5v
Table 2. Fig. 10 shows the comparison of the effective shear mod-
ulus for the overall U-10Mo fuels in this study with those from                             Fig. 11 presents the comparison of the normalized effective
the models in the references [22–24,26]. The treatment is the same                       shear modulus Ḡ/G calculated by Eq. (28) and several models in
as that in Section 4.1, the porosity or inclusion volume fraction in                     the references for porous materials with the experimental results
the models given in Appendix D is displaced with the macroscopic                         of aluminum foam [37]. It can be found that the effective shear
porosity and the shear modulus of the inclusion phase are con-                           modulus results calculated by Eq. (28) agree well with the experi-
sidered as zero. It can be noted that the results of effective shear                     mental results, while the other models tend to underestimate the
modulus calculated by the Mori-Tanaka model [23,24] match well                           values.

                                                                                     7
Y. Li, G. Ding, Z. Xie et al.                                                                                            Journal of Nuclear Materials 579 (2023) 154359


                                                                                          5. Conclusion

                                                                                              In this study, the effective elastic constants of irradiated U-
                                                                                          10Mo fuels with distributed FGBs are investigated based on ho-
                                                                                          mogenization theory. The irradiated U-10Mo fuels are divided into
                                                                                          the no-bubble region and the bubble-contained region during grain
                                                                                          recrystallization, and a multi-level homogenization method is pro-
                                                                                          posed to determine the effective elastic constants of porous U-
                                                                                          10Mo fuels with pore pressures. Different RVE models represent-
                                                                                          ing the critical grain-scale features are selected to determine the
                                                                                          macroscopic isotropic effective elastic constants. The effective bulk
                                                                                          modulus of irradiated U-10Mo fuels is determined with the de-
                                                                                          veloped theoretical analysis method for the equivalent spherical
                                                                                          model. The random distribution model is adopted and the uniax-
                                                                                          ial tension is simulated by FE method to ﬁrstly obtain the effective
                                                                                          Young’s modulus. Then, the effective shear modulus is calculated
                                                                                          by the obtained effective bulk modulus and the effective Young’s
                                                                                          modulus. The results of effective elastic constants determined in
Fig. 11. Comparison of the normalized effective shear modulus calculated by differ-       this study are also compared with those calculated by other mod-
ent models and the experimental results of aluminum foam.                                 els in the references and some available experimental data. The
                                                                                          main conclusions are as follows:

                                                                                          (1) The derived model of effective bulk modulus is the same as
                                                                                              the degenerated Mori-Tanaka model, with the bulk modulus
                                                                                              and shear modulus of inclusion phase set as zero. The effec-
                                                                                              tive elastic constants of irradiated U-10Mo fuels determined by
                                                                                              the multi-level homogenization method are demonstrated to
                                                                                              mainly depend on the macroscopically average porosity and the
                                                                                              elastic constants of the U-10Mo skeleton.
                                                                                          (2) The variations of bubble pressure induced by the elastic defor-
                                                                                              mations of the fuel skeleton can be neglected, leading to the
                                                                                              fact that the effective elastic constants of irradiated U-10Mo fu-
                                                                                              els are independent of internal bubble pressure.
                                                                                          (3) The results of effective Young’s modulus calculated by the de-
                                                                                              veloped models in this study agree well with the available ex-
                                                                                              perimental results of irradiated U-10Mo fuels, which indicates
                                                                                              that the developed models are effective and reasonable.

Fig. 12. Comparison of the effective Young’s modulus for the irradiated porous U-            In the future, with the models for local porosity and
10Mo fuels calculated by the mathematic model and the test results of L1P773.
                                                                                          macroscopic porosity of U-10Mo fuels, the multi-scale thermo-
                                                                                          mechanical coupling simulation for various fuel elements and as-
    Fig. 12 presents the comparison of the effective Young’s modu-                        semblies could be implemented, which will provide support for
lus for irradiated U-10Mo fuels calculated by Eq. (29) and the test                       their optimal design.
results of fuels in L1P773 [3]. For the specimens sectioned from
different locations in L1P773, the measured results of effective
                                                                                          Declaration of Competing Interest
Young’s modulus are 57 GPa, 64 GPa and 65 GPa, respectively. The
reported porosity in Ref. [3] is 13.7% for irradiated L1P773 with-
                                                                                              The authors declare that they have no known competing ﬁnan-
out considering the location dependence. So, the reported poros-
                                                                                          cial interests or personal relationships that could have appeared to
ity data is suitable for some speciﬁc locations. With the reported
                                                                                          inﬂuence the work reported in this paper.
porosity substituted into Eq. (29), the obtained effective Young’s
modulus is 64.5 GPa, very close to the measurements of 64 GPa
and 65 GPa. It can be speculated that the macroscopic porosi-                             CRediT authorship contribution statement
ties of the corresponding specimens are close to 13.7%. The speci-
men with the measured Young’s modulus of 57 GPa is possible to                                Yong Li: Methodology, Software, Validation, Formal analysis, In-
have a different macroscopic porosity. A potential conclusion can                         vestigation, Data curation, Writing – original draft, Visualization.
be drawn that the elastic modulus of the U-10Mo skeleton is de-                           Guochen Ding: Validation, Formal analysis, Visualization. Zhexiao
graded due to nuclear ﬁssions and inner material damage, if the                           Xie: Software, Formal analysis. Jing Zhang: Methodology, Formal
actual macroscopic porosity is lower than the reported value. In                          analysis, Validation. Xiaobin Jian: Software, Formal analysis, Val-
a word, the predictions in this study agree well with the experi-                         idation. Shurong Ding: Conceptualization, Methodology, Software,
ment results overall, validating the effectiveness and reasonability                      Resources, Writing – review & editing, Supervision, Project admin-
of the developed models. If the macroscopic porosities of fuels dur-                      istration. Yuanming Li: Conceptualization, Methodology, Supervi-
ing in-reactor irradiation are known, the elastic constants can be                        sion, Project administration.
calculated out with Eq. (28) or (29). The developed models in this
study will be favorable for the implement of multi-scale thermo-                          Data availability
mechanical coupling simulation of nuclear fuel elements or assem-
blies.                                                                                       The authors do not have permission to share data.

                                                                                      8
Y. Li, G. Ding, Z. Xie et al.                                                                                              Journal of Nuclear Materials 579 (2023) 154359


Acknowledgment

   The authors are very grateful for the supports of National
Natural Science Foundation of China (No. 12132005, 12102094,
12135008), the supports of the foundation from Science and
Technology on Reactor System Design Technology Laboratory.
This study is also sponsored by Shanghai Sailing Program
(21YF1402200).

Appendix A The strain energy increment of the homogenized
RVE based on the equivalent spherical model

    According to homogenization theory, the macroscopic effective
mechanical properties of composite materials can be obtained by
the RVE. Fig. A.1 shows the homogenization process of the RVE
based on the equivalent spherical model. The equivalent spherical
shell model is regarded as the RVE of the bubble-contained region,
homogenized as the equivalent spherical body. For the spherical                      Fig. B.1. The sketch of the hollow sphere for the calculation of the radial displace-
                                                                                     ment caused by the external hydrostatic pressure.
body subjected to uniform external pressure, uniform hydrostatic
stress and strain ﬁelds arise satisfying all the governing equations.
                                                                                     the equivalent spherical model caused by the external hydrostatic
                                                                                     pressure H p can be determined by the elastic solution of the hol-
                                                                                     low sphere as shown in Fig. B.1.
                                                                                        For the hollow sphere with elastic deformation caused by the
                                                                                     external hydrostatic pressure, its differential governing equations
                                                                                     can be expressed as
                                                                                     ∂σr 2σr − σθ − σϕ
                                                                                          +                     =0
                                                                                      ∂r             r
                                                                                           ∂u             u           u                                  (B.1)
                                                                                     εr = r , εθ = r , εϕ = r
Fig. A.1. The sketch of homogenization process for RVE based on the equivalent
                                                                                            ∂r        r              r                              
spherical model.
                                                                                     σ r = 2 Gε r + λ ε r + 2 ε θ , σ θ = σ ϕ = 2 Gε θ + λ ε r + 2 ε θ
                                                                                     where, σr , σθ and σϕ are the normal stresses in the global coordi-
   The uniform stress and strain tensors in the effective medium                     nate system; r is the radial coordinate; ur is the radial displace-
caused by the external hydrostatic pressure H p are spherical ten-                   ment; εr , εθ and εϕ are the normal strains in spherical coordi-
sors. Thus, the effective stress and strain components of the RVE                    nates. G and λ are the lame constants.
can be expressed as                                                                     The boundary conditions are
          σ̄kk                    ε̄kk                                               σr |R1 = 0,        σr |R2 = −Hp
σ̄i j =          δi j ; ε̄i j =          δi j                           (A.1)                                                                                      (B.2)
           3                       3
where, σ̄kk and ε̄kk are the effective ﬁrst invariant of stress and                      The radial displacement can be solved as
strain tensor in RVE deﬁned in Section 3.1.                                                        B
    Substituting Eqs. (13) and (17) to Eq. (A.1), the effective stress
                                                                                     ur = Ar +                                                                     (B.3)
                                                                                                   r2
and strain components caused by H p are
                                                                                     where, A = − E (11−2 v H ; B = − 1+v R3 H ; E and v are the
                                                                                                       − fbc ) p     2E (1− fbc ) 1 p
                                u
σ̄i j = −Hp δi j ;       ε̄i j = 2r δi j                                (A.2)        Young’s modulus and Poisson’s ratio of the U-10Mo skeleton; fbc
                                 R2                                                  is the volume fraction of the FGBs, also termed as local porosity.
    The strain energy increment in the effective medium caused by                        The volume ratio of the FGBs after the application of the exter-
H p is                                                                               nal hydrostatic pressure is
                                                                                                                                            3
1                                                                                    Vb    (R1 + ur (R1 ))3       3 (1 − v ) H p
  σ̄i j ε̄i jV = − 12 Hp δi j uR2r δi jV                                                 =                  = 1−                                                   (B.4)
2                                2                                                   Vb0         R31             2(1 − fbc ) E
               = − 32 H p uR2r 43 π R32                                 (A.3)
                             2
                                                                                     where, Vb0 and Vb is the volume of the FGBs before and after the
               = −2π R22 H p u2r
                                                                                     application of the external hydrostatic pressure.
   It is noted that the right term of Eq. (A.3) is the work of H p . So,                 The bubble pressure varies with the volume of the FGBs, satis-
there is no energy dissipation during the homogenization process                     fying the modiﬁed Van der Waal gas law, namely
for the RVE. If the RVE is placed in an inﬁnite effective medium,
                                                                                     Pb (V − hs bv N ) = NkT                                                       (B.5)
the average deformation of the RVE is also equal to that of the
inﬁnite body [30].                                                                   where, Pb is the bubble pressure in Pa; T is the temperature in
                                                                                     K; k is Boltzmann constant with a value of 1.38×10−23 J/K; hs is
Appendix B Elastic solution of radial displacement of the                            the ﬁtting parameter with a value of 0.6; bv is the Van der Waals
equivalent spherical model for the bubble-contained region                           constant of 8.5 × 10−29 m3 /atom for Xe.
                                                                                        So, the ratio of the bubble pressure after and before the appli-
    The state of the equivalent spherical model subjected to the                     cation of the external hydrostatic pressure can be expressed as
bubble pressure is taken for the reference conﬁguration as shown
in Fig. 3(b). The global coordinate system is located at the center                  Pb              kT /Pb0
                                                                                         = V                                                                       (B.6)
of the equivalent spherical model. Thus, the radial displacement of                  Pb0    b
                                                                                              (kT /Pb0 + hs bv ) − hs bv
                                                                                             Vb0

                                                                                 9
Y. Li, G. Ding, Z. Xie et al.                                                                                                                    Journal of Nuclear Materials 579 (2023) 154359


                  Table B.1
                  Ratios of the bubble pressure calculated according to Eq. (B.4) and Eq. (B.6) for different causes.

                    Local porosity in the                                        Bubble pressure before the
                    bubble-contained                                             application of the external           Volume ratios of the             Ratios of bubble
                    region f bc                     Temperature T/K              hydrostatic Pb0 /MPa                  FGBs Vb /Vb0                     pressure Pb /Pb0

                    0.10                            373                          10                                    0.9923                           1.0078
                    0.25                            373                          100                                   0.9907                           1.0094
                    0.10                            473                          10                                    0.9923                           1.0078
                    0.25                            473                          100                                   0.9907                           1.0094




   As the temperature, bubble pressure and local porosities vary                                     where, Ēbc and v̄bc are the effective Young’s modulus and Poisson’s
with the irradiation time and locations [12], cases with different                                   ratio of the homogenized bubble-contained region; E and v are the
temperatures, bubble pressure and local porosities are tested to                                     Young’s modulus and Poisson’s ratio of the U-10Mo skeleton.
evaluate the bubble pressure changes of the FGBs caused by the                                           Considering no fractures between the no-bubble region and the
elastic deformation of U-10Mo skeleton. The external hydrostatic                                     bubble-contained region, the radial displacement on the interface
pressure is set as 200 MPa. Ratios of the bubble pressure calculated                                 is continuous, denoted as
according to Eq. (B.4) and Eq. (B.6) for different causes are sum-                                                                      ⎡                                              ⎤
                                                                                                                                     1−2v̄bcR3           −2v̄bc    R3
marized in Table B.1. It can be noted that the relative bubble pres-                                 −P              1 + v̄bc 2R3 + 1+v̄bc
                                                                                                                                2                 1
                                                                                                                                                     + 11+
sure changes after applying the external hydrostatic are less than                                      (1 − 2v)R1 =         ⎣     3
                                                                                                                                             P−
                                                                                                                                                2R 3       v̄bc
                                                                                                                                                                H p ⎦R 1
                                                                                                     E                 Ēbc       R2                    R3
1%. The minimal changes in the bubble pressure have pretty small                                                                     −1          R31
                                                                                                                                                    1− 1                    R32
inﬂuences on the radial displacement of the equivalent spherical
                                                                                                                                                                                           (C.3)
model in the elastic deformation stage. So, the radial displacement
of the equivalent spherical model on the outer surface caused by                                        Thus, the mechanical interaction between the no-bubble region
the external hydrostatic pressure can be expressed as                                                and bubble-contained region is expressed as
                                                         
                        1 − 2v       f (1 + v )                                                                                 1     −2v̄bc
                                                                                                                                  + 11+
u2r = −H p                         + bc           R2                                   (B.7)         P=
                                                                                                                                2       v̄bc
                                                                                                                                                                 Hp
                      E (1 − fbc )  2E (1 − fbc )                                                                 −2v̄bc
                                                                                                            1
                                                                                                            2
                                                                                                              + 11+ (1 − ηbc ) + 1+E v 1+Ēbcv̄bc 11+
                                                                                                                    v̄bc                              v ηbc
                                                                                                                                                    −2v

                                                                                                                                 3(1 − v̄bc )
Appendix C Elastic solution of radial displacement of the                                              =                                                               Hp
                                                                                                         1 + v̄bc + 2(1 − 2v̄bc )K̄bc /K ηbc + 2(1 − 2v̄bc )(1 − ηbc )
equivalent spherical model for the overall U-10Mo fuels
                                                                                                                                                                                           (C.4)
    The equivalent spherical model for the overall U-10Mo fuels                                      where, K̄bc is the effective bulk modulus of the homogenized
consist of the no-bubble region and the homogenized bubble-                                          bubble-contained region; K is the bulk modulus of the U-10Mo
contained region, as show in Fig. C.2. The global coordinate system                                  skeleton; ηbc is the volume fraction of the bubble-contained region.
is located at the center of the equivalent spherical model.                                              Submit Eq. (C.4) to Eq. (C.2), the radial displacement of the
    The differential governing equations are same to Eq. (B.1). The                                  equivalent spherical model on the outer surface caused by the ex-
boundary conditions of the homogenized bubbled-contained re-                                         ternal hydrostatic pressure is
gion and the no-bubble region are
                                                                                                                                                                                               
⎧                                                                                                             Hp     ηbc (1 + v̄bc ) + (1 − ηbc )(1 + v̄bc )K̄bc /K + 2(1 − 2v̄bc )v̄bc K̄bc /K
                                                                                                     u2r = −                                                                                   R2
⎨ σr |R1 = −P,              σr |R2 = −Hp ,        o f the homogenized bubble                                 3K̄bc                3(1 − v̄bc ) + 2(1 − 2v̄bc )ηbc K̄bc /K − 1
                                                     −contained region                  (C.1)                                                                                              (C.5)
⎩
    σr |R1 = −P,                                  o f the no − bubble region
where, P is the mechanical interaction between the no-bubble re-
gion and bubble-contained region, which needs to be solved.                                          Appendix D. Some effective elastic constants models in the
   According the classical theory of elasticity, the radial displace-                                references
ments of the bubble-contained region and the no-bubble region
are derived as                                                                                           Researchers have proposed different mathematic models of ef-
                      ⎡                                              ⎤                               fective bulk modulus K̄ and effective shear modulus Ḡ for porous
                          R32      −2v̄bc        R31      −2v̄bc                                     materials and two-phase composite materials according to theo-
        1 + v̄bc               + 11+                  + 11+
ur =                  ⎣   2R 3       v̄bc
                                            P−
                                                 2R 3       v̄bc
                                                                   H p ⎦r,   R1 ≤ r ≤ R2             retical and experimental research. Some of the mathematic models
           Ēbc              R32                          R3
                             R31
                                 −1                 1 − R13                                          are presented as follows
                                                           2
        −P                                                                                               Ramakrishnan model [26]:
ur =       (1 − 2v)r,             0 ≤ r ≤ R1
        E                                                                                                          Km (1 − ϕ )2
                                                                                                     K̄ =
                                                                                       (C.2)              1 + ϕ (1 + vm )/[2(1 − 2vm )]
                                                                                                                                                                                           (D.1)
                                                                                                                    Gm (1 − ϕ )2
                                                                                                     Ḡ =
                                                                                                          1 + ϕ (11 − 19vm )/[4(1 + vm )]
                                                                                                     where, Km and Gm are the bulk modulus and shear modulus of the
                                                                                                     solid skeleton or the matrix phase; ϕ is the macroscopic porosity.
                                                                                                     Ramakrishnan model is proposed for the porous solid.
                                                                                                         Power-law model [22]:
                                                                                                                                       3 ( 1 − vm )
                                                                                                     K̄ = Km (1 − ϕ )nk ,        nk =
Fig. C.2. The sketch of the equivalent spherical model for the U-10Mo fuel during                                                     2 ( 1 − 2vm )                                        (D.2)
recrystallization comprised of the no-bubble region and the homogenized bubble-                                                       15(1 − vm )
contained region.                                                                                    Ḡ = Gm (1 − ϕ )ng ,        ng =
                                                                                                                                        7 − 5vm

                                                                                                10
Y. Li, G. Ding, Z. Xie et al.                                                                                                                 Journal of Nuclear Materials 579 (2023) 154359


    Exponential model [22]:                                                                            [11] B.D. Miller, J. Gan, D.D. Keiser, A.B. Robinson, J.F. Jue, J.W. Madden,
                  −n ϕ                                                                                    P.G. Medvedev, Transmission electron microscopy characterization of the ﬁs-
                        k                                                                                   sion gas bubble superlattice in irradiated U–7 wt%Mo dispersion fuels, J. Nucl.
K̄ = Km exp
                     −ϕ
                  1−n                                                                    (D.3)
                                                                                                            Mater. 458 (2015) 115–121.
                       ϕg                                                                              [12] D. Salvato, A. Leenaers, S. Van den Berghe, C. Detavernier, Pore pressure esti-
Ḡ = Gm exp
                    1−ϕ
                                                                                                            mation in irradiated UMo, J. Nucl. Mater. 510 (2018) 472–483.
                                                                                                       [13] Y.S. Kim, G.L. Hofman, J.S. Cheon, Recrystallization and ﬁssion-gas-bubble
    Dilute models [24]:                                                                                     swelling of U–Mo fuel, J. Nucl. Mater. 436 (2013) 14–22.
                                                                                                       [14] J. Rest, Evolution of ﬁssion-gas-bubble-size distribution in recrystallized
                                                                                                        U–10Mo nuclear fuel, J. Nucl. Mater. 407 (2010) 55–58.
                                         V f K f /Km − 1                                               [15] E.S. Perdahcıoğlu, H.J.M. Geijselaers, Constitutive modeling of two phase ma-
K̄ = Km 1 +                                                                                             terials using the mean ﬁeld method for homogenization, Int. J. Mater. Form. 4
                    1 + (1 + vm )/3(1 − vm ) − V f                  K f /Km − 1                             (2011) 93–102.
                                                                                                   [16] I. Doghri, C. Friebel, Effective elasto-plastic properties of inclusion-reinforced
                                              V f G f /Gm − 1                                               composites. Study of shape, orientation and cyclic response, Mech. Mater. 37
Ḡ = Gm 1 +                                                                                             (2005) 45–68.
                    1 + 2(4 − 5vm )/15(1 − vm ) − V f                   G f /Gm − 1                    [17] J. Zhang, J. Zhang, H. Wang, H. Wei, C. Tang, C. Lu, S. Ding, Y. Li, Research on
                                                                                                            the homogenized postirradiation elastoplastic constitutive relations for com-
                                                                                          (D.4)             posite nuclear fuels, Front. Mater. 8 (2021).
                                                                                                       [18] R. Hill, A self-consistent mechanics of composite materials - sciencedirect, J.
where, K f and G f are the bulk modulus and shear modulus of the                                            Mech. Phys. Solids 13 (1965) 213–222.
inclusion phase; vm is the Poisson’s ratio of the matrix phase; V f                                    [19] J.D. Eshelby, The determination of the elastic ﬁeld of an ellipsoidal inclu-
is the volume fraction of the inclusion phase.                                                              sion, and related problems, Proc. R. Soc. Lond. A Math. Phys. Sci. 241 (1957)
                                                                                                            376–396.
    Mori-Tanaka model [23,24]:                                                                         [20] A. Reuss, Berechung der Fliessgrenze von Mischkristallen, ZAMM J. Appl. Math.
                                                                                                        Mech. Z. Angew. Math. Mech. 9 (1929) 49–58.
                                             ( 1 + νm )
                                V f K f /Km − 1                                                        [21] W. Voigt, Ueber die beziehung zwischen den beiden elasticittsconstanten
K̄ = Km 1 +                            
                                      , α=                                                                 isotroper Krper, Ann. Phys. Berlin 274 (2006) 573–587.
                    1 + α 1 − Vf            3 ( 1 − νm )
                                             K f /Km − 1                                               [22] W. Pabst, T. Uhlířová, E. Gregorová, Shear and bulk moduli of isotropic
                                                                                                        porous and cellular alumina ceramics predicted from thermal conductivity via
                 V f G f /Gm − 1               2 ( 4 − 5 νm )                                               cross-property relations, Ceram. Int. 44 (2018) 8100–8108.
Ḡ = Gm 1 +                        , β=                                                            [23] T. Mori, K. Tanaka, Average stress in matrix and average elastic energy of ma-
            1 + β 1 − V f G f /Gm − 1          15(1 − νm )                                                  terials with misﬁtting inclusions, Acta Metall. 21 (1973) 571–574.
                                                                                                       [24] K. Huang, Y. Huang, Solid Constitutive Relations, Tsinghua University, 1999.
                                                                                          (D.5)        [25] C.T. Sun, R.S. Vaidya, Prediction of composite properties from a representative
                                                                                                            volume element, Compos. Sci. Technol. 56 (1996) 171–179.
                                                                                                       [26] N. Ramakrishnan, V.S. Arunachalam, Effective elastic moduli of porous solids,
References                                                                                                  J. Mater. Sci. 25 (1990) 3930–3937.
                                                                                                       [27] E.A. Dean, J.A. Lopez, Empirical dependence of elastic moduli on porosity for
 [1] X. Jian, X. Kong, S. Ding, A mesoscale stress model for irradiated U 10Mo                              ceramic materials, J. Am. Ceram. Soc. 66 (1983) 366–370.
     monolithic fuels based on evolution of volume fraction/radius/internal pres-                      [28] Xiangzhe Kong, Xiaobin Jian, Feng Yan, et al., Macro-mesoscale in-pile ther-
     sure of bubbles, Nucl. Eng. Technol. 51 (2019) 1575–1588.                                              mal-mechanical behavior simulation of a UMo/Zr monolithic fuel plate, Front.
 [2] M.K. Meyer, G.L. Hofman, S.L. Hayes, C.R. Clark, T.C. Wiencek, J.L. Snelgrove,                         Energy Res. 9 (2022) 1–14.
     R.V. Strain, K.H. Kim, Low-temperature irradiation behavior of uranium–molyb-                     [29] X. Jian, F. Yan, X. Kong, Y. Li, S. Ding, Further development of the ﬁssion gas
     denum alloy dispersion fuel, J. Nucl. Mater. 304 (2002) 221–236.                                       swelling model for U-10Mo fuels, J. Nucl. Mater. 565 (2022) 1–13.
 [3] J.L. Schulthess, W.R. Lloyd, B. Rabin, K. Wheeler, T.W. Walters, Mechanical                       [30] Hongyang Wei, Xiaobin Jian, Shurong Ding, A model of gas-induced effective
     properties of irradiated U Mo alloy fuel, J. Nucl. Mater. 515 (2019) 91–106.                           expansion strain for porous carbon materials in irradiation environments, J.
 [4] J. Gan, D.D. Keiser, B.D. Miller, A.B. Robinson, J.F. Jue, P. Medvedev, D.M. Wachs,                    Nucl. Mater. 515 (2019) 338–353.
     TEM characterization of U–7Mo/Al–2Si dispersion fuel irradiated to intermedi-                     [31] R. Hill, The elastic behaviour of a crystalline aggregate, Proc. Phys. Soc. A 65
     ate and high ﬁssion densities, J. Nucl. Mater. 424 (2012) 43–50.                                       (349) (1952) 349–354.
 [5] A. Leenaers, S. Van den Berghe, C. Detavernier, Surface engineering of low en-                    [32] R.M. Christensen, K.H. Lo, Solutions for effective shear properties in three
     riched uranium–molybdenum, J. Nucl. Mater. 440 (2013) 220–228.                                         phase sphere and cylinder models, J. Mech. Phys. Solids 27 (1979) 315–330.
 [6] R. Jungwirth, H. Palancher, A. Bonnin, C. Bertrand-Drira, C. Borca,                               [33] J. Zhang, S. Ding, Mesoscale simulation research on the homogenized elasto–
     V. Honkimäki, C. Jarousse, B. Stepnik, S.H. Park, X. Iltis, W.W. Schmahl,                              plastic behavior of FeCrAl alloys, Mater. Today Commun. 22 (2020) 1–12.
     W. Petry, Microstructure of as-fabricated UMo/Al(Si) plates prepared with                         [34] Z. Zhou, M. Chen, Predicting effective moduli of a Z-reinforced core with cav-
     ground and atomized powder, J. Nucl. Mater. 438 (2013) 246–260.                                        ities using a novel theoretical approach and a micromechanics ﬁnite element
 [7] Y.S. Kim, G.L. Hofman, J.S. Cheon, A.B. Robinson, D.M. Wachs, Fission induced                          method, Int. J. Mech. Sci. 105085 (2019) 161–162.
     swelling and creep of U–Mo alloy fuel, J. Nucl. Mater. 437 (2013) 37–46.                          [35] Y.C.Y.H. JIANG, A method for 3D simulation of internal gas effects on ther-
 [8] D.E. Burkes, A.M. Casella, A.J. Casella, E.C. Buck, K.N. Pool, P.J. MacFarlan,                         mal-mechanical behaviors in nuclear fuel elements, Nucl. Sci. Tech. 22 (2011)
     M.K. Edwards, F.N. Smith, Thermal properties of U–Mo alloys irradiated to                              185–192.
     moderate burnup and power, J. Nucl. Mater. 464 (2015) 331–341.                                    [36] X. Jian, J. Zhang, Y. Li, S. Ding, Skeleton-creep based bubble growth model and
 [9] Y.S. Kim, G.L. Hofman, Fission product induced swelling of U–Mo alloy fuel, J.                         multi-scale mechanical constitutive model for U-10Mo fuels under irradiation,
     Nucl. Mater. 419 (2011) 291–301.                                                                       Int. J. Plasticity. 163 (2023) 1–26.
[10] A.M. Casella, D.E. Burkes, P.J. MacFarlan, E.C. Buck, Characterization of ﬁssion                  [37] D.P. Mondal, N. Ramakrishnan, K.S. Suresh, S. Das, On the moduli of closed-cell
     gas bubbles in irradiated U-10Mo fuel, Mater. Charct. 131 (2017) 459–471.                              aluminum foam, Scr. Mater. 57 (2007) 929–932.




                                                                                                  11
