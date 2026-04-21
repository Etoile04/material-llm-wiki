# Fission gas release and swelling model of metallic fast reactor fuel

Chan Bock Lee \*, Dae Ho Kim, Youn Ho Jung

Korea Atomic Energy Research Institute, Yusung, P.O. Box 105, Taejon, South Korea

Received 21 August 2000; accepted 1 November 2000

## Abstract

A mechanistic model of ®ssion gas release and swelling for the U±Pu±10Zr metallic fuel in a fast reactor, GRSIS (Gas Release and Swelling in ISotropic fuel matrix), was developed. Fission gas bubbles are assumed to nucleate isotropically from gas atoms in the metallic fuel matrix since they could nucleate at both the grain boundaries and the phase boundaries, which are randomly distributed inside the grain. Bubbles can grow to larger sizes by gas atom diusion and coalescence with other bubbles. When bubble density or swelling due to bubbles reaches a threshold value, bubbles are assumed to be interconnected to each other to form an open channel to the external free space and then the ®ssion gases inside the interconnected open bubbles are released instantaneously. During the irradiation, ®ssion gases are successively released through the open bubbles. The GRSIS model was validated by comparison with the irradiation test results of U±Pu±10Zr fuels as well as parametric studies of the key variables in the model. Ó 2001 Elsevier Science B.V. All rights reserved.

PACS: 28.41.AK; 28.41.Bm

## 1. Introduction

U±Pu±10Zr metallic fuel is being considered as one of the candidates for the fuel of the KALIMER fast reactor which is under development [1]. The concept of using U±Pu±10Zr fuel in the fast reactor was ®rst developed at ANL (Argonne National Laboratory) and irradiation tests of fuels of various compositions were performed extensively in the EBR-II research reactor [2]. When the U±Pu±10Zr metallic fuel is irradiated around 600C, ®ssion gas bubbles nucleate and grow at a rate much higher than the ceramic $\mathrm { U O } _ { 2 }$ fuel, due to the high diusivity of ®ssion gas atoms in the metallic fuel. Fuel swelling due to the ®ssion gas bubbles could start at about 0.5% burnup after the incubation period and then increase rapidly until fuel gap closure at a burnup is less than 2%. Fig. 1 shows the fractional ®ssion gas release as a function of the burnup for U±Pu±10Zr fuel irradiated in ANL [3]. Fission gases are released out of the fuel through open channels formed by interconnection of the bubbles at a burnup of 0.5±1.0%. Then, fractional ®ssion gas release increases by up to about 70% and becomes saturated at a burnup of 4±5%.

Many models [4±10] have been developed for ®ssion gas release and swelling behavior of the U±Pu±10Zr metallic fuel for the fast reactor. The model in the LIFE-Metal code [4] is an empirical model, which calculates the ®ssion gas release by a simple function using burnup, porosity and temperature. It does not explicitly consider the ®ssion gas bubbles. STARS [5] and ALFUS [6±8] models consider the bubble formation and growth, based upon a model of the $\mathrm { U O } _ { 2 }$ fuel. Therefore, it is assumed that ®ssion gases are generated inside the grain and then diuse to the grain boundaries to nucleate the bubbles or to be absorbed by the bubbles in the grain boundaries. However, in the metallic fuel for the fast reactor, the ®ssion gas bubbles could nucleate at the phase boundaries inside the grain as well as at the grain boundaries. The phase boundaries are distributed quite randomly inside the grain in the U±Pu±10Zr metallic fuel. Therefore, the eect of grain size upon ®ssion gas behavior in the metallic fuel may not be signi®cant, compared with its eect in $\mathrm { U O } _ { 2 }$ fuel.

<table><tr><td colspan="2">Nomenclature</td><td rowspan="2"> $f _ { \mathrm { v } }$ </td><td rowspan="2">fractional volume of a closed bubble after interconnected to the open bubble</td></tr><tr><td> $a _ { \mathsf { b } _ { i } }$ </td><td>surface area of a bubble-i (m²)</td></tr><tr><td> $a _ { j }$ </td><td>lattice constant of bubble-j in FCC latice area occupied by a gas atom at the bubble</td><td> $g a b _ { i j }$ </td><td>collision or integration rate of bubble-i into bubble-j byradial growth of bubble-i</td></tr><tr><td> $a _ { 0 } ^ { 2 }$ </td><td>surface  $( \mathbf { m } ^ { 2 } )$ </td><td></td><td>due to gas diffusion to bubble-i (atoms/s m)</td></tr><tr><td> $a b _ { i i }$ </td><td>jump or transition rate of bubble-i into bubble i+1 (atoms/s m) integration rate of bubble-i into bubble-j</td><td> $j _ { \mathrm { { g } } _ { i } }$ </td><td>gas atom diffusion to a bubble-i (atoms/ bub-i s)</td></tr><tr><td> $a b _ { i j }$   $a t n b _ { i }$ </td><td>by bubble diffusion (atoms/s m) density of gas atom in a bubble-i (atoms/</td><td> $J _ { \mathrm { { g } } _ { i } }$ </td><td>gas atom diffusion to bubble-i (atoms/s m)</td></tr><tr><td>bubble-4i</td><td>bub-i)</td><td> ${ J } _ { \mathrm { b _ { 1 } n u c l } }$ </td><td>bubble-1 nucleation rate(atoms/s m) bubble-1 nucleation constant</td></tr><tr><td> $\mathrm { o r } \ b 4 i$ </td><td>open bubble to which the closed bubble-i is transformed after being open</td><td> $k _ { \mathrm { b _ { 1 } n u c l } }$ </td><td>(bub-1/s +atom)</td></tr><tr><td> $C _ { \mathrm { g } }$ </td><td>gas atom concentration in the matrix</td><td> $k _ { \mathrm { g } _ { i } }$ </td><td>gas diffusion constant to bubble-i  $( \mathrm { m } ^ { 3 } / \mathrm { s } )$ </td></tr><tr><td> $C _ { \mathrm { g b } _ { i } }$ </td><td>(atoms/m³) gas atom concentration as the bubble-i in</td><td> $k _ { i i }$ </td><td>jump rate constant of bubble-i into bub-  $\mathsf { b l e } \mathrm { - } i + 1 \ ( \mathsf { m } ^ { 3 } / \mathsf { s } )$ </td></tr><tr><td></td><td>the matrix (atoms/m³)</td><td> $k _ { i j }$ </td><td>collision or integration constant of bub-</td></tr><tr><td> $D _ { \mathsf { b } _ { i } }$   $D _ { \mathrm { { g } } }$ </td><td>diffusion coefficient of bubble-i  $( \mathrm { m } ^ { 2 } / \mathrm { s } )$  diffusion coefficient of gas atom (m²/s)</td><td> $l _ { j }$ </td><td>ble-i into bubble-i  $( j > i ) \ ( \mathrm { m } ^ { 3 } / \mathrm { s } )$  distance between bubble-j&#x27;s</td></tr><tr><td> $D _ { \mathrm { s } }$ </td><td>surface diffusion coefficient  $( \mathrm { m } ^ { 2 } / \mathrm { s } )$ </td><td> $N _ { \mathsf { b } _ { i } }$ </td><td>bubble-i concentration (bub-i/m³)</td></tr><tr><td> $D _ { \mathrm { s _ { 0 } } }$ </td><td>surface diffusion constant (m²/s)</td><td> $P _ { i j }$ </td><td>probability of bubble-i to collide with</td></tr><tr><td> $E _ { \mathrm { b b } }$ </td><td>empirical bias factor for bubble diffusion</td><td></td><td>bubble-j due to radial growth of bubble-i</td></tr><tr><td></td><td>to other bubbles</td><td> $Q _ { \mathrm { g } }$ </td><td>activation energy of gas atom diffusion</td></tr><tr><td> $E _ {  { \mathsf { b b } } _ { 4 } }$ </td><td>empirical bias factor for bubble diffusion to open bubbles</td><td> $Q _ { \mathrm { s } }$ </td><td>(cal/gm mole) activation energy of surface diffusion</td></tr><tr><td> $E _ { \mathrm { c } }$ </td><td>empirical correction constant for bubble jump rate</td><td> $r _ { \mathsf { b } _ { i } }$ </td><td>(cal/gm mole) radius of bubble-i (m)</td></tr><tr><td> $E _ { \mathrm { g b } _ { i } }$ </td><td>empirical bias factor for gas diffusion to</td><td> $r _ { \mathsf { b } _ { i } }$ </td><td>bubble radius (m)</td></tr><tr><td> $F$ </td><td>the bubble-i fission density (fission/s m)</td><td> $S _ { \mathrm { b } }$   $S _ { \mathrm { c } }$ </td><td>bubble swelling swelling by the closed bubbles</td></tr><tr><td> $f _ { i , i + 1 }$ </td><td>transition probability of bubble-i into</td><td> $S _ { \mathrm { o } }$ </td><td>swelling by the open bubbles</td></tr><tr><td></td><td>bubble-i+1 by collision with bubble-i</td><td> $S _ { \mathrm { t } }$ </td><td>total swelling by the closed and open</td></tr><tr><td> $f _ { \mathrm { s } }$ </td><td>fractional surface area of a closed bubble</td><td></td><td>bubbles</td></tr><tr><td></td><td>after interconnected to the open bubbles</td><td> $S _ { \mathrm { b } }$ </td><td>bubble swelling</td></tr><tr><td> $f _ { \mathrm { t h } }$ </td><td>fraction of closed bubbles to be open at</td><td> $\Delta t$ </td><td>time increment(s)</td></tr><tr><td></td><td></td><td></td><td></td></tr><tr><td></td><td>the threshold closed bubble swelling</td><td> $v _ { \mathsf { b } _ { i } }$ </td><td>volume of a bubble-i (m³)</td></tr><tr><td></td><td></td><td> $Y$ </td><td></td></tr><tr><td></td><td></td><td></td><td>fission yield of gas atoms (atoms/fission)</td></tr></table>

