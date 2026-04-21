# Parameterization of vacancy production rate in phasefield models of fission gas bubble evolution in nuclear fuel

参数化核燃料中裂变气体气泡演化的相场模型中的空位产生率

Larry K. Aagesen 拉里·K·阿格森

Show more 显示更多

Outline

YX Share 共享 Cite 引用

https://doi.org/10.1016/j.jnucmat.2024.155311

Get rights and content 获取权利与内容

## Highlights亮点

• Net vacancy production can be approximated by vacancy source-only and source+sink approaches.

净空位产生可以通过仅空位源方法和源+汇方法来近似计算。

• Quasi-steady state analytical models explain behavior of phase-field models.

准稳态分析模型解释了相场模型的行为。

• Vacancy source-only models have more flexibility to match vacancyinterstitial models.

空位源模型在匹配空位-间隙模型方面具有更大的灵活性。

• Fitting source term in source-only model provides a good approximation to full vacancy-interstitial model.

在仅含源项的模型中拟合源项，可以为完整空位-间隙原子模型提供一个良好的近似。

## Abstract摘要

Phase-field modeling has increasingly been used to study microstructural evolution in fission gas bubbles in nuclear fuel to improve understanding of fission gas release. To improve computational efficiency, often only vacancies and gas atoms are included as defect species. In this case, the net effects of vacancy and interstitial production, recombination, and biased sink absorption are included as a net vacancy source, or net vacancy source combined with an effective sink. However, there has been a lack of clarity on what parameter values should be used for these approaches to best match the more complete physical picture that includes interstitials and vacancies. Here, we compare a phase-field model of void growth to analytical models for the source-only and source plus sink approach to gain insight into how the phase-field models can be parameterized effectively. The source-only approach provides greater flexibility to match growth rates determined from the full vacancyinterstitial picture. A strategy was developed for determining the value of the net vacancy source term by comparing to an analytical model that includes vacancy and interstitial production, recombination, and biased sink absorption. This strategy can be used to parameterize phase-field models of fission gas bubble growth.

相场建模越来越多地被用于研究核燃料中裂变气体气泡的微观结构演化，以提高对裂变气体释放的理解。为了提高计算效率，通常仅将空位和气体原子包括为缺陷物种。在这种情况下，空位和间隙产生、复合以及偏置汇吸收的净效应被包括为一个净空位源，或者净空位源结合一个有效汇。然而，关于这些方法应使用哪些参数值才能最好地匹配包括间隙和空位的更完整物理图像，一直缺乏明确性。在这里，我们比较了空泡生长的相场模型与仅源和源加汇方法的解析模型，以了解如何有效地参数化相场模型。仅源方法提供了更大的灵活性，以匹配由完整空位-间隙图像确定的生长率。为确定净空位源项的值，开发了一种策略，通过比较包含空位和间隙原子产生、复合以及偏置汇吸收的解析模型来确定。这种策略可用于参数化裂变气体气泡生长的相场模型。

## Graphical abstract图形摘要

![](images/ac45488152b3a477fc3d807bde9f1d522e4d72170674c1910ccfbb5c6a1e9d3a.jpg)

![](images/a2e1bfac1b4313a1cdbb021355bb7d58d2047268fb64a84ce78d277d485a886d.jpg)

Download: Download high-res image (80KB)

: 下载：下载高清图片（80KB）

Download: Download full-size image

下载：下载完整尺寸的图片

Keywords关键词

Void; Bubble; Fission gas; Phase-field; Vacancies; Source; Sink;

空泡裂变气体相场空位源汇

## 1. Introduction1. 引言

During operation of nuclear reactors, gaseous fission product species such as Xe and Kr are produced within the nuclear fuel. Due to the low solubility of these gaseous species, fission gas bubbles readily nucleate within the fuel. As the bubbles grow, they interconnect with one another and can eventually connect to free surfaces of the fuel, which allows the fission gases within these interconnected bubbles to be released to the gap between the fuel and cladding and the plenum. The release of fission gases has several negative consequences for fuel performance, including degrading the thermal conductivity of the fuel-cladding gap, leading to higher centerline temperatures within the fuel, and increased cladding strain due to the higher pressure [1].

在核反应堆运行过程中，如 Xe 和 Kr 等气态裂变产物种类在核燃料内部产生。由于这些气态物种的溶解度低，裂变气体气泡容易在燃料内成核。随着气泡的增长，它们相互连接，并最终可能与燃料的自由表面连接，这使这些相互连接的气泡中的裂变气体得以释放到燃料与包壳之间的间隙以及腔室内。裂变气体的释放对燃料性能产生了几个负面影响，包括降低燃料-包壳间隙的热导率，导致燃料中心线温度升高，以及由于压力升高导致包壳应变增加[1]。

The growth and interconnection of bubbles leading to fission gas release is a complex process that is highly dependent on the type of fuel, the fuel microstructure, and the microstructure of the fission gas bubbles themselves. In the $\mathrm { U O } _ { 2 }$ pellets used in commercial light water reactors, the $\mathrm { U O } _ { 2 }$ grains are typically of size 5–10 μm. Within the grain interiors, small intragranular bubbles of nm size are found, which are limited in size due to re-solution of fission gas atoms by energetic fission fragments [1]. Because of their limited size, these intragranular bubbles do not interconnect and thus do not contribute directly to fission gas release. However, larger (100–500 nm) lenticular-shaped intergranular bubbles also form on grain boundaries in $\mathrm { U O } _ { 2 } ,$ which grow and interconnect along the grain boundaries. Tunnels also form along triple junctions in the grain boundary structure and connect to free surfaces, allowing gases from interconnected grain boundaries that contact to these tunnels to release their fission gas to the fuel-cladding gap [1]. In $\mathrm { U } _ { 3 } \mathrm { S i } _ { 2 }$ fuel pellets that have been proposed as an accident-tolerant alternative to $\mathrm { U O } _ { 2 } ,$ , the evolution of the fission gas bubble microstructure is similar to that observed in $\mathrm { U O } _ { 2 }$ [2]. However, in U-Zr and U-Pu-Zr metallic fuels that are under consideration for several advanced reactor designs, the microstructure of fission gas bubbles is significantly different. In the cooler periphery of these fuels, fission gases collect in tears or cracks that occur at interphase or grain boundaries [3], [4]. In the hotter central regions of U-(Pu)-Zr fuels, larger (5–10 μm) bubbles with an initially spherical morphology are found [5]. These bubbles eventually grow and interconnect, leading to fission gas release with a very different bubble morphology than observed in $\mathrm { U O } _ { 2 }$ fuel. These examples illustrate that the microstructure of fission gas bubbles has a major impact on the process of fission gas release and therefore fuel performance in a variety of nuclear fuels. Thus, quantitatively accurate techniques to model microstructural evolution are needed to inform fuel performance

气泡的增长和互联导致裂变气体释放是一个复杂的过程，它高度依赖于燃料类型、燃料微结构以及裂变气体气泡自身的微结构。在商业轻水反应堆中使用的 UO2 颗粒中，UO2 晶粒通常大小为 5-10 微米。在晶粒内部，可以发现纳米大小的微小晶内气泡，这些气泡的大小由于高能裂变碎片对裂变气体原子的再溶解而受到限制[1]。由于它们的大小有限，这些晶内气泡不会互联，因此不直接参与裂变气体的释放。然而，在 UO2 晶粒边界上还形成了较大（100-500 纳米）的透镜形状的晶间气泡，这些气泡沿着晶粒边界增长并互联。在晶粒边界结构中的三重交界处也形成了隧道，并与自由表面相连，使得互联的晶粒边界接触这些隧道的气体能够将其裂变气体释放到燃料包壳间隙[1]。 在提出的 $\mathrm { ~ U ~ } _ { 3 } \thinspace \mathrm { S i } _ { 2 }$ 燃料颗粒中，作为 $\mathrm { U O } _ { 2 }$ 的事故容忍替代品，裂变气体气泡微结构的演变与 $\mathrm { U O } _ { 2 }$ 中观察到的相似[2]。然而，在考虑用于几种先进反应堆设计的 U-Zr 和 U-Pu-Zr金属燃料中，裂变气体气泡的微结构显著不同。在这些燃料的较冷边缘区域，裂变气体聚集在相界面或晶界处的泪滴状或裂纹中[3]、[4]。在 $\mathrm { U - ( P u ) { - } Z r }$ 燃料的热中心区域，发现了较大（5-10 微米）的初始球形气泡[5]。这些气泡最终增长并相互连接，导致裂变气体的释放，其气泡形态与 $\mathrm { U O } _ { 2 }$ 燃料中观察到的非常不同。这些例子说明，裂变气体气泡的微结构对裂变气体释放过程以及各种核燃料的性能有重大影响。因此，需要定量准确的techniques 来模拟微结构的演变，以指导燃料性能模型。

For these reasons, in recent years the phase-field method has been increasingly applied to model fission gas bubble evolution in nuclear fuels [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19]. Phase-field modeling allows the fuel grain structure and fission gas bubble microstructure to be represented explicitly and thus can capture complex microstructural features (such as the aforementioned intergranular bubbles, tunnels, and interconnected spherical bubbles) and their impact on fission gas release. Various defect species such as interstitials, vacancies, and gas atoms can be included in these models. By analyzing phase-field simulation results, fission gas release models in engineering-scale fuel performance codes can be improved [11], [13], [17].

因此，近年来相场方法被越来越多地应用于模拟核燃料中裂变气体气泡的演化[6]、[7]、[8]、[9]、[10]、[11]、[12]、[13]、[14]、[15]、[16]、[17]、[18]、[19]。相场建模能够明确表示燃料颗粒结构以及裂变气体气泡的微观结构，因此能够捕捉到复杂的微观结构特征（如前述的晶间气泡、隧道和相互连接的球形气泡）及其对裂变气体释放的影响。这些模型可以包含各种缺陷物种，如间隙原子、空位和气体原子。通过分析相场模拟结果，可以改进工程规模燃料性能代码中的裂变气体释放模型[11]、[13]、[17]。

Although there are significant advantages to using phase-field modeling to investigate fission gas bubble microstructural evolution, one disadvantage is that such models are computationally expensive, especially for 3D simulations, which are necessary to simulate realistic microstructures. In addition to the large simulation domain sizes required, simulating the evolution of both vacancy and interstitial defects adds additional challenges. During reactor operation, energetic fission fragments are ejected from nuclei undergoing fission, leading to collision cascades that produces pairs of interstitials and vacancies (Frenkel pairs). Although many Frenkel pairs rapidly recombine in the aftermath of collision cascades, some remain as free species that can diffuse to sinks such as voids and dislocations. Because interstitials are preferentially absorbed at dislocation sinks, a net excess of vacancies usually remains that can contribute to fission gas bubble or void growth. Ideally, it would be preferable to track both vacancies and interstitial species in phase-field models, including their production, recombination, and absorption at sinks. However, interstitials usually diffuse much more rapidly than vacancies. This makes it computationally challenging to simulate experimentally relevant times, because the simulation time step is limited 尽管使用相场模型研究裂变气体气泡微观结构演化具有显著优势，但一个缺点是这类模型计算成本高昂，特别是在进行 3D 模拟时，这对于模拟真实的微观结构是必要的。除了需要大型的模拟域尺寸外，同时模拟空位和间隙缺陷的演化也增 加了额外的挑战。在反应堆运行期间，高能裂变碎片从经历裂变的核中喷射出来，导致碰撞级联，产生间隙和空位的对 （弗兰克尔对）。尽管许多弗兰克尔对在碰撞级联后迅速重新结合，但一些仍作为自由物种存在，可以扩散到空位和位 错等汇。由于间隙缺陷更倾向于在位错汇中被吸收，通常剩余净空位过剩，这可以促进裂变气体气泡或空位的增长。理 想情况下，最好在相场模型中跟踪空位和间隙物种，包括它们的产生、重新结合以及在汇中的吸收。 然而，间隙原子通 常比空位扩散得快得多。这使得在计算上很难模拟实验相关的时间，因为模拟的时间步长必须足够小，以解析快速扩散 的间隙原子种类的传输。

Due to this challenge, many phase-field models of nuclear fuel have not included interstitials, and have approximated the full vacancy-interstitial picture as a net production of vacancies. One approach has been including an evolution equation for vacancies only, and adding a source term for net vacancy production, similar to the source term required to simulate the production of insoluble fission gas atoms [6], [11], [12], [13], [15], [16], [18], [19]. For convenience, this approach will be referred to as source-only (SO). One disadvantage of this approach is that it is not known what the appropriate value of the source term should be to correctly represent the net vacancy production rate. The rate of Frenkel pair production during fission is several orders of magnitude greater than the fission rate [20], but rapid recombination in the aftermath of collision cascades should reduce the net production rate significantly. Thus, a range of net vacancy production rates have been used, from equal to the Xe production rate [6] to as much as 20 times the Xe production rate [11]. The effect of the range of net vacancy production rates has been studied parameterically [11]. Another approach has been to introduce both a vacancy source term and a sink term proportional to the vacancy concentration [14]. This approach will be referred to as source+sink (SS). The SS approach results in a vacancy concentration that is in steady-state and constant in the bulk of the fuel far from bubbles, as is expected from rate theory models. The value of the effective sink term was calculated [14] so that steady-state vacancy concentration, $c _ { v } ^ { s s }$ , matched the value predicted from cluster dynamics simulations [21]. Matching the expected steady-state vacancy concentration in the bulk improves the SS model's fidelity to one aspect of the full vacancy-interstitial model, but it has not been determined how growth rate of the SO or SS models compare to the full physics that includes vacancies and interstitials.

由于这一挑战，许多核燃料的相场模型未包括间隙原子，而是将完整的空位-间隙原子图像近似为空位的净生成。一种方法仅包含空位的演化方程，并添加一个空位净生成源项，类似于模拟不溶性裂变气体原子生成所需的源项[6]、[11]、[12]、[13]、[15]、[16]、[18]、[19]。为了方便，这种方法将被称作仅含源项（SO）。这种方法的一个缺点是，不清楚源项的合适值应该是多少，才能正确表示空位的净生成速率。裂变过程中 Frenkel 对的生成速率比裂变速率高几个数量级[20]，但在碰撞级联后的快速重组应显著降低净生成速率。因此，已经使用了从等于 Xe 生成速率[6]到高达 Xe生成速率 20倍的空位净生成速率[11]。已经参数化地研究了空位净生成速率范围的影响[11]。 另一种方法是同时引入空位源项和与空位浓度成比例的汇项[14]。这种方法将被称作源+汇（SS）。SS 方法导致空位浓度在远离气泡的燃料主体中处于稳态且恒定，这与速率理论模型预期相符。有效汇项的值被计算出来[14]，以使得稳态空位浓度 $c _ { v } ^ { s s }$ 与从团簇动力学模拟[21]预测的值相匹配。匹配燃料主体中预期的稳态空位浓度提高了 SS 模型对完整空位-间隙原子模型某一方面的保真度，但尚未确定 SO 或 SS 模型中空位和间隙原子增长速率与包含空位和间隙原子的完整物理模型相比如何。

