# Investigation of swelling behaviors of U-10Zr metallic fuel in the low temperature regime via a cavitational void swelling model

<!-- image-->

Zhengyu Qian a , Xin Xie a , Yingjie Fu a , Di Yun a,b,∗ , Wenbo Liu a , Xiankun Liu c , Qijie Feng c , Haibing Guo c , Yong Sun c , Wei Zhou c , Xinfu He d, Jinli Cao d,e , Wenjie Li f

a School of Nuclear Science and Technology, Xi’an Jiaotong University, Xi’an, China, 710049

b State Key Laboratory of Multiphase Flow, Xi’an Jiaotong University, Xi’an, China, 710049

c Institute of Nuclear Physics and Chemistry, China Academy of Engineering Physics, Mian Yang, China, 621999

d Reactor Engineering Technology Research Division, China Institute of Atomic Energy, Beijing, China, 102413

e School of Materials and Science and Engineering, University of Science and Technology Beijing, Beijing, China, 100083

f Science and Technology on Reactor System Design Technology Laboratory, Nuclear Power Institute of China, Chengdu, China, 610213

## a r t i c l e i n f o

Article history:   
Received 24 December 2021   
Revised 27 February 2022   
Accepted 9 March 2022   
Available online 10 March 2022

Keywords:   
Uranium zirconium fuel   
Thermo-mechanical analysis   
Fuel swelling   
Rate theory   
Cavitational void swelling

## a b s t r a c t

The uranium zirconium (U-Zr) metallic nuclear fuel has long been considered as a promising candidate fuel type for fast breeder reactors. One of the key performance issues of the U-10Zr metallic fuel is its rather strong swelling, which would lead to significant fuel cladding mechanical interaction (FCMI) at relatively high fuel burn-ups. It is therefore imperative to understand the fuel swelling behaviors and the underlying physics mechanisms. Recently published experimental results of U-10Zr fuel swelling behaviors in a low temperature regime (400-600K) showed perceivable swelling of the in-pile irradiated fuel. However, the underlying physics mechanism behind this swelling is not clear. In this work, we performed in-depth analyses on the microstructural features of the irradiated fuel with metallography and conducted a finite-element based simulation on a computational platform, COMSOL, to determine the hydrostatic stress in the irradiated fuel. The spherical objects in the metallography result have been identified as cavities with relatively low fission gas pressure instead of equilibrium gas bubbles. A rate theory code based on the cavitational void swelling model has been developed and the fuel swelling behaviors of U-10Zr fuel in the low temperature regime have been assessed. The simulation results suggest a much lower migration energy for vacancy diffusion in the metallic fuel compared to what is currently used, and a new set of key parameters for the rate theory model were determined.

© 2022 Elsevier B.V. All rights reserved.

## 1. Introduction

U-Zr metallic nuclear fuel has the characteristics of high uranium atom density (and hence a harder neutron spectrum and a high conversion ratio), high thermal conductivity and good compatibility with cladding [1–4]. At the same time, the overall maturity and reliability of technology and economics of metallic fuelbased fuel cycle are desirable [5]. These advantages make U-Zr metal fuel a promising fast reactor fuel. However, there are a number of issues from the fuel performance perspective that set limitations to the wide use of U-Zr metallic fuels. One important issue is the significant fuel swelling of metallic fuels that would post threats to fuel integrity via FCMI [6,7]. For the swelling of U-10Zr fuel at the high temperature regime (normal fast reactor operation temperature range for the fuel slug), there exists a large amount of irradiation data from past EBR-II and FFTF irradiations carried out in U.S [6]. A semi-empirical swelling model was established based on these experimental data [8]. However, the situation at the low temperature regime (400K - 600K) is completely different due to the lack of experimental data. Therefore, the fuel swelling behaviors at the low temperature regime are still largely unknown. In addition, there are other applications, e.g. in a high flux fast spectrum research reactor currently in the design phase in China that requires knowledge of swelling performance at the low temperature regime (400K - 600K), which is still a gap due to the lack of experimental data. Recently, research performed at China Academy of Engineering Physics by the co-authors of this work provided important swelling behavior results for U-10Zr in the low temperature regime [9]. This research showed that there was perceivable volumetric swelling (∼12%) in U-10Zr at the irradiation temperature range of 450K - 560K (450K being the fuel slug outer radius temperature and 560K being the centerline temperature). In addition, the metallographic examination of the cross-section of fuel materials used in the experiment pointed to the fact that there existed a large number of very small spherical structures whose nature remains to be determined.

