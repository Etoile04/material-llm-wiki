# Fission induced swelling and creep of U–Mo alloy fuel

---

                                                               Journal of Nuclear Materials 437 (2013) 37–46



                                                        Contents lists available at SciVerse ScienceDirect


                                                        Journal of Nuclear Materials
                                              journal homepage: www.elsevier.com/locate/jnucmat




Fission induced swelling and creep of U–Mo alloy fuel q
Yeon Soo Kim a,⇑, G.L. Hofman a, J.S. Cheon b, A.B. Robinson c, D.M. Wachs c
a
  Argonne National Laboratory, 9700 South Cass Avenue, Argonne, IL 60439, USA
b
  Korea Atomic Energy Research Institute, 989-111 Daedeok-daero, Yuseong, Daejeon 305-353, Republic of Korea
c
  Idaho National Laboratory, P.O. Box 1625, Idaho Falls, ID 83415, USA




a r t i c l e        i n f o                           a b s t r a c t

Article history:                                       Tapering of U–Mo alloy fuel at the end of plates is attributed to lateral mass transfer by ﬁssion induced
Received 29 November 2012                              creep, by which fuel mass is relocated away from the fuel end region where ﬁssion product induced fuel
Accepted 28 January 2013                               swelling is in fact the highest. This mechanism permits U–Mo fuel to achieve high burnup by effectively
Available online 8 February 2013
                                                       relieving stresses at the fuel end region, where peak stresses are otherwise expected because peak ﬁssion
                                                       product induced fuel swelling occurs there. ABAQUS FEA was employed to examine whether the observed
                                                       phenomenon can be simulated using physical–mechanical data available in the literature. The simulation
                                                       results obtained for several plates with different fuel fabrication and loading scheme showed that the
                                                       measured data were able to be simulated with a reasonable creep rate coefﬁcient. The obtained creep rate
                                                       constant lies between values for pure uranium and MOX, and is greater than all other ceramic uranium
                                                       fuels.
                                                                                                                          Ó 2013 Elsevier B.V. All rights reserved.



1. Introduction                                                                             In the postirradiation examination (PIE) of fuel plates, it is a
                                                                                        common observation that the fuel meat or foil swelling close to
   Two forms of U–Mo alloy fuel have been irradiation-tested in                         the plate width end is signiﬁcantly diminished. This phenomenon
the US GTRI (Global Threat Reduction Initiative) in order to qualify                    is clearly observable in some RERTR plates where one of the plate
this fuel for the conversion of research and test reactors from                         width ends faces the ATR core, resulting in a large power peaking
highly enriched uranium (HEU) to low enriched uranium (LEU).                            at the foil end and subsequently a peak in ﬁssion density. Because
One form, dispersion fuel, consists of fuel particles dispersed in                      fuel swelling increases with ﬁssion density, this is an obvious con-
an aluminum matrix and the other, monolithic fuel, is of solid alloy                    tradiction accordingly (see Fig. 2).
fuel foil directly bonded to aluminum cladding. The geometry for                            The most plausible causes for this phenomenon are lateral fuel
both fuel forms is a thin plate. Fig. 1 schematically illustrates the                   transport toward the fuel center in the width direction and accu-
cross section of a monolithic mini-fuel plate.                                          mulation of fuel mass at regions away from the foil end. The driv-
   Swelling of U–Mo fuel only increases the plate thickness be-                         ing force for the fuel volume transport is the shear stress that
cause the other dimensions are constrained. Consequently, fuel                          builds up because of ﬁssion product induced fuel swelling while
swelling can be estimated with fair accuracy by measuring the fuel                      the Al cladding volume is preserved. Because the fuel foil end is
plate thickness during post-irradiation analyses. U–Mo fuel swell-                      blocked by the cladding, the resulting stress directs the fuel vol-
ing kinetics as a function of ﬁssion density is previously docu-                        ume transport away from the plate to a lower stress region toward
mented [1]. The U–Mo fuel swelling we are dealing with occurs                           the fuel width center (Fig. 2). Fission induced creep of U–Mo is the
at irradiation temperatures typically lower than 250 °C in re-                         underlying mechanism that controls the rate of the fuel volume
search and test reactors. In addition, because the ﬁssion gas bub-                      transport [2].
bles are small, the fuel swelling part that is affected by                                  Although similar observations have been made for dispersion
temperature is also small.                                                              fuel plates, the phenomenon is more difﬁcult to quantify in this
                                                                                        type fuel because of its complex microstructure that include vari-
  q
                                                                                        ations in fuel volume fraction in the meat, the presence of variable
    The submitted manuscript has been created by the UChicago Argonne, LCC as
                                                                                        fractions of fuel–Al matrix interdiffusion products, and pore forma-
Operator of Argonne National Laboratory under contract No. DE-AC-02-06CH11357
between the UChicago Argonne, LLC and the Department of Energy. The U.S.                tion in matrix in some cases. Monolithic fuel plates do not have
Government retains for itself, and others acting on its behalf, a paid-up, nonexclu-    these complications, so this paper focuses on analyzing monolithic
sive, irrevocable worldwide license in said article to reproduce, prepare derivative    fuel plates, leaving dispersion fuel plate analysis for future work.
works, distribute copies to the public, and perform publicly and display publicly, by
                                                                                            Finite element analysis (FEA) using a commercial code ABAQUS
or on behalf of the Government.
  ⇑ Corresponding author. Tel.: +1 630 252 3173; fax: +1 630 252 5161.                  [3] was employed to examine whether the observed phenomenon
    E-mail address: yskim@anl.gov (Y.S. Kim).                                           is physically realistic by applying materials physical–mechanical

0022-3115/$ - see front matter Ó 2013 Elsevier B.V. All rights reserved.
http://dx.doi.org/10.1016/j.jnucmat.2013.01.346
38                                                        Y.S. Kim et al. / Journal of Nuclear Materials 437 (2013) 37–46


                                          Thickness
                                                                     Al-alloy cladding
                                                                                                    U-Mo foil
                                                      Width                                                        0.25

                                                                                                                                             1.4

                                           3.2                                  Foil width = 19.0

                                                                             Plate width = 25.4

                                                                                                            * Dimensions in mm

                                         Fig. 1. Schematic of as-fabricated cross section at axial mid-plane of a monolithic miniplate.




                                     Thickness                                            Peak thickness region
                                                                                                                               ATR core
                                                                     U-Mo foil
                                              Width




                                                              Al-alloy cladding

                                        Fig. 2. Fuel plate cross section in the width direction at near the ATR-core side end of L1P04A.



