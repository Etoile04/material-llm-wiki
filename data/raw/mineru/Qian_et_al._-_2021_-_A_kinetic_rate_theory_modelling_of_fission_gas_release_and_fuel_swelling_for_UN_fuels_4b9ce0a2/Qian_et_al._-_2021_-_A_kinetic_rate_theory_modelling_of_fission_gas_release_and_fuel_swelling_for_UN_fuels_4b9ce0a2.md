# 📄 PDF Parsing Result

**File:** `/Volumes/openclaw记忆/Zotero_storage/storage/TLW8PEBJ/Qian et al. - 2021 - A kinetic rate theory modelling of fission gas release and fuel swelling for UN fuels.pdf`
**Backend:** `pipeline`
**Pages:** 0 to end
**Formula Recognition:** ❌ Disabled
**Table Recognition:** ✅ Enabled

---

# A kinetic rate theory modelling of fission gas release and fuel swelling for UN fuels

![](images/2c818d677066e43bdee5524c287a51d345306c11d33f26efa58dfd2775d582b2.jpg)

Zhengyu Qian a , Wenbo Liu a , Rui Yu b , Yujie Tao b , Di Yun a,c,∗ , Long Gu b,d,e,∗

a School of Nuclear Science and Technology, Xi’an Jiaotong University, Xi’an 710049, China

b Institute of Modern Physics, Chinese Academy of Sciences, Lan Zhou 730000, China

c State Key Laboratory of Multi-phase Flow, Xi’an Jiaotong University, Xi’an 710049, China

d University of Chinese Academy of Sciences, Beijing 100049, China

e School of Nuclear Science and Technology, Lanzhou University, Lanzhou 730000, China

## a r t i c l e i n f o

Article history:   
Received 5 November 2020   
Revised 5 June 2021   
Accepted 6 July 2021   
Available online 10 July 2021

Keywords:   
UN fuels   
Fission gas release   
Fuel swelling   
Kinetic rate theory

## a b s t r a c t

Fission gas behavior and fuel swelling have always been an important issue for nitride fuels. In this paper, a mechanistic fission gas behavior model of nitride fuels has been established using the kinetic rate theory, based on the fuel temperature distribution input provided by a finite element computational platform. The fission gas release and fuel swelling of the nitride fuels were simulated in details and the simulation results were compared with experimental data from open literature. Using the established model, previous diffusion coefficients of Xe gas in nitride fuels derived by earlier works were analyzed, and a new diffusion coefficient suitable for simulation of nitride fuels was proposed. A parameter sensitivity analysis was carried out for the two important parameters in the rate theory simulation of fission gas behavior, the nucleation factor and the resolution coefficient. Suitable values for both parameters for nitride fuels were determined, and their influence on fission gas behavior and fuel swelling were assessed. In addition, a bimodal distribution for bubble size was observed and the underlying physics driving factor was determined to be the gas bubble resolution.

© 2021 Elsevier B.V. All rights reserved.

## 1. Introduction

Nitride fuel has the characteristics of high uranium atom density, good thermal conductivity and high melting point. It has a wide range of use in space reactors [1] and fast reactors [2], and is one of the options for Accident Tolerant Fuels (ATF) [3]. However, due to the fission reaction, a large amount of fission products will be produced. Among all fission products, noble gas, because of their very low solubility in the fuel matrix, will exist in the form of gas bubbles in the fuel matrix [4]. Under certain conditions, these gas bubbles coalesce and grow in size, and the resulting large bubbles will increase the fuel swelling [5]. At the same time, gas atoms can diffuse to the grain boundary, gather at the grain boundary and form interconnected tunnels and release the gas to the fuel plenum. The released fission gas will affect the cladding internal pressure and thermal conductivity of the fuel cladding gap [4]. Therefore, to achieve an understanding of fission gas behavior and to be able to predict fission gas behavior in nuclear fuels is necessary.

At present, for the simulation of the fission gas behavior and fuel swelling of nitride fuels the researchers largely relied on empirical models such as the Storms’ relationship [6], due to the lack of open literature information on detailed microstructures and physics mechanisms. However, the empirical relationship is highly dependent on experimental data and is applicable only to situations that fall into the regime of the conditions of the experiment from which the model was derived. If the experimental conditions start to deviate from this regime, the corresponding empirical relationship may not be useful. Therefore, it is necessary to develop a mechanistic model that can reasonably capture the fission gas behavior of nitride fuels. However, there are few mechanistic models for the fission gas behavior of nitride fuels. Feng [7] established a mechanistic model for simulating the fission gas release and fuel swelling of nitride fuels, which account for the fission gas behavior and fuel swelling of nitride fuels under multiple experimental conditions. But the model is relatively simple, an average bubble size was used to represent the detailed bubble size distribution, and the resolution constant is much higher than that usually used under other conditions [8-11]. Therefore, there is a space for further improvement and further verifications are needed as well.

![](images/063f819314e3223bc8723ad268fc66b9e1d33e4f3fe783a339529a86f3cfabd1.jpg)  
Fig. 1. The temperature of JOYO’s case versus burnup.

Using the classical kinetic rate theory to simulate fission gas behavior started with Booth [12], and then it was further developed by Speight [13], Hayns and Wood [14], Rest [15-17] and others, and as of now, it has become a mature method in this area. A crucial step towards developing a good rate theory model is the determination of key parameters, including the diffusion coefficient, the nucleation factor, the resolution constant, etc. Determining these key parameters usually requires a significant amount of experimental data. The acquisition of the diffusion coefficient of gas atoms mainly depends on the experimental measurements. The difference in diffusion coefficients under different experimental conditions can be very large [7, 18]. The main reason is that the measurement of gas atom diffusion coefficient is inherently very complicated. Take ceramic oxide fuel which is somewhat similar to nitride fuel into account, the boundary condition of a thin tracer layer is usually adopted, and sectioning or a nondestructive nuclear technique is used to determine the diffusion profile following annealing [19]. To obtain reliable results, the sample surface usually needs to be flat and representative. Surface preparation is very difficult with ceramic fuel due to the hardness and brittleness of the materials and the possibility of concentration gradients by preferential evaporation of one or more elements [20], which may cause deviations from the bulk composition. The nucleation factor FN is used to evaluate the stability of the Xe dimers during the nucleation process, and is the probability that the Xe dimers can exist stably after initial formation. In the rate theory simulation under different conditions [9-11,21-24], the nucleation factor is between 10−10-1; similarly, under different conditions, the resolution constant, which characterizes the intensity of the resolution effect, or the ability of a fission fragment to knock fission gas atoms from the bubbles back to the fuel matrix, is also between 10−19-10−15 cm3 [8-11]. The reason for the large difference is that the fuel type and the simulation conditions selected in the above simulation are different. Therefore, determination of all the above three parameters suitable for the selected simulation conditions for nitride fuels is a problem worthy of in-depth consideration. In this work, kinetic rate theory was used to establish the fission gas release and fuel swelling model for nitride fuels, and the key parameters such as the gas atom diffusion coefficient, nucleation factor and resolution constant were determined.