Since U-Zr metallic fuel was proposed as a fast reactor fuel form, a considerable amount of research has been conducted to establish models to describe the fuel swelling behaviors, among which many were mechanistic models. Previous studies on mechanistic models for fission gas behaviors and swelling of U-Zr metallic fuel can be divided into two major categories. In one category, researchers [10,11] attributed the fission gas release and swelling of metallic fuel to the interconnection of gas bubbles on the grain boundaries and the expansion of volume occupied by the gas bubbles, respectively. In the other category, researchers [12] thought that the cavitational void swelling may be the main source of swelling for U-Zr metallic fuels. The fission gas bubble swelling mechanism was derived from the widely accepted bubble growth kinetics in ceramic fuels based on large amount of experimental investigations on microstructural features of irradiated ceramic fuels [10,11]. The cavitational void swelling mechanism was proposed mainly based on some peculiar structural features of U-Zr metallic fuels. Metallography and scanning electron microscope (SEM) examinations revealed that the structures in irradiated U-Zr metallic fuel, particularly in the α-U phase zone, were the swirl worked tear-like porosities [12,13]. Depending on the findings on the microstructural level, Rest developed a model that accounted for the swelling of the α-U phase zone in U-Zr fuels by irradiation induced fission gas bubble nucleated cavitational void swelling mechanism [12]. The cavitational void swelling mechanism is mainly derived from Mansur’s work [14]. Mansur proposed the concept of critical cavity radius and pointed out that the cavity will grow by absorbing vacancies when the radius of the cavity is greater than the critical radius. After years of continuous development, the cavity swelling model has been applied to in fields. Emelyanova [15] used the void swelling model to explore the irradiation swelling of ODS-EUROFER steel. Griffiths [16] applied it to the study of irradiation swelling of austenitic stainless steel. These studies usually apply the void swelling model to structural metals and alloys, and Rest was the first to employ this model in metallic nuclear fuels and achieved good results. In this cavitational void swelling model, swelling kinetics transform from bubble swelling to void swelling when the sizes of gas bubbles penetrate the threshold for further cavitational void growth. As a result, stable cavities are formed and they grow larger in size by receiving net vacancy influx. In the past decades, both bubble swelling and cavitational void swelling mechanisms have been adopted to predict fuel swelling of U-Zr metallic fuels at the high temperature regime (800K -1000K), and they were both quite successful despite their rather apparent differences from a modeling perspective. Therefore, it becomes imperative to determine which mechanism is the true operating mechanism for the fuel swelling of metallic U-Zr fuels.

In traditional cognition, the swelling of U-10Zr fuel at low temperature is almost negligible according to Rest [12]. This new discovery [9] is quite on the contrary to the previous prediction by Rest. Both bubble growth kinetics and cavitational void swelling mechanism are strongly dependent on temperature. The recent research [9] showed that the swelling reached 12% at 0.5at% burnup, and the swelling increased rapidly with burnup. In the previous data about the EBR-II fuels [6], the swelling of fuel at the high temperature regime is close to 10% at 0.4at% burnup, but the temperature difference between the two temperature regimes is about 300K. Whether if the key swelling mechanism was bubble growth or cavitational void swelling, such a large temperature difference will pose a great impact on swelling, but the gap between experimental data between the two temperature regimes is actually quite small. Therefore, it is necessary to explore the swelling mechanism of U-Zr metallic fuels at the low temperature regime, particularly to shed lights on the future application of U-Zr metallic fuels at low temperatures. The emergence of experimental fuel swelling data and microstructural insights from the recent work in the low temperature regime [9] therefore opens a new opportunity to carefully examine the fuel swelling mechanisms for U-Zr metallic fuels.

Mechanistic kinetic rate theory models often suffer from a common shortage of large uncertainties due to the use of a number of parameters at the same time [17–19]. A central issue for the application of such mechanistic models to a fission gas behaviors problem, which is inherently complex in nature, is therefore the determination of a small set of key parameters that significantly influence the computational results. Specifically, in the case of U-Zr metallic fuels modeling, the greatest uncertainty may lie in the migration energy of vacancy diffusion. When Rest established the cavitational void swelling model, there was neither relevant experimental data nor today’s advanced multi-scale simulation technology to help assess the vacancy migration energy of α-U, so there inevitably existed great uncertainty in this migration energy. The large vacancy diffusion migration energy used in Rest’s model led to a huge difference of 6 orders of magnitude [12] in the diffusion coefficients between the high temperature and the low temperature regimes. And this has resulted in a significant difference in fuel swelling between the high temperature and the low temperature regimes.

In this work, we utilized finite element analysis to calculate the hydrostatic stress in the metallic fuel samples irradiated in a prior work and determined that the spherical objects found in the metallographic examination of irradiated samples of U-Zr metallic fuel at the low temperature regime were spherical cavities with low gas pressure instead of equilibrium gas bubbles. Building upon these findings, a rate theory model based on cavitational void swelling mechanism was established, which can well simulate the swelling of U-Zr fuels at different temperature regimes. Combined with the density functional theory (DFT) and molecular dynamics (MD) calculation [20,21], we used a more reasonable vacancy migration energy and the change in such energy has resulted in a much better agreement between calculation results and experimental data at the low temperature regime while slightly improving the agreement with experimental data on swelling at the high temperature regime. Sections 2 and 3 provide the detailed processes of determining the nature of the spherical objects in the metallographic results, and Section 4 gives a description of the model and demonstrates the comparison between experimental data and the calculation results of fuel swelling at different temperature regimes.

## 2. The low temperature irradiation of U-10Zr fuels

The irradiation experiment was performed in a research reactor operated by the Institute of Nuclear Physics and Chemistry in China. The full details of the irradiation experiment, which was performed by co-authors of this work, can be found elsewhere [9] and are not repeated here. However, in order to maintain the integrity of this paper and for the ease of comprehension of the modeling work presented herein, some important details of the irradiation experiment that are relevant to the modeling side of the work are re-introduced.

U-10Zr fuel slugs were irradiated in a pool-type research reactor (China Mianyang Research Reactor, CMRR). The maximum burnup of the tested fuels is about 0.7 at.%, including contributions from both U-235 and U-238. The U-235 enrichment was increased in order for the tested fuels to reach the intended burn-up in a shorter period of time. The geometries of the irradiated fuel slugs were the same, 5mm×15mm cylinders. The outer Zr-4 shell of the test capsules were also cylinders of 10mm 35mm cylinders with 1 mm wall thickness. Two types of irradiation samples and capsules were designed to investigate the free swelling (swelling with no mechanical constraint) behavior and fuel-cladding interaction, respectively. In this work, we focus on the set of tested fuel slugs with their capsules designed to evaluate the free swelling behaviors. Pure aluminum powder loosely filled to 68% of the theoretical density with almost homogeneous porosity was chosen to fill the gap between the inner slug and the outer capsule shell. This both allowed space to accommodate the fuel swelling and provided good thermal conduction in the gap. The temperature distribution was calculated via a finite-element based computer program and this calculated temperature profiled was used as the input to the rate theory program developed in this work. The detailed temperature distribution in the fuel is shown in section 3.