parameters in reasonable ranges. Simultaneously, another objec-                                The fuel foil was metallurgically bonded to Al 6061 cladding.
tive of the FEA simulation was to obtain a creep rate coefﬁcient                            Two kinds of bonding method were applied. One was friction stir
that enables the extent of the fuel mass transport observed at                              welding (FSW) and – as the name implies – it achieved a metallur-
the end of life (EOL) of the plates caused by creep.                                        gical bonding between the fuel foil and cladding by welding, during
                                                                                            which the cladding was instantaneously melted at the foil–cladding
2. Experimental                                                                             interface. The other method was hot isostatic pressing (HIP), in
                                                                                            which an isostatic pressure of 103 MPa was applied for 90 min
    The plates used for this paper were from irradiation tests RERTR-                       while the plate was heated at 560–580 °C . The details of the bond-
6, -7, -8, -9A, -9B, -10, and -12. The plate fabrication and irradiation                    ing methods can be found, for example, in Ref. [4]. It is worth noting
properties are summarized in Table 1. The plate dimensions are                              that both bonding methods produce uniform bonding and, more
100 mm in length, 25 mm in width, and 1.40 mm in thickness, which                           importantly, do not alter foil thickness during plate fabrication.
are a miniature version, except for the thickness, of full-size fuel                           All the test plates were irradiated in the Advanced Test Reactor
plates used in research reactors and test reactors. The fuel foil                           (ATR) at INL. The ﬁssion rate histories of one representative plate
dimensions are 82.6 mm in length and 19.0 mm in width. Foil thick-                          from each test are compared in Fig. 3.
ness is typically 0.25 mm, and in some cases 0.50 mm is used to                                The plates were loaded in the ATR in such a conﬁguration that
examine the performance of thinner cladding.                                                either a ﬂat plate surface or a narrow edge faced the ATR core cen-


Table 1
Description of irradiated mini fuel plates used in the analysis.

     Test         Plate ID      U–Mo foil property and             Enrichment      U-235 burnup,                            Total duration         Fission densityb   BOL Fuel
                                plate fabrication methoda          (%U-235)        U-235-ﬁssioned/U-235-initial (%)         (EFPD)                 (1021 f/cm3)       Tempc (°C)
     RERTR-6      L1F040        U–10Mo(f,n)                        19.7            46                                       135                    3.0                113
     RERTR-6      L1F100        U–10Mo(f,n)                        19.7            46                                       135                    3.0                124
     RERTR-6      L2F030        U–10Mo(f,t)                        19.7            40                                       135                    2.6                145
     RERTR-7      L1F140        U–10Mo(f,n)                        58.2            27                                        90                    4.4                177
     RERTR-7      L2F040        U–10Mo(f,t)                        58.3            17                                        90                    2.7                199
     RERTR-8      H1P010        U-12Mo(p,n)                        57.5            31                                       105                    5.7                164
     RERTR-9A     L1P04A        U–10Mo(p,n)                        58.3            28                                        98                    4.5                152
     RERTR-9A     L1F26C        U–10Mo(f,n)                        57.5            33                                        98                    5.5                181
     RERTR-9A     L1F32C        U–10Mo(f,n)                        57.8            32                                        98                    5.4                181
     RERTR-9B     L1F34T        U–10Mo(f,n)                        58.8            37                                       115                    6.4                186
     RERTR-9B     L1P05A        U–10Mo(p,n)                        58.3            34                                       115                    5.5                170
     RERTR-9B     L1P09T        U–10Mo(p,n)                        58.8            39                                       115                    6.8                189
     RERTR-10     L1P12Z        U–10Mo(p,n)                        67.0            22                                        75                    4.9                167
     RERTR-12     L1P755d       U–10Mo(p,n)                        70.0            25                                        90                    5.9                156

f: Friction bonding.
p: Hot isostatic pressing bonding.
n: As-fabricated foil thickness = 0.25 mm, plate thickness = 1.4 mm.
t: As-fabricated foil thickness = 0.50 mm, plate thickness = 1.4 mm.
   a
     Number in front of Mo stands for Mo alloying content in weight%.
  b
     Fuel volume average at EOL including ﬁssions by Pu produced during irradiation.
   c
     At fuel width center.
  d
     Face-on loading. All other plates were edge-on loaded to the center of the ATR (Fig. 4).
                                                                         Y.S. Kim et al. / Journal of Nuclear Materials 437 (2013) 37–46                                       39


                                                                                                               For plates from RERTR-6, -7, -8, -9A, 9B, -10, and -12, foil thick-
                                                                     RERTR-6 (L1F040)
                                                                     RERTR-7 (L1F140)                      nesses were measured using post-irradiation micrographs across
                                14
                                                                     RERTR-8 (H1P010)                      the foil width with an interval typically of 0.5 mm. The measured
                                                                     RERTR-9A (L1P04A)                     fuel swelling data are given in Table 2. The uncertainty in the mea-
                                12                                   RERTR-9B (L1P05A)                     sured fuel swelling is ±2%, mainly due to the fabrication variability




  Fission rate (1014 f/cm3-s)
                                                                     RERTR-10 (L1P12Z)
                                                                     RERTR-12 (L1P755)
                                                                                                           in foil thickness.
                                10
                                                                                                               Fuel swelling was also calculated by using the correlation avail-
                                                                                                           able in the literature [1]. The correlation includes two parts: swell-
                                8
                                                                                                           ing by solid ﬁssion products and swelling by ﬁssion gas bubbles. It
                                                                                                           is expressed as a function of ﬁssion density. Therefore, once the ﬁs-
                                6
                                                                                                           sion density at the desired point is known, fuel swelling can be cal-
                                                                                                           culated. However, the calculated fuel swelling is purely by ﬁssion
                                4
                                                                                                           products; mass transfer by creep is not included. The calculated
                                                                                                           fuel swelling values are also included in Table 2.
                                2
                                                                                                               The measured fuel swelling data of L1P04A are plotted with the
                                                                                                           calculated in Fig. 5. The measured swelling at the tapered end of
                                0
                                     0   20   40   60     80       100       120      140      160
                                                                                                           the foil, marked by A in Fig. 5, is substantially lower than the cal-
                                                        Time (d)                                           culated value. This and the evidence that the ﬁssion gas porosity
                                                                                                           does not vary in size and number density appreciably along several
