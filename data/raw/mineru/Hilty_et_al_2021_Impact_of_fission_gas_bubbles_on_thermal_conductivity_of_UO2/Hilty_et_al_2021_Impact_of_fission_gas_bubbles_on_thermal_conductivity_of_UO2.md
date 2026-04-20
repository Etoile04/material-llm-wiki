# 📄 PDF Parsing Result

**File:** `/Volumes/openclaw记忆/Zotero_storage/storage/6PCNHZZK/Hilty et al. - 2021 - Impact of fission gas bubbles on thermal conductivity of UO2.pdf`
**Backend:** `pipeline`
**Pages:** 0 to end
**Formula Recognition:** ❌ Disabled
**Table Recognition:** ✅ Enabled

---

# Impact of fission gas bubbles on thermal conductivity of UO2 fuels with high thermal conductivity additives

![](images/9cb30035928455807fa91460b973b58a09460aab50c98252db633bb5e9a9e805.jpg)

Floyd W. Hilty, Dong-Uk Kim, Michael R. Tonks∗

Department of Materials Science and Engineering, University of Florida, Gainesville FL 32611 United States

## a r t i c l e i n f o

Article history:   
Received 29 July 2020   
Revised 1 December 2020   
Accepted 4 January 2021   
Available online 7 January 2021

Keywords:   
Fission gas bubbles   
UO2   
High thermal conductivity additives

## a b s t r a c t

High thermal conductivity additives are being considered to create composite nuclear fuels with a higher effective thermal conductivity (ETC) to reduce the peak fuel temperatures during reactor operation. However, the benefits of the additive may be reduced, or possibly eliminated, when placed into a reactor environment. In this work, we investigate the impact of fission gas bubbles on the ETC of composite fuels. We create 2D simulations representing a small portion of a composite UO2 fuel containing a single additive particle and calculate the ETC with various volume fractions of fission gas bubbles. Our results show that fission gas bubbles, depending on the volume fraction and contact angle at the additive interface, can completely remove any benefit of the additive and even result in a lower thermal conductivity than in UO2 without the additive. We also expose a trend that relates the fraction of additive that is screened by bubbles to the ETC. We then propose a model which predicts the ETC of a composite fuel with fission gas bubbles to better estimate the benefits of a novel fuel design.

© 2021 Elsevier B.V. All rights reserved.

## 1. Introduction

There is a push to create a new generation of accident tolerant nuclear fuels [1]. The goal of these fuels are to reduce the probability and severity of accidents and to improve reactor efficiency. One area of focus in this search is the incorporation of high thermal conductivity additives in traditional UO2 fuels. These new composites have a higher effective thermal conductivity (ETC), allowing for more efficient heat extraction from the fuel and greater power generation. Many different types of additives have been used, as summarized by Zhou and Zhou [2], including beryllium oxide (BeO) [3], silicon carbide (SiC) [4], diamond [5], molybdenum [6], tungsten [7], carbon nanotubes [8], and graphene [9]. Uranium-bearing additives, including UN [10] and U3Si2 [11], have also been suggested; they have the dual benefits of increasing the thermal conductivity and the uranium density.

Modeling and simulation have been used to estimate the improvement in the ETC from the additives and to assess their impact on the fuel performance. Finite element models have been developed to predict the increase in the thermal conductivity for a given additive and microstructure [12–14]. In addition, we have developed an efficient thermal resistor model that has also been used to provide guidance on how to tailor the composite microstructure to maximize the impact of the additive [15]. Fuel performance simulations have been carried out for the composite fuel in which they use the increased thermal conductivity and decreased uranium density. They have shown performance improvements during normal and accident conditions [16–21].

However, there are complicating factors in a reactor environment. Radiation can cause some additives to react with the fuel and become unstable [22]. Even if an additive is stable under irradiation, the production of fission gas bubbles could reduce the thermal conductivity benefit of the additive. Fission gas, primarily composed of xenon (Xe) and krypton, has a low thermal conductivity and segregates to interfaces such as grain boundaries [23,24]. If fission gas bubbles were to form at the fuel/additive interface, they could form a thermal barrier around the additive, effectively screening it and dampening its thermal benefits to the composite. Since no microstructure characterization has been carried out on irradiated composite fuels with significant fission gas content, the interaction between the additive and fission gas bubbles is still uncertain. All fuel performance simulations that include the impact of high thermal conductivity additives [16–21] assume that the additives do not alter any of the other fuel behaviors, including the fission gas behavior.

In this work, we use 2D mesoscale simulation to provide a preliminary picture of the possible impact of fission gas bubbles on the thermal conductivity of composite fuel. A small portion of a composite fuel microstructure is represented, containing a single additive particle and fission gas bubbles with varying volume fractions, contact angles, and additive particle shapes. The ETC for each microstructure is calculated, in order to systematically investigate the impact of fission gas as a function of the bubble structure, showing that for certain bubble geometries, the composite fuel can be even worse than in standard UO2. Our computational methodology is summarized in Section 2, starting with the creation of the bubble structure and ending with the method for calculating the ETC. In Section 3, we demonstrate the impact of fission gas on the ETC of the composite. Section 4 outlines the effectiveness of four metrics used to describe the relationship between the ETC of the composite and the fission gas bubble’s morphology and position with respect to the additive. An analytical model is proposed in Section 5 to predict the ETC of a composite fuel at burn-up and then it is tested against systems not used in the development of the model. In Section 6, we discuss the possible limitations and implications of this model. Finally, we conclude our work in Section 7.

## 2. Methodology and numerical approach

Manufacturing and then irradiating UO2 composite fuels is extremely costly and time consuming. For this reason, there is a lack of experimental data that characterizes the evolution of the fuel microstructure and properties during reactor operation. Therefore, we use simulation to provide a preliminary view of the change in the ETC of composite fuel due to the formation and growth of fission gas bubbles. However, to determine the ETC, we first need a means of creating a pool of simulated microstructures for use in this study. This method and the resulting simulated microstructures are outlined in Section 2.1. In Section 2.2, we describe the method used to calculate the ETC of each of the simulated microstructures.