<!-- image-->  
Fig. 1. Metallography image of as-irradiated U-10Zr fuel at the low temperature regime (at a burn-up level of 0.55 at.%, selected small spherical cavities are marked by red arrows).

Fuel dimension changes were measured with both cold neutron radiography and metallography after an extensive cooling period after the irradiated fuel slugs were taken out of the reactor. Both radial and axial dimension changes were measured with cold neutron radiography at four different burn-ups. Two tested fuel slugs received different burn-up levels due to their different location inside the reactor test channel. The lower burn-up fuel slug reached a final burn-up of 0.55 at.% while the higher burn-up fuel slug reached a final burn-up of 0.7 at.%. All these data were then processed to estimate the fuel swelling behaviors which were then used as validation data to the rate theory model presented in this work. Both fuel specimens reached a volumetric swelling level of ∼12%.

Metallography results were obtained on the mid-cross-section (axially) of the U-10Zr sample irradiated to 0.55 at.% burn-up. Fig. 1 shows the metallography micro-image. There exists a large amount of very small spherical structures (selectively marked by red arrows in Fig. 1) whose nature is either fission gas bubble or cavity (where the internal fission gas pressure is relatively low). In Section 1, we mentioned that the swelling mechanism for gas bubble and cavity is different. For the gas bubble growth kinetics, the source of fuel swelling is gas atoms absorbed by bubbles, but for the cavitational void swelling mechanism, the source is voids absorbed by cavities. It is therefore necessary to discriminate whether these structures are bubbles or cavities. The average size of these structures has been measured to be about 3 μm in diameter (with 1328 cavities measured, mean diameter, 2.98μm, and standard deviation, 0.988μm) and the number density was estimated to be about $8 \times 1 0 ^ { 9 }$ o $\mathsf { b j e c t s } / \mathsf { c m } ^ { 3 }$ . It is difficult to identify the exact nature of these spherical objects. However, the internal gas pressure may be quickly estimated. At 0.55 at.% burn-up, fission gas generated can be reliably estimated, by the fission yield of 0.25, to be 0.1375 at.% which corresponds to fission gas level of $4 . 9 \times 1 0 ^ { 1 9 }$ fission gas atoms/cm3. If one assumes that all the fission gas atoms are retained in the cavities, then the fission gas density inside the cavities is $6 . 1 3 \times 1 0 ^ { 9 }$ fission gas atoms/spherical object. At this size range of cavities, one can safely assume an ideal gas law for the gaseous equation of state. Through applying the ideal gas law, the inner pressure of the average cavity is estimated to be about 3 MPa. As the equilibrium bubbles need to achieve a force balance between the inner pressure and the surface tension plus the hydrostatic stress, the hydrostatic stress is estimated to be about a compressive 2.3 MPa (given that the surface energy of U-10Zr fuel is 0.5 $\mathrm { J } / \mathrm { m } ^ { 2 }$ [12]). Now, if one relaxes the assumption that all fission gas atoms join the cavities and realize that only a fraction of them join the cavities, the resulting estimated internal pressure will have to be even lower than 2.3MPa. It then becomes necessary to have a realistic estimate of the hydrostatic stress in the irradiated fuel in order to verify the nature of the spherical objects.

## 3. Thermo-mechanical analysis after irradiation

## 3.1. Finite-element model via COMSOL multiphysics

A thermo-mechanical model for the irradiated U-10Zr fuel has been established based on the finite-element computational platform of COMSOL Multiphysics (version 5.5) [22]. The geometry of the model is consistent with the geometry of the irradiation device where the U-10Zr fuel slug is surrounded by loose aluminum powder and a Zr-4 cladding [9]. A 2-dimensional axi-symmetric model was applied to simulate the thermos-mechanical behaviors of the fuel slug. The heat transfer boundary conditions were set to match those from the Fluent calculation in the reference literature [9]. Table 1 summarizes the thermo-physical properties used in this simulation. where P is the porosity in the fuel slug, and T is the temperature in K. Properties of Al-6061 powder were taken from the in-software library of COMSOL multiphysics but the thermal conductivity and elastic modulus were corrected with the porosity effects [29,30]. The plasticity model, thermal creep and irradiation creep correlations have been taken from past literatures [31]. A parabolic fit to the volumetric swelling data measured from the experiment has been used as the swelling correlation (as a function of fuel burn-up) fed to the thermo-mechanical simulation. It needs to be pointed out that the purpose of the thermo-mechanical modeling performed here is to provide a reasonable estimate on the hydrostatic stress. Hence, the measured relationship between fuel swelling strains and fuel burn-ups were used as an input known correlation. The detailed temperature profile in the radial direction calculated via COMSOL is shown in Fig. 2 and it agrees well with that obtained by FLUENT in the reference literature [9].

## 3.2. Distribution of hydrostatic stress in the radial direction

