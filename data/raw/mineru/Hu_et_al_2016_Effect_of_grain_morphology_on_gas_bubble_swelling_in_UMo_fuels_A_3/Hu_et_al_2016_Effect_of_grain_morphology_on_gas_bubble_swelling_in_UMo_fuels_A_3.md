# 📄 PDF Parsing Result

**File:** `/Volumes/openclaw记忆/Zotero_storage/storage/3NIJ4CEK/Hu et al._2016_Effect of grain morphology on gas bubble swelling in UMo fuels – A 3D microstructure dependent Booth model.pdf`
**Backend:** `pipeline`
**Pages:** 0 to end
**Formula Recognition:** ❌ Disabled
**Table Recognition:** ✅ Enabled

---

# Effect of grain morphology on gas bubble swelling in UMo fuels e A 3D microstructure dependent Booth model

Shenyang Hu\* , Douglas Burkes, Curt A. Lavender, Vineet Joshi

Pacific Northwest National Laboratory, P. O. Box 999, Richland, WA, 99352, United States

## a r t i c l e i n f o

Article history:   
Received 3 June 2016   
Received in revised form   
29 August 2016   
Accepted 30 August 2016   
Available online 31 August 2016   
Keywords:   
UMo metal fuels   
Gas bubble swelling   
Grain morphology   
Fission rate   
The Booth model

## a b s t r a c t

A three dimensional microstructure dependent swelling model is developed for studying the fission gas swelling kinetics in irradiated nuclear fuels. The model is extended from the Booth model [1] in order to investigate the effect of heterogeneous microstructures on gas bubble swelling kinetics. As an application of the model, the effect of grain morphology, fission gas diffusivity, and spatially dependent fission rate on swelling kinetics are simulated in UMo fuels. It is found that the decrease of grain size, the increase of grain aspect ratio for the grain having the same volume, and the increase of fission gas diffusivity (fission rate) cause the increase of swelling kinetics. Other heterogeneities such as second phases and spatially dependent thermodynamic properties including diffusivity of fission gas, sink and source strength of defects could be naturally integrated into the model to enhance the model capability.

Published by Elsevier B.V.

## 1. Introduction

The development of low-enriched uranium (LEU) fuels such as g UMo dispersion and monolithic fuels is part of a global effort on nuclear non-proliferation [2]. Although g UMo fuels have the advantage of high density, excellent irradiation performance and good thermal conductivity, the volumetric swelling in irradiated metallic fuels is known to be an important design parameter because it affects not only the thermal conductivity of the fuels but also the mechanical integrity of fuel structures [3e5]. Nuclear reactions continuously generate fission gas atoms such as Xe and Kr. These gas atoms segregate and form gas bubbles because of their extremely low solubility in UMo fuels. The nucleation and growth of fission gas bubbles are primarily responsible for the swelling in metallic fuels. A series of materials processes such as casting, mechanical rolling and thermal treatment are used in fuel fabrication [6,7]. The resulting microstructure, such as grain size distribution, grain aspect ratio, Mo spatial distribution, porosity, dislocation density and structure, and second phase volume fractions, strongly depends on the material processes and process parameters. Therefore, a fundamental understanding of how fabricated microstructures and irradiation conditions affect the nucleation of gas bubbles and gas bubble swelling kinetics is essential for optimizing material processes to obtain desired microstructure and fuel performance.

Great efforts have been made in the development of modeling capability for predicting gas bubble swelling kinetics [1,2,5,8e17] and fission gas release kinetics [18e21] in nuclear fuels. Booth [1] treated an individual grain within the material as a sphere whose boundary behaves as a perfect sink, and first developed a mathematical description of the diffusion of gas atoms in the representative sphere. Speight [8] extended the Booth model to consider the influence of trapping and re-dissolving of gas at intra- and intergranular bubbles on the migration of fission gas atoms. General expressions are derived for the gas atom flux to grain boundaries and the gas atom concentration existing instantaneously within bubbles and in solution. Hayns and Wood et al. [9e11,16] introduced the feature of intra- and intergranular gas bubble nucleation into the Booth model. Rest et al. [12e15] derived an analytical solution of intra- and inter-granular gas bubble size evolution by coupling rate equations that describe the nucleation and growth of inter- and intragranular bubbles under the simultaneous effect of irradiation-induced gaseatom re-solution. Recently, the effect of recrystallization on gas bubble swelling was also taken into account in UMo metallic fuels [5,14]. However, these models are based on the assumptions that the inter- and intra-granular gas bubble sizes are independent of position and only depend on time or fission density. In other words, the size and/or size distribution evolution of intra- and inter-granular gas bubbles only depends on the average grain size of the polycrystalline materials and irradiation conditions. Therefore, these models are applicable to a material with uniform microstructure such as equiaxed grains with homogeneous defect distributions, homogeneous thermodynamic and kinetic properties of defects, and uniform radiation conditions.

