# A kinetic rate theory modelling of fission gas release and fuel swelling for UN fuels

---

                                                                 Journal of Nuclear Materials 556 (2021) 153188



                                                                 Contents lists available at ScienceDirect


                                                            Journal of Nuclear Materials
                                                          journal homepage: www.elsevier.com/locate/jnucmat




A kinetic rate theory modelling of ﬁssion gas release and fuel swelling
for UN fuels
Zhengyu Qian a, Wenbo Liu a, Rui Yu b, Yujie Tao b, Di Yun a,c,∗, Long Gu b,d,e,∗
a
  School of Nuclear Science and Technology, Xi’an Jiaotong University, Xi’an 710049, China
b
  Institute of Modern Physics, Chinese Academy of Sciences, Lan Zhou 730000, China
c
  State Key Laboratory of Multi-phase Flow, Xi’an Jiaotong University, Xi’an 710049, China
d
  University of Chinese Academy of Sciences, Beijing 100049, China
e
  School of Nuclear Science and Technology, Lanzhou University, Lanzhou 730000, China




a r t i c l e            i n f o                          a b s t r a c t

Article history:                                          Fission gas behavior and fuel swelling have always been an important issue for nitride fuels. In this pa-
Received 5 November 2020                                  per, a mechanistic ﬁssion gas behavior model of nitride fuels has been established using the kinetic rate
Revised 5 June 2021
                                                          theory, based on the fuel temperature distribution input provided by a ﬁnite element computational plat-
Accepted 6 July 2021
                                                          form. The ﬁssion gas release and fuel swelling of the nitride fuels were simulated in details and the sim-
Available online 10 July 2021
                                                          ulation results were compared with experimental data from open literature. Using the established model,
Keywords:                                                 previous diffusion coeﬃcients of Xe gas in nitride fuels derived by earlier works were analyzed, and a
UN fuels                                                  new diffusion coeﬃcient suitable for simulation of nitride fuels was proposed. A parameter sensitivity
Fission gas release                                       analysis was carried out for the two important parameters in the rate theory simulation of ﬁssion gas
Fuel swelling                                             behavior, the nucleation factor and the resolution coeﬃcient. Suitable values for both parameters for ni-
Kinetic rate theory                                       tride fuels were determined, and their inﬂuence on ﬁssion gas behavior and fuel swelling were assessed.
                                                          In addition, a bimodal distribution for bubble size was observed and the underlying physics driving factor
                                                          was determined to be the gas bubble resolution.
                                                                                                                            © 2021 Elsevier B.V. All rights reserved.




1. Introduction                                                                                  At present, for the simulation of the ﬁssion gas behavior and
                                                                                             fuel swelling of nitride fuels the researchers largely relied on em-
    Nitride fuel has the characteristics of high uranium atom den-                           pirical models such as the Storms’ relationship [6], due to the
sity, good thermal conductivity and high melting point. It has a                             lack of open literature information on detailed microstructures and
wide range of use in space reactors [1] and fast reactors [2], and                           physics mechanisms. However, the empirical relationship is highly
is one of the options for Accident Tolerant Fuels (ATF) [3]. How-                            dependent on experimental data and is applicable only to situa-
ever, due to the ﬁssion reaction, a large amount of ﬁssion products                          tions that fall into the regime of the conditions of the experiment
will be produced. Among all ﬁssion products, noble gas, because of                           from which the model was derived. If the experimental conditions
their very low solubility in the fuel matrix, will exist in the form of                      start to deviate from this regime, the corresponding empirical rela-
gas bubbles in the fuel matrix [4]. Under certain conditions, these                          tionship may not be useful. Therefore, it is necessary to develop a
gas bubbles coalesce and grow in size, and the resulting large bub-                          mechanistic model that can reasonably capture the ﬁssion gas be-
bles will increase the fuel swelling [5]. At the same time, gas atoms                        havior of nitride fuels. However, there are few mechanistic models
can diffuse to the grain boundary, gather at the grain boundary                              for the ﬁssion gas behavior of nitride fuels. Feng [7] established a
and form interconnected tunnels and release the gas to the fuel                              mechanistic model for simulating the ﬁssion gas release and fuel
plenum. The released ﬁssion gas will affect the cladding internal                            swelling of nitride fuels, which account for the ﬁssion gas behav-
pressure and thermal conductivity of the fuel cladding gap [4].                              ior and fuel swelling of nitride fuels under multiple experimental
Therefore, to achieve an understanding of ﬁssion gas behavior and                            conditions. But the model is relatively simple, an average bubble
to be able to predict ﬁssion gas behavior in nuclear fuels is neces-                         size was used to represent the detailed bubble size distribution,
sary.                                                                                        and the resolution constant is much higher than that usually used
                                                                                             under other conditions [8-11]. Therefore, there is a space for fur-
                                                                                             ther improvement and further veriﬁcations are needed as well.
    ∗
        Corresponding author.
        E-mail address: diyun1979@xjtu.edu.cn (D. Yun).



https://doi.org/10.1016/j.jnucmat.2021.153188
0022-3115/© 2021 Elsevier B.V. All rights reserved.
Z. Qian, W. Liu, R. Yu et al.                                                                                       Journal of Nuclear Materials 556 (2021) 153188


                                                                             small-size bubbles and large-size bubbles is far more than that of
                                                                             medium-size bubbles, and the size distribution of bubbles has a
                                                                             peak in the small-size and large-size regions, respectively. The bi-
                                                                             modal bubble size distribution is a phenomenon ubiquitous in nu-
                                                                             clear fuels. It exists in many types of fuels, including oxide fuels
                                                                             [25-26] and silicide fuels [27]. Kashibe et al. [26] attribute the bi-
                                                                             modal distribution to either coalescence of small bubbles, or bub-
                                                                             ble growth due to vacancy capture into the bubbles that contain
                                                                             solid ﬁssion products precipitate. Chkuaseli [25] believes that the
                                                                             bimodal bubble size distribution is the result of the combined ef-
                                                                             fect of the surface and volume diffusion mechanisms. He estab-
                                                                             lished a model, and then suppressed the surface diffusion, found
                                                                             that there was no bimodal distribution, and ﬁnally reached the
                                                                             conclusion. However, the calculation results of the model used in
                                                                             this paper show that the resolution has a greater impact on the
                                                                             bimodal distribution, which is far from the conclusion drawn by
                                                                             the above-mentioned researchers, and is worthy of deeper study.
                                                                             In view of the bimodal bubble size distribution in the calculation
                                                                             results of the model, it is proposed that resolution is the main
                                                                             driving factor for the bimodal bubble size distribution.
                Fig. 1. The temperature of JOYO’s case versus burnup.
                                                                             2. Mathematical model

    Using the classical kinetic rate theory to simulate ﬁssion gas               The behaviors of ﬁssion gas are very complicated, mainly in-
behavior started with Booth [12], and then it was further devel-             cluding the nucleation and diffusion of gas atoms in the grain, the
oped by Speight [13], Hayns and Wood [14], Rest [15-17] and oth-             coalescence and growth of intragranular bubbles, the accumulation
ers, and as of now, it has become a mature method in this area.              and growth of bubbles at the grain boundaries, and the release
A crucial step towards developing a good rate theory model is                through interconnected tunnels. The framework of the mechanis-
the determination of key parameters, including the diffusion co-             tic model for nitride fuels is mainly derived from the mechanistic
eﬃcient, the nucleation factor, the resolution constant, etc. Deter-         model, GRASS-SST [28] and FASTGRASS [29], initially developed for
mining these key parameters usually requires a signiﬁcant amount             UO2 fuels by Rest. Based on the FASTGRASS model, the bubble size
of experimental data. The acquisition of the diffusion coeﬃcient             grouping method proposed in the GRASS-SST code was added. A
of gas atoms mainly depends on the experimental measurements.                new method of calculating the resolution constant was added to
The difference in diffusion coeﬃcients under different experimen-            the model as well. At the same time, according to the character-
tal conditions can be very large [7, 18]. The main reason is that the        istics of UN fuel, the process of ﬁssion gas accumulation on the
measurement of gas atom diffusion coeﬃcient is inherently very               grain face was treated in a simpliﬁed manner. The model uses a
complicated. Take ceramic oxide fuel which is somewhat similar               set of coupled nonlinear differential equations to obtain the con-
to nitride fuel into account, the boundary condition of a thin tracer        centration of ﬁssion gas atoms and bubbles at different locations
layer is usually adopted, and sectioning or a nondestructive nuclear         of the fuel (in the bulk, on the grain face, on dislocations, and on
technique is used to determine the diffusion proﬁle following an-            the grain edge) in the following form:
nealing [19]. To obtain reliable results, the sample surface usually         dCα ,i
needs to be ﬂat and representative. Surface preparation is very dif-                = −aα ,iCα2 ,i − bα ,iCα ,i + eα ,i                                       (1)
                                                                              dt