Although computational models using techniques such as the phase-field method can simulate a far wider and more realistic variety of microstructures than is possible with an analytical model, there are advantages of analytical models in gaining qualitative and even quantitative understanding. Therefore, in this work, we compare the growth rates and vacancy concentrations of the SO and SS models to analytical models to gain understanding of what factors control the growth rates in the SO and SS models. We find advantages to the SO approach in that it provides greater flexibility to match growth rates predicted from vacancy-interstitial models. We also compare the SO model to an analytical model of bubble growth from the literature that includes the full physics of vacancies and interstitials, the so-called “chemical stress” model [20], and describe a strategy to parameterize the SO model to match the chemical stress model. To simplify the comparison as much as possible and make it possible to derive analytical solutions, we do not include any fission gas species. Thus, the models and simulations are representative of voids, but the results and conclusions are applicable to fission gas bubbles as well. To show how the parameterization strategy affects evolution in realistic 3D microstructures, we conclude by simulating growth of intergranular fission gas bubbles in $\mathrm { U O } _ { 2 }$ fuel and compare to previously published results.

尽管采用相场方法等技术的计算模型能够模拟比解析模型更广泛、更真实的微观结构，但解析模型在获得定性和甚至定量理解方面具有优势。因此，在这项工作中，我们将 SO 模型和 SS 模型的生长速率及空位浓度与解析模型进行比较，以了解哪些因素控制了 SO 模型和 SS 模型中的生长速率。我们发现 SO 方法的优势在于它提供了更大的灵活性，以匹配从空位-间隙模型预测的生长速率。我们还将 SO模型与文献中包含空位和间隙完整物理的气泡生长解析模型进行了比较，即所谓的“化学应力”模型[20]，并描述了一种将 SO模型参数化以匹配化学应力模型的方法。为了尽可能简化比较并使推导解析解成为可能，我们没有包括任何裂变气体物种。 因此，模型和模拟代表了空洞，但结果和结论也适用于裂变气体泡。为了展示参数化策略如何影响真实 3D微观结构中的演化，我们通过模拟 $\mathrm { U O } _ { 2 }$ 燃料中晶间裂变气体泡的生长来总结，并与之前发表的结果进行比较。

## 2. Analytical models for void/bubble growth

## 2.空洞/气泡生长的解析模型

## 2.1. Source-only (SO) model

## 2.1. 仅源模型（SO）

In the source-only model, the growth of a bubble of instantaneous radius R is considered. Radial coordinates with spherical symmetry are used, in a simulation domain of radius ${ \mathcal { R } } .$ The variable r describes the distance from the center of the domain to a given point. The void/bubble phase is within the region $0 < r \leq R ,$ and the solid $\mathrm { U O } _ { 2 }$ matrix phase is within the region $R < r \leq \mathcal { R }$ . The diffusion equation describing the non-dimensional concentration (mole fraction) of vacancies, $\pmb { c _ { v } }$ , within the solid in spherical coordinates is

在源模型中，考虑了瞬时半径为 R的气泡的增长。使用具有球对称性的径向坐标，在半径为 的模拟域内。变量 r 描述了从域中心到给定点的距离。空泡相位于区域 $0 < r \leq R$ 内，而固体 $\mathrm { ~ U O ~ } _ { 2 }$ 基相位于区域 $R < r \leq \mathcal { R }$ 内。描述固体中空位非维浓度（摩尔分数） $c _ { v }$ 的扩散方程在球坐标中为

$$
\begin{array} { r } { \frac { \partial c _ { v } } { \partial t } = \frac { D _ { v } } { r ^ { 2 } } \frac { \partial } { \partial r } \left( r ^ { 2 } \frac { \partial c _ { v } } { \partial r } \right) + S _ { v } } \end{array}\tag{1}
$$

where $D _ { v }$ is the diffusion coefficient of vacancies, and $\pmb { S _ { v } }$ is the production rate of vacancies (in units of $\mathsf { s } ^ { - 1 } )$ Although an analytical solution to the time-dependent Equation (1) is not available, if the rate of change in the bubble size is slow relative to the relaxation time of the diffusion field, the concentration profile of $c _ { v }$ will be near a steady state at a particular time t. This is known as the quasi-steady state approximation, and the diffusion equation in this case is

其中 $D _ { v }$ 是空位的扩散系数， $S _ { v }$ 是空位的生成速率（单位为 $s ^ { - 1 }$ ）。虽然无法得到时间依赖性方程（1）的解析解，但如果气泡大小的变化速率相对于扩散场的松弛时间较慢，则在特定时间 t， $c _ { v }$ 的浓度分布将接近稳态。这被称为准稳态近似，在这种情况下，扩散方程为

$$
\begin{array} { r } { \frac { \partial c _ { v } } { \partial t } \approx 0 \approx \frac { D _ { v } } { r ^ { 2 } } \frac { \partial } { \partial r } \left( r ^ { 2 } \frac { \partial c _ { v } } { \partial r } \right) + S _ { v } } \end{array}\tag{2}
$$

The quasi-steady state diffusion Equation (2) can be solved given appropriate boundary conditions. It is expected that very far from the bubble, vacancy concentration should not vary significantly with position; therefore, $c _ { v }$ should be constant with respect to changes in r at the simulation domain boundary, leading to the boundary condition $\left. \frac { \partial c _ { v } } { \partial r } \right| _ { r = \mathcal { R } } = 0$ . The vacancy concentration in the matrix at the bubble-matrix interface, $c _ { v R } = c _ { v } ( r = R )$ can be calculated using the Gibbs-Thomson equation and represents the other necessary boundary condition:

准稳态扩散方程（2）在给定适当的边界条件时可被求解。预期在远离气泡的地方，空位浓度不应随位置显著变化；因此，在模拟域边界上， $c _ { v }$ 应相对于 r 的变化保持常数，从而得到边界条件 $\left. \frac { \partial c _ { v } } { \partial r } \right| _ { r = \mathcal { R } } = 0$ 。气泡-基体界面处的基体空位浓度， $c _ { v R } = c _ { v } ( r = R )$ ，可以通过吉布斯-汤姆逊方程计算，并代表另一个必要的边界条件：

$$
\begin{array} { r } { c _ { v R } = c _ { m , 0 } + \frac { 2 \sigma _ { i n t } } { R k _ { v } ( c _ { v , 0 } - c _ { m , 0 } ) } } \end{array}\tag{3}
$$

where $\pmb { c _ { m , 0 } }$ is the equilibrium concentration of vacancies in the bulk solid far from a curved interface (assumed to be 0 here), $\sigma _ { i n t }$ is the interfacial energy of the bubble-solid interface, $k _ { v }$ is the curvature of the free energy versus composition in the matrix phase, and ${ c _ { v , 0 } } = 1$ is the equilibrium concentration of vacancies in the void.

其中 $\pmb { c _ { m , 0 } }$ 是远离曲界面的大块固体中的空位平衡浓度（此处假设为 0）， $\sigma _ { i n t }$ 是气泡-固体界面的界面能， $k _ { v }$ 是自由能与组成在基体相中的曲率， $\pmb { c _ { v , 0 } } = \pmb { 1 }$ 是空腔中的空位平衡浓度。

Subject to these boundary conditions, the solution to Equation (2) in the solid is given by [20]

在这些边界条件下，方程（2）在固体中的解由文献[20]给出

$$
\begin{array} { r } { c _ { v } ( r ) = c _ { v R } + \frac { S _ { v } } { 6 D _ { v } } \Big [ \frac { 2 \mathcal { R } ^ { 3 } ( r - R ) } { r R } - ( r ^ { 2 } - R ^ { 2 } ) \Big ] } \end{array}\tag{4}
$$

If ${ \mathcal { R } } \gg R ,$ Equation (4) can be approximated as [20]

如果 $\mathcal { R } \gg R$ ，方程（4）可以近似为 [20]

$$
\begin{array} { r } { c _ { v } ( r ) \approx c _ { v R } + \frac { S _ { v } \mathcal { R } ^ { 3 } } { 3 D _ { v } R } \big ( 1 - \frac { R } { r } \big ) } \end{array}\tag{5}
$$

The growth rate of the bubble can be determined by equating the time rate of change of the bubble volume V to the flux of vacancies J across the bubble-matrix interface at R, which has area $\scriptstyle 4 \pi R ^ { 2 }$ :

气泡的增长率可以通过将气泡体积 V 的时间变化率与气泡-基体界面在 R 处的空位通量 J 相等来确定，该界面的面积为$\scriptstyle 4 \pi R ^ { 2 }$ ：

$$
\begin{array} { r } { \frac { d V } { \partial t } = 4 \pi \Omega R ^ { 2 } J } \end{array}\tag{6}
$$

where Ω is the atomic volume. Since $\begin{array} { r } { V = \frac { 4 } { 3 } \pi R ^ { 3 } , \frac { d V } { d t } = 4 \pi R ^ { 2 } \frac { d R } { d t } } \end{array}$ . Substituting in to Equation (6),

其中 Ω 是原子体积。由于 $\begin{array} { r } { V = \frac { 4 } { 3 } \pi R ^ { 3 } } \end{array}$ $\begin{array} { r } { \frac { d V } { d t } = 4 \pi R ^ { 2 } \frac { d R } { d t } } \end{array}$ 。代入方程（6）中，

$$
\begin{array} { r } { \frac { d R } { d t } = \Omega J } \end{array}\tag{7}
$$

Flux J at the bubble-matrix interface is given by

在气泡-基材界面上的通量 J 由下式给出：

$$
\begin{array} { r } { J ( R ) = - D _ { v } \left( \frac { \partial ( c _ { v } / \Omega ) } { \partial r } \right) \Big | _ { r = R } = - \frac { D _ { v } } { \Omega } \left( \frac { \partial c _ { v } } { \partial r } \right) \Big | _ { r = R } } \end{array}\tag{8}
$$

Thus,因此，

$$
\begin{array} { r } { \frac { d R } { d t } = - D _ { v } \left( \frac { \partial c _ { v } } { \partial r } \right) \Big | _ { r = R } } \end{array}\tag{9}
$$

Substituting Equation (5) and taking the derivative,

将方程（5）代入并求导，

$$
\begin{array} { r } { \frac { d R } { d t } = \frac { S _ { v } \mathcal { R } ^ { 3 } } { 3 R ^ { 2 } } } \end{array}\tag{10}
$$

## 2.2. Source+sink (SS) model

## 2.2. 源汇（SS）模型

In this section, we derive a quasi-steady state solution for the SS model. The quasi-steady state diffusion equation for this case is

在本节中，我们为 SS 模型推导出一个准稳态解。该情况的准稳态扩散方程为

$$
\begin{array} { r } { \frac { \partial c _ { v } } { \partial t } \approx 0 \approx \frac { D _ { v } } { r ^ { 2 } } \frac { \partial } { \partial r } \left( r ^ { 2 } \frac { \partial c _ { v } } { \partial r } \right) + S _ { v } - K _ { v } c _ { v } } \end{array}\tag{11}
$$

where $\pmb { K _ { v } }$ is an effective sink strength that represents the net effect of vacancy/interstitial recombination and the preferential absorption of interstitials at dislocation sinks. Again assuming that very far from the bubble-matrix interface, $c _ { v }$ is constant with respect to changes in r, $\left. \frac { \partial c _ { v } } { \partial r } \right| _ { r = \mathcal { R } } = 0$ . The first term in Equation (11) is thus negligible far from the bubble, and the steady-state vacancy concentration $c _ { v } ^ { s s }$ can be determined by Equation (11) to be 其中 $\pmb { K _ { v } }$ 是一个有效 sink 强度，代表了空位/间隙原子复合以及间隙原子在位错 sink 处的优先吸收的净效应。再次假设 在远离气泡-基体界面处， $c _ { v }$ 对于 r的变化是常数， $\left. \frac { \partial c _ { v } } { \partial r } \right| _ { r = \mathcal { R } } = 0$ 。因此，远离气泡处方程（11）中的第一项可以忽略 不计，稳态空位浓度 $c _ { v } ^ { s s }$ 可以通过方程（11）确定。

$$
c _ { v } ^ { 8 . 8 } = \frac { K _ { v } } { S _ { c } }\tag{12}
$$

Equation (11) can be rewritten by dividing through by $D _ { v }$ and taking all $c _ { v }$ -dependent terms to one side:

方程（11）可以通过除以 $D _ { v }$ 并将所有依赖于 $\pmb { c _ { v } }$ 的项移到一边来重写：

$$
\begin{array} { r } { \frac { 1 } { r ^ { 2 } } \frac { \partial } { \partial r } \left( r ^ { 2 } \frac { \partial c _ { v } } { \partial r } \right) - \frac { K _ { v } } { D _ { v } } c _ { v } = - \frac { S _ { v } } { D v } } \end{array}\tag{13}
$$

Following the theory of differential equations, the equation can be split into homogeneous and particular

solutions, $\pmb { c _ { h } }$ and $\pmb { c _ { p } }$ , such that $c _ { v } = c _ { h } + c _ { p }$ . The solution to the homogeneous part can be found by solving 遵循微分方程理论，该方程可以分解为齐次解和特解， $c _ { h }$ 以及 $c _ { p }$ ，使得 $c _ { v } = c _ { h } + c _ { p }$ 。齐次部分的可通过求解得到 解。

$$
\begin{array} { r } { \frac { 1 } { r ^ { 2 } } \frac { \partial } { \partial r } \left( r ^ { 2 } \frac { \partial c _ { h } } { \partial r } \right) - \frac { K _ { v } } { D _ { v } } c _ { h } = 0 } \end{array}\tag{14}
$$

Expanding the first term and multiplying through by $\pmb { r ^ { 2 } }$ ,

将第一项展开并乘以 $r ^ { 2 }$

$$
\begin{array} { r } { r ^ { 2 } \frac { \partial ^ { 2 } c _ { h } } { \partial r ^ { 2 } } + 2 r \frac { \partial c _ { h } } { \partial r } - \frac { K _ { v } } { D _ { v } } c _ { h } r ^ { 2 } = 0 } \end{array}\tag{15}
$$

This is the modified spherical Bessel differential equation with $\pmb { n = 0 }$ [22]. Solutions are of the form 这是修改后的球贝塞尔微分方程 $\pmb { n } = \pmb { 0 } \left[ 2 2 \right]$ 。解的形式为

$$
c _ { h } = c _ { 1 } i _ { 0 } + c _ { 2 } k _ { 0 }\tag{16}
$$

where $c _ { 1 }$ and $c _ { 2 }$ are constants to be determined, and $\dot { \iota } _ { 0 }$ and $\pmb { k } _ { 0 }$ are the modified spherical Bessel functions of the first and second kind, respectively, for $\pmb { n = 0 }$ :

其中 $\pmb { c _ { 1 } }$ 和 ${ c _ { 2 } }$ 是待确定的常数， $\dot { \iota } _ { 0 }$ 和 $\pmb { k _ { 0 } }$ 分别是 $\pmb { n = 0 }$ 的第一类和第二类修正球贝塞尔函数

$$
\begin{array} { r } { i _ { 0 } = \frac { \sinh \left( \sqrt { \frac { K _ { v } } { D _ { v } } } r \right) } { \sqrt { \frac { K _ { v } } { D _ { v } } } r } } \end{array}\tag{17}
$$

$$
\begin{array} { r } { k _ { 0 } = \frac { \exp \left( - \sqrt { \frac { K _ { v } } { D _ { v } } } r \right) } { \sqrt { \frac { K _ { v } } { D _ { v } } } r } } \end{array}\tag{18}
$$

