# 📄 PDF Parsing Result

**File:** `/Volumes/openclaw记忆/Zotero_storage/storage/9Q8LMN2W/Li et al. - 2023 - Models for effective elastic constants of irradiated U-10Mo fuels with distributed fission gas bubbl.pdf`
**Backend:** `pipeline`
**Pages:** 0 to end
**Formula Recognition:** ❌ Disabled
**Table Recognition:** ✅ Enabled

---

# Models for effective elastic constants of irradiated U-10Mo fuels with distributed fission gas bubbles

![](images/7402277a681313a4dda9db8d240caf6c5a58204c4206a0fcc88a0dfe2da5290d.jpg)

Yong Li a , Guochen Ding a , Zhexiao Xie a , Jing Zhang a , Xiaobin Jian a , Shurong Ding a,∗ , Yuanming Li b

a Institute of Mechanics and Computational Engineering Department of Aeronautics and Astronautics, Fudan University, Shanghai, China b Science and Technology on Reactor System Design Technology Laboratory, Nuclear Power Institute of China, Chengdu, China

## a r t i c l e i n f o

Article history:   
Received 15 October 2022   
Revised 23 January 2023   
Accepted 27 February 2023   
Available online 10 March 2023

Keywords: Irradiated U-10Mo fuels Fission gas bubbles Recrystallization Effective elastic constants Homogenization theory Numerical simulation

## a b s t r a c t

The multi-scale related models for the effective elastic constants of porous U-10Mo fuels under the irradiation conditions are developed with the proposed multi-level homogenization method. The grain recrystallization effects are taken into account, with fission gas bubbles (FGBs) distributed in the external bubble-contained region of Representative Volume Element (RVE). Performing theoretical analysis and numerical simulation, the effective elastic performances are firstly obtained for the bubble-contained region, and then are volumetrically averaged with those of the internal no-bubble region. The effective elastic constants of irradiated U-10Mo fuels determined in this study agree well with some available experimental data in the references. The research results indicate that: (1) the effective elastic constants of porous U-10Mo fuels are hardly affected by the pore pressure, mainly depending on the macroscopically average porosity; (2) the theoretically derived model for the effective bulk modulus is the same as the degraded Mori-Tanaka model, with the inclusion phase there regarded as bubbles having zero elastic constants. The developed models correlate the elastic constants of irradiated U-10Mo fuels with their continuously varying porous structures, which lay a foundation for modeling the multi-scale irradiationinduced thermo-mechanical coupling behaviors.

© 2023 Elsevier B.V. All rights reserved.

## 1. Introduction

U-10Mo alloy with high-temperature γ -phase has been a promising nuclear fuel for converting some of the research and test reactors from high-enriched uranium to low-enrich uranium (LEU), due to its advantages of high uranium density, low neutron capture cross-section, high thermal conductivity, and good irradiation stability [1,2]. To qualify U-10Mo fuels as alternative LEU fuels for Research and Test Reactors, much research about processing technology, thermo-physical properties, and irradiation performance of U-10Mo fuels designed as U10Mo/Al dispersion fuels and U-10Mo monolithic fuels have been performed [3–6].

Elastic constants are important physical properties of nuclear fuels, as they are directly related to the mechanical and geometric stability of fuel elements. For any nuclear fuels, it is essential to keep the structural integrity and geometric stability to avoid the leakage of fission products and the channel block of coolant and control rods. Macroscopic elastic constants of irradiated U-10Mo fuels vary with the increase of fission density. According to the post-irradiation examination of RERTR-12 and AFIP-6 MK Ⅱ irradiation campaign, Schulthess and Lloyd et al. [3] observed that the effective Young’s modulus of U-10Mo fuels in LIP773 specimens is in the range of 57 65 GPa at the fission density of 3.3  1027 ∼3.4 × 1027 fission/m3, while the Young’s modulus of the unirradiated U-10Mo is 85 GPa [7].

The elastic constants of irradiated U-10Mo fuels depend on the evolving microstructure induced by fission events. During irradiation, the fission gas atoms are generated continuously and diffuse towards the grain boundary, resulting in the formation of FGBs. FGBs formed by fission gas atoms are a significant problem, as they change the U-10Mo fuels to porous structures, degrade the thermo-mechanical properties, and swell the fuels [3,8,9]. The examinations of TEM and SEM demonstrated that the FGBs in U-Mo fuels distributed themselves in intra-granular form and inter-granular form [4,10,11]. TEM images of intra-granular bubbles showed that fission gas atoms could be arranged into an ordered nano-bubble FCC lattice, as a superlattice in the BCC crystal lattice of the U-Mo matrix. Typical intra-granular bubble sizes are

2 6 nm in diameter and the distance between the intra-granular bubbles is in the 4∼12 nm range [11]. Thus, the intra-granular bubbles of fission gas in nm-size could be regarded as solid precipitates in the U-Mo matrix. FGBs of irradiated U-Mo fuels observed by SEM are located in the grain boundary area and named inter-granular bubble. The diameter of inter-granular bubbles is about 0.1∼1 μm [12]. With the increase of fission density, recrystallization occurs at intermediate fission densities, with the original large grains subdivided into fine grains. The recrystallization initiates near the grain boundary and propagates toward the inner part with the increase of fission density, until the whole grain are consumed [13]. The refined grains present higher grain boundary density and shorten gas diffusion distances to grain boundaries. Therefore, recrystallization accelerates the formation and growth of FGBs [14], and separates the irradiated U-10Mo fuels into the bubble-contained region and the no-bubble region.

The irradiated U-10Mo fuels could be regarded as composite materials consisting of U-10Mo matrix and inter-granular FGBs full-filled with fission gas atoms. According to homogenization theory, the macroscopic effective mechanical properties of composite materials can be obtained via the volumetric average of the mesoscopic mechanical variables, termed as mean-field method [15,16]. To calculate the mesoscopic mechanical variables, the RVE including mesoscopic components and all structural information should be chosen, and the mechanical behaviors of each part should be known [17]. The mean-field method for effective elastic performances can be carried out with analytical methods and numerical simulation. Different analytical models for effective elastic properties of composites have been proposed by researchers [18–24]. Finite element (FE) computations have also been used to obtain the effective elastic behavior of composites or porous materials [25,26]. Some semi-empirical relations of effective elastic constants to porosity for porous materials are also proposed to fit the experimental results [3,27]. However, the effective elastic constants of irradiated U-10Mo fuels with distributed FGBs still need to be studied, considering its special irradiation phenomena and the continuous evolution of the FGBs in the irradiated U-10Mo fuels during recrystallization. Different from the general porous materials, distinct bubble-contained region and no bubble region appear before completion of grain recrystallization, and pore pressures result in the existence of initial stresses.

