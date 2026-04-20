# Phase field modeling of void nucleation and growth in irradiated metals

---

Modelling and Simulation in Materials Science and Engineering




                                                                                                 Related content
                                                                                                     - Void nucleation and growth in irradiated
Phase field modeling of void nucleation and                                                            polycrystalline metals: a phase-field model
                                                                                                       Paul C Millett, Srujan Rokkam, Anter El-
growth in irradiated metals                                                                            Azab et al.

                                                                                                     - The phase field technique for modeling
                                                                                                       multiphase materials
To cite this article: Srujan Rokkam et al 2009 Modelling Simul. Mater. Sci. Eng. 17 064002             I Singer-Loginova and H M Singer

                                                                                                     - Phase field modeling of the effect of
                                                                                                       porosity on grain growth kinetics in
                                                                                                       polycrystalline ceramics
                                                                                                       K Ahmed, C A Yablinsky, A Schulte et al.
View the article online for updates and enhancements.


                                                                                                 Recent citations
                                                                                                     - Radiation induced nanovoid shrinkage in
                                                                                                       Cu at room temperature: An in situ study
                                                                                                       C. Fan et al

                                                                                                     - Karim Ahmed and Anter El-Azab

                                                                                                     - Point defects patterning in irradiated -
                                                                                                       zirconium: numerical study in the
                                                                                                       framework of the rate theory
                                                                                                       Dmitrii O. Kharchenko et al




                             This content was downloaded from IP address 159.226.142.11 on 14/10/2019 at 03:16
IOP PUBLISHING                               MODELLING AND SIMULATION IN MATERIALS SCIENCE AND ENGINEERING
Modelling Simul. Mater. Sci. Eng. 17 (2009) 064002 (18pp)                    doi:10.1088/0965-0393/17/6/064002




Phase field modeling of void nucleation and growth in
irradiated metals
                   Srujan Rokkam1 , Anter El-Azab2,4 , Paul Millett3 and Dieter Wolf3
                   1 Department of Mechanical Engineering, Florida State University, Tallahassee, FL 32310, USA
                   2 Department of Scientific Computing, Florida State University, Tallahassee, FL 32310, USA
                   3 Materials Science Department, Idaho National Laboratory, Idaho Falls, ID 83415, USA


                   E-mail: aelazab@fsu.edu

                   Received 29 March 2009, in final form 14 July 2009
                   Published 24 August 2009
                   Online at stacks.iop.org/MSMSE/17/064002

                   Abstract
                   Motivated by the need to develop a spatially resolved theory of irradiation-
                   induced microstructure evolution in metals, we present a phase field model for
                   void formation in metals with vacancy concentrations exceeding the thermal
                   equilibrium values. This model, which is phenomenological in nature, is cast in
                   the form of coupled Cahn–Hilliard and Allen–Cahn type equations governing
                   the dynamics of the vacancy concentration field and the void microstructure
                   in the matrix, respectively. The model allows for a unified treatment of
                   void nucleation and growth under the condition of random generation of
                   vacancies, which is similar to vacancy generation by collision cascade in
                   irradiated materials. The basic features of the model are illustrated using
                   two-dimensional solutions for the cases of void growth and shrinkage in
                   supersaturated and undersaturated vacancy fields, void–void interactions, as
                   well as the spontaneous nucleation and growth of a large population of voids.




1. Introduction

This work is concerned with the problem of void formation and evolution in metals
under vacancy supersaturation. This problem is related to the more complex situation of
irradiation-induced microstructure change in structural materials used in nuclear reactors. This
microstructure change is driven by neutron irradiation, and it leads to dimensional instabilities
in the form of volumetric swelling, creep instabilities and hardening and loss of ductility over
prolonged periods of in-reactor irradiation [1–3].
     Microstructure change under irradiation is a complex phenomenon that spans a wide range
of length and time scales. Primitive to all the pertinent processes is the radiation damage event

4   Author to whom any correspondence should be addressed.

0965-0393/09/064002+18$30.00       © 2009 IOP Publishing Ltd    Printed in the UK                               1
Modelling Simul. Mater. Sci. Eng. 17 (2009) 064002                                     S Rokkam et al

in which an energetic particle, e.g. a neutron, knocks an atom from its lattice giving it a high
amount of kinetic energy. This primary knock-on atom (or PKA), in turn, displaces many
other lattice atoms through a cascade of atomic collisions, resulting in roughly equal numbers
of vacant sites and interstitials. During the lifetime of a cascade (a few picoseconds) many
vacancies and interstitials annihilate each other by recombination, leaving behind a smaller
ensemble of point defects. The atomic displacement cascades, which occur in an uncorrelated
fashion in the irradiated material, lead to an increase in the concentration of vacancies and
interstitials several fold over their thermal equilibrium values. The diffusion and interaction of
these point defects with each other and with pre-existing microstructure lead to microstructural
evolution, e.g. void and dislocation loops formation and phase changes in irradiated metals.
     Void formation results from the clustering of vacancies in the irradiated material. This
process is facilitated by the tendency of dislocations to absorb interstitials at faster rates than
vacancies, which is known as dislocation bias, as well as by the stabilization of vacancy cluster
embryos by gas atoms available in the irradiated metals through nuclear transmutations. The
high rate of absorption of interstitials at dislocations effectively removes more interstitials (than
vacancies) from the system and thus makes more vacancies available to cluster together to form
void embryos. This process is further assisted by the tendency of interstitials themselves to
cluster and form dislocation loops. The presence of gas atoms enhances the void nucleation
process. The continued absorption of gas atoms by voids leads to the formation of gas bubbles
(gas-filled cavities). In the absence of gas atoms, however, supersaturation of vacancies alone
leads to the formation of voids, much like the classical example of void formation in quenched
metals. The formation of voids and gas bubbles causes volumetric swelling of the material, and
contributes to density decrease and dimensional instability of the structural material. These
microstructural features also have a significant impact on the yielding behavior of structural
metals.
     In the traditional approach to modeling void swelling in irradiated metals, void nucleation