ﬁcult with ceramic fuel due to the hardness and brittleness of the           Where, Cα ,i represents the concentration of the bubble of the
materials and the possibility of concentration gradients by prefer-          group i (when i=1, replace it with the letter g, which represents
ential evaporation of one or more elements [20], which may cause             the concentration of gas atoms); α =f, e represents the concentra-
deviations from the bulk composition. The nucleation factor FN is            tion of the bubbles in grain face and grain edge, respectively (when
used to evaluate the stability of the Xe dimers during the nucle-            there is no value, it represents the concentration of intragranular
ation process, and is the probability that the Xe dimers can exist           bubbles); aα ,i , bα ,i , eα ,i correspond to the rate constants of different
stably after initial formation. In the rate theory simulation under          ﬁssion gas behavior affecting bubble concentration respectively.
different conditions [9-11,21-24], the nucleation factor is between              The model uses the bubble size grouping method assuming that
10−10 -1; similarly, under different conditions, the resolution con-         the ﬁrst group (i=1) contain one gas atom, the number of gas
stant, which characterizes the intensity of the resolution effect, or        atoms contained in each bubble of the group i can be expressed
the ability of a ﬁssion fragment to knock ﬁssion gas atoms from              as:
the bubbles back to the fuel matrix, is also between 10−19 -10−15
                                                                             Ni = mNi−1
cm3 [8-11]. The reason for the large difference is that the fuel type                                                                                         (2)
                                                                             N1 =1
and the simulation conditions selected in the above simulation are
different. Therefore, determination of all the above three parame-           Where, Ni and Ni -1 represents the number of gas atoms contained
ters suitable for the selected simulation conditions for nitride fuels       in the bubbles of the group i and the group i-1; m represents the
is a problem worthy of in-depth consideration. In this work, ki-             multiplier of the number of gas atoms contained in the bubbles of
netic rate theory was used to establish the ﬁssion gas release and           the group i as compared to the group i-1, and this value is usually
fuel swelling model for nitride fuels, and the key parameters such           taken as 2 for ﬁne simulation calculations. For the case that the
as the gas atom diffusion coeﬃcient, nucleation factor and resolu-           number of gas atoms in the bubble Nk is neither equal to Ni nor
tion constant were determined.                                               Ni+1 . In this case, we use a probability Pi such that with probability
    In the process of determination the resolution constant in this          of Pi this bubble belongs to group i, and with the probability (1-Pi)
work, it was found that the bubble distribution calculated by the            that this bubble belongs to the i+1 group, and the Pi is calculated
                                                                                                   N −N
model showed a typical bimodal shape, the number density of                  by equation: Pi = N k −Ni .
                                                                                                     i+1   i


                                                                         2
Z. Qian, W. Liu, R. Yu et al.                                                                                                  Journal of Nuclear Materials 556 (2021) 153188




Fig. 2. Comparison between (a) the ﬁssion gas release, (b) the fuel swelling and (c) the proportion of intragranular gas of the model with different diffusion coeﬃcients
and the experimental value [30]. The left horizontal axis represents the nucleation factor, which changes from 1 to 1e-5, and the right horizontal axis represents resolution
constant, which varies from 1e-19 to 1e-16.



    The Eq. (1) has different form in different position of a grain,                     to grain boundaries; 5. the loss of gas atoms due to grain boundary
for the intragranular gas atoms, the form is:                                            sweeping; 6. the gain of gas atoms due to ﬁssion; 7-9. the increase
                                       
                                       I                                                 of gas atoms caused by resolution from intragranular bubbles and
dCg
dt
    = −16  π FN Rg DgCg 2 − Pg,iCgCi                                                     bubbles in grain face and grain edge.
                          i=2                                                               The fourth term on right hand side of the Eq. (3) refers to the
             6Dg ∂ Cg          V
−Sg bVgCg + dg ∂ r        − 3Cg dgbg + η f +                                  (3)       ﬂux of gas atoms diffused to the grain boundary under the concen-
                             r=dg /2
                                                                                         tration gradient, which can be obtained by solving the concentra-

I                 
                  I                    
                                       I
      biCi Ni +         biC f,i Ni +         biCe,i Ni                                   tion of gas atoms in spherical grain. The speciﬁc solution can refer
i=2               i=2                  i=2                                               to the FASTGRASS Manual [29].
Where, FN is the nucleation factor; Rg is the radius of the intra-                           It is worth noting that the Pi,j , which represents the probability
granular gas atom; Dg is the diffusion coeﬃcient of the intragran-                       of the coalescence between bubbles in group i and group j, has the
ular gas atom; Sgb represents the grain boundary area per unit                           following general form [5]:
volume; Vg represents the velocity of intragranular gas atoms; dg                                                                      2          
                                                                                         Pi, j = 4π Ri + R j        Di + D j + π Ri + R j      V j − Vi                (4)
is the diameter of the grain, 10μm; Vgb is the velocity of grain
boundary; η is the yield of ﬁssion gas, 0.25; f is the ﬁssion rate;                      Where, Ri and Rj are the radius of bubbles in group i and group
I corresponds to the total number of bubble groups.                                      j respectively; Di and Dj are the diffusion coeﬃcient of bubbles in
    The terms on right hand side of the Eq. (3) represent, respec-                       group i and group j respectively; Vi and Vj represent the veloc-
tively, 1. the loss of gas atoms due to nucleation; 2. the loss of gas                   ity of bubbles in group i and group j respectively. The two terms
atoms caused by capture of gas atoms by bubbles; 3. and 4. the                           of Eq. (4) correspond to the bubble coalescence caused by ran-
loss of gas atoms due to biased and random diffusion of gas atoms                        dom (motion in a concentration gradient) and biased (motion in a

                                                                                     3
Z. Qian, W. Liu, R. Yu et al.                                                                                                                 Journal of Nuclear Materials 556 (2021) 153188


                                                                                                                 Table 1
                                                                                                                 Characteristics of fuel sample [30].

                                                                                                                     Parameter

                                                                                                                     Diameter (mm)                    7.43
                                                                                                                     Height (mm)                      8
                                                                                                                     Bulk density (%T.D.)             86.0
                                                                                                                     Fuel stack length (mm)           198.8
                                                                                                                     U235-enrichment (wt%)            19.39
                                                                                                                     Cladding material                15Cr-20Ni stainless steel




                                                                                                     bubbles in group i due to resolution; 7. the gain of gas bubbles
                                                                                                     in group i due to bubble pull-off from a moving grain boundary
                                                                                                     (if the bubbles are bigger than a given critical size, otherwise they
                                                                                                     are equal to zero); 8. the gain of gas bubbles in group 2 due to
                                                                                                     nucleation.
                                                                                                         For the gas atoms and bubbles on the grain face and the grain
                                                                                                     edge, the speciﬁc form of Eq. (1) is arranged in the Appendix to re-
                                                                                                     duce the length of the paper. The fractional ﬁssion gas release and
                                                                                                     the fuel swelling caused by gas atoms are obtained by Eqs. (7) and
                                                                                                     (8), respectively.
Fig. 3. Comparison between the proportion of intragranular gas of the model with                                                                 
                                                                                                     dg                                                                dPI 
                                                                                                            I                                            I                       I
different Grain diameter and the experimental value [30].                                                            V f,i Ng f Ni   PAC f,i Ni
                                                                                                        =                          +              PI +         Ce,i Ni      +  V f,i SNBC f,i Ni
                                                                                                     dt                    dg           t                                dt
                                                                                                           i=1                                           i=1                   i=1
temperature gradient) migration of bubbles, respectively. It should                                                                                                                         (7)
be noted that when i=j, the value of Pi,j needs to be changed to
one-half of the original value, so that each pairwise coalescence is                                 Where, Ngf is the number of grain faces per grain; PA is the in-
counted only once. The bubble radius is determined by the Vander                                     terlinkage fraction of the grain face channel; PI is the grain edge
Waals model. It is solved by two equations,P ( 34 π R2i − BNi ) = Ni KB T ,                          interlinkage fraction; SNB is the area of node boundary/volume of
      2γ                                                                                             the node; the values of PA and PI are taken from the FASTGRASS