In the process of determination the resolution constant in this work, it was found that the bubble distribution calculated by the model showed a typical bimodal shape, the number density of small-size bubbles and large-size bubbles is far more than that of medium-size bubbles, and the size distribution of bubbles has a peak in the small-size and large-size regions, respectively. The bimodal bubble size distribution is a phenomenon ubiquitous in nuclear fuels. It exists in many types of fuels, including oxide fuels [25-26] and silicide fuels [27]. Kashibe et al. [26] attribute the bimodal distribution to either coalescence of small bubbles, or bubble growth due to vacancy capture into the bubbles that contain solid fission products precipitate. Chkuaseli [25] believes that the bimodal bubble size distribution is the result of the combined effect of the surface and volume diffusion mechanisms. He established a model, and then suppressed the surface diffusion, found that there was no bimodal distribution, and finally reached the conclusion. However, the calculation results of the model used in this paper show that the resolution has a greater impact on the bimodal distribution, which is far from the conclusion drawn by the above-mentioned researchers, and is worthy of deeper study. In view of the bimodal bubble size distribution in the calculation results of the model, it is proposed that resolution is the main driving factor for the bimodal bubble size distribution.

## 2. Mathematical model

The behaviors of fission gas are very complicated, mainly including the nucleation and diffusion of gas atoms in the grain, the coalescence and growth of intragranular bubbles, the accumulation and growth of bubbles at the grain boundaries, and the release through interconnected tunnels. The framework of the mechanistic model for nitride fuels is mainly derived from the mechanistic model, GRASS-SST [28] and FASTGRASS [29], initially developed for UO2 fuels by Rest. Based on the FASTGRASS model, the bubble size grouping method proposed in the GRASS-SST code was added. A new method of calculating the resolution constant was added to the model as well. At the same time, according to the characteristics of UN fuel, the process of fission gas accumulation on the grain face was treated in a simplified manner. The model uses a set of coupled nonlinear differential equations to obtain the concentration of fission gas atoms and bubbles at different locations of the fuel (in the bulk, on the grain face, on dislocations, and on the grain edge) in the following form:

$$
\tag{1}
$$

Where, Cα,i represents the concentration of the bubble of the group i (when i=1, replace it with the letter g, which represents the concentration of gas atoms); α=f, e represents the concentration of the bubbles in grain face and grain edge, respectively (when there is no value, it represents the concentration of intragranular bubbles); aα,i, bα,i, eα,i correspond to the rate constants of different fission gas behavior affecting bubble concentration respectively.

The model uses the bubble size grouping method assuming that the first group (i=1) contain one gas atom, the number of gas atoms contained in each bubble of the group i can be expressed as:

$$
\tag{2}
$$

Where, Ni and Ni-1 represents the number of gas atoms contained in the bubbles of the group i and the group i-1; m represents the multiplier of the number of gas atoms contained in the bubbles of the group i as compared to the group i-1, and this value is usually taken as 2 for fine simulation calculations. For the case that the number of gas atoms in the bubble Nk is neither equal to Ni nor Ni 1. In this case, we use a probability Pi such that with probability of Pi this bubble belongs to group i, and with the probability (1-Pi) that this bubble belongs to the i+1 group, and the Pi is calculated by equation: Pi = Nk−NiN N .

![](images/47aa2912bf7359016b4f1891315b9404a1e405138b00ef0db92adec8e9b9681b.jpg)

![](images/84986fb88455d357857c604b552b1e46bb697b8295e7a5d9595dba22e89a0c99.jpg)  
(a)

(b)  
![](images/14a01962f25cdeca0901ce9407e40f31fc955f08061b99211782d003dbf441b2.jpg)  
（c）  
Fig. 2. Comparison between (a) the fission gas release, (b) the fuel swelling and (c) the proportion of intragranular gas of the model with different diffusion coefficients and the experimental value [30]. The left horizontal axis represents the nucleation factor, which changes from 1 to 1e-5, and the right horizontal axis represents resolution constant, which varies from 1e-19 to 1e-16.

The Eq. (1) has different form in different position of a grain, for the intragranular gas atoms, the form is:

$$
\tag{3}
$$

Where, FN is the nucleation factor; Rg is the radius of the intragranular gas atom; Dg is the diffusion coefficient of the intragranular gas atom; Sgb represents the grain boundary area per unit volume; Vg represents the velocity of intragranular gas atoms; dg is the diameter of the grain, 10μm; Vgb is the velocity of grain boundary; η is the yield of fission gas, 0.25; f is the fission rate; I corresponds to the total number of bubble groups.

The terms on right hand side of the Eq. (3) represent, respectively, 1. the loss of gas atoms due to nucleation; 2. the loss of gas atoms caused by capture of gas atoms by bubbles; 3. and 4. the loss of gas atoms due to biased and random diffusion of gas atoms to grain boundaries; 5. the loss of gas atoms due to grain boundary sweeping; 6. the gain of gas atoms due to fission; 7-9. the increase of gas atoms caused by resolution from intragranular bubbles and bubbles in grain face and grain edge.

The fourth term on right hand side of the Eq. (3) refers to the flux of gas atoms diffused to the grain boundary under the concentration gradient, which can be obtained by solving the concentration of gas atoms in spherical grain. The specific solution can refer to the FASTGRASS Manual [29].

It is worth noting that the Pi,j, which represents the probability of the coalescence between bubbles in group i and group j, has the following general form [5]:

$$
\tag{4}
$$

Where, Ri and Rj are the radius of bubbles in group i and group j respectively; Di and Dj are the diffusion coefficient of bubbles in group i and group j respectively; Vi and Vj represent the velocity of bubbles in group i and group j respectively. The two terms of Eq. (4) correspond to the bubble coalescence caused by random (motion in a concentration gradient) and biased (motion in a temperature gradient) migration of bubbles, respectively. It should be noted that when i=j, the value of Pi,j needs to be changed to one-half of the original value, so that each pairwise coalescence is counted only once. The bubble radius is determined by the Vander Waals model. It is solved by two equations,P( 4 π R2 − BNi) = NiKBT , P = 2γRi + Ph, where B is the Vander Waals constant, 8.5×10−32m3, γ is surface energy of bubbles, 10 N/m, Ph is the hydrostatic pressure, where 107 N/m2 was used, Ni is the number of gas atoms in a bubble, KB is Boltzmann constant. We can obtain the bubble radius from the above two equations. The diffusion coefficient of the bubble is [5] Di = 3a40Ds2πR4 , the velocity of the bubble is [5]Vi = 3DsQ∗s a0k T 2R dTdx . α0 is the lattice constant, 0.49nm. Ds = 1.92 × 103 exp(− 4.22×104RT ) RT as can be referred in Weaver’s work [37].

