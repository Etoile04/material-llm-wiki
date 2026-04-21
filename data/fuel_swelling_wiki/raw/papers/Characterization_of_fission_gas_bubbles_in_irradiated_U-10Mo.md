# Characterization of fission gas bubbles in irradiated U-10Mo fuel

---

                                                                   Materials Characterization 131 (2017) 459–471



                                                                  Contents lists available at ScienceDirect


                                                                Materials Characterization
                                                      journal homepage: www.elsevier.com/locate/matchar




Characterization of ﬁssion gas bubbles in irradiated U-10Mo fuel                                                                                       MARK
                                ⁎
Andrew M. Casella , Douglas E. Burkes, Paul J. MacFarlan, Edgar C. Buck
Paciﬁc Northwest National Laboratory, P.O. Box 999, Richland, WA 99352, USA




A R T I C L E I N F O                                      A B S T R A C T

Keywords:                                                  A simple, repeatable method for characterization of ﬁssion gas bubbles in irradiated U-Mo fuels has been de-
Fission gas bubbles                                        veloped. This method involves mechanical potting and polishing of samples along with examination with a
U-Mo                                                       scanning electron microscope located outside of a hot cell. The commercially available software packages
Image analysis                                             CellProﬁler, MATLAB, and Mathematica are used to segment and analyze the captured images. The results are
Post irradiation examination
                                                           compared and contrasted. Baseline methods for ﬁssion gas bubble characterization are suggested for con-
AFIP-3
RERTR
                                                           sideration and further development.




1. Introduction                                                                             fuel. These bubble properties provide potential insight into the ﬁssion
                                                                                            gas evolution within the fuel matrix during irradiation and how this
    Development and deployment of low enriched uranium (LEU) fuels                          evolution contributes to fuel performance degradation and eventual
for research reactors has been pursued for more than thirty years                           failure. The Advanced Test Reactor (ATR) Full-size Plate In Center Flux
around the world, starting with the Reduced Enrichment for Research                         Trap Position (AFIP) experiments were designed to evaluate the per-
and Test Reactor (RERTR) program in the US [1]. The more recently                           formance of monolithic fuels at a scale prototypic of research reactor
established Materials Management and Minimization Reactor Conver-                           fuel plates. The AFIP-3 experimental fuel plates consisted of AA6061
sion Program continues these eﬀorts by signiﬁcantly accelerating the                        clad monolithic fuel plates using a metallic foil of U-10Mo enriched to
program's national and international nonproliferation objectives. Con-                      nominally 19.75% 235U. The metallic fuel foil of interest in this study
verting the fuel used in civilian research and test reactors to LEU per-                    was prepared by hot co-rolling a U-10Mo alloy ingot with Zr on either
manently secures the site by removing the threat posed by continued                         side [5]. The nominal thickness of the Zr was 25 μm on either side of
high-enriched uranium (HEU) operations. Reduction of the enrichment                         the foil and was introduced to minimize interaction between the U-
requires an increase in the uranium density of the fuel to provide ac-                      10Mo fuel and the AA6061 cladding, thereby acting as a “diﬀusion”
ceptable performance in reactor, leading to the development of new,                         barrier. The foil was hermetically sealed and bound within the AA6061
higher density dispersion and monolithic fuel plate designs. Uranium                        cladding using a hot isostatic pressing (HIP) process [6]. Additional
alloyed with nominally 10 wt% molybdenum (U-10Mo) is currently                              details on the various aspects of the AFIP-3 experiment can be found in
being developed as one potential high density LEU fuel to convert high-                     Perez et al. [7].
performance research and test reactors from the use of HEU fuels. In U-                         Post-irradiation, rectangular segments (roughly 12.5 mm × 27 mm)
10Mo, the molybdenum in uranium stabilizes the cubic gamma phase                            were taken from the AFIP-3BZ (referred to as Segment E) fuel plates at
allowing for acceptable swelling and integrity under irradiation [2–4].                     Idaho National Laboratory (INL) and transferred to Paciﬁc Northwest
    Characterizing the performance of new LEU fuels as a function of                        National Laboratory (PNNL) for examination of thermal properties [8].
burnup and temperature is essential in moving toward ﬁnal design,                           The analyses performed at PNNL provided information regarding
fabrication, and qualiﬁcation for use in existing or new reactors. Fission                  thermal transport and ﬁssion gas release on the physical scale of several
gas bubbles within the irradiated fuel matrix serve as key indicators of                    millimeters [9,10]. Additionally, these analyses provided data and in-
fuel performance. These bubbles contribute to swelling and thermal                          sight for eﬀorts to model microstructural evolution during irradiation
conductivity degradation and may ultimately be responsible for fuel                         and the subsequent impact on thermal properties [11]. However, more
failure. The size, number, distribution, eccentricity (a measure of                         detailed information regarding microstructure and ﬁssion gas bubble
bubble tendency to be spherical or lamellar), and orientation (a mea-                       distribution is necessary than was possible to acquire with an optical
sure of non-spherical bubbles toward a preferential alignment) of                           microscope. In order to obtain this detailed information, potted me-
bubbles can be determined from a cross-sectional image of irradiated                        tallography samples were resurfaced and examined with scanning


  ⁎
      Corresponding author.
      E-mail address: andrew.casella@pnnl.gov (A.M. Casella).

http://dx.doi.org/10.1016/j.matchar.2017.06.007
Received 3 April 2017; Received in revised form 2 June 2017; Accepted 4 June 2017
Available online 06 June 2017
1044-5803/ © 2017 Elsevier Inc. All rights reserved.
A.M. Casella et al.                                                                                                       Materials Characterization 131 (2017) 459–471


electron microscopy (SEM).
    Recent additions to the literature have documented eﬀorts to
identify and characterize ﬁssion gas bubbles in an irradiated U-Mo fuel
sample using the open source software CellProﬁler and the MATLAB
image processing toolbox [12,13]. In these articles, a fair amount of
eﬀort was devoted to the removal of sample preparation artifacts and
processing of the image taken from the SEM in order to generate an
image in which ﬁssion gas bubbles could be clearly and reliably iden-
tiﬁed and characterized. The work presented in this paper builds upon
these eﬀorts in an attempt to further develop an acceptable procedure
for characterizing ﬁssion gas bubble properties and distribution
throughout an irradiated fuel matrix.


2. Material and Methods

    Fuel segment E (TE), taken from the fuel plate irradiated in ex-
periment AFIP-3BZ, was received at PNNL in February 2014. The AFIP-
                                                                                      Fig. 2. Higher magniﬁcation extended depth of ﬁeld (EDF) image for TE-OM1.
