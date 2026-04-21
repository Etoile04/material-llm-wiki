# Swelling of U-Mo Monolithic Fuel: Developing a Predictive Swelling Correlation under Research Reactor Conditions

---

                                                                 Journal of Nuclear Materials 544 (2021) 152703



                                                                 Contents lists available at ScienceDirect


                                                           Journal of Nuclear Materials
                                                        journal homepage: www.elsevier.com/locate/jnucmat




Swelling of U-Mo Monolithic Fuel: Developing a Predictive Swelling
Correlation under Research Reactor Conditions
A.B. Robinson∗, W.J. Williams, W.A. Hanson, B.H. Rabin, N.J. Lybeck, M.K. Meyer
Idaho National Laboratory, P. O. Box 1625, Idaho Falls, ID 83415-6188 U.S.A.




a r t i c l e         i n f o                            a b s t r a c t

Article history:                                         Understanding swelling behavior in monolithic, uranium-molybdenum, plate-type fuel is necessary to
Received 28 August 2020                                  qualify the fuel for reactor use and for the conversion of high performance research reactors from highly
Revised 23 November 2020
                                                         enriched to low-enriched uranium. Multiple mechanisms inﬂuence plate dimensional stability, including
Accepted 24 November 2020
                                                         solid and gaseous ﬁssion-product induced swelling, irradiation-assisted creep, fuel-phase transformation,
Available online 5 December 2020
                                                         and interaction-layer formation. Separating these phenomena remains a challenge, and current models do
Keywords:                                                not appear to adequately predict experimental results at higher ﬁssion densities where it is most criti-
U-Mo, fuel swelling                                      cal. To mitigate the mechanistic uncertainty, post-irradiation proﬁlometry is used to increase the number
Non-destructive examination                              of data points available over a range of in-reactor irradiation experiments conducted at the Advanced
Post irradiation examination                             Test Reactor, and to provide a statistical precedent for a swelling-behavior model. This work establishes a
Low enriched uranium                                     predictive swelling correlation as a function of ﬁssion density, with associated conﬁdence and prediction
Research reactor fuel
                                                         bounds, by analyzing more than 18,0 0 0 thickness data points collected on 74 irradiated U-10Mo mono-
Monolithic fuel
                                                         lithic fuel test plates over a range of irradiation conditions.
                                                                                                                           © 2020 Elsevier B.V. All rights reserved.




1. Introduction                                                                           1.1. General Fuel Swelling Behavior

    A monolith fuel design based on uranium-molybdenum (U-Mo)                                During irradiation, swelling of nuclear fuel occurs due to an ac-
alloy has been selected as the fuel type for conversion of the                            cumulation of gaseous and solid ﬁssion products. The swelling be-
United States’ high performance research reactors (HPRRs) from                            havior of the fuel plate is a deﬁning attribute of the fuel system
highly enriched uranium (HEU) to low-enriched uranium (LEU). In                           that governs its suitability for use in a speciﬁc nuclear application.
this plate-type fuel design, a thin layer of zirconium is used to                         Swelling must be stable and predictable, and provide suﬃcient op-
eliminate the direct interaction between the U–10wt%Mo (U-10Mo)                           erating margin, for the range of fuel operating conditions.
fuel core and the 6061 aluminum alloy (AA6061) cladding during                               As ﬁssion-gas production in the fuel increases with increasing
fabrication and irradiation. In order to be qualiﬁed for use in re-                       ﬁssion density, most fuel materials have demonstrated a tendency
actors, U-Mo monolithic fuel plates must exhibit swelling in a sta-                       toward accumulation of the gas into micrometer-scale bubbles that
ble and predictable regime. The key phenomena that can impact                             lead to volumetric swelling that escalates with further increases in
the dimensional stability and robustness of a fuel plate during ir-                       ﬁssion density. Breakaway swelling is a term that has been used
radiation are ﬁssion-product-induced fuel swelling, transformation                        historically with reference to dispersion fuels to deﬁne a regime of
of radiation-stable phases into unstable phases, radiation-enhanced                       stable fuel behavior followed by a rapid or unpredictable transition
diffusion between dissimilar materials (resulting in the formation                        to high swelling behavior that is often associated with gas-bubble
of unstable phases), and fuel relocation resulting from irradiation-                      interconnection or large ﬁssion gas bubbles that have accumulated
assisted creep.                                                                           at the interface of the amorphous interaction layer and the alu-
                                                                                          minum matrix. If the fuel system exhibits breakaway swelling as
                                                                                          a function of ﬁssion density, then a ﬁssion-density threshold that
                                                                                          deﬁnes the fuel safety limit must be identiﬁed during the fuel de-
                                                                                          velopment effort in order to ensure this region is never reached by
  ∗
                                                                                          the fuel.
     Corresponding author. Post Irradiation Examinations, Idaho National Laboratory,
P.O. Box 1625, Idaho Falls, ID 83415-6188 U.S.A.                                             At fuel operating temperatures of interest for research reactors,
     E-mail address: adam.robinson@inl.gov (A.B. Robinson).                               below ~250°C, the dominant swelling mechanism of U-Mo at low


https://doi.org/10.1016/j.jnucmat.2020.152703
0022-3115/© 2020 Elsevier B.V. All rights reserved.
A.B. Robinson, W.J. Williams, W.A. Hanson et al.                                                                   Journal of Nuclear Materials 544 (2021) 152703


to medium ﬁssion density is volume expansion by solid ﬁssion                 “fuel swelling,” but it must be recognized that local plate-thickness
products caused by the volume difference between uranium and                 changes also result from fuel relocation caused by irradiation-
the resulting solid ﬁssion products. This type of fuel swelling is           assisted creep, which does not result in volume change, as well as
only dependent on ﬁssion density and is largely independent of               any volumetric swelling of cladding or interaction-layer products.
temperature, fabrication, irradiation conditions, and the phase of              On this basis, volumetric fuel swelling percent can be simply
fuel. Based on the estimates of Hofman and Walter [1] as well as             computed by:
Kim and Hofman [2], who evaluated solid ﬁssion-product swelling                      
                                                                                 V               t f
in U-10Mo fuel, swelling should be between 2 and 4% per 1021                                  =                                                              (1)
ﬁssions/cm3 .
                                                                                 V0               tf0
                                                                                          f
    The noble ﬁssion gases Xe and Kr, being largely insoluble,               where t f is the fuel thickness change after irradiation, and t f 0 is
