# Extended fuel swelling models and ultra high burn-up fuel behavior of U-Pu-Zr metallic fuel using FEAST-METAL

---

                                                              Nuclear Engineering and Design 258 (2013) 26–34



                                                        Contents lists available at SciVerse ScienceDirect


                                                    Nuclear Engineering and Design
                                           journal homepage: www.elsevier.com/locate/nucengdes




Extended fuel swelling models and ultra high burn-up fuel behavior of U–Pu–Zr
metallic fuel using FEAST-METAL
Aydın Karahan ∗ , Nathan C. Andrews
Center for Advanced Nuclear Energy Systems, Nuclear Science and Engineering, Massachusetts Institute of Technology, 77 Massachusetts Avenue, 24-215, Cambridge, MA 02139,
United States




h i g h l i g h t s

 Improved fuel swelling models in phase structure dependent form.
 A probabilistic veriﬁcation exercise for the open porosity formation threshold.
 Satisfactory validation effort for available EBR-II database.
 Ultra high burn-up behavior of U–6Zr fuel with 60% smear density fuel.



a r t i c l e        i n f o                           a b s t r a c t

Article history:                                       Computational models in FEAST-METAL U–Pu–Zr metallic fuel behavior code have been upgraded to
Received 21 June 2011                                  improve ﬁssion gas, solid ﬁssion product swelling, and pore sintering behavior in a microstructure
Received in revised form 15 January 2013               dependent form. First, ﬁssion gas bubble growth is modeled by selecting small and large bubble groups
Accepted 1 February 2013
                                                       according to a ﬁxed number of gas atoms per bubble group. Small bubbles nucleated at phase bound-
                                                       aries grow via gas migration and turn into large bubbles. Furthermore, bubble morphology for each phase
                                                       structure is captured by selecting the number of atoms per bubble and the shape of the bubbles in a phase
                                                       dependent form. The gas diffusion coefﬁcients for the single gamma phase and effective dual (˛ + ı) and
                                                       (ˇ + ) phase structures are modeled separately, using the activation energy of the corresponding phase
                                                       structure. In this study, it is found that pressure sintering of the interconnected porosity in dual phases
                                                       should be less effective than the reference model in order to match clad strain and ﬁssion gas release
                                                       behavior. In addition to these improvements, a probabilistic approach is taken to verify the ﬁssion gas-
                                                       swelling threshold at which interconnected porosity begins. This fracture problem is treated as a function
                                                       of critical crack length formed via bubble coalescence. It was found that a 10% gas-swelling threshold is
                                                       appropriate for a wide range of gas bubble sizes. The new version of FEAST-METAL predicts the burn-up,
                                                       smear density, and axial variation of the clad hoop strain and ﬁssion gas release behavior satisfactorily
                                                       for selected test pins under EBR-II conditions. The code is used to predict ultra-high burn-up U–Pu–6Zr
                                                       vented metallic fuel behavior with HT9 cladding for fast breeder reactor applications for 20 years of
                                                       irradiation. It is assumed that HT9 clad will retain its fracture toughness and creep properties for this
                                                       simulation. It appears that the increased dose on the cladding, increased solid ﬁssion product swelling,
                                                       and low operating fuel temperature requires lower fuel smear density (∼60%) in order to ensure accept-
                                                       able clad hoop strain at high burn-up (∼35 at.%). Furthermore, keeping the peak clad temperature below
                                                       550 ◦ C seems to control lanthanide migration and clad inner wastage at a reasonable level. Possible design
                                                       concerns and improvements are discussed.
                                                                                                                           © 2013 Elsevier B.V. All rights reserved.




                                                                                       1. Introduction

                                                                                           Uranium–plutonium alloy fuel type with 6–10 wt.% zirconium
                                                                                       irradiated in EBR-II and FFTF reactors showed that it is a promising
                                                                                       candidate for fast reactor applications (Walters, 1999; Crawford
                                                                                       et al., 2007). It has high heavy metal density, high thermal con-
 ∗ Corresponding author.
                                                                                       ductivity, ease of fabrication and good compatibility with sodium
   E-mail addresses: karahan@alum.mit.edu, info@e-modeler.com (A. Karahan),
nandrews@mit.edu (N.C. Andrews).
                                                                                       coolant. It also has rather controllable fuel swelling and fuel clad

0029-5493/$ – see front matter © 2013 Elsevier B.V. All rights reserved.
http://dx.doi.org/10.1016/j.nucengdes.2013.02.004
                                         A. Karahan, N.C. Andrews / Nuclear Engineering and Design 258 (2013) 26–34                                 27


mechanical interaction behavior. On the other hand, one should                  for each radial node based on its temperature. Furthermore, the
also guard against fuel clad chemical interaction due to lanthanide             gas diffusion coefﬁcient is also modeled in phase dependent form
attack towards the clad inner surface. Today, this fuel type is sug-            considering the activation energy of each phase structure.
gested for use in the fast breeder (Weaver et al., 2009) and fast                   In addition to ﬁssion gas behavior, the sintering model for inter-
burner (Hoffman et al., 2006) reactor designs. Enabling ultra-high              connected open porosity is also updated in the current version. The
burn-up capability and the resulting self-sustained fuel cycle with             previous porosity sintering model was a ﬁt using the experimental
no enrichment or reprocessing requirement presents itself as an                 data generated for high temperature single gamma phase (Ogata
interesting target. This can also help resolve the rapidly grow-                and Yokoo, 1999). This study has found that the compressibility
ing energy problem without raising security concerns due to fuel                factor of dual phases should be much lower in order to match ﬁs-
enrichment or reprocessing issues.                                              sion gas release and clad strain behavior in a satisfactory manner.
    Because the available database is rather limited, extrapolating             In addition to modeling improvements, a veriﬁcation study has also