3BZ fuel plate had in initial 235U enrichment of 19.937%, an initial Mo
concentration of 10.3 wt%, and was irradiated in the ATR for 101.0
Eﬀective Full Power Days (EFPD) during which it reached an average
burnup of 63.5 at.% and a calculated ﬁssion density of 4.32 × 1021
ﬁssions per cm3 [8,9]. Segment E was sectioned into smaller pieces at                                                          TE-OM1
PNNL and each piece was designated for a particular measurement
within the suite of examinations necessary for robust thermal analysis
(optical metallography, laser ﬂash analysis, gas pycnometry, and dif-
ferential scanning calorimetry). Of these smaller pieces, two were
dedicated to optical metallography; one (TE-OM1) was prepared so that
the examination was in the direction longitudinal to rolling during
fabrication and one (TE-OM2) was prepared so that the examination
was in the direction transverse to rolling during fabrication. Due to the
cutting pattern for sectioning fuel segment E, TE-OM2 actually con-
sisted of two small pieces potted together in one metallography sample.
It was decided for this work to focus on SEM image analysis of TE-OM1             Fig. 3. Image of TE-OM1 taken with an in-cell camera at the beginning of the current
                                                                                  work. The arrow points at the “foam” bubble that grew up around the sample due to
as it remained a single intact sample. As the analytical methods pre-
                                                                                  epoxy damage resulting from beta particles. The sample surface to be examined lies be-
sented in the paper have not been fully applied to TE-OM2, no con-
                                                                                  neath this bubble.
clusive results regarding the inﬂuence of rolling direction are currently
available. However, preliminary results are available [14]. Fig. 1 shows
a low magniﬁcation optical microscopy image of TE-OM1 while Fig. 2                the sample was transferred out of the hot cell and onto an SEM for
shows a higher magniﬁcation image of the same sample [8]. In Fig. 1,              imaging.
the entire fuel structure, including the fuel, zirconium “diﬀusion bar-               The series of low-magniﬁcation (67 ×) images shown in Fig. 4 il-
rier”, and cladding is shown. In Fig. 2, only a portion of the fuel is            lustrate the condition of sample TE-OM1 once it had been re-surfaced
shown, but several features of the microstructure are visible. Bands of           and placed in the SEM. As can be seen in the images, a signiﬁcant gap
ﬁssion gas bubbles are visible within a recrystallized matrix sur-                remained between the fuel and the surrounding epoxy. This gap is due
rounding intact grains, but it is challenging to reliably diﬀerentiate            to the same radiation damage that generated the foam that was me-
between individual bubbles, necessitating the use of an SEM.                      chanically removed from the surface. As the epoxy is non-conducting,
    Approximately two years elapsed after the completion of optical               typically a conductive coating must be applied prior to SEM examina-
analyses for the initial thermal property work during which Fig. 1 and            tion. However, the gap between the fuel and the epoxy and this sample
Fig. 2 were generated and the initiation of the SEM examinations dis-             allowed for direct examination without the application of such a
cussed in this paper. During that time, the high beta radiation ﬁeld              coating. Proceeding without sample coating oﬀered several advantages,
generated by the fuel signiﬁcantly degraded the epoxy in which the                including; simpliﬁcation of the procedure for sample preparation,
samples were set. Fig. 3 shows the condition of these samples at the              lowering exposure time to the sample preparer, elimination of possible
time that the current work was initiated. The epoxy foam that expanded            artifacts introduced by imperfect coating, ability to transfer the sample
over the samples was hard and had to be removed with 320 grit                     directly between optical and electron microscopes, and not introducing
abrasive. Once the surface was exposed, mechanical polishing for SEM              a potentially dispersible layer to a sample that had been deemed non-
analysis was completed according to the same process that has been                dispersible. The sample was grounded to the mounting post with silver
described previously [15]. Having re-prepared the surface for imaging,            paint. For the purposes of this paper, ﬁve equally-spaced positions
                                                                                  along the midline of the sample were examined at magniﬁcations of
                                                                                  2000 ×, 5000×, 10,000 ×, 15,000 ×, 20,000 ×, and 25,000 ×. These
                                                                                  positions were determined by ﬁrst locating the free end of the fuel (the
                                                                                  “left end” seen in the top two images of Fig. 4) and the painted end of
                                                                                  the fuel (the “right end” seen in the bottom two images of Fig. 4) and
                                                                                  assigning them as anchor points 1 and 2 respectively. The distance
                                                                                  between these two positions was 7.3 mm, which was less than the
                                                                                  9.1 mm length of sample TE-OM1 reported previously [8]. This diﬀer-
                                                                                  ence is due to the 1.8 mm of the sample being covered by silver paint
            Fig. 1. Low magniﬁcation optical microscopy image of TE-OM1.


                                                                            460
A.M. Casella et al.                                                                                                                       Materials Characterization 131 (2017) 459–471




Fig. 4. Low magniﬁcation images of the resurfaced TE-OM1 in the SEM. The arrow in the upper left image illustrates the “gap” between the fuel and the epoxy that was formed by
radiation damage. The vertical portion of the fuel is visible in this image, demonstrating the absence of epoxy in the “gap” region near the fuel. However, some epoxy remains in contact
with the fuel further down the sample as is also visible in the image.


(seen on the right side of the bottom two images in Fig. 4) that was used                       SEM, several pre-processing steps may be necessary in order to remove
to ground the sample. Position 3 was located 0.5 mm to the right of                             artifacts, remove background data, account for uneven illumination,
Position 1 and Position 7 was located 0.5 mm to the left of Position 2.                         and optimize contrast. Recently published work indicated that a sig-
Positions 4 through 6 were then equally spaced (1.575 mm apart) be-                             niﬁcant eﬀort was necessary in order to remove curtaining artifacts
tween Positions 3 and 7. The suite of images taken at all 6 magniﬁca-                           generated during sample preparation with a focused ion beam (FIB) and
tions for Position 3 is shown in Fig. 5.                                                        account for improper illumination [12,13]. In the current study, these
                                                                                                issues could be neglected as the sample preparation with mechanical
3. Theory/Calculation                                                                           polishers did not generate curtaining artifacts and performing SEM
                                                                                                analysis outside of a hot cell allowed for greater ﬂexibility in instrument
    As has been discussed previously in the literature [12,13], proper                          control so images with minimal illumination issues could be generated,
identiﬁcation and characterization of ﬁssion gas bubbles in images such                         as demonstrated in Fig. 5. As many of the diﬃculties in image pre-
as those presented in Fig. 5 can be diﬃcult with the results potentially                        processing could be neglected, analysis in the current work proceeded
being inﬂuenced by both the analyst and the software. As such, the                              by attempting to generate simple and as identical as possible analysis
purpose of the current work was to attempt to generate methods that                             techniques in CellProﬁler, MATLAB, and Mathematica. The lists of
are simple and reproducible in order to generate baseline analyses to                           commands or modules used for comparative analysis in this paper are
which future analyses can be compared. It was a main objective to                               presented in Table 1.
remove to the greatest extent possible any subjectivity and discuss the                             While the lists of commands in Table 1 for CellProﬁler and MATLAB
possible impacts of doing so. While many image analysis software                                are longer than that for Mathematica, the operations on the original
packages are available and new algorithms are constantly in develop-                            SEM image being performed by each software package are essentially
ment, the current work focuses on using the CellProﬁler and MATLAB                              the same. The ﬁrst four modules listed for CellProﬁler are shaded as
image processing toolbox packages investigated in recent publications                           they are input modules and necessary for any pipeline, while the ﬁnal
[12,13] in addition to the Mathematica image processing and analysis                            six modules are analysis modules. Additionally, the list of parameter
suite of tools.                                                                                 settings that must be speciﬁed by the analyst within each module in the
    Depending on the quality of the initial image captured from the                             pipeline is extensive [14].

                                                                                          461
