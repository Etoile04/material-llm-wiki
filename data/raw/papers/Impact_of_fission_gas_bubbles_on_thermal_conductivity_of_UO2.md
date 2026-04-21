# Impact of fission gas bubbles on thermal conductivity of UO2<math><msub is="true"><mrow is="true"></mrow><mn is="true">2</mn></msub></math> fuels with high thermal conductivity additives

---

                                                                 Journal of Nuclear Materials 546 (2021) 152779



                                                                Contents lists available at ScienceDirect


                                                           Journal of Nuclear Materials
                                                        journal homepage: www.elsevier.com/locate/jnucmat




Impact of ﬁssion gas bubbles on thermal conductivity of UO2 fuels
with high thermal conductivity additives
Floyd W. Hilty, Dong-Uk Kim, Michael R. Tonks∗
Department of Materials Science and Engineering, University of Florida, Gainesville FL 32611 United States




a r t i c l e          i n f o                          a b s t r a c t

Article history:                                        High thermal conductivity additives are being considered to create composite nuclear fuels with a higher
Received 29 July 2020                                   effective thermal conductivity (ETC) to reduce the peak fuel temperatures during reactor operation. How-
Revised 1 December 2020
                                                        ever, the beneﬁts of the additive may be reduced, or possibly eliminated, when placed into a reactor
Accepted 4 January 2021
                                                        environment. In this work, we investigate the impact of ﬁssion gas bubbles on the ETC of composite fu-
Available online 7 January 2021
                                                        els. We create 2D simulations representing a small portion of a composite UO2 fuel containing a single
Keywords:                                               additive particle and calculate the ETC with various volume fractions of ﬁssion gas bubbles. Our results
Fission gas bubbles                                     show that ﬁssion gas bubbles, depending on the volume fraction and contact angle at the additive inter-
UO2                                                     face, can completely remove any beneﬁt of the additive and even result in a lower thermal conductivity
High thermal conductivity additives                     than in UO2 without the additive. We also expose a trend that relates the fraction of additive that is
                                                        screened by bubbles to the ETC. We then propose a model which predicts the ETC of a composite fuel
                                                        with ﬁssion gas bubbles to better estimate the beneﬁts of a novel fuel design.
                                                                                                                            © 2021 Elsevier B.V. All rights reserved.




1. Introduction                                                                              ture to maximize the impact of the additive [15]. Fuel performance
                                                                                             simulations have been carried out for the composite fuel in which
    There is a push to create a new generation of accident tolerant                          they use the increased thermal conductivity and decreased ura-
nuclear fuels [1]. The goal of these fuels are to reduce the probabil-                       nium density. They have shown performance improvements during
ity and severity of accidents and to improve reactor eﬃciency. One                           normal and accident conditions [16–21].
area of focus in this search is the incorporation of high thermal                                However, there are complicating factors in a reactor environ-
conductivity additives in traditional UO2 fuels. These new compos-                           ment. Radiation can cause some additives to react with the fuel
ites have a higher effective thermal conductivity (ETC), allowing for                        and become unstable [22]. Even if an additive is stable under ir-
more eﬃcient heat extraction from the fuel and greater power gen-                            radiation, the production of ﬁssion gas bubbles could reduce the
eration. Many different types of additives have been used, as sum-                           thermal conductivity beneﬁt of the additive. Fission gas, primarily
marized by Zhou and Zhou [2], including beryllium oxide (BeO) [3],                           composed of xenon (Xe) and krypton, has a low thermal conduc-
silicon carbide (SiC) [4], diamond [5], molybdenum [6], tungsten                             tivity and segregates to interfaces such as grain boundaries [23,24].
[7], carbon nanotubes [8], and graphene [9]. Uranium-bearing ad-                             If ﬁssion gas bubbles were to form at the fuel/additive interface,
ditives, including UN [10] and U3 Si2 [11], have also been suggested;                        they could form a thermal barrier around the additive, effectively
they have the dual beneﬁts of increasing the thermal conductivity                            screening it and dampening its thermal beneﬁts to the compos-
and the uranium density.                                                                     ite. Since no microstructure characterization has been carried out
    Modeling and simulation have been used to estimate the im-                               on irradiated composite fuels with signiﬁcant ﬁssion gas content,
provement in the ETC from the additives and to assess their impact                           the interaction between the additive and ﬁssion gas bubbles is still
on the fuel performance. Finite element models have been devel-                              uncertain. All fuel performance simulations that include the impact
oped to predict the increase in the thermal conductivity for a given                         of high thermal conductivity additives [16–21] assume that the ad-
additive and microstructure [12–14]. In addition, we have devel-                             ditives do not alter any of the other fuel behaviors, including the
oped an eﬃcient thermal resistor model that has also been used                               ﬁssion gas behavior.
to provide guidance on how to tailor the composite microstruc-                                   In this work, we use 2D mesoscale simulation to provide a
                                                                                             preliminary picture of the possible impact of ﬁssion gas bubbles
                                                                                             on the thermal conductivity of composite fuel. A small portion of
  ∗
      Corresponding author.                                                                  a composite fuel microstructure is represented, containing a sin-
      E-mail address: michael.tonks@uﬂ.edu (M.R. Tonks).                                     gle additive particle and ﬁssion gas bubbles with varying volume


https://doi.org/10.1016/j.jnucmat.2021.152779
0022-3115/© 2021 Elsevier B.V. All rights reserved.
F.W. Hilty, D.-U. Kim and M.R. Tonks                                                                       Journal of Nuclear Materials 546 (2021) 152779


fractions, contact angles, and additive particle shapes. The ETC for           While the gas-UO2 interface energy is the same in all the var-
each microstructure is calculated, in order to systematically inves-       ious composite fuels, the additive-UO2 and gas-additive interface
tigate the impact of ﬁssion gas as a function of the bubble struc-         energies will depend on the additive and possibly on the fabri-
ture, showing that for certain bubble geometries, the composite            cation method used to create the composite fuel. Unfortunately,
fuel can be even worse than in standard UO2 . Our computational            these values are not known for the majority of the additives. Since
methodology is summarized in Section 2, starting with the cre-             the energies are not known, the range of ﬁssion gas bubble contact
ation of the bubble structure and ending with the method for cal-          angles on the surface of the various additives is also not known.
culating the ETC. In Section 3, we demonstrate the impact of ﬁs-           For this reason, we constructed microstructures with various con-
sion gas on the ETC of the composite. Section 4 outlines the effec-        tact angles (measured from the surface of the additive particle)
tiveness of four metrics used to describe the relationship between         that span the range of possible values: 35◦ (the bubble spreads
the ETC of the composite and the ﬁssion gas bubble’s morphology            out across the interface), 45◦ , 65◦ , 85◦ , 95◦ , 105◦ , and 135◦ (the
and position with respect to the additive. An analytical model is          bubble minimizes contact with the interface).
proposed in Section 5 to predict the ETC of a composite fuel at                To construct the microstructures, we used an existing phase-
burn-up and then it is tested against systems not used in the de-          ﬁeld model that describes the evolution of ﬁssion gas bubbles
velopment of the model. In Section 6, we discuss the possible lim-         in UO2 [25]. The model was solved using the ﬁnite element
itations and implications of this model. Finally, we conclude our          method with the Muliphysics Object-Oriented Simulation Environ-
work in Section 7.                                                         ment (MOOSE) [26,27]. In the model, a circular bubble of the de-
                                                                           sired size was introduced at the additive-UO2 interface and it was
                                                                           then allowed to relax to its equilibrium morphology. The structure
