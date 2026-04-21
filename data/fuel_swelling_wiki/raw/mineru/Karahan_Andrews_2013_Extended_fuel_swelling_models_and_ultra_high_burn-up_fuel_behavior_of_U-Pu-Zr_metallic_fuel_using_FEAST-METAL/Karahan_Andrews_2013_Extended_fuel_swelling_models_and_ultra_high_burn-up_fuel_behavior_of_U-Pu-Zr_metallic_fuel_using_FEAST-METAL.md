# 📄 PDF Parsing Result

**File:** `/Volumes/openclaw记忆/Zotero_storage/storage/DPC49EIJ/Karahan, Andrews_2013_Extended fuel swelling models and ultra high burn-up fuel behavior of U-Pu-Zr metallic fuel using FEAST-METAL.pdf`
**Backend:** `pipeline`
**Pages:** 0 to end
**Formula Recognition:** ❌ Disabled
**Table Recognition:** ✅ Enabled

---

# Extended fuel swelling models and ultra high burn-up fuel behavior of U–Pu–Zr metallic fuel using FEAST-METAL

Aydın Karahan∗, Nathan C. Andrews

Center for Advanced Nuclear Energy Systems, Nuclear Science and Engineering, Massachusetts Institute of Technology, 77 Massachusetts Avenue, 24-215, Cambridge, MA 02139, United States

## HIGHLIGHTS

\- Improved fuel swelling models in phase structure dependent form.

\- A probabilistic verification exercise for the open porosity formation threshold.

\- Satisfactory validation effort for available EBR-II database.

\- Ultra high burn-up behavior of U–6Zr fuel with 60% smear density fuel.

## ARTICLEINFO

Article history:   
Received 21 June 2011   
Received in revised form 15 January 2013   
Accepted 1 February 2013

## ABSTRACT

Computational models in FEAST-METAL U–Pu–Zr metallic fuel behavior code have been upgraded to improve fission gas, solid fission product swelling, and pore sintering behavior in a microstructure dependent form. First, fission gas bubble growth is modeled by selecting small and large bubble groups according to a fixed number of gas atoms per bubble group. Small bubbles nucleated at phase boundaries grow via gas migration and turn into large bubbles. Furthermore, bubble morphology for each phase structure is captured by selecting the number of atoms per bubble and the shape of the bubbles in a phase dependent form. The gas diffusion coefficients for the single gamma phase and effective dual (˛ + ı) and (ˇ + -) phase structures are modeled separately, using the activation energy of the corresponding phase structure. In this study, it is found that pressure sintering of the interconnected porosity in dual phases should be less effective than the reference model in order to match clad strain and fission gas release behavior. In addition to these improvements, a probabilistic approach is taken to verify the fission gasswelling threshold at which interconnected porosity begins. This fracture problem is treated as a function of critical crack length formed via bubble coalescence. It was found that a 10% gas-swelling threshold is appropriate for a wide range of gas bubble sizes. The new version of FEAST-METAL predicts the burn-up, smear density, and axial variation of the clad hoop strain and fission gas release behavior satisfactorily for selected test pins under EBR-II conditions. The code is used to predict ultra-high burn-up U–Pu–6Zr vented metallic fuel behavior with HT9 cladding for fast breeder reactor applications for 20 years of irradiation. It is assumed that HT9 clad will retain its fracture toughness and creep properties for this simulation. It appears that the increased dose on the cladding, increased solid fission product swelling, and low operating fuel temperature requires lower fuel smear density (∼60%) in order to ensure acceptable clad hoop strain at high burn-up (∼35 at.%). Furthermore, keeping the peak clad temperature below 550 ◦C seems to control lanthanide migration and clad inner wastage at a reasonable level. Possible design concerns and improvements are discussed.

© 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

Uranium–plutonium alloy fuel type with 6–10 wt.% zirconium irradiated in EBR-II and FFTF reactors showed that it is a promising candidate for fast reactor applications (Walters, 1999; Crawford et al., 2007). It has high heavy metal density, high thermal conductivity, ease of fabrication and good compatibility with sodium coolant. It also has rather controllable fuel swelling and fuel clad mechanical interaction behavior. On the other hand, one should also guard against fuel clad chemical interaction due to lanthanide attack towards the clad inner surface. Today, this fuel type is suggested for use in the fast breeder (Weaver et al., 2009) and fast burner (Hoffman et al., 2006) reactor designs. Enabling ultra-high burn-up capability and the resulting self-sustained fuel cycle with no enrichment or reprocessing requirement presents itself as an interesting target. This can also help resolve the rapidly growing energy problem without raising security concerns due to fuel enrichment or reprocessing issues.

Because the available database is rather limited, extrapolating available databases accurately with science-based, semi-empirical and continuum level models is the key to designing the future nuclear systems. FEAST-METAL is a U–Pu–Zr fuel behavior code developed to predict steady state and transient performance of metallic fuels (Karahan, 2009). The code has 1D stress/strain and temperature distribution models. It is also equipped with mechanistic models for fission gas swelling and release, fuel constituent migration, fuel clad chemical interaction and transient clad failure predictions. Furthermore, empirical models are included to describe fuel creep and thermal expansion, sintering behavior of fuel porosity under applied stress, fuel thermal conductivity, sodium logging into fuel porosity, HT9 clad irradiation and thermal creep, void swelling, and thermal expansion.