A.M. Casella et al.                                                                                                  Materials Characterization 131 (2017) 459–471




                                               Fig. 5. Images at multiple magniﬁcations of Position 3 of TE-OM1.


    The ﬁrst four (input) modules listed for CellProﬁler accomplish the            turned white and white pixels are turned black). Fission gas bubbles are
same task as the ﬁrst command for MATLAB and Mathematica, which is                 then identiﬁed as groupings of white pixels in contact with one another
simply to import the raw SEM image into the software package. After                and completely separated from other white pixels by surrounding black
this, all three software packages crop the image in order to remove the            pixels. Finally, the population of identiﬁed ﬁssion gas bubbles is char-
data associated with the image that is generally listed at the bottom by           acterized for comparison with other images.
the SEM software. If this information is not removed from the image, it                Each software package has built-in algorithms for characterizing the
will disrupt the process of determining the appropriate threshold value            population of identiﬁed objects (ﬁssion gas bubbles in this case). In the
for image segmentation due to the presence of pure black in the                    present work, the characteristics that are investigated are 1) number of
background and pure white in the letters. Subsequently, the image is               bubbles, 2) bubble size, 3) bubble orientation, and 4) bubble eccen-
converted to grayscale and the intensity threshold for segmentation is             tricity. The ﬁrst two characteristics are straight forward as the number
determined. The image is segmented and inverted (black pixels are                  of objects identiﬁed and the number of pixels comprising each object

                                                                             462
A.M. Casella et al.                                                                                                                               Materials Characterization 131 (2017) 459–471


Table 1
List of commands used to segment the images discussed in this paper.

  Step    CellProﬁler        MATLAB                        Mathematica

  1       Images             I1 = imread(‘path\I0’);       I1 = Import[“path\\I0”];
  2       Metadata           I2 = imcrop(I1,               I2 = ImageCrop[I1,{850,850},
                             [0,0,850,850]);               {Right,Bottom}];
  3       Names and          I3 = rgb2gray(I2);            I3 = Binarize[I2];
          types
  4       Groups             level = graythresh(I3);       I4 = ColorNegate[I3];
  5       Crop               I4 = im2bw(I3, level);        Mean                                               Fig. 6. Test array to determine characterization parameter properties.
                                                           [ComponentMeasurements[I4,
                                                           “property”][[All,2]]]//N
  6       Color to gray      I5 = im2uint8(I4);                                                      Table 3
  7       Apply              I6 = imadjust(I5,[0;1],                                                 Characterization of Array using all three software packages for comparison.
          threshold          [1;0]);
  8       Apply              cc = bwconncomp                                                                                    CellProﬁler           MATLAB             Mathematica
          threshold          (I6,8);
                                                                                                       # of objects             3                     3                  3
  9       Identify           bd = regionprops(cc,
                                                                                                       Object size              (3,4,4)               (3,4,4)            (3,4,4)
          primary            ‘all’);
                                                                                                           distribution
          objects
                                                                                                       Eccentricity             (0.8044, 0.7806,      (0.7303,           (0.8165, 0.7906,
  10      Measure            dsbd = struct2dataset
                                                                                                                                0.9056)               0.8660,            0.9129)
          object size        (bd);
                                                                                                                                                      0.7319)
          shape
                                                                                                       Orientation              (45, 90,              (−45, 18.435,      (−0.7854,
                                                                                                                                − 18.435)             90)                − 1.5708, − 2.8198)
                                                                                                       Centroid                 (1.3333, 1.6667)      (2.3333,           (1.8333, 5.8333)
are direct products of the image identiﬁcation process. The bubble or-                                                                                2.6667)
ientation and bubble eccentricity are both more complex as they are                                                             (5.75, 2)             (2.75, 6.25)       (6.25, 5.5)
based on the concept of a best-ﬁt ellipse.                                                                                      (1.75, 5.25)          (6.75, 3)          (2.25, 2.25)
    In order to understand the results generated from each software                                    Semiaxes                 (2.3986, 1.425)       (2.582,            (1.1547, 0.6667)
                                                                                                                                                      1.7638)
package, it is important to identify the methods for generating and                                                             (2.9164, 1.8227)      (3.6515,           (1.4142, 0.8660)
interpreting characteristics of best-ﬁt ellipses. Determining the exact                                                                               1.8257)
numerical process that each software package uses for the determina-                                                            (3.5504, 1.5057)      (3.0551,           (1.7321, 0.7071)
tion of best-ﬁt is not straight-forward. The user manuals for each soft-                                                                              2.0817)
ware package lack an explicit deﬁnition of a best-ﬁt ellipse. Insight into
this issue can only be gained by the given deﬁnitions for the char-
                                                                                                     software package can be resolved by the diﬀerent approaches each
acteristics of interest as are listed in Table 2.
                                                                                                     software package has for deﬁning axes and angles within the array of
    The deﬁnitions for Eccentricity and Orientation within CellProﬁler
                                                                                                     pixels being examined. These approaches as well as the method for
and MATLAB appear to be the same with the best-ﬁt ellipse being de-
                                                                                                     modifying them in order to generate comparable values between the
ﬁned as the ellipse with the same second-moments as the deﬁned re-
                                                                                                     three software packages are presented in Table 4. The results of mod-
gion. On the other hand, Mathematica only deﬁnes the parameters in
                                                                                                     ifying the values in Table 3 as suggested in Table 4 are shown in
terms of an undeﬁned best-ﬁt ellipse. Likely, in all cases, a numerical
                                                                                                     Table 5.
minimization method is used to generate a best-ﬁt ellipse that has the
                                                                                                         In addition to the modiﬁcations suggested in Table 4, additional
same second central-moment. In order to provide insight into this in-
                                                                                                     changes are necessary due to the method of reporting values for each
vestigation, consider the fabricated pixel array (Fig. 6), in which black
                                                                                                     software package. Speciﬁcally, the second and third objects must be
(background) pixels are denoted with a 0 and white (object) pixels are
                                                                                                     switched in order for the results generated by MATLAB to match those
denoted with a 1.
                                                                                                     of CellProﬁler and Mathematica. Object order is not important for
    It is clear that this array contains three objects, 1 composed of three
                                                                                                     analysis of average values, but is in the direct comparison of individual
pixels and 2 composed of four pixels. Subjecting this array to the ne-
                                                                                                     objects as is done in Table 3 and Table 5. Additionally, the values for
cessary steps listed in Table 1 generates the results listed in Table 3.
                                                                                                     the semiaxes must be divided by 2 for the results generated by Cell-
    The results presented in Table 3 show agreement between all three
                                                                                                     Proﬁler and MATLAB in order to match the half-values presented by
software packages for the number of objects identiﬁed and the object
                                                                                                     Mathematica. With these adjustments, as can be seen in Table 5, good
size distribution. However, there is considerable deviation in the results
                                                                                                     agreement exists for all values generated for these parameters by the
generated by each package for eccentricity, orientation, centroid, and
                                                                                                     three software packages, with the exception of the values of the
semiaxes. The diﬀerences in the orientation and the centroid for each

Table 2
Deﬁnitions of eccentricity and orientation within each software package considered in this study.

  Eccentricity

  CellProﬁler           “The eccentricity of the ellipse that has the same second-moments as the region” [16]
  MATLAB                “Returns a scalar that speciﬁes the eccentricity of the ellipse that has the same second-moments as the region. The eccentricity is the ratio of the distance between
                        the foci of the ellipse and its major axis length. The value is between 0 and 1. (0 and 1 are degenerate cases. An ellipse whose eccentricity is 0 is actually a circle,
                        while an ellipse whose eccentricity is 1 is a line segment.)” [17]
  Mathematica           “Eccentricity of the best-ﬁt ellipse” [18]

  Orientation
  CellProﬁler           “The angle (in degrees ranging from − 90 to 90°) between the x-axis and the major axis of the ellipse that has the same second-moments as the region” [16]
  MATLAB                “Returns a scalar that speciﬁes the angle between the x-axis and the major axis of the ellipse that has the same second-moments as the region. The value is in
                        degrees, ranging from −90 to 90°. “[17]
  Mathematica           “Angle between the largest axis [of the best-ﬁt ellipse] and the horizontal axis” [18]



                                                                                               463
A.M. Casella et al.                                                                                                                                    Materials Characterization 131 (2017) 459–471


Table 4
Comparison of angle and location deﬁnitions between the three software packages.

                                   CellProﬁler                               MATLAB                                     Mathematica

  Orientation angle and units




                                   Degrees                                   Degrees                                    Radians
  Correction to orientation        Reverse the sign                          Assign an orientation of − 90° to an       Convert to degrees (multiply by 180°/π); add 180° to the
      angle for comparison                                                   object with an orientation of 90°.         orientation of an object with an orientation less than − 90° and
                                                                                                                        subtract 180° from the orientation of an object with an orientation
                                                                                                                        greater than or equal to 90°
  2-dimensional origin             Top left                                  Top left                                   Bottom left
  Location identiﬁcation
      method (pixel index)




  Correction to location for       Add (0.5,0.5)                             Subtract (0.5, 0.5)                        ‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐‐
      comparison                   Subtract resulting y-value from 8         Subtract resulting y-value from 8
                                   (number of y-pixels)                      (number of y-pixels)



Table 5
Results from Table 3 after modiﬁcations described in Table 4.

                         CellProﬁler             MATLAB                Mathematica

  # of objects           3                       3                     3
  Object size            (3,4,4)                 (3,4,4)               (3,4,4)
      distribution
  Eccentricity           (0.8044, 0.7806,        (0.7303, 0.7319,      (0.8165, 0.7906,
                         0.9056)                 0.8660)               0.9129)
  Orientation            (−45, − 90,             (− 45, −90,           (−45, − 90,
                         18.435)                 18.435)               18.435)
  Centroid               (1.8333, 5.8333)        (1.8333,              (1.8333, 5.8333)
                                                 5.8333)
                         (6.25, 5.5)             (6.25, 2.5)           (6.25, 5.5)
                         (2.25, 2.25)            (2.25, 2.25)          (2.25, 2.25)
  Semiaxes               (1.1993, 0.7125)        (1.291, 0.8819)       (1.1547, 0.6667)
                         (1.4582,                (1.52755,             (1.4142, 0.8660)
                         0.91135)                1.04085)
                         (1.7752,                (1.82575,             (1.7321, 0.7071)
                         0.75285)                0.91285)



semiaxes and eccentricity. This exception is most likely due to diﬀerent
numerical algorithms being employed by each software system in order
to determine the best-ﬁt ellipse for each object. These results are shown
graphically in Fig. 7. Thus, after the modiﬁcations discussed are im-                              Fig. 7. Visual representation of best-ﬁt ellipses generated by each software package for
plemented, the results for number of objects, object size, and object                              the three objects (Red (small) = Mathematica, Green (intermediate) = CellProﬁler, Blue
orientation can be interpreted quantitatively, while the results for ec-                           (large) = MATLAB). (For interpretation of the references to colour in this ﬁgure legend,
centricity should be interpreted qualitatively until the algorithm for                             the reader is referred to the web version of this article.)

determining the best-ﬁt ellipse by the software package being used is
fully understood.                                                                                  was manually inserted into CellProﬁler in order to determine if the
    In order to expand the comparison of the results of image segmen-                              segmented image generated by CellProﬁler was in better agreement
tation performed with each software package to a true image, the                                   with the segmented images generated by MATLAB and Mathematica
10,000 × magniﬁcation image of position 3 of TE-OM1 (shown in                                      than the segmented image generated by CellProﬁler with its own
Fig. 5) was subjected to each of the processes described in Table 1.                               threshold value. The results of all four of these analyses are presented in
During each of the image processing schemes, a pixel intensity                                     Fig. 8.
threshold value was generated by each software package using its own                                   It is evident from visual inspection that the binary image generated
version of the Otsu method [13,19]. The resulting threshold values                                 solely within CellProﬁler, using the pixel intensity threshold generated
were 0.4235, 0.4706, and 0.4706 for CellProﬁler, MATLAB, and                                       by CellProﬁler, diﬀers from the other three binary images in Fig. 8.
Mathematica, respectively. As the threshold values were exactly the                                However, it is very diﬃcult to pick out any distinct diﬀerences between
same (within rounding error) for MATLAB and Mathematica, this value                                the three binary images generated with the same pixel intensity


                                                                                             464
A.M. Casella et al.                                                                                                                   Materials Characterization 131 (2017) 459–471




Fig. 8. Segmented images generated for the 10,000 × magniﬁcation SEM image at Position 3 of sample TE-OM1 generated by CellProﬁler with pixel intensity threshold value generated
by CellProﬁler (top left), CellProﬁler with pixel intensity threshold manually set to match the value determined by MATLAB and Mathematica (top right), MATLAB (bottom left), and
Mathematica (bottom right).


Table 6                                                                                            visual examination of Fig. 8. When using the intensity threshold value
Comparison of Basic Object Analysis Results for the four Images in Fig. 8. All results are         generated within CellProﬁler, fewer and smaller objects are identiﬁed
generated in the same software package used to generate the corresponding binary image.
                                                                                                   by CellProﬁler than MATLAB and Mathematica. However, the average
The results for eccentricity and orientation have been modiﬁed as described in Table 4 for
direct comparison.                                                                                 eccentricity and the average orientation do not greatly diﬀer from the
                                                                                                   values generated by MATLAB and Mathematica. It is likely that the
                       Number of      Average          Average           Average                   diﬀerent threshold value causes several objects comprised of a single
                       objects        object size      eccentricity      orientation               pixel to not be identiﬁed as objects. Additionally, some pixels com-
                                      (pixels)
                                                                                                   prising the edges of identiﬁed objects are thresholded as background,
  CellProﬁler          1155           62.96            0.690             − 3.66                    resulting in smaller objects. This process apparently has very little eﬀect
  CellProﬁler –        1328           76.18            0.695             − 3.26                    on the average eccentricity of the objects in the image. The absolute
      manual                                                                                       value of the average orientation is greater than the orientation values
      threshold
                                                                                                   generated by MATLAB and Mathematica, which is consistent with the
  MATLAB               1328           76.53            0.681             − 3.28
  Mathematica          1328           76.53            0.692             − 3.28                    dismissal of several one-pixel objects which by deﬁnition must have an
                                                                                                   orientation of zero. This is an interesting phenomenon that will be
                                                                                                   explored later as analyses will be performed for comparison with the
threshold. In order for a more direct quantitative comparison, the ob-                             deliberate removal of one-pixel objects.
ject population of each image was characterized within the software                                    The analyses performed to generate Table 6 were performed for
package it was created in order to generate Table 6. These character-                              each of the six magniﬁcations at each of the ﬁve positions to generate
izations were performed according to the procedures listed in Table 1                              the results presented in Fig. 9. The data presented in Fig. 9 were only
and the modiﬁcations subsequently discussed were applied.                                          generated in Mathematica. As expected, the number of bubbles counted
    Table 6 quantitatively veriﬁes the earlier conclusions based on                                at each location decreases fairly linearly as the magniﬁcation increases.


                                                                                             465
A.M. Casella et al.                                                                                                           Materials Characterization 131 (2017) 459–471




                           Fig. 9. Average values for bubbles at each magniﬁcation considered at each location examined along sample TE-OM1.


This is simply due to the increased magniﬁcation capturing a pro-                      particular interest, it was performed on the images discussed in this
portionally smaller area of the fuel. The average bubble size has been                 paper. This analysis was performed using the “FindFit” function in
converted to equivalent spherical diameter as this is a more accepted                  Mathematica. The log-normal distributions resulting from this analysis
unit in this ﬁeld of study. Mathematica automatically determines the                   for each magniﬁcation at position 7 are presented in Fig. 10. The results
“EquivalentDiskRadius” within its “ComponentMeasurements” func-                        follow a trend very similar to that shown in Fig. 9 but with less var-
tion. This equivalent disk radius is calculated by determining the radius              iation in the bubble sizes as a function of image magniﬁcation. It should
of a circle that has the same area as the bubble. The equivalent disk                  be noted that the values of mean and standard deviation presented in
diameter was determined by multiplying the equivalent disk radius by                   Fig. 10 correspond to the log normal distribution associated with the
2. As the images are 2-dimensional, it is not directly possible to directly            bubble population whereas the values in Fig. 9 were generated directly
determine the equivalent spherical diameter. However, assuming that                    from the bubble populations themselves. The process of ﬁtting a dis-
the equivalent disk were to be rotated through Pi radians to generate a                tribution ﬁrst requires a placement of bubbles into size bins that can
sphere, that sphere would have the same diameter as the equivalent                     ultimately aﬀect the values of the mean and standard deviation asso-
disk. As such, the equivalent disk diameter is presented as the equiva-                ciated with each distribution. For consistency, the width of each size
lent spherical diameter in Fig. 9. The average eccentricity appears to                 bin used in the development of each distribution shown in Fig. 10 is
approach 0.7 as the magniﬁcation increases at each sample position.                    0.1 μm.
The average orientation is determined in a fashion consistent with the
preceding discussion and shows a general scatter in results as magni-                  4. Discussion
ﬁcation increases.
     The average parameter values presented in Fig. 9 have relevance as                    The methods and results discussed in the previous sections de-
discussed in the following section. However, there is also value in                    monstrate the eﬀectiveness of a simple method for analyzing ﬁssion gas
knowing distributed parameter values along with their associated sta-                  bubbles in irradiated U-Mo fuel for the purpose of baseline analysis
tistics. Generating these distribution values and statistics forces further            across various researchers in the ﬁeld. However, as alluded to, further
action on the part of the analyst as is also discussed in the following                discussion of these methods and results are warranted. The ﬁrst topic of
section. As the purpose of this paper is to present a minimal method for               discussion is the outlying datapoint in Fig. 9 for average eccentricity at
generating baseline values for comparison of information generated by                  a magniﬁcation of 25,000 × at position 7. Upon further inspection of
researchers across this particular ﬁeld of study, emphasis is not placed               this image, it was discovered that there was an artifact in the image
here on such analysis. However, as particle size distribution is of                    acquisition and that removal of this artifact resulted in an average

                                                                                 466
A.M. Casella et al.                                                                                                                                                                                                            Materials Characterization 131 (2017) 459–471


                                                                                Position 7, 2000x Magnification                                                                                            Position 7, 5000x Magnification
                                                                                                                                                                                   3.5

                                                            3.0
                                                                                                                                                                                   3.0




           Probability Distribution Function                                                                                                   Probability Distribution Function
                                                                                            Mean = 0.323µm                                                                                                            Mean = 0.286 µm
                                                            2.5                             Std. Dev. = 0.394 µm                                                                                                      Std. Dev. = 0.281 µm
                                                                                                                                                                                   2.5

                                                            2.0                                                                                                                    2.0

                                                            1.5                                                                                                                    1.5

                                                            1.0                                                                                                                    1.0

                                                            0.5                                                                                                                    0.5

                                                            0.0                                                                                                                    0.0
                                                                  0.0                0.5                        1.0              1.5                                                     0.0   0.2              0.4            0.6         0.8       1.0
                                                                                    Equivalent Spherical Diameter       m                                                                                  Equivalent Spherical Diameter         m


                                                                                Position 7, 10000x Magnification                                                                                       Position 7, 15000 x Magnification
                                                            3.5
                                                                                                                                                                                   3.5
                                                            3.0
                                                                                                                                                                                                                       Mean = 0.274µm




                        Probability Distribution Function                                                                                      Probability Distribution Function
                                                                                                 Mean = 0.288µm                                                                    3.0
                                                                                                 Std. Dev. = 0.296 µm                                                                                                  Std. Dev. = 0.290 µm
                                                            2.5
                                                                                                                                                                                   2.5

                                                            2.0
                                                                                                                                                                                   2.0

                                                            1.5                                                                                                                    1.5

                                                            1.0                                                                                                                    1.0

                                                            0.5                                                                                                                    0.5


                                                            0.0                                                                                                                    0.0
                                                                  0.0   0.2                0.4            0.6         0.8       1.0                                                      0.0         0.2                 0.4            0.6             0.8
                                                                                    Equivalent Spherical Diameter           m                                                                              Equivalent Spherical Diameter         m


                                                                               Position 7, 20000x Magnification                                                                                       Position 7, 25000x Magnification


                                                                                                                                                                                   4




                        Probability Distribution Function                                                                                      Probability Distribution Function
                                                                                                  Mean = 0.262µm                                                                                                       Mean = 0.221µm
                                                            3
                                                                                                  Std. Dev. = 0.287 µm                                                                                                 Std. Dev. = 0.230 µm
                                                                                                                                                                                   3


                                                            2
                                                                                                                                                                                   2


                                                            1
                                                                                                                                                                                   1



                                                            0                                                                                                                      0
                                                                0.0           0.2                   0.4                0.6             0.8                                             0.0           0.2                 0.4               0.6                0.8
                                                                                    Equivalent Spherical Diameter       m                                                                                  Equivalent Spherical Diameter      m

                                                                                             Fig. 10. Log normal distribution ﬁts for images of all magniﬁcations at position 7 of TE-OM1.


eccentricity value for this image of 0.705 instead of 0.759. This image                                                                                                        magniﬁcations further from zero. These trends in average eccentricity
with and without the artifact is shown in Fig. 11. This dropped the                                                                                                            and orientation are due to the fact that all single pixel bubbles by de-
outlying data point back into a value more consistent with the trend of                                                                                                        ﬁnition have orientations and eccentricities of zero.
the other data points as shown in Fig. 12. Fig. 12 also provides a                                                                                                                  Fig. 12 shows that consideration of single pixel bubbles has a sig-
comparison of the average eccentricity and average orientation values                                                                                                          niﬁcant eﬀect on average eccentricity and orientation values for images
for each position and location for the two cases 1) all bubbles are                                                                                                            that contain a large fraction of single pixel bubbles. Additionally, there
considered and 2) only bubbles with areas greater than 1 pixel are                                                                                                             is signiﬁcant spread in the values for average orientation, especially as
considered. The results show that even if the artifact is removed from                                                                                                         the magniﬁcation of each sample increases. The particular outliers in
the 25,000 × magniﬁcation image at position 7, the eccentricity con-                                                                                                           the trend appear to occur at high magniﬁcations of positions 5 and 6. In
tinues to trend upward if bubbles comprised of a single pixel are not                                                                                                          order to provide insight into this phenomenon, the original images for
considered. Also, the average eccentricity values become more con-                                                                                                             20,000 × magniﬁcation at position 5 and 25,000 × magniﬁcation at
sistent across magniﬁcations with the removal of single pixel bubbles.                                                                                                         position 6 are shown in Fig. 13. The 20,000 × magniﬁcation image is
Additionally, removal of single pixel bubbles has little eﬀect on the                                                                                                          used for position 5 due to the afore mentioned artifact in the 25,000 ×
average orientation values other than to drive the values for low                                                                                                              magniﬁcation image.

                                                                                                                                             467