and growth are treated as two separate processes, which are modeled by the classical nucleation
theory and the reaction rate theory, respectively. The classical nucleation theory is applied to
obtain the nucleation rate of voids [4, 5]. Depending on the specific formulation of the theory,
it can also give the distribution function for the nucleating void population as well as the
steady state nucleation current, under the assumption that embryos grow in a supersaturation
of vacancies. The reaction rate theory, on the other hand, estimates the average density of
point defects in irradiated materials [6, 7]. The theory accounts for processes such as mutual
recombination and defect loss to microstructural sinks. The latter is represented in terms of
homogenized sink strength terms. The rate of absorption of point defects at microstructural
sinks yields an evolution law for the corresponding microstructure features. For example, the
void growth rate (in turn, the swelling rate) is determined by the net difference of vacancy
and interstitial absorption at the void surface [8, 9]. Both nucleation theory and rate theory
characterize the relevant processes as point-kinetic processes with the assumption of uniformity
in space. However, the microstructural evolution of irradiated materials is sensitive to the
details of the microstructure itself, i.e. it depends on the spatial correlation between various
microstructural features and associated processes. The effects of spatial correlations are
evident, for example, through the observations of void ordering and void lattice formation
in irradiated metals [10–12]. Furthermore, when stress or temperature gradients are present
in the system, defect clusters such as voids and gas bubbles can migrate as a result of these
gradients [1, 2, 13, 14]. As such, there is a need for spatially resolved models of microstructure
evolution in irradiated materials to better understand the process of microstructure evolution.
     In this communication, we investigate the problem of void evolution in metals with a
supersaturation of vacancies within the framework of the phase field modeling approach. This

2
Modelling Simul. Mater. Sci. Eng. 17 (2009) 064002                                  S Rokkam et al

approach has been extensively used to model microstructure evolution in many situations,
including phase transition, crystal growth and solidification, to name some [15, 16]. Typical
to this approach is the diffuse description of interfaces, the boundaries between distinct
phases, which evolve over time taking into account the correlated interactions between the
dynamical processes in the material under consideration. The diffuse-interface or phase field
model presented here characterizes the void microstructure evolution in the case of one-
component systems (pure metals) under the condition of dynamic vacancy supersaturation
due to irradiation. In particular, the process of void formation and growth is viewed as a
separation of the void phase from a supersaturated solution of vacancies and regular lattice
atoms. The term supersaturation refers here to the increase in vacancy concentration in the
matrix above its thermal equilibrium value. The effect of interstitials on the void nucleation and
growth dynamics is not considered in this study. Rather, as a simplifying modeling assumption,
only vacancies are considered at this point in order to establish the phase field methodology
for modeling void nucleation and growth in situations involving vacancy supersaturation
conditions, irradiation being one of them.
     Following this introduction, we present the phase field model in section 2 and briefly
outline its numerical solution in section 3. Numerical tests validating the phase field model are
presented in section 4, along with results for simulation of void nucleation and growth under
the condition of stochastic vacancy production. Analysis and discussion of these results in
light of classical nucleation and growth models are also included at that point. A summary of
this work and some preliminary conclusions are presented in section 5.


2. Phase field model

2.1. Free energy of the system

In this study, we consider a single crystal metal with two phases, a matrix phase with point
defects, namely vacancies, and a void phase. This material system is thus a heterogeneous
system, with spatially varying vacancy concentration in the matrix and interface between the
matrix and void phases. The voids themselves result from the condensation of vacancies from
a vacancy-supersaturated solution of vacancies and lattice atoms. The vacancy distribution
in the crystalline solid is described by (fractional) vacancy concentration field, denoted here
by cv (x, t), while the long range order of the system is represented using a non-conserved
phase field variable or order parameter η(x, t). Here, the term long range order refers to the
fact that the system is a heterogeneous one with different phases occupying different regions
in space. As such, the non-conserved phase field variable or order parameter η(x, t) takes
on a constant value within the individual phases and varies smoothly across interfaces. In
particular, the order parameter η(x, t) varies continuously from η = 0 in the matrix phase to
η = 1 in the void phase over a narrow diffuse interface between the matrix and void phases.
Both the concentration field cv (x, t) and the phase field η(x, t) are continuous in space and
evolve in time, characterizing the evolution of the vacancy field and the void microstructure,
respectively.
     The phase field approach is based on expressing the total free energy functional of the
heterogeneous material in terms of the free energy of its constituent phases and interfaces.
This free energy functional is then used to derive kinetic equations for the conserved and non-
conserved phase field variables of the system. Consistent with the Cahn–Hilliard definition
of free energy for a non-uniform system [17], we describe the free energy functional of a
crystalline solid consisting of a matrix phase with vacancies plus a void phase, in terms of the

                                                                                                3
Modelling Simul. Mater. Sci. Eng. 17 (2009) 064002                                    S Rokkam et al

vacancy concentration field cv (x, t) and the order parameters η(x, t) as follows:
              
[cv , η] = N   [h(η)ψ m (cv ) + w(cv , η) + κv |∇cv |2 + κη |∇η|2 + ψ el (cv , η)] d.         (1)
                  
In this expression, the prefactor N is the number of lattice sites per unit volume of the material
and thus all terms under the (volume) integral sign represent free energy per lattice site. Of
these, the first two terms under the integral sign correspond to the system bulk energy. The
interfacial energy contributions are accounted for by the two gradient terms. The last term in
equation (1) accounts for elastic effects in the system, namely, the interaction of point defects
with the stress field. The defect free-energy term ψ m (cv ) is derived in terms of the enthalpic
and entropic contributions of the vacancies, and it is written in the form
                 ψ m (cv ) = Evf cv + kB T [cv ln(cv ) + (1 − cv ) ln(1 − cv )],                (2)
with Evf being the vacancy formation energy, kB the Boltzmann constant and T the absolute
temperature. The shape function h(η) has the expression: h(η) = (η − 1)2 (η + 1)2 . This
function varies continuously from h(η) = 1 at η = 0 in the matrix phase, to h(η) = 0 at η = 1
in the void phase. The Landau-type term w(cv , η), which is responsible for bistability in the
system, is expressed in the form
                 w(cv , η) = −A(cv − cvo )2 η(η + 2)(η − 1)2 + B(cv − 1)2 η2 ,                  (3)
where cvo is the thermal equilibrium vacancy concentration in the solid, given by the expression
cvo ≈ exp(−Evf /kB T ), and A and B are constant prefactors. The gradient energy coefficients
κv and κη characterize the energy penalties corresponding to the inhomogeneities in vacancy
concentration and phase field, respectively. The corresponding energy terms are reminiscent
of the gradient terms in the spinodal decomposition theory of Cahn and Hilliard [17, 18] and
the theory of antiphase boundary of Allen and Cahn [19]. As such, the gradient energy terms
in equation (1) account for the field inhomogeneity across the diffuse void–matrix interface.
     The first two terms in the integral form of the free energy functional expression (1) represent
