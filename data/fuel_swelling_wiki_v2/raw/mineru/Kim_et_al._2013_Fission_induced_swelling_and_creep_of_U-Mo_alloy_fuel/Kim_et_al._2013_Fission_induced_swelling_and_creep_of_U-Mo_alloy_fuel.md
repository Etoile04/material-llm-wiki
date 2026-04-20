# 📄 PDF Parsing Result

**File:** `/Volumes/openclaw记忆/Zotero_storage/storage/DDLBEMIF/Kim et al._2013_Fission induced swelling and creep of U-Mo alloy fuel.pdf`
**Backend:** `pipeline`
**Pages:** 0 to end
**Formula Recognition:** ❌ Disabled
**Table Recognition:** ✅ Enabled

---

# Fission induced swelling and creep of U–Mo alloy fuel q

Yeon Soo Kim a,⇑ , G.L. Hofman a , J.S. Cheon b , A.B. Robinson c , D.M. Wachs c

a Argonne National Laboratory, 9700 South Cass Avenue, Argonne, IL 60439, USA

b Korea Atomic Energy Research Institute, 989-111 Daedeok-daero, Yuseong, Daejeon 305-353, Republic of Korea

c Idaho National Laboratory, P.O. Box 1625, Idaho Falls, ID 83415, USA

## a r t i c l e i n f o

Article history: Received 29 November 2012 Accepted 28 January 2013 Available online 8 February 2013

## a b s t r a c t

Tapering of U–Mo alloy fuel at the end of plates is attributed to lateral mass transfer by fission induced creep, by which fuel mass is relocated away from the fuel end region where fission product induced fuel swelling is in fact the highest. This mechanism permits U–Mo fuel to achieve high burnup by effectively relieving stresses at the fuel end region, where peak stresses are otherwise expected because peak fission product induced fuel swelling occurs there. ABAQUS FEA was employed to examine whether the observed phenomenon can be simulated using physical–mechanical data available in the literature. The simulation results obtained for several plates with different fuel fabrication and loading scheme showed that the measured data were able to be simulated with a reasonable creep rate coefficient. The obtained creep rate constant lies between values for pure uranium and MOX, and is greater than all other ceramic uranium fuels.

\- 2013 Elsevier B.V. All rights reserved.

## 1. Introduction

Two forms of U–Mo alloy fuel have been irradiation- tested in the US GTRI (Global Threat Reduction Initiative ) in order to qualify this fuel for the conversio n of research and test reactors from highly enriched uranium (HEU) to low enriched uranium (LEU). One form, dispersion fuel, consists of fuel particles dispersed in an aluminum matrix and the other, monolith ic fuel, is of solid alloy fuel foil directly bonded to aluminum cladding. The geometry for both fuel forms is a thin plate. Fig. 1 schemati cally illustrates the cross section of a monolithic mini-fuel plate.

Swelling of U–Mo fuel only increases the plate thickness because the other dimensions are constrained. Consequently, fuel swelling can be estimated with fair accuracy by measuring the fuel plate thickness during post-irradiatio n analyses. U–Mo fuel swelling kinetics as a function of fission density is previously documented [1]. The U–Mo fuel swelling we are dealing with occurs at irradiation temperat ures typically lower than -250 C in research and test reactors. In addition, because the fission gas bubbles are small, the fuel swelling part that is affected by temperature is also small.

In the postirradiation examination (PIE) of fuel plates, it is a common observation that the fuel meat or foil swelling close to the plate width end is significantly diminished. This phenomeno n is clearly observable in some RERTR plates where one of the plate width ends faces the ATR core, resulting in a large power peaking at the foil end and subsequent ly a peak in fission density. Because fuel swelling increases with fission density, this is an obvious contradiction accordingly (see Fig. 2).

The most plausible causes for this phenomeno n are lateral fuel transport toward the fuel center in the width direction and accumulation of fuel mass at regions away from the foil end. The driving force for the fuel volume transport is the shear stress that builds up because of fission product induced fuel swelling while the Al cladding volume is preserved. Because the fuel foil end is blocked by the cladding, the resulting stress directs the fuel volume transport away from the plate to a lower stress region toward the fuel width center (Fig. 2). Fission induced creep of U–Mo is the underlyin g mechanis m that controls the rate of the fuel volume transport [2].

Although similar observations have been made for dispersion fuel plates, the phenomeno n is more difficult to quantify in this type fuel because of its complex microstru cture that include variations in fuel volume fraction in the meat, the presence of variable fractions of fuel–Al matrix interdiffusion products, and pore formation in matrix in some cases. Monolithic fuel plates do not have these complicati ons, so this paper focuses on analyzing monolithic fuel plates, leaving dispersion fuel plate analysis for future work.

Finite element analysis (FEA) using a commercial code ABAQUS [3] was employed to examine whether the observed phenomeno n is physically realistic by applying materials physical–mechanical parameters in reasonable ranges. Simultaneous ly, another objective of the FEA simulation was to obtain a creep rate coefficient that enables the extent of the fuel mass transport observed at the end of life (EOL) of the plates caused by creep.

![](images/b0e0b9a280ac2800f20b8a9d7181a0e2cb1a67194e4414914f5d67ed2b36a01f.jpg)  
Fig. 1. Schematic of as-fabricated cross section at axial mid-plane of a monolithic miniplate.

![](images/671b10059e0173a9357ccc375c1acc4a7822d7343f10137f035fce1319970575.jpg)  
Fig. 2. Fuel plate cross section in the width direction at near the ATR-core side end of L1P04A.