Fig. 3. Foil-averaged ﬁssion rate histories of fuel plates. A representative plate from                    millimeters from the foil end (see Fig. 6) rule out, at least to the
each test is shown. An axial power peaking of 0.95 was multiplied to obtain the real                       ﬁrst order, the effect of ﬁssion gas induced fuel swelling. The calcu-
value at the location where the PIE was performed except for RERTR-6. For RERTR-6,
                                                                                                           lated areas A and B, the areas enclosed by the measured fuel swell-
the axial power factor is about 1.
                                                                                                           ing curve and the calculated swelling curve, were close to each
                                                                                                           other. The same calculation showed that the areas C and D at the
ter. In the former case, called face-on loading, the power distribu-                                       opposite end of the foil were also similar. This salient phenomenon
tion of the plate in the width direction is approximately symmetric                                        is commonly observed for all plates, although area comparisons are
and more uniform. Slight power peakings at the ends still exist due                                        not perfectly consistent in some plates. The conclusion is that a
to the self-shielding effect. In the latter case, edge-on loading, the                                     mass transfer has occurred from A to B, facilitated by ﬁssion in-
ﬁssion density of the edge of the plate that was closer to the ATR                                         duced creep in the fuel as a response to an applied stress.
core is higher, as is illustrated in Fig. 4. The power ratio of the high
power edge to the low power edge is about 2.5 for HEU plates and
about 2 for LEU plates of RERTR-6, as determined in neutron phys-                                          4. ABAQUS simulation
ics analyses [5,6].
    After irradiation, the plates were sectioned at the axial mid-                                         4.1. Input data
plane. The fuel cross section was metallographically examined as
shown in Fig. 4.                                                                                              A Young’s modulus of 66 GPa and a Poisson’s ratio of 0.34 for
                                                                                                           AA6061 cladding were taken from [7]. Yield strength of the tem-
                                                                                                           pered Al alloys increases to 280 MPa due to irradiation hardening
3. Post-irradiation analysis
                                                                                                           [1]. This datum was used for the cladding considering the heat pro-
                                                                                                           cesses during and post fabrication: hot rolling process for plate fab-
    As mentioned earlier, fuel swelling in a plate results only in a
                                                                                                           rication and autoclaving for oxide pre-ﬁlming. Strain hardening was
plate thickness increase because the cladding is relatively unre-
                                                                                                           taken into account and a strain hardening exponent of 0.13 for
strained in the thickness direction. Therefore, once the post-
                                                                                                           AA6061-T6 [8] was applied to the cladding with consideration of a
irradiation foil thickness is known, total fuel swelling can be
                                                                                                           decreased potential of the strain hardening by neutron irradiation.
quantiﬁed using the following equation:
                                                                                                              A Young’s modulus of U–Mo fuel of 85 GPa and Poisson’s ratio of
 
 DV    Dt f                                                                                                0.34 were used for U–Mo alloy [9]. Yield strength of U–Mo was not
      ¼ f                                                                                        ð1Þ       needed in the simulation.
 V0 f   t0
                                                                                                              Fission-induced creep of U–Mo is dependent on the applied
where Dtf is foil thickness change after irradiation, and tf0 is the as-                                   stress and ﬁssion rate. Thermal creep was not considered because
fabricated foil thickness.                                                                                 the temperature regime of interest is so low that this phenomenon



                                                         Thickness                           ATR core
                                                                      Width                  (Face-on loading)

                                                                         Length                                                               Coolant



                                                                                                                                                        Plate
                                                                                                                                                        bottom



                                                                                                     Section for metallography
                                                                          ATR core                   at plate mid-plane in length direction
                                                                          (Edge-on loading)

                                                                   Fig. 4. Schematic showing plate loading directions and PIE location.
40                                                                                                Y.S. Kim et al. / Journal of Nuclear Materials 437 (2013) 37–46


