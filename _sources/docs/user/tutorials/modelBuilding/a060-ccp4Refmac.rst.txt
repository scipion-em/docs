.. _`app:ccp4Refmac`:

CCP4 Refmac protocol
====================

| Protocol designed to refine atomic structures, in reciprocal space,
  regarding electron density maps in by using *Refmac* :cite:p:`vagin2004`, :cite:p:`kovalevskiy2018`.
  This protocol integrates *Refmac* functionality in *Scipion*, supporting accession to *Refmac* input and output data in the general model building workflow.
| *Refmac*, Refinement of Macromolecular Structures by the Maximum-Likelihood
  method, allows the refinement of atomic models against experimental
  data, and is integrated in CCP4 software suite
  (`CCP4 <https://www.ccp4.ac.uk/?page_id=878>`_).
  Initially applicable to X-ray data, some modifications of *Refmac* also support
  optimal fitting of atomic structures into electron density maps
  obtained from cryo-EM :cite:p:`brown2015`. Particullarly, *Refmac*
  considers a five-Gaussian approximation for electron scatttering
  factors because, unlike X-ray crystallography, cryo-EM scattering
  is modified by each atom electric charge and ionization state. In
  addition, *Refmac* computes structure factors only for the model-explained part
  of the map. These structure factors are complex because they include,
  not only amplitude data, but also phase information. *Refmac* will try to
  minimize the difference between the “observed” and calculated
  structure factors, computed from cryo-EM maps and from atom
  coordinates (structure), respectively. Additional instructions to use
  can be found in `REFMAC <http://www.ysbl.york.ac.uk/refmac/>`_.

-  Requirements to run this protocol and visualize results:

   -  *Scipion* plugin: **scipion-em**

   -  *Scipion* plugin: **scipion-em-ccp4**

   -  CCP4 software suite (from version 7.0.056 to 7.1)

   -  *Scipion* plugin: **scipion-em-chimera**

-  *Scipion* menu: *Model building -> Flexible fitting* (:numref:`model_building_app_protocol_refmac_1` (A))

-  Protocol form parameters (:numref:`model_building_app_protocol_refmac_1` (B)):

   .. figure:: Images_appendix/Fig126.svg
      :alt: Protocol **ccp4-refmac**. A: Protocol location in *Scipion* menu. B: Protocol form.
      :name: model_building_app_protocol_refmac_1
      :align: center
      :width: 90.0%

      Protocol **ccp4-refmac**. A: Protocol location in *Scipion* menu. B: Protocol form.

   -  *Input Volume*: An electron density map previously downloaded or
      generated in *Scipion*. An atomic structure should be refined regarding to
      this volume.

   -  *Atomic structure to be refined*: Atomic structure previously
      downloaded or generated in *Scipion*. This structure will be refined
      according to the electron density volume.

   -  *Max. Resolution (Å)*: Upper limit of resolution used for
      refinement, in Angstroms. Using double value of sampling rate is
      recommendable.

   -  *Min. Resolution (Å)*: Lower limit of resolution used for
      refinement, in Angstroms.

   -  *Generate masked volume*: Parameter set to “Yes” by default. With
      this option, structure factors will be computed for the map around
      model atomic structure. Otherwise (option “No”), structure factors
      will be computed for the whole map.

   -  *SFCALC mapradius*: Advanced parameter that indicates how much
      around the model atomic structure should be cut. 3Å is the default
      value.

   -  *SFCALC mradius*: Radius to compute the mask around the model
      atomic structure. 3Å is the default value.

   -  *Number of refinement iterations*: Cycles of refinement. 30 cycles
      is the default value.

   -  *Matrix refinement weight*: Weight parameter between electron
      density map (experimental data) and model atomic structure
      geometry. Increase this value if you want to give more weight to
      experimental data. If the value is set to 0.0, bond root mean
      square deviation from optimal values will be between 0.015 and
      0.025.

   -  *B factor*: Geometrical restriction applied to bonded and
      nonbonded atom pairs. This B factor value set the initial B
      values.

   -  *Extra parameters*: This parameter gives the opportunity to add
      some extra parameters. Use “:math:`|`” to separate the next
      parameter from the previous one.

-  Protocol execution:

   | Adding specific map/structure label is recommended in *Run name*
     section, at the form top. To add the label, open the protocol form,
     press the pencil symbol at the right side of *Run name* box,
     complete the label in the new opened window, press OK and, finally,
     close the protocol. This label will be shown in the output summary
     content (see below). If you want to run again this protocol, do not
     forget to set to *Restart* the *Run mode*.

   | Press the *Execute* red button at the form bottom.