## 2. Experimental

The plates used for this paper were from irradiation tests RERTR-6, -7, -8, -9A, -9B, -10, and -12. The plate fabrication and irradiation properties are summarized in Table 1. The plate dimensions are 100 mm in length, 25 mm in width, and 1.40 mm in thickness, which are a miniature version, except for the thickness, of full-size fuel plates used in research reactors and test reactors. The fuel foil dimensions are 82.6 mm in length and 19.0 mm in width. Foil thickness is typically 0.25 mm, and in some cases 0.50 mm is used to examine the performanc e of thinner cladding.

The fuel foil was metallurgical ly bonded to Al 6061 cladding. Two kinds of bonding method were applied. One was friction stir welding (FSW) and – as the name implies – it achieved a metallurgical bonding between the fuel foil and cladding by welding, during which the cladding was instantaneo usly melted at the foil–cladding interface. The other method was hot isostatic pressing (HIP), in which an isostatic pressure of -103 MPa was applied for 90 min while the plate was heated at 560–580 C . The details of the bonding methods can be found, for example, in Ref. [4]. It is worth noting that both bonding methods produce uniform bonding and, more importantl y, do not alter foil thickness during plate fabrication.

All the test plates were irradiated in the Advanced Test Reactor (ATR) at INL. The fission rate histories of one representat ive plate from each test are compared in Fig. 3.

The plates were loaded in the ATR in such a configuration that either a flat plate surface or a narrow edge faced the ATR core center. In the former case, called face-on loading, the power distribution of the plate in the width direction is approximat ely symmetric and more uniform. Slight power peakings at the ends still exist due to the self-shieldin g effect. In the latter case, edge-on loading, the fission density of the edge of the plate that was closer to the ATR core is higher, as is illustrated in Fig. 4. The power ratio of the high power edge to the low power edge is about 2.5 for HEU plates and about 2 for LEU plates of RERTR-6, as determined in neutron physics analyses [5,6].

Table 1  
Description of irra diated mini fuel plates used in the analysis.
<table><tr><td rowspan="2">Test</td><td rowspan="2">Plate ID</td><td rowspan="2">U-Mo foil property and plate fabrication methoda</td><td rowspan="2">Enrichment (%U-235)</td><td rowspan="2">U-235 burnup, U-235-fissioned/U-235-initial (%)</td><td rowspan="2">Total duration (EFPD)</td><td rowspan="2">Fission densityb (1021 f/cm³)</td><td rowspan="2">BOL Fuel Temp (C)</td></tr><tr><td></td></tr><tr><td>RERTR-6</td><td>L1F040</td><td>U-10Mo(f,n)</td><td>19.7</td><td>46</td><td>135</td><td>3.0</td><td>113</td></tr><tr><td>RERTR-6</td><td>L1F100</td><td>U-10Mo(f,n)</td><td>19.7</td><td>46</td><td>135</td><td>3.0</td><td>124</td></tr><tr><td>RERTR-6</td><td>L2F030</td><td>U-10Mo(f,t)</td><td>19.7</td><td>40</td><td>135</td><td>2.6</td><td>145</td></tr><tr><td>RERTR-7</td><td>L1F140</td><td>U-10Mo(f,n)</td><td>58.2</td><td>27</td><td>90</td><td>4.4</td><td>177</td></tr><tr><td>RERTR-7</td><td>L2F040</td><td>U-10Mo(f.t)</td><td>58.3</td><td>17</td><td>90</td><td>2.7</td><td>199</td></tr><tr><td>RERTR-8</td><td>H1P010</td><td>U-12Mo(p,n)</td><td>57.5</td><td>31</td><td>105</td><td>5.7</td><td>164</td></tr><tr><td>RERTR-9A</td><td>L1P04A</td><td>U-10Mo(p.n)</td><td>58.3</td><td>28</td><td>98</td><td>4.5</td><td>152</td></tr><tr><td>RERTR-9A</td><td>L1F26C</td><td>U-10Mo(f,n)</td><td>57.5</td><td>33</td><td>98</td><td>5.5</td><td>181</td></tr><tr><td>RERTR-9A</td><td>L1F32C L1F34T</td><td>U-10Mo(f,n)</td><td>57.8 58.8</td><td>32</td><td>98 115</td><td>5.4</td><td>181</td></tr><tr><td>RERTR-9B RERTR-9B</td><td>L1P05A</td><td>U-10Mo(f,n) U-10Mo(p.n)</td><td>58.3</td><td>37 34</td><td>115</td><td>6.4 5.5</td><td>186</td></tr><tr><td>RERTR-9B</td><td>L1P09T</td><td>U-10Mo(p.n)</td><td>58.8</td><td>39</td><td>115</td><td>6.8</td><td>170 189</td></tr><tr><td>RERTR-10</td><td>L1P12Z</td><td>U-10Mo(p.n)</td><td>67.0</td><td>22</td><td>75</td><td>4.9</td><td>167</td></tr><tr><td>RERTR-12</td><td>L1P755d</td><td>U-10Mo(p.n)</td><td>70.0</td><td>25</td><td>90</td><td>5.9</td><td>156</td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

f: Friction bonding.  
p: Hot isostatic pressing bonding.  
n: As-fabricated foil thickness = 0.25 mm, plate thickness = 1.4 mm.  
t: As-fabricated foil thickness = 0.50 mm, plate thickness = 1.4 mm.  
a Number in front of Mo stands for Mo alloying content in weight%.  
b Fuel volume average at EOL including fissions by Pu produced during irradiation.  
c At fuel width center.  
d Face-on loading. All other plates were edge-on loaded to the center of the ATR (Fig. 4).

