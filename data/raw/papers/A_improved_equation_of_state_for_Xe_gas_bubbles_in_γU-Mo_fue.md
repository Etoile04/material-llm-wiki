# A improved equation of state for Xe gas bubbles in γU-Mo fuels

---

                                                                Journal of Nuclear Materials 530 (2020) 151961



                                                              Contents lists available at ScienceDirect


                                                        Journal of Nuclear Materials
                                              journal homepage: www.elsevier.com/locate/jnucmat




A improved equation of state for Xe gas bubbles in gU-Mo fuels
Benjamin Beeler a, b, *, Shenyang Hu c, Yongfeng Zhang b, Yipeng Gao b
a
  North Carolina State University, Raleigh, NC, 27607, USA
b
  Idaho National Laboratory, Idaho Falls, ID, 83415, USA
c
  Paciﬁc Northwest National Laboratory, Richland, WA, 99354, USA




a r t i c l e i n f o                                  a b s t r a c t

Article history:                                       A monolithic fuel design based on a UeMo alloy has been selected as the fuel type for conversion of the
Received 11 July 2019                                  United States High-Performance Research Reactors (HPRRs). An issue with UeMo monolithic fuel is the
Received in revised form                               large amount of swelling that takes place during operation. The accurate prediction of fuel evolution
2 December 2019
                                                       under irradiation requires implementation of correct thermodynamic properties into mesoscale and
Accepted 16 December 2019
                                                       continuum level fuel performance modeling codes. However, the thermodynamic properties of the
Available online 20 December 2019
                                                       ﬁssion gas bubbles (such as the relationship among bubble size, equilibrium Xe concentration, and
                                                       bubble pressure) are not well known. This work studies Xe bubbles in gU-Mo from a diameter of 3 nm up
                                                       to 8.5 nm and from 400 K up to 700 K. The energetic relationship of Xe bubbles with regard to voids and
                                                       Xe substitutional atoms is described. The transition is also determined for when a bubble becomes over-
                                                       pressurized. Finally, an equation of state is ﬁt to the pressure as a function of molar volume and
                                                       temperature.
                                                                                                                                      Published by Elsevier B.V.




1. Introduction                                                                          fuels [3e6] which has led to the development of a swelling corre-
                                                                                         lation as a function of ﬁssion density from Argonne National Lab-
   The United States High-Performance Research Reactor                                   oratory (ANL correlation) [7] and Idaho National Laboratory [8]. A
(USHPRR) program targets replacing current highly enriched ura-                          2015 post-irradiation examination (PIE) report [9] from Williams
nium (HEU) fuel in high power research reactors with low enriched                        et al. showed higher swelling in Ue10Mo fuels at ﬁssion densities
uranium (LEU) fuel [1]. In order to achieve a reduced enrichment in                      much lower than previously observed. This accelerated fuel
these fuel types, there is the requirement for increased uranium                         swelling behavior could lead to early fuel failure and was not
density. One way this is achieved is by utilizing g stabilized ura-                      captured by the ANL correlation. As such, a more mechanistic fuel
nium alloys with 10 wt% or less alloy content. The fuel design being                     swelling model is needed in order to predict swelling behavior of
pursued under the USHPRR program is a uranium-molybdenum                                 UeMo fuels under both typical operating conditions, as well as
(UeMo) monolithic foil, with a zirconium (Zr) diffusion barrier in                       transients, accident scenarios and different reactor environments.
Al clad.                                                                                     Recently, substantial effort has been made on mesoscale models
   An issue with UeMo monolithic fuel is the large amount of                             to predict the swelling behavior of UeMo fuels [10e17]. These
swelling that takes place during operation [2]. Such swelling needs                      models rely on phase-ﬁeld and/or rate theory descriptions of
to be stable and predictable up to high ﬁssion densities. Research                       microstructure evolution of material systems in order to model
reactor fuel types based on UeMo are unique in their ability to                          swelling on realistic timescales. These simulation methodologies
stably retain ﬁssion gases to high ﬁssion densities, and as such                         include a number of parameters that are either ﬁt to limited
there is a relatively high content of ﬁssion gas and of ﬁssion gas                       experimental data, calculated from lower length scale modeling
bubbles within the fuel matrix. The importance of swelling in                            methodologies, or assumed based on other material systems.
addition to the unique fuel environment has led to a variety of                          However, the thermodynamic properties of the bubbles (such as
experimental studies characterizing the swelling behavior in UeMo                        the relationship among bubble size, equilibrium Xe concentration,
                                                                                         and bubble pressure) are not well known. Implementation of cor-
                                                                                         rect thermodynamic properties into mesoscale and continuum
    * Corresponding author. North Carolina State University, Raleigh, NC 27607, USA.     level fuel performance modeling codes is crucial for the accurate
      E-mail address: benjamin.beeler@inl.gov (B. Beeler).                               prediction of fuel behavior under irradiation, particularly in regard

https://doi.org/10.1016/j.jnucmat.2019.151961
0022-3115/Published by Elsevier B.V.
2                                             B. Beeler et al. / Journal of Nuclear Materials 530 (2020) 151961


to swelling.                                                                     the center of the supercell. This void is relaxed for 200 ps under the
    A number of molecular dynamics investigations have been                      same simulation conditions described above. Larger supercells