A.M. Casella et al.                                                                                                                     Materials Characterization 131 (2017) 459–471




Fig. 11. An artifact generated in the image acquisition at a magniﬁcation of 25,000 × at position 7 is shown in the left-hand image. The artifact was removed by cropping the bottom of
the image, resulting in the right-hand image.




                                                                 Fig. 12. Eﬀect of removal of objects with one pixel.


    There are two interesting observations to be made by comparing                             out the eﬀect of bubble-channel alignment. Additionally, in other high
these images with the results shown in Fig. 12. First, the average or-                         magniﬁcation images, single directional channels are not present. The
ientation of the bubbles appears to directly correlate to the orientation                      second observation is that the eccentricity of the bubbles in the image
channels of recrystallized matrix in which the bubbles reside. This is                         from position 5 is aﬀected by long, stretched bubbles occurring right at
uniquely observable due to one particular channel comprising the                               the edge of the intact matrix/grains within the recrystallized matrix.
majority of the areas of the images presented in Fig. 13. In lower                             While these bubbles appear in the image from position 6 as well, they
magniﬁcation images, many more channels are visible, acting to cancel                          are more prevalent in the image from position 5, acting to drive the


                                                                                         468
A.M. Casella et al.                                                                                                                      Materials Characterization 131 (2017) 459–471