tend to precipitate into gas bubbles. In general, the magnitude of           the as-fabricated fuel thickness. Here t f is measured, and t f 0 is
swelling depends primarily on the gas-bubble morphology that de-             known from the fabrication records.
velops during irradiation. In U-Mo, the ﬁssion gas precipitates in               Fuel-swelling analyses of historical plate-type U-Mo irradiated
an energetically stable face centered cubic superlattice of nano-            fuel, including both monolithic and dispersion fuel types, have
size bubbles that are registered on the underlying body centered             been published and include different fuel swelling models [2,13–
cubic U-Mo crystal lattice [3–7]. Gas bubbles are on the order of            16]. Different techniques were used to calculate total volume in-
2-3 nanometers in diameter, arrayed with a lattice parameter of              crease, including ﬁnal plate-thickness measurements, optical mi-
approximately 11-12 nanometers [3,4,8]. The formed nano-bubble               croscopy image analysis to measure only the fuel thickness in-
lattice remains stable up to a ﬁssion density of approximately               crease, ultrasonic testing, and immersion-density measurements to
3 × 1021 ﬁssions/cm3 . Up to this ﬁssion density the swelling rate           establish plate average behavior.
is low and both solid and gaseous ﬁssion products give rise to a                 Leenaers [13] modeled the fuel swelling of U–7Mo dispersion
linear solid-state swelling.                                                 fuel from large-size fuel plates irradiated as part of the EFU-
    At a ﬁssion density between 2.5 × 1021 and 3.5 × 1021                    TURE and SELENIUM experiments performed at the BR2 reactor.
ﬁssions/cm3 , gas-driven swelling gradually increases in importance          While this is a fuel system different from the monolithic fuel de-
relative to solid ﬁssion-product swelling. This transition is at-            sign, comparison of the swelling of U–7Mo in dispersion form
tributed to the onset of grain reﬁnement, sometimes referred to as           may provide relevant insights. Swelling proﬁles were calculated us-
grain subdivision, which occurs as a result of irradiation-induced           ing post-irradiation plate-thickness measurements, pre-irradiation
recrystallization of γ -U. An important impact of grain reﬁnement            fuel-meat thicknesses, and pre-irradiation fuel volume fractions.
is that it provides additional grain-boundary surface area on which          Two different swelling correlations were proposed based on the lo-
ﬁssion-gas-bubbles nucleate and grow. The fuel recrystallization is          cal ﬁssion density as:
accompanied by the collapse of the nano-bubble lattice in the af-                    
fected regions, whose over pressurized gas inventory is then col-                V
                                                                                              = 5.2 · f d − 0.1                                              (2)
lected by the inter-granular bubble population developing at the                 V0
                                                                                          f
boundaries of the newly reﬁned sub-micron grains [9,10]. The ﬁs-
sion density corresponding to the onset of grain reﬁnement, as                  For 0.5 < fd < 3.0 and ﬁssion density in multiples of 1021
well as the rate at which grain reﬁnement proceeds with increas-             ﬁssions/cm3 and
                                                                                     
ing ﬁssion density, may signiﬁcantly impact the total fuel swelling              V
observed at higher ﬁssion densities. At the highest achievable ﬁs-                            = 7.1 · f d − 6.6                                              (3)
                                                                                 V0
sion densities, localized regions of the crystalline γ -(U,Mo) phase                      f

can become amorphous, as has been observed using transmission                   For 3 < fd < 4.5 and ﬁssion density in multiples of 1021
electron microscopy (TEM) [11]. In addition to the primary oper-             ﬁssions/cm3 .
ating parameters (i.e., temperature and ﬁssion rate), many other                In an internal engineering report, Perez and Robinson [14] used
variables may have an effect on ﬁssion-gas behavior. Among these             both mini-plate-thickness measurements and metallographic im-
are local variations in microstructure, fuel/cladding interfaces, sec-       ages to calculate volume change. They indicated that the data used
ondary phases, and impurities.                                               to perform the plate-thickness fuel-swelling calculations included
    Fig. 1 shows the progression of ﬁssion-gas bubble morphology             the pre-irradiation plate thickness, the pre-irradiation fuel-foil
in U-Mo fuel. The top left shows the bubble superlattice at ﬁssion           thickness, the measured oxide thickness, and the post-irradiation
densities ~2.0 × 1021 ﬁssions/cm3 , the top right shows the collec-          plate thickness. Based on these available measurements, they cal-
tion of ﬁssion-gas bubbles at grain boundaries at ﬁssion densities           culated the total volume increase of the fuel zone and proposed
~3.0 × 1021 ﬁssions/cm3 , the bottom left shows micrometer scale             an empirical swelling model. A separate model was also developed
ﬁssion-gas bubbles at ﬁssion densities ~5.5 × 1021 ﬁssions/cm3 ,             using the metallographic images.
and the bottom right shows larger micrometer scale ﬁssion-gas                   Perez and Robinson indicated that the correlation for plate-
bubbles at ﬁssion densities ~7.5 × 1021 ﬁssions/cm3 .                        thickness data based on the calculated swelling was the curve ﬁt
                                                                             to the corresponding data (not including failed and delaminated
1.2. Modeling Swelling Behavior                                              plates) as:
                                                                                     
                                                                                 V                                                               2
   If fuel were mechanically unconstrained, volumetric swelling                               = 20.60 + 8.03 · ( fd − 3 ) + 0.924 · ( fd − 3 )               (4)
                                                                                 V0
would be isotropic. For the plate-type fuels typical in HPRRs, how-                       f
ever, signiﬁcant lateral and longitudinal mechanical constraint is           for fd < 6.8 × 1021 and ﬁssion density in multiples of 1021
applied to the fuel by the aluminum cladding. This constraint, in            ﬁssions/cm3 .
concert with fuel relocation that occurs as a result of irradiation-            Similarly, a correlation for the metallographic image data, based
assisted creep, results in dimensional changes only in the plate             on the calculated swelling, was the curve ﬁt to the corresponding
thickness direction [12]. The swelling in aluminum clad plate-type           data (not including failed and delaminated plates) as:
fuel is thus evaluated primarily through examination of changes                      
to plate thickness. In order to maintain consistency with historical             V                                                               2
                                                                                              = 23.87 + 7.27 · ( fd − 3 ) + 0.374 · ( fd − 3 )               (5)
nomenclature, all plate-thickness increase is herein referred to as              V0
                                                                                          f

                                                                         2
A.B. Robinson, W.J. Williams, W.A. Hanson et al.                                                                                      Journal of Nuclear Materials 544 (2021) 152703




                                                   Fig. 1. Progression of ﬁssion-gas bubbles in U-Mo from top left to bottom right.


for fd < 8.2 and ﬁssion density in multiples of 1021 ﬁssions/cm3 .                            for fd > 0.5 and ﬁssion density in multiples of 1021 ﬁssions/cm3 .
where (  V0 ) f is total volumetric swelling in (%).
           V
                                                                                              where (  V0 ) f is total volumetric swelling in (%).
                                                                                                         V

    Perez and Robinson [14] indicated that the standard deviation                                 Rest [16] modeled fuel swelling based on literature published
on the optical metallography data for fuel swelling vs. ﬁssion den-                           for irradiated U-Mo monolithic fuel irradiated at temperatures un-
sity was 13.07%. The standard deviation on the measured thickness                             der 600°C in the RERTR–6, RERTR–7, and RERTR–9 campaigns, and
data for fuel swelling vs. ﬁssion density was 12.41%. Based on this                           reports that the solid ﬁssion-product swelling is a linear function
information, they recommended that “calculated swelling” corre-                               of burnup (i.e., ﬁssion density) as:
lation (Equation [4]) should be used for the appropriate ﬁssion-                                      
                                                                                                  V
density range.                                                                                              = 3.5 × 10−21 · fd                                                  (8)
                                                                                                  V0
    In a previously unpublished work by Wachs et al. [15], post-                                        s