In this study, the effective elastic constants of irradiated U-10Mo fuels with distributed FGBs are studied based on homogenization theory. A multi-level homogenization method is proposed considering the distribution feature of the FGBs during recrystallization. Different RVEs of equivalent spherical model and random distribution model are selected to determine the independent effective elastic constants of the irradiated U-10Mo fuels. The effective bulk modulus is theoretically derived according to the elastic solution of the equivalent spherical model. The effective shear modulus is calculated by the effective bulk modulus and the effective Young’s modulus, while the latter is obtained by FE method based on the random distribution model. The effective elastic constants determined in this study are compared with other effective elastic constants models and some available experimental data in the references. At last, the effective elastic constants models related to the macroscopic porosity are developed for the irradiated U-10Mo fuels.

## 2. A multi-level homogenization method for modeling of effective elastic constants of irradiated fuels

According to the homogenization theory, the homogenized elastic constitutive relation for heterogeneous materials is defined as

$$
\tag{1}
$$

![](images/d91390c4464c788373a5b66ac868aebaa33d4de7643fb7446e61dfe100ec65e5.jpg)  
(a)

![](images/a62f5b1a39e2471a7ae25329f3b585c1a848fd38906d3948d8a1b135a1165498.jpg)  
(b)  
Fig. 1. Microstructures of the irradiated U-10Mo fuels by SEM (a) during recrystallization (b) after recrystallization [10].

where, Lhomijkl denotes the components of effective stiffness tensor; σ¯ij and ε¯kl are the volume-averaged stress components and elastic strain components over the RVE domainV , expressed as

$$
\tag{2}
$$

$$
\tag{3}
$$

where, σij and εij are the additional local stress components and elastic strain components of the RVE induced by the external forces.

The irradiated U-10Mo fuels can be regarded as heterogeneous materials consisting of the U-10Mo skeleton and the FGBs fullfilled with fission gas atoms. During recrystallization, the U-10Mo fuels could be divided into the no-bubble region and the bubblecontained region, as shown in Fig. 1(a). While the recrystallization is finished, the FGBs distribute in the U-10Mo fuels uniformly, as shown in Fig. 1(b) [10]. The local volume fraction of the FGBs in the bubble-contained region is denoted as fbc, also termed as local porosity. The macroscopic volume fraction of the FGBs for the whole irradiated U-10Mo fuels denoted as fbm, termed as macroscopic porosity, is expressed as

$$
\tag{4}
$$

where, Vc is the volume of the bubble-contained region; ηbc is the volume fraction of the bubble-contained region; V is the sum volume of the no-bubble region and the bubble-contained region.

To obtain the effective elastic constants of irradiated U-10Mo fuels, the RVE representing the microscopic information should be selected. Fig. 2 shows the multi-level homogenization process for the irradiated U-10Mo fuels during recrystallization. In the firstlevel homogenization, the bubble-contained region is homogenized to an isotropic material. Then the homogenized bubble-contained region and no-bubble region are homogenized to an isotropic material further. Thus, this multi-level homogenization method is implemented for the irradiated U-10Mo fuels during recrystallization. While the recrystallization is finished, the FGBs are assumed to be homogeneously distributed in all the U-10Mo matrix, and only the first-level homogenization is needed to obtain the effective elastic constants of the irradiated U-10Mo fuels. Two types of RVE including the equivalent spherical model and random distribution model are selected to determine the effective elastic constants of the irradiated U-10Mo fuels as shown in Fig. 2. The shapes of the FGBs and the no-bubble regions are approximately spherical in this study.

## 3. Determination of the effective elastic constants for the bubble-contained region

In the first-level homogenization, the FGBs are considered to be distributed in the U-10Mo skeleton uniformly and randomly. The bubble-contained region is regarded as a macroscopically isotropic material. The elastic constants of U-10Mo are taken from Ref. [7]. The surfaces of FGBs or pores are subjected to pressures, which depend on the bubble volume and the moles of contained fission gas atoms, obeying the modified Van der Waal gas law [29]. Two types of RVE are selected to determinate the effective bulk modulus and the effective shear modulus of the bubble-contained region.

![](images/7d8f0f628c2c9c847a2d5f2e1073ee6ff08f3e1dd958842d92a818277b469a83.jpg)

![](images/f17169ca489dbbcd2a5aa668467b7eb37e6a6cef63eeb977e26164b37d0a2771.jpg)

![](images/ac14fb0597290c0d36d3f77b662a2ac9e3193fdadbdcfaec3092468013095df0.jpg)

![](images/2afdd411548ec7b2091660d4cc893558a782320016afc99f442e68eb13725eb0.jpg)

![](images/c6b4cad0ac0989352700fd19908c93e89fcd375ff88ba5990f18535ab875f782.jpg)  
Fig. 2. The sketch of bubble-contained region and no-bubble region and the multi-level homogenization.

![](images/c2ca5ea89f57297d73ed334c51b3a2db6c5ff1c66500ee91ff30cc4cad5e75e8.jpg)  
Fig. 3. Schematics of the RVE used to determine the bulk modulus of the bubble-contained region: (a) the effective spherical model subjected to bubble pressure and external pressure, which can be superposed by (b) a model subjected to the bubble pressure as the reference configuration, and (c) a model subjected to the external hydrostatic pressure. The black dotted lines represent the boundaries of the FGBs and U-10Mo skeleton before the application of the external hydrostatic pressure.

## 3.1. Theoretical analysis of effective bulk modulus for the bubble-contained region

According to the homogenization theory, the effective bulk modulus of a heterogeneous material is expressed as

$$
\tag{5}
$$

where σ¯ii/3 and ε¯kk are the volumetrically averaged effective hydrostatic stress and effective elastic strain of the RVE caused by the external hydrostatic pressure.

For the bubble-contained region composed of the U-10Mo skeleton and the FGBs, the equivalent spherical model in Fig. 3 is selected as RVE to determine the effective bulk modulus, similar as that in Ref. [28]. The radius ratio of the FGBs and RVE depends on the local porosity, expressed as

$$
\tag{6}
$$

where, R1 and R2 are the radius of the FGBs and the RVE respectively.