P = R + Ph , where B is the Vander Waals constant, 8.5×10−32 m3 ,
        i                                                                                            Manual [29].
γ is surface energy of bubbles, 10 N/m, Ph is the hydrostatic pres-                                      The three term on right hand side of the Eq. (7) represent the
sure, where 107 N/m2 was used, Ni is the number of gas atoms in a                                    gas come from the venting of the grain face gas into intercon-
bubble, KB is Boltzmann constant. We can obtain the bubble radius                                    nected grain edge tunnels, from the venting of grain edge gas bub-
from the above two equations. The diffusion coeﬃcient of the bub-                                    bles through newly interconnected tunnels, and from long-range
                           3a40 Ds                                             3Ds Qs∗ a0 dT
ble is [5] Di =                      , the velocity of the bubble is [5]Vi =                 .       migration of ﬁssion gas bubbles in grain face up the temperature
                           2π R4i                                               kB T 2 Ri dx
                                                                                         4           gradient, respectively.
α 0 is the lattice constant, 0.49nm. Ds = 1.92 × 103 exp(− 4.22RT×10 ),
as can be referred in Weaver’s work [37].                                                                    4       
                                                                                                                     I

    bi represents the intensity of the resolution of bubbles in group                                Vα,i = π             Rα ,i 3Cα ,i                                                     (8)
                                                                                                             3
i, and it takes the form used by Lösönen [8]:                                                                        i=1
                                                                                                    In this way, the mechanistic model of the ﬁssion gas release and
                     3d                    δ
bi = b0                                               f                                  (5)         swelling of UN fuels has been established. The model can calculate
                   3d + Ri               δ + Ri                                                      the ﬁssion gas release and the fuel swelling caused by the retained
Where, b0 is the resolution constant; d is the thickness of the layer                                ﬁssion gas of UN fuels.
on the bubble surface that allows gas atoms to escape, 1nm; Ri is
the bubble radius; δ is the thickness of the layer where the reso-                                   3. Results and discussion
luted gas atoms can return to the bubble through diffusion, 0.4nm;
f is the ﬁssion rate.                                                                                3.1. Settings of input parameter
    For the intragranular bubbles in group i, the Eq. (1) is modiﬁed
to become:                                                                                               There are only few experiments focusing on the fuel swelling
dCi         2
            i/                              
                                            I                                                        and ﬁssion gas behavior of nitride fuels. In order to validate the
dt
    =              Pk,i−kCkCi−k −                 Pi,kCiCk −                                         model, the results of the UN in-reactor irradiation experiment in
            k=1                            k=1
            i=2                                                                                    the experimental reactor JOYO [30] were selected as the object of
                           
SgbViCi + 6dDg i ∂∂Cri                   −                                              (6)         the simulation because the literature of the JOYO experiment pro-
                      r=dg /2                                                                        vided very detailed information regarding ﬁssion gas behavior.
                     3V
3Ci
    V − biCi + dggb C f,i + Ce,i
dg gb
                                (                  )                                                     The characteristics of fuel sample used by the experiment are
    16π FN Rg DgCg 2                                                                                 shown in Table 1 [30]. In order to obtain the temperature param-
+          2
                       (
                     i=2             )                                                               eters that can be used for the mechanistic model of UN fuels, we
    The terms on the right hand side of the Eq. (6) represent, re-                                   used the geometric parameters in Table 1 and the known fuel line
spectively, 1. the gain of bubbles in group i due to the coalescence                                 power to establish a ﬁnite element model of the fuel based on
of small bubbles; 2. the loss of bubbles in group i due to coales-                                   the ﬁnite element platform of COMSOL Multiphysics [31]. The ther-
cence between bubbles in group i and bubbles in other group; 3.                                      mal conductivity model of the cladding material is diﬃcult to ﬁnd.
and 4. the loss of gas bubbles in group i due to biased and random                                   So we used the thermal conductivity model of D9 [38], which is
diffusion of gas bubbles to grain boundaries; 5. the loss of gas bub-                                also austenitic stainless steel. When the temperature is below than
bles in group i due to grain boundary sweeping; 6. the loss of gas                                   10 0 0K λ = 7.598 + 2.391 × 10−2 T − 8.899 × 10−6 T 2 , otherwise λ =

                                                                                                 4
Z. Qian, W. Liu, R. Yu et al.                                                                                                     Journal of Nuclear Materials 556 (2021) 153188




Fig. 4. Comparison between (a) the ﬁssion gas release, (b) the fuel swelling and (c) the proportion of intragranular gas of the model with modiﬁed diffusion coeﬃcients
and the experimental value [30]. The left horizontal axis represents the nucleation factor, which varies from 1 to 1e-5, and the right horizontal axis represents resolution
constant, which changes from 1e-19 to 1e-16.



7.260 + 1.509 × 10−2 T . The thermal conductivity model [39] of UN                          Table 2
                                                                                            Key parameters used in the simulation.
is k = 1.37T 0.41 (1 − P )(1 + P ), P is porosity.
    We then simulated the test samples of the JOYO reactor exper-                                Symbol     Property                            Value
iment. The He gap closing process and the resulting temperature                                  Dg         diffusion coeﬃcient (cm2 •s−1 )
                                                                                                                                                                          5
                                                                                                                                                4.05 × 10−3 exp[− 2.15RT×10 ]∗
decrease was simulated following the reference from Blank [32]. In                               Fn         nucleation factor                   1×10−4
order to simplify the process, we simpliﬁed it into a linear change.                             b0         resolution constant (cm3 )          1×10−18
The detailed temperature is shown in Fig. 1.                                                ∗
                                                                                                R is the gas constant (J•mol−1 •K−1 ), T is the temperature of gas atoms (K).




3.2. Determination and interaction mechanism of key parameters                           3.2.1. Diffusion coeﬃcient
                                                                                             The ﬁssion gas diffusion coeﬃcients that have been proposed
   The key parameters used for the two simulation cases above                            for UN fuel are summarized in Table 3. For the purpose of com-
have been listed in Table 2. Most of the parameters were deter-                          parison, all these diffusion coeﬃcients were used in our model to
mined in the simulation case of the JOYO experiment. The process                         generate corresponding simulation results on the ﬁssion gas behav-
of determining each parameter will be described in details below.                        ior. A key experimental value that was used to gauge the accuracy

                                                                                     5
Z. Qian, W. Liu, R. Yu et al.                                                                                                   Journal of Nuclear Materials 556 (2021) 153188