available databases accurately with science-based, semi-empirical               been performed for the threshold gas swelling parameter to pre-
and continuum level models is the key to designing the future                   dict the onset of open porosity formation. The benchmarking effort
nuclear systems. FEAST-METAL is a U–Pu–Zr fuel behavior code                    against selected tests from EBR-II database is described in Section
developed to predict steady state and transient performance of                  4. In Section 5, the code is applied to predict ultra-high burn-up
metallic fuels (Karahan, 2009). The code has 1D stress/strain and               metallic fuel behavior for sodium fast reactor conditions. For this
temperature distribution models. It is also equipped with mecha-                case, it is assumed that HT-9 clad will retain its fracture toughness,
nistic models for ﬁssion gas swelling and release, fuel constituent             creep and void swelling properties up to 500 dpa. The results are
migration, fuel clad chemical interaction and transient clad fail-              discussed and possible design improvements are suggested.
ure predictions. Furthermore, empirical models are included to
describe fuel creep and thermal expansion, sintering behavior                   2. Model improvements
of fuel porosity under applied stress, fuel thermal conductivity,
sodium logging into fuel porosity, HT9 clad irradiation and thermal             2.1. Fission gas model
creep, void swelling, and thermal expansion.
    The code’s ﬁssion gas behavior model is based on the GRSIS                      Several improvements have been made on ﬁssion gas module.
algorithm (Lee et al., 2001). It assumes bubbles can nucleate                   First, a constant atom number bubble grouping scheme is adopted.
isotropically within the fuel matrix. The fact that the fuel opera-             In this approach, gas bubbles are treated as two distinct groups as
tes above the half of the melting point and has phase boundaries,               the small and large bubble while each group has a ﬁxed number
which are nearly uniformly distributed within the grains, makes                 of gas atoms. Small bubbles nucleated isotropically grow via gas
the isotropic nucleation assumption acceptable. The ﬁrst version                diffusion towards this bubble type. As a result of this growth, a
of the code allows for bubble grouping based on the volume of                   fraction of them turn into large bubbles in each time step. Given
the bubble. Two groups of bubbles are allowed. Once nucleated,                  the hydrostatic stress and temperature, the radius of the each bub-
small bubbles grow via mainly gas diffusion towards bubbles and                 ble group is calculated using Van der Walls equation. The selected
turn into large bubbles. Above the threshold gas swelling, forma-               number of atoms for small bubbles and large bubbles are given in
tion of interconnected open porosity takes place. Interaction of the            Table 1 for each phase structure. By this way, the model approx-
open pores with closed bubbles leads to a rapid build-up of inter-              imates the observed behavior for bubble morphological evolution
connected porosity and ﬁssion gas release. Fission gas can escape               given in Fig. 1.
to the plenum via the interconnection of a closed bubble with                       The ﬁssion gas algorithm accepts only spherical geometry. In
open porosity or direct diffusion towards open porosity. Once ﬁs-               order to account for ellipsoid shape of bubbles in (˛ + ı) region, cor-
sion gas swelling saturates, solid ﬁssion product swelling lets the             rection factors are added for surface energy term in Van der Walls
fuel continue expanding. Typically, pressure sintering of the open              equation and also for bubble surface area term in order to capture
porosity under the applied contact pressure between the fuel and                the correct gas diffusion current towards ellipsoidal bubbles. Bub-
the cladding allows for solid ﬁssion products to build up without               ble growth and coalescence models are treated by using an effective
signiﬁcantly straining the cladding.                                            spherical geometry for ellipsoid bubbles.
    The current study changes the bubble grouping scheme in the                     The ﬁssion gas diffusion coefﬁcient is modeled in phase
GRSIS algorithm from constant volume to constant atom num-                      structure dependent form. Measured activation energy of the corre-
ber. Hence, small and large bubble groups have speciﬁc number                   sponding phase structure is adopted as given in Gruber and Kramer
of atoms. This approach has found more applications in model-                   (1987). Diffusion constants are taken as ﬁtting factors. The consti-
ing ﬁssion gas behavior in past studies (Tsuboi et al., 1992; Wood              tutive relations for dual phase and single gamma phase regions are
and Hayns, 1976). In addition to the bubble grouping scheme, the                given as follows:
morphological evolution of ﬁssion gas bubbles is modeled in phase                    ⎧                         
dependent form consistent with experimental observations given                       ⎨ 1.0 × 10−4 exp − 52, 000   T < T6
in Fig. 1 (Hofman et al., 1990). Fig. 1(a) is the typical bubble mor-           Dg =                  28,RT500 
phology at dual (˛ + ␦) phase, which typically occurs at the colder                  ⎩ 0.3 × 10−8 exp −           T > T6
                                                                                                                      RT
peripheral regions. Due to lack of thermal activation and inclusion
of stiff orthorhombic ˛ phase, the bubbles grow along the ˛/ı phase             Dg : gas diffusion coefﬁcient (m2 /s); T: temperature (K); R: gas
boundaries and take an ellipsoidal shape. Fig. 1(b) shows the bubble            constant = 1.987 Cal/mol/K; T6 : single gamma phase transition tem-
morphology of dual (ˇ + ␥) phase region. Again due to existence of              perature (K) (the value is 923 K for U–19Pu–10Zr fuel).
stiff tetragonal ˇ precipitates, bubbles remain small, on the order of              Note that sensitivity of the dual phase diffusion coefﬁcient on
a couple of microns, but this time the bubble shape is spherical. At            overall behavior is much higher compared to the single gamma
higher temperatures, the body centered cubic (BCC) single gamma                 phase diffusion coefﬁcient. A part of the reason is that the single
phase forms. Its softness favors existence of much larger bubble                gamma phase is compliant and the stiffer outer region tends to
sizes compared to dual phase regions. The size of large spherical               have a higher impact on ﬁssion gas release and swelling behavior
bubbles could be as much as 10 ␮m (Fig. 1(c)). In order to capture              of the fuel.
this behavior, the new version of FEAST-METAL speciﬁes the num-                     In addition to the ﬁssion gas diffusion constant, the open pore
ber of atoms per small and large bubbles in phase dependent form                formation coefﬁcient and open porosity surface area corrections
28                                                   A. Karahan, N.C. Andrews / Nuclear Engineering and Design 258 (2013) 26–34




               Fig. 1. Bubble morphology at (a) (˛ + ı) phase, (b) (ˇ + ) phase, (c) Single  phase (Hofman et al., 1990) (each ﬁgure spans approximately 4000 ␮m2 ).


