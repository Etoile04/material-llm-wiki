# 📄 PDF Parsing Result

**File:** `/Volumes/openclaw记忆/Zotero_storage/storage/9Q8MV4MM/Hu et al._2020_Defect cluster and nonequilibrium gas bubble associated growth in irradiated UMo fuels – A cluster dynamics and phase fi.pdf`
**Backend:** `pipeline`
**Pages:** 0 to end
**Formula Recognition:** ❌ Disabled
**Table Recognition:** ✅ Enabled

---

# Defect cluster and nonequilibrium gas bubble associated growth in irradiated UMo fuels – A cluster dynamics and phase field model

![](images/62ed4d0f29a1d827c98aef0494b7c7adfa083983720822fa0ef37c1e312052c3.jpg)

Shenyang Hua,∗ , Wahyu Setyawana , Benjamin W. Beeler b,c , Jian Ganb , Douglas E Burkes a

a Pacific Northwest National Laboratory, 902 Battelle Blvd., Richland, WA 99352, USA

b Idaho National Laboratory, PO Box 1625, MS 3740, Idaho Falls, ID 83415, USA

c North Carolina State University, 2500 Stinson Dr, Raleigh, NC 27607, USA

## a r t i c l e i n f o

Article history:   
Received 2 January 2020   
Revised 28 June 2020   
Accepted 29 July 2020   
Available online 15 August 2020

Keywords:   
UMo fuel   
Nonequilibrium gas bubble   
Gas bubble swelling   
Cluster dynamics and phase-field model

## a b s t r a c t

Irradiation examination shows that gas bubble swelling kinetics are much faster after irradiation-induced recrystallization than that prior to recrystallization in U-10 wt% Mo alloy (UMo) fuels. These kinetics imply that gas bubbles in coarse grains and small recrystallized grains have different growth behavior. For the first time, researchers developed a phase-field model of gas bubble evolution integrating microstructure-dependent cluster dynamics to study the gas bubble swelling behavior in the recrystallization zone of UMo fuels. Generation, diffusion, reaction, sink, emission, and clustering of vacancies and interstitials are described by the cluster dynamics model while a phase-field model is used to describe the evolution of nonequilibrium gas bubbles including nucleation and growth. With the coupled model, the effect of defect generation rate, clustering rate, interstitial emission, and sink rates on grain boundaries on the gas bubble evolution are systematically simulated. A set of model parameters (defect generation rate, clustering rate, interstitial emission, and sink rates) is determined by comparing measured and simulated gas bubble swelling kinetics. The results demonstrate that interstitial clustering is one of the important physical mechanisms that results in fast gas bubble swelling kinetics in the recrystallization zone. The developed model can also be extended to study the associated growth of defect and second-phase precipitates often observed in irradiated materials.

© 2020 Elsevier B.V. All rights reserved.

## 1. Introduction

U-10 wt% Mo alloys (UMo), with less than 20 wt% 235U enrichment, are considered a candidate for replacing highly enriched 235U fuels currently used in high performance research and test reactors in the United States. Irradiation examination of UMo monolithic fuels showed that irradiation-induced recrystallization dramatically speeds up the gas bubble swelling kinetics [1–6]. Recrystallization refines grain sizes from several micrometer coarse grains to 200nm-300nm fine grains. It implies that the gas bubbles in coarse grains and small recrystallized grains have different growth behavior. Fission reactions continuously generate fission gas atoms, vacancies, interstitials, and their clusters. Gas bubble growth requires both gas atoms and vacancies. Gas bubbles grow with absorption of vacancies and shrink with absorption of interstitials. Therefore, vacancy and interstitial concentrations affect the gas bubble growth kinetics. In coarse grains, experiments and modeling show that nano-sized gas bubbles form a face-centered cubic (fcc) superlattice [7–9]. The gas bubble density is about 1 \~ 4 × 1024/m3. Atomistic simulations of equation of states for gas bubbles in UMo fuels show that internal pressure inside the nano-sized Xe gas bubbles is on the order of a few GPa [10,11] and the gas bubble superlattice generates a compressive stress in the matrix [9]. The formation of interstitials and interstitial loops causes volume expansion of lattices. A compressive stress is not energetically favored for interstitial accumulation and interstitial loop growth. The compressive stress associated with dense nano-sized gas bubbles prevents interstitial accumulation and interstitial loop growth, which largely reduces the vacancy concentration. The low vacancy concentration causes slow gas bubble growth kinetics in coarse grains. On the other hand, the grain size in the recrystallization zone is about 200nm-300nm [5]. Inside these small grains, the gas bubble superlattice collapses, and gas bubbles with uniform distribution and low density form in the recrystallization zone [8,12]. The small grain size and low gas bubble density may release the stress in the matrix. Therefore, our hypothesis for the faster gas bubble growth in recrystallization zone is that interstitial clustering is energetically favored, which results in more vacancies available for the gas bubble growth.

Since gas bubbles are sinks for vacancies and interstitials, the evolution of gas bubbles (such as nucleation and growth) changes the sink strength while defect concentrations affect the gas bubble evolution. Therefore, to describe the gas bubble evolution in irradiated UMo fuels, the model needs to take the defect clustering and gas bubble associated growth into account. In this work, we extended the cluster dynamics model to a microstructure-dependent cluster dynamics model for taking into account both steady-state and evolving sinks. The generation, diffusion, reaction, sink, emission, and clustering of vacancies and interstitials in a polycrystalline structure with evolving gas bubbles are described by a microstructure-dependent cluster dynamics model. A phase-field model was used to describe the gas bubble nucleation and growth [13,14]. The information of defect clusters, defect fluxes, and fission gas atom flux obtained from cluster dynamics modeling is fed into the phase-field model of gas bubble evolution while the gas bubble structures from phase-field modeling are used to update the sinks in the cluster dynamics model. Integrating these two models enables us to study the effect of defect cluster evolution on gas bubble growth and swelling mechanisms. The model can also be extended to study the associated growth of defect and second phase precipitates often observed in irradiated materials [15–19].

## 2. Microstructure-dependent cluster dynamics and phase-field model of gas bubble evolution

To describe the gas bubble evolution in the recrystallization zone, two sets of field variables are used to describe the microstructure. One set is the order parameters ηm(x, t) and χ (x, t). ηm(x, t) describes the grain orientations and χ (x, t) describes the gas bubbles. ηm(x, t) is equal to 1 inside grain m, and 0 outside the grain m. It varies from 0 to 1 across the grain boundaries. The order parameter χ (x, t) is equal to 1 inside gas bubbles and 0 outside gas bubbles, and varies from 0 to 1 across the interface between gas bubble and matrix. The other set of field variables is defect concentrations Cli(n, x, t) and Cg(x, t). Cli(n, x, t) , which describe the concentrations of vacancy and interstitial clusters; li denotes a cluster with defect i which could be vacancy or interstitial while l means cluster or loop, n is the number of defect i in the cluster li, Cg(x, t) describes the concentration of fission gas atoms, and x, t are coordinate and time, respectively.

A phase-field model of grain growth [13] is used to generate polycrystalline structures. The grain boundaries are defined by a shape function η(x, t ) = 2 -m0m 1 (1 − ηm) 2 , which has the value of 0 inside the grains and continuously varies to 1 at the center of grain boundaries. m is the total number of grains in the simulation cell. Grain boundaries and gas bubbles are structural defects, which are sinks for vacancies and interstitials. The spatial distribution of sinks can be defined by θ (x, t ) = η(x, t ) + χ 2(x, t ). Fig. 1(a) shows the polycrystalline structure with cylindrical grains and distributed gas bubbles. At sinks of defects, when the defect concentration is larger than the equilibrium concentration, the defect will be emitted. In conventional rate theory the emitted defects will be used to update the overall defect concentration inside grains. This means that the emitted defects are uniformly distributed in the matrix. However, in reality, for a given simulation time increment, the distance of defect migration can be estimated by l  Dt, where D is diffusivity of defect and t is the time increment in the simulation. So, if l is much smaller than the grain size, uniformly redistributing the emitted defects inside the grains is incorrect. The emission rate in the polycrystalline structure should be nonuniform. In this work, to calculate defect emission, we define a defect emission zone near sinks. We first calculate the total amount of defect i during the time increment t, which will be emitted from sinks: Ci =   Sei,defDi[Ci − Ceq1i,def]dV where Ci is concentration of Ci,defl Sink