## 2. Modelling of ®ssion gas behavior

A schematic diagram of the ®ssion gas bubble nucleation and growth in the metallic fuel is shown in Fig. 2. Fission gas atoms are generated by ®ssion, and then nucleate bubbles or diuse into bubbles. Fission gas bubbles are assumed to nucleate isotropically from the gas atoms in the metallic fuel matrix, since they can nucleate at both the grain boundaries and the phase boundaries which are randomly distributed inside the grain. Bubbles can grow by the diusion of gas atoms into them. Bubbles are classi®ed into three classes of bubbles-1, 2 and 3 depending upon their sizes. The open bubbles, which are connected to each other and open to the external free space are de®ned as a fourth bubble type. Open bubbles are assumed to be of the same type as the closed bubbles. When the closed bubble-i becomes the open bubble, it is assumed to be transformed to bubble-4i.

When fuel matrix swelling due to the closed bubbles reaches a threshold value, it is assumed that a certain fraction of the bubbles are interconnected with each other to make the path connected to the external free space and to become open bubbles. Monte Carlo simulations for the relation of the closed bubble swelling, bubble interconnection and open bubble formation based upon the percolation model were performed by Massih [11] for two geometries of the simple cubic (SC) and the simple quadratic (SQ) lattices. For the UO2 fuel where bubbles nucleate and grow preferentially at the boundaries of the grain, a two-dimensional quadratic geometry needs to be applied. However, when bubbles nucleate isotropically in the matrix of a fuel like the U±Pu±10Zr metallic fuel in the fast reactor, threedimensional cubic geometry should be applied.

![](images/041fbbea353d462d2366ce02476370e6e3a6490b46a7bca276a21d18d1eb9e6e.jpg)  
Fig. 1. Fission gas release of ANL fuel irradiation tests [3].

According to the above bubble classi®cation, behavior of ®ssion gas atoms and bubbles can be described as follows.

Bubble-1 is nucleated from the fuel matrix depending upon the gas atom concentrations. Bubble-1 can collide with each other by both diusion and growth and then grow to bubble-2 with the probability depending upon the dierence of the bubble sizes between bubble-1 and bubble-2. Bubble-1 can also collide with bubble-2, 3 or 4 and be absorbed into them.

Bubble-2 can collide with each other and grow to bubble-3 with the probability depending upon the sizes of bubble-2 and bubble-3. Bubble-2 can also collide with bubble-3 or 4 and be incorporated to them. However, when bubble-2 collides with bubble-1, it absorbs bubble-1.

Since bubble-3 is the largest in size among the closed bubbles, their collision with each other does not result in the formation of a higher class of closed bubbles and therefore, bubble-3 is assumed to remain bubble-3 after their collision. The negligence of further growth of bubble-3 by collision with other bubble-3's could be justi®ed by the very low mobility of bubble-3 due to its larger size. However, when bubble-3 collides with bubble-4, the open bubble, it becomes the open bubble. When bubble-3 collides with bubbles-1 and 2, it absorbs them.

The open bubble, bubble-4 consists of bubbles-41, 42 and 43, depending upon the type of the bubble just before it was transformed into an open bubble. Open bubbles are assumed not to move by diusion and not to grow by gas diusion since gases in the open bubbles are released out of the fuel.

The diusion coecients of the bubbles depend upon bubble size and temperature. Collision of bubble-i with bubble-j due to the radial growth of bubble-i by gas atom diusion depends upon the amount of radial growth and the distance between bubble-i and bubble-j.

Based upon the percolation theory [11], it is assumed that after volume swelling by closed bubbles such as bubbles-1, 2 and 3 reaches the threshold value, some fractions of bubbles-1, 2 and 3 are interconnected with each other to form the open channel to the external free space, and therefore become the so-called open bubble, bubble-4. Fission gases in the interconnected open bubbles are assumed to be released instantly. After threshold bubble swelling, ®ssion gases are successively released through the open bubbles by the diusion of gas atoms into the open bubbles in the matrix, or the collision of closed bubbles such as bubbles-1, 2 and 3 with open bubbles.

![](images/53819b69b1ddff71d2a3c54b77b172613a57acbf4e4810edb203c9b3b02d66a4.jpg)  
Fig. 2. Fission gas and bubble movement in the GRSIS model.

The overall behavior of ®ssion gas atoms and bubbles can be set as follows:

$$
{ \begin{array} { r l } & { { \frac { \mathrm { d } C _ { \mathrm { g } } } { \mathrm { d } t } } = { \mathrm { g e n e r a t i o n ~ b y ~ f i s s i o n } } } \\ & { \qquad - { \mathrm { ~ g a s ~ d i f f u s i o n ~ t o ~ b u b b l e s } } } \\ & { \qquad - { \mathrm { ~ b u b b l e - 1 ~ n u c l e a t i o n } } , } \end{array} }\tag{1}
$$

$$
{ \frac { \mathrm { d } C _ { \mathrm { g b _ { 1 } } } } { \mathrm { d } t } } = \mathrm { b u b b l e - 1 ~ n u c l e a t i o n }
$$

integration of bubble-1 into bubbles-2; 3 and 4 by diffusion and growth ÿ transition of bubble-1 to bubble-2 after collision with bubble-1 by diffusion and growth  instantaneous release by bubble interconnection at threshold closed bubble swelling; 2