are the remaining ﬁtting factors in the ﬁssion gas model as deﬁned                           overestimating the compressibility factor for dual and stiffer phase
in Karahan (2009). The open porosity formation coefﬁcient con-                               structures. Experimental work should be pursued to clarify this
trols the distance between the closed bubbles and interconnected                             issue. Nevertheless, decreasing the “C” factor for dual phases
open porosity; hence, the coalescence behavior of the closed bub-                            improves coupled fuel behavior predictions signiﬁcantly.
bles with the open porosity while closed bubbles are growing via
diffusion. Its value is taken as 0.4. The open porosity surface area                         2.3. Solid ﬁssion product swelling
correction factor controls the area of the open pores at which direct
gas diffusion and release can take place. Its value is taken as 0.3. Both                        As mentioned before, solid ﬁssion product swelling together
of these factors are adjusted in order to predict EBR-II experiments                         with hot pressing of the open porosity is very critical in capturing
in a satisfactory manner.                                                                    the fuel clad mechanical interaction behavior. The previous version
                                                                                             of FEAST-METAL assumed conservatively that the U–Pu–10Zr solid
2.2. Pressure sintering model                                                                ﬁssion product swelling rate is 1.5% per at.% burn-up (Ogata and
                                                                                             Yokoo, 1999; Kim and Hofman, 2003). The current study adopts
    Under the applied hydrostatic stress, open porosity, which is                            1.2% per at.% burn-up which is the best estimate value as given by
at plenum pressure, is assumed to be sintered in creep depend-                               Hofman et al. (1997). As a result, we believe the extrapolation abil-
ent form. Using the experimental data for hot isostatic pressing                             ity of the code especially for high burn-up and high residence time
(McDeavitt, 1992) at high temperature single gamma phase, Ogata                              conditions has increased. Note also that if the heavy metal den-
et al., derived an empirical model for pore compression in creep                             sity (or zirconium content) is different than the reference fuel, the
dependent form (Ogata and Yokoo, 1999). In their model, a com-                               swelling rate is corrected proportional to the heavy metal density
pressibility factor (˛) is deﬁned as a function of the open porosity                         of the fuel with respect to the reference fuel.
fraction present within the fuel. This factor plays an essential role
to assess fuel clad mechanical interaction behavior and predict the                          3. Veriﬁcation of the threshold swelling
amount of porosity the fuel has at a given time. In this study, the
model is extended to a phase dependent form and a correction                                    FEAST-METAL assumes that above the gas swelling threshold
factor “C” is added for dual phases as given below:                                          of 10%, formation of the interconnected open porosity begins; in
     ⎧                                                                                       other words, fuel fracture takes place. It is based on previous experi-
     ⎪ 0.0           εopn = 0
     ⎪
     ⎨ 1  εopn 1.5                                                                         mental work, which was performed at high temperature conditions
           C                    0 < εopn < 0.1                                               for single gamma phase region (McDeavitt, 1992). In this study,
˛=     6           0.1
     ⎪
     ⎪                                                                                       possible dependency of this parameter on bubble size is examined
     ⎩C1                        εopn > 0.1                                                   with a probabilistic approach. The aim is to correlate the threshold
               6
                                                                                             swelling with the critical crack length due to interconnection of
˛: open porosity compressibility factor; εopn : fuel open porosity                           the bubble chains. First, the experimental work given in McDeavitt
fraction; C: ﬁtting factor. It is taken as unity for single gamma phase                      and Solomon (1996) is simulated and crack length distribution is
and 0.23 for (˛ + ı) and (ˇ + ) dual phases.                                                calculated. Then, it is applied for a wide range of bubble sizes.
    Note again that experimental data is not available for hot                                  The model tracks the interconnected bubbles up to the point at
pressing behavior of the dual phases. The study raises the possi-                            which the scalar product of the crack vector between the starting
bility of the extrapolation performed by Ogata and Yokoo (1999)                              bubble pair and the last bubble pair becomes less than zero. As can

Table 1
Small and large bubble size and number of atoms per bubble.

 Phase structure                Small bubble atom number               Small bubble size/shape                  Large bubble atom number              Large bubble size/shape

 (˛ + ı)                        0.37E+7                                ∼0.2 ␮m × 0.2 ␮m × 0.05 ␮m               0.98E+10                              ∼7 ␮m × 7 ␮m × 1 ␮m
                                                                       Ellipsoidal                                                                    Ellipsoidal

 (ˇ + )                        0.20E+7                                ∼0.15 ␮m                                 0.54E+10                              ∼3 ␮m
                                                                       Spherical                                                                      Spherical

 Single                        0.75E+8                                ∼0.5 ␮m                                  0.2E+12                               ∼10 ␮m
                                                                       Spherical                                                                      Spherical
                                                            A. Karahan, N.C. Andrews / Nuclear Engineering and Design 258 (2013) 26–34                                                                             29


                                                                                                                                    8.00E+13
                                                    5




                                                                                                     Crack length density (m/m³)
                       1                                                 6                                                          6.00E+13
                                                             4
                                       2
                                                3                                                                                   4.00E+13


                                                                                                                                    2.00E+13
                  Fig. 2. Interconnected bubble chain (crack length).


                                                                                                                                    0.00E+00
                                                                              2                                                                  0         10            20            30        40              50
                                   2
                   1                                                                                                                                                 Crack length (μm)
                                                                 1
                               3
                                                                                                   Fig. 5. Crack length density distribution for the reference simulation at 10% gas
                                                                          3                        swelling.


                                                                                                                                     0.3
                               Fig. 3. Bubble separation strategy.



be seen in Fig. 2, the crack follows bubbles-1–4, and 6. The chain                                                                   0.2
starting with bubble-1 and ending at bubble-5 is not taken into
                                                                                                                              PDF
consideration because the vector between bubble 4 and bubble-                                                                                                                                         1.5 micron
5 changes its direction with respect to the vector between the                                                                       0.1                                                              6 micron
bubble-1 and bubble-2.
    Given the cumulative distribution function for the bubble
size distribution, the code generates bubbles randomly within a
                                                                                                                                         0
200 × 200 × 200 ␮m cube media with an applied periodic boundary
                                                                                                                                             0            10             20                 30
condition at boundaries. After that, the code assesses intercon-
                                                                                                                                                      Bubble Diameter (μm)
nected bubbles. The bubbles are separated from each other so that
they will be just touching each other as shown in Fig. 3. The code                                 Fig. 6. Probability distribution function for average bubble diameter of 1.5 and 6 ␮m.
records all connected bubble pairs. By tracking bubble pairs and
calculating the cosine in between, crack length density due to bub-
                                                                                                   critical crack-length density is reached, remains around 10%. One
ble coalescence is obtained. At the ﬁnal step, the code rejects the
                                                                                                   may assume that an average bubble diameter in the neighborhood