## 2.1. Microstructure simulations

In order to determine the impact of fission gas bubbles on the thermal conductivity of a composite fuel, we need to represent microstructures with fuel, additive, and gas bubbles. Composite fuel microstructures can be summarized into two primary categories, those with isolated particles distributed throughout the UO2 and those with more continuous additive coating the grain boundaries. In this work, we focused on the isolated additive particles, since they are more common and are easier to manufacture. For nonuranium-bearing additives, it is desirable to keep the additive volume fraction small, since it decreases the overall uranium density of the fuel. Thus, additive particles are often isolated from other additive particles, though having a more continuous path of additive in the direction of heat transport does lead to higher thermal conductivity as shown in our previous work [15]. To simplify our analysis, we modeled a single isolated additive particle within a UO2 matrix, and we considered both spherical and rectangular particles. We represented the particle in 2D to further simplify the analysis.

The impact of fission gas bubbles on the thermal conductivity of composite fuel depends on the shape of the bubbles that form on the surface of the additive. That shape is determined by the energy of each unique interface created: additive-UO2, gas-additive, and gas-UO2. The fission gas bubble will adopt a shape that minimizes the total energy of the system by reducing the amount of high energy interfaces in favor of low energy interfaces. A low contact angle means the gas bubble readily spreads out across the surface of the additive, reducing the amount of additive-UO2 interface while creating more gas-additive and gas-UO2 interface. For a high contact angle, the gas-additive interface is minimized in favor of additive-UO2 and gas-UO2 interfaces.

While the gas-UO2 interface energy is the same in all the various composite fuels, the additive-UO2 and gas-additive interface energies will depend on the additive and possibly on the fabrication method used to create the composite fuel. Unfortunately, these values are not known for the majority of the additives. Since the energies are not known, the range of fission gas bubble contact angles on the surface of the various additives is also not known. For this reason, we constructed microstructures with various contact angles (measured from the surface of the additive particle) that span the range of possible values: 35◦ (the bubble spreads out across the interface), 45◦, 65◦, 85◦, 95◦, 105◦, and 135◦ (the bubble minimizes contact with the interface).

To construct the microstructures, we used an existing phasefield model that describes the evolution of fission gas bubbles in UO2 [25]. The model was solved using the finite element method with the Muliphysics Object-Oriented Simulation Environment (MOOSE) [26,27]. In the model, a circular bubble of the desired size was introduced at the additive-UO2 interface and it was then allowed to relax to its equilibrium morphology. The structure of the additive was not allowed to evolve. The size of the gas bubble was varied to investigate the impact of different volume fractions. Note that the phase field simulations were only used to obtain the equilibrium shape of the bubble and had no other impact on this study.

Using this technique, a wide range of simulated bubble structures were created, and some examples of them are shown in Fig. 1. The largest set of these microstructures have a single spherical additive particle placed at the center of the domain and a bubble centered on the right side of the particle along the x-axis, as shown on the left of Fig. 1. For each contact angle, microstructures were created with the bubble volume fraction ranging from 0.006 to 0.040. The range of fission gas bubble volume fractions occurring in real fuels can vary depending on the fuels composition, grain size, and burn-up; bubble volume fractions have been shown to reach values of 0.03–0.12 [28–30]. In each case, the volume fraction of additive was 0.11.

To investigate the effect of the bubble’s position relative to the direction of heat flow, a few example microstructures were created with the bubble located at the surface of the spherical particle (0.11 volume fraction), but at a position further up on the surface rotated at an angle of either 45◦ or 90◦ counterclockwise around the center of the particle. For these cases, the contact angles used were 35◦, 65◦, 95◦, and 135◦ and the bubble volume fractions were 0.006, 0.040, 0.017, and 0.014. One final microstructure was simulated with two bubbles placed at the additive particle interface. These bubbles were rotated plus and minus 45◦ around the center of the additive particle, with a total volume fraction of 0.012 and a contact angle of 35◦. Examples of these microstructures are shown in the top right of Fig. 1.

Additionally, a smaller series of structures was simulated using a rectangular additive particle with a 3:1 aspect ratio, but still with an additive volume fraction of 0.11. This particle was centered in the simulation domain and oriented such that its long axis was aligned with the direction of heat flow. For this particle geometry, ten calculations were performed, three with the bubble centered on the top of the additive particle, and seven with the bubble centered on the side of the additive particle (see bottom right of Fig. 1 for examples). The volume fraction for the three bubbles on the top ranged from 0.003 to 0.021 and for the seven bubbles on the side from 0.003 to 0.020. In all cases the contact angle was 90◦ on the flat surface.

## 2.2. Heat conduction

The goal of this study is to determine the ETC of the microstructures described in the previous section. This was carried out using heat conduction simulations with the MOOSE framework. In these simulations, the 2D microstructures were spatially resolved in a 400 400 μm Cartesian computational domain with a uniform mesh size of 1 μm. We used a Cartesian rather than cylindrical domain since it provided the simplest means of resolving the particle and fission gas bubbles, including the diffuse interfaces that result from the phase field method used to construct the bubbles. The local thermal conductivity used in the simulations was heterogeneous, with different values assigned in the bulk UO2, additive, and gas bubble regions. For these calculations, unless otherwise specified, the temperature was 300 K, the bulk phase was UO , the additive phase was BeO, and the gas phase was assumed to be composed completely of Xe (as it is the most common fission gas). At 300 K, the thermal conductivity of UO2 is 8.24 W/mK [31], of BeO is 370 W/mK [32], and of Xe gas is 0.0055 W/mK [33]. An example of of a mesh shaded by thermal conductivity is shown in Fig. 2.

![](images/b2422595306ff8bca69824921e02fdfbbeb34f7a4e44197e4891ef647cef4165.jpg)  
Fig. 1. Examples of microstructures used in this study. The left image shows spherical additive particles with gas bubbles on the right. They have a range of bubble volume fractions and contact angles. Top and bottom right are spherical and rectangular additive particle microstructures, respectively, showing different bubble positioning. Displayed above each microstructure is the screening fraction for that configuration, described in Section 4. Each image has been cropped from a 400 × 400 μm sample. The spherical particles have a radius of 75 μm, and the rectangular particles are 230 × 77 μm.