The code’s fission gas behavior model is based on the GRSIS algorithm (Lee et al., 2001). It assumes bubbles can nucleate isotropically within the fuel matrix. The fact that the fuel operates above the half of the melting point and has phase boundaries, which are nearly uniformly distributed within the grains, makes the isotropic nucleation assumption acceptable. The first version of the code allows for bubble grouping based on the volume of the bubble. Two groups of bubbles are allowed. Once nucleated, small bubbles grow via mainly gas diffusion towards bubbles and turn into large bubbles. Above the threshold gas swelling, formation of interconnected open porosity takes place. Interaction of the open pores with closed bubbles leads to a rapid build-up of interconnected porosity and fission gas release. Fission gas can escape to the plenum via the interconnection of a closed bubble with open porosity or direct diffusion towards open porosity. Once fission gas swelling saturates, solid fission product swelling lets the fuel continue expanding. Typically, pressure sintering of the open porosity under the applied contact pressure between the fuel and the cladding allows for solid fission products to build up without significantly straining the cladding.

The current study changes the bubble grouping scheme in the GRSIS algorithm from constant volume to constant atom number. Hence, small and large bubble groups have specific number of atoms. This approach has found more applications in modeling fission gas behavior in past studies (Tsuboi et al., 1992; Wood and Hayns, 1976). In addition to the bubble grouping scheme, the morphological evolution of fission gas bubbles is modeled in phase dependent form consistent with experimental observations given in Fig. 1 (Hofman et al., 1990). Fig. 1(a) is the typical bubble morphology at dual (˛ + -) phase, which typically occurs at the colder peripheral regions. Due to lack of thermal activation and inclusion of stiff orthorhombic ˛ phase, the bubbles grow along the ˛/ı phase boundaries and take an ellipsoidal shape. Fig. 1(b) shows the bubble morphology of dual (ˇ + ) phase region. Again due to existence of stiff tetragonal ˇ precipitates, bubbles remain small, on the order of a couple of microns, but this time the bubble shape is spherical. At higher temperatures, the body centered cubic (BCC) single gamma phase forms. Its softness favors existence of much larger bubble sizes compared to dual phase regions. The size of large spherical bubbles could be as much as 10 m (Fig. 1(c)). In order to capture this behavior, the new version of FEAST-METAL specifies the number of atoms per small and large bubbles in phase dependent form for each radial node based on its temperature. Furthermore, the gas diffusion coefficient is also modeled in phase dependent form considering the activation energy of each phase structure.

In addition to fission gas behavior, the sintering model for interconnected open porosity is also updated in the current version. The previous porosity sintering model was a fit using the experimental data generated for high temperature single gamma phase (Ogata and Yokoo, 1999). This study has found that the compressibility factor of dual phases should be much lower in order to match fission gas release and clad strain behavior in a satisfactory manner. In addition to modeling improvements, a verification study has also been performed for the threshold gas swelling parameter to predict the onset of open porosity formation. The benchmarking effort against selected tests from EBR-II database is described in Section 4. In Section 5, the code is applied to predict ultra-high burn-up metallic fuel behavior for sodium fast reactor conditions. For this case, it is assumed that HT-9 clad will retain its fracture toughness, creep and void swelling properties up to 500 dpa. The results are discussed and possible design improvements are suggested.

## 2. Model improvements

## 2.1. Fission gas model

Several improvements have been made on fission gas module. First, a constant atom number bubble grouping scheme is adopted. In this approach, gas bubbles are treated as two distinct groups as the small and large bubble while each group has a fixed number of gas atoms. Small bubbles nucleated isotropically grow via gas diffusion towards this bubble type. As a result of this growth, a fraction of them turn into large bubbles in each time step. Given the hydrostatic stress and temperature, the radius of the each bubble group is calculated using Van der Walls equation. The selected number of atoms for small bubbles and large bubbles are given in Table 1 for each phase structure. By this way, the model approximates the observed behavior for bubble morphological evolution given in Fig. 1.

The fission gas algorithm accepts only spherical geometry. In order to account for ellipsoid shape of bubbles in (˛ + ı) region, correction factors are added for surface energy term in Van der Walls equation and also for bubble surface area term in order to capture the correct gas diffusion current towards ellipsoidal bubbles. Bubble growth and coalescence models are treated by using an effective spherical geometry for ellipsoid bubbles.

The fission gas diffusion coefficient is modeled in phase structure dependent form. Measured activation energy of the corresponding phase structure is adopted as given in Gruber and Kramer (1987). Diffusion constants are taken as fitting factors. The constitutive relations for dual phase and single gamma phase regions are given as follows:

![](images/c4f1a683f8d55d973cd759702914c99e81313398f0338ac5d999dc62f556c47b.jpg)

Dg: gas diffusion coefficient (m2/s); T: temperature (K); R: gas constant = 1.987 Cal/mol/K; T6: single gamma phase transition temperature (K) (the value is 923 K for U–19Pu–10Zr fuel).

Note that sensitivity of the dual phase diffusion coefficient on overall behavior is much higher compared to the single gamma phase diffusion coefficient. A part of the reason is that the single gamma phase is compliant and the stiffer outer region tends to have a higher impact on fission gas release and swelling behavior of the fuel.