This work extended the capability of the Booth model by taking into account the effect of heterogeneous microstructures and inhomogeneous thermodynamic properties of defects on fission gas diffusion field, hence gas bubble swelling kinetics, in order to assess the effect of more realistic microstructures and accurate material properties on fuel performance. Our model employs all the evolution equations in the Booth model including fission gas concentration, the radius, density, and the content of fission gas atoms in inter- and intra-granular gas bubbles. However, our model releases the assumption of spatial independence of variables. Like the Booth model, our model assumes that the grain boundary is the perfect sink; fission gas has high mobility on grain boundaries; and fission gas concentration on grain boundaries remains in thermodynamic equilibrium. Experiments and modeling show that recrystallization in irradiated UMo fuels importantly affect the swelling kinetics [5,15]. However, the recrystallization mechanisms and kinetics are not well understood. Therefore, in this work, we focus on studying the effect of the heterogeneous microstructures such as rolling-induced elongated grains, inhomogeneous grain size distribution (coarse grains and recrystallized grains), and casting-induced Mo homogeneity on the gas bubble swelling kinetics prior to recrystallization. The development of a swelling model integrating the effect of dynamic recrystallization on swelling is underway.

## 2. Diffusion model of fission gas atoms inside a polycrystalline material

We consider an irradiated polycrystalline UMo fuel. The nuclear reaction continuously generates fission gas atoms such as Kr and Xe. Due to the extremely low solubility of fission gas atoms in the matrix phase, they precipitate to intra-granular gas bubbles and inter-granular gas bubbles. In the Booth model and extended models [8,14,22], the polycrystalline material is treated as an equivalent sphere that has average grain size and whose boundary behaves as a perfect sink of fission gas atoms. The diffusion of fission gas atoms inside a spherical grain with distributed small intra-granular gas bubbles is described as

$$
\tag{1}
$$

where.

c(r,t) is the concentration of total gas atoms (Xe, Kr, ….) in the UMo matrix.

r is radial distance in spherical coordinates.

t is the time.

cb(t) is the intra-granular bubble density.

nb(t) is the gas content per bubble.

rb(t) is the radius of the intra-granular gas bubble.

cg(t) is the volumetric average concentration of the dissolved gas.

fis the fission rate.

Y is the gas atom yield per fission.

b is the radiation-induced resolution rate of intra-granular gas bubble.

fn is the nucleation factor.

Dg is the diffusion coefficient gas atom under irradiation.

rg is the radius of the gas atom.

The first term on the right hand side of Equation (1) describes gas atom diffusion driven by the concentration gradient; the second term is the source term describing the generation of gas atoms during a fission reaction; the third and fourth terms present the loss of gas atoms associated with gas bubble nucleation and absorption at gas bubbles, respectively; and the last term is the gain of gas atoms associated with the radiation-induced resolution of gas bubbles. For simplicity, the local gas concentration c(r,t) in the third and fourth terms is replaced by the volumetric average concentration of the dissolved gas cg(t). Local gas bubble structural variables including the density, radius and gas content in the bubbles are assumed to be the spatial average inside the representative sphere. Therefore, the source and sink terms are not spatially dependent.

In a polycrystalline material the intra-granular gas bubble structure might strongly dependent upon microstructure. For example, the gas bubble structure at the center of a large grain could be different from that near the grain boundary. In UMo fuels, the gas bubbles inside large grains often form a fcc superlattice while the gas bubble superlattice structure is unstable inside small grains [2,23]. Therefore, the grain size, grain aspect ratio, and structural defects might result in a heterogeneous gas bubble structure, hence the gas bubble swelling kinetics. In order to study the effect of the heterogeneous microstructure on gas diffusion, gas bubble evolution, and gas bubble swelling, we treat all the variables in Equation (1) as a function of time and space in this work. The driving force of fission gas diffusion is generalized to be the local chemical potential gradient. Thus the effect of local stress fields, and structural defects such as grain boundaries on diffusion driving force could be naturally taken into account [24,25]. The fission rate, intra-granular gas bubble density, radius and the gas content in gas bubbles are time and space dependent functions. The diffusion Equation (1) is generalized as

$$
\tag{2}
$$

where r is the coordinate and m is the chemical potential of fission gas atoms. Grain boundaries are assumed to be a perfect sink similar to the Booth model. It is assumed that the concentration of fission gas atoms remain in thermal equilibrium concentration c eq:GB considering the fact that the diffusivity of gas atoms on grain boundaries are much larger than those inside grains, and the large inter-granular gas bubbles are strong sinks for the gas atoms. For a given intra-granular gas bubble microstructure (nb(r,t), cb(r,t), rb(r,t)) and the equilibrium concentration (c eq:GB ) of gas atoms on the grain boundaries, solving Equation (2) we obtain the total flux of gas atoms to the grain boundaries and the evolution of gas atom concentration c(r,t) inside the grains.

## 3. Evolution of intra- and inter-granular gas bubbles

A similar model presented by Spino et al. for UO2 fuels [22] is employed to describe inter- and intra-granular gas bubble evolution in UMo fuels for known local gas concentration and the total flux of gas atoms to grain boundaries. At the operation temperature of metallic UMo fuels (T < 500 K), the diffusion of fission gas atoms is assumed to be athermal with the gas atom diffusivity Dg proportional to the fission rate ḟ. The gas atom resolution rate b is also assumed proportional to the fission rate ḟ [13]. The intra-granular gas bubbles are assumed as identical inside a representative volume (dx\*dy\*dz) and the rate equation describing the time evolution of the density of gas atoms in intra-granular bubbles can be described by

$$
\tag{3}
$$