![](images/87d928cddb9ae4402ec1b859789be89fcb3fc0233eab4e0d38298843dd662fad.jpg)  
Fig. 2. An example UO2 microstructure composed of a spherical BeO particle with a gas bubble on its surface, shaded by the local thermal conductivity. The magnified section shows the uniform mesh applied in the simulations of this work. The mesh spacing is 1 μm and the simulation domain is 400 × 400 μm.

To determine the effective thermal conductivity of the entire microstructure from the heterogeneous local thermal conductivity, a homogenization approach is needed that takes into account the physics of heat conduction. In this study, we used the asymptotic expansion homogenization (AEH) method to determine the effective thermal conductivity. Details of the AEH method are described by Chung et al. [34] and its implementation in MOOSE is described by Hales et al. [35]. The AEH method has been shown to robustly and accurately determine the ETC and it has been used to determine the ETC of reactor fuel microstructures in several past works [15,23,36,37]. In this work, we always report the ETC assuming that heat is transported along the x-direction.

## 3. Impact of fission gas on effective thermal conductivity

Using the method and microstructures outlined in Section 2, we conducted a study to determine the impact of fission gas bubbles on the ETC of composite fuel. In Fig. 3, the ETC calculated for all the microstructures are plotted versus bubble volume fraction, with the color of the dot indicating which microstructure group they belong to. Additionally, the dashed lines are reference values for the fresh composite fuel in yellow, pure UO2 in green, and pure UO2 with a single spherical bubble in pink. Fig. 3(a) has all data for a spherical additive particle, and Fig. 3(b) has all rectangular additive particle data.

The overall trend is as expected; as the bubble grows, the ETC of the composite is reduced. However, the wide spread in the data for a given bubble volume fraction indicates that there are other mechanisms at work. In Fig. 3(a), we see that for a given bubble fraction, bubbles with a contact angle less than 85◦ have an increased impact on the ETC compared to bubbles with larger contact angles. This appears to be due to the bubble spreading out along the additive-UO2 interface for small contact angles. The more spread out a bubble is across the additive interface, the larger impact it has on the ETC of the composite. Due to the large impact of the bubble with the smallest contact angle (35◦), its ETC reaches the same value as a microstructure with gas but no additive at a bubble fraction of 0.04, eliminating any benefit of the additive.

The microstructures with the bubble rotated away from the center of the additive particle with respect to the direction of heat flow have a higher ETC then microstructures with the same bubble fraction and contact angle in the direction of heat flow. One good example of this is the microstructure with two bubbles, rotated at plus and minus 45◦. This structure has a higher ETC than a single bubble on the right of the particle with the same bubble volume fraction (0.012) and contact angle (35◦). Additionally, when a bubble is rotated 90◦ to be positioned at the top of the additive particle, the ETC is almost equal to that for the fresh composite fuel for bubble fractions of 0.02 or less.

![](images/d35d688657a0e0a189741ec5abe669633971fda7faff1c800056cded34594df4.jpg)  
(a)

![](images/83cd2267d1f95187ff9f01643c67445e127d6dda72769032942fd36a92098f1c.jpg)

![](images/b04c75551bc69402730f0cdcd56dfdc60ec98703aeaa48240ff1c9e2ae5fa09a.jpg)  
(b)

（c）  
![](images/32be815d7a3bc2abd676ad8238aba2e35a1fa867c82ef0def36254feb48a8d2b.jpg)  
(d)  
Fig. 3. ETC plotted versus the bubble volume fraction for the microstructures demonstrated in Fig. 1. (a) has the microstructures with spherical additive particles. The angles in the legend not labeled as rotations are contact angles. (b) has the rectangular additive particle microstructures; top and side in the legend refers to the bubble’s position. The dashed lines are reference structures, where yellow is UO2 with an additive volume fraction of 0.11 but no gas, green is pure UO2, and pink is UO2 with a single circular gas bubble but no additive. The difference in the dashed yellow from (a) and (b) is due to the shape of the additive particle. (c) extends the data points for the spherical particles with 35◦ and 45◦ contact angles to higher bubble volume fractions (labeled full system), showing that after a bubble fractions of 0.04 and 0.07, respectively, the ETC of a composite fuel with a bubble is worse than pure UO2 with a bubble. The blue and orange dashed lines are for UO2 with a crescent shaped bubble and no additive, as illustrated in (d) for a gas shape from the 0.04 bubble fraction with a 35◦ contact angle. (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)

A rectangular additive particle is more beneficial to the ETC of the composite then a spherical additive particle with the same volume fraction, reaching almost a 2 W/mK higher ETC. Bubbles on top of the rectangular additive particle have little impact on the ETC, as shown in Fig. 3(b). However, bubbles on the side of the rectangular particle in the direction of heat flow have a large impact. A bubble with a contact angle of 90◦ and a volume fraction of 0.02 lowered the ETC by 2 W/mK for the rectangular particle but only by 1 W/mK for a spherical particle.

As mentioned above for the spherical particle, a bubble with a volume fraction of 0.04 and a contact angle of 35◦ had the same ETC as UO2 with the same bubble fraction with no additive, indicating that it is possible for bubbles to entirely remove the thermal benefits of the additive. To investigate this in more detail, additional microstructures were created with higher bubble volume fractions with 35◦ and 45◦ contact angles. The ETC calculations for these points are shown Fig. 3(c).

These 35◦ and 45◦ contact angle bubbles cause the ETC of the composite to drop below the ETC for UO2 with a spherical bubble at bubble fractions larger than 0.04 and 0.07, respectively. A likely cause for this is the gas bubble in the system with an additive particle has a crescent shape, wider in the direction perpendicular to the heat transport direction, as shown in Fig. 1. To test this, we removed the additive particle from the full system microstructures, but maintained the bubble with the crescent shape (see Fig. 3(d)), and calculated the ETC for just UO2 with the crescent bubble for each structure in these series. These ETC values are shown as blue and orange dashed lines in Fig. 3(c). It appears that the full system data points and the crescent Xe gas line are approaching the same values for each contact angle, making the crescent shape the lower bound of the ETC of the full system with the spherical particle and the bubble.