![](images/ce3e38a91e5a4c92aaef5e43bf2f4e97bdddca01046db7d8f43c6f63d7f77835.jpg)  
Fig. 3. Foil-averaged fission rate histories of fuel plates. A representative plate from each test is shown. An axial power peaking of 0.95 was multiplied to obtain the real value at the location where the PIE was performed except for RERTR-6. For RERTR-6, the axial power factor is about 1.

After irradiation, the plates were sectioned at the axial midplane. The fuel cross section was metallographi cally examined as shown in Fig. 4.

## 3. Post-irradiation analysis

As mentioned earlier, fuel swelling in a plate results only in a plate thickness increase because the cladding is relatively unrestrained in the thickness direction. Therefore, once the postirradiation foil thickness is known, total fuel swelling can be quantified using the following equation :

$$
\tag{ð1Þ}
$$

where Dt f is foil thickness change after irradiation, and t f is the asfabricate d foil thickne ss.

For plates from RERTR-6, -7, -8, -9A, 9B, -10, and -12, foil thicknesses were measure d using post-irradiatio n micrograp hs across the foil width with an interval typically of 0.5 mm. The measure d fuel swelling data are given in Table 2. The uncertainty in the measured fuel swelling is ±2%, mainly due to the fabricatio n variability in foil thickness.

Fuel swelling was also calculated by using the correlation available in the literature [1]. The correlation includes two parts: swelling by solid fission products and swelling by fission gas bubbles. It is expressed as a function of fission density. Therefore, once the fission density at the desired point is known, fuel swelling can be calculated. However, the calculated fuel swelling is purely by fission products; mass transfer by creep is not included. The calculated fuel swelling values are also included in Table 2.

The measured fuel swelling data of L1P04A are plotted with the calculated in Fig. 5. The measured swelling at the tapered end of the foil, marked by A in Fig. 5, is substantially lower than the calculated value. This and the evidence that the fission gas porosity does not vary in size and number density appreciably along several millimeters from the foil end (see Fig. 6) rule out, at least to the first order, the effect of fission gas induced fuel swelling. The calculated areas A and B, the areas enclosed by the measured fuel swelling curve and the calculated swelling curve, were close to each other. The same calculation showed that the areas C and D at the opposite end of the foil were also similar. This salient phenomeno n is commonly observed for all plates, although area comparis ons are not perfectly consistent in some plates. The conclusion is that a mass transfer has occurred from A to B, facilitated by fission induced creep in the fuel as a response to an applied stress.

## 4. ABAQUS simulation

## 4.1. Input data

A Young’s modulus of 66 GPa and a Poisson’s ratio of 0.34 for AA6061 cladding were taken from [7]. Yield strength of the tempered Al alloys increases to -280 MPa due to irradiation hardening [1]. This datum was used for the cladding consideri ng the heat processes during and post fabrication: hot rolling process for plate fabrication and autoclaving for oxide pre-filming. Strain hardenin g was taken into account and a strain hardening exponent of 0.13 for AA6061-T6 [8] was applied to the cladding with consideration of a decrease d potential of the strain hardening by neutron irradiation.

A Young’s modulus of U–Mo fuel of 85 GPa and Poisson’s ratio of 0.34 were used for U–Mo alloy [9]. Yield strength of U–Mo was not needed in the simulation.

Fission-in duced creep of U–Mo is dependent on the applied stress and fission rate. Thermal creep was not considered because the temperature regime of interest is so low that this phenomeno n is inactive. It is accepted in the literature that the fission-induced creep rate is linearly proportional to the fission rate. In some case, a stronger stress dependence was employed such as e\_ c - r1:5 for UO2 [10]. However, as Dienst noted [11], a linear stress dependence is most frequently used because it is easy to standardize experime ntal data with good accuracy. Hence, the following equation has been adopted for the U–Mo creep rate:

![](images/8c573a5593b9e8b0427c90ab764131232f489dd94489f6da24381e475f4cfa78.jpg)  
Fig. 4. Schematic showing plate loading directions and PIE location.