To find the particular solution, based on the fact that the particular term of the differential equation, $S _ { v } / D _ { v }$ , is a constant, we try $c _ { p } = A$ , where A is a constant. Substituting to the particular form of the differential equation.

为了找到特解，基于微分方程的特项 $S _ { v } / D _ { v }$ 是常数的这一事实，我们尝试 $c _ { p } = A$ ，其中 A 是一个常数。将其代入微分方程的特定形式中。

$$
\begin{array} { r } { \frac { 1 } { r ^ { 2 } } \frac { \partial } { \partial r } \left( r ^ { 2 } \frac { \partial A } { \partial r } \right) + \frac { S _ { v } } { D _ { v } } - \frac { K _ { v } } { D _ { v } } A = 0 } \end{array}\tag{19}
$$

which results in导致

$$
\begin{array} { r } { A = \frac { S _ { v } } { K _ { v } } = c _ { p } } \end{array}\tag{20}
$$

Combining Equation (16) and (20), we obtain

结合方程（16）和（20），我们得到

$$
\begin{array} { r } { c _ { v } = c _ { h } + c _ { p } = c _ { 1 } i _ { 0 } + c _ { 2 } k _ { 0 } + \frac { S _ { v } } { K _ { v } } } \end{array}\tag{21}
$$

Now the boundary conditions must be used to determine $\pmb { c _ { 1 } }$ and ${ \pmb { c _ { 2 } } }$ . Because $i _ { 0 } \to \infty \mathrm { a s } r \to \infty$ , but $c _ { v }  c _ { v } ^ { s s }$ as $\pmb { r }  \infty .$ , this requires that $\pmb { c _ { 1 } = 0 }$ . We can determine ${ c _ { 2 } }$ from the fact that at $r = R , c _ { v } ( R ) = c _ { v R }$ , as determined from the Gibbs-Thomson condition of Equation (3). Defining $\lambda = \sqrt { S _ { v } / K _ { v } }$ for convenience,

现在必须使用边界条件来确定 $\pmb { c _ { 1 } }$ 和 ${ \pmb { c _ { 2 } } }$ 。因为 $i _ { 0 } \to \infty$ 当 $\pmb { r }  \infty$ ，但是 $c _ { v }  c _ { v } ^ { s s }$ 当 $\pmb { r }  \infty$ ，这要求 $\pmb { c _ { 1 } = 0 }$ 。我们可以从 $\pmb { r } = \pmb { R }$ 时 $\pmb { c } _ { v } ( \pmb { R } ) = \pmb { c } _ { v R }$ 这一事实来确定 $c _ { 2 }$ ，这是由方程（3）的吉布斯-汤姆森条件确定的。为了方便起见，定义 $\lambda = \sqrt { S _ { v } / K _ { v } }$ 。

$$
\begin{array} { r } { c _ { v } = c _ { 2 } k _ { 0 } + \frac { S _ { v } } { K _ { v } } = c _ { 2 } \frac { e ^ { - \lambda r } } { \lambda r } + \frac { S _ { v } } { K _ { v } } } \end{array}\tag{22}
$$

$$
\mathrm { E v a l u a t i n g a t } r = R ,
$$

在 进行评估，

$$
\begin{array} { r } { c _ { v } ( r = R ) = c _ { v R } = c _ { 2 } \frac { e ^ { - \lambda R } } { \lambda R } + \frac { S _ { v } } { K _ { v } } } \end{array}\tag{23}
$$

This allows us to solve for ${ \pmb { c _ { 2 } } }$ :

这使我们能够求解 $c _ { 2 }$

$$
\begin{array} { r } { c _ { 2 } = \frac { \lambda R } { e ^ { - \lambda R } } \Big ( c _ { v R } - \frac { S _ { v } } { K _ { v } } \Big ) } \end{array}\tag{24}
$$

Substituting Equation (24) into (22), we obtain the vacancy concentration as a function of position in the solid for the SS model:

将方程（24）代入方程（22），我们得到 SS 模型中固体中空位浓度随位置的变化函数：

$$
\begin{array} { r } { c _ { v } = \left( c _ { v R } - \frac { S _ { v } } { K _ { v } } \right) \frac { \lambda R } { e ^ { - \lambda R } } \frac { e ^ { - \lambda r } } { \lambda r } + \frac { S _ { v } } { K _ { v } } } \end{array}\tag{25}
$$

The growth rate of the void/bubble can be obtained by using Equation (25) in (9):

空隙/气泡的增长率可以通过使用(9)中的方程式(25)得到

$$
\begin{array} { r } { \frac { d R } { d t } = D _ { v } \left( \frac { S _ { v } } { K _ { v } } - c _ { v R } \right) \left( \sqrt { \frac { K _ { v } } { D _ { v } } } + \frac { 1 } { R } \right) } \end{array}\tag{26}
$$

and by using Equation (12),

并使用方程（12），

$$
\begin{array} { r } { \frac { d R } { d t } = D _ { v } \left( c _ { v } ^ { s s } - c _ { v R } \right) \left( \sqrt { \frac { K _ { v } } { D _ { v } } } + \frac { 1 } { R } \right) } \end{array}\tag{27}
$$

## 2.3. Chemical stress model

## 2.3. 化学应激模型

Accounting for the presence of both vacancies and interstitials, an approximation for the growth rate of bubbles due to the supersaturation of irradiation-produced defects can be obtained [20]. This model neglects the effects of bubble over/under-pressurization, for simplicity in comparison with the phase-field model. The model is derived by writing the growth rate accounting for both interstitials and vacancies as

考虑到空位和间隙的存在，可以通过超饱和辐照产生的缺陷来近似计算气泡增长率[20]。该模型为了与相场模型进行比较的简便性，忽略了气泡过度/欠压的影响。该模型通过将增长率表示为同时考虑间隙和空位的公式导出。

$$
\begin{array} { r } { \frac { d R } { d t } = \frac { 1 } { R } \big [ D _ { v } ( c _ { v } ^ { s s } - c _ { v R } ) - D _ { i } ( c _ { i } ^ { s s } - c _ { i R } ) \big ] } \end{array}\tag{28}
$$

where $D _ { i }$ is the diffusivity of interstitials and $c _ { i } R$ is the concentration of interstitials at the matrix-bubble interface. In steady-state far from bubbles, the following relationship holds: [20]

其中 $\mathbf { \delta } _ { D _ { i } }$ 是间隙原子的扩散率， $c _ { i } R$ 是在基体-气泡界面处间隙原子的浓度。在远离气泡的稳态条件下，以下关系成立：[20]

$$
Z _ { v } D _ { v } \left( c _ { v } ^ { s s } - c _ { v R } \right) = Z _ { i } D _ { i } ( c _ { i } ^ { s s } - c _ { i R } )\tag{29}
$$

where $\boldsymbol { Z _ { v } }$ and $\mathbf { \delta } _ { Z _ { i } }$ are capture rates of the point defects by sinks such as dislocations. Substituting Equation (29) into Equation (28),

其中 $\boldsymbol { Z _ { v } }$ 和 $\mathbf { \delta } _ { Z _ { i } }$ 是点缺陷被诸如位错等汇点捕获的捕获率。将方程（29）代入方程（28），

$$
\begin{array} { r } { \frac { d R } { d t } = \frac { D _ { v } } { R } ( c _ { v } ^ { s s } - c _ { v R } ) \left( 1 - \frac { Z _ { v } } { Z _ { i } } \right) } \end{array}\tag{30}
$$

The growth rate resulting from the supersaturation of defects has been referred to as a “chemical stress” because it produces bubble growth like a mechanical force [20].

由于缺陷过饱和导致的增长率被称作“化学应力”，因为它像机械力一样促使气泡生长[20]。

## 3. Phase-field model formulation

## 3.相场模型公式化

The model for $\mathrm { U O } _ { 2 }$ voids uses the approach developed by Kim et al. [23], typically referred to as the “KKS” formulation. For the SO and SS models, the formulation tracks the normalized concentration (site fraction) of uranium site vacancies, $c _ { v }$ . The bubble or void phase is represented as composed entirely of vacancies, $\boldsymbol { c _ { v } } = 1$ . The model also indicates the difference between matrix (solid) and bubble phases with a non-conserved order parameter, η, that varies continuously from 0 in the matrix phase to 1 in the void/bubble phase. (Since there are no fission gas atoms in the current phase-field model, it may be more typical to refer to the bubble regions as voids. However, to avoid potential confusion with the subscript v used for vacancies, we maintain the use of the term bubbles and the subscript b to refer to regions composed entirely of vacancies throughout.)

$\mathrm { U O } _ { 2 }$ 空位的模型采用了 Kim等人[23]开发的方法，通常称为“KKS”公式。对于 SO 和 SS 模型，该公式跟踪了铀位点空位的归一化浓度（位点分数）， $c _ { v }$ 。气泡或空位相被表示为由空位完全组成， ${ c _ { v } = 1 }$ 。该模型还用非守恒的序参数η表示基体（固体）和气泡相之间的差异，该参数在基体相中从 0 连续变化到气泡/空位相中的 1。（由于当前相场模型中没有裂变气体原子，因此将气泡区域称为空位可能更为常见。然而，为了避免与空位下标 v混淆，我们继续使用术语气泡和下标 b来指代完全由空位组成的区域。）

## The total free energy F of the system is given by

系统的总自由能 F由以下公式给出

$$
\begin{array} { r } { F = \underset { V } { \int } \left[ f _ { c h e m } + { W g ( \eta ) } + \frac { \kappa } { 2 } { \left| \nabla \eta \right| } ^ { 2 } \right] \mathrm { d } V , } \end{array}\tag{31}
$$

where $f _ { c h e m }$ is the chemical contribution to the free energy density, $g ( \eta ) = \eta ^ { 2 } ( 1 - \eta ) ^ { 2 }$ is a double-well function, W is the height of the double well, and κ is the gradient energy coefficient.

其中 $f _ { c h e m }$ 是自由能密度中的化学贡献， $g ( \eta ) = \eta ^ { 2 } ( 1 - \eta ) ^ { 2 }$ 是双井函数，W 是双井的高度，κ 是梯度能系数。

## 3.1. Chemical free energy density

## 3.1.化学自由能密度

The chemical free energy density is interpolated from the chemical free energy densities of the matrix and bubble phases:

化学自由能密度是通过从基体相和气泡相的化学自由能密度进行插值得到的：

$$
f _ { c h e m } = [ 1 - h ( \eta ) ] f _ { c h e m } ^ { m } ( c _ { v } ^ { m } ) + h ( \eta ) f _ { c h e m } ^ { b } ( c _ { v } ^ { b } )\tag{32}
$$

where $f _ { c h e m } ^ { m }$ is the chemical free energy density of the matrix phase; $f _ { c h e m } ^ { b }$ is the chemical free energy density of the bubble phase; $c _ { v } ^ { m }$ is the concentration of vacancies in the matrix phase; and $\pmb { c } _ { v } ^ { b }$ is the concentrations of vacancies in the bubble phase. $h ( \eta ) = \eta ^ { 3 } ( 6 \eta ^ { 2 } - 1 5 \eta + 1 0 )$ is an interpolation function that varies smoothly from $h ( 0 ) = 0 \mathrm { t o } h ( 1 ) = 1$ . Parabolic approximations are used for the dependence of chemical free energies on defect concentrations:

其中 $f _ { c h e m } ^ { m }$ 是基相的化学自由能密度； $f _ { c h e m } ^ { b }$ 是气泡相的化学自由能密度； $c _ { v } ^ { m }$ 是基相中的空位浓度； $c _ { v } ^ { b }$ 是气泡相中的空位浓度。 $h ( \eta ) = \eta ^ { 3 } ( 6 \eta ^ { 2 } - 1 5 \eta + 1 0 )$ 是一个插值函数，它从 $\pmb { h } ( \mathbf { 0 } ) = \mathbf { 0 }$ 平滑变化到 $h ( 1 ) = 1$ 。对于化学自由能随缺陷浓度的依赖关系，使用了抛物线近似。

$$
\begin{array} { r } { f _ { c h e m } ^ { m } = \frac { k _ { v } } { 2 } \big ( c _ { v } ^ { m } - c _ { v } ^ { m , m i n } \big ) ^ { 2 } } \end{array}\tag{33}
$$

$$
\begin{array} { r } { f _ { c h e m } ^ { b } = \frac { k _ { v } } { 2 } { ( c _ { v } ^ { b } - c _ { v } ^ { b , m i n } ) } ^ { 2 } } \end{array}\tag{34}
$$

where $k _ { v } = 6 . 4 \times 1 0 ^ { 1 1 } \mathrm { J } / \mathrm { m } ^ { 3 }$ (the same order of magnitude as used in previous phase-field simulations of fission gas bubble growth [11]), $c _ { v } ^ { m , m i n } = 0 , \mathrm { a n d } c _ { v } ^ { b , m i n } = 1$

其中 $k _ { v } = 6 . 4 \times 1 0 ^ { 1 1 } \mathrm { J } / \mathrm { m } ^ { 3 }$ （与之前裂变气体气泡生长相场模拟中使用的同一数量级[11]）， $\pmb { c } _ { v } ^ { m , m i n } = \pmb { 0 }$ ，以及$c _ { v } ^ { b , m i n } = 1$

## 3.2. KKS system constraints

## 3.2. KKS 系统约束

The physical concentrations are defined in terms of the phase concentrations as [23]

物理浓度是以相浓度来定义的[23]

$$
c _ { v } = [ 1 - h ( \eta ) ] c _ { v } ^ { m } + h ( \eta ) c _ { v } ^ { b }\tag{35}
$$

In addition, the KKS model requires that the local chemical potentials of a component be equal to each other in each phase [23]:

此外，KKS 模型要求在一个组分的局部化学势在每一相中相等[23]：

$$
\begin{array} { r } { \mu _ { v } = \frac { d f _ { c h e m } ^ { b } } { d c _ { v } ^ { b } } = \frac { d f _ { c h e m } ^ { m } } { d c _ { v } ^ { m } } } \end{array}\tag{36}
$$

where $\mu _ { v }$ is the chemical potential of vacancies.

其中 $\mu _ { v }$ 是空位的化学势。

## 3.3. Interfacial parameters parameterization

## 3.3. 界面参数参数化

The interfacial energy γ of the matrix-bubble interface is estimated to be $1 . 1 7 \mathrm { J } / \mathsf { m } ^ { 2 } \left[ 1 4 \right]$ . In the KKS model, the interfacial energy and interface thickness 2l are related to the gradient energy coefficient and double-well potential height via the following analytical expressions:

矩阵-气泡界面的界面能γ估计为 $1 . 1 7 \mathrm { J } / \mathsf { m } ^ { 2 } \left[ 1 4 \right]$ 。在 KKS 模型中，界面能与界面厚度 2l 通过以下解析表达式与梯度能系数和双井势能高度相关联：

$$
\begin{array} { r } { \gamma = \frac { \sqrt { \kappa W } } { 3 \sqrt { 2 } } } \end{array}\tag{37}
$$

$$
2 l = 2 . 2 \sqrt { 2 } \sqrt { \frac { \kappa } { W } }\tag{38}
$$