cracks that occupy any smaller size cracks.
                                                                                                   of 2 ␮m corresponds to the dual phase region and a diameter of
    The probability distribution function (PDF) given in McDeavitt
                                                                                                   4–6 ␮m corresponds to the single gamma phase region. At very
and Solomon (1996) for bubble size is shown in Fig. 4. The average
                                                                                                   low bubble sizes, an increase in threshold swelling above 10% is
bubble diameter is 2.7 ␮m. Bubbles are generated using this prob-
                                                                                                   observed. This may be due to the modeling assumption described in
ability distribution function up to 10% swelling. The resulting crack
                                                                                                   Fig. 2. Nevertheless, the calculation indicates that within the region
length density distribution (m/m3 ) is given in Fig. 5. The selected
                                                                                                   of interest, 10% threshold swelling for the onset of interconnected
criterion for critical crack length density at which fuel fracture takes
                                                                                                   porosity formation is a reasonable assumption. Accordingly, it is
place is taken as 1.5E+13 m/m3 and above 30 ␮m.
                                                                                                   kept the same in the new version of FEAST-METAL.
    By shifting the PDF to left and right (Fig. 6), the sensitivity of
the threshold swelling on bubble size is studied. Fig. 6 shows the
shifted PDF for 1.5 ␮m and 6 ␮m average bubble diameter.                                           4. Benchmarks
    The critical crack density is calculated for different bubble sizes.
As shown in Fig. 7, it was found that the threshold swelling, at which                               Benchmarking is accomplished using experimental data for
                                                                                                   X425 and X430 assemblies operated in EBR-II as described in

        0.3
                                                                                                                                    20
       0.25




                                                                                                    Threshold Swelling
        0.2                                                                                                                         15


 PDF   0.15
                                                                                                                                    10
        0.1

       0.05                                                                                                                          5

         0
              0            2               4            6            8            10     12                                          0
                                                                                                                                         1            2              3             4              5                6
                                           Bubble Diameter (μm)
                                                                                                                                                               Average Bubble Diameter (μm)
Fig. 4. Probability distribution function for bubble diameter for experimental work
given in McDeavitt and Solomon (1996).                                                                                             Fig. 7. Calculated threshold swelling as a function of average bubble size.
30                                                                            A. Karahan, N.C. Andrews / Nuclear Engineering and Design 258 (2013) 26–34


                                     a                                                 1.4 at %            End of Life          b                                                                       1.2 at %              End of Life
                                                                  800                                                                                                             800

                                  Fuel Centerline                 700                                                            Fuel Centerline                                  700



                                 Temperature (ºC)                                                                               Temperature (ºC)
                                                                  600                                                                                                             600

                                                                  500                                                                                                             500
                                                                        0                         0.5                    1                                                                 0                    0.5                     1
                                                                                      Normalized Axial Height                                                                                        Normalized Axial Height

Fig. 8. (a) Axial variation of the X425 fuel pin centerline temperature at low burn-up and at end of life; (b) axial variation of the X430 fuel pin centerline temperature at low
burn-up and at end of life.


                                                                             Closed Bubble                      Open Porosity                                                              Solid FP             Total Swelling

                                    a 50                                                                                                              b                           40




                                     Fuel Swelling (%)                                                                                                    Fuel Swelling (%)
                                                             40                                                                                                                   30
                                                             30
                                                                                                                                                                                  20
                                                             20
                                                                                                                                                                                  10
                                                             10
                                                                                                                                                                                  0
                                                             0
                                                                                                                                                                                       0                5                10           15
                                                                  0               5             10         15          20
                                                                                                                                                                                                      Peak Burnup (at %)
                                                                                      Peak Burnup (at %)

                     Fig. 9. (a) X425 fuel swelling behavior at peak clad strain location, and (b) X430 fuel swelling behavior at peak clad strain location.



                                         a                                                                                      b
                                                                      10.4 at %            15.8 at %             18.9 at %                                                             3.0 at %             7.4 at %           11.6 at %




                                    Contact Pressure (MPa)                                                                       Contact Pressure (MPa)
                                                             50                                                                                                      50

                                                             40                                                                                                      40
                                                             30                                                                                                      30
                                                             20                                                                                                      20
                                                             10                                                                                                      10
                                                             0                                                                                                                0
                                                                  0         0.2           0.4        0.6    0.8          1                                                         0           0.2       0.4       0.6        0.8       1
                                                                            Normalized Fuel Axial Height                                                                                       Normalized Fuel Axial Height

                            Fig. 10. (a) X425 fuel pin axial variation of contact pressure, and (b) X430 fuel pin axial variation of contact pressure.


Karahan (2009). Main target is to predict the ﬁssion gas release, clad                                                          between the X425 and X430 assemblies are fuel smear density, size
hoop strain, and fuel axial elongation behavior. Geometry, materi-                                                              of the fuel slug, linear heat rate and peak burn-up. X425 was one of
als and main operating conditions for X425 and X430 assemblies                                                                  the most successful fuel assemblies, reaching 18.9 at % peak burn-
are given in Table 2. The detailed operating history used in these                                                              up with no failure. X430 has higher smear density, which limits
simulations can be found in Karahan (2009). The main differences                                                                the achievable burn-up due to earlier start of fuel clad mechanical
                                                                                                                                interaction and clad straining.
                                                                                                                                    Axial variation in fuel centerline temperature at early irradia-
