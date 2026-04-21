# Lower length scale informed improvements to Bison U-Pu-Zr fuel swelling model

---

                   INL/EXT-20-59990 Rev. 0

                          September 2020




Lower length scale
informed improvements to
Bison U-Pu-Zr fuel
swelling model



Larry Aagesen
Andrea Jokisaari
Jia-Hong Ke
                                             NOTICE
This information was prepared as an account of work sponsored by an agency of the U.S.
Government. Neither the U.S. Government nor any agency thereof, nor any of their
employees, makes any warranty, express or implied, or assumes any legal liability or
responsibility for any third party’s use, or the results of such use, of any information, apparatus,
product, or process disclosed herein, or represents that its use by such third party would not
infringe privately owned rights. The views expressed herein are not necessarily those of the
U.S. Nuclear Regulatory Commission.
                                                        INL/EXT-20-59990 Rev. 0




Lower length scale informed improvements to Bison U-Pu-Zr
                    fuel swelling model


                            Larry Aagesen
                           Andrea Jokisaari
                             Jia-Hong Ke

                             September 2020




                  Idaho National Laboratory
       Computational Mechanics and Materials Department
                   Idaho Falls, Idaho 83415




                             Prepared for the
                        U.S. Department of Energy
                         Office of Nuclear Energy
          Under U.S. Department of Energy-Idaho Operations Office
                       Contract DE-AC07-99ID13727




                                    iii
                                       ABSTRACT
    Due to renewed interest in metallic fuels from the U-(Pu)-Zr material system, significant
improvements have recently been made to BISON’s capability to simulate metallic fuel, par-
ticularly in the area of swelling. In this report, lower length scale simulations that have been
conducted to inform the engineering-scale models in BISON during FY20 are described. For
the high-temperature regions of the fuel that are dominated by the γ phase of U-(Pu)-Zr, two
new models for swelling have implemented in BISON. Phase-field simulations were conducted
to calculate parameters for these and other BISON models that control when gaseous swelling
ceases and fission gas release begins. For the low-temperature regions of the fuel dominated by
the α phase of uranium, microstructurally resolved simulations of pore growth and crystal defor-
mation were performed to understand the effect of irradiation-generated crystal shape changes.
Conformally meshed microstructures with pores were simulated with a crystal plasticity model
and with a burnup eigenstrain model. Plastic deformation will not cause pore size to increase;
burnup eigenstrain (irradiation-induced crystal shape changes) will increase the volume of exist-
ing porosity and cause it to become anisotropic in shape. Additional model development work
for early-stage fission gas cluster/bubble formation in the γ phase were performed, by coupling
with defect clustering within cluster dynamics framework. Sensitivity analysis were conducted
to identify the critical thermo-kinetic parameters needed for rigorous assessment.




                                               iv
                                           CONTENTS

FIGURES                                                                                                  vi

TABLES                                                                                                  viii

1 Introduction                                                                                            1

2 High temperature interconnectivity                                                                      3
  2.1 Simulation parameters and results . . . . . . . . . . . . . . . . . . . . . . . . . . . .           3
  2.2 Determination of parameters for UPuZrGaseousEigenstrain . . . . . . . . . . . . . .                 6
  2.3 Determination of parameters for ADFissionGasViscoplasticityStressUpdateBase . . .                   7
  2.4 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .         9

3 Low temperature swelling                                                                               10
  3.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     10
  3.2 Models . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     10
  3.3 Mesh generation and assignment of grain orientation . . . . . . . . . . . . . . . . . .            11
  3.4 Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    12
  3.5 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .        14

4 Cluster dynamics                                                                                       17
  4.1 Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     17
  4.2 Methods . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .      17
  4.3 Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    19
  4.4 Summary and concluding remarks . . . . . . . . . . . . . . . . . . . . . . . . . . . .             23

5 References                                                                                             25




                                                    v
                                          FIGURES
1    Evolution of microstructure during simulation of gas bubble growth with s0 = 5 ×
     10−3 and M = 1. Isosurface of c = 0.5 is shown. (a) initial conditions; (b) the bubbles
     have grown but none have begun to merge; (c) bubble merging and coalescence has
     begun; (d) a percolated path exists from the simulation domain boundary at x = 0
     µm and the boundary at x = 72 µm. . . . . . . . . . . . . . . . . . . . . . . . . . .             4
2    Fraction of total bubble volume that is connected to a free surface, fV , as a function
     of porosity p for (a) M = 1, (b) M = 2.5, (c) M = 5, with N = 3 × 1014 /m3 . . . . .              5
3    Fraction of total bubble volume that is connected to a free surface, fV , as a function
     of porosity p for (a) N = 3.75 × 1014 /m3 and (b) N = 4.5 × 1014 /m3 , with M = 1. .              6
4    Fraction of total bubble volume that is connected to a free surface, fV , as a function
     of porosity p for (a) M = 1, (b) M = 5. . . . . . . . . . . . . . . . . . . . . . . . . .         8
5    Comparison of I(p) (smooth step function of Eq. 3) and fV (Eq. 2) with parameters
     based on fit to phase-field simulations. . . . . . . . . . . . . . . . . . . . . . . . . .        9
6    The grain structure used in this work. a) The solid surface, with each grain a different
     color. b and c) The mesh, to demonstrate grain boundaries and pores. One pore is
     located in the center of the image in b), while two pores are visible in c). . . . . . .         12
7    The change in pore volume for the simulations of burnup-generated eigenstrain. a)
     For the three variations of Euler angles with one hole in the structure. b) For the
     three variations of Euler angles with two holes in the structure. . . . . . . . . . . . .        13
8    The change in the pore structure with burnup-generated eigenstrain. a) The initial
     grain and pore structure before the accumulation of burnup-generated eigenstrain.
     b) The grain and pore structure after the accumulation of 0.1% burnup. The pores
     are evidently elongated. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .     14
9    The variation in the pore volume for the top) first, middle) second, and bottom)
     third variations in this work for a one-pore structure at multiple temperatures. . . .           15
10   The variation in the pore volume for the top) first, middle) second, and bottom)
     third variations in this work for a two-pore structure at multiple temperatures. . . .           16
11   Plots of cluster dynamics modeling results showing the time evolution of (a) number
     density and (b) mean radius of Xe clusters at 1000 K. . . . . . . . . . . . . . . . . .          20
12   Plots showing the evolution of the Xe and vacancy cluster size distributions at 1×105 ,
     5 × 105 , and 1 × 106 s. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   20
13   Plots showing the time evolution of Xe monomer and vacancy monomer concentra-
     tions. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   21
14   Plots of modeling results showing the effect of Xe cluster interface energies (0.20,
     0.25, 0.30 J m−2 ) on the time evolution of (a) number density and (b) mean radius
     of Xe clusters at 1000 K. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    21
15   Plots of modeling results showing the effect of Xe solubility (10−13 – 10−10 ) on the
     time evolution of (a) number density and (b) mean radius of Xe clusters at 1000 K. .             22
16   Plots of modeling results showing the effect of vacancy migration barrier (0.6 - 1.2
     eV) on the time evolution of (a) number density and (b) mean radius of Xe clusters
     at 1000 K. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .   22
17   Plots of modeling results showing the effect of vacancy cluster interface energy (0.1
     – 0.5 J m−2 ) on the time evolution of (a) number density and (b) mean radius of Xe
     clusters at 1000 K. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .    23




                                                vi
18   Plots of modeling results showing the effect of vacancy formation energy (0.6 – 1.4
     eV) on the time evolution of (a) number density and (b) mean radius of Xe clusters
     at 1000 K. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 23




                                               vii
                                       TABLES
1   Mean percolation threshold (pc ) and mean porosity at which fV = 0.8 (p0.8 ) for the
    five initial condition configurations considered, and corresponding standard devia-
    tions, for each set of simulation parameters. . . . . . . . . . . . . . . . . . . . . . . 6
2   Mean pcen and ∆ for the five initial condition configurations considered and corre-
    sponding standard deviations for each set of simulation parameters. . . . . . . . . . 8