where the interface thickness 2l is defined as the distance between $\eta = 0 . 1 \mathrm { a n d } \eta = 0 . 9$ . 2l was chosen to be 10 nm, such that bubbles with radii from tens to hundreds of nm can be adequately resolved. With γ and 2l specified, Equations (37) and (38) can be rearranged to obtain the required values of $\kappa = 1 . 6 0 \times 1 0 ^ { - 8 } \mathrm { J / m }$ and $W = 1 . 5 4 \times 1 0 ^ { 9 } \ : \mathrm { J } / \mathrm { m } ^ { 3 }$

其中界面厚度 2l 定义为 $\pmb { \eta } = \mathbf { 0 . 1 }$ 与 $\pmb { \eta } = \mathbf { 0 . 9 }$ 之间的距离。2l选取为 10纳米，以便能够充分解析半径从几十到几百纳米的气泡。在确定了γ和 2l 之后，可以将方程（37）和（38）重新排列，以得到所需的 $\pmb { \kappa } = \mathbf { 1 . 6 0 } \times \mathbf { 1 0 ^ { - 8 } }$ J/m 和$W = 1 . 5 4 \times 1 0 ^ { 9 } \ : \mathrm { J } / \mathrm { m } ^ { 3 }$ 的值。

## 3.4. Evolution equations3.4. 发展方程

The order parameter η evolves by the Allen-Cahn equation as

序参数η通过艾伦-卡恩方程演化，如

$$
\begin{array} { r } { \frac { \partial \eta } { \partial t } = - L \left( \frac { \delta F } { \delta \eta } \right) } \end{array}\tag{39}
$$

where L is the order parameter mobility for η. Using Equations (27) and (28) of Reference [23], this can be written as

其中 L是 η 的序参数迁移率。利用参考文献[23]中的方程（27）和（28），这可以写成

$$
\begin{array} { r } { \frac { \partial \eta } { \partial t } = L \left[ \frac { d h } { d \eta } \left[ \left( f _ { c h e m } ^ { m } - f _ { c h e m } ^ { b } \right) - \mu _ { v } \left( c _ { v } ^ { m } - c _ { v } ^ { b } \right) \right] - W \frac { d g } { d \eta } + \kappa \nabla ^ { 2 } \eta \right] } \end{array}\tag{40}
$$

In the SO model, the evolution equation for vacancies is

在 SO模型中，空位的演化方程为

$$
\begin{array} { r } { \frac { \partial c _ { v } } { \partial t } = \nabla \cdot M _ { v } \nabla \mu _ { v } + S _ { v } [ 1 - h ( \eta ) ] } \end{array}\tag{41}
$$

while in the SS model, the vacancy evolution equation is

而在 SS 模型中，空位演化方程是

$$
\begin{array} { r } { \frac { \partial c _ { v } } { \partial t } = \nabla \cdot M _ { v } \nabla \mu _ { v } + S _ { v } [ 1 - h ( \eta ) ] - K _ { v } c _ { v } ^ { m } } \end{array}\tag{42}
$$

where $M _ { v }$ is the vacancy mobility, and the function $[ 1 - h ( \eta ) ]$ limits defect production to the matrix phase only. The values of $\pmb { S _ { v } }$ and $\mathbf { \nabla } \kappa _ { v }$ are varied parameterically in both models to determine their effect on growth rate. The purpose of the effective sink term $- \pmb { K } _ { v } c _ { v } ^ { m }$ is to maintain the vacancy concentration in the matrix at steady-state conditions far from any large bubbles at $c _ { v } ^ { s s } \approx 8 \times 1 0 ^ { - 3 }$ based on cluster dynamics simulations for $\mathrm { U O } _ { 2 }$ under irradiation at temperatures less than 1300 K [24]. At steady-state in the bulk solid far from any bubbles, the vacancy concentration is constant in both time and position, so $\begin{array} { r } { \frac { \partial c _ { v } } { \partial t } = 0 } \end{array}$ and $\nabla \mu _ { v } = 0$ . Under these conditions, from Equation (42),

其中 $M _ { v }$ 是空位迁移率，函数 $[ \mathbf { 1 } - h ( \pmb { \eta } ) ]$ 限制缺陷生成仅限于基体相。在两种模型中， $ { \boldsymbol { S } } _ { v }$ 和 $\pmb { K _ { v } }$ 的值参数化变化，以确定它们对生长率的影响。有效汇项 $- \pmb { K } _ { v } c _ { v } ^ { m }$ 的目的是在远离任何大气泡的 $c _ { v } ^ { s s } \approx 8 \times 1 0 ^ { - 3 }$ 处，基于对 $\mathrm { U O } _ { 2 }$ 在温度低于 1300 K的辐照下进行簇动力学模拟，保持基体中的空位浓度在稳态条件下。在远离任何气泡的固体本体中，稳态时空位浓度在时间和位置上都是恒定的，因此 $\begin{array} { r } { \frac { \partial c _ { v } } { \partial t } = 0 } \end{array}$ 和 $\nabla \mu _ { v } = 0$ 。在这些条件下，由方程（42）得出，

$$
\begin{array} { r } { K _ { v } = \frac { S _ { v } } { c _ { v } ^ { \beta } } } \end{array}\tag{43}
$$

The defect mobility was calculated from the diffusion coefficients and second derivatives of free energies for each phase as in Equation (18) of Reference [23]:

缺陷迁移率是根据扩散系数和每个相的自由能的二阶导数，按照参考文献[23]中的方程(18)计算得出的：

$$
\begin{array} { r } { M _ { v } = \frac { D _ { g } ( \phi ) } { f _ { c _ { v } c _ { v } } } = \frac { h D _ { v } ^ { b } + ( 1 - h ) D _ { v } ^ { m } } { f _ { c _ { v } c _ { v } } } } \end{array}\tag{44}
$$

where $f _ { c _ { v } c _ { v } }$ is as defined in Equation (29) of Reference [23]:

其中 $f _ { c _ { v } c _ { v } }$ 如参考文献[23]中方程（29）所定义：

$$
\begin{array} { r } { f _ { c _ { v } c _ { v } } = \frac { \frac { d ^ { 2 } f _ { c h e m } ^ { m } } { d c _ { v } ^ { 2 } } \frac { d ^ { 2 } f _ { c h e m } ^ { b } } { d c _ { v } ^ { 2 } } } { [ 1 - h ( \eta ) ] \frac { d ^ { 2 } f _ { c h e m } ^ { b } } { d c _ { v } ^ { 2 } } + h ( \eta ) \frac { d ^ { 2 } f _ { c h e m } ^ { m } } { d c _ { v } ^ { 2 } } } = k _ { v } } \end{array}\tag{45}
$$

The vacancy diffusion coefficient in the matrix $D _ { v } ^ { m } = 0 . 9 6 \mathrm { n m } ^ { 2 } / s [ 1 4 ]$ , and $D _ { v } ^ { b }$ was set to $\mathbf { 1 0 ^ { 3 } } D _ { v } ^ { m }$ . The Allen-Cahn mobility L was set sufficiently high that interface motion was controlled by defect diffusion, resulting in $L = 1 . 5 6 \times 1 0 ^ { - 1 0 } \mathrm { m } ^ { 3 } / \mathrm { J } / s$ (see Table 1 for the parameters used for phase-field simulations of bubble growth).

矩阵中的空位扩散系数为 $D _ { v } ^ { m } = 0 . 9 6 \mathrm { n m } ^ { 2 } / s [ 1 4 ]$ $D _ { v } ^ { b }$ 设定为 $\mathbf { 1 0 ^ { 3 } } D _ { v } ^ { m }$ 。艾伦-卡恩迁移率 L 设定得足够高，使得界面运动由缺陷扩散控制，导致 $L = 1 . 5 6 \times 1 0 ^ { - 1 0 } \mathrm { ~ m ~ } ^ { 3 } / \mathrm { J } / s$ （见表 1，以了解用于气泡生长相场模拟的参数）。

Table 1. Parameters used for phase-field simulations of bubble growth.

表 1.用于气泡生长相场模拟的参数。