Fuel swel ling comparison between measured and calculated, DVV  (%).
<table><tr><td colspan="2">Distance from foil enda(mm)</td><td>0</td><td>0.5</td><td>1</td><td>1.5</td><td>2</td><td>2.5</td><td>3</td><td>3.5</td><td>4</td><td>4.5</td><td>5</td><td>5.5</td><td>6</td><td>6.5 7</td><td>7.5</td><td>8</td><td>8.5</td><td></td><td>9</td></tr><tr><td rowspan="2">L1F040</td><td>M C</td><td>0</td><td>7</td><td>17</td><td>22</td><td>28</td><td>29</td><td>28</td><td>25</td><td>23</td><td>21</td><td></td><td>19</td><td>19</td><td>19 19</td><td>17</td><td>17</td><td>16</td><td>16</td><td>15</td></tr><tr><td></td><td>21</td><td>19</td><td>19</td><td>18</td><td>17</td><td>16</td><td>15</td><td>15</td><td>14</td><td>21 14</td><td>14</td><td>13</td><td>13</td><td>13</td><td>12</td><td>12</td><td>12</td><td>12</td><td>12</td></tr><tr><td rowspan="2">L1F100</td><td>M C</td><td>0</td><td>10</td><td>17</td><td>26</td><td>31</td><td>31</td><td>31</td><td>29</td><td>27</td><td>21</td><td>23</td><td></td><td>23 22</td><td>17</td><td>19</td><td>19</td><td>18</td><td>18</td><td>16</td></tr><tr><td></td><td>26</td><td>25</td><td>24</td><td>23</td><td>22</td><td>21</td><td>20</td><td>19</td><td>19</td><td>25 18</td><td>18</td><td>18</td><td>17</td><td>17</td><td>17</td><td>17</td><td>16</td><td>16</td><td>15</td></tr><tr><td rowspan="2">L2F030</td><td>M</td><td>0</td><td>8</td><td>14</td><td>20</td><td>24</td><td>22</td><td></td><td>20</td><td>18 17</td><td>16</td><td>15</td><td>14</td><td>13</td><td>13</td><td>13</td><td>12</td><td>12</td><td>12</td><td>11</td></tr><tr><td></td><td>17</td><td>16</td><td>16</td><td>15</td><td>14</td><td>14</td><td></td><td>13</td><td>13 12</td><td>12</td><td>12</td><td>12</td><td>11</td><td>11</td><td>11</td><td>11</td><td>10</td><td>10</td><td>10</td></tr><tr><td rowspan="2">L1F140</td><td>C M</td><td>0</td><td>28</td><td>45</td><td>55</td><td>59</td><td>14 60</td><td></td><td>48</td><td>42 38</td><td>35</td><td>33</td><td>30</td><td>30</td><td>29</td><td>29</td><td>27</td><td>27</td><td>25</td><td>24</td></tr><tr><td></td><td>65</td><td>58</td><td>52</td><td>48</td><td>45</td><td>56 40</td><td></td><td>38</td><td>36 34</td><td>33</td><td>32</td><td>30</td><td>29</td><td>28</td><td>27</td><td>26</td><td>26</td><td>25</td><td>24</td></tr><tr><td rowspan="2">L2F040</td><td>C M</td><td>0</td><td>9</td><td>18</td><td>25</td><td>29</td><td>42 30</td><td>29</td><td>26</td><td>22</td><td></td><td></td><td></td><td>19</td><td>19</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>35</td><td>31</td><td>28</td><td>26</td><td>25</td><td>22</td><td></td><td>21</td><td>24 20</td><td>21</td><td>20 18</td><td>20 17</td><td>16</td><td>16</td><td>19 15</td><td>17 15</td><td>17 15</td><td>17 14</td><td>16 14</td></tr><tr><td rowspan="2">H1P010</td><td>C M</td><td></td><td></td><td>45</td><td>60</td><td></td><td>23</td><td></td><td></td><td>19 53</td><td>18</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td>0 75</td><td>23 67</td><td>61</td><td>55</td><td>70 70</td><td>70</td><td></td><td>60</td><td>60 42 40</td><td>50</td><td>48</td><td>45</td><td>43 35</td><td>40</td><td>40 32</td><td>38 32</td><td>38 31</td><td>38 30</td><td>38 29</td></tr><tr><td rowspan="4">L1P04A</td><td>C</td><td></td><td></td><td></td><td></td><td>52</td><td>49</td><td>47</td><td>44</td><td></td><td>39</td><td>39</td><td>37</td><td></td><td>34</td><td></td><td></td><td></td><td></td></tr><tr><td>M</td><td>0</td><td>20</td><td>45</td><td>56</td><td>63 64</td><td>63 29</td><td>59</td><td>52</td><td>45 23</td><td>38</td><td>35</td><td>33</td><td>31</td><td>30</td><td>29 27</td><td></td><td>26</td><td>25</td><td>23</td></tr><tr><td>Mb C</td><td>0 71</td><td>11</td><td>21 59</td><td>26</td><td>28</td><td>30</td><td></td><td>27 39</td><td>24 37</td><td>23</td><td>22</td><td>21</td><td>21</td><td>21</td><td>21</td><td>21</td><td>21</td><td>22</td><td>23 25</td></tr><tr><td></td><td>21</td><td>65 21</td><td>20</td><td>54 20</td><td>49 45</td><td>42</td><td></td><td>20</td><td>35 20</td><td>33 21</td><td>32 21</td><td>31 21</td><td>29 22</td><td>28 22</td><td>28 23</td><td>27</td><td>26</td><td>25</td><td>25</td></tr><tr><td rowspan="2">L1F26C</td><td>M</td><td>2</td><td>18</td><td>37</td><td>57</td><td>20</td><td>20 74</td><td>20 76</td><td></td><td>20 65</td><td></td><td></td><td>49</td><td>45</td><td>41</td><td></td><td>23</td><td>24</td><td>24</td><td></td></tr><tr><td></td><td>76</td><td>68</td><td>63</td><td>59</td><td>70 56</td><td></td><td>50</td><td>75 48</td><td>71 46</td><td>57</td><td>53 40</td><td></td><td>38</td><td></td><td>37 36</td><td>36 34</td><td>35</td><td>34</td><td>33 32</td></tr><tr><td rowspan="2">L1F32C</td><td>C M</td><td>0</td><td></td><td>42</td><td>58</td><td></td><td>53 75</td><td>77</td><td></td><td>44 62</td><td>42</td><td></td><td>39 45</td><td>42</td><td>37 39</td><td></td><td></td><td>34</td><td>33</td><td>32</td></tr><tr><td></td><td>72</td><td>21 67</td><td>62</td><td>58</td><td>70 54</td><td>51</td><td>48</td><td>75 46</td><td>71 44</td><td>55 40</td><td>50 39</td><td>38</td><td>36</td><td>35</td><td>37 35</td><td>35 34</td><td>33 33</td><td>32 32</td></table>