Fig. 5. Comparison between (a) the ﬁssion gas release, (b) the fuel swelling and (c) the proportion of intragranular gas of the model with different combinations of nucleation
factor and resolution constant and the experimental value [30].



           Table 3                                                                        than 210 sets of tests with different nucleation factors and differ-
           Summary of diffusion coeﬃcients in open literature [7, 18].
                                                                                          ent resolution constants, and obtained the calculation results as
             Reference                        Value                                       shown in the Fig. 2 below. After ﬁnishing this step, we found that,
                                                                       5                  considering the three experimental values we can refer to, the cal-
             Melehan and Gates                4.0 × 10−6 exp[− 2.71RT×10 ]
             Biddle
                                                                       5
                                              3.0 × 10−8 exp[− 2.41RT×10 ]
                                                                                          culated results with diffusion coeﬃcient by Oi are the closest to
             Oi                               2.05 × 10−4 exp[− 2.15RT×10 ]
                                                                           5
                                                                                          the simulated conditions, but the disparity between the calculated
             BMI                              4.65 × 10 exp[− 3×10
                                                        −4
                                                                   RT
                                                                       5
                                                                         ]                results and the experimental values is still quite large. Among the
                                                                          5
             NASA                             2.4 × 10−10 exp[− 1.57RT×10 ]               three key experimental values for calibration, we are most con-
                                                                                          cerned with the proportion of intragranular gas, which directly re-
                                                                                          ﬂects the distribution of ﬁssion gas (80% in the grain bulk, 15% at
                                                                                          the grain boundary, 5% released), as this information is not avail-
of the diffusion coeﬃcients is the ratio of gas atoms retained in                         able in any other experiments for UN fuels. However, the results
the grain, which has been determined to be 80% [30]. The deter-                           of parameter sensitivity analysis show that the ﬁve groups of dif-
mination of parameters is indeed a diﬃculty in rate theory. There                         fusion coeﬃcients we investigated cannot meet the requirement of
are too many parameters that may affect the ﬁnal result. Therefore,                       closely matching with experimental data.
we make a detailed parameter sensitivity analysis to prove the ra-                           For the proportion of intragranular gas, only a few parame-
tionality of the parameters chosen in this work.                                          ters can affect it, mainly including the diffusion coeﬃcient of gas
   Firstly, according to the ﬁve groups of diffusion coeﬃcients that                      atoms and the grain size. Therefore, on the basis of Oi’s diffusion
can be obtained from literature research, we have carried out more

                                                                                      6
Z. Qian, W. Liu, R. Yu et al.                                                                                   Journal of Nuclear Materials 556 (2021) 153188


coeﬃcient, we considered the effect of different grain diameters.
Fig. 3 shows the comparison between the calculated results and
the experimental values with different grain diameters. It can be
seen that with the increase of grain diameter, the proportion of in-
tragranular gas is increasing, which means that the larger the grain
diameter is, the more diﬃcult it is for the ﬁssion gas to reach the
grain boundary. For the grain diameter of UN, 20 μm was used in
REDSTONE [18] and 10 μm was used in FRAPCON-EP [7]. There-
fore, we choose to test the grain diameter in the range of 10 μm
to 25 μm. And the above 210 tests are with the grain diameter of
10 μm. That is to say, even if the minimum grain diameter is used,
a reasonable result cannot be obtained. We can only adjust the dif-
fusion coeﬃcient to get more ﬁssion gas to the grain boundary.
    The pre-exponential factor of Oi’s diffusion coeﬃcients are in-
creased by factors of 10, 20, 30 and 40, respectively. The results
of the calculation are shown in Fig. 4. First of all, we should pay
attention to the change of fuel swelling with our selected parame-
ters. It can be seen that the change of fuel swelling caused by the
change of diffusion coeﬃcient is relatively small. This is because
that with the increase of the diffusion coeﬃcient of gas atoms,             Fig. 6. Comparison between the inferred diffusion coeﬃcient and that in open lit-
there will be two effects. One is that the number of ﬁssion gas             erature [7, 18].
atoms in the grain bulk will decrease. Because of the decrease of
gas atoms, the number of gas atoms that can enter gas bubbles will
decrease, and the swelling will be mitigated; another is that the           [17]. In previous works, the nucleation factor FN is usually taken
increase of gas atom diffusion coeﬃcient will lead to the increase          as a constant. For example, the constant 1 was used in the sim-
of bubble coalescence probability, so the probability of gas atom           ulation of the ﬁssion gas behavior of UO2 by Rest [34]; Miao [9-
absorbed by bubbles will increase, and this will lead to increase of        10] chose 0.01 for FN in the application of rate theory modeling for
swelling. The two effects are contradictory, so in most cases, with         U3 Si2 fuel; however, the value of FN is usually between 10−4 -10−10
the increase of diffusion coeﬃcient of gas atoms, the changes of            among metallic fuels [21-24]. For UN fuel, only a value of 0.027,
swelling are very small due to the two contradictory effects. We            which was used by Feng [7], is available for reference. Therefore,
found that the effect of diffusion coeﬃcient is enhanced in the re-         for UN fuel, the determination of the nucleation factor is a key
gion of small nucleation factor and large resolution constant. This         point worth discussing. In this paper, the experimental results of
is because that when the nucleation factor is small, the increase of        JOYO reactor were used to determine the most suitable nucleation
the proportion of large bubbles in the bulk becomes strong, at the          factor for UN fuel.
same time, a large resolution constant will lead to the gas atoms               Generally speaking, the smaller the nucleation factor, the
in the grain boundary bubble to return to the grain, which will             smaller the number of stable bubble cores formed, and the bub-
supplement the number of gas atoms in the bulk. In this case,               ble core is the incubation point of stable bubbles. The smaller the
the effect of decreasing gas atom caused by the increase of dif-            number of cores, the larger every single bubble can grow as the
fusion coeﬃcient will be weakened, and the effect of increasing             partitioning of ﬁssion gas is into a smaller amount of bases. The
bubble coalescence rate caused by the increase of diffusion coeﬃ-           contribution of large bubbles to fuel swelling is much higher than
cient will increase. Therefore, the effect of diffusion coeﬃcient on        that of small bubbles, considering the same number of total gas
swelling will be enhanced in the region of small nucleation factor          atoms, so the fuel swelling will be greater. At the same time, when
and large resolution constant. In general, the swelling caused by           the bubbles and the number density of bubbles are small, the bub-
the adjustment of diffusion coeﬃcient is much smaller than that             bles’ ability to absorb gas atoms will be weakened. A large number
of the other two key parameters. So we choose this three combi-             of gas atoms can reach the grain boundary through diffusion and
nations of nucleation factor and resolution constant with the least         release to the free space, so the release of ﬁssion gas will be en-
relative error between the calculated results and the experimen-            hanced. As a result, the proportion of gas atoms retained in the
tal values, they are (1e-4+1e-18), (1e-3+5e-18), (1e-3+1e-17) re-           grain will also decrease.
spectively. For convenience, we rearrange the results of the above              The results of our model under different nucleation factors and
three combinations. We can see that in Fig. 5, with the increase of         comparison with experimental values are shown in Fig. 7. The
diffusion coeﬃcient, the ﬁssion gas release increases and the pro-          value of 10−4 is recognized to be the most suitable nucleation fac-
portion of intragranular gas decreases. From the data of intragran-         tor for UN fuel by a comprehensive consideration of all the three
ular gas proportion, we can exclude the combination (1e-3+5e-18)            comparisons shown in the Fig. 7.
and (1e-3+1e-17), because even at the maximum diffusion coef-
ﬁcient of 40∗ Oi, they are still far from the experimental value of         3.2.3. Resolution constant
80%. So we ﬁnally chose the combination of (1e-4+1e-18), we also                The resolution constant b0 is used to describe the intensity of
ﬁne tuned the diffusion coeﬃcient, and ﬁnally determined that the           the resolution effect. In the process of analyzing the behaviors of
                                                                  5
most appropriate diffusion coeﬃcient is4.05 × 10−3 exp[− 2.15RT
                                                              ×10
                                                                  ].        ﬁssion gas, the effect of resolution was determined to be very sig-