2. Methodology and numerical approach
                                                                           of the additive was not allowed to evolve. The size of the gas bub-
                                                                           ble was varied to investigate the impact of different volume frac-
   Manufacturing and then irradiating UO2 composite fuels is ex-
                                                                           tions. Note that the phase ﬁeld simulations were only used to ob-
tremely costly and time consuming. For this reason, there is a lack
                                                                           tain the equilibrium shape of the bubble and had no other impact
of experimental data that characterizes the evolution of the fuel
                                                                           on this study.
microstructure and properties during reactor operation. Therefore,
                                                                               Using this technique, a wide range of simulated bubble struc-
we use simulation to provide a preliminary view of the change in
                                                                           tures were created, and some examples of them are shown in
the ETC of composite fuel due to the formation and growth of ﬁs-
                                                                           Fig. 1. The largest set of these microstructures have a single spheri-
sion gas bubbles. However, to determine the ETC, we ﬁrst need a
                                                                           cal additive particle placed at the center of the domain and a bub-
means of creating a pool of simulated microstructures for use in
                                                                           ble centered on the right side of the particle along the x-axis, as
this study. This method and the resulting simulated microstruc-
                                                                           shown on the left of Fig. 1. For each contact angle, microstruc-
tures are outlined in Section 2.1. In Section 2.2, we describe the
                                                                           tures were created with the bubble volume fraction ranging from
method used to calculate the ETC of each of the simulated mi-
                                                                           0.006 to 0.040. The range of ﬁssion gas bubble volume fractions
crostructures.
                                                                           occurring in real fuels can vary depending on the fuels composi-
                                                                           tion, grain size, and burn-up; bubble volume fractions have been
2.1. Microstructure simulations                                            shown to reach values of 0.03–0.12 [28–30]. In each case, the vol-
                                                                           ume fraction of additive was 0.11.
    In order to determine the impact of ﬁssion gas bubbles on the              To investigate the effect of the bubble’s position relative to the
thermal conductivity of a composite fuel, we need to represent mi-         direction of heat ﬂow, a few example microstructures were cre-
crostructures with fuel, additive, and gas bubbles. Composite fuel         ated with the bubble located at the surface of the spherical particle
microstructures can be summarized into two primary categories,             (0.11 volume fraction), but at a position further up on the surface
those with isolated particles distributed throughout the UO2 and           rotated at an angle of either 45◦ or 90◦ counterclockwise around
those with more continuous additive coating the grain boundaries.          the center of the particle. For these cases, the contact angles used
In this work, we focused on the isolated additive particles, since         were 35◦ , 65◦ , 95◦ , and 135◦ and the bubble volume fractions were
they are more common and are easier to manufacture. For non-               0.006, 0.040, 0.017, and 0.014. One ﬁnal microstructure was sim-
uranium-bearing additives, it is desirable to keep the additive vol-       ulated with two bubbles placed at the additive particle interface.
ume fraction small, since it decreases the overall uranium density         These bubbles were rotated plus and minus 45◦ around the center
of the fuel. Thus, additive particles are often isolated from other        of the additive particle, with a total volume fraction of 0.012 and a
additive particles, though having a more continuous path of ad-            contact angle of 35◦ . Examples of these microstructures are shown
ditive in the direction of heat transport does lead to higher ther-        in the top right of Fig. 1.
mal conductivity as shown in our previous work [15]. To simplify               Additionally, a smaller series of structures was simulated using
our analysis, we modeled a single isolated additive particle within        a rectangular additive particle with a 3:1 aspect ratio, but still with
a UO2 matrix, and we considered both spherical and rectangular             an additive volume fraction of 0.11. This particle was centered in
particles. We represented the particle in 2D to further simplify the       the simulation domain and oriented such that its long axis was
analysis.                                                                  aligned with the direction of heat ﬂow. For this particle geome-
    The impact of ﬁssion gas bubbles on the thermal conductivity           try, ten calculations were performed, three with the bubble cen-
of composite fuel depends on the shape of the bubbles that form            tered on the top of the additive particle, and seven with the bub-
on the surface of the additive. That shape is determined by the en-        ble centered on the side of the additive particle (see bottom right
ergy of each unique interface created: additive-UO2 , gas-additive,        of Fig. 1 for examples). The volume fraction for the three bubbles
and gas-UO2 . The ﬁssion gas bubble will adopt a shape that min-           on the top ranged from 0.003 to 0.021 and for the seven bubbles
imizes the total energy of the system by reducing the amount of            on the side from 0.003 to 0.020. In all cases the contact angle was
high energy interfaces in favor of low energy interfaces. A low con-       90◦ on the ﬂat surface.
tact angle means the gas bubble readily spreads out across the sur-
face of the additive, reducing the amount of additive-UO2 interface        2.2. Heat conduction
while creating more gas-additive and gas-UO2 interface. For a high
contact angle, the gas-additive interface is minimized in favor of            The goal of this study is to determine the ETC of the mi-
additive-UO2 and gas-UO2 interfaces.                                       crostructures described in the previous section. This was carried

                                                                       2
F.W. Hilty, D.-U. Kim and M.R. Tonks                                                                                           Journal of Nuclear Materials 546 (2021) 152779




Fig. 1. Examples of microstructures used in this study. The left image shows spherical additive particles with gas bubbles on the right. They have a range of bubble
volume fractions and contact angles. Top and bottom right are spherical and rectangular additive particle microstructures, respectively, showing different bubble positioning.
Displayed above each microstructure is the screening fraction for that conﬁguration, described in Section 4. Each image has been cropped from a 400 × 400 μm sample. The
spherical particles have a radius of 75 μm, and the rectangular particles are 230 × 77 μm.