The effective bulk modulus can be obtained by solving the stress and elastic strain fields of the RVE under the uniform external hydrostatic pressure. As shown in Fig. 3(a), the external hydrostatic pressure Hp is applied on the outer surface S2 of the RVE. The mechanical interaction between the FGBs and the U-10Mo skeleton on the interface S1 is Pb, corresponding to the bubble pressure of FGBs. The global coordinate system is located at the center of the equivalent spherical model. The deformation of the RVE subjected to the bubble pressure and the external hydrostatic pressure can be considered as a combination of two components. Elastic deformation caused by the bubble pressure as shown in Fig. 3(b). Elastic deformation caused by the external hydrostatic pressure as shown in Fig. 3(c). To obtain the effective elastic volumetric strain caused by the external hydrostatic pressure, the configuration shown in Fig. 3(b) is regarded as the reference configuration. As mentioned above, initial stresses exist in the irradiated fuels. The elastic mechanical responses are corresponding to the additional stresses and elastic strains due to the external forces.

The term σ¯ii/3 can be expressed as

$$
\tag{7}
$$

where, Vm and Vb correspond to the volumes of the U-10Mo skeleton and the FGBs, respectively, and V is the total volume of the

RVE. It is noted that these stresses are the stress increments induced by the external pressures. Here, the FGBs can be assumed as an equivalent solid media bearing spherical stresses (negative values of hydrostatic pressure).

As xi,k = δik, therefore

$$
\tag{8}
$$

where, xi is the coordinate components of material points inside the RVE.

Neglecting body forces, the equilibrium differential equations are expressed as σik,k = 0. Applying the divergence theorem to Eq.(8), the effective hydrostatic stress can be calculated as

$$
\tag{9}
$$

where, n1k and n2k are the normal components of S1 and S2 respectively.

x1i and x2i are the coordinate components of material points on the surfaces S1 and S2 respectively, which can be expressed as

$$
\tag{10}
$$

T 1i is the surface force of the FGBs on the surface S1, given as

$$
\tag{11}
$$

T and T2i are the surface forces of the U-10Mo skeleton on the surfaces S1 and S2, expressed as

$$
\tag{12}
$$

Substituting Eqs. (10)∼(12) into Eq. (9) yields

![](images/55b81136d3e33bcae776e68d6ade646fc0df3bfee719483f09a809771005ee92.jpg)

So, the effective hydrostatic pressure of the equivalent spherical model is equal to the external hydrostatic pressure applied to the model, unrelated to the bubble pressure. While the bubble pressure is balanced by the surrounding U-10Mo skeleton.

The term ε¯kkis expressed as

$$
\tag{14}
$$

where, εkk depicts the additional elastic volumetric strain field caused by the external hydrostatic pressure.

Using geometric equation εij = 12 (ui, j + u j,i), and applying the divergence theorem to Eq.(14) yields

$$
\tag{15}
$$

where, u1k and u2k are the displacement components of material points on the surfaces S1 and S2 respectively, which can be expressed as

$$
\tag{16}
$$

where, u1r = R1 − R1 and u2r = R2 − R2 are the radial displacement of material points on the surfaces S1 and S2 caused by the external hydrostatic pressure, respectively. In fact, the elastic deformation

induced bubble volume variation can be ignored, so the superimposition treatment is acceptable.

Substituting Eq. (16) to Eq. (15) yields

![](images/4b99976c30128318e8b7d558c5582a9691f26017228005d3ffceec269483a5a3.jpg)

For the equivalent spherical model with uniform hydrostatic pressure boundary condition, its effective elastic volumetric strain is 3 times of the average radial strain.

Thus, the effective bulk modulus of the RVE is

$$
\tag{18}
$$

According to the elastic solution of u2r given in Appendix B, the effective bulk modulus of the bubble-contained region is determined as

$$
\tag{19}
$$

where, E is the Young’s modulus of the dense U-10Mo skeleton with the value of 85,000 MPa; v is the Poisson’s ratio of the U-10Mo skeleton with the value of 0.34. The influences of the fission solid products and the intra-granular FGBs on the elastic constants of the U-10Mo skeleton are ignored [7].

It should be mentioned that the variation of bubble pressure after applying the external hydrostatic pressure is slight, as demonstrated in Appendix B. Consequently, the above superposition method can be adopted, and the effective bulk modulus of porous U-10Mo fuels is independent of bubble pressure. Simultaneously, it is found from Appendix A that no energy dissipation occurs during the homogenization of the RVE. Furthermore, the stress and strain results calculated with the RVE are equal to those with the RVE placed in the infinite effective medium, as pointed out in Ref. [30]. Thus, it can be obtained that the homogenization modeling in this study conforms to the basic conditions of the homogenization theory and the generalized self-consistent theory [31,32].

3.2. Modeling of the effective shear modulus for the bubble-contained region

As the effective shear modulus can’t be determined by the equivalent spherical model, we will obtain the effective shear modulus based on the inter-relationships between different elastic constants. For the macroscopic isotropic materials, the effective shear modulus can be calculated byG¯ = 3K¯E¯¯ ¯ . The effective Young’s modulus is usually determined by the FE simulation of uniaxial loading based on RVE [33,34]. Then, combined with the effective bulk modulus in Section 3.1, the effective shear modulus can be acquired.

## 3.2.1. Finite element model for performing uniaxial tension

To obtain the effective Young’s modulus, a 3D finite element model with FGBs distributed in the U-10Mo matrix randomly is considered as RVE shown in Fig. 4. The RVE contains twenty-five FGBs, and the calculated effective Young’s modulus are approximately isotropy in the simulation. The FGBs full-filled with fission gas atoms could be considered as an equivalent solid to implement the FE simulation [34,35]. The equivalent constitutive relations and elastic constants of the equivalent solid given in Ref. [35] are adopted. The bubble pressure balanced by the surrounding U-10Mo skeleton before uniaxial tension is ignored in the simulation. Displacement δx is applied on the upper surface in the x direction to result in the elastic deformation of the RVE. As the RVE with randomly distributed FGBs is asymmetric in geometry, displacement constraints are applied to guarantee the periodic boundary conditions. The displacement constraints can be expressed as

![](images/6ac1bc2b6bb266011fdc7651dfaece743314408086bdce5cb58c229e5880c46b.jpg)  
Fig. 4. The FE model with FGBs randomly distributed in the U-10Mo matrix.

![](images/1be1942d1a8fc03c469475ff9d08d0f02563e79fdb85a3b94cb6c3cbc7fb42f1.jpg)  
Fig. 5. The diagram of periodic boundary conditions.

$$
\tag{20}
$$