Fig. 13. Original backscatter images for 20,000 × magniﬁcation at position 5 (left) and 25,000 × magniﬁcation at position 6 (right). Examples of the “long, stretched bubbles” along the
grain boundaries are pointed out by arrows. Additional bubbles can be observed by tracing the interface of the grain boundaries and recrystallized channels.


average bubble eccentricity value up.                                                           bubble in the image that is captured appropriately in the segmentation
    For the most part, the trends in the results presented in Fig. 9 are                        process that is indicated by the blue circle. The two large objects in the
expected. The number of objects in each image for a given position                              binary image generated by the artifacts are identiﬁed within the list of
decreased steadily as the magniﬁcation increased. This is the case when                         objects created by the segmentation project by their size. In order to
one-pixel objects are included and when they were neglected in the                              verify that the two largest objects are indeed those caused by the ar-
analyses. A similar trend, although less linear, is seen for the average                        tifacts they are plotted by themselves along with the full image with
object equivalent spherical diameter. The trend in the average object                           these two objects removed in Fig. 15. The results of removing these two
eccentricity is the inverse of that of the average equivalent spherical                         large objects from the object analysis process (the pixels assigned to
diameter. The trend in the average object orientation is not the same for                       these objects were simply converted from white to black, eﬀectively
the diﬀerent positions examined as are the trends for the other para-                           making them part of the background) are shown in Table 7. As can be
meters. Instead, the trend is that as the magniﬁcation increases, the                           seen, removal of these artifacts has little impact on the results. Larger
spread between the average orientation values for each position in-                             artifacts must be present in order to present a true issue.
creases.                                                                                            As the artifacts are shown to have minimal impact, there are two
    One observation that can be seen in the average equivalent spherical                        remaining causes in the larger than expected object sizes in the 2000 ×