The three terms on the right hand side of Equation (3) present, respectively, the change in the density of gas atoms in intragranular gas bubbles due to bubble nucleation, the gas bubble growth by absorbing gas atoms in the matrix, and the loss of gas atoms from bubbles due to irradiation-induced re-solution. Equation (3) can be separated into two equations describing the time evolution of the fission gas bubble density and of the gas content per gas bubble, as follows:

$$
\tag{4}
$$

$$
\tag{5}
$$

Under the assumption of thermal equilibrium, the radius of intra-granular gas bubbles rb(r,t) is related to nb(r,t) through the gas law and the capillarity relation. Using a modified Van der Waals gas law,

$$
\tag{6}
$$

where g is the surface tension, bn is the Van der Waals constant for Xe, k is Boltzmann's constant, T is the absolute temperature, and hs is a fitting parameter that for a given T makes Equation (6) equivalent to the hard-sphere equation of state [26]. For nanometer sized gas bubbles, we have an approximate solution to Equation (6) as

$$
\tag{7}
$$

Therefore, the radius of intra-granular gas bubbles can be calculated by Equation (7) once we know the solution of Equation (5).

The grain boundary acts as a perfect sink for fission gas atoms. Since there are plenty of gas bubble heterogeneous nucleation sites on grain boundaries, and the mobility of gas atoms on grain boundaries is usually large, it is assumed that the density, radius and gas content of inter-granular gas bubbles is independent of location. With this assumption, inter-granular gas bubble density in irradiated materials can be calculated as [10,15,22].

$$
\tag{8}
$$

where.

a is the lattice constant.

z is the number of sites explored per gas-atom jump.

x is the grain-boundary diffusion enhancement factor.

d is the width of the boundary.

K is the flux of gas atoms from grain interior to the grain boundary.

In Equation (8) x is a major fitting parameter. For UMo fuels, the results [10,15,22] show that a value from 15 to 125 can reasonably reproduce existing experimental data [13]. Heterogeneous microstructures may cause a non uniform gas flux, hence a heterogeneous inter-granular gas bubble structure. Since the developed model directly solves the diffusion equation in polycrystalline materials it enables one to calculate the spatially dependent fission gas flux K(r,t) [atoms/m2 s] from grain interior to the grain boundary. Using K(r,t) [atoms/m2 s] we can study the heterogeneous intergranular gas bubble structure evolution if necessary. The nucleation kinetics may also affect the gas bubble structures such as the gas bubble size distribution. Rest et al. [14] developed a model to predict the evolution of fission gas bubble size distribution on grain boundary in UMo fuels. It is also possible to extend the current model to study the gas bubble size distribution evolution by integrating the method [14].

Solving Equations (2), (4), (5) and (7) together with the equilibrium concentration of gas atoms at grain boundaries, we have the average gas flux K(t) [atoms/m2 s]. The total amount N(t) [atoms/ m2 ] of gas atoms on the grain boundary can be calculated by t integrating the gas flux as NðtÞ ¼ Z KðtÞdt. The content of gas 0atoms per inter-granular gas bubble can be calculated by Nb(t) ¼ N(t)/Cb(t).

The modified Van der Waals gas law in Equation (6) can also be used to estimate the radius of the intergranular gas bubbles. For a finite size of gas bubble, the radius of an inter-granular gas bubble is obtained from the solution to Equation (6), i.e.,

$$
\tag{9}
$$

## 4. Gas bubble swelling before the grain recrystallization

The intra- and inter-granular gas bubble evolution equations presented above can be used to assess the fission gas swelling in irradiated fuels. The fractional swelling due to fission gas is thus given by

$$
\tag{10}
$$

where V is the volume of the simulation cell. The first term at the right hand side of Equation (10) accounts for the contribution of distributed intra-granular gas bubbles, the second term for the contribution of inter-granular gas bubbles, and the third term for the contribution of distributed gas atoms in the matrix. S is the total area of grain boundaries in the polycrystalline materials and ε0 is the formation volume of gas atom. Both experiments and theory [5,14,15] demonstrated that recrystallization in UMo fuels plays an important role in fuel swelling. Experiments show that recrystallization takes place when the fission density is larger than a critical value (3.1 \~ 3.5  1027 fission/m3 ) [14]. In this work we focus on investigating the effect of initial grain morphology on swelling kinetics prior to recrystallization.

## 5. Results and discussions

The simulations are carried out in a three dimensional (3D) polycrystalline domain200 dx  200dy  200dz, where dx, dy, dz are the grid sizes in x-, y- and z-axis, respectively. Periodic boundary conditions are applied in x-, y- and z-directions. Images of 3D polycrystalline structures can be directly used as the initial structure. Unfortunately, there is no 3D image of polycrystalline UMo available. In addition, it is very challenging to reconstruct 3D polycrystalline structures using 2D SEM and/or EBSD images. Therefore, in this work, a phase-field model of grain growth is employed to create a 3D polycrystalline structure as the initial structure for the simulations. For a given polycrystalline structure, the grain boundary is first identified where a chemical potential mGB of fission gas atoms could be applied that is an additional driving force for fission gas diffusion to grain boundaries besides the fission gas concentration gradient. The total area S of grain boundaries, which is used in Equation (10), is calculated; and an equilibrium concentration of fission gas on the grain boundaries is updated every 10 time steps in the simulations. Table 1 lists the model parameters that are used in literature [2,13e15,22,27]. Different sets of Xe diffusivity, fission rates, and nucleation factors are used to study their effect on the swelling kinetics.