dCgb2  integration of bubble-1 into bubble-2 by dt diffusion and growth  transition of bubble-1 to bubble-2 after collision with bubble-1 by diffusion and growth  gas diffusion to bubble-2 ÿ integration of bubble-2 into bubbles-3 and-4 by diffusion and growth transition of bubble-2 to bubble-3 after collision with bubble-2 by diffusion and growth ÿ instantaneous release by bubble interconnection at threshold closed bubble swelling; 3

dCgb3  integration of bubbles-1 and-2 into bubble-3 dt by diffusion and growth  transition of bubble-2 to bubble-3 after collision with bubble-2 by diffusion and growth  gas diffusion to bubble-3  integration of bubble-3 into bubble-4 by diffusion and growth ÿ instantaneous release by bubble interconnection at threshold closed bubble swelling; 4

$\frac { \mathrm { d } C _ { \mathrm { g b } _ { 4 } } } { \mathrm { d } t } = \mathrm { g a s }$ diffusion into bubble-4  integration of bubbles-1; 2 and 3 into bubble-4 by diffusion and growth  instantaneous increase by bubble interconnection at threshold closed bubble swelling; 5

where $C _ { \mathrm { g } }$ is the gas atom concentration in the matrix $\left( { \mathrm { a t o m s } } / { \mathrm { \dot { m } } ^ { 3 } } \right)$ and $C _ { \mathrm { g b } _ { i } }$ is the gas atom concentration as the bubble-i in the matrix atoms=m3:

Then, the balance equations of gas atoms and bubbles can be expressed as follows:

$$
\frac { \mathrm { d } C _ { g } } { \mathrm { d } t } = Y F - \left( J _ { \mathrm { g _ { 1 } } } + J _ { \mathrm { g _ { 2 } } } + J _ { \mathrm { g _ { 3 } } } + J _ { \mathrm { g _ { 4 } } } \right) - J _ { \mathrm { b _ { 1 } n u c l } } ,\tag{6}
$$

$$
\begin{array} { r l } & { \frac { \displaystyle \mathrm { d } C _ { \mathrm { g b 1 } } } { \displaystyle \mathrm { d } t } = J _ { \mathrm { b 1 n u c l } } + J _ { g 1 } - ( a b _ { 1 2 } + a b _ { 1 3 } + a b _ { 1 4 } ) } \\ & { - \ : \mathrm { ( } g a b _ { 1 2 } + g a b _ { 1 3 } + g a b _ { 1 4 } + g a b _ { 2 1 } + g a b _ { 3 1 } ) } \\ & { - f _ { 1 2 } ( a b _ { 1 1 } + g a b _ { 1 1 } ) - \mathrm { i n s t a n t a n e o u s ~ r e l e a s e ~ b y ~ b u b b l e } } \\ & { \mathrm { i n t e r c o n n e c t i o n ~ a t ~ t h r e s h o l d ~ c l o s e d ~ b u b b l e ~ s w e l l i n g , } } \end{array}\tag{7}
$$

$$
\begin{array} { r l } & { \frac { \mathrm { d } C _ { \mathrm { g b 2 } } } { \mathrm { d } t } = J _ { g _ { 2 } } + a b _ { 1 2 } + g a b _ { 1 2 } + f _ { 1 2 } ( g a b _ { 1 1 } + a b _ { 1 1 } ) } \\ & { - \left( a b _ { 2 3 } + a b _ { 2 4 } \right) - ( g a b _ { 2 3 } + g a b _ { 2 4 } + g a b _ { 3 2 } ) } \\ & { - f _ { 2 3 } ( a b _ { 2 2 } + g a b _ { 2 2 } ) - \mathrm { i n s t a n t a n e o u s ~ r e l e a s e ~ b y ~ b u b b l e } } \\ & { \mathrm { i n t e r c o n n e c t i o n ~ a t ~ t h r e s h o l d ~ c l o s e d ~ b u b b l e ~ s w e l l i n g , } } \end{array}\tag{8}
$$

$$
\begin{array} { l } { \displaystyle \frac { \mathrm { d } C _ { \mathrm { g b _ { 3 } } } } { \mathrm { d } t } = J _ { g _ { 3 } } + a b _ { 1 3 } + a b _ { 2 3 } + g a b _ { 1 3 } + g a b _ { 2 3 } + g a b _ { 3 1 } } \\ { \displaystyle + g a b _ { 3 2 } + f _ { 2 3 } ( a b _ { 2 2 } + g a b _ { 2 2 } ) - ( a b _ { 3 4 } + g a b _ { 3 4 } ) } \end{array}\tag{9}
$$

$$
\begin{array} { r l } & { \frac { \mathrm { d } C _ { \mathrm { g b } _ { 4 } } } { \mathrm { d } t } = J _ { g _ { 4 } } + a b _ { 1 4 } + a b _ { 2 4 } + a a b _ { 3 4 } + g a b _ { 1 4 } + g a b _ { 2 4 } } \\ & { + g a b _ { 3 4 } + \mathrm { i n s t a n t a n e o u s ~ i n c r e a s e ~ b y ~ b u b b l e ~ } } \\ & { \mathrm { i n t e r c o n n e c t i o n ~ a t ~ t h r e s h o l d ~ c l o s e d ~ b u b b l e ~ s w e l l i n g , } } \end{array}\tag{10}
$$

where Y is the ®ssion yield of gas atoms atoms=fission, $F$ is the ®ssion density fission $/ \mathrm { ~ s ~ m ~ } ^ { 3 } ) , J _ { \mathrm { g } _ { i } }$ is the gas diffusion to bubble-i atoms=s m3, ${ J } _ { \mathrm { b _ { 1 } n u c l } }$ is the bubble-1 nucleation rate atoms=s m3, $a b _ { i j }$ is the integration rate of bubble-i into bubble-j by bubble diusion atoms=s m3, $g a b _ { i j }$ is the integration rate of bubble-i into bubble-j by radial growth of bubble-i due to gas diusion to bubble-i atoms=s m3 and $f _ { i , i + 1 }$ is the transition probability of bubble-i into bubble-i  1 by collision with bubble-i.

The relation of bubble density, $N _ { \mathsf { b } _ { i } }$ and total gas atom density of bubble-i, $C _ { \mathrm { g b } _ { i } }$ is

$$
C _ { \mathrm { g b } _ { i } } = a t n b _ { i } \cdot N _ { \mathfrak { b } _ { i } } ,\tag{11}
$$

where atnbi is the density of gas atom in a bubble-i (atoms/bub-i) and $N _ { \mathsf { b } _ { i } }$ is the bubble-i concentration (bub-i/m3).

Collision rate of bubble-i with the open bubbles by diusion and growth, respectively are:

$$
a b _ { i 4 } = a b _ { i 4 1 } + a b _ { i 4 2 } + a b _ { i 4 3 } ,\tag{12}
$$

$$
g a b _ { i 4 } = g a b _ { i 4 1 } + g a b _ { i 4 2 } + g a b _ { i 4 3 } .\tag{13}
$$

Then, the balance equations of open bubbles are as follows:

$$
\begin{array} { c } { { \displaystyle { \frac { \mathrm { d } C _ { g b _ { 4 1 } } } { \mathrm { d } t } = a t n b _ { 1 } \cdot \frac { \mathrm { d } } { \mathrm { d } t } N _ { \mathfrak { b } _ { 4 1 } } } } } \\ { { = a b _ { 1 4 1 } + a b _ { 1 4 2 } + a b _ { 1 4 3 } + g a b _ { 1 4 1 } + g a b _ { 1 4 2 } } } \\ { { + g a b _ { 1 4 3 } , } } \end{array}\tag{14}
$$