irradiation thickness measurements and in-canal ultrasonic test-                              where ( 
                                                                                                      V )s is the solid ﬁssion product swelling in (%) and fd is
                                                                                                       V
                                                                                                            0
ing data sets were used to propose models to express volumetric
                                                                                              the local ﬁssion density in ﬁssions/cm3 .
swelling strains. He indicated that the best-ﬁt correlation for the
                                                                                                 He reported that gas-bubble swelling has different rates de-
experimental data based on the post-irradiation examination (PIE)
                                                                                              pending on ﬁssion density, as follows:
swelling is given by,                                                                                 
                                                                                                V
    V                                                                  2
                                                                                                            = 1.8 × 10−21 · fd for fd ≤ 3 × 1021 ﬁssions/cm3                    (9)
                 = 18.15 + 9.56 · ( fd − 3 ) − 0.122 · ( fd − 3 )                   (6)           V0
                                                                                                        g
    V0                                                                                                
             f
                                                                                                  V                                                       
for fd > 0.5 × 1021 and ﬁssion density in multiples of 1021                                                 = 5.4 + 2.1 × 10−21 · fd − 3 × 1021
                                                                                                  V0
                                                                                                        g
ﬁssions/cm3 .                                                                                                                                         2
   He also indicated that the best-ﬁt correlation for the experi-                                               + 0.43 × 10−42 · fd − 3 × 1021                                (10)
ment data based on the ultrasonic testing swelling data is
                                                                                            for fd   > 3 × 1021      ﬁssions/cm3 . where         ( V )
                                                                                                                                        V0 g is the gaseous ﬁs-
    V                                                                  2                     sion product swelling (in %) and fd is the local ﬁssion density in
                 = 19.72 + 6.73 · ( fd − 3 ) + 0.485 · ( fd − 3 )                   (7)
    V0
             f
                                                                                              ﬁssions/cm3 .

                                                                                          3
A.B. Robinson, W.J. Williams, W.A. Hanson et al.                                                                                 Journal of Nuclear Materials 544 (2021) 152703




                                                   Fig. 2. Comparison of swelling models reported in the literature [2,13–16].



    Furthermore, the fuel swelling of U-Mo alloy was modeled by                            historical swelling data. It is worth noting that all swelling analy-
Kim and Hofman [2], and an empirical model of swelling as a func-                          sis of U-Mo fuel for research reactors to date assumes no power or
tion of ﬁssion density was developed based on evaluation of fuel                           temperature dependence of the swelling rate.
plates irradiated as part of the RERTR-6 through RERTR-9 experi-
ments. The model assumes a linear swelling correlation at low ﬁs-                          1.3. Calculating Fuel Swelling
sion densities, below 3.0 × 1021 ﬁssions/cm3 , and an increased re-
lationship at higher ﬁssion densities due to ﬁssion-gas-bubble for-                        1.3.1. Plate Average Fuel Swelling
mation and growth. The model was developed based on metallo-                                    Ascertaining the fuel swelling within each fuel plate is the
graphic post-irradiation fuel thickness measurements made on a                             ﬁrst step to developing a new swelling correlation; however, there
limited number of fuel plates. The data set used to establish this                         are multiple approaches to measure and calculate fuel swelling.
model was carefully selected by the authors to eliminate outliers                          One approach is to measure the average swelling of a fuel plate—
and plates which were considered non-representative. This ap-                              i.e., its volumetric growth during irradiation. This may be deter-
proach differs from the statistical approach used by Perez, Robin-                         mined through pre- and post-irradiation measurements of immer-
son, and Wachs, in which all data were used, and the ﬁt was based                          sion density using the Archimedes method to establish the plate
on the assumption of statistical representativeness of the collection                      volume changes. The volume of the plate can be calculated us-
of the results, even as some outliers were included.                                       ing Eq. (13), and plate-average fuel swelling may then be calcu-
    The corresponding equations Kim and Hofman [2] provide to                              lated using Eq. (14), assuming no growth of the aluminum dur-
describe the swelling empirically are as follows:                                          ing irradiation. Immersion density provides bulk (i.e. plate aver-
                                                                                         age) U-Mo swelling values because it bypasses Eq. (1) by directly
    V
                 = 5.0 · fd f or fd ≤ 3x1021 f issions/cm3                      (11)       measuring the plate volume change. This has the advantage of
    V0
             f                                                                             eliminating local contributions to plate-thickness changes, such as
                                                                                         pre-irradiation foil-thickness variations and fuel relocation, due to
    V
                 = 15 + 6.3 · ( fd − 3 ) + 0.33                                            creep, instead accounting only for total volumetric growth of the
    V0
             f                                                                             fuel.
                              2
                   · ( fd − 3 ) f or fd > 3x1021 f issions/cm3                  (12)                            Massdry − Masssubmerged
                                                                                           P l ate V ol ume =                                                            (13)
where (V/V0 )f total swelling in percent and fd is the ﬁssion den-                                                        ρ f luid
sity in multiples of 1021 ﬁssions/cm3 .                                                                          P l ate V ol umePost − P l ate V ol ume pre
    The models for total swelling proposed by Kim [2], Leenaers                            F uel Swel l ing =                                                            (14)
                                                                                                                               F uel V ol ume pre
[13], Perez [14], Wachs [15], and Rest [16] are compared in Fig. 2
below. The models proposed by Leenaers for U–7Mo dispersion                                   An example of the calculated plate-average fuel swelling vs.
fuel, Kim-Hofman for U-10Mo monolithic fuel, and Rest for mono-                            plate-average ﬁssion density for the RERTR-12 experiment is
lithic fuel are all very similar. The swelling models proposed by                          shown in Fig. 3. It clearly shows a stable and predictable increase
Perez-Robinson and Wachs predict higher swelling than the other                            in fuel swelling as ﬁssion density increases. The upper and lower
models. This work seeks to revisit this analysis to propose a more                         95% prediction bounds [17] form a prediction interval for a single
complete swelling vs. ﬁssion density correlation, using current and                        future observation—i.e., an interval based on the current data and

                                                                                       4
A.B. Robinson, W.J. Williams, W.A. Hanson et al.                                                                              Journal of Nuclear Materials 544 (2021) 152703




                  Fig. 3. Plate-average fuel swelling for RERTR-12 fuel mini-plates measured by immersion density vs. plate average ﬁssion density [2,17].



model that will, with 95% conﬁdence, contain a future randomly                           gion with negligible thickness increase and a region with addi-
selected observation from the same population [18]. Also plotted                         tional thickness increase and no net volumetric change.
is the highest anticipated plate-average ﬁssion density for the Na-                         Despite these challenges, it is proposed that utilizing the sig-
tional Bureau of Standards Reactor (NBSR), which is projected to                         niﬁcant increase in data provided through local fuel swelling cal-
have the highest ﬁssion density among the USHPRRs at ~6.8 × 1021                         culations will improve resulting models. Further, it is suggested
ﬁssions/cm3 , the ﬁssion density corresponding to 100% LEU burnup                        that these challenges may be overcome through statistical methods
of U-10Mo (~7.8 × 1021 ﬁssions/cm3 ), and the previously described                       to maximize the data that can contribute to the calculations. This
empirical correlation developed by Kim and Hofman. This corre-                           work establishes a predictive swelling correlation for a monolithic-
lation falls within the prediction bounds at ﬁssion densities be-                        type uranium-molybdenum fuel for use in HPRRs using proﬁlome-
low approximately 5.0 × 1021 ﬁssions/cm3 , but at higher ﬁssion                          try data collected over a series of irradiation tests in the Advanced
densities appears to underpredict plate-average fuel swelling. It                        Test Reactor (ATR) at Idaho National Laboratory (INL).
should be noted that while the Kim-Hofman model was not devel-
oped using immersion-density-determined plate average swelling,
                                                                                         2. Materials and Methods