In addition to the fission gas diffusion constant, the open pore formation coefficient and open porosity surface area corrections are the remaining fitting factors in the fission gas model as defined in Karahan (2009). The open porosity formation coefficient controls the distance between the closed bubbles and interconnected open porosity; hence, the coalescence behavior of the closed bubbles with the open porosity while closed bubbles are growing via diffusion. Its value is taken as 0.4. The open porosity surface area correction factor controls the area of the open pores at which direct gas diffusion and release can take place. Its value is taken as 0.3. Both of these factors are adjusted in order to predict EBR-II experiments in a satisfactory manner.

![](images/28406baca049b2fe507edce958a1650b7a5d237adf3806e3e86c724e42f2d0f5.jpg)  
Fig. 1. Bubble morphology at (a) (˛ + ı) phase, (b) (ˇ + -) phase, (c) Single - phase (Hofman et al., 1990) (each figure spans approximately 4000 m2).

## 2.2. Pressure sintering model

Under the applied hydrostatic stress, open porosity, which is at plenum pressure, is assumed to be sintered in creep dependent form. Using the experimental data for hot isostatic pressing (McDeavitt, 1992) at high temperature single gamma phase, Ogata et al., derived an empirical model for pore compression in creep dependent form (Ogata and Yokoo, 1999). In their model, a compressibility factor (˛) is defined as a function of the open porosity fraction present within the fuel. This factor plays an essential role to assess fuel clad mechanical interaction behavior and predict the amount of porosity the fuel has at a given time. In this study, the model is extended to a phase dependent form and a correction factor “C” is added for dual phases as given below:

![](images/a595a537cf7d5d863ea9d6bb5e59ad706b77fba04db27e1c5fa945a33889964f.jpg)

˛: open porosity compressibility factor; εopn: fuel open porosity fraction; C: fitting factor. It is taken as unity for single gamma phase and 0.23 for (˛ + ı) and (ˇ + -) dual phases.

Note again that experimental data is not available for hot pressing behavior of the dual phases. The study raises the possibility of the extrapolation performed by Ogata and Yokoo (1999)

overestimating the compressibility factor for dual and stiffer phase structures. Experimental work should be pursued to clarify this issue. Nevertheless, decreasing the “C” factor for dual phases improves coupled fuel behavior predictions significantly.

## 2.3. Solid fission product swelling

As mentioned before, solid fission product swelling together with hot pressing of the open porosity is very critical in capturing the fuel clad mechanical interaction behavior. The previous version of FEAST-METAL assumed conservatively that the U–Pu–10Zr solid fission product swelling rate is 1.5% per at.% burn-up (Ogata and Yokoo, 1999; Kim and Hofman, 2003). The current study adopts 1.2% per at.% burn-up which is the best estimate value as given by Hofman et al. (1997). As a result, we believe the extrapolation ability of the code especially for high burn-up and high residence time conditions has increased. Note also that if the heavy metal density (or zirconium content) is different than the reference fuel, the swelling rate is corrected proportional to the heavy metal density of the fuel with respect to the reference fuel.

## 3. Verification of the threshold swelling

FEAST-METAL assumes that above the gas swelling threshold of 10%, formation of the interconnected open porosity begins; in other words, fuel fracture takes place. It is based on previous experimental work, which was performed at high temperature conditions for single gamma phase region (McDeavitt, 1992). In this study, possible dependency of this parameter on bubble size is examined with a probabilistic approach. The aim is to correlate the threshold swelling with the critical crack length due to interconnection of the bubble chains. First, the experimental work given in McDeavitt and Solomon (1996) is simulated and crack length distribution is calculated. Then, it is applied for a wide range of bubble sizes.

The model tracks the interconnected bubbles up to the point at which the scalar product of the crack vector between the starting bubble pair and the last bubble pair becomes less than zero. As can be seen in Fig. 2, the crack follows bubbles-1–4, and 6. The chain starting with bubble-1 and ending at bubble-5 is not taken into consideration because the vector between bubble 4 and bubble-5 changes its direction with respect to the vector between the bubble-1 and bubble-2.