For given model parameters, solving Equation (3), we can have the time evolution of intra-granular gas bubbles (4, 5,7); using Equation (8), we can calculate the inter-granular gas bubble evolution, and then the swelling can be calculated by Equation (10).

## 5.1. Effect of grain morphology on gas bubble microstructure

The Booth model used average intra-granular gas bubble morphology (average gas bubble concentration, radius, and gas content in bubbles) as model variables for assessing the swelling kinetics. First we present the intra-granular gas bubble evolution in a polycrystalline structure with 548 grains and an average grain size 1.34 mm in diameter to demonstrate the capability of our model. Xe diffusivity, fission rates, nucleation factors and the equilibrium fission gas concentration c eqGB used in the simulations are D0 ¼ 1.0  10-40 m5 /fission, ḟ ¼ 1.2  1020 fission/(m3 s), fn ¼ 0.03 and b ¼ 2.4  10-4 , respectively. Fig. 1 shows the distribution of intra-granular gas bubble density(bubbles/m3 ), gas content (the number of Xe atoms per gas bubble), and gas bubble radius (nm) inside gas bubbles on the plane A at time t  672 h. The color bar shows the value of the variables. For instance, red regions in Fig. 1b denote high gas bubble density while blue regions denote low gas bubble density. It can clearly be seen that the gas bubble density, radius, and gas content in bubbles decrease from the center of grains to grain boundaries. The spatial distributions of gas bubble density, radius, and gas content inside grains were analyzed. The results show that 1) the maximum gas bubble density, radius, and gas content inside grains increases with increased grain size, and 2) average gas bubble density, radius, and gas content inside grains also increase as the grain size increases. Fig. 2a shows the grain size dependence of average gas bubble density inside grains at time t  1157 and 2315 hours, respectively. The time evolution of gas bubble density on the line B-B0 shown in Fig. 1b is plotted in Fig. 2b. The results show that the increment of gas bubble density inside grains monotonically decreases, and the gas bubble structure gradually reaches a steady state structure. The temporal evolution and grain size dependence of radius and gas content inside grains have the same tendencies as that shown in Fig. 2. At steady state the intra-granular gas bubble density and radius inside grains increases with increased grain size. The predicted gas bubble density and diameter inside large grains is about 1.8  1024 bubble/m3 and 2.2 nm, respectively. TEM results of intra-granular gas bubble structures in UMo fuels shows that a nano sized gas bubble superlattice forms inside grains [23,28,29]. The gas bubble density is around 1.0 \~ 2.6  1024 bubble/m3 , and the gas bubble size is about 2 \~ 3.5 nm in diameter. No large change in the gas bubble density and only a slight increase of gas bubble size were observed with increasing fission density. From the comparison it can be seen that the intra-granular gas bubble structure obtained from simulations are in acceptable agreement with the experimental results. In addition, our model not only predicts overall gas bubble evolution kinetics including the average gas bubble density and size, but can also provide more thorough insight of heterogeneous gas bubble structures in irradiated materials than the Booth model.

Table 1  
Model parameters used in the simulations.
<table><tr><td>Characteristic length</td><td>l</td><td>50 nm</td></tr><tr><td>Grid size</td><td>dx=dy=dz</td><td>50 nm</td></tr><tr><td>Diffusivity of Xe</td><td>Dg=DOf</td><td>Do=1.0×10-40 m5/fission</td></tr><tr><td>Grain boundary energy</td><td>Y</td><td>1.0J/m²</td></tr><tr><td>Yield of Xe per fission</td><td>β</td><td>0.25</td></tr><tr><td>Fission rate</td><td>f</td><td>1.2 ×1020~2.4 ×1022 fission/m³/s</td></tr><tr><td>Grain boundary enhance factor</td><td>三</td><td>0.25</td></tr><tr><td>Dissolution rate</td><td>b=bof</td><td>bo =2.0 ×10-24</td></tr><tr><td>Ver der Waals constant for Xe</td><td>bv</td><td>8.5×10-29</td></tr><tr><td>Nucleation factor</td><td>fn</td><td>0.01~ 0.03</td></tr><tr><td>Fitting factor of EOS for Xe hs</td><td></td><td>0.6</td></tr><tr><td>Grain boundary thickness</td><td>6</td><td>1 nm</td></tr><tr><td>Grain boundary potential</td><td>μGB</td><td>0.0 eV/atom</td></tr><tr><td>Xe atom radius</td><td>rg</td><td>2.16×10-10m</td></tr><tr><td>Nearest jump sites</td><td>Z</td><td>8</td></tr><tr><td>Xe formation volume</td><td>ε0</td><td>1.05 ×1029m²</td></tr></table>

## 5.2. Comparison of gas bubble swelling kinetics