out using heat conduction simulations with the MOOSE frame-                                   To determine the effective thermal conductivity of the entire
work. In these simulations, the 2D microstructures were spatially                         microstructure from the heterogeneous local thermal conductivity,
resolved in a 400 × 400 μm Cartesian computational domain with                            a homogenization approach is needed that takes into account the
a uniform mesh size of 1 μm. We used a Cartesian rather than                              physics of heat conduction. In this study, we used the asymptotic
cylindrical domain since it provided the simplest means of resolv-                        expansion homogenization (AEH) method to determine the effec-
ing the particle and ﬁssion gas bubbles, including the diffuse in-                        tive thermal conductivity. Details of the AEH method are described
terfaces that result from the phase ﬁeld method used to construct                         by Chung et al. [34] and its implementation in MOOSE is described
the bubbles. The local thermal conductivity used in the simulations                       by Hales et al. [35]. The AEH method has been shown to robustly
was heterogeneous, with different values assigned in the bulk UO2 ,                       and accurately determine the ETC and it has been used to deter-
additive, and gas bubble regions. For these calculations, unless oth-                     mine the ETC of reactor fuel microstructures in several past works
erwise speciﬁed, the temperature was 300 K, the bulk phase was                            [15,23,36,37]. In this work, we always report the ETC assuming that
UO2 , the additive phase was BeO, and the gas phase was assumed                           heat is transported along the x-direction.
to be composed completely of Xe (as it is the most common ﬁssion
gas). At 300 K, the thermal conductivity of UO2 is 8.24 W/mK [31],                        3. Impact of ﬁssion gas on effective thermal conductivity
of BeO is 370 W/mK [32], and of Xe gas is 0.0055 W/mK [33]. An
example of of a mesh shaded by thermal conductivity is shown in                               Using the method and microstructures outlined in Section 2,
Fig. 2.                                                                                   we conducted a study to determine the impact of ﬁssion gas bub-
                                                                                          bles on the ETC of composite fuel. In Fig. 3, the ETC calculated for
                                                                                          all the microstructures are plotted versus bubble volume fraction,
                                                                                          with the color of the dot indicating which microstructure group
                                                                                          they belong to. Additionally, the dashed lines are reference values
                                                                                          for the fresh composite fuel in yellow, pure UO2 in green, and pure
                                                                                          UO2 with a single spherical bubble in pink. Fig. 3(a) has all data for
                                                                                          a spherical additive particle, and Fig. 3(b) has all rectangular addi-
                                                                                          tive particle data.
                                                                                              The overall trend is as expected; as the bubble grows, the ETC
                                                                                          of the composite is reduced. However, the wide spread in the data
                                                                                          for a given bubble volume fraction indicates that there are other
                                                                                          mechanisms at work. In Fig. 3(a), we see that for a given bubble
                                                                                          fraction, bubbles with a contact angle less than 85◦ have an in-
                                                                                          creased impact on the ETC compared to bubbles with larger con-
                                                                                          tact angles. This appears to be due to the bubble spreading out
                                                                                          along the additive-UO2 interface for small contact angles. The more
                                                                                          spread out a bubble is across the additive interface, the larger im-
                                                                                          pact it has on the ETC of the composite. Due to the large impact of
                                                                                          the bubble with the smallest contact angle (35◦ ), its ETC reaches
                                                                                          the same value as a microstructure with gas but no additive at a
                                                                                          bubble fraction of 0.04, eliminating any beneﬁt of the additive.
                                                                                              The microstructures with the bubble rotated away from the
                                                                                          center of the additive particle with respect to the direction of heat
                                                                                          ﬂow have a higher ETC then microstructures with the same bub-
Fig. 2. An example UO2 microstructure composed of a spherical BeO particle with
a gas bubble on its surface, shaded by the local thermal conductivity. The magniﬁed       ble fraction and contact angle in the direction of heat ﬂow. One
section shows the uniform mesh applied in the simulations of this work. The mesh          good example of this is the microstructure with two bubbles, ro-
spacing is 1 μm and the simulation domain is 400 × 400 μm.                                tated at plus and minus 45◦ . This structure has a higher ETC than

                                                                                      3
F.W. Hilty, D.-U. Kim and M.R. Tonks                                                                                             Journal of Nuclear Materials 546 (2021) 152779




Fig. 3. ETC plotted versus the bubble volume fraction for the microstructures demonstrated in Fig. 1. (a) has the microstructures with spherical additive particles. The angles
in the legend not labeled as rotations are contact angles. (b) has the rectangular additive particle microstructures; top and side in the legend refers to the bubble’s position.
The dashed lines are reference structures, where yellow is UO2 with an additive volume fraction of 0.11 but no gas, green is pure UO2 , and pink is UO2 with a single circular
gas bubble but no additive. The difference in the dashed yellow from (a) and (b) is due to the shape of the additive particle. (c) extends the data points for the spherical
particles with 35◦ and 45◦ contact angles to higher bubble volume fractions (labeled full system), showing that after a bubble fractions of 0.04 and 0.07, respectively, the
ETC of a composite fuel with a bubble is worse than pure UO2 with a bubble. The blue and orange dashed lines are for UO2 with a crescent shaped bubble and no additive,
as illustrated in (d) for a gas shape from the 0.04 bubble fraction with a 35◦ contact angle. (For interpretation of the references to color in this ﬁgure legend, the reader is
referred to the web version of this article.)



a single bubble on the right of the particle with the same bubble                          ticle has a crescent shape, wider in the direction perpendicular to
volume fraction (0.012) and contact angle (35◦ ). Additionally, when                       the heat transport direction, as shown in Fig. 1. To test this, we re-
a bubble is rotated 90◦ to be positioned at the top of the additive                        moved the additive particle from the full system microstructures,
particle, the ETC is almost equal to that for the fresh composite                          but maintained the bubble with the crescent shape (see Fig. 3(d)),
fuel for bubble fractions of 0.02 or less.                                                 and calculated the ETC for just UO2 with the crescent bubble for
    A rectangular additive particle is more beneﬁcial to the ETC of                        each structure in these series. These ETC values are shown as blue
the composite then a spherical additive particle with the same vol-                        and orange dashed lines in Fig. 3(c). It appears that the full system
ume fraction, reaching almost a 2 W/mK higher ETC. Bubbles on                              data points and the crescent Xe gas line are approaching the same
top of the rectangular additive particle have little impact on the                         values for each contact angle, making the crescent shape the lower
ETC, as shown in Fig. 3(b). However, bubbles on the side of the                            bound of the ETC of the full system with the spherical particle and
rectangular particle in the direction of heat ﬂow have a large im-                         the bubble.
pact. A bubble with a contact angle of 90◦ and a volume fraction of                            These results indicate that it is possible for bubbles to make a
0.02 lowered the ETC by 2 W/mK for the rectangular particle but                            composite fuel with a high thermal conductivity additive have an
only by 1 W/mK for a spherical particle.                                                   effective thermal conductivity that is worse then pure UO2 fuel,
    As mentioned above for the spherical particle, a bubble with a                         if the bubble has a shape that is exceptionally good at disrupting