where, j = 1, 2, 3;uj+ and uj− denote the displacement vectors of arbitrary two corresponding points nj+ and nj−on the opposing surfaces; U0 and U j denote the displacement vectors of master nodes N0 and N j . The master nodes and corresponding points are shown in Fig. 5.

Commercial software ABAQUS is used to realize the FE solution. The mesh grid of the U-10Mo skeleton and the FGBs are shown in Fig. 6 with 69,305 C3D10 elements, and the mesh convergence has been verified.

## 3.2.2. The results of effective young’s modulus

Based on the homogenization theory, the effective Young’s modulus can be expressed as

$$
\tag{21}
$$

where, σ¯x and ε¯x is the effective stress component and effective elastic strain component in x direction.

![](images/3ee720dbd8eb2b934a4b9f15186b63373bc6aed3cf36b23ca6c62ee0826e35bf.jpg)  
Fig. 6. The mesh grid of the FE model (a) U-10Mo skeleton (b) the FGBs.

![](images/7dd78d3e7ceaae6e3d0a6f8df7e3a109277db93b9a22167cf87579e79a11412d.jpg)  
Effective strain component of RVE in x direction  
Fig. 7. Effective stress component in x direction and normalized volume of FGBs evolution results during uniaxial tension.

In the finite element analysis, the effective strain component in x direction can be expressed as

$$
\tag{22}
$$

where, a is the edge length of the RVE shown in Fig. 4.

In the finite element analysis, the effective stress component in x direction can be calculated as

$$
\tag{23}
$$

where, nm and nb are the total element numbers of the U-10Mo skeleton part and the FGBs part (equivalent solid media); σ m and b are the integration point stress of the ith U-10Mo skeleton elex, j   
ment and jth FGBs element along x direction, respectively; V m and V b are the element volume of the ith U-10Mo skeleton element and the jth FGBs element, respectively; fm and fbc are the volume fractions of the U-10Mo skeleton elements and the FGBs elements respectively, which can be expressed as

$$
\tag{24}
$$

Fig. 7 gives the contributions of effective stress component in x direction together with the normalized volumes of FGBs during uniaxial tension. The normalized volume of FGBs is defined as the ratio of current FGBs volume to that before uniaxial tension. It can be observed that the volumes of FGBs are scarcely changed during uniaxial tension simulation, implying that the change in bubble pressure can be neglected and the obtained effective Young’s modulus is also independent of bubble pressure. As a result, it is reasonable that the nominal Young’s modulus and shear modulus of equivalent solid media are considered to be zero. As shown in Fig. 7, the effective stress component in x direction of the RVE is only contributed by the U-10Mo skeleton part. The effective Young’s modulus of the RVE for the case of fbc 15% is about 62.90 GPa, 74% of the Young’s modulus of the U-10Mo skeleton.

![](images/e34b5d4fd66579b2e2d528bb0b83304458129c32ef062fcc0ba3a80234019a34.jpg)  
Fig. 8. Comparison of effective shear modulus with different local porosity calculated in this study and those by the effective shear modulus models in references.

## 3.2.3. Models for effective shear modulus

Cases with different volume fraction of FGBs are simulated to calculate the effective Young’s modulus of the bubble-contained region. The effective shear modulus of the bubble-contained region are determined by the effective bulk modulus calculated by Eq.(19) and the effective Young’s modulus calculated by the FE simulation.

Fig. 8 presents the effective shear modulus of the bubblecontained region calculated in this study, together with values calculated by the models in the Refs. [22–24,26]. The detailed expressions of the models are given in Appendix D. According to the above analysis, the bulk modulus and Young’s modulus of FGBs can be regarded as zero. Thus, the shear modulus of the inclusion phase is set as zero in the Mori-Tanaka model [23,24] and Dilute model [24]. It can be noted that the effective shear modulus in this study is in good agreement with the results obtained with Mori-Tanaka model [23,24] and Power-law model [22]. The maximum relative difference between the results in this study and those of the Mori-Tanaka model is less than 1.53%. In the range of low porosity, the results obtained with Dilute model [24] and Exponential model [22] agree well with the results in this study. With the rise of porosity, the deviations of Dilute model and Exponential model results increase, while the former predicts larger values and the later predicts smaller values. The Ramakrishnan model [26] predicts smaller values of effective shear modulus throughout the considered porosity range.

So, the effective shear modulus of the bubble-contained region can be evaluated by the Mori-Tanaka model according to the local porosity, expressed as

$$
\tag{25}
$$

The nominal shear modulus of FGBs is considered as zero.

Table 1  
The effective bulk moduli for the cases with the same macroscopic porosities and different local porosities.
<table><tr><td>Macroscopic porosity fbm</td><td>Local porosity in the bubble- contained region fbc</td><td>Volume fraction of the bubble- contained regionnbc</td><td>Effective bulk modulus calculated by Eq.(26) /GPa</td></tr><tr><td>0.05</td><td>0.2</td><td>0.25</td><td>75.7</td></tr><tr><td rowspan="3"></td><td>0.1</td><td>0.5</td><td>76.1</td></tr><tr><td>0.05</td><td>1</td><td>76.1</td></tr><tr><td>0.25</td><td>0.4</td><td>65.0</td></tr><tr><td rowspan="3">0.10 0.20</td><td>0.2</td><td>0.5</td><td>65.4</td></tr><tr><td>0.1</td><td>1</td><td>65.9</td></tr><tr><td>0.25</td><td>0.8</td><td>49.5</td></tr><tr><td></td><td>0.2</td><td>1</td><td>49.9</td></tr></table>

## 4. Determination of the effective elastic constants for overall U-10Mo fuels

In the second-level homogenization, the bubble-contained region is considered as the homogenized matrix phase with the effective elastic constants determined by Eq. (19) and (25). The nobubble region is treated as the inclusion phase. The overall U-10Mo fuel is homogenized to an isotropic material. Similar to the homogenization operation of bubble-contained region, the equivalent spherical model and random distribution model are adopted to determine the effective elastic constants of overall U-10Mo fuels consisting of the no-bubble region and the bubble-contained region.

## 4.1. Models for the effective bulk modulus of overall U-10Mo fuels

As shown in Section 3.1, the effective bulk modulus of equivalent spherical model is determined by the relationship of the external hydrostatic pressure and the radial displacement caused by the external hydrostatic pressure. For the U-10Mo fuels comprising the no-bubble region and the bubble-contained region, the same theoretical analysis method can be adopted. The radial displacement of the corresponding equivalent spherical model (seen in Fig. 2) is derived in Appendix B. According to the elastic solution of the radial displacement, the effective bulk modulus for the overall U-10Mo fuels is expressed as