Fig. 6 shows the comparison between the diffusion coeﬃcient we              niﬁcant. In the simulation of ﬁssion gas behavior of other fuel
derived for our model and the diffusion coeﬃcients from the liter-          types, Rest [11] used b0 =2×10−17 cm3 and b0 =2×10−18 cm3 for
ature in the past.                                                          UO2 and U-10Mo fuel, respectively. In addition, in the simulation
                                                                            of UO2 fuel, Lösönen [8] used b0 =3×10−17 cm3 . Miao [9-10] chose
3.2.2. Nucleation factor                                                    b0 =2×10−17 cm3 as the resolution constant for U3 Si2 fuel; in the
    The nucleation factor FN is used to evaluate the stability of the       simulation of UN fuel, Feng [7] used b0 =1.36×10−15 cm3 , which
bubble core during the nucleation process. It refers to the proba-          is signiﬁcantly larger than the value used by others. To obtain the
bility that the bubble core can exist stably after initial formation        most accurate resolution constant that can be used for UN fuel, dif-

                                                                        7
Z. Qian, W. Liu, R. Yu et al.                                                                                                  Journal of Nuclear Materials 556 (2021) 153188




Fig. 7. Comparison between (a) the ﬁssion gas release, (b) the fuel swelling and (c) the proportion of intragranular gas of the model with different nucleation factor and the
experimental value [30].




ferent resolution constants were used in the simulation of the JOYO                          To analyze the complex effects of resolution on ﬁssion gas re-
experiment, and the resolution constants for comparison were se-                          lease and fuel swelling, the number densities of bubbles of differ-
lected to be between 10−19 -10−16 . The results are shown in the                          ent sizes in the grain with different resolution constants were ana-
Fig. 8. It is found that the three important quantities, ﬁssion gas                       lyzed in details. The number density of bubbles in different groups
release, fuel swelling and proportion of intragranular gas, showed                        under different resolution constants is shown in Fig 9. The bubble
different trends. The resolution effects will cause the gas atoms in                      group label refers to the group number such that the bubble in
both intragranular and intergranular bubbles to be knocked back to                        that particular group contains 2^ (group label) gas atoms. It can be
the fuel matrix [35]. It is easy to infer that the proportion of gas                      seen that with the increase of the resolution constant, the number
atoms in the grain will increase with the increase of the resolution                      of small-size bubbles increases. This is because a large number of
constant, because there are more gas atoms knocked back to the                            gas atoms in both intragranular and intergranular bubbles return to
fuel matrix. However, the trend of ﬁssion gas release and the fuel                        the grain due to the effect of resolution. These gas atoms provide
swelling are more complex with the change of the resolution con-                          the driving force for bubble nucleation and growth, so the number
stant. The fuel swelling rises at the beginning and then fall when                        of small-size bubbles increases. At the same time, it can also be
the resolution constant is increased, while the release of ﬁssion gas                     found that the number density of large-size bubbles also increases,
possesses opposite trend to the fuel swelling.                                            which is due to the weaker effect of resolution on large-size bub-


                                                                                      8
Z. Qian, W. Liu, R. Yu et al.                                                                                                  Journal of Nuclear Materials 556 (2021) 153188




Fig. 8. Comparison between (a) the ﬁssion gas release, (b) the fuel swelling and (c) the proportion of intragranular gas of the model with different resolution constants and
the experimental value [30].




bles and the stronger gas atoms absorption capacity of large-size                        atoms reaching the grain boundary through diffusion due to the in-
bubbles. However, with the increase of the resolution constant, the                      crease of intragranular gas atoms. The effect of this process is op-
effect of resolution is enhanced to the extent that the large-size                       posite to the previous one. When the resolution constant is small,
bubbles can be destroyed, resulting in a rapid decrease in the num-                      although the number of gas atoms in the grain increases, there are
ber of large-size bubbles. So the resulting effect is that the number                    still some intragranular bubbles that can absorb these gas atoms,
of small-size bubbles increases, the number of medium-size bub-                          so the ﬁrst process plays a determining role. But when the reso-
bles decreases, and the number of large-size bubbles increases at                        lution constant is large, not only the number of gas atoms in the
ﬁrst and then decrease with the increase of the resolution con-                          grain will greatly increase, but the intragranular bubbles will also
stant. The swelling of bubbles is the main source of fuel swelling,                      be destroyed, so the inﬂuence of the second process is enhanced.
and the contribution of large-size bubbles to the fuel swelling is                       Consequently, the ﬁssion gas release shows a trend of decline at
particularly important, so the fuel swelling presents a trend of ris-                    ﬁrst and then rise with the enhancement of resolution.
ing at ﬁrst and then falling. Resolution has two impacts on ﬁssion                           After considering all the three quantities in Fig. 8, we deter-
gas release. One is that the gas atoms in the intergranular bubbles                      mined that the b0 =1×10−18 cm3 may be the most suitable value
return to the grain due to resolution. This process will reduce the                      for the UN fuels. This value is much smaller than Feng’s, and it is
ﬁssion gas release. The other is the increase of the number of gas                       also more reasonable from a physics point of view.


                                                                                     9
Z. Qian, W. Liu, R. Yu et al.                                                                                                   Journal of Nuclear Materials 556 (2021) 153188




Fig. 9. The number density of bubbles in different groups with different resolution
                                                                                             Fig. 11. Comparison between the ﬁssion gas release of the model and the experi-
constants. The bubble group label represents bubbles that contain 2group label number
                                                                                             mental value [30].
of gas atoms.




       Fig. 10. Variation in swelling against burnup for different values of m.              Fig. 12. Comparison between the fuel swelling of the model and the experimental
                                                                                             value [30].


3.2.4. “m” in bubble size grouping method
    There is an important parameter m in the bubble size grouping                            of the JOYO experimental reactor are shown in Fig. 11 and Fig. 12,
method, and it determines the ﬁneness of the model. The grouping                             respectively. It can be seen that the mechanistic model can accu-
method used in our model is consistent with that of GRASS-SST                                rately predict the ﬁssion gas release. Fig. 11 is the fractional ﬁs-
[28]. The choice of m is generally an integer, because the num-                              sion gas release versus burnup. In the early stage of fuel irradia-
ber of gas atoms in the bubble is always an integer. Fig. 10 shows                           tion, due to the high porosity of the UN fuel, it is assumed that
the evolution of retained ﬁssion gas resulted fuel swelling against                          interconnected tunnels already formed on the grain faces to trans-
burnup for m=2 to 4. The predicted swelling increases with the                               port ﬁssion gas to the grain edge tunnels [7]. Fission gas is released
increase of m, and the difference of swelling corresponding to dif-                          through the surface connected porosity [33], so the ﬁssion gas re-
ferent m is reasonably small. As m increases, the computing time                             lease increases rapidly. At intermediate burnup, the temperature of
is greatly reduced, and the number of bubble groups is also re-                              the fuel continues to drop due to the slow closure of the He gap,
duced. In principle, the more detailed manner the bubble division                            and the diffusion of ﬁssion gas is highly dependent on tempera-
is, the more accurate the model will be, and therefore m=2 was                               ture. Therefore, as the temperature continues to drop, the number
chosen in our simulation.                                                                    of gas atoms reaching the grain boundary continues to decrease,
                                                                                             so the fractional release of ﬁssion gas continues to drop. At higher
3.3. The results by our model                                                                burnup, as the fuel temperature remains relatively constant, the
                                                                                             ﬁssion gas release gradually stabilizes. Fig. 12 shows the change
   According to the temperature shown in Fig. 1, the results of                              of fuel swelling with fuel burnup. With the increase of burnup, the
the fractional ﬁssion gas release and fuel swelling versus burnup                            number of ﬁssion gas in the grain is increasing, the swelling in-

                                                                                        10