Table 2                                                                                                                         tion and at end of life is given in Fig. 8. Due to its higher linear
X425 and X430 fuel speciﬁcations.
                                                                                                                                heat rate, X430 fuel pin has higher fuel centerline temperature
  Assembly no.                                                         X425                             X430                    (Fig. 8(b)) compared to X425 (Fig. 8(a)). Towards the end of life, fuel
  Fuel composition                                                     U–19Pu–10Zr                      U–19Pu–10Zr             temperature drops due to somewhat lower linear heat rate, lower
  Clad material                                                        HT9                              HT9
                                                                                                                                coolant exit temperature, and lower fuel porosity. Fig. 9 shows
  Fuel slug density (g/cm3 )                                           15.8                             15.8
  Fuel slug radius (mm)                                                2.16                             2.86                    the fuel swelling behavior of X425 and X430 at peak clad strain
  Clad inner radius (mm)                                               2.54                             3.28                    axial location (40% from bottom). During the ﬁrst few atom percent
  Clad outer radius (mm)                                               2.92                             3.68                    of burn-up, ﬁssion gas swelling and formation of interconnected
  Fuel smear density (%)                                               72.3                             76
                                                                                                                                porosity takes place. With the start of hard contact between the fuel
  Fuel active length (cm)                                              34.3                             34.3
  Axial peaking factor                                                 1.12                             1.12
                                                                                                                                and cladding, open porosity decreases in order to accommodate
  Plenum to fuel ratio                                                 1.0                              1.4                     solid ﬁssion product swelling.
  Peak linear heat rate (kW/m)                                         40                               50                          Fig. 10(a) and (b) shows the axial variation of contact pressure
  Coolant inlet temperature (◦ C)                                      370                              370                     for X425 and X430, respectively. The constitutive models for the
  Peak clad temperature (◦ C)                                          590                              590
                                                                                                                                fuel dimensional changes, such as fuel and clad swelling, creep and
  Peak fast ﬂux (n/cm2 /s)                                             2.3 × 1015                       1.6 × 1015
  Peak burn-up (at.%)                                                  18.9                             11.6                    thermal expansion, play a major role in the contact pressure cal-
  Peak dose at end of life (dpa)                                       ∼95                              ∼60                     culation. The range of validity of the contact pressure calculation
                                                                             A. Karahan, N.C. Andrews / Nuclear Engineering and Design 258 (2013) 26–34                                                                       31


                                                 X425-Experimental Data               X430 Experimental Data                                                       X430-Experimental Data           X425-Experimental Data
                                                 X425-FEAST                           X430 FEAST                                                                   X430-FEAST                       X425-FEAST
                             2.5                                                                                                                100




 Peak Clad Hoop Strain (%)                                                                                            Fission Gas Release (%)
                              2                                                                                                                  80

                             1.5                                                                                                                 60

                              1                                                                                                                  40

                             0.5                                                                                                                 20

                              0                                                                                                                   0
                                   0                     5              10                15               20                                          0                5                10                15                20
                                                                 Peak Burnup (at %)                                                                                             Peak Burnup (at %)

                              Fig. 11. Peak clad hoop strain burn-up variation for X425 and X430.                                                     Fig. 13. Fission gas release predictions for X425 and X430 fuels.


                                                                                                                        The ﬁnal benchmark set is against the fuel axial elongation tests.
is dependent on the accuracy of the constitutive models. The com-                                                   Anisotropic fuel slug elongation occurs due to (1) axial variation
puted contact pressure at a time step assures that the fuel and clad                                                of fuel temperature and burn-up, (2) fuel cracking, and (3) grain
displacement rates are identical. This strategy is consistent with                                                  boundary tearing. FEAST models anisotropic fuel axial deforma-
previous approaches such as Ogata and Yokoo (1999). The contact                                                     tion as a function of plutonium content of the fuel and average
pressure increases with burn-up mainly due to increased plenum                                                      linear heat rate to fuel slug diameter ratio using an anisotropy factor
pressure and lower fuel temperature towards end of life. Since the                                                  which acts as a ﬂag to determine the onset of axial contact between
interconnected porosity remains at the plenum pressure, the con-                                                    fuel slug and clad. Once the speciﬁed fraction of the initial gap is
tact pressure required to compress the porosity needs to be higher                                                  ﬁlled by swollen fuel slug, the axial interaction takes place.
than the plenum pressure. It is much higher at the lower axial sec-
tions due to low operating temperature (less compliant fuel). If the                                                drgap = (1 − f ) × drgap 0
open porosity drops below 10%, the fuel may become much stiffer.
                                                                                                                    drgap : gap thickness at which fuel-clad axial contact takes place;
However, Fig. 9 shows the open porosity is above 10% during the
                                                                                                                    drgap0 : initial gap between the fuel and clad; f: anisotropy factor
operation.
                                                                                                                    calculated as a function of plutonium content and linear heat rate
    Fig. 11 shows the burn-up variation of clad strain and compar-
                                                                                                                    to fuel slug diameter ratio
ison with the experimental data at the middle and end of life for
                                                                                                                        Table 3 shows that it is possible to predict the experimental
X425 and X430 fuels. The clad strain is mainly due to irradiation
                                                                                                                    data given in (Hofman et al., 1990; Pahl et al., 1990; Crawford et al.,
creep. The match is satisfactory. Fig. 12 shows the axial variation of
                                                                                                                    1994), satisfactorily.
the clad hoop strain for X425 fuel. FEAST is able to predict the axial
anisotropy in clad hoop strain variation. Due to lower temperature
                                                                                                                    5. Ultra high burn-up metallic fuel behavior
at bottom axial part, the clad strain tends to be higher in this region.
On the other hand, at the upper axial regions, the fuel is rather com-
                                                                                                                        Increasing the achievable burn-up of fast breeder reactor fuels
pliant. FEAST predictions for clad strain at 15.8 at.% appear to be at
                                                                                                                    is the key target for improving fuel utilization, minimizing nuclear
the conservative side for the upper axial regions. This may be due
                                                                                                                    waste and reducing enrichment requirements. Attainment of very
to (1) overestimation of the contact pressure, or (2) uncertainties
                                                                                                                    high burn-ups, beyond 30–35 at.%, requires cladding materials that
associated with irradiation creep constitutive model.
                                                                                                                    can preserve their high creep fracture and void swelling resistance
    Fission gas release behavior for X425 and X430 is given in Fig. 13.
                                                                                                                    up to very high doses, e.g. 500 dpa. In addition, one should guard
The match with experimental data at end of life is satisfactory. Fur-
                                                                                                                    against lanthanide attack towards clad inner surface and clad hoop
thermore, onset of ﬁssion gas release and its increase and saturation
                                                                                                                    strain due to fuel clad mechanical interaction (irradiation creep)
in early irradiation matches with the generic data given in Pahl et al.
                                                                                                                    and void swelling of the cladding. The current study assumes HT9