volume fraction of 0.04 and a contact angle of 35◦ had the same                            heat ﬂow. However, this situation also requires that the bubble be
ETC as UO2 with the same bubble fraction with no additive, indi-                           centered on the additive particle in the direction of heat ﬂow. In
cating that it is possible for bubbles to entirely remove the ther-                        a real system, it is unlikely that every bubble would adopt such a
mal beneﬁts of the additive. To investigate this in more detail, ad-                       position, and that a higher ETC would be expected.
ditional microstructures were created with higher bubble volume                                This investigation reveals a few features that are signiﬁcant in
fractions with 35◦ and 45◦ contact angles. The ETC calculations for                        determining the impact of bubbles on the ETC in a composite fuel.
these points are shown Fig. 3(c).                                                          First, the ability of the bubble to coat the surface of the additive
    These 35◦ and 45◦ contact angle bubbles cause the ETC of the                           particle is a signiﬁcant contributor to the ETC reduction. Second,
composite to drop below the ETC for UO2 with a spherical bubble                            the bubble placement on the additive particle surface with respect
at bubble fractions larger than 0.04 and 0.07, respectively. A likely                      to heat ﬂow also strongly impacts the ETC of the composite. Third,
cause for this is the gas bubble in the system with an additive par-                       the shape of the additive particle can impact how resistant the


                                                                                       4
F.W. Hilty, D.-U. Kim and M.R. Tonks                                                                                             Journal of Nuclear Materials 546 (2021) 152779




Fig. 4. ETC versus the three metrics. (a) shows schematics of the three metrics used in (c–e), left to right, respectively. (b) repeats the ETC versus bubble volume fraction,
for comparison. (c) shows the ETC versus surface coverage, which fails to represent different bubble positions, as seen by the 90◦ rotation data points. (c) shows ETC versus
the cross-sectional coverage, which better accounts for the position of the bubble but there is still signiﬁcant spread in the data. (d) shows ETC versus the screening fraction,
in which a clear trend is visible.



ETC of the composite is to the impact of bubbles. Lastly, under ex-                        This metric slightly improves the trend for the different contact an-
treme conditions, it is possible for a bubble to reduce the ETC of                         gles; however, it completely fails to account for the bubble position
the composite to equal to, or even worse than, pure UO2 fuel with                          on the surface of the additive particle. This failure is most promi-
the same volume fraction of ﬁssion gas bubbles.                                            nent in the data points for the rotated microstructures.
                                                                                               The cross-sectional coverage fraction is deﬁned as the portion
4. Coverage metrics                                                                        of the cross section area of the additive particle in the direction
                                                                                           of heat ﬂow that has bubble in line with it, as shown in Fig. 4(a).
    It is clear from the results in Section 3 that the bubble volume                       This metric captures the bubble placement on the surface; when
fraction does not fully represent the impact of bubbles on the ETC                         the bubble is positioned closer to the top and bottom of the addi-
of composite fuel, as shown again in Fig. 4(b). In this Section, we                        tive particle it will impact less of the cross section of the additive
present our efforts to determine a better metric that describes the                        particle. The ETC versus the cross-sectional coverage is shown in
relationship between the bubble morphology and the ETC of the                              Fig. 4(d), and it shows great improvement over the surface cov-
composite fuel using the observations made in the previous sec-                            erage fraction. The 45◦ and 90◦ rotated microstructures are now
tion. Three metrics were investigated: the surface coverage frac-                          grouped with the other microstructures with a similar ETC. In
tion, the cross-sectional coverage fraction, and the screening frac-                       addition, the overall trend between the rectangular particle and
tion. We deﬁne these three metrics and show their capability to                            spherical particle microstructures are beginning to adopt the same
represent the impact of the bubble morphology, below.                                      shape. However, there is still signiﬁcant spread for the spherical
    The surface coverage fraction is the fraction of the additive’s                        particle data set with a mid range of cross-sectional coverage.
surface that is in contact with the bubble, as demonstrated in                                 The screening fraction is deﬁned as the fraction of additive vol-
Fig. 4(a). It captures the spread of the bubble over the additive sur-                     ume that has bubble along the direction of heat ﬂow divided by
face. The ETC versus the surface coverage for all microstructures                          the total volume of additive, as shown in Fig. 4(a). This metric rep-
with bubble volume fractions of 0.04 or less is shown in Fig. 4(c).                        resents the idea that a bubble effectively eliminates the beneﬁt of

                                                                                       5
F.W. Hilty, D.-U. Kim and M.R. Tonks                                                                         Journal of Nuclear Materials 546 (2021) 152779


all additive in line with it in the direction of heat transport. The         hand side of Eq. (1) (see Fig. 5(a)). This normalization process re-
ETC versus the screening fraction is shown in Fig. 4(e), and with            veals that while the general trends for both spherical and rectan-
it the relationship between the bubble morphology and ETC be-                gular particles are similar, they are not identical. For a spherical
comes a well deﬁned trend. The screening fraction collapses the              particle (aspect ratio 1:1), a = 1. To ﬁt values of a for other as-
spherical additive data into an almost uniﬁed curve, including the           pect ratios, a series of microstructures was created using rectan-
45◦ and 90◦ rotated microstructures. The few microstructures that            gular additive particles with aspect ratios ranging from 4:1 to 1:4
deviate slightly from the overall trend have extreme contact angles          with constant additive volume fraction and enough bubble volume
or an unusual morphology such as the two bubbles microstructure.             so that S = 1 (see Fig. 5(c)). For each aspect ratio, two microstruc-
Due to its excellent performance, we used the screening fraction as          tures were created with different volume fractions of constituents.
our coverage metric to develop an analytical model of the ETC of a           The value of the coeﬃcient a for each microstructure was found
composite with ﬁssion gas in the next section.                               such that the model’s predicted ETC matched those calculated us-
                                                                             ing the AEH method. The resulting ﬁt to relate a to the aspect ratio
5. Analytical model                                                          of the additive particle is
                                                                             a = 0.54 − 0.2 ln(R ),                                                    (2)
   We have used what was learned from the simulation results
discussed in Sections 3 and 4 to create a model that predicts the            where R = lwidth
                                                                                        ength o f particl e
                                                                                              o f particle
                                                                                                            with respect to the direction of heat ﬂow.
ETC of a composite microstructure with ﬁssion gas bubbles as a               A plot with the calculated values for a and the ﬁt from Eq. (2) can
function of the cross-sectional coverage. We describe its develop-           be seen in Fig. 5(b).
ment in Section 5.1 and assess its performance in Section 5.2.
                                                                             5.2. Model assessment