diameter is that there is a large jump from 2000 × magniﬁcation to                              magniﬁcation images. There are some bubbles in the images in Fig. 14
5000 × magniﬁcation. Comparatively, this value ﬂattens out to a                                 that are well above the mean size; one is directly indicated by the blue
nearly constant value at all magniﬁcations between 5000× and                                    circle. However, as these are smaller than the objects created by the
25,000 ×, but with a consistent, small downward trend. This could be                            artifacts and not overly abundant, it is unlikely that their presence is the
caused by a much larger area being analyzed, allowing for more of the                           cause of the large average object values for the low magniﬁcation
rarer, exceptionally large objects to be captured, contributing to the                          images. It is most likely that the third and ﬁnal option is the culprit. The
larger size. Additionally, the presence of image artifacts can have                             fraction of pixels that are assigned to objects that are not actually part
greater eﬀects on lower magniﬁcation images (fewer pixels per object).                          of the objects (due to lack of resolution) causes this phenomenon. The
Another explanation is that if a portion of the object takes up a portion                       fact that the jump in size from 5000× to 2000× magniﬁcation is
of a pixel and the pixel is assigned to the object, more pixel space that is                    observed for all 5 positions supports this conclusion.
not actually part of the object can be assigned to the object when pixels                           The average eccentricity of the bubbles in each image, regardless of
represent larger spaces (as is the case for lower magniﬁcation images).                         position and magniﬁcation is fairly constant, especially when 1-pixel
These hypotheses can be investigated with the image analysis below,                             objects are neglected. It makes sense that the eccentricity increases the
which indicate that the third option is the most likely. One way to in-                         most for 2000× magniﬁcation images when one-pixel objects are ne-
vestigate this is to use “Area” instead of “Count” to determine object                          glected, as a one-pixel object has an eccentricity of zero, and the most
size in Mathematica, but this was not investigated here as the algorithm                        one-pixel objects occur in the 2000 × magniﬁcation images. The values
is not openly deﬁned and utilizing it goes against the primary objective                        of the orientation seem to vary greatly as a function of position and
of this investigation. The “Count” option counts the number of pixels                           magniﬁcation. This is likely an indication of a fairly random distribu-
assigned to the object after segmentation, while the “Area” option de-                          tion in bubble orientation. However, the average orientation does tend
termines the approximate area of the object, where each pixel area is                           to be fairly low in all cases, indicating either that not many elongated
weighted by its neighborhood conﬁguration [18]. A similar option is                             bubbles are situated in a vertical conﬁguration, or that just as many
available in MATLAB with “Area” counting the number of pixels asso-                             bubbles that are conﬁgured with a high orientation are conﬁgured with
ciated with an object and “bwarea” weighting diﬀerent patterns of                               a low orientation. The removal of the one-pixel objects from analysis
pixels diﬀerently [17].                                                                         causes the absolute value of average orientation to increase, as the
    In order to investigate the plausibility of each of these options, the                      orientation of a one-pixel object is zero.