Table 1  
Small and large bubble size and number of atoms per bubble.
<table><tr><td>Phase structure</td><td>Small bubble atom number</td><td>Small bubble size/shape</td><td>Large bubble atom number</td><td>Large bubble size/shape</td></tr><tr><td>(a+8）</td><td>0.37E+7</td><td>~0.2 μm × 0.2 μm × 0.05 μm Ellipsoidal</td><td>0.98E+10</td><td>~7μm×7μm×1μm Ellipsoidal</td></tr><tr><td>(β+2)</td><td>0.20E+7</td><td>~0.15 μm Spherical</td><td>0.54E+10</td><td>~3 μm Spherical</td></tr><tr><td>Singley</td><td>0.75E+8</td><td>~0.5 μm Spherical</td><td>0.2E+12</td><td>~10μm Spherical</td></tr></table>

![](images/6d1a1dbc3e3254b196718ebd8a72134383f76cd69a8327c2db2fc8eb56e13a59.jpg)  
Fig. 2. Interconnected bubble chain (crack length).

![](images/a82efd9f35e1fad0560c2cb67fcff58e1d0f7e1bf0714d7ca7846a4422920695.jpg)  
Fig. 3. Bubble separation strategy.

Given the cumulative distribution function for the bubble size distribution, the code generates bubbles randomly within a 200 × 200 × 200 m cube media with an applied periodic boundary condition at boundaries. After that, the code assesses interconnected bubbles. The bubbles are separated from each other so that they will be just touching each other as shown in Fig. 3. The code records all connected bubble pairs. By tracking bubble pairs and calculating the cosine in between, crack length density due to bubble coalescence is obtained. At the final step, the code rejects the cracks that occupy any smaller size cracks.

The probability distribution function (PDF) given in McDeavitt and Solomon (1996) for bubble size is shown in Fig. 4. The average bubble diameter is 2.7 m. Bubbles are generated using this probability distribution function up to 10% swelling. The resulting crack length density distribution (m/m3) is given in Fig. 5. The selected criterion for critical crack length density at which fuel fracture takes place is taken as 1.5E+13 m/m3 and above 30 m.

By shifting the PDF to left and right (Fig. 6), the sensitivity of the threshold swelling on bubble size is studied. Fig. 6 shows the shifted PDF for 1.5 m and 6 m average bubble diameter.

The critical crack density is calculated for different bubble sizes. As shown in Fig. 7, it was found that the threshold swelling, at which critical crack-length density is reached, remains around 10%. One may assume that an average bubble diameter in the neighborhood of 2 m corresponds to the dual phase region and a diameter of 4–6 m corresponds to the single gamma phase region. At very low bubble sizes, an increase in threshold swelling above 10% is observed. This may be due to the modeling assumption described in Fig. 2. Nevertheless, the calculation indicates that within the region of interest, 10% threshold swelling for the onset of interconnected porosity formation is a reasonable assumption. Accordingly, it is kept the same in the new version of FEAST-METAL.

![](images/b56208493e12bd062384438ab17227a15650196d1c538ee361d1789322fe034b.jpg)  
Fig. 4. Probability distribution function for bubble diameter for experimental work given in McDeavitt and Solomon (1996).

![](images/bd647d02089274b44ad51038714821d77865e49135b84e98abf53479d2a62585.jpg)  
Fig. 5. Crack length density distribution for the reference simulation at 10% gas swelling.

![](images/14bfd359c16fbade2fdfa1feb6d83cc9ff7b17bb20b01c0034eeec624f54d5f5.jpg)  
Fig. 6. Probability distribution function for average bubble diameter of 1.5 and 6 m.

## 4. Benchmarks

Benchmarking is accomplished using experimental data for X425 and X430 assemblies operated in EBR-II as described in

![](images/4258c571034c7d1d9bcc1e9ca183fb7bc0cecbd1600719d62e8c22e3ca72c544.jpg)  
Fig. 7. Calculated threshold swelling as a function of average bubble size.

![](images/28f8a625eac9f6f8ef01becd06e16b6f2523746a42e234a89e5f3aa1869ae605.jpg)

![](images/dd4babc8f7f9e3aca0f544b5b1c1c3e51edefd5b24f31d098e61b12687c470b2.jpg)  
Fig. 8. (a) Axial variation of the X425 fuel pin centerline temperature at low burn-up and at end of life; (b) axial variation of the X430 fuel pin centerline temperature at low burn-up and at end of life.

![](images/c60c94f7af814f77f604c2296ca28b459d87dc8ed600d01aa7c46c3d24cde207.jpg)

![](images/0d9af2c587506ed52fda7119241a70532bce3074153782cae583f04c94f646d8.jpg)  
Fig. 9. (a) X425 fuel swelling behavior at peak clad strain location, and (b) X430 fuel swelling behavior at peak clad strain location.

![](images/58945c731ec2c6669cff604666d64974ae763831db61d32a8e8661027ac10f74.jpg)

![](images/5217a85d9d736f5e1e8ac5ed33b195b8c2356e5b57894a5bb6d966ddd140f3b8.jpg)  
Fig. 10. (a) X425 fuel pin axial variation of contact pressure, and (b) X430 fuel pin axial variation of contact pressure.

Karahan (2009). Main target is to predict the fission gas release, clad hoop strain, and fuel axial elongation behavior. Geometry, materials and main operating conditions for X425 and X430 assemblies are given in Table 2. The detailed operating history used in these simulations can be found in Karahan (2009). The main differences between the X425 and X430 assemblies are fuel smear density, size of the fuel slug, linear heat rate and peak burn-up. X425 was one of the most successful fuel assemblies, reaching 18.9 at % peak burnup with no failure. X430 has higher smear density, which limits the achievable burn-up due to earlier start of fuel clad mechanical interaction and clad straining.

X425 and X430 fuel specifications.
<table><tr><td>Assembly no.</td><td>X425</td><td>X430</td></tr><tr><td>Fuel composition</td><td>U-19Pu-10Zr</td><td>U-19Pu-10Zr</td></tr><tr><td>Clad material</td><td>HT9</td><td>HT9</td></tr><tr><td>Fuel slug density(g/cm³)</td><td>15.8</td><td>15.8</td></tr><tr><td>Fuel slug radius (mm)</td><td>2.16</td><td>2.86</td></tr><tr><td>Clad inner radius (mm)</td><td>2.54</td><td>3.28</td></tr><tr><td>Clad outer radius (mm)</td><td>2.92</td><td>3.68</td></tr><tr><td>Fuel smear density (%)</td><td>72.3</td><td>76</td></tr><tr><td>Fuel active length (cm)</td><td>34.3</td><td>34.3</td></tr><tr><td>Axial peaking factor</td><td>1.12</td><td>1.12</td></tr><tr><td>Plenum to fuel ratio</td><td>1.0</td><td>1.4</td></tr><tr><td>Peak linear heat rate (kW/m)</td><td>40</td><td>50</td></tr><tr><td>Coolant inlet temperature (C)</td><td>370</td><td>370</td></tr><tr><td>Peak clad temperature (C)</td><td>590</td><td>590</td></tr><tr><td>Peak fast flux(n/cm²/s)</td><td>2.3×1015</td><td>1.6×1015</td></tr><tr><td>Peak burn-up (at.%)</td><td>18.9</td><td>11.6</td></tr><tr><td>Peak dose at end of life (dpa)</td><td>~95</td><td>~60</td></tr></table>

Axial variation in fuel centerline temperature at early irradiation and at end of life is given in Fig. 8. Due to its higher linear heat rate, X430 fuel pin has higher fuel centerline temperature (Fig. 8(b)) compared to X425 (Fig. 8(a)). Towards the end of life, fuel temperature drops due to somewhat lower linear heat rate, lower coolant exit temperature, and lower fuel porosity. Fig. 9 shows the fuel swelling behavior of X425 and X430 at peak clad strain axial location (40% from bottom). During the first few atom percent of burn-up, fission gas swelling and formation of interconnected porosity takes place. With the start of hard contact between the fuel and cladding, open porosity decreases in order to accommodate solid fission product swelling.

Fig. 10(a) and (b) shows the axial variation of contact pressure for X425 and X430, respectively. The constitutive models for the fuel dimensional changes, such as fuel and clad swelling, creep and thermal expansion, play a major role in the contact pressure calculation. The range of validity of the contact pressure calculation is dependent on the accuracy of the constitutive models. The computed contact pressure at a time step assures that the fuel and clad displacement rates are identical. This strategy is consistent with previous approaches such as Ogata and Yokoo (1999). The contact pressure increases with burn-up mainly due to increased plenum pressure and lower fuel temperature towards end of life. Since the interconnected porosity remains at the plenum pressure, the contact pressure required to compress the porosity needs to be higher than the plenum pressure. It is much higher at the lower axial sections due to low operating temperature (less compliant fuel). If the open porosity drops below 10%, the fuel may become much stiffer. However, Fig. 9 shows the open porosity is above 10% during the operation.

![](images/8d1bbf1f77f9f0305173f0bcedfa6de7277d01e839f47717108af6612142f8d9.jpg)  
Fig. 11. Peak clad hoop strain burn-up variation for X425 and X430.

Fig. 11 shows the burn-up variation of clad strain and comparison with the experimental data at the middle and end of life for X425 and X430 fuels. The clad strain is mainly due to irradiation creep. The match is satisfactory. Fig. 12 shows the axial variation of the clad hoop strain for X425 fuel. FEAST is able to predict the axial anisotropy in clad hoop strain variation. Due to lower temperature at bottom axial part, the clad strain tends to be higher in this region. On the other hand, at the upper axial regions, the fuel is rather compliant. FEAST predictions for clad strain at 15.8 at.% appear to be at the conservative side for the upper axial regions. This may be due to (1) overestimation of the contact pressure, or (2) uncertainties associated with irradiation creep constitutive model.

Fission gas release behavior for X425 and X430 is given in Fig. 13. The match with experimental data at end of life is satisfactory. Furthermore, onset of fission gas release and its increase and saturation in early irradiation matches with the generic data given in Pahl et al. (1992), very well.

![](images/60b59fe9ee8a51c6d6987e32c4f50738adee452917c80954e5d8d4985f5ca581.jpg)  
Fig. 12. Clad hoop strain axial variation at 15.8 at.% and 18.9 at.% peak burn-up for X425 fuel.

![](images/92ede8deb27d91044dc457099ce6b0c891798c11a5f53828c78b1aec559302b1.jpg)  
Fig. 13. Fission gas release predictions for X425 and X430 fuels.

The final benchmark set is against the fuel axial elongation tests. Anisotropic fuel slug elongation occurs due to (1) axial variation of fuel temperature and burn-up, (2) fuel cracking, and (3) grain boundary tearing. FEAST models anisotropic fuel axial deformation as a function of plutonium content of the fuel and average linear heat rate to fuel slug diameter ratio using an anisotropy factor which acts as a flag to determine the onset of axial contact between fuel slug and clad. Once the specified fraction of the initial gap is filled by swollen fuel slug, the axial interaction takes place.

![](images/d98d72085c7b57f924d8dd377e1c5fac14bbdf72c67bd2c91c2d18628746257f.jpg)

drgap: gap thickness at which fuel-clad axial contact takes place; drgap0: initial gap between the fuel and clad; f: anisotropy factor calculated as a function of plutonium content and linear heat rate to fuel slug diameter ratio

Table 3 shows that it is possible to predict the experimental data given in (Hofman et al., 1990; Pahl et al., 1990; Crawford et al., 1994), satisfactorily.

## 5. Ultra high burn-up metallic fuel behavior

Increasing the achievable burn-up of fast breeder reactor fuels is the key target for improving fuel utilization, minimizing nuclear waste and reducing enrichment requirements. Attainment of very high burn-ups, beyond 30–35 at.%, requires cladding materials that can preserve their high creep fracture and void swelling resistance up to very high doses, e.g. 500 dpa. In addition, one should guard against lanthanide attack towards clad inner surface and clad hoop strain due to fuel clad mechanical interaction (irradiation creep) and void swelling of the cladding. The current study assumes HT9 cladding preserves its void swelling rate, fracture toughness and irradiation creep properties up to 500 dpa and examines the effect of fuel swelling on clad hoop strain and fuel clad chemical interaction behavior of the fuel for ultra-high burn-up and long residence time conditions.

The sample fuel specifications are given in Table 4. U–6Zr is the initial fuel composition. 6 wt.% Zirconium is selected due to irradiation data of 6 wt.% fuel pins that showed similar behavior as 10 wt.% Zr fuel. The selected fuel smear density is 60%. This value is much lower than typical EBR-II fuel, which is 75%, in order to provide more space for more solid fission product swelling and delay onset of fuel clad mechanical interaction. The plenum region is vented, hence, no pressure build-up is allowed. As a result, a high thermal creep fracture margin during transients is satisfied. Furthermore, design of a very large plenum region could be challenging to satisfy the core pressure drop constraint. The core axial height, the operating history of the fuel pin and the plutonium build-up has similar values to previous work on breed and burn reactor performed by Yarsky (2005). Axial peaking factor is 1.4 and its variation is given in

Table 3  
Fuel axial elongation benchmarks (Hofman et al., 1990; Pahl et al., 1990; Crawford et al., 1994).
<table><tr><td rowspan="2">Fuel composition</td><td rowspan="2">Fuel smear density (%)</td><td rowspan="2">q&#x27;/D (W/cm²)</td><td colspan="3">Axial elongation (%)</td></tr><tr><td>Experimental data</td><td>Error band</td><td>FEAST-METAL</td></tr><tr><td>U-10Zr</td><td>76</td><td>790</td><td>6.2</td><td>±1.2</td><td>7.1</td></tr><tr><td>U-19Pu-10Zr</td><td>76</td><td></td><td>1.5</td><td>±.7</td><td>1.8</td></tr><tr><td>U-10Zr</td><td>72</td><td>830</td><td>8.5</td><td>±1.2</td><td>7.8</td></tr><tr><td>U-8Pu-10Zr</td><td>72</td><td></td><td>6.5</td><td>±.6</td><td>6.7</td></tr><tr><td>U-19Pu-10Zr</td><td>72</td><td></td><td>2.5</td><td>±.8</td><td>2.1</td></tr><tr><td>U-10Zr</td><td>75</td><td>650</td><td>8.0</td><td>*</td><td>8.0</td></tr><tr><td>U-8Pu-10Zr</td><td>75</td><td></td><td>5.8</td><td>* *</td><td>5.8</td></tr><tr><td>U-19Pu-10Zr</td><td>75</td><td></td><td>6.5</td><td></td><td>7.1</td></tr></table>

Ultra-high burn-up sample fuel specifications.
<table><tr><td>Parameter</td><td>Value</td></tr><tr><td>Fuel composition (wt.%)</td><td>U-6Zr</td></tr><tr><td>Clad material</td><td>HT9</td></tr><tr><td>Fuel slug density (g/cm²)</td><td>17</td></tr><tr><td>Fuel slug radius (mm)</td><td>3.0</td></tr><tr><td>Clad inner radius (mm)</td><td>3.87</td></tr><tr><td>Clad outer radius (mm)</td><td>4.50</td></tr><tr><td>Fuel smear density (%)</td><td>60.0</td></tr><tr><td>Fuel active length (cm)</td><td>200</td></tr><tr><td>Plenum volume</td><td>Vented</td></tr><tr><td>Axial peaking factor</td><td>1.4</td></tr><tr><td>Peak linear heat rate (kW/m)</td><td>50</td></tr><tr><td>Peak clad temperature (C)</td><td>550</td></tr><tr><td>Peak fast flux (n/cm²/s)</td><td>4.5×1015</td></tr><tr><td>Peak burn-up (at.%)</td><td>36</td></tr><tr><td>Peak dose at end of life (dpa)</td><td>~500</td></tr></table>

![](images/c6d1e4f5dd5bd65498230a14c22b1e4f1d238ab8b2dece38d7e6e6158cb8b9a4.jpg)  
Fig. 14. Axial variation of the normalized power of ultra-high burn-up fuel.

Fig. 14. The first 10 years, the fuel operates at low power at passive region and produces plutonium (Fig. 15). Once it is shuffled into the active region, power level increases by an order of magnitude. The fuel is allowed to spend five years in the active fuel region. The last five years, high burn-up fuel is operated at an intermediate power level, consistent with Yarsky (2005). The peak plutonium content is 10 wt.%, which is bred during low power operation in the first phase.

![](images/2646047facafa650c8b3c75b7c7fc25008071c800f73aaf8a7418d4ab1183894.jpg)  
Fig. 15. Time variation of peak linear heat rate of ultra-high burn-up fuel.

![](images/ddc5dc9d5958d70695a84072fb3fcd65a9f58f0faf288e48dc171041ee661042.jpg)  
Fig. 16. Axial variation of fuel centerline temperature of ultra-high burn-up fuel.

Fig. 16 shows the fuel centerline temperature axial variation at beginning of life, middle of life (18.5 at.% peak burn-up) and end of life. At beginning of life, fuel temperature follows the coolant temperature due to low linear heat rate. At high power region, the peak fuel temperature reaches 735 ◦C due to its high linear heat rate and high fuel porosity. Towards end of life, both linear heat rate and fuel porosity comes down and near 100 ◦C drop in fuel centerline temperature occurs. Fuel swelling behavior at peak clad strain location is given in Fig. 17. Above 10% gas swelling, open porosity starts to form and fission gas release starts (Fig. 17). At 12 at.% peak burnup, 50% of the fuel consists of the interconnected porosity. With the start of hard contact between the fuel and clad, solid fission product swelling is balanced by hot pressing of the open porosity under the applied contact pressure. Towards the end of life, reduction of the fuel temperature makes the fuel much stiffer. In order to accommodate the solid fission product swelling, clad hoop strain rate increases significantly as shown in Fig. 18. The total predicted peak clad hoop strain is 3% at the end of life. 1% of this is predicted to be void swelling and the rest of it is due to the irradiation creep. Fuel clad mechanical interaction at the bottom of the fuel shown in Fig. 18(a) is much higher due to lower fuel temperature.

![](images/d99539133648ea28f386a6491699d8338d360774caf24a5969435d6bbf9f5c2d.jpg)  
Fig. 17. Fuel swelling behavior of ultra-high burn-up fuel.

![](images/127d5364648653599745af19c33fcda7de4c19c90dfd3e25472511675b0f503c.jpg)

![](images/a146ecae60b58c252a6dcac703d22df4fd521850d3233d5d381849c379c8ff24.jpg)  
Fig. 18. (a) Axial variation of contact pressure of ultra-high burn-up fuel, and (b) axial variation of clad hoop strain of ultra-high burn-up fuel.

![](images/bfe1b473a2e145ea01da03445a4720fb7d8881cac9f93877176ae74fa09eec5d.jpg)

![](images/261d563a2286f9b5f01636ce6145b32ee860a9fc3e4e5c15bc61dd9cc61aa9a3.jpg)  
Fig. 19. (a) Fission gas release of ultra-high burn-up fuel, and (b) fuel axial elongation of ultra-high burn-up fuel.

Compared to X425 fuel (Fig. 10(a)), the contact pressure between the fuel and clad is much lower for the sample high burnup fuel. On the other hand, nearly five times higher dose on the cladding reduces the necessary contact pressure between fuel and clad to ensure the plastic flow of the cladding. Fission gas release towards end of life is 95% (Fig. 19(a)). As a result of higher burnup, higher fuel porosity, longer fuel residence time, and higher coolant inlet temperature, the fission gas release is much higher compared to EBR-II conditions (Fig. 13). Furthermore, fuel axial elongation is 20% (Fig. 19(b)), nearly twice as high compared to 75% smear density U–10Zr EBR-II fuel pins. It is due to much lower fuel smear density and low initial linear heat rate. Fig. 20 shows the clad wastage behavior at end of life. It appears that most corrosion occurs at the clad inner side at the upper axial part of the fuel due to lanthanide attack. The total clad wastage appears to be below 20% of the total clad thickness.

![](images/44ae2b1da6d07a180e3c4d033d6436555217e0c35398f56d531dacd4fef531d9.jpg)  
Fig. 20. Clad inner and outer wastage of ultra-high burn-up fuel.

## 5.1. Potential concerns for ultra-high burn-up metallic fuel

\- It may be challenging for HT9 clad to preserve its creep fracture margin up to 500 dpa.

\- Fuel clad chemical interaction behavior appears to be controllable below 550 ◦C peak clad temperature; however, it may still bear a high uncertainty.

\- During long term transients, eutectic formation and penetration and fuel pin failure is a still concern although the fuel pin is vented.

\- Combination of the stiff fuel at low temperature and high cladding dose requirement eases the clad straining via irradiation creep while the fuel remains porous.

## 5.2. Possible design improvements

\- The study suggests using a porous, compliant and chemically stable buffer region at the fuel clad interface, similar to the work described by Karahan and Kazimi (2010), in order (1) to hinder fuel clad chemical interaction during steady state and transient, and (2) to allow for higher fuel temperature to ease hot pressing of the fuel porosity to accommodate solid fission product swelling. This may allow for operation with much lower contact pressure between fuel and clad.

\- If the axial power peaking is high, it may be possible to increase the fuel smear density at axial locations at which the burn-up is lower and the fuel is more compliant. This approach may also flatten the axial power profile, reduce the peak clad dose, and increase the fuel utilization.

## 6. Conclusions

Physical models in FEAST-METAL are improved further in order to increase the code’s performance in various operating conditions. Since the available database for metallic fuels is rather limited, gaining extrapolation ability via physics based semi-empirical models is very critical to design next generation reactors within a limited time span and guide the required experimental work.

First, a fission gas bubble grouping scheme based on constant atom number per bubble group is adopted while retaining isotropic bubble nucleation behavior. The bubble morphology of each phase structure is captured by assigning a constant number of gas atoms per bubble and the bubble shape at each radial node. Furthermore, the gas diffusion coefficient is defined in a phase dependent manner, using the activation energy of the corresponding phase structure. In addition to improvements on fission gas behavior, a best estimate value is preferred for solid fission product swelling rate. Next, it is proposed that hot pressing model for fuel interconnected porosity could be over-estimating the pore decrease for the dual phases. A correction factor is suggested for the compressibility factor for the dual phases in order to match fuel thermo-mechanical behavior, satisfactorily. The benchmarks show that the code can predicts the available EBR-II experimental data very well, similar to the previous version. On the other hand, added physics based models could improve the applicability of the code beyond the validated region.

The sample ultra-high burn-up vented fuel simulation shows that the fuel swelling and clad hoop strain is controllable by reducing the fuel smear density to near 60%. The resulting peak value of the total clad hoop strain is 3%. The stiffer fuel and high cladding dose leads to straining of the cladding although the fuel is very porous at the end of life. Fuel clad chemical interaction could be controlled if peak clad temperature remains below 550 ◦C. Near 20% clad wastage and the uncertainty associated with it may bring a design concern. The need for more compliant fuel slug and a necessity to hinder fuel clad chemical interaction may require a porous buffer layer between the fuel and clad. It is suggested that a chemically stable, low thermal conductivity, porous and compliant layer may allow for the sintering of the fuel open porosity and hinder fuel clad chemical interaction.

## Acknowledgement

This project is supported by TerraPower, LLC Company, Bellevue, WA.

## References

Crawford, D.C., Hayes, S.L., Pahl, R.G., 1994. Large-diameter, high plutonium metallic fuel testing in EBR-II. Trans. Am. Nucl. Soc. 71, 178–179.

Crawford, D.C., Porter, D.L., Hayes, S.L., 2007. Fuels for sodium-cooled fast reactors: US perspective. J. Nucl. Mater. 371, 202–231.

Gruber, E.E., Kramer, J.M., 1987. Gas bubble growth mechanisms in the analysis of metal fuel swelling. In: Proceedings of 13th International Symposium Radiation Induced Changes in Microstructure, ASTM-STP-955, p. p. 432.

Hoffman, E.A., Yang, W.S., Hill, R.N., 2006. Preliminary Core Design Studies for the Advanced Burner Reactor Over a Wide Range of Conversion Ratios, ANL-AFCI-177. Argonne National Laboratory, Argonne, IL.

Hofman, G.L., Pahl, R.G., Lahm, C.E., Porter, D.L., 1990. “Swelling Behavior of U–Pu–Zr Fuel”. Metall. Trans. A 21A, 517–528.

Hofman, G.L., Walters, L.C., Bauer, T.H., 1997. Metallic fast reactor fuels. Prog. Nucl. Energy 31, 83–110.

Karahan, A., Modeling of thermo-mechanical and irradiation behavior of metallic and oxide fuels for sodium fast reactors. Ph.D. Thesis. Nuclear Science and Engineering Department, Massachusetts Institute of Technology, 2009.

Karahan, A., Kazimi, M.S., 2010. Using graphitic foam as the bonding material in metal fuel pins for sodium fast reactors, Nuclear Fuels and Structural Materials Embedded Topical Meeting, American Nuclear Society Annual Meeting, vol. 102, pp. 790–792.

Kim, Y.S., Hofman, G.L., 2003. AAA Fuels Handbook, ANL-AAA-068. Argonne National Laboratory.

Lee, C.B., Kim, D.H., Jung, Y.H., 2001. Fission gas release and swelling model of metallic fast reactor fuel. J. Nucl. Mater. 288, 29–42.

McDeavitt, S.M., 1992. Hot isostatic pressing of U–10Zr alloy nuclear fuel by coupled grain boundary diffusion and power law creep. Ph.D. Thesis. Purdue University.

McDeavitt, S.M., Solomon, A.A., 1996. Hot-isostatic pressing of U–10Zr by a coupled grain boundary diffusion and creep cavitation mechanism. J. Nucl. Mater. 228, 184–200.

Ogata, T., Yokoo, T., 1999. Development and validation of alfus: an irradiation behavior analysis code for metallic fast reactor fuels. Nucl. Technol. 128, 113–123.

Pahl, R.G., Wisner, R.S., Billone, M.C., Hofman, G.L., 1990. Steady-state irradiation testing of U–Pu–Zr fuel > 18 at.% burn-up. In: Proceedings of the 19990 International Fast Reactor Safety Meeting, vol. 4, pp. 129–137.

Pahl, R.G., Porter, D.L., Crawford, D.C., Walter, L.C., 1992. Irradiation behavior of metallic fast reactor fuels. J. Nucl. Mater. 188, 3–9.

Tsuboi, Y., Ogata, T., Kinoshita, M., Saito, H., 1992. Mechanistic model of fission gas behavior in metallic fuel. J. Nucl. Mater. 188, 312–318.

Walters, L.C., 1999. Thirty years of fuels and materials information from EBR-II. J. Nucl. Mater. 270, 39–48.

Weaver, K., Ahlfeld, C., Gilleland, J., Whitmer, C., Zimmerman, G., 2009. Extending the nuclear fuel cycle with traveling-wave reactors, paper 9294. In: Proceedings of Global 2009, Paris, France, September 6–11.

Wood, M.H., Hayns, M.R., 1976. Factors influencing fission gas release and swelling in nuclear fuels, Technical Report, AERE-R-8153, Harwell, UK.

Yarsky, P., 2005. Core design and reactor physics of a breed and burn gas-cooled fast reactor. Ph.D. Thesis. Nuclear Science and Engineering Department, Massachusetts Institute of Technology.