the free-energy density of the homogeneous system. In the absence of stress, these two energy
terms define two stable wells: one at cv = cvo and η = 0 corresponding to the matrix phase
with vacancy concentration equal to the thermal concentration, and another at cv = 1 and
η = 1 corresponding to the void phase. The former well arises due to the fact that the local
energy density ψ m (cv ) has a minimum at cv = cvo . The Landau term w(cv , η) is chosen so as
to retain the energy well defined by ψ m (cv ) and to contribute a stable well at cv = 1 and η = 1,
corresponding to a pure vacancy phase (voids), in addition. The shape function h(η) ensures
that the contribution of the energy density ψ m (cv ) is nullified when cv = 1 and η = 1, in effect
ensuring that the energy density inside the void phase is identically zero. Figure 1 shows a color
contour map of the sum of these two energy terms and the corresponding energy wells. We
note that the scale of the figure does not resolve the thermal concentration value corresponding
to the first energy well because this well is very close to zero on the concentration axis.

2.2. Kinetic equations
Following the standard procedure in the phase field approach, the kinetic equations for the
space and time evolution of the phase field variables cv (x, t) and η(x, t) have been derived:
                  ∂cv                   1 δ
                      (x, t) = ∇ · Mv ∇       + ξ(x, t),                                        (4)
                  ∂t                    N δcv
                  ∂η             δ
                     (x, t) = −L    + ζ (x, t).                                                 (5)
                  ∂t             δη
4
Modelling Simul. Mater. Sci. Eng. 17 (2009) 064002                                                   S Rokkam et al




                 Figure 1. A contour map of the free energy-density, the sum of the first two terms in expression (1),
                 showing two minima at (cv = cvo , η = 0) and (cv = 1, η = 1) corresponding to the matrix phase,
                 with thermal equilibrium vacancy concentration, and the void phase, respectively.



Equation (4) is identified as a form of generalized diffusion equation or modified Cahn–
Hilliard equation [17], with Mv and (1/N )δ/δcv being the mobility and chemical potential
of vacancies, respectively. The functions ξ(x, t) and ζ (x, t) represent the thermal fluctuations
of the concentration field cv (x, t) and the long range order parameter field η(x, t), respectively.
To this end, the above equations do not account for the generation of vacancies or the direct
formation of voids as a result of the cascade process in irradiated materials. Such terms can
be simply added to the right-hand side of equations (4) and (5). In particular, an irradiation
sources term Pv (x, t) can be added to the right-hand side of equation (4) to represent the
production of vacancies due to the cascade process. Other terms can also be added to represent
the absorption of vacancies at homogeneous or non-homogeneous sinks in the matrix. For the
sake of illustrating the capabilities of this model, only a stochastic generation term Pv (x, t)
will be considered, while other processes resulting in annihilation of vacancies are suppressed
and the event of direct formation of voids in high-energy collision cascades are ignored.
     The kinetic equation describing the evolution of the η(x, t) field, that is equation (5), is
similar to the phenomenological Allen–Cahn equation [19], with ∂η/∂t being a generalized
velocity that is induced by the thermodynamic force δF /δη and L being the corresponding
mobility. The void surface velocity vn is given by the rate of motion of the level set
η(x, t) = 0.5. This velocity can be found for any level set η(x(t), t) = c by setting the total
time derivative of η(x(t), t) equal to zero, which yields vn = −(∂η(x, t)/∂t)/|∇η(x, t)|η=0.5 .
     The final form of the kinetic equations can be obtained by first evaluating the
variational derivatives of the free energy functional with respect to cv (x, t) and η(x, t) using
expressions (2)–(3), then substituting the results in equations (4) and (5). After adding the
vacancy source term, the kinetic equations can be rewritten in the form:
                                                                                     
∂cv                            ∂ψ m (cv ) ∂w(cv , η)                   ∂ψ el (cv , η)
     (x, t) = ∇ · Mv ∇ h(η)               +             − 2κv ∇ 2 cv +
 ∂t                                ∂cv          ∂cv                        ∂cv
                 +ξ(x, t) + Pv (x, t),                                                                            (6)
                                                               
∂η                ∂h(η) m ∂w(cv , η)             ∂ψ el (cv , η)
   (x, t) = −LN        ψ +           − 2κη ∇ η +
                                            2
                                                                  + ζ (x, t).                                     (7)
∂t                 ∂η       ∂η                       ∂η
                                                                                                                    5
Modelling Simul. Mater. Sci. Eng. 17 (2009) 064002                                                   S Rokkam et al

The solution of the coupled partial differential equations (6) and (7) using a suitable numerical
scheme gives us the time evolution of the void phase and the vacancy concentration field. In the
sequel, the contribution of the elastic term ψ el (cv , η) in equations (6) and (7) will be ignored
by the assumption that no stress acts on the system.

3. Non-dimensionalization and numerical solution of the kinetic equations
                                                                            
We cast the kinetic equations into a reduced form using a length scale = κη /kB T and time
scale of τ = 2 /Dv (where Dv is the diffusivity of the vacancies). Here we use the approximate
expression Mv = Dv /kB T for the mobility in terms of the diffusivity, which means that the
mobility is isotropic and uniform over the entire domain of the solution. In a more rigorous
treatment, the vacancy mobility must depend on the vacancy concentration. On normalizing
spatial distances by and time by τ , the kinetic equations (6) and (7) reduce to the form:
                  
∂cv
      = ∇ · M̃v ∇ h(η)(Ẽvf + ln cv − ln(1 − cv )) − 2κ̃v ∇˜ 2 cv
         ˜      ˜
 ∂ t˜
                                                                    
                −2Ã(cv − cv )η(η + 2)(η − 1) + 2B̃(cv − 1)η + ξ(x̃, t˜) + Pv (x̃, t˜),
                            o                  2                  2
                                                                                           (8)

                                                                                
∂η                                                                          ˜
     = −L̃ h (η)ψ̃ (cv ) − Ã(cv − cv ) (4η − 6η + 2) + 2B̃(cv − 1) η − 2κ̃η ∇ η + ζ (x̃, t˜).
                  m                 o 2    3                       2           2
∂ t˜
                                                                                         (9)