-  Visualization of protocol results:

   After executing the protocol, press *Analyze Results* and a window
   panel will be opened (:numref:`model_building_app_protocol_refmac_2`). Results can be visualized by selecting each
   menu element.

   .. figure:: Images_appendix/Fig127.svg
      :alt: Protocol **ccp4-refmac**. Menu to visualize *Refmac* results.
      :name: model_building_app_protocol_refmac_2
      :align: center
      :width: 50.0%

      Protocol **ccp4-refmac**. Menu to visualize *Refmac* results.

   Options to visualize results:

   -  Volume and models: *ChimeraX* graphics window displays coordinate axes,
      selected input volume, starting atomic structure generated by *Coot*,
      and final *Refmac* refined structure (:numref:`model_building_app_protocol_refmac_3`).

      .. figure:: Images_appendix/Fig128.svg
         :alt: Protocol **ccp4-refmac**. Map and models visualized with *ChimeraX*.
         :name: model_building_app_protocol_refmac_3
         :align: center
         :width: 80.0%

         Protocol **ccp4-refmac**. Map and models visualized with *ChimeraX*.

   -  Display Mask: *ChimeraX* graphics window displays the mask generated around
      the model atomic structure that has to be refined (:numref:`model_building_app_protocol_refmac_4`).

      .. figure:: Images_appendix/Fig129.svg
         :alt: Protocol **ccp4-refmac**. Mask visualized with *ChimeraX*.
         :name: model_building_app_protocol_refmac_4
         :align: center
         :width: 80.0%

         Protocol **ccp4-refmac**. Mask visualized with *ChimeraX*.

   -  Final Results Table: Table showing the basic statistics of *Refmac*
      results. Comparison between initial and final refinement values
      allows to follow the refinement process. Lower final values than
      initial ones indicate that discrepancy indices between
      experimental data and ideal values are disminishing with
      refinement, which is desirable. R factor and Rms BondLength fair
      values should be around 0.3 and 0.02, respectively (:numref:`model_building_app_protocol_refmac_5`).

      .. figure:: Images_appendix/Fig130.svg
         :alt: Protocol **ccp4-refmac**. *Refmac* final results table.
         :name: model_building_app_protocol_refmac_5
         :align: center
         :width: 40.0%

         Protocol **ccp4-refmac**. *Refmac* final results table.

   -  Show log file: *Refmac*-generated text file containing statistics of every
      running cycle (:numref:`model_building_app_protocol_refmac_6`).

      .. figure:: Images_appendix/Fig131.svg
         :alt: Protocol **ccp4-refmac**. *Refmac* raw log file.
         :name: model_building_app_protocol_refmac_6
         :align: center
         :width: 80.0%

         Protocol **ccp4-refmac**. *Refmac* raw log file.

   -  Results Table (last iteration) (:numref:`model_building_app_protocol_refmac_7`):

      .. figure:: Images_appendix/Fig132.svg
         :alt: Protocol **ccp4-refmac**. *Refmac* last iteration results table.
         :name: model_building_app_protocol_refmac_7
         :align: center
         :width: 45.0%

         Protocol **ccp4-refmac**. *Refmac* last iteration results table.

      -  Resolution limits: 0.0 and the resolution value provided as
         input.

      -  Number of used reflections: Each reflection is defined as the
         common direction that the scattered waves follow, considering
         all the atoms included in a crystallographic unit cell. A
         structure factor will be computed for this common direction.
         The number of reflections is thus identical to the number of
         structure factors.

      -  Percentage observed: Percentage of observed reflections.

      -  Percentage of free reflections: Percentage of reflections
         observed and not included in the refinement process. These
         reflections are used to compute the *R factor free*.

      -  | Overall *R factor*: Fraction of total differences between
           observed and computed amplitudes of structure factors,
           previously scaled, regarding total observed amplitudes of
           structure factors.
     
           .. math::

                   R factor = \frac{\sum||F_o|-|F_c||}{\sum|F_o|} 
                
         | where :math:`|F_o|` is the observed amplitude of the
           structure factor and :math:`|F_c|` is the calculated
           amplitude of the structure factor.

      -  Average Fourier shell correlation: :math:`FSC`, cross-correlation
         between shells of two 3D volumes in Fourier space, calculated
         using complex Fourier coefficients, divided by the number of
         structure factors in a particular frequency (resolution) shell.
         :math:`FSC_{average}` has the advantage over :math:`FSC` of being
         independent on weight (related with inverse variances of
         cryo-EM density maps) whenever resolution shells are thin
         enough that the number of structure factors in each shell is
         almost equal :cite:p:`brown2015`.

      -  | Overall weighted *R factor*: Overall *R factor* that applies
           a weight factor to differences between observed and computed
           amplitudes of structure factors, and also applies that weight
           factor to the observed amplitudes of structure factors. As in
           the :math:`FSC_{average}`, the weight is related with inverse
           variances of cryo-EM density maps.

           .. math::

                   weighted R factor = \frac{\sum(w |F_o|-|F_c|)}{\sum(w |F_o|)}
                
         | where :math:`w` is the weight factor.

      -  | Overall weighted *R2 factor*: Also known as generalised *R
           factor*, this factor is computed as the root square of the
           fraction of total squares of weighted differences between
           observed and computed amplitudes of structure factors,
           previously scaled, regarding the total of weighted squares of
           observed amplitudes of structure factors.

           .. math::

                   weighted R^2 factor = \frac{\sum(w (|F_o|-|F_c|)^2)}{\sum(w (|F_o|)^2)}

      -  Average correlation coefficient:

      -  Overall correlation coefficient: Correlation between observed
         and calculated structure factor amplitudes, taking into account
         only reflections included in the refinement process.

      -  Cruickshank’s *DPI* for coordinate error: Diffraction precision
         index, useful to estimate atomic placement precision. This
         factor is a function of the number of atoms and reflections
         included in the refinement, of the overall *R factor*, of the
         maximum resolutions of reflections included in the refinement,
         as well as the completeness of the observed data.

      -  Overall figure of merit: :math:`Cosine` of the error of phases
         in radians; 1 indicates no error.

      -  *ML* based su of positional parameters: Comprehensive standard
         uncertainties of positional parameters based on the maximum
         likelihood function.

      -  *ML* based su of thermal parameters: Comprehensive standard
         uncertainties of thermal parameters (B values) based on the
         maximum likelihood function.

   -  *R factor* vs. iteration: Plot to visualize *R factor* and *R
      factor free* regarding iterations (:numref:`model_building_app_protocol_refmac_8`):

      .. figure:: Images_appendix/Fig133.svg
         :alt: Protocol **ccp4-refmac**. *R factor* vs. cycle plot.
         :name: model_building_app_protocol_refmac_8
         :align: center
         :width: 50.0%

         Protocol **ccp4-refmac**. *R factor* vs. cycle plot.

   -  *FOM* vs. iteration: Plot to visualize Figure Of Merit regarding
      iterations (:numref:`model_building_app_protocol_refmac_9`):

      .. figure:: Images_appendix/Fig134.svg
         :alt: Protocol **ccp4-refmac**. *Figure Of Merit* vs. cycle plot.
         :name: model_building_app_protocol_refmac_9
         :align: center
         :width: 50.0%

         Protocol **ccp4-refmac**. *Figure Of Merit* vs. cycle plot.

   -  *-LL* vs. iteration: Plot to visualize the log(Likelihood)
      regarding iterations. Likelihood indicates the probability of a
      refined model, given the specific observed data (:numref:`model_building_app_protocol_refmac_10`):

      .. figure:: Images_appendix/Fig135.svg
         :alt: Protocol **ccp4-refmac**. log(Likelihood) vs. cycle plot.
         :name: model_building_app_protocol_refmac_10
         :align: center
         :width: 50.0%

         Protocol **ccp4-refmac**. log(Likelihood) vs. cycle plot.

   -  *-LLfree* vs. iteration: Same definition as -LL vs. iteration,
      although considering only “free” reflections not included in
      refinement (:numref:`model_building_app_protocol_refmac_11`):

      .. figure:: Images_appendix/Fig136.svg
         :alt: Protocol **ccp4-refmac**. log(Likelihood) for “free“ reflections vs. cycle plot.
         :name: model_building_app_protocol_refmac_11
         :align: center
         :width: 50.0%

         Protocol **ccp4-refmac**. log(Likelihood) for “free“ reflections vs. cycle plot.

   -  Geometry vs. iteration: Plot to visualize geometry parameter
      statistics regarding iterations (:numref:`model_building_app_protocol_refmac_12`):

      .. figure:: Images_appendix/Fig137.svg
         :alt: Protocol **ccp4-refmac**. Geometry parameter statistics vs. cycle plot.
         :name: model_building_app_protocol_refmac_12
         :align: center
         :width: 50.0%

         Protocol **ccp4-refmac**. Geometry parameter statistics vs. cycle plot.

      -  *rmsBOND*: Root mean square of structure atom covalent bond
         lengths, computed in Å, regarding ideal values of bond lengths.
         Selecting default weighting, *rmsBOND* values will be around 0.02.

      -  *zBOND*: Number of standard deviations from the mean of
         covalent bond lengths. Selecting default weighting, *zBOND*
         values will be between 0.2 and 1.0.

      -  *rmsANGL*: Root mean square of bond angles from refined
         structure, computed in degrees, regarding their ideal values.
         *rmsANGL* values should converge around 0.1.

      -  *zANGL*: Number of standard deviations from the mean of bond
         angles.

      -  *rmsCHIRAL*: Root mean square of chiral volumes from refined
         structure regarding their ideal values. Chiral volumes are
         determined by four atoms that form a piramid, and may show
         positive or negative values.

-  Summary content:

   -  | Protocol output (below *Scipion* framework):
      | *ccp4 - refmac -> ouputPdb*;
      | *PdbFile(pseudoatoms=True/ False, volume=True/ False)*.
      | Pseudoatoms is set to *True* when the structure is made of
        pseudoatoms instead of atoms. Volume is set to *True* when an
        electron density map is associated to the atomic structure.

   -  | *SUMMARY* box:
      | Statistics included in the above Final Results Table (:numref:`model_building_app_protocol_refmac_13`):

      .. figure:: Images_appendix/Fig138.svg
         :alt: Protocol **ccp4-refmac**. Summary.
         :name: model_building_app_protocol_refmac_13
         :align: center
         :width: 80.0%

         Protocol **ccp4-refmac**. Summary.