One main difference between the heat transfer analysis in this work and that in the earlier work is the inclusion of porosity effect in the fuel slug. This has resulted in an increase in temperature over time when porosity developed in the fuel slug. The maximum temperature in the fuel slug (specimen P2-A4 in ref [9]) at 0.55 at.% is 283°C, which is about 24°C higher than the maximum temperature obtained by the equilibrium solution in reference [9]. Fig. 3 demonstrates the distribution of hydrostatic stress along the radial direction in the mid-cross-section plane (middle height plane) of the fuel slug. It can be seen that due to the low temperature of the fuel and hence the ineffectiveness of creep to relieve the stress, the hydrostatic stress has been estimated to about 60-130 MPa (compressive). Thus, there exists more than an order of magnitude difference between the simulation-provided hydrostatic stress and that estimated in the fuel by analysis of the gas atom number density per cavity (2.3 MPa). This throws the equilibrium bubble scenario into major question. Moreover, it needs to be pointed out that when fuel temperature is relatively low, a large fraction of fission gas would be residing in the fuel matrix due to effective gas bubble resolution together with the low fission gas diffusivity [32]. This would lead to a further decrease of already extremely low hydrostatic stress estimated from the gas atom number density per cavity. As such, we conclude that the possibility of the cavities being equilibrium gas bubbles is dim.

Table 1  
Thermo-physical properties of U-10Zr fuel and Zr-4 cladding used in the thermos-mechanical simulation.
<table><tr><td>Property</td><td>Value</td><td>Units</td><td>Source</td></tr><tr><td>Fuel (U-10Zr)</td><td></td><td></td><td></td></tr><tr><td>k</td><td> $( 1 \mathrm { - P } ) ^ { 1 . 5 } \mathrm { k } _ { 0 }$ </td><td>W/m/K</td><td>[23]</td></tr><tr><td></td><td> $\stackrel { \cdot } { \mathrm { k } } _ { 0 } = \stackrel { \cdot } { 1 } 1 . 7 \stackrel { \cdot } { + } 1 . 3 3 \times 1 0 ^ { - 2 } \mathrm { T } + 9 . 3 8 \times 1 0 ^ { - 6 } \mathrm { T } ^ { 2 }$ </td><td></td><td></td></tr><tr><td> $C _ { \mathrm { p } }$ </td><td> $2 6 . 5 8 + 0 . 0 2 7 ( \mathrm { T } \mathrm { - } 2 7 3 . 1 5 ) / 2 0 6 . 3$ </td><td>J/kg/K</td><td>[24]</td></tr><tr><td> $\mathtt { E }$ </td><td> $5 6 \substack { - 0 . 1 1 5 8 ( \mathrm { T } \mathrm { - } 8 9 0 ) }$ </td><td>GPa</td><td>[25]</td></tr><tr><td> $\alpha _ { \mathrm { T } }$ </td><td> $1 . 7 6 \times 1 0 ^ { - 5 }$ </td><td> $1 / \mathrm { K }$ </td><td>[26]</td></tr><tr><td> $\nu$ </td><td>0.33</td><td></td><td>[25]</td></tr><tr><td>Cladding (Zr-4)</td><td></td><td></td><td></td></tr><tr><td>k</td><td> $7 . 5 1 + 2 . 0 9 \times 1 0 ^ { - 2 } \mathrm { T } - 1 . 4 5 \times 1 0 ^ { - 5 } \mathrm { T } ^ { 2 } + 7 . 6 7 \times 1 0 ^ { - 9 } \mathrm { T } ^ { 3 }$ </td><td> $\mathsf { W } / \mathrm { m } / \mathrm { K }$ </td><td>[27]</td></tr><tr><td> $C _ { \mathfrak { p } }$ </td><td>286.5+0.1T</td><td> $\mathrm { J } / \mathrm { k g } / \mathrm { K }$ </td><td>[27]</td></tr><tr><td> $\dot { \mathrm { ~ E ~ } }$ </td><td> $[ 9 . 9 ~ \times ~ 1 0 ^ { 5 } ~ - ~ 5 6 6 . 9 ~ \times ~ ( \mathrm { T } ~ - ~ 2 7 3 . 1 5 ) ] \times ~ 9 . 8 0 6 7 ~ \times ~ 1 0 ^ { 4 }$ </td><td>Pa</td><td>[28]</td></tr></table>

<!-- image-->  
Fig. 2. Distribution of temperature in the radial direction calculated via COMSOL.

<!-- image-->  
Fig. 3. Distribution of hydrostatic stress in the radial direction on the mid cross section plane of the fuel slug calculated via COMSOL (metallography region is marked by the yellow window).

## 4. The rate theory model

Through the analysis in Section 3, we determined that the small spherical structures in the fuel are more likely to be cavities. It means that the swelling of U-10Zr fuel mainly comes from the cavities and the cavitational void swelling model developed by J. Rest [12] can be used to capture the swelling behaviors at the low temperature regime. A rate theory code that is based on the model established by J. Rest [12] has been developed in this work to simulate the cavitational void swelling in U-10Zr fuel at both the low temperature regime and the high temperature regime. The detailed scheme of the rate theory model has been well described in the work by J. Rest and will not be repeated here [12]. It is worth noting that the cavitational void swelling in the α-U begins with nucleation of gas bubbles and when the gas bubble penetrates the threshold for further cavitational void growth, stable cavity is formed and grows larger in size by receiving net vacancy influx. In the γ -U phase, however, the initial bubble nuclei keep absorbing fission gas atoms due to comparatively high fission gas diffusivity because of the higher temperature. Therefore, it is the net influx of vacancies or fission gas atoms that set the swelling behaviors different.

## 4.1. The swelling behavior of U-10Zr fuel at the low temperature regime (400 – 600K)