3   Physical parameters used in the simulation of Xe and vacancy clustering at 1000 K. 19




                                           viii
                                       1    Introduction
Nuclear fuel based on the U-(Pu)-Zr system has been used in past reactor designs and is being
considered for new reactor designs, such as Oklo’s Aurora and the Versatile Test Reactor. The
concept of a fast-spectrum reactor fueled with U-(Pu)-Zr was extensively validated during the
years of operation of the Experimental Breeder Reactor-II (EBR-II). Fuel for such reactor concepts
has typically employed compositions of 10 wt. % Zr and Pu composition ranging from 0 to 26
wt. %. Although reactors based on this design have not yet been used for commercial energy
production in the U.S., renewed interest from commercial designers in metallic fuel designs has led
the Department of Energy to invest in an effort to improve the metallic fuel simulation capabilities
in the fuel performance code BISON.
     Swelling is a major concern in U-(Pu)-Zr fuels. Swelling begins early in life for metallic fuels
and reaches significantly larger values than those observed in the oxide fuels used in commercial
light water reactors [1]. As a result, significant effort has been invested in recent years to develop
mechanistic models of swelling in BISON [2, 3], particularly for models of gaseous swelling, which
dominates over solid swelling. However, mechanistic models require physical parameters as model
inputs that in some cases are not well known. Due to the high cost and time required to obtain
such parameters through experiments, simulations using lower-length scale techniques that can
provide such parameters and give physical insight to improve BISON models are a cost-effective
alternative. In this report, efforts to improve BISON models of swelling and fission gas release
using lower-length scale simulations carried out by the Department of Energy’s NEAMS program
during FY20 are described.
     The mechanism of gaseous swelling differs in different regions of the fuel. In the center of
the fuel pins, where the fuel is hotter, the microstructure is dominated by the γ phase, which
has a body-centered cubic (BCC) crystal structure. In this region of the fuel, the fission gas
bubbles are quite large compared to those observed in UO2 fuel, with diameters on the order of
tens of microns [1]. The morphology of the bubbles is generally spherical. The BISON models of
gaseous swelling in the high-temperature region assume a spherical distribution of bubbles with a
uniform size [2, 3]. As these bubbles grow, they begin to interconnect. When the bubbles form
a fully interconnected structure, the gas within the bubbles is released from the fuel, and any
further fission gas produced will travel out of the fuel through this network rather than causing
the existing bubbles to grow further. The porosity values at which this interconnection process
begins and ends therefore control when swelling terminates and when fission gas release begins.
However, the values for these values have not been measured to our knowledge and would be
difficult to obtain experimentally. Therefore, phase-field simulations have been used to determine
when interconnection begins and ends in the two available gaseous swelling models in BISON. These
simulations and the resulting BISON parameters are described in Section 2.
     Along the periphery of fuel pins or at the portion adjacent to the coolant inlet, fuel temper-
atures are lower. Metallic fuel in the U-Pu-Zr system exhibits swelling at low temperatures that
is morphologically distinct from swelling that occurs at high temperatures. Although the exact
temperature depends on composition, the cubic γ phase exists above approximately 600 ◦ C (873
K) [4], in which swelling appears to be driven by gas bubble formation [5]. At lower temperatures, a
multitude of phases can exist depending on the exact fuel composition, but phases typically include
orthorhombic α-uranium and hexagonal δ-(U, Pu)Zr2 [4]. The microscopic swelling that occurs at
low temperatures appears as elongated porosity with ragged edges [5]. The swelling mechanism is
hypothesized to be mechanical cavitation resulting from irradiation-induced shape changes of α-
uranium crystals. Irradiation (i.e., fuel burnup) causes single crystals of α-uranium to change shape
macroscopically, shrinking in the [100] direction, growing in the [010] direction, and unchanged in

                                                  1
the [001] direction [6].
     Internal strains can develop within polycrystalline α-uranium on the level of hundreds of mega-
pascals due to temperature changes or irradiation. Previous work has indicated that irradiation-
induced strains within polycrystalline α-uranium will lead to stresses on the order of hundreds of
megapascals within burnup levels of 0.001% FIMA [7]. In addition, similar stresses resulting from
anisotropic thermal expansion can occur with a temperature change of approximately 200 K [8, 9].
In Section 3, microstructurally resolved simulations of plastic flow in α-uranium and irradiation-
induced crystal shape changes were conducted to understand the impact of these behaviors on
pre-existing porosity.
     Cluster dynamics simulations is utilized to capture the early-stage fission gas (Xe) bubble for-
mation in the high temperature γ phase. The method is based on mean-field rate theories charac-
terizing various classes of cluster reactions evolving the distribution of cluster size. The reactions
are driven by the supersaturated fission gas composition. Due to the extremely low solubility of
fission gas atoms in metallic fuels, a large density of fission gas clusters will form at the early stage.
The production of such fission gas atoms during reactor operation results in continuous increase
of size and volume fraction of fission gas clusters, whose growth is assisted by the vacancy mecha-
nism and radiation-induced point defects in metallic fuels. The model development and simulation
results of Xe clustering coupled with defect clusters in γ U-Zr are described in Section 4.




                                                    2
                       2    High temperature interconnectivity
In Ref. [10], phase-field simulations of the growth and interconnection of fission gas bubbles in the
high-temperature regime of U-(Pu)-Zr were performed to parameterize the BISON gaseous swelling
and fission gas release models described in Ref. [2]. In this model, UPuZrGaseousEigenstrain, the
swelling is given by [11]
                                            1/2
                                                     [(kT /2σ)YXe Ḟ t]3/2
                                    
                                ∆V            3
                                        =                                                         (1)
                                 V0 g        4π             N 1/2
where k is the Boltzmann constant, T is the temperature in K, σ is the surface tension of the fuel-
bubble interface, YXe is the gaseous fission product yield, Ḟ is the fission rate density, t is time, and
N is the number density of bubbles. With increasing burnup, the volumetric swelling increases by
Eq. (1) until porosity is high enough to allow gas release. The number of atoms produced by fission
that are added to the bubbles (and thus that contribute to swelling by Eq. 1) decreases linearly in
a range controlled by the Bison model parameters interconnection initiating porosity and
interconnection terminating porosity (referred to as pi and pt , respectively, in this report).
In Ref. [10], preliminary estimates of pi and pt were determined to be 0.26 and 0.28, respectively.
However, these values were based on a single set of initial conditions in which fission gas bubbles
were randomly placed in the simulation domain. In this report, we consider an additional four sets
of initial bubble positions to determine the effect of the initial conditions on the calculated BISON
model parameters and to estimate the uncertainty in these values.
    In addition, a new model for swelling due to fission gas bubbles was recently added to BISON [3].
In this model, additional physics are added beyond those considered in the derivation of Eq. 1, such
as the van der Waals equation of state for the fission gas within the bubble and the hydrostatic
stress in the fuel matrix surrounding the gas bubble. In the model of Ref. [3], the fraction of
bubbles in a given volume element that are connected to an external surface is described by an
interconnectivity function I(p), where p is the local porosity. Previously, I(p) was set to be an
empirical function. In this report, we fit a function for I(p) based on phase-field simulations with
multiple configurations.


                      2.1     Simulation parameters and results
In Ref. [10], the growth and interconnection of bubbles was simulated using a Cahn-Hilliard model
with a source term, with a single defect species produced only in the fuel matrix. For details of the
model, please see Ref. [10]. As a baseline, 112 bubbles were randomly placed in the initial conditions
in a 72 µm × 72 µm × 72 µm simulation domain, resulting in number density N = 3 × 1014 /m3
as observed in the later stages of experiment (based on Fig. 2 of Ref. [12]). The effect of varying
defect species mobility M and number density N was considered.
    Here, we consider an additional four sets of initial random bubble positions and determine