In the above, t˜ = t/τ is the dimensionless time and ∇˜ = ∇ is the dimensionless gradient
operator. The parameters Ẽvf , Ã and B̃ are obtained by normalizing Evf , A and B, respectively,
with respect to kB T . Likewise, the function ψ̃ m (cv ) denotes the expression obtained by
normalizing ψ m (cv ) with respect to kB T . The mobility of the vacancies and void/matrix
interface in the dimensionless form are now expressed in the forms M̃v = Dv τ / 2 = 1
and L̃ = LN τ (kB T ), respectively. Finally, the dimensionless gradient energy coefficients in
equations (8) and (9) can be identified as κ̃v = κv /κη and κ̃η = 1.
     The kinetic equations (8) and (9) are solved in two dimensions using a central finite
difference scheme with forward Euler marching scheme in time. The discretized form of these
equations is
                         t
cv |n+1
    i,j = cv |i,j +
              n
                            M̃v (ψv |ni+1,j + ψv |ni−1,j + ψv |ni,j +1 + ψv |ni,j −1 − 4ψv |ni,j )
                      ( x)2
                 + t(ξ + Pv )|ni,j ,                                                                          (10)

  i,j = η|i,j −
η|n+1                 t L̃ψη |ni,j .
          n
                                                                                                              (11)
In the above, ψv |ni,j and ψη |ni,j are the values of the quantities in brackets in equations (8)
and (9), respectively, evaluated at grid point (xi , yj ) at nth time step. These quantities are
given in appendix A. In the equation for η, the fluctuation term is dropped for simplicity.
    In the numerical tests presented here, the following values are used for the reduced model
parameters: M̃v = 1, L̃ = 1, κ̃η = 2κ̃v = 1, Ẽvf = 9.09 and Ã = B̃ = 9.09. This choice
corresponds to a temperature of T ≈ 1276 K, Evf = 1 eV and cvo ≈ 1.13 × 10−4 . With the
numerical scheme discussed herein, simulations were performed on a square domain with
periodic boundary conditions under the assumption of constant temperature.
    We remark here that the material parameters listed above do not necessarily represent a
specific metal. Rather, these values were used for the purpose of testing the model itself. In

6
Modelling Simul. Mater. Sci. Eng. 17 (2009) 064002                                                 S Rokkam et al

                      1.2


                        1


                      0.8


                 h    0.6


                      0.4
                                                       η( x,0)
                      0.2                              Sv = 100
                                                       Sv = 500

                        0
                               40       50        60         70     80        90
                                                        x

                 Figure 2. Two line profiles of η(x̃, t˜) through the void center at t˜ = 50 for Sv of 100 and 500.
                 Also displayed is the initial line profile, which is labeled by η(x, 0).

a comprehensive version of this model, the energy and mobility parameters must be chosen
so as to reproduce the correct sharp interface model of the phenomenon of void formation in
metals. This task is left for a future extension of this model. For the purpose of testing the
model here, it suffices here to pick these parameters to check the basic features of dynamical
nucleation and evolution of voids as reproduced by the current phase field model, and without
extensive computational cost.
     In all simulations, the time step t˜ was taken to be 5×10−5 . For the purpose of simulating
the nucleation and growth of voids, the solution domain was divided into 128 × 128 grid points
with x̃ = ỹ = 1. In all other examples, see section 4, the solution domain was divided
into 256 × 256 grid points with x̃ = ỹ = 0.5.

4. Results and discussion

In order to examine whether the phase field model correctly reproduces the physics of void–
matrix interface motion, two-void growth and shrinkage test cases were studied. In the first
case, a small initial void was placed at the center of the simulation domain and the vacancy
concentration in the matrix surrounding the void is set higher than the value required to
maintain the given void under equilibrium. Here, the vacancy concentration is indicated
by the supersaturation Sv , which is the ratio of cv (x̃, t˜) to the thermal concentration value.
The simulation was carried out in the absence of vacancy production and without thermal
fluctuations. The evolution of the diffuse void–matrix interface is monitored by tracking
the profile of the phase field η(x̃, t˜) and the radius of the void is taken to be the level set
η = 0.5. Figure 2 displays typical line profile snapshots of the field η(x̃, t˜) at two different
supersaturation ratios for the same initial profile; the figure shows that the void–matrix interface
moved outward. Simultaneously, an inward flux of vacancies into the void was observed. In
effect, the void grows by absorbing vacancies from the matrix, and the extent of this void
growth corresponds to the number of vacancies absorbed by the void. This process leads to
lowering the vacancy concentration near the void surface, as shown in figures 3(a)–(d).

                                                                                                                 7
Modelling Simul. Mater. Sci. Eng. 17 (2009) 064002                                                      S Rokkam et al




                 Figure 3. Evolution of cv (x̃, t˜) and η(x̃, t˜) for a uniform initial vacancy concentration higher
                 than that required to maintain the initial void size: (a) cv (x̃, 0), (b) cv (x̃, 250), (c) η(x̃, 0) and
                 (d) η(x̃, 250). As shown in (b), the vacancy concentration is lower close to the void surface due to
                 vacancy absorption.


     In a second test case, a void at the center of the simulation domain is allowed to evolve
in a domain surrounded by a matrix with initial vacancy concentration set to zero. As such
vacancies are emitted from the void, which, in turn, shrinks at a rate corresponding to the
number of vacancies ejected from it. This scenario is depicted in figure 4. The vacancy
concentration gradients established around the void reveal higher vacancy concentration
closer to the void surface, as shown in figure 4(b), which is opposite to the concentration
gradient observed in the first test case. The background concentration in the matrix was
found to increase slowly until it reached vacancy concentration of the order of thermal
equilibrium cvo far away from the shrinking void. The two test cases depicted in figures 3
and 4 show that voids can act as sink or source of vacancies during shrinkage and growth,
respectively.
     The above test has been repeated to investigate the effect of vacancy supersaturation on
void dynamics. Figure 5 shows the void radius as a function of time for different supersaturation
values. In these simulations, an initial radius R ≈ 11.48 (dimensionless) was considered. In
all cases, an initial evolution of the void radius, namely growth, occurred, which is attributed
to the tendency of the system to adjust the initial η and cv fields to be consistent with each
other and with the gradient energy coefficient in the energy functional—the initial conditions
do not necessarily correspond to an equilibrium situation. All initial radii reach a value of
approximately 11.85 before the growth or shrinkage starts out. In this regime, the void grows
or shrinks depending on the level of vacancy supersaturation in the surrounding matrix; that is,
the void radius either grows, stays about the same, or decreases as a function of time depending
on whether background vacancy concentration is above the level needed to sustain the void
size, at that level, or below it. These observations are consistent with the well-known Gibbs–
Thomson effect [20]. For the case studied in figure 5, a supersaturation ratio of about five is
needed to maintain the void size at equilibrium past the initial transient. It is worth noting
here that, for all cases shown in figure 5, the radius evolution proceeds in such as way that,