its dataset was designed to emulate plate average swelling. This
was accomplished by averaging from a ﬁne selection of thickness-
                                                                                         2.1. Irradiation Experiments
change data to exclude local contributions, such as fuel relocation,
discussed below, from the model [2].
                                                                                             For this work, only irradiated fuel plates of the HPRR program’s
                                                                                         down-selected fuel type [19] were included, comprising a data set
1.3.2. Local Fuel Swelling
                                                                                         acquired from 74 fuel test plates. The fuel design consists of a
    While plate-average swelling provides useful information re-
                                                                                         U-10Mo monolithic fuel core, a Zr diffusion layer metallurgically
garding the overall behavior of U-Mo under irradiation, the num-
                                                                                         bonded to the faces of the fuel core by a hot co-rolling process,
ber of data points is limited to the number of irradiated sam-
                                                                                         and AA6061 cladding, bonded using a hot isostatic pressing (HIP)
ples. As an alternative, considerably more swelling data are avail-
                                                                                         process. A brief introduction to the geometry and irradiation con-
able by considering local dimensional measurements of the fuel-
                                                                                         ditions for each experiment is included here.
plate thickness to calculate local fuel swelling. Eq. (15) deﬁnes the
                                                                                             The AFIP–3 experiment contained one down-selected full-size
general form of the local fuel swelling relationship by assuming
                                                                                         fuel plate, approximately 570 mm long, 56 mm wide and 1.27 mm
swelling is limited to the fuel:
                                                                                         thick. Beginning-of-life peak power density was 16,0 0 0 W/cm3 ,
                       (Plate T hickness post − Plate T hickness pre )                   and peak ﬁssion density was 4.6 × 1021 ﬁssions/cm3 [20].
% Fuel Swelling =                                                      × 100%                The AFIP–4 experiment contained six down-selected sub-sized
                                   (F uel T hicknss pre )
                                                                                         fuel plates approximately 190.5 mm long, 56 mm wide and
                                                                             (15)
                                                                                         1.27 mm thick. Beginning-of-life power densities ranged from
    Care must be taken when interpreting local dimensional                               9,0 0 0 to 20,0 0 0 W/cm3 , and ﬁssion densities from 2.5 × 1021 to
measurements, as local plate-thickness changes also include                              4.7 × 1021 ﬁssions/cm3 [21].
those changes resulting from mechanisms other than volumetric                                The RERTR–9 and RERTR–10 experiments contained two and
swelling due to ﬁssion products, especially fuel relocation due to                       four down-selected mini-plates, respectively. Plates were ap-
irradiation-assisted creep. This is an added result of the plate-                        proximately 101 mm long, 25.4 mm wide, and 1.27 mm
geometry dimensional constraints that, in addition to limiting all                       thick. Beginning-of-life power densities varied from 12,0 0 0 to
swelling to the plate thickness direction, also prevent the fuel from                    36,0 0 0 W/cm3 and ﬁssion densities from 2.3 to 10.7 × 1021
increasing in thickness at its edge. As the fuel swells, the edge                        ﬁssions/cm3 [22,23].
constraint forces the fuel to relocate, via irradiation-assisted creep,                      The RERTR–12 experiment evaluated the fuel design over a
to adjacent regions, the result of which is both a fuel-zone re-                         wide range of operating conditions, using the same external plate

                                                                                     5
A.B. Robinson, W.J. Williams, W.A. Hanson et al.                                                               Journal of Nuclear Materials 544 (2021) 152703


dimensions as RERTR-9 and 10 and three different U-10Mo foil                   AFIP-6MkII and AFIP-7), tp 0 is the pre-irradiation local plate thick-
thicknesses: 0.254, 0.508, and 0.635 mm. Beginning-of-life power               ness, tf is the initial fuel foil thickness, and tZr is the nominal zir-
densities ranged from 2,200 to 40,0 0 0 W/cm3 , and ﬁssion densi-              conium diffusion layer thickness on the face of the fuel foil.
ties ranged from 0.35 × 1021 to 7.9 × 1021 ﬁssions/cm3 . Through                   The uncertainty of the calculated local fuel-swelling values us-
the use of HEU in order to obtain desired test conditions, ﬁssion              ing the above approach was investigated. Each term in the swelling
densities were in excess of those achievable with LEU, or 19.75%               equation has measurement uncertainty based on the measurement
enriched fuel. In total, 56 mini-plate specimens were tested in the            method, as well as location uncertainty. It was determined that the
experiment; however, due to in-reactor pillowing of 4 plates, only             uncertainty of the swelling was dominated by the pre-irradiation
52 plates were used for this analysis [17].                                    foil-thickness term due to the small number of measurement data
    The AFIP–6MkII experiment was designed to evaluate the high                points and less-precise measurement reporting. Because the uncer-
power, large-scale performance of monolithic U-Mo fuels. The                   tainty varied signiﬁcantly, not only from experiment to experiment,
AFIP–6MkII fuel plate design included a fueled region, 571.5 mm                but also location to location within an experiment, this individual
long that was axially centered in the ATR core. The 235 U en-                  point uncertainty analysis was eventually abandoned in favor of
richment was approximately twice that of previous AFIP exper-                  using statistical methods for analyzing the resulting data sets, as
iments (40% enrichment) in order to yield higher ﬁssion pow-                   explained below.
ers in the specimens [24]. Beginning-of-life peak power density                    In order to correlate local fuel swelling with local ﬁssion den-
was 34,0 0 0 W/cm3 , and peak ﬁssion density was 5.1 × 1021                    sity, local ﬁssion-density values for each of the 74 plates were esti-
ﬁssions/cm3 .                                                                  mated by calculating the local-to-average ratio (L2AR) ﬁssion-rate
    The AFIP–7 experiment [25] was designed to evaluate the per-               gradients using Monte Carlo N-Particle (MCNP) code, which could
