# Ronchi_1979_Physical processes and mechanisms related to fission gas swelling in MX-type nuclear fuels.pdf

---

Journal of Nuclear Materials 84 (1979) 55-84
0 North-Holland Publishing Company




      PHYSICAL PROCESSES AND MECHANISMS RELATED TO FISSION GAS SWELLING
      IN MX-TYPE NUCLEAR FUELS *

      C. RONCHI
      Joint Research Centre, Karlsruhe Establishment, European Institute for Transuranium Elements,
      Karlsruhe, Fed. Rep. Germany


      Received 26 January 1979; in revised form 28 March 1979



          An analysis of the fission gas behaviour in MX-type.nuclear fuels is given, taking into account the particualr needs of the
      performance modelling of these fuels. Fission gas bubbles are treated with a new formalism (statistical bubble populations)
      in order to account for the wide sire ranges observed by microscopic analysis. The abrupt increase of bubble size above a
      certain temperature (critical temperature) is interpreted in terms of plastic relaxation of the fuel around centres of precipita-
      tion and coalescence (stable bubbles) having concentration decreasing with temperature.



1. Introduction                                                        of the computer codes. The formidable problem of
                                                                       describing the strain history of a fuel pin during its
    The analysis of the swelling performance of MX-                   irradiation lifetime could only be approached by an
type nuclear fuels (carbides, carbonitrides and nitri-                 attempt to codify and systematize observed or
des) is entering a new phase, in which basic premises                  expected effects, covering partial aspects of the field
and approaches are being re-examined and attempts                      of investigation. The reliability of the theory predic-
at consolidation of the physical models are being                      tions is thus determined both by the extent to which
made. Our understanding of the swelling effects in                     a code is able to account for the complexity of the
these fuels in the earlier stage of investigation was                  system, and by the validity of the physical models.
based on relatively few experimental observations,                    A unique improvement of one of the two aspects
however, a causal reconstruction of the process was                   does not bring actual benefits to the analysis.
attempted, starting from simple, elementary mecha-                        On the other hand the analysis that encompasses
nisms. These first interpretations have now to be                     such a complex field should be numerically tractable
reconsidered in the light of more complete experi-                    within reasonable computing time and storage require-
mental data. Furthermore, today, as important as                      ments. This poses the fundamental question of the
the attempt to decide which causal sequences,                         greatest permissible simplification of the physical
among the imaginables ones, correctly define the                      description of the phenomena involved. Moreover,
phenomenon, is another question: to what extent                       the code must be able in each subfield to sort out
are our attempts at describing fuel swelling by means                 from the imaginary matrix of mechanisms-by-situa-
of mathematical models justified? Eventually, does                    tions the shortest way of coming to a reasonably
a more sophisticated and detailed analysis represent                  correct evaluation of the effects.
any better tool that could be suited to fuel optimiza-                    This paper is an attempt to analyze and collect the
tion, than those in use?                                              mechanisms of fission gas swelling in such a manner
    Even a cursory glance at the present state of the                 that, although treated independently, they can be
fuel performance modelling work, reveals that there                   organized together to construct swelling models of
has been an unprecedented growth in complexity                        different but in any case exhaustive complexity, in
                                                                      compliance with the needs arising in the various situa-
* To Walter van Lierde, in memoriam.                                  tions.

                                                                 55
 START
establishesinitial                                                                                          fuel structure
parameters




                                                                                                        .
                                                                                                    pore migration
                                                                                                     + sweeping
                                                                                                            .




                     Fig. 1. Scheme of the fwion   gas model as arranged for computer   calculations.
                                C. Ronchi / Fission gas swelling in MX-type nuclear fuels                                 51


    The analysis of fuel swelling has been conducted            mechanisms of decreasing complexity can be construc-
following a mechanistic scheme, whereby the proper-             ted, by short cutting calculation steps, when the effects
ties of the atomic lattice, the ceramographic structure         considered are not expected to be relevant in the parti-
and the geometrical shape of the fuel are sequentially          cular case analyzed.
considered.
    First a system of rate equations for the fission gas