$$
\tag{26}
$$

where, v¯ bc = 3K¯ bc−2G¯ bc is the effective Poisson’s ratio of bubble- 6K¯ bc+2G¯ bc contained region.

The local porosity can be obtained with the model in Ref. [36]. The effective bulk moduli for the cases with the same macroscopic porosities and different local porosities are compared in Table 1. It can be noted that the obtained effective bulk moduli are close. Thus, the effective bulk modulus of overall U-10Mo fuels is mainly dominated by the macroscale porosity. Assuming homogeneous distribution of the FGBs in the overall U-10Mo fuels, with the macroscopic porosity fbmthe effective bulk modulus of irradiated U-10Mo fuels during recrystallization can be calculated as

$$
\tag{27}
$$

![](images/fd7ef24491e6b27953f26234d30bae8361a22c1338df448d84ef6ae8509b8c58.jpg)  
Fig. 9. Comparison of the results of effective bulk modulus for the overall U-10Mo fuels calculated by different models.

The macroscopic porosity is used for the porosity or inclusion volume fraction in the models given in Appendix D. The bulk modulus of the inclusion phase is considered as zero. Fig. 9 gives the comparison of the obtained effective bulk modulus for the overall U-10Mo fuels by Eq.(27) with those from different models in the references. It should be mentioned that the degenerated Mori-Tanaka model [23,24] with the elastic constants set as zero is the same as Eq. (27), leading to the same results. It is found that Dilute model [24] overestimate the values. While, the Ramakrishnan model [26] underestimate the values of effective bulk modulus throughout the considered macroscopic porosity range, and the differences are enlarged with the increase of macroscopic porosity. These differences might be caused by the adopted calculation method, where the external pressure of the porous solid is amplified with 1/(1 − fbm) to act as the pressure applied on the outer surface of the RVE (same as that in Fig. 3). As confirmed in Section 3.1, the external hydrostatic pressure of the RVE should be equal to the external pressure of the porous solid. The amplification of the pressure on the RVE would duplicate the effect of the macroscopic porosity, needing to be removed. So, the effective bulk modulus obtained by the Ramakrishnan model [26] is actually reduced with the factor of (1 − fbm).

## 4.2. Modeling of the effective shear modulus for overall U-10Mo fuels

Similar to the solution strategy of the effective shear modulus for the bubble-contained region, a 3D FE model with the nobubble region randomly distributed in the bubbles-contained region randomly is considered here. The boundary conditions are the same as those shown in Section 3.2.1, while the FGBs part is occupied by the no-bubble region, and the matrix are occupied by the homogenized bubble-contained region. The overall effective shear modulus is calculated based on the FE results of the overall effective Young’s modulus and the overall effective bulk modulus determined by Eq. (26).

Different cases with varied volume fractions of the bubblecontained region and local porosity are investigated, as listed in Table 2. Fig. 10 shows the comparison of the effective shear modulus for the overall U-10Mo fuels in this study with those from the models in the references [22–24,26]. The treatment is the same as that in Section 4.1, the porosity or inclusion volume fraction in the models given in Appendix D is displaced with the macroscopic porosity and the shear modulus of the inclusion phase are considered as zero. It can be noted that the results of effective shear modulus calculated by the Mori-Tanaka model [23,24] match well with the results obtained in this study. As a result, the effective shear modulus for the overall U-10Mo fuels is demonstrated to rely mainly on the macroscopic porosity.

Table 2  
Cases with different volume fraction of the bubble-contained region and different local porosity to calculate the effective shear modulus.
<table><tr><td>Volume fraction of the bubble-contained region nbc</td><td>Local porosity in the bubble-contained region fbc</td><td>Macroscopic porosity fbm</td></tr><tr><td>0.00</td><td>0.00</td><td>0.00</td></tr><tr><td>0.85</td><td>0.10</td><td>0.085</td></tr><tr><td>0.85</td><td>0.25</td><td>0.212</td></tr><tr><td>1.00</td><td>0.10</td><td>0.10</td></tr><tr><td>1.00</td><td>0.25</td><td>0.25</td></tr></table>

![](images/1b74539d0aee523eadde3b3f5a3c9e5ef14b52ec3c7ba29cf71c7b13605f9059.jpg)  
Fig. 10. Comparison of effective shear modulus for the overall U-10Mo fuels in this study with those from different models in the references.

It can be obtained that the effective bulk modulus and effective shear modulus of irradiated U-10Mo fuels during irradiation can be determined by the macroscopic porosity and the elastic constants of the U-10Mo skeleton as follows:

$$
\tag{28}
$$

According to the inter-relationships between different effective elastic constants, the effective Young’s modulus and the Poisson’s ratio are given by

$$
\tag{29}
$$

Fig. 11 presents the comparison of the normalized effective shear modulus G¯/G calculated by Eq. (28) and several models in the references for porous materials with the experimental results of aluminum foam [37]. It can be found that the effective shear modulus results calculated by Eq. (28) agree well with the experimental results, while the other models tend to underestimate the values.

![](images/0da2d9d2326163e60dcaca5d0b88e31c497b6d071b073ab01461dd2629e29009.jpg)  
Fig. 11. Comparison of the normalized effective shear modulus calculated by different models and the experimental results of aluminum foam.

![](images/accc76de0d64014954888e67c2812aebae6ffc99820dfb87793136164c94889d.jpg)  
Fig. 12. Comparison of the effective Young’s modulus for the irradiated porous U-10Mo fuels calculated by the mathematic model and the test results of L1P773.

Fig. 12 presents the comparison of the effective Young’s modulus for irradiated U-10Mo fuels calculated by Eq. (29) and the test results of fuels in L1P773 [3]. For the specimens sectioned from different locations in L1P773, the measured results of effective Young’s modulus are 57 GPa, 64 GPa and 65 GPa, respectively. The reported porosity in Ref. [3] is 13.7% for irradiated L1P773 without considering the location dependence. So, the reported porosity data is suitable for some specific locations. With the reported porosity substituted into Eq. (29), the obtained effective Young’s modulus is 64.5 GPa, very close to the measurements of 64 GPa and 65 GPa. It can be speculated that the macroscopic porosities of the corresponding specimens are close to 13.7%. The specimen with the measured Young’s modulus of 57 GPa is possible to have a different macroscopic porosity. A potential conclusion can be drawn that the elastic modulus of the U-10Mo skeleton is degraded due to nuclear fissions and inner material damage, if the actual macroscopic porosity is lower than the reported value. In a word, the predictions in this study agree well with the experiment results overall, validating the effectiveness and reasonability of the developed models. If the macroscopic porosities of fuels during in-reactor irradiation are known, the elastic constants can be calculated out with Eq. (28) or (29). The developed models in this study will be favorable for the implement of multi-scale thermomechanical coupling simulation of nuclear fuel elements or assemblies.