performed targeted at elucidating fundamental Xe bubble proper-                  were investigated in speciﬁc cases to ensure that no artifacts due to
ties in UeMo. Xiao et al. [18,19] studied UeMo-Xe bubbles of less                the size of the supercell were present in the simulations. No sta-
than 2 nm in diameter, analyzing the pressure and induced swelling               tistically signiﬁcant changes to bubble energies or pressures were
with increasing Xe content. They also modeled bubble coalescence                 observed due to changes in the supercell size.
as a function of temperature. They observed interesting effects such                 In order to analyze bubbles, two sets of simulations are per-
as a decrease in bubble pressure and Xe density with increasing                  formed: an NPT and an NVT ensemble. An NVT ensemble is utilized
number of Xe atoms present in the bubble. The origin of such                     to mimic a bubble in a very large system that effectively exerts a
anomalous effects is unclear. Recently, Hu, et al. developed an                  resistive pressure on the bubble. This allows for the calculation of a
equation of state of Xe bubbles in UeMo at 500 K by determining                  Xe bubble pressure and a subsequent equation of state based on the
Xe density and pressure [20]. They also studied dislocation emis-                density of the bubble. The NPT ensemble allows the system volume
sion from ﬁssion gas bubbles and suggested a possible cause of the               to change and to determine the transition between an under-
face-centered cubic ﬁssion gas superlattice due to the anisotropic               pressurized bubble, where the volume of the system is less than
tensile stress surrounding the bubbles. However, this work was                   the equilibrium volume of a Ue10Mo alloy, to an over-pressurized
restricted to a single temperature and very small bubbles of                     bubble, where the volume of the system is greater than the equi-
diameter less than 2 nm. Although this is typically the size of                  librium volume of a Ue10Mo alloy. The target pressure for the NPT
bubbles found in the ﬁssion gas superlattice [7], after grain                    ensemble is 0.
reﬁnement the superlattice bubbles coalesce into larger bubbles, up                  The generation of bubbles is performed by inserting Xe atoms
to 1 mm in diameter [9]. The inclusion of only small, highly pres-               into the void one at a time, while relaxation of the system is
surized bubbles into an equation of state that governs all possible              ongoing. For smaller bubbles, the insertion rate is as low as one Xe
Xe bubble conﬁgurations excludes a signiﬁcant amount of infor-                   atom per 17.5 ps. For the largest voids/bubbles investigated, the
mation. Therefore, it is valuable to extend the previous work that               insertion rate is higher, with one Xe atom inserted every 0.8 ps. This
was performed to investigate much larger systems and a wider                     is modiﬁed according to the bubble size in order to ensure a similar
variety of Xe concentrations within bubbles in order to incorporate              rate of Xe to vacancy ratio change as a function of time. In order to
as much information as possible to facilitate mesoscale models of                track the bubble size, two atoms (one on either side of the void) are
ﬁssion gas swelling and microstructural evolution in UeMo fuels.                 tracked throughout the simulation and the distance between the
    This work studies Xe bubbles in gU-Mo from a diameter of 3 nm                two atoms is classiﬁed as the diameter of the bubble. The pressure
up to 8.5 nm and from 400 K up to 700 K. The energetic relationship              of the bubble is determined by computing the stress per atom on
of Xe bubbles with regard to voids and Xe substitutional atoms is                each of the Xe atoms in the system, summing the individual com-
described. The transition is also determined for when a bubble                   ponents of the stress tensor over all Xe atoms and ﬁnally dividing
becomes over-pressurized. Finally, an equation of state is ﬁt to the             by the degrees of freedom (three) and the volume of the bubble.
pressure as a function of molar volume and temperature.                              Two unique formalisms of the equation of state (EOS) are ﬁt to
                                                                                 the molecular dynamics data, both of which will be discussed in
2. Computational details                                                         greater detail below. A minimization script is utilized to ﬁt the EOS
                                                                                 for each functional form to the determined pressure and molar
    Molecular dynamics simulations are performed utilizing the                   volume data from the molecular dynamics simulations. The data is
LAMMPS [21] software package and the UeMo-Xe embedded atom                       input into the script, and the relative error is summed and utilized
method (EAM) interatomic potential [22]. This potential is capable               to optimize the EOS, iterating by providing a random step to each of
of describing the body-centered cubic phase of UeMo alloys, and is               the ﬁtting coefﬁcients and only accepting the iteration if the total
presently the only potential capable of describing the UeMo-Xe                   relative error is reduced.
ternary system. The potential is able to reproduce the stable
structure, modulus of elasticity, room-temperature density and
                                                                                 3. Results
melting temperature of Ue10Mo. Additionally, this potential is able
to reproduce a number of properties of pure Xe gas and face-
                                                                                 3.1. Surface, formation and binding energies of voids and bubbles
centered cubic Xe. However, it is unknown the level of accuracy
of the defect properties of Xe in UeMo with this potential, as no
                                                                                     In order to generate bubbles in the methodology outlined above,
such experimental data is available, and the inherent mechanical
                                                                                 voids of varying size must be generated. This allows for the calcu-
instability in density functional theory simulations makes such
                                                                                 lation of a void surface area as a function of radius, and the surface
examinations untenable. The authors would recommend validation
                                                                                 energy can be determined from equation (1)
of this potential with ab initio molecular dynamics simulations;
however, such a study was beyond the scope of this project and                              ðE  EÞ
additionally no such study of the kind has been performed.                       Esur f ¼            N                                            (1)
                                                                                                A
    A supercell of 40  40  40 body-centered cubic (bcc) unit cells