Table 2                                                   
Fuel swelling comparison between measured and calculated, DVV0 (%).
                                                                                                           f

       Distance from foil enda (mm)                                           0        0.5   1      1.5        2        2.5   3    3.5      4      4.5   5    5.5   6    6.5   7    7.5    8     8.5     9    9.5
       L1F040                                             M                    0        7    17     22         28       29    28   25       23     21    21   19    19   19    19   17     17    16      16   15
                                                          C                   21       19    19     18         17       16    16   15       15     14    14   14    13   13    13   12     12    12      12   12
       L1F100                                             M                    0       10    17     26         31       31    31   29       27     21    25   23    23   22    17   19     19    18      18   16
                                                          C                   26       25    24     23         22       21    21   20       19     19    18   18    18   17    17   17     17    16      16   15
       L2F030                                             M                    0        8    14     20         24       24    22   20       18     17    16   15    14   13    13   13     12    12      12   11
                                                          C                   17       16    16     15         14       14    14   13       13     12    12   12    12   11    11   11     11    10      10   10
       L1F140                                             M                    0       28    45     55         59       60    56   48       42     38    35   33    30   30    29   29     27    27      25   24
                                                          C                   65       58    52     48         45       42    40   38       36     34    33   32    30   29    28   27     26    26      25   24
       L2F040                                             M                    0        9    18     25         29       30    29   26       24     22    21   20    20   19    19   19     17    17      17   16
                                                          C                   35       31    28     26         25       23    22   21       20     19    18   18    17   16    16   15     15    15      14   14
       H1P010                                             M                    0       23    45     60         70       70    70   60       60     53    50   48    45   43    40   40     38    38      38   38
                                                          C                   75       67    61     55         52       49    47   44       42     40    39   39    37   35    34   32     32    31      30   29
       L1P04A                                             M                    0       20    45     56         63       64    63   59       52     45    38   35    33   31    30   29     27    26      25   23
                                                          Mb                   0       11    21     26         28       30    29   27       24     23    23   22    21   21    21   21     21    21      22   23
                                                          C                   71       65    59     54         49       45    42   39       37     35    33   32    31   29    28   28     27    26      25   25
                                                          Cb                  21       21    20     20         20       20    20   20       20     20    21   21    21   22    22   23     23    24      24   25
       L1F26C                                             M                    2       18    37     57         70       74    76   75       71     65    57   53    49   45    41   37     36    35      34   33
                                                          C                   76       68    63     59         56       53    50   48       46     44    42   40    39   38    37   36     34    34      33   32
       L1F32C                                             M                    0       21    42     58         70       75    77   75       71     62    55   50    45   42    39   37     35    33      32   32
                                                          C                   72       67    62     58         54       51    48   46       44     42    40   39    38   36    35   35     34    33      32   32
       L1F34T                                             M                    0       25    46     64         77       80    80   76       73     68    63   57    52   50    47   45     42    40      40   39
                                                          C                   98       89    82     76         70       66    62   58       55     53    51   49    47   46    44   43     42    41      40   39
       L1P05A                                             M                    0       21    42     56         67       71    73   73       69     63    58   52    48   44    42   39     37    35      33   32
                                                          Mb                   0       13    25     31         32       33    32   31       30     29    29   28    28   28    29   30     30    31      31   32
                                                          C                   91       81    73     67         62       58    55   52       49     47    45   43    41   40    39   37     36    35      34   33
                                                          Cb                  28       27    27     27         27       27    27   27       27     27    27   28    28   28    29   30     30    31      34   33
       L1P09T                                             M                     5      37    64     76         88       90    88   86       80     74    70   66    62   60    56   49     47    45      43   41
                                                          C                   104      95    87     81         75       70    66   63       60     57    55   53    51   50    48   47     46    45      44   43
       L1P12Z                                             M                    8       30    52     61         68       62    58   53       47     43    37   37    33   31    28   25     25    22      22   20
                                                          Mb                   0        7    16     21         21       21    20   18       18     18    19   18    19   19    20   21     21    21      21   20
                                                          C                   72       65    59     54         49       46    42   40       37     35    33   32    31   29    28   28     27    26      25   25
                                                          Cb                  21       21    20     20         20       20    20   20       20     20    21   21    21   22    22   23     23    24      24   25
       L1P755                                             M                   15             45                52             43            37           32         30         27          26            25
                                                          Mc                  12             38                42             38            28           27         25         25          25            24
                                                          C                   50             43                38             35            32           30         29         28          27            27
                                                          Cc                  42             36                31             29            27           26         26         26          26            26

 M: Measured.
 C: Calculated.
 a
   Distance from higher power side of foil end.
 b
   Distance from lower power side of foil end.
 c
   Distance from the opposite end of the foil in the face-on loaded plate.



                                                                                                                                         is inactive. It is accepted in the literature that the ﬁssion-induced
                                                                                                                                         creep rate is linearly proportional to the ﬁssion rate. In some case,
                                 80
                                                                                                                                         a stronger stress dependence was employed such as e_ c  r1:5 for
                                 70
                                                                                                                                         UO2 [10]. However, as Dienst noted [11], a linear stress depen-
                                                                                                      Measured                           dence is most frequently used because it is easy to standardize




     Fuel swelling (ΔV/V0)f, %
                                                                                                      Calculated
                                 60                                                                                                      experimental data with good accuracy. Hence, the following equa-
                                          A           B                                                                                  tion has been adopted for the U–Mo creep rate:
                                 50
                                                                                                                                         e_ c ¼ Arf_                                                            ð2Þ
                                 40
                                                                                                                                         where e_ c is the equivalent creep strain rate (s1), A the creep rate
                                 30                                                                                                      coefﬁcient (cm3/MPa), r the equivalent stress (MPa), and f_ the ﬁs-
                                                                                                                    D                    sion rate (ﬁssions/cm3 s).
                                 20
                                                                                                                              C
                                                                                                                                            The total fuel swelling (i.e., swelling by ﬁssion gas bubble and
                                                                                                                                         swelling by solid ﬁssion products) correlation is available from[1] :
                                 10                                                                                                       
                                                                                                                                          DV
                                 0
                                                                                                                                               ¼ 5:0f d ;     for f d 6 3  1021 fissions=cm3                   ð3Þ
                                                                                                                                          V0 f
                                      0       1   2   3       4   5   6   7       8   9 10 11 12 13 14 15 16 17 18 19
                                                          Distance from core side fuel end, mm                                            
                                                                                                                                          DV
                                                                                                                                               ¼ 15 þ 6:3ðfd  3Þ þ 0:33ðfd  3Þ2 ;       for 3  1021
Fig. 5. Comparison between measured and calculated fuel swelling for L1P04A                                                               V0 f
plate.
                                                                                                                                                   < fd fissions=cm3                                            ð4Þ
                                                       Y.S. Kim et al. / Journal of Nuclear Materials 437 (2013) 37–46                                                  41




                                                                         50 μm                                                       50 μm




                                         Foil end region (high stress)                           Peak thickness region (low stress)
                                         Average pore size ~1.9 μm                               Average pore size ~2.0 μm

                                               Fig. 6. Optical micrographs showing ﬁssion gas pore morphology of L1P09T.


where fuel swelling is in percent and fd is in 1021 f/cm3. Note that                         The EOL condition of the plate L1P04A, which was irradiated
the temperature effect is neglected in these equations for the fol-                      with edge-on loading and had the same cladding thickness on both
lowing reasons. At the low temperature regime (<250 °C), ﬁssion                         faces, was simulated. For this case, only the upper half of the fuel
gas diffusion is predominantly initiated by ﬁssion enhanced diffu-                       plate was modeled by symmetry. A schematic of fuel plate cross-
sion (FED) and the amount of thermally activated gas diffusion is                        section and the FEA modeling scheme are shown in Fig. 7.
small. Also at these low temperatures, the decomposition of the                              CPEG8R, generalized plane strain 8-node biquadratic quadrilat-
as-fabricated meta-stable c phase to the a + c0 phases is very slow                      eral with reduced integration, was used. A geometrically nonlinear
and ﬁssion induced diffusion effectively reverse the a + c0 phases                       analysis was applied to make more precise analysis based on the
to the c phase [12,13]. Because of the c phase that has small gas                        geometry in the most recently completed increment. Again, bond-
bubble size, temperature effect on fuel swelling is small to the ex-                     ing between fuel and cladding was assumed intact throughout life,
tent difﬁcult to discern masked by measurement uncertainties [1].                        which is inaccurate in some cases where debonding occurs.
   Fuel true strain is derived from fuel swelling given in Eqs. (3)                          FEA simulation was performed for ﬁssion product induced fuel