2000 × magniﬁcation image at position 3 is examined in more detail in                               While the average values for parameters of interest are signiﬁcant as
Fig. 14. There are what appear to be two surface preparation artifacts                          presented above, additional information can be gleaned by observing
that lead to large objects in the segmentation of the image. These ar-                          data gained from the processing of segmented images in other formats
tifacts are indicated with red circles. Additionally, there is a truly large                    such as the log normal equivalent spherical diameter distributions


                                                                                          469
A.M. Casella et al.                                                                                                                           Materials Characterization 131 (2017) 459–471




Fig. 14. Comparison of raw and segmented binary image for 2000 × at Position 3. Highlighted in red are artifacts that show up as large bubbles as a result of the image processing
procedure. Highlighted in blue is an example of a legitimately large bubble. (For interpretation of the references to colour in this ﬁgure legend, the reader is referred to the web version of
this article.)


presented in Fig. 10. As mentioned previously, these analyses require                              Table 7
further analyst action which the eﬀort described in this paper strove to                           Characterization of bubble distributions with (in italics) and without inclusion of arti-
                                                                                                   facts.
minimize. In order to ﬁt data to a distribution, it is ﬁrst necessary to
place the values acquired from the image into size bins as discussed in                                             Number of      Object        Object       Eccentricity   Orientation (°)
the previous section. The selection of the size of the bin can aﬀect the                                            objects        size          size
ﬁtting parameters associated with the ﬁnal associated distribution. For                                                            (pixels)      (μm2)
the distributions presented in Fig. 10, bins with widths of 0.1 μm were
                                                                                                     Position 3,    9324           6.650         0.140        0.756          − 11.235
used. This bin sizing for distribution determination was not automated,                                  2000×      9322           6.595         0.139        0.756          − 11.249
but was kept consistent for the present analysis. Further investigation
into an automated determination of optimal bin sizing is suggested for
further work. Additionally, it should be noted that in the current work,                           current work was to provide a simple baseline approach to ﬁssion gas
no consideration was given to correlating the results gathered from the                            bubble analysis that could serve as a launching pad for such further
two-dimensional analysis to the three-dimensional properties of the                                development.
samples that were investigated. These two endeavors: optimal binning
and mapping from two-dimensional characterization to three-dimen-
                                                                                                   5. Conclusions
sional characterization are of great interest and impact and insights can
be gathered from existing literature [20–22]. The objective of the
                                                                                                       This paper presents a proposed baseline method with minimal




                                                                 Fig. 15. Visual demonstration of removal of two artifacts.


                                                                                             470
A.M. Casella et al.                                                                                                            Materials Characterization 131 (2017) 459–471


analyst intervention for providing analysis of ﬁssion gas bubbles in ir-            review of the manuscript and helpful discussion. The authors would like
radiated U-Mo fuels. The full method involves sample preparation and                to acknowledge Mr. Jason Schulthess, Mr. Adam Robinson, Dr. Barry
analysis, and it is understood that it may be divided along these lines for         Rabin, and Mrs. Susan Case from Idaho National Laboratory for the
implementation as preparation of smaller samples with focused ion                   preparation and delivery of the irradiated fuel segments. The authors
beams allows for limitations of dose to analysts. However, the authors              would like to acknowledge those at Paciﬁc Northwest National
do point out that the samples prepared with mechanical methods pre-                 Laboratory who were involved in the preparation of samples and per-
sented here do not exhibit the curtaining eﬀects that cause a great eﬀort           formance of measurements, speciﬁcally Jamin Trevino. Finally, the
in pre-analysis ﬁltering discussed previously in the literature. The                authors would like to acknowledge the sponsor, the National Nuclear
preparation of non-dispersable, polished samples encased in epoxy al-               Security Administration's Oﬃce of Material Management and
lows for removal of samples from hot cells where they can be handled                Minimization Reactor Conversion Program, for the opportunity to
with shielding and extension tools. These samples do not exhibit cur-               conduct this work under contract DE-AC05-76RL01830.
taining eﬀects and can be immediately subjected to the analysis
methods presented here.                                                             References
    Three software packages were examined for sample analysis in the
paper. It was determined that the methods of MATLAB and                              [1] J.L. Snelgrove, G.L. Hofman, M.K. Meyer, C.L. Trybus, T.C. Wiencek, Development
Mathematica were well aligned, while those of CellProﬁler varied                         of very-high-density low-enriched-uranium fuels, Nucl. Eng. Des. 178 (1997)
                                                                                         119–126.
somewhat. It is likely that this deviation can be corrected if suﬃciently            [2] D.B. Lee, K.H. Kim, C.K. Kim, Thermal compatibility studies of unirradiated U-Mo
investigated. However, as the purpose of this work was to determine a                    alloys dispersed in aluminum, J. Nucl. Mater. 250 (1997) 79–82.
baseline pathway of sample analysis that minimizes analyst interven-                 [3] M.K. Meyer, G.L. Hofman, S.L. Hayes, C.R. Clark, T.C. Wiencek, J.L. Snelgrove,
                                                                                         R.V. Strain, K.H. Kim, Low-temperature irradiation behavior of uranium-mo-
tion, it is concluded that MATLAB or Mathematica provide a more di-                      lybdenum alloy dispersion fuel, J. Nucl. Mater. 304 (2002) 221–236.
rect pathway to that end. The standard image analysis tool sets avail-               [4] J.M. Park, K.H. Kim, C.K. Kim, M.K. Meyer, G.L. Hofman, R.V. Strain, The irra-
able in each of these software packages allows for rapid analysis with                   diation behavior of atomized U-Mo alloy fuels at high temperature, Met. Mater. Int.
                                                                                         7 (2) (2001) 151–157.