8
Modelling Simul. Mater. Sci. Eng. 17 (2009) 064002                                                        S Rokkam et al




                 Figure 4. Evolution of cv (x̃, t˜) and η(x̃, t˜) for a uniform initial vacancy concentration equal to
                 zero: (a) cv (x̃, 0), (b) cv (x̃, 250), (c) η(x̃, 0) and (d) η(x̃, 250). Emission of vacancies by the void
                 is illustrated in part (b) where a radial concentration gradient is established.



at long time, the void radius approaches asymptotic value dictated by a final balance between
the void size and the adjusted vacancy concentration profile in the surrounding matrix. This
observation suggests that the Gibbs–Thomson effect should be understood in the sense of
equilibrium of a void of a given radius with a concentration profile in the matrix, rather than
with a single (background) concentration value surrounding the void itself. In other words,
this type of equilibrium involves opposing thermodynamic forces, one of which is associated
with the vacancy concentration gradient around the void.
      To characterize the dynamics of void growth, we studied the evolution of a single void in a
matrix with different vacancy supersaturations. Figure 6 shows the void growth rates computed
from the normal velocity of the void–matrix interface, vn = −(∂η(x, t)/∂t)/|∇η(x, t)|η=0.5 .
It is observed that the void growth is proportional to the vacancy supersaturation and it follows
a power law of the form R = λt n ; R being the void radius increase, λ a prefactor and n the
exponent. The simulations were performed in the absence of vacancy sources. As such, the
total number of vacancies in the system is conserved and the dynamics of void phase is purely
diffusion controlled. The data points in figure 6 are obtained from numerical simulations, and
the trend-lines are obtained as best fit using the graphing software. It is found that the power
law exponent n takes on a value of 0.5 and the prefactor λ is a function of supersaturation and
it takes on values of 0.268, 0.349 and 0.412 for supersaturation ratios of 100, 200 and 300,
respectively. This finding is consistent with most diffusion controlled precipitation processes
where the growth is proportional to t 1/2 .
      The interaction between voids has been investigated by studying a two-void system in
a matrix with thermal equilibrium vacancy concentration. When the sizes of these voids are
not in equilibrium with background concentration, emission and/or absorption of vacancies by
the voids is expected. Figure 7 shows the vacancy concentration field around two interacting
voids. It is found that in this case, the smaller void emits vacancies that are in turn absorbed
by the larger void, i.e. the smaller void behaves as a source and larger void behaves as a sink.

                                                                                                                         9
Modelling Simul. Mater. Sci. Eng. 17 (2009) 064002                                                   S Rokkam et al

                                12.1

                                 12

                                11.9



                  Void radius
                                11.8

                                11.7

                                11.6             Sv = 10          Sv = 2
                                                 S =5             S =1
                                                     v             v
                                11.5             Sv = 3           Sv = 0

                                11.4
                                       0   10        20      30        40   50
                                                          Time

                 Figure 5. Void radius as a function of time for different initial vacancy supersaturation levels.

                                3.5
                                           S = 100
                                            v
                                  3        S = 200
                                            v
                                           S = 300
                                2.5         v



                                  2
                 ∆R(t)
                                1.5

                                  1

                                0.5

                                  0
                                       0   10    20          30        40   50
                                                          Time
                 Figure 6. Void growth as a function of time in supersaturated systems; the fitting parameters for
                 the power law R = λt n are obtained as n = 0.5 and λ = 0.268, 0.349, 0.412 for Sv = 100, 200,
                 300, respectively.

This observation is characteristic of an Ostwald ripening process in precipitating alloys [20],
where the larger precipitates grow at the expense of smaller ones. The fact that one void emits
vacancies and the other absorbs them also signifies the reproduction of the Gibbs–Thomson
behavior in this two-void system.
     Void dynamics has also been investigated under the condition of vacancy generation.
This process is emulated here by considering a stochastic source term Pv (x̃, t˜) = Pvcasc ×
rand(x̃rand , t˜), with Pvcasc being a constant rate of change in vacancy concentration associated
with a single cascade event and rand(x̃rand , t˜) is a dimensionless random number in the
range [0,1] used to determine the strength of the source assigned to a random point x̃rand
in space and each time step. The only constraint on the selection of x̃rand is that it must be in

10
Modelling Simul. Mater. Sci. Eng. 17 (2009) 064002                                                   S Rokkam et al




                 Figure 7. Evolution of concentration field around two interacting voids: (a) initial field and (b) a
                 snapshot of the system at t˜ = 50. The concentration field is depressed around the larger void due
                 to vacancy absorption, and it is higher than the remote background values closer to the small void
                 due to vacancy emission.




                 Figure 8. Display of the vacancy field illustrating the growth and nucleation of voids in a
                 supersaturated matrix under the condition of stochastic vacancy generation: (a) initial system,
                 (b) central void at t˜ = 100, (c) t˜ = 190, (d) t˜ = 250. The nucleation of new voids due to
                 irradiation is evident in parts (c) and (d).


the matrix, and this is easy to fix based on the value of the η field. The source Pv (x̃, t˜) thus
introduces random spikes in the vacancy concentration field. The source vacancies entering the
system thus cause fluctuations in the vacancy concentration, which affects vacancy diffusion
and nucleation of new voids. We remark here that the current selection of the source is only
to test the model. In a real irradiation situation, it will require further modeling to fix the
amplitude Pvcasc and the random selection of space and time points at which the sources are
introduced. The source may even be assigned to a spatial region larger than the mesh size as
we used here.
     Figure 8 shows the time history of the vacancy concentration field around a large central
void in a matrix subjected to vacancy production by irradiation, with an initially uniform

                                                                                                                  11
Modelling Simul. Mater. Sci. Eng. 17 (2009) 064002                                                S Rokkam et al




                 Figure 9. Display of the vacancy field illustrating the concurrent void nucleation and growth
                 in a supersaturated system under the effect of stochastic vacancy generation: (a) initial system,
                 (b) t˜ = 225, (c) t˜ = 275, (d) t˜ = 300.