The research of China Academy of Engineering Physics provided important swelling data in the low temperature regime to validate the cavitational void swelling model. At the same time, the experimental data also pointed out that the early model [12] significantly underestimated the fuel swelling at low temperatures. This is mainly because of the extremely low vacancy diffusion coefficient used in the model at the low temperature. For the cavitational void swelling, the growth of cavities, which is derived by accumulating vacancies, determines the fuel swelling. Such a low diffusion coefficient leads to almost zero cavity growth, which resulted in seriously underestimated fuel swelling at low temperatures. As such, the fact that the swelling at the low temperature regime is not much lower compared to that at the high temperature regime suggests a flatter curve for the vacancy diffusion coefficient across the low and high temperature regimes, and a smaller value for the activation energy of vacancy diffusion becomes necessary.

Based on the above analysis, we adjusted the parameters used in the Rest’s work [12]. The key parameters used in our model to interpret U-10Zr fuel swelling behaviors at the low temperature regime are summarized in Table 2. Here, the formation energy and diffusion activation energy of vacancy are set to 1.77 and 0.34 eV, respectively. The values were obtained with 5 2 3 supercells utilizing the Vienna Ab initio Simulation Package (VASP) based on the density functional theory (DFT) [33–35], and they are also consistent with previous literature results via DFT calculations [20]. An activation energy of 0.19 eV is used for interstitial migration. This value is adopted from the earlier DFT work as well [20]. The preexponential factors for both vacancy and interstitial diffusion coefficients in the fuel were obtained in this work. The rationale for the derivation of these values is that, if the model calculated swelling behaviors compare well with experimental data at both the low and the high temperature regimes, then these key parameters are believed to be reasonable, given the additional pre-requisite that they do not fall out of their normal expected range. The temperature distribution and the geometric information were obtained by the finite-element analysis performed in Section 3.

Table 2  
Key Parameters for the Low Temperature Fuel Swelling Calculation.
<table><tr><td>Parameter</td><td>Value</td><td>Reference</td></tr><tr><td>Fuel axial length (mm)</td><td>15.0</td><td>[9]</td></tr><tr><td>Fuel radius (mm)</td><td>2.5</td><td>[9]</td></tr><tr><td>Pre-exponential factor for vacancy diffusion  $( \mathsf { c m } ^ { 2 } { \bullet } \mathsf { s } ^ { - 1 } )$ </td><td> $1 . 0 \times 1 0 ^ { - 7 }$ </td><td>This work</td></tr><tr><td>Migration energy for vacancy diffusion (eV)</td><td>0.34</td><td>[20]</td></tr><tr><td>Formation energy for vacancy (eV)</td><td> $1 . 7 7$ </td><td>This work</td></tr><tr><td>Pre-exponential factor for interstitial diffusion  $( \mathsf { c m } ^ { 2 } { \bullet } \mathsf { s } ^ { - 1 } )$ </td><td> $1 \times 1 0 ^ { - 4 }$ </td><td>This work</td></tr><tr><td>Migration energy for interstitial diffusion (eV)</td><td>0.19</td><td>[20]</td></tr><tr><td>Pre-exponential factor for fission gas atom diffusion coefficient (cm2/s)</td><td> $1 . 2 \times 1 0 ^ { - 3 }$ </td><td>[39]</td></tr><tr><td>Migration energy for fission gas atom diffusion (eV)</td><td> $1 . 1 6$ </td><td>[39]</td></tr><tr><td>Dislocation density  $( \mathsf { c m } ^ { - 2 } )$ </td><td> $7 \times 1 0 ^ { 9 }$ </td><td>[12]</td></tr><tr><td>Bubble nucleation factor in the bulk</td><td> $1 \times 1 0 ^ { - 5 }$ </td><td>[12]</td></tr><tr><td>Bubble nucleation factor on the phase boundaries</td><td> $1 \times 1 0 ^ { - 5 }$ </td><td>[12]</td></tr><tr><td>Grain size (cm)</td><td> $1 \times 1 0 ^ { - 3 }$ </td><td>This work, roughly estimated via TEM</td></tr></table>

<!-- image-->  
(a)

<!-- image-->  
(b)  
Fig. 4. Comparison between fuel swelling by simulation and by experimental measurements (a) specimen #10, (b) specimen #11 from reference [9].