## 5. Conclusion

In this study, the effective elastic constants of irradiated U-10Mo fuels with distributed FGBs are investigated based on homogenization theory. The irradiated U-10Mo fuels are divided into the no-bubble region and the bubble-contained region during grain recrystallization, and a multi-level homogenization method is proposed to determine the effective elastic constants of porous U-10Mo fuels with pore pressures. Different RVE models representing the critical grain-scale features are selected to determine the macroscopic isotropic effective elastic constants. The effective bulk modulus of irradiated U-10Mo fuels is determined with the developed theoretical analysis method for the equivalent spherical model. The random distribution model is adopted and the uniaxial tension is simulated by FE method to firstly obtain the effective Young’s modulus. Then, the effective shear modulus is calculated by the obtained effective bulk modulus and the effective Young’s modulus. The results of effective elastic constants determined in this study are also compared with those calculated by other models in the references and some available experimental data. The main conclusions are as follows:

(1) The derived model of effective bulk modulus is the same as the degenerated Mori-Tanaka model, with the bulk modulus and shear modulus of inclusion phase set as zero. The effective elastic constants of irradiated U-10Mo fuels determined by the multi-level homogenization method are demonstrated to mainly depend on the macroscopically average porosity and the elastic constants of the U-10Mo skeleton.

(2) The variations of bubble pressure induced by the elastic deformations of the fuel skeleton can be neglected, leading to the fact that the effective elastic constants of irradiated U-10Mo fuels are independent of internal bubble pressure.

(3) The results of effective Young’s modulus calculated by the developed models in this study agree well with the available experimental results of irradiated U-10Mo fuels, which indicates that the developed models are effective and reasonable.

In the future, with the models for local porosity and macroscopic porosity of U-10Mo fuels, the multi-scale thermomechanical coupling simulation for various fuel elements and assemblies could be implemented, which will provide support for their optimal design.

## Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## CRediT authorship contribution statement

Yong Li: Methodology, Software, Validation, Formal analysis, Investigation, Data curation, Writing – original draft, Visualization. Guochen Ding: Validation, Formal analysis, Visualization. Zhexiao Xie: Software, Formal analysis. Jing Zhang: Methodology, Formal analysis, Validation. Xiaobin Jian: Software, Formal analysis, Validation. Shurong Ding: Conceptualization, Methodology, Software, Resources, Writing – review & editing, Supervision, Project administration. Yuanming Li: Conceptualization, Methodology, Supervision, Project administration.

## Data availability

The authors do not have permission to share data.

## Acknowledgment

The authors are very grateful for the supports of National Natural Science Foundation of China (No. 12132005, 12102094, 12135008), the supports of the foundation from Science and Technology on Reactor System Design Technology Laboratory. This study is also sponsored by Shanghai Sailing Program (21YF1402200).

## Appendix A The strain energy increment of the homogenized RVE based on the equivalent spherical model

According to homogenization theory, the macroscopic effective mechanical properties of composite materials can be obtained by the RVE. Fig. A.1 shows the homogenization process of the RVE based on the equivalent spherical model. The equivalent spherical shell model is regarded as the RVE of the bubble-contained region, homogenized as the equivalent spherical body. For the spherical body subjected to uniform external pressure, uniform hydrostatic stress and strain fields arise satisfying all the governing equations.

![](images/8b8a404a0c5dea1906429ff0cf0d2987ea6d81f6a6013e4e580388ec9f0d6032.jpg)  
Fig. A.1. The sketch of homogenization process for RVE based on the equivalent spherical model.

The uniform stress and strain tensors in the effective medium caused by the external hydrostatic pressure Hp are spherical tensors. Thus, the effective stress and strain components of the RVE can be expressed as

$$
\tag{A.1}
$$

where, σ¯kk and ε¯kk are the effective first invariant of stress and strain tensor in RVE defined in Section 3.1.

Substituting Eqs. (13) and (17) to Eq. (A.1), the effective stress and strain components caused by Hp are

$$
\tag{A.2}
$$

The strain energy increment in the effective medium caused by Hp is

$$
\tag{A.3}
$$

It is noted that the right term of Eq. (A.3) is the work of Hp. So, there is no energy dissipation during the homogenization process for the RVE. If the RVE is placed in an infinite effective medium, the average deformation of the RVE is also equal to that of the infinite body [30].

## Appendix B Elastic solution of radial displacement of the equivalent spherical model for the bubble-contained region

The state of the equivalent spherical model subjected to the bubble pressure is taken for the reference configuration as shown in Fig. 3(b). The global coordinate system is located at the center of the equivalent spherical model. Thus, the radial displacement of the equivalent spherical model caused by the external hydrostatic pressure Hp can be determined by the elastic solution of the hollow sphere as shown in Fig. B.1.

![](images/315f7d9bb81fba769db46eefab2092a1c54eaa9e94b483a3364deb8c2900e34a.jpg)  
Fig. B.1. The sketch of the hollow sphere for the calculation of the radial displacement caused by the external hydrostatic pressure.

For the hollow sphere with elastic deformation caused by the external hydrostatic pressure, its differential governing equations can be expressed as

$$
\tag{B.1}
$$

where, σr, σθ and σϕ are the normal stresses in the global coordinate system; r is the radial coordinate; ur is the radial displacement; εr, ε and εϕ are the normal strains in spherical coordinates. G and λ are the lame constants.

The boundary conditions are

$$
\tag{B.2}
$$

The radial displacement can be solved as

$$
\tag{B.3}
$$

where, A = − E 1−2v (1− fbc) Hp; B = − 1+v 2E(1− fbc) R31Hp; E and v are the Young’s modulus and Poisson’s ratio of the U-10Mo skeleton; fbc is the volume fraction of the FGBs, also termed as local porosity.

The volume ratio of the FGBs after the application of the external hydrostatic pressure is

$$
\tag{B.4}
$$

where, V and V is the volume of the FGBs before and after the application of the external hydrostatic pressure.

The bubble pressure varies with the volume of the FGBs, satisfying the modified Van der Waal gas law, namely