defect i, Ceq1 is the equilibrium concentration of defect i on the sink, Di is diffusivity of defect, a is the lattice constant, and Sei,de f is the local emission strength. The integration is on sinks (the red region in Fig. 1(b)). After that, the absorption zone (the yellow region in Fig. 1(b)) is defined where the minimum distance to sinks is less than l, and the total lattice of the absorption zone, Ntot, is calculated. Then, the emitted defects are uniformly distributed in the absorption zone by ξ˙ i,de f = Ci/(tNtot ). Fig. 1(b) shows the sinks including grain boundaries, gas bubbles, and the emission zone on the plane A in Fig. 1(a). The red lines represent grain boundaries, red circles for gas bubbles, and the yellow regions are the absorption zones. The sinks change with the evolution of gas bubbles and grain boundaries.

Having described defects and microstructures, next we present the cluster dynamics and phase-field models.

## 2.1. Microstructure-dependent cluster dynamics

In UMo fuels, 235U fission generates high-energy neutrons and fission fragments that cause radiation damage. The cluster dynamics model describes the evolution of gas atoms, vacancies, interstitials, and their clusters in polycrystalline structures with distributed gas bubbles. The generation of gas atoms, vacancies, and interstitials are calculated with the fission product yields and the kinetic energy distribution of the fission products. The details of defect generation are described in next section. Grain boundaries, gas bubbles, and dislocations are treated as sink and emission sites of defects. According to the kinetic rate theory, with the assumption that 1) only single interstitial, vacancy, and gas atoms are mobile, and 2) mobile gas atoms only interact with existing gas bubbles, the evolution of defect concentrations can be written as [20– 23]:

$$
\tag{1}
$$

![](images/4aa40c356453505ba0a8f551c77ab870f8aef4a1657767472d49bd2003268116.jpg)

i = j = I and V, m and li st and for a cluster with m defects i, M = MI or MV (2)

where C (x, t) is the concentration of mobile single defect i, i  V for single vacancy, i = I for single interstitial. Di is the diffusivity of defect i; Ui is the interaction energy between sink and defect i or chemical potential of defect on sinks; G˙ i denotes generation rate of vacancy, interstitial. α is a rate constant for the recombination between single vacancies and single interstitials; Kl j is the capture coefficient of mobile defect i by defect cluster mlj; γ l j (m) is the emission coefficient of mobile defect i by cluster m of defect j; S˙ i,de f is the sink rate of defect i on sinks (def) including grain boundary (gb), gas bubble interface (bb), and dislocation network(dis); and Ceq1i,de f is the equilibrium concentration of defect i on sinks (def); ξ˙ i,de f is the emission rate of defect i from sink (def). ρdis is the dislocation density. Clj(m, x, t) in Eq. (2) is the concentration of defect cluster li, which has m defects j. S˙ li,bb(m) is the sink rate of cluster li at gas bubbles. MI and MV are the largest allowable sizes of interstitial and vacancy clusters, respectively. The evolution of fission gas atom concentration (Xe is considered in this work) in UMo with distributed gas bubbles can written as

![](images/51dd030baf074227c160c7dfb8b1e3e7840a30eff2f9715bf8c2779785ba53f7.jpg)

![](images/7ae0aa0fc0132296a2ff21e1aa9506e2eea9f75ca69c39b06baf612b5a260fb4.jpg)  
(b)  
Fig. 1. (a) Polycrystalline structure with distributed gas bubbles, and (b) different regions on plane A: grain boundaries (red lines); gas bubbles (red circles); and absorption zone (yellow).

$$
\tag{3}
$$

where Cg(x, t) is the concentration of Xe atoms, Dg is the diffusivity of Xe; Ug is the interaction energy between sink and Xe or chemical potential of defect on sinks; G˙ g denotes generation rate of Xe, and S˙ g,bb is the sink rate of Xe at gas bubbles.

The evolution of the dislocations is described by a model similar to the one developed by Stoller [24,25],

$$
\tag{4}
$$

The first term in the right side describes the generation of network dislocations by Bardeen-Herring source. The second term represents the annihilation of climbing dislocations. vli is the climb velocity, SBH the density of Bardeen-Herring sources, and τ lj the mean lifetime before annihilation. The third term represents the rate at which new dislocation line length is generated by the unfault of largest interstitial loops (interstitial clusters MI). rM is the radius of interstitial cluster of size MI. τ (MI) is the time needed for the incorporation of the interstitial cluster M into the dislocation network. The calculation of vli, SBH, τ lj and τ (MI) is referred to the work [24].

Defect equilibrium concentration Ceq1i,de f is calculated by exp(E fi,de f /kBT ) where E fi,de is the formation energy of defect i on defect def. The rate constant α = Ziv(DI + DV )/a2 where a is the lattice constant, and Ziv is the combinatorial factor of vacancy and interstitial. Rate constant Kl j (m) = 4π ri,l jZi Di/ where  is the atom volume, ri, lj is the capture radius between defect i and cluster mlj; emission rate γ l j (m) = Kl j (m − 1)exp(−Ei (l j)/kBT )

where Ei (l j) is the binding energy between defect i and cluster mlj. The capture radius ri, lj is estimated by ri,l j = (ml j )1/3rat + rat and ri,l j = a 	ml j/(2π h) for vacancy and interstitial clusters, respectively. mlj is the total number of vacancies/interstitials in cluster lj and rat is the atom radius. h is the magnitude of Burgers vector of interstitial loop in units of a.

The binding energy between defect i and cluster mlj is a function of cluster size Eib(l j) = E fi + (Eb − E f )( 3
(ml j ) 2 − 3
(ml j − 1) 2 )/( √3 4 − 1). E f and Eb are the formation energy of defect i and the binding energy between defect i and 2i, respectively [21,26]. Zi is the bias coefficient, which also depends on the cluster size. S˙ is the sink rate of cluster mlj at gas bubbles. The defect diffusivity Di and the chemical potential Ui of defect i on grain boundaries and/or gas bubbles are different from those in matrix. The spatially dependent thermodynamic property of defect i is described as

$$
\tag{5}
$$

where 
0i is the property of defect i inside the grains, and 
i, defθ (ηm, χ ) is the difference of the property of defect i on the structural defect from that inside grains.

In conventional rate theory, the sink strength of defect i on a structural defect is estimated at the steady state by calculating the diffusion flux of defect i to an isolated structural defect in the matrix. For instance, the reaction-controlled sink rate of distributed gas bubbles with average radius R and density ρbb can be calculated by 4π R2Diρbbci Y si,bb/a [16]. For a single gas bubble, the sink rate is written as

$$
\tag{6}
$$

where Y si,bb is the biases of gas bubbles for interstitials or vacancies, and c is the average concentration of defect i at gas bubble interface. Y s 4π R2/a is the sink strength of a gas bubble with radius of R. Y si,bb depends on the type of defect i and gas bubble properties such as the defect structures at the gas bubble interface and gas pressure. A overpressure gas bubble generates a compressive stress around the gas bubble that causes an increase of Y sI,bb (bias of interstitials) and an decrease of Y sV,bb (bias of vacancies). For a system that has a high sink density and multiple types of sinks, or has evolving sinks such as evolving voids and/or gas bubbles in nuclear fuels, the concentration ci around the gas bubbles is not uniform, the gas bubble size varies with time, and the system may never reach steady state. This instability can be demonstrated by the observed gas bubble swelling kinetics in UMo fuels, which increase with the increase of fission density [5]. Therefore, it is hard to calculate the sink rate using the rate theory Eq. (6).

In our model, the gas bubble interface and grain boundary are implicitly described by θ1(ηm, χ ) = η(x, t ) + 2(1 − χ (x, t ))2 . The temporal evolution of defect concentrations is obtained by solving the Eqs. (1)–(4) in the system with spatial distributed and evolving sinks. The concentration near the gas bubble reflects the effect of all the coupling of the spatial dependent features of sinks mentioned above. We proposed a method to calculate the spatially dependent sink rate with the following assumptions: 1) all the defect absorption and emission take place inside the grain boundary and/or gas bubble interface zone, which is defined by θ 1(ηm, χ), and 2) the sink rate inside the gas bubble interface zone can be calculated as

$$
\tag{7}
$$

where Zsi,bb is the local sink strength. The total sink strength can be calculated by integrating the local sink strength Zsi,bb over the interface region (θ 1(ηm, χ ) > 0) of the gas bubble. The local sink strength Zsi,bb can be estimated with the total sink strength to be equal to Y s 4π R2/a from the rate theory. If the interface thickness of a gas bubble with radius R0 is H0 which is defined by θ 1(ηm, χ) > 0, the volume of interface zone is approximately calculated by V0 = 4π R20H0. Zsi,bb can be estimated by Zsi,bb = Y si,bb4π R20/(aV0) = Y si,bb/(aH0).