vacancy field set by Sv = 1000. This large value of supersaturation is not typical in metals under
irradiation; here, it has been selected so high to shorten the incubation period for nucleation.
In this example, a few features of void dynamics are illustrated: (a) the increase in the void to
a much larger size as a result of massive absorption of vacancies, (b) nucleation of additional
voids under irradiation and (c) suppression of nucleation close to a free surface (introduced
by the large void surface in the present case). Referring to figure 8, it is clear that the central
void grows as a function of time by massive absorption of vacancies from the matrix. The
growth of the initial central void is also accompanied by the nucleation and growth of small
additional voids. The creation of new voids is, however, observed only away from the large
central void surface because this surface absorbs vacancies at a very high rate, thus lowering
the vacancy concentration in its vicinity to a level lower than that required for the nucleation
process. Indeed, figure 8 shows that the vacancy concentration is highly depressed in a large
region surrounding the central void. This observation is consistent with the classical literature
on nucleation of voids in irradiated materials, where free surfaces and grain boundaries are
characterized by denuded zones within which no voids are created [21].
     The case of homogeneous nucleation in a supersaturated system has been observed by
considering a supersaturated system subject to stochastic vacancy generation. In this case,
no initial voids are introduced, i.e. the phase field η(x̃, 0) is set equal to zero everywhere in
the domain of solution initially, and the simulation was started with an initial supersaturation
Sv = 1000. The radiation induced vacancies enter the system through the stochastic source
term, as explained earlier. Figure 9 shows snapshots of the corresponding cv (x̃, t) field over
the domain of solution. The stochastic term Pv (x̃, t˜) represents fluctuations in the vacancy
concentration field that are introduced randomly in space and time. While the average value of
the source increases the background vacancy concentration, the spiky nature of these sources
assists the nucleation process. Indeed, after an initial incubation period, small void nuclei
started to appear in the system at different times, which grew by absorbing the vacancies

12
Modelling Simul. Mater. Sci. Eng. 17 (2009) 064002                                                     S Rokkam et al

                                  0.5
                                             Pv casc = 0.1
                                  0.4        Pv casc = 0.25




                  Void fraction
                                                 I   II    III
                                  0.3


                                  0.2


                                  0.1


                                   0
                                        0   50       100      150   200   250   300
                                                             Time
                 Figure 10. Different stages of void formation observed by analysis of the void volume fraction as
                 a function of time: stage I, incubation; stage II, nucleation; stage III, growth. Reduction in the rate
                 of production of vacancies in the system results in longer incubation periods and lower nucleation
                 and growth rates. The magnitude of the vacancy generation spikes introduced in the system are
                 given by a random fraction times the displayed Pvcasc values in the figures.


from the surrounding matrix. It should be noted that formation of the small void nuclei (both
in figures 8 and 9) involves the creation of an interface between the void and solid phases.
The formation of the diffuse void–matrix interface is a result of the competition between the
gradient energy terms and the bulk energy terms of the energy functional (equation (1)). The
gradient energy terms inherently account for the curvature of the diffuse void-interface and its
formation is favored by constraints which evolve the system so as to decrease its free energy.
In classical homogeneous nucleation theory, this corresponds to the formation of infinitely
narrow interface characterized by the surface tension of the interface.
     Figure 10 shows the porosity (or void fraction of simulated domain) as a function of
time for two different vacancy generation rates. The porosity versus time curve enables us to
split the void phase dynamics in figure 9 into a series of three characteristic stages. Stage I
corresponds to an incubation period where no void phases are formed. During this stage, the
vacancies introduced by virtue of the source term increase the level of supersaturation in the
system and hence raises its metastability. As time goes on, the system enters a regime in
which small stable nuclei are formed in order to reduce the free energy of the system; this
is stage II known as the nucleation regime. It can be observed that once the nucleation of
the voids begins, multiple nuclei are formed within a small time window. This observation is
similar to the homogeneous nucleation regime in classical nucleation studies. The voids that
have already been formed then grow concurrently with the formation of new voids. However,
this stage is predominantly dominated by nucleation. Stage II, the nucleation regime, saturates
after a short duration due to depletion of vacancies. This saturation leads to the transition to
stage III, the growth regime. In the latter regime, the already existing voids continue to grow
by absorbing vacancies from the solid, and the larger voids also grow at the expense of smaller
ones in their vicinity, a process known as Ostwald ripening [20].
     For the test case of homogeneous nucleation discussed above, figure 11 shows the number
of voids as a function of simulation time. The figure shows that, subsequent to the incubation

                                                                                                                     13
Modelling Simul. Mater. Sci. Eng. 17 (2009) 064002                                               S Rokkam et al

                                    60
                                                                     P vcasc = 0.1
                                    50            I   II    III
                                                                     P vcasc = 0.25

                                    40



                  Number of voids
                                    30

                                    20

                                    10

                                     0
                                         0   50       100     150   200   250         300
                                                             Time

                 Figure 11. Number of voids as a function of time during the nucleation and growth stages for the
                 test case discussed in figures 9 and 10.


period, the number of voids increases linearly with time throughout stage II, which corresponds
to the steady state nucleation regime. In stage III, the ripening results in smaller void density
because the smaller voids may dissolve and give vacancies back into the matrix. As such,
the number of voids decreases with simulation time in stage III. The dissolution of smaller
voids increases the vacancy concentration of the surrounding matrix and thereby facilitates a
vacancy exchange between neighboring voids, a process that occurs such that the larger void
grows at the expense of its smaller neighbors. In some cases, in stage III, void coalescence
also takes place if voids are nucleated close to each other or if they become close to each other
as a result of growth. This process also contributes to the reduction in the void density in
stage III.
     The effect of the radiation source on the dynamics of void nucleation and growth is
illustrated in figures 10 and 11. Two values of the source rate Pvcasc have been considered,
0.1 and 0.25, which represent a given vacancy generation rate and a relatively higher rate for
the sake of comparison. Note that the time and space average of the source is much smaller
than Pvcasc because the actual source is a fraction of Pvcasc , which we introduce randomly in
space and time. As expected, the results displayed in figures 10 and 11 clearly show that a
stronger magnitude of the source shortens the incubation period (stage I) and results in a larger
number of nuclei in stage II and a higher void fraction in stage III, i.e. it results in higher void
nucleation and growth rates.
     It is to be noted that the current void nucleation and growth problem differ from the