(128,000 U atoms) is generated, and approximately 22% of U atoms                 where E is the potential energy per atom of the system with a void,
are randomly switched to Mo atoms, yielding a Ue10Mo (10 wt                      E is the potential energy per atom of the perfect crystal of UeMo, A
percent) alloy in the bcc structure. Relaxation of the bulk system is            is the total surface area of the void and N is the number of atoms in
performed in an NPT-ensemble, relaxing each x, y, and z compo-                   the system with a void. The void surface energy is shown in Fig. 1 as
nent individually, with a damping parameter of 0.1. A Langevin                   a function of void radius. It should be emphasized that all of these
thermostat in the Gronbech-Jensen-Farago [23,24] formalism is                    systems are random solid substitutional alloys of Ue10Mo in an
utilized with the damping parameter set to 0.01 ps. Temperatures                 NVT ensemble unless speciﬁcally mentioned otherwise. It can be
of interest are 400 K, 500 K, 600 K and 700 K, which span the                    observed that the void surface energy converges above a radius of
realistic operating temperatures for UeMo fuels [8]. The system is               1.5 nm for all temperatures to a value of approximately 1.2 J/m2.
allowed to equilibrate for 200 ps at a given temperature, and sub-               This is similar in magnitude to, albeit slightly lower than, the
sequently a void is constructed by deleting a sphere of atoms from               average surface energy for UeMo free surfaces as determined in
                                                           B. Beeler et al. / Journal of Nuclear Materials 530 (2020) 151961                                                          3




Fig. 1. Void surface energy as a function of radius for voids in Ue10Mo from 400 K to          Fig. 3. Relative bubble energy at 500 K as a function of Xe/vacancy ratio for bubbles of
700 K.                                                                                         ﬁve unique sizes. Bubble diameters labeled, units in nm.



Ref. [25], which utilized an Angular-Dependent potential [26]                                  number of atoms in the system with a void, Esys is the energy of the
capable of describing the UeMo system. It is expected that different                           bulk system (no voids or bubbles) and Nsys is the number of atoms
interatomic potentials would yield different values for the void                               in the bulk system. The energy per atom of Xe in its reference state
surface energy. However, this calculation gives conﬁdence that                                 is neglected in this calculation, as the energy is sufﬁciently small ( <
voids are reaching a relaxed, converged state to provide a founda-                             0.01 eV/at) to result in only statistically insigniﬁcant changes to
tion for insertion of Xe atoms to create bubbles and that all void                             formation energies. In order to compare different bubble sizes to
radii in this system yield a similar energetic landscape for analysis.                         one another, a relative bubble energy is deﬁned as the bubble for-
   An example bubble is shown in Fig. 2. Atoms are progressively                               mation energy less the void formation energy. With this formalism,
inserted into a void, leading to an increasing Xe to vacancy ratio as a                        only the excess energy attributable to the Xe atoms and their
function of simulation time, resulting in a highly pressurized Xe                              subsequent inﬂuence on the energy of the system is analyzed. This
bubble at the end of the simulation. The maximum Xe/vacancy ratio                              allows for the investigation of energetic effects of Xe bubbles for
obtained is approximately 0.5, which was observed to be sufﬁ-                                  different bubble sizes. The relative bubble energy at 500 K is shown
ciently high to obtain a bubble pressure of a few GPa, which ensures                           in Fig. 3 for bubbles of diameter 3.1, 4.4, 5.8, 7.1 and 8.5 nm.
investigation of all likely bubble pressures in these systems.                                     For all bubbles, there is a region below a Xe/vacancy ratio of 0.15
   The bubble formation energy can be calculated by the following                              where additional Xe atoms inserted into the bubble produce no
equation:                                                                                      noticeable change in the relative bubble energy, which corresponds
                                                                                               to a Xe molar volume of approximately 80 cm3/mol. There can even
                                                                                               exist a slight reduction in system energy due to Xe aiding in the
                  Nvoid sys                                                                    faceting of the low pressure bubble. Above a Xe/vacancy ratio of
Ebub
 f   ¼ Ebub            E                                                           (2)
                  N sys                                                                        approximately 0.15, the relative bubble energy displays a quadratic
                                                                                               increase as a function of the Xe/vacancy ratio. The speciﬁc nature of
where Ebub is the energy of the system with a bubble, Nvoid is the




Fig. 2. A Xe bubble at 500 K with a diameter of 7.1 nm in Ue10Mo as a function of time. Starting from a void (a), to a Xe/vacancy ratio of 0.16 (b), and a Xe/vacancy ratio of 0.32 (c).
Red atoms are U, blue atoms are Mo and green atoms are Xe.
4                                                     B. Beeler et al. / Journal of Nuclear Materials 530 (2020) 151961

Table 1
Point defect formation energies and binding energies in Ue10Mo at 400 K. Units in
eV.

    Defect Type                 Formation Energy                Binding Energy

    Vacancy                     1.6                             e
    Interstitial                1.1                             e
    Xe substitutional           6.1                             e
    Divacancy                   2.1                             1.2
    Xe sub-vac pair             7.4                             0.4




the quadratic growth is dependent upon the bubble size, where a
larger bubble displays a more rapid increase in relative bubble
energy. This shows that it is much more difﬁcult to obtain a high Xe/
vacancy ratio in large bubbles compared to small bubbles.
   The energetic preference for adding or removing a Xe atom into
an existing bubble can be investigated by looking at the binding
energy of the nth Xe atom in a given bubble. The binding energy of
the nth Xe atom in a given bubble can be deﬁned as:
                                                                                         Fig. 4. Binding energy of the nth Xe atom in a bubble as a function of the Xe/vacancy
                                                                                         ratio.
E   bind
           ¼ EðnÞ  Eðn  1Þ  ESub
                                Xe þ EVac                                      (3)

where E(n) is the energy of a system with a bubble with n Xe atoms,                      would expect in bcc U [28], with a comparatively lower interstitial
E (n-1) is the energy of system with a bubble with n-1 Xe atoms,                         formation energy. The Xe substitutional energy is 6.1 eV. The Xe
ESub
  Xe is the formation energy of a Xe substitutional, and EVac is the                     interstitial energy is omitted from this table, as it was observed that