M: Measured.  
C: Calculated.  
a Distance from higher power side of foil end.  
b Distance from lower power side of foil end.  
c Distance from the opposite end of the foil in the face-on loaded plate.

![](images/75093c9fefd5f612eadcd3327a35f3d52f08cc46b4be7a2ba3ae6e333d5f5e21.jpg)  
Fig. 5. Comparison between measured and calculated fuel swelling for L1P04A plate.

$$
\tag{ð2Þ}
$$

where e\_ c is the equival ent creep strain rate (s1 ), A the creep rate coefficient (cm3 /MPa), r the equiva lent stress (MPa), and \_f the fission rate (fissions/cm3 s).

The total fuel swelling (i.e., swelling by fission gas bubble and swelling by solid fission products) correlation is available from [1] :

$$
\tag{ð3Þ}
$$

$$
\tag{ð4Þ}
$$

![](images/2ca76425a0a7147b2f515b0b8ab484b7083a0e429dc526271feff3e21e9927b9.jpg)  
Fig. 6. Optical micrographs showing fission gas pore morphology of L1P09T.

where fuel swelling is in percent and fd is in 10 21 f/cm3 . Note that the temperature effect is neglected in these equations for the following reasons. At the low temperat ure regime (<-250 C), fission gas diffusion is predomina ntly initiated by fission enhanc ed diffusion (FED) and the amount of therma lly activated gas diffusion is small. Also at these low temperatur es, the decompos ition of the as-fabric ated meta-stable c phase to the a + c0 phases is very slow and fission induced diffusion effectively reverse the a + c0 phases to the c phase [12,13]. Because of the c phase that has small gas bubble size, temperat ure effect on fuel swelling is small to the extent difficult to discern maske d by measureme nt uncertain ties [1].

Fuel true strain is derived from fuel swelling given in Eqs. (3) and (4) as follows:

$$
\tag{ð5Þ}
$$

## 4.2. Simulation for creep rate coefficient

The creep rate coefficient A in Eq. (2) was obtained by simulation of the U–Mo creep using ABAQUS FEA simulation.

The EOL condition of the plate L1P04A, which was irradiate d with edge-on loading and had the same cladding thickness on both faces, was simulated. For this case, only the upper half of the fuel plate was modeled by symmetry. A schematic of fuel plate crosssection and the FEA modeling scheme are shown in Fig. 7.

CPEG8R, generalized plane strain 8-node biquadra tic quadrilateral with reduced integration, was used. A geometrical ly nonlinear analysis was applied to make more precise analysis based on the geometry in the most recently completed increment. Again, bonding between fuel and cladding was assumed intact throughout life, which is inaccurate in some cases where debonding occurs.

FEA simulation was performed for fission product induced fuel swelling together with creep in L1P04A using several A values, and the best simulation was found when A = 500  1025 cm3 /MPa, as shown in Fig. 8. The fuel swelling simulation plotted in Fig. 8a shows fair simulation of the swelling peaks at both fuel ends. As the creep coefficient increases, the peaks move toward the foil width center, and their apices become closer to the measure d. Fitting becomes worse again when A is increased above 500  1025 cm3 /MPa. However, the uncertainties involved in the fuel swelling and the small differenc e from the case with A = 250  1025 cm3 /MPa suggest that

![](images/1d811bbcd3837db9ec7c9e402363ed3e2a9dc60f543f3e1ebaec5ea509a5e005.jpg)  
(a)

![](images/682af16ba12cbd3dd66928fd464c221b98845c3d9f243dda219770fcd96ed4e9.jpg)  
Fig. 7. Finite element modeling for L1P04A with edge-on loading and symmetric cladding thickness. (a) Schematic of fuel plate cross section and (b) finite element modeling.

![](images/f958f9c9bc373ea32a2cc7605e86fe303e0f423ffd6b73735be59767007fbee3.jpg)  
(a)

![](images/257a47a25f3839e18aab740032c8ef845670698311c0e973681d0ff11f5c0ce1.jpg)

(b)  
![](images/d11480ea5bdc30237c8165c60b6bd2fdc62b4c670f5a9e1226ba0ed935d8e597.jpg)  
Fig. 8. Finite element simulation results to fit creep rate coefficient using the measured data for L1P04A. (a) Fitting of the fuel swelling by using different creep rate coefficients A (in 10 25 cm3 /MPa), (b) Von Mises stress corresponding to the creep rate coefficient used in (a), and (c) Contour of fuel volume expansion by the combination of fuel swelling and creep-induced mass transfer from the foil end region to the foil width central region.

the obtained creep rate constant should also include considerable uncertainty although it is difficult to quantify.

The corresponding Von Mises stresses for the fuel swelling given in Fig. 8a are plotted in Fig. 8b. It is considered that the stresses obtained with A = 500  1025 cm3 /MPa is reasonable. The stress becomes zero at the foil end to satisfy the traction free boundary condition. It is also worth noting that the stress at the fuel central region in the width direction becomes smallest. The wave nature in stress suggests that this uneven stress state may be the major driving force to cause separation of fuel foil from cladding (i.e., debonding) during irradiation observed in some plates.