Fig. 4(a) and (b) compare the calculated fuel volumetric swellings by the mechanistic model and the measured data from the reactor irradiation experiments (specimen #10 and #11 in reference [9]). It is reasonable to believe that there is no fission gas release in this irradiation experiment due to the low temperature of the irradiated fuel and the relatively low final burn-up that the fuel had reached. This is also consistent with the prediction results by our model. It can be observed that the trends of the swelling curves are well in accordance with the experimental data. At the same time, the calculated average cavity size is about 1.94 μm, reasonably close to that obtained from metallography result (3 μm). To verify the rationality of the vacancy migration energy selected in this work, a parameter sensitivity analysis were conducted. Fig. 5 shows the simulation results of the model with different vacancy migration energies. It is not hard to find that the vacancy migration energy selected in this work can well capture the swelling of U-10Zr fuel at the low temperature regime. In addition, the rather strong deviations of simulation results from the experimental data, when other values of vacancy migration energies were adopted, reflected the high sensitivity of calculated swelling to this peculiar parameter. It, in fact, further provides support to the value of such parameter adopted in this work. It needs to be pointed out that this, alone, cannot be a testimony to the validity of the model and the corresponding parameters used herein. Besides the low temperature regime, the trends of both the fission gas release and the swelling curves in the high temperature regime, which is the operation temperature regime for EBR-II tested fuels, have to be consistent with experimental observations as well. This will be demonstrated in the following section.

<!-- image-->  
Fig. 5. Comparison between fuel swelling by simulation and experimental measurements under different vacancy migration energies (εF represents the vacancy migration energy used in the present study).

Table 3  
Key Parameters for the High Temperature Fuel Fission Gas Release and Swelling Calculation.
<table><tr><td>Parameter</td><td>Value</td><td>Reference</td></tr><tr><td>Fuel axial length (mm)</td><td>343.0</td><td>[6]</td></tr><tr><td>Fuel radius (mm)</td><td>2.83</td><td>[6]</td></tr><tr><td>Peak cladding temperature ()</td><td>522</td><td>[6]</td></tr><tr><td>Bubble nucleation factor in the bulk</td><td> $1 \times 1 0 ^ { - 5 }$ </td><td>[12]</td></tr><tr><td>Peak linear power rate (W/cm)</td><td>427</td><td>[6]</td></tr><tr><td>Grain size   zone (cm)</td><td> $5 \times 1 0 ^ { - 3 }$ </td><td>[12]</td></tr><tr><td>Irradiation enhanced bubble</td><td> $1 \times 1 0 ^ { - 2 9 }$ </td><td>[12]</td></tr><tr><td>diffusivity (cm²/s) Gas bubble re-solution constant (cm3)</td><td> $1 \times 1 0 ^ { - 1 8 }$ </td><td>[12]</td></tr></table>

<!-- image-->  
Fig. 6. Simulated fuel swelling and fission gas release at the high temperature regime.

## 4.2. The swelling behavior of U-10Zr fuel at the high temperature regime (800 – 1000K)

Different from with the situation of the low temperature regime, there are more data that can be used to validate at the high temperature regime, but the multiphase characteristics of U-10Zr fuel will greatly increase the difficulty of modeling. At such temperature range, there will exist two difference phase regions (α fuel zone and the γ fuel zone) and this makes it necessary to consider the fission gas behaviors in different phase regions separately. According to the temperature distribution calculated via the COM-SOL Multiphysics Finite Element platform, the fuel was divided into two regions and the phase boundary temperature was chosen to be 903K. In the $\gamma$ phase zone, the gas bubble growth kinetics was used to model the fission gas release and fuel swelling, while the bubble nucleated cavitational void swelling kinetics was adopted in the α phase zone. The fuel irradiation experiment parameters and the key parameters used for the mechanistic model for the γ phase zone are tabulated in Table 3. Parameters for the U-10Zr fuel were taken from the published data for the EBR-II irradiation experiment X423 [6].

Fig. 6 gives the fuel swelling and fission gas release predicted by our mechanistic model. The results of the model are obtained after comprehensively considering the fission gas behaviors in different phase regions. For the γ phase zone, there is nearly no fission gas release until relatively high burn-up, while for the α phase zone, fission gas release experiences an incubation period of about 0.65 at.% burn-up and then shows a sharp increase at the burnup range between 0.65 at.% and 0.75 at.%. Since the α phase zone occupies about 72.2% of the total fuel volume, its fission gas release behavior becomes dominant. The fission gas release demonstrates an asymptotic behavior towards the release level of about 70%. Different from fission gas release, the trend of unrestrained fuel swelling with burnup is relatively simple. At 0.65 at.% burnup, the total fuel swelling reached 25%, and this corresponds to the burn-up region where fission gas release starts to show a sharp increase. This is consistent with the common observations that fission gas starts to release in high fraction when U-10Zr fuel swells to an extent beyond 30% volumetric strain. These points show that the results of the model are basically in accordance with the current understanding of the U-10Zr fuel behaviors [6]. Fig. 7 compares the fission gas release predicted by the model and the experimental data [6]. It is perceivable that the simulated fission gas release matches the experimental data reasonably well. Fig. 8 shows the axial distribution of fuel swelling under different burnup. It can be seen that the results of our model can effectively envelope experimental data points at the burn-up of 0.4 at.%, and also shows a good agreement with data points at 0.9 at.% burn-up in both values and trends. Generally speaking, the modified model can effectively capture the behaviors of swelling and fission gas release of U-10Zr fuel at the high temperature range.

<!-- image-->  
Fig. 7. Comparison between simulated fission gas release and experimental data for U-10Zr [36].

## 4.3. The diffusion coefficients and their effects on swelling

In Sections 4.1 and 4.2, we demonstrated the swelling behavior of U-10Zr fuel at both the low and the high temperature regimes obtained by the modified model and the results of the model are basically in accordance with the experimental data. Compared with the Rest’s model, we mainly change the vacancy and interstitial diffusion coefficients, so it is necessary to compare these two parameters between this work and prior works and Fig. 9 shows such comparison. The parameters we used can well reflect the swelling of U-Zr metal fuel at both the high and the low temperature regimes at the same time, while Rest’s model could not predict the swelling behaviors in the low temperature regime. From the Fig. 9, we can intuitively see that at the high temperature range the diffusion coefficients used in our model exhibited no differences with those used by Rest, but at the low temperature range, the difference between the diffusion coefficients becomes significant. This is mainly due to the fact that the migration energy used in our work is much smaller and hence the diffusion coefficient curve of vacancy becomes much flatter. Therefore, the diffusion coefficient is about 3 to 4 orders of magnitude higher than that used by Rest at the low temperature region (500 – 600k). This difference becomes the key factor in boosting the cavity growth kinetics and hence the cavitational fuel swelling in the low temperature regime.

<!-- image-->  
(a)

<!-- image-->  
(b)

Fig. 8. Comparison between axial distribution of fuel swelling by simulation and by experimental measurements (a) 0.4 at.%, (b) 0.9 at.% fuel burn-ups [12].  
<!-- image-->  
Fig. 9. Comparison between diffusion coefficients of vacancy and interstitial obtained in this work and those from a prior work by J. Rest [12].

<!-- image-->  
Fig. 10. Calculated U-10Zr fuel cavitational void swelling with respect to temperature (the curve beyond 903K is hypothetical due to the phase change to γ -U and the resulting different swelling mechanism).

Void swelling versus temperature curve usually takes a bell shape and the swelling reaches a maximum at certain temperature before it decreases due to higher annihilation rate of defects at high temperatures. Fig. 10 illustrates the trend of U-10Zr fuel swelling with respect to temperature, and at the same time the comparison between swelling calculated by our work and that by Rest’s is also included. The swelling reaches a peak value and then sharply declines with increasing temperature, which is consistent with prior works [18,19]. Due to the flatter distribution of vacancy diffusion coefficient used in our model, fuel swelling remains at a higher and detectable value at the temperature of 400K as compared to Rest’s work. This figure also marks the key difference between the simulated U-10Zr swelling in this work and that in the prior work by Rest in the temperature range of 400K - 800K. It should to be noted that there is still uncertainty in the temperature range between 600K and 800K due to lack of experimental data, and further research of an in-reactor irradiation of U-10Zr fuel at the temperature range would be needed to further validate the results obtained in this work.

## 4.4. The swelling behavior of U-10Zr fuel in the low temperature regime with the gas bubble driven swelling model

The previous sections showed that the cavitational-void swelling model can predict the swelling of U-10Zr fuel in different temperature ranges under the premise of modified vacancy and interstitial diffusion coefficients. But many prior works adopted the fission gas bubble growth mechanism (which has been widely used for oxide fuels [37,38]) as the main contributing mechanism for the fuel swelling of U-Zr/U-Pu-Zr type metallic fuels [10,11]. It becomes necessary at this point to use the bubble growth kinetics to model U-10Zr fuel swelling at the low temperature regime. Consequently, we made an attempt to capture the fuel swelling behaviors at the low temperature regime with the gas bubble growth model. The key parameters are the same with those from Table 2 and 3. However, the resulting fuel swelling at 0.55 at.% burn-up of the fuel, which is 1.2% including solid fission product induced swelling, is very small. This is mainly because of the rather small diffusion coefficient for fission gas atoms in the low temperature regime. Of course, we can adjust the diffusion coefficient of gas atoms similar to what we did in the cavitationalvoid swelling model, but only when the pre-exponential factor of fission gas diffusion coefficient is artificially raised by as much as six orders of magnitude, which is unreasonably high, can 10% fuel swelling be obtained. By changing other key parameters such as the bubble re-solution factor or the bubble nucleation factor while holding the fission gas diffusion coefficient, the resulting fuel swelling did not exceed 1.5%, including solid fission product induced swelling. Therefore, we believe that it is difficult to obtain the swelling behaviors of U-10Zr fuel in the low temperature regime using the gas bubble growth model if the key parameters were to be set to be within a reasonable range physics wise. From the above we conclude that bubble growth kinetics is not suitable for the simulation of fuel swelling of U-10Zr fuel at the low temperature regime, because even if some unreasonably set parameters were used (which is not allowed in rate theory simulations in general), we cannot use bubble growth kinetics to obtain fuel swelling close to that observed in the experiments. However, we can use reasonable parameters to describe the fuel swelling at the low temperature regime through cavitational void swelling model, which also shows that cavity swelling is the main swelling mechanism at this low temperature regime.

## 5. Conclusions

In this work, an in-depth analysis of the swelling data and metallography results of U-10Zr metal fuels irradiated in the low temperature regime (400 – 600K) was carried out, and the main conclusions are as follows:

1) From the metallography results, spherical cavities with an average size of 3 μm (in diameter) were observed. The number density of the cavities was about $8 \times 1 0 ^ { 9 }$ cavities/cm3.