their impact on the obtained BISON parameters. The (x, y, z) positions of the bubble centers in
the initial conditions were determined by a random number generator. To vary the initial bubble
positions, a different seed was supplied to the random number generator, resulting in a different
set of initial bubble positions. Each of the five total sets of initial bubble positions is referred to as
Configuration 1 – 5. An example of the initial conditions and subsequent microstructural evolution
for Configuration 1 is shown in Fig.1, for the case with M = 1 and N = 3 × 1014 /m3 [12].
    To understand how the interconnection of bubbles progresses and provide a basis for parame-
terization of BISON models of swelling and fission gas release, the fraction of bubble volume that
is connected to an external surface, fV , was calculated for the simulations as follows. Individual


                                                    3
              (a) Initial conditions                               (b) t = 25.3




                  (c) t = 50.6                                     (d) t = 76.2

Figure 1: Evolution of microstructure during simulation of gas bubble growth with s0 = 5 × 10−3
and M = 1. Isosurface of c = 0.5 is shown. (a) initial conditions; (b) the bubbles have grown but
none have begun to merge; (c) bubble merging and coalescence has begun; (d) a percolated path
exists from the simulation domain boundary at x = 0 µm and the boundary at x = 72 µm.




                                               4
      1                                                                    1
               M = 1, Config. 1
     0.8       M = 1, Config. 2                                           0.8
               M = 1, Config. 3
               M = 1, Config. 4
     0.6                                                                  0.6
               M = 1, Config. 5
fV
     0.4                                                                  0.4


     0.2                                                                  0.2


      0                                                                    0
           0       0.1      0.2               0.3         0.4                   0         0.1         0.2   0.3   0.4
                                p
                          (a)                                                                     (b)
                                     1
                                              M = 5, Config. 1
                                    0.8       M = 5, Config. 2
                                              M = 5, Config. 3
                                              M = 5, Config. 4
                                    0.6
                                              M = 5, Config. 5
                            fV
                                    0.4


                                    0.2


                                     0
                                          0         0.1             0.2             0.3         0.4
                                                                    p
                                                            (c)

Figure 2: Fraction of total bubble volume that is connected to a free surface, fV , as a function of
porosity p for (a) M = 1, (b) M = 2.5, (c) M = 5, with N = 3 × 1014 /m3 .


bubbles were identified as isolated regions where c > 0.5 using a recursive flood fill algorithm [13]
and the volume of each such individual bubble was determined. A free surface is assumed to exist
at the simulation domain boundary at x = 72 µm. For each bubble, it is determined whether or
not it intersects that boundary, and fV is calculated as the volume of bubbles that intersect the
free surface divided by the total bubble volume at each time step.
    fV is plotted as a function of porosity p for varying mobility cases in Fig. 2. fV is non-zero at
the start of the simulation because some bubbles contact the free surface in the initial condition;
however, their contribution is small. The increase in fV is slow until p ≈ 0.25. Past that point,
fV increases rapidly until p ≈ 0.3. At p = 0.35, all bubbles are connected to a free surface for all
configurations and parameters considered.
    The effect of variation in N on the interconnection and venting of the bubbles was also considered
by varying the number of bubbles in the simulation initial conditions to obtain N = 3.75 × 1014 /m3
and N = 4.5×1014 /m3 . As discussed in Ref. [10], decreasing N to values lower than N = 3×1014 /m3
in the initial conditions results in spinodal decomposition of the matrix phase between the bubbles
placed in the initial conditions due to the use of a simplified Cahn-Hilliard description of the


                                                                5
     1                                                      1


    0.8                                                    0.8


    0.6                                                    0.6


    0.4                                                    0.4


    0.2                                                    0.2


     0                                                      0
          0       0.1         0.2         0.3    0.4             0         0.1       0.2          0.3   0.4


                (a) N = 3.75 × 1014 /m3                                  (b) N = 4.5 × 1014 /m3

Figure 3: Fraction of total bubble volume that is connected to a free surface, fV , as a function of
porosity p for (a) N = 3.75 × 1014 /m3 and (b) N = 4.5 × 1014 /m3 , with M = 1.

                M       N (m−3 )      Mean pc   Std. dev. pc         Mean p0.8   Std. dev. p0.8
                1       3 × 1014      0.262     0.00722              0.279       0.00338
                2.5     3 × 1014      0.255     0.00623              0.268       0.00930
                5       3 × 1014      0.261     0.0115               0.281       0.0149
                1       3.75 × 1014   0.248     0.00872              0.272       0.00284
                1       4.5 × 1014    0.249     0.0134               0.264       0.00391


Table 1: Mean percolation threshold (pc ) and mean porosity at which fV = 0.8 (p0.8 ) for the five
initial condition configurations considered, and corresponding standard deviations, for each set of
simulation parameters.


free energy; such behavior is not expected physically in the U-Zr system, so simulations with
N < 3 × 1014 /m3 are not considered further here. As can be seen in Fig. 3, for the cases with larger
N , the trends in fV versus p are similar to those observed for N = 3 × 1014 /m3 in Fig. 2a, although
for larger N , there appears to be less variation between the curves for each configuration.


   2.2        Determination of parameters for UPuZrGaseousEigenstrain
As described in Section 2, the BISON model UPuZrGaseousEigenstrain decreases the rate at which
fission gas atoms are added to bubbles linearly in the range pi < p < pt . In this section, we describe
how values for pi and pt are determined from the phase-field simulation results. As discussed in
Ref. [10], we assume that significant gas release cannot occur from the internal volume of the fuel
to the free surface until the percolation threshold, pc , is reached. The percolation threshold in this
case is the porosity at which a continuous pathway through the bubble phase exists that connects
the domain boundaries at x = 0 µm and x = 72 µm. Since we assume significant gas release cannot
occur prior to p = pc , the BISON model parameter pi should be set equal to the mean value of pc
determined for a representative microstructure.
     The mean value of pc for the five different configurations and its standard deviation are shown
in Table 1 for each set of simulation parameters considered. Although the mobility of the defect

                                                       6
species M has not been physically parameterized for the simplified model employed in this work,
the data of Table 1 shows that the mean values of pc are very close to each other for the different
mobilities M = 1, 2.5, 5 and constant N = 3 × 1014 /m3 . The total variation in mean pc for the
different mobility cases is comparable to the standard deviation in each of the individual values
(although it should be noted that a larger number of samples should ideally be considered when
determining statistical quantities such as the standard deviation). Therefore, we conclude that
although the defect species mobility does result in significant differences in the microstructure for
different mobility [10], the resultant value of pc does not vary significant with changes in M , at
least for the range of values considered here. Therefore, we choose pc = 0.262 as a representative
value from the M = 1 case. Assuming pi = pc as previously discussed, the recommended value of
pi for BISON simulations is 0.262.
    Although N = 3 × 1014 /m3 is based on the best available experimental data, this value may
vary due to temperature, Pu content, and other factors. Therefore, the effect of variation in N was
also considered by simulating initial conditions with N = 3.75 × 1014 /m3 and N = 4.5 × 1014 /m3 .
As shown in Table 1, pc decreases with increasing N . Therefore, if future experimental data allows
N to be better quantified, additional simulations to further quantify the effect of N should be
performed.
    To determine pt for BISON simulations, we use the fact that post-irradiation examination of
EBR-II fuel rods showed that fission gas release plateaued at approximately 80% of the fission gas
produced [5]. We therefore set pt to the porosity p at which fV = 0.8, which we refer to as p0.8 . The
mean and standard deviation of p0.8 for the different cases considered are also shown in Table 1.
The mean value of p0.8 also does not vary strongly with M , so again using the M = 1 case as
representative, the recommended value of pt for BISON simulations is 0.279. Similar to the trend
observed in pc , the mean value of p0.8 decreases with increases in N .


                     2.3 Determination of parameters for
                   ADFissionGasViscoplasticityStressUpdateBase