Our model is an extension of the Booth model. It is expected that two models should predict similar swelling kinetics if the polycrystalline structure has equiaxed grains because such a polycrystalline structure could be reasonably described by a representative spherical grain in the Booth model. To verify this, we consider two polycrystalline structures with equiaxed grains. The average grain sizes are 1.34 mm and 4.63 mm in diameter, respectively. The parameters: Xe diffusivity, fission rates, and nucleation factors are D0 1.0 10-40 m5 /fission, ḟ 1.2 1020 fission/(m3 s) and fn ¼ 0.01, respectively. The equilibrium fission gas concentration c eqGB is an additional parameter in our model compared to theBooth model. Fig. 3 presents the swelling kinetics obtained from the Booth model and our microstructural dependent swelling model for different equilibrium fission gas concentration c eqGB on grain boundaries. Increasing the fission gas equilibrium concentration c eqGB means decreasing the concentration gradient, hence, decreasing the diffusion driving force and gas flux from the grain interior to grain boundaries. As expected, the results in Fig. 3 show that the swelling kinetics decreases with the increase of the equilibrium fission gas concentration c eqGB. For small and large grain polycrystalline structures, the swelling kinetics predicted by our model approaches that from the Booth model when the equilibrium fission gas concentration on the grain boundaries increases from 5.0 10-6 to 1.5 10-5 . However, the simulations confirm that increasing or decreasing the Xe solubility will not further affect the swelling kinetics. In other words, the symbol lines for c eqGB ¼ 5:0  10-6 and c eqGB ¼ 1:5  10-5 give the upper and lower CGB bounds of swelling kinetics, respectively. Since the Booth model uses a representative spherical grain while our model uses a three dimensional polycrystalline structure, the difference in grain shape and grain size distribution used in two models causes different Xe fluxes to grain boundaries, hence, the difference in swelling kinetics. But comparing the results in Fig. 3 we can conclude that 1) the swelling kinetics predicted from our model are in good agreement with those from the Booth model, and 2) the Booth model underestimates the swelling kinetics due to the simplified assumption of grain morphology. The Xe solubility that is a parameter in our model can be estimated by Xe formation energies at grain boundaries in UMo alloys. Unfortunately, there is no such data available in literature to the authors knowledge. Henceforward, the equilibrium fission gas concentration on the grain boundaries will be set to be 1.5  10-5 because it produces the best agreement with the Booth model and the swelling kinetics are not sensitive to the Xe solubility.

![](images/2ba0949d78dcd3ceaab20034727cc90fd30b347f6c80e6821f9640086d170b7f.jpg)  
(a)

![](images/3f18753bdee22be11a14dd54293487d2b90038a261ce832208f1931fcc8ac931.jpg)  
(b)

B  
![](images/5c055e04dad3c309886f670664a9df2b1571a9719877eb8f6e7b2ec7e915dc13.jpg)  
(c）

![](images/54673485eefd9fc70ea1dbe4ca521f30561e3041798d955ee5d340f881961296.jpg)  
(d)

Fig. 1. (a) a simulated polycrystalline UMo structure with 548 grains and average grain size 1.34 mmin diameter, (b) the distribution of intra-granular gas bubble density, (c) the distribution of gas content in gas bubbles, (d) the distribution of gas bubble radius on the plane A shown in Fig. 1a.  
![](images/78c627fd791014b75d2841fba44ef2ad30e2856c765134c2338c87af1c53f88a.jpg)  
(a)

![](images/95fd1ef6964ff196874c43e6c591f1536d6ea89c027cd8db23f2b1f2f617ffe2.jpg)  
(b)  
Fig. 2. (a) Grain size dependence of average intra-granular gas bubble density for two different times. (b) Temporal evolution of intra-granular gas bubble density along the BB0 line shown in Fig. 1b.

![](images/4b30f8b1ae295fbda5356547b965b93f3392a8dbeb405bd620df5304efdec74c.jpg)  
Fig. 3. A comparison of swelling kinetics obtained from the Booth model and our model in two polycrystalline structures.

For intra-granular gas bubbles, the spatial average of gas bubble density and radius are calculated. The results from our model and the Booth model are plotted in Fig. 4. Our model predicted a higher inter-granular gas bubble density and lower intra-granular gas bubble density than that predicted by the Booth model, hence, a larger swelling kinetics. These results are consistent with the analysis above. However, if comparing the time evolution of gas bubble density and radius, we can find that the two models give very similar evolution kinetics. For example, the inter-granular gas bubble density attains the steady state quickly (Fig. 4b) while the intra-granular gas bubble density attains the steady state slowly (Fig. 4a). For gas bubble radius, our model predicts a smaller radius of inter-granular gas bubble density (Fig. 4c) and larger radius of intra-granular gas bubbles than that from the Booth model (Fig. 4d).

Although the two models produce similar swelling kinetics, the difference in gas bubble densities and size is obvious. For example, about 30% difference is observed for an average intra-granular gas bubble radius. The Booth model solves the fission gas diffusion and gas bubble evolution in a representative sphere. Our model solves the fission gas diffusion field in a polycrystalline structure. Due to the presence of small grains, the fission gas flux calculated in our model is larger than that from the Booth model, which results in a larger nucleation rate of inter-granular gas bubbles, and all the gas bubble structure difference. Therefore, the Booth model will underestimate the swelling kinetics, especially in a polycrystalline structure with a broad grain size distribution.

## 5.3. Effect of grain morphology on gas bubble swelling kinetics

Four crystal structures are generated by the phase-field model of grain growth for studying the effect of grain morphology on swelling kinetics. Crystal A has small grains. Crystal B has large grains. Crystals C and D have elongated grains with aspect ratios 4:1 and 16:1, respectively. These elongated grains mimic rollinginduced grain morphological changes and have the same volume as that in Crystal B. The grain morphology of these crystal structures are listed in Table 2.

The predicted effect of grain morphology on swelling kinetics is presented in Fig. 5. Two obvious tendencies are observed: 1) the swelling kinetics increase with decreasing grain size, and 2) the swelling kinetics increase with increasing aspect ratio for grains with the same volume. With the grain morphology changes from large grain to small grain and/or from equiaxed grain to elongated grain, the diffusion path of fission gas becomes shorter and shorter, which causes an increase of fission gas flux to grain boundaries and a decrease of fission gas concentration inside grains. As a consequence, the intra-granular gas bubble density and radius decreases, the intra-granular gas bubble structure more quickly reaches steady state, and swelling kinetics increases due to the increasing contribution of inter-granular gas bubbles to swelling. These results demonstrate that the developed model extends the Booth model's capability, and enables one to study the effect of grain morphology on swelling. The model can be further extended to consider the effect of any heterogeneous structures such as the distributed second phase that may have different swelling mechanisms, e.g., the a and a0 phases, dislocations, recrystallization zone, and heterogeneous fission rate on swelling kinetics.

