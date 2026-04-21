# Characterization of intergranular fission gas bubbles in U-Mo fuel

---

                                    ANL-08/11




Characterization of Intergranular
Fission Gas Bubbles in U-MO Fuel




Nuclear Engineering Division
About Argonne National Laboratory
Argonne is a U.S. Department of Energy laboratory managed by UChicago Argonne, LLC
under contract DE-AC02-06CH11357. The Laboratory’s main facility is outside Chicago,
at 9700 South Cass Avenue, Argonne, Illinois 60439. For information about Argonne,
see www.anl.gov.




Availability of This Report
This report is available, at no cost, at http://www.osti.gov/bridge. It is also available
on paper to the U.S. Department of Energy and its contractors, for a processing fee, from:
		 U.S. Department of Energy
   Office of Scientific and Technical Information
		 P.O. Box 62
		 Oak Ridge, TN 37831-0062
		 phone (865) 576-8401
		 fax (865) 576-5728
		 reports@adonis.osti.gov




Disclaimer
This report was prepared as an account of work sponsored by an agency of the United States Government. Neither the United States
Government nor any agency thereof, nor UChicago Argonne, LLC, nor any of their employees or officers, makes any warranty, express
or implied, or assumes any legal liability or responsibility for the accuracy, completeness, or usefulness of any information, apparatus,
product, or process disclosed, or represents that its use would not infringe privately owned rights. Reference herein to any specific
commercial product, process, or service by trade name, trademark, manufacturer, or otherwise, does not necessarily constitute or imply
its endorsement, recommendation, or favoring by the United States Government or any agency thereof. The views and opinions of
document authors expressed herein do not necessarily state or reflect those of the United States Government or any agency thereof,
Argonne National Laboratory, or UChicago Argonne, LLC.
                                                            ANL-08/11




Characterization of Intergranular
Fission Gas Bubbles in U-MO Fuel




by
Y.S. Kim, G.L. Hofman, and J. Rest
Nuclear Engineering Division, Argonne National Laboratory


February 14, 2008
                                           Table of Contents


Summary                                                                                               viii


Section 1       Introduction ……...……………………………………..………..........                                         1


Section 2       Characterization of grain and grain boundary …………….…..............                      4
2.1     Pre-irradiation grain morphology of atomized U-Mo ….………………..........                            4
2.2     Homogenization of ‘cored’ microstructure during irradiation …………..........                      6
2.3     Pre-irradiated microstructure of machined U-Mo ………….…………………                                     8
2.4     Post irradiation measurement of grain size ……………...……………………                                     9


Section 3       Quantitative analysis of intergranular bubbles ………….…................. 15
3.1     Bubble size and population distribution on grain boundaries ………………...                          15
3.2     Bubble density analysis ....………………………………………...…….......... 30
3.2.1   Bubble density per unit grain-boundary length ………………………………. 30
3.2.2   Bubble density per unit fuel cross section area ……………………………….                                  31
3.2.3   Bubble density per unit grain surface area ……………………………………                                      35
3.2.4   Bubble density per unit fuel volume ………………………………………….                                          40
3.3     Gas bubble volume fraction and fission gas swelling. ......................................    41


Section 4       Mechanistic model development …………………………….……….                                         45
4.1     Calculation of evolution of average intra and intergranular bubble-size and
        density ………………………………………………………………………...                                                         45
4.2     Calculation of bubble-size distribution on grain boundaries …………………                            49
4.3     Comparison of calculated intergranular bubble-size distribution with the
        measured data …………………………………………………………………                                                        52
4.4     Calculation of intragranular bubble-size distribution: effect of uncertainties
        in materials properties ……………………………………...............................                          64
4.5     Conclusions …………………………………………………………………...                                                       67
        References …....……………………………………………………………….                                                      68


                                                  iii
                                                     List of Figures


Figure                                                                                                              Page

1.       OM (optical microscopy) photos showing microstructure of hot side of
         R2R040 from RERTR-7A. Burnup of this region is 90 at%U-235 (LEU
         equiv.). The gray areas are fuel and bright areas are Al matrix. The black
         spots in fuel are fission gas bubbles. The interaction layers located along the
         intersection of the fuel particles and the aluminum matrix are very thin. .........                             2

2.       SEM (scanning electron microscopy) photos of irradiated U-Mo fuels from
         RERTR-4 and 5. The samples shown in this figure were fabricated with the
         same batch of atomized fuel particles and irradiated at similar temperatures. .                                3

3.       U-Mo phase diagram. ........................................................................................    5

4.       SEM image of a U-7Mo-1Zr alloy particle after metallographic etching [2].
         This fuel particle is larger (~200 μm) than the typical size (~75 μm) used in
         RERTR-3 plates. ……………………………………………………..……..                                                                     5

5.       Model of the initial condition of grain and grain boundary and corresponding
         Mo-concentration. CL=centerline, GB=grain boundary, b=half of GB
         thickness, L=distance between two neighbor grain centers (i.e., grain size). ...                                6

6.       Time-dependent Mo concentration. CMo(1.5,t) is the time-dependent Mo
         concentration at the grain center, C(0,t) is the time-dependent Mo
         concentration at the grain boundary center. Data used for the calculation are:
         fission rate=6x1014 f/cm3-s, D=1.6x10-16 cm2/s, grain size (L)=3 μm, grain
         boundary width (2b)=0.5 μm. ...………………………………………………                                                               7

7.       OM micrographs of γ-annealed powder plates. Y02 and Z02 are the siblings
         of Y01 and Z03, respectively. ………………....……………………….……..                                                          8

8.       OM and SEM micrographs of Z03. Z03 fuel powder was γ-phase annealed
         for 100 hours at 800oC before plate-fabrication. ……………...………………                                                 9

9.       OM and SEM micrographs of Y01. Y01 fuel powder was γ-phase annealed
         for 100 hours at 800oC before plate-fabrication. …………..…………………                                                 10

10.      OM and SEM of V03. ...………………………………………………………                                                                    11

11.      Grain size distribution in V03. ...……………………………………………... 12




                                                           iv
12.   OM of S03. ...…………………………………………………………………. 13

13.   Bubble size distributions for 580H-Z03 plate from RERTR-3 (γ-annealed). ... 16

14.   Bubble size distribution for 580C-Y01 plate from RERTR-3 (γ-annealed). …         17

15.   Bubble size distribution for V002 plate from RERTR-1. …...………………..               18

16.   Bubble size distribution for A003 plate from RERTR-1. ...…………………..               19

17.   Bubble size distribution for 580G-V07 plate from RERTR-3. ...…………….. 20

18.   Bubble size distribution for 580W-V03 plate from RERTR-3. ...…………….              21

19.   Bubble size distribution for 580Z-S03 plate from RERTR-3. ...……………...            22

20.   Bubble size distribution for 600Y-A6008H plate from RERTR-5. ...………...           23

21.   Bubble size distribution for 600AG-R6007F plate from RERTR-5. ...……….            24

22.   Bubble size distribution for 600M-V6019G plate from RERTR-5. ...………..            25

23.   Bubble size distribution for 600D-V6018G plate from RERTR-5. …...……...           26

24.   Bubble size distribution for 600AH-V8005B plate from RERTR-5. ...………             27

25.   Bubble size distribution for 600V-A8002L plate from RERTR-5. ……...…...           28

26.   Measured average bubble size vs. fission density. …..……………………….                  29

27.   Number of bubbles per unit length vs. fission density. ...…………………….. 31

28.   Tetrakaidecahedron (TKDH) modeling of grain cross section. ...……………. 33

29.   Number of bubbles per unit fuel cross section area calculated from ρL. ...…...   34

30.   Comparison between the measured and calculated grain boundary length per
      unit fuel cross section area vs. grain size. .……………………………………                     35

31.   Schematic of the model used for bubble distribution analysis on the grain
      surface. ...……………………………………………………………………...                                        35

32.   Schematic of possible grain boundary bubble configurations on cross section      36

33.   Schematic showing the method to determine the average distance between
                                                                                       37
      bubbles. ...……………………………………………………………………..


                                           v
34.   Number of bubbles per unit grain boundary surface area vs. fission density. .. 39
35.   SEM photo of A6008H (600Y) from RERTR-5 showing an example of
      surface area bubbles. The red marker is for the area the bubble density was
      measured. ...…………………………………………………………………... 40
36.   Number of bubbles per unit fuel volume calculated from ρ S . ..……………... 41

37.   Gas bubble volume fraction calculated from ρCS . ...…………………………. 43

38.   Comparison of total fuel swelling assessed from plate thickness changes and
      contribution by intergranular gas bubble swelling. ...………………………..               44

39.   Calculated and measured intergranular bubble-size distribution for Z03 plate.
      Atomized and γ-annealed U-10Mo. ….……………………………………….                              55

40.   Calculated and measured intergranular bubble-size distribution for Y01 plate.
      Machined and γ-annealed U-10Mo. ...………………………………………... 56

41.   Calculated and measured intergranular bubble-size distribution for V03. As-
      atomized U-10Mo. ...………………………………………………………….                                     57

42.   Calculated and measured intergranular bubble-size distribution for V07. As-
      atomized U-10Mo. ...………………………………………………………….                                     58

43.   Calculated and measured intergranular bubble-size distribution for V8005B.
      As-atomized U-10Mo. ...……………………………………………………...                                  59

44.   Calculated and measured intergranular bubble-size distribution for V6019G.
      As-atomized U-10Mo. ...……………………………………………………...                                  60

45.   Calculated and measured intergranular bubble-size distribution for V002. As-
      atomized U-10Mo. ...…………………………………………………………. 61

46.   Calculated and measured intergranular bubble-size distribution for S03. As-
      atomized U-6Mo. ...…………………………………………………………...                                    62

47.   Calculated and measured intergranular bubble-size distribution for R6007F.
      As-atomized U-7Mo. ...……………………………………………………….                                    63

48.   Calculated intragranular bubble size distributions for 3 values of the gas-
      atom diffusivity (Dg) and gas-atom re-solution rate (b0). ...…………………..          66




                                          vi
                                        List of Tables


Table                                                                               Page

1.      Grain size measurement for RERTR-3 plates …...…………………………… 14

2.      Description of fuel used in the analysis ………………………………………                      15

3.      Average bubble sizes from measurements …………………………………… 29

4.      Measured number of bubbles per grain boundary length …………………….. 30

5.      Grain size measurement ………………………………………………………                                  32

6.      Number of bubbles per unit fuel cross section area converted from the
        measured bubble number per unit grain boundary length data ………………. 34

7.      Calculated and measured number of bubbles per unit grain surface area ( ρ S ). 39

8.      Gas bubble volume fractions …………………………………………………. 42

9.      Values of parameters used in the calculations ………………………………..                  53

10.     Description of fuel used in the analysis ………………………………………                      54

11.     Intragranular results using estimated values for D g and b ………………….           54




                                           vii
                                               Summary


This report can be divided into two parts: the first part, which is composed of sections 1, 2, and
3, is devoted to report the analyses of fission gas bubbles; the second part, which is in section 4,
is allocated to describe the mechanistic model development.

Swelling data of irradiated U-Mo alloy typically show that the kinetics of fission gas bubbles is
composed of two different rates: lower initially and higher later. The transition corresponds to a
burnup of ~40 at% U-235 (LEU) or a fission density of ~3x1021 fissions/cm3. Scanning electron
microscopy (SEM) shows that gas bubbles appear only on the grain boundaries in the pre-
transition regime. At intermediate burnup where the transition begins, gas bubbles are observed
to spread into the intragranular regions. At high burnup, they are uniformly distributed
throughout fuel.

In highly irradiated U-Mo alloy fuel large-scale gas bubbles form on some fuel particle
peripheries. In some cases, these bubbles appear to be interconnected and occupy the interface
region between fuel and the aluminum matrix for dispersion fuel, and fuel and cladding for
monolithic fuel, respectively. This is a potential performance limit for U-Mo alloy fuel.

Microscopic characterization of the evolution of fission gas bubbles is necessary to understand
the underlying phenomena of the macroscopic behavior of fission gas swelling that can lead to a
counter measure to potential performance limt. The microscopic characterization data,
particularly in the pre-transition regime, can also be used in developing a mechanistic model that
predicts fission gas bubble behavior as a function of burnup and helps identify critical physical
properties for the future tests.

Analyses of grain and grain boundary morphology were performed. Optical micrographs and
scanning electron micrographs of irradiated fuel from RERTR-1, 2, 3 and 5 tests were used.
Micrographic comparisons between as-fabricated and as-irradiated fuel revealed that the site of
first bubble appearance is the grain boundary. Analysis using a simple diffusion model showed
that, although the difference in the Mo-content between the grain boundary and grain interior
region decreased with burnup, a complete convergence in the Mo-content was not reached at the
end of the test for all RERTR tests.

A total of 13 plates from RERTR-1, 2, 3 and 5 tests with different as-fabrication conditions and
irradiation conditions were included for gas bubble analyses. Among them, two plates contained
powders γ-annealed at ~800oC for ~100 hours. Most of the plates were fabricated with as-
atomized powders except for two as-machined powder plates. The Mo contents were 6, 7 and
10wt%. The irradiation temperature was in the range 70 – 190oC and the fission rate was in the
range 2.4x1014 – 7x1014 f/cm3-s.