The BISON base class ADFissionGasViscoplasticityStressUpdateBase and classes derived from
it implement the swelling model of Ref. [3]. In the base class, an interconnectivity function I(p)
is used to decrease swelling and increase fission gas release based on the fraction of bubbles that
are connected to an external surface. In this section, we describe how I is determined from the
phase-field simulation results of Section 2.1.
    The plots of fV versus p in Section 2.1 give the fraction of bubbles that are connected to a
free surface, which can be used to parameterize I(p). For each of the simulations in Section 2.1, a
function of the form                                           
                                          1             p − pcen
                                    fV =      1 + erf                                           (2)
                                          2                ∆
was fit to the data, where erf is the error function, pcen is the center of the distribution, and ∆
is the characteristic width of the distribution. As mentioned in Section 2.1, fV is non-zero in the
initial conditions due to the initial random placement of the bubbles and non-zero initial bubble
radius. To account for this, simulation data with p < 0.1 was excluded from the fit.
    An example of simulated fV versus p and the corresponding fV fit from it is shown in Fig. 4
for Configuration 1, M = 1, N = 3 × 1014 /m3 . In this case, pcen = 0.269 and ∆ = 0.0392. With
the exception of an early increase in fV at p ≈ 0.2, Equation 2 appears to represent the data well.
This early increase was not observed in all configurations.
    A similar fit was performed for each configuration and set of simulation parameters considered.


                                                  7
                         1


                       0.8


                       0.6


                       0.4


                       0.2


                         0
                             0        0.1             0.2        0.3        0.4


Figure 4: Fraction of total bubble volume that is connected to a free surface, fV , as a function of
porosity p for (a) M = 1, (b) M = 5.

             M     N (m−3 )      Mean pcen    Std. dev. pcen     Mean ∆   Std. dev. ∆
             1     3 × 1014      0.262        0.00707            0.0336   0.00769
             2.5   3 × 1014      0.247        0.00979            0.0360   0.0149
             5     3 × 1014      0.259        0.00936            0.0397   0.0112
             1     3.75 × 1014   0.249        0.00314            0.0367   0.00533
             1     4.5 × 1014    0.244        0.00448            0.0309   0.00668


Table 2: Mean pcen and ∆ for the five initial condition configurations considered and corresponding
standard deviations for each set of simulation parameters.


The mean of pcen and ∆ for the five configurations and corresponding standard deviations are
given in Table 2 for each set of simulation parameters considered. The mean values of pcen and
∆ determined for the different mobility cases are again close to each other, although in this case
pcen for M = 2.5 lies slightly outside of one standard deviation from the values determined for
M = 1 and M = 5. However, due to the lack of an apparent trend with M and the effect of the
small sample sizes used, we believe that, similar to the percolation threshold, M does not strongly
influence pcen , and choose M = 1 as a representative mobility value for consistency with Section
2.2. There does appear to be a decrease in pcen with increasing N , pointing to the need for further
simulations with different N if improved experimental measurements of N become available.
    Using the fit data for M = 1, N = 3 × 1014 /m3 , I(p) can be determined. The functional form
for I(p) used in BISON is [3]
                            
                            0
                                                             p ≤ pstart
                                 5          4          3
                      I(p) = 6pnorm − 15pnorm + 10pnorm pstart < p < pend                        (3)
                            
                              1                               p ≥ pend
                            

                                                  p − pstart
                                       pnorm =                                                   (4)
                                                 pend − pstart

                                                  8
                           1
                                   erf
                                   smooth step
                        0.8

                        0.6

                        0.4

                        0.2

                           0
                               0        0.1            0.2        0.3          0.4


Figure 5: Comparison of I(p) (smooth step function of Eq. 3) and fV (Eq. 2) with parameters
based on fit to phase-field simulations.


where pstart is the interconnection initiating porosity and pend is the interconnection terminating
porosity. Thus, the free parameters to be determined are pstart and pend . To determine these values,
a MATLAB script was written that varied pstart and pend to determine what values minimized the
least-squares error between Eq. 3 and Eq. 2 with pcen = 0.262 and ∆ = 0.0336. This resulted in
pstart = 0.2026 and pend = 0.3219. A plot of the smooth step function I(p) with these parameters
and Eq. 2 is shown in Figure 5. The least-squares minimization process results in good agreement
between Eq. 2 and 3 for the given parameters.


                                        2.4     Summary
In this section, phase-field simulations were used to study bubble growth and interconnection in the
high-temperature regime of U-(Pu)-Zr fuel. The model used a simplified description of the physics
based on the Cahn-Hilliard equation with a source term. The source term was held constant and
the defect species mobility M and initial number density of bubbles N was varied to determine their
effect. Although changing M resulted in significant changes in the microstructure [10], it did not
result in significant changes to the calculated values of the percolation threshold pc , the porosity at
which 80% venting occurs p0.8 , or the parameters of Eq. 2 that describes fV versus p. Changes in
N did result in small changes to these parameters; thus, if improved experimental measurements of
N become available, new simulations should be performed using those values as initial conditions.
    The data from the phase-field simulations was used to determine parameters for two models of
gaseous swelling of U-(Pu)-Zr fuel in BISON. For the model UPuZrGaseousEigenstrain, the inter-
connection initiating porosity pi = 0.262 and the interconnection terminating porosity pt = 0.279.
For the model ADFissionGasViscoplasticityStressUpdateBase and classes derived from it, the
interconnection initiating porosity pstart = 0.2026 and the interconnection terminating porosity
pend = 0.3219.




                                                   9
                               3    Low temperature swelling

                                         3.1     Introduction
In this section, the evolution of porosity within α-uranium during irradiation and plastic deforma-
tion is investigated by studying the deformation of polycrystalline α-uranium with pores located
on triple points. Crystal plasticity is employed to model plastic deformation, while the influence
of irradiation-induced eigenstrains is investigated with linear elasticity. Irradiation-induced eigen-
strains are found to significantly increase the volume and the aspect ratio of porosity, while plastic
deformation does not significantly change either quantity.

                                             3.2      Models
The crystal plasticity model of α-uranium is implemented within the MARMOT finite element
code. This model is based on the physics-based, mean-field crystal plasticity model implemented
within the viscoplastic self-consistent (VPSC) code developed by Los Alamos National Laboratory
[14, 15]. The MARMOT model also includes some modifications presented in Ref. [16], primarily
temperature dependence of the plastic behavior; however, the exact form of the temperature de-
pendence has been developed for this work. Both the VPSC model and the finite element model
are based on dislocation motion within slip systems. While the VPSC model computes the be-
havior of a polycrystalline material by iteratively solving for each grain within an averaged matrix
of material, the MARMOT implementation spatially resolves each grain and solves for the local
displacements in the material.
    The crystal plasticity model is based on dislocation density evolution. The model is implemented
in MARMOT via the UserObject-based crystal plasticity system. The model incorporates both
slip and twinning and is briefly summarized here. Following the notation in Ref. [16], each slip
system is denoted by α, where α = 1...8, and each twin system is denoted by β, where β = 1, 2.
Wall slip occurs for α = 1, floor slip for α = 2, chimney slip for α = 3, 4, roof slip for α = 5...8,
and the {130} twin system is for β = 1, 2. A summary of the slip and twin systems are given in
Refs. [14, 15, 16]. The slip rate, γ̇, for a given system, α, is given as [15]
                                                    τ α 1/m
                                        γ˙α = γ̇0           sign (τ α )                                   (5)
                                                    τ0α
where m is the rate sensitivity parameter, γ̇0 is the reference slip rate, τ α is the resolved shear
stress on the slip system, and τ0α is the threshold stress of the slip system. The twin slip rate is
treated similarly. However, the twin systems are denoted by β, with
                                      
                                                 1/m
                                             τβ
                                                                τ0β > 0
                                      
                                                     sign τ β
                                                              
                                        γ̇
                                      
                                ˙β
                               γ =         0
                                             τ β
                                               0

                                                                τ0β < 0
                                      
                                      0

because twinning is not expected to operate under compressive stress. The critical resolved shear
stress is given as [15, 16]
                                    τcα = Γ τ0α + τfαor + τsub
                                                           α
                                                               
                                                                                              (6)