## 5.4. Effect of fission rate and Xe diffusivity on gas bubble swelling kinetics

Xe diffusivity in irradiated materials is assumed to be proportional to fission rate written as DXe D0ḟ[30]. D0 is a constant of proportionality associated with the volume affected by a fission spike. For UMo fuels it is taken to be D0 1.0  10-40 m5 [15]. Therefore, Xe diffusivity is directly related to the fission rate. Gas bubble swelling is simulated in the four crystal structures listed in Table 2 for different Xe diffusivity or fission rates. Fig. 6a presents the result in Crystal B that has large grains. It is found that the swelling kinetics increase with increasing Xe diffusivity/fission rate. The swelling in terms of fission density, that is fission rate multiplied by time, is replotted in Fig. 6b. It clearly shows that the total amount of swelling is determined by the fission density for a given crystal structure. The effect of fission rates on swelling kinetics for Crystals B, C and D were also studied. The results reveal the similar grain morphological dependence shown in Fig. 5 for different fission rates, i.e., 1) the swelling kinetics increase with decreasing grain size, and 2) the swelling kinetics increase with increasing aspect ratio for grains with the same volume.

## 5.5. Effect of Mo inhomogeneous distribution on gas bubble swelling kinetics

A core shell structure of Mo distribution, which has higher Mo concentration at the center of grains and lower Mo concentration at the grain boundaries, often forms during casting of metallic UMo fuels due to a strong temperature dependence of Mo solubility in g UMo. From experiments the Mo concentration varies anywhere between 10 at% to 25 at% [31,32]. This Mo inhomogeneity might cause inhomogeneous distribution of U235, which may result in spatially dependent fission rate. In addition, the material process might induce other inhomogeneities such as second phase UC particle distribution, formation of alpha U phase, and dislocation networks associated with cold and hot rolling. These heterogeneous structures will affect fission gas diffusivity and nucleation rate, hence the gas bubble swelling kinetics. If we introduce the inhomogeneous model parameters related to the structure and thermodynamic property inhomogeneity, the current model is able to study the influence of heterogeneous structures and inhomogeneous properties on swelling kinetics. As an example of the application, we consider the effect of spatially dependent fission rate on swelling related to U235 inhomogeneous distribution. A phase-field model of solute diffusion in a polycrystalline structure is used to create a core shell structure of Mo distribution. The Mo distribution is converted to U235 distributions based on the lattice conservation and U enrichment. Then we assumed that the fission rate is proportional to the U235 concentration. Fig. 7a shows the core shell structure of Mo distribution obtained from the phase-field model in Crystal B. The color bar presents Mo atoms per unit volume (m3 ) in U10 wt% Mo alloys. Three different Mo distributions, which are denoted as Case1, Case 2, and Case 3, are created for studying the effect of Mo inhomogeneity/fission rate on swelling. Mo has a uniform distribution in the polycrystalline structure in Case 1. The inhomogeneity of Mo distribution in Case 3 is stronger than that in Case 2. The fission rate is written as ḟ(r)  F(r)ḟ. F(r) is the scale factor of fission rate that is a function of local Mo concentration. In order to have the same average fission rate and fission density in all Cases F(r) satisfies the equation R F r dV=V 1, Vwhere V is the volume of simulation cell. Fig. 7b presents the scale factors of fission rate along the BB0 line as shown in Fig. 7a for Case1, Case 2 and Case3. F(r) is equal to 1 in Case 1 that means a homogeneous fission rate. The fission rate near grain boundaries is larger than at the center of grains.

![](images/6ce6a4d7c9f5455f4723f186bd22099528b7131a712759a58dd674a9a8fe51c5.jpg)  
(a)

![](images/f9c37fbfb77f760b4bca7debe7ce5bfbe0e6983749365a75a03f0aa924eb1b39.jpg)  
(b)