Our model releases the effect of coupling the spatially dependent features of sinks on the sink rate. Zsi,bb measures the average sink strength in the interface zone. For given the lattice constant a and the thickness of interface zone H0 which is a model parameter related to the grid size in the simulation cell, Zsi,bb only depends on the bias Y si,bb. As discussed above Y si,bb is a material property that depends on defect structures at the interface and the interaction between the interface and defect i and could be assessed by atomistic simulations. The defect emission rate can be defined as Sei,bb = Zei,bbDici, θ1(ηm, χ ) > 0 at the interface zone. Zei,bb is the local emission strength which also can be described as Zei,bb = Y ei,bb/(aH0). Y ei,bb is the bias that depends on the interface en- ergy between defect i and gas bubbles. The total emission Ci of defect i from the emission zone, which is described in the previous section, is calculated with Se . The absorption rate can be calculated by ξ˙ i,de f = Ci/(tNtot ). In the rate theory, defect sink and emission rates at grain boundaries have similar expressions as those at gas bubble and/or precipitate interface [27]. The same method was used to calculate sink and emission rates at grain boundaries.

The biases (Y si,bb and Y ei,bb) depend on the properties of sinks such as the misorientation angle of grain boundaries [27–29], coherency of precipitate interface, and the pressure of gas bubbles. To investigate the effect of biases on gas bubble evolution we carried out a parametric study by varying the biases.

## 2.2. Phase-field model of gas bubble evolution

Gas bubbles in irradiated nuclear fuels may not reach equilibrium. This means that the gas concentration inside gas bubbles may be larger or smaller than the equilibrium concentration. For example, the gas bubbles may become voids if the matrix has high vacancy concentration. In contrast, the gas bubble might be overpressurized if the vacancy concentration is low in matrix. To describe the nonequilibrium gas bubbles, we assume that gas bubbles are energetically favored sinks for vacancies and gas atoms, and are energetically unfavored sinks for interstitials. Once vacancies and gas atoms reach gas bubbles they are absorbed immediately by gas bubbles while interstitials are partially absorbed or emitted by gas bubbles. Three field variables (i.e., Xe atom concentration Cgg, vacancy concentration CgV, and order parameter χ ) are used to describe the gas bubbles in the phase-field model of nonequilibrium gas bubble evolution. The vacancy concentration CgV is different from CV in the cluster dynamics model. Vacancies, interstitials, and their clusters sinking to gas bubbles (described by S˙ i,bb and S˙ l j,bb in the cluster dynamics model) generate a net change of vacancies inside the gas bubbles. CgV accounts for the net vacancy concentration inside gas bubbles.

The Kim-Kim-Suzuki (KKS) model is used to describe the twophase equilibrium in UMo (i.e., matrix and void). According to the KKS model [30], the total free energy density of a system with vacancies and voids can be written as

$$
\tag{8}
$$

where χ is the order parameter, which is zero in matrix and unity in bubbles, p(χ ) = χ3(10 − 15χ + 6χ2) is a monotonously changing function from p(0) = 0 to p(1) = 1, g(χ ) = 30χ 2(1 − χ )2 is a double-well potential, and w is the height of the double well potential.

fm and fb are the bulk free energy density of the matrix and void, respectively. They are set to be f m = Am(cmv − c eqv )2 and f b = Abv(cbv − 1)2 where c eqv is the equilibrium concentration of vacancy in matrix. The total free energy F(CgV, χ ) of the system includes chemical free energy and interfacial energy. It is defined as

$$
\tag{9}
$$

where κ is a gradient coefficient. Two model parameters w and κ can be determined by the interfacial energy σ and interface thickness λ [14].

Following the KKS model, the concentration of vacancies is written as follows:

$$
\tag{10}
$$

At each point in the system, local thermodynamic equilibrium is assumed

$$
\tag{11}
$$

The evolution equations of gas bubbles are written as follows:

(12)

$$
\tag{13}
$$

where DgV is diffusivity of vacancies and L is the interface mobility. S˙ V,bb and S˙ I,bb are sink rates of vacancy and interstitial at gas bubbles, respectively. S˙ lv,bb and S˙ li,bb are the sink rates of vacancy and interstitial clusters at the gas bubbles.

It is assumed that all gas atoms, vacancy, and vacancy and interstitial clusters are absorbed by gas bubbles when they reach the gas bubbles. The sink rate is calculated by S˙ i,bb = SimCiχ /t, i = V, I, li, and lv. m is the number of defect cluster i. For interstitials, when their concentration on the gas bubble interface is larger than their equilibrium concentration, the interstitials are emitted as described in cluster dynamics model.

The gas phase inside gas bubbles is treated as a solution phase. The free energy density of the gas phase is described as

$$
\tag{14}
$$

where Ceqgg is the equilibrium concentration of gas atoms which is set to 0.45 [11]. The evolution of gas atom concentration is given as

$$
\tag{15}
$$

where Dgg is the diffusivity of gas atoms, and S˙ g,g is the sink rate of gas atoms calculated in cluster dynamics model. For large gas bubbles, it is reasonable to assume that gas atoms are confined inside gas bubbles once they are absorbed by the gas bubbles. To apply this assumption in the model, Dgg is defined as Dgg = Dgg0χ 2. Dgg is equal to Dgg0 inside the gas bubble, and equal to zero in the matrix. Dgg0 is the diffusivity of gas atoms inside gas bubbles, which should be much larger than that in the matrix.

One of merits of this work is that we developed a phase-field model of nonequilibrium gas bubble evolution in nuclear fuels. The Eqs. (8)–(13) describe two-phase equilibrium (i.e. void and matrix phases). Eqs. (14) and (15) describe the gas phase inside the void. Eq. (15) only evolves inside the voids, which can be seen from the definition of the diffusivity Dgg. Dgg is zero outside voids. All gas atoms inside the voids are from the sink term in Eq. (15), which is calculated from the cluster dynamic model. The evolution Eq. (15) drives the gas concentration inside voids to reach a uniform value (a solution phase). So, the nonequilibrium gas bubble model can describe the transition from the over-pressure gas bubble (high gas concentration) to the void-like gas bubble (low gas concentration), which completely depends on the ratio of gas atoms and vacancy inside the gas bubble.

## 2.3. Nucleation of gas bubbles

The concentration distributions of vacancies, interstitials, and their clusters are nonuniform because of inhomogeneous grain and gas bubble structures. With the increase of local net vacancy concentration (single vacancy, single interstitial, and their clusters), the defects will collapse and form a void. Based on this assumption, a statistical method is used to introduce the nuclei of gas bubbles. To do so, the total vacancy concentration, ctot (x, t ) is calculated by summing all the defects (single vacancy, single interstitial, and their clusters) at every N1 simulation step. The sum of vacancy concentration ctotin the matrix can calculated by integrating ctot (x, t ). The number of potential nucleation sites is determined by N2 = ctot /ccrt , where ccrt is the critical value of vacancy concentration required for the formation of a nucleus. Then, position xi, (i = 1, 2, . . . , N2 ) is chosen randomly; the total vacancy ctot1 at xi by integrating ctotM (x, t ) in a sphere with radius r1; and a spherical nucleus with radius rc is introduced if the total vacancy ctot is larger than the critical value ccrt. Inside the nucleus, the order parameter χ is set to be 1.0, the radius rc is calculated by [3ctot /(4π )]1/3. N1 and ccrt are model parameters. For given model parameters, r1 is estimated by 	DV N1t. In the simulations, N1 and ccrt are set to be 5000 and 1.0, respectively.

## 2.4. Flow chart of cluster dynamics and phase field model of gas bubble evolution

Fig. 2 shows the flow chart of cluster dynamics and phase field model of nonequilibrium gas bubble evolution. The chart shows that the cluster dynamics model and phase field model exchange information through the simulation. Defect concentrations and the absorption of defects at gas bubbles from the cluster dynamics simulation are used in nucleation and growth of gas bubbles in the phase-field model. The gas bubble structures obtained from phasefield modeling is used to update the sink as well as defect concentrations in the cluster dynamics model. The integrated model enables one to simulate defect and gas bubble-associated growth.

## 2.5. Model parameters

## 2.5.1. Calculation of defect generation during fission