formation energy of a monovacancy. The addition of a vacancy in-                         Xe interstitials transformed into a Xe substitutional and a matrix
dicates the two systems of comparison with a ﬁxed bubble size: 1) a                      interstitial. There exists strong binding between individual va-
bubble with m vacancies and n  1 Xe, and a substitutional Xe atom,                      cancies (negative binding energy indicating attraction here) as well
2) a bubble with m vacancies and n Xe, and a monovacancy in the                          as a strong binding between Xe substitutionals and vacancies. The
lattice. The Xe substitutional reference state was chosen as this is                     value of 6.1 eV for a Xe substitutional was utilized in equation (3).
the low energy defect conﬁguration for Xe in Ue10Mo. This was the                            The binding energy of the nth Xe atom in a given bubble is
assumed conﬁguration based on density functional theory calcu-                           shown in Fig. 4, for all bubble sizes investigated. It can be seen that
lations in pure bcc U [27]. However, speciﬁc calculations utilizing                      the binding energy is negative for all Xe/vacancy ratios included in
the interatomic potential were undertaken to verify this informa-                        this study, illustrating that it is always favorable for a Xe atom to
tion. A simulation supercell of 1024 atoms (8  8x8 unit cells) was                      reside in a bubble, regardless of existing Xe/vacancy ratio, rather
utilized to calculate the energy, at 400 K, of bcc U, bcc Mo and bcc                     than to reside in the bulk UeMo alloy. The binding energy does
Ue10Mo. Due to the large number of possible unique conﬁgura-                             grow less strong with increasing Xe/Vac ratio, as would be ex-
tions of a random solid substitutional alloy, one thousand unique                        pected, but there is no observed scenario where it is energetically
simulations were performed to calculate the energies of alloy sys-                       favorable for a Xe atom to reside in the bulk instead of as an atom in
tems and ensure converged energies. The formation energy of a                            the bubble. Extrapolating a quadratic ﬁt to a binding energy of zero
Ue10Mo alloy was found to be 0.18 eV/at. Point defects investigated                      yields a Xe/Vac ratio of 0.94, where it would be energetically un-
included vacancy, interstitial, divacancy, Xe substitutional, Xe                         favorable for a Xe atom to reside within the bubble. However, it is
interstitial and a Xe substitutional-vacancy pair. To account for the                    very likely that as Xe/Vac ratio increases, lattice deformation
non-zero formation energy in point defect calculations, equation                         around the bubble will become dramatic, altering the binding en-
(4) was utilized,                                                                        ergy behavior as a function of Xe content. It should also be noted
                                                                                         that data for all bubble sizes is included in this graph as there is no
    def      def      alloy                                                              observable difference in Xe binding energy as a function of Xe/Vac
Ef        ¼ EF      EF                                                        (4)
                                                                                         ratio for different bubble sizes.
where Ealloy
         F   is the total formation energy of an alloy of UeMo, and
Edef
 F   is the total formation energy of a UeMo alloy with a defect.                        3.2. Bubble pressurization transition
Each of these total formation energies are calculated via equation
(5)                                                                                          In order to determine the under-to over-pressurized transition,
                                                                                         simulations in an NPT ensemble at 400 K are performed to allow
EF ¼ ETot  EU  NU  EMo  NMo                                                (5)       the volume to change as a function of time. The equilibrium volume
                                                                                         of a Ue10Mo alloy is determined prior to the introduction of a void
where ETot is the total energy of the system, EU is the energy per                       and subsequent introduction of Xe atoms. A relaxed system with a
atom of bcc U, EMo is the energy per atom of bcc Mo, and NU and NMo                      void exhibits a reduced volume compared to the equilibrium sys-
are the number of U and Mo atoms in the system of interest,                              tem. As Xe is introduced into the void/bubble, the Xe exerts an
                                    def
respectively. Subsequently, the Ef , which is the individual defect                      outward force on the system. As progressively more Xe is added
formation energy, can be calculated. The subsequent defect for-                          into the bubble, the pressure becomes signiﬁcant enough to expand
mation energies are presented in Table 1.                                                the bulk system and increase the supercell volume. This work de-
    It should be noted that all defects are an average of both species,                  ﬁnes the transition from under-to over-pressurized bubbles as the
for example an interstitial could be either U or Mo, and this is an                      point where the volume of the system with a Xe bubble is equal to
average over all 1000 unique simulations. The vacancy and inter-                         the equilibrium volume of a system with no void or bubble. Thus, at
stitial defect energies are qualitatively coherent, based on what one                    a lower than equilibrium Xe/vacancy ratio the system will have a
                                                        B. Beeler et al. / Journal of Nuclear Materials 530 (2020) 151961                                                 5




Fig. 5. The normalized volume of a system with a bubble as a function of Xe/vacancy        Fig. 6. Predicted bubble pressure from Eq. (6) minus the calculated pressure from
ratio for ﬁve unique bubble sizes. Bubble diameters labeled, units in nm.                  molecular dynamics as a function of bubble size.