where τcα is the friction stress, τfαor is the stress arising from the presence of forest dislocations, τsub
                                                                                                         α is

the stress arising from the presence of a dislocation substructure, and Γ is a temperature-dependent
factor for hardening. The stress from forest dislocations is given as [15]
                                                            q      
                                             τfαor = χbα µα ραfor                                          (7)

                                                      10
where χ = 0.9, bα is the Burgers vector, µα is the shear modulus of the slip system, and ραfor is the
dislocation density of the forest dislocations on the slip system. The expression for Γ is [16]
                                                            
                                                     T − T0
                                         Γ = exp −                                                (8)
                                                        B

where T is the temperature, T0 = 293 K is a reference temperature, and B = 350 K is a scaling
factor. The stress arising from dislocations stored in substructures is given as
                                                                 
                                  α       α α√               1
                                 τsub = kb µ ρsub log α √                                 (9)
                                                          b ρsub

where k = 0.086. The forest dislocation densities are evolved with time as [16]
                                                     q                  
                                 ρ̇αfor = k1 |γ̇ α |    ραfor − dα ραfor                        (10)

where                                                                    
                                  α                   kB T           ˙0
                                 d    = dα0       1 + α α 3 ln                                  (11)
                                                     D (b )           ˙
kB is the Boltzmann constant, Dα is a drag stress, and ˙0 = 107 s−1 . The substructure dislocation
density is evolved with time as [15, 16]
                                           X       √
                                 ρ̇sub = q   f α bα ρsub |γ̇ α | dα ραfor                      (12)
                                              α

where q is a rate coefficient and f α is a dislocation recovery rate coefficient. The values of the
parameters for the slip systems are given in Ref. [16].
   The burnup eigenstrain follows that described previously [7]. In that model, the irradiation
growth strain tensor of a single crystal of α-U, β , is written as
                                                         ∂β
                                                  β =       β                                  (13)
                                                         ∂β
        ∂
where ∂ββ is a constant for irradiation induced growth strain and β is the burnup. The irradiation-
induced growth strain is related to the growth coefficients Gi [6] as
                                                                
                                           G[100]   0       0
                                 ∂β
                                      = 0        G[010]    0 .                               (14)
                                  ∂β
                                             0      0     G[001]
The anisotropic growth coefficient for a single crystal is approximated at 423 K with G[100] = −420,
G[010] = 420, and G[001] = 0 [6].


        3.3    Mesh generation and assignment of grain orientation
Finite element modeling of polycrystalline material with this crystal plasticity formulation requires
meshes that conform to the grain structure. Each grain within the polycrystalline structure is a
unique mesh block and the interface between the grains is sharp. The conformal mesh of the grain
structure is generated via several steps using the Sculpt and Cubit software tools from Sandia
National Laboratory [17]. First, a phase field simulation of grain growth generates a realistic
diffuse-interface equiaxed structure. Next, this structure is transformed into a Sculpt data file.

                                                      11
                  (a)                             (b)                            (c)

Figure 6: The grain structure used in this work. a) The solid surface, with each grain a different
color. b and c) The mesh, to demonstrate grain boundaries and pores. One pore is located in the
center of the image in b), while two pores are visible in c).


The grain structure is sampled at regular intervals in a rasterized fashion to generate a data file
containing point positions and values of all order parameters at each point. Porosity can be added
to the grain structure by modifying the data file such that all of the order parameter values are zero
within the region of the pore. Sculpt is then used to generate a sharp-interface mesh of the grain
structure. Finally, Cubit is used to specify boundaries on the mesh so that mechanical boundary
conditions can be applied. The grain structure used in this work is shown in Fig. 6 with zero pores
shown in Fig. 6a, one pore (Fig. 6b) and two pores (Fig. 6b).
    In this work, a single grain structure is created from one phase field simulation that contains
five grains. Each grain in the mesh is assigned Euler rotation angles, such that a five-grain list of
Euler angles is called a group. To study different grain structures, the group of Euler rotation angles
are changed. Grain orientation information is assigned during the MOOSE-based simulation. A
data file is provided that specifies the Euler angles of the rotation of each grain. Grain structures
with zero, one, and two pores located on triple points are created, with the same group of Euler
angles applied to the microstructures with pores as to the one without. One combination of three
microstructures with the group of Euler angles is termed a set of microstructure variations.


                                          3.4    Results
The results of this study indicate that the accumulation of irradiation-driven, macroscopic crystal
eigenstrain drives the expansion of existing porosity, while plastic flow does not contribute to volume
changes.
     To examine the effect of burnup eigenstrain, three sets of microstructure variations are simulated
at 373 K. Only one temperature is studied because burnup eigenstrain is expected to be constant
with temperature over the range of 110 K - 550 K [18]. The simulations do not capture plastic flow
and therefore are not quantitative; however, they do reveal the general impact of irradiation-driven
eigenstrain on porosity evolution in α-uranium. In these simulations, mirror boundary conditions
are applied to three faces of the computational domain, while the other three faces are allowed
to displace freely. Burnup reached a maximum of 0.1% FIMA, corresponding to β11 = −0.42,
β22 = 0.42, β33 = 0. The evolution of the percent volume change of the porosity with burnup in
shown in Fig. 7 for the three variations simulated of microstructures with one and two pores. The


                                                  12
                         (a)                                          (b)

Figure 7: The change in pore volume for the simulations of burnup-generated eigenstrain. a) For
the three variations of Euler angles with one hole in the structure. b) For the three variations of
Euler angles with two holes in the structure.


clearest observable trend is that the volume of the porosity ultimately increases with increasing
burnup, particularly when more than one pore is present. In addition, the simulations indicate
that continuing burnup causes elongation of pore structures. The change in the pore structure is
illustrated in Fig. 8 for one variation at zero burnup (Fig. 8a) and at a burnup of 0.1% (Fig. 8b).
    The effect of plastic flow on porosity is studied at 373 K, 473 K, 573 K, 673 K, 773 K, and 873
K for three sets of microstructure variation. In these simulations, one face of the computational
domain undergoes uniform, increasing compressive strain that increases with time, while an adjacent
face experiences a uniform, increasing tensile strain equal in magnitude to the compressive strain.
The strains are given as linear approximations of the burnup strains as

                                    x = ln(3.454 × 10−8 t + 1)                               (15)

for the tensile strain on the computational domain boundary normal to the x-axis and

                                   y = ln(−3.339 × 10−8 t + 1)                               (16)

for the compressive strain on the computational domain boundary normal to the y-axis. These
linear approximations lead to small deviations from the actual burnup eigenstrain of approximately
3% that decrease to zero at a time of 1 × 106 s (strain magnitude of 0.034) and increase at times
greater than that. These expressions correspond to a burnup of 8.07 × 10−8 s−1 , on the order of
the burnup rate in EBR-II.
    The primary trend of importance is that the pore volume change is not generally impacted
by the temperature and large changes in pore volume do not occur. The pore volumes for one
pore are shown in Fig. 9, while the pore volumes for two pores are shown in Fig. 10. Some minor
variation is observed in pore volume, generally a small loss of volume, although in some cases pore
volume initially increased, then decreased; or in the case of a single pore, volume increased. If


                                                13
                          (a)                                             (b)

Figure 8: The change in the pore structure with burnup-generated eigenstrain. a) The initial grain
and pore structure before the accumulation of burnup-generated eigenstrain. b) The grain and pore
structure after the accumulation of 0.1% burnup. The pores are evidently elongated.


there is a temperature dependence of volume change, generally the change in volume is larger at
lower temperatures. The small reduction in variation in pore volume is due to the approximation
of the contraction and expansion eigenstrains as linearly increasing compressive and tensile applied
strains. As a result, we conclude that plastic strain does not impact the volume of existing porous
structures. In addition, the pore structure qualitatively is not affected much. Minor pore elongation
occurs, but the deformation of the pore structures with plastic flow can be related to the macroscopic
applied strain (compression in one direction and elongation in the normal direction would naturally
lead to elongation of initially spherical shapes).


                                        3.5     Summary