no modiﬁcation of the automatic values set within them. The conver-                  [5] G.A. Moore, M.C. Marshall, Co-rolled U10Mo/Zirconium-barrier-layer Monolithic
sion of results from units associated with pixels to physical parameters                 Fuel Foil Fabrication Process. INL/EXT-10-17774, Idaho National Laboratory, Idaho
such as equivalent spherical diameter introduces steps that could po-                    Falls, Idaho, 2010.
                                                                                     [6] B.H. Park, C.R. Clark, J.F. Jue, INL HIP Plate Fabrication. INL/EXT-10-17792, Idaho
tentially contain errors, but analyst involvement is minimal. The ﬁtting
                                                                                         National Laboratory, Idaho Falls, Idaho, 2010.
of these parameters to distributions, such as the log normal distribu-               [7] D.M. Perez, M.A. Lillo, G.S. Chang, G.A. Roth, N.E. Woolstenhulme, D.M. Wachs,
tions presented here for bubble size distribution introduces a somewhat                  AFIP-3 Irradiation Summary Report. INL/EXT-11-21776, Rev. 2, Idaho National
subjective decision on the part of the analyst to determine the size of                  Laboratory, Idaho Falls, Idaho, 2012.
                                                                                     [8] D.E. Burkes, A.M. Casella, E.C. Buck, A.J. Casella, M.K. Edwards, P.J. MacFarlan,
the bins used for distribution ﬁtting. It is recommended that such bin                   K.N. Pool, B.D. Slonecker, F.N. Smith, F.H. Steen, Fuel Thermo-physical
sizes be reported with any analysis so that work can be reproduced by                    Characterization Project: Fiscal Year 2014 Final Report, PNNL-24135, Paciﬁc
other researchers.                                                                       Northwest National Laboratory, Richland, Washington, 2015.
                                                                                     [9] D.E. Burkes, A.M. Casella, A.J. Casella, E.C. Buck, K.N. Pool, P.J. MacFarlan,
    It is important, as discussed in this paper, that analysts carefully                 M.K. Edwards, F.N. Smith, Thermal properties of U-Mo alloys irradiated to mod-
consider and investigate the methods used by the software package of                     erate burnup and power, J. Nucl. Mater. 464 (2015) 331–341.
choice to ensure that the resulting values from analysis carry the pre-             [10] D.E. Burkes, A.J. Casella, A.M. Casella, W.G. Luscher, F.J. Rice, K.N. Pool,
                                                                                         Measurement of ﬁssion gas release from irradiated U-Mo monolithic fuel samples, J.
scribed meaning. For instance, while all software packages discussed in                  Nucl. Mater. 461 (2015) 61–71.
this paper deﬁned eccentricity and orientation in the same way, the                 [11] S. Hu, A.M. Casella, C.A. Lavender, D.J. Senor, D.E. Burkes, Assessment of eﬀective
values they generated diﬀered somewhat. The simple tests presented                       thermal conductivity in U-Mo metallic fuels with distributed gas bubbles, J. Nucl.
                                                                                         Mater. 462 (2015) 64–76.
here allowed for determining the meaning of the results. However, even              [12] R. Collette, J. Douglas, L. Patterson, G. Bahun, J. King, D. Keiser Jr., J. Schulthess,
though the values are well understood, it is not clear that they are the                 Beneﬁts of utilizing CellProﬁler as a characterization tool for U-10Mo nuclear fuel,
most appropriate results. For example, the ﬁnal method of determining                    Mater. Charact. 105 (2015) 71–81.
                                                                                    [13] R. Collette, J. King, D. Keiser Jr., B. Miller, J. Madden, J. Schulthess, Fission gas
orientation presented here uses a value of − 90° for the orientation of
                                                                                         bubble identiﬁcation using MATLAB's image processing toolbox, Mater. Charact.
all bubbles whose equivalent ellipse is vertically oriented. Perhaps as-                 118 (2016) 284–293.
signing these bubbles an orientation of 0° would be more appropriate as             [14] A.M. Casella, D.E. Burkes, P.J. MacFarlan, E.C. Buck, J.A. Trevino, Fuel Thermo-
it would average out those with an orientation of 90° and those with an                  physical Characterization Project: SEM Characterization of Irradiated Monolithic U-
                                                                                         Mo Fuel, PNNL-26231, (2016).
orientation of −90°. Still, the current analysis does present results that          [15] D.E. Burkes, A.M. Casella, E.C. Buck, A.J. Casella, M.K. Edwards, P.J. MacFarlan,
are useful for physical interpretation as evidenced through Fig. 13.                     K.N. Pool, F.N. Smith, F.H. Steen, Development and validation of capabilities to
    While the authors feel that the work presented in this paper pro-                    measure thermal properties of layered monolithic U-Mo alloy plate-type fuel, Int. J.
                                                                                         Thermophys. 35 (2014) 1476–1500.
vides a useful and valid proposal for baseline analysis of ﬁssion gas               [16] A.E. Carpenter, T.R. Jones, CellProﬁler: cell image analysis software manual.
bubbles in irradiated U-Mo fuels, it is acknowledged that no such                        http://cellproﬁler.org/manuals/, (2014).
method will ever be truly devoid of analyst intervention and inter-                 [17] MathWorks, Inc., MATLAB and Image Processing Toolbox Release, (2016) (Natick,
                                                                                         Massachusetts, February 2016).
pretation. The method does make it clearer to locate image artifacts and            [18] Wolfram Research, Inc., Mathematica, Version 9.0 (Champaign, IL), (2012).
process images. The results from this image processing will ultimately              [19] N. Otsu, A threshold selection method from gray-level histograms, IEEE Trans. Syst.
have to be reviewed carefully for ﬁnal interpretation. However, ad-                      Man Cybern. 9 (1979) 62–66.
                                                                                    [20] F. Cappia, D. Pizzocri, A. Schubert, P. Van Uﬀelen, G. Paperini, D. Pellottiero,
hering to a well-deﬁned baseline method that minimizes subjective
                                                                                         R. Macián-Juan, V.V. Rondinella, Critical assessment of the pore size distribution in
analyst interpretation prior to additional presentation of analyst inter-                the rim region of high burnup UO2 fuels, J. Nucl. Mater. 480 (2016) 138–149.
pretation would provide a useful calibration for these results among the            [21] J. Takahashi, H. Suito, Evaluation of the accuracy of the three-dimensional size
                                                                                         distribution estimated from the Schwartz-Saltykov method, Metall. Mater. Trans. A
various groups currently working in this ﬁeld.
                                                                                         34 (2003) 171–181.
                                                                                    [22] Y.-H. Xu, H.C. Pitot, An improved stereologic method for three-dimensional esti-
Acknowledgements                                                                         mation of particle size distribution from observations in two dimensions and its
                                                                                         application, Comput. Methods Prog. Biomed. 72 (2003) 1–20.

    The authors would like to acknowledge Dr. Amanda Casella for her




                                                                              471