2) The distribution of the hydrostatic stress in the metallic fuel was obtained by a finite-element based thermo-mechanical analysis. Combined with the experimental data, the results suggest that the spherical objects observed via metallography were cavities with low gas pressure instead of equilibrium gas bubbles.

3) Employing a kinetic rate theory method, U-10Zr metallic fuel swelling behaviors in both the low temperature regime and the high temperature regime (α-U zone in the EBR-II fuel temperature regime) were modeled. It was shown that using a much lower migration energy for vacancy diffusion (0.34 eV, according to our DFT calculation, and consistent with results from previous literature) compared to an earlier work could well describe the fuel swelling behaviors at both temperature regimes when a cavitational void swelling model is applied for the α-U zone.

4) The EBR-II fuel swelling and fission gas release behaviors were well captured when a gas bubble growth model was applied for the γ -U phase of EBR-II irradiated U-10Zr fuels. Several important parameters for the rate theory model have been determined based on comparisons between the simulation results and experimental data.

## Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## CRediT authorship contribution statement

Zhengyu Qian: Conceptualization, Methodology, Investigation, Writing – original draft. Xin Xie: Methodology, Investigation. Yingjie Fu: Conceptualization, Methodology, Investigation. Di Yun: Conceptualization, Methodology, Writing – review & editing, Supervision, Funding acquisition. Wenbo Liu: Methodology, Investigation, Funding acquisition. Xiankun Liu: Investigation. Qijie Feng: Investigation. Haibing Guo: Investigation. Yong Sun: Investigation. Wei Zhou: Investigation, Funding acquisition. Xinfu He: Conceptualization, Methodology. Jinli Cao: Investigation. Wenjie Li: Writing – review & editing, Supervision, Funding acquisition.