![](images/be556b17e7e2fe468a9e7019753f591bff0bbdec66c2c300f25d0ee2dd8fdc91.jpg)  
(c）

![](images/aa9a1aac45dce4057f4a97e3f54883b031bcae31fb46afe78ad979f925d8aa71.jpg)  
(d)  
Fig. 4. Comparison of average gas bubble density and size evolution obtained from the Booth model and our model in two polycrystalline structures. (a) Intra-granular gas bubble density, (b) Inter-granular gas bubble density, (c) Radius of intra-granular gas bubbles, and (d) Radius of inter-granular gas bubbles.

Morphology of four polycrystalline structures.
<table><tr><td></td><td>Number of grains</td><td>Average diameter</td><td>Aspect ratio</td></tr><tr><td>Crystal A</td><td>548</td><td>1.34 μm</td><td>1:1</td></tr><tr><td>Crystal B</td><td>20</td><td>4.36 μm</td><td>1:1</td></tr><tr><td>Crystal C</td><td>20</td><td></td><td>4:1</td></tr><tr><td>Crystal D</td><td>20</td><td></td><td>16:1</td></tr></table>

![](images/b42439f009925d2ea015514b7782d44052d1b8ffd6922d88aa434109ebb2904f.jpg)  
Fig. 5. The effect of grain morphology on gas bubble swelling kinetics under fission rate ḟ  2.4  1022 fission/(m3 s) and nucleation factor fn 0.02.

![](images/104ae0048534888e9fdb8debc10d771c8529d83abf6f32345ce7633e174e4d00.jpg)  
(a)

![](images/44ba647e5a93e88a94b21634bd5f98dd5c9797bcd31b4d4b804b1de7d60413df.jpg)  
(b)  
Fig. 6. Effect of fission rates on gas bubble swelling kinetics in Crystal B. (a) swelling vs time, and (b) swelling vs fission density.

The simulation results are shown in Fig. 8. It can be seen that swelling kinetics increase with increasing fission rate inhomogeneity from Case 1, Case 2 to Case 3 for crystal structures with small and large grains, respectively. However, the influence of fission rate inhomogeneity on swelling is not significant. In Case 3 the fission rate at the center of the grain is about 0.71ḟ while the fission rate at the grain boundaries is about 1.22ḟ. Such an inhomogeneous fission rate causes about 6.5% swelling increase under fission rate ḟ ¼ 1.2  1020 fission/(m3 s) after 900 h of irradiation. Besides the impact of Mo inhomogeneity on the fission rate, Mo inhomogeneity may also cause the phase transition from gamma U to alpha U and affect the recrystallization process, which may impact the fuel swelling and fuel performance.

![](images/3114f66dda3448e5d251cbe1f2998f8d35db876d2158126c02310cb1057594f1.jpg)  
Fig. 8. Effect of Mo inhomogeneous distributions on swelling kinetics under fission rate ḟ 1.2 1020 fission/(m3 s) and nucleation factor fn 0.03.

![](images/b030b30eaa6ed7ceb0d7bdeae9617d677887ffaca69b6cc0f4e49789ef87ab9b.jpg)  
(a)

![](images/82ba1d0cf1542f442cdf1b86ecba883320323c4eceeb8159c214369ab04f7f87.jpg)  
(b)  
Fig. 7. (a) Mo spatial distribution on plane A which is generated by phase-field modeling in Crystal B of U10 wt% Mo fuels, (b) scale factor of fission rate along the BB0 line shown in (a) for three different Mo distributions.

## 6. Conclusions and remarks

A microstructure dependent gas bubble swelling model is developed that is extended from the Booth model. The model enables one to investigate the effect of heterogeneous microstructures such as grain size distribution, and grain aspect ratio, and spatially dependent thermodynamic properties including diffusivity of fission gas, sink and source strength of defects, temperature, stresses and chemical potential on gas bubble swelling kinetics. As application of the model, the effect of grain morphology, fission gas diffusivity, spatially dependent fission rates on swelling kinetics were simulated. It was found that 1) swelling kinetics increase with decreasing grain sizes. 2) swelling kinetics increase with increasing grain aspect ratio for grains having the same volume. 3) swelling kinetics increase with increasing fission gas diffusivity (fission rate), and 4) the total amount of swelling is determined by the fission density under the assumptions that the fission gas diffusivity, gas bubble nucleation factor, and dissolution strength are proportional to the fission rate. It was found that the effect of the spatially dependent fission rate related to inhomogeneous Mo distribution on swelling kinetics is not significant under simulation conditions such as grain size around a few micrometers and before recrystallization.

The simulations demonstrate that the developed model dramatically extends the prediction capability of the Booth model. However, for engineering applications, the model needs to be further improved. In current simulations, the grain sizes are around a few micrometers that are much smaller than those (approximately few tens of micrometers) in monolithic UMo fuels. The limitation is from the assumption that the thickness of gas bubble denuded zone on the grain boundary is set to be the characteristic length l0. All the fission gas atoms diffusing into the gas bubble denuded zone will be absorbed by the inter-granular gas bubble. The grid size dx  dy  dz in the simulation cell is set to be l0. Thus the simulation size is limited by the characteristic length l0 and current computer capability. For a given l0, we may use an adaptive mesh, smaller mesh on grain boundaries and larger mesh inside the grain, to largely increase the simulation size. The recrystallization is critical to UMo fuel swelling and performance. The current model is applicable before recrystallization occurs. Experiments show that the recrystallization is related to the local radiation defect accumulation such as dislocation loop density [33e36]. Therefore, the heterogeneous microstructures such as grain morphology will affect the evolution of dislocation loop density, hence, recrystallization and the swelling kinetics. The work integrating the recrystallization kinetics into the swelling model is underway. In addition, the developed model is able to study the effect of sink and sources of defects on the swelling kinetics such as dislocations and grain boundaries. A predictive model needs the thermodynamic properties of defects including the sink strength and emission rates.