Bubble size for both of the γ-annealed powder plates is smaller than the as-atomized powder
plates. The bubble size for the as-atomized powder plates increases as a function of burnup and
the bubble growth rate shows signs of slowing at burnups higher than ~40 at% U-235 (LEU).
The bubble-size distribution for all plates is a quasi-normal, with the average bubble size ranging


                                            viii
0.14 - 0.18 μm. Although there are considerable errors, after an initial incubation period the
average bubble size increases with fission density and shows saturation at high fission density.

Bubble population (density) per unit grain boundary length was measured. The γ-annealed
powder plates have a higher bubble density per unit grain boundary length than the as-atomized
powder plates. The measured bubble number densities per unit grain boundary length for as-
atomized powder plates are approximately constant with respect to burnup.

Bubble density per unit cross section area was calculated using the density per unit grain
boundary length data. The grains were modeled as tetrakaidecahedrons. Direct measurements for
some plates were also performed and compared with the calculated quantities.

Bubble density per unit grain boundary surface area was calculated by using the density per unit
grain boundary length data. These data were used as input for mechanistic modeling described in
section 4.

Volumetric bubble density was calculated by using density per unit grain boundary surface area.
Based on these data, bubble volumetric fraction was calculated. Bubble volume fraction was also
calculated by using the density per unit cross section area. Bubble volume fraction was also
directly measured for some plates. These three results are comparable although the direct
measurement data are slightly larger than the others. Bubble volume fraction increased as a
function of burnup, reaching ~2% of fuel volume at 3x1021 f/cm3. Fission gas bubble swelling is
minor compared to that of solid fission product swelling. This suggests that in the pre-transition
regime a considerable concentration of fission gas remains in atomic solution or in small bubbles
not resolvable by SEM.

The mechanistic model presented here considers analytical solutions to coupled rate equations
that describe the nucleation and growth of inter- and intragranular bubbles under the
simultaneous effect of irradiation-induced gas-atom re-solution. The goal of the formulation is to
avoid a coupled set of nonlinear equations that can only be solved numerically, using instead a
simplified, physically reasonable hypothesis that makes the analytical solutions viable. The gas-
induced swelling rate is then assessed by calculating the evolution of the bubble population with
burn-up and subsequently the amounts of gas in bubbles and lattice sites. Uncertain physical
parameters of the model are adjusted by fitting the calculated bubble populations at given burn-
ups with measured bubble size and density data.

Calculations of intergranular bubble size distribution made with this new mechanistic model of
grain boundary bubble formation kinetics is consistent with the measured distributions. The gas-
atom diffusion enhancement factor for grain boundaries was determined to be 7x103 in order to
obtain agreement with the measured distributions. This value of enhancement factor is consistent
with values obtained in the literature. The enhancement factor is about six times higher for as-
fabricated powder plates than for the annealed plates, due to the lower Mo content on the
boundaries. Model predictions are sensitive to various model parameters such gas-atom
diffusivity and re-solution rate. Improved prediction capability requires an accurate
quantification of these critical materials properties and measurement data.




                                            ix
1. Introduction

Addition of 2 wt% or more of silicon to the Al matrix has been demonstrated to be effective in
reducing interaction layer (IL) growth in U-Mo/Al dispersion fuel irradiated in the RERTR-6
(~40 at% U-235) test and the RERTR-7A (~100 at% U-235 LEU equiv.) test (see Fig. 1). At
high burnup, however, large fission gas pores formed within fuel particles. In some cases, the
connection between pores on fuel peripheries appears to have separated the fuel from the matrix.
Because the volume expansion due to IL growth in the Si-modified matrix plates is negligible,
large fission gas pore formation within the fuel is a potential life-limiting factor at very high
burnup such as achieved in the RERTR-7A test.

Three types of bubbles are observed in high burnup U-Mo fuel. The first type is found in the
interior part of a fuel particle (A in Fig.1). These bubbles are small in size, and evenly distributed
throughout the fuel. These are denoted bulk bubbles. The second type of bubble is larger in size
than the bulk bubbles and forms at the contact plane of two neighboring fuel particles (B in
Fig.1). These are termed intersection bubbles. The third type of bubble is located at the fuel
particle periphery (C in Fig.1). These bubbles are relatively large and unevenly distributed. At
high burnup, these bubbles tend to coalesce to form large-scale pores. It appears that there are
threshold burnups for the formation of the second and third type bubble.

In spite of the difference in type, the initial stage of bubble formation is considered similar for all
bubbles. Therefore, characterization of bulk bubbles at the initial stage (burnup less than ~40 at%
U-235) is considered critical for developing a mechanistic model which includes a capability to
assess where and how various type bubbles grow.

Post irradiation U-Mo fuel cross sections show the characteristic bulk bubble morphology for
several burnup levels, as shown in Fig. 2. Fission gas bubbles first appear on linear features,
heterogeneously over the fuel cross section (shown in (a)). The linear features are likely grain
boundaries. There are virtually no bubbles observed in the interior of the grains. As burnup
increases (~40-50 %U-235), the bubble population increases on the grain boundaries and
additional bubbles progressively spread to the interior regions (shown in (b)). At this stage, the
fuel swelling rate increases. The phenomenon underlying this increase in bubble nucleation and
growth is grain refinement or ‘recrystallization’ of the γ U-Mo. Eventually at higher burnup,
bubbles uniformly cover the entire fuel cross section (shown in (c)).

Developing a mechanistic fuel swelling model is important to assess fuel performance and to
assist in interpretation of post irradiation examination (PIE) results. In particular,
characterization of bubbles at the initial stage (burnup less than ~40 at% U-235) is considered
critical for developing a mechanistic model which includes a capability to assess where and how
the bubbles grow as a function of burnup. This is a first step towards the identification of the
factor or the combination of factors that leads to the pore growth at the fuel periphery.

The work presented in this report is thus limited to fission gas bubble formation and fuel
swelling mechanisms to burnups up to ~40 at%U-235 or fission density of 3x1021 f/cm3. The
study at higher burnups involves more complicated phenomena and will be the subject of a
future report.



                                                  1
                                       B
                                                                     C


                                                    A




       50 μm




                 C                              B

Fig. 1 OM (optical microscopy) photos showing microstructure of hot side of
       R2R040 from RERTR-7A. Burnup of this region is 90 at%U-235 (LEU
       equiv.). The gray areas are fuel and bright areas are Al matrix. The black
       spots in fuel are fission gas bubbles. The interaction layers located along
       the intersection of the fuel particles and the aluminum matrix are very thin.



                                         2
                  (a) 35 %U-235 BU (V6018G from RERTR-5)




                 (b) 65 %U-235 BU (V6001M from RERTR-4)




                  (c) 80 %U-235 BU (V6022M from RERTR-4)

Fig. 2 SEM (scanning electron microscopy) photos of irradiated U-Mo fuels from
       RERTR-4 and 5. The samples shown in this figure were fabricated with the
       same batch of atomized fuel particles and irradiated at similar temperatures.




                                        3
2. Characterization of grain and grain boundary

Two kinds of fuel particles were used in the miniplate tests, viz., centrifugally atomized particles
and machined chips made from homogenized cast alloy rods.

2.1 Pre-irradiation grain morphology of atomized U-Mo

The microstructure of the atomized powder consists of a “cellular” solidification structure which
is commonly found in rapidly cooled alloys that have a pronounced solidus-liquidus gap. When
the U-10Mo melt (or U0.78Mo0.22) in the U-Mo phase diagram shown in Fig. 3 is cooled, the melt
follows the right arrow (line A). When it meets the liquidus line, U0.64Mo0.36 solidifies as solid
islands. As the cooling progresses, the solid phase volume increases and simultaneously the Mo
content in the solid phase decreases. In the atomization process, however, the cooling does not
follow this equilibrium process. Instead, once it meets the solidus line, the remaining liquid
phase, which consists of a lower Mo-content than the solid islands, solidifies abruptly leaving an
interconnected network with a lower Mo-content. The boundaries between the cells most likely
form low angle grain boundaries.

The region, when etched, may appear as a thick boundary because of its low Mo-content and
obscures the thinner grain boundaries. We can consider this as effective grain boundaries. In this
report we call these simply ‘grain boundaries.’

Because the swelling rate of U-Mo alloy increases as the Mo content decreases, it is arguable
that the lower Mo-content region near the grain boundaries has a more favorable environment for
bubble nucleation.

A similar process for a lower Mo-content alloy, such as U-7Mo, is shown by the left arrow (B in
Fig. 3). The gap between the solidus and liquidus lines on arrow B is slightly smaller than on
arrow A. Thus, U-7Mo will have slightly smaller solid islands, i.e., smaller grains than U-10Mo.
In addition, the grain boundary Mo content of U-7Mo is lower than that of U-10Mo.

The average cell size, i.e., in our terminology ‘grain size,’ reported by Kim et al [1] is ~2 μm for
an atomized U-10Mo powder. Our measurement using an SEM picture of an as-fabricated
RERTR-3 plate from the memo by Sinkler et al. [2] yielded a grain size of 2.5 μm surrounded by
grain boundaries that lie within a ~0.5-μm thick zone of a nominally lower Mo concentration.

Atomized U-Mo fuel particles typically consist of colonies of the aforementioned small grains
(cells) often of columnar shape enclosed by what appear to be primary γ grain boundaries. In Fig.
4, the grain structure is shown for an extra-ordinarily large particle (~200 μm) recently fabricated
in KAERI [3]. The thicker boundaries are primary grain boundaries grouping colonies of smaller
grains. This sample should have similar general characteristics as U-Mo alloy despite the
addition of 1 wt% Zr. Because of its larger-than-standard size, the grain size is probably larger
than that of the standard size fuel particle used in RERTR tests (~75 μm). The grain size in this
sample particle is in the range of 2 - 12 μm.




                                                 4
                             1400

                                        L                  B         A
                             1300

                             1200

                             1100




            Temperature, C
           o                 1000
                                                                 γ                          γ+δ
                              900

                                        β          β+γ
                              800

                              700                    α+β

                                            γα+γ
                                                                                                  o
                              600             +δ      o                  γ+γ '
                                                                                           580 C
                                                   550 C

                              500
                                        α            α+' +δ
                                                     γ    γ′ '                           γ ' +δ
                                                                       γ′ 2
                                                                     MoU
                              400

                              300
                                    0       5   10    15 20          25 30       35 40     45 50      55
                                                     Mo content (at%)


                                                Fig. 3 U-Mo phase diagram.




Fig. 4 SEM image of a U-7Mo-1Zr alloy particle after metallographic etching [2].
       This fuel particle is larger (~200 μm) than the typical size (~75 μm) used in
       RERTR-3 plates.


                                                                         5
2.2 Homogenization of ‘cored’ microstructure during irradiation

In order to assess what extent the as-solidified ‘cored’ Mo concentration will be eliminated as a
result of fission enhanced diffusion, we use Bleiberg’s analysis of α+γ' to γ phase reversal during
fissioning. Bleiberg [4,5] reported that the α phase lamellae initially spaced by the thin γ' phase
layers in U-Mo alloy fuel disappeared during irradiation to a burnup of ~0.1 at% total U burnup
(LEU equiv. 0.5%U-235 burnup). The average distance between the α lamellae centers was 0.5
μm and their thickness was 0.2 μm. Bleiberg concluded that phase homogenization was sensitive
to the fission rate and the distance between lamella centers.

We derived a model to analyze grain homogenization time, schematically shown in Fig. 5, in an
analogous manner to the Bleiberg model. We assumed Bleiberg’s model is also applicable to our
single-phase case because the Mo concentration difference at the grain boundary and the grain
interior region is substantial. The as-fabricated Mo concentration at the grain interior is estimated
to be 22 at% and that at the grain boundary 17 at% [1,2].

                  CL                   CL



                        GB               Grain




                                                   22
            CMo                                                    5
            (at%)                                              C
                                 17
                                                                   0
                    0        b                     L                   0    b           L/2
                                                                       Distance from GB center
                         Distance from GB center
     (a) Schematic of a grain boundary in slab             (b) Schematic of Mo concentration
           geometry, and Mo concentration                      difference between grain boundary
                                                               and grain interior

       Fig. 5 Model of the initial condition of grain and grain boundary and
              corresponding Mo-concentration. CL=centerline, GB=grain boundary,
              b=half of GB thickness, L=distance between two neighbor grain centers
              (i.e., grain size).

