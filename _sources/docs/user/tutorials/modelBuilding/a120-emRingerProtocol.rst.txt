.. _`app:emRingerProtocol`:

Phenix EMRinger protocol
========================

Protocol designed to assess the geometry of refined atomic structures
regarding electron density maps in *Scipion* by using :math:`EMRinger` :cite:p:`barad2015`. Integrated in cryo-EM validation tools of `PHENIX software suite <https://www.phenix-online.org/>`_ and
created as an extension of the X-ray crystallography validation tool
:math:`Ringer`, :math:`EMRinger` tool computes the amount of rotameric
angles of the structure side chains as a function of map value to assess
the goodness of the fitting to the cryo-EM density map.

-  | Requirements to run this protocol and visualize results:

   -  | *Scipion* plugin: **scipion-em**

   -  | *Scipion* plugin: **scipion-em-phenix**

   -  | **PHENIX software suite** (tested for versions 1.13-2998, 1.16-3549, 1.17.1-3660 and 1.18.2-3874)

   -  | *Scipion* plugin: **scipion-em-chimera**
   
-  | *Scipion* menu: *Model building -> Validation* (:numref:`model_building_app_protocol_emringer_1` (A))

   .. figure:: Images_appendix/Fig139.svg
      :alt: Protocol **phenix-emringer**. A: Protocol location in *Scipion* menu. B: Protocol form.
      :name: model_building_app_protocol_emringer_1
      :align: center
      :width: 90.0%

      Protocol **phenix-emringer**. A: Protocol location in *Scipion* menu. B: Protocol form.

-  Protocol form parameters (:numref:`model_building_app_protocol_emringer_1` (B)):

   -  | *Input Volume*: Electron density map previously downloaded or generated in *Scipion*.

   -  | *Input atomic structure*: Atomic structure previously downloaded or generated in *Scipion* and fitted to the input electron density map.

-  Protocol execution:

   | Adding specific map/structure label is recommended in *Run name*
     section, at the form top. To add the label, open the protocol form,
     press the pencil symbol on the right side of *Run name* box,
     complete the label in the new opened window, press OK and, finally,
     close the protocol. This label will be shown in the output summary
     content (see below). If you want to run again this protocol, do not
     forget to set to *Restart* the *Run mode*.

   | Press the *Execute* red button at the form bottom.

-  Visualization of protocol results:

   After executing the protocol, press *Analyze Results* and the results
   window will be opened (:numref:`model_building_app_protocol_emringer_2`).

   .. figure:: Images_appendix/Fig140.svg
      :alt: Protocol **phenix-emringer**. Taps to visualize Volume and models and :math:`EMRinger` results.
      :name: model_building_app_protocol_emringer_2
      :align: center
      :width: 50.0%

      Protocol **phenix-emringer**. Taps to visualize Volume and models and :math:`EMRinger` results.

   Two taps are shown in the upper part of the results window:

   -  | *Volume and models*: *ChimeraX* graphics window will be opened by default. Atomic structure and volume are referred to the origin of coordinates in *ChimeraX*. To show the relative position of atomic structure and electron density volume, the three coordinate axes are represented; X axis (red), Y axis (yellow), and Z axis (blue) (:numref:`model_building_app_protocol_volume_3`).

   -  | *EMRinger Results* (:numref:`model_building_app_protocol_emringer_3`):

      .. figure:: Images_appendix/Fig141.svg
         :alt: Protocol **phenix-emringer**. Menu to visualize :math:`EMRinger` results.
         :name: model_building_app_protocol_emringer_3
         :align: center
         :width: 50.0%

         Protocol **phenix-emringer**. Menu to visualize :math:`EMRinger` results.

      -  | *Summary Table of Results* (:numref:`model_building_app_protocol_emringer_4`):

         .. figure:: Images_appendix/Fig142.svg
            :alt: Protocol **phenix-emringer**. Final :math:`EMRinger` results.
            :name: model_building_app_protocol_emringer_4
            :align: center
            :width: 40.0%

            Protocol **phenix-emringer**. Final :math:`EMRinger` results.

         -  | *Optimal Threshold*: *Electron Potential* cutoff value of the volume, in a range of 20, at which maximum values of *EMRinger Score* and *Percentage of Rotameric Residues* are reached.

         -  | *Rotamer-Ratio*: *Percentage of Rotameric Residues* at the *Optimal Threshold*.

         -  | *Max Zscore*: Z-score indicating the significance of the distribution at the *Optimal Threshold*; in other words, probability of finding a certain number of rotameric residues at a specific side chain dihedral angle, among the total number of map peaks found above the *Optimal Threshold*, assuming a binomial distribution of rotameric residues B(*n, p)* (:math:`n`: total number of map peaks found above the *Optimal Threshold*; :math:`p`: 39/72; with map sampling every 5º, 39 angle binds are considered rotameric from a total of 360/5 = 72).

         -  | *Model Length*: Total number of residues of the model considered in EMRinger computation, non-:math:`\gamma`-branched, non-proline aminoacids with a non-H :math:`\gamma` atom.

         -  | *EMRinger Score*: Highest Z-score, rescaled regarding model length, across the range of *Electron Potential* thresholds. Since the Z-score is rescaled to the *EMRinger Score* according model length, *EMRinger Score* allows suitable comparisons among different model-map pairs. *EMRinger Score* of 1.0 is usual for initial models refined regarding 3.2-3.5Å resolution maps. For high-quality models with high resolution, *EMRinger Score* values higher than 2 are expected.

      -  | *Threshold Scan*: Plots of *EMRinger Score* (blue line) and *Percentage of Rotameric Residues* (red line) regarding the *Electron Potential* threshold. The maximum value of *EMRinger Score* stablishes the *Optimal Threshold*.

      -  | *Density threshold*: Box to select one of the 20 volume density cutoff values at which the *Percentage of Rotameric Residues* has been computed. The *Optimal Threshold*, at which the *EMRinger Score* was obtained, is shown by default.

      -  | *Peak count for the selected density threshold*: Histograms counting rotameric (blue) and non-rotameric (red) residues at the selected *Electron Potential Threshold*.

      -  | *Chain*: Box to select one of the chains of the model. By default, the name of the first chain is shown.

      -  | *Rolling window for the selected chain*: The analysis of EMRinger rolling window, performed on rolling sliding 21-residue windows along the primary sequence of monomers, allows to distinguish high quality regions of the model.

      -  | *Residue*: Box to select one residue, with at least one *Chi* angle (non-H :math:`\gamma` atom-containing), located in the specific position indicated in the primary sequence of one of the monomer chains indicated.

      -  | *Ringer results for the selected residue*: Individual plots for each *Chi* angle of the selected residue. Detailed numeric values are shown in the *extra/*.csv* file.

-  Summary content:

   | *SUMMARY* box:
   | Statistics included in the above *Summary Table of Results* (an
     example can be observed in :numref:`model_building_emringer_protocol` (6).