In this section, the effect of irradiation-induced crystallographic eigenstrain and plastic flow on pre-
existing porous structures within polycrystalline α-uranium. Irradiation-induced eigenstrain drives
the increase in the volume of pores and the elongation of pores. Plastic flow does not appreciably
change the volume of pores nor the geometry of the pores. From these results, it is apparent that
burnup eigenstrain is a major driver of porosity structure evolution, while plastic flow that results
from biaxial tension and compression will not close existing porosity at any temperature. Further
research into the mechanisms that cause pores or tears to initially form and to grow is needed.
The high stresses that form at grain boundaries and fission gas accumulation and pressurization
can cause the formation of initial porosity and cause pores to grow more than predicted in this
work. The mechanism irradiation-driven burnup eigenstrain accumulation is also currently under
investigation, and insight is needed for the temperature dependence of the eigenstrain accumulation
and any dependence it may have on internal stress state within the material.




                                                  14
Figure 9: The variation in the pore volume for the top) first, middle) second, and bottom) third
variations in this work for a one-pore structure at multiple temperatures.




                                              15
Figure 10: The variation in the pore volume for the top) first, middle) second, and bottom) third
variations in this work for a two-pore structure at multiple temperatures.




                                               16
                                   4    Cluster dynamics

                                       4.1     Introduction
Fission gas bubble formation is known to be the dominant mechanism of high temperature swelling
in the body-centered cubic (bcc) γ phase of U-Zr-based metallic fuels. The bubbles and swelling
affect physical properties of metallic fuels, such as the degradation of thermal conductivity and
mechanical integrity. Such fission gas bubble forms at the central region of the metallic fuel where
temperature is higher and the thermodynamically stable phase of bcc γ dominates [19].
    At the early stage, the gas bubbles form and nucleate as an initial form of small fission gas
atom clusters. They grow in number density and size with time due to the production of fission
gas atoms during reactor operation or burnup. A large amount of gas atoms in lattice segregate to
form clusters because of the extremely low solubility of fission gas in the γ phase, which provides
large chemical driving force of cluster nucleation. After stable clusters nucleate out in the matrix,
lattice diffusion mediated by point defects controls the growth of the cluster size.
    This work performs an initial development of a mesoscale model based on cluster dynamics
to investigate the early-stage of fission gas cluster nucleation and growth. The objective is to
provide useful time-dependent trends such as cluster/bubble size and number density and to inform
engineering scale simulations of swelling models employed within BISON. The cluster dynamics
method is an efficient rate theory model constructed by a large set of master equations [20, 21]. It
tracks the evolution of cluster size distribution or population as a function of time or fluence. The
model considers multiple events of cluster reactions including emission, dissociation, adsorption,
and combination, thus providing the capability to study early-state complex nucleation processes.
The approach is of particular interests for modeling from nano-size solute/defect clustering to large
second-phase particle coarsening. In this simulation study we focus on the cluster formation of
Xe gas atoms in the high-temperature γ matrix phase. With appropriate parameters of reaction
thermo-kinetics, the model can be extended to consider other types of fission gas atoms or matrix
phases.


                                         4.2    Methods
The cluster dynamics model developed in this work considers Xe self clustering and vacancy clus-
tering coupled by the vacancy-mediated Xe diffusion, with the assumption that the monomers of
Xe and vacancy contribute to the transport of reaction species. Specifically, the non-equilibrium
vacancy concentration is solved in every time step and incorporated into the calculation of the Xe
diffusion coefficient. The recalculated Xe diffusion coefficient is then used to update the reaction
coefficients of Xe clustering.
    For Xe self clustering, the master equation for changes in the number density of such clusters
in size n (fn ) as a function of time is described as

                                       ∂f1Xe         X
                                             = GXe
                                                1  −    Xe
                                                       J1→m                                      (17)
                                        ∂t
                                                      m>1

                                ∂fnXe X Xe      X
                                                   Xe
                                     =   Jp→n −   Jn→q (n > 1)                                   (18)
                                 ∂t    p        q

Here GXe1 is the Xe monomer generation rate, which is defined as the product of fission yield of Xe
and fission rate. Jp→n is the flux associated with the cluster reaction from the cluster of class p to


                                                 17
class n (p < n < q). The cluster flux can be described by
                                                +         −
                                        Jp→n = ωp,n fp − ωn,p fn                                (19)
               + are the rates of adsorption reactions for clusters of size p to grow to size n, and
Coefficients ωp,n
              −
coefficients ωn,p are the rates of emission reaction for clusters of size n to shrink to size p. The
same description applies similarly to the reaction flux Jn→q .
   For vacancy clustering, the master equations are similar to Eqs.(17), (18), and (19), except that
additional terms including the reactions of sinks and mutual recombination of point defects are
needed to describe the evolution of vacancy monomers. The master equation for vacancy clustering
can be expressed as
          ∂f1Va   ∂CVa        X
                                 Va
                =      = GVa
                          1 −   J1→m − ks DVa CVa − 4π(rVa + rI )(DVa + DI )CVa CI              (20)
           ∂t      ∂t
                                  m>1

                               ∂fnVa X Va      X
                                                  Va
                                    =   Jp→n −   Jn→q (n > 1)                                   (21)
                                ∂t    p        q

where GVa1 is the vacancy generation rate caused by irradiation, CVa and CI are the concentrations of
vacancy and interstitial, respectively, ks is vacancy sink strength, and rVa and rI are recombination
                                                                            Va
radii for vacancies and interstitials, respectively. Note that the term −J1→m   can be viewed as the
sink contribution caused by vacancy clustering. No sink bias between vacancies and interstitials is
assumed thus DVa CVa = DI CI can be applied into the last term of Eq.(20).
    One important assumption is made in this work that only the monomers of Xe atom and vacancy
are mobile (n − p = q − n = 1). The assumption is now known to be not fully correct, as several
simulation studies have proposed that the XeVa2 complex is possibly mobile in bcc U10Mo [22].
This type of solute-defect complex, if stable at the high temperature burnup condition, can provide
an additional diffusion pathway for Xe to migrate by vacancy-assisted mechanisms. However, the
evaluation of the XeVa2 formation energy, cluster mobility, stability, reaction pathways of mixed
clusters (with both Xe and Va) remains unexplored either experimentally or computationally. The
evaluation and application of this complex mobility are outside the scope of this work. It is
planned to construct the capability to handle mixed cluster reactions and mobility, allowing future
applications to incorporate verified mechanisms and parameters.
                                                               +
    For cluster reactions controlled by monomer diffusion, ωn,n+1    can be expressed by

                                      +
                                     ωn,n+1 = 4π(rn + r1 )D1 f1                                 (22)
                                                                                              −
where rn and r1 are the reaction radii and D1 is the diffusion coefficient of Xe or vacancy. ωn+1,n
                                                  +
can then be described by the given relation with ωn,n+1  [23]
                                        +
                                       ωn,n+1
                                                                             
                             −                        G1 + Gn − Gn+1
                            ωn+1,n =            exp −                                           (23)
                                          Ω                 kT
where Ω is the atomic volume of a Xe atom or vacancy, and Gn is the free energy of the cluster n.
The typical expression of Gn can be expressed as [23]
                                                               2/3
                                                           3Ω
                                  Gn = nµd + 4πσ                       n2/3                     (24)
                                                           4π
where µd is the chemical potential of Xe or vacancy in the cluster phase and σ is the interface
energy or surface tension. The first and second terms of Eq.(24) represent the bulk and interface

                                                  18
contribution of the cluster free energy, respectively. Note that DXe in Eq.(22) is coupled with the
nonequilibrium vacancy concentration determined by Eq.(20).
   The above cluster dynamics master equations with vacancy cluster coupling are formulated in