$$
\tag{B.5}
$$

where, Pb is the bubble pressure in Pa; T is the temperature in K; k is Boltzmann constant with a value of 1.38×10−23 J/K; hs is the fitting parameter with a value of 0.6; bv is the Van der Waals constant of 8.5 × 10−29 m3/atom for Xe.

So, the ratio of the bubble pressure after and before the application of the external hydrostatic pressure can be expressed as

$$
\tag{B.6}
$$

Table B.1  
Ratios of the bubble pressure calculated according to Eq. (B.4) and Eq. (B.6) for different causes.
<table><tr><td>Local porosity in the bubble-contained</td><td>Temperature T/K</td><td>Bubble pressure before the application of the external hydrostatic Pbo/MPa</td><td>Volume ratios of the FGBs Vb/Vb0</td><td>Ratios of bubble pressure Pb/Pbo</td></tr><tr><td>region fbc 0.10</td><td>373</td><td>10</td><td>0.9923</td><td>1.0078</td></tr><tr><td>0.25</td><td>373</td><td>100</td><td>0.9907</td><td>1.0094</td></tr><tr><td>0.10</td><td>473</td><td>10</td><td>0.9923</td><td>1.0078</td></tr><tr><td>0.25</td><td>473</td><td>100</td><td>0.9907</td><td>1.0094</td></tr></table>

As the temperature, bubble pressure and local porosities vary with the irradiation time and locations [12], cases with different temperatures, bubble pressure and local porosities are tested to evaluate the bubble pressure changes of the FGBs caused by the elastic deformation of U-10Mo skeleton. The external hydrostatic pressure is set as 200 MPa. Ratios of the bubble pressure calculated according to Eq. (B.4) and Eq. (B.6) for different causes are summarized in Table B.1. It can be noted that the relative bubble pressure changes after applying the external hydrostatic are less than 1%. The minimal changes in the bubble pressure have pretty small influences on the radial displacement of the equivalent spherical model in the elastic deformation stage. So, the radial displacement of the equivalent spherical model on the outer surface caused by the external hydrostatic pressure can be expressed as

$$
\tag{B.7}
$$

Appendix C Elastic solution of radial displacement of the equivalent spherical model for the overall U-10Mo fuels

The equivalent spherical model for the overall U-10Mo fuels consist of the no-bubble region and the homogenized bubblecontained region, as show in Fig. C.2. The global coordinate system is located at the center of the equivalent spherical model.

The differential governing equations are same to Eq. (B.1). The boundary conditions of the homogenized bubbled-contained region and the no-bubble region are

$$
\tag{C.1}
$$

where, P is the mechanical interaction between the no-bubble region and bubble-contained region, which needs to be solved.

According the classical theory of elasticity, the radial displacements of the bubble-contained region and the no-bubble region are derived as

$$
\tag{C.2}
$$

![](images/302bcf4a521d1227bd2eda91da2ee9086413f9888675d0fe5f2683a46a9223cf.jpg)  
Fig. C.2. The sketch of the equivalent spherical model for the U-10Mo fuel during recrystallization comprised of the no-bubble region and the homogenized bubblecontained region.

where, E¯ bc and v¯ bc are the effective Young’s modulus and Poisson’s ratio of the homogenized bubble-contained region; E and v are the Young’s modulus and Poisson’s ratio of the U-10Mo skeleton.

Considering no fractures between the no-bubble region and the bubble-contained region, the radial displacement on the interface is continuous, denoted as

$$
\tag{C.3}
$$

Thus, the mechanical interaction between the no-bubble region and bubble-contained region is expressed as

$$
\tag{C.4}
$$

where, K¯ bc is the effective bulk modulus of the homogenized bubble-contained region; K is the bulk modulus of the U-10Mo skeleton; ηbc is the volume fraction of the bubble-contained region.

Submit Eq. (C.4) to Eq. (C.2), the radial displacement of the equivalent spherical model on the outer surface caused by the external hydrostatic pressure is

$$
\tag{C.5}
$$

## Appendix D. Some effective elastic constants models in the references

Researchers have proposed different mathematic models of effective bulk modulus K¯ and effective shear modulus G¯ for porous materials and two-phase composite materials according to theoretical and experimental research. Some of the mathematic models are presented as follows

Ramakrishnan model [26]:

$$
\tag{D.1}
$$

where, Km and Gm are the bulk modulus and shear modulus of the solid skeleton or the matrix phase; ϕ is the macroscopic porosity. Ramakrishnan model is proposed for the porous solid.

Power-law model [22]:

$$
\tag{D.2}
$$

Exponential model [22]:

$$
\tag{D.3}
$$

Dilute models [24]:

$$
\tag{D.4}
$$

where, Kf and Gf are the bulk modulus and shear modulus of the inclusion phase; vm is the Poisson’s ratio of the matrix phase; Vf is the volume fraction of the inclusion phase.

Mori-Tanaka model [23,24]:

$$
\tag{D.5}
$$

## References

[1] X. Jian, X. Kong, S. Ding, A mesoscale stress model for irradiated U 10Mo monolithic fuels based on evolution of volume fraction/radius/internal pressure of bubbles, Nucl. Eng. Technol. 51 (2019) 1575–1588.

[2] M.K. Meyer, G.L. Hofman, S.L. Hayes, C.R. Clark, T.C. Wiencek, J.L. Snelgrove, R.V. Strain, K.H. Kim, Low-temperature irradiation behavior of uranium–molybdenum alloy dispersion fuel, J. Nucl. Mater. 304 (2002) 221–236.

[3] J.L. Schulthess, W.R. Lloyd, B. Rabin, K. Wheeler, T.W. Walters, Mechanical properties of irradiated U Mo alloy fuel, J. Nucl. Mater. 515 (2019) 91–106.

[4] J. Gan, D.D. Keiser, B.D. Miller, A.B. Robinson, J.F. Jue, P. Medvedev, D.M. Wachs, TEM characterization of U–7Mo/Al–2Si dispersion fuel irradiated to intermediate and high fission densities, J. Nucl. Mater. 424 (2012) 43–50.

[5] A. Leenaers, S. Van den Berghe, C. Detavernier, Surface engineering of low enriched uranium–molybdenum, J. Nucl. Mater. 440 (2013) 220–228.

[6] R. Jungwirth, H. Palancher, A. Bonnin, C. Bertrand-Drira, C. Borca, V. Honkimäki, C. Jarousse, B. Stepnik, S.H. Park, X. Iltis, W.W. Schmahl, W. Petry, Microstructure of as-fabricated UMo/Al(Si) plates prepared with ground and atomized powder, J. Nucl. Mater. 438 (2013) 246–260.

