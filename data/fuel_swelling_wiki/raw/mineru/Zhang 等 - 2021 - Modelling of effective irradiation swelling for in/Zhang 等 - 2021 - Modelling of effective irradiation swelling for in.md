# 📄 PDF Parsing Result

**File:** `/Volumes/openclaw记忆/Zotero_storage/storage/BVQXCVCI/Zhang 等 - 2021 - Modelling of effective irradiation swelling for in.pdf`
**Backend:** `pipeline`
**Pages:** 0 to end
**Formula Recognition:** ❌ Disabled
**Table Recognition:** ✅ Enabled

---

Original Article

Modelling of effective irradiation swelling for inert matrix fuels Jing Zhang a , Haoyu Wang b , Hongyang Wei a, b , Jingyu Zhang a , Changbing Tang b , Chuan Lu b , Chunlan Huang b , Shurong Ding a, \* , Yuanming Li b, \*\*

![](images/996f101e97c008a6e1eedd984d97aab0ab6450d347939e3239c1efd38e488063.jpg)

a Institute of Mechanics and Computational Engineering, Department of Aeronautics and Astronautics, Fudan University, Shanghai, 200433, China b Science and Technology on Reactor System Design Technology Laboratory, Nuclear Power Institute of China, Chengdu, 610213, China

## a r t i c l e i n f o

Article history:   
Received 2 December 2020   
Received in revised form   
14 February 2021   
Accepted 22 February 2021   
Available online 28 February 2021 Keywords:   
Inert matrix fuel   
Equivalent spherical model Effective irradiation swelling Hydrostatic pressure   
Irradiation and thermal creep

## a b s t r a c t

The results of effective irradiation swelling in a wide range of burnup levels are numerically obtained for an inert matrix fuel, which are verified with DART model. The fission gas swelling of fuel particles is calculated with a mechanistic model, which depends on the external hydrostatic pressure. Additionally, irradiation and thermal creep effects are included in the inert matrix. The effects of matrix creep strains, external hydrostatic pressure and temperature on the effective irradiation swelling are investigated. The research results indicate that (1) the above effects are coupled with each other; (2) the matrix creep effects at high temperatures should be involved; and (3) ranged from 0 to 300 MPa, a remarkable dependence of external hydrostatic pressure can be found. Furthermore, an explicit multi-variable mathematic model is established for the effective irradiation swelling, as a function of particle volume fraction, temperature, external hydrostatic pressure and fuel particle fission density, which can well reproduce the finite element results. The mathematic model for the current volume fraction of fuel particles can help establish other effective performance models.