the Xolotl codes under the U-Zr branch. Xolotl is a continuum-scale cluster dynamics simulator
developed by Oak Ridge National Laboratory [24, 25, 26]. The master equations are solved by the
PETSc package bundled within Xolotl.


                                        4.3     Results
Given that many necessary thermodynamic and kinetic parameters of Xe and vacancy clustering are
either uncertain or unexplored for U-Zr metallic fuels, this work does not aim to build a predictive
or surrogate model. Instead, the activity focuses primarily on constructing the cluster dynamics
coupling framework and showing the sensitivity of various parameters and resulting trends. The
simulation using correct parameters is of significant importance but it is beyond the scope of this
work. Nevertheless, by utilizing parameters within their reasonable ranges, the model is able to
capture important physical events and demonstrate the trend of results. The physical parameters
used in this study are listed in Table 3. Note that the parameters except fission rate and yield are
uncertain at the present moment. The parameters listed in Table 3 are based on available studies
of similar system with a reasonable range of adjustment.

  Table 3: Physical parameters used in the simulation of Xe and vacancy clustering at 1000 K.

                    Parameter                             Value        Unit
                    Xe cluster interface energy            0.30       J m−2
                    Xe solubility                         10−10          -
                    Vacancy cluster interface energy       0.30       J m−2
                    Vacancy formation energy                1.2         eV
                    Vacancy migration barrier               1.0         eV
                    Xe migration barrier                    0.5         eV
                    Fission yield                         0.3017         -
                    Fission rate                       2.5 × 10−9    nm s−1
                                                                       −3

                    Lattice parameter                      0.35        nm
                    Recombination radius                   0.20        nm
                    Dislocation density                  2 ×1013       m−2
                    Cutoff cluster size                     10        atoms
                    Xe density in bubble                  10.16       nm−3

    Fig. 11a and 11b show the time evolution of number density and mean radius of Xe clusters
from 103 to 106 s using the parameters listed in Table 3. The time reaching the onset of Xe cluster
nucleation is between 2 × 104 s and 3 × 104 s. The cluster number density becomes saturated at
5 × 104 s and maintains at the number density 4 × 10−8 nm−3 (or 4 × 1019 m−3 ). The mean
radius of the Xe cluster increases since the nucleation takes place and can reach 7–8 nm in 106 s
driven by the vacancy mediated process.
    Fig. 12 demonstrates the evolution of Xe and vacancy cluster size distribution from 105 to 106
s. The result does not show a pronounced microstructure feature of Xe cluster coarsening. The
non–coarsening feature can be observed in Fig. 11a as well (no decrease in number density after
4 × 105 but increase in mean radius). This can be explained by the unlimited source of Xe atoms
caused by fission. It maintains the chemical driving force for continuous nucleation and growth of

                                                19
                        (a)                                               (b)

Figure 11: Plots of cluster dynamics modeling results showing the time evolution of (a) number
density and (b) mean radius of Xe clusters at 1000 K.




Figure 12: Plots showing the evolution of the Xe and vacancy cluster size distributions at 1 × 105 ,
5 × 105 , and 1 × 106 s.


Xe clusters. Note that the vacancy cluster has a very small range of size distribution (at the region
< 0.5 nm in Fig. 12) and reaches a steady state much faster than Xe clustering.
     The time evolution of Xe and vacancy monomer concentrations is shown in Fig. 13. The Xe
monomer concentration increases significantly to 1.7 × 10−5 nm−3 before the onset of Xe cluster
nucleation (between 2 × 104 s and 3 × 104 s). After Xe clusters rapidly nucleate, they act as a sink
of Xe atoms and thus the Xe monomer concentration starts to decrease. It is expected that the
Xe monomer concentration may reach a steady state after 106 s due to the competition between
fission gas production and Xe clustering. In contrast, the vacancy monomer concentration shows
a constant trend throughout the whole simulation time. It suggests that due to the combined
effects of dislocation sinks, recombination, and vacancy cluster sinks, a steady state condition can
be reached much faster than that of Xe monomers.
     The following paragraphs show the individual effect of various parameters of interests, including
the Xe cluster interface energy, Xe solubility in matrix, vacancy cluster interface energy, vacancy


                                                 20
Figure 13: Plots showing the time evolution of Xe monomer and vacancy monomer concentrations.




                       (a)                                                (b)

Figure 14: Plots of modeling results showing the effect of Xe cluster interface energies (0.20, 0.25,
0.30 J m−2 ) on the time evolution of (a) number density and (b) mean radius of Xe clusters at
1000 K.


formation energy, and vacancy migration barrier. The comparison is based on the simulation result
described above using parameters listed in Table 3 unless stated otherwise.
    Fig. 14 shows the effect of Xe cluster interface energy on the evolution of number density and
mean radius of Xe clusters. Decreasing the interface energy causes earlier onset and higher rate
of nucleation. It enhances a higher density of small Xe clusters. Thus the mean radius increases
slower with the decrease of interface energy. The overall effect of decreasing interface energy is
similar to that of increasing the Xe solubility in matrix. The effect of Xe solubility is shown
in Fig. 15. Generally, decreasing Xe solubility enhance the chemical driving force of clustering
or cluster nucleation. It causes an earlier onset of nucleation and higher nucleation rate. The
comparison between Fig. 14 and Fig. 15 suggests that a 0.05 eV of interface energy decrease results
in a similar effect as 1/10 of Xe solubility, particular for the latter stage of nucleation process
reaching the steady state cluster density.


                                                 21
                        (a)                                               (b)

Figure 15: Plots of modeling results showing the effect of Xe solubility (10−13 – 10−10 ) on the time
evolution of (a) number density and (b) mean radius of Xe clusters at 1000 K.




                        (a)                                               (b)

Figure 16: Plots of modeling results showing the effect of vacancy migration barrier (0.6 - 1.2 eV)
on the time evolution of (a) number density and (b) mean radius of Xe clusters at 1000 K.


    The effect of vacancy migration barrier is shown in Fig. 16. Decreasing the barrier causes higher
vacancy hopping rates that enhance the annihilation process of point defects by recombination and
sinks. It decreases the non-equilibrium vacancy concentration during irradiation, thereby slowing
down the overall nucleation rate and delaying the nucleation onset. The evolution of cluster density
and size shift to the later time as the vacancy migration barrier decreases. Note that decreasing
vacancy migration barrier also causes an increase of steady-state number density and decrease of
mean radius. This unexpected feature is caused by the accumulation of total Xe atoms produced
by fission. The delay of Xe clustering causes that the nucleation happens at a higher Xe monomer
concentration as the fission rate and yield are constant and independent of vacancy migration
barrier. The accumulated high Xe monomer concentration then increases the nucleated cluster
density and reduces the averaged size, as observed in Fig. 16.
    Contrary to the pronounced effect of vacancy migration barrier on Xe cluster evolution, the
sensitivity of vacancy clustering thermodynamic parameters is rather small. Fig. 18 and Fig. 17
show the effects of vacancy formation energy and cluster interface energy on the Xe cluster evolution,
respectively. For the range of these two parameters considered, the effect on Xe clustering is very

                                                 22
                       (a)                                             (b)

Figure 17: Plots of modeling results showing the effect of vacancy cluster interface energy (0.1 –
0.5 J m−2 ) on the time evolution of (a) number density and (b) mean radius of Xe clusters at 1000
K.




                       (a)                                             (b)

Figure 18: Plots of modeling results showing the effect of vacancy formation energy (0.6 – 1.4 eV)
on the time evolution of (a) number density and (b) mean radius of Xe clusters at 1000 K.


minor. It indicates that the concentration of vacancy monomer is determined by kinetics more
significantly than thermodynamics given the considered parameters and radiation damages.


                    4.4      Summary and concluding remarks