slightly lower volume than the equilibrium system, and at a higher                         Fig. 5 where the normalized volume is 1. Interestingly, the results
than equilibrium Xe/vacancy ratio the system will have a slightly                          do not agree particularly well. The difference in the predicted
higher volume than the equilibrium system. The results are shown                           versus calculated pressures as a function of bubble diameter is
in Fig. 5. The system becomes over-pressurized at different Xe/va-                         shown in Table 2. The difference in predicted versus calculated is
cancy ratios depending upon the bubble diameter. For smaller                               most pronounced for small bubbles, however this difference is
bubbles, the transition occurs at a lower Xe/vacancy ratio. However,                       reduced as the bubble size increases. For all bubble sizes, the pre-
for the bubbles investigated, the range of variance for all bubble                         dicted pressure is greater than the calculated pressure. Thus, it is
sizes is somewhat small. The transition occurs as early as a 0.13 Xe/                      possible that the Young-Laplace equation does not hold for bubbles
vacancy ratio for a bubble of diameter 3.1 nm, and as late as a 0.20                       less than 10 nm in diameter in this system, however, it may apply
Xe/vacancy ratio for a bubble of diameter 8.5 nm. Proceeding the                           for bubbles larger than 10 nm in diameter.
transition, the volume increase is related to the size of the bubble as                        To verify this hypothesis, two larger bubbles were investigated
well, as larger bubbles see signiﬁcantly more rapid volume increase                        to determine if the predicted and calculated equilibrium pressures
with a given increase in the Xe/vacancy ratio. The quantitative                            converged as bubble size increases. In order to accommodate larger
value of the relative volume as a function of Xe/vacancy ratio will                        bubbles, a larger supercell (60  60  60, 432,000 atoms) is utilized.
change with changes in supercell size volume, but the qualitative                          Bubbles with a 11.2 nm diameter and a 12.6 nm diameter are
relationships will not vary. Supercell size effects were investigated                      investigated in an NPT ensemble at 0 pressure and 400 K, with a
in limited cases to ensure the qualitative relationships held and that                     comparable Xe/vacancy ratio rate of change to the previous bubbles
the transition point was converged.                                                        included in this study. The results of this work are included in Fig. 6.
    An equilibrium bubble can be understood as the bubble existing                         As the bubble radius increases, the difference between predicted
at the under-to over-pressurized transition. Typically the pressure                        and calculated pressure continues to decrease, with each pressure
of such a bubble is determined by satisfying the Young-Laplace                             converging to an identical value for large bubbles. An exponential
equation, often denoted by equation (6),                                                   function is ﬁt to this data, (with an R2 value of 0.96), which shows
                                                                                           that as bubble radius increases, the discrepancy between predicted
     2g                                                                                    and calculated equilibrium pressure exponentially decays. Given
P¼                                                                               (6)       this information, we propose a modiﬁcation to the Young-Laplace
      R
                                                                                           equation speciﬁcally for Xe bubbles in UeMo, although this rela-
where g is the surface energy and R is the radius of the bubble.                           tionship may hold for other gas bubbles in other material systems.
Although the Young-Laplace equation was formulated to describe                             The equilibrium pressure as a function of bubble radius should be
the interface across ﬂuids, it is commonly used to describe gas                            deﬁned by equation (7).
bubbles in solids. To verify if the Young-Laplace relationship holds
for Xe bubbles in UeMo, the predicted equilibrium pressure from
equation (6) is determined and compared to the computationally                                  2g
                                                                                           P¼       A  expðB  RÞ                                                    (7)
calculated equilibrium pressure using the Xe/vacancy ratio from                                  R

                                                                                           where g equal 1.2 J/m2 (from Fig. 1), A equals 4.94 and B
Table 2                                                                                    equals 0.87 for the UeMo-Xe system. This equation decays to the
Predicted pressure based on Eq. (6), calculated pressure, and the subsequent dif-          Young-Laplace equation for bubble radii greater than 6 nm. It
ference. Units of pressure in GPa.
                                                                                           should be emphasized that this equation was not ﬁt to data for
 Diameter (nm)              Predicted            Calculated             Difference         bubbles smaller than 3 nm in diameter, and as such the authors
 3.1                        1.39                 0.24                   1.15               make no conclusions regarding the validity of this expression for
 4.4                        1.07                 0.31                   0.77               smaller bubbles. Additionally, it is possible that there exists a
 5.7                        0.82                 0.43                   0.38               temperature dependence of this function, but since the surface
 7.1                        0.65                 0.43                   0.22               energy does not vary over the temperature range of interest, it is
 8.5                        0.55                 0.43                   0.13
                                                                                           assumed that the relationship denoted in equation (7) shows only
6                                                       B. Beeler et al. / Journal of Nuclear Materials 530 (2020) 151961


minimal variation.                                                                         coefﬁcients for the equation of state are a ¼ 870912.08 J-cm3/
                                                                                           mol2, b ¼ 27.133 cm3/mol, c ¼ 88.987 cm3/mol. Compared to the
3.3. Xe bubble equation of state in UeMo                                                   work of Hu, this is a signiﬁcant decrease in the parameter a, a
                                                                                           slightly larger value in b, and a substantial decrease in c. Although
    The equation of state (EOS) can be determined by tracking the                          the work of Hu utilized the same interatomic potential as this work,
pressure inside the bubble and the bubble size as a function of the                        the area of interest with regard to bubble properties was dramat-
number of Xe atoms present in the bubble while the system is                               ically different. Hu investigated small bubbles, less than 2 nm in
equilibrated in an NVT ensemble, which provides a pressure versus                          diameter, at high pressures, greater than 2 GPa and up to 8 GPa.
density relationship. This data can be ﬁt to an EOS that provides a                        They did not include bubbles with larger radii or low density Xe gas
generalized function predicting the relationship between pressure,                         in their ﬁtting. As such, it is expected that there would exist dif-
temperature and molar volume. In order to extend the applicability                         ferences in the results for a ﬁtted EOS.
of the EOS, temperatures from 400 K to 700 K are analyzed, for all                             Considering the ﬁtted parameters, emphasis should be drawn to
bubble sizes previously mentioned. No restrictions are imposed on                          the negative magnitude of the a parameter. In the original van der
the ﬁtting parameters for each individual EOS.                                             Waals formalism, the a/v2 term was included to provide for inter-
                                                                                           molecular attraction. Typical values of a are positive [29], indicating
3.3.1. Kaplun EOS                                                                          net attraction between molecules and a reduction in the overall
    An EOS for Xe bubbles is taken from Kaplun [29], which was also                        pressure. However, in this study, the a parameter is negative,
utilized in the work of Hu [20],                                                           indicating additional repulsion leading to an increase in the pres-
                                                                                           sure of the system. This could potentially be due to the fact that
     RT      c  a                                                                        these are generally high pressure systems, or this could be an