The simulation result of the combination of fission product induced fuel swelling and fuel mass transfer from the foil end to the foil central region in L1P04A is shown in Fig. 8c. The FEA simulation also implies that fuel volume increase by fission productinduced fuel swelling at the foil end region is effectively removed and accumulate d instead at the region showing peak foil thickness. Fuel flow is the highest at the foil thickness centerline and the lowest at the foil–cladding interface where the fuel is assumed to be perfectly bonded with the cladding.

The driving force for the mass transfer is provided by shear stress in the foil width direction. The evolution of the shear stress at the foil–cladding interface in the thickness direction was calculated at BOL, MOL and EOL and shown in Fig. 9. The shear stress increases as fission product induced fuel swelling increases. As a result, mass transfer increases.

![](images/e51eb6477d57de2eaa06063a63cc286eb527ac5a00761eadbd02224ad8024c19.jpg)  
Fig. 9. Calculated shear stress at the foil–cladding interface at three points in irradiation time of L1P04A. The signs are opposite across the center in the width direction due to direction change.

![](images/40300c53ba5d8c9dfd4ef1088de304d8a5a4eae5772948f1f8198ef3833e11f3.jpg)  
Fig. 10. Comparison of the predicted fuel swelling by FEA to the measured swelling of plate L1P05A. The predicted fuel swelling by the empirical correlation is also provided as a reference.

## 4.3. Validation of FEA simulatio n

The creep rate coefficient obtained in the previous subsection A = 500  1025 cm3 /MPa and the FEA simulation results were validated by applying this value in the simulation for other plates. Among the measure d plates given in Table 2, three plates with different fabricatio n geometry and plate loading direction were selected.

L1P04A and L1P05A had symmetr ic cladding thickness on both plate sides and edge-on loaded. FEA simulation was performed for L1P05A using the creep rate coefficient A = 500  1025 cm3 /MPa. The FEA result is in reasonable agreement with the measure ment (Fig. 10 ), although the simulated apex at the core side of L1P05A exhibits a slight discrepancy with the measureme nt.

L1P12Z was inadvertently fabricated with different cladding thickness on each side. FEA simulation was made for L1P12Z, using A = 500  1025 cm3 /MPa, to include the effect of the asymmetr ic cladding thickness. The schematic of fuel cross section and the fuel FEA modeling scheme are shown in Fig. 11 . As shown in Fig. 12 a, the FEA result is in excellent agreement with the measured fuel swelling. Fuel deformation obtained by FEA shown in Fig. 12 b occurs dominantly on the thin cladding side of the plate compare d to the thick side, which is in accord with the metallography shown in Fig. 12 c.

L1P755 from the RERTR-12 test is a face-on loaded. This loading scheme was employed to provide a more uniform power distribution across the plate width. As shown in Fig. 13 a, however, gamma scanning during PIE showed that power peaking still exists although less than the edge-on loaded plates. The FEA simulation result for L1P755, using A = 500  1025 cm3 /MPa shown Fig. 13 b compare s the FEA simulation result with the measured fuel swelling and the calculated fuel swelling without considering creep, in which the FEA simulation is consisten t with the measure ment.

## 5. Discussion

The consistent FEA simulatio ns with the measured data for L1P05A, L1P12Z and L1P755 using the creep rate coefficient A = 500  1025 cm3 /MPa in general implies that the fuel mass transfer is indeed enabled by a creep mechanism and that ABAQUS FEA is applicable in simulation of the fission induced creep observed for A = 500  1025 U–Mo alloy fuel regardless of fuel plate fabricatio n and loading types. ABAQUS FEA also demonstrates that

![](images/183dca47111e5348d49cb1dac37f6cc989a3bfda039db653daf07d322dc22402.jpg)  
(a)

![](images/71fd40ca85bfb00422902aaf9b65ea0092b595c109548fe3ead45568198f558e.jpg)  
(b)  
Fig. 11. Finite element modeling for L1P12Z with edge-on loading and asymmetric cladding thickness on each side. (a) Schematic of fuel plate cross section and (b) finite element modeling.

![](images/61bb019c9bbe3cdbc67b3526dc4c965dd849820c72b412ad9312203a57d1454d.jpg)  
(a) Comparison of the predicted fuel swelling by FEA to the measured swelling of plate L1P12Z. The predicted fuel swelling by the empirical correlation is also provided as a reference.

![](images/31e1f61a13f43e0438754d27ad8161e2537c65b8f638d27e774beb5815b4a3fb.jpg)  
(b) Fuel displacements for both halves of the foil.

![](images/4eeb914da6322a882845eb200a0f8ffbd6b065cfa39b8ae9c79d75b1ebf78a2e.jpg)  
(c) Optical micrograph of cross section of L1P12Z in the width direction  
Fig. 12. Finite element analysis results and PIE data of L1P12Z.

not only the obtained creep rate constant is acceptable, but also the FEA modeling itself is valid in simulating the measured data.

Fission enhanced creep at low homologous temperatures was reported for all uranium fuels and was first identified in a-U in the 1950s by Russian [14] and British [15] workers, and subsequently in ceramic fuels by various researchers [11,16–22] . Common for all, the creep rate was found to be athermal having a linear dependence on the applied stress and fission rate, as in Eq. (2). The obtained creep rate coefficient cm 3 /MPa is compared with other U-fuels in the literature at homologous temperatures relative to their melting points in Table 3. The obtained value for U–10Mo lies between values of pure uranium and MOX, and is about a half of the value of pure U. The slightly lower creep rate of the U–10Mo compare d to pure U is most likely due to its higher strength compared to the pure U.