5.1. Model development
                                                                                 The model was assessed using four different series of tests.
                                                                             First, its predictions were compared with the data from Fig. 3(a)
    There are three pieces needed to create an analytical model
                                                                             and (b). Note that these data were used to inform the development
to predict the decrease in the effective thermal conductivity of a
                                                                             of the model. Then the model was compared against three mate-
composite fuel due to ﬁssion gas bubbles. The ﬁrst is the ETC of
                                                                             rial systems not used in its development: BeO and UO2 at other
the fresh fuel. This point is the best-case scenario and is what the
                                                                             temperatures, microstructures in which the additive thermal con-
model should predict when the screening fraction, S, is zero. Sec-
                                                                             ductivity was varied but the bulk conductivity was held constant,
ond is an estimate for the worst-case scenario. We propose that
                                                                             and microstructures in which the bulk thermal conductivity was
this point should be the ETC for a pure UO2 fuel with a volume
                                                                             varied but the additive thermal conductivity was held constant. For
fraction of ﬁssion gas bubbles of interest, and the model’s predic-
                                                                             all of these tests the microstructures with a single spherical addi-
tion when S is one. Lastly, the rate at which the ETC will decrease
                                                                             tive particle with a bubble centered on the right side, see the left
from the two end points needs to be established. From the trend
                                                                             of Fig. 1, were used.
shown in Section 4 when using the screening fraction descriptor,
                                                                                 Fig. 6 (a) shows how the predictions from Eq. (1) compare to
the ETC of the fuel decreases following an S2 trend for both addi-
                                                                             the AEH calculations of the composite fuels from Section 2.1. The
tive particle shapes.
                                                                             model performs reasonably well for both the spherical and rectan-
    Our model then can reduce the ETC of the fresh fuel by an
                                                                             gular particle microstructures. It does not account for all the vari-
amount proportional to difference in thermal conductivities in the
                                                                             ations in the AEH calculations, but it does provide a good approx-
best- and worst- case scenarios scaled by the screening fraction.
                                                                             imation for what ETC one could expect for a fuel as it approaches
Using this approach, we propose the following analytical model to
                                                                             a screening fraction of one.
describe the relationship between the screening fraction and ETC
                                                                                 The performance of the model for microstructures at various
of a composite fuel with ﬁssion gas bubbles:
                                                                             temperatures are shown in Fig. 6(b). The values of 30 0, 90 0, and
                            
ke f f − k0    k1                                                            1500 K were chosen for the temperature to span a range from
            =a    − 1 S2 ,                                        (1)        room to reactor operating temperatures. The thermal conductivity
     k0        k0
                                                                             of UO2 , BeO, and Xe gas at these temperatures was obtained using
where ke f f is the ETC of the composite, a is a ﬁtting parameter dis-       the models of Fink [31], Slack [32], and Assael [33], respectively. As
cussed in the next paragraph, and S is the screening fraction. k0 is         the temperature increases, the thermal conductivity of each phase
the ETC of the fresh composite fuel without any gas bubbles, and             decreases, resulting in a lowering and ﬂattening of the ETC of the
is the model’s value at S = 0. k1 is the ETC of UO2 without addi-            composite. The model captures this effect and is equally valid for
tive with the largest bubble fraction of interest, and is the model’s        each temperature tested.
value at S = 1. Ideally, one would obtain k0 from experiments and                The performance of the model using UO2 and Xe gas thermal
could estimate k1 from any of the available models for the ETC               conductivities at 300 K and the additive thermal conductivity set
of irradiated UO2 fuel [38–40]. It should be noted that any uncer-           to 50, 500, and 1000 W/mK is shown in Fig. 6(c). There was only a
tainty in the method used to obtain k0 and k1 will directly prop-            slight deviation between the ETCs with additive thermal conductiv-
agate into this model because the beginning and end points for               ities of 500 and 1000 W/mK and the analytical model matched ex-
the model are set by these parameters. It is also important to note          tremely well with the AEH calculations. The 50 W/mK results were
that this model assumes that the ETC of the composite fuel will              also well represented by the analytical model. However, the AEH
not drop below the ETC of UO2 without additive, even though we               calculation for the structure with the highest screening fraction
have shown that this can occur. We make this assumption due to               and bubble volume fraction is lower than the k1 line. This is due to
the fact that it only occurred for bubbles with low contact angles           the shape of the bubble (see Fig. 3(d)) as discussed earlier. What is
that were directly in-line with the direction of heat ﬂow, which is          important to note is that only the 50 W/mK data crossed the line,
unlikely.                                                                    indicating that the conditions required to achieve a lower ther-
    The coeﬃcient a is a ﬁtting parameter that captures the effect           mal conductivity than a pure UO2 fuel with Xe gas are dependent
of the additive particle aspect ratio in the direction of heat trans-        upon the additive thermal conductivity. For this data set, the sys-
port. The need for this parameter can be observed by normalizing             tem with and without additive meet at approximately 0.035 bub-
the ETC of each microstructure using the expression on the right             ble volume fraction. For the high volume fraction data set shown

                                                                         6
F.W. Hilty, D.-U. Kim and M.R. Tonks                                                                                             Journal of Nuclear Materials 546 (2021) 152779


earlier, which had an additive thermal conductivity of 370 W/mK,                           this work, but could be of signiﬁcant value to the nuclear research
this happened at 0.04 bubble volume fraction. The higher addi-                             community. We observed that the thermal conductivity of the ad-
tive thermal conductivity tests likewise reached this threshold at                         ditive impacted the point at which this transition occurred. Addi-
approximately 0.04 bubble volume fraction. This presents a pos-                            tionally, it is likely that the relative volume fraction of the additive
sible limit to the applicability of this model at a bubble vol-                            and bubbles impacts this critical point, as the screening fraction
ume fraction of 0.04 when the additive thermal conductivity is                             is somewhat dependent upon these two parameters. The contact
two orders of magnitude larger then the bulk phase, and decreas-                           angle also plays an important role in the critical point, since the
ing as the thermal conductivity of the two phases approach one                             contact angle strongly impacts the shape of the ﬁssion gas bubble.
another.                                                                                   This can be seen in Fig. 3(c), where the volume fraction at which
    The performance of the model using BeO and Xe gas thermal                              the composite fuel becomes worse than pure UO2 fuel moved from