For simplicity, we assume the diffusion coefficient of Mo is constant with respect to Mo
concentration and dependent only on the fission rate, given by D = 112 f r V 5 / 3 where fr is the
fission rate and V is the volume affected by a fission spike (2.01x10-18 cm3), and we also assume
the fission rate is constant throughout irradiation. Then, the diffusion process is governed by
Fick’s equation:
                                     ∂C ( x ,t )    ∂ 2 C ( x ,t )
                                                 =D                                `               (1)
                                       ∂t               ∂x 2
with the boundary and initial conditions,



                                                       6
                                   ∂C
                                         =0        at x = 0 , L / 2 ,
                                   ∂x                                                                     (2)
                                   C ( x ,0 ) = 0       0 ≤ x ≤ b; C ( x ,0 ) = 5  b≤ x≤ L/2
The solution is similar to that obtained by Bleiberg [4] as follows:
                 2 L/2                4 ∞ L/2                   ⎛     x⎞         ⎛  x⎞  ⎛             t ⎞
    C ( x ,t ) =    ∫ C ( x ,0 )dx +      ∑     ∫ C ( x ,0 ) cos⎜ 2nπ ⎟dx cos⎜ 2nπ ⎟ exp⎜ − 4 Dn 2π 2 2 ⎟ (3)
                 L 0                  L n =1 0                  ⎝     L⎠         ⎝ L⎠   ⎝            L ⎠

Expanding the series in Eq.(3) to n=10, we obtained the change in Mo concentration as a
function of time at the grain boundary and grain interior as shown in Fig. 6.

As seen in Fig. 6, the Mo concentration at the grain center and the grain boundary converge with
time. Complete homogenization, however, takes ~2000 days. For the RERTR-3 plates, the
concentration difference between the grain center and the grain boundary is still 2.5 at% at EOL
(or 48 EFPD). For this analysis, we used grain size=3 μm and grain-boundary ‘width’=0.5 μm
(see section 2.1 and Table 1).

                                     23
                                                                 CMo(1.5,t)
                                     22

                                     21




                  Mo concentration
                                                             CMo(0,t)
                                     20

                                     19

                                     18

                                     17       48 d

                                     16
                                          0          100   200           300   400   500
                                                             Time (d)

        Fig. 6 Time-dependent Mo concentration. CMo(1.5,t) is the time-dependent Mo
               concentration at the grain center, C(0,t) is the time-dependent Mo
               concentration at the grain boundary center. Data used for the calculation are:
               fission rate=6x1014 f/cm3-s, D=1.6x10-16 cm2/s, grain size (L)=3 μm, grain
               boundary width (2b)=0.5 μm.

From this analysis, we conclude that, for the given irradiation condition of typical RERTR-3
plates, the grain boundaries remain at a lower Mo-concentration until EOL.




                                                                 7
2.3 Pre-irradiated microstructure of machined U-Mo

Machined powders are heavily cold worked and contain a high concentration of dislocations.
During hot rolling of the fuel plates and subsequent irradiation this dislocation structure will
undergo polygonization. Apparently the final subgrain structure of machined powders is similar
to that of the atomized ones, providing nucleation sites for gas bubbles. Machined powders are
made from well homogenized cast alloy rods, and therefore do not contain the ‘cored’ cellular
structure typical of the rapidly solidified atomized powders.

In addition to as-fabricated fuel powders, two powders one from atomized and the other from
machined powders, were annealed before plate fabrication in the γ-phase to obtain powders with
a homogeneous γ microstructure. Thus, both coring and cold working effects were removed. Fig.
7 shows examples of both types of annealed fuel powders. The microstructures are rather similar
consisting of relatively large grains determined (by X-ray diffraction) as cubic γ U-Mo [3].




                                   5 μm                                                5 μm

           (a) Machined powder (Y02)                      (b) Atomized powder (Z02)

       Fig. 7 OM micrographs of γ-annealed powder plates. Y02 and Z02 are the
              siblings of Y01 and Z03, respectively.




                                                8
2.4 Post irradiation measurement of grain size

To determine the average grain size, we selected three plates from irradiated RERTR-3 plates for
the measurement. They are Z03, V03, and S03. The description of the plates is given in Table 1.
These plates included atomized powders supplied by KAERI. Z03 contains a γ phase annealed
powder. Annealing was performed for 100 hours at 800oC. The grains grew considerably and
only large grains are present in the fuel particles. Z03 and V03 contain U-10Mo whereas S03 has
U-6Mo. As-fabricated U-Mo powders were used in V03 and S03. The grain morphology is
considered to be the same for these plates as discussed earlier in Sect. 2.1. These two plates are
considered typical plates in the RERTR-3 test.

Z03 and Y01
As a result of γ-annealing, there are only large grains in Z03 and Y01 as shown in Figs. 8 and 9,
respectively. These figures show that the cellular or subgrain structure has been eliminated.




                                                              50 μm

                                 (a) Optical microscopy of Z03.




                          (b) SEM of Z03. The scale bar is for 10 μm
       Fig. 8 OM and SEM micrographs of Z03. Z03 fuel powder was γ-phase annealed
              for 100 hours at 800oC before plate-fabrication.

                                                9
                                                              50 μm

                       (a) Optical microscopy of Y01.




                 (b) SEM of Y01. The scale bar is for 5 μm.

Fig. 9 OM and SEM micrographs of Y01. Y01 fuel powder was γ-phase annealed
       for 100 hours at 800oC before plate-fabrication.

                                    10
The bubble morphology observed in the SEM photos of Figs. 8 and 9 is different from other as-
atomized plates such as V03 and S03. The bubbles in Z03 and Y01 are smaller in size as well as
fewer in number than the other plates. This is attributed to differences in the condition in the fuel.

Although bubbles are not visible in the OM photo, comparison between the OM photo and SEM
photo shows that the lines along which bubbles are observed on the OM photo match the grain
boundaries in the SEM photo.

For the machined chips in Y01, the subgrain boundaries have largely disappeared and grain
growth has occurred during the 800oC anneal for 70 hours.

V03

The size and shape of the grains vary within the particles; smaller at the periphery than in the
interior part, and frequently columnar in shape in the periphery whereas equiaxed in the interior.
The grain size measurement from the SEM picture in Fig. 10 (b) is consistent with the
measurement for grains from the as-fabricated plate as discussed in Section 3. As discussed for
Z03, bubbles are not visible in the OM photo. Comparison between the OM photo and SEM
photo shows that the lines in the OM photo are grain boundaries in the SEM photo.

The grain size distribution measured on the OM photo of Fig. 10 (a) for V03 is given in Fig. 11.
Although there are some large grains observed, the predominant size is about 4 μm for this fuel.
                                                      A




                                                                                              C

    B




               D
                                                                             50 μm


                                      Fig. 10 (a) OM of V03.

                                                 11
                                                      Fig. 10 (b) SEM of V03.


                                                           RERTR-3 580W

                                    9000000

                                    8000000




No of grain / cm of fuel particle
                                    7000000

                                    6000000

                                    5000000
3

                                    4000000

                                    3000000

                                    2000000

                                    1000000

                                          0
                                              2.1   4.2   6.3   8.4    10.5   12.6   14.7   16.8   18.9
                                                                Grain size (μm)

                                              Fig. 11 Grain size distribution in V03.




                                                                  12
S03

The same analysis as for V03 was performed. An optical micrograph is shown in Fig. 12. The
grain and bubble morphology of S03 (U-6Mo fuel) is similar to that of V03. This is additional
confirmation that bubble formation first happens on the grain boundaries. The formation of
bubbles invisible with SEM, i.e., smaller than the SEM resolution ~0.02 μm, most likely takes
place within intragranular regions. However, the relatively large bubbles visible in SEM are only
found on the grain boundaries. A recent Belgian TEM study of irradiated U-Mo fuel showed that
intragranular bubbles of ~0.002 μm indeed form homogeneously throughout the fuel matrix [6].




                                       Fig. 12 OM of S03.

From the OM and SEM observations of Z03, V03 and S03, we can conclude that the observed
bubbles with SEM are intergranular.

In table 1, the measured grain sizes are given. The lineal intercept method [7] was used and
checked with the Saltykov method [7]. The lineal intercept method uses several straight lines in
different directions on a cross section of a fuel particle, and the number of intersections with
grain boundaries is counted. The grain size is the average of the values obtained by dividing line
length with the number of intersections for each line.




                                                13
           Table 1. Grain size measurement for RERTR-3 plates

         Fuel                  Z03                 V03                 S03
                            Atomized           Atomized            Atomized
                             U-10Mo             U-10Mo               U-6Mo
                           γ- annealed        as-fabricated       as-fabricated
Size and method          32.4%U-235 BU      37.6%U-235 BU       38.6%U-235 BU
   OM photo (μm)                16                  4                   4
   SEM photo (μm)               19                  3                   3




                                  14
3. Quantitative analysis of intergranular bubbles

3.1 Bubble size and population distribution on grain boundaries

In Table 2 the irradiation conditions for the fuel plates used in the analysis are summarized [8].

                         Table 2. Description of fuel used in the analysis

                                                                   Fission
                                                                               Total    Fuel
                    Plate                   Fuel       Burn up,      rate
         Test                Plate ID                                        duration   Temp
                   AG ID                  property    at% U-235     (1014)    (days)     (oC)
                                                                   f/cm3-s
       RERTR-3      580H      Z03       U-10Mo(a,γ)       32          5.3      48       121
       RERTR-3      580C      Y01       U-10Mo(m,γ)       30          4.8      48       109
       RERTR-1      H-3 *     V002       U-10Mo(a)        39          3.8      94       66
       RERTR-1      H-4 *     A003      U-10Mo(m)         40          3.8      94       68
       RERTR-3      580G      V07        U-10Mo(a)        30          5.1      48       122
       RERTR-3      580W      V03        U-10Mo(a)        38          6.3      48       149
       RERTR-3      580Z      S03        U-6Mo(a)         39          7.0      48       158
       RERTR-5      600Y     A6008H      U-10Mo(a)        49          3.1      116      177
       RERTR-5     600AG     R6007F      U-7Mo(a)         37          2.4      116      185
       RERTR-5      600M     V6019G      U-10Mo(a)        49          2.9      116      142
       RERTR-5      600D     V6018G      U-10Mo(a)        35          2.3      116      121
       RERTR-5     600AH     V8005B      U-10Mo(a)        37          2.4      116      170
       RERTR-5      600V     A8002L     U-10Mo(m)         48          2.9      116      191
                a: atomized, m: machined, γ: annealed at 800oC for 70 -100 hours.
                *: capsule position

Figures 13-25 present the measured bubble size distributions. This information was used for the
calculation of the average bubble diameter shown in Table 3.

All the results provided here are based on the measurements from SEM images of fracture
surfaces. Because the fracture surfaces are not perfectly flat, bubble-containing features are not
perfect lineal intercepts with the underlying grain boundaries. Also readings on SEM pictures
with lower magnifications lead to uncertainties in the measurements. These experimental
limitations may explain some of the variability in the measured bubble size distributions. For
some plates, different SEM pictures were available to obtain better counting statistics. The
uncertainties related to the bubble size measurements are ± 10% , which leads to uncertainties
 ± 20% in the spans between the maximum and minimum bubble sizes. The bubble size
populations for the middle bins are less affected by these uncertainties than those towards both
ends. The errors for the middle bins are ± 10% and for the end bins ± 50% .

The bubble size and number are measured on bubble-containing boundaries. For each SEM
picture, the maximum and minimum bubble sizes were measured. The difference between the
maximum and minimum was divided by seven. Therefore, for each fuel plate, seven size groups
are used to characterize the bubble distribution.



                                                 15
                      0.4




                      0.3




Population fraction
                      0.2




                      0.1




                      0.0
                            0.0                0.1                   0.2               0.3                  0.4
                                                 Average bubble size by group, μm

                              Fig. 13 Bubble size distributions for 580H-Z03 plate from RERTR-3 (γ-annealed).




                                                                16
                      0.4




                      0.3




Population fraction
                      0.2




                      0.1




                      0.0
                            0.0                0.1                   0.2               0.3                 0.4
                                                Average bubble size by group, μm

                              Fig. 14 Bubble size distribution for 580C-Y01 plate from RERTR-3 (γ-annealed).




                                                                17
                      0.4




                      0.3




Population fraction
                      0.2




                      0.1




                      0.0
                            0.0           0.1                   0.2                0.3            0.4
                                           Average bubble size by group, μm

                                  Fig. 15 Bubble size distribution for V002 plate from RERTR-1.




                                                           18
                      0.4




                      0.3




Population fraction
                      0.2




                      0.1




                      0.0
                            0.0           0.1                   0.2                0.3            0.4
                                           Average bubble size by group, μm

                                  Fig. 16 Bubble size distribution for A003 plate from RERTR-1.




                                                           19
                      0.4




                      0.3




Population fraction
                      0.2




                      0.1




                      0.0
                            0.0             0.1                   0.2               0.3               0.4
                                              Average bubble size by group, μm

                                  Fig. 17 Bubble size distribution for 580G-V07 plate from RERTR-3.




                                                             20
                      0.4




                      0.3




Population fraction
                      0.2




                      0.1




                      0.0
                            0.0             0.1                   0.2               0.3               0.4
                                              Average bubble size by group, μm

                                  Fig. 18 Bubble size distribution for 580W-V03 plate from RERTR-3.




                                                             21
                      0.4




                      0.3




Population fraction
                      0.2




                      0.1




                      0.0
                            0.0             0.1                   0.2                0.3              0.4
                                             Average bubble size by group, μm

                                  Fig. 19 Bubble size distribution for 580Z-S03 plate from RERTR-3.




                                                             22
                      0.4




                      0.3




Population fraction
                      0.2




                      0.1




                      0.0
                            0.0               0.1                  0.2               0.3                0.4
                                               Average bubble size by group, μm

                                  Fig. 20 Bubble size distribution for 600Y-A6008H plate from RERTR-5




                                                              23
                      0.4




                      0.3




Population fraction
                      0.2




                      0.1




                      0.0
                            0.0                0.1                  0.2               0.3                 0.4
                                                Average bubble size by group, μm

                                  Fig. 21 Bubble size distribution for 600AG-R6007F plate from RERTR-5.




                                                               24
                      0.4




                      0.3




Population fraction
                      0.2




                      0.1




                      0.0
                            0.0               0.1                   0.2              0.3                 0.4
                                                Average bubble size by group, μm

                                  Fig. 22 Bubble size distribution for 600M-V6019G plate from RERTR-5.




                                                               25
                      0.4




                      0.3




Population fraction
                      0.2




                      0.1




                      0.0
                            0.0               0.1                   0.2               0.3                0.4
                                               Average bubble size by group, μm

                                  Fig. 23 Bubble size distribution for 600D-V6018G plate from RERTR-5.




                                                               26
                      0.4




                      0.3




Population fraction
                      0.2




                      0.1




                      0.0
                            0.0                0.1                  0.2               0.3                 0.4
                                                Average bubble size by group, μm

                                  Fig. 24 Bubble size distribution for 600AH-V8005B plate from RERTR-5.




                                                               27
                      0.4




                      0.3




Population fraction
                      0.2




                      0.1




                      0.0
                            0.0               0.1                   0.2               0.3                0.4
                                                Average bubble size by group, μm

                                  Fig. 25 Bubble size distribution for 600V-A8002L plate from RERTR-5.




                                                               28
                                             Table 3. Average bubble sizes from measurements

                               Plate ID                     Partial                    Average bubble diameter
                                                       recrystallization               from measurements, μm
                              Z03                             No                                0.09
                              Y01                             No                                0.09
                              V002                            No                                0.15
                              A003                            No                                0.18
                              V07                             No                                0.13
                              V03                             No                                0.16
                              S03                            Yes                                0.18
                             A6008H                          Yes                                0.17
                             R6007F                           No                                0.16
                             V6019G                           No                                0.16
                             V6018G                           No                                0.14
                             V8005B                           No                                0.16
                             A8002L                          Yes                                0.18

In Fig. 26 the average bubble sizes for the plates used in the analysis are shown. Although there
are considerable errors, after an initial incubation period the average bubble size increases with
fission density and shows saturation at high fission density. As indicated in Table 3, some plates
showed the initial stage of recrystallization with signs of multi-layer bubble formation on the
grain boundaries. For these plates, the measurement were made on grains not yet affected by
recrystallization.

                                                             Z 0 3, 12 1 o C -4 8 d      A 6 0 08 H , 1 77 o C -1 16 d
                                                                         o
                                                             Y 0 1, 10 9 C -4 8 d        R 60 07 F , 18 5 o C -1 16 d
                                                                         o
                                                             V 00 2 , 6 6 C -9 4d        V 6 0 19 G , 14 2 o C -1 1 6d
                                             0.25
                                                                         o
                                                             A 00 3 , 6 8 C -9 4d        V 6 0 18 G , 12 1 o C -1 1 6d
                                                             V 07 , 1 2 2 o C -4 8d      V 8 0 05 B , 1 70 o C -11 6 d
                                                             V 03 , 1 4 9 o C -4 8d      A 8 0 02 L, 19 1 o C -1 1 6d
                                             0.20                        o
                                                             S 03 , 1 5 8 C -4 8d




                   Average bubble size, μm
                                             0.15



                                             0.10



                                             0.05
                                                                                        Estimated trend


                                             0.00
                                                 0.0   0.5         1.0           1.5    2.0        2.5          3 .0     3 .5
                                                                  F issio n de nsity, 1 0 21 f/cm 3
                          Fig. 26 Measured average bubble size vs. fission density.


                                                                                 29
3.2 Bubble density analysis

3.2.1 Bubble density per unit grain-boundary length

The bubble populations on grain boundaries were measured on SEM photomicrographs of
fractured fuel cross sections as shown in Figs. 8-10. The center-to-center distances between
neighboring bubbles were measured. The reciprocal of the average value of the measured
distances is equal to the number density per unit grain boundary length, i.e.,

                                               n
                                    ρL =                                                         (4)
                                           ∑λ
                                           n
                                                   n


where λ are the distances between bubbles and n is the number of bubbles included in the
measurements. The measurement data are given in Table 4.

Some plates with fission densities at or greater than 3x1021 f/cm3 showed the sign of
recrystallization. Typically, the appearance of the initial stage of recrystallization is manifested
by the formation of multi-layered bubbles on the grain boundaries. For these plates, only grain
boundaries with single-layer bubbles were counted in order to catch the bubble characteristics of
the pre-recrystallized stage. However, this measurement technique inevitably results in
underestimates for bubble volume fractions as compared to those obtained from direct
measurement by the point counting method. This will be discussed later in Subsection 3.2.4 and
a comparison will be given in Table 8.

                Table 4. Measured number of bubbles per grain boundary length

                                                            Measured density
                                         Partial             per unit grain
                        Plate ID
                                    recrystallization       boundary length,
                                                              ρL, 104 cm-1
                        Z03                No                     1.96
                        Y01                No                     1.79
                        V002               No                     1.30
                        A003               No                     1.41
                        V07                No                     1.34
                        V03                No                     1.36
                        S03                Yes                    1.18
                       A6008H              Yes                    1.43
                       R6007F              No                     1.39
                       V6019G              No                     1.36
                       V6018G              No                     1.32
                       V8005B              No                     1.37
                       A8002L              Yes                    1.35




                                                       30
In Fig. 27, the measured bubble number densities per unit length of grain boundary for all plates
are shown. The bubble number densities show no explicit dependence upon fission density. The
gamma-annealed powder plates show generally larger values than the as-fabricated powder
plates. The machined powder plates also tend to show slightly greater values than the atomized
powder plates. The effect of Mo content from this result seems to be negligible considering the
measurement error, except perhaps for the lowest Mo content (i.e., 6Mo) of which only a single
sample was available.




                Number of bubbles per unit grain boundary length
                                                                   3.0
                                                                              U-10Mo (annealed)
                                                                              U-10Mo (atomized)
                                                                              U-10Mo (machined)
                                                                   2.5        U-7Mo (atomized)
                                                                              U-6Mo (atomized)




                                  4
                                                                   2.0




                               (10 bubbles/cm)
                                                                   1.5




                                                                   1.0
                                                                         0          1               2                 3            4
                                                                                        Fission density (1021 cm-3)
                                                                   Fig. 27 Number of bubbles per unit length vs. fission density


3.2.2 Bubble density per unit fuel cross section area

Grain size was measured for all plates in the analysis. As discussed in Sect. 2.3, the grain
boundaries were discernable because they contain gas bubbles. Two methods were used. The
first method is to measure the grain size directly in four different directions of a grain and then
calculate the average size by using measurements for several grains from the plate. The second
method is the lineal intercept method described in Sect. 2.3. This method is preferable to the
direct measurement method. For some plates, no picture was available with good magnification
including at least 5 entire grains. In addition, for other plates, the shape of grains was columnar.
For this case only one method was used.

It must be mentioned that all grain size measurements were made on SEM images and only a
limited number of them were available. Therefore, for some plates, good statistical results could
not be obtained because the measurements inevitably included abnormally large or small grains,
which could artificially skew the average value. However, bubble measurements were made on
these SEM micrographs in order to be consistent for all measurements.


                                                                                            31
Table 5 gives the summary of the measured grain sizes for the plates used in the analysis. This
information is used to obtain number density per unit fuel cross section area and subsequently
number density per unit fuel volume.


                                Table 5. Grain size measurement

                  Plate ID       Direct measurement        Lineal method
                            Grain size,      Standard      Grain size, μm
                                μm         deviation, μm
                   Z03          24.4            9.3            23.6 **
                  Y01           NM             NM               10.1 *
                  V002           6.3            0.9              4.9
                  A003          NM              NM               3.2
                  V07           NM              NM               6.5
                  V03           NM              NM               7.3
                   S03          4.4             NM               3.6
                A6008H           5.3            1.3
                R6007F          NM              NM               6.2
                V6019G           8.5            3.6              7.6
                V6018G           4.9             2               5.2
                V8005B           8.1            4.5              NM
                A8002L           3.9            1.3              NM
           * Machined and annealed, ** Atomized and annealed, NM=Not measured


In order to obtain the bubble volume fraction, the bubble area fraction measured on the fuel cross
section is needed. Because bubbles are homogeneously distributed, the bubble volume fraction is
equal to the bubble area fraction measured on the cross section [7]. However, our SEM
micrographs were taken on fuel fracture surfaces. In the modeling described below, we can
convert the bubble density per unit length of grain boundaries to the bubble density per unit cross
section area. The bubble area fraction can be obtained by using the average bubble size and
bubble density per unit cross section area.

In our model, a grain is modeled as a tetrakaidecahedron (TKDH) [7]. The projection through the
center of the TKDH yields a plane as shown in Fig. 28. There are two different kinds of sides
with length l and 2 l. The total length of the perimeter (P) and area (S) are:
                                    P = 4(1+ 2 )l                                             (5)
                                                  2
                                            S =7l                                             (6)
The bubble number density per unit area on this projected plane from the measured number
density per unit length, ρcs , can be obtained by
                                            1P
                                     ρ CS =    ρL                                             (7)
                                            2S



                                                32
where ρ L is the measured bubble density per unit length given in Table 4. The factor ½ in front
of the equation takes into account that every side of TKDH is shared by a neighboring grain.



                                                                          2l




                                                                                l



                          2 2l
                                        2l                                2l

                                                         l

                                                10 l
                  Fig. 28 Tetrakaidecahedron (TKDH) modeling of grain cross section.


Substituting Eqs. (5) and (6) in Eq.(7) gives
                                            2 ⋅ (1 + 2 )
                                     ρ CS =              ρL                                        (8)
                                                 7⋅l
The diagonal length varies between 2 2 l and 10 l, as shown in Fig. 28. Taking the average of
this and setting the grain size equal to the diagonal length, we obtain d=3l where d is the grain
size. Therefore, Eq. (8) becomes
                                            6 ⋅ (1 + 2 )
                                     ρ CS =              ρL                                        (9)
                                                 7⋅d
The data for the bubble density per unit grain boundary length are given in Fig. 27. Using Eq. (9),
the calculated density data per unit fuel cross section area for all plates are presented in Table 6
and plotted in Fig. 29.

Using Eq. (9), we obtain the grain boundary length per unit fuel cross section area, L*.
                                       ρ     6 ⋅ (1 + 2 )
                                  L* = CS =                                                 (10)
                                       ρL         7⋅d
Figure 30 shows the results for L*. The symbols are the measured values and the line is the
calculated by using the TKDH model. Good agreement between the measured and calculated
shows that the application of the TDKH model is valid.



                                                 33
Table 6. Number of bubbles per unit fuel cross section area converted from the
       measured bubble number per unit grain boundary length data

                                                                                                 Measured            Calculated
                                                                             Partial          density per unit     density per unit
                               Plate ID                                 recrystallization     grain boundary      fuel cross section
                                                                                                  length,                area,
                                                                                               ρ L , 104 cm-1       ρcs , 108 cm-2
                               Z03                                            No                     1.96               0.17
                               Y01                                            No                     1.79               0.36
                               V002                                           No                     1.30               0.55
                               A003                                           No                     1.41               0.92
                               V07                                            No                     1.34               0.43
                               V03                                            No                     1.36               0.39
                               S03                                            Yes                    1.18               0.67
                              A6008H                                          Yes                    1.43               0.56
                              R6007F                                          No                     1.39               0.46
                              V6019G                                          No                     1.36               0.37
                              V6018G                                          No                     1.32               0.53
                              V8005B                                          No                     1.37               0.35
                              A8002L                                          Yes                    1.35               0.72




     Bubble number density per unit fuel cross section area
                                                              1.2
                                                                             U-10Mo (annealed)
                                                                             U-10Mo (atomized)
                                                              1.0
                                                                             U-10Mo (machined)
                                                                             U-7Mo (atomized)
                                                                             U-6Mo (atomized)
                                                              0.8




                         8             2
                                                              0.6




                     (10 bubbles/cm )
                                                              0.4


                                                              0.2


                                                              0.0
                                                                    0                1                  2                 3            4

                                                                                            Fission density (1021 cm-3)
        Fig. 29 Number of bubbles per unit fuel cross section area calculated from ρL.


                                                                                               34
                                                         1.0




              Grain boundary length
                                                                                            mesured value
                                                         0.8                                calculated value




                                                         0.6




              per unit fuel cross section area, μm/μm2
                                                         0.4




                                                         0.2




                                                         0.0
                                                               0   5   10          15         20               25

                                                                       Grain size, μm


  Fig. 30 Comparison between the measured and calculated grain boundary length per unit fuel
                              cross section area vs. grain size.


3.2.3 Bubble density per unit grain surface area
We assume that the bubbles on the grain surfaces of a TKDH are uniformly distributed. Thus, we
model the distribution as a close-packed array as shown in Fig. 31. Each bubble occupies an
equal amount of the circular surface area with diameter D with the border line depicted by the
dashed line. As can be seen, there is some non-occupied area; we call this ‘empty area.’ In this
model, the distance between two neighboring bubbles from center to center is also D.




                              Empty area                                                    Gas bubble


                      Occupied area
                      circle by a bubble                                                D

   Fig. 31 Schematic of the model used for bubble distribution analysis on the grain surface.


                                                                        35
In this model, the bubble density per unit surface area is the reciprocal of the specific area for a
bubble. The specific area consists of the area of the circle with diameter D, and the sum of two
empty areas shown in Fig. 31. The area of a circle (Sc) is
                                                π ⋅ D2
                                           Sc =                                                   (11)
                                                   4
The area of an empty area (Se) is
                                                (2 ⋅ 3 − π) D 2
                                           Se =             ⋅                                     (12)
                                                      2       4
Thus, the area of a bubble (Sb) is
                                                  3 2        3 1
                                           Sb =      ⋅D =                                         (13)
                                                 2          2 ρ 'L 2
where ρ L′ is the average bubble density per unit grain boundary length measured on the grain
surface. This quantity is usually different from that measured on the grain boundaries. This will
be discussed later in this Section.

Therefore, the density per unit grain surface area is
                                                1     2
                                           ρS = =        ρ 'L 2                                  (14)
                                                Sb     3

The relationship between ρ L′ and ρ L needs to be known in order to use Eq. (14) because ρL are
the known data from the measurements, which are given in Table 4. We model the bubbles on
the grain surface as distributed in a close-packed plane, as shown in Fig. 32. The average
distance between two bubbles on the grain boundaries exposed on the cross section is usually
larger than that measured on the real grain surface (see Fig. 32) because the cross section is not
necessarily made on the close-packed line (solid line in Fig. 32). The solid line in Fig. 32 shows
the close-packed line of bubbles, whereas the broken lines show the possible grain boundaries on
a cross section having greater distances between bubbles than those on the solid line. As a result,
the measured bubble number density per unit grain boundary length measured on a cross section
is less than that measured on a real grain surface.




             Bubble                                                 Grain boundary
                                                                    without close packed
                                                                    bubbles

      Grain boundary
      with close packed
      bubbles


      Fig. 32 Schematic of possible grain boundary bubble configurations on cross section.

                                                  36
In addition, as can be seen in the SEM photos in Figs. 8 - 10, the grain boundaries are rarely
straight lines. There are many turns visible on the grain boundaries, suggesting that the grain
boundaries are composed of many combinations of possible distances between two bubbles as
shown in Fig. 32. Therefore the distance between two bubbles is a statistical average considering
all possible combinations of bubble configuration. Thus, a model to modify the measured values
of bubble number density per unit grain boundary length on a cross section for real values is
necessary.

In Fig. 33, let the center-to-center distance between O and B1, that between O and B2, and that
between O and B3 be d1, d2, and d3, respectively. The probability that a cross section is cut
through two bubbles on one of these three cases is inversely proportional to the square of the
distances between two bubbles. Thus, considering the three most probable cases that can be
exposed on a cross section surface; O and B1, O and B2, and O and B3, the average surface-to-
surface distance between two bubbles on a cross section can be expressed as
                                 A        A       A
                            δ = 2 ⋅ δ1 + 2 ⋅ δ 2 + 2 ⋅ δ 3                                     (15)
                                 d1       d2      d3
where A d12 , A d 22 , and A d 32 are the probabilities that the cross section is cut through O and B1,
O and B2, and O and B3, respectively, where A is an arbitrary constant and δ1, δ2, and δ3 are the
surface-to-surface distances between O and B1, O and B2, and O and B3, respectively.




                                                 O

                                                                  R2
                                                   R11
                                                   B                   B2



                                                                    R3      B3




   Fig. 33 Schematic showing the method to determine the average distance between bubbles.

                                                 37
It can be shown that d1=D, d 2 = 3 D , and d 3 = 7 D where D is the distance between the
centers of two nearest bubbles shown in Fig. 32. Then, Eq. (15) becomes
                                         A        1      1
                                  δ = 2 ⋅ (δ1 + δ 2 + δ 3 )                              (16)
                                        D         3      7
Since the sum of probabilities of all three cases is unity, i.e.,
                                   A A A
                                       +    +    =1                                      (17)
                                   d12 d 22 d 32
we have
                                           D2
                                  A=                                                     (18)
                                           1 1
                                        1+ +
                                            3 7

Substituting Eq. (18) in Eq. (16) gives
                                       1               1       1
                           δ =                ⋅ (δ1 + δ 2 + δ 3 )                                       (19)
                                      1 1              3       7
                                  1+ +
                                      3 7
Using δ1=D-x0, δ 2 = 3 D -x0, δ 3 = 7 D -x0 where x0 is the average bubble size, we can
rearrange Eq.(19) as
                                          1      1
                                  (1 +       +      )
                           δ =             3      7   ⋅ D − x0                                          (20)
                                           1 1
                                     1+ +
                                           3 7
Since, by definition, ρ L = 1 / (δ + x o ) and ρ'L=1/D, δ = 1 / ρ L − x 0 and D = 1 / ρ L′ . Substitution of
these equalities in Eq. (20) gives
                                                     1      1
                                             (1 +        +     )
                                      ρ L′ =          3      7   ρL                                     (21)
                                                      1 1
                                                 1+ +
                                                      3 7
The term in front of ρL in Eq. (21) has a value of 1.32, meaning that the measured values are
about 32% lower than the real values.

By using Eqs. (14) and (21), the density per unit grain surface area can be calculated from the
measured ρ L given in Table 4. The results are provided in Table 7 and shown in Fig. 34.
Because ρ L is independent on fission density, ρ s , which is a is a function of only ρ L , is also
independent on fission density.




                                                    38
                                                         Table 7. Calculated and measured number of bubbles per unit grain
                                                                                 surface area ( ρ S )
                                                                        Calculated,         Measured,        Measured /
                                                                            8   -2               8    -2
                                                         Plate ID         10 cm               10 cm          calculated
                                                           Z03             13.6                 NM               NA
                                                           Y01             11.3                 NM               NA
                                                           V002             6.0                 NM               NA
                                                           A003             7.0                 NM               NA
                                                           V07              6.4                 NM                N
                                                           V03              6.5                 NM               NA
                                                           S03              5.0                  4.6            0.93
                                                         A6008H             7.3                  4.9            0.67
                                                          R6007F            6.1                  7.2             1.2
                                                         V6019G             6.5                 NM               NA
                                                         V6018G             6.1                  5.9            0.97
                                                         V8005B             6.6                 NM               NA
                                                         A8002L             6.4                 NM               NA
                                                                     NM = Not measured, NA = Not available




Bubble number density per unit grain surface area
                                                    18
                                                                  U-10Mo (annealed)
                                                    16            U-10Mo (atomized)
                                                                  U-10Mo (machined)
                                                                  U-7Mo (atomized)
                                                    14            U-6Mo (atomized)

                                                    12



                 8             2
                                                    10




              (10 bubbles/cm )
                                                    8

                                                    6

                                                    4
                                                         0                 1                 2                 3             4
                                                                                Fission density (1021 cm-3)

                                Fig. 34 Number of bubbles per unit grain boundary surface area vs. fission density

                                                                                        39
We also directly measured the bubble density on some exposed grain surfaces (see Fig. 35) for
several plates. The results are also included in Table 7. The comparison between the measured
and the calculated show good agreement.




  Fig. 35 SEM photo of A6008H (600Y) from RERTR-5 showing an example of surface area
           bubbles. The red marker is for the area the bubble density was measured.


3.2.4 Bubble density per unit fuel volume
The bubble density per unit fuel volume can be obtained by considering the surface-to-volume
ratio of the TDKH. The volume of a TDKH is
                                  VTDKH = 8 ⋅ 2 ⋅ l03                                       (22)
where l0 is the edge length and approximately equal to (1/3)d where d is the average size of the
TDKH.

The surface area of the TDKH is
                               STDKH = 6 ⋅ (1 + 2 3 ) ⋅ l0 2                              (23)
By using Eqs. (22) and (23) we obtain a relation between the cross section surface and volume
density:
                                     1 S
                               ρ V = ⋅ TDKH ρ S                                           (24)
                                     2 VTDKH


                                              40
or
                                                                          9(1 + 2 3 )
                                                                   ρV =                 ρS                                 (25)
                                          8 2 ⋅d
where ρS is the bubble density per unit grain surface area given by Eq. (14).

The bubble density per unit fuel volume is calculated using Eqs. (14) and (25), and is shown in
Fig. 36 and given in Table 8. Figure 36 shows that, although not obvious, the lower Mo-content
plates show higher bubble volume fractions. This means that the lower Mo-content plates show
higher fuel swelling. This observation is subject to the theoretical modeling described in Section
4.

                                                    10
                                                                U-10Mo (annealed)




            Bubble number density per unit volume
                                                                U-10Mo (atomized)
                                                     8          U-10Mo (machined)
                                                                U-7Mo (atomized)
                                                                U-6Mo (atomized)
                                                     6



                        12            3




                     (10 bubbles/cm )
                                                     4



                                                     2



                                                     0
                                                         0            1                 2                    3    4
                                                                                                 21     -3
                                                                           Fission density (10        cm )


                                                    Fig. 36 Number of bubbles per unit fuel volume calculated from ρ S .


3.3 Gas bubble volume fraction and fission gas swelling

The total gas bubble (i.e., observable bubble) volume fraction in fuel can be calculated as
follows:
                                        π ⋅ xo 3
                                   vb =          ρV                                                                        (26)
                                           6
where vb is the gas bubble volume fraction in the fuel.

Bubble volume fraction, vb , can also be given by



                                                                                  41
                                           π ⋅ xo 2
                                    vb =       ρ CS                                            (27)
                                           4
where ρ CS is the bubble density per unit fuel cross section area from Table 6 and x0 is the
average bubble size from Table 3. In Eq. (27), the fact that the bubble volume fraction is equal to
the bubble area fraction is used [7]. The gas bubble volume fractions are calculated using ρ S and
ρ CS from Eqs. (26) and (27), and are given in Table 8.

                                 Table 8. Gas bubble volume fractions

                     Fission                       ρV         vb              vb           vb
     Plate ID        density,       Partial    calculated calculated      calculated    measured
                                   Recrystall- from ρ ,    from ρS,       from ρCS,        *
                                                       S
                    1021 f/cm3      ization     1012 cm-3                                  %
                                                              %               %
   Z03 (a-γ)           2.2            No           2.0        0.1             0.1         0.2
   Y01 (m-γ)           2.0            No           4.0        0.2             0.2         NM
   V002 (a)            3.1            No           4.3        0.8             1.0         1.2
   A003 (m)            3.1            No           7.8        2.4             2.3         2.7
   V07 (a)             2.1            No           2.5        0.8             0.6         NM
   V03 (a)             2.6            No           3.5        0.4             0.8         NM
   S03 (a)             2.9            Yes          3.2        0.7             1.7         2.0
   A6008H (m)          3.1            Yes          4.9        1.5             1.3         NM
   R6007F (a)          2.4            No           4.9        1.3             0.9         1.6
   V6019G (a)          3.0            No           3.5        0.7             0.7         2.0
   V6018G (a)          2.3            No           3.0        0.7             0.8         NM
   V8005B (a)          2.4            No           4.2        0.6             0.7         NM
   A8002L (m)          3.0            Yes          2.9        0.6             1.8         3.2

       a: atomized powder, m: machined powder, γ: γ-phase annealed powder,
       * Measured by point counting, NM = Not measured

The direct volume analysis method, i.e., the point counting method, was used to obtain the
bubble volume fractions for several plates. The point counting method converts the area fraction
occupied by the bubbles on a SEM photo to the gas bubble volume fraction. This verification
method allows a direct measurement of the volume fraction from the area fraction occupied by
bubbles on the cross section. The results calculated from ρ CS show better consistency than those
from ρ S when compared with the point counting results.

In general, all three methods are fairly consistent with some exceptions. The plates with
inconsistent results are all from the partially recrystallized plates. The values from ρ CS are larger
than those from ρ S , and are more consistent with the direct measurement values. The values
from the direct measurement are the largest of all. All of these observations point toward the
argument that the inconsistencies originated from the measurement of ρ L that excluded the

                                                      42
partially recrystallized regions on the fuel cross sections, whereas the calculated values from ρ CS
and the direct measurements included those regions that have more populated bubbles, as
discussed in Subsection 3.2.1.

The machined plates have consistent results for all three methods. The machined powders have
more equiaxial shaped grains and a more homogeneous distribution of grains than the atomized
powder fuel because there is no thermal process involved during fabrication. This allows for a
more accurate grain size measurement. In atomized particles, however, the grains are typically in
columnar shapes at the particle periphery, and more isotropic in shape at the particle interior and
larger in size than those at the periphery. Because we use high magnification SEM photos, the
measurements are frequently localized and dependent on the fracture direction resulting in errors
in grain size measurements.

The calculated results for gas bubble volume fraction using the bubble density per unit cross
section area are shown in Fig. 37. The bubble volume fraction, which is equal to fission gas
bubble swelling, is a function of fission density. The lower Mo-content fuel plates show slightly
higher bubble volume fractions. This also suggests fuel swelling is dependent on the Mo content,
although an exact quantification is not available for the present work.

                                                               Burnup (at%U-235 for U-10Mo)
                                                  0   10        20      30        40      50        60    70
                                              4
                                                        U-10Mo (m)




             Gas bubble volume fraction (%)
                                                        U-10Mo (a)
                                              3         U-7Mo (a)
                                                        U-6Mo (a)
                                                        U-10Mo (annealed)

                                              2



                                              1



                                              0
                                                  0        1           2           3            4         5
                                                                Fission density (1021 f/cm3)

                                              Fig. 37 Gas bubble volume fraction calculated from ρ CS .

The fuel swelling data based on plate thickness measurements before-and-after the irradiation
tests are shown in Fig. 38 [9]. A linear fit gives total fuel swelling (%) as

                                                                             43
                                  ⎛ ΔV ⎞
                                  ⎜⎜    ⎟⎟      = 6 × 10 −21 Fd                                (28)
                                   ⎝ V0 ⎠ total
The solid fission product swelling and intragranular fission gas bubble contribution to swelling is
the difference between the total swelling and the measured gas bubble swelling.

Fission gas bubble swelling was obtained by using the gas bubble volume fraction data shown in
Fig. 37. Modification to reflect the initial fuel volume by multiplying by (1+(ΔV/V0)s) was made
where (ΔV/V0)s is the fuel matrix swelling obtained by subtracting the gas bubble swelling from
the total swelling. The result is shown in Fig. 38. The plate thickness data of monolithic fuel
plates and dispersion fuel plates with Si-modified matrixes, for which the thickness increase is
due to fuel swelling, are used to obtain the total swelling.

                                      % U-235 BU (LEU Equiv. for U-10Mo)

                      0          10             20                 30      40
                 30
                          Total swelling from thickness change
                             RERTR-6 (dispersion: matrix with 2wt%<Si)
                 25
                             RERTR-6 (monolithic)
                             RERTR-7 (monolithic)
                 20       Grain boundary bubble contribution



    ΔV/ V0 (%)
                               Gas bubble swelling
                 15


                 10


                  5


                  0
                      0                 1                      2                3

                                         Fission density (1021 f/cm3)

          Fig. 38 Comparison of total fuel swelling assessed from plate thickness changes and
                         contribution by intergranular gas bubble swelling.

Figure 38 shows that the contribution to the total swelling by fission gas bubbles is very small.
This suggests that in the pre-transition regime a considerable concentration of fission gas
remains in atomic solution or in small bubbles not resolvable by SEM.




                                                       44
4. Mechanistic model development

4.1 Calculation of evolution of average intra and intergranular bubble-size and density

The model presented here considers analytical solutions to coupled rate equations that describe
the nucleation and growth of inter- and intragranular bubbles under the simultaneous effect of
irradiation-induced gas-atom re-solution. The goal of the formulation is to avoid a coupled set of
nonlinear equations that can only be solved numerically, using instead a simplified, physically
reasonable hypothesis that makes the analytical solutions viable. The gas-induced swelling rate
is then assessed by calculating the evolution of the bubble population with burn-up and
subsequently the amounts of gas in bubbles and lattice sites. Uncertain physical parameters of the
model are adjusted by fitting the calculated bubble populations at given burn-ups with measured
bubble size and density data.


At the irradiation temperatures of interest (T < 500K), the diffusion of fission gas atoms is
                                                          •
athermal and proportional to the fission rate, f (fissions·cm-3·s-1), and the gas-atom diffusion
coefficient, Dg , is given by
                                            •
                               Dg = D0 f                                                                                   (29)

In general, the gas-atom re-solution rate is also proportional to the fission rate, i.e.,

                                       •
                              b = b0 f                                                                                     (30)

Within the content of mean field theory, the rate equation describing the time evolution of the
density of gas in intragranular bubbles is given by

                    d [mb (t )cb (t )]
                                       = 16πf n D g rg c g (t )c g (t ) + 4πrb (t )D g c g (t )cb (t ) − bmb (t )cb (t )   (31)
                          dt

The three terms on the right hand side of Eq. (31) represent, respectively, the change in the
density of gas in intragranular bubbles due to bubble nucleation, the gas-atom diffusion to
bubbles of radius, rb , and the loss of gas atoms from bubbles due to irradiation induced re-
solution. Equation (31) can also be represented as the sum of two equations denoting,
respectively, the time evolution of the fission gas bubble density c b and of the gas content in
bubbles, mb , as follows

                    dc b (t ) 16πf n D g rg c g (t )c g (t ) b
                             =                              − c b (t )                                                     (32)
                      dt               m b (t )              2



                                                              45
                   dnb                           b
                       = 4πrb (t ) D g c g (t ) − mb (t )                                       (33)
                    dt                           2

In Eq. (33) f n is the bubble nucleation factor, and c g and rg are the gas atom concentration and
radius, respectively. In general, the value of f n is less than one reflecting the premise that gas-
bubble nucleation within the fuel matrix requires the presence of vacancies/vacancy clusters in
order to become viable. The value of f n is estimated based on the hypothesis that gas-atom
diffusion occurs by a vacancy mechanism and that a 2 gas atom cluster is a stable nucleus. In this
case f n is approximately the bulk vacancy concentration (i.e., ≈ 10-4).


The 1st term on the right hand side (rhs) of Eq. (33) can be interpreted to represent the generation
rate of "average" size bubbles of radius rb . For every 2 atom bubble that is nucleated, 2 / mb of a
bubble of radius rb appears. In other words, nucleation of mb two-atom clusters leads to the gain
of one bubble of radius rb . This "average size" bubble is in the peak region of the bubble-size
distribution.


Both "whole" bubble destruction and gas-atom "chipping" from bubbles are included (last terms
on right-hand side) in Eq. (32) and (33) in order to capture the behaviour of an average size
bubble (that characterizes the full bubble-size distribution). Within the full bubble-size
distribution there are bubbles that are destroyed by one fission fragment collision (e.g. bubbles
smaller than a critical size) and others that are only partially damaged (e.g. bubbles larger than a
critical size). Including b in both Eq. (32) and (33) is an attempt to depict these processes using a
simplified formulation that enables an analytical solution for swelling. If bcb / 2 was not included
in Eq. (32), then the density of bubbles could never decrease due to irradiation. Likewise if
bmb / 2 was not included in Eq. (33), the number of atoms in a bubble could never decrease.
However, the equal partition of gas-atom re-solution between these two mechanisms, as implied
from the use of same re-solution parameter b in Eqs. (32) and (33) is an assumption that remains
to be tested experimentally.


Due to the strong effect of irradiation-induced gas-atom re-solution, in the absence of geometric
contact, the bubbles stay in the nanometer size range. The density of bubbles increases rapidly
early in the irradiation. Subsequently, at longer times, the increase in bubble concentration occurs
at a much-reduced rate. Based on the above considerations, the left-hand side of Eq. (32) is set
equal to zero. This approximation will be more reasonable for larger values of t . A solution for
cb in terms of mb and c g is then given by

                          16πf n rg D0cg2
                   cb =                                                                         (34)
                             b0 mb (t )



                                                     46
The quantities c g , cb and m b in Eqs (31-34) represent average values. For example, cb (t ) bubbles
each containing mb (t ) gas atoms represents the average value of the bubble size distribution at
time t. In general, rb is related to mb through the gas law and the capillarity relation. Using a
modified Van der Waals gas law,
                   2γ ⎛ 4 3            ⎞
                      ⎜ πrb − hs bv mb ⎟ = mb kT                                                 (35)
                   rb ⎝ 3              ⎠

where γ is the surface tension, bv is the van der Waals constant for Xe, k is Boltzmann’s
constant, T is the absolute temperature, and hs is a fitting parameter that for a given T makes Eq.
(35) equivalent to the hard-sphere equation of state [10].


For bubbles in the nanometer size range an approximate solution to Eq. (35) is given by
                                                 1/ 3
                             ⎛ 3h b m (t ) ⎞
                   rb (t ) = ⎜ s v b ⎟                                                           (36)
                             ⎝     4π      ⎠

Using Eq. (36) and an argument similar to that used to derive Eq. (34), the steady-state solution
to Eq. (33) is given by

                                               ⎛ 4πD0 c g (t ) ⎞
                                        1/ 2                        3/ 2
                             ⎛ 3h b ⎞
                   mb (t ) = ⎜ s v ⎟           ⎜⎜              ⎟⎟                                (37)
                             ⎝ 4π ⎠             ⎝   b0          ⎠

According to Speight [11], the fraction of gas f s that diffuses to the grain boundary of grains of
diameter d g can be approximated by

                    fs =
                           8
                              (Dg t )1/ 2 − 62 Dg t
                           dg              dg
                                                                                                 (38)

Imposing gas-atom conservation, i.e., requiring that the sum of the gas in solution, in
intragranular bubbles, and on the grain boundary is equal to the amount of gas generated, the
term c g (t ) is determined as
                                                                                       1/ 2
                                             ⎡                            •
                                                                                   ⎤
                              − (1 + f s ) + ⎢(1 + f s ) + 64 π f n rg Dg f β t / b⎥
                                                        2


                   c g (t ) =                ⎣                                     ⎦
                                                  32 π f n rg Dg / b
                                                                                                 (39)

where β is the number of gas atoms produced per fission event.
Following the work of Wood and Kear [12], grain boundary bubble nuclei of radius Rb are
produced until such time that a gas atom is more likely to be captured by an existing nucleus than

                                                             47
to meet another gas atom and form a new nucleus. An approximate result for the grain-boundary
bubble concentration is given by
                                                        1/ 2
                       ⎛    8 zaK   ⎞
                  Cb = ⎜ 1 / 3 2    ⎟
                       ⎜ 12 π ξD δ ⎟
                       ⎝          g ⎠
                                                                                            (40)

where a is the lattice constant, z is the number of sites explored per gas-atom jump, δ is the
width of the boundary, ξ is a grain-boundary diffusion enhancement factor, and K is the flux of
gas-atoms per unit area of grain boundary.


The intergranular bubble nucleation and growth formulation incorporated here is based on the
assumption that, although the effect of radiation-induced re-solution on intergranular bubble
behavior is not negligible, a reasonable approximation can be obtained by neglecting such effect
in the governing equations [13].
Under the above considerations, the flux K of atoms at the grain boundary is given by

                           d g dcg d ( f st )
                   K=
                           3 dt            dt                                               (41)

Differentiating Eq. (39)

                                            •
                   dc g          β f − c g df s / dt
                       =                                                                    (42)
                    dt   (1 + f s + 32 π f n rg Dg c g / b)
where, using Eq. (38)

                   d ( f st ) 12 ⎛⎜ Dg t Dg t ⎞⎟
                             =          −
                     dt        d g ⎜⎝ π   d g ⎟⎠
                                                                                            (43)

The concentration of gas on the grain boundaries, C g is given by

                                dg
                  C g (t ) =         f s (t )c g (t )                                       (44)
                                3

and the average number of gas atoms in a grain boundary bubble is

                                C g (t )
                   N b (t ) =
                                Cb (t )                                                     (45)

                                                               48
The radius of a grain boundary bubble is obtained from the solution to Eq. (35), i.e.

                                                                      1/ 3
                        ⎡ 3h b m                 2           3⎤
                        ⎢           ⎛ 3hs bv mb ⎞ ⎛ mb kT ⎞ ⎥
                   Rb =     s v b
                                  + ⎜           ⎟ − ⎜⎜    ⎟⎟
                        ⎢ 8π        ⎝ 8π ⎠ ⎝ 8πγ ⎠ ⎥
                        ⎣                                     ⎦
                                                                                      1/ 3
                                                                                                (46)
                                            ⎡ 3h b m                 2           3⎤
                                            ⎢           ⎛ 3hs bv mb ⎞ ⎛ mb kT ⎞ ⎥
                                          +     s v b
                                                      − ⎜           ⎟ − ⎜⎜    ⎟⎟
                                            ⎢ 8π        ⎝ 8π ⎠ ⎝ 8πγ ⎠ ⎥
                                            ⎣                                     ⎦

The fractional swelling due to fission gas is thus given by

                   ⎛ ΔV ⎞   cg a 3 4π ⎛ 3                   ⎞
                   ⎜    ⎟ =       +    ⎜ rb cb + Rb2Cb 6 ⎟                                      (47)
                   ⎝ V ⎠g     4     3 ⎜⎝               d g ⎟⎠

where the first term at the right-hand-side of Eq. (47) accounts for the contribution of the gas in
dynamic solution, and the second term for the contributions of both intragranular and
intergranular bubbles, respectively.

Finally, the fraction of gas in dynamic solution (i.e. not in bubbles) is given by

                                             c g (t )
                    X (t ) =
                               c g (t ) + C g (t ) + nb (t )cb (t )
                                                                                                 (48)
In general, in an irradiation environment where bubble nucleation, gas-atom diffusion to bubbles,
and irradiation-induced re-solution are operative, a differential growth rate between bubbles of
different size results in a peaked mono-modal size distribution [14]. The position of the peak in
the bubble-size distribution that occurs under these conditions is defined by the balance between
diffusion of gas-atoms to bubbles and irradiation-induced re-solution of atoms from bubbles. As
more gas is added to the lattice (e.g., due to continued fission), the gas-atom diffusion flux to
bubbles increases and the peak shifts to larger bubble sizes and decreases in amplitude, resulting
in an increased level of bubble swelling with increased burn-up. The model presented in this
section describes the average behavior of this peak as a function of burn-up.

4.2 Calculation of bubble-size distribution on grain boundaries

Let n(r )dr be the number of bubbles per unit volume on the grain boundaries with radii in the
range r to r + dr . Growth by gas atom collection from fission gas diffusing from the grain
interior removes bubbles from this size range, but these are replaced by the simultaneous growth
of smaller bubbles. The distribution of intragranular gas consists of a substantial concentration
of fission-gas atoms in solution due to the strong effect of irradiation-induced gas-atom re-
solution. Bubbles appear on the grain boundaries due to the reduced effect of re-solution
ascribed to the strong sink-like property of the boundary, enhanced gas-atom diffusion on the

                                                              49
boundary, and a sizeable reduction in the bubble nucleation rate as compared to that occurring in
the grain interior. A differential growth rate between bubbles of different size leads to a net rate
of increase in the concentration of bubbles in the size range r to r + dr . This behavior is
expressed by
                    ⎡ dn(r ) ⎤       d ⎡       dr ⎤
                    ⎢⎣ dt ⎥⎦ dr = − dr ⎢⎣n(r ) dt ⎥⎦ dr .                                             (49)

The growth rate ( dr / dt ) of a particular bubble is related to the rate ( dm / dt ) at which it absorbs
gas from the matrix. The rate of precipitation is controlled by the grain-boundary gas-atom
diffusion coefficient ξD g and the average concentration C g of fission gas retained by the
boundary.

Studies on the evolution of helium bubbles in aluminum during heavy-ion irradiation at room
temperature have shown that bubble coarsening can take place by radiation-induced coalescence
without bubble motion [15]. This coalescence (called sputtering coalescence) is the result of the
net displacement of Al atoms out of the volume between bubbles initially in close proximity.
The resulting non equilibrium-shaped bubble evolves toward a more energetically favorable
spherical shape whose final size is determined by the equilibrium bubble pressure.

In what follows it is assumed that the observed intergranular bubble coalescence events occur
primarily by the sputtering coalescence mechanism. This mechanism should also be operative
for intragranular bubbles, but will have a limited effect due to the small size of the bubbles
compared to the inter-bubble spacing.

Bubble coalescence without bubble motion can be understood on the basis of a difference in the
probability for an atom to be knocked out of the volume between a pair of bubbles and the
probability of an atom to be injected into this inter-bubble volume. If the bubbles contained the
same atoms as that comprising the inter-bubble volume, the net flux of atoms out of the inter-
bubble volume would be zero. However, since the gas bubbles contain fission gas and not
matrix atoms, the flux of atoms into the inter-bubble volume is reduced by the bubble volume
fraction, i.e., the net flux out of volume is proportional to λV − λ (V − VB ) , where λ is the atom
knock-on distance, and V B is the intergranular bubble volume fraction. It is assumed that most
of the impacted atoms receive enough energy to travel distances λ on the order of the inter-
bubble spacing. Thus, assuming that the atom displacement rate is proportional to the fission
rate, the net rate of change in the concentration of bubbles in the size range r to r + dr due to
bubble coarsening without bubble motion is given by
                     ⎡ dn(r ) ⎤       6       •

                     ⎢⎣ dt ⎥⎦   dr =     λδ s f πr 2 n(r )dr ,                                     (50)
                                      dg
where the effective grain-face-bubble volume is assumed to be disk-shaped (lenticular) with
volume = δ sπr 2 , and where δ s is the thickness of the material undergoing sputtering. For a
lenticular bubble with radius of curvature ρ the equivalent radius of a spherical bubble is given
by
                     r = ρf (θ )
                                 1/ 3
                                                                                                   (51)
where

                                                   50
                               3         1
                   f (θ ) = 1 − cos(θ ) + cos 2 (θ )                                             (52)
                               2         2
and
                               γ gb
                   cos(θ ) =        ,                                                            (53)
                               2γ
where γ gb is the grain boundary energy. In Eq. (50), it is assumed that bubble coalescence is
approached by the gradual erosion of material between the bubbles. Thus, Eq. (50) expresses a
differential shrinkage rate between bubbles of different size due to the agglomeration of smaller
bubbles by larger bubbles that leads to a net rate decrease in the concentration of bubbles in the
size range r to r + dr

The overall net rate of change of the concentration of bubbles in a given size range is derived by
subtracting the right-hand side of Eq. (50) from that of Eq. (49):
            dn(r )         d ⎡      dr ⎤     6     •
                   dr = − ⎢n(r ) ⎥ dr − λδ s f πr 2 n(r )dr .                                  (54)
              dt          dr ⎣      dt ⎦    dg
The equilibrium population of bubbles is obtained by setting Eq. (51) to zero
                    d ⎡ dr ⎤ dr dn(r ) 6        •
            − n(r ) ⎢ ⎥ −                − λδ s f πr 2 n(r )dr = 0 .                           (55)
                   dr ⎣ dt ⎦ dt dr        dg
Equation (55) must be solved subject to the relevant boundary condition. In general, this
boundary condition concerns the rate at which bubbles are formed at their nucleation size r0 . The
rate of bubble nucleation is provided by the Wood-Kear nucleation mechanism [12] where on the
grain boundary the average time τ b for a gas atom to diffuse to an existing bubble (as discussed
above this is the time at which bubble nucleation would essentially cease) is given by
                             1
                    τb =            .                                                          (56)
                          πξD g C b
Thus, from Eq. (56) it follows that the bubble nucleation rate is given by
                     dC b      C
                          =η b .                                                               (57)
                      dt       τb
where η is a proportionality constant that is determined by imposing the conservation of gas
atoms.

From a consideration of the growth rate of freshly nucleated bubbles it follows that
                               3η ⎛ C b ⎞
                    n(r0 )dr =      ⎜    dr ⎟ / (dr / dt )r = r0 .                               (58)
                               d g ⎜⎝ τ b ⎟⎠
The observed grain boundary bubbles are a combination of spherical lenticular shaped objects
whose size is substantially larger than the estimated thickness of the grain boundary (see Table
3). In general, the solubility of gas on the grain boundary is substantially higher than in the bulk
material. The gas concentration on the boundary will increase until the solubility limit is reached
(approximately given by τ b ), whereupon the gas will precipitate into bubbles. Thus, the rate at
which a grain boundary bubble adsorbs gas is approximately given by


                                                 51
                   (dm / dt )r =r = bv C g / (4τ bπr03 / 3) ,
                                 0
                                                                                                (59)
where C g is given by Eq.(44). Using Eq. (35)
                   dm
                        ==
                                     (
                             16πγ kTr 3 + 3γbv r 2 dr )                                       (60)
                                  3(rkT + 2γbv )
                                                 2
                    dt                                 dt
Combining Eqs. (59) and (60)
                                           3C g bv (rkT + 2γbv )
                                                                 2

                   (dr / dt )r =r0 =                                                          (61)
                                     16πγ (4τ bπr03 / 3)(kTr 3 + 3γbv r 2 )
Subsequent to intergranular bubble nucleation, gas solubility on the boundary will drop to a
relatively low value and gas arriving at the boundary will be adsorbed by the existing bubble
population. The rate at which a grain boundary bubble adsorbs gas is approximately given by
                   dm / dt = 12πrξD g C g / d g .                                             (62)
Combining Eq. (60) and (62)
                           9rξD g C g (rkT + 2γbv )     3bvξD g C g
                                                    2

                 dr / dt =                            ≈             .                           (63)
                                         (
                            4γd g kTr + 3γbv r
                                        3       2
                                                          )dgr
Using the approximation on the right-hand side of Eq. (63), Eq. (55) becomes
                        3b ξD C      3b ξD C dn(r ) 6                •
                  n(r ) v g2 g − v g g                    − λδ s f πr 2 n(r ) = 0 ,          (64)
                           dgr             dgr       dr       dg
The solution of Eq. (64) subject to the boundary condition expressed by Eq. (58) and (61) is
                  n( r ) =
                                                                [       ]
                           64ηγC b2π 2 r 3 (kTr 3 + 3γbv r 2 )exp − κ (r 4 − r04 )
                                                                                   ,         (65)
                                        3bv C g d g (rkT + 2γbv )
                                                                  2


where
                             •
                       π f λδ s
                   κ=            .                                                              (66)
                      2bvξDg C g

4.3 Comparison of calculated intergranular bubble-size distribution with the measured
data

The values of the key parameters used in the model are given in Table 9. Many of them are
known from the literature [16]; the values of the others (e.g. ξ and Dg ) resulted from the fitting
of the present theory with measured data of bubble populations. The value used for Dg is
consistent with that used in the homogenization analysis in Section 2 [5]. The intergranular
bubble size depends on the value of ξ (see Eq. (40) and Table 9), which is a grain-boundary gas-
atom diffusion enhancement factor that reflects the fact that grain boundary diffusion is
decidedly faster than grain lattice diffusion [17,18]. The effect of ξ on the intergranular bubble
nucleation is visible in Eq. (40). By increasing ξ the intergranular bubble density is reduced
with a commensurate increase in bubble size. The larger value used for ξ for the non-annealed
miniplates reflects the increase in diffusivity with decreased molybdenum content.



                                                          52
                      Table 9. Values of parameters used in the calculations

                Parameter                               Value                     Reference
                     β                                     0.25                  Olander [16]
                     ξ                                  7 x 103                (annealed) [17]
                                                                  4
                                                        4 x 10             (non-annealed) This work
                            •
               b0 ( b = b0 f )                       1 x 10-24 m3                 This work
                                •
              D0 ( Dg = D0 f )                       2.5 x 10-41 m5               This work
                     rg
                                                       0.216 nm                  Olander [16]
                     γ                                 0.8 J m-2                  This work
                  cos(θ )                                  0.2                       [19]
                    bv                       8.5 x 10-23 m3/atom                 Olander [16]
                     fn                                 5 x 10-3               Spino/Rest [10]
                     hs                                    0.6                 Spino/Rest [10]
                  δs = δ                              1 x 10-9 m                   [17,18]
                     λ                                2 x 10-7 m                 Olander [16]


The calculated distribution was obtained by integrating Eq. (65) over the experimentally defined
bin sizes Δ i , i.e. the bubble density N (Δ i ) in units of m-2 is

                                          Δ 0 + iΔ
                                dg
                   N (Δ i ) =                    n(r )dr
                                    3 Δ 0 + (∫i −1) Δ
                                                                                                      (67)


where Δ 0 is the minimum bubble size observed.

Table 10 shows a description of fuel used in the analysis. This data base consists of both as-
atomized and γ-annealed specimens. From table 10, the range of burn up is from 30 – 49 at% U-
235, fission rate from 2.3 – 7 x 1014 f/cm3-s, temperature from 66 – 185 ºC, and Mo content from
6 – 10 wt.%. As shown in Table 11, the values for the critical parameters D g and b listed in
Table 9 were estimated by comparing the calculated intragranular average bubble size and
density to measured results [6]. The value for D g is comparable to the one used by Bleiberg [5]
for irradiation induced mixsing. The remaining critical parameter ξ was determined by best
overall interpretation of the measured intergranular bubble-size distributions for the γ-annealed


                                                                      53
and for the as-atomized specimens, respectively. The calculated results shown in Table 11 can
be brought more in line with the data by decreasing D g , increasing b , or both. This then would
require a commensurate decrease in ξ . For this exercise to be meaningful measured
intragranular bubble-size distributions are required.


                          Table 10. Description of fuel used in the analysis

                                                         Burnup,      Fission              Fuel
                  Plate                                                            Time
       Test                  Plate ID    Fuel property     at%      rate (1014)            Temp
                 AG ID                                                            (days)
                                                          U-235       f/cm3-s               (oC)
   RERTR-3      580H        Z03      U-10Mo(a,γ)       32         5.3         48      121
   RERTR-3      580C       Y01       U-10Mo(m,γ)       30         4.8         48      109
   RERTR-1        -        V002       U-10Mo(a)        39         3.8         94       66
   RERTR-3      580G       V07        U-10Mo(a)        30         5.1         48      122
   RERTR-3 580W            V03        U-10Mo(a)        38         6.3         48      149
   RERTR-3      580Z        S03        U-6Mo(a)        39         7.0         48      158
   RERTR-5 600AG R6007F                U-7Mo(a)        37         2.4        116      185
   RERTR-5 600M V6019G                U-10Mo(a)        49         2.9        116      142
   RERTR-5 600AH V8005B               U-10Mo(a)        37         2.4        116      170
      a: atomized, γ: annealed at 800 C for 70-100 hours before plate fabrication, m: machined
                                     o




              Table 11. Intragranular results using estimated values for D g and b

                                                   Calculated                       Data [4]
   Bubble diameter (nm).                              2.1                             ≈2
   Bubble density (cm-3)                           1.4 x 1018                      ≈ 3 x 1018




                                                 54
                                   Grain-boundary bubble size distribution for Z03
                       4e+8

                                                                                           Theory
                                                                                           Data
                       3e+8




Bubble Density (cm )
-2

                       2e+8




                       1e+8




                       0




                           0.04        0.06        0.08          0.10       0.12        0.14            0.16

                                                     Bubble Diameter (μm)

                       Fig. 39 Calculated and measured intergranular bubble-size distribution for Z03
                                         plate. Atomized and γ-annealed U-10Mo.




                                                            55
                                   Grain-boundary bubble size distribution for Y01
                       4e+8

                                                                                          Theory
                                                                                          Data
                       3e+8




Bubble Density (cm )
-2

                       2e+8




                       1e+8




                       0




                           0.04        0.06        0.08          0.10       0.12        0.14        0.16

                                                     Bubble Diameter (μm)

                       Fig. 40 Calculated and measured intergranular bubble-size distribution for Y01
                                          plate. Machined and γ-annealed U-10Mo.




                                                            56
                                      Grain-boundary bubble size distribution for V03
                       2.5e+8

                                                                                              Theory
                       2.0e+8                                                                 Data




Bubble Density (cm )
-2
                       1.5e+8



                       1.0e+8



                       5.0e+7



                       0.0




                             0.05        0.10         0.15          0.20       0.25         0.30           0.35

                                                        Bubble Diameter (μm)

                         Fig. 41 Calculated and measured intergranular bubble-size distribution for V03.
                                                    As-atomized U-10Mo.




                                                               57
                                     Grain-boundary bubble size distribution for V07
                        2e+8

                        2e+8                                                               Theory
                                                                                           Data
                        2e+8

                        1e+8




Bubble Density (cm-2)
                        1e+8

                        1e+8

                        8e+7

                        6e+7

                        4e+7

                        2e+7

                        0


                            0.05        0.10        0.15           0.20      0.25         0.30        0.35

                                                       Bubble Diameter (μm)

                        Fig. 42 Calculated and measured intergranular bubble-size distribution for V07.
                                                   As-atomized U-10Mo.




                                                              58
                                      Grain-boundary bubble size distribution for V8005B
                       2.5e+8

                                                                                              Theory
                       2.0e+8                                                                 Data




Bubble Density (cm )
-2
                       1.5e+8



                       1.0e+8



                       5.0e+7



                       0.0




                               0.05        0.10         0.15         0.20        0.25        0.30         0.35

                                                          Bubble Diameter (μm)

                             Fig. 43 Calculated and measured intergranular bubble-size distribution for
                                                  V8005B. As-atomized U-10Mo.




                                                                59
                                      Grain-boundary bubble size distribution for V6019G
                       2.5e+8

                                                                                              Theory
                       2.0e+8                                                                 Data




Bubble Density (cm )
-2
                       1.5e+8



                       1.0e+8



                       5.0e+7



                       0.0




                               0.05        0.10         0.15         0.20        0.25        0.30         0.35

                                                          Bubble Diameter (μm)

                             Fig. 44 Calculated and measured intergranular bubble-size distribution for
                                                  V6019G. As-atomized U-10Mo.




                                                                60
                                    Grain-boundary bubble size distribution for V002
                       1.8e+8

                       1.6e+8                                                              Theory
                                                                                           Data
                       1.4e+8




Bubble Density (cm )
-2                     1.2e+8

                       1.0e+8

                       8.0e+7

                       6.0e+7

                       4.0e+7

                       2.0e+7

                       0.0


                             0.05       0.10         0.15         0.20       0.25         0.30        0.35

                                                       Bubble Diameter (μm)

                       Fig. 45 Calculated and measured intergranular bubble-size distribution for V002.
                                                   As-atomized U-10Mo.




                                                             61
                                     Grain-boundary bubble size distribution for S03
                       1.6e+8

                       1.4e+8                                                               Theory
                                                                                            Data
                       1.2e+8




Bubble Density (cm )
-2
                       1.0e+8

                       8.0e+7

                       6.0e+7

                       4.0e+7

                       2.0e+7

                       0.0


                             0.05        0.10        0.15          0.20       0.25         0.30           0.35

                                                       Bubble Diameter (μm)

                        Fig. 46 Calculated and measured intergranular bubble-size distribution for S03.
                                                   As-atomized U-6Mo.




                                                              62
                                      Grain-boundary bubble size distribution for R6007F
                       2.5e+8

                                                                                              Theory
                       2.0e+8                                                                 Data




Bubble Density (cm )
-2
                       1.5e+8



                       1.0e+8



                       5.0e+7



                       0.0




                               0.05        0.10         0.15         0.20        0.25        0.30         0.35

                                                          Bubble Diameter (μm)

                             Fig. 47 Calculated and measured intergranular bubble-size distribution for
                                                  R6007F. As-atomized U-7Mo.




                                                                63
Figures 39 and 40 show the calculated and measured intergranular bubble-size distribution for γ-
annealed plates. Figure 39 is atomized whereas Fig. 40 is machined. Figures 41 - 47 show calculated
and measured intergranular bubble-size distribution for as-atomized plates. Figures 41-45 are for 10
wt% Mo whereas Figs. 46 and 47 are for 6 and 7 wt% Mo, respectively. As is evident from Figs. 39
- 47, in general, the model calculations are in remarkable agreement with the data. The error bars are
shown on the measured data reflect the measurement uncertainties discussed in Subsection. 3.1. The
larger deviation between calculated and measured results shown for the plates in Figs 46 and 47 is
most likely due to the lower as fabricated Mo content and, thus, requires different values for D g and
ξ.

4.4 Calculation of intragranular bubble-size distribution: effect of uncertainties in
    materials properties

Intragranular bubbles are subject to destruction by irradiation-induced re-solution. In general, the
average intragranular bubble in UMo is small enough that whole bubble destruction is a
reasonable assumption. In this case, the net rate of change in the concentration of bubbles in the
size range r to r + dr due to destruction by fission fragments is given by
                   ⎡ dn(r ) ⎤           •

                   ⎢ dt ⎥     dr = 2λ f f πr 2 n(r )dr                                         (68)
                   ⎣        ⎦
where λ f is the average range of a fission fragment. Replacing the last term in Eq. (54) with Eq.
(68) and using the boundary condition
                               ⎛c      ⎞
                   n(r0 )dr = ⎜⎜ b dr ⎟⎟ / (dr / dt )r = r0                                    (69)
                               ⎝τ b ⎠
where
                            1
                   τb =                                                                        (70)
                          πD g cb
and
                   dr bv D g c g
                      =                                                                        (71)
                   dt     r
one obtains
                              πcb2 r exp[− κ (r 4 − r04 )]
                   n( r ) =                                                                    (72)
                                        bv c g
where
                                •
                          π fλ
                  κ=                                                                           (73)
                        2bv D g c g




                                                         64
In order to proceed λ f needs to be expressed in terms of the re-solution rate b . Whole bubble
destruction is included in Eq. (31) through via the last term in Eq. (32), i.e.

         dcb (t )    b
                  ≈ − cb (t ) .                                                                 (74)
            dt       2
Using Eq. (67), (68) and (72) in Eq. (74), after utilizing an approximation for the Error function,
one obtains

                     9b02
           λs =                ,                                                                  (75)
                  128bv D0 c g


Figure 48 shows calculated intragranular bubble size distributions for 3 values of the gas-atom
diffusivity, and re-solution rate, respectively. The results shown in Fig. 48 indicate the
sensitivity of the calculated distributions to variations in the values of these critical parameters.
One of the major challenges in the field of fission gas behavior in nuclear fuels is the
quantification of critical materials properties. There is a direct correlation between the accuracy
of the values of critical properties and the confidence level that the proposed underlying physics
is realistic.




                                                  65
                           Intragranular Bubble Size Distribution in U-10Mo
                             for 3 values of Gas-Atom Diffusion Coefficient
                      16

                      14                                                D0=5x10-32cm5
                                                                        D0=2.5x10-31cm5
                      12                                                D0=5x10-31cm5

                      10

    x 10 )
   -27

                      8
   -4
                      6
    n(cm
                      4

                      2

                      0


                             0.0         0.5        1.0       1.5        2.0            2.5

                                           Bubble Diameter (nm)


                           Intragranular Bubble Size Distribution in U-10Mo
                               for 3 values of Gas-Atom Re-solution Rate
                      25

                                                                        b0=5x10-19cm3
                      20                                                b0=1x10-18cm3
                                                                        b0=5x10-18cm3

                      15




    n(cm-4 x 10-27)
                      10



                       5



                       0




                             0       1         2          3         4       5             6

                                           Bubble Diameter (nm)

Fig. 48 Calculated intragranular bubble size distributions for 3 values of the gas-
                                           •                                            •
       atom diffusivity ( Dg = D0 f ) and gas-atom re-solution rate ( b = b0 f ).


                                                   66
5. Conclusions

1.   Analysis using a simple diffusion model shows that the grain boundaries are not completely
     homogenized by irradiation under typical RERTR test conditions.

2.   Fission gas bubbles visible in SEM micrographs first appear on the grain boundaries in U-
     Mo alloy fuels from RERTR-1, 2, 3 and 5 tests.

3.   The plates with γ-phase annealed powders have smaller bubbles and lower volume
     fractions than the plates with as-fabricated powders.

4.   Although there are considerable errors, after an initial incubation period the average bubble
     size increases with fission density and shows saturation at high fission density.

5.   The γ-annealed powder plates have a higher bubble density per unit grain boundary length
     than the as-atomized powder plates. The measured bubble number densities per unit grain
     boundary length for as-atomized powder plates are approximately constant with respect to
     burnup.

6.   Bubble density per unit cross section area was calculated using the density per unit grain
     boundary length data. The grains were modeled as tetrakaidecahedrons. Direct
     measurements for some plates were also performed and compared with the calculated
     quantities. Bubble density per unit grain boundary surface area was also calculated by
     using the density per unit grain boundary length data. These data were used as input for
     mechanistic modeling.

7.   The contribution to the total fuel swelling by fission gas bubbles is very small in the pre-
     recrystallization regime. This suggests that in the pre-transition regime a considerable
     concentration of fission gas remains in atomic solution or in small bubbles not resolvable
     by SEM.

8.   Calculations of intergranular bubble size distribution made with a new mechanistic model
     of grain boundary bubble formation kinetics is consistent with the measured distributions.

9.   The gas-atom diffusion enhancement factor for grain boundaries was determined for as-
     annealed powder plates to be ≈ 104 in order to obtain agreement with the measured
     distributions. This value of enhancement factor is consistent with values obtained in the
     literature. The enhancement factor is six times higher for as-fabricated powder plates than
     for the annealed plates due to the lower Mo content on the boundaries.

10. Model predictions are sensitive to various model parameters such gas-atom diffusivity and
    re-solution rate. Improved predictive capability requires an accurate quantification of these
    critical materials properties and measurement data.




                                                67
References

[1]    K.H. Kim et al., J. Nucl. Mater, 245 (1997) 179.
[2]    J.M. Park et al., RERTR Conf., 2006. Available from: http://www.rertr.anl.gov/index.html
[3]    W. Sinkler et al., ANL Memo to M.K. Meyer, WS-2000.
[4]    M.L. Bleiberg et al., J. Appl. Phys., 27(11) (1956) 1270.
[5]    M.L. Bleiberg, J. Nucl. Mater., 2 (1959) 182.
[6]    S. Van Den Berghe at al., RERTR conf., 2007. Available from:
       http://www.rertr.anl.gov/index.html
[7]    R.T. DeHoff and F.N. Rhines, Quantitative microscopy, McGraw-Hill, New York, 1968.
[8]    Yeon Soo Kim, G.L. Hofman, M.R. Finlay, J.L. Snelgrove, Milestone report on
       Postirradiation Examinations: RERTR-3, 4 and 5, ANL, September 2005.
[9]    Yeon Soo Kim et al., RERTR conf, 2007. Available from:
       http://www.rertr.anl.gov/index.html
[10]   J. Spino, J. Rest, W. Goll, C.T. Walker, J. Nucl. Mater, 346 (2005) 131.
[11]   ]M.V. Speight, Nucl. Sci. Eng. 37 (1969) 180.
[12]   M.H. Wood, K.L. Kear, J. Nucl. Mater 118 (1983) 320.
[13]   J. Rest, J. Nucl. Mater, 321 (2003) 305.
[14]   M.V. Speight, J. Nucl. Mater, 38 (1971) 236.
[15]   R.C. Birtcher, S.E. Donnelly, C. Templier, Phys. Rev. B, 50 (1994) 764.
[16]   D.R. Olander, Fundamental Aspects of Nuclear Reactor Fuel Elements, Technical
       Information Center, ERDA, USA, 1976.
[17]   N.A. Gjostein, in Diffusion, Chapter 9, American Society for Metals, Metals Park, Ohio
       (1973) 272.
[18]   J.C. Fisher, J. Appl. Phys., 22 (1951) 74.
[19]   E.D. Hondros, in Precipitation Processes in Solids, K.C. Russell and H.I. Aaronson, Eds.,
       The Metallurgical Society of AIME (1976) 1.




                                              68
Nuclear Engineering Division
Argonne National Laboratory
9700 South Cass Avenue, Bldg. 208
Argonne, IL 60439-4842

www.anl.gov




A U.S. Department of Energy laboratory
managed by UChicago Argonne, LLC