The high creep rate enables the extent of observed fuel lateral mass transfer, which is the effective mechanis m that lessens the stresses caused by fission product induced fuel swelling at the foil end region where peak fission density is usually achieved. This mechanis m allows U–Mo fuel to achieve high burnup without failure, by reducing the potential to plate buckling due to lateral stresses induced by fuel swelling. The high creep rate can also explain the extent of fuel particle deformation observed in high burnup dispersion fuel plates shown in Fig. 14 , in which the spherical U– Mo particles, when they were as-fabricate d, underwent significant deformation during irradiation although deformat ion of fuel particles can also occur to some extent during production of the particles and plate fabrication. This plate also shows sintering between particles. The analysis of creep behavior of the dispersio n fuel plates is not pursued in this work.

![](images/cce66a36c2912e88ef0d988d5b8723bbf2cdd782aa514057099167640a7f4ecc.jpg)  
(a) Power peaking factors in the foil width direction measured by gamma scan

![](images/913af64749f487c0af450a01310797472885801e399e951e360f38444b2feeb9.jpg)  
(b) Comparison of the calculated fuel swelling by FEA to the measured swelling. The predicted fuel swelling by the empirical correlation is also provided as a reference.

Fig. 13. Power distribution across foil width and FEA analysis results for plate L1P755.  
Creep rate coefficient (A) in Eq. (2).
<table><tr><td>Fuel</td><td>A(10- -25 cm³/MPa)</td><td>~T/Tm</td><td>Reference</td></tr><tr><td>U</td><td>800</td><td>0.3</td><td>[14,17]</td></tr><tr><td>U-10Mo wt.%</td><td>500</td><td>0.3</td><td>Present study</td></tr><tr><td>MOX</td><td>56</td><td>0.25</td><td>[18]</td></tr><tr><td>UO2</td><td>7</td><td>0.25</td><td>[11,19,20]</td></tr><tr><td>UN</td><td>3</td><td>0.3</td><td>[21,22]</td></tr><tr><td>UC</td><td>1</td><td>0.3</td><td>[20]</td></tr></table>

T = test temperature, Tm = melting point.

The rather large increase in local fuel loading at the peak thickness location resulting from the lateral fuel creep may have to be considered for hot-spot calculations for reactors that operate fuel at high power after substanti al burnup. The additional plate thickness increase by creep in addition to fission product induced fuel swelling at the peak thickness location must be incorporated in safety analyses. The additional foil thickness increase by creep is -25% from the as-fabricate d foil thickness at a fission density of 7  1021 f/cm3 , which may be considerable in a safety analysis.

In the FEA analyses performed in this study, we used lifeaveraged fission rates instead of the time-depend ent ones given in Fig. 3 for the ease of calculation. The validity of this simplistic approach was examine d. Fission induced creep is a product of stress and fission rate; however, the stress is more important because it provides the driving force and the fission rate determines amplitud e of the creep rate. The stress is produced by the fission product induced fuel swelling, which is a function of fission density. The total creep strain is a time integration of the creep rate given in Eq. (2). Therefore, the case with the time-depend ent fission rate has higher fission density in early life than the average-fission rate case because the fission rate decrease s with burnup in all of the tests, except for RERTR-9A . FEA simulation for L1F140 at middle of life (MOL) compares the two cases in Fig. 15 . The fuel swelling at peak thickness location was slightly (-2%) larger for the time-dep endent fission rate case, whereas no differenc e was found at EOL between the two cases. This result is undoubte dly due to the linear stress on fission rate dependence of the creep rate.

Studies of the effect of porosity on thermal creep are available in the literature (see for example [23]). Porosity typically enhances the thermal creep rate. Since fission gas pores are formed in U–Mo, the porosity effect may be important for a more accurate analysis. Porosity in some high burnup U–Mo plates becomes considerable, greater than 10%. Hayes et al. [23] estimated that -12% augmentation in the creep rate was needed at this porosity in UO 2. Unlike thermal creep, however , for which the exponent of the stress term ranges 3–4, the porosity effect for fission induced creep is smaller because the exponent for the stress term is one. For this reason, a detailed study to accurately factor in this effect is not explored in this study. Nonetheless , it should be noted that the constant creep rate coefficient A employed in this study is simplistic. A burnup depende nt creep rate coefficient is more appropriate particularly at high burnup when porosity increases considerably by fission gas bubbles.

The temperature effect has not been considered in the FEA performed in this study, which follows the findings reported in literature [11,14–22]. The temperature s of the plates analyzed in this work are narrowly bounded between 110 and 190 C (Table 1). This low and narrow range of temperature s is the prerequis ite for athermal creep.

An implication from this work that affects the measureme nt of fission product induced fuel swelling is that one must avoid measuring it at or near the foil end regions. Measurements at these regions will lead to erroneous results affected by fuel lateral mass transfer.

## 6. Conclusion s

The taper of U–Mo fuel foil observed at the foil width end region, where fission density is highest, has been reviewed. The underlyin g mechanis m is lateral mass transfer by fission induced creep, which is athermal and depende nt on fission rate and stress that builds up by fission product induced fuel swelling in the area. The creep of U–Mo fuel is the effective mechanism that lowers the stresses at the foil end region where fission product induced fuel swelling is the highest because of peak fission density there, which enables U–Mo alloy fuel to achieve high burnup without failure. It also provides a realistic explanat ion for the observed anisotropic swelling in the fuel plates.