To calculate the defect generation G˙ i, we need to know the fission product yields and the kinetic energy distribution of the fission products. Fission product (FP) yields depend on the fissioning nuclide and the energy of the neutron causing the fission. Here, we evaluate the model for fission from 23592 U due to thermal neutrons (neutron energy=0.0253 eV), which is applicable for lightwater reactors (LWRs). Based on previous work of Setyawan et al. [31], we take the independent fission product yield (iFPY) from the JEFF 3.3 library to calculate the defect generation in this work. The distribution of the fission products and kinetic energies (Etot) as a function of atomic number can be found in the reference [31]. The 18 elements listed in Table 1 make up almost 100% of the distribution. Every fission creates two fission products, one light fission product and one heavy fission product. The mass of the most probable isotope in each element is taken as the mass of the element. UMo fuels are currently developed for high performance research reactors. In high performance research reactor such as High Flux Isotope Reactor (HFIR) at Oak Ridge National Laboratory, the percentages of fissions caused by neutrons in the thermal, intermediate, and fast neutron ranges are 83.03% (< 0.625 eV), 15.50% (0.625 eV \~100 keV), and 1.48% (>100 keV) [32]. We calculated the fission product yields for neutron energy of 40keV. The calculation shows that the sum of fission product yields from18 elements is less than 0.5% for neutron energy 0.0253 eV and 40keV.

Using Etot and the mass of the most probable isotope, the Stopping and Range of Ions in Matter (SRIM) simulations are performed to obtain the portion of the energy lost due to electronic stopping (Eelectronic) and the energy that effectively causes damage via displacement cascade (Edamage), for each fission product. For SRIM simulations, the displacement threshold energy (Ed) of γ U from molecular dynamic (MD) cascade simulations [33] and the material density of pure γ U are used. Norgett, Robinson, and Torrens (NRT) formula of 0.4∗Edamage/Ed is used to estimate the Frenkel pair generation per fission [34]. The results show that one 23592 U fission generates about 14,825 Frenkel pairs in γ U. Since we do not have the cascade data of U-10wt%Mo, the defect generation calculated in γ U is used in the simulations. Table 1 summarizes the Etot, Eelectron, Edamage, and the number of Frenkel pairs for each FP.

## 2.5.2. Thermodynamic and kinetic properties of defects

Table 2 lists the model parameters used in the simulations. Very limited thermodynamic and kinetic properties of defects in U10Mo, which are needed in cluster dynamics and phase field models, are available in the literature. The defect formation energies of U vacancy and interstitials are assessed from the data of DFT and MD simulations in U and UMo alloys [35-37]. Selfdiffusivity of U is from MD simulations and experiments [38-41]. Xe diffusion is adopted from the rate theory model of gas bubble swelling in UMo [5]. Capture radius, bias coefficients, and model parameter of network dislocations are adopted from the cluster dynamic and rate theory models [21,23,24,27,42].

The thermodynamic and kinetics properties such as chemical potential Ui of mobile defects on grain boundaries, binding energy among defect and defect clusters, chemical free energies of different phases, and gas atom mobility inside gas bubbles are set up to reasonably capture the interaction among defects and phase stability. For instance, the diffusivity of vacancies and gas atoms inside gas bubbles is set up to be large so that the concentrations of vacancy and gas atoms quickly become uniform inside gas bubbles after the absorption at the gas bubble interface. In the simulations, DVg = 100DV and Dgg0 = 100Dg were used. The chemical potential of vacancy, interstitial, and gas atom inside the gas bubbles depends on the ratio of gas atom and vacancy or gas concentration Cgg. Generally speaking, vacancies and gas atoms should have lower chemical potentials inside gas bubbles than those in the matrix, which drives vacancies and gas atoms diffusing to gas bubbles. Interstitials should have a higher chemical potential inside a pressured gas bubble than that in matrix, which prevents interstitials diffusing to gas bubbles. For gas bubbles with low pressure or voids, interstitials, like vacancies, should have lower chemical potential inside voids than that in the matrix.

![](images/dea643e2fde49d111b02aaeb3eae339fd31dda8e6e24344139dcaa9f35acdaad.jpg)  
Fig. 2. Flow chart of the integrated cluster dynamics and phase-field model.

The most probable isotopes of fission products from 23592 U due to thermal neutrons, the independent fission product yield (iFPY), total kinetic energy (Etot), electronic loss (Eelectron), and Edamage = Etot – Eelectron used in SRIM simulations to estimate the number of Frenkel pairs in γ U with displacement threshold energy Ed 35.6eV at 800K.
<table><tr><td>Element</td><td>iFPY</td><td>Etot(MeV)</td><td>Eelectron(MeV)</td><td>Edamage(MeV)</td><td>Frenkel pairs</td></tr><tr><td>Se</td><td>0.042</td><td>101.3</td><td>98.362</td><td>2.938</td><td>1376.9</td></tr><tr><td>Br</td><td>0.051</td><td>101.2</td><td>98.117</td><td>3.083</td><td>1751.6</td></tr><tr><td>Kr</td><td>0.164</td><td>101.5</td><td>98.333</td><td>3.167</td><td>5829.3</td></tr><tr><td>Rb</td><td>0.112</td><td>101.2</td><td>97.840</td><td>3.360</td><td>4216.0</td></tr><tr><td>sr</td><td>0.209</td><td>101.1</td><td>97.766</td><td>3.334</td><td>7816.4</td></tr><tr><td>3Y</td><td>0.114</td><td>101.3</td><td>97.792</td><td>3.508</td><td>4504.4</td></tr><tr><td>100Zr 40</td><td>0.180</td><td>101.4</td><td>97.536</td><td>3.864</td><td>7824.6</td></tr><tr><td>102Nb 41</td><td>0.073</td><td>101.8</td><td>97.728</td><td>4.072</td><td>3319.2</td></tr><tr><td>14M0</td><td>0.041</td><td>101.2</td><td>97.172</td><td>4.028</td><td>1847.3</td></tr><tr><td>Sn</td><td>0.041</td><td>81.5</td><td>75.928</td><td>5.572</td><td>2555.1</td></tr><tr><td>3Sb</td><td>0.073</td><td>78.8</td><td>73.052</td><td>5.748</td><td>4685.4</td></tr><tr><td>14Te</td><td>0.180</td><td>77.5</td><td>71.641</td><td>5.859</td><td>11864.3</td></tr><tr><td>1361</td><td>0.114</td><td>74.6</td><td>68.582</td><td>6.018</td><td>7726.5</td></tr><tr><td>8xe</td><td>0.209</td><td>71.9</td><td>66.289</td><td>5.611</td><td>13154.9</td></tr><tr><td>141Cs 55</td><td>0.112</td><td>68.2</td><td>61.898</td><td>6.322</td><td>7931.9</td></tr><tr><td>4Ba</td><td>0.164</td><td>64.8</td><td>58.330</td><td>6.470</td><td>11908.0</td></tr><tr><td>146La</td><td>0.051</td><td>62.6</td><td>56.049</td><td>6.551</td><td>3721.8</td></tr><tr><td>148Ce 58</td><td>0.042</td><td>60.2</td><td>53.491</td><td>6.709</td><td>3144.7</td></tr><tr><td>SUM</td><td>1.969</td><td></td><td></td><td></td><td></td></tr></table>

iFPY-weighted sum of Frenkel pairs  14825.

The inhomogeneous chemical potentials of vacancy, gas atoms,and interstitials are assumed to be UV /kBT = [−2.eV/kBT]χ 2, UgkBT = [−2. eVk T ]χ 2, and UI/kBT = [2.eV/kBT ]χ 2 in the simulations. Biases coefficient of interstitial clusters Zi , the sink rate constant of grain boundaries Zsi,gb, t he emission rate constant Zei,bb, and the defect generation rate G are model parameters for studying their effect on gas bubble evolution. In the literature, some experimental reports exist on the effect of fission rates on gas bubble swelling in UMo dispersion fuels [43,44], but no relative results for UMo monolithic fuels. With the assumptions that Xe diffusivity, resolution and recrystallization kinetics are proportional to the fission rate, simulations show that the gas bubble swelling depends heavily on fission density, but weakly on fission rate [45]. Furthermore, considering the factors that 1) gas bubble swelling modeling in 3D is a computer time-consuming process and 2) the simulations will focus on parametric studies, we used a high fission rate 3.29 1022fissions/s/m3 to accelerate the simulation and save the computational cost.

## 3. Results

The simulations start from a polycrystalline structure with cylindrical grains and distributed gas bubbles as shown in Fig. 1. The simulation cell has dimensions of 128l0 128l0 32l0. The use of cylindrical grains is to save the simulation cost while capturing grain boundary effect. To solve the Eqs. (1)–(4),(10),(11), and (13), time, length, and energy are normalized by t∗ = t/(D0/l 20 ), x∗ = x/l0, and kBT, respectively. D0 is the largest diffusivity of Di, l0 is the characteristic length, and T is the absolute temperature.