and (4) as follows:                                                                      swelling together with creep in L1P04A using several A values, and
            "                                                                            the best simulation was found when A = 500  1025 cm3/MPa, as
                   #
                   DV                                                                    shown in Fig. 8. The fuel swelling simulation plotted in Fig. 8a shows
ef ;true ¼ ln 1 þ                                                              ð5Þ
                                                                                         fair simulation of the swelling peaks at both fuel ends. As the creep
                   V0 f
                                                                                         coefﬁcient increases, the peaks move toward the foil width center,
                                                                                         and their apices become closer to the measured. Fitting becomes
                                                                                         worse again when A is increased above 500  1025 cm3/MPa. How-
4.2. Simulation for creep rate coefﬁcient
                                                                                         ever, the uncertainties involved in the fuel swelling and the small
                                                                                         difference from the case with A = 250  1025 cm3/MPa suggest that
   The creep rate coefﬁcient A in Eq. (2) was obtained by simula-
tion of the U–Mo creep using ABAQUS FEA simulation.


                                                                                                                         Unit: mm

                                                                           Al-alloy cladding

                                                                             U-Mo fuel                                        0.25      1.4




                                                                                 19
                                                                                 25
                                                                                 (a)




                                                                                                                                      0.127

                                                                                 (b)
Fig. 7. Finite element modeling for L1P04A with edge-on loading and symmetric cladding thickness. (a) Schematic of fuel plate cross section and (b) ﬁnite element modeling.
42                                                                                 Y.S. Kim et al. / Journal of Nuclear Materials 437 (2013) 37–46


                                                                          80
                                                                                                                                        Measured
                                                                          70
                                                                                                                                        A=2.5
                                                                          60
                                                                                                                                        A=125




                                                      Fuel swelling, %
                                                                          50                                                            A=250

                                                                          40                                                            A=500

                                                                          30

                                                                          20

                                                                          10

                                                                           0
                                                                               0                   5                 10                15
                                                                                            Distance from core side fuel end, mm
                                                                                                                    (a)

                                                       10000
                                                                                           A=2.5            A=125             A=250             A=500
                                                                1000




                                             Stress, MPa
                                                                         100


                                                                         10


                                                                           1


                                                                         0.1
                                                                               0                   5                 10                 15
                                                                                            Distance from core side fuel end, mm
                                                                                                                    (b)
                                                                                          Thickness
                                                                                                                                                        1 mm
                           Magnitude of creep strain                                                   Width




                                                                                                                    (c)
Fig. 8. Finite element simulation results to ﬁt creep rate coefﬁcient using the measured data for L1P04A. (a) Fitting of the fuel swelling by using different creep rate
coefﬁcients A (in 1025 cm3/MPa), (b) Von Mises stress corresponding to the creep rate coefﬁcient used in (a), and (c) Contour of fuel volume expansion by the combination of
fuel swelling and creep-induced mass transfer from the foil end region to the foil width central region.




the obtained creep rate constant should also include considerable                                                    the foil central region in L1P04A is shown in Fig. 8c. The FEA sim-
uncertainty although it is difﬁcult to quantify.                                                                     ulation also implies that fuel volume increase by ﬁssion product-
   The corresponding Von Mises stresses for the fuel swelling gi-                                                    induced fuel swelling at the foil end region is effectively removed
ven in Fig. 8a are plotted in Fig. 8b. It is considered that the stresses                                            and accumulated instead at the region showing peak foil thickness.
obtained with A = 500  1025 cm3/MPa is reasonable. The stress                                                      Fuel ﬂow is the highest at the foil thickness centerline and the low-
becomes zero at the foil end to satisfy the traction free boundary                                                   est at the foil–cladding interface where the fuel is assumed to be
condition. It is also worth noting that the stress at the fuel central                                               perfectly bonded with the cladding.
region in the width direction becomes smallest. The wave nature in                                                       The driving force for the mass transfer is provided by shear
stress suggests that this uneven stress state may be the major driv-                                                 stress in the foil width direction. The evolution of the shear stress
ing force to cause separation of fuel foil from cladding (i.e., debond-                                              at the foil–cladding interface in the thickness direction was calcu-
ing) during irradiation observed in some plates.                                                                     lated at BOL, MOL and EOL and shown in Fig. 9. The shear stress in-
   The simulation result of the combination of ﬁssion product in-                                                    creases as ﬁssion product induced fuel swelling increases. As a
duced fuel swelling and fuel mass transfer from the foil end to                                                      result, mass transfer increases.
                                                                             Y.S. Kim et al. / Journal of Nuclear Materials 437 (2013) 37–46                                    43


                                                         Width center                                          4.3. Validation of FEA simulation

                                                                                                                   The creep rate coefﬁcient obtained in the previous subsection
                             5
                                                                                                               A = 500  1025 cm3/MPa and the FEA simulation results were val-
                             4                                                                                 idated by applying this value in the simulation for other plates.
                             3                                                                                 Among the measured plates given in Table 2, three plates with dif-
                                                                                                               ferent fabrication geometry and plate loading direction were




        Shear stress, MPa
                             2
                                                                                                               selected.
                             1                                                                                     L1P04A and L1P05A had symmetric cladding thickness on both
                             0
                                                                                                               plate sides and edge-on loaded. FEA simulation was performed for
                                                                                                               L1P05A using the creep rate coefﬁcient A = 500  1025 cm3/MPa.
                            -1                                                                                 The FEA result is in reasonable agreement with the measurement
                            -2                                                                                 (Fig. 10), although the simulated apex at the core side of L1P05A
                                                                                          BOL                  exhibits a slight discrepancy with the measurement.
                            -3
                                                                                          MOL                      L1P12Z was inadvertently fabricated with different cladding
                            -4                                                            EOL                  thickness on each side. FEA simulation was made for L1P12Z, using
                            -5                                                                                 A = 500  1025 cm3/MPa, to include the effect of the asymmetric
                                 0     2     4       6      8       10     12     14     16      18            cladding thickness. The schematic of fuel cross section and the fuel
                                           Distance from core side fuel end, mm                                FEA modeling scheme are shown in Fig. 11. As shown in Fig. 12a,
                                                                                                               the FEA result is in excellent agreement with the measured fuel
