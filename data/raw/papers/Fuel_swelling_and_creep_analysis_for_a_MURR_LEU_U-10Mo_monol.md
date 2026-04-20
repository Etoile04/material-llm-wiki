# Fuel swelling and creep analysis for a MURR LEU U-10Mo monolithic plate

---

                                           ANL/RTR/TM-18/19




Fuel Swelling and Creep Analysis for a MURR
LEU U-10Mo Monolithic Plate




Nuclear Science and Engineering Division
About Argonne National Laboratory
Argonne is a U.S. Department of Energy laboratory managed by UChicago Argonne, LLC
under contract DE-AC02-06CH11357. The Laboratory’s main facility is outside Chicago, at
9700 South Cass Avenue, Argonne, Illinois 60439. For information about Argonne
and its pioneering science and technology programs, see www.anl.gov.




DOCUMENT AVAILABILITY
     Online Access: U.S. Department of Energy (DOE) reports produced after 1991 and a
     growing number of pre-1991 documents are available free via DOE’s SciTech Connect
     (http://www.osti.gov/scitech/)


Reports not in digital format may be purchased by the public from the
National Technical Information Service (NTIS):
     U.S. Department of Commerce
     National Technical Information Service 5301 Shawnee Rd
     Alexandria, VA 22312
     www.ntis.gov
     Phone: (800) 553-NTIS (6847) or (703) 605-6000
     Fax: (703) 605-6900
     Email: morders@ntis.gov


Reports not in digital format are available to DOE and DOE contractors from the
Office of Scientific and Technical Information (OSTI):
     U.S. Department of Energy
     Office of Scientific and Technical Information
     P.O. Box 62
     Oak Ridge, TN 37831-0062
     www.osti.gov
     Phone: (865) 576-8401
     Fax: (865) 576-5728
     Email: reports@osti.gov




Disclaimer
This report was prepared as an account of work sponsored by an agency of the United States
Government. Neither the United States Government nor any agency thereof, nor UChicago Argonne,
LLC, nor any of their employees or officers, makes any warranty, express or implied, or assumes any
legal liability or responsibility for the accuracy, completeness, or usefulness of any information,
apparatus, product, or process disclosed, or represents that its use would not infringe privately owned
rights. Reference herein to any specific commercial product, process, or service by trade name,
trademark, manufacturer, or otherwise, does not necessarily constitute or imply its endorsement,
recommendation, or favoring by the United States Government or any agency thereof. The views and
opinions of document authors expressed herein do not necessarily state or reflect those of the United
States Government or any agency thereof, Argonne National Laboratory, or UChicago Argonne, LLC.
                                                                 ANL/RTR/TM-18/19




Fuel Swelling and Creep Analysis for a MURR
LEU U-10Mo Monolithic Plate




prepared by

Walid Mohamed1, Hee Seok Roh1, John Stillman2, Erik Wilson2
1 Chemical and Fuel Cycle Technologies Division, Argonne National Laboratory


2 Nuclear Science and Engineering Division, Argonne National Laboratory




March 2019
(This page left intentionally blank)
                                                                                                                                              ANL/RTR/TM-18/19


Table of Contents
1    Introduction........................................................................................................................................1
2    Simulation and Model Setup ..........................................................................................................2
     2.1      Irradiation Parameters ...................................................................................................................................... 2
     2.2      Finite Element Model ......................................................................................................................................... 3
     2.3      Materials Models and Correlations............................................................................................................... 4
     2.4      Evaluation of Swelling and Creep Models for U-10Mo Fuel ............................................................... 4
               2.4.1 Fuel Swelling Correlations ................................................................................................................. 4
               2.4.2 Irradiation Creep Model ...................................................................................................................... 6
3    Results and Discussion ....................................................................................................................7
     3.1      FEA with Kim Swelling Correlation .............................................................................................................. 8
     3.2      FEA with Swelling Correlation Excluding AFIP-6 MKII Data ........................................................... 10
     3.3      FEA Considering 95% UCL of Correlation Including AFIP-6 MKII Data ...................................... 12
     3.4      Stress analysis ..................................................................................................................................................... 14
4    Summary ........................................................................................................................................... 15
5    Acknowledgements ........................................................................................................................ 15
Appendix A............................................................................................................................................. 16
References ............................................................................................................................................. 19




Fuel Swelling and Creep Analysis for a MURR
LEU U-10Mo Monolithic Plate                                                                                                                                                          i
                                                                                                                                                                ANL/RTR/TM-18/19


List of Figures
Figure 1. Local-to-average fission density distribution in the U-10Mo foil of plate 23 as modeled in this
work. .............................................................................................................................................................................................. 3
Figure 2. Fission density distribution in the U-10Mo foil of plate 23 at EOL as modeled in this work........ 3
Figure 3. Comparison of fuel swelling correlations modeled in this work.................................................. 6
Figure 4. Swelling strain contours in U-10Mo fuel core of plate 23 considering (a) Kim swelling
correlation, (b) excluding AFIP-6 MKII swelling correlation, and (c) 95% UCL including AFIP-6 MKII
correlation. ................................................................................................................................................................................. 7
Figure 5. Contours of displacement along thickness direction in plate 23 considering Kim swelling
correlation and different values of creep rate coefficient (× 10 − 25 cm3/MPa-fission). ......................... 8
Figure 6. Schematic of plate 23 longitudinal mid-plane used for the analysis of plate thickness at EOL.
......................................................................................................................................................................................................... 9
Figure 7. Effect of variation in creep rate coefficient on displacement profile along longitudinal mid-
plane of plate 23 at EOL with Kim swelling correlation. Positive and negative Y-axis represents
outboard and inboard directions, respectively. ........................................................................................................... 9
Figure 8. Net increase in plate 23 thickness along longitudinal mid-plane at EOL considering Kim
swelling correlation with various values of creep rate coefficient (× 10 − 25 cm3/MPa-fission)....... 10
Figure 9. Contours of displacement along thickness direction in plate 23 with swelling correlation
excluding AFIP-6 MKII data and different values of creep rate coefficient (× 10 − 25 cm3/MPa-
fission)........................................................................................................................................................................................ 10
Figure 10. Effect of variation in creep rate coefficient on displacement profile along longitudinal mid-plane
of plate 23 at EOL with swelling correlation excluding AFIP-6 MKII data. Positive and negative Y-axis
represents outboard and inboard directions, respectively................................................................................... 11
Figure 11. Net increase in plate 23 thickness along longitudinal mid-plane at EOL with swelling correlation
excluding AFIP-6 MKII and various values of creep rate coefficient (× 10 − 25 cm3/MPa-fission). ........ 12
Figure 12. Contours of displacement along thickness direction in plate 23 considering 95% UCL of
swelling correlation including AFIP-6 MKII data and different values of creep rate coefficient (× 10 −
25 cm3/MPa-fission). ........................................................................................................................................................... 12
Figure 13. Effect of variation in creep rate coefficient on displacement profile along longitudinal mid-plane
of plate 23 at EOL with the 95% UCL swelling correlation including AFTP-6 MKII data. Positive and
negative Y-axis represents outboard and inboard directions, respectively. .................................................. 13
Figure 14. Net increase in plate 23 thickness along longitudinal mid-plane at EOL with 95% UCL of
swelling correlation including AFIP-6 MKII data and various values of creep rate coefficient (× 10 −
25 cm3/MPa-fission). ........................................................................................................................................................... 14




Fuel Swelling and Creep Analysis for a MURR
LEU U-10Mo Monolithic Plate                                                                                                                                                                             ii
                                                                                                                                                             ANL/RTR/TM-18/19


List of Tables
Table 1: Variation in average power and fission densities with time for plate 23 in MURR LEU fuel element
[10] ................................................................................................................................................................................................. 2
Table 2: Nominal dimensions of plate 23 as modeled in this work [10].................................................................. 4
Table 3: Fuel swelling in plate 23 at 2.62 × 1027 𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓/𝑚𝑚3 (EOL) from FEA and calculations......... 7
Table 4: Maximum increase in the thickness of plate 23 at EOL under different combinations of swelling
correlations and creep rate coefficients (× 10 − 25 cm3/MPa-fission). ................................................................ 14
Table 5: Peak equivalent stress in U-10Mo fuel core. ................................................................................................. 15




Fuel Swelling and Creep Analysis for a MURR
LEU U-10Mo Monolithic Plate                                                                                                                                                                         iii
                                                                                       ANL/RTR/TM-18/19




1 Introduction
     The U.S. DOE National Nuclear Security Administration (NNSA) Office of Material Management
and Minimization (M3) conversion program aims to eliminate or minimize the civilian use of weapons-
grade highly enriched uranium (HEU) both domestically and internationally. A key approach to achieve
this goal is the conversion of research and test reactors from HEU to high density, low-enriched uranium
fuels (LEU, < 20% U235) [1].

     Over the past few decades, U-Mo alloys were considered to be the most promising candidates for the
conversion of research and test reactors to LEU fuels due to their stable irradiation performance [2]. U-Mo
alloys showed recognized dimensional stability and acceptable swelling behavior compared to other forms
of fuels under typical irradiation conditions of research and test reactors. The observed stability of U-Mo
alloys is attributed to the Mo content, which stabilizes the cubic gamma phase of the fuel. Furthermore, U-
Mo alloys are recognized for their low neutron absorption cross section when compared to other fuel
materials proposed for the conversion program [3].

     The recent U-Mo fuel design adopted by the U.S. for the conversion of its High-Performance Research
Reactors (USHPRR) is a monolithic plate form characterized by a high density LEU-10Mo fuel core. The
U-10Mo monolithic plate design consists of U-10Mo fuel core sandwiched between Zr diffusion barriers
and encapsulated in Al-based AA6061 cladding. Six reactors (including one critical facility) constitute the
USHPRR fleet that will primarily use U-10Mo monolithic fuel for LEU conversion [4]. Among these
reactors, the University of Missouri Research Reactor (MURR) is the main focus of this study.

       The conversion of the MURR from the use of HEU to LEU is currently in progress. The University of
Missouri is collaborating with the Reactor Conversion Proram at Argonne National Laboratory (ANL) in
various activities relavant to the conversion of the MURR such as: fuel element design, fuel cycle analyses
[5], and steady state thermal hydraulics safety analysis [6]. To achieve successful conversion of the MURR,
it is essential to develop a fuel element design that ensures safe reactor operation and acceptable shutdown
and safety margins [4]. Furthermore, it is necessary that the experimental performance of the existing facilty
is maintained at the same level of efficiency and capacity upon conversion.

     It is well known that in-service fuel swelling due to gaseous and solid fission products can impact the
overall fuel performance. In the MURR monolithic fuel plate, changes in fuel dimensions along the
thickness direction are attibuted to the combined effect of fuel swelling and irradiation creep. From a safety
analysis viewpoint, it is critical to determine the swelling and creep induced change in the MURR plate
thickness under steady-state conditions. Successful prediction and determination of irradiated fuel plate
thickness is required to ensure that adequate coolant channel thickness remains unblocked to ensure proper
heat removal from the fuel plate during operation.

      In this work, finite element analysis (FEA) is used to model and simulate the thermo-mechanical
behavior of a selected LEU MURR fuel plate under typical irradiation conditions of the proposed LEU
MURR core. The proposed LEU fuel element for MURR conversion has 23 curved fuel plates. The fuel
element design and analysis are described in Reference [7]. The safety analysis for calculating the margin
to flow instability during steady-state operations evaluated all fuel plate coolant channels in reference cores

Fuel Swelling and Creep Analysis for a MURR
LEU U-10Mo Monolithic Plate                                                                                  1
                                                                                         ANL/RTR/TM-18/19


that had elements with a mixture of burnups, which is typical for MURR operations [7]. In addition to the
application of engineering hot channel factors to account for variations in the fuel element manufacturing
that could affect the coolant channel gaps, the analysis assumed a constriction of the coolant channel gaps
due to an increase in the fuel plate thicknesses during the element lifetime. Estimates of the local plate
thickness increase at end-of-life (EOL) due to fuel swelling and creep were developed from experimental
data presented in References [8] and [9]. The maximum local plate thickness increase from that analysis
was calculated for fuel plate 23 in an EOL element. Furthermore, the minimum margin to flow instability
for the reference LEU cores was calculated to occur in coolant channel 23 of an EOL element, which is the
coolant channel between plates 22 and 23. Therefore, the work performed here evaluated plate 23 only, as
this was found to be the most limiting plate.

     The main goal of the present FE based study is to determine the maximum local increase in the
thickness of plate 23 under various combinations of swelling correlations and creep rate coefficients. The
estimated increase in the thickness of plate 23 is then used to evaluate the reduction in the thickness of the
adjacent coolant channels.


2 Simulation and Model Setup
2.1 Irradiation Parameters
     The irradiation conditions to be encountered by plate 23 in the MURR LEU fuel element were
simulated in three steps: (i) steady-state start up with a predefined plate temperature of 294 K, (ii) transient
step of 2873 hours representing the total irradiation time of plate 23 with swelling and creep behavior
included and maximum allowable temperature change per step of 5 K, and (iii) steady-state shutdown step
wherein the whole structure of the plate is cooled to 325 K.

     Table 1 summarizes the variation in the average power and fission densities in the plate 23 with time
as modeled in this work. Detailed, two-dimensional profiles for the power density and fission density by
axial and azimuthal mesh were derived from the results of neutron physics calculations for plate 23 under
prototypic conditions [10]. The plate-average values presented in Table 1 were approximated by taking the
arithmetic average of the data, without taking into account the variable mesh sizes for the data. Figure 1
shows spatial distribution of local-to-average fission density in plate 23 U-10Mo fuel core, which was
assumed constant over the irradiation cycle. The local-to-average fission density values were calculated
using the plate-average fission density in Table 1 and preserve the detailed, two-dimensional fission density
profile calculated for plate 23. Finally, the fission density distribution in the fuel core of plate 23 at EOL is
shown in Figure 2 with a maximum fission density estimated to be 2.62 × 1027 𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓/𝑚𝑚3 .

 Table 1: Variation in average power and fission densities with time for plate 23 in MURR LEU fuel
 element [10]
    Irradiation time, hr     Average power density, W/cm3          Average fission density, fission/m3
             48                        5982.35                                 3.20 × 1025
           1258                        5776.23                                 8.26 × 1026
           1560                        5746.41                                 1.02 × 1027
        2873 (EOL)                     5225.09                                 1.86 × 1027


Fuel Swelling and Creep Analysis for a MURR
LEU U-10Mo Monolithic Plate                                                                                    2
                                                                                    ANL/RTR/TM-18/19




 Figure 1. Local-to-average fission density distribution in the U-10Mo foil of plate 23 as modeled in this
 work.




  Figure 2. Fission density distribution in the U-10Mo foil of plate 23 at EOL as modeled in this work.


2.2 Finite Element Model
     The finite element (FE) geometric model of plate 23 in MURR LEU fuel element was developed
considering the nominal dimensions listed in Table 2. The thickness of the inboard and outboard
coolant channels adjacent to plate 23 is 2.3622 mm (channel 23) and 2.4257 mm (channel 24),
respectively [10].




Fuel Swelling and Creep Analysis for a MURR
LEU U-10Mo Monolithic Plate                                                                                  3
                                                                                     ANL/RTR/TM-18/19


 Table 2: Nominal dimensions of plate 23 as modeled in this work [10]
 Section                           Thickness, mm                  Length, mm              Width, mm
 LEU-10Mo fuel core                    0.4318                        609.6                102.8116
 Zr diffusion barrier  0.0254 (on each side of the fuel core)        609.6                102.8116
 Cladding               0.381 (on each side of the fuel core)        647.7                109.7202

     The element C3D8T (a 3D temperature-displacement continum element with 8-nodes of thermally
coupled brick) in ABAQUS FE solver [11] was adopted to represent the LEU-10Mo fuel core, Zr diffusion
barrier, and cladding sections of plate 23. As noted by the element type (C3D8T), full integration was used
to achive highest possible aaccuracy of displacement data which in turn increased the computation time.
Based on results obtained from a series of mesh sensitivty and sub-modeling studies, the FE geometric
model of plate 23 was meshed with a total of 186,624 C3D8T elements distributed between the three
sections of the plate as follows: 55,216 elements in each of the fuel core and Zr diffusion barrier sections
and 76,192 elements in the cladding section. Ideal bonding was assumed at the interfaces between the fuel
core, Zr diffusion barriers, and Al-cladding which implies that no delamination was allowed to take place.
See Appendix A for further details on FE mesh profile analysis.


2.3 Materials Models and Correlations
     Documented properties of U-10Mo alloy, commercially pure Zr, and AA6061-O alloy were used to
model the fuel core, diffusion barrier, and cladding, respectively. Material properties were varied as
functions of temperature and irradiation exposure following the “Preliminary Report on U-Mo Monolithic
Fuel for Research Reactors, INL/EXT-17-40975, Revision 1”[12].

     The behaviors of the AA6061-O cladding and the Zr diffusion barier were simulated considering
elasticity, plasticity, thermal expansion, and thermal creep [12]. Hardening due to fast neutron irradiation
was only considered for the AA6061-O cladding.

      The thermo-mechanical behavior of the U-10Mo fuel core is described considering elasticity,
plasticity, thermal expansion, swelling (due to solid and gaseous fission products), irradiation creep and
thermal conductivity degradation due to porosity (fission gas bubbles) formation in the fuel [12]. The
following are the primary models/ correlations used to model the U-10Mo fuel:

    (i) Model for thermal conductivity degradation of the fuel material [12]
    (ii) Irradiation induced creep model [12], [13]
    (iii) Model for the fuel swelling due to fission products [8], [12]


2.4 Evaluation of Swelling and Creep Models for U-10Mo Fuel
     As mentioned earlier, the thermo-mechanical behavior and the resultant increase in the thickness of
plate 23 will be evaluated under various combinations of swelling correlations and irradiation creep
coefficients. Thus, a brief evaluation of the swelling and creep correlation is presented in this section.

2.4.1 Fuel Swelling Correlations
     In this work, the irradiation performance of plate 23 in the MURR LEU fuel element was simulated
considering the following three swelling correlations:


Fuel Swelling and Creep Analysis for a MURR
LEU U-10Mo Monolithic Plate                                                                               4
                                                                                                 ANL/RTR/TM-18/19


     (i)      Swelling correlation developed by Kim et al. [8]:

 �∆𝑉𝑉�𝑉𝑉 � = 5.0 × 𝑓𝑓𝑑𝑑      𝑓𝑓𝑓𝑓𝑓𝑓 𝑓𝑓𝑑𝑑 ≤ 3 × 1027 𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓/𝑚𝑚3                                      Equation 1
        0 𝑓𝑓


 �∆𝑉𝑉�𝑉𝑉 � = 15 + 6.3 × (𝑓𝑓𝑑𝑑 − 3) + 0.33 × (𝑓𝑓𝑑𝑑 − 3)2 𝑓𝑓𝑓𝑓𝑓𝑓 𝑓𝑓𝑑𝑑
        0 𝑓𝑓
               > 3 × 1027 𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓/𝑚𝑚3

where �∆𝑉𝑉�𝑉𝑉 � total swelling in percent and 𝑓𝑓𝑑𝑑 is the fission density in × 1027 𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓/𝑚𝑚3 . Kim et al.
             0 𝑓𝑓
devloped the above swelling correlation considering fuel thickness measurements made on a limited
number of plates irradiated in the RERTR-6 through RERTR-9 campaigns [8], [12]. In that work, Kim et
al. considerd a single fuel thickness data point at the mid-point of an irradiated plate transverse mid-section
in order to minimize the contribution of irradiation creep to the thickness measurements. This swelling
correlation will be referred to as “Kim swelling correlation” in the next sections of this report.

     (ii)     Swelling correlation excluding AFIP-6 MKII data [12]:

      According to the “Preliminary Report on U-Mo Monolithic Fuel for Research Reactors, INL/EXT-17-
40975, Revision 1” [12], a large number of local fuel thickness measurements (18,675) were made on
irradiated plates from RERTR-9, RERTR-10, RERTR-12, AFIP-4, AFIP-6MKII, and AFIP-7. The
following fuel swelling correlation due to solid and gaseous fission products was established with fuel
thickness data from the AFIP-6MKII experiment excluded:

    % 𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆 = 3.83 × 10−21 𝑓𝑓𝑑𝑑 2 + 4.54 × 10−21 𝑓𝑓𝑑𝑑                                            Equation 2

where 𝑓𝑓𝑑𝑑 is fission density in 𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓/𝑐𝑐𝑐𝑐3 . In the next sections of this report, this swelling correlation will
be refered to as “excluding AFIP-6 MKII”.

     (iii)    95% Upper CL of swelling correlation including AFIP-6 MKII data [12]:

     When the data from the AFIP-6 MK-II experiment are included, higher fuel swelling will be predicted
based on equation (64) presented in the “Preliminary Report on U-Mo Monolithic Fuel for Research
Reactors, INL/EXT-17-40975, Revision 1”[12]. Moreover, the 95% upper confidence limit (UCL) of that
swelling correlation will predict even higher fuel swelling to take place. Thus, the following 95% UCL of
swelling correlation including AFIP-6 MK-II data was considered in this work as an extreme case (i.e.
conservative approach).

  % 𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆𝑆 = 6.39 × 10−43 𝑓𝑓𝑑𝑑 2 + 3.86 × 10−21 𝑓𝑓𝑑𝑑 + 5.28                                       Equation 3

where 𝑓𝑓𝑑𝑑 is fission density in 𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓/𝑐𝑐𝑐𝑐3 . In the next swctions of this report, this correlation will be
refered to as “95% UCL including AFIP-6 MKII”.

     The aforementioned three fuel swelling correlations are plotted and compared in Figure 3. It can be
seen that fuel swelling as predicted by the Kim swelling correlation is more or less the same as that predicted
by the swelling correlation excluding AFIP-6 MKII data up to ~1.8 × 1027 𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓/𝑚𝑚3. The swelling
correlation excluding AFIP-6 MKII predicts relatively higher fuel swelling at the maximum fission density

Fuel Swelling and Creep Analysis for a MURR
LEU U-10Mo Monolithic Plate                                                                                              5
                                                                                              ANL/RTR/TM-18/19


experienced by plate 23 in the MURR LEU fuel element (indicated by red dashed live). As expected, the
95% UCL including AFIP-6 MKII correlation predicts higher fuel swelling at all fission densities.

                     70
                                  Kim swelling correlation
                     60           excluding AFIP-6 MKII
                                  95% UCL including AFIP-6 MKII
                     50




   Fuel swelling %
                                         Plate 23 maximum fission density
                     40


                     30


                     20


                     10


                      0
                          0          1           2           3          4           5         6            7
                                                     Fission density (x1027), fission/m3

                              Figure 3. Comparison of fuel swelling correlations modeled in this work.


2.4.2 Irradiation Creep Model
    In this work, irradiation creep of irradiated U-10Mo fuel was modeled following the relation proposed
by Kim et al [13] which expresses the creep strain rate as follows:

 𝜀𝜀 ° = 𝐴𝐴 × 𝜎𝜎 × 𝑓𝑓 °                                                                                   Equation 4

where 𝜀𝜀 ° is creep strain rate (1/sec), 𝐴𝐴 is irradiation creep rate coefficient (cm3/MPa-fission), 𝜎𝜎 is equivalent
stress (MPa), and 𝑓𝑓 ° is fission density rate (fission/ cm3-sec). Kim et al determind the value of the creep
rate coeeficient 𝐴𝐴 to be 500 × 10−25 (cm3/MPa-fission) by performing FEA on a 2-D model of U-10Mo
monolithic mini-plate where the Kim swelling correlation was used to describe fuel swelling. Then, 𝐴𝐴 was
empirically adjusted until the thickness of simulated plate as predicted by FEA is in good agreement with
corresponding experimental measurements of local plate thickness. Thus, the value of A = 500 × 10−25
(cm3/MPa-fission) was derived considering the Kim swelling correlation and measured data. Accordingly,
this value should be revised and evaluated when other swelling correlations are used to describe the swelling
behavior of U-10Mo fuel. In the present study, it was decided to model the irradiation creep behavior of U-
10Mo fuel considering the model proposed by Kim et al. with the following values of creep rate coefficient:
750, 500, 250 and 5 (cm3/MPa-fission).

    Thus, the thermo-mechnaical behavior of plate 23 in MURR LEU fuel element was simulated
considering three swelling correlations along with four different values of creep rate coefficient.

Fuel Swelling and Creep Analysis for a MURR
LEU U-10Mo Monolithic Plate                                                                                        6
                                                                                      ANL/RTR/TM-18/19


3 Results and Discussion
      As mentioned earlier in this report, the main goal of this study is to determine the maximum increase
in the thickness of plate 23 at EOL considering various combinations of swelling correlations and values
of creep rate coefficient. For each of the three swelling correlations discussed in section (2.4.1), peak
displacement along the thickness direction of plate 23 was determined in four cases corresponding to creep
rate coefficient of 750, 500, 250 and 5 (× 10−25 cm3/MPa-fission).

     Figure 4 shows the swelling strain component in the U-10Mo fuel core as predicted by the FE
simulations considering the three swelling correlations of interest. According to the data in Table 3, the FE
results of fuel swelling are in very good agreement with fuel swelling as directly estimated by Equation 1,
2, and 3 at EOL (fission desnity of 2.62 × 1027 𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓/𝑚𝑚3 , see Figure 2).




                         (a)                                                   (b)




                                                    (c)

 Figure 4. Swelling strain contours in U-10Mo fuel core of plate 23 considering (a) Kim swelling
 correlation, (b) excluding AFIP-6 MKII swelling correlation, and (c) 95% UCL including AFIP-6 MKII
 correlation.

 Table 3: Fuel swelling in plate 23 at 2.62 × 1027 𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓𝑓/𝑚𝑚3 (EOL) from FEA and calculations
 Swelling correlation                                  Swelling strain from          Swelling strain from
                                                                 FEA, %                calculations, %
 Kim swelling correlation                                          13.1                      13.1
 Excluding AFIP-6 MKII correlation                                 14.5                      14.5
 95% UCL including AFIP-6 MKII correlation                         20.7                      19.8




Fuel Swelling and Creep Analysis for a MURR
LEU U-10Mo Monolithic Plate                                                                                 7
                                                                                     ANL/RTR/TM-18/19


3.1 FEA with Kim Swelling Correlation
     As seen from Figure 5, the location of peak displacement in plate 23 U-10Mo fuel core along thickness
direction does not change with variation in in creep rate coefficient in the range between 750 and 5 (×
10−25 cm3/MPa-fission). Maximum outboard increase in fuel core thickness was observed along
longitudinal mid-plane whereas maximum inboard increase was observed at the edge of the fuel core.

     Furthermore, FEA revealed that higher peak dispalcement along the thickness direction of the fuel
core occurred with A = 5 (× 10−25 cm3/MPa-fission) compared to creep rate coefficient varying between
750 and 250 (× 10−25 cm3/MPa-fission).




                    (a) A = 750                                            (b) A = 500




                     (c) A = 250                                            (d) A = 5

 Figure 5. Contours of displacement along thickness direction in plate 23 considering Kim swelling
 correlation and different values of creep rate coefficient (× 10−25 cm3/MPa-fission).

      Since the maximum displacement along thickness direction was observed along the longitudinal mid-
plane of the fuel, the plate thickness profile was analyzed along the same mid-plane as illustrated in Figure
6. From Figure 7a, it can be seen that displacement through the thickness direction at EOL along the
longitudinal mid-plane of plate 23 did not change as the creep rate coeffienct varied between 750 and 250
(× 10−25 cm3/MPa-fission). Larger displacement along plate thickness direction was observed with creep
rate coefficient of 5 (× 10−25 cm3/MPa-fission). This last observation is mainly due to the lack of stress
relaxation mechanism in this case combined with the curved geometry of the plate. However, about 2.039
mm of coolant channel 24 (outboard) remains unblocked with the large displacement observed with creep
rate coefficient of 5 (× 10−25 cm3/MPa-fission) as shown in Figure 7b.

     Interestingly, FEA revealed that variation in creep rate coefficient has insignificnt effect on the
observed net increase in plate thickness as shown in Figure 8. The maximum net increase in plate 23
thickness with fuel swelling described by Kim correlation was found to be 0.051 mm.



Fuel Swelling and Creep Analysis for a MURR
LEU U-10Mo Monolithic Plate                                                                                8
                                                                                                 ANL/RTR/TM-18/19




 Figure 6. Schematic of plate 23 longitudinal mid-plane used for the analysis of plate thickness at EOL.

                                            1.2                                                          unirradiated
                                              1


      Plate surface position relative to
                                            0.8                                                          A = 750
                                            0.6
                                            0.4
                                                                                                         A = 500
                                            0.2
                                              0



    unirradiated plate 23 centerline, mm
                                           -0.2 0     100   200   300         400    500   600   700     A = 250
                                           -0.4
                                           -0.6
                                                                                                         A=5
                                           -0.8
                                             -1
                                                                  Plate length, mm

                                                                            (a)
                                           3.5                                                          unirradiated



    Plate surface position relative to
                                           2.5
                                                                                                        A = 750
                                           1.5
                                                                                                        A = 500
                                           0.5
                                                                                                        A = 250
                                           -0.5



  unirradiated plate 23 centerline, mm
                                           -1.5                                                         A=5

                                           -2.5                                                         Channel 24
                                                                                                        Channel 23
                                           -3.5
                                                  0   100   200   300         400    500   600   700
                                                                  Plate length, mm

                                                                            (b)

 Figure 7. Effect of variation in creep rate coefficient on displacement profile along longitudinal mid-
 plane of plate 23 at EOL with Kim swelling correlation. Positive and negative Y-axis represents outboard
 and inboard directions, respectively.


Fuel Swelling and Creep Analysis for a MURR
LEU U-10Mo Monolithic Plate                                                                                             9
                                                                                                      ANL/RTR/TM-18/19


                                     0.06




   Increase in plate thickness, mm
                                     0.05

                                     0.04

                                     0.03                                                                       A=750
                                                                                                                A=500
                                     0.02                                                                       A=250
                                                                                                                A=5
                                     0.01

                                       0
                                            0    100          200   300        400    500       600       700

                                                                    Plate lenth, mm

 Figure 8. Net increase in plate 23 thickness along longitudinal mid-plane at EOL considering Kim
 swelling correlation with various values of creep rate coefficient (× 10−25 cm3/MPa-fission).



3.2 FEA with Swelling Correlation Excluding AFIP-6 MKII Data
     The analysis presented in section 3.1 was repeated for the swelling correlation excluding AFIP-6 MKII
data. In this case, the maximum displacement was observed along the longitudinal mid-plane of plate 23
regardless of the creep rate coefficient (see Figure 9).




                                                (a) A = 750                                 (b) A = 500




                                                (c) A = 250                                  (d) A = 5

 Figure 9. Contours of displacement along thickness direction in plate 23 with swelling correlation
 excluding AFIP-6 MKII data and different values of creep rate coefficient (× 10−25 cm3/MPa-fission).



Fuel Swelling and Creep Analysis for a MURR
LEU U-10Mo Monolithic Plate                                                                                         10
                                                                                                             ANL/RTR/TM-18/19


     From Figure 10a, displacement profiles are more or less the same as creep rate coefficient varied
between 750 and 250 250 (× 10−25 cm3/MPa-fission) whereas relatively larger displcamant was found with
creep rate coefficient of 5 250 (× 10−25 cm3/MPa-fission). In this case, about 1.997 mm of coolant channel
24 (outboard) remains unblocked with the large displacement observed with creep rate coefficient of 5 (×
10−25 cm3/MPa-fission) as shown in Figure 10b.

      As shown in Figure 11, the net increase in plate thickness has only a minimal dependence on the creep
rate coefficient for values between 750 and 250 (× 10−25 cm3/MPa-fission). The maximum net increase in
plate 23 thickness was found to be 0.055 mm. This is about 0.004 mm higher than the net increase when
fuel swelling was described by the Kim swelling correlation (see section 3.1, Figure 7a).

                                            1.2
                                                                                                                    unirradiated
                                              1


      Plate surface position relative to
                                            0.8
                                                                                                                    A = 750
                                            0.6
                                            0.4
                                            0.2                                                                     A = 500

                                              0



    unirradiated plate 23 centerline, mm
                                           -0.2 0          100     200     300        400     500   600     700     A = 250
                                           -0.4
                                           -0.6                                                                     A=5
                                           -0.8
                                             -1
                                                                           Plate length, mm

                                                                                      (a)
                                            3.5                                                                    unirradiated




      Plate surface position relative to
                                              3
                                            2.5
                                                                                                                   A = 750
                                              2
                                            1.5
                                              1                                                                    A = 500
                                            0.5
                                              0
                                           -0.5                                                                    A = 250




    unirradiated plate 23 centerline, mm
                                             -1
                                           -1.5                                                                    A=5
                                             -2
                                           -2.5
                                             -3                                                                    Channel 24
                                           -3.5                                                                    Channel 23
                                                  0   50   100 150 200 250 300 350 400 450 500 550 600 650 700
                                                                          Plate length, mm

                                                                                     (b)

 Figure 10. Effect of variation in creep rate coefficient on displacement profile along longitudinal mid-
 plane of plate 23 at EOL with swelling correlation excluding AFIP-6 MKII data. Positive and negative
 Y-axis represents outboard and inboard directions, respectively.




Fuel Swelling and Creep Analysis for a MURR
LEU U-10Mo Monolithic Plate                                                                                                        11
                                                                                                           ANL/RTR/TM-18/19


                                     0.06




   Increase in plate thickness, mm
                                     0.05

                                     0.04

                                                                                                                     A=750
                                     0.03
                                                                                                                     A=500

                                     0.02                                                                            A=250
                                                                                                                     A=5
                                     0.01

                                       0
                                            0    100          200       300        400     500       600       700
                                                                    Fuel plate lenth, mm
 Figure 11. Net increase in plate 23 thickness along longitudinal mid-plane at EOL with swelling
 correlation excluding AFIP-6 MKII and various values of creep rate coefficient (× 10−25 cm3/MPa-
 fission).


3.3 FEA Considering 95% UCL of Correlation Including AFIP-6
    MKII Data
     All observations reported in the previous two sections were found when the fuel swelling is predicted
based on the 95% UCL of the correlation including AFIP-6 MKII data. As shown in Figure 12, the location
of the maximum displacement along plate thickness is insensitive to variation in the creep rate coeffienct.




                                                (a) A = 750                                      (b) A = 500




                                                (c) A = 250                                       (d) A = 5

 Figure 12. Contours of displacement along thickness direction in plate 23 considering 95% UCL of
 swelling correlation including AFIP-6 MKII data and different values of creep rate coefficient (×
 10−25 cm3/MPa-fission).


Fuel Swelling and Creep Analysis for a MURR
LEU U-10Mo Monolithic Plate                                                                                                12
                                                                                               ANL/RTR/TM-18/19



     Similar to the analysis presented in the previous two sections, Figure 13a shows that relatively larger
displacemnt was observed when the creep rate coefficient was set to 5 (× 10−25 cm3/MPa-fission)
compared to higher values up to 750 (× 10−25 cm3/MPa-fission).

      Moreover, about 1.866 mm of coolant channel 24 remains unblocked with creep rate coefficient of 5
(× 10−25 cm3/MPa-fission). Finally, 0.083 mm was found to be the maximum increase in plate thickness
in this case (Figure 13b).

                                         1.4
                                                                                                     unirradiated
                                         1.2



    Plate surface position relative to
                                           1
                                         0.8                                                         A = 750
                                         0.6
                                         0.4
                                                                                                     A = 500
                                         0.2
                                           0


  unirradiated plate 23 centerline, mm
                                         -0.2 0     100   200   300         400    500   600   700   A = 250
                                         -0.4
                                         -0.6                                                        A=5
                                         -0.8
                                          -1
                                                                Plate length, mm


                                                                           (a)
                                          3.5                                                        unirradiated
                                            3



    Plate surface position relative to
                                          2.5
                                            2                                                        A = 750
                                          1.5
                                            1                                                        A = 500
                                          0.5
                                            0
                                         -0.5                                                        A = 250



  unirradiated plate 23 centerline, mm
                                           -1
                                         -1.5                                                        A=5
                                           -2
                                         -2.5
                                           -3                                                        Channel 24
                                         -3.5                                                        Channel 23
                                                0   100   200   300         400    500   600   700
                                                                Plate length, mm

                                                                           (b)

 Figure 13. Effect of variation in creep rate coefficient on displacement profile along longitudinal mid-
 plane of plate 23 at EOL with the 95% UCL swelling correlation including AFTP-6 MKII data. Positive
 and negative Y-axis represents outboard and inboard directions, respectively.




Fuel Swelling and Creep Analysis for a MURR
LEU U-10Mo Monolithic Plate                                                                                       13
                                                                                       ANL/RTR/TM-18/19


                                     0.09




   Increase in plate thickness, mm
                                     0.08
                                     0.07
                                     0.06
                                     0.05                                                             A=750

                                     0.04                                                             A=500
                                                                                                      A=250
                                     0.03
                                                                                                      A=5
                                     0.02
                                     0.01
                                       0
                                            0   100   200   300   400   500      600         700
                                         Fuel plate lenth, mm
 Figure 14. Net increase in plate 23 thickness along longitudinal mid-plane at EOL with 95% UCL of
 swelling correlation including AFIP-6 MKII data and various values of creep rate coefficient (×
 10−25 cm3/MPa-fission).

      Since the net maximum increase in the thickness of plate 23 in the MURR LEU fuel element represents
the most important outcome from this study, the value of the maximum increase in the plate thickness at
EOL across all combinations of fuel swelling correlations and creep rate coefficients are listed in Table 4.
Based on the FEA results, the maximum increase in the plate 23 thickness is 0.083 mm and it occurs when
fuel swelling is described by the 95% UCL of swelling correlation including AFIP-6 MKII data and creep
rate coefficient in the range between 7500 and 250 (× 10−25 cm3/MPa-fission).

 Table 4: Maximum increase in the thickness of plate 23 at EOL under different combinations of swelling
 correlations and creep rate coefficients (× 10−25 cm3/MPa-fission).
                                                        Maximum increase in plate thickness, mm
 Swelling correlation                               A = 750      A = 500        A = 250       A=5
 Kim swelling correlation                            0.051        0.051          0.051        0.050
 Excluding AFIP-6 MKII correlation                   0.055        0.055          0.055        0.054
 95% UCL including AFIP-6 MKII correlation           0.083        0.083          0.083        0.081



3.4 Stress analysis
     Table 5 lists the peak equivalent stress experienced by the U-10Mo fuel core under the various
combinations of fuel swelling correlations and creep rate coefficient values simulated in this work. It can
be seen that the decrease in creep rate coefficient from 250 to 5 (× 10−25 cm3/MPa-fission) resulted in a
noticeable increase in the peak equivalent stress of the fuel core. This is attributed to the lack of stress
relaxation mechanisms in the case of such a very low creep rate coefficient.
     Furthermore, the influence of the swelling correlation on the peak equivalent stress in the fuel core is
noticeable only at the lowest creep rate coefficient attempted in this study. According to reference [10], the
maximum operating temperature experienced by the U-10Mo fuel core is about 150°C at which the yield
stress of the material is 805 MPa [12]. In all the cases simulated in this work, the peak equivalent stress in
the U-10Mo fuel core is well below the yield stress of the material. Thus, no plastic deformation occurred
in the fuel core under any combination of fuel swelling correlation and creep rate coefficient values
simulated in this work.

Fuel Swelling and Creep Analysis for a MURR
LEU U-10Mo Monolithic Plate                                                                                 14
                                                                                     ANL/RTR/TM-18/19




 Table 5: Peak equivalent stress in U-10Mo fuel core.
                                                                Peak equivalent stress, MPa
 Swelling correlation                               A = 750       A = 500        A = 250         A=5
 Kim swelling correlation                            31.34         31.54          32.34          243.40
 Excluding AFIP-6 MKII correlation                   31.42         31.64          32.79          262.67
 95% UCL including AFIP-6 MKII correlation           31.34         31.20          32.70          342.54



4 Summary
     In this work, FEA was used to evaluate the swelling and creep behavior of plate 23 in a MURR LEU
U-10Mo fuel element. The thermo-mechanical behavior of plate 23 was simulated under typical irradiation
conditions of the MURR LEU core. Fuel swelling was described considering three swelling correlations:
the Kim swelling correlation, a swelling correlation excluding AFIP-6 MKII data, and the 95% upper
confidence limit of the correlation including AFIP-6 MKII, where the last one represents an extreme case
(most conservative estimate of fuel swelling). Furthermore, irradiation creep strain rate in the U-10Mo fuel
was modeled such that it linearly varies with equivalent stress, fission rate and empirical creep rate
coefficient.

      The deformation profile and corresponding increase in the thickness of plate 23 at EOL were
determined considering various combinations of the aforementioned three swelling correlations and creep
rate coefficients of 750, 500, 250, and 5 (× 10−25 cm3/MPa-fission). The following remarks were made:

     • Maximum displacement along the thickness direction of plate 23 was found at the same location
       in all simulated combinations of swelling correlations and creep rate coefficients.
     • Under the same swelling correlation, larger outboard displacement was always observed at the
       lowest creep rate coefficient attempted in this study (5 × 10−25 cm3/MPa-fission).
     • Variation in the creep rate coefficnet has an insignificant effect on the net increase in plate
       thickness for the same swelling correlation.
     • Maximum increase in plate thickness was found to be 0.083 mm and it occurs when fuel swelling
       is described by the 95% UCL of the correlation including AFIP-6 MKII data and creep rate
       coefficient in the range between 750 and 250 (× 10−25 cm3/MPa-fission).
     • Under any of the three swelling correlations considered in this work, the lack of stress relaxation
       mechanisms in the case of creep rate coefficient of 5 (× 10−25 cm3/MPa-fission) resulted in a
       noticeable increase in the peak equivalent stress in the U-10Mo fuel core. However, the fuel core
       did not experience any plastic deformation since the peak equivalent stress in all cases was well
       below the yield stress of the material.


5 Acknowledgements
     This work was sponsored by the U.S. Department of Energy, Office of Material Management and
Minimization in the U.S. National Nuclear Security Agency Office of Defense Nuclear Nonproliferation
Office under Contract DE-AC02-06CH11357.


Fuel Swelling and Creep Analysis for a MURR
LEU U-10Mo Monolithic Plate                                                                               15
                                                                                    ANL/RTR/TM-18/19


Appendix A
Finite Element Meshing Profile Optimization and Analysis

     Initially, the finite element (FE) geometrical model of plate 23 was prepared following a well-
optimized fine-mesh profile that was previously used to model prototypic U-10Mo monolithic mini-
plates [14]. In that meshing profile, the U-Mo fuel core section was represented by six layers along
the plate thickness direction, and each of the Zr diffusion barrier and the cladding sections was
represented by three layers (on each side of the fuel core). However, due to the larger width and
length of the MURR plate 23 relative to the dimensions of the mini-plates, the size of the input file
representing the FE model for plate 23 was approximately 1 GB compared to few tens of MB for the
corresponding monolithic mini-plate input file. Consequently, it was not possible to consider such a
fine-mesh profile considering the available computational resources, as well as the extremely large
size of the output database files.

     The FE model of plate 23 was then meshed considering various combinations of the number of
layers representing the three sections of the plate along the thickness direction. A coarse-mesh profile
with the fuel core represented by two layers along the plate thickness directions and each of the Zr
diffusion barrier and cladding section represented by one layer (on each side of the fuel core) resulted
in a model input file of size ∼ 41 MB and output database file of ∼ 3.8 GB. The FE model with that
meshing profile was considered as a full-size baseline model for plate 23.

     A sub-modeling technique was used to determine the effect of variation in meshing profile on
the displacement component along the plate thickness direction. A region of interest that envelopes
the highest fission density in the fuel core (see Figure 2) around the transverse mid-section of plate
23 was determined and a FE sub-model was developed to represent that region as depicted by Figure
15. The region of interest was simulated in two cases corresponding to a total length of 6 inch (2 inch
and 4 inch around plate 23 transverse mid-plane) and 10 inch (4 inch and 6 inch around plate 23
transverse mid-plane), separately.




             Figure 15. Schematic of the region of interest around the fuel core mid-section.


Fuel Swelling and Creep Analysis for a MURR
LEU U-10Mo Monolithic Plate                                                                          16
                                                                                    ANL/RTR/TM-18/19


      A fine mesh profile along the thickness direction of the plate was adopted for the region of
interest. In the fine mesh profile, the fuel core section was represented by a total of six layers, the Zr
diffusion barrier was represented by two layers (on each side of the fuel core), and the cladding
section was represented by four layers (on each side of the fuel core). The purpose of this approach
is to achieve results of high accuracy for the sub-model within reasonable computation time.

     Two FE sub-models were developed for the region of interest shown in Figure 15 as follows: sub-
model (1): with X = 2 inch and Y = 4 inch (i.e. 6 inch length) and sub-model (2): with X = 4 inch and Y
= 6 inch (i.e. 10 inch length). In the sub-modeling technique, the displacement data at all-time points
from the coarse-mesh full-size model were used as boundary conditions for the fine-mesh sub-
models. Figure 16 shows contours of the displacement component along the thickness direction of
plate 23 from the coarse-mesh full-size model and the two fine-mesh sub-models 1.




                                                   (a)




                       (b)                                                (c)
 Figure 16. Contours of displacement component along thickness directions of plate 23 from coarse-mesh
 full-size model (a) and fine-mesh profile sub-models measuring 6 inch (b) and 10 inch (c) in length.


1 Displacement contours presented in Appendix A are based on the fuel swelling correlation excluding AFIP-6

MKII data.

Fuel Swelling and Creep Analysis for a MURR
LEU U-10Mo Monolithic Plate                                                                             17
                                                                                 ANL/RTR/TM-18/19


     The displacement peaks found at the edges of the two sub-models (Figure 16 b and c) are
attributed to the truncation of the FE geometrical model at the edges of the region of interest which
is commonly referred to as the edge effect. To exclude the edge effect, the displacement component
along the plate thickness direction was reanalyzed in the two sub-models where the edge regions
were excluded as shown in Figure 17.




                    (a)                                                   (b)
 Figure 17. Contours of displacement component along thickness directions from (a) 6 inch and (b) 10
 inch in length sub-models of plate 23 excluding the edge effect region in both cases.

     It can be seen that the peak displacement along plate thickness in a 6 inch length sub-model is
0.290 mm (Figure 17a) whereas the corresponding peak displacement in the sub-model with a 10
inch length is 0.254 mm (Figure 17b). The larger displacement observed in the 6 inch sub-model can
be attributed to residual edge effects compared to the 10 inch sub-model where the excluded edge
effect regions are far enough from the sub-model mid-plane. Although both the 6 inch sub-model and
10 inch sub-model possess the same mesh profile, the 10 inch sub-model is affected less by the edge
effect, and is thus considered more representative of the full size plate. Furthermore, the peak
displacement along the plate thickness direction from the fine-mesh 10 inch length sub-model,
following the exclusion of the edge effect regions, matches that of the coarse-mesh full-size model
(see Figure 16a and Figure 17b). Because of the excellent agreement between the peak displacement
predicted by the coarse-mesh full-size model of plate 23 and fine-mesh sub-model with a 10 inch
length, the coarse-mesh full-size model of plate 23 was considered satisfactory for the analyses
presented in this study.




Fuel Swelling and Creep Analysis for a MURR
LEU U-10Mo Monolithic Plate                                                                            18
                                                                                   ANL/RTR/TM-18/19


References
[1]    J. L. Snelgrove, G. L. Hofman, M. K. Meyer, C. L. Trybus, and T. C. Wiencek, “Development of very-
       high-density low-enriched-uranium fuels,” Nucl. Eng. Des., vol. 178, pp. 119–126, 1997.

[2]    M. K. Meyer et al., “IRRADIATION PERFORMANCE OF U-Mo MONOLITHIC FUEL,” Nucl. Eng.
       Technol., vol. 46, no. 2, pp. 169–182, Apr. 2014.

[3]    J. Rest, Y. S. Kim, G. L. Hofman, M. K. Meyer, and S. L. Hayes, “U-Mo Fuels Handbook, Version
       1.0,” ANL-09/31, Argonne National Laboratory, 2006.

[4]    E. H. Wilson, A. Bergeron, J. A. Stillman, T. A. Heltemes, D. Jaluvka, and L. Jamison, “U.S. HIGH
       PERFORMANCE RESEARCH REACTOR CONVERSION PROGRAM: AN OVERVIEW ON ELEMENT
       DESIGN,” RRFM 2017, Rotterdam, Netherlands.

[5]    J. Stillman, “Technical Basis in Support of the Conversion of the University of Missouri Research
       Reactor (MURR) Core from Highly-Enriched to Low-Enriched Uranium – Core Neutron
       Physics," ANL/RERTR/TM-12-30, Argonne National Laboratory, 2012.

[6]    E. E. Feldman, “Technical Basis in Support of the Conversion of the University of Missouri
       Research Reactor (MURR) Core from Highly-Enriched to Low-Enriched Uranium – Steady-
       State Thermal-Hydraulic Analysis," ANL/RERTR/TM-12-37, Argonne National Laboratory,
       2012.

[7]    J. Stillman, “Low-Enriched Uranium Conversion Preliminary Safety Analysis Report for the
       University of Missouri Research Reactor," University of Missouri Research Reactor, Columbia,
       MO, submitted to the U.S. Nuclear Regulatory Commission, 2017.

[8]    Y. S. Kim and G. L. Hofman, “Fission product induced swelling of U–Mo alloy fuel,” J. Nucl. Mater.,
       vol. 419, no. 1–3, pp. 291–301, Dec. 2011.

[9]    G. L. Hofman and Y. S. Kim, “FISSION INDUCED SWELLING AND CREEP OF
       URANIUMMOLYBDENUM ALLOY FUEL,” RRFM 2009, Vienna , Austria.

[10]   J. Stillman, E. Wislon, L. Foyto, K. Kutikkad, J. C. McKibben, and N. Peters, “Irradiation
       Demonstration Element Design Parameters for MURR LEU U-Mo Fuel Conversion,"
       ANL/RTR/TM-18/4, Argonne National Laboratory, 2018.

[11]   “ABAQUS/ CAE 6.14 Documentation Collection," Providence, RI: Dassault Systemes Simulia
       Corp., 2014.

[12]   M. Meyer et al., “Preliminary Report on U-Mo Monolithic Fuel for Research Reactors," INL/EXT-
       17-40975, Revision 1, 2017.

[13]   Y. S. Kim, G. L. Hofman, J. S. Cheon, A. B. Robinson, and D. M. Wachs, “Fission induced swelling
       and creep of U–Mo alloy fuel,” J. Nucl. Mater., vol. 437, no. 1–3, pp. 37–46, June 2013.

[14]   W. Mohamed and H. S. Roh, “INFLUENCE OF MATERIALS PROPERTIES ON THE IRRADIATION
       BEHAVIOR OF U-10MO MONOLITHIC MINI-PLATES,” Proceedings of the ASME 2015
       International Mechanical Engineering Congress and Exposition IMECE2015, 2015, no. 630, pp.
       1–14.

Fuel Swelling and Creep Analysis for a MURR
LEU U-10Mo Monolithic Plate                                                                            19
                                              ANL/RTR/TM-18/19




Fuel Swelling and Creep Analysis for a MURR
LEU U-10Mo Monolithic Plate                                20
    Nuclear Science and Engineering Division
    Argonne National Laboratory
    9700 South Cass Avenue, Bldg. 208
    Argonne, IL 60439

    www.anl.gov




Argonne National Laboratory is a U.S. Department of Energy
laboratory managed by UChicago Argonne, LLC