Z. Qian, W. Liu, R. Yu et al.                                                                                                           Journal of Nuclear Materials 556 (2021) 153188


                                                                                                Table 4
                                                                                                Comparison between the calculation values and the experimental data [30].

                                                                                                  Parameter                                Calculated values     Experimental data

                                                                                                  Fuel swelling (%)                        7.1869                6.7
                                                                                                  Fission gas release (%)                  5.2838                5.2
                                                                                                  Proportion of intragranular gas (%)      80.5                  80




Fig. 13. Comparison between the radial distribution of Xe of the model and the
experimental value [30].




creases continuously, and the difference in slope is mainly due to
the inﬂuence of temperature changes, as depicted in Fig. 1.
    At the same time, for the fuel sample of the JOYO experimen-
tal reactor, Tanaka et al. also obtained the statistics on the ﬁssion                           Fig. 15. The bubble size distribution of the JOYO’s simulation. The bubble group
gas retained in the fuel. The comparison between the model cal-                                 label represents bubble that contains 2group label number of gas atoms.
culation and the experimental data is shown in Fig. 13. It can be
seen that the result of the model is in reasonable accordance with
the trend of the experimental values. Another point of concern is                               gas is shown in Fig. 14 and the bubble number density is shown
that most of the ﬁssion gas produced is retained in the grain, and                              in Fig. 15.
the ratio of retained gas is 80%. A small part of the gas is released                               In order to further validate the model, some experimental re-
to the external fuel plenum, and this fractional release is close to                            sults of the fuel swelling and ﬁssion gas release of UN fuel from
5%. The remaining part of the ﬁssion gas is trapped in the grain                                the open literature were summarized, and calculations were per-
boundary of the fuel in the form of bubbles. It can be seen that                                formed using our model to generate results that can be compared
the simulation results accurately captured this partition of ﬁssion                             to these data. However, due to ambiguities that exist in the exper-
gas. The comparison between the result of the model and the ex-                                 imental conditions, such as the detailed temperature distribution
perimental data is shown in Table 4.The distribution of retained                                and fuel geometry, exact model parameters cannot be obtained.




                                Fig. 14. Retained fractions of ﬁssion gas in (a) inter- or intra-granular bubbles, in (b) large bubbles or small bubbles.


                                                                                           11
Z. Qian, W. Liu, R. Yu et al.                                                                                                 Journal of Nuclear Materials 556 (2021) 153188




       Fig. 16. Comparison among the (a) ﬁssion gas release and the (b) fuel swelling of the model, the Storms’ relationship and the experimental value [6-7, 30, 33].



Therefore, for the geometric and temperature setting, we used pa-
rameters from the JOYO experiment.
    The comparison between the ﬁssion gas release calculated by
the model and the experimentally obtained value is shown in
Fig. 16(a). Due to the above mentioned ambiguity issue of the ex-
act experimental conditions, this comparison shall be treated as a
vague validation of the model which only provides information on
the match of the simulation results to the trend of the experimen-
tal data. It can be seen that the distribution of the experimental
data is relatively scattered, and the calculation results are in rea-
sonable agreement with the experimental data, and can basically
reﬂect the trend of most experimental points. Fig. 16(b) shows
the comparison between the fuel swelling calculated by the model
and the experimental data. It is perceivable that the result of our
model can well reﬂect the trend of the experimental data. The rea-
son for the accelerated increase of swelling is due to the genera-
tion of large bubbles, and the contribution of large bubbles to fuel
swelling is much greater than that of small bubbles [5].


3.4. Inﬂuence of resolution on the bimodal bubble size distribution                       Fig. 17. The number density of bubbles in different groups when there is no res-
                                                                                          olution or the resolution constant is b0 =1×10−19 cm3 and b0 =5×10−19 cm3 , re-
                                                                                          spectively. The bubble group label in the x axis represents bubble that contains
    In the determination the resolution constant in Section 3.2.3,
                                                                                          2group label number of gas atoms.
an interesting phenomenon that the bubble size shows a bimodal
distribution was discovered. The bimodal bubble size distribution
dictates that there are two peaks in the bubble size distribution,
and it can be widely seen in a variety of nuclear fuels, including                        ble radius. Resolution will cause an increase in the amount of gas
U-O [25-26] and U-Si [27] fuels.                                                          atoms in the grain. The increase of these atoms will also provide a
    Fig. 17 shows the number density of bubbles in different groups                       driving force for bubble nucleation and bubble growth. The ability
when there is no resolution or when the resolution constants are                          of large-size bubbles to absorb gas atoms is greater than that of
b0 =1×10−19 cm3 and b0 =5×10−19 cm3 , respectively. We can eas-                           medium-size bubbles, so there may be a tendency for the number
ily ﬁnd that the result without resolution shows a unimodal bub-                          of large-size bubbles to increase due to resolution. In Fig. 18 where
ble size distribution. However, the bubble size distributions show                        a schematic diagram is exhibited, the black solid line represents
an obvious bimodal shape under the inﬂuence of resolution, and                            the reduction ability of the resolution under different bubble sizes
the larger the resolution constant, the more obvious the bimodal                          for the number of bubbles, and the red-orange solid line represents
shape. It is not diﬃcult to get an inference that resolution is the                       the ability of different size bubbles to absorb gas atoms. When the
driving factor for the bimodal bubble size distribution.                                  black line is higher than the red-orange line, the number of bub-
    The essence of resolution is to knock the gas atoms in the bub-                       bles tends to decrease, and when the red-orange line is higher than
ble back into the matrix [36]. The main effect of resolution on the                       the black line, the number of bubbles tends to increase. Compared
bubble is to reduce the number and size of the bubbles. For bub-                          with medium-size bubbles, large-size bubbles are less affected by
bles, the intensity of resolution decreases with the increase of bub-                     resolution and have a stronger ability to absorb gas atoms to grow.

                                                                                     12
Z. Qian, W. Liu, R. Yu et al.                                                                                                             Journal of Nuclear Materials 556 (2021) 153188


                                                                                         Zhengyu Qian: Conceptualization, Methodology, Investigation,
                                                                                      Writing –Original Draft
                                                                                         Wenbo Liu: Methodology, Investigation
                                                                                         Rui Yu: Investigation
                                                                                         Yujie Tao: Investigation
                                                                                         Di Yun: Conceptualization, Methodology, Writing –Review and
                                                                                      Editing
                                                                                         Long Gu: Conceptualization, Writing –Review and Editing,
                                                                                      Funding acquisition

                                                                                      Declaration of Competing Interest

                                                                                          The authors declare that they have no known competing ﬁnan-
                                                                                      cial interests or personal relationships that could have appeared to
                                                                                      inﬂuence the work reported in this paper.

                                                                                      Acknowledgments

                                                                                         This work was supported by the State Key Research and De-
                                                                                      velopment Program of China, Grant No. 2020YFB1902100. National
                                                                                      Natural Science Foundation of China, Grant No. 11675126 and
                                                                                      11705255 is acknowledged. Special fund of Shanghai Economic
       Fig. 18. Schematic diagram of resolution on bubbles of different sizes.
                                                                                      and Information Technology Commission (approved number: GYQJ-
                                                                                      2018-2-02) is also acknowledged.
Therefore, the number of large-size bubbles will not decrease but
increase, which will result in the formation of a peak in the area                    Appendix
of large-size bubbles. A large number of gas atoms returning to the
grain will also promote nucleation and generate more bubble nu-                          For gas atoms in the grain face, the form of Eq. (1) is modiﬁed
clei. These new nuclei will slowly absorb gas atoms to grow, but                      to become:
due to the shorter growth time, the ﬁnal size is smaller, so it con-                  dC f,g                                               
                                                                                                                                           I
tributes to the small-size bubbles, and this causes another peak to                    dt
                                                                                                π FN, f R f,g D f,gC f,g 2 − Pg,iC f,gC f,i
                                                                                             = −16
                                                                                                                           i=2