© 2021 Korean Nuclear Society, Published by Elsevier Korea LLC. This is an open access article under the CC BY-NC-ND license (http://creativecommons.org/licenses/by-nc-nd/4.0/).

## 1. Introduction

Inert matrix fuel elements are widely used in research and test reactors [1,2], which also have a promising application prospect in advanced future nuclear reactors [3,4] and in the aspects of disposal of nuclear wastes [5]. Simultaneously, different inert matrix composite fuel pellets are proposed to burn plutonium and some other minor actinides extracted from the spent fuels [6,7]. These inert matrix fuel pellets are expected to be loaded in current light water reactors with extended burnup, because these composite fuels have higher thermal conductivity than the traditional homogeneous UO2 and can reach high burnup [8e10]. Additionally, inert matrix fuels have shown good performances under transient conditions [7,11].

In the extreme environments of nuclear reactors, the nuclear fuel particles undergo irradiation swelling due to the accumulation of solid and gaseous fission products [6,12,13]. The irradiation swelling induced by solid fission products can be a linear function of fission density [14]. However, the mechanism of fission gas swelling is complex. The fission gas swelling is closely dependent on the gas atom diffusion within the fuel grain. After a critical fission density, grain recrystallization occurs, which accelerates fission gas swelling [14e18]. Moreover, the fission gas swelling is affected by external hydrostatic pressure [19e22], so the irradiation and thermal creep strains [23e25] in the inert metal matrix have an impact on the fission gas swelling of fuel particles, because the creep relaxing effects will change the mechanical interactions between the fuel particles and the matrix. It should be noted that the irradiation swelling of fuel particles will contribute to the volumetric variations of composite fuel pellets, which will exert influences on the thermo-mechanical interactions [14,26] between the fuel pellets and the cladding. To better understand the irradiation-induced thermo-mechanical behavior of inert matrix fuel elements and implement optimized design, it is critical to predict the effective irradiation swelling of inert matrix nuclear fuels. The effective irradiation swelling refers to the homogenized swelling under the irradiation environments.

Owing to the fact that the irradiation experiments are timeconsuming with high cost and hard to be examined in situ, it is very necessary to develop the theoretical models and numerical simulation methods to obtain the effective irradiation swelling of inert matrix fuels [27e29]. Inert matrix nuclear fuels tend to contain massive fuel particles [6,30], and it is difficult to simulate the irradiation-induced thermo-mechanical coupling behavior of a whole fuel element or fuel assembly with the interactions between the fuel particles and matrix involved. Thus, an effective way is to homogenize the inert matrix fuels and study its effective properties [31e34]. Both the theoretical models and numerical methods have been performed to acquire the effective irradiation swelling of some dispersion nuclear fuels [14,26,30,35,36]. DART model [26,36] is an effective tool to calculate the effective irradiation swelling of Al-based dispersion nuclear fuels. But the creep and work hardening effects of the matrix were not explicitly taken into account, and small-deformation assumption was performed [26]. Simultaneously, the intergranular gas atom resolution effect and the hydrostatic pressure on the external surface of matrix due to the mechanical interactions inside matrix and among particles should be further incorporated.

In this study, the modelling of effective irradiation swelling for PuO2/Zr inert matrix fuels [7,11] is implemented, with the obtained fission gas swelling results of fuel particles validated, and the effective irradiation swelling results verified with DART model. Then, a multi-variable function for effective irradiation swelling is developed. The finite element model includes the grain recrystallization of fuel particles and the external-hydrostatic-pressure dependence of particle fission gas swelling coupled with the matrix creep effects. The effects of external hydrostatic pressure, temperature and matrix creep on the effective irradiation swelling are investigated.

## 2. Finite element modelling

To obtain the effective irradiation swelling results of the considered inert matrix fuels under different conditions, finite element simulations are implemented with the commercial software ABAQUS. In this section, the representative finite element model will be presented, in which the mechanical constitutive relations for the fuel particles and matrix are defined with the user-defined subroutines, based on the stress update algorithms in our previous studies [27,37]. In the threedimensional constitutive relation for the fuel particles, the total strains contain the contributions of elasticity, plasticity and irradiation swelling. The thermo-mechanical property models in Refs. [12,16,17,34,38,39] are adopted in this study. The models of elastic constants, plasticity and creep strain rate in Refs. [13,40] are taken into account for matrix.

## 2.1. The finite element model

Assuming that the PuO2 fuel particles are periodically distributed in a large matrix, an equivalent spherical model is considered as the representative volume element (RVE), with a particle radius of 0.05 mm and a matrix shell. Since the RVE describes all the mesostructure information of inert matrix fuels, the effective irradiation swelling can be calculated by the finite element (FE) analysis via a RVE. Finally, 1/8 fraction of the RVE is selected as the finite element model, allowing for the symmetry of RVE, shown as Fig. 1. Once the initial particle volume fraction fv0 is set, the initial outer radius r0 of the equivalent spherical model can be calculated as shown in Table 1.

The symmetric boundary conditions are applied on the surfaces of x  0, y  0 and z  0. The constant pressure condition is applied to the outside of the equivalent sphere in consideration of the internal mechanical interactions of inert matrix fuels. A uniform, steady-state temperature is assumed in the finite element model. The temperature is ranged from 473 K to 773 K. The fission rate in the fuel particle is set as 1 - 1020 fissions/(m3 \$s) and the fast neutron flux is set as 2.01568 - 1011 n/(mm2 \$s) in this study [27].

## 2.2. Verifications

## 2.2.1. Verification of the equivalent spherical model

The effective irradiation swelling of the considered inert matrix fuels can be obtained directly through the volumetric variation of the finite element model. The effective irradiation swelling can be expressed as

$$
\tag{1}
$$

where V is the post-irradiation spherical volume, V0 is the initial spherical volume, r is the post-irradiation outer spherical radius, r0is the initial outer spherical radius, shown in Fig. 1.

The initial outer radius is known, which varies with the initial particle volume fraction. The fission density and the corresponding post-irradiation outer spherical radius can be obtained from the FE results. So, the effective irradiation swelling at different fission densities can be calculated.

To ensure the computation precision and efficiency, the sensitivity of mesh density is investigated first for the finite element model under the conditions that the initial particle volume fraction is 20%, the internal temperature is 573 K and the external pressure is 0 MPa. Three mesh cases are considered, having 256, 3400 and 7267 elements respectively, as shown in Fig. 2. The obtained effective volume swelling results are given in Fig. 3. The maximum relative error of the results between Mesh2 and Mesh3 is 0.52%. Hence, results of effective irradiation swelling have converged with Mesh 2, and therefore Mesh 2 is adopted in the following studies. It is noted that the finite element results displayed in the following are all tested to be converged.

Regarding the effective properties of the considered inert matrix fuels, cubic RVE models with different particle arrangement were established in the previous study [30]. In order to verify the applicability of the developed equivalent spherical model in this study, FE simulations for three cases with different particle arrangements are also performed, including simple cubic (SC), body-centered cubic (BCC) and face-centered cubic (FCC), and the particle radius of 0.05 mm is assumed to be the same for each case. It can be observed from Fig. 4 that the FE results of effective irradiation swelling for different models match well with each other, which demonstrates that the equivalent spherical model can be used for calculating the effective irradiation swelling for inert matrix fuels.

## 2.2.2. Verification of the swelling models

The fission gas swelling model of fuel particles is vitally important for calculating the effective irradiation swelling of inert matrix fuels. In order to validate the gas swelling model used in this study, the obtained results are compared with experimental results. As is known that in the reactor irradiation environments the UO2 pellets can form high burnup structure in the rim zone, where grain recrystallization occurs [38]. In Fig. 5, the experimental results for the rim-zone fission gas swelling [41e43] are displayed.

The external hydrostatic pressure on the rim zone surface is relatively low. The corresponding temperature is about 500 Ke900 K [41], and the as-fabricated grain size is about 5mme15mm[44]. So the external hydrostatic pressure is set as zero, the temperature as 800 K and the as-fabricated grain size as 7mm. In this study, with the external hydrostatic pressure considered, the radius of intergranular bubbles is calculated with the Van der Waal gas equation [38,39], expressed as

![](images/9ba194fb21c9b046b172f8e444a35252085c787709a8df54a74d7a128ea56949.jpg)  
Fig. 1. The equivalent spherical model.

Initial particle volume fraction and the equivalent spherical radius.
<table><tr><td>Initial particle volume fraction</td><td>Initial outer radius of equivalent sphere/mm</td></tr><tr><td>10%</td><td>0.1077</td></tr><tr><td>20%</td><td>0.0855</td></tr><tr><td>30%</td><td>0.0747</td></tr><tr><td>40%</td><td>0.0679</td></tr></table>

$$
\tag{2}
$$

where, 2 =Rbis the bubble surface tension in Pa, Ph is the external ghydrostatic pressure in Pa, Rb is the radius of the intergranular bubbles in m, hs is the fitting parameter to make the Van der Waals equation equivalent to the hard-sphere equation of state, bv is the Van der Waal gas constant of Xe in m3 , Nb is the average number of gas atoms in each bubble, k ¼ 1.38 - 1023J/K is the boltzmann constant and T is temperature in K. The above model parameters can be found in Refs. [38,39].

The comparison between the obtained simulation results and experimental results is shown in Fig. 5. It can be observed that the results in this study agree well with the experimental ones, which validate the gaseous swelling model used here. Furthermore, the obtained results for an external hydrostatic pressure of 50 MPa can be found in Fig. 5, and it can be known that hydrostatic pressure has a considerable effect on gaseous swelling, especially at high burnup.

DART model [26,35,36] is a useful tool to calculate the effective irradiation swelling of dispersion fuels, which takes into account the volumetric variation of inert matrix fuels from three aspects: the contribution of matrix swelling induced by chemical reaction of fuel particles with matrix, accumulation of fission products and irradiation-enhanced sintering.

![](images/cd953049dacc9d64ef2dc1286906766aba8db02f9959e210d94a545cc28da68c.jpg)  
Fig. 3. The sensitivity of effective irradiation swelling to the meshes.

For the considered inert matrix fuel in this study, there is no occurrence of chemical reaction during irradiation. It should be also mentioned that the fuel particles are assumed to be dense, so the irradiation-enhanced sintering effect is not considered here. Then, the effective swelling of DART model can be simplified as

![](images/0122e21f730e7d9a5e6db70b0181d60f84e7f4adf6ef7bf518f981db862b9ccd.jpg)  
(a)

![](images/93b3ddd50b9cc11828c2b4a8f2b0927e677df6c3a3da02cd7205a893c18adda4.jpg)

![](images/e36836bee858c0cc4493990cb7d350dc4ab81bd8250a639033a0513c8dea0525.jpg)  
Fig. 2. The models for three mesh cases.  
（c）

![](images/23f1716951b46203d282e475d1b30d10f5aaefae2c22fa4096550c2e5ccb0653.jpg)  
Fig. 4. Comparison of FE results with different models.

![](images/541c0770128d7b5e36fec17cf43abe347b15a35cce3367943c05f40c261f5b9b.jpg)  
Fig. 5. The comparison of the simulation results in this study with the experimental results for the fission gas swelling of fuel particles.

$$
\tag{3}
$$

where, V is the post-irradiation total volume of inert matrix fuel, V0 is the initial total volume of inert matrix fuel, Vf is the absolute Dvolume variation of particle and V represents the absolute volume variation of inert matrix fuel.

Based on Eq. (3), the effective irradiation swelling can be calculated utilizing the current particle volume obtained in this study. Fig. 6 gives the results obtained according to Eq.(3) and the simulation results in this study, with the initial particle volume fraction of 20%, the temperature of 700 K and the external hydrostatic pressure of 0 MPa. The simulation results with and without matrix creep effect are simultaneously displayed in Fig. 6. The effects of irradiation hardening and strain hardening effects in the matrix plasticity model are both considered in the simulations. One can see that the simulation results without matrix creep effect and the results with matrix creep effect match well with the results from Eq. (3), respectively. It should be mentioned that the absolute volume variation of particle in Eq. (3) is not directly obtained from DART model. Meanwhile, it is demonstrated that our results satisfy the basic relation of Eq. (3) in DART model. Additionally, the fission gas swelling results of fuel particles are validated in this study, as shown in Fig. 5. So, the effective treatment in this study can be verified. Meanwhile, it can be obtained that it is necessary to consider matrix creep effect because the results at fission density of 4.3  1027fissions/m3 with matrix creep effect is about 13.3% higher than the ones without matrix creep effect.

![](images/2410b2b5dc8ed7b545fe78c7cf5252a8064063a5d3bbbc2711e1d759cc959a63.jpg)  
Fig. 6. The comparison of the results calculated according to DART model with the obtained results in this study.

## 3. Influence factors on effective irradiation swelling

## 3.1. Effects of hydrostatic pressure

During irradiation, there are mechanical interactions between the fuel particles and matrix because of the particle irradiation swelling. Thus, external forces exist at the outside of equivalent sphere. The external forces will change with the fission density. It can be known from Section 2.2.2 that the gaseous swelling is affected by particle hydrostatic pressure. Therefore, the effective swelling of inert matrix fuels is also affected by external hydrostatic pressure. It should be noted that the effective irradiation swelling is dominated by the particle hydrostatic pressure Hpf (identical to Ph in Eq. (2)) on the outside of fuel particles with the external pressure applied on the matrix set as Hp, as depicted in Fig. 7.

When the inert matrix fuel is homogenized, the mechanical interaction between the fuel particles and matrix can't be taken into account. So, the model of particle hydrostatic pressure Hpf should be studied. Then the model can be used to calculate the fission gas swelling of fuel particles directly. The hydrostatic pressure Hp0 is defined as the particle hydrostatic pressure when the external hydrostatic pressure on the outside of equivalent sphere is zero, as illustrated in Fig. 8. The particle hydrostatic pressure Hp0 evolves with increasing fission density. Firstly, the simulation is carried out under the condition that there is no pressure on the external surface of matrix. During irradiation, the interaction between the fuel particle and matrix happens because of particle irradiation swelling, and the fuel particle is subjected to a hydrostatic pressure of Hp0, which can be determined by the FE computation. Fig. 9 depicts the calculation results of hydrostatic pressure Hp0 at different temperatures and different initial particle volume fractions. It can be found that Hp0 at the certain fission density of 6 - 1027fissions/m3 gradually decreases with the increase of temperature and initial particle volume fraction. When the temperature is higher than 573 K, the hydrostatic pressure Hp0 drops sharply. When the temperature is higher than 673 K, the hydrostatic pressure keeps decreasing at yet a much slower rate. These evolution traits are related to the creep effects in the matrix, as analyzed in Section 3.3.

![](images/ae15f5911a3c34e45b8bfbf79ea3002d0a39f60e492b3dbdfef684ff71b75081.jpg)  
Fig. 7. The hydrostatic pressure Hpf on a fuel particle surface.

![](images/2f7366bf4a88717e8228d26449cfccf0164d7b3920dc0ba1ccbfb4020d2e05b6.jpg)  
Fig. 8. The hydrostatic pressure Hp0 on a fuel particle surface.

![](images/500e3a3e557c0715a57c830c7bb3d2a645dd895b794868cd56ede813b1f2f55c.jpg)  
Fig. 9. The FEM results and fitted results of hydrostatic pressure Hp0 as a function of temperature and initial particle volume fraction at the certain fission density of 6 1027fissions/m3 .

When different hydrostatic pressure levels of Hp is applied on the external surface of the matrix, the particle hydrostatic pressures of Hpf at different fission densities have been obtained by FE calculations, as depicted in Fig. 10. The considered initial particle volume fraction is 20% and the temperature is 573 K. One can observe that the particle hydrostatic pressure will increase from zero to a stable value at the fission density of 1 1027fissions/m3 , after which the pressure magnitudes vary slightly. The stable value of hydrostatic pressure Hp0 is \~400 MPa. It should be indicated that the results in Fig. 9 represent the stable values under different conditions. Besides, the stable results of hydrostatic pressures Hpf are approximately equal to the sum of Hp0 and Hp, namely as Eq. (4), which is also true for all the cases in this study.

![](images/2a7044c0c995d60509966bc1545871c5791b2fc42a8ec127eeb164ae3b5f2de8.jpg)  
Fig. 10. The particle hydrostatic pressures Hpf under different external hydrostatic pressures.

$$
\tag{4}
$$

One can know that the external hydrostatic pressure Hp will influence the particle hydrostatic pressure Hpf. As a result, the fission gas swelling of fuel particles and also the effective irradiation swelling will be affected by Hp. In a nuclear reactor, the external hydrostatic pressures (the hydrostatic pressures for the homogenized pellets) in inert matrix fuels change continuously with the internal interactions within the inert matrix fuel parts and the interactions between the fuel pellet/meat and the cladding. So, the effective irradiation swelling under different external hydrostatic pressures should be investigated. The results of effective irradiation swelling under different external hydrostatic pressures Hp are shown in Fig. 11, respectively for two temperature cases of 573 K and 673 K. The initial particle volume fractions are all considered as 20%.

By comparing Fig. 11(a) and (b), it can be seen that the effective

Under the condition that the initial particle volume fraction is 20%, it can be found from Fig. 9 that the stable hydrostatic pressure Hp0 at 573 K and 673 K are about 430 MPa and 85 MPa respectively. So, the stable particle hydrostatic pressures Hpf at 573 K for Hp ¼ 200 MPa and 673 K for Hp ¼ 300 MPa will become 630 MPa and 385 MPa. Because the fission gas swelling of fuel particles will be hardly lessened by the particle hydrostatic pressure Hpf when its magnitude exceeds 300 MPa, the phenomena in Fig. 11 can be explained.

Simultaneously, one can see from Fig. 11 that the effective irradiation swelling values are close to each other for all the cases at the fission density lower than 2  1027fissions/m3 , which indicates that the fission gas swelling of fuel particle will play an important role at higher fission densities. Thus, the fission gas swelling of fuel particles only depends on the stable value of particle hydrostatic pressure. When the stable particle external pressure Hp0 is determined, the magnitudes of Hpf can be calculated by Eq. (4). The stable hydrostatic pressure Hp0 is dominantly dependent on the variables of temperature and initial particle volume fraction, whose functional relations are fitted, given as

$$
\tag{5}
$$

irradiation swelling decreases more slightly with the external hydrostatic pressure in Fig. 11(a). When temperature is 573 K, the effective irradiation swelling for the case of Hp 200 MPa is 4.07% lower than that for Hp 0 MPa at the fission density of 1.47  1028 fissions/m3 . Meanwhile, the effective irradiation swelling decreases significantly with the increase of external pressure until the external hydrostatic pressure reaches 200 MPa in Fig. 11(b). Compared to the case of Hp ¼ 0, the effective irradiation swelling for Hp ¼ 200 MPa is reduced by \~15.77% at the fission density of 1.47 1028 fissions/m3 . Afterwards, the effective irradiation swelling decreases slowly after the external hydrostatic pressure exceeds 200 MPa. Compared to the case of Hp 200 MPa, the effective irradiation swelling for Hp ¼ 300 MPa is only \~3.54% lower at the fission density of 1.47 1028 fissions/m3 .

where, Hp0 is in MPa, fv0 is the initial particle volume fraction and T is temperature in K.

The comparisons of calculation results with the fitting results for the cases with different initial particle volume fractions and different temperatures are also exhibited in Fig. 9. The maximum difference between the fitting results and the calculated results is 50 MPa, and the maximum relative error is about 7%. The error is within the acceptable range, since the effective irradiation swelling is not very sensitive to the particle hydrostatic pressure, especially at high pressure levels.

## 3.2. Effects of temperature

In a nuclear reactor core, the temperatures of fuel particles vary with their locations and irradiation conditions. The effective irradiation swelling of the considered inert matrix fuels also give a rise with temperature, as can be found in Section 3.1. Thus, the effects of irradiation temperature on the effective irradiation swelling should be investigated in detail. Fig. 12 displays the effective irradiation swelling results at different temperatures. The external hydrostatic pressure is set as100 MPa and the initial particle volume fraction is designated as 20%.

![](images/31d817c18a70024d62c7a2cb9fd0c1beeafd6b0c58b7bebde1c54bc8c3c06686.jpg)  
(a)

![](images/2b68ce8acb2f1b653c2e8feb257416b13812865833adaa00c96bb449b662b3b7.jpg)  
(b)  
Fig. 11. The effective irradiation swelling under different external hydrostatic pressures Hp at (a) T ¼ 573 K and (b) T ¼ 673 K.

![](images/b64a8a6a0ce281abbd56dae49461d7103be6a2492ae25d93deb5f21a2652d90d.jpg)  
Fig. 12. The effective irradiation swelling under different temperatures.

From 473 K to 573 K, the effective irradiation swelling increases slightly, because the temperature is relatively low and the particle hydrostatic pressure Hpf is high. From 573 K to 673 K, the effective irradiation swelling increases more significantly. This results from the sharp decrease of particle hydrostatic pressure, which is caused by the matrix creep. When the temperature is higher, the matrix creep will be larger, and the stress relaxation effect will be enhanced. From 673 K to 773 K, the effective irradiation swelling continues to rise up because of further decrease of particle hydrostatic pressure. It should be noted that the results in Fig. 12 are obtained with an assumption of constant external hydrostatic pressure Hp. If Hp is also lowered, the effective irradiation swelling will be correspondingly enlarged.

It can also be seen that the effective irradiation swelling accelerates after the critical fission density of grain recrystallization. With the increase of fission density, the coupling effects of hydrostatic pressure and temperature appear more significantly. The evolution phenomenon of effective irradiation swelling under different temperatures is also consistent with the evolution of intergranular bubble radius revealed by Eq. (2).

## 3.3. Effects of matrix creep

The fission product induced swelling leads to the stress and deformation in the matrix. The resultant creep strains in the matrix will also result in its stress evolutions, simultaneously affect the mechanical interactions between the fuel particles and the matrix. Hence, the fission gas swelling of fuel particles tends to be increased.

Fig. 13 gives the effective creep strain results of matrix at different temperatures at the fission density of 1.47  1028 fissions/ m3 . For all the cases, the external hydrostatic pressure is set as 100 MPa and the initial particle volume fraction is equal to the same value of 20%. It can be seen that the effective creep strains gradually decrease from the inside to the outside of matrix. The maximum magnitudes occur near the particle/matrix interface because the intensive particle/matrix interaction takes place here. From Fig. 13(a)e(d), it can be found that the effective creep strains increase with temperature. The maximum strain at 473 K is 0.044, while the maximum value at 773 K is 0.341, which increases by 674.4%.

The creep strains of the matrix will relieve the stresses of the matrix, and also affect the interaction between the matrix and particle. Thereby, it will affect the particle hydrostatic pressure and the fission gas swelling of fuel particles. Fig. 14 compares the results of hydrostatic pressure Hp0 at different temperatures for the cases with and without considering matrix creep. At 473 K, the effect of matrix creep is weak, and the differences of Hp0 is slight. As the temperature increases, the differences become more distinct. At 773 K, Hp0 is reduced by 92.6% with creep considered, compared to the no creep case. It can also be found that Hp0 sharply decreases from 573 K to 673 K for the case with creep considered, on account of the creep strains of matrix which is enhanced obviously with the temperature in this range so that the stresses of the matrix are lessened.

Fig. 15 compares the effective irradiation swelling at different temperatures for the cases with and without considering matrix creep. The results at 473 K and 573 K are close to each other, because the creep effect is weak at these two temperatures and Hp0 are similar with each other, as can be seen from Fig. 14. The effective irradiation swelling results with creep are larger than those without creep at 673 K, and the maximum relative difference is 9.24%. The effective irradiation swelling with creep at 773 K increases by 15.34% at the considered maximum fission density than the one without creep. The variations of effective irradiation swelling are consistent with the particle hydrostatic pressures in Fig. 14.

It can be known that the matrix creep can cause stress relaxation and affect the effective irradiation swelling of the considered inert matrix fuels, especially under high temperatures and high fission densities. It can be concluded that the matrix creep needs to be considered in developing effective irradiation swelling model, so that the obtained model can be used for an arbitrary, steady-state case.

The results of matrix shell thickness with and without creep contribution are compared in Fig. 16(a). With the enhancement of creep effect, the matrix shell thickness becomes smaller, and the maximum difference between the results with and without the creep contribution is about 2.82% at 773 K. It can be observed that the matrix shell thickness all decrease with the fission density. It should be mentioned that the deformations of the matrix are mainly induced by the plasticity strains for the case without creep. Because the stress of matrix is larger without the stress relaxing effects of creep, which induces the occurring of plasticity strain. From Fig. 16(b), one can find that the volume of the matrix remains the same, because the deformations of plasticity and creep will make no contributions to the volumetric variations.

## 3.4. Fitting models for effective irradiation swelling and current particle volume fraction

As mentioned previously, the effective irradiation swelling is defined as the ratio of the absolute volume variation to the initial volume of the finite element model. In fact, the absolute volume variation consists of two contributions from the matrix and fuel particle, as depicted in Fig. 17. One can find that the effective irradiation swelling is dominated by the contribution from the fuel particle. Especially, when the fission density is greater than \~3  1027fissions/m3 , the contribution ratio of the fuel particle reaches almost 100%. It is noted that the results in Fig. 17 are obtained for the case with the initial particle volume fraction of 20%, the temperature of 473 K and the external hydrostatic pressure of 100 MPa. For the other investigated cases, the effective irradiation swelling also originates from the contribution of fuel particles, because the deformations of plasticity and creep will result in no matrix volume variation despite their effects on the particle volume increase.

![](images/a3151cc95d8830bd87402e2c19615006f3cd10acd54986b164db47225723dfcc.jpg)

![](images/c4461b1e2e15689e3bed66b6f675f24accbc9b9125a9873e70b4ff4acdbcbae5.jpg)

![](images/5f54f47f77f08305d21fd405e6791ec04de399ce37190493259feb56595a1310.jpg)  
(a)

![](images/311f0b2a89c7f5485d5b883232fcd1d3c0fc2d93c07e78b2baaca4b36d50b58b.jpg)

![](images/b4bdb47dbe46df86545a1205f08d787d50874ee50c1cfd018d025514c124819a.jpg)

(b)  
![](images/6d609f956c5304e7ead62d16e92239ee5613c2e69dac0e407492679be0aa54d3.jpg)  
（C）

![](images/30d1b9ee3c2a00444a8efbd10a0f184ee110d1b8cfe3cba8fcc96c25a528d89c.jpg)  
(d)

Fig. 13. The effective creep strain contour plots of matrix at different temperatures at the fission density of 1.47  1028 fissions/m3 .  
![](images/45e9fd3dbef133f49657da6584a6ff9afd8f3313603888f9a27ce18417b1053d.jpg)  
Fig. 14. Hydrostatic pressure Hp0 under the condition of with and without matrix creep considered.

So, the effective irradiation swelling of the considered inert matrix fuels can be calculated as

$$
\tag{6}
$$

where Vf is the post-irradiation particle volume in the finite element model, Vf0 is the initial particle volume, V0 is the initial total volume of the finite element model, and V represent the Dabsolute volume variation of the finite element model. Eq. (6) can also be expressed as

$$
\tag{7}
$$

where fv0 is the initial particle volume fraction, and Vf is the ab-Dsolute volume variation of the fuel particle part in the finite element model, and Vf =Vf 0 is the irradiation swelling of fuel par-Dticle. Vf =Vf 0 mainly results from the fission gas swelling and Dfission solid swelling, which can be outputted with the state variables in the finite element simulations.

Fig. 18(a)e(c) depict the comparison of the effective irradiation swelling results obtained by Eq. (1) with the ones calculated by Eq. (7) under different conditions. The results agree well with each other. It indicates that the effective irradiation swelling satisfies Eq. (7). Once the fuel particle swelling is known, the effective swelling

![](images/59e78a0c0db141e7e2b8884ade6dcf5fda3ba9d07e5e4aa44f2a9b4d839db55e.jpg)  
(a)

![](images/abce103536be8753da0cce86eca34eaa08849b2cc15187a9560fb1e5242996eb.jpg)  
(b)

Fig. 15. The comparison of effective irradiation swelling at different temperatures with and without creep considered.  
![](images/45b673d5b5e1f440ffd9981bb364b587a1bed0d483f367aa7e81df818e37b682.jpg)  
(a)

![](images/c615170758b2b90fedaa0bea8f1321b8c9c0ebccaea8a5382c904396ba674f35.jpg)  
(b)

Fig. 16. (a) The comparison of matrix shell thickness with and without creep considered and (b) the volume of matrix with creep considered at different temperatures.  
![](images/bf2fed7897591462f4cf623f1c19f3bef24c68fda2369149c4c2a8b7c8791933.jpg)  
Fig. 17. The proportion of particle and matrix volume change.

can be obtained. It can also be known that Eq. (7) can be used to calculate the effective irradiation swelling of many kinds of inert matrix nuclear fuels, as long as the contribution of the matrix volume variation can be neglected.

The effective irradiation swelling is intensively related to the irradiation swelling of fuel particles. In this study, a fitting mathematical model for the irradiation swelling of PuO2 fuel particles is also developed. The total irradiation swelling of fuel particles includes the fission solid and gas swelling, described as

$$
\tag{8}
$$

The fission solid swelling is proportional to fission density and can be calculated as

$$
\tag{9}
$$

where, Fd depicts the fission density in fissions/m3 .

Importantly, a multi-variable coupling model for the fission gas swelling of PuO2 fuel particles is obtained as a function of external hydrostatic pressure, temperature, initial particle volume fraction and fission density, expressed as

$$
\tag{10}
$$

where, Hpf is the particle hydrostatic pressure in MPa, with Hpf ¼ Hp0 þHp, and Hp denotes the external hydrostatic pressure, namely the hydrostatic pressure obtained from calculation of the thermal-mechanical behavior in homogenized fuel pellets; T is the temperature in K, Fd is fission density in fissions/m3 . The critical fission density is dependent on fission rate, which can be described asFdx ¼ 4 - 1024ð \_f Þ 2=15. \_f is the fission rate in fissions/(m3 s).

![](images/86cc2f93d134bd670689cf810d946b26005b0e9ac071d138f09de1babfe894c4.jpg)  
(a)

![](images/5c727af3f3a315900a78e61bfbf8b623919b325fed85825ad2216315c6efe990.jpg)  
(b)

![](images/8cba0a8e4bfab0e84e1db2238ac8de78aa18d33122eec968d95a0bdcb0a13f3f.jpg)  
（c）  
Fig. 18. Verification of the effective irradiation swelling under (a) external hydrostatic pressure HP ¼ 100 MPa, (b) different temperatures and (c) different initial particle volume fractions.

![](images/f9cebb2beedf6c00cbc2f3ff1c516c232a857a510d28ee719321da589e2736fe.jpg)  
(a)

![](images/e8a3482079929ff9811ccc47494559a9d45d37333093f9678884f87b7ec8819d.jpg)  
(b)  
Fig. 19. Verification of the fitting mathematical model for the fission gas swelling of PuO2 particles under (a) different temperatures and (b) different particle hydrostatic pressures.

In fact, the contribution of matrix creep is also implicitly involved, which relies on the temperature, the fission density, the external hydrostatic pressure et al. and is coupled with the irradiation swelling of fuel particles. The comparison of finite element calculation results and fitting model results for the fission gas swelling of PuO2 fuel particles under different temperatures and different particle hydrostatic pressures are shown in Fig. 19. One can conclude that the fitting model results match well with the computation ones on the whole. When the fission density of fuel particles is near the critical fission density, the relative error can reach 10%. The relative error is below 5% at higher fission densities. As mentioned in the previous section, the contribution of fission gas swelling of fuel particles is remarkable at high fission densities. Consequently, the fitting mathematical model is acceptable.

Once the basic influencing variables are known, the irradiation swelling of fuel particles in the considered inert matrix fuels can be quickly calculated by the fitting mathematical model. Subsequently, the effective irradiation swelling can be obtained according to Eq. (7).

Apparently, the current volume fraction of fuel particles will change with the increase of fission density. In order to obtain the other effective thermo-mechanical performances, such as the effective thermal conductivity, it is necessary to obtain the mathematical model for the current volume fraction of inert matrix fuels. According to the definition of particle volume fraction, with the irradiation swelling of fuel particles known, the current particle volume fraction can be obtained as

![](images/ebbb6f058d57c35445eee27eb669fffba569a49e2729586600a8115feee2056c.jpg)  
Fig. 20. Verification of current particle volume fraction formula.

$$
\tag{11}
$$

where fv0is the initial particle volume fraction and DVfV is the irradiation swelling of fuel particles. The update particle volume Vf can be calculated as

$$
\tag{12}
$$

Similarly, the current fuel volume V can be obtained as

$$
\tag{13}
$$

which depends on the irradiation swelling of fuel particles, and the initial particle volume and volume fraction.

To ensure the correctness of Eq. (11), the finite element calculation results and the results calculated by the formula under the temperature of 573 K, the initial particle volume fraction of 20%, and the matrix external pressure Hp of 0 MPa are plotted in Fig. 20. One can find that the results obtained by two routes are in good agreement, which indicates that Eq. (11) can be used to update the particle volume fraction.

## 4. Conclusions

In this study, a fitting mathematic model for the effective irradiation swelling is developed, and a model of current particle volume fraction is also proposed, which is verified with the finite element results. The effective irradiation swelling of the considered inert matrix fuels is demonstrated to depend mainly on the irradiation swelling of fuel particles, as long as the contribution of matrix volume variation can be neglected. The gaseous swelling model of fuel particle and FE model results of effective irradiation swelling are verified through making comparison with experimental results and DART model. Through finite element analysis, the effects of external hydrostatic pressure, temperature and matrix creep on the effective irradiation swelling are investigated. The conclusions can be drawn as follows.

(1) The effective irradiation swelling of the considered inert matrix fuels decreases with the increase of external hydrostatic pressure, which is dominantly influenced when the particle hydrostatic pressure is lower than 300 MPa. This is attributed to the fact that the intergranular bubble radius depends on the particle hydrostatic pressure. For the conditions with the initial particle volume fraction of 20%, the temperature of 673 K and the fission density of 1.47 - 1028 fissions/m3 , the results indicate that the effective irradiation swelling for particle hydrostatic pressure of 285 MPa is reduced by \~15.77% compared to the case of 85 MPa.

(2) The effective irradiation swelling of the considered inert matrix fuels increases with temperature. From 573 K to 673 K, the effective swelling increases by\~10.9% at the fission density of 1.47 1028 fissions/m3 under the condition that the external hydrostatic pressure is 100 MPa and the initial particle volume fraction is 20%. The contribution from the intergranular bubble radius will be enlarged at higher temperatures. Simultaneously, the enhanced matrix creep lessens the particle hydrostatic pressure.

(3) The matrix creep can reduce the mechanical interaction between the matrix and fuel particles, and the weakened constraint effect accelerates the fission gas swelling of fuel particles. The matrix shell thickness decreases, and its circumference size increases to accommodate the enlarged fuel particle, but the matrix volume remains the same. The effect of creep on the effective irradiation swelling can be enhanced, which is induced by its coupling correlations with the temperature and the hydrostatic pressure within fuel particles.

## Declaration of competing interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Acknowledgement

The authors are very grateful for the supports of National Natural Science Foundation of China (No. 11772095), the support of the National Key Research and Development Program of China (2016YFB0700103) and the supports of the foundation from Science and Technology on Reactor System Design Technology Laboratory.

## References

[1] A.N. Holden, Dispersion Fuel Elements, Gordon and Breach Science Publishers Inc, New York, 1967.

[2] J.L. Kloosterman, P.M.G. Damen, Reactor physics aspects of plutonium burning in inert matrix fuels, J. Nucl. Mater. 274 (1999) 112e119.

[3] C. Lombardi, L. Luzzi, E. Padovani, et al., Thoria and inert matrix fuels for a sustainable nuclear power, Prog. Nucl. Energy 50 (8) (2008) 944e953.

[4] W.J. Carmack, M. Todosow, M.K. Meyer, K.O. Pasamehmetoglu, Inert matrix fuel neutronic, thermal-hydraulic, and transient behavior in a light water reactor, J. Nucl. Mater. 352 (2006) 276e284.

[5] Xin Gong, Shurong Ding, Yunmei Zhao, Yongzhong Huo, Lin Zhang, Yuanming Li, Effects of irradiation hardening and creep on the thermomechanical behaviors in inert matrix fuel elements, Mech. Mater. 65 (2013) 110e123.

[6] L.V. Duyn, Evaluation of the Mechanical Behavior of a Metal Matrix Dispersion Fuel for Plutonium Burning, Georgia Institute of Technology: A thesis for the Degree Master of Science in Mechanical Engineering, 2003.

[7] A. Savchenko, L. Konovalov, A. Vatulin, A. Morozov, V. Orlov, O. Uferov, S. Ershov, A. Laushkin, G. Kulakov, S. Maranchak, Z. Petrova, Dispersion type zirconium matrix fuels fabricated by capillary impregnation method, J. Nucl. Mater. 362 (2e3) (2007) 356e363.

[8] A.M. Savchenko, A.V. Vatulin, A.V. Morozov, et al., Inert matrix fuel in dispersion type fuel elements, J. Nucl. Mater. 352 (1e3) (2006) 372e377.

[9] E.A.C. Neeft, K. Bakker, R.P.C. Schram, et al., The EFTTRA-T3 irradiation experiment on inert matrix fuels, J. Nucl. Mater. 320 (1e2) (2003) 106e116.

[10] A.M. Savchenko, I.I. Konovalov, A.V. Vatulin, E.M. Glagovsky, New concept of designing Pu and MA containing fuel for fast reactors, J. Nucl. Mater. 385 (1) (2009) 148e152.

[11] A.M. Savchenko, A.V. Vatulin, E.M. Glagovsky, I.I. Konovalov, A.V. Morozov, A.V. Kozlov, S.A. Ershov, V.A. Mishunin, G.V. Kulakov, V.I. Sorokin, A.P. Simonov, Z.N. Petrova, V.V. Fedotov, Main results of the development of dispersion type IMF at A.A. Bochvar Institute, J. Nucl. Mater. 396 (1) (2010) 26e31.

[12] M. Suzuki H S, Light water reactor fuel analysis code, 2005. FEMAXI-6 (Ver.1) [Z].

[13] A. MATPRO, Handbook of Materials Properties for Use in the Analysis of Light Water Reactor Fuel Rod Behavior, 1978.

[14] Y.S. Kim, G.Y. Jeong, J.M. Park, A.B. Robinson, Fission induced swelling of UMo/ Al dispersion fuel, J. Nucl. Mater. 465 (2015) 142e152.

[15] Y.M. Zhao, J.Y. Zhang, S.R. Ding, A new method for solving the fission gas diffusion equations with time varying diffusion coefficient and source term considering recrystallization of fuel grains, Nuclear Materials and Energy 20 (2019) 100686.

[16] J. Rest, A model for fission-gas-bubble behavior in amorphous uranium silicide compounds, J. Nucl. Mater. 325 (2e3) (2004) 107e117.

[17] J. Rest, Application of a mechanistic model for radiation-induced amorphization and crystallization of uranium silicide to recrystallization of UO2, J. Nucl. Mater. 248 (1997) 180e184.

[18] A. Leenaers, W. Van Renterghem, S. Van den Berghe, High burn-up structure of U(Mo) dispersion fuel, J. Nucl. Mater. 476 (2016) 218e230.

[19] Y. Cui, S.R. Ding, Z.T. Chen, Y.Z. Huo, Modifications and applications of the mechanistic gaseous swelling model for UMo fuel[J], J. Nucl. Mater. 457 (2015) 157e164.

[20] X. Tian, X.Z. Kong, F. Yan, S.R. Ding, Hydrostatic pressure effect of fission gas swelling in UMo/Al dispersion fuel plate, Atomic Energy Sci. Technol. 51 (11) (2017) 2062e2068.

[21] Y.B. Miao, A. Kyle, David Andersson Gamble, et al., Gaseous swelling of U3Si2 during steady-state LWR operation: a rate theory investigation, Nucl. Eng. Des. 322 (2017) 336e344.

[22] M.C. Paraschiv, A. Paraschiv, V.V. Grecu, On the nuclear oxide fuel densification, swelling and thermal re-sintering, J. Nucl. Mater. 302 (2) (2002) 109e124.

[23] Y.S. Kim, G.L. Hofman, J.S. Cheon, A.B. Robinson, D.M. Wachs, Fission induced swelling and creep of UeMo alloy fuel, J. Nucl. Mater. 437 (1e3) (2013) 37e46.

[24] G.Y. Jeong, Y.S. Kim, D. Sohn, Mechanical analysis of UMo/Al dispersion fuel, J. Nucl. Mater. 466 (2015) 509e521.

[25] Z.H. Xing, S.H. Ying, Study on the irradiation swelling of U3Si2-Al dispersion fuel, Atomic Energy Sci. Technol. 35 (1) (2001) 15e19.

[26] J. Rest, et al., The DART Dispersion Analysis Research Tool: A Mechanistic Model for Predicting Fission-Product-Induced Swelling of Aluminum Dispersion Fuels, Argonne National Laboratory, 1995.

[27] X. Gong, Y.M. Zhao, S.R. Ding, A new method to simulate the micro-thermomechanical behaviors evolution in dispersion nuclear fuel elements, Mech. Mater. 77 (2014) 14e27.

[28] Q.M. Wang, X.Q. Yan, S.R. Ding, Y.Z. HUO, Research on the interfacial behaviors of plate-type dispersion nuclear fuel elements, J. Nucl. Mater. 399 (1) (2010) 41e54.

[29] Q.M. Wang, Y. Cui, S.R. Ding, Y.Z. HUO, Simulation of the coupling behaviors of particle and matrix irradiation swelling and cladding irradiation growth of plate-type dispersion nuclear fuel elements, Mech. Mater. 43 (4) (2011) 222e241.

[30] W. CAI, Y.M. ZHAO, X. GONG, S.R. DING, Y.Z. HUO, Calculation simulation of equivalent irradiation swelling for dispersion nuclear fuel, Atomic Energy Sci. Technol. 49 (3) (2015) 502e510.

[31] Y.M. Zhao, X. Gong, S.R. Ding, Y.Z. Huo, A numerical method for simulating the non-homogeneous irradiation effects in full-sized dispersion nuclear fuel plates, Int. J. Mech. Sci. 81 (2014) 174e183.

[32] M.L. Liu, Y.H. Lee, Dasari V. Rao, Development of effective thermal conductivity model for particle-type nuclear fuels randomly distributed in a matrix, J. Nucl. Mater. 508 (2018) 168e180.

[33] Z. Hashin, Analysis of composite materials-a survey, Appl. Mech 50 (1983) 481e505.

[34] P S. In Sanchez-Palencia E Z A E. Homogenization Techniques for Composites Media, Springer-Verlag, Berlin, 1987.

[35] J. Rest, DART model for irradiation-induced swelling of uranium silicide dispersion, Fuel Elements 126 (1998) 88e101.

[36] B. Ye, J. Rest, A Description of the Mechanistic DART-THERMAL Dispersion Fuel Performance Code and Application to Irradiation Behavior Analysis of U-

Mo/Al, 2013.

[37] Y.M. Zhao, X. Gong, Y. Cui, S.R. Ding, Simulation of the fission-induced swelling and creep in the CERCER fuel pellets, Mater. Des. 89 (2016) 183e195.

[38] J. Rest, A model for the effect of the progression of irradiation-induced recrystallization from initiation to completion on swelling of UO2 and U-10Mo nuclear fuels, J. Nucl. Mater. 346 (2005) 226e232.

[39] J. Spino, J. Rest, W. Goll, C.T. Walker, Matrix swelling rate and cavity volume balance of UO2 fuels at high burn-up, J. Nucl. Mater. 346 (2005) 131e144.

[40] J.D. Hales, R.L. Williamson, S.R. Novascone, et al., BISON Theory Manual the Equations behind Nuclear Fuel Analysis, Idaho National Laboratory, 2016.

[41] Martin Lemes, Alejandro Soba, Alicia Denis, An empirical formulation to

describe the evolution of the high burnup structure, J. Nucl. Mater. 456 (2015) 174e181.

[42] J. Spino, A.D. Stalios, H. Santa Cruz, D. Baron, Stereological evolution of the rim structure in PWR-fuels at prolonged irradiation: dependencies with burn-up and temperature, J. Nucl. Mater. 354 (2006) 66e84.

[43] J. Noirot, L. Desgranges, J. Lamontagne, Detailed characterisations of high burn-up structures in oxide fuels, J. Nucl. Mater. 372 (2008) 318e339.

[44] B. Roostaii, H. Kazeminejad, S. Khakshournia, Influence of porosity formation on irradiated UO2 fuel thermal conductivity at high burnup, J. Nucl. Mater. 479 (2016) 374e381.