## Acknowledgements

This research was also supported by the National Natural Science Foundation of China (Grant No. 11675126, Grant No. 11705255 and Grant No. 11405153). Financial support provided by the NSAF Joint Fund (No. U2130105) and the CNNC Innovation Project at Xi’an Jiaotong University are also acknowledged.

## References

[1] L.C. Walters, B.R. Seidel, J.H. Kittel, Nucl. Technol. 65 (1984) 179.

[2] R.G. Pahl, D.L. Porter, D.C. Crawford, L.C. Walters, J. Nucl. Mater. 188 (1992) 3.

[3] G.L. Hofman, L.C. Walters, T.H. Bauer, Prog. Nucl. Energy 31 (1997) 83.

[4] D.C. Crawford, D.L. Porter, S.L. Hayes, J. Nucl. Mater. 371 (2007) 202.

[5] W.J. Carmack, D.L. Porter, Y.I. Chang, S.L. Hayes, M.K. Meyer, D.E. Burkes, C.B. Lee, T. Mizuno, F. Delage, J. Somers, J. Nucl. Mater. 392 (2009) 139.

[6] T. Ogata, Chapter 3.01, Comprehensive Nuclear Materials, Elsevier, 2012.

[7] G.L. Hofman, R.G. Pahl, C.E. Lahm, D.L. Porter, Metall. Trans. A, 21A (1990) 517.

[8] M.C. Billone, Y.Y. Liu, E.E. Gruber, T.H. Hughes, J.M. Kramer, Proc. Int. Conf. Reliable Fuels for Liquid Metal Reactors, Tucson, Arizona, September 7-11 (1986).

[9] H. Guo, W. Zhou, Y. Sun, D. Qian, J. Ma, J. Leng, H. Huo, S. Wang, Nucl. Engr. Tech. 49 (2017) 734.

[10] Y. Tsuboi, T. Ogata, M. Kinoshita, H. Saito, J. Nucl. Mater. 188 (1992) 312.

[11] C.B. Lee, D.H. Kim, Y.H. Jung, J. Nucl. Mater. 288 (2001) 29.

[12] J. Rest, J. Nucl. Mater. 207 (1993) 192.

[13] W.R. McDonell, ANS Trans. 15 (1972) 185 Proc. Int. Conf. on Physical Metallurgy of Reactor Fuel Element, eds. J.E. Harris and E.C. Sykes (The Metallurgical Society, London, 1975) p. 266.

[14] L.K. Mansur, W.A. Coghlan, J. Nucl. Mater. 119 (1983) 1.

[15] O. Emelyanova, A. Gentils, V.A. Borodin, J. Nucl. Mater. 545 (2021) 152724.

[16] M. Griffiths, J. Ramos-Nervi, L. Greenwood, J. Nuclear Eng. 2 (4) (2021) 484–515.

[17] J. Rest, G.L. Hofman, Y.S. Kim, J. Nucl. Mater. 385 (2009) 563–571.

[18] J. Rest, J. Nucl. Mater. 407 (2010) 55–58.

[22] COMSOL Multiphysics User’s Guide manual, COMSOL Inc., www.comsol.com.

[21] B. Beeler, Y. Zhang, M. Okuniewski, C. Deo, J. Nuclear Mater. 508 (2018) 181.

[20] G.-Y. Huang, B. Wirth, J. Phys. Condens. Matter 23 (2011) 205402.

[23] H. Savage, J. Nucl. Mater. 25 (1968) 249.

[19] Z. Qian, W. Liu, R. Yu, Y. Tao, D. Yun, L. Gu, J. Nucl. Mater. 556 (2021) 153188.

[24] T. Kobayashi, et al., Nucl. Technol. 89 (1990) 183.

[25] A. Karahan, Ph. D. Thesis, Massachusetts Institute of Technology, 2009.

[26] L. Leibowitz, R.A. Blomquist, Int. J. Thermophys. 9 (1988) 873.

[27] S.D. Yu, S. Xu, Nucl. Engr. Design 216 (2002) 165.

[28] E.F. Fisher, C.J. Renken, Physical Rev. 135 (1964) 482.

[29] D. Yun, A.M. Yacout, M. Stan, T.H. Bauer, A.E. Wright, J. Nucl. Mater. 448 (2014) 129.

[30] Y. Gao, Master’s Thesis of Xi’an Jiaotong University (2018).

[31] E.E. Gruber, J.M. Kramer, Proc. 13th Int. Symp. (Part-I) Radiation Induced Changes in Microstructure, ASTM-STP-955 (1987) 432.

[32] D.R. Olander, Fundamentals of Nuclear Reactor Fuel Elements, Energy Res. Development Administration (1976) (Chapter 13).

[33] G. Kresse, J. Furthmüller, Phys. Rev. B 54 (16) (1996) 11169.

[34] G. Kresse, J. Hafner, Phys. Rev. B 47 (1) (1993) 558.

[35] G. Kresse, J. Furthmüller, Comp. Mater. Sci. 6 (1) (1996) 15.

[36] R.G. Pahl, R.S. Wisner, M.C. Billone, G.L. Hofman, In Proceedings of the Int. Fast Reactor Safety Meeting, Snowbird, UT (1990) 129 Vol. IV.

[37] M.S. Veshchunov, J. Nucl. Mater. 277 (2000) 67.

[38] Pekka Lösönen, J. Nucl. Mater. 304 (2002) 29.

[39] T. Ogata, M. Kinoshita, H. Saito, T. Yokoo, J. Nucl. Mater. 230 (1996) 129.