![](images/c217ba78cfc3ba66d064aac003224349c1ed9897b88be1f7c020d50637d21732.jpg)  
Fig. 3. Comparison between the proportion of intragranular gas of the model with different Grain diameter and the experimental value [30].

bi represents the intensity of the resolution of bubbles in group i, and it takes the form used by Lösönen [8]:

$$
\tag{5}
$$

Where, b0 is the resolution constant; d is the thickness of the layer on the bubble surface that allows gas atoms to escape, 1nm; Ri is the bubble radius; δ is the thickness of the layer where the resoluted gas atoms can return to the bubble through diffusion, 0.4nm; f is the fission rate.

For the intragranular bubbles in group i, the Eq. (1) is modified to become:

$$
\tag{6}
$$

The terms on the right hand side of the Eq. (6) represent, respectively, 1. the gain of bubbles in group i due to the coalescence of small bubbles; 2. the loss of bubbles in group i due to coalescence between bubbles in group i and bubbles in other group; 3. and 4. the loss of gas bubbles in group i due to biased and random diffusion of gas bubbles to grain boundaries; 5. the loss of gas bubbles in group i due to grain boundary sweeping; 6. the loss of gas bubbles in group i due to resolution; 7. the gain of gas bubbles in group i due to bubble pull-off from a moving grain boundary (if the bubbles are bigger than a given critical size, otherwise they are equal to zero); 8. the gain of gas bubbles in group 2 due to nucleation.

Table 1  
Characteristics of fuel sample [30].
<table><tr><td colspan="2">Parameter</td></tr><tr><td>Diameter (mm)</td><td>7.43</td></tr><tr><td>Height (mm)</td><td>8</td></tr><tr><td>Bulk density (%T.D.)</td><td>86.0</td></tr><tr><td>Fuel stack length (mm)</td><td>198.8</td></tr><tr><td>U235-enrichment (wt%)</td><td>19.39</td></tr><tr><td>Cladding material</td><td>15Cr-20Ni stainless steel</td></tr></table>

For the gas atoms and bubbles on the grain face and the grain edge, the specific form of Eq. (1) is arranged in the Appendix to reduce the length of the paper. The fractional fission gas release and the fuel swelling caused by gas atoms are obtained by Eqs. (7) and (8), respectively.

$$
\tag{7}
$$

Where, Ngf is the number of grain faces per grain; PA is the interlinkage fraction of the grain face channel; PI is the grain edge interlinkage fraction; SNB is the area of node boundary/volume of the node; the values of PA and PI are taken from the FASTGRASS Manual [29].

The three term on right hand side of the Eq. (7) represent the gas come from the venting of the grain face gas into interconnected grain edge tunnels, from the venting of grain edge gas bubbles through newly interconnected tunnels, and from long-range migration of fission gas bubbles in grain face up the temperature gradient, respectively.

$$
\tag{8}
$$

In this way, the mechanistic model of the fission gas release and swelling of UN fuels has been established. The model can calculate the fission gas release and the fuel swelling caused by the retained fission gas of UN fuels.

## 3. Results and discussion

## 3.1. Settings of input parameter

There are only few experiments focusing on the fuel swelling and fission gas behavior of nitride fuels. In order to validate the model, the results of the UN in-reactor irradiation experiment in the experimental reactor JOYO [30] were selected as the object of the simulation because the literature of the JOYO experiment provided very detailed information regarding fission gas behavior.

The characteristics of fuel sample used by the experiment are shown in Table 1 [30]. In order to obtain the temperature parameters that can be used for the mechanistic model of UN fuels, we used the geometric parameters in Table 1 and the known fuel line power to establish a finite element model of the fuel based on the finite element platform of COMSOL Multiphysics [31]. The thermal conductivity model of the cladding material is difficult to find. So we used the thermal conductivity model of D9 [38], which is also austenitic stainless steel. When the temperature is below than 1000K λ = 7.598 + 2.391 × 10−2T − 8.899 × 10−6T 2, otherwise λ =

![](images/561c91f4f6f869def1b59153899b692898447508e8cd1bc85f07ac9813baa9e1.jpg)  
（a)

![](images/4c5d2bf23093e09792d9f56c7e9d0f402c9f4e600b72446e7f6fcd41c6879cfe.jpg)  
(b)

![](images/917ba1eb159bf89156e89c5a55740f010f6fc1d029b35d94cf0b1026091d9773.jpg)  
（c）  
Fig. 4. Comparison between (a) the fission gas release, (b) the fuel swelling and (c) the proportion of intragranular gas of the model with modified diffusion coefficients and the experimental value [30]. The left horizontal axis represents the nucleation factor, which varies from 1 to 1e-5, and the right horizontal axis represents resolution constant, which changes from 1e-19 to 1e-16.

7.260 + 1.509 × 10−2T. The thermal conductivity model [39] of UN is k = 1.37T 0.41(1 − P)(1 + P), P is porosity.

We then simulated the test samples of the JOYO reactor experiment. The He gap closing process and the resulting temperature decrease was simulated following the reference from Blank [32]. In order to simplify the process, we simplified it into a linear change. The detailed temperature is shown in Fig. 1.

## 3.2. Determination and interaction mechanism of key parameters

The key parameters used for the two simulation cases above have been listed in Table 2. Most of the parameters were determined in the simulation case of the JOYO experiment. The process of determining each parameter will be described in details below.