P¼        1þ      2                                                             (8)
      v      vb  v                                                                        aspect of the interaction of the Xe gas with the UeMo matrix.
                                                                                           Kaplun states that their derivation of a modiﬁed van der Waals EOS
where R is the gas constant for Xe (8.314 J/mol-K [29]), T is the                          loses applicability in regimes of high pressure and density, and they
temperature in K, P is the pressure in MPa, v is the molar volume in                       only compare to Xe pressures of 5 MPa and below, which would be
cm3/mol, and a, b, and c are ﬁtting parameters. This EOS reduces to                        considered extremely low for this work. Regardless, at very low gas
the well known van der Waals EOS when b ¼ c. It appears that Hu                            densities, the a/v2 term vanishes and this equation converges to the
[20] mislabeled the ﬁtting parameters in their equation, according                         ideal gas law. Thus, although the magnitude of a is atypical for
to the units of the parameters. Hu et al. have conﬁrmed that the                           isolated gases, it is deemed representative of high pressure Xe
correct EOS parameters from their work are a ¼ 259,780 J-cm3/                              bubbles in UeMo in this work.
mol2, b ¼ 18.928 cm3/mol and c ¼ 280.658 cm3/mol [20]. These                                   The accuracy of the EOS ﬁt can be quantiﬁed in a number of
parameters are utilized as the starting guess for the ﬁtting pro-                          ways. A root-mean squared deviation (RMSD) is likely not the best
cedure in this work to obtain an optimized EOS.                                            metric, due to the large range of pressures in the data set covering
    The subsequent ﬁt, with and without molecular dynamics data,                           multiple orders of magnitude. Thus, it can be better to gauge ac-
is shown in Fig. 7. An inlay is included for molar volumes from 20 to                      curacy via a normalized RMSD (NRMSD), which is deﬁned by
100 cc/mol, to better illustrate the high pressure data. The data                          dividing the RMSD by the range (the difference of the maximum
heavily overlaps and only shows minor differences as a function of                         and minimum) of the dataset, or via a total relative error, which is
temperature and as such the individual isotherms are difﬁcult to                           the summation of the relative error of each individual data point
distinguish. For clarity, the MD data is removed in Fig. 7b and the                        divided by the total number of data points. Both metrics will be
optimized EOS is displayed on a log/linear scale to emphasize the                          used here, with emphasis placed on total relative error. The NRMSD
differences between the individual isotherms. The optimized




Fig. 7. An equation of state (EOS) based on a modiﬁed van der Waals equation from Kaplun for Xe bubbles in Ue10Mo from 400 K to 700 K (a) compared to molecular dynamics data
and (b) without molecular dynamics data.
                                                        B. Beeler et al. / Journal of Nuclear Materials 530 (2020) 151961                                                  7


of the optimized Kaplun EOS compared to the MD data is 6.5% and                                      Table 3
the total relative error is 10.3%. Considering that the pressure in this                             Virial equation of state (Eq. (9)) parameters for Xe bubbles in
                                                                                                     UeMo.
dataset varies over 3 orders of magnitude and the temperature
varies over 300 K, this is considered excellent agreement. The                                         Parameter                           Value
NRMSD of the previously optimized EOS from Hu calculated with                                          b0                                  197.229 cm3/mol
respect to the MD data in this work is 9.8% and the total relative                                     b1                                  120307.145 cm3-K/mol
error is 16.5%. Thus, using the relative error as the standard mea-                                    b2                                  60.555 cm3-K2/mol
                                                                                                       c0                                  22038.723 cm6/mol2
sure of accuracy, this represents approximately a 6% improvement
                                                                                                       c1                                  2292.793 cm6-K/mol2
over the most ﬁnely calibrated EOS for Xe bubbles in UeMo in the                                       c2                                  117.564 cm6-K2/mol2
literature, as well as a dramatic expansion on the range of appli-                                     d0                                  1030015.045 cm9/mol3
cability, with respect to bubble size, pressure and temperature.                                       d1                                  5.200 cm9-K/mol3
                                                                                                       d2                                  280.677 cm9-K2/mol3

3.3.2. Virial EOS
    Due to the atypical nature of the a parameter in 3.3.1, an addi-
tional equation of state formalism was utilized to investigate the                         put forth as the most accurate EOS available for description of Xe
possibility of alternate functional forms better representing the                          bubbles in UeMo over this temperature and pressure range.
molecular dynamics data. A virial equation of state is utilized,                           However, comparable accuracy is achieved with the modiﬁed van
expanded to the third order with respect to volume and the second                          der Waals EOS and the reader is encouraged to utilize their
order with respect to temperature, as is shown in equation (9),                            preferred functional form.
                            
     RT         B C D                                                                      4. Conclusions
P¼            Aþ þ 2 þ 3                                                         (9)
      v         v v   v
                                                                                               This work investigated Xe bubbles in gU-Mo from a diameter of
where A ¼ 1, and B, C and D are temperature dependent Taylor                               3 nm up to 8.5 nm and from 400 K up to 700 K. The energetic
series of 1/T (B ¼ b0 þ b1/T þ b2/T2, C ¼ c0 þ c1/T þ c2/T2 and D ¼ d0 þ                   relationship of Xe bubbles with regard to voids and Xe point defects
d1/T þ d2/T2), leading to nine unique ﬁtting parameters. The virial                        is described. The relative energy of a bubble increases quadratically
equation is a general function relating pressure, molar volume and                         as a function of Xe/vacancy ratio, with larger bubbles exhibiting a
temperature that can be directly derived from statistical mechanics                        more rapid increase in energy. The binding energy of Xe atoms is
[30].                                                                                      negative, indicating attraction, for all bubbles and all Xe/vacancy
    The subsequent ﬁt, with and without molecular dynamics data,                           ratios investigated. This shows that the energy of a Xe atom in the