form in the small-size bubble area. When there is a bigger resolu-                               6Dg ∂ Cg 
tion constant which is indicated by the blue dotted line in Fig. 18,                  +SgbVgCg − dg ∂ r                                                                          (A1)
                                                                                                                       r=dg /2
only larger-size bubbles can maintain the increasing trend and this                                           V       N        PC
                                                                                      − V f,g SNBC f,g − df,ggC g f − A t f,g
causes the right peak to move to further right. Correspondingly, the                                                  f,g
                                                                                          3VgbCg
stronger resolution will destroy the small bubbles more violently,                    +     dg
and the left peak will shift to further left. The result of our model
                                                                                      Where, FN,f is the nucleation factor in grain face; SNB is the area of
in Fig 17 when the resolution constant b0 =5×10−19 cm3 veriﬁes
                                                                                      fuel boundary/volume of the fuel; Ngf is the number of grain faces
this point.
                                                                                      per grain; PA is the interlinkage fraction of the grain face channel.
                                                                                          The terms on right hand side of the Eq. (A1) represent, respec-
4. Conclusions                                                                        tively, 1. the loss of gas atoms due to nucleation; 2. the loss of gas
                                                                                      atoms caused by capture of gas atoms by bubbles; 3. and 4. the
   A mechanistic ﬁssion gas behavior model of UN fuels has been                       gain of gas atoms due to biased and random diffusion of gas atoms
established under the framework of kinetic rate theory in this pa-                    from the grain; 5. the loss of gas atoms due to the long-range mi-
per. The model can accurately simulate the ﬁssion gas release and                     gration; 6. the loss of gas atoms due to the biased migration to the
fuel swelling of UN fuels. Based on the data from the JOYO exper-                     grain edge; 7. the loss of gas atoms due to migration of grain face
imental reactor, the rationality of the currently available Xe diffu-                 gas through grain face channels to the grain edge; 8. the increase
sion coeﬃcients in UN fuels was analyzed by using the ﬁnite el-                       of gas atoms because of the grain boundary sweeping.
ement simulation platform COMSOL to provide input parameters                              For the grain face bubbles in group i, the equation form changes
for the UN fuels mechanistic ﬁssion gas behavior model, and a                         to be:
new diffusion coeﬃcient which can be used for the modeling of
UN fuels has been proposed. In addition, the sensitivity analysis of                  dC f,i     
                                                                                                 i/2                                
                                                                                                                                    I
                                                                                       dt
                                                                                             =          Pk,i−kC f,kC f,i−k −              Pi,kC f,iC f,k
two parameters, the nucleation factor and the resolution constant,                               k=1                                k=1
has been carried out. The inﬂuence of these parameters on fuel
                                                                                                 i=2             
                                                                                      +SgbViCi − 6dDg i ∂∂Cri                                                                    (A2)
swelling and ﬁssion gas release was explained, and the suitable                                                   r=dg /2
                                                                                          3V                                  V N            PC
values that can be used for UN fuels were determined. At the same                     − dggb C f.i − V f,i SNBC f,i − df,igC g f − A t f,i
                                                                                                                                    f,i
time, in view of the phenomenon of bimodal bubble size distribu-                          3VgbCi              16π FN, f R f,g D f,gC f,g 2
tion, the underlying physics mechanisms were analyzed in details,
                                                                                      +     dg
                                                                                                 − bi C f,i +             2
                                                                                                                                              (i = 2 )
and a reasonable explanation that the resolution is the driving fac-                      The terms on right hand side of the Eq. (A2) represent, respec-
tor was put forward.                                                                  tively, 1. the gain of grain face bubbles due to the coalescence of
                                                                                      small bubbles; 2. the loss of grain face bubbles caused by coales-
Author statement                                                                      cence between bubbles in group i and bubbles in other group; 3.
                                                                                      and 4. the gain of grain face bubbles due to biased and random dif-
   I hereby provide the following statement on the role of each                       fusion of bubbles from the grain; 5. the loss of grain face bubbles
author and conﬁrm that all details provided here are truthful.                        due to bubble pull-off from a moving grain boundary; 6. the loss of

                                                                                 13
Z. Qian, W. Liu, R. Yu et al.                                                                                                              Journal of Nuclear Materials 556 (2021) 153188


grain face bubbles due to the long-range migration; 7. the loss of                                   [9] Y. Miao, K.A. Gamble, D. Andersson, Z. Mei, A.M. Yacout, Rate theory scenarios
grain face bubbles due to the biased migration to the grain edge;                                        study on ﬁssion gas behavior of U3 Si2 under LOCA conditions in LWRs, Nucl.
                                                                                                         Eng. Des. 326 (2018) 371–382.
8. the loss of grain face bubbles due to migration of grain face bub-                               [10] Y. Miao, K.A. Gamble, D. Andersson, B. Ye, Z. Mei, G. Hofman, A.M. Yacout,
bles through grain face channels to the grain edge; 9. the increase                                      Gaseous swelling of U3 Si2 during steady-state LWR operation: A rate theory
of grain face bubbles because of the grain boundary sweeping; 10.                                        investigation, Nucl. Eng. Des. 322 (2017) 336–344.
                                                                                                    [11] J. Rest, Modeling of Fission-Gas Induced Swelling of Nuclear Fuels, 2016.
the loss of grain face bubbles because of resolution; 11. the gain of                               [12] A.H. Booth, A Method of Calculating Fission Gas Diffusion from Uo $ Sub 2$
grain face bubbles in group 2 due to nucleation.                                                         Fuel and its Application to the X-2-F Loop Test, Atomic Energy of Canada Ltd,
    Eqs. (A3) and (A4) represent the form of Eq. (1) for gas atoms                                       Chalk River Project, Chalk River, Ont, 1957.
                                                                                                    [13] M.V. Speight, A calculation on the migration of ﬁssion gas in material exhibit-
and bubbles in grain edge.
                                                                                                         ing precipitation and re-solution of gas atoms under irradiation, Nucl. Sci. Eng.
                                            
                                            I                                                            37 (1969) 180–185.
dCe,g
 dt
      = −16      π FN,e Re,g De,gCe,g 2 −         Pg,iCe,gCe,i                                      [14] M.R. Hayns, M.H. Wood, Models of ﬁssion gas behaviour in fast reactor fuels
                                            i=2                                                          under steady state and transient conditions, J. Nucl. Mater. 67 (1977) 155–170.
                           N                                                         (A3)
     (           )
+PA 1 − PI C f,g /t + V f,g dggf    (1 − PI )C f,g                                                  [15] J. Rest, G.L. Hofman, Y.S. Kim, Analysis of intergranular ﬁssion-gas bubble-size
                                                                                                         distributions in irradiated uranium–molybdenum alloy fuel, J. Nucl. Mater. 385
− ddtPI Ce,g                                                                                             (2009) 563–571.
                                                                                                    [16] J. Rest, Evolution of ﬁssion-gas-bubble-size distribution in recrystallized
    The terms on right hand side of the Eq. (A3) represent, respec-                                      U–10Mo nuclear fuel, J. Nucl. Mater. 407 (2010) 55–58.
                                                                                                    [17] J. Rest, An analytical study of gas-bubble nucleation mechanisms in urani-
tively, 1. the loss of gas atoms due to nucleation; 2. the loss of gas
                                                                                                         um-alloy nuclear fuel at high temperature, J. Nucl. Mater. 402 (2010) 179–185.
atoms caused by capture of gas atoms by bubbles; 3. the gain of                                     [18] D.L. Deforest, Transient Fission Gas Behavior In Uranium Nitride Fuel Under
gas atoms due to the biased migration of gas atoms from the grain                                        Proposed Space Applications, AIR FORCE INST OF TECH WRIGHT-PATTERSON
                                                                                                         AFB OH, 1991.
face; 4. the gain of gas atoms due to the migration of grain face
                                                                                                    [19] H. Matzke, Diffusion in ceramic oxide systems, Fission Product Behav. Ceram.