$$
\begin{array} { c } { { \displaystyle { \frac { \mathrm { d } C _ { g b _ { 4 2 } } } { \mathrm { d } t } = a t n b _ { 2 } \cdot \frac { \mathrm { d } } { \mathrm { d } t } N _ { \mathfrak { b } _ { 4 2 } } } } } \\ { { = a b _ { 2 4 1 } + a b _ { 2 4 2 } + a b _ { 2 4 3 } + g a b _ { 2 4 1 } + g a b _ { 2 4 2 } } } \\ { { + g a b _ { 2 4 3 } } } \end{array}\tag{15}
$$

$$
\begin{array} { c } { { \displaystyle { \frac { \mathrm { d } C _ { g b _ { 4 3 } } } { \mathrm { d } t } = a t n b _ { 3 } \cdot \frac { \mathrm { d } } { \mathrm { d } t } N _ { \mathfrak { b } _ { 4 3 } } } } } \\ { { = a b _ { 3 4 1 } + a b _ { 3 4 2 } + a b _ { 3 4 3 } + g a b _ { 3 4 1 } + g a b _ { 3 4 2 } } } \\ { { + g a b _ { 3 4 3 } . } } \end{array}\tag{16}
$$

The speci®c parameters of gas atoms and bubbles in the above equations can be obtained as follows.

Bubble-1 nucleation rate, ${ J } _ { \mathrm { b _ { 1 } n u c l } }$ is obtained from bubble nucleation constant and gas atom concentration in the fuel matrix, such that

$$
J _ { \mathrm { b _ { 1 } n u c l } } = k _ { \mathrm { b _ { 1 } n u c l } } \cdot C _ { \mathrm { g } } \cdot a t n b _ { l } ,\tag{17}
$$

where $k _ { \mathrm { b _ { 1 } n u c l } }$ is the bubble-1 nucleation constant (bub-1/s atom).

Diusion of gas atoms into the bubbles can be calculated from the analytical solution in the case that gas atoms diuse into the spherical sink [12]. Atomic ¯ux into bubble-i by diusion, $J _ { \mathbf { g } _ { i } }$ can be calculated as a function of the gas diusion constant and the concentrations of gas and bubbles are as follows:

$$
J _ { \mathrm { g } _ { i } } = k _ { \mathrm { g } _ { i } } \cdot C _ { \mathrm { g } } \cdot N _ { \mathrm { b } _ { i } } ,\tag{18}
$$

$$
k _ { \mathrm { g } _ { i } } = E _ { \mathrm { g b } _ { i } } \cdot ( 4 \pi r _ { \mathrm { b } _ { i } } ) \cdot D _ { \mathrm { g } } ,\tag{19}
$$

where $k _ { \mathrm { g } _ { i } }$ is the gas diusion constant to bubble-i $( \mathbf { m } ^ { 3 } / \mathbf { s } ) .$ $E _ { \mathrm { g b } _ { i } }$ is the empirical bias factor for gas diusion to the bubble-i, $r _ { \mathsf { b } _ { i } }$ is the radius of bubble-i (m) and $D _ { \mathrm { g } }$ is the diusion coecient of gas atom (m2/s).

The bubble diusion coecient can be calculated by a function of surface diusion coecient Ds and bubble characteristics [12]

$$
D _ { \mathsf { b } _ { i } } = \frac { 3 a _ { 0 } ^ { 4 } } { 2 \pi r _ { \mathsf { b } _ { i } } ^ { 4 } } D _ { \mathsf { s } } ,\tag{20}
$$

where $D _ { \mathsf { b } _ { i } }$ is the diusion coecient of bubble-i $( \mathrm { m } ^ { 2 } / \mathrm { s } )$ and $a _ { 0 } ^ { 2 }$ is the area occupied by a gas atom at the bubble surface m2:

Surface diusion coecient, $D _ { \mathrm { s } }$ can be obtained by

$$
D _ { \mathrm { s } } = D _ { \mathrm { s } _ { 0 } } \exp ( - Q _ { \mathrm { s } } / k T ) ,\tag{21}
$$

where $D _ { \mathrm { s } }$ is the surface diusion coecient $( \mathrm { m } ^ { 2 } / \mathrm { s } ) , D _ { \mathrm { s _ { 0 } } }$ is the surface diusion constant $( \mathbf { m } ^ { 2 } / \mathbf { s } )$ and $Q _ { \mathrm { s } }$ is the activation energy of surface diusion (cal/gm mole).

Bubbles can collide with each other by diusional movement so that collision constant of bubble-i and bubble-j by bubble diusion, $k _ { i j } \ ( \mathbf { m } ^ { 3 } / \mathbf { s } )$ [12] is

$$
\begin{array} { r l } {  { k _ { i j } = E _ { \mathrm { b b } } \cdot 4 \pi ( r _ { \mathrm { b } i } + r _ { \mathrm { b } j } ) ( D _ { \mathrm { b } i } + D _ { \mathrm { b } j } ) } } \\ & { \cong E _ { \mathrm { b b } } \cdot 4 \pi r _ { \mathrm { b } j } \cdot D _ { \mathrm { b } i } } \\ & { = E _ { \mathrm { b b } } \cdot 4 \pi r _ { \mathrm { b } j } \cdot \frac { 3 a _ { 0 } ^ { 4 } D _ { \mathrm { s } } } { 2 \pi r _ { \mathrm { b } i } ^ { 4 } } } \\ & { = 6 E _ { \mathrm { b b } } \cdot a _ { 0 } ^ { 4 } \cdot \frac { r _ { \mathrm { b } j } } { r _ { \mathrm { b } i } ^ { 4 } } D _ { \mathrm { s } } , j > i \mathrm { a n d } r _ { \mathrm { b } j } \gg r _ { \mathrm { b } i } , } \end{array}\tag{22}
$$

where $E _ { \mathrm { b b } }$ is the empirical bias factor for bubble diusion to other bubbles and $k _ { i j }$ is the collision or integration constant of bubble-i into bubble- $j \ ( \mathrm { m } ^ { 3 } / \mathrm { s } )$ .

Then, the integration rate of bubble-i into bubble-j by bubble diusion $( j > i )$ is

$$
a b _ { i j } = k _ { i j } \cdot N _ { \mathbf { b } _ { i } } \cdot N _ { \mathbf { b } _ { j } } \cdot a t n b _ { i } .\tag{23}
$$

When the number density of bubble-i is $N _ { \mathsf { b } _ { i } }$ , the average distance between bubble-i's can be calculated by assuming FCC (face centered cubic) where there are four bubbles in a cubic lattice [12]. Fig. 3 shows the bubble distribution in a single surface of FCC lattice. The distance between bubbles $( l _ { j } )$ can be calculated from the lattice constant, $a _ { j }$ as $l _ { j } ^ { ' } = ( \sqrt { 2 } / 2 ) a _ { j }$ Bubble swelling $( S _ { \mathrm { b } } )$ is the total bubble volume in an FCC lattice or total bubble volume per unit volume. Therefore,

$$
S _ { \flat } = { \frac { 4 \cdot ( 4 / 3 ) \pi r _ { \flat _ { j } } ^ { 3 } } { a _ { j } ^ { 3 } } } = N _ { \flat _ { j } } \cdot { \frac { 4 } { 3 } } \pi r _ { \flat _ { j } } ^ { 3 } .\tag{24}
$$

![](images/957b072cc6884895146ad5951b8e062bee6984922cb37286636e30a1732413d9.jpg)  
Fig. 3. Average distance between the bubbles.