Table 2  
Key parameters used in the simulation.
<table><tr><td>Symbol</td><td>Property</td><td>Value</td></tr><tr><td>Dg</td><td>diffusion coefficient (cm2.s-1)</td><td>4.05×10-3exp[-2.15x10 RT</td></tr><tr><td>Fn</td><td>nucleation factor</td><td>1×10-4</td></tr><tr><td>bo</td><td>resolution constant (cm)</td><td>1×10-18</td></tr></table>

∗R is the gas constant (J•mol−1•K−1), T is the temperature of gas atoms (K).

## 3.2.1. Diffusion coefficient

The fission gas diffusion coefficients that have been proposed for UN fuel are summarized in Table 3. For the purpose of comparison, all these diffusion coefficients were used in our model to generate corresponding simulation results on the fission gas behavior. A key experimental value that was used to gauge the accuracy of the diffusion coefficients is the ratio of gas atoms retained in the grain, which has been determined to be 80% [30]. The determination of parameters is indeed a difficulty in rate theory. There are too many parameters that may affect the final result. Therefore, we make a detailed parameter sensitivity analysis to prove the rationality of the parameters chosen in this work.

![](images/7dc83cf0b055019da7a4b60e3bcab995f2923f2b7e7a08c2dba67885e46d10fe.jpg)  
(a)

![](images/76c6d756d3b828b87fcd442a6c57360995138a1c89b82f1edd3f22efb941d830.jpg)  
(b)

![](images/51065243f443e3ca4d0f52a6d0c2edc6f52f4eec71adcd1ee66ffd2856063c47.jpg)  
(c）  
Fig. 5. Comparison between (a) the fission gas release, (b) the fuel swelling and (c) the proportion of intragranular gas of the model with different combinations of nucleation factor and resolution constant and the experimental value [30].

Summary of diffusion coefficients in open literature [7, 18].
<table><tr><td>Reference</td><td>Value</td></tr><tr><td>Melehan and Gates</td><td>4.0× 10-6exp[-2.7110] RT</td></tr><tr><td>Biddle</td><td>3.0×10-8exp[- 2.41×105 RT</td></tr><tr><td>Oi</td><td>2.15×105 2.05× 10-4 exp[- RT</td></tr><tr><td>BMI</td><td>4.65×10-4exp[- 3x105 RT</td></tr><tr><td>NASA</td><td>2.4 ×10-10 exp[- 1.57×105 RT</td></tr></table>

Firstly, according to the five groups of diffusion coefficients that can be obtained from literature research, we have carried out more than 210 sets of tests with different nucleation factors and different resolution constants, and obtained the calculation results as shown in the Fig. 2 below. After finishing this step, we found that, considering the three experimental values we can refer to, the calculated results with diffusion coefficient by Oi are the closest to the simulated conditions, but the disparity between the calculated results and the experimental values is still quite large. Among the three key experimental values for calibration, we are most concerned with the proportion of intragranular gas, which directly reflects the distribution of fission gas (80% in the grain bulk, 15% at the grain boundary, 5% released), as this information is not available in any other experiments for UN fuels. However, the results of parameter sensitivity analysis show that the five groups of diffusion coefficients we investigated cannot meet the requirement of closely matching with experimental data.

For the proportion of intragranular gas, only a few parameters can affect it, mainly including the diffusion coefficient of gas atoms and the grain size. Therefore, on the basis of Oi’s diffusion coefficient, we considered the effect of different grain diameters. Fig. 3 shows the comparison between the calculated results and the experimental values with different grain diameters. It can be seen that with the increase of grain diameter, the proportion of intragranular gas is increasing, which means that the larger the grain diameter is, the more difficult it is for the fission gas to reach the grain boundary. For the grain diameter of UN, 20 μm was used in REDSTONE [18] and 10 μm was used in FRAPCON-EP [7]. Therefore, we choose to test the grain diameter in the range of 10 μm to 25 μm. And the above 210 tests are with the grain diameter of 10 μm. That is to say, even if the minimum grain diameter is used, a reasonable result cannot be obtained. We can only adjust the diffusion coefficient to get more fission gas to the grain boundary.

The pre-exponential factor of Oi’s diffusion coefficients are increased by factors of 10, 20, 30 and 40, respectively. The results of the calculation are shown in Fig. 4. First of all, we should pay attention to the change of fuel swelling with our selected parameters. It can be seen that the change of fuel swelling caused by the change of diffusion coefficient is relatively small. This is because that with the increase of the diffusion coefficient of gas atoms, there will be two effects. One is that the number of fission gas atoms in the grain bulk will decrease. Because of the decrease of gas atoms, the number of gas atoms that can enter gas bubbles will decrease, and the swelling will be mitigated; another is that the increase of gas atom diffusion coefficient will lead to the increase of bubble coalescence probability, so the probability of gas atom absorbed by bubbles will increase, and this will lead to increase of swelling. The two effects are contradictory, so in most cases, with the increase of diffusion coefficient of gas atoms, the changes of swelling are very small due to the two contradictory effects. We found that the effect of diffusion coefficient is enhanced in the region of small nucleation factor and large resolution constant. This is because that when the nucleation factor is small, the increase of the proportion of large bubbles in the bulk becomes strong, at the same time, a large resolution constant will lead to the gas atoms in the grain boundary bubble to return to the grain, which will supplement the number of gas atoms in the bulk. In this case, the effect of decreasing gas atom caused by the increase of diffusion coefficient will be weakened, and the effect of increasing bubble coalescence rate caused by the increase of diffusion coefficient will increase. Therefore, the effect of diffusion coefficient on swelling will be enhanced in the region of small nucleation factor and large resolution constant. In general, the swelling caused by the adjustment of diffusion coefficient is much smaller than that of the other two key parameters. So we choose this three combinations of nucleation factor and resolution constant with the least relative error between the calculated results and the experimental values, they are (1e-4+1e-18), (1e-3+5e-18), (1e-3+1e-17) respectively. For convenience, we rearrange the results of the above three combinations. We can see that in Fig. 5, with the increase of diffusion coefficient, the fission gas release increases and the proportion of intragranular gas decreases. From the data of intragranular gas proportion, we can exclude the combination (1e-3+5e-18) and (1e-3+1e-17), because even at the maximum diffusion coefficient of 40∗Oi, they are still far from the experimental value of 80%. So we finally chose the combination of (1e-4+1e-18), we also fine tuned the diffusion coefficient, and finally determined that the most appropriate diffusion coefficient is4.05 × 10−3 exp[− 2.15×105RT ]. Fig. 6 shows the comparison between the diffusion coefficient we derived for our model and the diffusion coefficients from the literature in the past.

## 3.2.2. Nucleation factor

The nucleation factor FN is used to evaluate the stability of the bubble core during the nucleation process. It refers to the probability that the bubble core can exist stably after initial formation [17]. In previous works, the nucleation factor FN is usually taken as a constant. For example, the constant 1 was used in the simulation of the fission gas behavior of UO2 by Rest [34]; Miao [9- 10] chose 0.01 for FN in the application of rate theory modeling for U3Si2 fuel; however, the value of FN is usually between 10−4-10−10 among metallic fuels [21-24]. For UN fuel, only a value of 0.027, which was used by Feng [7], is available for reference. Therefore, for UN fuel, the determination of the nucleation factor is a key point worth discussing. In this paper, the experimental results of JOYO reactor were used to determine the most suitable nucleation factor for UN fuel.

![](images/725de4e38e4d37be1d1f4c8f4235e7535c3450d5255237bddffeb49e8fdf357a.jpg)  
Fig. 6. Comparison between the inferred diffusion coefficient and that in open literature [7, 18].

Generally speaking, the smaller the nucleation factor, the smaller the number of stable bubble cores formed, and the bubble core is the incubation point of stable bubbles. The smaller the number of cores, the larger every single bubble can grow as the partitioning of fission gas is into a smaller amount of bases. The contribution of large bubbles to fuel swelling is much higher than that of small bubbles, considering the same number of total gas atoms, so the fuel swelling will be greater. At the same time, when the bubbles and the number density of bubbles are small, the bubbles’ ability to absorb gas atoms will be weakened. A large number of gas atoms can reach the grain boundary through diffusion and release to the free space, so the release of fission gas will be enhanced. As a result, the proportion of gas atoms retained in the grain will also decrease.

The results of our model under different nucleation factors and comparison with experimental values are shown in Fig. 7. The value of 10−4 is recognized to be the most suitable nucleation factor for UN fuel by a comprehensive consideration of all the three comparisons shown in the Fig. 7.

## 3.2.3. Resolution constant

The resolution constant b0 is used to describe the intensity of the resolution effect. In the process of analyzing the behaviors of fission gas, the effect of resolution was determined to be very significant. In the simulation of fission gas behavior of other fuel types, Rest [11] used b0 2 10−17 cm3 and b0 2 10−18 cm3 for UO2 and U-10Mo fuel, respectively. In addition, in the simulation of UO2 fuel, Lösönen [8] used b0=3×10−17 cm3. Miao [9-10] chose b0=2×10−17 cm3 as the resolution constant for U3Si2 fuel; in the simulation of UN fuel, Feng [7] used b0=1.36×10−15 cm3, which is significantly larger than the value used by others. To obtain the most accurate resolution constant that can be used for UN fuel, different resolution constants were used in the simulation of the JOYO experiment, and the resolution constants for comparison were selected to be between 10−19-10−16. The results are shown in the Fig. 8. It is found that the three important quantities, fission gas release, fuel swelling and proportion of intragranular gas, showed different trends. The resolution effects will cause the gas atoms in both intragranular and intergranular bubbles to be knocked back to the fuel matrix [35]. It is easy to infer that the proportion of gas atoms in the grain will increase with the increase of the resolution constant, because there are more gas atoms knocked back to the fuel matrix. However, the trend of fission gas release and the fuel swelling are more complex with the change of the resolution constant. The fuel swelling rises at the beginning and then fall when the resolution constant is increased, while the release of fission gas possesses opposite trend to the fuel swelling.

![](images/f9c48cdfbf33cad19fed2186f74005311ab70969089a9449295473c94de900fd.jpg)  
(a)

![](images/73e4e3177f5722bd4cb2ae23291db9b53c8f41db882f2f60b6d3eae95ba6a273.jpg)  
(b)

![](images/bd7b82647e0c7e9a7e7f382bfa3a929b7bb9c48899fd22e9f3a361060a4f7a3c.jpg)  
(c）  
Fig. 7. Comparison between (a) the fission gas release, (b) the fuel swelling and (c) the proportion of intragranular gas of the model with different nucleation factor and the experimental value [30].

To analyze the complex effects of resolution on fission gas release and fuel swelling, the number densities of bubbles of different sizes in the grain with different resolution constants were analyzed in details. The number density of bubbles in different groups under different resolution constants is shown in Fig 9. The bubble group label refers to the group number such that the bubble in that particular group contains 2^ (group label) gas atoms. It can be seen that with the increase of the resolution constant, the number of small-size bubbles increases. This is because a large number of gas atoms in both intragranular and intergranular bubbles return to the grain due to the effect of resolution. These gas atoms provide the driving force for bubble nucleation and growth, so the number of small-size bubbles increases. At the same time, it can also be found that the number density of large-size bubbles also increases, which is due to the weaker effect of resolution on large-size bubbles and the stronger gas atoms absorption capacity of large-size bubbles. However, with the increase of the resolution constant, the effect of resolution is enhanced to the extent that the large-size bubbles can be destroyed, resulting in a rapid decrease in the number of large-size bubbles. So the resulting effect is that the number of small-size bubbles increases, the number of medium-size bubbles decreases, and the number of large-size bubbles increases at first and then decrease with the increase of the resolution constant. The swelling of bubbles is the main source of fuel swelling, and the contribution of large-size bubbles to the fuel swelling is particularly important, so the fuel swelling presents a trend of rising at first and then falling. Resolution has two impacts on fission gas release. One is that the gas atoms in the intergranular bubbles return to the grain due to resolution. This process will reduce the fission gas release. The other is the increase of the number of gas atoms reaching the grain boundary through diffusion due to the increase of intragranular gas atoms. The effect of this process is opposite to the previous one. When the resolution constant is small, although the number of gas atoms in the grain increases, there are still some intragranular bubbles that can absorb these gas atoms, so the first process plays a determining role. But when the resolution constant is large, not only the number of gas atoms in the grain will greatly increase, but the intragranular bubbles will also be destroyed, so the influence of the second process is enhanced. Consequently, the fission gas release shows a trend of decline at first and then rise with the enhancement of resolution.

![](images/932d586cbc6e108537b1fd6a206ab7b20867ea676d69dcc8481dc9b4c957299d.jpg)  
(a)

![](images/a48e4e3eb16d280fc44a0adec0fba9ac89cc43cf2ed8f5af1d97a8e6cc29bab6.jpg)  
(b)

![](images/315c60b9f4a7741d3c34f2d1af14b15421291a1cbdbe66827853c85cd1789164.jpg)  
(c)  
Fig. 8. Comparison between (a) the fission gas release, (b) the fuel swelling and (c) the proportion of intragranular gas of the model with different resolution constants and the experimental value [30].

After considering all the three quantities in Fig. 8, we determined that the b0=1×10−18 cm3 may be the most suitable value for the UN fuels. This value is much smaller than Feng’s, and it is also more reasonable from a physics point of view.

![](images/a224d178cd20adc5e778ef256ea7c4f35857eea81d6597d24afe6040628ac53c.jpg)  
Fig. 9. The number density of bubbles in different groups with different resolution constants. The bubble group label represents bubbles that contain 2group label number of gas atoms.

![](images/85ab07e20bfdd7f973537ebfe907cab272441e66800c152e2e61960233feaefa.jpg)  
Fig. 10. Variation in swelling against burnup for different values of m.

## 3.2.4. “m” in bubble size grouping method

There is an important parameter m in the bubble size grouping method, and it determines the fineness of the model. The grouping method used in our model is consistent with that of GRASS-SST [28]. The choice of m is generally an integer, because the number of gas atoms in the bubble is always an integer. Fig. 10 shows the evolution of retained fission gas resulted fuel swelling against burnup for m=2 to 4. The predicted swelling increases with the increase of m, and the difference of swelling corresponding to different m is reasonably small. As m increases, the computing time is greatly reduced, and the number of bubble groups is also reduced. In principle, the more detailed manner the bubble division is, the more accurate the model will be, and therefore m 2 was chosen in our simulation.

## 3.3. The results by our model

According to the temperature shown in Fig. 1, the results of the fractional fission gas release and fuel swelling versus burnup of the JOYO experimental reactor are shown in Fig. 11 and Fig. 12, respectively. It can be seen that the mechanistic model can accurately predict the fission gas release. Fig. 11 is the fractional fission gas release versus burnup. In the early stage of fuel irradiation, due to the high porosity of the UN fuel, it is assumed that interconnected tunnels already formed on the grain faces to transport fission gas to the grain edge tunnels [7]. Fission gas is released through the surface connected porosity [33], so the fission gas release increases rapidly. At intermediate burnup, the temperature of the fuel continues to drop due to the slow closure of the He gap, and the diffusion of fission gas is highly dependent on temperature. Therefore, as the temperature continues to drop, the number of gas atoms reaching the grain boundary continues to decrease, so the fractional release of fission gas continues to drop. At higher burnup, as the fuel temperature remains relatively constant, the fission gas release gradually stabilizes. Fig. 12 shows the change of fuel swelling with fuel burnup. With the increase of burnup, the number of fission gas in the grain is increasing, the swelling increases continuously, and the difference in slope is mainly due to the influence of temperature changes, as depicted in Fig. 1.

![](images/4755bcbe04fe34071fbd633bb8f633d1955db06bb441dff2663de5cd379e9c6c.jpg)  
Fig. 11. Comparison between the fission gas release of the model and the experimental value [30].

![](images/45599b60f247de13f9957bef9b915c13bef8b30a7d4c6ccb659b037779b19cd4.jpg)  
Fig. 12. Comparison between the fuel swelling of the model and the experimental value [30].

![](images/0d72d2e8a5b6a46eafa70a057478321fb72788621b8c50f2b009c042e86d9927.jpg)  
Fig. 13. Comparison between the radial distribution of Xe of the model and the experimental value [30].

At the same time, for the fuel sample of the JOYO experimental reactor, Tanaka et al. also obtained the statistics on the fission gas retained in the fuel. The comparison between the model calculation and the experimental data is shown in Fig. 13. It can be seen that the result of the model is in reasonable accordance with the trend of the experimental values. Another point of concern is that most of the fission gas produced is retained in the grain, and the ratio of retained gas is 80%. A small part of the gas is released to the external fuel plenum, and this fractional release is close to 5%. The remaining part of the fission gas is trapped in the grain boundary of the fuel in the form of bubbles. It can be seen that the simulation results accurately captured this partition of fission gas. The comparison between the result of the model and the experimental data is shown in Table 4.The distribution of retained gas is shown in Fig. 14 and the bubble number density is shown in Fig. 15.

![](images/253903553ec83fe757afb2cbdb4447271d7280b9e2028b64ec3141aa5d922db5.jpg)  
(a)

Table 4  
Comparison between the calculation values and the experimental data [30].
<table><tr><td>Parameter</td><td>Calculated values</td><td>Experimental data</td></tr><tr><td>Fuel swelling (%)</td><td>7.1869</td><td>6.7</td></tr><tr><td>Fission gas release (%)</td><td>5.2838</td><td>5.2</td></tr><tr><td>Proportion of intragranular gas (%)</td><td>80.5</td><td>80</td></tr></table>

![](images/876c14535db0791fa42065e61f86671090d548ad9d5328bad0fd432441d213c5.jpg)  
Fig. 15. The bubble size distribution of the JOYO’s simulation. The bubble group label represents bubble that contains 2group label number of gas atoms.

In order to further validate the model, some experimental results of the fuel swelling and fission gas release of UN fuel from the open literature were summarized, and calculations were performed using our model to generate results that can be compared to these data. However, due to ambiguities that exist in the experimental conditions, such as the detailed temperature distribution and fuel geometry, exact model parameters cannot be obtained.

![](images/6023347305c23d7302824f82ab9038eda4e4549a82e39bf34b970ac72107ee54.jpg)  
(b)  
Fig. 14. Retained fractions of fission gas in (a) inter- or intra-granular bubbles, in (b) large bubbles or small bubbles.

![](images/16d5fc474c60a8c5601f85c74d6e4c593bb4c2ae093136c53f5409ace543a5dc.jpg)  
(a)

![](images/cf92c809066ff60373a30f0b3de35a48fbf10b1294fc40e98c0e510ef6f99765.jpg)  
Fig. 16. Comparison among the (a) fission gas release and the (b) fuel swelling of the model, the Storms’ relationship and the experimental value [6-7, 30, 33].

Therefore, for the geometric and temperature setting, we used parameters from the JOYO experiment.

The comparison between the fission gas release calculated by the model and the experimentally obtained value is shown in Fig. 16(a). Due to the above mentioned ambiguity issue of the exact experimental conditions, this comparison shall be treated as a vague validation of the model which only provides information on the match of the simulation results to the trend of the experimental data. It can be seen that the distribution of the experimental data is relatively scattered, and the calculation results are in reasonable agreement with the experimental data, and can basically reflect the trend of most experimental points. Fig. 16(b) shows the comparison between the fuel swelling calculated by the model and the experimental data. It is perceivable that the result of our model can well reflect the trend of the experimental data. The reason for the accelerated increase of swelling is due to the generation of large bubbles, and the contribution of large bubbles to fuel swelling is much greater than that of small bubbles [5].

## 3.4. Influence of resolution on the bimodal bubble size distribution

In the determination the resolution constant in Section 3.2.3, an interesting phenomenon that the bubble size shows a bimodal distribution was discovered. The bimodal bubble size distribution dictates that there are two peaks in the bubble size distribution, and it can be widely seen in a variety of nuclear fuels, including U-O [25-26] and U-Si [27] fuels.

Fig. 17 shows the number density of bubbles in different groups when there is no resolution or when the resolution constants are b0=1×10−19 cm3 and b0=5×10−19 cm3, respectively. We can easily find that the result without resolution shows a unimodal bubble size distribution. However, the bubble size distributions show an obvious bimodal shape under the influence of resolution, and the larger the resolution constant, the more obvious the bimodal shape. It is not difficult to get an inference that resolution is the driving factor for the bimodal bubble size distribution.

The essence of resolution is to knock the gas atoms in the bubble back into the matrix [36]. The main effect of resolution on the bubble is to reduce the number and size of the bubbles. For bubbles, the intensity of resolution decreases with the increase of bubble radius. Resolution will cause an increase in the amount of gas atoms in the grain. The increase of these atoms will also provide a driving force for bubble nucleation and bubble growth. The ability of large-size bubbles to absorb gas atoms is greater than that of medium-size bubbles, so there may be a tendency for the number of large-size bubbles to increase due to resolution. In Fig. 18 where a schematic diagram is exhibited, the black solid line represents the reduction ability of the resolution under different bubble sizes for the number of bubbles, and the red-orange solid line represents the ability of different size bubbles to absorb gas atoms. When the black line is higher than the red-orange line, the number of bubbles tends to decrease, and when the red-orange line is higher than the black line, the number of bubbles tends to increase. Compared with medium-size bubbles, large-size bubbles are less affected by resolution and have a stronger ability to absorb gas atoms to grow.

![](images/eeb6f9eefb7909b43bea4ab8c3e6a6eda3297395e7da92953ab946a4aea45c37.jpg)  
Fig. 17. The number density of bubbles in different groups when there is no resolution or the resolution constant is b0=1×10−19 cm3 and b0=5×10−19 cm3, respectively. The bubble group label in the x axis represents bubble that contains 2group label number of gas atoms.

![](images/4c438dfb2e743747914ce958a12942d999865cfc54d6d531636878df8142df1c.jpg)  
Fig. 18. Schematic diagram of resolution on bubbles of different sizes.

Therefore, the number of large-size bubbles will not decrease but increase, which will result in the formation of a peak in the area of large-size bubbles. A large number of gas atoms returning to the grain will also promote nucleation and generate more bubble nuclei. These new nuclei will slowly absorb gas atoms to grow, but due to the shorter growth time, the final size is smaller, so it contributes to the small-size bubbles, and this causes another peak to form in the small-size bubble area. When there is a bigger resolution constant which is indicated by the blue dotted line in Fig. 18, only larger-size bubbles can maintain the increasing trend and this causes the right peak to move to further right. Correspondingly, the stronger resolution will destroy the small bubbles more violently, and the left peak will shift to further left. The result of our model in Fig 17 when the resolution constant b 5 10−19 cm3 verifies this point.

## 4. Conclusions

A mechanistic fission gas behavior model of UN fuels has been established under the framework of kinetic rate theory in this paper. The model can accurately simulate the fission gas release and fuel swelling of UN fuels. Based on the data from the JOYO experimental reactor, the rationality of the currently available Xe diffusion coefficients in UN fuels was analyzed by using the finite element simulation platform COMSOL to provide input parameters for the UN fuels mechanistic fission gas behavior model, and a new diffusion coefficient which can be used for the modeling of UN fuels has been proposed. In addition, the sensitivity analysis of two parameters, the nucleation factor and the resolution constant, has been carried out. The influence of these parameters on fuel swelling and fission gas release was explained, and the suitable values that can be used for UN fuels were determined. At the same time, in view of the phenomenon of bimodal bubble size distribution, the underlying physics mechanisms were analyzed in details, and a reasonable explanation that the resolution is the driving factor was put forward.

## Author statement

I hereby provide the following statement on the role of each author and confirm that all details provided here are truthful.

Zhengyu Qian: Conceptualization, Methodology, Investigation, Writing –Original Draft

Wenbo Liu: Methodology, Investigation

Rui Yu: Investigation

Yujie Tao: Investigation

Di Yun: Conceptualization, Methodology, Writing –Review and Editing

Long Gu: Conceptualization, Writing –Review and Editing, Funding acquisition

## Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Acknowledgments

This work was supported by the State Key Research and Development Program of China, Grant No. 2020YFB1902100. National Natural Science Foundation of China, Grant No. 11675126 and 11705255 is acknowledged. Special fund of Shanghai Economic and Information Technology Commission (approved number: GYQJ-2018-2-02) is also acknowledged.

## Appendix

For gas atoms in the grain face, the form of Eq. (1) is modified to become:

$$
\tag{A1}
$$

Where, FN,f is the nucleation factor in grain face; SNB is the area of fuel boundary/volume of the fuel; Ngf is the number of grain faces per grain; PA is the interlinkage fraction of the grain face channel.

The terms on right hand side of the Eq. (A1) represent, respectively, 1. the loss of gas atoms due to nucleation; 2. the loss of gas atoms caused by capture of gas atoms by bubbles; 3. and 4. the gain of gas atoms due to biased and random diffusion of gas atoms from the grain; 5. the loss of gas atoms due to the long-range migration; 6. the loss of gas atoms due to the biased migration to the grain edge; 7. the loss of gas atoms due to migration of grain face gas through grain face channels to the grain edge; 8. the increase of gas atoms because of the grain boundary sweeping.

For the grain face bubbles in group i, the equation form changes to be:

$$
\tag{A2}
$$

The terms on right hand side of the Eq. (A2) represent, respectively, 1. the gain of grain face bubbles due to the coalescence of small bubbles; 2. the loss of grain face bubbles caused by coalescence between bubbles in group i and bubbles in other group; 3. and 4. the gain of grain face bubbles due to biased and random diffusion of bubbles from the grain; 5. the loss of grain face bubbles due to bubble pull-off from a moving grain boundary; 6. the loss of grain face bubbles due to the long-range migration; 7. the loss of grain face bubbles due to the biased migration to the grain edge; 8. the loss of grain face bubbles due to migration of grain face bubbles through grain face channels to the grain edge; 9. the increase of grain face bubbles because of the grain boundary sweeping; 10. the loss of grain face bubbles because of resolution; 11. the gain of grain face bubbles in group 2 due to nucleation.

Eqs. (A3) and (A4) represent the form of Eq. (1) for gas atoms and bubbles in grain edge.

$$
\tag{A3}
$$

The terms on right hand side of the Eq. (A3) represent, respectively, 1. the loss of gas atoms due to nucleation; 2. the loss of gas atoms caused by capture of gas atoms by bubbles; 3. the gain of gas atoms due to the biased migration of gas atoms from the grain face; 4. the gain of gas atoms due to the migration of grain face gas through grain face channels; 5. the loss of gas atoms due to the release of grain edge gas atoms through interconnected tunnels.

$$
\tag{A4}
$$

The terms on right hand side of the Eq. (A4) represent, respectively, 1. the gain of grain edge bubbles due to the coalescence of small bubbles; 2. the loss of grain edge bubbles caused by coalescence between bubbles in group i and bubbles in other group; 3. the gain of grain edge bubbles due to the biased migration of gas bubbles from the grain face; 4. the gain of gas atoms due to the migration of grain face bubbles through grain face channels; 5. the loss of grain edge bubbles due to bubble pull-off from a moving grain boundary; 6. the loss of grain edge bubbles because of resolution; 7. the loss of grain edge bubbles due to the release of grain edge bubbles through interconnected tunnels; 8. the gain of grain edge bubbles in group 2 due to nucleation.

## References

[1] R.B. Matthews, K.M. Chidester, C.W. Hoth, R.E. Mason, R.L. Petty, Fabrication and testing of uranium nitride fuel for space power reactors, J. Nucl. Mater. 151 (1988) 345.

[2] J.H. Kittel, B. Frost, J.P. Mustelier, K.Q. Bagley, G.C. Crittenden, J. Van Dievoet, History of fast reactor fuel development, J. Nucl. Mater. 204 (1993) 1–13.

[3] K.Y. Spencer, L. Sudderth, R.A. Brito, J.A. Evans, C.S. Hart, A. Hu, A. Jati, K. Stern, S.M. McDeavitt, Sensitivity study for accident tolerant fuels: Property comparisons and behavior simulations in a simplified PWR to enable ATF development and design, Nucl. Eng. Des. 309 (2016) 197–212.

[4] J. Rest, M. Cooper, J. Spino, J.A. Turnbull, P. Van Uffelen, C.T. Walker, Fission gas release from UO2 nuclear fuel: a review, J. Nucl. Mater. 513 (2019) 310–345.

[5] D.R. Olander, Fundamental Aspects Of Nuclear Reactor Fuel Elements: Solutions To Problems, California Univ., Berkeley (USA). Dept. of Nuclear Engineering, 1976.

[6] E.K. Storms, An equation which describes fission gas release from UN reactor fuel, J. Nucl. Mater. 158 (1988) 119–129.

[7] B. Feng, Feasibility of Breeding in Hard Spectrum Boiling Water Reactors with Oxide and Nitride Fuels, ProQuest Dissertations Publishing, 2011.

[8] P. Lösönen, On the effect of irradiation-induced resolution in modelling fission gas release in UO2 LWR fuel, J. Nucl. Mater. 496 (2017) 140–156.

[9] Y. Miao, K.A. Gamble, D. Andersson, Z. Mei, A.M. Yacout, Rate theory scenarios study on fission gas behavior of U Si under LOCA conditions in LWRs, Nucl. Eng. Des. 326 (2018) 371–382.

[10] Y. Miao, K.A. Gamble, D. Andersson, B. Ye, Z. Mei, G. Hofman, A.M. Yacout, Gaseous swelling of U3Si2 during steady-state LWR operation: A rate theory investigation, Nucl. Eng. Des. 322 (2017) 336–344.

[11] J. Rest, Modeling of Fission-Gas Induced Swelling of Nuclear Fuels, 2016.

[12] A.H. Booth, A Method of Calculating Fission Gas Diffusion from Uo \$ Sub 2\$ Fuel and its Application to the X-2-F Loop Test, Atomic Energy of Canada Ltd, Chalk River Project, Chalk River, Ont, 1957.

[13] M.V. Speight, A calculation on the migration of fission gas in material exhibiting precipitation and re-solution of gas atoms under irradiation, Nucl. Sci. Eng. 37 (1969) 180–185.

[14] M.R. Hayns, M.H. Wood, Models of fission gas behaviour in fast reactor fuels under steady state and transient conditions, J. Nucl. Mater. 67 (1977) 155–170.

[15] J. Rest, G.L. Hofman, Y.S. Kim, Analysis of intergranular fission-gas bubble-size distributions in irradiated uranium–molybdenum alloy fuel, J. Nucl. Mater. 385 (2009) 563–571.

[16] J. Rest, Evolution of fission-gas-bubble-size distribution in recrystallized U–10Mo nuclear fuel, J. Nucl. Mater. 407 (2010) 55–58.

[17] J. Rest, An analytical study of gas-bubble nucleation mechanisms in uranium-alloy nuclear fuel at high temperature, J. Nucl. Mater. 402 (2010) 179–185.

[18] D.L. Deforest, Transient Fission Gas Behavior In Uranium Nitride Fuel Under Proposed Space Applications, AIR FORCE INST OF TECH WRIGHT-PATTERSON AFB OH, 1991.

[19] H. Matzke, Diffusion in ceramic oxide systems, Fission Product Behav. Ceram. Oxide Fuel (1986).

[20] M. Backhaus Ricoult, Diffusion Processes and Interphase Boundary Morphology in Ternary Metal-Ceramic Systems, Berichte der Bunsengesellschaft für physikalische Chemie 90 (1986) 684–690.

[21] C.B. Lee, B.H. Lee, C. Nam, D.S. Sohn, GRSIS Program To Predict Fission Gas Release And Swelling Behavior Of Metallic Fast Reactor Fuel, Korea Atomic Energy Research Institute, 1999.

[22] G. Kaganas, J. Rest, A physical Description Of Fission Product Behavior Fuels For Advanced Power Reactors, Argonne National Lab.(ANL), Argonne, ILUnited States, 2007.

[23] C.B. Lee, D.H. Kim, Y.H. Jung, Fission gas release and swelling model of metallic fast reactor fuel, J. Nucl. Mater. 288 (2001) 29–42.

[24] W.G. Steele, A.R. Wazzan, D. Okrent, Steady-state fission gas behavior in uranium plutonium zirconium metal fuel elements, Nucl. Eng. Des. 113 (1989) 289–295.

[25] V.F. Chkuaseli, Fission gas bubble behaviour in uranium dioxide, J. Nucl. Mater. 201 (1993) 92–96.

[26] S. Kashibe, K. Une, K. Nogita, Formation and growth of intragranular fission gas bubbles in UO2 fuels with burnup of 6–83 GWd/t, J. Nucl. Mater. 206 (1993) 22–34.

[27] G.L. Hofman, J. Rest, J.L. Snelgrove, A New Swelling Model And Its Application To Uranium Silicide Research Reactor Fuel, Argonne National Lab., ILUnited States, 1992.

[28] J. Rest, GRASS-SST: a comprehensive, mechanistic model for the prediction of fission-gas behavior in UO2-base fuels during steady-state and transient conditions, Argonne Natl. Lab (1978).

[29] J. Rest, S.A. Zawadzki, FASTGRASS: a mechanistic model for the prediction of Xe, I, Cs, Te, Ba, and Sr release from nuclear fuel under normal and severe-accident conditions, Nuclear Regulatory Commission, Washington, DC (United States), Div. Syst. Res. (1992).

[30] K. Tanaka, K. Maeda, K. Katsuyama, M. Inoue, T. Iwai, Y. Arai, Fission gas release and swelling in uranium–plutonium mixed nitride fuels, J. Nucl. Mater. 327 (2004) 77–87.

[31] C. Multiphysics, C. Module, COMSOL multiphysics user’s guide, Version: COM-SOL Multiphys. 3 (2014).

[32] H. Blank, Basic aspects of swelling in dense livuid metal fast breeder reactor fuels, J. Less Common Metals 121 (1986) 583–603.

[33] A.A. Bauer, J.B. Brown, E.O. Fromm, V.W. Storhok, Mixed-Nitride Fuel Irradiation Performance, Battelle Memorial Inst., Columbus, Ohio, 1971.

[34] J. Rest, G.L. Hofman, An alternative explanation for evidence that xenon depletion, pore formation, and grain subdivision begin at different local burnups, J. Nucl. Mater. 277 (2000) 231–238.

[35] D.R. Olander, D. Wongsawaeng, Re-solution of fission gas–a review: part I. Intragranular bubbles, J. Nucl. Mater. 354 (2006) 94–109.

[36] R.S. Nelson, The stability of gas bubbles in an irradiation environment, J. Nucl. Mater. 31 (1969) 153–161.

[37] S.C. Weaver, Helium gas bubble migration in uranium mononitride in a temperature gradient, Am. J. Clin. Nutr. (1967).

[38] L. Leibowitz, R.A. Blomquist, Thermal conductivity and thermal expansion of stainless steels D9 and HT9, Int. J. Thermophys. 9 (1988) 873–883.

[39] B.D. Rogozkin, N.M. Stepennova, A.A. Proshkin, Mononitride fuel for fast reactors, Atom Energy+ 95 (2003) 624–636.