conductivities at 300 K and the bulk conductivity of 2.52, 4.24, and                       a value of 0.04 to 0.07 when the contact angle changed from 35◦
12.24 W/mK are shown in Fig. 6(d). Changing the bulk phase ther-                           to 45◦ . At this time, we leave further investigation of this transi-
mal conductivity has a strong impact on the ETC calculated with                            tion to future work. From these results, it appears that composite
AEH. This is expected since, by deﬁnition, the bulk phase makes up                         fuels with small ﬁssion gas contact angles may only improve fuel
the majority of the composite’s volume. The trend observed from                            performance at lower burn-up.
this test mirrors that seen when the temperature was changed.                                  The simulations used in this work were 2D, to reduce com-
This is because in that case the bulk phase conductivity was also                          putational expense, and it is well established that 2D simulations
changing, showing it to be the dominant phase in determining the                           tend to over estimate the impact of a secondary phase [41]. How-
ETC of the composite. As with the previous cases, the analytical                           ever, the primary impact of the ﬁssion gas bubble is to inhibit heat
model is in strong agreement with the AEH calculations and ap-                             transport through the additive and this effect is likely to be sim-
pears to capture the changes to the ETC based on the material dif-                         ilar in 3D. Although there are additional paths for heat transport
ferences quite well.                                                                       in a 3D composite when compared to 2D, if the ﬁssion gas is fully
                                                                                           screening the additive then those additional paths will not be more
6. Discussion                                                                              advantageous than in a pure UO2 fuel. It is possible that rate at
                                                                                           which the ETC of the composite decreases may be different. There-
    In this work, we have used 2D simulations of composite fuel                            fore, future work should carry out 3D simulations to see if similar
domains containing a single additive particle to investigate the im-                       trends between the ETC and screening fraction are observed. The
pact of ﬁssion gas bubbles on the ETC of composite fuels during                            analytical model presented here also needs to be compared against
reactor operation. The results indicated that as ﬁssion gas bubbles                        3D simulation results.
segregate to the additive interface, they can eliminate any beneﬁt                             We also simpliﬁed this study by using microstructures with
of the additive and even transition to having lower ETC than a mi-                         a single additive particle situated in a matrix of UO2 and we
crostructure without additive but the same bubble volume fraction.                         did not vary the size of the particle or the size of the domain
The point at which this transition occurs was not well deﬁned in                           (which would vary the effective spacing between particles due to




Fig. 5. Determination of the ﬁtting parameter a. (a) shows the normalized ETC, using the expression on the right hand side of Eq. (1), for each calculated structure, colored
to indicate additive particle shape. While the general trend of for the two particle shapes is similar they do not match perfectly, indicating the need for the shape dependent
ﬁtting parameter. (b) shows the value of a versus the aspect ratio calculated using AEH and determined using the ﬁt. The blue dots are the values of a needed to make the
model match the AEH results. There are two sets of microstructures included, both transition a particle from an aspect ratio of 4:1 to 1:4. One set has half of the additive
volume fraction of the ﬁrst. The data sets with different volume fractions are nearly identical, with the set having less additive appearing just slightly lower than the other.
(c) shows examples of rectangular additive particle microstructure with varying aspect ratios. (For interpretation of the references to color in this ﬁgure legend, the reader
is referred to the web version of this article.)


                                                                                       7
F.W. Hilty, D.-U. Kim and M.R. Tonks                                                                                          Journal of Nuclear Materials 546 (2021) 152779




Fig. 6. Plots showing the analytical model’s performance when applied to our simulated microstructures, illustrated in Fig. 1. (a) compares the model predictions with the
ETC values from the top row of Fig. 3; they use the thermal conductivity of UO2 , BeO, and Xe gas at 300 K. In (b) the temperature of the system is changed, resulting
in different thermal conductivities for all phases. In (c) only the additive phase thermal conductivity is changed. In (d) only the bulk thermal conductivity is changed. The
points are calculations for the simulated microstructures, solid lines are the analytical model, and dashed lines are calculations of the bulk phase and 0.04 volume fraction
Xe gas, but no additive. The coloring indicates the value for the property being changed.


the boundary conditions). However, in a real system there would                          work is not applicable to continuous structures and the impact of
be many particles, with a potentially wide range of shapes, sizes,                       bubbles on their ETC should be investigated.
and spacing between particles. With a greater number of particles
the probability of clusters forming could become signiﬁcant. These                       7. Conclusion
clusters could push the system to a more heterogeneous state and
add uncertainty to the trends observed. As bubbles segregate to                              In this study we investigated the impact of ﬁssion gas bubbles
the various particles, some bubbles would be aligned with the                            on UO2 fuels with dispersed high thermal conductivity additives.
direction of heat transport while others would not. Additionally,                        Various microstructures were created, each with a single additive
there would be grain boundaries, creating other possible interfaces                      particle interacting with bubbles. The bubble contact angle and
for the Xe gas to segregate to and form bubbles. Thus, there would                       volume fraction were varied and the effective thermal conductivity
be a range of screening fractions for all the various particles. We                      was calculated with the AEH method using MOOSE. The screen-
believe that measurements of an average screening fraction from                          ing fraction of the gas phase on the additive was determined to be
an experimental micrograph or from simulations with many parti-                          the best metric to predict the ETC of the composite. Then a model,
cles would still result in a strong correlation with the ETC and the                     Eq. (1), was proposed that uses the screening fraction, the thermal
bubble effect could still be reasonably approximated using our an-                       conductivity of the fresh composite fuel, the thermal conductivity
alytical model. However, this should be investigated. In addition, if                    of UO2 with a large bubble volume fraction, and a ﬁtting parame-
our model were to be implemented in a fuel performance code to                           ter a that accounts for the aspect ratio of the additive particle. The
describe the impact of ﬁssion gas on composite fuel ETC, the ﬁs-                         model’s predictions for the ETC of the composites closely match
sion gas release model would have to be modiﬁed to evolve the                            the AEH calculations, though its applicability to more complicated
average screening fraction with time.                                                    and 3D structures remains to be determined.
    Finally, we only considered composite fuels with discrete ad-                            A signiﬁcant ﬁnding of this work was the potential for compos-
ditive particles dispersed throughout the fuel. However, the struc-                      ite UO2 fuels with a high thermal conductivity additive to elimi-
ture of an additive could alternatively have a continuous character,                     nate the beneﬁt of the additive on the ETC and to even result in
rather than dispersed, with the additive phase forming connected                         a lower thermal conductivity then UO2 with ﬁssion gas bubbles
structures along grain boundaries. These structures could be more                        but no additive. This effect is related to the shape of the bubbles.
resistant to the effects of bubbles since they have the potential to                     If the bubble is distorted from a spherical shape to be elongated
channel heat around the bubble. Therefore, the results from this                         perpendicular to the direction of heat ﬂow due to the presence of

                                                                                     8
F.W. Hilty, D.-U. Kim and M.R. Tonks                                                                                                   Journal of Nuclear Materials 546 (2021) 152779