The relation of lattice constant and bubble number density is

$$
a _ { j } = \left( \frac { 4 } { N _ { \mathrm { b } _ { j } } } \right) ^ { 1 / 3 } .\tag{25}
$$

And therefore, the average distance $( l _ { j } )$ between bubbles can be obtained by

$$
l _ { j } = \frac { \sqrt { 2 } } { 2 } a _ { j } = 1 . 1 2 2 \cdot N _ { \mathrm { b } _ { j } } ^ { - 1 / 3 } .\tag{26}
$$

When there is a bubble-i in the space where bubble-$j ^ { \circ } \mathbf { s }$ are evenly distributed at the number density, $N _ { \mathsf { b } _ { j } }$ with their distance, $l _ { j }$ as shown in Fig. 4, the average distance between the centers of bubble-i and bubble-j is $0 . 2 5 ~ l _ { j }$ and the distance between the surfaces of bubble-i and bubble-j is 0.25 $l _ { j } - \left( r _ { \mathsf { b } _ { i } } + r _ { \mathsf { b } _ { j } } \right)$ . Therefore, the probability of bubble-i colliding with bubble-j due to the radial growth of bubble-i, $P _ { i j }$ is

$$
\begin{array} { r } { P _ { i j } = \frac { \mathrm { r a d i a l ~ g r o w t h ~ o f ~ b u b b l e } - i } { \mathrm { d i s t a n c e ~ b e t w e e n ~ t h e ~ s u r f a c e s ~ o f ~ b u b b l e } - i \mathrm { ~ a n d ~ } j } } \\ { = \frac { \Delta r _ { \mathrm { b } _ { i } } } { 0 . 2 5 1 _ { j } - ( r _ { \mathrm { b } _ { i } } + r _ { \mathrm { b } _ { j } } ) } . \qquad ( 2 ^ { \prime } \mathrm { ~ a n d ~ } j } \end{array}\tag{}
$$

The radial growth of bubble-i by gas diusion to a bubble-i, $j _ { \mathrm { { g } } _ { i } }$ can be calculated from the following equations. The volume increase $( \Delta \nu _ { \mathsf { b } _ { i } } )$ and radial growth $( \Delta r _ { \mathsf { b } _ { i } } )$ of a bubble-i by gas diusion are:

$$
\Delta \nu _ { \mathsf { b } _ { i } } = j _ { \mathsf { g } _ { i } } \cdot \frac { \nu _ { \mathsf { b } _ { i } } } { a t n b _ { i } } \cdot \Delta t ,\tag{28}
$$

$$
\Delta r _ { \mathsf { b } _ { i } } = \frac { \Delta \nu _ { \mathsf { b } _ { i } } } { 4 \pi r _ { \mathsf { b } _ { i } } ^ { 2 } } = \frac { r _ { \mathsf { b } _ { i } } j _ { \mathsf { g } _ { i } } \Delta t } { 3 a t n b _ { i } } ,\tag{29}
$$

where $j _ { \mathbf { g } _ { i } }$ is the gas atom diusion to a bubble-i (atoms/ bub-i s), $V _ { \mathsf { b } _ { i } }$ is the volume of a bubble-i $( \mathbf { m } ^ { 3 } )$ and Dt is the time increment (s).Then, collision or integration rate of

![](images/4ef331b64a1191a5f93fe90012ab390f9b43711d7ae87c8f6e3d0d8d0303f68a.jpg)  
Fig. 4. Average distance between surfaces of the bubble-i and bubble-j's.

bubble-i with bubble-j by radial growth of bubble-i, $g a b _ { i j }$ (atoms/s m3) can be calculated by

$$
g a b _ { i j } = P _ { i j } \cdot a t n b _ { i } \cdot N _ { \mathsf { b } _ { i } } .\tag{30}
$$

Jump or transition rate of bubble-i into bubble-i  1 after the collision with bubble-i can be obtained by

$$
a b _ { i i } = k _ { i i } \cdot N _ { \mathrm { b } _ { i } } ^ { 2 } \cdot 2 a t n b _ { i } ,\tag{31}
$$

where $a b _ { i i }$ is the jump or transition rate of bubble-i into bubble $i + 1$ (atoms/s $\mathbf { m } ^ { 3 } )$ and $k _ { i i }$ is the jump rate constant of bubble-i into bubble-i  1 (m3/s).

Jump rate constant of bubble-i into bubble-i  1, $k _ { i i }$ $( \mathrm { m } ^ { 3 } / \mathrm { s } )$ is

$$
\begin{array} { r l } & { k _ { i i } = E _ { \mathrm { c } } \cdot 4 \pi \cdot 2 { r _ { \mathrm { b } _ { i } } } \cdot 2 { D _ { \mathrm { b } _ { i } } } \cdot f _ { i , i + 1 } } \\ & { \quad \quad = 2 4 \cdot E _ { \mathrm { c } } a _ { 0 } ^ { 2 } \frac { { D _ { \mathrm { s } } } } { { r _ { \mathrm { b } _ { i } } ^ { 3 } } } f _ { i , i + 1 } , } \end{array}\tag{32}
$$

where $E _ { \mathrm { c } }$ is the empirical correction constant for bubble jump rate and $f _ { i , i + 1 }$ is the transition probability of bubble-i into bubble-i  1 by collision with bubble-i, $f _ { i , i + 1 }$ can be obtained by

$$
f _ { i , i + 1 } = { \frac { 2 a t n b _ { i } } { a t n b _ { i + 1 } } } .\tag{33}
$$

When a bubble-i is incorporated into the open bubbles, it is assumed to become the open bubble-4i. After absorption of bubble-i by the open bubble, gases in the bubble-i are assumed to be released into free space which has a lower pressure than bubble-i and therefore, the surface area and volume of bubble-i may decrease as illustrated in Fig. 5. Therefore, when a bubble-i becomes the open bubble, its volume and surface area may be reduced to certain fractions of the initial values such as $f _ { \mathrm { v } }$ and $f _ { \mathrm { s } } ,$ respectively.

Therefore, from Eq. (23), the volume, $V _ { 4 }$ and surface area, $A _ { 4 }$ of the open bubbles, bubble-4 can be calculated by:

$$
\frac { \mathrm { d } V _ { 4 } ( t ) } { \mathrm { d } t } = f _ { \mathrm { v } } N _ { \mathrm { b } _ { 4 } } ( k _ { 1 4 } N _ { \mathrm { b } _ { 1 } } \nu _ { \mathrm { b } _ { 1 } } + k _ { 2 4 } N _ { \mathrm { b } _ { 2 } } \nu _ { \mathrm { b } _ { 2 } } + k _ { 3 4 } N _ { \mathrm { b } _ { 3 } } \nu _ { \mathrm { b } _ { 3 } } ) ,\tag{34}
$$

$$
\frac { \mathrm { d } { A } _ { 4 } ( t ) } { \mathrm { d } t } = f _ { \mathrm { s } } N _ { \mathrm { b } _ { 4 } } ( k _ { 1 4 } N _ { \mathrm { b } _ { 1 } } a _ { \mathrm { b } _ { 1 } } + k _ { 2 4 } N _ { \mathrm { b } _ { 2 } } a _ { \mathrm { b } _ { 2 } } + k _ { 3 4 } N _ { \mathrm { b } _ { 3 } } a _ { \mathrm { b } _ { 3 } } ) .\tag{35}
$$

Total swelling by the closed bubbles, $S _ { \mathrm { c } }$ is

$$
\begin{array} { r } { S _ { \mathrm { c } } = V _ { 1 } + V _ { 2 } + V _ { 3 } . } \end{array}\tag{36}
$$

![](images/ed2d1e930547e30ca2aae643d4928fe8b4db92ade70322d71211022c5baee0b8.jpg)  
Fig. 5. Illustration of bubble coalescence.

Total volume of bubble-i, Vi is

$$
V _ { i } = \nu _ { i } N _ { \mathrm { b } _ { i } } = \frac { 4 } { 3 } \pi r _ { \mathrm { b } _ { i } } ^ { 3 } N _ { \mathrm { b } _ { i } } \quad ( i = 1 , 2 , 3 ) .\tag{37}
$$

When the swelling by the closed bubbles reaches the threshold swelling $( S _ { \mathrm { t h } } )$ for bubble interconnection to be open to the external free space, a certain fraction of the bubbles become the open bubbles instantaneously. Therefore, when $S _ { \mathrm { c } } \geqslant S _ { \mathrm { t h } } .$ , volume and surface area of the closed and open bubbles change as follows:

$$
\begin{array} { r l } & { V _ { i } \to ( 1 - f _ { \mathrm { t h } } ) V _ { i } , \quad i = 1 , 2 , 3 , } \\ & { V _ { 4 } = f _ { \mathrm { t h } } f _ { \mathrm { v } } ( V _ { 1 } + V _ { 2 } + V _ { 3 } ) . } \end{array}\tag{38}
$$

$$
\begin{array} { r l } & { A _ { i }  ( 1 - f _ { \mathrm { t h } } ) A _ { i } , \quad i = 1 , 2 , 3 , } \\ & { A _ { 4 } = f _ { \mathrm { t h } } f _ { \mathrm { s } } ( A _ { 1 } + A _ { 2 } + A _ { 3 } ) , } \end{array}\tag{39}
$$

where $f _ { \mathrm { s } }$ is the fractional surface area of a closed bubble after interconnected to the open bubbles, $f _ { \mathrm { t h } }$ is the fraction of closed bubbles to be open at the threshold closed bubble swelling and $f _ { \mathrm { v } }$ is the fractional volume of a closed bubble after interconnected to the open bubbles.

Total swelling by the closed and open bubbles is

$$
S _ { \mathrm { t } } = S _ { \mathrm { c } } + S _ { \mathrm { o } } = V _ { 1 } + V _ { 2 } + V _ { 3 } + V _ { 4 } .\tag{40}
$$

Then, ®ssion gas release (FGR) can be calculated as follows:

$$
\begin{array} { r l } & { \mathrm { F G R } = 0 , \quad S _ { \mathrm { t } } < S _ { \mathrm { t h } } } \\ & { \qquad = f _ { \mathrm { t h } } \big ( C _ { \mathrm { g b _ { 1 } } } + C _ { \mathrm { g b _ { 2 } } } + C _ { \mathrm { g b _ { 3 } } } \big ) , \quad S _ { \mathrm { t } } = S _ { \mathrm { t h } } } \\ & { \qquad = C _ { \mathrm { g b _ { 4 } } } , \quad S _ { \mathrm { t } } > S _ { \mathrm { t h } } . } \end{array}\tag{41}
$$

According to the Monte Carlo simulation of percolation theory for SC lattice geometry, the critical concentration of bubbles $( P _ { \mathrm { c } } )$ is 0.32 and the fractional volume of the bubbles $( V _ { \mathrm { S C } } )$ is 0.17 [11]. Then, the critical swelling for the interlinked tunnel formation by bubble interconnection is calculated as follows:

$$
\left( \frac { \Delta V } { V } \right) _ { \mathrm { S C } } = \frac { V _ { \mathrm { S C } } } { 1 - V _ { \mathrm { S C } } } = 0 . 2 .\tag{42}
$$

Critical swelling in SC lattice geometry is independent of the size of bubble and lattice constant. When $P _ { \mathrm { c } }$ is 0.32 in SC lattice geometry, the fraction of bubbles in the largest cluster, that is, the open bubbles, $F _ { \mathrm { S C } } ^ { \infty }$ is about 0.54 [11]. The above calculation is based upon a random distribution of bubbles which are of the same size and sphere shape. Therefore, critical swelling and fraction of bubbles in the largest cluster may change depending upon variations in size and shape of bubbles.

Calculation ¯ow of the GRSIS (Gas Release and Swelling in ISotropic fuel matrix) program [13] is shown in Fig. 6. Bubbles are classi®ed in terms of radius, surface area, volume and atomic density. Bubble sizes should be selected from the microstructure analysis of the irradiated fuels. Threshold swelling and fraction of interconnected bubbles at the threshold swelling need to be set. The next step is reading of the irradiation history, such as time, ®ssion rate and temperature. From the irradiation condition of the fuel, rate constants of the ®ssion gas and bubble movements are calculated. Then, concentrations of gas atoms and bubbles are calculated. Bubble swelling is calculated from the bubble concentrations and threshold swelling for bubble interconnection to be open to the external open space is checked. Then, the fuel gap closure by fuel swelling is checked. When the fuel swelling becomes larger than the fuel gap allowance, bubble swelling is recalculated after increasing the contact pressure between fuel and cladding. As the contact pressure increases, fuel swelling by bubbles decreases. Therefore, it is iterated until fuel swelling is equal to the fuel gap allowance and then, the contact pressure is determined.

Input variables in the GRSIS model are fuel design parameters, a set of bubble characterizations, threshold bubble swelling and a fraction of interconnected bubbles and irradiation histories such as time, ®ssion density and temperature. Then, the output of the GRSIS model is gas atom concentrations in the matrix, concentrations of bubbles, swelling by closed and open bubbles, ®ssion gas release and contact pressure between fuel and cladding.

## 3. Model evaluation

Table 1 shows the reference data of the variables upon which evaluation of the GRSIS model is based. Fig. 7 shows the general swelling behavior of the fuel irradiated at $5 5 0 ^ { \circ } \mathrm { C }$ as predicted by the GRSIS model. Fuel swelling by the solid ®ssion products increases linearly with the burnup [2]. After some incubation time, the swelling by closed bubbles starts to increase and at the threshold swelling, the open bubbles are assumed to form instantaneously in the GRSIS model.

When total fuel swelling reaches the allowable limit due to gap closure, the contact stress between the fuel and the cladding starts to increase with the burnup. During this period, swelling by closed bubbles decreases due to increase in external pressure on the closed bubble while fraction of open bubbles increases. When the contact stress reaches the yield stress of the porous fuel, fuel deformation occurs while the contact stress is not changed. Fuel deformation occurs by collapse of open bubbles and therefore, the fraction of open bubbles decreases during this period while the fraction of closed bubbles increases since the contact stress does not increase anymore due to fuel deformation. When all the open bubbles have collapsed due to fuel deformation, fuel is allowed to expand or slide in an axial direction since the radial constraint stress from the cladding is higher than the yield stress of the porous fuel.

![](images/b93309de97605395e3d81f00cd337cd5db7fdfc6723f8554cc09a37f325bbcc8.jpg)  
Fig. 6. Calculation ¯ow of the GRSIS model.

Fig. 8 compares the fractional ®ssion gas release versus the burnup with the measured data from the irradiation tests of U±10Zr, U±8Pu±10Zr and U±19Pu± 10Zr fuels [3]. There is not much dierence among the dierent fuels. In calculations by the GRSIS program, the fuel temperature was assumed to be 550°C during the irradiation. It can be seen that the GRSIS model could predict the general behavior of the metallic fast reactor fuels, even though anisotropic swelling of U± (Pu)±Zr fuel at low temperature such as cavitational void swelling [10] is not considered in the GRSIS model.

Parametric study of the key variables in the GRSIS model was performed as follows.

## 3.1. Diusion coecient of ®ssion gas atoms

There are several correlations available for the diffusion coecients of the elements in the uranium alloy fuel [7,14,15]. However, there still exists a large dierence among the correlations, as much as a factor of 10 100. In the GRSIS model, Adda's correlation for U±10Zr fuel [14] is used. Then, the surface diusion coecient of the gas atoms was assumed to be larger than the matrix diusion coecient of the gas atoms by a factor of $1 0 ^ { 3 }$ [12]. Fig. 9 shows the ®ssion gas release and bubble swelling behavior when the gas diusion coecient is changed while the temperature is ®xed. When the diusion coecient is changed by a factor of 100, there is no signi®cant change in ®ssion gas release behavior, which means that when the gas diusion coecient is greater than a certain value, it does not further enhance the ®ssion gas release and swelling. However, when the gas diusion coecient is reduced, bubble swelling rate decreases so that ®ssion gas release by bubble interconnection occurs at higher burnup.

Table 1  
Reference data of the GRSIS variables for U±PU±10Zr fuel
<table><tr><td>Class</td><td>Variables</td><td>Value</td></tr><tr><td rowspan="4">Bubble characteristics</td><td>Radius of bubble-1  $( r _ { \mathsf { b } _ { 1 } } , \mathsf { \mu m } )$ </td><td>0.5</td></tr><tr><td>Radius of bubble-2  $( r _ { \mathsf { b } _ { 2 } }$  ，μm)</td><td>2.5</td></tr><tr><td>Radius of bubble-3(rb，μm)</td><td>12.5</td></tr><tr><td>Surface tension (N/m)</td><td>1.0</td></tr><tr><td rowspan="9">Diffusion related constants [14,15]</td><td>Gas diffusion factor  $( D _ { \mathrm { g o } } , \ \mathrm { m } ^ { 2 } / \mathrm { s } )$ </td><td> $9 . 5 \times 1 0 ^ { 8 }$ </td></tr><tr><td>Activation energy of gas diffusion  $( Q _ { \mathrm { g } } ,$  cal/gm mole)</td><td>32,000</td></tr><tr><td>Surface diffusion factor  $( D _ { \mathrm { s _ { 0 } } } , \ \mathrm { m } ^ { 3 } / \mathrm { s } )$ </td><td> $9 . 5 \times 1 0 ^ { 5 }$ </td></tr><tr><td>Activation energy of surface diffusion  $\left( Q _ { \mathrm { s } } , { \mathrm { c a l / g m ~ m o l e } } \right)$ </td><td> $^ { 3 2 , 0 0 0 }$ </td></tr><tr><td>Area occupied by surface molecule  $( a _ { 0 } ^ { 2 } , \ m ^ { 2 } )$ </td><td> $9 \times 1 0 ^ { - 2 0 }$ </td></tr><tr><td>Bubble-1 nucleation constant  $( k _ { \mathrm { b _ { 1 } n u c l } }$  ,bub-1/s atom)</td><td> $1 \times 1 0 ^ { - 2 0 }$ </td></tr><tr><td>Bias factor of gas diffusion to closed bubble  $( E _ { \mathrm { g b } _ { i } } , \ i = 1 , 2 , 3 )$ </td><td>1.0</td></tr><tr><td>Bias factor of gas diffusion to open bubble  $( E _ { \mathrm { g b } _ { 4 } } )$ </td><td>1.0</td></tr><tr><td>Biasfactor of bubblediffusionto closed bubble  $( E _ { \mathrm { b b } } )$   $( E _ { \mathrm { { b b } _ { 4 } } } )$ </td><td>1.0</td></tr><tr><td rowspan="5">Threshold swelling</td><td>Bias factor of bubble diffusion to open bubble</td><td>1.0</td></tr><tr><td>Threshold closed bubble swelling  $( S _ { \mathrm { t h } } )$ </td><td>0.2</td></tr><tr><td>Fraction of interconnected bubbles at threshold sweling (fth) Correction factor of bubble volume after becoming open bubble</td><td>0.3 1.0</td></tr><tr><td>（f） Correction factor of bubble surface area after becoming open</td><td></td></tr><tr><td>bubble (fs)</td><td>0.6</td></tr></table>

## 3.2. Temperature

Fig. 10 shows the dependence of ®ssion gas release upon temperature. The bubble swelling rate increases with temperature so that bubble interconnection occurs at lower burnup. However, at temperatures higher than about $4 5 0 ^ { \circ } \mathrm { C } ,$ there was not much dependence of the threshold burnup and ®ssion gas release upon temperature, so that bubble swelling rate does not increase much with temperature. Temperature dependence is signi®cant only at low temperatures due to the low diffusion coecients of the gas atoms. As the temperature increases, the fraction of the closed bubbles of larger sizes increase as well as the open bubbles. That is, bubble growth and interconnection are more active at high temperatures. At temperatures less than $3 0 0 ^ { \circ } \mathrm { C } ,$ bubble swelling is so low that bubble interconnection and ®ssion gas release do not occur.

![](images/4169eb51fa087607c549ac269dd22600af6895c6bfadad11894f6a344d4ba142.jpg)  
Fig. 7. Fuel swelling and the contact pressure.

![](images/6826b841942689a031ad975e2613e74ebff70fd3a97cb3e9212320a1eb4aa692.jpg)  
Fig. 8. Comparison of the GRSIS prediction with the ANL fuel irradiation test results [3].

## 3.3. Bubble nucleation rate

Fig. 11 shows the eect of the bubble-1 nucleation rate. In the temperature region where bubble growth and gas diusion are active, there is no signi®cant eect of bubble nucleation on bubble swelling and ®ssion gas release. Once the bubble is formed in the fuel matrix, the controlling parameter is not bubble nucleation, but the growth of the larger size bubbles.

As to the ®ssion density, there is no signi®cant eect of ®ssion density on the fuel swelling and ®ssion gas release behavior. Even though the gas concentration in the matrix increases slightly with the ®ssion density, the fraction of gas atoms in the fuel matrix is very small compared with those in the bubbles.

## 3.4. Threshold swelling at bubble interconnection

Fig. 12 shows the eect of threshold swelling at bubble interconnection and the fraction of the bubbles interconnected to be open to the external free space at the point of threshold swelling. As the threshold swelling increases, the burnup at which the instantaneous ®ssion gas release by interconnection of the closed bubble occurs increases. However, after the threshold burnup, there is not much dierence in ®ssion gas release. Fractional ®ssion gas release increases with the fraction of the interconnected bubbles at the threshold bubble swelling.

## 3.5. Classi®cation of bubble sizes

In the GRSIS model, the closed bubbles are divided into three classes depending upon their sizes. The size of bubble-1 represents the minimum size of the stabilized bubbles after nucleation. Bubble-3 represents the maximum possible size of the closed bubbles grown in the fuel matrix before being open to the external space by interconnection to the open bubbles. Therefore, the sizes of bubble-1 and bubble-3 should be determined from the microstructure examination of the irradiated fuels [16,17]. Then, the size of bubble-2 need to be set in the middle of bubble-1 and bubble-3. However, the wellcharacterized data on bubble size distribution from the irradiated fuels to determine the reliable bubble size distribution are not available so that the sensitivity analysis of bubble size classi®cation was performed.

![](images/28c761347660224dcc6f933dfca85e6c79a966b2dcc4860602eeaed36a4aa292.jpg)  
Fig. 9. Eect of diusion coecient upon the fractional ®ssion gas release.

![](images/c2e07c2b9459d655e0f93bfa84e29239aab7fd61f0d90266eb548bfcbeb47db9.jpg)  
Fig. 10. Eect of temperature upon the fractional ®ssion gas release.

Fig. 13 shows the eect of bubble classi®cation upon the fuel behavior. Fuel swelling and ®ssion gas release are slightly dependent upon the dierence between bubbles-1, 2 and 3. As the size of bubble-1 decreases, the burnup at threshold swelling increases. As the sizes of bubbles-2 and 3 decrease, fractional ®ssion gas release increases due to easier growth of bubble-1 to bubbles-2 and 3, and subsequent bubble interconnection. It seems that classi®cation of bubbles-1, 2 and 3 with the radii of 0.5, 2.5 and 12.5 lm, respectively, are best ®tted to the results of the ANL metallic fuel irradiation tests [3], even though anisotropic swelling of the metallic fuel at the low temperature region such as cavity swelling [10] is not considered in the GRSIS model.

## 3.6. Fuel gap allowance for swelling

Fig. 14 shows the eect of fuel gap allowance for swelling upon fuel behavior. As the fuel gap allowance for swelling increases, fractional ®ssion gas release increases due to higher allowable fuel swelling before gap closure, while the contact pressure between fuel and cladding decreases. However, fuel behavior before fuel gap closure is not aected by fuel gap allowance for swelling.

![](images/c3b705c1699fa013ca14c903cf69cd9475fbeb592abc59e6e03b3eb78e27122a.jpg)  
Fig. 11. Eect of bubble nucleation rate upon the fractional ®ssion gas release.

![](images/306ce89fda45db2026fc7bcef589bb2ab0dcbeb4c4fa0aa20ccac4b9931389d6.jpg)  
Fig. 12. Eect of threshold swelling and interconnected bubble fraction upon the fractional ®ssion gas release.

## 3.7. Volume and area reduction of the open bubble

When closed bubbles collide with open bubbles to become open bubbles, the volume and surface area of the closed bubbles may decrease as illustrated in Fig. 5. Fig. 15 shows the eect of the volume and area reduction of closed bubbles after becoming open bubbles. As volume and area of closed bubbles decrease after they become open bubbles, fractional ®ssion gas release and open bubble swelling decrease.

## 3.8. Biased diusion of ®ssion gas atoms to the open bubble

Fig. 16 shows the eect of biased diusion of gas atoms into the open bubbles. When diusion of gas atoms to open bubbles is assumed to be two times higher than that to closed bubbles, fractional ®ssion gas release increases by about 8%.

![](images/e936d1689cd8e7fbdd2fbeb199514c79c42243c5d08b62ac36eaa4861d883548.jpg)  
Fig. 13. Eect of bubble size classi®cation upon the fractional ®ssion gas release.

![](images/341511a1a96674a2bd7245134f66eb737b6afd8af410ed4969a18221cabcb968.jpg)  
Fig. 14. Eect of fuel gap allowance for swelling upon the fractional ®ssion gas release.

![](images/4c8e847231697098811bab4c435712ecc2350bb53c4cb611ee973a9a0ebd32f0.jpg)  
Fig. 15. Eect of surface area correction factor of the open bubble upon the fractional ®ssion gas release.

![](images/f10ed50575fa771a5b410d862b3a8fccfe210e979eef59a371dd56b39f49f79e.jpg)  
Fig. 16. Eect of biased diusion to the open bubbles upon the fractional ®ssion gas release.

## 4. Conclusion and discussion

A mechanistic model of swelling and ®ssion gas release for the U±Pu±10Zr metallic fuel in the fast reactor, GRSIS, was developed. Fission gas bubbles were classi®ed into three classes depending upon their sizes. Bubbles are assumed to nucleate isotropically from the gas atoms in the fuel matrix since the bubbles could nucleate at the phase boundaries which are randomly distributed inside the grain, as well as at the grain boundary. When bubble swelling reaches the threshold value, bubble interconnection could occur to form an open channel to the external free space, and ®ssion gases inside the interconnected bubbles are released instantaneously. The model can also take into account the fuel gap closure caused by fuel bubble swelling.

The GRSIS model was validated by comparison with the irradiation test results in ANL and parametric study of the key variables. It was found that the GRSIS model could predict the general behavior of metallic fast reactor fuels such as U±10Zr, U±8Pu±10Zr and U±19Pu±10Zr, even though anisotropic cavitational void swelling of the fuel at the low temperature region was not considered in the GRSIS model. Parametric study of the GRSIS model showed that ®ssion gas release is very sensitive to the diusivity of the gas atoms which increases with temperature while it is quite insensitive to grain size, bubble nucleation rate and ®ssion density. However, classi®cation of the bubble sizes and values of the other variables in the GRSIS model may need to be further investigated and veri®ed.

## Acknowledgements

This work has been carried out under the Nuclear R&D Program supported by Ministry of Science and Technology in Korea. The authors would like to thank J. Rest of ANL for the critical reading and comments of the manuscript.

## References

[1] C.K. Park, et al., KALIMER Design Concept Report, KAERI/TR-888/97, KAERI, 1997.

[2] G.L. Hofmann, L.C. Walters, T.H. Bauer, Progress Nucl. Energy 31 (1&2) (1997) 83.

[3] R.G. Pahl, D.L. Porter, D.C. Crawford, L.C. Walter, J. Nucl. Mater. 188 (1992) 3.

[4] M.C. Billone, Y.Y. Liu, E.E. Gruber, T.H. Hughes, J.M. Kramer, Status of fuel element modelling codes for metallic fuels, in: International Conference on Reliable Fuels for Liquid Metal Reactors, Tucson, AZ, 1986, p. 5.

[5] J.M. Kramer, T.H. Hughes, E.E. Gruber, Validation of models for the analysis of the transient behavior of metallic fast reactor fuel, in: Transactions of the 10th International Conference on Structural Mechanics in Reactor Technology, 1989.

[6] Y. Tsuboi, T. Ogata, M. Kinoshita, H. Saito, J. Nucl. Mater. 188 (1992) 312.

[7] T. Ogata, M. Kinoshita, H. Saito, T. Yokoo, J. Nucl. Mat. 230 (1996) 129.

[8] T. Ogata, T. Yokoo, Nucl. Technol. 128 (1999) 113.

[9] E.E. Gruber, J.M. Kramer, J. Am. Ceram. Soc. 70 (1987) 699.

[10] J. Rest, J. Nucl. Mater. 207 (1993) 192.

[11] A.R. Massih, J. Nucl. Mater. 119 (1983) 116.

[12] D.R. Olander, Fundamental aspects of nuclear fuel elements, TIC ERDA, 1977.

[13] C.B. Lee, B.H. Lee, C. Nam, D.S. Sohn, GRSIS program to predict ®ssion gas release and swelling behavior of metallic fast reactor fuel , KAERI/TR-1289/99, KAERI, 1999.

[14] Y. Adda, J. Philibert, H. Faraggi, Revue De Metallurgie 54 (1957) 597.

[15] A.D. Schope, L.R. Jackson, Diusion studies of zirconium±uranium system, Battelle Memorial Inst. Report BMI-T-24, 1950.

[16] G.L. Hofmann, R.G. Pahl, C.E. Lahm, D.L. Porter, Metall. Trans. A 21 (1990) 517.

[17] H. Tsai, A.B. Cohen, M.C. Billone, L.A. Neimark, Irradiation performance of U±Pu±10Zr metal fuels for liquid-metal-cooled reactors, in: Proceedings of the International Conference on Fast Reactor and Related Fuel Cycles, Kyoto, Japan, 1991.