classical problem of nucleation and growth of, say, precipitates in alloys. For example,
while the precipitate formation problem corresponds to a constant total mass of solute in
the alloy, the current problem involves generation of vacancies. Also, the nucleation process
in classical models is attributed to thermal fluctuations. Here, the source fluctuations dominate
the nucleation process. In spite of these important differences, the incubation, nucleation and
growth behavior observed in the current problem resembles, to a large extent, the precipitate
formation and growth behavior in the classical precipitation problem. In order to illustrate
these similarities, we analyzed the behavior of the porosity and void number in light of classical

14
Modelling Simul. Mater. Sci. Eng. 17 (2009) 064002                                     S Rokkam et al

results. For example, the porosity in stage II, which is a measure of the void area fraction in
our model, is compared with the classical analytical expression of the Kolmogorov–Johnson–
Mehl–Avrami (KJMA) equation [22–24] in 2D, which takes on the form

                 ρ = ρ e [1 − exp(−kt 3 )],                                                     (12)

with ρ e being the porosity (or void fraction) at the end of the nucleation stage II and k a constant
characteristic of the nucleation kinetics in the system. For the results presented herein, the
above formula fits the porosity evolution results, with ρ e = 0.278 and k = 1.72 × 10−4 for
Pvcasc = 0.25 and ρ e = 0.259 and k = 7.93 × 10−5 for Pvcasc = 0.1. In the growth regime,
stage III, the porosity is fit to the analytical expression of the Ostwald ripening regime [25, 26],
according to

                 ρ = ρ o (1 + t/τ1 ).                                                           (13)

It can be observed that in the growth regime, porosity increases in a linear fashion with a slope
of ρ o /τ1 . The fit parameters can be obtained as ρ o = 0.1885 and τ1 = 230.05 for Pvcasc = 0.25,
and ρ o = 0.1516, and τ1 = 371.73 for vacancy source Pvcasc = 0.1. Further, it can be observed
from figure 11 that the nuclei formed in stage II at a constant rate nvoid = J t. The nucleation
rate J is found to be 2.22 and 1.04 for Pvcasc = 0.25 and Pvcasc = 0.1, respectively. The
decrease in the number of voids during the growth process of stage III can be approximated
using an expression for the Ostwald ripening process [25–27] according to

                 nvoid = no (1 + t/τ2 )−m .                                                     (14)

The fitting parameters for figure 11 were obtained as no = 53.45, τ2 = 331.15 and m = 0.926
for Pvcasc = 0.25 and no = 178.28, τ2 = 34.92 and m = 0.673 for Pvcasc = 0.1.
     The results presented above illustrate that the current phase field model reproduces the
basic dynamics of void formation and growth in irradiated metals, and that the behavior of void
density and porosity obtained by the phase field model display more or less the same behavior
observed in classical models of similar phenomena. This agreement, although preliminary,
cannot yet be generalized at this stage of model development. The additional benefit of phase
field simulations, however, is the ability to generate actual microstructure realizations and
to consider, in an extended version of this model, the effects or pre-existing microstructural
features, especially grain boundaries and precipitate/matrix interfaces on the nucleation and
growth of voids.


5. Concluding remarks

A phase field model for void microstructure evolution under vacancy supersaturation condition
is presented. The process of vacancy generation under irradiation is systematically included
as a part of the model. This model is phenomenological in nature because it is derived from
a free energy functional that includes materials parameters that are yet to be determined in
terms of fundamental materials properties. In particular, the free energy functional of the
system consists of the well-known statistical physics expression of the free energy of a non-
interacting vacancy system, plus additional energy terms that are inspired by the classical
gradient formulations of the free energy of heterogeneous media in the theory of spinodal
decomposition of Cahn and Hilliard [17, 18] and the theory of antiphase boundary of Allen
and Cahn [19]. Bistability is built into the free-energy expression by a Landau-type free-
energy term. The present model differs from a recent model introduced relatively recently for

                                                                                                  15
Modelling Simul. Mater. Sci. Eng. 17 (2009) 064002                                  S Rokkam et al

void formation in a supersaturated vacancy concentration [28] in that our model considers,
in addition to the vacancy field, a non-conserved phase field variable η that demarcates the
matrix and void phases. The present model is thus able to introduce the surface energy of
voids through the gradient term associated with this variable, and thus limits the diffuse-
interface region to a small width that transitions from a matrix phase with a very low
concentration of vacancies to a void phase that contains only vacancies. A consequence
of considering a long range order parameter in the present model is that the dynamics of
vacancies and voids are governed by coupled equations of the Cahn–Hilliard and Allen–Cahn
types.
     The present model has been solved using the explicit finite difference scheme and applied
to a set of 2D test problems. All test cases indicate that the void surface (or the void–matrix
interface) can act as a source or sink of vacancies, and that voids grow (or shrink) depending
on the background vacancy concentration. In particular, the test cases for single voids have
successfully reproduced the Gibbs–Thomson effect. A second important verification case has
been the interaction between large and small voids that are closely separated. In this case, the
model also successfully reproduces the Ostwald ripening effect; that small voids dissolve by
giving vacancies back to the matrix, which are then absorbed by the larger void. A third test
case that was successfully simulated by this model was the nucleation in the vicinity of a free
surface. This test case was modeled by investigating the nucleation process close to the surface
of a large void, and the model revealed the expected trend that the presence of a free surface
leads to the formation of a denuded or void-free zone due to massive absorption of vacancies
by the free surface. Yet, the most important test of the present model has been the reproduction
of the dynamics of homogeneous nucleation and growth of voids in a system that is initially
void-free and subject to stochastic vacancy generation. In particular, it has been found that
the model reproduces the distinct stages of (I) incubation, (II) transient and steady state void
nucleation and (III) nucleation saturation and void growth, including ripening and coalescence
of voids. The void fraction and void density were fit to formulae of classical models in both the
nucleation and growth regimes, in spite of important differences between the current problem
conditions and those considered in the related classical models.
     It should be borne in mind that the present model represents only an initial step toward