The average grain size is about 300nm, which is similar to that observed in the recrystallization zone in UMo. The initial size distribution and density of gas bubbles are set to have the volumetric swelling 1.32% at fission density fd = 2.6 × 1027(fission/m3) to mimic the gas bubble microstructure just after the recrystallization. Besides the given model parameters and properties listed in Table 2, some thermodynamic and kinetic properties are unknown or have large uncertainty, f(e.g., the defect generation rate, clustering rate, and the defect emission rate).

In Section 2.5.1 the generation of Frenkel pairs per 235U fission in γ U is estimated at about 14,825. The MD method has been extensively used to simulate the defect evolution under energetic cascades in metals [46–48]. It is found that 1) most generated Frenkel pairs annihilate during a very short period (within a few ps), and 2) the NRT formula of 0.4∗Edamage/Ed overestimates the number of defects by a factor 3 \~ 4. For long time cascade defect aging up to tens ns, Object kinetic Monte Carlo (OkMC) simulations in tungsten show that the number of defects further decreases. The amount of reduced defects depends on PKA energy and temperature [49]. The generation rate of defects can be calculated by G˙ I = G˙ V = G ˙f0, where ˙f0 is the fission rate. G is the number of survived Frenkel pairs per fission during the simulation time increment t. G is a unknown model parameter.

Based on the MD and OkMC simulations of defect evolution G 1000 \~ 3000, which means less than 20% defects calculated by NRT formula survive, and this should be a safe estimation. The generation rate of gas atoms is calculated by G˙ g = 0.25 ˙f0, which means four fissions generate one gas atom. Emission, sink, and clustering rates of defects depend on the interaction energies among defects. The knowledge of the interaction energies in the UMo system is lacking. Therefore, parametric studies for the unknown model parameters are carried out in the simulations. Table 3 lists the model parameters used in the case studies.

Table 2  
Model parameters in the cluster dynamics model.
<table><tr><td>Parameter</td><td>Value</td><td>Parameter</td><td>Value</td></tr><tr><td>T</td><td>453K</td><td>ZIv</td><td>50</td></tr><tr><td>rat</td><td>1.5A</td><td>Z1, dis</td><td>1.25</td></tr><tr><td>Ω</td><td>2.1×10-29m²</td><td>Zv, dis</td><td>1.0</td></tr><tr><td>a</td><td>3.48A</td><td>M</td><td>30</td></tr><tr><td>Dv</td><td>1.83× 10-19m²/s</td><td>Mv</td><td>10</td></tr><tr><td>D</td><td>1.42 ×10-18m²/s</td><td></td><td>0.8eV</td></tr><tr><td>Dg</td><td>1.83×10-20m²/s</td><td></td><td>0.5eV</td></tr><tr><td>Pdiso</td><td>1.0 × 1014m-2</td><td></td><td>1.61eV</td></tr><tr><td></td><td>0.7eV</td><td>时比臨</td><td>0.5eV</td></tr><tr><td></td><td>0.8eV</td><td>0</td><td>1.0j/m²</td></tr><tr><td>Do</td><td>1.42 ×10-18m²/s</td><td>l</td><td>12nm</td></tr><tr><td>fo</td><td>3.29 × 10²2fission/s/m</td><td>入</td><td>36nm</td></tr><tr><td>Am</td><td>10.75kgT</td><td>Abv</td><td>0.91kgT</td></tr><tr><td>Abb</td><td>0.91kgT</td><td>△t</td><td>0.101s</td></tr><tr><td>h</td><td>2</td><td>Zj</td><td>1.0</td></tr><tr><td>Zij</td><td>1.25</td><td>Zj</td><td>42</td></tr></table>

Table 3

Model parameters used in the case studies.
<table><tr><td>Cases</td><td>G</td><td>Yigb</td><td>Y.bb</td><td>2</td></tr><tr><td>Defect generation rate</td><td>1000 2000</td><td>3.0</td><td>0.08</td><td>2.4</td></tr><tr><td>Interstitial emission rate</td><td>3000 3000</td><td>3.0</td><td>0.05 0.06</td><td>2.4</td></tr><tr><td>Defect sink rate</td><td>3000</td><td>0.1 0.3 1.0</td><td>0.08 0.10 0.08</td><td>2.4</td></tr><tr><td>Defect clustering rate</td><td>3000</td><td>3.0 3.0</td><td>0.08</td><td>0.6 1.2 2.4 3.6</td></tr></table>

## 3.1. Effect of defect generation rate on gas bubble swelling

For a given generation rate, G ˙f0, of Frenkel pairs per fission with G = 2000 and the rest of the parameters shown in the first row in Table 3, the evolution of CgV(x, t), the concentrations of interstitial CI(x, t), vacancy CV(x, t), and total concentration of gas atoms Cg(x, t ) + Cgg(x, t ) on the plane A shown in Fig. 1(a) are presented in Fig. 3(a-d), respectively. The gray color in Fig. 3(a) represents grain boundaries, which shows the iso-surface of η(x, t ) 0.5. Light blue shows the iso-surface of vacancy concentration, CgV(x, t ) = 0.5, representing gas bubbles. The color bar in Fig. 3(ad) presents the concentration of defects. The change in gas bubble number and size show the nucleation, growth, and coalescing of gas bubbles. Concentrations CI(x, t) and CV(x, t) in the matrix are not uniform. Interstitial concentration in the interior of grains increases, then decreases, while vacancy concentration increases with time. Both CI(x, t) and CV(x, t) inside gas bubbles are almost zero because they recombine with vacancies CgV(x, t). The white circles show the interface of gas bubbles. It can be seen that there is a depletion zone of interstitials and vacancies near the gas bubbles. Inside gas bubble CgV(x, t) is equal to 1 and gas atom concentration Cgg(x, t) has a general tendency to decrease with time. The color shows that the largest Cgg(x, t) is about 0.8, which is associated with the nucleation stage of gas bubbles. Cgg(x, t) in large gas bubbles is also smaller than that inside small gas bubbles. These results demonstrated that the developed model reasonably captures the defect-gas bubble associated growth in UMo fuels (i.e., dynamic interaction between evolving gas bubbles (sinks) and defects).

The gas bubble swelling is calculated by

$$
\tag{16}
$$

where the integration is over the simulation cell, and V is the volume of simulation cell. The effect of defect generation rates on gas bubble swelling is plotted in Fig. 4. The experimental data points [1] are shown by red circles in Fig. 4. As expected, the gas bubble swelling kinetics increase as the generation rate of Frenkel pairs per fission increases because there are more vacancies available for gas bubble growth. However, the predicted gas bubble swelling kinetics are much slower than measured swelling kinetics, even using a large defect generation rate (3000 Frenkel pairs per fission). Although the swelling kinetics may reach the experimental data as the defect generation rate further increases, 3000 Frenkel pairs generation rate corresponds to 20% defect survive of defects calculated by NRT formula, which is a high surviving rate after 0.1 second aging according to MD and OkMC simulations [46,50]. Therefore, other thermodynamic and kinetics might play an important role in gas bubble swelling in the recrystallization zone.

![](images/f95edc0883500ad12a471c9f3ce35f5abce58cf64acb816e66334f0086b767e0.jpg)

![](images/8da993a2cdc4192aa055068bd0f2f2e1b81a9b86d822ff231a1b7a507cfea43b.jpg)

![](images/eb092c9abba8578d5245b6e89acb1951ec26227217f3d2b4b5eebc53264b32ca.jpg)

![](images/4ccc6388ca26ddbf2d89b6044902c5755c2b6e680b6a289a52622b23e7f005b8.jpg)

![](images/558fcf1d1e302b12d8b9910821e5826b8da83f506e1bb31cbae305cf979b699d.jpg)

![](images/4d43f618af7cc5f805e049dec33b6a11f876379d504427a93f57553de96d9eec.jpg)

![](images/366d55398b1ad4e7eae32d02779bff49afedae40fae126f13e9870f2c2a1593a.jpg)

![](images/69fa933811d7141f346fb496f944a509cb98494cc1ac13a1d5ff9e6624be91d3.jpg)

![](images/58a80a2805da5500146df67ef3cd7a14a1b2334c1880d92ff15650958dcfaf03.jpg)

![](images/02b797401ee9602c5678398914538a9ef000e42d7e14b3e0fd6d95bed05511f8.jpg)

![](images/751b339f05bb79496c7524c3a83ea518f056587585987b3dc49528c49f11ffa5.jpg)

![](images/3f6012bd0fccb385afc01088ebe9be529c76bf383066ba6458680db3e09dfa22.jpg)  
Fig. 3. Evolution of defects and gas bubble. (a) gas bubble CgV(x, t), (b) interstitials CI(x, t), (c) vacancy CV(x, t) and (d) gas atom Cg(x, t ) + Cgg (x, t ). fd is the fission density (fission/m3).