formance of monolithic U-Mo fuels in element-assembly geometry                 then be scaled with the average calculated ﬁssion densities.
with curved fuel plates. The fuel was enriched to 19.75 wt.% 235 U.                Due to differences in the locations of the measurement sets
The AFIP–7 plates were formed to a prescribed radius and swaged                and measurement densities, as well as ﬁxed physics calculation
into a single fuel-element assembly. AFIP–7 plates were the largest            grids, data sets were either interpolated or downsized as appro-
irradiated to date: approximately 1016 mm long, 63.5 mm wide,                  priate onto a common data grid. For all plates analyzed, the pre-
and 1.27 mm thick, with a radius of curvature of 90.35 mm. Irradi-             irradiation thickness data (both plate and foil thicknesses) were
ation testing was performed at operating conditions similar to ATR             the sparsest of the data sets. For RERTR-9, 10, and 12 and AFIP-4
driver fuel during normal, non-powered axial locator mechanism                 plates, average pre-irradiation plate and fuel-foil thicknesses were
(PALM) cycle operation. AFIP–7 beginning-of-life ﬁssion power var-             used for the swelling calculations. Due to the small plate and
ied from 11,0 0 0 to 16,0 0 0 W/cm3 , and ﬁssion densities varied from         foil sizes for these experiments, combined with very little vari-
2.0 to 3.1 × 1021 ﬁssions/cm3 over the course of two irradiation               ation in thickness prior to irradiation, this was a valid simpliﬁ-
cycles [26].                                                                   cation. For larger-sized plates (AFIP-3BZ, AFIP-6MkII, and AFIP-7),
                                                                               pre-irradiation data sets were interpolated to create a grid size that
2.2. Local Fuel Swelling Determination                                         matched the calculated ﬁssion-density grid. For AFIP-4 plates, the
                                                                               calculated ﬁssion-density grid was downsized to match the post-
2.2.1. Calculating Fuel Swelling                                               irradiation thickness grid.
    Post-irradiation proﬁlometry was performed on each of the 74                   The resulting local fuel-thickness increases were then plotted
fuel plates of the selected design to determine the local fuel-plate           against the calculated local ﬁssion density, as shown in Fig. 4. The
thickness. All measurements were performed using calibrated mea-               data are grouped by experiment for visualization. The number of
surement devices, and the local oxide-layer thickness was also                 data points in each experiment data set is provided in the leg-
measured using eddy current technique. In experiments in which                 end for reference; the totals include all measurements from each
the oxide-layer was statistically thick enough to affect the thick-            individual plate within that experiment. An important point to
ness of the plate measured in proﬁlometry (AFIP-6MkII and AFIP-                be made regarding the signiﬁcant amount of apparent scatter in
7), the contribution of the oxide-layer was subtracted to correct              the data, shown in Fig. 4, is that some local fuel-thickness-change
the total post-irradiation thickness to just that of the plate. This           values observed at any given ﬁssion density may be considerably
contribution is a fraction of the total oxide layer thickness, due             higher or lower than the underlying trend expected, based on ac-
to the aluminum surface consumed in its formation, and is de-                  cepted fuel swelling correlations. This is primarily as a result of
termined based on the ratio of the density of the oxide formed                 fuel relocation due to irradiation-assisted creep and constrained re-
(3.04 g/cm3 ) to the density of aluminum (2.7 g/cm3 ). Because there           gions at the edges of the plates.
are 27 grams of Al per mole of AlO(OH) and 60 grams of AlO(OH)
per mole of AlO(OH), there are (27/60) × 3.04 grams of Al/cm3                  2.2.2. Binning Data
of AlO(OH) or 1.37 g Al/cm3 AlO(OH). This results in a volumetric                  In order to account for the uncertainties in variations in local
increase of 97.5% [27]; therefore, multiplying the measured oxide              fuel-thickness changes as well as uncertainties in the local calcu-
thickness by 1/1.975 corrects for this volumetric increase.                    lated ﬁssion densities, which contribute to the scatter observed in
    Pre-irradiation plate- and foil-thickness data were obtained               the data, calculated fuel-thickness increases were averaged across
from as-built fabrication-data packages compiled for each experi-              experiment datasets within discrete steps, or “bins.” These bins for
ment, and fuel-core thickness values were veriﬁed in select loca-              averaging data may be deﬁned by ﬁxed steps in ﬁssion density,
tions using optical microscopy. The fuel thickness within the foil is          such as every 0.1 × 1021 (ﬁssions/cm3 ), allowing each data point
further corrected to account for the zirconium barrier layer thick-            within a given ﬁssion density range to contribute to the bin’s av-
ness. In the absence of dimensional changes from other sources                 erage value. Alternatively, bins may be deﬁned by the number of
(e.g., fuel relocation due to irradiation-assisted creep), fuel swelling       data points averaged, such as averaging the closest 100 ﬁssion den-
can then be calculated using equation (16).                                    sity and fuel thickness change data pairs, to create bins having
                                  1
                                          
                           t p − 1.975 tox − t p0                              equal weights. Both binning examples are shown in Fig. 5, and the
% Fuel Swelling =                                 × 100%         (16)        resulting binned data are suggested as an effective approach for
                                 t f − 2tZr
                                                                               mitigating the inherent sources of uncertainty described above and