In this work, a cluster dynamics model is developed to characterize the early-stage of fission gas
cluster nucleation and growth. The model couples vacancy clustering and Xe clustering together
to provide a physics-based evaluation of mobile vacancy monomer concentration and radiation-
modified Xe diffusion rate. The simulation results show Xe clustering strongly depends on param-
eters including Xe solubility, Xe cluster interface energy, and migration barrier of vacancy. The
sensitivity of other parameters such as vacancy formation energy and vacancy cluster interface
energy is not as important. Note that there remain several limitations and challenges to provide
high-fidelity Xe cluster/bubble modeling. These include the consideration of potentially mobile
mixed clusters like XeVa2 as well as temperature and size dependence of parameters like interface

                                               23
energy. Atomistic modeling techniques such as density functional theory (DFT) and molecular
dynamics (MD) are highly required to reduce the uncertainty. MD may be a better modeling tool
than DFT for modeling γ U-Zr as the phase is not thermodynamically stable at 0 K. The work
can also be improved significantly if combined with systematic advanced characterizations of the
defect and bubble evolution. One discrepancy found between modeling and available experiment
data is that the latter observed evident decrease of Xe bubble number density as time reaches
higher than 107 s. This feature is not observed in the simulation as the time is extended to > 107
s. This indicates that additional physics or complex cluster reaction types, such as cluster/bubble
coalescence [27], may be involved during the later stage of cluster/bubble growth. This reaction
type has not been considered in the current model for early-stage clustering.




                                                24
                                       5    References
 1. Gerard L Hofman, RG Pahl, CE Lahm, and DL Porter. Swelling behavior of U-Pu-Zr fuel.
    Metallurgical Transactions A, 21(2):517–528, 1990.

 2. Stephen R. Novascone, Albert Casagranda, Larry K. Aagesen, Benjamin W. Beeler, Wen Jiang,
    Andrea M. Jokisaari, Dylan J. McDowell, Alexander D. Lindsay, James B. Tompkins, G. Pa-
    store, Adam X. Zabriskie, D. Schwen, Richard L. Williamson, Benjamin W. Spencer, and
    Andrew E. Slaughter. Summary of Bison milestones and activities - NEAMS FY19 Report.
    Technical Report INL/EXT-19-55699, Idaho National Laboratory, Idaho Falls, ID, 2019.

 3. Christopher Matthews and Cetin Unal. Initial implementation of a bubble-surface force-balance
    fission gas behavior algorithm for metallic nuclear fuel into BISON. Technical Report LA-UR-
    19-31814, Los Alamos National Laboratory, Los Alamos, NM, 2019.

 4. Dawn E Janney, Cynthia A Papesch, Douglas E Burkes, James I Cole, Randall S Fielding,
    Steven M Frank, Thomas Hartmann, Timothy A Hyde, Dennis D Keiser Jr, J Rory Kennedy,
    et al. Metallic fuels handbook, part 1: Alloys based on U-Zr, Pu-Zr, U-Pu, or U-Pu-Zr, including
    those with minor actinides (Np, Am, Cm), rare-earth elements (La, Ce, Pr, Nd, Gd) and Y.
    Technical Report INL/EXT-15-36520, Idaho National Laboratory, Idaho Falls, ID, 2017.

 5. GL Hofman, LC Walters, and TH Bauer. Metallic fast reactor fuels. Progress in Nuclear
    Energy, 31(1-2):83–110, 1997.

 6. SH Paine and JH Kittel. Preliminary analysis of fission-induced dimensional changes in single
    crystals of uranium. Technical Report ANL-5676, Argonne National Laboratory, Lemont, IL,
    1958.

 7. AM Jokisaari. Irradiation-induced internal stresses in polycrystalline α-uranium: a mesoscale
    mechanical approach. Computational Materials Science, 176:109545, 2020.

 8. RC Lobb. Void nucleation during thermal cycling of adjusted uranium. Journal of Nuclear
    Materials, 48:67–73, 1973.

 9. A Rezwan, AM Jokisaari, and MR Tonks. Modeling brittle fracture due to anisotropic thermal
    expansion in polycrystalline materials. to be submitted to Computational Materials Science.

10. L. K. Aagesen, B. W. Beeler, A. Casagranda, A. M. Jokisaari, S. R. Novascone, A. Rezwan,
    M. R. Tonks, and Y. Zhang. Marmot modeling of swelling in U-Zr and integration into BISON.
    Report INL/EXT-19-55959, Idaho National Laboratory, 2019.

11. D. R. Olander. Fundamental aspects of nuclear reactor fuel elements. Technical Information
    Center, Energy Research and Development Administration, 1976.

12. T H Bauer. In-Pile Measurement of the Thermal Conductivity of Irradiated Metallic Fuel.
    Nuclear Technology, 110(3):1–15, 1995.

13. Cody J Permann, Michael R Tonks, Bradley Fromm, and Derek R Gaston. Order parameter
    re-mapping algorithm for 3d phase field model of grain growth using fem. Computational
    Materials Science, 115:18–25, 2016.

14. RJ McCabe, L Capolungo, PE Marshall, CM Cady, and CN Tomé. Deformation of wrought
    uranium: experiments and modeling. Acta Materialia, 58(16):5447–5459, 2010.

                                                25
15. Marko Knezevic, Laurent Capolungo, Carlos N Tomé, Ricardo A Lebensohn, David J Alexan-
    der, Bogdan Mihaila, and Rodney J McCabe. Anisotropic stress–strain response and mi-
    crostructure evolution of textured α-uranium. Acta Materialia, 60(2):702–715, 2012.

16. Nicolò Grilli, Alan CF Cocks, and Edmund Tarleton. Crystal plasticity finite element modelling
    of coarse-grained α-uranium. Computational Materials Science, 171:109276, 2020.

17. Hojun Lim, Fadi Abdeljawad, Steven J Owen, Byron W Hanks, James W Foulk, and Corbett C
    Battaile. Incorporating physically-based microstructures in materials modeling: Bridging phase
    field and crystal plasticity frameworks. Modelling and Simulation in Materials Science and
    Engineering, 24(4):045016, 2016.

18. BA Loomis and SB Gerber. Length and electrical resistivity changes of neutron irradiated
    uranium. Philosophical Magazine, 18(153):539–553, 1968.

19. T. Ogata. 3.01 - metal fuel. In Rudy J.M. Konings, editor, Comprehensive Nuclear Materials,
    pages 1 – 40. Elsevier, Oxford, 2012.

20. Vitaly V. Slezov. Kinetics of First-order Phase Transitions, chapter 2, pages 7–38. John Wiley
    Sons, Ltd, 2009.

21. T. Jourdan, G. Bencteux, and G. Adjanor. Efficient simulation of kinetics of radiation induced
    defects: A cluster dynamics approach. Journal of Nuclear Materials, 444(1):298 – 313, 2014.

22. Shenyang Hu, Wahyu Setyawan, Vineet V. Joshi, and Curt A. Lavender. Atomistic simulations
    of thermodynamic properties of xe gas bubbles in u10mo fuels. Journal of Nuclear Materials,
    490:49 – 58, 2017.

23. T. Jourdan, F. Soisson, E. Clouet, and A. Barbu. Influence of cluster mobility on cu precipi-
    tation in -fe: A cluster dynamics modeling. Acta Materialia, 58(9):3400 – 3405, 2010.

24. Sophie Blondel, David E. Bernholdt, Karl D. Hammond, Lin Hu, Dimitrios Maroudas, and
    Brian D. Wirth. Benchmarks and tests of a multidimensional cluster dynamics model of helium
    implantation in tungsten. Fusion Science and Technology, 71(1):84–92, 2017.

25. Dimitrios Maroudas, Sophie Blondel, Lin Hu, Karl D Hammond, and Brian D Wirth. Helium
    segregation on surfaces of plasma-exposed tungsten. Journal of Physics: Condensed Matter,
    28(6):064004, jan 2016.

26. Xolotl - Spatially dependent cluster dynamics simulator.           https://github.com/ORNL-
    Fusion/xolotl.

27. J Rest. Evolution of fission-gas bubble size distributions during high temperature irradiation
    of uranium-alloy fuel. In International conference on fast reactors and related fuel cycles:
    Challenges and opportunities, Jul 2009.




                                                26