## 3.2. Effect of interstitial emission rate on gas bubble swelling

The normalized emission rate is described as

$$
\tag{17}
$$

The interface of gas bubbles is a two dimensional (2D) sink. In the simulations the interface thickness H0 which is defined by θ 1(ηm, χ ) > 0 is equal to l0. l0 is the grid size of simulation cell. In reality, defects emit from a very thin interface layer. The layer thickness is about the lattice constant a. So the average bias Y ei,de f has a scale factor H0/a for 3D sink, and a scale factor (H0/a)2 for a one dimensional (1D) sink such as dislocations and interstitial loops. Fig. 5 shows the effect of interstitial emission rate or the bias Y ei,bb on gas bubble swelling. Increasing the emission rate results in more emission of interstitials from the gas bubble interface. As a result, the interstitial concentration near the gas bubble decreases with the increase of Y ei,bb, and less vacancies are recombined with interstitials, hence, increasing the vacancy absorption by gas bubbles, the gas bubble growth, and swelling kinetics. When Y ei,bb reaches 0.08, further increasing Y ei,bb does not affect the swelling kinetics. It indicates that all interstitials arriving at gas bubbles are emitted and the interstitials have an equilibrium concentration near the gas bubbles. The results show that for the given model parameters listed in the second row in Table 3, increasing the interstitial emission rate on gas bubble interface could not produce the measured swelling kinetics.

![](images/be864f661833875eae684563ebd808c3d6bdaf8f35e51ba1a5b32b4a7a8ec456.jpg)  
Fig. 4. Effect of defect generation rates on gas bubble swelling.

![](images/269a158fde49d036c458a0aebe44935f378ea97efb08569a147ef17dd7424626.jpg)  
Fig. 5. Effect of interstitial emission rate from gas bubbles on gas bubble swelling.

## 3.3. Effect of interstitial and vacancy sink rates on gas bubble swelling

Interstitial and vacancy sink to grain boundaries. The normalized sink rate is calculated by

$$
\tag{18}
$$

Fig. 6 shows the effect of sink rate at grain boundaries on gas bubble swelling. It is interesting to find that that when Y s i,gb < 1.0 the gas bubble swelling kinetics is independent of Y s . But the gas i,gb bubble swelling kinetics deviate from measured swelling kinetics with the increase of the sink rate Y Si,gb. Therefore, adjusting the sink rate on grain boundaries could not produce the measured gas bubble swelling kinetics.

Interstitials and vacancies sinking to grain boundaries change their concentrations on grain boundaries as well as in matrix. We assume that interstitials and vacancies on grain boundaries recombine immediately. Thus, if more interstitials than vacancies are absorbed by grain boundaries, it leads to grain growth. In contrast, if more vacancies than interstitials are absorbed by grain boundaries, that may result in the formation of voids. The defect concentration absorbed by grain boundaries can be calculated by

![](images/4e79f4207648937d4889326b05dfed61008f115adfa259757b00a08023bb49a5.jpg)  
Fig. 6. Effect of interstitial and vacancy sink rate on grain boundaries on gas bubble swelling.

$$
\tag{19}
$$

where t is the time.

Fig. 7(a) shows the distribution of cIV,gb on the plane A for the case Y S 3.0 at fission density fd 8.04E  27(fission/m3). It can i,gb be seen that cIV,gb on grain boundaries is larger than zero. A positive value of cIV,gb means that more interstitials than vacancies are absorbed by grain boundaries. The effect of sink rates on cIV,gb along the line AA’ on the plane A are plotted in Fig. 7(b). Since the sink rate S˙ i,gb is proportional to the diffusivity Di, it is understandable that cIV,gb increases with the increase of S˙ i,gb. As more interstitials sink to dislocations and grain boundaries, it is expected that more vacancies are left in the matrix. A high vacancy concentration should speed up the gas bubble swelling.

The results in Fig. 6 show an opposite tendency. Notice that the sink rate S˙ i,gb is also proportional to local defect concentration ci(x, t ) − Ceq1 . In the matrix, vacancy concentration is much higher i,gbthan that of interstitials. Increasing sink rate coefficient Y Si,gb also increases the sink strength of vacancies on the grain boundaries. As a consequence, both interstitial and vacancy concentrations in the matrix decrease with the increase of sink rate coefficient Y S i,gb The decrease of the gas bubble swelling kinetics shown in Fig. 7 is attributed to the decreasing vacancy concentration.

## 3.4. Effect of interstitial clustering on gas bubble swelling

Interstitials and vacancies form clusters which reduce the concentrations of mobile vacancies and interstitials in the matrix. As a result, the defect clustering affects the gas bubble nucleation and growth. The capture coefficients of clusters depend on the interaction energy between defect i and defect cluster lj. Assuming that vacancy and interstitial clusters has a spherical and a loop shape, respectively, the normalized capture coefficients of mobile defect i by defect cluster lj are calculated by

$$
\tag{20}
$$

![](images/ca579ac3f9a424e6e8d7114249fb9a2753e254703467a85a63185ec2dbc0525e.jpg)  
(a)

![](images/b3d87da9b9471e90cc9bc25fb0e1da24777fef72e72f63b530ac000acd68ef3d.jpg)  
(b)

Fig. 7. (a) concentration cIV,gb of interstitial and vacancy absorbed on grain boundaries, and effect of sink rate coefficient on cIV,gb along the AA’ line shown in Fig. 7(a).  
![](images/72514dac9608bf1b9e544a0faa0954e34e7ee83033dbfab45d09f66f9b336f79.jpg)  
Fig. 8. Effect of interstitial and vacancy clustering rate on gas bubble swelling.

$$
\tag{21}
$$

where Z0l j is a scale value of bias coefficient Zil j. The parameters Zvlj, Zilj, and Z lj [26] are listed in Table 2. Vacancy clusters are 2D sinks. Interstitial loops are 1D sinks. To calculate their capture coefficients Kl j∗v (m) and Kl j∗ (m), scale factors H0/a and (H0/a)2 should be applied, respectively. The effect of bias coefficient Z0l jZil j of clusters on swelling kinetics is plotted in Fig. 8. It can be seen that with the increase of Z0lj , the gas bubble swelling kinetics increases and converges to measured swelling kinetics. If the interstitial clusters have a large clustering rate or growth rate, the predicted gas bubble swelling kinetics is in agreement with the measured swelling kinetics. Compared the effect of other thermodynamic and kinetic properties on the swelling kinetics, we conclude that the defect clustering plays an important role in fast gas bubble swelling kinetics in recrystallization zone in UMo fuels.

Fig. 9a, b, and c show the temporal evolution of gas bubble structures including gas bubble density, average gas bubble size, and average ratio of Xe and vacancy inside the gas bubbles, respectively. In Fig. 9a, it can be seen that the gas bubble density increases due to the gas bubble nucleation, and then decreases with gas bubble coalescence as the fission density increases. Experiments show a wide distribution of gas bubble size (100nm \~ 300nm) [2]. This implies gas bubble nucleation and coalescence take place. Fig. 9b shows that the average gas bubble size increases with the fission density increase. The drop of average gas bubble size around fd = 3.0 × 1027(fissions/m3) is because of rapid increase of gas bubble density associated with gas bubble nucleation. For different defect clustering rates, the average gas bubble size at high fission density has a slight difference. The predicted average gas bubble sizes, about 160nm at fd = 7.0 × 1027(fissions/m3), is in reasonable agreement with the average intergranular gas bubble size [2]. Fig. 9c shows the average Xe concentration inside the gas bubbles. The Xe concentration is the same as the ratio of Xe and vacancy inside the gas bubbles. It is clear that average Xe concentration inside the gas bubble is much lower than the equilibrium value (0.45), and decreases with the increase of fission density as well as the increase of clustering rate. The average ratio of Xe and vacancy inside gas bubbles is about 1:10 at fd = 7.0 × 1027(fissions/m3). It implies that the gas bubbles become voids. All the information of gas bubble structure evolution can be extracted from the simulations. However, systematic experimental results of gas bubble structure evolution are required to validate the model.