where tp is the local total plate thickness measured post-                     allowing the underlying fuel-swelling correlation to be established
irradiation, tox is the local surface oxide thickness (included for            from the experimental data.

                                                                           6
A.B. Robinson, W.J. Williams, W.A. Hanson et al.                                                                                  Journal of Nuclear Materials 544 (2021) 152703




                                             Fig. 4. Local fuel-thickness increase vs. local ﬁssion density for each experiment [17].




        Fig. 5. Comparison of local swelling data vs. local ﬁssion density data binned by: (A) 0.1 × 1021 ﬁssions/cm3 increments and (B) 100 data point increments.



    Fig. 5A shows the method of binning by ﬁssion density, with                             ing from each of the four different binning methods, generating
a bin size of 0.1 × 1021 ﬁssions/cm3 , and has data points sized                            prediction models and 95% conﬁdence bounds. Fig. 6 shows the
relative to the number of raw swelling points included in each bin                          linear-regression models have overlapping conﬁdence bounds, in-
(larger points have more data; smaller points, fewer). Fig. 5B shows                        dicating the different binning methods do not statistically affect
the data binned in 100 data point increments. Differences between                           the trend models. Based on these results, the method utilizing 100
the methods can be seen at the higher ﬁssion-density range, where                           data points per bin was selected. This method has the beneﬁt that
the discrete ﬁssion-density method results in more bins with sig-                           each binned data point has the same statistical signiﬁcance and
niﬁcantly fewer points, whereas the equal-bin-size method results                           eliminates the need for weighting the individual bins based on the
in fewer points in this range, but of equal weight. In general,                             number of raw data points within each bin. This binned data were
the smaller number of data points available in the higher ﬁssion-                           used to evaluate different ﬁtting methods and, ultimately, to deﬁne
density range of interest is apparent using either binning method.                          the predictive swelling correlation.
    Statistical analysis was performed to ensure that the choice
of binning methods did not affect the results, comparing four                               3. Results
methods: binning every 0.1 × 1021 (ﬁssions/cm3 ), 0.25 × 1021
(ﬁssions/cm3 ), 0.5 × 1021 (ﬁssions/cm3 ), and 100 nearest data                                The fuel swelling vs ﬁssion density data, binned every 100
points. Linear regression was performed on the data sets result-                            data points, were ﬁt using linear, piecewise linear with variable

                                                                                        7
A.B. Robinson, W.J. Williams, W.A. Hanson et al.                                                                                  Journal of Nuclear Materials 544 (2021) 152703




                                                   Fig. 6. Linear regression of binned data for four different binning methods.




                                                          Fig. 7. Four different model ﬁts to the binned swelling data.


inﬂection point, quadratic, and cubic functions without constrain-                          binned data were ﬁt using the piecewise linear with variable in-
ing the ﬁts through the origin in order to compare different ﬁtting                         ﬂection point. A comparison between the piecewise linear ﬁts of
equations. The binned data and ﬁts are plotted in Fig. 7 with each                          binned data with and without inclusion of the AFIP-6MkII experi-
ﬁt’s R-squared value included in the legend.                                                ment is shown in Fig. 8.
    Given the large concentration of data points from the AFIP-                                Fig. 9 shows the quadratic ﬁt of binned data, including AFIP-
6MkII experiment located in the recrystallization region at appar-                          6MkII, along with 95% conﬁdence bounds. Fig. 10 shows the same
ently higher swelling values in Fig. 4, the data were binned again                          quadratic ﬁt and conﬁdence bounds, plotted with the raw scatter
by 100 data points, excluding AFIP-6MkII for comparison. These                              of data. In both Figs. 9 and 10, 95% prediction bounds are included

                                                                                        8
A.B. Robinson, W.J. Williams, W.A. Hanson et al.                                                                              Journal of Nuclear Materials 544 (2021) 152703




                               Fig. 8. Comparison of piecewise linear ﬁt to binned data with and without inclusion of the AFIP-6MkII data set.




                          Fig. 9. Quadratic ﬁt of all binned data as a function of ﬁssion density, along with 95% conﬁdence and prediction bounds.


based on quadratic model ﬁts of the binned and raw data, respec-                         gaseous ﬁssion-products, which typically results in a non-linear
tively.                                                                                  swelling dependence on ﬁssion density when higher ﬁssion den-
                                                                                         sities are reached.
4. Discussion                                                                                Considering the complicated physical phenomena with multiple
                                                                                         mechanisms involved and the observed dependence of swelling on
4.1. Model Fit Comparison                                                                ﬁssion density over the entire range of interest, swelling correla-
                                                                                         tions for use in fuel performance analyses are frequently developed
    As discussed previously, the solid ﬁssion product-dominated                          using empirical relationships that best ﬁt the experimental data.
swelling that occurs at low ﬁssion densities is known to increase                        This approach was employed here to develop a useful swelling cor-
linearly with increasing ﬁssion density. There is a subsequent in-                       relation. In this case, various empirical correlations were evaluated
crease in the swelling rate as a function of ﬁssion density, typ-                        by analyzing the quality of the ﬁt to the binned data set with
ically observed at intermediate ﬁssion densities. This is due to                         100 data points per bin. Examining Fig. 7, the piecewise linear,
irradiation-induced recrystallization and the associated transition                      quadratic, and cubic functions each appear to adequately represent
from swelling behavior dominated by solid to that dominated by                           the data, with R-squared values exceeding 96%, indicating that the

                                                                                     9
A.B. Robinson, W.J. Williams, W.A. Hanson et al.                                                                          Journal of Nuclear Materials 544 (2021) 152703




Fig. 10. Recommended U-Mo fuel swelling model (Equation [17]) along with 95% prediction bounds for the raw data ﬁt (Equations [20] and [21]) overlaid with the raw data
prior to binning.



ﬁts are high quality. Additionally, the uncertainty bounds for the                     4.2. Recommended Swelling Correlation Model
three model forms (not displayed) are overlapping, suggesting any
of the models will adequately represent swelling.                                         A quadratic ﬁt, constrained through the origin, was performed
    The piecewise linear function was used with a variable inﬂec-                      on the binned data of all experiments, including AFIP-6MkII, and
tion point, optimized to best ﬁt the data, in an attempt to capture                    the resulting swelling correlation is represented in Eq. (17):
the change in swelling rate at intermediate ﬁssion densities asso-
                                                                                       % Swel l ing = 6.13 × 10−43 fd2 + 4.00 × 10−21 fd                          (17)
ciated with the transition from solid to gaseous ﬁssion-product-
dominated swelling behavior. Unsurprisingly, this function has the                     where fd is ﬁssion density in         ﬁssions/cm3 .
                                                                                                                                       The model and 95%
highest R-squared value; however, the location of the transition                       conﬁdence bounds are included in both Figs. 9 and 10, and show
point is highly dependent on the data located in the critical re-                      consistent conﬁdence in the model. Additionally, 95% prediction
crystallization range of ﬁssion densities, between 3.0 × 1021 and                      bounds for the model’s ﬁt to the binned data are plotted in
4.5 × 1021 ﬁssions/cm3 . This is apparent in Fig. 8, where exclud-                     Fig. 9 and show symmetry with the swelling correlation model.
ing the AFIP-6MkII experiment from the binned data results in the                      The equations for the prediction bounds, which may be useful for
inﬂection point shifting from a ﬁssion density of ~3.3 × 1021 to                       reactor-safety analysis, are provided in Eqs. (18) and (19).
~4.5 × 1021 ﬁssions/cm3 . This data set appears possibly to have
higher swelling values than the data obtained from other irradia-                      Lower P rediction Bound = 5.87 × 10−43 fd2 + 4.14 × 10−21 fd − 5.28
tion tests in that ﬁssion-density range. A number of hypotheses are                                                                                               (18)
being investigated to explain this apparent difference in swelling
behavior. One possible explanation is that this higher swelling is                     U pper P rediction Bound = 6.39 × 10−43 fd2 + 3.86 × 10−21 fd + 5.28
due to the earlier onset of recrystallization and subsequent low-                                                                                                 (19)
ering of the transition point in the swelling relationship to lower
ﬁssion densities, possibly due to molybdenum variations, impuri-                           In order to visually demonstrate the outcome of this analysis, as
ties, or higher power density/temperature [28]. It should also be                      shown in Fig. 10, the recommended swelling correlation model is
noted that recrystallization occurs gradually over a range of ﬁssion                   plotted along with all of the raw local swelling data presented pre-
densities, rather than at a sharp threshold. Therefore, due to both                    viously in Fig. 4. The 95% prediction bounds, based on a quadratic
the instability in the location and the unrealistic, sharp nature of                   ﬁt of the raw data and provided in Eqs. (20) and (21), are much
the inﬂection point, a piecewise linear ﬁt cannot provide an ac-                       larger than for the binned data due to greater uncertainties in the
ceptable swelling correlation. Because there is no statistical distinc-                individual swelling and local ﬁssion-density values. However, there
tion between the quadratic and cubic ﬁts, the quadratic ﬁt was se-                     is good symmetrical agreement between the raw-data prediction
lected to reduce the order of the swelling correlation. Additionally,                  bounds and the recommended swelling correlation, derived from
while it is recognized that the AFIP-6MkII experiment had a higher                     the binned data.
power density and temperature envelope than the other experi-
                                                                                       Lower P rediction Bound = 6.12 × 10−43 fd2 + 4.00 × 10−21 fd − 14.79
ments in the data set, its inclusion in or exclusion from the binned
data does not appear to inﬂuence the stability of the quadratic                                                                                                   (20)
ﬁt. Therefore, the experiment is included in the binned data
set as it encompasses the critical recrystallization ﬁssion density                    U pper P rediction Bound = 6.13 × 10−43 fd2 + 4.00 × 10−21 fd + 14.79
regime.                                                                                                                                                           (21)

                                                                                  10
A.B. Robinson, W.J. Williams, W.A. Hanson et al.                                                                          Journal of Nuclear Materials 544 (2021) 152703




Fig. 11. Comparison of the recommended U-Mo fuel-swelling correlation and prediction bounds, Eqs. (17),(18) and (19), determined from local thickness measurements with
fuel swelling for RERTR–12 mini-plates measured by immersion density [17].


    In general, the prediction bounds for the binned data,                             swelling. Instead a quadratic swelling correlation model was pro-
Eqs. (18) and (19), are recommended for use by reactor analysts                        posed, along with 95% prediction bounds for reactor-safety analy-
as they better predict the overall swelling behavior of U-Mo fuel.                     sis, and was validated against separate experiment datasets.
It is recommended that the prediction bounds for the raw data,                             The developed swelling correlation will be further modiﬁed as
Eqs. (20) and (21), should be used by experimenters trying to pre-                     new data are obtained in future testing. Furthermore, if a power
dict individual swelling values or for comparing measurements to                       or temperature dependence of the swelling rate is found to exist
existing data.                                                                         in future testing, additional swelling correlations will be developed
                                                                                       for applicable test conditions.
4.3. Model Validation

    It is appropriate to validate the recommended U-Mo fuel-                           U.S. Department of Energy Disclaimer
swelling correlation model, determined in the preceding analysis
of the extensive local thickness-measurement data set, by compar-                         This information was prepared as an account of work sponsored
ing Eqs. (17◦ C19) with the plate average fuel swelling for RERTR–12                   by an agency of the U.S. Government. Neither the U.S. Govern-
mini-plates measured using immersion density, shown previously                         ment nor any agency thereof, nor any of their employees, makes
in Fig. 3. This comparison is made in Fig. 11 and provides con-                        any warranty, express or implied, or assumes any legal liability or
ﬁdence that the binned data analysis method is sound, and the                          responsibility for the accuracy, completeness, or usefulness of any
recommended U-Mo fuel-swelling correlation accurately predicts                         information, apparatus, product, or process disclosed, or represents
overall average fuel plate behavior, minimizing local uncertainties                    that is use would not infringe privately owned rights. References
of individual measurements. The U-Mo monolithic fuel tested to                         herein to any speciﬁc commercial product, process, or service by
date does not indicate any sign of breakaway swelling up to ﬁssion                     trade name, trademark, manufacturer, or otherwise, does not nec-
densities achievable with an LEU fuel design (100% LEU burnup                          essarily constitute or imply its endorsement, recommendation, or
corresponds to ~7.8 × 1021 ﬁssions/cm3 ). The local fuel-swelling                      favoring by the U.S. Government or any agency thereof. The views
values shown are stable and predictable using the correlation de-                      and opinions of authors expressed herein do not necessarily state
scribed here with the uncertainties indicated.                                         or reﬂect those of the U.S. Government or any agency thereof.

5. Conclusions
                                                                                       Declaration of Competing Interest
    Post-irradiation proﬁlometry data from seven U-Mo plate-type
                                                                                           The authors declare that they have no known competing ﬁnan-
fuel irradiation experiments were used to develop a predictive
                                                                                       cial interests or personal relationships that could have appeared to
swelling correlation model based on statistical binning of the data
                                                                                       inﬂuence the work reported in this paper.
to reduce scatter and reveal the underlying intrinsic swelling trend
of the fuel type. Multiple methods for binning the large quan-
tity of data were compared, and binning every 100 data points                          CRediT authorship contribution statement
was selected to provide equal weighting between bins, and dif-
ferent models for ﬁtting this binned data were analyzed. Though                           A.B. Robinson: Conceptualization, Writing - original draft,
a piece-wise linear model provided the highest R-squared ﬁt, it is                     Methodology. W.J. Williams: Data curation, Visualization. W.A.
not recommend for the swelling correlation, due to instability in                      Hanson: Writing - review & editing. B.H. Rabin: Supervision, Writ-
the inﬂection point and the gradual nature of the recrystallization-                   ing - review & editing. N.J. Lybeck: Software, Data curation. M.K.
driven transition from solid to gaseous dominated ﬁssion-product                       Meyer: Supervision.

                                                                                  11
A.B. Robinson, W.J. Williams, W.A. Hanson et al.                                                                                       Journal of Nuclear Materials 544 (2021) 152703


Acknowledgements                                                                                 [12] P. Medvedev, S. Miller, Analysis of monolithic in-plane fuel meat swelling,
                                                                                                      Idaho National Laboratory Place Holder.
                                                                                                 [13] A. Leenaers, Surface engineered low enriched uranium-molybdenum fuel for
    This work is supported by the U.S. Department of Energy, un-                                      research reactors: in- and out-of-pile studies for the conversion of research
der DOE Idaho Operations Oﬃce Contract DE-AC07-05ID14517. Ac-                                         reactors from using high-enriched to low-enriched nuclear fuels PhD Thesis,
cordingly, the U.S. Government retains a nonexclusive, royalty-free                                   University of Ghent - SCK-CEN, 2014.
                                                                                                 [14] D.M. Perez, A.B. Robinson, RERTR Mini-plate Monolithic Fuel Swelling, Rev. 0,
license to publish or reproduce the published form of this contri-                                    ECAR-1367, Idaho National Laboratory, February 2011.
bution, or allow others to do so, for U.S. Government purposes.                                  [15] D. Wachs et.al., Draft Report on Information Relevant to U-Mo Fuel Design,
                                                                                                      INL/LTD-12-25703, Idaho National Laboratory, 2013.
References                                                                                       [16] J. Rest, Y.S. Kim, G.L. Hofman, M.K. Meyer, S.L. Hayes, U–Mo Fuels Handbook,
                                                                                                      ANL 09/31, Argonne National Laboratory, 2009.
                                                                                                 [17] F. Rice, W. Williams, A. Robinson, J. Harp, M. Meyer, B. Rabin, RERTR-12 Post-
 [1] G. Hofman, L. Walters, Materials Science and Technology: A Comprehensive
                                                                                                      irradiation Examination Summary Report, INL/EXT-14-33066, Idaho National
     Treatment, in: Nuclear Materials Volume 10A, Wiley-VCH, Weinheim, New
                                                                                                      Laboratory, February 2015. doi:10.2172/1173078.
     York, 1994, p. 25.
                                                                                                 [18] W.Q. Meeker, G.J. Hahn, L.A. Escobar, Statistical Intervals: A Guide for Prac-
 [2] Y. Kim, G. Hofman, Fission product induced swelling of U-Mo alloy fuel, Journal
                                                                                                      titioners and Researchers, 2nd Edition, John Wiley & Sons, Inc., Hoboken, NJ,
     of Nuclear Materials 419 (1-3) (2011) 291–301, doi:10.1016/j.jnucmat.2011.08.
                                                                                                      April 2017.
     018.
                                                                                                 [19] A.B. Robinson, D.M. Perez, D.L. Porter, G.L. Chang, D.D. Keiser Jr., D.M. Wachs,
 [3] J. Gan, B.D. Miller, D.D. Keiser Jr., A.B. Robinson, J.W. Madden, P.G. Medvedev,
                                                                                                      G. Hofman, Irradiation Performance of U-Mo Alloy Based Monolithic Plate-Type
     D. Wachs, Microstructural characterization of irradiated U–7Mo/Al-5Si disper-
                                                                                                      Design Selection Update, INL/EXT-09-16807 Revision 1, Idaho National Labora-
     sion fuel to high ﬁssion density, Journal of Nuclear Materials 454 (1-3) (2014)
                                                                                                      tory, July 2013. doi:10.2172/968567.
     434–445, doi:10.1016/j.jnucmat.2014.08.052.
                                                                                                 [20] D.M. Perez, M.A. Lillo, G.S. Chang, G.A. Roth, N.E. Woolstenhulme, D.M. Wachs,
 [4] J. Gan, J.D.D. Keiser, B.D. Miller, A.B. Robinson, D.M. Wachs, M.K. Meyer, Ther-
                                                                                                      AFIP-3 Irradiation Summary Report, INL/EXT-11-21776, Idaho National Labora-
     mal Stability of Fission Gas Bubble Superlattice in Irradiated U–10Mo Fuel,
                                                                                                      toy, March 2012. doi:10.2172/1058080.
     Journal of Nuclear Materials 464 (2015) 1–5, doi:10.1016/j.jnucmat.2015.04.
                                                                                                 [21] D.M. Perez, M.A. Lillo, G.S. Chang, G.A. Roth, N.E. Woolstenhulme, D.M. Wachs,
     023.
                                                                                                      AFIP-4 Irradiation Summary Report, INL/EXT-11-23297, Idaho National Labora-
 [5] B.D. Miller, J. Gan, D.D. Keiser Jr., A.B. Robinson, J.F. Jue, J.W. Madden,
                                                                                                      tory, January 2012. doi:10.2172/1027915.
     P. Medvedev, Transmission electron microscopy characterization of the ﬁssion
                                                                                                 [22] D.M. Perez, M.A. Lillo, G.S. Chang, G.A. Roth, N.E. Woolstenhulme, D.M. Wachs,
     gas bubble superlattice in irradiated U–7wt%Mo dispersion fuels, Journal of
                                                                                                      RERTR-9 Irradiation Summary Report, INL/EXT-10-18421, Idaho National Labora-
     Nuclear Materials 458 (2015) 115–121, doi:10.1016/j.jnucmat.2014.12.012.
                                                                                                      tory, May 2011. doi:10.2172/1023454.
 [6] D. Salvato, A. Leenaers, W. Van Renterghem, S. Van den Berghe, C. Detavernier,
                                                                                                 [23] D.M. Perez, M.A. Lillo, G.S. Chang, G.A. Roth, N.E. Woolstenhulme, D.M. Wachs,
     J. Evans, The initial formation stages of a nanobubble lattice in neutron irra-
                                                                                                      RERTR-10 Irradiation Summary Report, INL/EXT-10-18456, Idaho National Lab-
     diated U(Mo), Journal of Nuclear Materials 529 (151947) (2020), doi:10.1016/j.
                                                                                                      oratory, May 2011. doi:10.2172/1023460.
     jnucmat.2019.151947.
                                                                                                 [24] D.M. Perez, J.W. Nielsen, G.S. Chang, D.M. Wachs, G.A. Roth, N.E. Woolsten-
 [7] S. Van den Berghe, W. Van Renterghem, A. Leenaers, Transmission electron mi-
                                                                                                      hulme, AFIP-6 Mark II Irradiation Summary Report, INL/EXT-12-26305, Idaho
     croscopy investigation of irradiated U–7wt%Mo dispersion fuel, Journal of Nu-
                                                                                                      National Laboratory, September 2012. doi:10.2172/1083245.
     clear Materials 375 (3) (2008) 340–346, doi:10.1016/j.jnucmat.2007.12.006.
                                                                                                 [25] W.J. Williams, A.B. Robinson, B.H. Rabin, Post-Irradiation Non-Destructive Anal-
 [8] W. Van Renterghem, B. Miller, A. Leenaers, S. Van den Berghe, J. Gan, J. Mad-
                                                                                                      yses of the AFIP-7 Experiment, The Minerals, Metals & Materials Society 69
     den, D. Keiser, Transmission electron microscopy investigation of neutron irra-
                                                                                                      (12) (2017) 2546–2553, doi:10.1007/s11837- 017- 2552- y.
     diated Si and ZrN coated UMo particles prepared using FIB, Journal of Nuclear
                                                                                                 [26] D.M. Perez, J.W. Nielsen, G.S. Chang, G.A. Roth and N.E. Woolstenhulme, AFIP–
     Materials 498 (2018) 60–70, doi:10.1016/j.jnucmat.2017.10.016.
                                                                                                      7 Irradiation Summary Report, INL/EXT-12-25915, Idaho National Laboratory,
 [9] J. Gan, B.D. Miller, D.D. Keiser Jr., J.F. Jue, J.W. Madden, A.B. Robinson, H. Ozal-
                                                                                                      September 2012. doi:10.2172/1083244.
     tun, G. Moore, M.K. Meyer, Irradiated microstructure of U-10Mo monolithic
                                                                                                 [27] S. Van den Berghe, Y. Parthoens, F. Charollais, Y.-S. Kim, A. Leenaers, E. Koo-
     fuel plate at very high ﬁssion density, Journal of Nuclear Materials 492 (2017)
                                                                                                      nen, V. Kuzminov, P. Lemoine, C. Jarousse, H. Guyon, D. Wachs, D. Keiser
     195–203, doi:10.1016/j.jnucmat.2017.05.035.
                                                                                                      Jr, A. Robinson, J. Stevens, G. Hofman, Swelling of U(Mo)–Al(Si) dispersion
[10] J. Rest, Evolution of ﬁssion-gas-bubble-size distribution in recrystallized U–
                                                                                                      fuel under irradiation – Non-destructive analyses of the LEONIDAS E-FUTURE
     10Mo nuclear fuel, Journal of Nuclear Materials 407 (1) (2010) 55–58, doi:10.
                                                                                                      plates, Journal of Nuclear Materials 430 (1-3) (2012) 246–258, doi:10.1016/j.
     1016/j.jnucmat.2010.07.009.
                                                                                                      jnucmat.2012.06.045.
[11] M.K. Meyer, J. Gan, J.-F. Jue, D.D. Keiser Jr., E. Perez, A.B. Robinson, D.M. Wachs,
                                                                                                 [28] W. Williams, F. Rice, A. Robinson, M. Meyer, B. Rabin, AFIP–6MII Post-
     N. Woolstenhulme, G.L. Hofman, Y.S. Kim, Irradiation Performance of U–Mo
                                                                                                      irradiation Examination Summary Report, INL/EXT-20-34142 Revision 0, Idaho
     Monolithic Fuel, Nuclear Engineering and Technology 46 (2) (2014) 169–182,
                                                                                                      National Laboratory, 2015.
     doi:10.5516/NET.07.2014.706.




                                                                                            12