![](images/8356d3194e989b604f1ab7ea28812edfb71422dce0120ceedc014180b0f5823b.jpg)  
Fig. 14. Optical micrograph of the fuel meat end region of R6R018 where the meat-averaged fission density is -10  1021 f/cm3 -fuel-particle.

![](images/df310549cd2ced32365e7af89a3a6e88119dbcc842c7fce13c8aa2ea716c614c.jpg)  
Fig. 15. Comparison of FEA results for fuel swelling between the cases with the time-dependent fission rate and life-average fission rate at MOL for fuel plate L1F140.

ABAQUS finite element analysis (FEA) simulation coupled with a model for fission product induced fuel swelling and creep, produced consistent results using the measure d fuel swelling data for all fuel plate types and loading schemes with physical– mechanical data available in the literature. This proves that the fuel mass transfer is indeed induced by a creep mechanis m and validates that ABAQUS FEA is applicabl e in simulation of the fission induced creep observed for U–Mo alloy fuel.

ABAQUS simulatio n also produced the best-fit creep rate constant for U–10Mo alloy fuel 500  1025 cm3 /MPa, a value that is approximat ely a factor of two lower than that for pure uranium. However, the obtained creep rate constant includes considerable uncertainty, for which quantification is not tried in this study.

## Acknowled gments

The authors would like to thank Mrs. C. Clark, G. Moore, and J. Jue for the fabrication of the plates used in this work. The operation s staff at ATR is also acknowledged for the irradiation tests. The physics data available by Dr. G. Chang and Ms. M. Lillo are also appreciated . One of the authors (Y.S. Kim) thanks Mr. Y.S. Choo of KAERI for the measure ment of pore sizes used in Fig. 6 and Ms. S.H. Kim for the review of the manuscript. This work was supported by the U.S. Department of Energy, Office of Global Threat Reduction (NA-21), National Nuclear Security Administr ation, under Contract No. DE-AC-02-06C H11357 between UChicago Argonne, LLC and the Department of Energy.

## References

[1] Y.S. Kim, G.L. Hofman, J. Nucl. Mater. 419 (2011) 291.

[2] G.L. Hofman, Y.S. Kim, A.B. Robinson, in: Trans. 13th Internat. Topical Meeting Research Reactor Fuel Management (RRFM), RRFM 2009, Vienna, Austria, March 22–25, 2009. <http://www.euronuclear.org/meetings/rrfm2009/ index.htm>.

[3] ABAQUS Analysis User’s Manual, Dassault Systems, 2011.

[4] C.R. Clark, J.M. Wight, G.C. Knighton, G.A. Moore, J.F. Jue, in: The 27th International Meeting on Reduced Enrichment for Research and Test Reactors (RERTR), Boston, Massachusetts, November 6–10, 2005. <http:// www.rertr.anl.gov/RERTR27>.

[5] M.A. Lillo, MCNP-Calculated Gradients Across RERTR-6 and RERTR-7 Miniplates Irradiated in ATR, Interoffice Memo, INL, 2007.

[6] G.S. Chang, M.A. Lillo, As-Run Neutronics Analysis of the RERTR-9A/B Capsules in the ATR B 11 Position, Engineering Calculations and Analysis Report-231, 2008.

[7] J.S. Cheon, Y.S. Kim, Material Properties of Aluminum Alloys and Pure Zirconium for Use in High-density Fuel Development for Research Reactors, ANL/RERTR/TM-12-6, 2012.

[8] Y. Tamarin, Atlas of Stress–Strain Curves, Materials Park, Ohio, ASM International, 2002.

[9] A.M. Nomine, D. Bedere, D. Miannay, Grandeur, Mecaniques zassociées à la corrosion sous contrainte de I’alliage U–10Mo’’, paper presented at the Coloque sur la rupture des materiaux, Grenoble, 9–21 January, 1972.

[10] D. Brucklacher, in: Proc. Intern. Conf. CEBG Berkeley, Metals Soc. London, 1974.

[11] W. Dienst, J. Nucl. Mater. 65 (1977) 1.

[12] M.L. Bleiberg et al., J. Appl. Phys. 27 (11) (1956) 1270.

[13] M.L. Bleiberg, J. Nucl. Mater. 2 (1959) 182.

[14] S.T. Konobeevsky, N.E. Pravdyuk, V.I. Kutaitsev, in: UN Int’l Conf. Peaceful Use of Atomic Energy, Geneva, Switzerland, Paper No. 681, 1955.

[15] A.C. Roberts, A.H. Cottrell, Phil. Mag. 1 (1956) 711.

[16] A.S. Zaimovsky, in: UN Int’l Conf. Peaceful Use of Atomic Energy, 1958.

[17] M. Hesketh, Discussion in Paper, in: M. Englander, C.T. Montpreville, eds., 11th Colloque de Metallurgie, Creep, June 1967, Centre D’Etudes Nucleaires de Saclay, 1968, p. 28.

[18] R.J. White, The Re-Irradiation of MIMAS-MOX Fuel in IFA-629.1, HWR-586, March, 1999.

[19] A.A. Solomon, J. Am. Ceram. Soc. 56 (1973) 164.

[20] D.J. Clough, J. Nucl. Mater. 65 (1977) 24.

[21] D. Brucklacher, W. Dienst, Proc. Am. Ceram. Soc., Anaheim, California, USA, November 1971.

[22] P. Zeisser, G. Maraniello, P. Combette, J. Nucl. Mater. 65 (1977) 48.

[23] S.L. Hayes, J.K. Thomas, K.L. Peddicord, Mater. Lett. 9 (1990) 435.