a more complete phase field model for microstructure evolution in irradiated metals. Two
additional steps need to be carried out in order to complete this model in the future and
apply it to real irradiation conditions. The first step is to consider interstitials as a species
that plays a role in the nucleation and growth process of voids in the system. In particular,
the presence of interstitials leads to annihilation of vacancies in the matrix, thus lowering
the rate of nucleation. Interstitials can also be absorbed by voids, a process that slows
down the growth rate of the latter. The second step is to pin down the model parameters
in terms of actual materials properties. In this regard, the interfacial mobility L and all energy
prefactors in equations (1) and (3) can be found by matching the model with the corresponding
sharp interface model of void formation and evolution. In doing so, asymptotic analysis
can also be performed to ensure that the phase field model reproduces the same behavior
of the corresponding sharp interface model [29]. These steps are the subject of an ongoing
investigation.

Acknowledgments

This work was performed as part of a Computational Materials Science Network (CMSN)
project supported by the US DOE Office of Basic Energy Sciences via contract number
DEFG02-07ER46367 at Florida State University. The authors also acknowledge the financial

16
Modelling Simul. Mater. Sci. Eng. 17 (2009) 064002                                                   S Rokkam et al

support by the Idaho National Laboratory through subcontract number 00075400 at Florida
State University.

Appendix A. Finite difference scheme

The quantities ψv |ni,j and ψη |ni,j introduced in equations (10) and (11) are given by

ψv |ni,j = h(η)[Ẽvf + ln cv − ln(1 − cv )] − 2Ã(cv − cvo )(η4 − 3η2 + 2η)

                  + 2B̃(cv − 1)η2 − 2κ̃v ∇˜ 2 cv |ni,j ,                                                      (A.1)

ψη |ni,j = h (η)[Ẽvf cv + cv ln cv + (1 − cv ) log(1 − cv )]

                      −Ã(cv − cvo )2 (4η3 − 6η + 2) + 2B̃(cv − 1)2 η − 2κ̃η ∇˜ 2 η|ni,j ,                    (A.2)

where the Laplacian terms ∇˜ 2 cv |ni,j and ∇˜ 2 ηv |ni,j are in turn evaluated using a 5-point central
difference scheme.


References

 [1] Mansur L K and Bloom E E 1982 Radiation effects in reactor structural alloys J. Met. 34 23–31
 [2] Lucas G E 1993 The Evolution of mechanical property change in irradiated austenitic stainless steels J. Nucl.
        Mater. 206 287–305
 [3] Garner F A, Packan N H and Kumar A S 1987 Radiation-Induced Changes in Microstructure: 13th Int. Symp.
        (Seattle, WA) (PA, USA: ASTM)
 [4] Russell K C 1971 Nucleation of voids in irradiated metals Acta Metall. 19 753–8
 [5] Mayer R M and Brown L M 1980 Nucleation and growth of voids by radiation: II. Differential equations J. Nucl.
        Mater. 95 58–63
 [6] Bralisford A D and Bullough R 1972 The rate theory of swelling due to void growth in irradiated metals J. Nucl.
        Mater. 44 121–35
 [7] Wiedersich H 1972 On the theory of void formation during irradiation Radiat. Eff. 12 111
 [8] Brailsford A D and Bullough R 1981 The theory of sink strengths Phil. Trans. R. Soc. Lond. Ser. A 302 87–137
 [9] Brailsford A D, Bullough R and Hynes M R 1976 Point defect sink strengths and void-swelling J. Nucl. Mater.
        60 246–56
[10] Sass S and Gyre B L 1973 Diffraction from void and bubble arrays in irradiated molybdenum Phil. Mag. 27 1447
[11] Evans J H 1971 Observations of a regular void array in high purity molybdenum and TZM irradiated at high
        temperatures with 2 MeV nitrogen ions Radiat. Eff. 10 55–60
[12] Johnson P B, Mazey D J and Evans J H 1983 Bubble structures in helium (1+)-irradiated metals Radiat. Eff.
        78 147
[13] Brager H R, Garner F A and Guthrie G L 1977 The effect of stress on the microstructure of neutron irradiated
        type 316 stainless steel J. Nucl. Mater. 66 301
[14] Garner F A 1994 Irradiation performance of cladding and structural steels in liquid metal reactors Materials
        Science and Technology: A Comprehensive Treatment vol 10A Nuclear Materials ed R T Brian Frost
        (New York: VCH) pp 419–543
[15] Boettinger W J, Warren J A, Beckermann C and Karma A 2002 Phase-field simulation of solidification Annu.
        Rev. Mater. Res. 32 163–94
[16] Chen L Q 2002 Phase-Field models for microstructure evolution Annu. Rev. Mater. Res. 32 113–40
[17] Cahn J W and Hilliard J E 1958 Free energy of a nonuniform system: I. Interfacial free energy J. Chem. Phys.
        28 258–67
[18] Cahn J W 1961 On spinodal decomposition Acta Metall. 9 795–801
[19] Allen S M and Cahn J W 1979 A microscopic theory for antiphase boundary motion and its application to
        antiphase domain coarsening Acta Metall. 27 1085–95
[20] Balluffi R W, Allen S M and Carter W C 2005 Kinetic of Materials (New Jersey: Wiley)
[21] Zinkle S J and Singh B N 2000 Microstructure of Cu–Ni alloys neutron irradiated at 210 ◦ C and 420 ◦ C to 14 dpa
        J. Nucl. Mater. 283–287 306–12

                                                                                                                  17
Modelling Simul. Mater. Sci. Eng. 17 (2009) 064002                                              S Rokkam et al

[22] Kolmogorov A N 1937 Statistical theory of metal crystallization Izv. Akad. Nauk SSSR 1 355–9 (in Russian)
[23] Johnson W A and Mehl R F 1939 Reaction kinetics in processes of nucleation and growth Trans. AIME 135
        416–58
[24] Avrami M 1941 Kinetics of phase change: III. Granulation, phase change, and microstructure J. Chem. Phys.
        9 177–84
[25] Zinke-Allmang M, Feldmann L C and Grabow M C 1992 Clustering on surfaces Surf. Sci. Rep. 16 377
[26] Raab A and Springholz G 2001 Oswald Ripening of facetted self-assembled PbSe quantum dots during annealing
        Phys. Status Solidi b 224 509–13
[27] Sagui C and Grant M 1999 Theory of nucleation and growth during phase separation Phys. Rev. E 59 4175–87
[28] Yu H-C and Lu W 2005 Dynamics of the self-assembly of nanovoids and nanobubbles in solids Acta Mater.
        53 1799–807
[29] Emmerich H 2003 The Diffuse Interface Approach in Materials Science. Thermodynamic Concepts and
        Applications of Phase-Field Models (Berlin: Springer)




18