Fig. 9. Calculated shear stress at the foil–cladding interface at three points in                              swelling. Fuel deformation obtained by FEA shown in Fig. 12b oc-
irradiation time of L1P04A. The signs are opposite across the center in the width
direction due to direction change.
                                                                                                               curs dominantly on the thin cladding side of the plate compared
                                                                                                               to the thick side, which is in accord with the metallography shown
                                                                                                               in Fig. 12c.
                      100                                                                                          L1P755 from the RERTR-12 test is a face-on loaded. This loading
                                                                Predicted with swelling correlation            scheme was employed to provide a more uniform power distribu-
                            90                                  Predicted with FEA                             tion across the plate width. As shown in Fig. 13a, however, gamma
                            80                                  Measured                                       scanning during PIE showed that power peaking still exists
                            70                                                                                 although less than the edge-on loaded plates. The FEA simulation




  Fuel swelling, %
                                                                                                               result for L1P755, using A = 500  1025 cm3/MPa shown Fig. 13b
                            60                                                                                 compares the FEA simulation result with the measured fuel swell-
                            50                                                                                 ing and the calculated fuel swelling without considering creep, in
                                                                                                               which the FEA simulation is consistent with the measurement.
                            40

                            30

                            20                                                                                 5. Discussion
                            10
                                                                                                                  The consistent FEA simulations with the measured data for
                             0                                                                                 L1P05A, L1P12Z and L1P755 using the creep rate coefﬁcient
                                 0 1   2   3 4   5   6 7    8   9 10 11 12 13 14 15 16 17 18 19
                                           Distance from core side fuel end, mm                                A = 500  1025 cm3/MPa in general implies that the fuel mass
                                                                                                               transfer is indeed enabled by a creep mechanism and that ABAQUS
Fig. 10. Comparison of the predicted fuel swelling by FEA to the measured swelling                             FEA is applicable in simulation of the ﬁssion induced creep ob-
of plate L1P05A. The predicted fuel swelling by the empirical correlation is also                              served for A = 500  1025 U–Mo alloy fuel regardless of fuel plate
provided as a reference.                                                                                       fabrication and loading types. ABAQUS FEA also demonstrates that



                                                                                                                                        Unit: mm
                                                                                                 Al-alloy cladding
                                                                                                                                                          0.7
                                                                  0.25                            U-Mo fuel                                    0.202

                                                                                                                                                          0.7

                                                                                                         19
                                                                                                         25
                                                                                                        (a)



                                                                                                                                                       0.254




                                                                                                        (b)
Fig. 11. Finite element modeling for L1P12Z with edge-on loading and asymmetric cladding thickness on each side. (a) Schematic of fuel plate cross section and (b) ﬁnite
element modeling.
44                                                                         Y.S. Kim et al. / Journal of Nuclear Materials 437 (2013) 37–46


                                                                   100
                                                                                                         Predicted with swelling correlation
                                                                   90                                    Predicted with FEA
                                                                   80                                    Measured

                                                                   70




                                                Fuel swelling, %
                                                                   60

                                                                   50

                                                                   40

                                                                   30

                                                                   20

                                                                   10

                                                                    0
                                                                         0 1 2 3 4 5 6 7             8   9 10 11 12 13 14 15 16 17 18 19
                                                                                  Distance from core side fuel end, mm
                                                                    (a) Comparison of the predicted fuel swelling by FEA to the
                                                                    measured swelling of plate L1P12Z. The predicted fuel swelling
                                                                    by the empirical correlation is also provided as a reference.


                                                               0.16

                                                               0.14                                                            Top
                                                                                                                               Bottom
                                                               0.12




                                   Displacement, mm
                                                               0.10

                                                               0.08

                                                               0.06

                                                               0.04

                                                               0.02

                                                               0.00
                                                                         0 1 2 3 4 5 6 7             8    9 10 11 12 13 14 15 16 17 18 19
                                                                                   Distance from core side fuel end, mm
                                                                             (b) Fuel displacements for both halves of the foil.

                                                                                                               Al-alloy Cladding               U-10Mo foil




                             L1P12Z-C1
                             Zr-layer
                             U-10Mo HIP

                              500 μm



                              (c) Optical micrograph of cross section of L1P12Z in the width direction

                                                                          Fig. 12. Finite element analysis results and PIE data of L1P12Z.




not only the obtained creep rate constant is acceptable, but also the                                         lies between values of pure uranium and MOX, and is about a half
FEA modeling itself is valid in simulating the measured data.                                                 of the value of pure U. The slightly lower creep rate of the U–10Mo
   Fission enhanced creep at low homologous temperatures was                                                  compared to pure U is most likely due to its higher strength com-