[7] Y.S. Kim, G.L. Hofman, J.S. Cheon, A.B. Robinson, D.M. Wachs, Fission induced swelling and creep of U–Mo alloy fuel, J. Nucl. Mater. 437 (2013) 37–46.

[8] D.E. Burkes, A.M. Casella, A.J. Casella, E.C. Buck, K.N. Pool, P.J. MacFarlan, M.K. Edwards, F.N. Smith, Thermal properties of U–Mo alloys irradiated to moderate burnup and power, J. Nucl. Mater. 464 (2015) 331–341.

[9] Y.S. Kim, G.L. Hofman, Fission product induced swelling of U–Mo alloy fuel, J. Nucl. Mater. 419 (2011) 291–301.

[10] A.M. Casella, D.E. Burkes, P.J. MacFarlan, E.C. Buck, Characterization of fission gas bubbles in irradiated U-10Mo fuel, Mater. Charct. 131 (2017) 459–471.

[11] B.D. Miller, J. Gan, D.D. Keiser, A.B. Robinson, J.F. Jue, J.W. Madden, P.G. Medvedev, Transmission electron microscopy characterization of the fission gas bubble superlattice in irradiated U–7 wt%Mo dispersion fuels, J. Nucl. Mater. 458 (2015) 115–121.

[12] D. Salvato, A. Leenaers, S. Van den Berghe, C. Detavernier, Pore pressure estimation in irradiated UMo, J. Nucl. Mater. 510 (2018) 472–483.

[13] Y.S. Kim, G.L. Hofman, J.S. Cheon, Recrystallization and fission-gas-bubble swelling of U–Mo fuel, J. Nucl. Mater. 436 (2013) 14–22.

[14] J. Rest, Evolution of fission-gas-bubble-size distribution in recrystallized U–10Mo nuclear fuel, J. Nucl. Mater. 407 (2010) 55–58.

[15] E.S. Perdahcıoglu,˘ H.J.M. Geijselaers, Constitutive modeling of two phase materials using the mean field method for homogenization, Int. J. Mater. Form. 4 (2011) 93–102.

[16] I. Doghri, C. Friebel, Effective elasto-plastic properties of inclusion-reinforced composites. Study of shape, orientation and cyclic response, Mech. Mater. 37 (2005) 45–68.

[17] J. Zhang, J. Zhang, H. Wang, H. Wei, C. Tang, C. Lu, S. Ding, Y. Li, Research on the homogenized postirradiation elastoplastic constitutive relations for composite nuclear fuels, Front. Mater. 8 (2021).

[18] R. Hill, A self-consistent mechanics of composite materials - sciencedirect, J. Mech. Phys. Solids 13 (1965) 213–222.

[19] J.D. Eshelby, The determination of the elastic field of an ellipsoidal inclusion, and related problems, Proc. R. Soc. Lond. A Math. Phys. Sci. 241 (1957) 376–396.

[20] A. Reuss, Berechung der Fliessgrenze von Mischkristallen, ZAMM J. Appl. Math. Mech. Z. Angew. Math. Mech. 9 (1929) 49–58.

[21] W. Voigt, Ueber die beziehung zwischen den beiden elasticittsconstanten isotroper Krper, Ann. Phys. Berlin 274 (2006) 573–587.

[22] W. Pabst, T. Uhlírová, ˇ E. Gregorová, Shear and bulk moduli of isotropic porous and cellular alumina ceramics predicted from thermal conductivity via cross-property relations, Ceram. Int. 44 (2018) 8100–8108.

[23] T. Mori, K. Tanaka, Average stress in matrix and average elastic energy of materials with misfitting inclusions, Acta Metall. 21 (1973) 571–574.

[24] K. Huang, Y. Huang, Solid Constitutive Relations, Tsinghua University, 1999.

[25] C.T. Sun, R.S. Vaidya, Prediction of composite properties from a representative volume element, Compos. Sci. Technol. 56 (1996) 171–179.

[26] N. Ramakrishnan, V.S. Arunachalam, Effective elastic moduli of porous solids, J. Mater. Sci. 25 (1990) 3930–3937.

[27] E.A. Dean, J.A. Lopez, Empirical dependence of elastic moduli on porosity for ceramic materials, J. Am. Ceram. Soc. 66 (1983) 366–370.

[28] Xiangzhe Kong, Xiaobin Jian, Feng Yan, et al., Macro-mesoscale in-pile thermal-mechanical behavior simulation of a UMo/Zr monolithic fuel plate, Front. Energy Res. 9 (2022) 1–14.

[29] X. Jian, F. Yan, X. Kong, Y. Li, S. Ding, Further development of the fission gas swelling model for U-10Mo fuels, J. Nucl. Mater. 565 (2022) 1–13.

[30] Hongyang Wei, Xiaobin Jian, Shurong Ding, A model of gas-induced effective expansion strain for porous carbon materials in irradiation environments, J. Nucl. Mater. 515 (2019) 338–353.

[31] R. Hill, The elastic behaviour of a crystalline aggregate, Proc. Phys. Soc. A 65 (349) (1952) 349–354.

[32] R.M. Christensen, K.H. Lo, Solutions for effective shear properties in three phase sphere and cylinder models, J. Mech. Phys. Solids 27 (1979) 315–330.

[33] J. Zhang, S. Ding, Mesoscale simulation research on the homogenized elasto– plastic behavior of FeCrAl alloys, Mater. Today Commun. 22 (2020) 1–12.

[34] Z. Zhou, M. Chen, Predicting effective moduli of a Z-reinforced core with cavities using a novel theoretical approach and a micromechanics finite element method, Int. J. Mech. Sci. 105085 (2019) 161–162.

[35] Y.C.Y.H. JIANG, A method for 3D simulation of internal gas effects on thermal-mechanical behaviors in nuclear fuel elements, Nucl. Sci. Tech. 22 (2011) 185–192.

[36] X. Jian, J. Zhang, Y. Li, S. Ding, Skeleton-creep based bubble growth model and multi-scale mechanical constitutive model for U-10Mo fuels under irradiation, Int. J. Plasticity. 163 (2023) 1–26.

[37] D.P. Mondal, N. Ramakrishnan, K.S. Suresh, S. Das, On the moduli of closed-cell aluminum foam, Scr. Mater. 57 (2007) 929–932.