## Acknowledgements

The work described in this article was performed by Pacific Northwest National Laboratory, which is operated by Battelle for the United States Department of Energy under Contract DE-AC05- 76RL01830. This study was supported by the U.S. Department of Energy, National Nuclear Security Administration, Office of Material Management and Minimization Reactor Conversion Program.

## References

[1] A.H. Booth, Atomic Energy of Canada Limited Report No. 496, 1957.

[2] Y.S. Kim, G.L. Hofman, J. Nucl. Mater. 419 (2011) 291e301.

[3] Y.S. Kim, G.L. Hofman, J.S. Cheon, A.B. Robinson, D.M. Wachs, J. Nucl. Mater. 437 (2013) 37e46.

[4] R.M. Hengstler, L. Beck, H. Breitkreutz, C. Jarousse, R. Jungwirth, W. Petry,

W. Schmid, J. Schneider, N. Wieschalla, J. Nucl. Mater. 402 (2010) 74e80.

[5] Y.S. Kim, G.L. Hofman, J.S. Cheon, J. Nucl. Mater. 436 (2013) 14e22.

[6] G. Moore, AFIP-2 Fabrication Summary Report, INL/EXT-08e14871, 2010.

[7] D.E. Burkes, A.M. Casella, E.C. Buck, A.J. Casella, M.K. Edwards, P.J. MacFarlan, K.N. Pool, B.D. Slonecker, F.N. Smith, F.H. Steen, R.E. Thornhill, Fuel Thermophysical Characterization Project: Fiscal Year 2013 Final Report, PNNL-22981, 2013.

[8] M.V. Speight, Nucl. Sci. Eng. 37 (1969), 180-&.

[9] M.R. Hayns, M.H. Wood, Proc. R. Soc. Lond. A Math. 368 (1979) 331e343.

[10] M.H. Wood, K.L. Kear, J. Nucl. Mater. 118 (1983) 320e324.

[11] M.H. Wood, J.R. Matthews, J. Nucl. Mater. 91 (1980) 35e40.

[12] J. Rest, J. Nucl. Mater. 402 (2010) 179e185.

[13] J. Rest, G.L. Hofman, Y.S. Kim, J. Nucl. Mater. 385 (2009) 563e571.

[14] J. Rest, J. Nucl. Mater. 407 (2010) 55e58.

[15] J. Rest, J. Nucl. Mater. 346 (2005) 226e232.

[16] J.R. Matthews, M.H. Wood, J. Nucl. Mater 91 (1980) 241e256.

[17] Y. Cui, S.R. Ding, Z.T. Chen, Y.Z. Huo, J. Nucl. Mater. 457 (2015) 157e164.

[18] R.J. White, M.O. Tucker, J. Nucl. Mater. 118 (1983) 1e38.

[19] D.M. Dowling, R.J. White, M.O. Tucker, J. Nucl. Mater. 110 (1982) 37e46.

[22] J. Spino, J. Rest, W. Goll, C.T. Walker, J. Nucl. Mater. 346 (2005) 131e144.

[21] P.C. Millett, M.R. Tonks, S.B. Biner, J. Nucl. Mater 424 (2012) 176e182.

[20] K. Forsberg, A.R. Massih, J. Nucl. Mater. 127 (1985) 141e145.

[23] J. Gan, D.D. Keiser, B.D. Miller, A.B. Robinson, J.F. Jue, P. Medvedev, D.M. Wachs, J. Nucl. Mater. 424 (2012) 43e50.

[24] S.Y. Hu, C.H. Henager, H.L. Heinisch, M. Stan, M.I. Baskes, S.M. Valone, J. Nucl. Mater. 392 (2009) 292e300.

[25] N. Moelans, B. Blanpain, P. Wollants, Phys. Rev. B 78 (2008).

[26] C. Ronchi, J. Nucl. Mater. 96 (1981) 314e328.

[27] A. Denis, R. Piotrkowski, J. Nucl. Mater. 229 (1996) 149e154.

[28] S. Van den Berghe, W. Van Renterghem, A. Leenaers, J. Nucl. Mater. 375 (2008) 340e346.

[29] J. Gan, D.D. Keiser, D.M. Wachs, A.B. Robinson, B.D. Miller, T.R. Allen, J. Nucl. Mater. 396 (2010) 234e239.

[30] H. Matzke, Radiat. Eff. Defect S 53 (1980) 219e242.

[31] Z.J. Xu, V. Joshi, S.Y. Hu, D. Paxton, C. Lavender, D. Burkes, J. Nucl. Mater. 471 (2016) 154e164.

[32] K.H. Kim, D.B. Lee, C.K. Kim, G.E. Hofman, K.W. Paik, J. Nucl. Mater. 245 (1997) 179e184.

[33] J. Rest, J. Nucl. Mater. 349 (2006) 150e159.

[34] I.L.F. Ray, H. Thiele, H. Matzke, J. Nucl. Mater. 188 (1992), 90-&.

[35] K. Nogita, K. Une, Nucl. Instrum. Method B 91 (1994) 301e306.

[36] J. Spino, D. Baron, M. Coquerelle, A.D. Stalios, J. Nucl. Mater. 256 (1998) 189e196.