Gas bubble swelling is calculated by Eq. (16), which should be equivalent to the volume increase associated with absorbed interstitials induced grain growth, the formation of interstitial and vacancy clusters, and dislocation climb by absorbing defects. The absorbed interstitials on grain boundaries shown in Fig. 7(a) have a concentration that is much higher than thermal equilibrium concentration. If the absorbed interstitials cause grain growth, the volumetric swelling associated with the grain growth can be calculated by integrating the absorbed interstitial on the gain boundary. Fig. 10 shows the effect of sink rates and clustering rates on grain growth-induced swelling. It is found that the swelling rate associated with grain growth gradually reach zero for all cases. This means that absorbed interstitials decrease with the fission density increase or the increase of gas bubble and interstitial density. For the cases that predicted gas bubble swelling kinetics in agreement with experiment (Z0l j > 2.4), the total swelling associated with grain growth is less than 0.002, which is much smaller than gas bubble swelling (0.25 at fd = 7.0 × 1027(fissions/m3)). Therefore in the recrystallization zone, grain growth-induced the volumetric swelling is negligible compared with volumetric swelling associated with gas bubble and interstitial clustering. In other words, the defect clustering is one of main mechanisms that results in a fast gas bubble swelling kinetics in the recrystallization zone.

![](images/aa550ec6d96b3ee9a8bc4e327e7bb3d8283f4f2c8de395ebb5901afa79479724.jpg)  
(a)

![](images/ea72cf1ad5b676729df6c8307c365cdb30922ea7b549e3dab085a38a0acdaeb3.jpg)  
(b)

![](images/c0ea2d881aefe0dd3dbdafc2d9cdd2df7056a3117f4e7faf88b2aa9961eb1eec.jpg)  
（c）

Fig. 9. Evolution of gas bubble structures for different clustering rates. (a) gas bubble density, (b) average gas bubble size in diameter, and (c) the average ratio of Xe and vacancy inside the gas bubbles.  
![](images/f9a9803cb29736f8d8b172f26e05be196edc63c05c87a389076e0276a244f291.jpg)  
(a)

![](images/35d0af337c3e960e9ac4df00f7af63b8459dd5b3cbb89d9868af066296ae70b4.jpg)  
(b)  
Fig. 10. Effect of defect kinetic properties on swelling associated with grain growth. (a) defect sink rate coefficient Y Si,gb on grain boundaries, and (b) defect clustering rate coefficient Z0l j

## 4. Conclusions

For the first time, we developed a mesoscale model of defect cluster and nonequilibrium gas bubble associated growth by integrating phase-field and cluster dynamics approaches for investigating the effect of defect clustering on gas bubble swelling in polycrystalline UMo under irradiation. With the model, the effect of defect generation rate, clustering rate, interstitial emission and sink rates on gas bubble evolution were systematically simulated. We found that 1) gas bubble swelling kinetics increases with the increase of defect generation rate, interstitial emission rate from gas bubble interfaces, and defect clustering rate, but decreases with the increase of defect sink rate on grain boundaries; 2) swelling associated with grain growth is negligible compared with gas bubble swelling; and 3) compared with the sink and emission of defects from grain boundaries and interfaces, interstitial clustering and growth is the key mechanism for the rapid gas bubble growth observed in irradiated UMo.

From the simulations a set of model parameters is determined, i.e., G 3000, Y s b = 1.0, Y ei,bb = 0.08, and Z0l j = 2.4. With this set of i,g i,bb   
model parameters, predicted gas bubble swelling kinetics in the recrystallization zone is in good agreement with the experimental results. The evolution of gas bubble structures including gas bubble density, gas bubble size, and the ratio of Xe and vacancy inside gas bubble are also analyzed. The gas bubble structures are in reasonable agreement with existing experimental data. However, the model is based on assumptions of interstitial clustering and random gas bubble distribution in the recrystallization zone. Experimental results including the stability of nano-sized intragranular gas bubbles, large gas bubble spatial distribution, and the stability and evolution of interstitial loops in recrystallization zone are required to validate these assumptions. The simulations were accelerated by using a very high fission rate (3.29 1022 fissions/m3) in order to reach the fuel operation time (several months) and total fission density (7.5  1027 fissions/m3). To increase simulation time step, which enables one to use a low fission rate (\~ 5 × 1020 fissions/m3), an efficient approach should be developed to deal with the fast interstitial diffusion. Rate theory modeling shows that the increase of resolution rate (which is proportional to the fission rate) decreases the gas bubble swelling kinetics while the increase of fission rate increases the swelling kinetics [45]. Therefore, we

need to further improve the model to handle the fast diffusion of interstitials and take the gas atom resolution into account. In addition, more systematic and consistent experimental data including the effect of grain size and morphology, fission rate, and 235U inhomogeneity on gas bubble structures and swelling kinetics are required for validating the model.

In summary, the simulations demonstrate the capability of the developed model to study the effect of thermodynamic and kinetic properties on defect cluster and gas bubble associated growth, gas bubble structure evolution, and gas bubble swelling kinetics in polycrystalline UMo, and explore the swelling mechanisms. Defect and second-phase-precipitate-associated growth are often observed in irradiated materials. For example, voids form and grow on evolving precipitates. The developed model can be extended to study defect and second-phase-precipitate associated growth in irradiated materials.

## Declaration of Competing Interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

## Acknowledgement

This work was supported by the U.S. Department of Energy, National Nuclear Security Administration Office of Material Management and Minimization, under DE-AC07-05ID14517. Pacific Northwest National Laboratory is a multiprogram national laboratory operated by Battelle Memorial Institute for the U.S. Department of Energy under DE-AC05-76RL01830. Computations were performed on the Constance cluster at Pacific Northwest National Laboratory.

## Supplementary materials

Supplementary material associated with this article can be found, in the online version, at doi:10.1016/j.jnucmat.2020.152441.

## References

[1] Y.S. Kim, G.L. Hofman, Fission product induced swelling of U-Mo alloy fuel, J. Nucl. Mater. 419 (1-3) (2011) 291–301.

[2] J. Rest, Evolution of fission-gas-bubble-size distribution in recrystallized U-10Mo nuclear fuel, J. Nucl. Mater. 407 (1) (2010) 55–58.

[3] M. Meyer, B. Rabin, J. Cole, I. Glagolenko, W. Jones, J.-F. Jue, D.K. Jr., C. Miller, G. Moore, H. Ozaltun, F. Rice, A. Robinson, J. Smith, D. Wachs, W. Williams, N. Woolstenhulme, Preliminary Report on U-Mo Monolithic Fuel for Research Reactors, 2017.

[4] M.K. Meyer, J. Gan, J.F. Jue, D.D. Keiser, E. Perez, A. Robinson, D.M. Wachs, N. Woolstenhulme, G.L. Hofman, Y.S. Kim, Irradiation Performance of U-Mo Monolithic Fuel, Nucl. Eng. Technol. 46 (2) (2014) 169–182.

[5] Y.S. Kim, G.L. Hofman, J.S. Cheon, Recrystallization and fission-gas-bubble swelling of U-Mo fuel, J. Nucl. Mater. 436 (1-3) (2013) 14–22.

[6] S.Y. Hu, D. Burkes, C.A. Lavender, V. Joshi, Effect of grain morphology on gas bubble swelling in UMo fuels - A 3D microstructure dependent Booth model, J. Nucl. Mater. 480 (2016) 323–331.

[7] J. Gan, D.D. Keiser, B.D. Miller, A.B. Robinson, D.M. Wachs, M.K. Meyer, Thermal stability of fission gas bubble superlattice in irradiated U-10Mo fuel, J. Nucl. Mater. 464 (2015) 1–5.

[8] J. Gan, B.D. Miller, D.D. Keiser, J.F. Jue, J.W. Madden, A.B. Robinson, H. Ozaltun, G. Moore, M.K. Meyer, Irradiated microstructure of U-10Mo monolithic fuel plate at very high fission density, J. Nucl. Mater. 492 (2017) 195–203.

[9] S.Y. Hu, D.E. Burkes, C.A. Lavender, D.J. Senor, W. Setyawan, Z.J. Xu, Formation mechanism of gas bubble superlattice in UMo metal fuels: Phase-field modeling investigation, J. Nucl. Mater. 479 (2016) 202–215.

[10] H.X. Xiao, C.S. Long, X.F. Tian, S.J. Li, Atomistic simulations of the small xenon bubble behavior in U-Mo alloy, Mater. Des. 74 (2015) 55–60.

[11] S.Y. Hu, W. Setyawan, V.V. Joshi, C.A. Lavender, Atomistic simulations of thermodynamic properties of Xe gas bubbles in U10Mo fuels, J. Nucl. Mater. 490 (2017) 49–58.

[12] Y.B. Miao, K. Mo, B. Ye, L. Jamison, Z.G. Mei, J. Gan, B. Miller, J. Madden, J.S. Park, J. Almer, S. Bhattacharya, Y.S. Kim, G.L. Hofman, A.M. Yacout, High-energy synchrotron study of in-pile-irradiated U-Mo fuels, Scr. Mater. 114 (2016) 146–150.