These results indicate that it is possible for bubbles to make a composite fuel with a high thermal conductivity additive have an effective thermal conductivity that is worse then pure UO2 fuel, if the bubble has a shape that is exceptionally good at disrupting heat flow. However, this situation also requires that the bubble be centered on the additive particle in the direction of heat flow. In a real system, it is unlikely that every bubble would adopt such a position, and that a higher ETC would be expected.

This investigation reveals a few features that are significant in determining the impact of bubbles on the ETC in a composite fuel. First, the ability of the bubble to coat the surface of the additive particle is a significant contributor to the ETC reduction. Second, the bubble placement on the additive particle surface with respect to heat flow also strongly impacts the ETC of the composite. Third, the shape of the additive particle can impact how resistant the

![](images/0a0ce52936036e2e3163a5916b957f328fd0b8327b045f71fa799d3d0820755d.jpg)  
(a)

![](images/f0a72a5059187f46736ed8be9b4130f95021bd9b7fe48705a2468b53491c2ea0.jpg)

![](images/3a61b816e34bce17f147503f263fdd4207d587a5ce3f7a61db842518aa293dfd.jpg)  
(b)

![](images/13d9cfde530b31339ad40d4722fe7f8d8620dec8517a8bad2a2816f85e57bc13.jpg)  
（c）

![](images/6901ead676333aec849d5f220bc9a7dfa914bd75be8f8161db638606ee1a90a0.jpg)  
(d)