(1992), very well.
                                                                                                                    cladding preserves its void swelling rate, fracture toughness and
                                                                                                                    irradiation creep properties up to 500 dpa and examines the effect
                                                                                                                    of fuel swelling on clad hoop strain and fuel clad chemical interac-
                                       15.8 at % Experimental Data               18.9 at% Experimental Data         tion behavior of the fuel for ultra-high burn-up and long residence
                                       15.8 at %-FEAST                           18.9 at %-FEAST                    time conditions.
                             2.5                                                                                        The sample fuel speciﬁcations are given in Table 4. U–6Zr is the
                                                                                                                    initial fuel composition. 6 wt.% Zirconium is selected due to irradia-




  Clad Hoop Strain (%)
                              2                                                                                     tion data of 6 wt.% fuel pins that showed similar behavior as 10 wt.%
                                                                                                                    Zr fuel. The selected fuel smear density is 60%. This value is much
                             1.5
                                                                                                                    lower than typical EBR-II fuel, which is 75%, in order to provide
                              1                                                                                     more space for more solid ﬁssion product swelling and delay onset
                                                                                                                    of fuel clad mechanical interaction. The plenum region is vented,
                             0.5                                                                                    hence, no pressure build-up is allowed. As a result, a high thermal
                                                                                                                    creep fracture margin during transients is satisﬁed. Furthermore,
                              0
                                                                                                                    design of a very large plenum region could be challenging to satisfy
                                   0              0.2             0.4          0.6             0.8         1
                                                                                                                    the core pressure drop constraint. The core axial height, the oper-
                                                             Normalized Axial Height                                ating history of the fuel pin and the plutonium build-up has similar
Fig. 12. Clad hoop strain axial variation at 15.8 at.% and 18.9 at.% peak burn-up for
                                                                                                                    values to previous work on breed and burn reactor performed by
X425 fuel.                                                                                                          Yarsky (2005). Axial peaking factor is 1.4 and its variation is given in
32                                                                        A. Karahan, N.C. Andrews / Nuclear Engineering and Design 258 (2013) 26–34

Table 3
Fuel axial elongation benchmarks (Hofman et al., 1990; Pahl et al., 1990; Crawford et al., 1994).

  Fuel composition                                       Fuel smear density (%)                   q /D (W/cm2 )                                             Axial elongation (%)

                                                                                                                                                             Experimental data                                       Error band               FEAST-METAL

  U–10Zr                                                 76                                       790                                                        6.2                                                ±1.2                          7.1
  U–19Pu–10Zr                                            76                                                                                                  1.5                                                 ±.7                          1.8
  U–10Zr                                                 72                                       830                                                        8.5                                                ±1.2                          7.8
  U–8Pu–10Zr                                             72                                                                                                  6.5                                                 ±.6                          6.7
  U–19Pu–10Zr                                            72                                                                                                  2.5                                                 ±.8                          2.1
                                                                                                                                                                                                                 *
  U–10Zr                                                 75                                       650                                                        8.0                                                                              8.0
                                                                                                                                                                                                                 *
  U–8Pu–10Zr                                             75                                                                                                  5.8                                                                              5.8
                                                                                                                                                                                                                 *
  U–19Pu–10Zr                                            75                                                                                                  6.5                                                                              7.1


Table 4                                                                                                                                                                                  Beginning of Life             18.5 at %           End of Life




                                                                                                                    Fuel Centerline Temperature (ºC)
Ultra-high burn-up sample fuel speciﬁcations.                                                                                                          800
  Parameter                                                                         Value

  Fuel composition (wt.%)                                                           U–6Zr                                                              700
  Clad material                                                                     HT9
  Fuel slug density (g/cm3 )                                                        17
  Fuel slug radius (mm)                                                             3.0                                                                600
  Clad inner radius (mm)                                                            3.87
  Clad outer radius (mm)                                                            4.50
                                                                                                                                                       500
  Fuel smear density (%)                                                            60.0
  Fuel active length (cm)                                                           200
  Plenum volume                                                                     Vented
                                                                                                                                                       400
  Axial peaking factor                                                              1.4
                                                                                                                                                                            0                 0.2              0.4            0.6            0.8         1
  Peak linear heat rate (kW/m)                                                      50
  Peak clad temperature (◦ C)                                                       550                                                                                                                   Normalized Axial Height
  Peak fast ﬂux (n/cm2 /s)                                                          4.5 × 1015
  Peak burn-up (at.%)                                                               36                             Fig. 16. Axial variation of fuel centerline temperature of ultra-high burn-up fuel.
  Peak dose at end of life (dpa)                                                    ∼500

                                                                                                                   ﬁve years, high burn-up fuel is operated at an intermediate power
                                   2                                                                               level, consistent with Yarsky (2005). The peak plutonium content
                                                                                                                   is 10 wt.%, which is bred during low power operation in the ﬁrst
                                                                                                                   phase.




  Power Peaking Factor
                                  1.5                                                                                  Fig. 16 shows the fuel centerline temperature axial variation at
                                                                                                                   beginning of life, middle of life (18.5 at.% peak burn-up) and end of
                                   1                                                                               life. At beginning of life, fuel temperature follows the coolant tem-
                                                                                                                   perature due to low linear heat rate. At high power region, the peak
                                                                                                                   fuel temperature reaches 735 ◦ C due to its high linear heat rate and
                                  0.5                                                                              high fuel porosity. Towards end of life, both linear heat rate and fuel
                                                                                                                   porosity comes down and near 100 ◦ C drop in fuel centerline tem-
                                                                                                                   perature occurs. Fuel swelling behavior at peak clad strain location
                                   0
                                        0      0.2            0.4           0.6             0.8             1      is given in Fig. 17. Above 10% gas swelling, open porosity starts to
                                                                                                                   form and ﬁssion gas release starts (Fig. 17). At ∼12 at.% peak burn-
                                                         Normalized Axial Height
                                                                                                                   up, 50% of the fuel consists of the interconnected porosity. With
                  Fig. 14. Axial variation of the normalized power of ultra-high burn-up fuel.                     the start of hard contact between the fuel and clad, solid ﬁssion
                                                                                                                   product swelling is balanced by hot pressing of the open porosity
                                                                                                                   under the applied contact pressure. Towards the end of life, reduc-
Fig. 14. The ﬁrst 10 years, the fuel operates at low power at passive
                                                                                                                   tion of the fuel temperature makes the fuel much stiffer. In order to
region and produces plutonium (Fig. 15). Once it is shufﬂed into the
                                                                                                                   accommodate the solid ﬁssion product swelling, clad hoop strain
active region, power level increases by an order of magnitude. The
                                                                                                                   rate increases signiﬁcantly as shown in Fig. 18. The total predicted