reported for all uranium fuels and was ﬁrst identiﬁed in a-U in                                               pared to the pure U.
the 1950s by Russian [14] and British [15] workers, and subse-                                                    The high creep rate enables the extent of observed fuel lateral
quently in ceramic fuels by various researchers [11,16–22]. Com-                                              mass transfer, which is the effective mechanism that lessens the
mon for all, the creep rate was found to be athermal having a                                                 stresses caused by ﬁssion product induced fuel swelling at the foil
linear dependence on the applied stress and ﬁssion rate, as in Eq.                                            end region where peak ﬁssion density is usually achieved. This
(2). The obtained creep rate coefﬁcient cm3/MPa is compared with                                              mechanism allows U–Mo fuel to achieve high burnup without fail-
other U-fuels in the literature at homologous temperatures relative                                           ure, by reducing the potential to plate buckling due to lateral stres-
to their melting points in Table 3. The obtained value for U–10Mo                                             ses induced by fuel swelling. The high creep rate can also explain
                                                                                           Y.S. Kim et al. / Journal of Nuclear Materials 437 (2013) 37–46                                        45


                                            2.0                                                                                  The rather large increase in local fuel loading at the peak thick-
                                                                                                                             ness location resulting from the lateral fuel creep may have to be




  Transverse power peaking factor
                                                                                                                             considered for hot-spot calculations for reactors that operate fuel
                                                                                                                             at high power after substantial burnup. The additional plate thick-
                                            1.5
                                                                                                                             ness increase by creep in addition to ﬁssion product induced fuel
                                                                                                                             swelling at the peak thickness location must be incorporated in
                                                                                                                             safety analyses. The additional foil thickness increase by creep is
                                            1.0                                                                              25% from the as-fabricated foil thickness at a ﬁssion density of
                                                                                                                             7  1021 f/cm3, which may be considerable in a safety analysis.
                                                                                                                                 In the FEA analyses performed in this study, we used life-
                                                                                                                             averaged ﬁssion rates instead of the time-dependent ones given
                                            0.5
                                                                                                                             in Fig. 3 for the ease of calculation. The validity of this simplistic
                                                                                                                             approach was examined. Fission induced creep is a product of
                                                                                                                             stress and ﬁssion rate; however, the stress is more important be-
                                            0.0                                                                              cause it provides the driving force and the ﬁssion rate determines
                                                  0              5                10               15
                                                                                                                             amplitude of the creep rate. The stress is produced by the ﬁssion
                                                          Distance from higher power foil end, mm                            product induced fuel swelling, which is a function of ﬁssion den-
                                                         (a) Power peaking factors in the foil width                         sity. The total creep strain is a time integration of the creep rate gi-
                                                              direction measured by gamma scan                               ven in Eq. (2). Therefore, the case with the time-dependent ﬁssion
                                                                                                                             rate has higher ﬁssion density in early life than the average-ﬁssion
                                             60                                                                              rate case because the ﬁssion rate decreases with burnup in all of
                                                                               Predicted with swelling correlation           the tests, except for RERTR-9A. FEA simulation for L1F140 at mid-
                                                                               Predicted with FEA                            dle of life (MOL) compares the two cases in Fig. 15. The fuel swell-
                                             50                                Measured                                      ing at peak thickness location was slightly (2%) larger for the
                                                                                                                             time-dependent ﬁssion rate case, whereas no difference was found




                         Fuel swelling, %
                                             40                                                                              at EOL between the two cases. This result is undoubtedly due to the
                                                                                                                             linear stress on ﬁssion rate dependence of the creep rate.
                                             30                                                                                  Studies of the effect of porosity on thermal creep are available
                                                                                                                             in the literature (see for example [23]). Porosity typically enhances
                                                                                                                             the thermal creep rate. Since ﬁssion gas pores are formed in U–Mo,
                                             20
                                                                                                                             the porosity effect may be important for a more accurate analysis.
                                                                                                                             Porosity in some high burnup U–Mo plates becomes considerable,
                                             10                                                                              greater than 10%. Hayes et al. [23] estimated that 12% augmenta-
                                                                                                                             tion in the creep rate was needed at this porosity in UO2. Unlike
                                              0                                                                              thermal creep, however, for which the exponent of the stress term
                                                  0 1   2 3 4       5 6   7 8 9 10 11 12 13 14 15 16 17 18 19
                                                                                                                             ranges 3–4, the porosity effect for ﬁssion induced creep is smaller
                                                          Distance from higher power fuel end, mm
                                                                                                                             because the exponent for the stress term is one. For this reason, a
                                                        (b) Comparison of the calculated fuel swelling                       detailed study to accurately factor in this effect is not explored in
                                                        by FEA to the measured swelling. The predicted fuel                  this study. Nonetheless, it should be noted that the constant creep
                                                         swelling by the empirical correlation is also                       rate coefﬁcient A employed in this study is simplistic. A burnup
                                                         provided as a reference.                                            dependent creep rate coefﬁcient is more appropriate particularly
                                                                                                                             at high burnup when porosity increases considerably by ﬁssion
Fig. 13. Power distribution across foil width and FEA analysis results for plate
L1P755.
                                                                                                                             gas bubbles.
                                                                                                                                 The temperature effect has not been considered in the FEA per-
                                                                                                                             formed in this study, which follows the ﬁndings reported in litera-
                                                                                                                             ture [11,14–22]. The temperatures of the plates analyzed in this
Table 3
                                                                                                                             work are narrowly bounded between 110 and 190 °C (Table 1).
Creep rate coefﬁcient (A) in Eq. (2).                                                                                        This low and narrow range of temperatures is the prerequisite
                                                                                                                             for athermal creep.
           Fuel                                               A (1025 cm3/MPa)        T/Tm            Reference
                                                                                                                                 An implication from this work that affects the measurement of
           U                                                  800                      0.3              [14,17]              ﬁssion product induced fuel swelling is that one must avoid mea-
           U–10Mo wt.%                                        500                      0.3              Present study
           MOX                                                 56                      0.25             [18]
                                                                                                                             suring it at or near the foil end regions. Measurements at these re-
           UO2                                                  7                      0.25             [11,19,20]           gions will lead to erroneous results affected by fuel lateral mass
           UN                                                   3                      0.3              [21,22]              transfer.
           UC                                                   1                      0.3              [20]

T = test temperature, Tm = melting point.
                                                                                                                             6. Conclusions