was developed, whose solution enables the concen-               2. Basic equations for the in-pile fission gas kinetics
tration of gas in dynamic solution, the amount precip-          in MX-type fuels
itated into intragranular bubbles and the rate of
migration of gas to deep sinks (pores and grain bound-              The fission gas kinetics during steady-state irradia-
aries) to be calculated. The mathematics and the                tion in MX-type fuels was developed from an earlier
physics of this first part of the treatment, merely             model [ 11, the basic assumptions of which can be
dealing with fission gas kinetics, is presented and dis-        summarized as follows:
cussed in section 2.                                                The fission gas created in the fuel at a rate p, is
    Having defined the fission gas behaviour, the               assumed to attain the saturation level and then pre-
second step consists of calculating the strain rates            cipitate (a) into bubbles at a rate of dP/dt and (b)
following precipitation of gas into bubbles and pores.          into preexisting pores or stable bubbles on lattice
This argument is treated in section 6. In practice,             extended defects, at a rate of dg/dt. Part of the gas
bubble (or pore) growth (or shrinkage) rates occur-             is assumed to be re-injected into the matrix by fission
ring by microscopic plastic deformation processes,              fragment spikes, at a rate of dR/dt.
generated by the pressure of the precipitated gas,                  The balance of these three effects is described by
are calculated, taking into account any existing inter-         the following rate equation:
nal stress field. Logically, this second stage of the
treatment replaces the equation of state which, under                                                                 (1)
assumption of equilibrium conditions, enables the
concentration of fission gas in bubbles to be trans-            where dc/dt is the net rate of creation of gas in dyna-
formed into fractional volumes representing the                 mical solution.
effective change in density of the fuel.                           The centres of precipitation (bubbles and pores)
    In this basic framework, other aspects are con-             are subdivided in M classes, each one being individual-
sidered in the analysis which, under certain conditions,        ized by means of radius and concentration. This sub-
must be taken into account to obtain a correct evalu-           division is accomplished in compliance with a mode1
ation of the swelling rate. Thus, the size distribution         explained below.
and the mobihties of the gas sinks (bubbles and pores)             The schematic rate equation (1) expands to a sys-
 are considered with their mutual interactions (sections        tem of rate equations of type:
 3, 5 and 6). Furthermore, biased gas diffusion in
                                                                c(t)  = concentration rate of gas in dynamical solu-
heterogeneous bubble populations and ripening
                                                                        tion,                                        (2a)
 effects are discussed in section 4.
                                                                i(t)  = concentration rate of gas trapped in deep sinks
     Finally, in section 7 the gas release conditions are
                                                                        on grain boundaries,                        (2b)
 considered, taking into account the fuel morphology.
                                                                hj(t) = concentration rate of gas trapped in the ith
The concept of pore interlinkage and of open porosity
                                                                        bubble class,                                (2c)
is introduced, to enable the ratio of gas retained in
                                                                ii(t) = rate of the average bubble radius in the ith
 the grain boundaries and that escaping from the pellets
                                                                        class,                                      (2d)
 to be calculated.
                                                                $(t) = rate of the spatial concentration of the bubbles
    All the items treated are formally compatible and
                                                                        of class j.                                  (2e)
interdependent. In practice they have been organized
 together in the form of subroutines in a computer code,        Eq. (2a) is the formulation of the kinetic mechanisms
the flow chart of which is schematized in fig. 1. Thanks        of the gas within the grains. This is an extension of
to the structure of the analysis, different swelling            the equation described in ref. [ 11. The mathematical
58                                C Ronchi / Fissiongas swellingin AM-type nuclear fuels

treatment of the processes involved, already reported           in a later stage. The migration of the gas to the grain
in this reference, is here only briefly mentioned and           boundaries is described by the equation:
discussed. Eq. (2d), describing the migration of gas to
the grain boundaries, is discussed in more detail. Eqs.
                                                                ;=D,V’c+         ( /3- $++D,V2c+oL,                   (4)
(2d) and (2e) are formulated according to new mecha-
nisms and represent the subject of sections 3 and 6,
respectively.                                                   with c = 0 for t = 0 and 0 < r Q a (grain radius), c = 0
                                                                fort>Oandr=a,ac/ar=Ofort>Oandr=O.
2.1. Rate of the gas in dynamic solution and precip-                However, an analytical solution of this equation is
itated in bubbles                                               impossible because 01is determined by eq. (2). In fact,
                                                                a! will vary, according to the precipitation and re-solu-
   The net rate of precipitation is written as the dif-         tion processes, in the range 0 < a! < /3.The two
ference between the bubble capture rate and the re-             extreme situations (cr = 0 and ar= 0) are decribed by
solution rate [l] :                                             the two diffusion equations:
db*
$ = Kjrj (t) c(t) - Corj (t)’ ,                                 %=DV2c
                                                                at     g     ’
with Ki = 4nniDB and C0 = 4ndq I b’ , where D, is the
                                                                and
gas diffusion coefficient, d the bubble shell thickness
subjected to re-solution, ‘17
                            the re-solution frequency
                                                                ;=D,V’c+p.
and b’ the van der Waals co-volume for the proper
(Xe + Kr) mixture.
   The equation for the rate of gas in dynamic solu-            Eqs. (Sa) and (5b) have analytical solutions and the
tion is thus written as:                                        two respective fractional release functions can be ob-
                                                                tained:

                                                      (3)

The total net precipitation rate can assume both posi-
                                                               for eq. (5a) and
tive and negative values during the time evolution,
depending upon the mutual variations of the capture
and re-solution terms. Usually, after a certain time,                                                               (6b)
atomic precipitation and re-solution are equalized,
and the bubble growth stops. This leads to a signifi-          for eq. (Sb).
cant increase of the gas migration rate to the grain               The functions (6a) and (6b) assume nearly the
boundaries and, correspondingly, to a decrease of              same values for (Dp,/a2)1’2 < 0.2 and hence eqs. (4),
dc/dt, that results in a stabilization of c around an          (5a) and (5b) give the same fractional release in the
“asymptotic” value c,,                                         initial irradiation stage. In the following time interval,
                                                               with 0.2 < (D&a2)1’2, where the two functions differ
2.2. Rate of precipitation of gas into the grain               by about 20%, the_production rate, dc/dr, is nearly
boundaries                                                     zero, because most of the gas precipitates into bub-
                                                               bles. Therefore, eq. (5a) provides a better description
   (a) 7Ae case of constant temperature. The second            of the physical system at this stage. Only after relativ-
equation calculates the’rate of precipitation of gas           ely long times are the precipitation processes counter-
into the grain boundaries, which are considered as             balanced by the re-solution and at this time the func-
deep sinks. No re-solution is therefore calculated             tions (6a) and (6b) are definitively equivalent. The
from the grain boundaries, where release through               fractional release function (6a) eventually represents
percolation or pore migration is supposed to occur             a good analytical approximation of the release from
                                            C. Ronchi f Fission gas swelling in MX-type nuclear fuels                               59


Table 1
Data used for the calculation of the bubble concentration evolution

DV                  Volume diffusion coefficient              1.2 X 10m3 e-(48 oooln + Kp(m2/s)
0s                  Surface diffusion coefficient             4.9 X lo-4,-(35OOO/T)+Kp     *

                    Fission gas diffusion coefficient         1.2~10-60-(386OO/T)+K~               w
Dg
                    Surface tension                           0.6 J/m2
r’                  Relaxed surface bubble size               0.5 nm
r0                  Atomic radius of gas-in-fuel              0.3 nm
K                   Constant                                  1.942 .. . m5/mol
v-6                 Re-solution constant                      lo-l4    m/s
P                   Gas creation rate                         3.4 X 10m5 (mol/m3s)
T                   Temperature (range)                       s00-1500”c



eq. (4). Therefore, we finally obtain:                                       can be obtained with conventional Fourier’ method.
                                                                             The solution is written as:
$=Pas(a) [1 - 2 (nn)2
                -5 exp(- “‘CJg’)]
                         n =1
                                                                             c---r=-       2 2    [C-Y nn sin 5   ] F,(r)   .       (9)
                                                                                       ran=1

      +   ~?$!S~qJ(-~),                                          (7)
                                                                             The integral coefficients of the series can be written as
          n=l   a                                                            follows:
where Pos(or) indicates the operator: i(o + lal).
    (b) The case of variable temperature.The in-pile                         F,,(T) = jexp       [-m2n2 ‘v](D(r’))-‘#dr’        ,
temperature of a fuel cannot realistically be taken as                                 0
constant. The variations of temperature during irradi-
                                                                             where (D) is the average of D in the interval 0 < r < 7’.
ation are particularly relevant in MX-type fuels rated
                                                                                The integrals F, can be reduced to approximated
at high linear powers. Typically, the temperature of
                                                                             simple forms for the cases of increasing and decreasing
these fuels rises during the initial stage, and then
                                                                             temperature. For increasing temperature it can be seen
decreases slowly to asymptotic values. It is clear that
                                                                             that F, assumes the integrable form:
in this case, eq. (7) cannot be used, not even as an
approximate solution. Eq. (4) must thus be solved,
introducing the hypothesis of variable D,. Since T                           Fn(r)-&Jr’exp(-y)dr’
is a many-variable function, no analytical solution
can be obtained. On the other hand, a numerical
integration of the second order equation (4) would
result in a heavy complication of system (2) with                                                                               (104
the introduction of the unnecessary spatial variable.
However, it will be shown here that, by operating a                          For the case of decreasing temperature it can be easily
variable substitution and making reasonable approxi-                         demonstrated that F, can be approximated by:
mations, eq. (4) can be solved to obtain a simple
function for the grain boundary precipitation rate,
                                                                             Fn(7) - ~JT’         exp(- F)        dr’ ,         (lob)
presenting a close analogy with the previous formula
                                                                                           "0
for constant temperature.
    With the variable substitution:                                          where with 0, is indicated the average of D taken
m = c - at and             dr = D(r) dr      (ED*)      ,                    from the final time, back to the time at which r’ =
                                                                 (8)
                                                                             a2/n2n2. This “kinetic average” of the diffusion coef-
eq. (4) reduces to a simple form whose general integral                      ficient can easily be evaluated during the numerical
60                                           C. Ronchi / Fission gas pelvis   in MX-r+vpenuclear fiiels


solution of the system (2). Furthermore, since the
contribution of the progressive harmonics is rapidly
decreasing with n, the value 5 m fj, can be replaced
in each of the equations (lo), without altering the
nurne~c~ results. Substituting the simple integral
functions of eq. (I 0) into eq. (9) and applying the
inverse Fourier transform to the coefficients of the                                      ..,     .                                 I
series which do not contain exponentials, enables a                                   0               II)          2.0            30
simple expression for c(t, r) to be obtained. Finally,                                                           BlJWJp    ( %)

the release to the grain boundaries can be calculated                         Fig. 2. An example of release calculation for a fuel subjected
as:                                                                           to a varied thermal regime. The stages A, B and C represent
                                                                              three asymptotic trends of function (I 1). The case examined
$    = 4na2&u3)-‘D         5      _    (mol/cm3 * s) ,                        is a typical He-bonded pin of MC *inters, irradiated at 1350
                               I r-a                                          w/g.
Giving, for the two cases:                                                    in the following time is only determined by the term
                                                                              D/B, i.e., by the instantaneous diffusion coefficient
                                                                              and by the thermal history in a preceeding time inter-
                                                                              val, which is short when the kinetics around time t
                                                                              are rapid and long when they are slow.
               Oa
     +6Dat
       7      c
              n=lexp( 1  -- n21r2r
                               2         ’
                                                                                  The expression for release rate in the form given
                                                                              in eq. (11) can be inserted in the system of equations
                                                                              (2). Rowever, for the sake of formal completeness,
for increasing F                                                              the variable substitution, eq. (8) has to be inserted
                                                                              as a further differential equation in the system. With
                                                                 (11)         this formulation, the fission gas kinetics equations
                                                                              can be introduced into a fuel behaviour code system
for decreasing T.                                                             as a compact subroutine, with time and (variable)
The term in brackets in both formulae is ob~ously a                           temperature as calling parameters. Fig. 2 shows an
generalization of the fractional term already defmed                          example of a release calculation, made with the code
for cases of constant temperature. The term represents                        TPROF on a section of a carbide pm [2j.
the velocity at which the steady state is approached.
    In the case of increasing temperature, the last term
                                                                              3. Analysis of the properties of the bubble distribution
containing the exponential summation represents the
                                                                              in MX4ype fuels
ad~~on~ release rate due to the decrease of the
overall gas concentration at the higher temperature.                          3.1. Analysis of the bubble size distributions and
It is worth remarking that in many practical cases,                           evolution of their concentration as a finction of time
the fractional term in brackets may attain unity                              and temperature
after relatively short times (e.g., when an initial tem-
perature peak occurs). In these cases, the gas release                           A f~d~ent~       question in the analytical treatment
                                                                              of the fission gas swelling is the degree of accuracy by
                                                                              which the concept of bubble populations and size
* To this purpose it is worthwhile mentioning the difficulties                distributions has to be introduced. Rigorous approach-
    arising in the treatment of the coalescence processes in                  es have been proposed [3 ] trying to deduce the devel-
    oxide fuels. There, the experimentalobservationreveals                    opment of the bubble size distributions, starting from
    #at the interaction be?een fission spikes and bubbles is                  the nucleation processes, through alI the possible coal-
    more important than gas tipping and coalescence in                        escence events between individuals of the ~tribution.
    defining the concentration and size of the bubbles [5 J.
    In practice, in these fuels only large bubbles (in the 10 mm
                                                                              However, even assuming that the available theory for
    range) can be considered as permanent trapping sites.                     the nucleation mechanisms is valid and exhaustive *,
                                  C. Ron&i /Fission gas welting in MX-type occur   fitels                           61


this approach presents two difficulties, a conceptual          used for the observation: depending on the magnifica-
and a practical one. The first one consists in the intrin-     tion and on the optical resolution, parameters are
sic disadvantage of a too detailed description of an           defined like average sizes, concentrations, relative
idealized system, where quantities are calculated              frequencies, etc., which, strictly speaking, are
which, in any comparison with reality, are redundant           meanin~ess, since they are always referred to a
and even misleading if the limits of validity of the           limited number of visible features, which, is usually
theoretical description are not well known. In fact,           very small compared to the true total number of
the experimental observation shows that there-is a             possibly existing smaller individuals. Enlarging the
limit in the possibility of constructing an analytical         magnification on the observed field does not solve
picture of bubble formation in nuclear fuels. Even             the problem, first, because the true size distribution
in the simplest cases, the heterogeneity of the system         can in principle extend down to non~ete~table
on the microscope scale is so large that all the quanti-       atomic sizes, secondly, with a counting at very high
ties concerned (sizes, concentrations and rates) have          magnification, the statistical relevance of features of
to be averaged over relatively large volumes and the           large size inevitably loses any importance and, in con-
comparison with the analysis prediction has to be              sequence, phenomena of paramount importance in
based on these values. An analytical model for swel-           the macroscopic size range could pass unnoticed or
ling should also consider this stochastic aspect of the        be inadequately represented. The problem is also
phenomenon, which sets a limit to the deterministic            faced when, in some cases, a correlation has to be
analysis. The second difficulty is inherent in the for-        established between available porosity measurements
malism for the calculation of the coalescence events.          carried out with different methods (TEM, REM and
Even with the more recently formulated rate equa-              optical microscopy). In practice, considering the pro-
tions f4], where the mathematics analysis has been             blem from an en~neering point of view, many of the
significantly improved, size ~st~butions extending             measurements should not be taken too seriously and
over several orders of magnitude (as observed in               a typical step size would be given which does not
some cases in MX-type fuels) require long computing            necessarily coincide with that needed in a study of
times or result in important loss of precision in the          the, atomistic gas behaviour. Therefore, any observa-
calculations.                                                  tion would not be entirely objective, because the ob-
    An alternative method to describe the evolution            server intervenes in its de~nition. Nevertheless, in
of the bubble distribution is based on the concept             spite of these difficulties, one recognizes that for
of statistical population. This concept has been               results obtained in different limited observation
formally introduced in the basic kinetics equations            fields, the said size distribution parameters, as con-
(2), without a further definition, a population being          ventionally defined, are representative and significant
simply identified by its label k and by the three varia-       for the phenomena investigated. Furthermore, size
bles nk, rk and f)k. The choice of this method instead         histograms measured at different ma~i~cations show
of the deterministic one resulted mainly from the              strikingly similar characters (fig. 3): the distributions
difficulties arising in the description of the MX-fuel         are always skew and their maximum is not well defined,
swelling. There, intragranular bubbles grow to extrem-         but it depends on the (rather imprecise) frequencies in
ely large sizes, which eventually may akin to the              the lowest classes. The fact that pictures taken at dif-
intergroup      and sintering pores. A first question in       ferent magni~cations show identical features is not
the description of these widely dispersed sizes is the         astonishing. This kind of self-sim~~ty of the size
degree of accuracy by which the concept of size class          distribution functions of certain existing set of indiv-
(or distribution) are to be introduced. This is not, as        iduals is often occurring in natural phenomena. The
it seems, an inoffensive formal problem, but involves          reason for this peculiarity has to be searched in the
the significance of the experimental observations as           laws of discrete statistical aggregation of very large
well as their analytical prediction. In fact, starting         number of particles - in our case of voids [6]. This
from the former point of view, it can be realized that         suggest a new approach in the representation of this
each experimental determination of bubble size histo-          kind of distributions, basing their description on a
grams is strictly related to the experimental method           general formulation of the size generating mechanisms
62                                       C. Ronchi / Fission gas swelling in MX-type nuclear fuels

                                                                         tribution which is present with a characteristic con-
         a O”:60.                                                        centration n and persists through the whole irradia-
                               I            11                           tion time. This concept will be critically examined in
              40

               20   !l             ;I
                                                                         the next section. For the present purpose it will be
                                                                         simply assumed that the stable population subdivides
               OtJ-----L
                      123656       _123456l~ml
                                                                         the fuel volume into rr-’ cells, each one corresponding

          b 1:
                    nn
                                                                         to the zone of influence, or trapping volume of one
                               I            II
                                                                         stable bubble.
              40                                                             The creation of a gas atom within the cells can be
               26                                                        considered as a random event. It can be easily inferred
                                                                         that the number of cells ni where at time t, j creation
                                                                         events occurred is given by a Poisson distribution

                                                                         n,(t) = F @f exp(-a)        ,

                                                                         where CDis the average number of gas atoms per cell,
                    123456              1 2 3 4 5 6   lnml
                                                                         that, if /I is the creation rate, is given by:
Fig. 3. Three pairs of histograms representing the temperature           @ = pt/n .
effect on the fission gas bubble distribution, as observed in
diverse dimension ranges: (a) optically visible porosity, (b)            For large values of a’, we can assert that the gas atoms
bubbles observed by REM, and (c) bubbles observed by TEM.                in the sinks cells are normally distributed with variance
Both the shape of the histograms and the feature of the trans-           Cp.No hypotheses have been made so far concerning
formation due to the temperature increase (from I to II) show
a clear self-similarity of the distributions at the different mag-
                                                                         the bubble size and the effective capture of the atoms
nifications at which bubbles have been observed.                         of gas. The introduction of these two concepts leads
                                                                         to two fundamental relationships. First, according to
                                                                         the equation of state of the gas in the bubble, where
and on a statistical treatment of their field of occur-                  the pressure is approximately equal to 27/r, the volume
rence. The advantage of this approach is that the con-                   increase due to the precipitation of a gas atom is pro-
cept of expected (or observed) population enables                        portional to the bubble radius:
any order of description (or observation) to be                          aVj +rabi,                                         (12)
accounted for.
                                                                         where the differential ab, represents a capture event.
3.2. Statistical distribution of fission gas bubbles                        Secondly, independent of the definition of cap-
                                                                         ture event, which may concern a single gas atom or
   The phenomenon of formation and growth of fusion                      a small mobile bubble, the capture probability can
gas bubbles during irradiation is fundamentally of                       be demonstrated to be proportional to the surface
stochastic nature. Apart from the effects which are                      area of the bubble centered in the cell, and it can be
directly related to existing extended defects which                      written:
are randomly distributed in the fuel matrix (disloca-
tion networks and grain boundaries) and that will be                     abj = Kr2 azj ,
examined separately, the microscopic heterogeneity
of the fission gas distribution is basically determined                  where az, represents the probability of a creation
by the statistics of the creation events and of the fol-                 event in the cell. The factor K is a function of the
lowing migration processes.                                              kinetic constants and of the concentration of the
   To provide a simple satisfactory answer to the                        precipitation species. It can be easily demonstrated
question of establishing a theoretical distribution                      that when the steady-state regime is attained, K
function for the growing bubble sizes, the concept                       assumes a nearly constant value. Substituting for abi
of stable population is introduced, i.e., a bubble dis-                  into eq. (12) and passing to the differential notation,
                                 C. Ron&i / Fission gas swetling in KY-type nuclear JEte1.s                                 63


one obtains:
dV
-=Kdz=d(Kz)-zdK,
 V
and, after integration:

In V=Kz-           ‘zdK.
               s
               20


Because of the property of the function K mentioned
above, the integral at the right hand side will converge
                                                                Fig. 4. The theoretical density of frequency curve for a bubble
to a constant value, so that, for sufficiently long times       population is represented as a function of the bubble volume
the relationship between In V and z becomes linear:             sizes. The analysis shows that the total number of individuals
                                                                and their average size may be calculated, whereas the disper-
z = K-’ In V - constant .                                       sion of the distribution is proportional to the number of
But, as shown above, the sum of the creation events z           individuals involved in the population generating processes;
                                                                these may be gas atoms or smaller mobile bubbles.
is normally dist~buted, and thence so must be also
the logarithm of the bubble volumes. In conclusion,
the distribution is described by a frequency function
of type:                                                        important character of generality to this function:
                                                                even if the growth mechanisms of bubbles are com-
f(V) = (2n02)- ‘I2 exp -
                           ([ln(V-    VfJ - ml2
                                     2u2        I
where V. is the smallest admissible volume and m the
                                                                plex and different populations are s~ultaneously
                                                                present in very differing size ranges, the knowledge
                                                                of the ruling mechanisms enables a complete repre-
mean of the logarithmic distribution.                           sentation of the results in terms of relatively few
    This result enables a stable bubble population to           variables: any observed population, defined by its
be characterized by four parameters: m, Vo, n and u.            average size and its concentration n, is log-normally
The analytics dist~bution function may be used either           distributed with a fractional variance given by the
to interpret experimental data or to describe analytic-         ratio:
ally the bubble development. The first parameter is in
fact calculated from system (2), while a method to              u2 = n/nT .
evaluate the other ones is given in the next paragraphs          where nT is the total concentration of sub-individuals
(fig. 4).                                                        subject to the possibility of being captured.
    The above arguments can be extended to obtain                    Finally, thanks to the rna~ernati~~ properties of a
more general conclusions. The definition of capture              log-normal distribution, the analysis of the experimen-
event, as expressed above does not necessarily refer            tal porosity histograms can be carried out with a
to a particular type of individual (gas atoms) but it            simple formalism. In fact, if A(xlm, u2) is a distribu-
can be applied to other mobile gas carriers (e.g. smaller        tion function with parameters m and us, and Xiis the
bubbles) or to any combinations of them, for which a            ith moment, the ith moment dist~bution is defined
proper constant K may be calculated. If the number               as:
of individuals involved in the capture process is very
large compared to that of the sinks, the definition of
“creation” event maintain its random character (this
is the case, for instance, when in each sink cell a dense
population of smaller bubbles is present). Therefore,           It can be easily demonstrated that:
the same reasoning as for the single gas atoms can be
                                                                Aj(xfm, u2)= A(xl(m +iu2), a’),
repeated and a log-normal function still expresses the
expected size distribution of the sinks. This gives an          i.e., that all the moment distributions are also log-nor-
64                                C. Ronchi / Fission gas swellingin MX-type nuclear fkels


mal functions with parameters (m t&r’, u2). In partic-
ular, if the volumes (or sizes) are lo~norm~ly distri-
buted, so then are also the volume fractions (weight
fractions). This enables a suitable plot of the com-
plete porosity analysis data to be obtained. If a total
porosity P is measured, the fractional contribution
of each size class is plotted on probability paper, on
which the graph of a cumulative log-normal distribu-
tion is a straight line. Inspection of the curve obtained
enables a spectral analysis of the measured distribu-
tion to be carried out in terms of single log-normal
distributions, These can be individuated with a simple
numerical procedure, and the parameters m, VO and
o can be determined for each population and be com-
pared with the theoretically predicted distributions.
An example of this kind of analysis is known in fig. 5.
                                                                                               Bubble SW I unll=
                                                                                                               75 nmI

                                                                 Fig. 5. The porosity size distribution measured in a fuel pellet,
3.3. Coalescence and capture volume
                                                                 plotted on probability paper (o), can be deconvoluted, reveal-
                                                                 ing the presence of the single log-normal distributed bubble
   It is known that bubbles undergo random                       populations. In this case, where the irradiation temperature
(brownian) motion in the matrix. After a time t, a               was kept strictly constant, the populations are two(+); the
bubble will have moved a mean square distance F                  larger one is located on dislocation networks.
given by :
x= (6qJy2      ,                                     (13)        average concentration of the bubbIes. In fact, a
where Db is the bubble diffusion coefficient, which              simple relation:
is defined as the product of the diffusion coefficient
                                                                 n = $?rP)-r      ,                                         (14)
of the rate controlling atomic species (surface atoms
or vacancies) and a geometrical factor representing              relates the bubble concentration to the bubble cap-
the functional relationship between the discrete                 ture volume. Actually, the simplicity of eq. (14) is
atomic jumps and the displacement of the center                  only apparent, because the c~culation of Z@(t)can only
of gravity of the bubble. This factor is inversely
proportional to at least the third power of the bubble
size. Therefore, if eq. (13) is calculated as the integral
distance migrated by a growing bubble, it will be seen
                                                                         t=t-                                     :=t+rt
that Xwill rapidly. attain an asymptotic value and the
order of ma~itude of this value is dete~lned by the
distance migrated during the early life of the bubble.
This property of brownian bubble motion enables
a substantial simplification to be made in the descrip
tion of the coalescence processes. In fact, a bubble
from its nucleation time t, will sweep out a spherical
volume of radius Z It can be assumed that all the
bubbles possibly existing in this volume will have
coalesced into one (fig. 6). Therefore, if a correct
                                                                 Fig. 6. Scheme of the growth process of a single bubble, as
description of the bubble radius increase (due to                occurring during sweeping of its capture volume of radius X.
gas capture and coalescence) is given, the history               During its migration the bubble collects other bubbles (B)
of Xc&r be associated with the development of the                and gas atoms (A}.
be made with the aid of system (2), that furnishes the        sizes comprised between to and r+ has been expressed
gas precipitation rates, and of a form~ism accounting         with an interpolation formula given by:
for the average effect of the coalescence processes.
The treatment presented below provides a solution
to the latter problem, by cakulating the bubble con-
centration as a function of time and temperature,



   Q.,, the bubble diffusion coefficient results from
the sum of the main operating mechanisms of bubble
migration. Since, as will be seen later, the coalescence
processes are particularly effective at the beginning         3.3.2, Calculationform&sm
of the bubble growth when no fission products are                 The formulation of the rate equation for the bubble
present to contaminate the bubble surface, surface            concentration has to be made in the framework of
diffusion has to be accounted for in addition to the          system (2). The system provides at each time, the
volume diffusion mechanism. This gives for the bubble         spatial concentration bj of gas contained in the bubble
diffusion coefficient [e.g., ‘71:                             population of labelj, having an initial concentration
                                                              nf. An equation of state of van der Waals type is
                                                              established for the precipitated gas, having a concen-
                                                              tration bj fmol/cms fuel}
                                                              Abb nj, rj) = bjRT_ (‘ST! - bib*)
where h is the inter-atomic spacing, f a correlation
factor (in bee 0.72149), I?” the volume self-diffusion
coefficient, LP the surface self-diffusion coefficient,
and r the bubble radius.
                                                                 Xp($]=O,
    However, it can be seen that when I is very small,        where b* and a* are the co-volume and van der Waals
eq. (15) is no longer viable. In fact, for values of r near   pressure factor, respectively, and 7 is the surface ten-
to rot the atomic radius of the gas, the bubble diffu-        sion of the solid. trj represents the inst~t~eous con-
sion coefficient should converge to the value of Ds,          centration of bubbles. Differentiating eq. (17) provides
the atomic diffusion coefficient of gas. On the other         an expression for the bubble growth rate
hand, eq. (15) predicts for a monoatomic bubble a dif-
fusion coefficient three to four times larger than I>‘.
This result is certainly false because it originates from
a crude extrapolation of mere geometrical considera-          where dj is furnished by the code and 5 can be cal-
tions to the atomic size range, without accounting            culated from eq. (14) generalized for the case of
for changes in the migration enthalpy which gradu-            variable L+,, in the form:
ally appear when bubbles assume the character of
atomic clusters and eventually reduce to a single
atom trapped in a vacancy.
    Furthermore, the mech~ism of surface diffusion,
particularly rapid in small bubbles, can only be applied      The evaluation of eq, (18) is lengthy but straightfor-
to bubbles which are so large that the atomic strains         ward, It enables the inst~taneous bubble growth rate
around the precipitated atoms are completely relaxed          to be calculated as a function of the gas precipitation
and the concept of free surface can be introduced.            and coalescence processes.
This is thou~t to occur when the bubble radius                   (a) The case ofcu~ta~t te~p~~~r~. Figs. 7a.and
exceeds a value of r+, corresponding to a few atomic          7b show the calcualted values of n&t). The nucleation
spacings.                                                     of bubbles starts after an incubation time depending
    Therefore, the ~ffu~on coefficient of bubbles of          on the re-solution frequency and on the fission gas
                                      C. Ron&i / Fission gas we&g   in MX+ype nuclear fire18


                                                                     tion. Therefore, the amount of gas contained in
                                                                    bubbles which are “underway” becomes at times
                                                                    t >> at constant and depends only on St and not on t.
                                                                         If the steady-state condition is achieved within
                                                                    short times with respect to the irradiation period,
                                                                    the description of the fission gas behaviour may be
                                                                    substantially simplified. In this case, the interest is
                                                                    practically limited to the development of the first
                                                                    stabilized population, which solely controls the whole
                                                                    gas kinetics. This happens, for instance, at tempera-
                                                                    tures above 1OOOaCin MC, where the steady state is
                                                                    reached within a few days or less.
                                                                        The relatively small amount of gas contained in
                                                                    the bubbles subjected to capture is distributed in
                                                                    sub-populations which can be characterized by a
                                                                    sequence of parameters (n:, &I>, . . .. {nt;, Ah:),
                                                                    (fig. 8), defining steady state (not ~nd~y~ua~~y   per-
                                                                    sisting) populations, which, owing to this character,
                                                                    are not affecting the gas kinetics and are therefore
                                                                    not inserted in the rate equation system (2). It is
                                                                    worth remarking that, when the capture volume
                                                                    Vj(=) of the stable population exceeds the grain size,
                                                                    all the intragranular bubbles can be treated as steady
                                                                    state, non-growing populations. One finds in this case
                                                                    the same result obtained by conventional rate equation
                                                                    analysis [e.g., 11.
                      10~   10‘ x1” 106 IO7                             At low temperatures, where the steady-state con-
                                   lfme   (Sl
                                                                    ditions may be attained very late in the fuel lifetime,
Fig. 7. (a) Calculated concen~ation of gas bubbles as a Func-
tion of irradiation time at different temperatures, for a MC-
                                                                    the slower the kinetics, the more complex becomes
fuel rated at 200 W/g. (b) The concentration of gas in dyna-        the analysis, and the conceptual and formal advan-
mical solution is plotted for the same casts. The incubation        tages of the method, with respect to the deterministic
times at the various temperatures are indicated by the 7’s.         analysis, become less important. To describe the non-


diffusion  coefficient, The density of nuclei is cal-
culated from the concentration of gas in solution. It
can be seen that at time at after the nucleation has
started, a stable population is established with a
de~nitive concentration nj(m), corresponding to an
asymptotic capture volume V&m).This depends
mainly on temperature and, to a much lesser extent,
on the nucleation density. Since this also attains an
asymptotic value with time, a steady-state regime is                                    gas concentrnllon in bubbles   -
                                                                                                               ttlme   -1
finally approached, by which the calculation of the
nucleation-coherence-growth         process can be                  Fig. 8. For rapid kinetics (high temperatures) the effective
                                                                    bubble size ~s~ibut~on may be described as a set of a grow-
indefinitely repeated in time, with the result that,                ing population of invariable concentration no and steady
within periods of &, all new bubbles are ultimately                 state populations having a constant gas content Abi (and
captured by the initially established stable popula-
                                    C. Ronchi /Fission gas swelling in MX-type nuclear fuels                                     61


steady-state kinetics in terms of bubble populations,
the calculation procedure of nucleation-coalescence-
growth has to be repeated at regular times tl ... tk . ..
rM. In each time interval, a population of index j
0’ = 1, .... M) is nucleated and evolves with concen-
tration nj, gas content bi and size r,-(bj).The process
is illustrated in fig. 9. The choice of the time intervals
depends on the kinetics and on the precision require-
ments.
    Since the mobility of the populations decreases
with their average sizes, the new-born ones do gradu-                                              1, t ‘.’   time   -bgl

ally merge into those in the capture volume of which
they are migrating (fig. 9), proportionally to the
evolving ratio of their respective capture volumes.
A system of equations has therefore to be solved:
nr =n”*
bl = ii1 + i&‘2/V,];          1st population

rr = rr(br)




bj = Ej- Zj[ Vi/Vj_l]   :‘+ bj+l [ y+l/Vj] :’   jth popula-        Fig. 9. For slow kinetics (low temperatures) the asymptotic
                                                 tion              concentration no is attained only after a long irradiation
rj = r,-(bi)
                                                                   time, therefore the nucleation-coalescence-growth       process
                                                                   has to be repeatedly calculated, giving rise to a sequence of
                                                                   populations n1, .. . . nk. Their mutual coalescences are calcula-
                                                                   ted by the overlapping of their capture volumes VI, .. .. vk
where the circumflex indicates the self-developing                 (see bottom).
values, as represented in fig. 9. The parameters of
these populations are inserted in the basic system (2)
and hence affect the overall gas kinetics. It should be            sideration shows that this is operatively very useful
noticed that the number of populations needed in a                 where bubbles are treated around the experimental
practical calculation is limited, even for unlimited               detection limit.
irradiation times, because the latter-born populations                 (b) The case of variable temperature. If the tem-
are gradually absorbed by the preceeding ones and                  perature of the fuel varies during irradiation, more
their concentrations and effective gas content become              complex situations may arise in the gas kinetics. In
insignificant and they may be removed from the                     the case of a temperature increase, the previous cal-
equation system. Comparing this procedure to the                   culation procedure is still viable: the higher temper-
deterministic calculation of the size histograms, it               ature will produce an adjustment of the concentra-
can be seen that the concept of population (or “con-               tions of bubbles, whose extent depends mainly on
centration class’) replaces that of size class. Although           the sizes previously attained. Even a continuous tem-
this could be seen as a practically identical result, the          perature increase can be easily accounted for. If tem-
former concept still maintains a more articulate char-             perature decreases, the situation becomes more com-
acter. In fact, each concentration class is established            plicated. The newly forming bubbles are not suffi-
and defined on a totality of sub-individuals which are             ciently mobile to reach the preexisting stable bubbles,
not necessarily specified, but simply represented by               so that, in consequence, new populations will be
their average, or effective, properties. A careful con-            stabilized, having the characteristic concentrations
68                               C. Ronchi / Fission gas swelling in MX-type nuclear fuels

of the varied temperatures. The new stable popula-               answered in this connection, namely:
tions introduced are again labelled nl, .-., ni and have         - to which extent can the bubble nucleation process
to be inserted in the rate equation system. It is clear          be affected by the presence of preexisting bubbles;
that the description of the bubble behaviour in terms            - how can the minimal size of a distribution of stable
of a continuously decreasing temperature presents a              bubbles be determined.
fundamental difficulty. In fact, the number of popula-                It is known from the theory of nucleation and
tions which can be introduced in the equations can-              growth of precipitates from oversaturated solutions,
not be increased inde~nitely: even with large comput-            that the stability of small precipitates can be affected
ing units no more than lo-20 populations can be                  by the presence of larger ones, which “suck” from
processed in acceptable times. On the other hand, a              them atoms of solute, growing at their expense. The
too close description of the effect would lead to a too          phenomenon, commonly called ripening effect, occurs
deterministic analysis, that could be insignificant.             according to relatively slow diffusion processes, activ-
Therefore, a criterion has to be looked for in the               ated by the difference in ~ermodyn~c        potential
exper~ental observations, so as to minimize the                  between precipitates of different sizes. This pheno-
number of populations of bubbles introduced. Re-                 menon can also be expected in the system formed
garding MX-type fuels, subjected to relevant cool-               by fission gas-in-solid and gas bubbles, taking into
down during irradiation, it can be seen [8] that,                account the typical environment condition of a
after a central temperature decrease from 2000 to                nuclear fuel.
 1500°C and a burn-up of 1 to 5% FIMA, the bubble                    There the ripening mech~ism can be described
sizes extend up to l-5 pm and the experimental                   as follows:
histograms may be easily represented with less than              The fission gas concentration gradient in the vicinity
5 classes log-normally distributed. This would mean              of a bubble surface decreases with the pressure of the
that the bubble concentration adjustment may be                  gas within the bubble. Bubbles of larger sizes have
introduced stepwise, following temperature varia-                then a precipitation flux (i.e. a flow of gas per unit
tions of the order of Sl to 100°C.                               surface area) ~orrespon~n~y higher than smaller
                                                                 ones. Under steady-state conditions (gas created at
                                                                 constant rate) and when large oversaturation levels
4. Interaction between bubbles of different size                 are attained (low temperature), this difference is
classes: ripening effects and limit for continual nuclea         negligible, but it becomes significant when the con-
tion                                                             centration of gas in solution approaches the solub-
                                                                 ility value (high temperature). Therefore, if two
    The range of stability of the bubble sizes is a              bubbles are sufficiently close together (high spatial
fundamental aspect of the swelling analysis of MX-               concentration) and their inner pressures differ suffi-
type fuels. In fact, it has been emphasized that the             ciently, the bubble at higher pressure (usually that of
temperature variations occurring in these fuels during           smaller size) is expected to emit gas, which will flow
irradiation produce substantial modi~cations in the              into that at lower pressure (see fig. 10).
fmion gas bubble populations. In particular, it has                  The results show that, although the ripening
been shown fhat’when temperature decreases, new                  mechanism occurs at a relatively low rate, it can play
bubble populations with higher spatial concentration             an important role for fission gas swelling.
are predicted to nucleate and grow. Based on mere
kinetics arguments, new bubbles should be continu-               4.1. The equilibrium equations between fission gas
ously produced in this case, and the new nuclei, of              concentration and bubbles of different sizes
increasing concentration, should capture the largest
part of the gas created, preventing growth of the                    During irradiation, a fission gas bubble of radius ri
larger pre-existing bubbles- The effect is obviously             is supposed to grow by capturing gas atoms, and,
of great significance for swelling, so that the condi-           subsequently, a suitable number of vacancies till the
tions must be studied beyond which this analysis                 gas expands and reaches a pressure equal the capillar-
ceases to be valid. Two questions have thus to be                ity tension 2r/ri. If c is the oversaturation concen-
                                     C. Ronchi /Fission gas swelling in MX-type nuclear fuels                              69

                                                                    By differentiating and summing over i, one obtains:


                                                                                                                        (22)

                                                                    where db/dt is the gross rate of precipitation of gas,
                                                                    as defined in section 2.1.
                                                                       Summing eq. (2 1) over i and substituting into eq.
                                                                    (22), one obtains an expression for c(R$:


                                                                                                                        (23)

                                                                    where T-is the average size of the bubble distribution
                     II                                             and N the total number of individuals.
Fig. 10. Three cases of ripening: two bubbles of different sizes        The last quantity still undefined is the gas concen-
(I and II) generate an asymmetry in the effective gas concentra-    tration in the vicinity of the bubble surface, c(ri). To
tion (middle curves). According to the size difference of the       determine this quantity, it must be assumed that the
two bubbles and to the level of the gas concentration with
respect to the solubility value (dashed line), the smaller bubble
                                                                    matrix has a finite (though small) gas solubility. If
can be stable, stationary or unstable.                              AHs is the heat of solution of fission gas, the equili-
                                                                    brium concentration of fission gas in the vicinity of
                                                                    the bubble is determined by the internal gas pressure,
tration of gas, the rate of growth of the bubble is
                                                                    and is given by:
given by:
                                                                             27K
$($ rr& = 47rx2Ds 5 !CI,                                            c(li) = -kTr exp(-LWg/W      ,                        (24)
                                                          (20)                  i
                                                                    where K is temperature independent parameter
where D, is the gas diffusion coefficient and CI the
                                                                    [9,10]. Finally, by substituting eqs. (23) and (24)
molar volume of the gas. In eq. 20, x denotes the
                                                                    into eq. (22) one obtains:
radius of a sphere, contained in the capture volume
of the bubble. The molar volume of the gas is
assumed to correspond to the equilibrium pressure;                                                                        (25)
using the perfect gas equation of state *, one obtains:
                                                                    with
52= Vbubbre/n= kTri/27 )
                                                                    M=27
                                                                       k~ exp(-1WplkT) .
where 7 is the surface tension of the solid. By writing
in explicit form the derivative of eq. (20) and inte-
                                                                    The final equation means that the growth rate of
grating between ri and the radius of capture of the
                                                                    bubbles with radius ri is equal to the sum of a posi-
bubble R,, one obtains, for R, > rl,
                                                                    tive term (the first in the bracket) determined by the
                                                                    gross precipitation rate and a term (second in the
                                   with A = kTD,/2y .(21)
                                                                    bracket) whose sign and extent depends upon the
                                                                    distance of ri, in units of F from the centre of the
It is now supposed that bubbles of different radii ri
                                                                    distribution. Thus, bubbles larger than F have an
(i = 1, .... IV) are present in the matrix; the equation
                                                                    enhanced growth rate, while the smaller ones are
of state is valid for each one:
                                                                    retarded. Therefore only a subfamily above a certain
rf = 3nikT/8rry .                                                   size is predicted to be stable at a certain temperature.
                                                                    A determination of this threshold size is only pos-
* Assuming the van der Waals law the following arguments            sible if the value of db/dt is known. According to the
  hold a fortiori.                                                  previous kinetic model, the gross precipitation rate
70                                          C. Ronchi /Fission gas swellingin MT-type nuclear fieIs


at sufficiently high temperatures decreases (after an                        within the order of magnitude of the mean value of
initial stage of increase) to a value which can be up                         the existing distribution. This is confirmed by the ob-
to two orders of magnitude lower than the creation                            servations [ 81.
rate of gas. Therefore, the bubble coarsening mecha-                          - At low temperature (small F and Ds), the effect is at
nism should be proportionally enhanced. From eq.                             first sight negligible (rmin/r is very low). However,
(29, the smallest bubble radius having positive                               since there is a nearly direct proportionality between
growth rate can be expressed as:                                             r min and the total concentration N, the latter cannot
                                                                             rise indefinitely, no matter how low the temperature
pin      =
             [
                 3 :Qno4
                           p@NL/Dg)-1
                                            1
                                        + 1 -9                               is. For that reason eq. (26) establishes a limit for the
                                                                             continual nucleation of bubbles. At each temperature,
(in SI units), where i? is the gas solubility under stan-                    the concentration of bubbles is confined below a cer-
dard pressure conditions. The relationship between                           tain limit. For example, taking the lowest value for
the smallest stable bubble size and the environmental                        the gas diffusion coefficient in a nuclear fuel, i.e., the
parameters is simple, yet the parameter i? is badly                          radiation enhanced term (10-r’ m2/s at 10” fissions/
known and therefore only a limited use of eq. (26)                           m3 * s), it results that the bubble population density
can be made. In fact, an estimate of the rare gas solub-                     should remain below 1O24m-‘* , this is the extreme
ility has only been obtained for UC, using fractional                        situation where all the bubbles are formed at nearly
release data [ 111. A thermodynamic expression of the                        the same time. When a preexisting distribution is
solubility, as used in eq. (24) can only be deduced from                     available (e.g., in the case where cooldown follows a
theoretical lattice calculations. However, the values of                     preliminary high temperature irradiation period) the
AHs predicted are extremely large [12,13] and the                            limit of N decreases proportionally to the concentra-
solubility values obtained are far below the experi-                         tion and sizes of the existing distribution.
mental values. An application to a concrete case (UC                         - According to eq. (25), a size distribution under
irradiated above 1000°C) has been made, based on                             steady-state irradiation is expected to vary: the
crude extrapolations of the experimental data for T.                         largest individuals grow faster than the smallest, and
The results are shown in table 2. The figures presented                      the latter may eventually become unstable in the
have only an indicative value, nevertheless some inter-                      evolving distribution, so that the number of stable
esting conclusions can be drawn:                                             individuals tends to decrease with time. However,
- At sufficiently high temperature the ripening mech-                        the preferential growth of the larger bubbles stops
anism confined the size range of the stable bubbles                          when their inner pressure is predominantly deter-


Table 2
Efficiency of gas ripening at different temperatures

                            Temperature (K)

                            1300                 1500                1700

p(mol/m3 * s)                           -        3x10-17         -

Z(mol/m3)                   10-16                3 x 10-16           10-15

N(mT3)                      lo*‘-1020            1o*o-10’9           10’9-10’s

                                                                        x 1O-2 a)
rmin                                            {lo-2 1
                                                 10                  {6 X10-l

     r                      {lOI
                             10 1               {lo-l
                                                   1                 rib)

a) From an average value of D, taken from the literature.
b, From a value of D, measured in ref. [ 91.
                                 C. Ron&   /Fission gas swelling in MX-rypenucIeatfuels                               71


mined by the applied hydrostatic restraint (this               tural changes in the fuel. The restructing (grain
occurs under standard pin design conditions in the             growth and pore migration) does not attain the
size range IO-’ - 1 pm), thereby preventing the                marked character of the oxide restructuring at the
ripening mechanism from assuming a divergent                   same ratings: generally, long-range migration of
course, ending with a disruptive swelling.                     pores in MX-type fuels is confined to regions where
    Finahy, the question arises why the coarsening             both temperature and temperature gradient are met
effect, whose mechanism is based upon general                  in an optimum range of values. In consequence, this
thermodynamic considerations, should be effective              process cannot produce in the fuel a substantial mat-
in MX-type fuels and not, for instance in oxide fuels.         ter transport along the pellet radius. However, the
The answer can be reasonably found in the different            short-to-medium range migration of pores may pro-
nature of the fission spike resolution processes occur-        duce locahy important changes in bubbles, since
ring in the two types of materials. The observations           these are swept out by moving pores.
made in studying the re-solution effects indicate that             Since the fission gas swept by pores exerts on the
fission fragments in oxides do not only re-eject single        fuel a different swelling action, due to the increased
gas atoms from bubbles which are close to the frag-            probability of escaping from the pellet, a quantita-
ment path, but also produce relevant material dis-             tive treatment of the sweeping effect is needed in
placements into the struck voids. This is in agreement         any complete swelling analysis.
&ith the results of the study of the surface tracks of             In MX-type fuels, fission gas bubbles quickly
fission fragments in UOZ [ 141. Collisions events              attain sizes of many hundreds of hgstrbms. The
between fragments and bubbles are believed to cause            gas under these conditions obeys the normal equation
the immediate destruction of the bubbles if they are           of state, where the pressure is near the equ~ibrium
sufficiently small [5,15] and to create new bubble             value. As indicated in eq. (12), the relationship
nuclei within the spike volume [5]. If the lifetime of         between the gas contained in the bubbles and their
the individual bubbles is consequently drastically             fractional volume is of type:
reduced, slow processes like ripening become insigni-
                                                               AVf V = Kb3j2 ,                                      (271
ficant. In fact, the simple situation observed in oxide
fuels (little variation of bubble concentration with           where K is a constant. The non-linear dependence of
time and temperature and relatively uniform sizes              swelling on gas concentration leads to important con-
[5,16,17]) is thought to be the net effect of counter-         sequences. Let us suppose that during an irradiation
acting bulk resolution and coalescence phenomena.              period t, gas amounts bi are repeatedly swept out
On the other hand, although no experimental data               after having produced a swelling AV,lV; at the end
are presently available concerning the resolution              of the irradiation the total swelling produced will be:
mechanism in &%X-typefuels, theoretical calculations
of the temperature and stress fields in the spikes [ 181
exclude that sputtering processes and bulk displace-
ments can be signi~c~tly produced in these com-
                                                               where (AV/V&      represents the swelling ratio that
pounds. The interaction of the fission fragments with
                                                               would have been produced in the absence of sweep-
bubbles in MX-type fuels should therefore merely
                                                               ing.
result in re-ejection of gas atoms by primary and
                                                                  In the case where the created gas is periodically
secondary collisions.
                                                               and completely swept out, relation (28) assumes a
                                                               simpler form. If At is the irradiation time and At/J
                                                               the sweeping period (or the bubble lifetime), the
5. Bubble lifetime and effect of sweeping on overall
                                                               final swelling is
sweIBng

    The thermal conditions attained in MX-type fuels                                                                (29)
irradiated in present standard pins at the highest ob-
tainable ratings produce to a certain extent, struc-           Eq. (29) indicates that if the bubble lifetime is suffi-
12                                  C. Ronchi /Fission gas swelling in MX-type nuclear fuels


ciently short (limitedly equal to the bubble nuclea-               motion has a minimal effect on the configurations ob-
tion time), gas is effectively swept out as single atoms           served in the fuel after irradiation.
with no swelling. Actually, eq. (27) from which eq.                   (b) Sweeping rate due to pore motion in a con-
(29) stems, does not apply to very small bubbles,                  stant direction due to thermal gradients. If a popula-
where, due to the high pressures involved, van der                 tion of pores with concentration Ne is migrating up
Waals equation of state must be used. In this case, it             the thermal gradient with a velocity u, and the bubbles
can be seen that swelling is nearly proportional to                are relatively immobile, their sweeping rate is given by:
the gas mount and hence sweeping of bubbles does
not produce significant benefits. In sum, eq. (29) has                                                                    (31)
a finit limit for J + =, which is chiefly determined by
the co-volume of the fission gas.                                  where dV/dt is the rate of volume sweeping:
    After these preliminary remarks, the analysis is               dV
aimed at determining the frequency of the sweeping                          f     .
                                                                   dt==r        uy
events in specific cases, considering the relative mobil-
ities of pores and bubbles. On this basis, a half-life             the mean life for bubbles can thus be expressed as:
time for bubbles can be defined and used for a statis-             ;ro = (N07+$)-’     .                                  (32)
tical correction of microscopic swelling.
                                                                   The bubble lifetime depends on the specific surface of
5.1. Various sweeping me~~nisms                                    the porosity and on its migration rate. The former is
                                                                   given as characterizing parameter of the initial fuel
   (a) The sweeping rate due to brownian motion of                 structure, and its evolution is calculated according
both populations, of pores and bubbles, having con-                to mechanisms explained in the next paragraphs.
centrations No and N, respectively, with mean radii                More difficult is the determination of u in MX-type
re and r and diffusion coefficient De and D, is given              fuels, where the usual formulae for pore migration
by 1191                                                            established for oxides seem to be unvalid. Taking
                                                                   experimental values of u measured in laboratory
dN
dt = 4n(& + D)(r,, + r) NON.                            (30)       experiments under reactor heating simulation condi-
                                                                   tions [20], one obtains for MC:
The mean lifetime is then defined as
                                                                    108s 270 > 106s,
r. = [47rNo(Do + D)(ro + r)] -’ .                                  in the temperature range between 1500 and 1800%,
                                                                   and gradients of the order of lOO”C/mm. Sweeping
If the two populations differ greatly in size and mobil-
                                                                   is therefore certainly effective under thermal condi-
ity, the sweeping rate depends principally on the pro-
                                                                   tions which can be attained by highly rated MX-type
duct between the higher ones of these quantities, and
                                                                   fuels. However, an analytical expression for the pore
on the concentration of the “collecting” population,
                                                                   migration rate in these compounds is at present mis-
the value of which is supposed to remain unchanged.
                                                                   sing.
    Since in brownian phenomena the mobility of an
                                                                       (c) Sweeping rate due to pore motion in a random
individual is inversely proportional to its volume, the
                                                                   direction due to local driving forces. In (a), it has
rate-controlling mobility for sweeping is that of the
                                                                   been shown that brownian motion of pores in the
smaller fission gas bubbles, while the sweeping cross
                                                                   size range above a few thousand angstroms is negli-
section is determined by the larger pores. A numer-
                                                                   gible because the centre of gravity of individuals of
ical estimate of the bubble mean Iife in a typical car-
                                                                   these sizes can only be displaced by extiemely high
bide fuel at 2000°C gives
                                                                   numbers of atomic jumps. However, random motion
7-O -    10’S    (for vaporization mechanism),                     of large pores is still possible if local forces are acting,
                                                                   to drive the vapour transport in microscopically well
70   -   10” s   (for solid state diffusion),
                                                                   defined directions.
for bubbles of 500 A radius. This means that brownie                   In practice, this occurs when differences in curva-
                                 C. Ronchi / Fission gas swelling in MX-type nuclear firels                              73


ture exist on the pore surface and/or when the pore is           calculated according to eq. (32) and is given by:


                                                                                                   1
bounded by two or more free surfaces having different            dN _N
surface energies. In fact, the equilibrium partial pres-
                                                                 dt-
                                                                                         exd-Q/R T) p
sure of the vapour is related to the curvature t and
energy y of the evaporating surface by the equation              where a is the actual radius of the grain. It is worth
 [21]:                                                           remarking that the effective sweeping rate of the
                                                                 bubbles decreases with time due to the concomitant
P = PO wGW/R W ,                                                 growth of a and Fa. The size limits above which eq.
where p. represents the pressure over a random                   (34) becomes effectively zero must be experimentally
oriented plane evaporating surface and a the mole-               determined for each type of fuel.
cular volume.
                                                                 5.2. Calculation of the sweeping effects in a general
   Since the driving force for matter transport
                                                                 swelling model
through the vapour phase is given by the vapour pres-
sure gradient in the pore, the velocity of transport                 The above treatment may be introduced in the
of the pore can be written as:                                   general calculation of the fission gas swelling with dif-
                                                                 ferent formalisms and degrees of approximation,
u = (D.$/RT)   grad(p) = (Q/RT)’ AypDJr’        ,    (33)
                                                                 depending on the importance of the role that sweeping
with D = vapour diffusion coefficient, and s2 = solid            phenomena are believed to play in the examined cases.
molecular volume; where Ay is a possible existing sur-               As far as MX-type fuels are concerned, in almost
face energy difference between the two halves of the             all cases the correction for sweeping effects can be
pore surface. Considering that Ay can reasonably                 introduced at the end of the calculation, applying eq.
attain values up to a few 10-l J/m’, it can easily               (29) where the factor J can be evaluated as the ratio
be seen that considerable velocities (X lo-l2 m/s) can           between the irradiation time and the bubble mean
be obtained already at temperatures of 18OO’C.                   lifetime. Experiment shows that this is a reasonable
Sweeping due to random migration of pores by pre-                approximation for (1 0 J < 2. The complementary
ferential vapourization is predominant in the high-              correction for gas-in boundary concentration can be
temperature central pellet regions, where the temper-            made using eq. (4).
ature gradient falls down to a few lOO”C/cm [8].                     In cases where sweeping is particularly rapid (e.g.
    (d) Grain boundary sweeping. Grain boundary                  in carbides and carbon rich carbonitrides, during for-
migration due to grain growth processes can produce              mation of zone II [8]), a decay equation for the
remarkable sweeping of bubbles in a wide temperature             bubble concentration can be applied. Using the para- ’
range. In MX-type fuels, bubbles of sizes up to several          meters of the general model, if b is the concentration
hundreds of angstroms are observed to be easily swept            of gas-in-bubbles, the amount of gas swept during the
off by moving boundaries 181. Only large pores, which            time dt can be expressed as:
are subjected to a weaker specific driving force, are
left behind the moving boundaries up to temperatures
at which their mobilities become comparable to those
of the grain boundaries [20]. Experiments performed                 A previous evaluation of the bubblelifetimes gives
on various fuels of high fractional density, under tem-          a criterion for the choice of the integration time step.
perature gradients and for times up to 500 h [20],               Obviously the description of the system in the case of
have shown that grain growth occurs at constant                  a high sweeping rate becomes less accurate because of
volume rate, according to the formula:                           the large heterogeneities which are actually introduced
d Vgrain                                                         by sweeping. Moreover, in these cases, microscopic
-        =Kexp(-QlRT).                              (34)         swelling is small and therefore the absolute error intro-
   dt
                                                                 duced is negligible. On the other hand, the analysis of
In the model calculations, the measured rates are multi-         the macroporosity behaviour does become more accu-
plied by a factor (1 - F,) accounting for the increasing         rate in order to correctly describe the release rate and
grain boundary porosity Fa. The rate of sweeping is              the effective local swelling.
14                               C. Ronchi / Fission gas swellingin MX-type nuclear fuels

6. Dynamics of the porosity growth                              defects with the effective internal and external stress
                                                                fields. As long as the matrix can be considered as iso-
    In the previous treatment, nothing has been said            tropic with respect to the migration mechanism of
about the mechanisms of bubble and pore growth                  point defects, the growth and the shrinkage of poros-
following the fission gas precipitation. Porosity does          ity are equivalent processes, where the driving force
grow until the pressure of the contained gas p, the             is simply reversed. Even with the simplest models,
resulting capillar stress due to the surface tension y          the calculation of the matter flow from or into the
and the external hydrostatic stress crOachieve the              porosity requires some essential hypotheses about
equilibrium condition satisfying the equation:                  the nature and the distribution of defect sources and
                                                                sinks.
p - 27/r + (IO = 0 .
                                                                    Let us first consider fission gas bubbles, which
Assuming a proper equation of state for the gas,                grow within elemental volumes containing only dis-
which enables the pressure p to be expressed as a               location with density p. The problem of calculating
function of the bubble size r, the so called bubble             the point defect kinetics in this environment has
equilibrium radius can be readily calculated. In most           been widely treated in the literature on void forma-
of the swelling models, the effective bubble size is            tion in irradiated materials. The current models are
simply assumed to be equal to its equilibrium value             based on two steady-state equations for the concen-
r”. Actually, this hypothesis deserves a careful dis-           trations of vacancies (v) and interstitials (i), of type:
cussion. The forces driving the bubble growth to the
equilibrium configurations are finite and decrease                                                                    (35)
when the effective radius approaches Y’, so that in
principle the equilibrium size is only asymptotically            where Dv and Di are the diffusion coefficients for
attained with time. Therefore, before making simpli-             vacancies and interstitials, respectively; Z are bias
fying assumptions, an analysis has to be performed               factors describing the different interaction force of
of the time scale of the growth kinetics under the              vacancies and interstitials with dislocations. In eq.
different specific conditions of the irradiated fuels.          (39, defect creation rate by irradiation and annihila-
The situation of the fuel porosity during irradiation           tion rate of Frenkel pairs have been omitted. The
is non-stationary;   gas atoms are continuously precip-         boundary conditions which are usually assumed
itating at variable rate and with the increase of                [22-241 are that the concentration of point defects
bubble size, each precipitated gas atom requires                on the free surface is equal to the equilibrium value
an increasing number of vacancies in order that the             in the presence of a stress field CJand that the net
equilibrium condition is established. Therefore, it is          flux on the cell interface (r = /3, the bubble interdis-
to be expected that when vacancies are not suffi-               tance) is zero. This hypothesis is only approximately
ciently mobile, a net overpressure is created in the            correct because it does not take into account the
bubbles, which are constantly prevented from achiev-            actual cell expansion due to swelling, however, for
ing their equilibrium size. The need for such an analy-         large /3and small bubble radii, the flux at the inter-
sis is evident when transient swelling has to be                face can be reasonably assumed as small. With these
described; however, because of the very low self-               boundary conditions, the general solution of eq. (35)
diffusivities involved, a dynamic model for bubble              is of the form:
growth becomes essential in MX-type fuels also under
steady-state regime.                                            G(i)   = r -’   [tit,))   exdG&$


5.1. Mechanism of growth of bubbles and pores

    The growth of the fuel porosity is atomistically
described by a process of precipitation of vacancies            where cc’) and d2) are constants determined by the
and emission of interstitials from the pore free surface,       boundary values. If the stress field energy is lower
activated by the energetic interaction of the point             than kT, the bubble rate can be expressed in a simple
                                     C. Ronchi /Fission gas swelling in KY-type nuclear fuels                             15


form:                                                               treatment of swelling and of the two new quantities
                                                                    D, and p.
‘c= a214 grad@,) - Digrad(ci)
                          Ir_                                           Unfortunately, the dislocation density is hardly
                                                                    obtainable from standard fuel characterization data.
                                                                    On the other hand, comparison of eq. (36) with
                                                                    experimentally determined [26] creep rules in MC
where D, is the self diffusion coefficient, (Ythe bubble            fuels, shows that the theoretical formula would fit
radius and G! the molecular volume.                                 the phenomenological law if dislocation densities of
    It is clear that formally, eq. (36) is equivalent to             10’3-10’4 m-* are assumed. Of course in this com-
the results obtained by applying a Nabarro-Herring                  parison, a discerning criterion is needed to sort out
creep mechanism to a spherical configuration (fig. 11).             only those measurements which can be significantly
In fact, the treatment given by Herring for a poly-                 fitted into the operating mechanism mentioned above.
crystalline medium with tangential stress relaxed at                Thus, results have to be chosen among those ob-
the boundaries, leads to the analogous relationship                 tained from single or arc-melted samples, where grain
 [25] :                                                             boundary sliding, microcracks propagation and other
                                                                    deformation mechanisms related to the ceramogra-
P = oszO,L-*(a, b)/kT     ,
                                                                    phic structure are effectively unimportant. Also to
where the effective source-sink distance L is here                  be excluded are creep rules where the deformation
expressed in terms of two independent grain dimen-                  mechanism is in part operating through short circuit
sions a and b. A similar expression can be derived                  paths (as in MCI_,, where the metallic phase prov-
from eq. (36) by calculating the effective strain rate              ides a fast diffusion mechanism for the cations and
of the cell of radius 0, whereby the distance L is ex-              the matter flow is consequently determined by the
pressed as a function of the bubble interdistance, of               anion diffusion [27]).
the bubble size and of the dislocation density:                         In conclusion, to calculate the bubble growth rate
                                                                    two approaches are possible, the first one following
L = PI..% P, PI -
                                                                    an atomistic description and determining the matter
In conclusion, the growth of bubbles is expected to                 flow by eq. (36), the second one, by introducing
occur via a diffusional creep mechanism whose con-                  directly the phenomenological creep equations. The
stitutive law can in principle be expressed as a func-              choice of the method has to be made considering the
tion of parameters which are already included in the                reliability of the available experimental data entering
                                                                    in the rate equations.
                                                                        The same argumentation may be applied to the
                                                                    description of the growth processes of large pores
                                                                    (sintering pores and intergranular pores created during
                                                                    irradiation). The fuel volume may be decomposed in
                                                                    cells containing a pore in the centre. In this case, the
                                                                    elementary volumes contain all the existing fuel
                                                                    defects, including dislocation networks and grain
                                                                    boundaries. Therefore, the deformation of the cells
                                                                    can take place according to additional mechanisms,
             \      I                  -L/
                                                                    involving the more complex defect configuration
                                                                    available. If a creep rule is assumed to describe this
                                                                    deformation, this must have the general form:

Fig. 11. The growth of a fissiongas bubble has to be inter-         e = Ko” exp(-AH/RT)         ,
preted as a creep process of its surrounding shell under the
action of the imbalance between the gas over-pressure and the       where n, K and AHvary with temperature and stress,
stress field in the matrix. The creep property of the shell is      according to the predominant operating deformation
determined by the point defect and dislocation behaviour.           mechanism.
76                                C. Ronchi /Fission gas swellingin MX-type nuclear fuels

     Even using different creep laws for the description        lations or to the sintering porosity) gradually develops
 of the growth of pores and bubbles, a joint continuum          under the action of a stress generated in part by the
 creep formalism may be usefully adopted, dealing with          individual itself and in part by the surrounding poros-
 the more flexible concepts of strains and stress instead       ity, a realistic expression of its rate can only be ob-
 of size rates and local pressures. In addition, it will be     tained after introducing a model for the interaction
 shown ln the next paragraph that with the continuum            between the various kinds of cavities in the matrix.
 formalism, the boundary conditions can be expressed            The analytical procedure consists in solving a sequence
 in terms of stresses, involving more consistent physical       of problems:
hypotheses than those mentioned above.
     Finally, experimental creep laws should be adop-           6.2.1. Representation of the stressed porous medium
ted for the calculation of both pore and bubble
growth, ln the temperature range where the radiation-
enhanced kinetics becomes predominant. In fact, it is              In fig. 12 is shown a schematic representation of
known that inserting a source term in eq. (35) describ-         the porous fuel: this is divided into spherical cells,
ing the radiation defect production, results in an addi-        each one containing in the centre a macroscopic pore.
tional flow term, which causes a spontaneous (stress            The radius of cell b and that of pore a are related to
independent) porosity growth. However, a theoretical            the porosity F, and the concentration of pores Nr, by
evaluation of this term for the fuel lattice seems to be        the equations:
at present difficult to obtain. Furthermore, as discus-
sed by Hesketh [28], the influence of radiation                 b = [_&(F]1’3,              a= (j!A)1’3      .           (37)
damage on Nabarro-Herring’s creep only occurs in an
indirect way, by affecting the dislocation concentra-
tion. The present state of the theory of irradiation            The stress field in the spherical shell has defined
creep in nuclear fuels is not yet advanced enough to            boundary conditions: on the inner surface, the stress
permit reliable applications of general formulae to             is determined by the imbalance between fission gas
model calculations. Therefore, the few existing exper-          pressure and surface tension; on the outer surface,
imental data on in-pile creep have been hitherto pre-           the stress is equal to the local value of the “geome-
ferred for working applications.                                trical” external field. So far, the stress conditions on
                                                                the cell boundaries will be considered as isotropic
                                                                and treated in terms of pressures. However, more
6.2. Expression for the porosity rate equations


    The physical hypotheses introduced in the prece-
ding paragraph enable a first formulation of equations                           Boundary   conditions   :
(2a) to be obtained so that the system can be eventu-
ally integrated. A first attempt to solve these equa-
tions under more simplified assumptions has already
been made, to analyze the rapid bubble growth during
reactor power excursions [29]. A model, based on
nearly equivalent hypotheses has also been developed
to study bubble growth in U02 and y-U [30]. At
present, these ideas are widely used for the analysis of
fuel swelling under reactor power and/or temperature
excursions.
    The proposed aim is to give a unified picture of the
porosity evolution, considering as far as possible the          Fig. 12. Representation of the fuel elementary volume for
actual properties of the porous medium. Since an                the calculation of the interacting growth of pores and bubbles.
individual void (belonging to one of the bubble popu-           Zext is the local mean stress fiald in the fuel.
                                 C. Ronchi /Fission gas swelling in MX-type nuclear fuels                                    77

general conditions can be assumed if required by the            posed to be provided experimentally.
examined cases.                                                     To deduce the stress distribution in the hollow
   If ‘ysbis the grain boundary surface energy and pP           sphere, starting from the plasticity condition, the
the gas pressure in the central pore and u. the mean            same procedure can be followed as in the elastic case;
value of the local macroscopic stress field, it follows:        the results are thus analogous with those reported in
                                                                ref. [31].
-u,(a) = pi = Rp - 27.&,/a ;   -u,(b)   = p. = -(To (38)
                                                                    The radial stress component is given by an equa-
    Furthermore, the medium constituting the shell is           tion of the type:
represented as a set of small sub-cells, centered on the
                                                                u,(R) = GR+”                 +D ,                           (41)
fission gas bubbles and having the same characteristics
as the large cell to which they belong. Equations anal-         where
ogous to eq. (37) relate the microscopic swelling /A            G = (pi _ po) $/nb3/n(a3/n _ b3P)-l ,
and the bubble concentration to the sub-cell radius fl
and the bubble radius o. The boundary conditions are            D = (pop/n _ pia3/n)(a3/n _ b3/“)-’             .
also analogous to eq. (38), whereby the stress acting
on the sub-cell surface a is given by the mean stress at        Since spherical symmetry is postulated from the
the bubble position, calculated by taking into account          stress equilibrium equation:
the global configuration of the large cell (i.e. central
pore t shell + bubbles). The value of Ois one of the               do,
                                                                R ‘-&.j.= 2(q           - 0.r) >
system’s unknowns.
                                                                 One obtains the tangential stress component as:
-c&)    = R; = Rb - 27/o ; -a,(@) = &, = --iii.      (39)
Since the problem is completely formulated, having               ut=ur        1-t            t&D.                           (43)
assigned a value to the external variable uo, the stress                  (              )
field and the permanent deformations which are                   The first step of the analysis is to express the micro-
simultaneously generated in the large cell and in the            scopic swelling rate which represents the mean strain
set of subcells can be calculated. Depending on the              rate of the large shell; we have in fact, by definition
sign of the quantities p’s and on their mutual inequal-
ity relationships, a variety of cases is given where the                                                                    (44)
local strain rate results from the simultaneous occur-
rence of diverse types of deformations (bubble swelling          Calculating the equivalent stress in eq. (40) by means
or shrinkage, intergranular swelling, hot pressing or            of eqs. (41) and (42) enables eq. (44) to be obtained
sintering).                                                      in terms of the problem variables:
                                                                 i=Ala        +pb -2+l”             ,
6.2.2. Mathematic model
    Basis of the analytical treatment is the calcula-            with
tion of the stress field in a hollow sphere, subjected
                                                                 A = (3/2n) CE~~“@~~”
                                                                                   - a”“) K exp(-MjR                7’) .
to external (PO) and internal (pi) load. This is a clas-
sical problem in the theory of elasticity [3 11. In the          The hydrostatic stress on the microcell is given by:
case considered, the yielding of the matrix has to be
                                                                 u@) = 3(2uP) + UPQ
accounted for, and the physical relationship between
strain and stress becomes more complicated. Assum-
                                                                         a-w l/n tup
ing that the deformation occurs according to the
mechanisms discussed in section 6.2 it can be written:
                                                                    =
                                                                         ccl/n - 1                  (l-1 )
                                                                                                        n   ’               (45)

& = $14 - itI = 21&l = Kuf exp(-M/H)           ,                 where
                                                     (40)

where e, and ue are the effective strain and stress,             cc= (W3            *
respectively. The parameters K, n and AH are sup                 The only term unknown in eqs. (44) and (45), is 0,
78                                 C. Ronchi /Fission gas swellingin MX-type nuclear fuels

which is determined by the stress field in the embrac-                With the hypothesis of constant i, eqs. (46) and
ing large cell centered on the pore. The calculation of           (47) are reduced to an easily integrable case [32]. The
this stress field represents the second step of the proce-        stress is calculated as the sum of two components.
dure. The large pore cell is composed of incompres-               The first one is a stress field expressed again by eqs.
sible material and bubbles. The volume strain rate of             (41) and (43) with the boundary conditions given by
this cell (mean strain rate) will therefore be given by           eq. (38). The second one is a constant hydrostatic
the growth (or shrinkage) of the bubbles. The stress-             stress field generated by the gas overpressure in the
strain equations in the large cell may be written as             bubbles; its mean value is given by uh, calculated
[32] :                                                            from eq. (45). This hydrostatic component is called
                                                                  swelling pressure and measures the force at which the
                                                                  bubble growth occurs. It is worthwhile remarking that
                                                                  this second stress component only affects the volume
                                                                 rate of the macroshell (microscopic density) without
ir=gqur-u)+d,                                         (46)       producing shears in the cell; in particular, it does not
                                                                 affect the volume ratio between the shell and the cen-
where o”= $(2or + or) and ee is given by eq. (40).
                                                                 tral pore (macroscopic density). On the other hand,
   These equations, the equilibrium equation eq. (42)
                                                                 the first component is purely deviatoric and does not
and the strain compatibility condition:
                                                                 cause variations of the microscopic density, however,
e,te,=l?g,
                 ‘t                                              this component is responsible for the shears occurring
                                                                 with the volume defined by the shell and its central
are in principle sufficient to determine the variables           pore, which formally represent the macroscopic
er, et, ut , ur, if the boundary conditions are fixed.           density variations.
These are given by eq. (38). The system formed by                    Substituting the analytical expressions for the stress
eqs. (42), (46) and (47) can only be integrated with             tensor into eq. (46) enables the strain rates to be cal-
numerical methods, because of the term e which, in               culated. Since the resulting formulae are quite exten-
the general case, is non-linear in u. However, with a            sive, but can be obtained in a straightforward manner,
further assumption the calculation procedure can be              the strain rates will only be indicated with their func-
substantially simplified. The term e is spatially depen-         tional dependence.
dent through the stress u, the mean stress in the large              Finally an expression for the rate equations (2a)
cell, which is given by:                                         can be obtained. The extension of the model to the
                                                                 case of A4bubble classes of different sizes is immedi-
a= $(2ut + a,) = u,(l - l/n) + D/n .                  (48)       ate since the pressure of the gas in the various classes
In the case of a linear creep rule (n = l), i? is constant       is individually calculated. The equations therefore
through the cell radius and therefore also e is spatially        assume the simple form:
independent. This property leads to significant sim-
plifications in the calculation, so that it would be
desirable to reduce the general case to the same con-
dition. To achieve that, it can be assumed that all the
bubble microcells are subjected to a constant restraint,         where the microcell size p is only defined by the total
equal to that exerted in the center of gravity of the            concentration of bubbles N = ZyNk. The microscopic
large cell, that is expressed as:                                swelling rate is given by:
a= u((R)) ,
with                                                                                                                 (51)

(R)=;b       s            ,                          (49)
         (            1                                          i.e., by the average mean strain rate of the bubbles.
where m = a/b.                                                   The total density decrease of the macrocell (local
                                    C. Ronchi /Fission gas swelling in MX-type nuclear fiels                                       19


swelling rate) is eventually   expressed as:                       meter F is introduced

X = 36,(b) .                                                       F=@o      -&/PO     3
                                                        (52)
                                                                   where /J and p. are swelling calculated with the
Eqs. (50)-(52) solve the problem proposed at the                   dynamic model and with the equilibrium model,
beginning of the paragraph, enabling system (2) to be              respectively. Under steady state conditions, F is
definitively integrated. The new variable uo, represen-            obviously always positive, because in the dynamic
ting the local mean value of the geometrical stress                model the bubble rate is activated by the deviation
field in the system defined by the fuel pellet and its             from the pressure equilibrium condition and
cladding, can only be treated as an external variable.             becomes effectively zero when this is attained. There-
In practice, the stress field calculated in this model             fore F will be called “constriction factor” here and
represent the variation on a microscopic scale of the              its value represent a measure of the mismatch
geometrical stress field around the different types of             between the effects of the fission gas precipitation
cavities, and the strain rates obtained replace the                and the yielding of the surrounding material.
volumetric terms in the currently used pellet creep                    Fig. 13 shows a plot of F as a function of irradia-
equations. That certainly introduces an amelioration               tion time for various temperatures. Owing to its
of the mathematical description and an improvement                 definition, F is zero at t = 0 and assumes positive
 in the form in the analysis of the mechanical behaviour           values for t > 0 and tends to zero for t + 00.There-
of the pin. However, coupling the integration of the               fore, F has to pass through a maximum, whose posi-
swelling rate equations with a realistic calculation of            tion and height depends principally on the mechan-
the geometrical stress in the fuel can only be made with           ical strength of the matrix. Looking at the numerical
further simplifying hypotheses and this still repre-               results plotted in fig. 13, one can see that there is a
sents one of the major operational problems in the                 range of temperatures where the maximum of F is
fuel modeling analysis.                                            not attained within technological time intervals and
                                                                   F increases in value and slope with burn-up. By plot-
                                                                   ting for the same cases, /J versus time, or burn-up, in
6.3. Results
                                                                   a logarithmic graph, (fig. 14) one recognizes that at
                                                                   low temperatures the slopes of the curves are near to
    A discussion of the results of the swelling calcula-            1 and they increase with temperature up to a limit
tions according to the model presented above goes                  value of 1S, corresponding to the known relation-
beyond the proposed limits of this paper. In fact a                ship between microscopic swelling and gas precip-
significant calculation of the local swelling rate can
only be made in connection with a suitable evalua-
tion of the hydrostatic stress field u. , which is
determined by the specific pin design parameters.
In this section only the salient differences are exam-
ined, which result from the assumption of the new
hypotheses of non-equilibrium     bubble growth
(dynamical model). To this purpose, eqs. (SO)-(52)
have been integrated independently      of equations (2),
according to very simplified schemes (pre-fixed tem-
perature and external stress, constant precipitation
rates and bubble concentrations).    To discuss the
results, the parameter 1 (microscopic swelling) has
been chosen, because it is much less affected than
                                                                                               IO‘ 10' IO8 10’
local swelling X by the value of uo. To represent the
                                                                                                      TIME1s)
deviations from the results obtained with conven-
                                                                   Fig. 13. Bubble constriction factor at different temperatures
tional models (bubble equilibrium models), a para-                 as a function of the irradiation time.
80                                       C. Ronchi /Fission gas swellingin MX-type nuclear fuels




                                                                                                                    lo’8   ‘O’O 102*


                       I                        I

                            VI5    lo6    10’
                                  TIME   Is)
Fig. 14. Microscopic swelling calculated as a function of irradia-
tion time. Release and containment stress were not included
in the calculation.


itated b, under equilibrium       conditions:
p’b312.
This relation is obviously only approached in the
bubble growth stage in which the influence of the                                              BUBBLE   CONCENTRATION      i m-j)

external stress on the gas pressure is negligible, i.e., for           Fig. 15. Effect of the fuel self-restraint at different temper-
intermediate sizes. In principle, the attainment of this               atures as a function of the assumed bubble concentration.
growth regime corresponds to a nearly complete relief
 of the gas overpressure due to the sufficiently rapid                 processes between bubbles lead to a significant
relaxation of the matrix. These results show that if the               increase of swelling, only if the fuel is plastic enough
temperature of the fuel is sufficiently high, the swel-                to relieve within a sufficiently short time the (relativ-
ling predictions of the more simplified equilibrium                    ely low) overpressure resulting from the coalescence
models are negligibly different from those obtained                    of two or more individuals. Finally, the dependence
with the more comprehensive dynamic model, so                          of the bubble growth on temperature has to be con-
that the use of the former there is fully justified. On                sidered. To this purpose, the calculations of swelling
the other hand, at low temperature, the new results                    have been carried out including the evolution of the
have great significance in predicting the swelling                     bubble spatial concentration with temperature, and
behaviour. There, swelling assumes a nearly constant                   have been restricted to a range where gas release could
rate, depending principally on the atomic size of the                  be reasonably disregarded. The curves of microscopic
gas and on the mechanical strength of the matrix.                      swelling as a function of temperature are shown in
Furthermore, fission gas bubbles approach the typical                  fig. 16 for different burn-ups. These curves can be
property of the solid precipitates, namely that of                     approximately fitted by two straight-line branches,
occupying a volume independent of the spatial dis-                     that at higher temperature being much steeper. The
persion. This peculiarity is illustrated in fig. 15, where             two branches define at their intersection point a tem-
the constriction factor and swelling are plotted as a                  perature, which characterizes the transition between
function of the bubble concentration N; at low tem-                    the low temperature and high temperature swelling
peratures, decreasing N (i.e., increasing the average                  regimes.
bubble volume) produces an increase of F that keeps                        These predictions agree with the experimental ob-
swelling nearly constant. The effect gradually dis-                    servations and measurements of microscopic swelling.
appears at higher temperatures, where F becomes                        The experimental curves of p versus temperature dis-
lower in any case and an increasing dependence of                      play also an abrupt change in slope at a certain tem-
swelling on bubble concentration is calculated. In                     perature, called critical temperature for microscopic
other words, it can be argued that the coalescence                     swelling (T,) [8]. The properties of this transition
                                    C. Ronchi ! Fission gas swelling in MAT-typenuclear fuels                             81


                                                                    of pressure of the fission gas precipitated and of the
                                                                    external restraint. The fission gas kinetics equations
                                                                    (2) enable the gas flux to the grain boundaries to be
                                                                    calculated as a function of irradiation time. This
                                                                    flux is in part collected by sintering porosity (of
                                                                    concentration A$) and in part by large grain bound-
                                                                    ary hubbies, whose concentration Np is calculated
                                                                    with a procedure analogous, to that described in
                                                                    section 3. By knowing the concentrations pP and Nn,
                                                                    the calculation of local swelling rate can be performed
                                                                    according to the model described above. However,
                                                                    pores and bubbles growing on the grain boundaries
                                                                    have a distinctive property which has to be accounted
                                                                    for; this is the high probability that contact points are
                                                                    established between neighbouring individuals. If the
                                                                    density of,contact points between pores is large
                  1WO      1200     1400       1600
                                           I   [Kl
                                                                    enough, it can be intuitively deduced that chains of
Fig. 16. Microscopic swelling calculated as a function of tem-
                                                                    interlinked pores are formed, and that, in the limiting
perature at different burn-ups. On behalf of simplicity release     case, the chains may be as long as the macroscopic
and cladding containment calculation have been omitted. These       linear dimensions of the sample. The possible exist-
would have led to a significant decrease of swelling at temper-     ence of these chains leads to the definition of a new
atures far above the knee points (critical temperatures).
                                                                    class of pores, called open porosity, whose develop-
                                                                    ment must be treated separately. In fact, the fission
which have been studied in detail [8,33] can now be                 gas pressure in the open pores falls very quickly to
understood in the light of a physical explanation.                  the level of the plenum pressure, because the inter-
According to the model proposed, the “knee-point”                   linking channels provide a direct release path of the
T, is due to the activation of two independent pro-                 gas. The calculation of the open pore fraction within
cesses: the mechanical yielding of the matrix and the               a given fuel local structure is therefore necessary to
decrease with temperature of the average bubble con-                analyze the mutually dependent phenomena of inter-
centration, leading to an increase of the average                   granular swelling and gas release.
bubble size and a progressive loss of the capillarity                    To solve this problem, two approaches are in
restraints (27/r’s terms), which constitute a primary               principle possible. With the first one, based on phys-
containment factor at high temperature for the fission              ical considerations, one tries to explain pore inter-
gas.                                                                linkage as an equilibrium configuration attained
    Following the numerical calculations, the change                 during growth, under the action of inner pressure
of the swelling slope through T, occurs without dis-                and grain boundary and surface energies. The models
continuity, but the change is accomplished in a so                  developed on this basis [34] have brought few practi-
small temperature interval (a few tens of degrees), that            cal advantages, because the geometry assumed is
the introduction of the definition of a knee is in prac-            rather complicated and finally of little significance
tice perfectly justified as well as very useful to char-            in concrete applications. However, these models have
acterize the swelling performance of a given fuel.                  put forward physical arguments of the structural stab-
                                                                    ility of the interlinkage configurations, so that, based
                                                                    on these proofs, a second more practical approach
7. The properties of the intergranular pores during                 can be assumed, dealing with the usually available
irradiation                                                         parameters, characterizing the fuel structure.
                                                                         A very general way of defining the concept of
   In the preceding paragraph, the growth of the                     interlinkage between pores is that based on the statis-
coarse porosity in the fuel is calculated on the basis              tical definition of percolation probability through an
82                                      C. Ronchi / Fission gas swellingin MX-type nuclear fuels

ordered spatial distribution of nodes. Assuming a lat-                 Ns is the coordination number of an arrangement of
tice of sites (pores) connected with bonds (channels                   spheres of radius rp around spheres of radius rp. Ng
or contact points) randomly distributed, with an                       can be approximately estimated from lattice geometry
average concentration P = (number of bonds)/(num-                      as:
ber of sites), a total interlinkage is thought to occur
                                                                       Ns -$n{l       -41       - [s/(1 +s)]*}-’           ,
when a finite probability is calculated for an infinite
chain of bonds starting from a given site. The analysis
                                                                       s = rg/rp .                                                       (57)
of the interlinking probability can be carried out with-
out regard to how the bonds are created between the                    In eq. (56), np and ng can be expressed as a function
pores, but simply assuming that they exist and are                     of the fractional porosity F and the parameter s, ob-
stable. The model, previously developed for LWR                        taining:
fuels [35], has now been extended to FBR advanced
fuels.                                                                 P= +N, [l + (F-l              - 1)(2Nn/rr)


7.1. Percolation model for a sintered medium                                X{l -Jl        - [s/(1 ts)]*}/sY,                            (58)
                                                                       which enables P to be calculated from the two ex-
   Based on the macroscopic parameter P, it can be                     perimental parameters F and g and from the geome-
shown that the probability that a site has n bonds is
                                                                       trical factor Nn. A first crude assumption would be
given by [36] :
                                                                       to consider the condition P> 1.56 as a limit for the
                                                                       intergranular release through percolation. Actually
pn = ep 2     p/k!    ,                                    (53)        P is a function of erratic structural parameters,
        k=l
                                                                       depending on the local fuel condition and hetero-
                                                                       geneity. Therefore, a statistical distribution around
with IZLpn = P and the number of chains having N
                                                                       an average value of P has to be assumed. In this
bonds is given by:
                                                                       case, one obtains the pore interlinkage fraction
                                                                                                0
                                                           (54)        F,    = (271u)- V2                       exp[-(x   - P)*/20*] dx ,(59)
                                                                                              &/-
                                                                                              P,=1.5...

The percolation      condition   is thus:                              where u has to be calculated from the experimental
?i(N,P)+e>O            for   N-t-,                         (55)        histograms of rp, rg and F:
                                                                                 8P
which is verified for every

P> 1.569 . .. .
                                                                       ’ =   I   6    “P
                                                                                            tap,
                                                                                               &-,        ‘g
                                                                                                               )*2&y,                    (60)

                                                                       where the measures of rp and rg are supposed to be
i.e., whenever each site has, on average, 1.6 disposable               correlated and that of F to be orthogonal.
bonds. In our case, the problem is that of finding a
practical way to evaluate P for pores in a sintered                    7.2. Release through percolation and intergranular
medium. Assuming that the pores are distributed as                     swelling
spheres of radius rp among grains of radius rs, the
average number of bonds per core can be calculated                         The knowledge of the open pore fraction enables
as:                                                                    a calculation of the gas release rate to be made with
                                                                       more precision. The introduction of the concept of
P= :N, [rrpl(np + ngNp/Ng)l,                                (56)       open chains and partial retention of gas in the grain-
where np and ng are the concentrations of pores and                    boundary porosity is also extremely important to
grains, respectively. Np is the coordination number                    calculate swelling and hot pressing in temperature
for a compact arrangement of pores (Nn ‘v 6) and                       ranges where a significant flow of gas is arriving at
                                 C. Ronchi f Fission gas swelling in KY-type nuclear jkels                                 83


the grain boundaries, but pores are not mobile
enough to act as gas carriers over long distances.
This is in practice the situation encountered in
MX-type fuels for a large number of cases.
    The salutation of gas release and intergr~ular
swelling (or hot pressing) is made in the model fol-
lowing a simple scheme:
      (i) An initial distribution of pore and grain sizes
is taken as input. This distribution has to be deter-
mined by an accurate ceramographic analysis of the
starting material. In cases where grain growth occurs
during irradiation, the mode and the extent of this
process is accounted for.
     (ii) After calculating the interlinkage factor, a
fraction F, of the porosity is considered open and
the gas arriving there released. In the remnant
(1 -F,) of the pores, the gas contributes to increase
the inner pressure so that they are forced to grow.
    (iii) The pore volume increase under the gas
thrust is calculated according to the model described            Fig. 17. Percolation factor calculated as a function of grain
in the preceding paragraph. The evolving porosity                size and porosity. The dashed area indicates the domain where
produces a change in F, , so that new situations are             a fabricated pellet or a restructured fuel may preserve suff&
                                                                 cient release patterns without needing s~i~cant swelling of
created, by which closed pores become open releasing             the intergranular pores.
their gas content. The pressure collapse in these pores
further activates hot pressing.
    The first question arising from the above considera-         least recommendable are structures which present a
tions, regards the optimum local distribution of the             high percentage of pores located within the grains.
fab~cation porosity in order to obtain the highest               This porosity does not contribute to fo~ation of
percolation factor. A study of the function (59) as a            open chains and from itself it represents a gas reser-
function of the fabrication parameters, shows that               voir of negligible capacity: small amounts of gas can
for a given porosity interlinkage increase with the              in fact fill large pores up to pressures at which hot
ratios (grain to pore size). However, the value of s             pressing is made effectively impossible.
required to obtain a high interlinkage ratio increases
steeply with decreasing porosity (fig. 17), so that in
practice only with fabrication porosities above 10%              Acknowledgement
there is a chance of obtaining sintered pellets with
more than 50% open pores. On the other hand, an                     I am very indebted to Jacques van de Laar for his
indefinite increase of the grain size is only a hypothe-         valuable help in performing computer calculations.
tical way of increasing interlinkage, because with
increase of grain size more and more pores are in fact
left within the grains. Moreover, large grains are often         References
subdivided into subgrains on the boundaries of which
preferential trapping of gas is observed to occur as on           [l] C. Ronchi and Hj. Matzke, J. Nucl. Mater. 45 (1972/73)
grain boundaries.
    In practice, the largest suitable value of s can only         [ 21 E CaJigara, to be published.
                                                                  [3] E. Gruber, J. Appl. Phys. 38 (1967) 243.
be estimated from an accurate ceramographic analysis
                                                                  [4] M.R. Hayns and M.H. Wood, J. Nucl. Mater. 67 (1977)
of the fuels in connection with the results obtainable                 1.55.
with the fabrication methods adopted. In any case,                [5] C. Baker, J. Nucl. Mater. 66 (1977) 283.
a4                                   C. Ronchi /Fission gos swellingin KY-type nuclear fuels


       J.A. Turnbull, J. Nucl. Mater. 38 (1971) 203.               [ 221. R. Bullough and R.C. Perrin, in: Radiation Damage In
  [ 61 B.B. Mandelbrot Fractals, Form, Chance and Dimension               Reactor Materials, Vol. II (IAEA, Vienna, 1969) p. 233.
       (Freeman, San Francisco, 1977).                             [ 231 J.L. Straalshund and G.L. Guthrie, Nucl. Technol. 16
  [7] F.A. Nichols, J. Nucl. Mater. 21 (1969) 19.                         (1972) 36.
  [S] C. Ronchi, I. Ray, J. van de Laar and H. Thiele, Report      [ 241 R. Bullough and R.C. Perrin, Voids Formed by Irradia-
       EUR 5907 (1978).                                                   tion in Reactor Materials (AERE, Harwell, 1973) p. 79.
  [ 91 P.L. Studt, J.F. Shackelford and R.M. Fulrath, J. Appl.     [25] C. Herring, J. Appl. Phys. 21 (1950) 437.
       Phys. 41(1970) 2777.                                        [ 261 M.S. Seltzer, J.S. Perrin, A.H. Clauer and B.A. Wilcox,
[lo] R.M. Barrer and D.E.W. Vaugham, Trans. Faraday Sot.                  Reactor Technol. 14 (1971) 99.
       63 (1967) 2275.                                             [27] N.M. Killey, J. Nucl. Mater. 41 (1971) 178.
[ 111 Hj. Matzke and F.S. Springer, Radiation Effects 2            [ 281 R.V. Hesketh, J. Nucl. Mater. 29 (1%9) 217.
       (1970) 11.                                                  [ 291 H.G. Bogensberger and C. Ronchi, Nucl. Technol. 29
[12] D.E. Rimmer and A.H. Cottrel, Phil. Mag. 2 (1957)                    (1976) 73.
       1345.                                                       [ 301 A.J. Markworth and W. Oldfield, Mater. Sci. Eng. 10
[ 131 G.W. Johnson and R. Shuttleworth, Phil. Mag. 4 (1959)               (1972) 159.
       957.                                                        [ 311 S. Timoshenko and J.N. Goodier, Theory of Elasticity
[ 141 C. Ronchi, J. Appl. Phys. 44 (1973) 3575.                           (McGraw-Hill, New York, 1951) p. 343.
[ 151 M.O. Marlowe, Report GEAP 12428 (1973).                      [ 321 W. Prager and P.G. Hodge, TheorIe Ideal Plastischer
[ 161 C. Baker, Report CEGB RD/B/N4194 (1977).                            K&per (Springer, Berlin, 1954).
[ 171 Hj. Matzke and C. Ronchi, in: Physical Metallurgy of         [33] H. Blank, J. Nucl. Mater. 58 (1975) 123.
       Reactor Fuel Elements (Berkeley, 1973) 259.                 [ 341 M.O. Tucker and J.A. Tumbull, Proc. Roy. Sot. A 343
[ 181 C. Ronchi, unpublished results.                                     (1975) 299.
[ 191 S. Chandrasekhar, Rev. Mod. Phys. 15 (1943) 1.               [ 351 C. Ronchi , LWR Safety Program ANL 75-72 (1975)
[ 201 C. Sari, Report EUR 5812 (1978).                                    p. 94.
[21] L. Landau and F. Lifchitz, Physique Statistique (MIR,         [36] K. Maschke, Phys. Stat. Sol. B60 (1973) 563.
       Moscou, 1967) p. 544.