the additive, then it can act as a signiﬁcant barrier to heat ﬂow.                              [14] F. Badry, R. Brito, M.G. Abdoelatef, S. McDeavitt, K. Ahmed, An Experi-
The transition at which this occurs is not deﬁned in this work, but                                  mentally validated mesoscale model of thermal conductivity of a UO2 and
                                                                                                     BeO composite nuclear Fuel, JOM 71 (12) (2019) 4829–4838, doi:10.1007/
it was shown that the transition point is impacted by the ther-                                      s11837- 019- 03831- y.
mal conductivity of the additive phase and contact angle of the gas                             [15] F. Hilty, M.R. Tonks, Development and application of a microstructure depen-
bubble on the additive surface. This result indicates that composite                                 dent thermal resistor model for UO2 reactor fuel with high thermal conductiv-
                                                                                                     ity additives, J. Nucl. Mater. 540 (2020) 10.1016/j.jnucmat.2020.152334.
fuels with high thermal conductivity additives may only give fuel                               [16] S.W. Lee, H.T. Kim, I.C. Bang, Performance evaluation of UO2 /graphene compos-
performance beneﬁts at lower burn-up.                                                                ite fuel and SiC cladding during LBLOCA using MARS-KS, Nucl. Eng. Des. 257
                                                                                                     (2013) 139–145, doi:10.1016/j.nucengdes.2013.01.012.
Data availability                                                                               [17] D. Chandramouli, S.T. Revankar, Development of thermal models and analysis
                                                                                                     of UO2 -BeO fuel during a loss of coolant accident, Int. J. Nucl. Energy 5 (2014)
                                                                                                     e751070.
    Data will be provided on request.                                                           [18] R. Liu, W. Zhou, P. Shen, A. Prudil, P.K. Chan, Fully coupled multiphysics mod-
                                                                                                     eling of enhanced thermal conductivity UO2 and BeO fuel performance in a
                                                                                                     light water reactor, Nucl. Eng. Des. 295 (2015) 511–523.
Declaration of Competing Interest
                                                                                                [19] R. Liu, W. Zhou, A. Prudil, P.K. Chan, Multiphysics modeling of UO2 -SiC com-
                                                                                                     posite fuel performance with enhanced thermal and mechanical properties,
    Authors declare that they have no conﬂict of interest.                                           Appl. Therm. Eng. 107 (2016) 86–100, doi:10.1016/j.applthermaleng.2016.06.
                                                                                                     173.
                                                                                                [20] R. Liu, W. Zhou, Multiphysics modeling of novel UO2 -BeO sandwich fuel per-
CRediT authorship contribution statement                                                             formance in a light water reactor, Ann. Nucl. Energy 109 (2017) 298–309.
                                                                                                [21] W. Zhou, W. Zhou, Thermophysical and Mechanical Analyses of UO2 -36.4vol.%
    Floyd W. Hilty: Methodology, Software, Formal analysis, Inves-                                   BeO Fuel Pellets with Zircaloy, SiC, and FeCrAl Claddings, Metals 8 (1) (2018)
                                                                                                     65, doi:10.3390/met8010065. Number: 1 Publisher: Multidisciplinary Digital
tigation, Writing - original draft. Dong-Uk Kim: Methodology, Soft-                                  Publishing Institute
ware. Michael R. Tonks: Conceptualization, Writing - review &                                   [22] F. Cappia, J.M. Harp, K. McCoy, Post-irradiation examinations of UO2 compos-
editing, Supervision, Project administration, Funding acquisition.                                   ites as part of the accident tolerant fuels campaign, J. Nucl. Mater. 517 (2019)
                                                                                                     97–105.
                                                                                                [23] X.-M. Bai, M.R. Tonks, Y. Zhang, J.D. Hales, Multiscale modeling of thermal con-
Acknowledgments                                                                                      ductivity of high burnup structures in UO2 fuels, J. Nucl. Mater. 470 (2016)
                                                                                                     208–215, doi:10.1016/j.jnucmat.2015.12.028.
    This work was funded by the US DOE Nuclear Energy Univer-                                   [24] C. Walker, D. Staicu, M. Sheindlin, D. Papaioannou, W. Goll, F. Sontheimer, On
                                                                                                     the thermal conductivity of UO2 nuclear fuel at a high burn-up of around
sity Programs under IRP 15-8843, “Development of Accident Toler-                                     100MWd/kgHM, J. Nucl. Mater. 350 (1) (2006) 19–39, doi:10.1016/j.jnucmat.
ant Fuel Options For Near Term Applications”. The authors would                                      20 05.11.0 07.
like to thank Jacopo Buongiorno and Kumar Sridharan from the                                    [25] L.K. Aagesen, Y. Gao, D. Schwen, K. Ahmed, Grand-potential-based phase-ﬁeld
                                                                                                     model for multiple phases, grains, and chemical components, Phys. Rev. E 98
Massachusetts Institute of Technology for their leadership of the                                    (2018) 023309, doi:10.1103/PhysRevE.98.023309.
project.                                                                                        [26] D. Gaston, C. Newman, G. Hansen, D. Lebrun-Grandie, MOOSE: a parallel com-
                                                                                                     putational framework for coupled systems of nonlinear equations, Nucl. Eng.