the extent of fuel particle deformation observed in high burnup                                                                 The taper of U–Mo fuel foil observed at the foil width end re-
dispersion fuel plates shown in Fig. 14, in which the spherical U–                                                           gion, where ﬁssion density is highest, has been reviewed. The
Mo particles, when they were as-fabricated, underwent signiﬁcant                                                             underlying mechanism is lateral mass transfer by ﬁssion induced
deformation during irradiation although deformation of fuel parti-                                                           creep, which is athermal and dependent on ﬁssion rate and stress
cles can also occur to some extent during production of the parti-                                                           that builds up by ﬁssion product induced fuel swelling in the area.
cles and plate fabrication. This plate also shows sintering between                                                          The creep of U–Mo fuel is the effective mechanism that lowers the
particles. The analysis of creep behavior of the dispersion fuel                                                             stresses at the foil end region where ﬁssion product induced fuel
plates is not pursued in this work.                                                                                          swelling is the highest because of peak ﬁssion density there, which
46                                                                      Y.S. Kim et al. / Journal of Nuclear Materials 437 (2013) 37–46


                                                                 Al matrix                                U-Mo alloy particle




                                Fig. 14. Optical micrograph of the fuel meat end region of R6R018 where the meat-averaged ﬁssion density is 10  1021 f/cm3-fuel-particle.



                                                                                                          operations staff at ATR is also acknowledged for the irradiation
                        30                                                                                tests. The physics data available by Dr. G. Chang and Ms. M. Lillo
                                                               With life-averaged power                   are also appreciated. One of the authors (Y.S. Kim) thanks Mr.
                                                               With power history                         Y.S. Choo of KAERI for the measurement of pore sizes used in
                        25
                                                                                                          Fig. 6 and Ms. S.H. Kim for the review of the manuscript. This work
                                                                                                          was supported by the U.S. Department of Energy, Ofﬁce of Global




     Fuel swelling, %
                        20
                                                                                                          Threat Reduction (NA-21), National Nuclear Security Administra-
                                                                                                          tion, under Contract No. DE-AC-02-06CH11357 between UChicago
                        15                                                                                Argonne, LLC and the Department of Energy.

                        10                                                                                References

                                                                                                           [1] Y.S. Kim, G.L. Hofman, J. Nucl. Mater. 419 (2011) 291.
                         5                                                                                 [2] G.L. Hofman, Y.S. Kim, A.B. Robinson, in: Trans. 13th Internat. Topical Meeting
                                                                                                               Research Reactor Fuel Management (RRFM), RRFM 2009, Vienna, Austria,
                                                                                                               March 22–25, 2009. <http://www.euronuclear.org/meetings/rrfm2009/
                         0                                                                                     index.htm>.
                             0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19                             [3] ABAQUS Analysis User’s Manual, Dassault Systems, 2011.
                                      Distance from core side fuel end, mm                                 [4] C.R. Clark, J.M. Wight, G.C. Knighton, G.A. Moore, J.F. Jue, in: The 27th
                                                                                                               International Meeting on Reduced Enrichment for Research and Test Reactors
Fig. 15. Comparison of FEA results for fuel swelling between the cases with the                                (RERTR), Boston, Massachusetts, November 6–10, 2005. <http://
time-dependent ﬁssion rate and life-average ﬁssion rate at MOL for fuel plate                                  www.rertr.anl.gov/RERTR27>.
L1F140.                                                                                                    [5] M.A. Lillo, MCNP-Calculated Gradients Across RERTR-6 and RERTR-7
                                                                                                               Miniplates Irradiated in ATR, Interofﬁce Memo, INL, 2007.
                                                                                                           [6] G.S. Chang, M.A. Lillo, As-Run Neutronics Analysis of the RERTR-9A/B Capsules
                                                                                                               in the ATR B 11 Position, Engineering Calculations and Analysis Report-231,
                                                                                                               2008.
enables U–Mo alloy fuel to achieve high burnup without failure. It                                         [7] J.S. Cheon, Y.S. Kim, Material Properties of Aluminum Alloys and Pure
also provides a realistic explanation for the observed anisotropic                                             Zirconium for Use in High-density Fuel Development for Research Reactors,
                                                                                                               ANL/RERTR/TM-12-6, 2012.
swelling in the fuel plates.                                                                               [8] Y. Tamarin, Atlas of Stress–Strain Curves, Materials Park, Ohio, ASM
   ABAQUS ﬁnite element analysis (FEA) simulation coupled with                                                 International, 2002.
a model for ﬁssion product induced fuel swelling and creep, pro-                                           [9] A.M. Nomine, D. Bedere, D. Miannay, Grandeur, Mecaniques zassociées à la
                                                                                                               corrosion sous contrainte de I’alliage U–10Mo’’, paper presented at the
duced consistent results using the measured fuel swelling data                                                 Coloque sur la rupture des materiaux, Grenoble, 9–21 January, 1972.
for all fuel plate types and loading schemes with physical–                                               [10] D. Brucklacher, in: Proc. Intern. Conf. CEBG Berkeley, Metals Soc. London, 1974.
mechanical data available in the literature. This proves that the                                         [11] W. Dienst, J. Nucl. Mater. 65 (1977) 1.
                                                                                                          [12] M.L. Bleiberg et al., J. Appl. Phys. 27 (11) (1956) 1270.
fuel mass transfer is indeed induced by a creep mechanism and                                             [13] M.L. Bleiberg, J. Nucl. Mater. 2 (1959) 182.
validates that ABAQUS FEA is applicable in simulation of the ﬁssion                                       [14] S.T. Konobeevsky, N.E. Pravdyuk, V.I. Kutaitsev, in: UN Int’l Conf. Peaceful Use
induced creep observed for U–Mo alloy fuel.                                                                    of Atomic Energy, Geneva, Switzerland, Paper No. 681, 1955.
                                                                                                          [15] A.C. Roberts, A.H. Cottrell, Phil. Mag. 1 (1956) 711.
   ABAQUS simulation also produced the best-ﬁt creep rate con-
                                                                                                          [16] A.S. Zaimovsky, in: UN Int’l Conf. Peaceful Use of Atomic Energy, 1958.
stant for U–10Mo alloy fuel 500  1025 cm3/MPa, a value that is                                          [17] M. Hesketh, Discussion in Paper, in: M. Englander, C.T. Montpreville, eds., 11th
approximately a factor of two lower than that for pure uranium.                                                Colloque de Metallurgie, Creep, June 1967, Centre D’Etudes Nucleaires de
However, the obtained creep rate constant includes considerable                                                Saclay, 1968, p. 28.
                                                                                                          [18] R.J. White, The Re-Irradiation of MIMAS-MOX Fuel in IFA-629.1, HWR-586,
uncertainty, for which quantiﬁcation is not tried in this study.                                               March, 1999.
                                                                                                          [19] A.A. Solomon, J. Am. Ceram. Soc. 56 (1973) 164.
Acknowledgments                                                                                           [20] D.J. Clough, J. Nucl. Mater. 65 (1977) 24.
                                                                                                          [21] D. Brucklacher, W. Dienst, Proc. Am. Ceram. Soc., Anaheim, California, USA,
                                                                                                               November 1971.
   The authors would like to thank Mrs. C. Clark, G. Moore, and J.                                        [22] P. Zeisser, G. Maraniello, P. Combette, J. Nucl. Mater. 65 (1977) 48.
Jue for the fabrication of the plates used in this work. The                                              [23] S.L. Hayes, J.K. Thomas, K.L. Peddicord, Mater. Lett. 9 (1990) 435.