fuel is allowed to spend ﬁve years in the active fuel region. The last

                                                                                                                                                                                                    Closed Bubble                  Open Porosity




   Peak Linear Heat Rate (kW/m)
                                   60                                                                                                                                                               Solid FP                       Total Swelling
                                                                                                                                                                            100
                                   50
                                                                                                                                                                                80




                                                                                                                                                        Fuel Swelling (%)
                                   40
                                                                                                                                                                                60
                                   30

                                   20                                                                                                                                           40

                                   10                                                                                                                                           20

                                    0                                                                                                                                           0
                                        0            5               10               15                   20                                                                        0               10                20            30             40
                                                                Time (year)                                                                                                                                  Peak Burnup (at %)

                            Fig. 15. Time variation of peak linear heat rate of ultra-high burn-up fuel.                                                                    Fig. 17. Fuel swelling behavior of ultra-high burn-up fuel.
                                                                                                              A. Karahan, N.C. Andrews / Nuclear Engineering and Design 258 (2013) 26–34                                                     33


                                                                               a                                                                       b
                                                                                                                    15%              30%        36%                                           15 at %         30 at %         36 at %




                                                                         Contact Pressure (MPa)
                                                                                                  30




                                                                                                                                                       Clad Hoop Strain (%)
                                                                                                                                                                                  3
                                                                                                  20
                                                                                                                                                                                  2

                                                                                                  10                                                                              1

                                                                                                  0                                                                               0
                                                                                                        0    0.2    0.4      0.6      0.8        1                                    0                    0.5                    1
                                                                                                               Normalized Axial Height                                                           Normalized Axial Height

                                Fig. 18. (a) Axial variation of contact pressure of ultra-high burn-up fuel, and (b) axial variation of clad hoop strain of ultra-high burn-up fuel.



                                                 a                                                                                                    b




                                            Fission Gas Release (%)                                                                                    Fuel Axial Elongaon (%)
                                                                       100                                                                                                        30

                                                                        80
                                                                                                                                                                                  20
                                                                        60
                                                                        40                                                                                                        10
                                                                        20
                                                                                    0                                                                                                 0
                                                                                                  0          10           20           30       40                                        0             10       20        30           40
                                                                                                              Peak Burnup (at %)                                                                         Peak Burnup (at %)

                                                                      Fig. 19. (a) Fission gas release of ultra-high burn-up fuel, and (b) fuel axial elongation of ultra-high burn-up fuel.

peak clad hoop strain is 3% at the end of life. 1% of this is predicted                                                                               5.1. Potential concerns for ultra-high burn-up metallic fuel
to be void swelling and the rest of it is due to the irradiation creep.
Fuel clad mechanical interaction at the bottom of the fuel shown in                                                                                   - It may be challenging for HT9 clad to preserve its creep fracture
Fig. 18(a) is much higher due to lower fuel temperature.                                                                                                margin up to 500 dpa.
    Compared to X425 fuel (Fig. 10(a)), the contact pressure                                                                                          - Fuel clad chemical interaction behavior appears to be controllable
between the fuel and clad is much lower for the sample high burn-                                                                                       below 550 ◦ C peak clad temperature; however, it may still bear a
up fuel. On the other hand, nearly ﬁve times higher dose on the                                                                                         high uncertainty.
cladding reduces the necessary contact pressure between fuel and                                                                                      - During long term transients, eutectic formation and penetration
clad to ensure the plastic ﬂow of the cladding. Fission gas release                                                                                     and fuel pin failure is a still concern although the fuel pin is vented.
towards end of life is 95% (Fig. 19(a)). As a result of higher burn-                                                                                  - Combination of the stiff fuel at low temperature and high cladding
up, higher fuel porosity, longer fuel residence time, and higher                                                                                        dose requirement eases the clad straining via irradiation creep
coolant inlet temperature, the ﬁssion gas release is much higher                                                                                        while the fuel remains porous.
compared to EBR-II conditions (Fig. 13). Furthermore, fuel axial
elongation is 20% (Fig. 19(b)), nearly twice as high compared to                                                                                      5.2. Possible design improvements
75% smear density U–10Zr EBR-II fuel pins. It is due to much lower
fuel smear density and low initial linear heat rate. Fig. 20 shows the                                                                                - The study suggests using a porous, compliant and chemically sta-
clad wastage behavior at end of life. It appears that most corrosion                                                                                    ble buffer region at the fuel clad interface, similar to the work
occurs at the clad inner side at the upper axial part of the fuel due                                                                                   described by Karahan and Kazimi (2010), in order (1) to hinder
to lanthanide attack. The total clad wastage appears to be below                                                                                        fuel clad chemical interaction during steady state and transient,
20% of the total clad thickness.                                                                                                                        and (2) to allow for higher fuel temperature to ease hot pressing of
                                                                                                                                                        the fuel porosity to accommodate solid ﬁssion product swelling.
                                                                                                                                                        This may allow for operation with much lower contact pressure
                                                                                                                                                        between fuel and clad.
                                                                                                                                                      - If the axial power peaking is high, it may be possible to increase
                                                                                                                                                        the fuel smear density at axial locations at which the burn-up
                                          Clad Inner Wastage                                                            Clad Outer Wastage              is lower and the fuel is more compliant. This approach may also
                         150                                                                                                                            ﬂatten the axial power proﬁle, reduce the peak clad dose, and
                                                                                                                                                        increase the fuel utilization.




     Clad Wastage (μm)
                         100
                                                                                                                                                      6. Conclusions

                                                                                                                                                          Physical models in FEAST-METAL are improved further in order
                           50
                                                                                                                                                      to increase the code’s performance in various operating conditions.
                                                                                                                                                      Since the available database for metallic fuels is rather limited, gain-
                            0                                                                                                                         ing extrapolation ability via physics based semi-empirical models
                                0          0.2                                                         0.4        0.6          0.8          1         is very critical to design next generation reactors within a limited
                                                                                                                                                      time span and guide the required experimental work.
                                                                                      Normalized Axial Height
                                                                                                                                                          First, a ﬁssion gas bubble grouping scheme based on constant
                         Fig. 20. Clad inner and outer wastage of ultra-high burn-up fuel.                                                            atom number per bubble group is adopted while retaining isotropic
34                                                A. Karahan, N.C. Andrews / Nuclear Engineering and Design 258 (2013) 26–34