[13] L.Q. Chen, Phase-field models for microstructure evolution, Annu. Rev. Mater. Res. 32 (2002) 113–140.

[14] Y.L. Li, S.Y. Hu, X. Sun, M. Stan, A review: applications of the phase field method in predicting microstructure and property evolution of irradiated nuclear materials, npj Comput. Mater. 3 (2017), doi:10.1038/s41524-017-0018-y.

[15] P.J. Maziasz, C.J. Mchargue, Microstructural evolution in annealed austenitic steels during neutron-irradiation, Int. Mater. Rev. 32 (4) (1987) 190–219.

[16] A.D. Brailsford, R. Bullough, Rate theory of swelling due to void growth in irradiated metals, J. Nucl. Mater. 44 (2) (1972) 121 +.

[17] G.R. Odette, R.E. Stoller, A theoretical assessment of the effect of microchemical, microstructural and environmental mechanisms on swelling incubation in austenitic stainless-steels, J. Nucl. Mater. 122 (1-3) (1984) 514–519.

[18] L.K. Mansur, Theoretical evaluation of a mechanism of precipitate-enhanced cavity swelling during irradiation, Philos. Mag. A 44 (4) (1981) 867–877.

[19] H.R. Brager, J.L. Straalsund, Defect development in neutron-irradiated type-316 stainless-steel, J. Nucl. Mater. 46 (2) (1973) 134–158.

[20] L.K. Mansur, Theory and experimental background on dimensional changes in irradiated alloys, J. Nucl. Mater. 216 (1994) 97–123.

[21] D. Brimbal, L. Fournier, A. Barbu, Cluster dynamics modeling of the effect of high dose irradiation and helium on the microstructure of austenitic stainless steels, J. Nucl. Mater. 468 (2016) 124–139.

[22] A.A. Kohnert, B.D. Wirth, Cluster dynamics models of irradiation damage accumulation in ferritic iron. II. Effects of reaction dimensionality, J. Appl. Phys. 117 (15) (2015).

[23] A.A. Kohnert, B.D. Wirth, L. Capolungo, Modeling microstructural evolution in irradiated materials with cluster dynamics methods: A review, Comp. Mater. Sci. 149 (2018) 442–459.

[24] R.E. Stoller, Modeling dislocation evolution in irradiated alloys, Metallur. Trans. A 21 (7) (1990) 1829–1837.

[25] J. Bardeen, C. Herring, John Wiley and Sons, Inc, New York, 1952, p. 261.

[26] A.H. Duparc, C. Moingeon, N. Smetniansky-de-Grande, A. Barbu, Microstructure modelling of ferritic alloys under high flux 1 MeV electron irradiations, J. Nucl. Mater. 302 (2-3) (2002) 143–155.

[27] G.S. Was, Fundamentals of Radiation Materials Science, Metal and Alloys, Springer, New York, 2007.

[28] T.S. Duh, J.J. Kai, F.R. Chen, L.H. Wang, Numerical simulation modeling on the effects of grain boundary misorientation on radiation-induced solute segregation in 304 austenitic stainless steels, J. Nucl. Mater. 294 (3) (2001) 267–273.

[29] L.D. Xia, Y.Z. Ji, W.B. Liu, H. Chen, Z.G. Yang, C. Zhang, L.Q. Chen, Radiation induced grain boundary segregation in ferritic/martensitic steels, Nucl. Eng. Technol. 52 (1) (2020) 148–154.

[30] S.G. Kim, W.T. Kim, T. Suzuki, Phase-field model for binary alloys, Phys. Rev. E 60 (6) (1999) 7186–7197.

[31] W. Setyawan, M.W.D. Cooper, K.J. Roche, R.J. Kurtz, B.P. Uberuaga, D.A. Andersson, B.D. Wirth, Atomistic model of xenon gas bubble re-solution rate due to thermal spike in uranium oxide, J. Appl. Phys. 124 (7) (2018).

[32] c. Xoubi, R.T. Primm III, Modeling of the high flux isotope reactor cycle 400, ORNL/TM-2004/251, Technical Report (1996) http://www.osti.gov/bridge.

[34] M.J. Norgett, M.T. Robinson, I.M. Torrens, Proposed method of calculating displacement dose-rates, Nucl. Eng. Des. 33 (1) (1975) 50–54.

[35] B. Beeler, B. Good, S. Rashkeev, C. Deo, M. Baskes, M. Okuniewski, First principles calculations for defects in U, J. Phys. Condens. Matter 22 (50) (2010) 1–7.

[36] B. Beeler, C. Deo, M. Baskes, M. Okuniewski, First principles calculations of the structure and elastic constants of alpha, beta and gamma uranium, J. Nucl. Mater. 433 (1-3) (2013) 143–151.

[37] K.R. Lund, K.G. Lynn, M.H. Weber, M.A. Okuniewski, Vacancy formation enthalpy in polycrystalline depleted uranium, 16th international conference on positron annihilation (Icpa-16) 443 (2013).

[38] D.E. Smirnova, A.Y. Kuksin, S.V. Starikov, V.V. Stegailov, Atomistic modeling of the self-diffusion in gamma-U and gamma-U-Mo, Phys. Met. Metallogr. 116 (5) (2015) 445–455.

[39] S.J. Rothman, L.T. Lloyd, A.L. Harkness, Self-diffusion in gamma uranium, Trans. Am. I Min. Met. Eng. 218 (4) (1960) 605–607.

[40] Y. Adda, A. Kirianenko, Abaissement des coefficients dautodiffusion de luranium en phase-gamma par des additions de molybdene, de zirconium ou de niobium, J. Nucl. Mater. 6 (1) (1962) 135–136.

[41] K. Huang, D.D. Keiser, Y.H. Sohn, Interdiffusion, Intrinsic Diffusion, Atomic Mobility, and Vacancy Wind Effect in gamma(bcc) Uranium-Molybdenum Alloy, Metall. Mater. Trans. A 44A (2) (2013) 738–746.

[42] J.H. Ke, H.B. Ke, G.R. Odette, D. Morgan, Cluster dynamics modeling of Mn-Ni-Si precipitates in ferritic-martensitic steel under irradiation, J. Nucl. Mater. 498 (2018) 83–88.

[43] A. Leenaers, Y. Parthoens, G. Cornelis, V. Kuzminov, E. Koonen, S. Van den Berghe, B. Ye, G.L. Hofman, J. Schulthess, Effect of fission rate on the microstructure of coated UMo dispersion fuel, J. Nucl. Mater. 494 (2017) 10–19.

[44] A. Leenaers, W. Van Renterghem, S. Van den Berghe, High burn-up structure of U(Mo) dispersion fuel, J. Nucl. Mater. 476 (2016) 218–230.

[45] B. Beelera, J. Colea, W. Frazierb, Y. Gao, I. Glagolenkoa, G. Hofmanc, S.Y. Hu, V. Joshib, C. Lavendar, N. Lombardob, Z.G. Mei, G. Parkd, K. Vernere, A. Ya-

coutc, B. Ye, Y.F. Zhang, Microstructural-level fuel performance modeling of U-Mo monolithic fuel, INL Sci. Rep. (2019).

[46] K. Nordlund, S.J. Zinkle, A.E. Sand, F. Granberg, R.S. Averback, R. Stoller, T. Suzudo, L. Malerba, F. Banhart, W.J. Weber, F. Willaime, S.L. Dudarev, D. Simeone, Improving atomic displacement and replacement calculations with physically realistic damage models, Nat. Commun. (2018) 9.

[47] C. Bjorkas, K. Nordlund, Comparative study of cascade damage in Fe simulated with recent potentials, Nucl. Instrum. Meth. B 259 (2) (2007) 853–860.

[48] C. Bjorkas, K. Nordlund, S. Dudarev, Modelling radiation effects using the ab-initio based tungsten and vanadium potentials, Nucl. Instrum. Meth. B 267 (18) (2009) 3204–3208.

[49] G. Nandipati, W. Setyawan, H.L. Heinisch, K.J. Roche, R.J. Kurtz, B.D. Wirth, Displacement cascades and defect annealing in tungsten, Part II: Object kinetic Monte Carlo simulation of tungsten cascade aging, J. Nucl. Mater. 462 (2015) 338–344.

[50] G. Nandipati, W. Setyawan, H.L. Heinisch, K.J. Roche, R.J. Kurtz, B.D. Wirth, Displacement cascades and defect annealing in tungsten, Part III: The sensitivity of cascade annealing in tungsten to the values of kinetic parameters, J. Nucl. Mater. 462 (2015) 345–353.