<table><tr><td>Parameter参数</td><td>Value价值</td><td>Source源文本：源翻译文本：源</td></tr><tr><td> $c _ { v } ^ { m , m i n }$ </td><td>0</td><td>Section 3.1第三章第一节</td></tr><tr><td> $c _ { v } ^ { b , m i n }$ </td><td>1</td><td>Section3.1第三章第一节</td></tr><tr><td> $k _ { \nu }$   ${ \ " } \mathbf { k } _ { \nu }$  "似乎不是一个有效的学术文本段 对不起，您提供的源文本</td><td> $6 . 4 \times 1 0 ^ { 1 1 } \mathrm { J } / \mathrm { m } ^ { 3 }$ </td><td>Section3.1第三章第一节</td></tr><tr><td>落。为了进行准确的翻译，我需要完整的、清晰的学术文本。请提</td><td> $6 . 4 \times 1 0 ^ { \wedge } 0 \#$ </td><td></td></tr><tr><td>供一个合适的学术句子或段落，我将很乐意帮您翻译成简体中文</td><td> $\mathrm { J } / \mathrm { m } ^ { \wedge } 1 \#$ </td><td></td></tr><tr><td>K</td><td> $1 . 6 0 \times 1 0 ^ { - 8 } \mathrm { J / m }$ </td><td>Section3.3第三章第三节</td></tr><tr><td></td><td> $1 . 6 0 \times 1 0 ^ { \wedge } 0 \#$ </td><td></td></tr><tr><td></td><td>J/m</td><td></td></tr><tr><td>W</td><td> $1 . 5 4 \times 1 0 ^ { 9 } \mathrm { J } / \mathrm { m } ^ { 3 }$ </td><td>Section 3.32.3节</td></tr><tr><td></td><td> $1 . 5 4 \times 1 0 ^ { \wedge } 0$ </td><td></td></tr><tr><td></td><td> $\mathrm { J } / \mathrm { m } ^ { \wedge } 1$ </td><td></td></tr><tr><td>D</td><td> $0 . 9 6 \mathrm { n m } ^ { 2 } / \mathrm { s } 0 . 9 6$ </td><td>[14][14]译文中没有提供具体内容，因为源</td></tr><tr><td></td><td>纳米  $^ 2 / \textcircled { \ast } \textcircled { }$ </td><td>文本中未包含任何要翻译的文本内容。如果</td></tr><tr><td>L</td><td></td><td>需要翻译特定的学术文本，请提供源文本</td></tr><tr><td></td><td> $1 . 5 6 \times 1 0 ^ { - 1 0 }$ </td><td>Section3.4第三章第四节</td></tr><tr><td></td><td> $\mathrm { m } ^ { 3 } / \mathrm { J } / s$ </td><td></td></tr><tr><td></td><td> $1 . 5 6 \times 1 0 ^ { \wedge } 0 \#$  米</td><td></td></tr><tr><td></td><td>^1#/焦/秒</td><td></td></tr></table>

The evolution equations were non-dimensionalized using the characteristic energy scale $\pmb { E } ^ { * } = \mathbf { 6 4 } \times \mathbf { 1 0 ^ { 9 } } \mathbf { J } / \mathrm { m ^ { 3 } } ,$ length scale $l ^ { * } = 1 \mathrm { n m }$ , and time scale $\tau ^ { * } = 1 s ,$ , and discretized using the finite element method as implemented in the MOOSE framework [25]. Since the simulations have spherical symmetry, the problem is solved in spherical coordinates, with symmetry allowing the problem to be solved in 1D as a function of the radial coordinate r only. The simulation domain size $\mathcal { R } = 5 0 0 \mathrm { n m }$ in each case, and 1D elements are used with linear Lagrange shape functions, with a mesh size $\Delta r = 1 \mathrm { { n m } }$

演化方程通过使用特征能量尺度 $\pmb { E } ^ { * } = \mathbf { 6 4 } \times \mathbf { 1 0 ^ { 9 } } \mathrm { J } / \mathrm { m } ^ { 3 }$ 、长度尺度 $\ l ^ { l ^ { * } } = 1$ 纳米和时间的尺度 $\tau ^ { * } = 1$ 秒进行了无量纲化，并采用 MOOSE框架中实现的有限元方法进行了离散化[25]。由于模拟具有球对称性，问题在球坐标系中解决，对称性使得问题可以仅作为径向坐标 r的函数在 1D中解决。每种情况下，模拟域的大小为 $\mathcal { R } = 5 0 0$ 纳米，并使用线性拉格朗日形状函数的 1D 单元，网格大小为 $\Delta r = 1$ 纳米。

Natural boundary conditions are used, resulting in no-flux boundary conditions for chemical species and a zerogradient condition for η. Time integration uses the second-order backward differentiation formula. The evolution equations are solved at each time step using the preconditioned Jacobian-Free Newton-Krylov method. Adaptive time stepping is used with the IterationAdaptiveDT algorithm as implemented in the MOOSE framework [26].

采用自然边界条件，导致化学物种的无流量边界条件以及η的零梯度条件。时间积分使用二阶向后差分公式。在每个时间步长中，使用预调条件的雅可比自由牛顿-克里洛夫方法求解演化方程。自适应时间步长采用 MOOSE 框架中实现的IterationAdaptiveDT 算法[26]。

## 4. Results4. 结果

## 4.1. Source-only model simulations

## 4.1 仅源模型模拟

The growth of a bubble with initial radius of 30 nm was simulated with the source-only model (Equation (41)). This initial bubble size and the simulation times were chosen so that the bubble sizes in simulations would span the range of experimentally observed bubble sizes in Ref. [27]. The initial concentrations of vacancies in the void and matrix phases were adjusted to 1.0001214 and $\mathbf { 1 . 2 1 4 \times 1 0 ^ { - 4 } }$ , respectively, to account for the Gibbs-Thomson shift in composition as per Equation (3). The source term was set to $ { \boldsymbol { S } } _ { v } = 4 . 0 9 2 \times 1 0 ^ { - 1 0 } \  { s } ^ { - 1 }$ . This is approximately 5 times larger than the Xe source term for typical light-water reactor conditions [14], which is within the range considered in past parametric studies of source term strength [11]. The bubble radius as a function of time (as determined by the position where $\pmb { \eta = 0 . 5 }$ by interpolation of the finite element shape functions at each time step) is shown in Fig. 1a, showing that the bubble grows to a radius of approximately 100 nm at the end of the simulation time of $\mathbf { 2 \times 1 0 ^ { 7 } }$ s. The rate of change in bubble size $\frac { d R } { d t }$ at each simulation time t was calculated using backward finite differences of the interface position:

初始半径为 30纳米的气泡增长通过仅源模型（方程（41））进行了模拟。选择这个初始气泡大小和模拟时间是为了使模拟中的气泡大小范围覆盖文献[27]中实验观察到的气泡大小。空腔相和基体相中的空位初始浓度分别调整为 1.0001214和 $\mathbf { 1 . 2 1 4 \times 1 0 ^ { - 4 } }$ ，以根据方程（3）考虑吉布斯-汤姆逊组成偏移。源项设置为 $ { S _ { v } } = 4 . 0 9 2 \times 1 0 ^ { - 1 0 } \  { s } ^ { - 1 }$ 。这大约是典型轻水反应堆条件下氙源项的 5 倍[14]，位于过去参数研究中考虑的源项强度范围之内[11]。图 1a 显示了气泡半径随时间的变化（通过在每个时间步长对有限元形状函数进行插值确定的 $\pmb { \eta = 0 . 5 }$ 位置），表明在模拟时间结束时 $\mathbf { 2 \times 1 0 ^ { 7 } }$ 秒，气泡增长到大约 100纳米的半径。在每个模拟时间 t，气泡大小的变化率 $\frac { d R } { d t }$ 通过界面位置的向后有限差分进行了计算：

$$
\begin{array} { r } { \frac { d R } { d t } ( t ) = \frac { R ( t ) - R ( t - \Delta t ) } { \Delta t } } \end{array}\tag{46}
$$

where $R ( t )$ is the bubble radius at the current time step, $R ( t - \Delta t )$ is the radius at the previous time step, and Δt is the interval between the previous and current time steps. The relatively fine mesh size of $\Delta r = 1$ relative to $2 l = 1 0$ nm was used to reduce noise in the calculation of $d R / d t . \ { \frac { d R } { d t } }$ from the simulation is plotted as a function of R in Fig. 1b, along with the predicted value of $\frac { d R } { d t }$ from the quasi-steady state model from Equation (10). The simulated $\frac { d R } { d t }$ starts at 0 and begins to increase as vacancies build up as they are created by the source term. The growth rate predicted by the quasi-steady state approximation starts much higher because it assumes the vacancy concentration profile is already in steady-state and thus does not account for the time required for vacancies to build up to the steady-state profile. At $R \approx 4 0 \ : \mathrm { n m }$ , the simulated growth rate reaches a maximum and then becomes to decrease as the vacancy concentration approaches its steady-state profile. At this point the simulated rate approaches the quasi-steady state approximation. The simulated growth rate closely matches the quasi-steady state approximation for $R > 6 5 \ : \mathrm { n m }$ . The vacancy concentration profile as a function of r at time $\smash { t = 1 . 4 \times 1 0 ^ { 7 } }$ s is shown in Fig. 1c for both the simulation and quasi-steady state approximation. Although the simulated $c _ { v }$ profile is slightly lower in magnitude than the analytical expression, the slope is approximately the same near the bubblematrix interface, meaning that the flux and therefore $\frac { d R } { d t }$ is very nearly the same by this time.

其中 $R ( t )$ 是当前时间步的气泡半径， $R ( t - \Delta t )$ 是前一个时间步的半径，Δt 是前一个时间步与当前时间步之间的时间间隔。相对于 $2 l = 1 0$ 纳米的 $\Delta r = 1$ 较细网格尺寸被用来减少 $d R / d t$ 计算中的噪声。图 1b 中绘制 $\overline { { \int } } \frac { d R } { d t }$ 从模拟中得到的值作为 R 的函数，并与由方程（10）的准稳态模型预测的 $\textstyle { \frac { d R } { d t } }$ 值一起显示。模拟的 $\textstyle { \frac { d R } { d t } }$ 从 0 开始，随着空位由源项产生并逐渐积累而开始增加。准稳态近似预测的增长率开始时高得多，因为它假设空位浓度分布已经达到稳态，因此没有考虑到空位积累到稳态分布所需的时间。在 $R \approx 4 0$ 纳米时，模拟的增长率达到最大值，然后随着空位浓度接近其稳态分布而开始下降。此时，模拟的速率接近准稳态近似。模拟的增长率在 $\pmb { R } > 6 5$ 纳米时与准稳态近似非常接近。图 1c展示了在 $\smash { t = 1 . 4 \times 1 0 ^ { 7 } }$ 秒时，空位浓度剖面作为 r 的函数，同时显示了模拟和准稳态近似的结果。尽管模拟的 $c _ { v }$ 剖面在量级上略低于解析表达式，但在气泡-基体界面附近斜率大致相同，这意味着此时通量以及 $\frac { d R } { d t }$ 几乎相同。

![](images/9918e8b7036f5017312522ccba173da5469faf97790716d97c3fa39c9fc4c7f5.jpg)

![](images/9f8d8bfa992d3ece5667cb2552590e889df1f0849d2e8c2d14014c7f7fe53baf.jpg)

![](images/499c2d2bd63dbb1769db9d21b3fe486c54d30a7044a1c3bd120e6ba075a89608.jpg)  
Fig. 1. Simulations with vacancy source only (SO) and comparison to quasi-steady state approximation. $S _ { v } = 4 . 0 9 2 \times 1 0 ^ { - 1 0 } \ : \mathrm { s } ^ { - 1 } , D _ { v } = 0 . 9 6 \ : \mathrm { n m } ^ { 2 } / \mathrm { s } . ( \mathrm { a } )$ Void radius R, as determined by finding the position where $\eta = 0 . 5$ by interpolation of the finite element shape function at each time step. (b) Void growth rate $d R / d t .$ dR/dt was calculated at each time step using backward finite differences of the interface position with respect to time, as described in Equation (46). (c) Vacancy concentration as a function of radius at $t { = } 1 . 4 \times 1 0 ^ { 7 } s$ .  
图 1.仅含空位源（SO）的模拟及其与准稳态近似的比较。 $\textsf { S } _ { \nu } = 4 . 0 9 2 \times 1 0 ^ { - 1 0 } { s ^ { - 1 } }$ ， $\mathrm { ~ D ~ } _ { \nu } = 0 . 9 6$ nm $^ 2 / s$ 。（a）通过在每个时间步长插值有限元形状函数找到 $\mathsf { \Pi } \mathsf { \Pi } \mathsf { \Pi } \mathsf { \Pi } \mathsf { \Pi } \mathsf { \Pi } \mathsf { \Pi } \mathsf { \Pi } \mathsf { \Pi } \mathsf { \Pi } \mathsf { \Pi } \mathsf { \Pi } \mathsf { \Pi } \mathsf { \Pi } \mathsf { \Pi } \mathsf { \Pi } \mathsf { \Pi } \mathsf { \Pi } \mathsf { \Pi } \mathsf { \Pi } \mathsf { \Pi } \mathsf { \Pi } \mathsf { \Pi } \mathsf { \Pi } \mathsf { \Pi } \mathsf { \Pi } \mathsf { \Pi } \mathsf { \Pi } \mathsf { \Pi } \mathsf { \Pi } \mathsf { \Pi } \mathsf { \Pi } \mathsf { \Pi } \mathsf { \Pi } \mathsf { \Pi } \mathsf { \Pi } \mathsf { \Pi } \mathsf { \Pi } \mathsf { \Pi } \mathsf { \Pi } \mathsf { \Pi } \mathsf { \Pi } \mathsf { \Pi } \mathsf { \Pi } \mathsf { \Pi } \mathsf { \Pi } \mathsf { \Pi \Pi } \mathsf { \Pi } \mathsf { \Pi \Pi } \mathsf \mathsf { \Pi } \mathsf \mathsf { \Pi \Pi } \mathsf \mathsf { \Pi \Pi } \mathsf \mathsf \mathsf  \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi \Pi$ 的位置确定的孔洞半径 R。（b）孔洞生长速率 dR/dt。在每个时间步长使用相对于时间的界面位置的后向有限差分计算 $\mathrm { d R } / \mathrm { d t }$ ，如方程（46）所述。（c）在 $\mathrm { t } = 1 . 4 \times 1 0 ^ { 7 } s$ 时，空位浓度随半径的变化。

To understand the effect of significantly increasing the effective vacancy production rate, the value of $S _ { v }$ was increased by a factor of $1 0 ^ { 2 }$ to $ { \boldsymbol { S } } _ { v } = 4 . 0 9 2 \times 1 0 ^ { - 8 } \  { s } ^ { - 1 }$ , as shown in Fig. 2. As expected, the bubble size grew much faster, reaching a radius of over 160 nm after a much shorter simulation time of $\mathbf { 1 \times 1 0 ^ { 6 } }$ s compared with Fig. 1. The simulated $\frac { d R } { d t }$ is shown in Fig. 2b and compared to the analytical steady-state approximation. The bubble size increases much more significantly before there is good agreement between the simulation results and the analytical solution. This is because the bubble growth rate is significantly higher, meaning that the quasi-steady state approximation breaks down. Only toward the later times in the simulation, when $\frac { d R } { d t }$ has decreased significantly, does the simulation come into reasonable agreement with the analytical solution. The vacancy

concentration profile $c _ { v }$ versus r is shown in Fig. 2c at $\pmb { t = 5 \times 1 0 ^ { 5 } \ s }$ , where $R = 1 1 0 \mathrm { n m }$ . The slope of the simulated $c _ { v }$ profile is steeper than the analytical solution, meaning that the growth rate is slightly larger in simulation at this time, as seen in Fig. 2b.

为了理解显著提高有效空位产生率的效果，图 2所示，将 $S _ { v }$ 的值增加了 10 倍 至2 $S _ { v } = 4 . 0 9 2 \times 1 0 ^ { - 8 } \ \textcircled { \cdot } \mathrm { { / / } } \ \mathrm { { ^ { - 1 } } }$ 。如预期，气泡大小增长得更快，在比图 1短得多的模拟时间 $\mathbf { 1 \times 1 0 ^ { 6 } }$ 秒后，气泡半径超过 160 纳米。模拟的 $\frac { d R } { d t }$ 如图 2b 所示，并与解析稳态近似进行了比较。在模拟结果与解析解之间达到良好一致之前，气泡大小显著增加。这是因为气泡增长率显著提高，意味着准稳态近似不再适用。只有在模拟后期，当 $\textstyle { \frac { d R } { d t } }$ 显著降低时，模拟才与解析解有合理的一致性。空位浓度分布 $\pmb { c _ { v } }$ 与 r 的关系在图 2c中 $\pmb { t = 5 \times 1 0 ^ { 5 } }$ 秒时显示，其中 $\pmb { R } = \pmb { 1 } \pmb { 1 0 }$ 纳米。模拟的 $c _ { v }$ 分布曲线的斜率比解析解更陡峭，意味着在此时模拟中的增长率略大，如图 2b所示。

![](images/ac46783fb8799e6cdeb6ca13738f02d6640f44afb01b03fe939294be30f2b59f.jpg)

![](images/7850dc8b92e491e5bbcb5f88bc21d12f18a31e07f7e172622a5195fe1bfb0d46.jpg)

![](images/ba2e53485b48195f453cd7bfbb893f145df20319565a6de14065449dbb680da1.jpg)  
Fig. 2. Simulations with vacancy source only (SO) and comparison to quasi-steady state approximation for increased vacancy source term. $S _ { \nu } { = } 4 . 0 9 2 \times 1 0 ^ { - 8 } \ : \mathrm { s } ^ { - 1 } , D _ { \nu } { = } 0 . 9 6 \ : \mathrm { n m } ^ { 2 } / \mathrm { s } .$ (a) Void radius R, (b) void growth rate dR/dt, (c) vacancy concentration as a function of radius at $t = 5 \times 1 0 ^ { 5 } s$  
图 2. 仅含空位源（SO）的模拟以及与增加空位源项的准稳态近似比较。 $\mathsf { S } _ { \nu } = 4 . 0 9 2 \times 1 0 ^ { - 8 } \mathsf { s } ^ { - 1 } \mathrm { ~ , ~ } \mathsf { D } _ { \nu } = 0 . 9 6 \mathrm { n m } ^ { 2 } / \mathsf { s } ,$ (a) 空洞半径 R，(b) 空洞生长速率 dR/dt，(c) 在 $\mathrm { t } = 5 \times 1 0 ^ { 5 } s$ 时，空位浓度随半径的变化。  
These results show that the quasi-steady state analytical model begins to deviate from the phase-field model predictions of bubble growth rate as the value of $\pmb { S _ { v } }$ becomes orders of magnitude larger than the Xe production

rate. Thus, care should be taken when using the analytical model predictions to parameterize phase-field simulations. This issue is further considered in Section 5.2.

这些结果表明，当 $ { \boldsymbol { S } } _ { v }$ 的值比 $\mathtt { X e }$ 产生速率大几个数量级时，准稳态分析模型开始偏离相场模型对气泡增长率预测。因此，在使用分析模型预测来参数化相场模拟时应谨慎。这一问题在第 5.2 节中进一步讨论。

## 4.2. Source+sink model simulations

## 4.2. 源汇模型模拟

Growth of a 30 nm bubble was simulated using the SS model using Equation (42). The vacancy source term was set to $1 0 ^ { 4 }$ times greater than the fission rate, as expected in typical light water reactor conditions [20], resulting in $ { \boldsymbol { S } } _ { v } = 4 . 0 9 2 \times 1 0 ^ { - 6 } \  { \boldsymbol { s } } ^ { - 1 }$ [14]. The sink term was set to maintain $c _ { v } ^ { s s } = 0 . 0 0 8$ , resulting in $K _ { v } = 5 . 1 1 4 \times 1 0 ^ { - 4 } \ s ^ { - 1 }$ using Equation (43). Simulation results are shown in Fig. 3. The growth rate of the bubble is even greater than the high $ { \boldsymbol { S } } _ { v }$ cases considered for the SO model, reaching a final radius of 319 nm at the end of the simulation time of $1 0 ^ { 6 } \mathtt { s } ( \mathtt { F i g } . 3 \mathsf { a } )$ . The growth rate in the simulation is compared to the quasi-steady state analytical model of Equation (26) in Fig. 3b. The general trends of the simulation and analytical model are consistent. During the initial stages of growth, the ${ \bf 1 } / R$ term in Equation (26) is comparable to the $\sqrt { K _ { v } / D _ { v } }$ term, and as R increases, the growth rate goes down. As R increases past 150 nm, the ${ \bf 1 } / R$ term becomes small compared to the $\sqrt { K _ { v } / D _ { v } }$ term and the growth rate approaches a constant value. Although the analytical model captures the trend well, the simulated growth rate is somewhat larger, indicating that the growth rate is high enough that analytical model has begun to break down. Nonetheless, the analytical model provides useful qualitative understanding of the reasons for the trend in growth rate with changing radius. The vacancy concentration profile versus radius from simulation is shown in Fig. 3c at time $\mathbf { \mathit { t } } = \mathbf { 2 } \times \mathbf { 1 0 ^ { 5 } }$ s and compared to the analytical expression of Equation (25). Agreement between simulation and the analytical model is good and the vacancy concentration reaches the expected value of $c _ { v } ^ { s s } = 0 . 0 0 8$ far from the bubble.

使用 SS 模型通过方程（42）模拟了 30纳米气泡的生长。空位源项设置为裂变率的 $1 0 ^ { 4 }$ 倍，这在典型的轻水反应堆条件下是预期的 [20]，导致 $S _ { v } = 4 . 0 9 2 \times 1 0 ^ { - 6 } ~ \rlap / _ { \parallel } \jmath _ { v } ^ { - 1 } \left[ 1 4 \right]$ 。汇项被设置为保持 $c _ { v } ^ { s s } = 0 . 0 0 8$ ，使用方程（43）得到$K _ { v } = 5 . 1 1 4 \times 1 0 ^ { - 4 }$ 秒 。模拟结果如图 3 所示。气泡的生长速率甚至超过了 SO 模型中考虑的高−1 $ { \boldsymbol { S } } _ { v }$ 情况，到模拟结束时达到 319纳米的最终半径，模拟时间为 $1 0 ^ { 6 }$ 秒（图 3a）。模拟中的生长速率与图 3b中的方程（26）的准稳态解析模型进行了比较。模拟和解析模型的总趋势是一致的。在生长的初始阶段，方程（26）中的 $1 / R$ 项与 $\sqrt { K _ { v } / D _ { v } }$ 项相当，随着 R的增加，生长速率下降。当 R 超过 150纳米时， $1 / R$ 项相对于 $\sqrt { K _ { v } / D _ { v } }$ 项变得较小，生长速率接近一个常数。 尽管分析模型很好地捕捉了趋势，但模拟的增长率略大，表明增长率足够高以至于分析模型已经开始失效。然而，分析模型仍然为理解随着半径变化增长率趋势的原因提供了有用的定性理解。图 3c 显示了在时间 $\pmb { t = 2 \times 1 0 ^ { 5 } }$ 秒时，模拟得到的空位浓度剖面与半径的关系，并与方程（25）的解析表达式进行了比较。模拟与解析模型之间的一致性良好，空位浓度在远离气泡的地方达到了预期的 $c _ { v } ^ { s s } = 0 . 0 0 8$ 值。

![](images/fc93c36020e1ef8b34d83b97068681feac1e6e70e88759b521678bcceb74d401.jpg)

![](images/5970ce9ffdcaf34ec3de7eaaa426ff4586d90f3a2ae06e638a9f342cdd4049f8.jpg)

![](images/a98c97b2adcc6f6e810d5c52cf34b469d47bd58f8466f9905f0c3dda873fe41a.jpg)  
Fig. 3. Simulations with vacancy source and effective sink (SS) and comparison to quasi-steady state approximation. $S _ { \nu } = 4 . 0 9 2 \times 1 0 ^ { - 6 } \ s ^ { - 1 } , K _ { \nu } = 5 . 1 1 4 \times 1 0 ^ { - 4 } \ s ^ { - 1 } , D _ { \nu } = 0 . 9 6 \ \mathrm { n m } ^ { 2 } / s .$ . (a) Void radius R, (b) void growth rate $d R / d t ,$ (c) vacancy concentration as a function of radius at $t = 2 \times 1 0 ^ { 5 }$ s.  
图 3.具有空位源和有效汇（SS）的模拟以及与准稳态近似的比较。 $\textsf { S } _ { \nu } = 4 . 0 9 2 \times 1 0 ^ { - 6 } \varsigma ^ { - 1 } , \ \mathrm {  ~ K ~ } _ { \nu } = 5 . 1 1 4 \times 1 0 ^ { - 4 } \varsigma ^ { - 1 }$ $\textsf { D } _ { v }$ $= 0 . 9 6 \mathrm { n m } ^ { 2 } / s$ 。 (a) 空洞半径 R，(b) 空洞生长速率 dR/dt，(c) 在 $\mathrm { t } = 2 \times 1 0 ^ { 5 } \mathrm { s }$ 时空位浓度随半径的变化。

The effect of changing the source and effective sink terms is studied next. The growth rate predicted by the chemical stress model, Equation (30), remains constant as long as $c _ { v } ^ { s s }$ in the matrix far from the bubbles is maintained at the same value. To test whether the SS model shows this same behavior, the vacancy source and effective sink were doubled from the values considered in Fig. 3, resulting in $S _ { v } = 8 . 1 8 4 \times 1 0 ^ { - 6 } \ s ^ { - 1 }$ and $K _ { v } = 1 . 0 2 2 8 \times 1 0 ^ { - 3 } \ s ^ { - 1 }$ , which maintains $c _ { v } ^ { s s } = 0 . 0 0 8$ . Fig. 4a shows that the growth rate increases significantly compared to Fig. 3a, even though $c _ { v } ^ { s s }$ is the same between the two models. This behavior, contrary to the chemical stress model, can fairly be called a disadvantage of the SS model. The growth rate from the simulation is compared to the quasi-steady state analytical model in Fig. 4b. The analytical model correctly predicts the trend of increased growth rate relative to the previous case of $S _ { v } = 4 . 0 9 2 \times { \bf 1 0 } ^ { - 6 } \ s ^ { - 1 } , K _ { v } = 5 . 1 1 4 \times { \bf 1 0 } ^ { - 4 } \ s ^ { - 1 }$ . From Equation (26), the $\sqrt { K _ { v } / D _ { v } }$ term is larger than considered in Fig. 3b, resulting in the larger growth rate. The vacancy concentration profile versus radius for this case is shown in Fig. 4c $\operatorname { a t } t = 2 \times 1 0 ^ { 5 } :$ s, showing good agreement

接下来研究了改变源项和有效汇项的影响。只要保持远离气泡的基体中的 $c _ { v } ^ { s s }$ 值不变，化学应力模型（方程 30）预测的增长率将保持恒定。为了测试 SS 模型是否表现出相同的行为，将空位源和有效汇的值从图 3 中的数值加倍，得到$S _ { v } = 8 . 1 8 4 \times 1 0 ^ { - 6 } \ s ^ { - 1 }$ 和 $K _ { v } = 1 . 0 2 2 8 \times 1 0 ^ { - 3 } \ s ^ { - 1 }$ ，这保持了 $c _ { v } ^ { s s } = 0 . 0 0 8$ 。图 4a 显示，尽管两个模型中的 $c _ { v } ^ { s s }$ 相同，但增长率相比图 3a 显著增加。这种行为与化学应力模型相反，可以公平地称为 SS 模型的缺点。模拟得到的增长率与准稳态解析模型在图 4b中进行了比较。解析模型正确预测了相对于之前 $ { S _ { v } } = 4 . 0 9 2 \times 1 0 ^ { - 6 } \ s ^ { - 1 }$ ，$K _ { v } = 5 . 1 1 4 \times 1 0 ^ { - 4 } \ s ^ { - 1 }$ 情况下的增长率增加趋势。由方程（26）可知， $\sqrt { K _ { v } / D _ { v } }$ 项大于图 3b 中的考虑值，导致增长率更大。此案例下的空位浓度剖面与半径的关系在图中显示。 4c在 $\pmb { t = 2 } \times \pmb { 1 0 ^ { 5 } } \ s$ 时，显示出模拟结果与解析模型之间有良好的一致性。

![](images/6ab7c5d62e9f3e70101daf11bb8824acb072be7c6260510567ae46f25c09c0bd.jpg)

![](images/92aaf8a796cd0e60d341a36f0dc29d43395ee6a2bbfdfbbb81424517f017e6a5.jpg)

![](images/d389782bd3eabbe79481e986c247d2468c33f149663ee82f61cdd587b90b2835.jpg)  
Fig. 4. Simulations with vacancy source and effective sink (SS) and comparison to quasi-steady state approximation for increased $S _ { \nu }$ and $K _ { \nu } ,$ maintaining the same vacancy concentration far from the bubble in the matrix, $c _ { v } ^ { s s } = 0 . 0 0 8$ $S _ { v } = 8 . 1 8 4 \times 1 0 ^ { - 6 } \ : s ^ { - 1 } , K _ { v } = 1 . 0 2 2 8 \times 1 0 ^ { - 3 } \ : s ^ { - 1 } , D _ { v } = 0 . 9 6 \ : \mathrm { n m ^ { 2 } / s . \ : ( a ) }$ Void radius R, (b) void growth rate $d R / d t ,$ (c) vacancy concentration as a function of radius at $t { = } 2 \times 1 0 ^ { 5 } s$

图 4.具有空位源和有效汇（SS）的模拟，以及与准稳态近似法的比较，增加了 $\textsf { S } _ { \nu }$ 和 $\mathrm { K } _ { \nu }$ ，保持远离气泡的基体中空位浓度相同， $c _ { v } ^ { s s } = 0 . 0 0 8$ 。 $\mathsf { S } _ { \nu } = 8 . 1 8 4 \times 1 0 ^ { - 6 } \varsigma ^ { - 1 }$ ， $\mathrm { ~ K ~ } _ { \nu } = 1 . 0 2 2 8 \times 1 0 ^ { - 3 } \ s ^ { - 1 }$ ， $\mathrm { ~ D ~ } _ { \nu } = 0 . 9 6 \mathrm { ~ n m ~ } ^ { 2 } / s$ 。 (a) 气孔半径 R，(b)气孔生长速率 dR/dt，(c) 在 $\mathrm { t } = 2 \times 1 0 ^ { 5 } \mathrm { s }$ 时，空位浓度随半径的变化。

The effect of vacancy diffusivity is next considered in the SS model. To clarify its expected impact, Equation (26) can be rewritten as

在 SS 模型中接下来考虑空位扩散性的影响。为了明确其预期影响，方程（26）可以重写为

$$
\begin{array} { r } { \frac { d R } { d t } = \left( \frac { S _ { v } } { K _ { v } } - c _ { v R } \right) \left( \sqrt { K _ { v } D _ { v } } + \frac { D _ { v } } { R } \right) } \end{array}\tag{47}
$$

Thus, a decrease in $D _ { v }$ is expected to decrease the growth rate at all times. Figs. 5a and 5b show that this is indeed the case. Agreement between the simulated vacancy concentration profile and the quasi-steady state analytical model is again relatively good, as shown in Fig. 5c at $\mathbf { \pmb { t } } = \mathbf { 2 } \times \mathbf { 1 0 ^ { 5 } }$ s.

因此，预计 $D _ { v }$ 的减少将会在所有时刻降低增长率。图 5a 和 5b 显示情况确实如此。模拟的空位浓度剖面与准稳态解析模型之间的一致性相对较好，如图 5c在 $\mathbf { { \pmb t } = 2 \times 1 0 ^ { 5 } }$ 秒时所示。

![](images/8bced93f3dcf54b4e6bd5dd97a274be8747c722ef48f82ff2bfb28eeb476b2f1.jpg)

![](images/72171288b8cd4d74d90324f4cc726874c36073696d5d8946a1d85595fa73f499.jpg)

![](images/bc619baf2a939feaecb8081d3728b26b8852c4f03ac72d325f9bf5651e2e1361.jpg)  
Fig. 5. Simulations with vacancy source and effective sink (SS) and comparison to quasi-steady state approximation for decreased $D _ { \nu ^ { * } } S _ { \nu } = 4 . 0 9 2 \times 1 0 ^ { - 6 } s ^ { - 1 } , K _ { \nu } = 5 . 1 1 4 \times 1 0 ^ { - 4 } s ^ { - 1 } , D _ { \nu } = 0 . 4 8 \mathrm { n m } ^ { 2 } / s . ( \mathrm { a } )$ Void radius R, (b) void growth rate dR/dt, (c) vacancy concentration as a function of radius at $t = 2 \times 1 0 ^ { 5 }$ s.  
图 5.具有空位源和有效汇（SS）的模拟，以及与降低 $\mathrm { ~ D ~ } _ { \nu }$ 的准稳态近似比较。 $\mathsf { S } _ { \nu } = 4 . 0 9 2 \times 1 0 ^ { - 6 } \mathsf { s } ^ { - 1 }$ ， $\mathrm { ~ K ~ } _ { \nu } = 5 . 1 1 4 \times 1 0$ $^ { - 4 } \thinspace s ^ { \ - 1 }$ $\mathrm { ~ D ~ } _ { \nu } = 0 . 4 8 \ \mathrm { n m } ^ { 2 } / s$ 。 (a) 空洞半径 R，(b) 空洞生长速率 dR/dt，(c) 在 $\mathrm { t } = 2 \times 1 0 ^ { 5 } s$ 时，空位浓度随半径的变化。

## 5. Discussion5. 讨论

## 5.1. Comparison of Source-only and Source+sink phase-field models

## 5.1. 源端仅模型与源端+汇端相场模型的比较

The SO phase-field model can be parameterized to match the physical growth rate of bubbles using the simple expression of Equation (10). The SS phase-field model is initially appealing in that it allows the physical value of $c _ { v } ^ { s s }$ to be maintained in the bulk of the matrix. However, it is difficult to parameterize the SS model to match physical growth rates. By Equation (47), $ { \boldsymbol { S } } _ { v }$ $D _ { v }$ , and $\pmb { K } _ { v }$ all impact the growth rate. Although $ { \boldsymbol { S } } _ { v }$ and $\pmb { K _ { v } }$ could be considered as effective parameters whose values do not necessarily need to match physical constants, $D _ { v }$ is an important physical parameter whose value controls the rates of other processes such as coarsening, and adjusting it to an arbitrary value could unphysically affect the rates of these other processes. Thus, when trying to match a growth rate from a more physical model, the SO approach is more suitable.

SO相场模型可以通过参数化来匹配气泡的物理生长速率，使用方程（10）的简单表达式。SS 相场模型最初吸引人之处在于它允许在基体的大部分中保持 $c _ { v } ^ { s s }$ 的物理值。然而，很难对 SS 模型进行参数化以匹配物理生长速率。根据方程（47）， $\pmb { S _ { v } }$ ， $D _ { v }$ ，和 $\pmb { K _ { v } }$ 都影响生长速率。尽管 $ { \boldsymbol { S } } _ { v }$ 和 $\pmb { K _ { v } }$ 可以被视为有效参数，其值不一定需要与物理常数匹配，但 $D _ { v }$ 是一个重要的物理参数，其值控制了其他过程如粗化的速率，调整它到任意值可能会非物理地影响这些其他过程的速率。因此，在尝试匹配一个更物理模型的生长速率时，SO 方法更为合适。

## 5.2. Comparison to chemical stress model

## 5.2与化学应激模型的比较

The chemical stress model includes the effect of interstitial and vacancy production, recombination, and sink absorption, and thus provides a more complete physical picture of bubble growth for this simplified geometry, although several approximations are needed to reach the analytical expression of Equation (30). Thus, one potential strategy for parameterizing vacancy-only phase-field models of void and fission gas bubble growth is to set the phase-field model parameters so that they best match the growth rates of the chemical stress model. Due to the disadvantages of the SS model discussed in Section 5.1, we focus on the SO model for comparison with the chemical stress model.

化学应力模型包含了间隙和空位产生、复合以及汇吸收的影响，因此为这种简化几何结构下的气泡生长提供了一个更完整的物理图像，尽管需要一些近似来得到方程（30）的分析表达式。因此，一种潜在的参数化仅空位相场模型中空洞和裂变气体气泡生长的策略是，设置相场模型参数以使其最佳匹配化学应力模型中的生长速率。由于在第 5.1节中讨论的SS 模型的缺点，我们专注于 SO模型与化学应力模型进行比较。

The bubble radius as a function of time for the chemical stress model can be determined by integrating Equation (30) analytically and using the boundary condition $\textstyle R = R _ { 0 }$ at . Assuming that $c _ { v } ^ { s s } \gg c _ { v R }$ , this results in 气泡半径作为化学应力模型中时间的函数，可以通过解析地积分方程（30）并使用边界条件 $R = R _ { 0 }$ 在 $\pmb { t = 0 }$ 上确定。 假设 $c _ { v } ^ { s s } \gg c _ { v R }$ ，这将导致

$$
\begin{array} { r } { R = \Big [ 2 D _ { v } \left( 1 - \frac { Z _ { v } } { Z _ { i } } \right) c _ { v } ^ { s s } t + R _ { 0 } ^ { 2 } \Big ] ^ { 1 / 2 } } \end{array}\tag{48}
$$

Similarly, the bubble radius as a function of time can be determined for the SO model by integrating Equation (10) and again using $\textstyle R = R _ { 0 }$ at , resulting in

同样地，可以通过对方程（10）进行积分，并再次使用 $\textstyle R = R _ { 0 }$ 在 $\pmb { t = 0 }$ 处，来确定 SO 模型中气泡半径随时间变化的函数，从而得到

$$
R = \left[ S _ { v } \mathcal { R } ^ { 3 } t + R _ { 0 } ^ { 3 } \right] ^ { 1 / 3 }\tag{49}
$$

The vacancy source strength $S _ { v }$ can be determined by finding the value that provides the best match between Equation (48) and (49). Since the exact values of $\scriptstyle { Z _ { v } }$ are $\textstyle z _ { i }$ are not important here, only their ratio, and $\textstyle z _ { i }$ is typically greater than $\boldsymbol { Z _ { v } }$ by a few percent [20], we choose $\textstyle z _ { v } = 1$ and $Z _ { i } = 1 . 1$ . Using a least-squares based optimization, we found that $S _ { v } = \bf { 1 . 5 3 } \times \bf { 1 0 ^ { - 9 } } \ \varsigma ^ { - 1 }$ provided the best match, as shown in Fig. 6. Because of the different R-dependence of the two models, a perfect match throughout the growth process is not possible, but bubble radii are quite close for the full range of time considered. A phase-field simulation of void growth with $S _ { v } = 1 . 5 3 \times 1 0 ^ { - 9 } \ s ^ { - 1 }$ was also performed, and the bubble radius from the simulation is also shown in Fig. 6. The simulated bubble radius is in very good agreement with the SO model, indicating that this value of $ { \boldsymbol { S } } _ { v }$ is not large enough to cause significant discrepancy between the quasi-steady state analytical model and the phase-field model, as was discussed in Section 4.1. As seen in Fig. 6, the SO model is in reasonably good agreement with the chemical stress model throughout a physically reasonable simulation time of $\mathbf { 2 \times 1 0 ^ { 7 } }$ s for $\mathrm { U O } _ { 2 }$ fuel in typical light water reactor (LWR) operating conditions. Thus, the SO model can be parameterized with $S _ { v } = \bf { 1 . 5 3 } \times \bf { 1 0 ^ { - 9 } } \ s ^ { - 1 }$ to represent the more complex kinetics of the full vacancy-interstitial model. This value of $S _ { v }$ is 15.9 times greater than the Xe production rate in typical light water reactor operation [14], and thus within the range of $ { \boldsymbol { S } } _ { v }$ values considered in previous parametric study [11]. This “effective” $S _ { v }$ value, representing the combined effects of Frenkel pair production, recombination, and sink absorption, is significantly lower than the expected value of Frenkel pair production itself, which is on the order of $1 0 ^ { 4 }$ times the fission rate.

空位源强度 $ { \boldsymbol { S } } _ { v }$ 可以通过找到使方程（48）和（49）之间最佳匹配的值来确定。由于 $\scriptstyle { Z _ { v } }$ 的确切值 $\mathbf { \mathcal { Z } } _ { i }$ 在这里并不重要，仅它们的比值重要，且 $\textstyle z _ { i }$ 通常比 $\scriptstyle { Z _ { v } }$ 大几个百分点[20]，我们选择 $\boldsymbol { Z _ { v } } = \boldsymbol { 1 }$ 和 $Z _ { i } = 1 . 1$ 。通过基于最小二乘法的优化，我们发现 $S _ { v } = 1 . 5 3 \times 1 0 ^ { - 9 } \ s ^ { - 1 }$ 提供了最佳匹配，如图 6所示。由于两个模型对 R 的依赖性不同，整个生长过程中的完美匹配是不可能的，但在考虑的时间范围内，气泡半径非常接近。还进行了空隙生长的相场模拟，使用$S _ { v } = 1 . 5 3 \times 1 0 ^ { - 9 } \ s ^ { - 1 }$ ，模拟得到的气泡半径也显示在图 6 中。模拟的气泡半径与 SO 模型非常一致，表明这个 $ { \boldsymbol { S } } _ { v }$ 的值不足以在准稳态解析模型和相场模型之间造成显著差异，正如在第 4.1节中讨论的那样。如图所见。 6，SO 模型在物理上合理的模拟时间 $\mathbf { 2 \times 1 0 ^ { 7 } }$ 秒内与化学应力模型相当一致，适用于典型的轻水反应堆（LWR）运行条件下的 $\mathrm { U O } _ { 2 }$ 燃料。因此，SO 模型可以用 $S _ { v } = 1 . 5 3 \times 1 0 ^ { - 9 }$ 秒 来参数化，以表示完整空位-间隙模型更复杂的动力学。这个−1 $\pmb { S _ { v } }$ 值是典型轻水反应堆运行中 Xe 产生率的 15.9 倍[14]，因此位于之前参数研究[11]中考虑的 $S _ { v }$ 值范围内。这个“有效”的 $S _ { v }$ 值，代表 Frenkel对产生、复合和汇吸收的综合效应，远低于 Frenkel 对产生本身的预期值，其数量级为裂变率的 $1 0 ^ { 4 }$ 倍。

![](images/e97f81460d7483d1aea8fbfd41d5008b90ad4c3a15af6d9c9ff59041e7e60928.jpg)  
Download: Download high-res image (113KB)  
Fig. 6. Comparison of void growth rates using the chemical stress model and the SO model. $ { S _ { \nu } } = 1 . 5 3 \times 1 0 ^ { - 9 } \ : s ^ { - 1 }$ in the SO model provided the best match to the chemical stress model. A phase-field simulation of void growth using the same $S _ { \nu }$ value showed good agreement with the SO model prediction.  
图 6.使用化学应力模型和 SO模型比较空隙增长率。在 SO 模型中， $\mathsf { S } _ { \nu } = 1 . 5 3 \times 1 0 ^ { - 9 } \varsigma ^ { - 1 }$ 与化学应力模型最匹配。使用相同的 $\textsf { S } _ { \nu }$ 值进行的相场模拟空隙增长与 SO模型的预测有良好的一致性。

The strategy employed here, where $\pmb { S _ { v } }$ for the phase-field model is determined by finding the value that gives the best match between Equation (48) and (49), can be used as a general strategy to parameterize SO phase-field models of fission gas bubble growth. When performing a fit to determine $ { \boldsymbol { S } } _ { v } ,$ , should be chosen so that the initial porosity of the analytical SO model, $\pmb { p } = \pmb { R _ { 0 } ^ { 3 } } / \mathcal { R } ^ { 3 }$ , matches the initial porosity of the phase-field simulation initial conditions. Although the focus of this work has been on application to $\mathrm { U O } _ { 2 } ,$ , this methodology can be easily adapted to other fuels such as U-Zr or U-Mo. To do so, the appropriate values of $D _ { v } , Z _ { v } , Z _ { i }$ , and $c _ { v } ^ { s s }$ for the fuel to be simulated should be substituted in Equation (48). The fit to determine $\pmb { S _ { v } }$ in Equation (49) should be performed by starting from an initial bubble size that matches experimentally observed bubble sizes at low burnup, with the domain size $\mathcal { R }$ chosen so that the porosity of the simulation domain matches that of experiment as described above.

此处采用的策略是，通过寻找使方程（48）与方程（49）之间最佳匹配的值来确定相场模型中的 $S _ { v }$ ，这种策略可以作为参数化裂变气体气泡生长 SO 相场模型的一般方法。在拟合确定 $\pmb { S _ { v } }$ 时，应选择 $\mathcal { R }$ ，以便分析 SO 模型的初始孔隙率$\pmb { p } = \pmb { R _ { 0 } ^ { 3 } } / \mathcal { R } ^ { 3 }$ 与相场模拟初始条件的初始孔隙率相匹配。尽管本工作的重点在于应用于 $\mathrm { U O } _ { 2 }$ ，但这种方法可以很容易地调整应用于其他燃料，如 U-Zr 或 U-Mo。为此，应将模拟燃料的适当值 $D _ { v }$ $\boldsymbol { Z _ { v } }$ $\mathbf { \mathcal { Z } } _ { i }$ 和 $c _ { v } ^ { s s }$ 代入方程（48）。确定方程（49）中的 $ { \boldsymbol { S } } _ { v }$ 的拟合应从与低燃耗下实验观察到的气泡大小相匹配的初始气泡大小开始，并选择域大小 $\mathscr { R }$ ，以便模拟域的孔隙率与上述实验的孔隙率相匹配。

## 5.3. Impact of effective vacancy source term on 3D microstructural evolution

## 5.3. 有效空位源项对三维微结构演化的影响

To show the impact of the strategy developed in Section 5.2 on complex microstructural evolution, the growth of intergranular fission gas bubbles in a hexagonal grain structure in $\mathrm { U O } _ { 2 }$ was simulated with a previously developed phase-field model [11]. The previous simulations were performed using the SO approach, assuming that the effective vacancy source term $ { \boldsymbol { S } } _ { v }$ was 10 times larger than the Xe production rate $S _ { g }$ , or $S _ { v } = 1 0 S _ { g }$ . Based on the findings of Section 5.2, growth was simulated with an updated value of $S _ { v } = 1 5 . 9 S _ { g }$ . The initial conditions consisted of spherical intergranular bubbles with initial radius of 44 nm, randomly positioned on the hexagonal grain boundaries with areal density $2 0 / \mu \mathrm { m } ^ { 2 }$ . The simulation temperature was 1200 K and a fission rate of $\mathbf { 1 . 0 9 \times 1 0 ^ { 1 3 } }$ fi $\mathtt { s s i o n s } / ( \mathrm { c m } ^ { 3 } s )$ was used based on typical LWR operating conditions. Details of the model formulation, parameterization, and an image of the initial conditions are available in Ref. [11].

为展示第 5.2节中开发的策略对复杂微观结构演化的影响，使用之前开发的相场模型[11]模拟了在 $\mathrm { U O } _ { 2 }$ 六角晶粒结构中晶界间裂变气体气泡的生长。之前的模拟采用了 SO 方法，假设有效空位源项 $S _ { v }$ 是 Xe 产生速率 $S _ { g }$ 的 10 倍，或者$S _ { v } = 1 0 S _ { g }$ 。基于第 5.2节的发现，使用更新后的值 $S _ { v } = 1 5 . 9 S _ { g }$ 进行了生长模拟。初始条件包括在六角晶界上随机分布的球形晶界气泡，初始半径为 44 纳米，面密度为 $2 0 / \mu \mathrm { m } ^ { 2 }$ 。模拟温度为 1200 K，并根据典型的轻水反应堆运行条件，采用裂变率为 $\mathbf { 1 . 0 9 \times 1 0 ^ { 1 3 } }$ 裂 $ \ddagger / ( \mathrm { c m } ^ { 3 } s )$ 。模型的构建细节、参数化以及初始条件的图像可在参考文献[11]中找到。

The microstructures obtained using the previous and updated values of $\pmb { S _ { v } }$ are compared in Fig. 7 at time $\pmb { t = 1 0 ^ { 7 } \ s }$ Qualitatively, the features of the microstructure are quite similar, with the bubbles growing slightly more for the updated value of $S _ { v } = 1 5 . 9 S _ { g }$ shown in Fig. 7b. The volume fraction of the bubble phase, $V _ { f }$ , is initially 0.026 after equilibration of initial conditions. $\mathsf { A } \mathsf { t } \pmb { \mathrm { \Lambda } } \mathbf { = } \mathbf { 1 0 } ^ { \mathsf { 7 } }$ s, $V _ { f } = 0 . 0 3 1$ for the original value of $\begin{array} { r } { S _ { v } = 1 0 S _ { g } , } \end{array}$ , whereas $V _ { f } = 0 . 0 3 5$ at the same time for $S _ { v } = 1 5 . 9 S _ { g }$ . In addition to the increased overall growth rate, the larger value of $ { \boldsymbol { S } } _ { v }$ results in interconnection between bubbles occurring earlier. This can be seen by the comparing the circled regions in Figs. 7a and 7b. In Fig. 7b, connection between bubbles has already occurred in the upper red-circled regions, whereas these bubbles have not connected in Fig. 7a. In the lower green-circled region, the connection between bubbles is considerably thicker in 7b compared to 7a, indicative of earlier bubble interconnection. Because bubble interconnection along grain boundaries is one of the limiting steps for fission gas release [1], Fig. 7 shows the importance of parameterizing the vacancy source term correctly in fuel performance modeling.

使用先前和更新后的 $ { \boldsymbol { S } } _ { v }$ 值获得的微观结构在图 7中进行了比较，时间为 $\mathbf { t } = \mathbf { 1 0 } ^ { 7 }$ 秒。从定性的角度看，微观结构的特征非常相似，更新后的 $S _ { v } = 1 5 . 9 S _ { g }$ 值使得气泡在图 7b 中略有增大。气泡相的体积分数 $V _ { f }$ 在初始条件平衡后最初为$0 . 0 2 6 ^ { }$ 。在 ${ \bf { t } } = { \bf { 1 0 } } ^ { 7 }$ 秒时，原始的 $V _ { f } = 0 . 0 3 1$ 值为 $S _ { v } = 1 0 S _ { g }$ ，而同一时间 $V _ { f } = 0 . 0 3 5$ 的值为 $S _ { v } = 1 5 . 9 S _ { g }$ 。除了整体增长率增加外，更大的 $ { \boldsymbol { S } } _ { v }$ 值导致气泡之间的互联更早发生。这可以通过比较图 7a 和 7b 中圈出的区域来观察到。在图 7b中，气泡之间的连接已经在上方红色圈出的区域发生，而在图 7a中这些气泡尚未连接。在下方绿色圈出的区域，图 7b中的气泡连接比图 7a 要厚得多，表明气泡互联更早发生。因为沿晶界气泡互联是裂变气体释放的限制步骤之一[1]，图。 7显示了在燃料性能建模中正确参数化空位源项的重要性。

![](images/5023c91ecd525883a11bdd7463e7c0b5c04276f080b5b80b2b084fd1f8d61c48.jpg)  
$S _ { v } = 1 0 S _ { g }$

![](images/b39672b5b2e998e4b5b1cda47546db1708454d56aa82fde370f24a0a807fdd90.jpg)  
$S _ { v } = 1 5 . 9 S _ { g }$  
Download: Download high-res image (283KB) 下载：下载高清图片（283KB） Download: Download full-size image 下载：下载完整尺寸的图片  
Fig. 7. Simulation of intergranular fission gas bubble evolution in $\mathrm { U O } _ { 2 }$ using the SO approach [11]. Microstructure at $1 0 ^ { 7 }$ s using (a) the original estimated value of $S _ { \nu } { = } 1 0 S _ { g }$ from Ref. [11], (b) the updated value $S _ { \nu } { = } 1 5 . 9 S _ { g }$ based on Section 5.2. In (b), the bubble phase grows more rapidly, and bubble interconnection occurs earlier, as seen by comparing the circled regions between (a) and (b). (For interpretation of the colors in the figure(s), the reader is referred to the web version of this article.)  
图 7.使用 SO方法模拟 $\mathrm { U O } _ { 2 }$ 中晶间裂变气体气泡演化的过程[11]。在 $1 0 ^ { 7 }$ 秒时的微观结构，采用(a)来自文献[11]的原始估计值 $\textsf { S } _ { \nu } = 1 0 \mathsf { S } _ { g }$ ，(b)基于第 5.2 节的更新值 $\mathsf { S } _ { \nu } = 1 5 . 9 \mathsf { S } _ { g }$ 。在(b)中，气泡相生长更为迅速，气泡互联发生得更早，通过比较(a)和(b)中圈出的区域可以看出。 (图中颜色的解释，请读者参考本文的网络版。)

## 6. Conclusions6. 结论

In this work, the predictions of quasi-steady state analytical models were compared to phase-field simulations of void growth. These analytical models provide useful insight into how phase-field models that do not include interstitials can more effectively capture the full physics of vacancy-interstitial production, recombination, and sink absorption. The analytical models were shown to describe the behavior of phase-field models well, especially when the bubble growth rate is small. The initial growth rate of the SO model is significantly lower than that predicted by the analytical model, due to the fact that some time is required for the vacancy concentration to build up to its quasi-steady state value. In future work, this disagreement at early times could be alleviated by initializing the vacancy concentration field in the phase-field model based on the analytical solution (if appropriate for the

在此工作中，将准稳态分析模型的预测与空隙生长的相场模拟进行了比较。这些分析模型为理解不包含间隙原子的相场模型如何更有效地捕捉空位-间隙原子产生、复合和汇吸收的完整物理过程提供了有用的见解。分析模型被证明能够很好地描述相场模型的行为，特别是在气泡生长速率较小时。SO 模型的初始生长速率明显低于分析模型预测的值，这是因为需要一段时间使空位浓度积累到其准稳态值。在未来的工作中，可以通过基于分析解（如果适用于考虑的物理问题）初始化相场模型中的空位浓度场来减轻早期时间的不一致性。

The SS model produces growth rates much larger than the chemical stress model using physically motivated parameters for diffusivity, vacancy source, and effective sink terms. Surprisingly, the growth rate of bubbles was different for different choices of source and effective sink terms when these choices maintained the same value of steady-state vacancy concentration. Compared with the SO model, the growth rate of the SS model is a more complicated function of model parameters, and has less flexibility to parameterize to match predictions of the chemical stress model or other models of the full vacancy-interstitial driven kinetics.

SS 模型使用基于物理机制的扩散性、空位源和有效汇项参数，产生的增长率远大于化学应力模型。令人惊讶的是，当这些选择保持稳态空位浓度相同值时，气泡增长率对于不同的源和有效汇项选择是不同的。与 SO 模型相比，SS 模型的增长率是模型参数的更复杂函数，并且在参数化以匹配化学应力模型或其他完整空位-间隙驱动的动力学模型预测方面具有较少的灵活性。

The chemical stress model was compared to the SO model, and a least-squares optimization was used to parameterize the vacancy source strength in the SO model so that it best matched the growth kinetics of the chemical stress model. The growth rate in the SO model decreases more rapidly with radius than the chemical stress model, making it impossible to match the growth rate at all times. However, the bubble radius of the analytical SO model was reasonably close to that of the chemical stress model for physically realistic conditions and simulation times, and the phase-field model matched the analytical model well. This presents an effective strategy for parameterization of the vacancy-only SO model to realistically capture the more complex defect dynamics of vacancy-interstitial recombination and sink absorption, at reduced computational cost relative to including interstitials in phase-field models. This strategy enables large, multi-bubble simulations to be performed with greater quantitative accuracy, while maintaining the lower computational cost of the SO model. However, additional work is needed to further refine this strategy. The capture rates $\scriptstyle z _ { v }$ and $\mathbf { \delta } _ { Z _ { i } }$ to our knowledge have not been determined exactly for $\mathrm { U O } _ { 2 } ;$ to improve phase-field model parameterization, these parameters should be determined experimentally or calculated using atomistic simulation methods. Additionally, the chemical stress model itself relies on several approximations. In future work, the growth kinetics of the chemical stress model should be compared to a quantitative computational model of bubble growth that includes vacancies, interstitials, and production, recombination, and sink absorption processes, to further refine the strategy of parameterizing vacancy-only phase-field models.

化学应力模型与 SO 模型进行了比较，并采用最小二乘优化方法对 SO 模型中的空位源强度进行参数化，以使其最佳匹配化学应力模型的增长动力学。SO 模型中的增长率随半径的减小比化学应力模型更快，因此无法在所有时刻匹配增长率。然而，在物理现实条件和模拟时间内，解析 SO模型的气泡半径与化学应力模型的气泡半径相当接近，相场模型与解析模型匹配良好。这为仅空位的 SO 模型的参数化提供了一种有效策略，以在降低计算成本的同时，真实地捕捉空位-间隙复合和汇吸收的更复杂缺陷动力学。这种策略使得能够以更高的定量准确性执行大型多气泡模拟，同时保持 SO 模型的较低计算成本。然而，还需要进一步的工作来细化这种策略。 捕获率 $\scriptstyle { Z _ { v } }$ 和 $\mathbf { \mathcal { Z } } _ { i }$ ，据我们所知，尚未针对 $\mathrm { ~ U O ~ } _ { 2 }$ 进行精确确定；为了改进相场模型参数化，这些参数应通过实验确定或使用原子尺度模拟方法计算。此外，化学应力模型本身依赖于几个近似。在未来的工作中，化学应力模型的增长动力学应与包含空位、间隙原子以及产生、复合和汇吸收过程的气泡增长定量计算模型进行比较，以进一步优化仅空位相场模型的参数化策略。

CRediT authorship contribution statement

CRediT 作者贡献声明

Larry K. Aagesen: Writing – review & editing, Writing – original draft, Software, Methodology, Investigation, Conceptualization.

拉里·K·阿格森：撰写 -审稿与编辑，撰写 - 原始草稿，软件，方法论，调查研究，概念构思。

## Declaration of Competing Interest

利益冲突声明

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

作者声明，他们没有已知的竞争性财务利益或个人关系，这些可能影响到本文报告的工作。

## Acknowledgements致谢

This work was funded by the Department of Energy Nuclear Energy Advanced Modeling and Simulation program. This manuscript has been authored by Battelle Energy Alliance, LLC under Contract No. DE-AC07-05ID14517 with the US Department of Energy. The United States Government retains and the publisher, by accepting the article for publication, acknowledges that the United States Government retains a nonexclusive, paid-up, irrevocable, worldwide license to publish or reproduce the published form of this manuscript, or allow others to do so, for United States Government purposes.

此项工作得到了美国能源部核能先进建模与仿真计划的资助。本文由 Battelle 能源联盟有限责任公司根据与美国能源部签订的合同号 DE-AC07-05ID14517撰写。美国政府保留其非独占、已支付、不可撤销、全球范围的许可权，以出版或复制本文的已发表形式，或允许他人出于美国政府目的进行此类出版或复制，出版商通过接受本文发表，确认美国政府保留此权利。

Recommended articles

## Data availability数据可用性

Data will be made available on request.

数据将在请求后提供。

## References

[1] M. Tonks, D. Andersson, R. Devanathan, R. Dubourg, A. El-Azab, M. Freyss, F. Iglesias, K. Kulacsy, G. Pastore, S.R. Phillpot, M. Welland Unit mechanisms of fission gas release: current understanding and future needs J. Nucl. Mater., 504 (2018), pp. 300-317 View PDF View article View in Scopus Google Scholar

[2] T. Barani, G. Pastore, D. Pizzocri, D.A. Andersson, C. Matthews, A. Alfonsi, K.A. Gamble, P. Van Uff elen, L. Luzzi, J.D. Hales

Multiscale modeling of fission gas behavior in $\mathrm { U } _ { 3 } \mathrm { S i } _ { 2 }$ under LWR conditions J. Nucl. Mater., 522 (2019), pp. 97-110 View PDF View article View in Scopus Google Scholar

[3] C.L. Angerman, G.R. Caskey Swelling of uranium by mechanical cavitation J. Nucl. Mater., 13 (2) (1964), pp. 182-196 View PDF View article View in Scopus Google Scholar

[4] R.G. Pahl, D.L. Porter, C.E. Lahm, G.L. Hofman, Experimental studies of U-Pu-Zr fast-reactor fuel-pins in the Experimental Breeder Reactor-II, Metall. Mater. Trans., A, Phys. Metall. Mater. Sci. 21 (7), 1863–1869. Google Scholar

[5] G.L. Hofman, R.G. Pahl, C.E. Lahm, D.L. Porter Swelling behavior of U-Pu-Zr fuel Metall. Trans. A, Phys. Metall. Mater. Sci., 21 (3) (1990), pp. 517-528 View in Scopus Google Scholar

[6] S.Y. Hu, C.H. Henager, H.L. Heinisch, M. Stan, M.I. Baskes, S.M. Valone Phase-field modeling of gas bubbles and thermal conductivity evolution in nuclear fuels J. Nucl. Mater., 392 (2) (2009), pp. 292-300 View PDF View article Google Scholar

[7] P.C. Millett, A. El-Azab, D. Wolf Phase-field simulation of irradiated metals part II: gas bubble kinetics Comput. Mater. Sci., 50 (3) (2011), pp. 960-970 View PDF View article View in Scopus Google Scholar

[8] Y.L. Li, S.Y. Hu, R. Montgomery, F. Gao, X. Sun Phase-field simulations of intragranular fission gas bubble evolution in $\mathrm { U O } _ { 2 }$ under postirradiation thermal annealing Nucl. Instrum. Methods Phys. Res., Sect. B, Beam Interact. Mater. Atoms, 303 (2013), pp. 62-67 View PDF View article View in Scopus Google Scholar

[9] S.Y. Hu, D.E. Burkes, C.A. Lavender, D.J. Senor, W. Setyawan, Z.J. Xu Formation mechanism of gas bubble superlattice in UMo metal fuels: phase-field modeling investigation J. Nucl. Mater., 479 (2016), pp. 202-215 View PDF View article View in Scopus Google Scholar

[10] L.Y. Liang, Z.G. Mei, Y.S. Kim, M. Anitescu, A.M. Yacout Three-dimensional phase-field simulations of intragranular gas bubble evolution in irradiated U-Mo fuel Comput. Mater. Sci., 145 (2018), pp. 86-95 View PDF View article View in Scopus Google Scholar

[11] L.K. Aagesen, D. Schwen, M.R. Tonks, Y.F. Zhang

Phase-field modeling of fission gas bubble growth on grain boundaries and triple junctions in $\mathrm { U O } _ { 2 }$ nuclear fuel Comput. Mater. Sci., 161 (2019), pp. 35-45 View PDF View article View in Scopus Google Scholar

[12] Z.H. Xiao, Y.F. Wang, S.Y. Hu, Y.L. Li, S.Q. Shi A quantitative phase-field model of gas bubble evolution in $\mathrm { U O } _ { 2 }$ Comput. Mater. Sci., 184 (2020) Google Scholar

[13] L.K. Aagesen, D.A. Andersson, B.W. Beeler, M.W.D. Cooper, K.A. Gamble, Y. Miao, G. Pastore, M.R. Tonks Phase-field simulations of intergranular fission gas bubble behavior in $\mathrm { U } _ { 3 } \mathrm { S i } _ { 2 }$ nuclear fuel J. Nucl. Mater., 541 (2020), Article 152415 View PDF View article View in Scopus Google Scholar

[14] Larry K. Aagesen, Sudipta Biswas, Wen Jiang, David Andersson, Michael W.D. Cooper, Christopher Matthews Phase-field simulations of fission gas bubbles in high burnup $\mathrm { U O } _ { 2 }$ during steady-state and LOCA transient conditions J. Nucl. Mater., 557 (2021), Article 153267 View PDF View article View in Scopus Google Scholar

[15] A.A. Prudil, E.S. Thomas, M.J. Welland Network percolation using a two-species included phase model to predict fission gas accommodation and venting J. Nucl. Mater., 515 (2019), pp. 170-186 View PDF View article View in Scopus Google Scholar

[16] A.A. Prudil, M.J. Welland, N. Ofori-Opoku Modelling the growth and evolution of statistically significant populations of intergranular fission gas bubbles by IPM J. Nucl. Mater., 566 (2022) Google Scholar

[17] L.K. Aagesen, A. Casagranda, C. Matthews, B.W. Beeler, S. Novascone Phase-field simulations of fission gas bubble growth and interconnection in U-(Pu)-Zr nuclear fuel Mater. Theory, 6 (8) (2022) Google Scholar

[18] Y.B. Jiang, Y. Xin, W.B. Liu, Z.P. Sun, P. Chen, D. Sun, M.Y. Zhou, X. Liu, D. Yun Phase-field simulation of radiation-induced bubble evolution in recrystallized U-Mo alloy Nucl. Eng. Technol., 54 (1) (2022), pp. 226-233 View PDF View article View in Scopus Google Scholar

[19] Dong-Uk Kim, Sophie Blondel, David E. Bernholdt, Philip Roth, Fande Kong, David Andersson, Michael R. Tonks, Brian D. Wirth Modeling mesoscale fission gas behavior in $\mathrm { U O } _ { 2 }$ by directly coupling the phase field method to spatially resolved cluster dynamics

[20] D.R. Olander Fundamental aspects of nuclear reactor fuel elements Technical Information Center, Offi ce of Public Aff airs Energy Research and Development Administration (1976) Google Scholar

[21] C. Matthews, R. Perriot, M.W.D. Cooper, C.R. Stanek, D.A. Andersson Cluster dynamics simulation of xenon diffusion during irradiation in $\mathrm { U O } _ { 2 }$ J. Nucl. Mater., 540 (2020), Article 152326 View PDF View article View in Scopus Google Scholar

[22] M. Abramowitz, I.A. Stegun Handbook of Mathematical Functions with Formulas, Graphs, and Mathematical Tables (9th edition), Dover, New York (1972) Google Scholar

[23] S.G. Kim, W.T. Kim, T. Suzuki Phase-field model for binary alloys Phys. Rev. E, 60 (6) (1999), pp. 7186-7197 View in Scopus Google Scholar

[24] C. Matthews, R. Perriot, M.W.D. Cooper, C.R. Stanek, D.A. Andersson Cluster dynamics simulation of uranium self-diffusion during irradiation in $\mathrm { U O } _ { 2 }$ J. Nucl. Mater., 527 (2019), Article 151787 View PDF View article View in Scopus Google Scholar

[25] Cody J. Permann, Derek R. Gaston, David Andrš, Robert W. Carlsen, Fande Kong, Alexander D. Lindsay, Jason M. Miller, John W. Peterson, Andrew E. Slaughter, Roy H. Stogner, Richard C. Martineau MOOSE: enabling massively parallel multiphysics simulation SoftwareX, 11 (2020), Article 100430 View PDF View article View in Scopus Google Scholar

[26] J.D. Hales, K.A. Gamble, B.W. Spencer, S.R. Novascone, G. Pastore, W. Liu, D.S. Staff ord, R.L. Williamson, D.M. Perez, R.J. Gardner BISON users manual. Technical Report INL/MIS-13-30307, Rev. 3 Idaho National Laboratory (September 2015) Google Scholar

[27] R.J. White The development of grain-face porosity in irradiated oxide fuel J. Nucl. Mater., 325 (2004), pp. 61-77 View PDF View article Crossref View in Scopus Google Scholar

Cited by (0)

All content on this site: Copyright © 2024 Elsevier B.V., its licensors, and contributors. All rights are reserved, including those for text and data mining, AI training, and similar technologies. For all open access content, the Creative Commons licensing terms apply.