is shown in Fig. 8. An inlay is included for molar volumes from 20 to                      UeMo lattice is sufﬁciently high, such that Xe will always want to
100 cc/mol. The MD data is removed in Fig. 8b and the optimized                            reside in the bubble, regardless of bubble pressure investigated in
EOS is displayed on a log/linear scale to emphasize the differences                        this work. The under-to over-pressurized transition for bubbles is
between the individual isotherms. The optimized coefﬁcients are                            determined. This transition is below a Xe/vacancy ratio 0.2 for all
shown in Table 3. The NRMSD of the optimized Virial EOS compared                           bubbles in this work. A modiﬁcation of the Young-Laplace equation
to the MD data is 5.7% and the total relative error is 9.0%. This is an                    is suggested to determine the equilibrium volume pressure of Xe
increase in accuracy over the modiﬁed van der Waals EOS from this                          bubbles in UeMo. Finally, two distinct equations of state were ﬁt to
work by 1.3% and from Hu by 7.5%, utilizing total relative error to                        the pressure as a function of molar volume and temperature for Xe
judge accuracy. Thus, the virial EOS provides the most accurate                            in UeMo bubbles. The virial EOS variant represents an improve-
description of molecular dynamics information in this work and is                          ment in accuracy and extended applicability compared to a




Fig. 8. An equation of state (EOS) based on a virial expansion for Xe bubbles in Ue10Mo from 400 K to 700 K (a) compared to molecular dynamics data and (b) without molecular
dynamics data.
8                                                       B. Beeler et al. / Journal of Nuclear Materials 530 (2020) 151961


previously developed EOS.                                                                       Fission Gas Bubbles in U-Mo Fuel, Argonne National Laboratory, 2008. Tech.
                                                                                                Rep. ANL-08/11.
    The knowledge that the Xe/vacancy ratio depends on the bubble
                                                                                            [5] M. Meyer, G. Hofman, S. Hayes, C. Clark, T. Wiencek, J. Snelgrove, R. Strain,
size and optimally decreases with increasing bubble diameter is                                 K. Kim, Low-temperature irradiation behavior of uranium-molybdenum alloy
valuable, in that the assumption is typically made of a constant Xe/                            dispersion fuel, J. Nucl. Mater. 304 (2002) 221.
vacancy ratio, regardless of bubble size. Also, the examined Xe/                            [6] Y. Kim, G. Hofman, J. Cheon, A. Robinson, D. Wachs, Fission induced swelling
                                                                                                and creep of u-mo alloy fuel, J. Nucl. Mater. 437 (2013) 37.
vacancy ratios in this study are somewhat lower than the previous                           [7] Y. Kim, G. Hofman, Fission product induced swelling of u-mo alloy fuel, J. Nucl.
estimate of ﬁssion gas densities in bubbles in UeMo, although the                               Mater. 419 (2011) 291.
pressures are similar in magnitude. A modiﬁcation to the Young-                             [8] M. Meyer, B. Rabin, J. Cole, I. Glagolenko, W. Jones, J.-F. Jue, J.D. Keiser,
                                                                                                C. Miller, G. Moore, H. Ozaltun, F. Rice, A. Robinson, J. Smith, D. Wachs,
Laplace equation will dramatically modify the suggested equilib-                                W. Williams, N. Woolstenhulme, Preliminary Report on U-Mo Monolithic Fuel
rium state for small ﬁssion gas bubbles. The information provided                               for Research Reactors, Idaho National Laboratory, 2017. Tech. Rep. INL/EXT-
in this work regarding bubble energetics, under-to over-pressuri-                               17-40975.
                                                                                            [9] W. Williams, F. Rice, A. Robinson, M. Meyer, B. Rabin, Aﬁp-6 Mkii Post-
zation transition, and an updated equation of state for Xe bubble in                            irradiation Examination Summary Report, Idaho National Laboratory, 2015.
Ue10Mo can be directly utilized to improve the ﬁdelity of meso-                                 Tech. Rep. INL/LTD-15-34142.
scale models that describe ﬁssion gas induced swelling in UeMo                             [10] L. Liang, Y. Kim, Z.-G. Mei, L. Aagesen, A. Yacout, Fission gas bubbles and
                                                                                                recrystallization-induced degradation of the effective thermal conductivity in
fuels.                                                                                          u-7mo fuels, J. Nucl. Mater. 511 (2018) 438.
                                                                                           [11] L. Liang, Z.-G. Mei, Y. Kim, M. Anitescu, A. Yacout, Three-dimensional phase-
CRediT authorship contribution statement                                                        ﬁeld simulations of intragranular gas bubble evolution in irradiated u-mo
                                                                                                fuel, Comput. Mater. Sci. 145 (2018) 86.
                                                                                           [12] L. Liang, Z.-G. Mei, A. Yacout, Fission-induced recrystallization effect on
   Benjamin Beeler: Conceptualization, Methodology, Software,                                   intergranular bubble-driven swelling in u-mo fuel, Comput. Mater. Sci. 138
Formal analysis, Investigation, Writing - original draft, Project                               (2017) 16.
administration, Visualization. Shenyang Hu: Conceptualization,                             [13] L. Liang, Z.-G. Mei, Y. Kim, B. Ye, G. Hofman, M. Anitescu, A. Yacout, Mesoscale
                                                                                                model for ﬁssion-induced recrystallization in u-7mo alloy, Comput. Mater. Sci.