References                                                                                           Des. 239 (10) (2009) 1768–1778.
                                                                                                [27] M.R. Tonks, D. Gaston, P.C. Millett, D. Andrs, P. Talbot, An object-oriented ﬁnite
 [1] S. Bragg-Sitton, Development of advanced accident-tolerant fuels for commer-                    element framework for multiphysics phase ﬁeld simulations, Comput. Mater.
     cial LWRs, Nucl. News 57 (2014) 83–91.                                                          Sci. 51 (1) (2012) 20–29.
 [2] W. Zhou, W. Zhou, Enhanced thermal conductivity accident tolerant fuels                    [28] J. Turnbull, The effect of grain size on the swelling and gas release properties
     for improved reactor safety—A comprehensive review, Ann. Nucl. Energy 119                       of UO2 during irradiation, J. Nucl. Mater. 50 (1) (1974) 62–68.
     (2018) 66–86.                                                                              [29] S. Kashibe, K. Une, K. Nogita, Formation and growth of intragranular ﬁssion gas
 [3] S. ishimoto, M. Hirai, K. Ito, Y. Korei, Thermal Conductivity of UO2 -BeO Pellet, J.            bubbles in UO2 fuels with burnup of 6–83GWd/t, J. Nucl. Mater. 206 (1) (1993)
     Nucl. Sci. Technol. 33 (2) (1996) 134–140, doi:10.1080/18811248.1996.9731875.                   22–34.
 [4] S. Yeo, R. Baney, G. Subhash, J. Tulenko, The inﬂuence of SiC particle size and            [30] M. Tonks, D. Andersson, R. Devanathan, R. Dubourg, A. El-Azab, M. Freyss,
     volume fraction on the thermal conductivity of spark plasma sintered UO2 and                    F. Iglesias, K. Kulacsy, G. Pastore, S.R. Phillpot, et al., Unit mechanisms of ﬁs-
     SiC composites, J. Nucl. Mater. 442 (1) (2013) 245–252, doi:10.1016/j.jnucmat.                  sion gas release: current understanding and future needs, J. Nucl. Mater. 504
     2013.09.003.                                                                                    (2018) 300–317.
 [5] Z. Chen, G. Subhash, J.S. Tulenko, Raman spectroscopic investigation of graphi-            [31] J.K. Fink, Thermophysical properties of uranium dioxide, J. Nucl. Mater. 279
     tization of diamond during spark plasma sintering of UO2 -diamond composite                     (20 0 0) 1–18.
     nuclear fuel, J. Nucl. Mater. 475 (2016) 1–5.                                              [32] G.A. Slack, S.B. Austerman, Thermal conductivity of BeO single crystals, J. Appl.
 [6] S.C. Finkeldei, J.O. Kiggans, R.D. Hunt, A.T. Nelson, K.A. Terrani, Fabrication of              Phys. 42 (1971) 4713–4717.
     UO2 -Mo composite fuel with enhanced thermal conductivity from sol-gel feed-               [33] M. Assael, A. Kalyva, S. Monogenidou, M. Huber, R. Perkins, D. Friend, E. May,
     stock, J. Nucl. Mater. 520 (2019) 56–64, doi:10.1016/j.jnucmat.2019.04.011.                     Reference values and reference correlations for the thermal conductivity and
 [7] J.H. Yang, K.W. Song, K.S. Kim, Y.H. Jung, A fabrication technique for a UO2 pel-               viscosity of ﬂuids, J. Phys. Chem. Ref. Data 47 (2018) 021501, doi:10.1063/1.
     let consisting of UO2 grains and a continuous W channel on the grain bound-                     5036625.
     ary, J. Nucl. Mater. 353 (3) (2006) 202–208, doi:10.1016/j.jnucmat.2006.01.019.            [34] P.W. Chung, K.K. Tamma, R.R. Namburu, Asymptotic expansion homogenization
 [8] A. Cartas, H. Wang, G. Subhash, R. Baney, J. Tulenko, Inﬂuence of Carbon                        for heterogeneous media: computational issues and applications, Compos. Part
     Nanotube Dispersion in UO2 and carbon nanotube ceramic matrix compos-                           A 32 (9) (2001) 1291–1301, doi:10.1016/S1359-835X(01)0 010 0-2.
     ites utilizing spark plasma sintering, Nucl. Technol. 189 (3) (2015) 258–267,              [35] J. Hales, M. Tonks, K. Chockalingam, et al., Asymptotic expansion homoge-
     doi:10.13182/NT14-7.                                                                            nization for multiscale nuclear fuel analysis, Comput. Mater. Sci. 99 (2015)
 [9] T. Yao, G. Xin, S.M. Scott, B. Gong, J. Lian, Thermally-conductive and                          290–297.
     mechanically-robust graphene nanoplatelet reinforced UO2 composite nuclear                 [36] L. Liang, Y.S. Kim, Z.-G. Mei, L.K. Aagesen, A.M. Yacout, Fission gas bubbles and
     fuels, Sci. Rep. 8 (1) (2018) 2987, doi:10.1038/s41598- 018- 21034- 4. Number: 1                recrystallization-induced degradation of the effective thermal conductivity in
     Publisher: Nature Publishing Group                                                              U-7Mo fuels, J. Nucl. Mater. 511 (2018) 438–445.
[10] B.J. Jaques, J. Watkins, J.R. Croteau, G.A. Alanko, B. Tyburska-Pschel, M. Meyer,          [37] M.R. Tonks, C. Bhave, X. Wu, Y. Zhang, Uncertainty quantiﬁcation of mesoscale
     P. Xu, E.J. Lahoda, D.P. Butt, Synthesis and sintering of UN-UO2 fuel composites,               models of porous uranium dioxide, in: Uncertainty Quantiﬁcation in Multiscale
     J. Nucl. Mater. 466 (2015) 745–754, doi:10.1016/j.jnucmat.2015.06.029.                          Materials Modeling, Elsevier, 2020, pp. 329–354.
[11] B. Gong, T. Yao, P. Lei, L. Cai, K.E. Metzger, E.J. Lahoda, F.A. Boylan, A. Mo-            [38] P. Lucuta, H. Matzke, I. Hastings, A pragmatic approach to modelling ther-
     hamad, J. Harp, A.T. Nelson, J. Lian, U3 Si2 and UO2 composites densiﬁed by                     mal conductivity of irradiated UO2 fuel: Review and recommendations, J. Nucl.
     spark plasma sintering for accident-tolerant fuels, J. Nucl. Mater. 534 (2020)                  Mater. 232 (2) (1996) 166–180, doi:10.1016/S0022-3115(96)00404-7.
     152147, doi:10.1016/j.jnucmat.2020.152147.                                                 [39] C. Ronchi, M. Sheindlin, D. Staicu, M. Kinoshita, Effect of burn-up on the ther-
[12] W. Zhou, R. Liu, S.T. Revankar, Fabrication methods and thermal hydraulics                      mal conductivity of uranium dioxide up to 10 0.0 0 0MWdt−1 , J. Nucl. Mater. 327
     analysis of enhanced thermal conductivity UO2 and BeO fuel in light water                       (1) (2004) 58–76, doi:10.1016/j.jnucmat.2004.01.018.
     reactors, Ann. Nucl. Energy 81 (2015) 240–248, doi:10.1016/j.anucene.2015.02.              [40] M.R. Tonks, X.-Y. Liu, D. Andersson, D. Perez, A. Chernatynskiy, G. Pastore,
     044.                                                                                            C.R. Stanek, R. Williamson, Development of a multiscale thermal conductivity
[13] W. Zhou, S.T. Revankar, R. Liu, M.S. Beni, Microstructure-based thermal con-                    model for ﬁssion gas in UO2 , J. Nucl. Mater. 469 (2016) 89–98.
     ductivity and thermal behavior modeling of nuclear fuel UO2 -BeO, Heat Transf.             [41] M.C. Teague, B.S. Fromm, M.R. Tonks, D.P. Field, Using coupled mesoscale ex-
     Eng. 39 (9) (2018) 760–774, doi:10.1080/01457632.2017.1341216. Taylor & Fran-                   periments and simulations to investigate high burn-up oxide fuel thermal con-
     cis                                                                                             ductivity, JOM 66 (12) (2014) 2569–2577.


                                                                                            9