![](images/cfc115029cccafa99047a8241766028b0c8d335d6c8f98a9614e0ecf52c8e90e.jpg)  
(e）  
Fig. 4. ETC versus the three metrics. (a) shows schematics of the three metrics used in (c–e), left to right, respectively. (b) repeats the ETC versus bubble volume fraction, for comparison. (c) shows the ETC versus surface coverage, which fails to represent different bubble positions, as seen by the 90◦ rotation data points. (c) shows ETC versus the cross-sectional coverage, which better accounts for the position of the bubble but there is still significant spread in the data. (d) shows ETC versus the screening fraction, in which a clear trend is visible.

ETC of the composite is to the impact of bubbles. Lastly, under extreme conditions, it is possible for a bubble to reduce the ETC of the composite to equal to, or even worse than, pure UO2 fuel with the same volume fraction of fission gas bubbles.

## 4. Coverage metrics

It is clear from the results in Section 3 that the bubble volume fraction does not fully represent the impact of bubbles on the ETC of composite fuel, as shown again in Fig. 4(b). In this Section, we present our efforts to determine a better metric that describes the relationship between the bubble morphology and the ETC of the composite fuel using the observations made in the previous section. Three metrics were investigated: the surface coverage fraction, the cross-sectional coverage fraction, and the screening fraction. We define these three metrics and show their capability to represent the impact of the bubble morphology, below.

The surface coverage fraction is the fraction of the additive’s surface that is in contact with the bubble, as demonstrated in Fig. 4(a). It captures the spread of the bubble over the additive surface. The ETC versus the surface coverage for all microstructures with bubble volume fractions of 0.04 or less is shown in Fig. 4(c).

This metric slightly improves the trend for the different contact angles; however, it completely fails to account for the bubble position on the surface of the additive particle. This failure is most prominent in the data points for the rotated microstructures.

The cross-sectional coverage fraction is defined as the portion of the cross section area of the additive particle in the direction of heat flow that has bubble in line with it, as shown in Fig. 4(a). This metric captures the bubble placement on the surface; when the bubble is positioned closer to the top and bottom of the additive particle it will impact less of the cross section of the additive particle. The ETC versus the cross-sectional coverage is shown in Fig. 4(d), and it shows great improvement over the surface coverage fraction. The 45◦ and 90◦ rotated microstructures are now grouped with the other microstructures with a similar ETC. In addition, the overall trend between the rectangular particle and spherical particle microstructures are beginning to adopt the same shape. However, there is still significant spread for the spherical particle data set with a mid range of cross-sectional coverage.

The screening fraction is defined as the fraction of additive volume that has bubble along the direction of heat flow divided by the total volume of additive, as shown in Fig. 4(a). This metric represents the idea that a bubble effectively eliminates the benefit of all additive in line with it in the direction of heat transport. The ETC versus the screening fraction is shown in Fig. 4(e), and with it the relationship between the bubble morphology and ETC becomes a well defined trend. The screening fraction collapses the spherical additive data into an almost unified curve, including the 45◦ and 90◦ rotated microstructures. The few microstructures that deviate slightly from the overall trend have extreme contact angles or an unusual morphology such as the two bubbles microstructure. Due to its excellent performance, we used the screening fraction as our coverage metric to develop an analytical model of the ETC of a composite with fission gas in the next section.

## 5. Analytical model

We have used what was learned from the simulation results discussed in Sections 3 and 4 to create a model that predicts the ETC of a composite microstructure with fission gas bubbles as a function of the cross-sectional coverage. We describe its development in Section 5.1 and assess its performance in Section 5.2.

## 5.1. Model development

There are three pieces needed to create an analytical model to predict the decrease in the effective thermal conductivity of a composite fuel due to fission gas bubbles. The first is the ETC of the fresh fuel. This point is the best-case scenario and is what the model should predict when the screening fraction, S, is zero. Second is an estimate for the worst-case scenario. We propose that this point should be the ETC for a pure UO2 fuel with a volume fraction of fission gas bubbles of interest, and the model’s prediction when S is one. Lastly, the rate at which the ETC will decrease from the two end points needs to be established. From the trend shown in Section 4 when using the screening fraction descriptor, the ETC of the fuel decreases following an S2 trend for both additive particle shapes.

Our model then can reduce the ETC of the fresh fuel by an amount proportional to difference in thermal conductivities in the best- and worst- case scenarios scaled by the screening fraction. Using this approach, we propose the following analytical model to describe the relationship between the screening fraction and ETC of a composite fuel with fission gas bubbles:

$$
\tag{1}
$$

where ke f f is the ETC of the composite, a is a fitting parameter discussed in the next paragraph, and S is the screening fraction. k0 is the ETC of the fresh composite fuel without any gas bubbles, and is the model’s value at S 0. k is the ETC of UO without additive with the largest bubble fraction of interest, and is the model’s value at S = 1. Ideally, one would obtain k0 from experiments and could estimate k1 from any of the available models for the ETC of irradiated UO2 fuel [38–40]. It should be noted that any uncertainty in the method used to obtain k0 and k1 will directly propagate into this model because the beginning and end points for the model are set by these parameters. It is also important to note that this model assumes that the ETC of the composite fuel will not drop below the ETC of UO2 without additive, even though we have shown that this can occur. We make this assumption due to the fact that it only occurred for bubbles with low contact angles that were directly in-line with the direction of heat flow, which is unlikely.

The coefficient a is a fitting parameter that captures the effect of the additive particle aspect ratio in the direction of heat transport. The need for this parameter can be observed by normalizing the ETC of each microstructure using the expression on the right hand side of Eq. (1) (see Fig. 5(a)). This normalization process reveals that while the general trends for both spherical and rectangular particles are similar, they are not identical. For a spherical particle (aspect ratio 1:1), a = 1. To fit values of a for other aspect ratios, a series of microstructures was created using rectangular additive particles with aspect ratios ranging from 4:1 to 1:4 with constant additive volume fraction and enough bubble volume so that S  1 (see Fig. 5(c)). For each aspect ratio, two microstructures were created with different volume fractions of constituents. The value of the coefficient a for each microstructure was found such that the model’s predicted ETC matched those calculated using the AEH method. The resulting fit to relate a to the aspect ratio of the additive particle is

$$
\tag{2}
$$

where R = length o f particlewidth of particle with respect to the direction of heat flow. A plot with the calculated values for a and the fit from Eq. (2) can be seen in Fig. 5(b).

## 5.2. Model assessment

The model was assessed using four different series of tests. First, its predictions were compared with the data from Fig. 3(a) and (b). Note that these data were used to inform the development of the model. Then the model was compared against three material systems not used in its development: BeO and UO2 at other temperatures, microstructures in which the additive thermal conductivity was varied but the bulk conductivity was held constant, and microstructures in which the bulk thermal conductivity was varied but the additive thermal conductivity was held constant. For all of these tests the microstructures with a single spherical additive particle with a bubble centered on the right side, see the left of Fig. 1, were used.

Fig. 6 (a) shows how the predictions from Eq. (1) compare to the AEH calculations of the composite fuels from Section 2.1. The model performs reasonably well for both the spherical and rectangular particle microstructures. It does not account for all the variations in the AEH calculations, but it does provide a good approximation for what ETC one could expect for a fuel as it approaches a screening fraction of one.

The performance of the model for microstructures at various temperatures are shown in Fig. 6(b). The values of 300, 900, and 1500 K were chosen for the temperature to span a range from room to reactor operating temperatures. The thermal conductivity of UO2, BeO, and Xe gas at these temperatures was obtained using the models of Fink [31], Slack [32], and Assael [33], respectively. As the temperature increases, the thermal conductivity of each phase decreases, resulting in a lowering and flattening of the ETC of the composite. The model captures this effect and is equally valid for each temperature tested.

The performance of the model using UO2 and Xe gas thermal conductivities at 300 K and the additive thermal conductivity set to 50, 500, and 1000 W/mK is shown in Fig. 6(c). There was only a slight deviation between the ETCs with additive thermal conductivities of 500 and 1000 W/mK and the analytical model matched extremely well with the AEH calculations. The 50 W/mK results were also well represented by the analytical model. However, the AEH calculation for the structure with the highest screening fraction and bubble volume fraction is lower than the k1 line. This is due to the shape of the bubble (see Fig. 3(d)) as discussed earlier. What is important to note is that only the 50 W/mK data crossed the line, indicating that the conditions required to achieve a lower thermal conductivity than a pure UO2 fuel with Xe gas are dependent upon the additive thermal conductivity. For this data set, the system with and without additive meet at approximately 0.035 bubble volume fraction. For the high volume fraction data set shown earlier, which had an additive thermal conductivity of 370 W/mK, this happened at 0.04 bubble volume fraction. The higher additive thermal conductivity tests likewise reached this threshold at approximately 0.04 bubble volume fraction. This presents a possible limit to the applicability of this model at a bubble volume fraction of 0.04 when the additive thermal conductivity is two orders of magnitude larger then the bulk phase, and decreasing as the thermal conductivity of the two phases approach one another.

The performance of the model using BeO and Xe gas thermal conductivities at 300 K and the bulk conductivity of 2.52, 4.24, and 12.24 W/mK are shown in Fig. 6(d). Changing the bulk phase thermal conductivity has a strong impact on the ETC calculated with AEH. This is expected since, by definition, the bulk phase makes up the majority of the composite’s volume. The trend observed from this test mirrors that seen when the temperature was changed. This is because in that case the bulk phase conductivity was also changing, showing it to be the dominant phase in determining the ETC of the composite. As with the previous cases, the analytical model is in strong agreement with the AEH calculations and appears to capture the changes to the ETC based on the material differences quite well.

## 6. Discussion

In this work, we have used 2D simulations of composite fuel domains containing a single additive particle to investigate the impact of fission gas bubbles on the ETC of composite fuels during reactor operation. The results indicated that as fission gas bubbles segregate to the additive interface, they can eliminate any benefit of the additive and even transition to having lower ETC than a microstructure without additive but the same bubble volume fraction. The point at which this transition occurs was not well defined in this work, but could be of significant value to the nuclear research community. We observed that the thermal conductivity of the additive impacted the point at which this transition occurred. Additionally, it is likely that the relative volume fraction of the additive and bubbles impacts this critical point, as the screening fraction is somewhat dependent upon these two parameters. The contact angle also plays an important role in the critical point, since the contact angle strongly impacts the shape of the fission gas bubble. This can be seen in Fig. 3(c), where the volume fraction at which the composite fuel becomes worse than pure UO2 fuel moved from a value of 0.04 to 0.07 when the contact angle changed from 35◦ to 45◦. At this time, we leave further investigation of this transition to future work. From these results, it appears that composite fuels with small fission gas contact angles may only improve fuel performance at lower burn-up.

The simulations used in this work were 2D, to reduce computational expense, and it is well established that 2D simulations tend to over estimate the impact of a secondary phase [41]. However, the primary impact of the fission gas bubble is to inhibit heat transport through the additive and this effect is likely to be similar in 3D. Although there are additional paths for heat transport in a 3D composite when compared to 2D, if the fission gas is fully screening the additive then those additional paths will not be more advantageous than in a pure UO2 fuel. It is possible that rate at which the ETC of the composite decreases may be different. Therefore, future work should carry out 3D simulations to see if similar trends between the ETC and screening fraction are observed. The analytical model presented here also needs to be compared against 3D simulation results.

We also simplified this study by using microstructures with a single additive particle situated in a matrix of UO2 and we did not vary the size of the particle or the size of the domain (which would vary the effective spacing between particles due to

![](images/17535d757623ef8c5c0ec4889848007997849a5255865c51c757bd7c0abeb4ff.jpg)  
(a）

![](images/36d845a2ab30bd0346d3dd7795306c35bda5fc9f6eed734c692bb03ce9151799.jpg)

（(b)  
![](images/9a01c909aa697a8eaa09c33a4bec9b9459db6ff823206c6046ed2c1cbce22bac.jpg)  
（c）  
Fig. 5. Determination of the fitting parameter a. (a) shows the normalized ETC, using the expression on the right hand side of Eq. (1), for each calculated structure, colored to indicate additive particle shape. While the general trend of for the two particle shapes is similar they do not match perfectly, indicating the need for the shape dependent fitting parameter. (b) shows the value of a versus the aspect ratio calculated using AEH and determined using the fit. The blue dots are the values of a needed to make the model match the AEH results. There are two sets of microstructures included, both transition a particle from an aspect ratio of 4:1 to 1:4. One set has half of the additive volume fraction of the first. The data sets with different volume fractions are nearly identical, with the set having less additive appearing just slightly lower than the other. (c) shows examples of rectangular additive particle microstructure with varying aspect ratios. (For interpretation of the references to color in this figure legend, the reader is referred to the web version of this article.)

![](images/e7821a099392ed00b5f29158b83bec74d682cca9abdd1d645faa1244d40aae29.jpg)  
(a)

![](images/96314378eb95f3d6655671b600392abc9df8ffb4a7173869fd30160fc36b3f18.jpg)  
(b)

![](images/48c3545323e60e92491ef25d1493b17688b4f84a8a688176e9d70455a96537f8.jpg)  
（c）

![](images/f811f7c97d80b19e68d109b00b2ecc4c18cdf10cff14fadbaf79ce8e57b7e240.jpg)  
(d）)  
Fig. 6. Plots showing the analytical model’s performance when applied to our simulated microstructures, illustrated in Fig. 1. (a) compares the model predictions with the ETC values from the top row of Fig. 3; they use the thermal conductivity of UO2, BeO, and Xe gas at 300 K. In (b) the temperature of the system is changed, resulting in different thermal conductivities for all phases. In (c) only the additive phase thermal conductivity is changed. In (d) only the bulk thermal conductivity is changed. The points are calculations for the simulated microstructures, solid lines are the analytical model, and dashed lines are calculations of the bulk phase and 0.04 volume fraction Xe gas, but no additive. The coloring indicates the value for the property being changed.

the boundary conditions). However, in a real system there would be many particles, with a potentially wide range of shapes, sizes, and spacing between particles. With a greater number of particles the probability of clusters forming could become significant. These clusters could push the system to a more heterogeneous state and add uncertainty to the trends observed. As bubbles segregate to the various particles, some bubbles would be aligned with the direction of heat transport while others would not. Additionally, there would be grain boundaries, creating other possible interfaces for the Xe gas to segregate to and form bubbles. Thus, there would be a range of screening fractions for all the various particles. We believe that measurements of an average screening fraction from an experimental micrograph or from simulations with many particles would still result in a strong correlation with the ETC and the bubble effect could still be reasonably approximated using our analytical model. However, this should be investigated. In addition, if our model were to be implemented in a fuel performance code to describe the impact of fission gas on composite fuel ETC, the fission gas release model would have to be modified to evolve the average screening fraction with time.

Finally, we only considered composite fuels with discrete additive particles dispersed throughout the fuel. However, the structure of an additive could alternatively have a continuous character, rather than dispersed, with the additive phase forming connected structures along grain boundaries. These structures could be more resistant to the effects of bubbles since they have the potential to channel heat around the bubble. Therefore, the results from this work is not applicable to continuous structures and the impact of bubbles on their ETC should be investigated.

## 7. Conclusion

In this study we investigated the impact of fission gas bubbles on UO2 fuels with dispersed high thermal conductivity additives. Various microstructures were created, each with a single additive particle interacting with bubbles. The bubble contact angle and volume fraction were varied and the effective thermal conductivity was calculated with the AEH method using MOOSE. The screening fraction of the gas phase on the additive was determined to be the best metric to predict the ETC of the composite. Then a model, Eq. (1), was proposed that uses the screening fraction, the thermal conductivity of the fresh composite fuel, the thermal conductivity of UO2 with a large bubble volume fraction, and a fitting parameter a that accounts for the aspect ratio of the additive particle. The model’s predictions for the ETC of the composites closely match the AEH calculations, though its applicability to more complicated and 3D structures remains to be determined.

A significant finding of this work was the potential for composite UO2 fuels with a high thermal conductivity additive to eliminate the benefit of the additive on the ETC and to even result in a lower thermal conductivity then UO with fission gas bubbles but no additive. This effect is related to the shape of the bubbles. If the bubble is distorted from a spherical shape to be elongated perpendicular to the direction of heat flow due to the presence of the additive, then it can act as a significant barrier to heat flow. The transition at which this occurs is not defined in this work, but it was shown that the transition point is impacted by the thermal conductivity of the additive phase and contact angle of the gas bubble on the additive surface. This result indicates that composite fuels with high thermal conductivity additives may only give fuel performance benefits at lower burn-up.

## Data availability

Data will be provided on request.

## Declaration of Competing Interest

Authors declare that they have no conflict of interest.

## CRediT authorship contribution statement

Floyd W. Hilty: Methodology, Software, Formal analysis, Investigation, Writing - original draft. Dong-Uk Kim: Methodology, Software. Michael R. Tonks: Conceptualization, Writing - review & editing, Supervision, Project administration, Funding acquisition.

## Acknowledgments

This work was funded by the US DOE Nuclear Energy University Programs under IRP 15-8843, “Development of Accident Tolerant Fuel Options For Near Term Applications”. The authors would like to thank Jacopo Buongiorno and Kumar Sridharan from the Massachusetts Institute of Technology for their leadership of the project.

## References

[1] S. Bragg-Sitton, Development of advanced accident-tolerant fuels for commercial LWRs, Nucl. News 57 (2014) 83–91.

[2] W. Zhou, W. Zhou, Enhanced thermal conductivity accident tolerant fuels for improved reactor safety—A comprehensive review, Ann. Nucl. Energy 119 (2018) 66–86.

[3] S. ishimoto, M. Hirai, K. Ito, Y. Korei, Thermal Conductivity of UO2-BeO Pellet, J. Nucl. Sci. Technol. 33 (2) (1996) 134–140, doi:10.1080/18811248.1996.9731875.

[4] S. Yeo, R. Baney, G. Subhash, J. Tulenko, The influence of SiC particle size and volume fraction on the thermal conductivity of spark plasma sintered UO2 and SiC composites, J. Nucl. Mater. 442 (1) (2013) 245–252, doi:10.1016/j.jnucmat. 2013.09.003.

[5] Z. Chen, G. Subhash, J.S. Tulenko, Raman spectroscopic investigation of graphitization of diamond during spark plasma sintering of UO2-diamond composite nuclear fuel, J. Nucl. Mater. 475 (2016) 1–5.

[6] S.C. Finkeldei, J.O. Kiggans, R.D. Hunt, A.T. Nelson, K.A. Terrani, Fabrication of UO2-Mo composite fuel with enhanced thermal conductivity from sol-gel feedstock, J. Nucl. Mater. 520 (2019) 56–64, doi:10.1016/j.jnucmat.2019.04.011.

[7] J.H. Yang, K.W. Song, K.S. Kim, Y.H. Jung, A fabrication technique for a UO2 pellet consisting of UO2 grains and a continuous W channel on the grain boundary, J. Nucl. Mater. 353 (3) (2006) 202–208, doi:10.1016/j.jnucmat.2006.01.019.

[8] A. Cartas, H. Wang, G. Subhash, R. Baney, J. Tulenko, Influence of Carbon Nanotube Dispersion in UO and carbon nanotube ceramic matrix composites utilizing spark plasma sintering, Nucl. Technol. 189 (3) (2015) 258–267, doi:10.13182/NT14-7.

[9] T. Yao, G. Xin, S.M. Scott, B. Gong, J. Lian, Thermally-conductive and mechanically-robust graphene nanoplatelet reinforced UO2 composite nuclear fuels, Sci. Rep. 8 (1) (2018) 2987, doi:10.1038/s41598-018-21034-4. Number: 1 Publisher: Nature Publishing Group

[10] B.J. Jaques, J. Watkins, J.R. Croteau, G.A. Alanko, B. Tyburska-Pschel, M. Meyer, P. Xu, E.J. Lahoda, D.P. Butt, Synthesis and sintering of UN-UO2 fuel composites, J. Nucl. Mater. 466 (2015) 745–754, doi:10.1016/j.jnucmat.2015.06.029.

[11] B. Gong, T. Yao, P. Lei, L. Cai, K.E. Metzger, E.J. Lahoda, F.A. Boylan, A. Mohamad, J. Harp, A.T. Nelson, J. Lian, U3Si2 and UO2 composites densified by spark plasma sintering for accident-tolerant fuels, J. Nucl. Mater. 534 (2020) 152147, doi:10.1016/j.jnucmat.2020.152147.

[12] W. Zhou, R. Liu, S.T. Revankar, Fabrication methods and thermal hydraulics analysis of enhanced thermal conductivity UO2 and BeO fuel in light water reactors, Ann. Nucl. Energy 81 (2015) 240–248, doi:10.1016/j.anucene.2015.02. 044.

[13] W. Zhou, S.T. Revankar, R. Liu, M.S. Beni, Microstructure-based thermal conductivity and thermal behavior modeling of nuclear fuel UO2-BeO, Heat Transf. Eng. 39 (9) (2018) 760–774, doi:10.1080/01457632.2017.1341216. Taylor & Francis

[14] F. Badry, R. Brito, M.G. Abdoelatef, S. McDeavitt, K. Ahmed, An Experimentally validated mesoscale model of thermal conductivity of a UO2 and BeO composite nuclear Fuel, JOM 71 (12) (2019) 4829–4838, doi:10.1007/ s11837-019-03831-y.

[15] F. Hilty, M.R. Tonks, Development and application of a microstructure dependent thermal resistor model for UO reactor fuel with high thermal conductivity additives, J. Nucl. Mater. 540 (2020) 10.1016/j.jnucmat.2020.152334.

[16] S.W. Lee, H.T. Kim, I.C. Bang, Performance evaluation of UO2/graphene composite fuel and SiC cladding during LBLOCA using MARS-KS, Nucl. Eng. Des. 257 (2013) 139–145, doi:10.1016/j.nucengdes.2013.01.012.

[17] D. Chandramouli, S.T. Revankar, Development of thermal models and analysis of UO2-BeO fuel during a loss of coolant accident, Int. J. Nucl. Energy 5 (2014) e751070.

[18] R. Liu, W. Zhou, P. Shen, A. Prudil, P.K. Chan, Fully coupled multiphysics modeling of enhanced thermal conductivity UO2 and BeO fuel performance in a light water reactor, Nucl. Eng. Des. 295 (2015) 511–523.

[19] R. Liu, W. Zhou, A. Prudil, P.K. Chan, Multiphysics modeling of UO2-SiC composite fuel performance with enhanced thermal and mechanical properties, Appl. Therm. Eng. 107 (2016) 86–100, doi:10.1016/j.applthermaleng.2016.06. 173.

[20] R. Liu, W. Zhou, Multiphysics modeling of novel UO2-BeO sandwich fuel performance in a light water reactor, Ann. Nucl. Energy 109 (2017) 298–309.

[21] W. Zhou, W. Zhou, Thermophysical and Mechanical Analyses of UO2-36.4vol.% BeO Fuel Pellets with Zircaloy, SiC, and FeCrAl Claddings, Metals 8 (1) (2018) 65, doi:10.3390/met8010065. Number: 1 Publisher: Multidisciplinary Digital Publishing Institute

[22] F. Cappia, J.M. Harp, K. McCoy, Post-irradiation examinations of UO2 composites as part of the accident tolerant fuels campaign, J. Nucl. Mater. 517 (2019) 97–105.

[23] X.-M. Bai, M.R. Tonks, Y. Zhang, J.D. Hales, Multiscale modeling of thermal conductivity of high burnup structures in UO2 fuels, J. Nucl. Mater. 470 (2016) 208–215, doi:10.1016/j.jnucmat.2015.12.028.

[24] C. Walker, D. Staicu, M. Sheindlin, D. Papaioannou, W. Goll, F. Sontheimer, On the thermal conductivity of UO2 nuclear fuel at a high burn-up of around 100MWd/kgHM, J. Nucl. Mater. 350 (1) (2006) 19–39, doi:10.1016/j.jnucmat. 2005.11.007.

[25] L.K. Aagesen, Y. Gao, D. Schwen, K. Ahmed, Grand-potential-based phase-field model for multiple phases, grains, and chemical components, Phys. Rev. E 98 (2018) 023309, doi:10.1103/PhysRevE.98.023309.

[27] M.R. Tonks, D. Gaston, P.C. Millett, D. Andrs, P. Talbot, An object-oriented finite element framework for multiphysics phase field simulations, Comput. Mater. Sci. 51 (1) (2012) 20–29.

[28] J. Turnbull, The effect of grain size on the swelling and gas release properties of UO2 during irradiation, J. Nucl. Mater. 50 (1) (1974) 62–68.

[29] S. Kashibe, K. Une, K. Nogita, Formation and growth of intragranular fission gas bubbles in UO2 fuels with burnup of 6–83GWd/t, J. Nucl. Mater. 206 (1) (1993) 22–34.

[30] M. Tonks, D. Andersson, R. Devanathan, R. Dubourg, A. El-Azab, M. Freyss, F. Iglesias, K. Kulacsy, G. Pastore, S.R. Phillpot, et al., Unit mechanisms of fission gas release: current understanding and future needs, J. Nucl. Mater. 504 (2018) 300–317.

[31] J.K. Fink, Thermophysical properties of uranium dioxide, J. Nucl. Mater. 279 (2000) 1–18.

[32] G.A. Slack, S.B. Austerman, Thermal conductivity of BeO single crystals, J. Appl. Phys. 42 (1971) 4713–4717.

[33] M. Assael, A. Kalyva, S. Monogenidou, M. Huber, R. Perkins, D. Friend, E. May, Reference values and reference correlations for the thermal conductivity and viscosity of fluids, J. Phys. Chem. Ref. Data 47 (2018) 021501, doi:10.1063/1. 5036625.

[34] P.W. Chung, K.K. Tamma, R.R. Namburu, Asymptotic expansion homogenization for heterogeneous media: computational issues and applications, Compos. Part A 32 (9) (2001) 1291–1301, doi:10.1016/S1359-835X(01)00100-2.

[35] J. Hales, M. Tonks, K. Chockalingam, et al., Asymptotic expansion homogenization for multiscale nuclear fuel analysis, Comput. Mater. Sci. 99 (2015) 290–297.

[36] L. Liang, Y.S. Kim, Z.-G. Mei, L.K. Aagesen, A.M. Yacout, Fission gas bubbles and recrystallization-induced degradation of the effective thermal conductivity in U-7Mo fuels, J. Nucl. Mater. 511 (2018) 438–445.

[37] M.R. Tonks, C. Bhave, X. Wu, Y. Zhang, Uncertainty quantification of mesoscale models of porous uranium dioxide, in: Uncertainty Quantification in Multiscale Materials Modeling, Elsevier, 2020, pp. 329–354.

[38] P. Lucuta, H. Matzke, I. Hastings, A pragmatic approach to modelling thermal conductivity of irradiated UO fuel: Review and recommendations, J. Nucl. Mater. 232 (2) (1996) 166–180, doi:10.1016/S0022-3115(96)00404-7.

[39] C. Ronchi, M. Sheindlin, D. Staicu, M. Kinoshita, Effect of burn-up on the thermal conductivity of uranium dioxide up to 100.000MWdt−1, J. Nucl. Mater. 327 (1) (2004) 58–76, doi:10.1016/j.jnucmat.2004.01.018.

[40] M.R. Tonks, X.-Y. Liu, D. Andersson, D. Perez, A. Chernatynskiy, G. Pastore, C.R. Stanek, R. Williamson, Development of a multiscale thermal conductivity model for fission gas in UO2, J. Nucl. Mater. 469 (2016) 89–98.

[41] M.C. Teague, B.S. Fromm, M.R. Tonks, D.P. Field, Using coupled mesoscale experiments and simulations to investigate high burn-up oxide fuel thermal conductivity, JOM 66 (12) (2014) 2569–2577.