Methodology, Validation, Writing - review & editing. Yongfeng                                   124 (2016) 228.
Zhang: Conceptualization, Methodology, Writing - review & edit-                            [14] B. Ye, G. Hofman, A. Leenaers, A. Bergeron, V. Kuzminov, S.V. den Berghe,
ing, Supervision. Yipeng Gao: Conceptualization, Methodology,                                   Y. Kim, H. Wallin, A modelling study of the inter-diffusion layer formation in
                                                                                                u-mo/al dispersion fuel plates at high power, J. Nucl. Mater. 499 (2018) 191.
Writing - review & editing.                                                                [15] S. Hu, V. Joshi, C. Lavender, A rate-theoryephase-ﬁeld model of irradiation-
                                                                                                induced recrystallization in umo nuclear fuels, J. Occup. Med. 69 (2017) 2554.
Acknowledgement                                                                            [16] S. Hu, D. Burkes, C. Lavender, V. Joshi, Effect of grain morphology on gas
                                                                                                bubble swelling in umo fuels e a 3d microstructure dependent booth model,
                                                                                                J. Nucl. Mater. 480 (2016) 323.
    This work was supported by the U.S. Department of Energy,                              [17] S. Hu, D. Burkes, C. Lavender, D. Senor, W. Setyawan, Z. Xu, Formation
Ofﬁce of Material Management and Minimization, National Nuclear                                 mechanism of gas bubble superlattice in umo metal fuels: phase-ﬁeld
                                                                                                modeling investigation, J. Nucl. Mater. 479 (2016) 202.
Security Administration, under DOE-NE Idaho Operations Ofﬁce                               [18] H.-X. Xiao, R. Tang, X.-F. Tian, C.-S. Long, Molecular dynamics simulation of xe
Contract DE-AC07-05ID14517. This manuscript has been authored                                   behavior in u-mo alloys fuel, Chin. Phys. Lett. 31 (2014), 047101.
by Battelle Energy Alliance, LLC with the U.S. Department of Energy.                       [19] H.-X. Xiao, C.-S. Long, X.-F. Tian, S. Li, Atomistic simulations of the small xenon
                                                                                                bubble behavior in uemo alloy, Mater. Des. 74 (2015) 55.
The publisher, by accepting the article for publication, acknowl-
                                                                                           [20] S. Hu, W. Setyawan, V. Joshi, C. Lavender, Atomistic simulations of thermo-
edges that the U.S. Government retains a nonexclusive, paid-up,                                 dynamic properties of xe gas bubbles in u10mo fuels, J. Nucl. Mater. 490
irrevocable, worldwide license to publish or reproduce the pub-                                 (2017) 49.
lished form of this manuscript, or allow others to do so, for U.S.                         [21] S. Plimpton, Fast parallel algorithms for short-range molecular dynamics,
                                                                                                J. Comput. Phys. 117 (1995) 1e19.
Government purposes. This research made use of the resources of                            [22] D. Smirnova, A. Kuksin, S. Starikov, V. Stegailov, Z. Insepov, J. Rest, A. Yacout,
the High Performance Computing Center at Idaho National Labo-                                   A ternary eam interatomic potential for u-mo alloys with xenon, Model.
ratory, which is supported by the Ofﬁce of Nuclear Energy of the                                Simul. Mater. Sci. Eng. 21 (2013), 035011.
                                                                                           [23] N. Gronbech-Jensen, O. Farago, A simple and effective verlet-type algorithm
U.S. Department of Energy and the Nuclear Science User Facilities.                              for simulating Langevin dynamics, Mol. Phys. 111 (2013) 983.
                                                                                           [24] N. Gronbech-Jensen, N. Hayre, O. Farago, Application of the g-jf discrete-time
Appendix A. Supplementary data                                                                  thermostat for fast and accurate molecular simulations, Comput. Phys. Com-
                                                                                                mun. 185 (2014) 524.
                                                                                           [25] B. Beeler, Y. Zhang, Y. Gao, An atomistic study of grain boundaries and surfaces
   Supplementary data related to this article can be found at                                   in gamma u-mo, J. Nucl. Mater. 507 (2018) 248.
https://doi.org/10.1016/j.jnucmat.2019.151961.                                             [26] D. Smirnova, A. Kuksin, S. Starikov, V. Stegailov, Atomistic modeling of the
                                                                                                self-diffusion in gamma u and gamma u-mo, Phys. Met. Metallogr. 116 (2015)
                                                                                                445.
References                                                                                 [27] B. Beeler, C. Deo, M. Baskes, M. Okuniewski, Atomistic investigations of
                                                                                                intrinsic and extrinsic point defects in bcc uranium, Effects Radiat Nuc Mater:
[1] J. Snelgrove, G. Hofman, M. Meyer, C. Trybus, T. Weincek, Development of                    STP 1547 25 (2012) 231.
    very-high density low enriched uranium fuels, Nucl. Eng. Des. 178 (1997) 119.          [28] B. Beeler, B. Good, S. Rashkeev, C. Deo, M. Baskes, M. Okuniewski, First prin-
[2] G. Hofman, L. Walters, T. Bauer, Metallic fast reactor fuels, Prog. Nucl. Energy            ciples calculations for defects in U, J. Phys. Condens. Matter 22 (2010), 505703.
    31 (1997) 83.                                                                          [29] A. Kaplun, A. Meshalkin, Thermodynamic validation of the form of uniﬁed
[3] J. Rest, G. Hofman, Y. Kim, Analysis of intergranular ﬁssion-gas bubble-size                equation of state for liquid and gas, High Temp. 41 (2003) 319.
    distributions in irradiated uranium-molybdenum alloy fuel, J. Nucl. Mater. 385         [30] H.K. Onnes, Expression of state of gases and liquids by means of series, KNAW
    (2009) 563.                                                                                 Proceedings 4 (1902) 125.
[4] Y. Kim, G. Hofman, J. Rest, G. Shevlyakov, Characterization of Intergranular