bubble nucleation behavior. The bubble morphology of each phase                          Crawford, D.C., Porter, D.L., Hayes, S.L., 2007. Fuels for sodium-cooled fast reactors:
structure is captured by assigning a constant number of gas atoms                            US perspective. J. Nucl. Mater. 371, 202–231.
                                                                                         Gruber, E.E., Kramer, J.M., 1987. Gas bubble growth mechanisms in the
per bubble and the bubble shape at each radial node. Further-                                analysis of metal fuel swelling. In: Proceedings of 13th International
more, the gas diffusion coefﬁcient is deﬁned in a phase dependent                            Symposium Radiation Induced Changes in Microstructure, ASTM-STP-955,
manner, using the activation energy of the corresponding phase                               p. p. 432.
                                                                                         Hoffman, E.A., Yang, W.S., Hill, R.N., 2006. Preliminary Core Design Studies for the
structure. In addition to improvements on ﬁssion gas behavior, a                             Advanced Burner Reactor Over a Wide Range of Conversion Ratios, ANL-AFCI-
best estimate value is preferred for solid ﬁssion product swelling                           177. Argonne National Laboratory, Argonne, IL.
rate. Next, it is proposed that hot pressing model for fuel intercon-                    Hofman, G.L., Pahl, R.G., Lahm, C.E., Porter, D.L., 1990. “Swelling Behavior of U–Pu–Zr
                                                                                             Fuel”. Metall. Trans. A 21A, 517–528.
nected porosity could be over-estimating the pore decrease for the
                                                                                         Hofman, G.L., Walters, L.C., Bauer, T.H., 1997. Metallic fast reactor fuels. Prog. Nucl.
dual phases. A correction factor is suggested for the compressibility                        Energy 31, 83–110.
factor for the dual phases in order to match fuel thermo-mechanical                      Karahan, A., Modeling of thermo-mechanical and irradiation behavior of metallic
                                                                                             and oxide fuels for sodium fast reactors. Ph.D. Thesis. Nuclear Sci-
behavior, satisfactorily. The benchmarks show that the code can
                                                                                             ence and Engineering Department, Massachusetts Institute of Technology,
predicts the available EBR-II experimental data very well, similar to                        2009.
the previous version. On the other hand, added physics based mod-                        Karahan, A., Kazimi, M.S., 2010. Using graphitic foam as the bonding material in
els could improve the applicability of the code beyond the validated                         metal fuel pins for sodium fast reactors, Nuclear Fuels and Structural Materials
                                                                                             Embedded Topical Meeting, American Nuclear Society Annual Meeting, vol. 102,
region.                                                                                      pp. 790–792.
    The sample ultra-high burn-up vented fuel simulation shows                           Kim, Y.S., Hofman, G.L., 2003. AAA Fuels Handbook, ANL-AAA-068. Argonne National
that the fuel swelling and clad hoop strain is controllable by reduc-                        Laboratory.
                                                                                         Lee, C.B., Kim, D.H., Jung, Y.H., 2001. Fission gas release and swelling model of metal-
ing the fuel smear density to near 60%. The resulting peak value of                          lic fast reactor fuel. J. Nucl. Mater. 288, 29–42.
the total clad hoop strain is 3%. The stiffer fuel and high cladding                     McDeavitt, S.M., 1992. Hot isostatic pressing of U–10Zr alloy nuclear fuel by cou-
dose leads to straining of the cladding although the fuel is very                            pled grain boundary diffusion and power law creep. Ph.D. Thesis. Purdue
                                                                                             University.
porous at the end of life. Fuel clad chemical interaction could be                       McDeavitt, S.M., Solomon, A.A., 1996. Hot-isostatic pressing of U–10Zr by a coupled
controlled if peak clad temperature remains below 550 ◦ C. Near                              grain boundary diffusion and creep cavitation mechanism. J. Nucl. Mater. 228,
20% clad wastage and the uncertainty associated with it may bring a                          184–200.
                                                                                         Ogata, T., Yokoo, T., 1999. Development and validation of alfus: an irradiation
design concern. The need for more compliant fuel slug and a neces-
                                                                                             behavior analysis code for metallic fast reactor fuels. Nucl. Technol. 128,
sity to hinder fuel clad chemical interaction may require a porous                           113–123.
buffer layer between the fuel and clad. It is suggested that a chemi-                    Pahl, R.G., Wisner, R.S., Billone, M.C., Hofman, G.L., 1990. Steady-state irradiation
                                                                                             testing of U–Pu–Zr fuel > 18 at.% burn-up. In: Proceedings of the 19990 Interna-
cally stable, low thermal conductivity, porous and compliant layer
                                                                                             tional Fast Reactor Safety Meeting, vol. 4, pp. 129–137.
may allow for the sintering of the fuel open porosity and hinder                         Pahl, R.G., Porter, D.L., Crawford, D.C., Walter, L.C., 1992. Irradiation behavior of
fuel clad chemical interaction.                                                              metallic fast reactor fuels. J. Nucl. Mater. 188, 3–9.
                                                                                         Tsuboi, Y., Ogata, T., Kinoshita, M., Saito, H., 1992. Mechanistic model of ﬁssion gas
                                                                                             behavior in metallic fuel. J. Nucl. Mater. 188, 312–318.
Acknowledgement                                                                          Walters, L.C., 1999. Thirty years of fuels and materials information from EBR-II. J.
                                                                                             Nucl. Mater. 270, 39–48.
  This project is supported by TerraPower, LLC Company, Bellevue,                        Weaver, K., Ahlfeld, C., Gilleland, J., Whitmer, C., Zimmerman, G., 2009. Extending
                                                                                             the nuclear fuel cycle with traveling-wave reactors, paper 9294. In: Proceedings
WA.                                                                                          of Global 2009, Paris, France, September 6–11.
                                                                                         Wood, M.H., Hayns, M.R., 1976. Factors inﬂuencing ﬁssion gas release and swelling
References                                                                                   in nuclear fuels, Technical Report, AERE-R-8153, Harwell, UK.
                                                                                         Yarsky, P., 2005. Core design and reactor physics of a breed and burn gas-cooled
                                                                                             fast reactor. Ph.D. Thesis. Nuclear Science and Engineering Department, Mas-
Crawford, D.C., Hayes, S.L., Pahl, R.G., 1994. Large-diameter, high plutonium metallic       sachusetts Institute of Technology.
   fuel testing in EBR-II. Trans. Am. Nucl. Soc. 71, 178–179.