gas through grain face channels; 5. the loss of gas atoms due to                                         Oxide Fuel (1986).
the release of grain edge gas atoms through interconnected tun-                                     [20] M. Backhaus Ricoult, Diffusion Processes and Interphase Boundary Morphol-
nels.                                                                                                    ogy in Ternary Metal-Ceramic Systems, Berichte der Bunsengesellschaft für
                                                                                                         physikalische Chemie 90 (1986) 684–690.
dCe,i     2
          i/                          
                                      I                                                             [21] C.B. Lee, B.H. Lee, C. Nam, D.S. Sohn, GRSIS Program To Predict Fission Gas Re-
 dt
      =          Pk,i−kCe,kCe,i−k −         Pe,kCe,iCe,k                                                 lease And Swelling Behavior Of Metallic Fast Reactor Fuel, Korea Atomic Energy
          k=1                         k=1                                                                Research Institute, 1999.
          i=2
                                                                                                    [22] G. Kaganas, J. Rest, A physical Description Of Fission Product Behavior Fuels
                                N
+PA (1 − PI )C f,i /t + V f,i dggf (1 − PI )C f,i                                    (A4)                For Advanced Power Reactors, Argonne National Lab.(ANL), Argonne, ILUnited
  3V C                                                                                                   States, 2007.
− gbdg e,i − bi Ce,i − ddtPI Ce,i                                                                   [23] C.B. Lee, D.H. Kim, Y.H. Jung, Fission gas release and swelling model of metallic
  16π FN,e Re,g De,gCe,g 2                                                                               fast reactor fuel, J. Nucl. Mater. 288 (2001) 29–42.
+           2
                        (  i=2  )                                                                   [24] W.G. Steele, A.R. Wazzan, D. Okrent, Steady-state ﬁssion gas behavior in ura-
                                                                                                         nium plutonium zirconium metal fuel elements, Nucl. Eng. Des. 113 (1989)
    The terms on right hand side of the Eq. (A4) represent, respec-                                      289–295.
tively, 1. the gain of grain edge bubbles due to the coalescence of                                 [25] V.F. Chkuaseli, Fission gas bubble behaviour in uranium dioxide, J. Nucl. Mater.
small bubbles; 2. the loss of grain edge bubbles caused by coales-                                       201 (1993) 92–96.
                                                                                                    [26] S. Kashibe, K. Une, K. Nogita, Formation and growth of intragranular ﬁssion gas
cence between bubbles in group i and bubbles in other group; 3.                                          bubbles in UO2 fuels with burnup of 6–83 GWd/t, J. Nucl. Mater. 206 (1993)
the gain of grain edge bubbles due to the biased migration of gas                                        22–34.
bubbles from the grain face; 4. the gain of gas atoms due to the                                    [27] G.L. Hofman, J. Rest, J.L. Snelgrove, A New Swelling Model And Its Applica-
                                                                                                         tion To Uranium Silicide Research Reactor Fuel, Argonne National Lab., ILUnited
migration of grain face bubbles through grain face channels; 5. the                                      States, 1992.
loss of grain edge bubbles due to bubble pull-off from a moving                                     [28] J. Rest, GRASS-SST: a comprehensive, mechanistic model for the prediction of
grain boundary; 6. the loss of grain edge bubbles because of reso-                                       ﬁssion-gas behavior in UO2 -base fuels during steady-state and transient con-
                                                                                                         ditions, Argonne Natl. Lab (1978).
lution; 7. the loss of grain edge bubbles due to the release of grain                               [29] J. Rest, S.A. Zawadzki, FASTGRASS: a mechanistic model for the prediction of
edge bubbles through interconnected tunnels; 8. the gain of grain                                        Xe, I, Cs, Te, Ba, and Sr release from nuclear fuel under normal and severe-ac-
edge bubbles in group 2 due to nucleation.                                                               cident conditions, Nuclear Regulatory Commission, Washington, DC (United
                                                                                                         States), Div. Syst. Res. (1992).
                                                                                                    [30] K. Tanaka, K. Maeda, K. Katsuyama, M. Inoue, T. Iwai, Y. Arai, Fission gas release
References
                                                                                                         and swelling in uranium–plutonium mixed nitride fuels, J. Nucl. Mater. 327
                                                                                                         (2004) 77–87.
 [1] R.B. Matthews, K.M. Chidester, C.W. Hoth, R.E. Mason, R.L. Petty, Fabrication                  [31] C. Multiphysics, C. Module, COMSOL multiphysics user’s guide, Version: COM-
     and testing of uranium nitride fuel for space power reactors, J. Nucl. Mater.                       SOL Multiphys. 3 (2014).
     151 (1988) 345.                                                                                [32] H. Blank, Basic aspects of swelling in dense livuid metal fast breeder reactor
 [2] J.H. Kittel, B. Frost, J.P. Mustelier, K.Q. Bagley, G.C. Crittenden, J. Van Dievoet,                fuels, J. Less Common Metals 121 (1986) 583–603.
     History of fast reactor fuel development, J. Nucl. Mater. 204 (1993) 1–13.                     [33] A.A. Bauer, J.B. Brown, E.O. Fromm, V.W. Storhok, Mixed-Nitride Fuel Irradia-
 [3] K.Y. Spencer, L. Sudderth, R.A. Brito, J.A. Evans, C.S. Hart, A. Hu, A. Jati, K. Stern,             tion Performance, Battelle Memorial Inst., Columbus, Ohio, 1971.
     S.M. McDeavitt, Sensitivity study for accident tolerant fuels: Property compar-                [34] J. Rest, G.L. Hofman, An alternative explanation for evidence that xenon deple-
     isons and behavior simulations in a simpliﬁed PWR to enable ATF develop-                            tion, pore formation, and grain subdivision begin at different local burnups, J.
     ment and design, Nucl. Eng. Des. 309 (2016) 197–212.                                                Nucl. Mater. 277 (20 0 0) 231–238.
 [4] J. Rest, M. Cooper, J. Spino, J.A. Turnbull, P. Van Uffelen, C.T. Walker, Fission gas          [35] D.R. Olander, D. Wongsawaeng, Re-solution of ﬁssion gas–a review: part I. In-
     release from UO2 nuclear fuel: a review, J. Nucl. Mater. 513 (2019) 310–345.                        tragranular bubbles, J. Nucl. Mater. 354 (2006) 94–109.
 [5] D.R. Olander, Fundamental Aspects Of Nuclear Reactor Fuel Elements: Solu-                      [36] R.S. Nelson, The stability of gas bubbles in an irradiation environment, J. Nucl.
     tions To Problems, California Univ., Berkeley (USA). Dept. of Nuclear Engineer-                     Mater. 31 (1969) 153–161.
     ing, 1976.                                                                                     [37] S.C. Weaver, Helium gas bubble migration in uranium mononitride in a tem-
 [6] E.K. Storms, An equation which describes ﬁssion gas release from UN reactor                         perature gradient, Am. J. Clin. Nutr. (1967).
     fuel, J. Nucl. Mater. 158 (1988) 119–129.                                                      [38] L. Leibowitz, R.A. Blomquist, Thermal conductivity and thermal expansion of
 [7] B. Feng, Feasibility of Breeding in Hard Spectrum Boiling Water Reactors with                       stainless steels D9 and HT9, Int. J. Thermophys. 9 (1988) 873–883.
     Oxide and Nitride Fuels, ProQuest Dissertations Publishing, 2011.                              [39] B.D. Rogozkin, N.M. Stepennova, A.A. Proshkin, Mononitride fuel for fast reac-
 [8] P. Lösönen, On the effect of irradiation-induced resolution in modelling ﬁssion                     tors, Atom Energy+ 95 (2003) 624–636.
     gas release in UO2 LWR fuel, J. Nucl. Mater. 496 (2017) 140–156.




                                                                                               14
