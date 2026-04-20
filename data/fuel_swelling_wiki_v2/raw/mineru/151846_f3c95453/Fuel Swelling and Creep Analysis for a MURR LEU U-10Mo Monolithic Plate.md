# 📄 PDF Parsing Result

**File:** `/Volumes/openclaw记忆/Zotero_storage/storage/RICSSFMX/151846.pdf`
**Backend:** `pipeline`
**Pages:** 0 to end
**Formula Recognition:** ❌ Disabled
**Table Recognition:** ✅ Enabled

---

ANL/RTR/TM-18/19

# Fuel Swelling and Creep Analysis for a MURR LEU U-10Mo Monolithic Plate

Nuclear Science and Engineering Division

## About Argonne National Laboratory

Argonne is a U.S. Department of Energy laboratory managed by UChicago Argonne, LLC under contract DE-AC02-06CH11357. The Laboratory’s main facility is outside Chicago, at 9700 South Cass Avenue, Argonne, Illinois 60439. For information about Argonne and its pioneering science and technology programs, see www.anl.gov.

## DOCUMENT AVAILABILITY

Online Access: U.S. Department of Energy (DOE) reports produced after 1991 and a growing number of pre-1991 documents are available free via DOE’s SciTech Connect (http://www.osti.gov/scitech/)

## Reports not in digital format may be purchased by the public from the National Technical Information Service (NTIS):

U.S. Department of Commerce   
National Technical Information Service 5301 Shawnee Rd   
Alexandria, VA 22312   
www.ntis.gov   
Phone: (800) 553-NTIS (6847) or (703) 605-6000   
Fax: (703) 605-6900   
Email: morders@ntis.gov

Reports not in digital format are available to DOE and DOE contractors from the Office of Scientific and Technical Information (OSTI):

U.S. Department of Energy

Office of Scientific and Technical Information

P.O. Box 62

Oak Ridge, TN 37831-0062

www.osti.gov

Phone: (865) 576-8401

Fax: (865) 576-5728

Email: reports@osti.gov

## Disclaimer

This report was prepared as an account of work sponsored by an agency of the United States Government. Neither the United States Government nor any agency thereof, nor UChicago Argonne, LLC, nor any of their employees or officers, makes any warranty, express or implied, or assumes any legal liability or responsibility for the accuracy, completeness, or usefulness of any information, apparatus, product, or process disclosed, or represents that its use would not infringe privately owned rights. Reference herein to any specific commercial product, process, or service by trade name, trademark, manufacturer, or otherwise, does not necessarily constitute or imply its endorsement, recommendation, or favoring by the United States Government or any agency thereof. The views and opinions of document authors expressed herein do not necessarily state or reflect those of the United States Government or any agency thereof, Argonne National Laboratory, or UChicago Argonne, LLC.

# Fuel Swelling and Creep Analysis for a MURR LEU U-10Mo Monolithic Plate

prepared by

Walid Mohamed1, Hee Seok Roh1, John Stillman2, Erik Wilson2

1 Chemical and Fuel Cycle Technologies Division, Argonne National Laboratory

2 Nuclear Science and Engineering Division, Argonne National Laboratory

March 2019

(This page left intentionally blank)

## Table of Contents

1 Introduction... .1   
2 Simulation and Model Setup .... ..2   
2.1 Irradiation Parameters.. ... 2   
2.2 Finite Element Model ... ... 3   
2.3 Materials Models and Correlations... ...... 4   
2.4 Evaluation of Swelling and Creep Models for U-10Mo Fuel .. .... 4   
2.4.1 Fuel Swelling Correlations ........ ...... 4   
2.4.2 Irradiation Creep Model.. ...... 6   
3 Results and Discussion ...... ......7   
3.1 FEA with Kim Swelling Correlation.. ...... 8   
3.2 FEA with Swelling Correlation Excluding AFIP-6 MKII Data . ...... 10   
3.3 FEA Considering 95% UCL of Correlation Including AFIP-6 MKII Data.............................. ....... 12   
3.4 Stress analysis .. ..... 14   
4 Summary........................................................................................................................................... 15   
5 Acknowledgements.... ...... 15   
Appendix A.... ..... 16   
References .. ... 19

## List of Figures

Figure 1. Local-to-average fission density distribution in the U-10Mo foil of plate 23 as modeled in this   
work.. ..... 3   
Figure 2. Fission density distribution in the U-10Mo foil of plate 23 at EOL as modeled in this work........ 3   
Figure 3. Comparison of fuel swelling correlations modeled in this work.. ...... 6   
Figure 4. Swelling strain contours in U-10Mo fuel core of plate 23 considering (a) Kim swelling   
correlation, (b) excluding AFIP-6 MKII swelling correlation, and (c) 95% UCL including AFIP-6 MKII   
correlation. .. ..... 7   
Figure 5. Contours of displacement along thickness direction in plate 23 considering Kim swelling   
correlation and different values of creep rate coefficient (× 10 − 25 cm3/MPa-fission)... ...... 8   
Figure 6. Schematic of plate 23 longitudinal mid-plane used for the analysis of plate thickness at EOL.   
...... 9   
Figure 7. Effect of variation in creep rate coefficient on displacement profile along longitudinal mid  
plane of plate 23 at EOL with Kim swelling correlation. Positive and negative Y-axis represents   
outboard and inboard directions, respectively....... . 9   
Figure 8. Net increase in plate 23 thickness along longitudinal mid-plane at EOL considering Kim   
swelling correlation with various values of creep rate coefficient (× 10 − 25 cm3/MPa-fission).......10   
Figure 9. Contours of displacement along thickness direction in plate 23 with swelling correlation   
excluding AFIP-6 MKII data and different values of creep rate coefficient (× 10 − 25 cm3/MPa  
fission)...... ........... 10   
Figure 10. Effect of variation in creep rate coefficient on displacement profile along longitudinal mid-plane   
of plate 23 at EOL with swelling correlation excluding AFIP-6 MKII data. Positive and negative Y-axis   
represents outboard and inboard directions, respectively..... .. 11   
Figure 11. Net increase in plate 23 thickness along longitudinal mid-plane at EOL with swelling correlation   
excluding AFIP-6 MKII and various values of creep rate coefficient (× 10 − 25 cm3 /MPa-fission). ........12   
Figure 12. Contours of displacement along thickness direction in plate 23 considering 95% UCL of   
swelling correlation including AFIP-6 MKII data and different values of creep rate coefficient (× 10 −   
25 cm3/MPa-fission). ... ..... 12   
Figure 13. Effect of variation in creep rate coefficient on displacement profile along longitudinal mid-plane   
of plate 23 at EOL with the 95% UCL swelling correlation including AFTP-6 MKII data. Positive and   
negative Y-axis represents outboard and inboard directions, respectively. ......................... ............... 13   
Figure 14. Net increase in plate 23 thickness along longitudinal mid-plane at EOL with 95% UCL of   
swelling correlation including AFIP-6 MKII data and various values of creep rate coefficient (× 10 −   
25 cm3/MPa-fission). ............. ...... 14

## List of Tables

Table 1: Variation in average power and fission densities with time for plate 23 in MURR LEU fuel element   
[10] .......... ...... 2   
Table 2: Nominal dimensions of plate 23 as modeled in this work [10]..... .... 4   
Table 3: Fuel swelling in plate 23 at 2.62 × 1027 ????????????????????????????/????3 (EOL) from FEA and calculations......... 7   
Table 4: Maximum increase in the thickness of plate 23 at EOL under different combinations of swelling   
correlations and creep rate coefficients (× 10 − 25 cm3 /MPa-fission). ... ..... 14   
Table 5: Peak equivalent stress in U-10Mo fuel core. ... ... 15

## 1 Introduction

The U.S. DOE National Nuclear Security Administration (NNSA) Office of Material Management and Minimization (M3) conversion program aims to eliminate or minimize the civilian use of weaponsgrade highly enriched uranium (HEU) both domestically and internationally. A key approach to achieve this goal is the conversion of research and test reactors from HEU to high density, low-enriched uranium fuels (LEU, < 20% U235) [1].

Over the past few decades, U-Mo alloys were considered to be the most promising candidates for the conversion of research and test reactors to LEU fuels due to their stable irradiation performance [2]. U-Mo alloys showed recognized dimensional stability and acceptable swelling behavior compared to other forms of fuels under typical irradiation conditions of research and test reactors. The observed stability of U-Mo alloys is attributed to the Mo content, which stabilizes the cubic gamma phase of the fuel. Furthermore, U-Mo alloys are recognized for their low neutron absorption cross section when compared to other fuel materials proposed for the conversion program [3].

The recent U-Mo fuel design adopted by the U.S. for the conversion of its High-Performance Research Reactors (USHPRR) is a monolithic plate form characterized by a high density LEU-10Mo fuel core. The U-10Mo monolithic plate design consists of U-10Mo fuel core sandwiched between Zr diffusion barriers and encapsulated in Al-based AA6061 cladding. Six reactors (including one critical facility) constitute the USHPRR fleet that will primarily use U-10Mo monolithic fuel for LEU conversion [4]. Among these reactors, the University of Missouri Research Reactor (MURR) is the main focus of this study.

The conversion of the MURR from the use of HEU to LEU is currently in progress. The University of Missouri is collaborating with the Reactor Conversion Proram at Argonne National Laboratory (ANL) in various activities relavant to the conversion of the MURR such as: fuel element design, fuel cycle analyses [5], and steady state thermal hydraulics safety analysis [6]. To achieve successful conversion of the MURR, it is essential to develop a fuel element design that ensures safe reactor operation and acceptable shutdown and safety margins [4]. Furthermore, it is necessary that the experimental performance of the existing facilty is maintained at the same level of efficiency and capacity upon conversion.

It is well known that in-service fuel swelling due to gaseous and solid fission products can impact the overall fuel performance. In the MURR monolithic fuel plate, changes in fuel dimensions along the thickness direction are attibuted to the combined effect of fuel swelling and irradiation creep. From a safety analysis viewpoint, it is critical to determine the swelling and creep induced change in the MURR plate thickness under steady-state conditions. Successful prediction and determination of irradiated fuel plate thickness is required to ensure that adequate coolant channel thickness remains unblocked to ensure proper heat removal from the fuel plate during operation.

In this work, finite element analysis (FEA) is used to model and simulate the thermo-mechanical behavior of a selected LEU MURR fuel plate under typical irradiation conditions of the proposed LEU MURR core. The proposed LEU fuel element for MURR conversion has 23 curved fuel plates. The fuel element design and analysis are described in Reference [7]. The safety analysis for calculating the margin to flow instability during steady-state operations evaluated all fuel plate coolant channels in reference cores that had elements with a mixture of burnups, which is typical for MURR operations [7]. In addition to the application of engineering hot channel factors to account for variations in the fuel element manufacturing that could affect the coolant channel gaps, the analysis assumed a constriction of the coolant channel gaps due to an increase in the fuel plate thicknesses during the element lifetime. Estimates of the local plate thickness increase at end-of-life (EOL) due to fuel swelling and creep were developed from experimental data presented in References [8] and [9]. The maximum local plate thickness increase from that analysis was calculated for fuel plate 23 in an EOL element. Furthermore, the minimum margin to flow instability for the reference LEU cores was calculated to occur in coolant channel 23 of an EOL element, which is the coolant channel between plates 22 and 23. Therefore, the work performed here evaluated plate 23 only, as this was found to be the most limiting plate.

The main goal of the present FE based study is to determine the maximum local increase in the thickness of plate 23 under various combinations of swelling correlations and creep rate coefficients. The estimated increase in the thickness of plate 23 is then used to evaluate the reduction in the thickness of the adjacent coolant channels.

## 2 Simulation and Model Setup

## 2.1 Irradiation Parameters

The irradiation conditions to be encountered by plate 23 in the MURR LEU fuel element were simulated in three steps: (i) steady-state start up with a predefined plate temperature of 294 K, (ii) transient step of 2873 hours representing the total irradiation time of plate 23 with swelling and creep behavior included and maximum allowable temperature change per step of 5 K, and (iii) steady-state shutdown step wherein the whole structure of the plate is cooled to 325 K.

Table 1 summarizes the variation in the average power and fission densities in the plate 23 with time as modeled in this work. Detailed, two-dimensional profiles for the power density and fission density by axial and azimuthal mesh were derived from the results of neutron physics calculations for plate 23 under prototypic conditions [10]. The plate-average values presented in Table 1 were approximated by taking the arithmetic average of the data, without taking into account the variable mesh sizes for the data. Figure 1 shows spatial distribution of local-to-average fission density in plate 23 U-10Mo fuel core, which was assumed constant over the irradiation cycle. The local-to-average fission density values were calculated using the plate-average fission density in Table 1 and preserve the detailed, two-dimensional fission density profile calculated for plate 23. Finally, the fission density distribution in the fuel core of plate 23 at EOL is shown in Figure 2 with a maximum fission density estimated to be 2.62 × 1027 ????????????????????????????/????3.

Table 1: Variation in average power and fission densities with time for plate 23 in MURR LEU fuel element [10]
<table><tr><td rowspan=1 colspan=1>Irradiation time, hr</td><td rowspan=1 colspan=1>Average power density, W/cm³</td><td rowspan=1 colspan=1>Average fission density,fission/m</td></tr><tr><td rowspan=1 colspan=1>48</td><td rowspan=1 colspan=1>5982.35</td><td rowspan=1 colspan=1>3.20 × 1025</td></tr><tr><td rowspan=1 colspan=1>1258</td><td rowspan=1 colspan=1>5776.23</td><td rowspan=1 colspan=1>8.26× 1026</td></tr><tr><td rowspan=1 colspan=1>1560</td><td rowspan=1 colspan=1>5746.41</td><td rowspan=1 colspan=1>1.02 × 1027</td></tr><tr><td rowspan=1 colspan=1>2873 (EOL)</td><td rowspan=1 colspan=1>5225.09</td><td rowspan=1 colspan=1>1.86 × 1027</td></tr></table>

![](images/3b9d67eab176d58836c8a6d5b03631847ed49c15afa73fa6e065475b8cdd2076.jpg)  
Figure 1. Local-to-average fission density distribution in the U-10Mo foil of plate 23 as modeled in this work.

![](images/f59caecf78a28dd28172f99c6c92d17350a52ba05958c9ae5c9928a2bb6409dd.jpg)  
Figure 2. Fission density distribution in the U-10Mo foil of plate 23 at EOL as modeled in this work.

## 2.2 Finite Element Model

The finite element (FE) geometric model of plate 23 in MURR LEU fuel element was developed considering the nominal dimensions listed in Table 2. The thickness of the inboard and outboard coolant channels adjacent to plate 23 is 2.3622 mm (channel 23) and 2.4257 mm (channel 24), respectively [10].

Table 2: Nominal dimensions of plate 23 as modeled in this work [10]
<table><tr><td rowspan=1 colspan=1>Section</td><td rowspan=1 colspan=1>Thickness, mm</td><td rowspan=1 colspan=1>Length, mm</td><td rowspan=1 colspan=1>Width, mm</td></tr><tr><td rowspan=1 colspan=1>LEU-10Mo fuel core</td><td rowspan=1 colspan=1>0.4318</td><td rowspan=1 colspan=1>609.6</td><td rowspan=1 colspan=1>102.8116</td></tr><tr><td rowspan=1 colspan=1>Zr diffusion barrier</td><td rowspan=1 colspan=1>0.0254 (on each side of the fuel core)</td><td rowspan=1 colspan=1>609.6</td><td rowspan=1 colspan=1>102.8116</td></tr><tr><td rowspan=1 colspan=1>Cladding</td><td rowspan=1 colspan=1>0.381 (on each side of the fuel core)</td><td rowspan=1 colspan=1>647.7</td><td rowspan=1 colspan=1>109.7202</td></tr></table>

The element C3D8T (a 3D temperature-displacement continum element with 8-nodes of thermally coupled brick) in ABAQUS FE solver [11] was adopted to represent the LEU-10Mo fuel core, Zr diffusion barrier, and cladding sections of plate 23. As noted by the element type (C3D8T), full integration was used to achive highest possible aaccuracy of displacement data which in turn increased the computation time. Based on results obtained from a series of mesh sensitivty and sub-modeling studies, the FE geometric model of plate 23 was meshed with a total of 186,624 C3D8T elements distributed between the three sections of the plate as follows: 55,216 elements in each of the fuel core and Zr diffusion barrier sections and 76,192 elements in the cladding section. Ideal bonding was assumed at the interfaces between the fuel core, Zr diffusion barriers, and Al-cladding which implies that no delamination was allowed to take place. See Appendix A for further details on FE mesh profile analysis.

## 2.3 Materials Models and Correlations

Documented properties of U-10Mo alloy, commercially pure Zr, and AA6061-O alloy were used to model the fuel core, diffusion barrier, and cladding, respectively. Material properties were varied as functions of temperature and irradiation exposure following the “Preliminary Report on U-Mo Monolithic Fuel for Research Reactors, INL/EXT-17-40975, Revision 1”[12].

The behaviors of the AA6061-O cladding and the Zr diffusion barier were simulated considering elasticity, plasticity, thermal expansion, and thermal creep [12]. Hardening due to fast neutron irradiation was only considered for the AA6061-O cladding.

The thermo-mechanical behavior of the U-10Mo fuel core is described considering elasticity, plasticity, thermal expansion, swelling (due to solid and gaseous fission products), irradiation creep and thermal conductivity degradation due to porosity (fission gas bubbles) formation in the fuel [12]. The following are the primary models/ correlations used to model the U-10Mo fuel:

(i) Model for thermal conductivity degradation of the fuel material [12]

(ii) Irradiation induced creep model [12], [13]

(iii) Model for the fuel swelling due to fission products [8], [12]

## 2.4 Evaluation of Swelling and Creep Models for U-10Mo Fuel

As mentioned earlier, the thermo-mechanical behavior and the resultant increase in the thickness of plate 23 will be evaluated under various combinations of swelling correlations and irradiation creep coefficients. Thus, a brief evaluation of the swelling and creep correlation is presented in this section.

## 2.4.1 Fuel Swelling Correlations

In this work, the irradiation performance of plate 23 in the MURR LEU fuel element was simulated considering the following three swelling correlations:

(i) Swelling correlation developed by Kim et al. [8]:

![](images/f5a5321939f4bcbac1c5344536a7de85a353af4e4c0317047c27d4e942130e39.jpg)

Equation 1

![](images/c186a6f3674f89e42de304659efae23a7838062aa41ea14ad2752b578fa63e03.jpg)

where �∆???? ????� � total swelling in percent and ???????? is the fission density in × 1027 ????????????????????????????/????3. Kim et al. devloped the above swelling correlation considering fuel thickness measurements made on a limited number of plates irradiated in the RERTR-6 through RERTR-9 campaigns [8], [12]. In that work, Kim et al. considerd a single fuel thickness data point at the mid-point of an irradiated plate transverse mid-section in order to minimize the contribution of irradiation creep to the thickness measurements. This swelling correlation will be referred to as “Kim swelling correlation” in the next sections of this report.

(ii) Swelling correlation excluding AFIP-6 MKII data [12]:

According to the “Preliminary Report on U-Mo Monolithic Fuel for Research Reactors, INL/EXT-17- 40975, Revision 1” [12], a large number of local fuel thickness measurements (18,675) were made on irradiated plates from RERTR-9, RERTR-10, RERTR-12, AFIP-4, AFIP-6MKII, and AFIP-7. The following fuel swelling correlation due to solid and gaseous fission products was established with fuel thickness data from the AFIP-6MKII experiment excluded:

![](images/921dcd55e624040f64d2c0d07cda491a5dbbc1a97b0a54293d03e7f60d8a2b79.jpg)

Equation 2

where ???? is fission density in ????????????????????????????/???? 3. In the next sections of this report, this swelling correlation will be refered to as “excluding AFIP-6 MKII”.

(iii) 95% Upper CL of swelling correlation including AFIP-6 MKII data [12]:

When the data from the AFIP-6 MK-II experiment are included, higher fuel swelling will be predicted based on equation (64) presented in the “Preliminary Report on U-Mo Monolithic Fuel for Research Reactors, INL/EXT-17-40975, Revision 1”[12]. Moreover, the 95% upper confidence limit (UCL) of that swelling correlation will predict even higher fuel swelling to take place. Thus, the following 95% UCL of swelling correlation including AFIP-6 MK-II data was considered in this work as an extreme case (i.e. conservative approach).

![](images/3307a2186972c0bb7dd3f5d0c964e45b6d21266ed2571f07aff6c164a9cd8ad7.jpg)

Equation 3

where ???? is fission density in ????????????????????????????/???? 3. In the next swctions of this report, this correlation will be refered to as “95% UCL including AFIP-6 MKII”.

The aforementioned three fuel swelling correlations are plotted and compared in Figure 3. It can be seen that fuel swelling as predicted by the Kim swelling correlation is more or less the same as that predicted by the swelling correlation excluding AFIP-6 MKII data up to \~1.8 × 1027????????????????????????????/????3. The swelling correlation excluding AFIP-6 MKII predicts relatively higher fuel swelling at the maximum fission density experienced by plate 23 in the MURR LEU fuel element (indicated by red dashed live). As expected, the 95% UCL including AFIP-6 MKII correlation predicts higher fuel swelling at all fission densities.

![](images/ec99397e077f4781057061bc5737801753f4eafd1771e18bfb0967bf3b077dbc.jpg)  
Figure 3. Comparison of fuel swelling correlations modeled in this work.

## 2.4.2 Irradiation Creep Model

In this work, irradiation creep of irradiated U-10Mo fuel was modeled following the relation proposed by Kim et al [13] which expresses the creep strain rate as follows:

![](images/fd49fe9d66b25211216ed4ddc6c3b27d1d5026bbfa8e8807f09df5babfcf559d.jpg)

Equation 4

where ????° is creep strain rate (1/sec), ???? is irradiation creep rate coefficient (cm3 /MPa-fission), ???? is equivalent stress (MPa), and ????° is fission density rate (fission/ cm3 -sec). Kim et al determind the value of the creep rate coeeficient ???? to be 500 × 10−25 (cm3 /MPa-fission) by performing FEA on a 2-D model of U-10Mo monolithic mini-plate where the Kim swelling correlation was used to describe fuel swelling. Then, ???? was empirically adjusted until the thickness of simulated plate as predicted by FEA is in good agreement with corresponding experimental measurements of local plate thickness. Thus, the value of A = 500 × 10−25 (cm3 /MPa-fission) was derived considering the Kim swelling correlation and measured data. Accordingly, this value should be revised and evaluated when other swelling correlations are used to describe the swelling behavior of U-10Mo fuel. In the present study, it was decided to model the irradiation creep behavior of U-10Mo fuel considering the model proposed by Kim et al. with the following values of creep rate coefficient: 750, 500, 250 and 5 (cm3 /MPa-fission).

Thus, the thermo-mechnaical behavior of plate 23 in MURR LEU fuel element was simulated considering three swelling correlations along with four different values of creep rate coefficient.

## 3 Results and Discussion

As mentioned earlier in this report, the main goal of this study is to determine the maximum increase in the thickness of plate 23 at EOL considering various combinations of swelling correlations and values of creep rate coefficient. For each of the three swelling correlations discussed in section (2.4.1), peak displacement along the thickness direction of plate 23 was determined in four cases corresponding to creep rate coefficient of 750, 500, 250 and 5 (× 10−25 cm3 /MPa-fission).

Figure 4 shows the swelling strain component in the U-10Mo fuel core as predicted by the FE simulations considering the three swelling correlations of interest. According to the data in Table 3, the FE results of fuel swelling are in very good agreement with fuel swelling as directly estimated by Equation 1, 2, and 3 at EOL (fission desnity of 2.62 × 1027 ????????????????????????????/????3 , see Figure 2).

![](images/184a3da02c6ec671f9fb37b6a9eb0055c2889cd7c0d987f2b656eda493fdad88.jpg)  
(a)

![](images/f5e11127fc23f6c8d5698519aa26cb4f1e58c62c6658b4b38e6957fba017316c.jpg)

![](images/27a5f898a9a2011e21f50d6f4aa8b51b478a16ac6fc3ffa8d807896c33422190.jpg)  
(b)

![](images/3565cded3b39c90ef35e349a2990f27f1e06044845d26df71ba786b5ce0f08a4.jpg)  
(c)  
Figure 4. Swelling strain contours in U-10Mo fuel core of plate 23 considering (a) Kim swelling correlation, (b) excluding AFIP-6 MKII swelling correlation, and (c) 95% UCL including AFIP-6 MKII correlation.

Table 3: Fuel swelling in plate 23 at 2.62 × 1027 ????????????????????????????/????3 (EOL) from FEA and calculations
<table><tr><td rowspan=1 colspan=1>Swelling correlation</td><td rowspan=1 colspan=1>Swelling strain fromFEA,%</td><td rowspan=1 colspan=1>Swelling strain fromcalculations, %</td></tr><tr><td rowspan=1 colspan=1>Kim swelling correlation</td><td rowspan=1 colspan=1>13.1</td><td rowspan=1 colspan=1>13.1</td></tr><tr><td rowspan=1 colspan=1>Excluding AFIP-6 MKII correlation</td><td rowspan=1 colspan=1>14.5</td><td rowspan=1 colspan=1>14.5</td></tr><tr><td rowspan=1 colspan=1>95% UCL including AFIP-6 MKII correlation</td><td rowspan=1 colspan=1>20.7</td><td rowspan=1 colspan=1>19.8</td></tr></table>

## 3.1 FEA with Kim Swelling Correlation

As seen from Figure 5, the location of peak displacement in plate 23 U-10Mo fuel core along thickness direction does not change with variation in in creep rate coefficient in the range between 750 and 5 (× 10−25 cm3 /MPa-fission). Maximum outboard increase in fuel core thickness was observed along longitudinal mid-plane whereas maximum inboard increase was observed at the edge of the fuel core.

Furthermore, FEA revealed that higher peak dispalcement along the thickness direction of the fuel core occurred with A = 5 (× 10−25 cm3 /MPa-fission) compared to creep rate coefficient varying between 750 and 250 (× 10−25 cm3 /MPa-fission).

![](images/61492c10e8359233a2fbce1f1f582589ab62010bb7579804a11c372c735fa33b.jpg)  
(a) A = 750

![](images/bbc0a125d1d78ee200e6393a46b028280ad003d2d152466d8fac63747a536d15.jpg)  
(b) A = 500

![](images/1f0e51f6289007f694ba8840c032712441c3cc423d5db4b5be6041f403a202bc.jpg)  
(c) A = 250

![](images/17913ce641fec41b9e65aa191865f537268c33c2c1f4df3ff7ad36a780b9d582.jpg)  
(d) A = 5  
Figure 5. Contours of displacement along thickness direction in plate 23 considering Kim swelling correlation and different values of creep rate coefficient (× 10−25 cm3 /MPa-fission).

Since the maximum displacement along thickness direction was observed along the longitudinal midplane of the fuel, the plate thickness profile was analyzed along the same mid-plane as illustrated in Figure 6. From Figure 7a, it can be seen that displacement through the thickness direction at EOL along the longitudinal mid-plane of plate 23 did not change as the creep rate coeffienct varied between 750 and 250 (× 10−25 cm3 /MPa-fission). Larger displacement along plate thickness direction was observed with creep rate coefficient of 5 (× 10−25 cm3 /MPa-fission). This last observation is mainly due to the lack of stress relaxation mechanism in this case combined with the curved geometry of the plate. However, about 2.039 mm of coolant channel 24 (outboard) remains unblocked with the large displacement observed with creep rate coefficient of 5 (× 10−25 cm3 /MPa-fission) as shown in Figure 7b.

Interestingly, FEA revealed that variation in creep rate coefficient has insignificnt effect on the observed net increase in plate thickness as shown in Figure 8. The maximum net increase in plate 23 thickness with fuel swelling described by Kim correlation was found to be 0.051 mm.

![](images/21526b6450a23a679dad18e3d7aa89c9162e096547f58a0bc4e8e8d01fcb258b.jpg)  
Figure 6. Schematic of plate 23 longitudinal mid-plane used for the analysis of plate thickness at EOL.

![](images/e84b85d955c32338f00b1c73da0c0dd21b6fc122edee1ebb34a956fcd7713719.jpg)

(a)  
![](images/59aef4bbb81b78a8a5cd7807bd761df2212b2c0293316985844a6307bd32bc6c.jpg)  
(b)  
Figure 7. Effect of variation in creep rate coefficient on displacement profile along longitudinal midplane of plate 23 at EOL with Kim swelling correlation. Positive and negative Y-axis represents outboard and inboard directions, respectively.

![](images/ac8acbf7e02516cb6e3ce016b63e4d9b74f3daf89d2c1832347a905b3c2a1ca0.jpg)  
Figure 8. Net increase in plate 23 thickness along longitudinal mid-plane at EOL considering Kim swelling correlation with various values of creep rate coefficient (× 10−25 cm3 /MPa-fission).

## 3.2 FEA with Swelling Correlation Excluding AFIP-6 MKII Data

The analysis presented in section 3.1 was repeated for the swelling correlation excluding AFIP-6 MKII data. In this case, the maximum displacement was observed along the longitudinal mid-plane of plate 23 regardless of the creep rate coefficient (see Figure 9).

![](images/e493a79f6a2030700f30e019d96c6ed8c2dd3b547cf0d72219da7ab7ad8a917d.jpg)  
(a) A = 750

![](images/ee880aab7424064052c138a683615e11d70b978f26716f1690423d2bb8b7242c.jpg)  
(b) A = 500

![](images/c7bede7b544dcfb70248193b61b6d71443990b864375d6408e31b6e779444b34.jpg)  
(c) A = 250

![](images/ccce320a87821cd6e089b97fcce02b15fc148ca62b261a998dae3baaf0f6fc2b.jpg)  
(d) A = 5  
Figure 9. Contours of displacement along thickness direction in plate 23 with swelling correlation excluding AFIP-6 MKII data and different values of creep rate coefficient (× 10−25 cm3 /MPa-fission).

From Figure 10a, displacement profiles are more or less the same as creep rate coefficient varied between 750 and 250 250 (× 10−25 cm3 /MPa-fission) whereas relatively larger displcamant was found with creep rate coefficient of 5 250 (× 10−25 cm3 /MPa-fission). In this case, about 1.997 mm of coolant channel 24 (outboard) remains unblocked with the large displacement observed with creep rate coefficient of 5 (× 10−25 cm3 /MPa-fission) as shown in Figure 10b.

As shown in Figure 11, the net increase in plate thickness has only a minimal dependence on the creep rate coefficient for values between 750 and 250 (× 10−25 cm3 /MPa-fission). The maximum net increase in plate 23 thickness was found to be 0.055 mm. This is about 0.004 mm higher than the net increase when fuel swelling was described by the Kim swelling correlation (see section 3.1, Figure 7a).

![](images/d9f25f48f9e2a5a99012be47a3411255bb41cac87c6c582b338f40a55674afa0.jpg)

(a)  
![](images/c9f95d3b6711a8e6d15f6bb2983094bf8ff6974ab504ba30d8a9e1815e460f8b.jpg)  
(b)  
Figure 10. Effect of variation in creep rate coefficient on displacement profile along longitudinal midplane of plate 23 at EOL with swelling correlation excluding AFIP-6 MKII data. Positive and negative Y-axis represents outboard and inboard directions, respectively.

![](images/ba6de2f680a89d1f77332970ad88f48d4daa74071349efe9328b83d0ba876cdc.jpg)  
Figure 11. Net increase in plate 23 thickness along longitudinal mid-plane at EOL with swelling correlation excluding AFIP-6 MKII and various values of creep rate coefficient (× 10−25 cm3 /MPafission).

## 3.3 FEA Considering 95% UCL of Correlation Including AFIP-6 MKII Data

All observations reported in the previous two sections were found when the fuel swelling is predicted based on the 95% UCL of the correlation including AFIP-6 MKII data. As shown in Figure 12, the location of the maximum displacement along plate thickness is insensitive to variation in the creep rate coeffienct.

![](images/667c6311bd110017a884dbae3a484e235171b3caac5b1a6d7f528ac383c6507f.jpg)  
(a) A = 750

![](images/a8a567839ba1c2c83a28dd6c6a9379c3976242af2e9db0280d34dd7fda11d7fe.jpg)  
(b) A = 500

![](images/c230adfc252678bb4ae7b053cf887c3430eb9b9ce0a67a27ff1be2adda0556a1.jpg)  
(c) A = 250

![](images/19dc8d0aacd551599b43faddc22cacfaca513721407041a30f77be50f65c2b33.jpg)  
(d) A = 5  
Figure 12. Contours of displacement along thickness direction in plate 23 considering 95% UCL of swelling correlation including AFIP-6 MKII data and different values of creep rate coefficient (× 10−25 cm3 /MPa-fission).

Similar to the analysis presented in the previous two sections, Figure 13a shows that relatively larger displacemnt was observed when the creep rate coefficient was set to 5 (× 10−25 cm3 /MPa-fission) compared to higher values up to 750 (× 10−25 cm3 /MPa-fission).

Moreover, about 1.866 mm of coolant channel 24 remains unblocked with creep rate coefficient of 5 (× 10−25 cm3 /MPa-fission). Finally, 0.083 mm was found to be the maximum increase in plate thickness in this case (Figure 13b).

![](images/7f1802c7dea850f1d37cc21ee1a42bc564e6659ba630e69e4a919e5075998553.jpg)

(a)  
![](images/19885e4469d4329adce61b9850c3127f5ff9b17a21f247f5af5c9f6df0ae194e.jpg)  
(b)  
Figure 13. Effect of variation in creep rate coefficient on displacement profile along longitudinal midplane of plate 23 at EOL with the 95% UCL swelling correlation including AFTP-6 MKII data. Positive and negative Y-axis represents outboard and inboard directions, respectively.

![](images/91e7fec8c4992ef0f4286e64aa880ebf1283848ac50a51250e91417d95d79e12.jpg)  
Figure 14. Net increase in plate 23 thickness along longitudinal mid-plane at EOL with 95% UCL of swelling correlation including AFIP-6 MKII data and various values of creep rate coefficient (× 10−25 cm3 /MPa-fission).

Since the net maximum increase in the thickness of plate 23 in the MURR LEU fuel element represents the most important outcome from this study, the value of the maximum increase in the plate thickness at EOL across all combinations of fuel swelling correlations and creep rate coefficients are listed in Table 4. Based on the FEA results, the maximum increase in the plate 23 thickness is 0.083 mm and it occurs when fuel swelling is described by the 95% UCL of swelling correlation including AFIP-6 MKII data and creep rate coefficient in the range between 7500 and 250 (× 10−25 cm3 /MPa-fission).

Table 4: Maximum increase in the thickness of plate 23 at EOL under different combinations of swelling correlations and creep rate coefficients (× 10−25 cm3 /MPa-fission).
<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=4>Maximum increase in plate thickness, mm</td></tr><tr><td rowspan=1 colspan=1>Swelling correlation</td><td rowspan=1 colspan=1>A= 750</td><td rowspan=1 colspan=1>A= 500</td><td rowspan=1 colspan=1>A= 250</td><td rowspan=1 colspan=1>A=5</td></tr><tr><td rowspan=1 colspan=1>Kim swelling correlation</td><td rowspan=1 colspan=1>0.051</td><td rowspan=1 colspan=1>0.051</td><td rowspan=1 colspan=1>0.051</td><td rowspan=1 colspan=1>0.050</td></tr><tr><td rowspan=1 colspan=1>Excluding AFIP-6 MKII correlation</td><td rowspan=1 colspan=1>0.055</td><td rowspan=1 colspan=1>0.055</td><td rowspan=1 colspan=1>0.055</td><td rowspan=1 colspan=1>0.054</td></tr><tr><td rowspan=1 colspan=1>95% UCL including AFIP-6 MKII correlation</td><td rowspan=1 colspan=1>0.083</td><td rowspan=1 colspan=1>0.083</td><td rowspan=1 colspan=1>0.083</td><td rowspan=1 colspan=1>0.081</td></tr></table>

## 3.4 Stress analysis

Table 5 lists the peak equivalent stress experienced by the U-10Mo fuel core under the various combinations of fuel swelling correlations and creep rate coefficient values simulated in this work. It can be seen that the decrease in creep rate coefficient from 250 to 5 (× 10−25 cm3 /MPa-fission) resulted in a noticeable increase in the peak equivalent stress of the fuel core. This is attributed to the lack of stress relaxation mechanisms in the case of such a very low creep rate coefficient.

Furthermore, the influence of the swelling correlation on the peak equivalent stress in the fuel core is noticeable only at the lowest creep rate coefficient attempted in this study. According to reference [10], the maximum operating temperature experienced by the U-10Mo fuel core is about 150°C at which the yield stress of the material is 805 MPa [12]. In all the cases simulated in this work, the peak equivalent stress in the U-10Mo fuel core is well below the yield stress of the material. Thus, no plastic deformation occurred in the fuel core under any combination of fuel swelling correlation and creep rate coefficient values simulated in this work.

Table 5: Peak equivalent stress in U-10Mo fuel core.
<table><tr><td rowspan=1 colspan=1></td><td rowspan=1 colspan=4>Peak equivalent stress, MPa</td></tr><tr><td rowspan=1 colspan=1>Swelling correlation</td><td rowspan=1 colspan=1>A= 750</td><td rowspan=1 colspan=1>A=500</td><td rowspan=1 colspan=1>A= 250</td><td rowspan=1 colspan=1>A=5</td></tr><tr><td rowspan=1 colspan=1>Kim swelling correlation</td><td rowspan=1 colspan=1>31.34</td><td rowspan=1 colspan=1>31.54</td><td rowspan=1 colspan=1>32.34</td><td rowspan=1 colspan=1>243.40</td></tr><tr><td rowspan=1 colspan=1>Excluding AFIP-6 MKII correlation</td><td rowspan=1 colspan=1>31.42</td><td rowspan=1 colspan=1>31.64</td><td rowspan=1 colspan=1>32.79</td><td rowspan=1 colspan=1>262.67</td></tr><tr><td rowspan=1 colspan=1>95%UCL including AFIP-6 MKII correlation</td><td rowspan=1 colspan=1>31.34</td><td rowspan=1 colspan=1>31.20</td><td rowspan=1 colspan=1>32.70</td><td rowspan=1 colspan=1>342.54</td></tr></table>

## 4 Summary

In this work, FEA was used to evaluate the swelling and creep behavior of plate 23 in a MURR LEU U-10Mo fuel element. The thermo-mechanical behavior of plate 23 was simulated under typical irradiation conditions of the MURR LEU core. Fuel swelling was described considering three swelling correlations: the Kim swelling correlation, a swelling correlation excluding AFIP-6 MKII data, and the 95% upper confidence limit of the correlation including AFIP-6 MKII, where the last one represents an extreme case (most conservative estimate of fuel swelling). Furthermore, irradiation creep strain rate in the U-10Mo fuel was modeled such that it linearly varies with equivalent stress, fission rate and empirical creep rate coefficient.

The deformation profile and corresponding increase in the thickness of plate 23 at EOL were determined considering various combinations of the aforementioned three swelling correlations and creep rate coefficients of 750, 500, 250, and 5 (× 10−25 cm3 /MPa-fission). The following remarks were made:

• Maximum displacement along the thickness direction of plate 23 was found at the same location in all simulated combinations of swelling correlations and creep rate coefficients.

• Under the same swelling correlation, larger outboard displacement was always observed at the lowest creep rate coefficient attempted in this study (5 × 10−25 cm3 /MPa-fission).

• Variation in the creep rate coefficnet has an insignificant effect on the net increase in plate thickness for the same swelling correlation.

• Maximum increase in plate thickness was found to be 0.083 mm and it occurs when fuel swelling is described by the 95% UCL of the correlation including AFIP-6 MKII data and creep rate coefficient in the range between 750 and 250 (× 10−25 cm3 /MPa-fission).

• Under any of the three swelling correlations considered in this work, the lack of stress relaxation mechanisms in the case of creep rate coefficient of 5 (× 10−25 cm3 /MPa-fission) resulted in a noticeable increase in the peak equivalent stress in the U-10Mo fuel core. However, the fuel core did not experience any plastic deformation since the peak equivalent stress in all cases was well below the yield stress of the material.

## 5 Acknowledgements

This work was sponsored by the U.S. Department of Energy, Office of Material Management and Minimization in the U.S. National Nuclear Security Agency Office of Defense Nuclear Nonproliferation Office under Contract DE-AC02-06CH11357.

## Appendix A

## Finite Element Meshing Profile Optimization and Analysis

Initially, the finite element (FE) geometrical model of plate 23 was prepared following a welloptimized fine-mesh profile that was previously used to model prototypic U-10Mo monolithic miniplates [14]. In that meshing profile, the U-Mo fuel core section was represented by six layers along the plate thickness direction, and each of the Zr diffusion barrier and the cladding sections was represented by three layers (on each side of the fuel core). However, due to the larger width and length of the MURR plate 23 relative to the dimensions of the mini-plates, the size of the input file representing the FE model for plate 23 was approximately 1 GB compared to few tens of MB for the corresponding monolithic mini-plate input file. Consequently, it was not possible to consider such a fine-mesh profile considering the available computational resources, as well as the extremely large size of the output database files.

The FE model of plate 23 was then meshed considering various combinations of the number of layers representing the three sections of the plate along the thickness direction. A coarse-mesh profile with the fuel core represented by two layers along the plate thickness directions and each of the Zr diffusion barrier and cladding section represented by one layer (on each side of the fuel core) resulted in a model input file of size ∼ 41 MB and output database file of ∼ 3.8 GB. The FE model with that meshing profile was considered as a full-size baseline model for plate 23.

A sub-modeling technique was used to determine the effect of variation in meshing profile on the displacement component along the plate thickness direction. A region of interest that envelopes the highest fission density in the fuel core (see Figure 2) around the transverse mid-section of plate 23 was determined and a FE sub-model was developed to represent that region as depicted by Figure 15. The region of interest was simulated in two cases corresponding to a total length of 6 inch (2 inch and 4 inch around plate 23 transverse mid-plane) and 10 inch (4 inch and 6 inch around plate 23 transverse mid-plane), separately.

![](images/8bfd868d37572b0f4ea71038ac47b02504439097a6cf3df084277fdd1d518645.jpg)  
Figure 15. Schematic of the region of interest around the fuel core mid-section.

A fine mesh profile along the thickness direction of the plate was adopted for the region of interest. In the fine mesh profile, the fuel core section was represented by a total of six layers, the Zr diffusion barrier was represented by two layers (on each side of the fuel core), and the cladding section was represented by four layers (on each side of the fuel core). The purpose of this approach is to achieve results of high accuracy for the sub-model within reasonable computation time.

Two FE sub-models were developed for the region of interest shown in Figure 15 as follows: submodel (1): with X = 2 inch and Y = 4 inch (i.e. 6 inch length) and sub-model (2): with X = 4 inch and Y = 6 inch (i.e. 10 inch length). In the sub-modeling technique, the displacement data at all-time points from the coarse-mesh full-size model were used as boundary conditions for the fine-mesh submodels. Figure 16 shows contours of the displacement component along the thickness direction of plate 23 from the coarse-mesh full-size model and the two fine-mesh sub-models1.

![](images/40aab8c59da10d38d4c6dddc2cad5ef56dd858ca007b497c200047e6c5acd443.jpg)  
(a)

![](images/5e3cd2ae7bb5777efa8ee5a1cc26fce33dd481dd7f171d4e8ed58c2193cc6117.jpg)  
(b)

![](images/07256c58727deb2b05ff4650715282090914d72ea8e415f6d4a40bf69aba51fe.jpg)  
(c)  
Figure 16. Contours of displacement component along thickness directions of plate 23 from coarse-mesh full-size model (a) and fine-mesh profile sub-models measuring 6 inch (b) and 10 inch (c) in length.

The displacement peaks found at the edges of the two sub-models (Figure 16 b and c) are attributed to the truncation of the FE geometrical model at the edges of the region of interest which is commonly referred to as the edge effect. To exclude the edge effect, the displacement component along the plate thickness direction was reanalyzed in the two sub-models where the edge regions were excluded as shown in Figure 17.

![](images/10e6a6057e77e1ac0c004bcf44422cc87e9a36a3d2d9ae9496ef412744beb77f.jpg)  
(a)

![](images/ff22fa9716dd6d74f10a621231ffa59cccda367470a10a070525b84525868798.jpg)  
Figure 17. Contours of displacement component along thickness directions from (a) 6 inch and (b) 10 inch in length sub-models of plate 23 excluding the edge effect region in both cases.

It can be seen that the peak displacement along plate thickness in a 6 inch length sub-model is 0.290 mm (Figure 17a) whereas the corresponding peak displacement in the sub-model with a 10 inch length is 0.254 mm (Figure 17b). The larger displacement observed in the 6 inch sub-model can be attributed to residual edge effects compared to the 10 inch sub-model where the excluded edge effect regions are far enough from the sub-model mid-plane. Although both the 6 inch sub-model and 10 inch sub-model possess the same mesh profile, the 10 inch sub-model is affected less by the edge effect, and is thus considered more representative of the full size plate. Furthermore, the peak displacement along the plate thickness direction from the fine-mesh 10 inch length sub-model, following the exclusion of the edge effect regions, matches that of the coarse-mesh full-size model (see Figure 16a and Figure 17b). Because of the excellent agreement between the peak displacement predicted by the coarse-mesh full-size model of plate 23 and fine-mesh sub-model with a 10 inch length, the coarse-mesh full-size model of plate 23 was considered satisfactory for the analyses presented in this study.

## References

[1] J. L. Snelgrove, G. L. Hofman, M. K. Meyer, C. L. Trybus, and T. C. Wiencek, “Development of veryhigh-density low-enriched-uranium fuels,” Nucl. Eng. Des., vol. 178, pp. 119–126, 1997.

[2] M. K. Meyer et al., “IRRADIATION PERFORMANCE OF U-Mo MONOLITHIC FUEL,” Nucl. Eng. Technol., vol. 46, no. 2, pp. 169–182, Apr. 2014.

[3] J. Rest, Y. S. Kim, G. L. Hofman, M. K. Meyer, and S. L. Hayes, “U-Mo Fuels Handbook, Version 1.0,” ANL-09/31, Argonne National Laboratory, 2006.

[4] E. H. Wilson, A. Bergeron, J. A. Stillman, T. A. Heltemes, D. Jaluvka, and L. Jamison, “U.S. HIGH PERFORMANCE RESEARCH REACTOR CONVERSION PROGRAM: AN OVERVIEW ON ELEMENT DESIGN,” RRFM 2017, Rotterdam, Netherlands.

[5] J. Stillman, “Technical Basis in Support of the Conversion of the University of Missouri Research Reactor (MURR) Core from Highly-Enriched to Low-Enriched Uranium – Core Neutron Physics," ANL/RERTR/TM-12-30, Argonne National Laboratory, 2012.

[6] E. E. Feldman, “Technical Basis in Support of the Conversion of the University of Missouri Research Reactor (MURR) Core from Highly-Enriched to Low-Enriched Uranium – Steady-State Thermal-Hydraulic Analysis," ANL/RERTR/TM-12-37, Argonne National Laboratory, 2012.

[7] J. Stillman, “Low-Enriched Uranium Conversion Preliminary Safety Analysis Report for the University of Missouri Research Reactor," University of Missouri Research Reactor, Columbia, MO, submitted to the U.S. Nuclear Regulatory Commission, 2017.

[8] Y. S. Kim and G. L. Hofman, “Fission product induced swelling of U–Mo alloy fuel,” J. Nucl. Mater., vol. 419, no. 1–3, pp. 291–301, Dec. 2011.

[9] G. L. Hofman and Y. S. Kim, “FISSION INDUCED SWELLING AND CREEP OF URANIUMMOLYBDENUM ALLOY FUEL,” RRFM 2009, Vienna , Austria.

[10] J. Stillman, E. Wislon, L. Foyto, K. Kutikkad, J. C. McKibben, and N. Peters, “Irradiation Demonstration Element Design Parameters for MURR LEU U-Mo Fuel Conversion," ANL/RTR/TM-18/4, Argonne National Laboratory, 2018.

[11] “ABAQUS/ CAE 6.14 Documentation Collection," Providence, RI: Dassault Systemes Simulia Corp., 2014.

[12] M. Meyer et al., “Preliminary Report on U-Mo Monolithic Fuel for Research Reactors," INL/EXT-17-40975, Revision 1, 2017.

[13] Y. S. Kim, G. L. Hofman, J. S. Cheon, A. B. Robinson, and D. M. Wachs, “Fission induced swelling and creep of U–Mo alloy fuel,” J. Nucl. Mater., vol. 437, no. 1–3, pp. 37–46, June 2013.

[14] W. Mohamed and H. S. Roh, “INFLUENCE OF MATERIALS PROPERTIES ON THE IRRADIATION BEHAVIOR OF U-10MO MONOLITHIC MINI-PLATES,” Proceedings of the ASME 2015 International Mechanical Engineering Congress and Exposition IMECE2015, 2015, no. 630, pp. 1–14.

Nuclear Science and Engineering Division

Argonne National Laboratory

9700 South Cass Avenue, Bldg. 208

Argonne, IL 60439

www.anl.gov
