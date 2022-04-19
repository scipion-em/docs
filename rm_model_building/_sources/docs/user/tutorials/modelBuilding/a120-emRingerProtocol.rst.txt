.. _`app:emRingerProtocol`:

Phenix EMRinger protocol
========================

Protocol designed to assess the geometry of refined atomic structures
regarding electron density maps in by using :math:`EMRinger`
:raw-latex:`\citep{barad2015}`. Integrated in cryo-EM validation tools
of :math:`Phenix` software suite (https://www.phenix-online.org/) and
created as an extension of the X-ray crystallography validation tool
:math:`Ringer`, :math:`EMRinger` tool computes the amount of rotameric
angles of the structure side chains as a function of map value to assess
the goodness of the fitting to the cryo-EM density map.

-  Requirements to run this protocol and visualize results:

   -  plugin:

   -  plugin:

   -  PHENIX software suite (tested for versions 1.13-2998, 1.16-3549,
      1.17.1-3660 and 1.18.2-3874)

   -  plugin:

-  menu: ( (A))

-  Protocol form parameters ( (B)):

   .. figure:: Images_appendix/Fig139.pdf
      :alt: Protocol . A: Protocol location in menu. B: Protocol form.
      :name: fig:app_protocol_emringer_1
      :width: 90.0%

      Protocol . A: Protocol location in menu. B: Protocol form.

   -  : Electron density map previously downloaded or generated in .

   -  : Atomic structure previously downloaded or generated in and
      fitted to the input electron density map.

-  Protocol execution:

   | Adding specific map/structure label is recommended in section, at
     the form top. To add the label, open the protocol form, press the
     pencil symbol on the right side of box, complete the label in the
     new opened window, press OK and, finally, close the protocol. This
     label will be shown in the output summary content (see below). If
     you want to run again this protocol, do not forget to set to the .
   | Press the red button at the form bottom.

-  Visualization of protocol results:

   After executing the protocol, press and the results window will be
   opened ().

   .. figure:: Images_appendix/Fig140.pdf
      :alt: Protocol . Taps to visualize Volume and models and
      :math:`EMRinger` results.
      :name: fig:app_protocol_emringer_2
      :width: 50.0%

      Protocol . Taps to visualize Volume and models and
      :math:`EMRinger` results.

   Two taps are shown in the upper part of the results window:

   -  : graphics window will be opened by default. Atomic structure and
      volume are referred to the origin of coordinates in . To show the
      relative position of atomic structure and electron density volume,
      the three coordinate axes are represented; X axis (red), Y axis
      (yellow), and Z axis (blue) ().

   -  ():

      .. figure:: Images_appendix/Fig141.pdf
         :alt: Protocol . Menu to visualize :math:`EMRinger` results.
         :name: fig:app_protocol_emringer_3
         :width: 50.0%

         Protocol . Menu to visualize :math:`EMRinger` results.

      -  ():

         .. figure:: Images_appendix/Fig142.pdf
            :alt: Protocol . Final :math:`EMRinger` results.
            :name: fig:app_protocol_emringer_4
            :width: 40.0%

            Protocol . Final :math:`EMRinger` results.

         -  : cutoff value of the volume, in a range of 20, at which
            maximum values of and are reached.

         -  : at the .

         -  : Z-score indicating the significance of the distribution at
            the ; in other words, probability of finding a certain
            number of rotameric residues at a specific side chain
            dihedral angle, among the total number of map peaks found
            above the , assuming a binomial distribution of rotameric
            residues B( (:math:`n`: total number of map peaks found
            above the ; :math:`p`: 39/72; with map sampling every 5º, 39
            angle binds are considered rotameric from a total of 360/5 =
            72).

         -  : Total number of residues of the model considered in
            EMRinger computation, non-:math:`\gamma`-branched,
            non-proline aminoacids with a non-H :math:`\gamma` atom.

         -  : Highest Z-score, rescaled regarding model length, across
            the range of thresholds. Since the Z-score is rescaled to
            the according model length, allows suitable comparisons
            among different model-map pairs. of 1.0 is usual for initial
            models refined regarding 3.2-3.5Å resolution maps. For
            high-quality models with high resolution, values higher than
            2 are expected.

      -  : Plots of (blue line) and (red line) regarding the threshold.
         The maximum value of stablishes the .

      -  : Box to select one of the 20 volume density cutoff values at
         which the has been computed. The , at which the was obtained,
         is shown by default.

      -  : Histograms counting rotameric (blue) and non-rotameric (red)
         residues at the selected .

      -  : Box to select one of the chains of the model. By default, the
         name of the first chain is shown.

      -  : The analysis of EMRinger rolling window, performed on rolling
         sliding 21-residue windows along the primary sequence of
         monomers, allows to distinguish high quality regions of the
         model.

      -  : Box to select one residue, with at least one angle (non-H
         :math:`\gamma` atom-containing), located in the specific
         position indicated in the primary sequence of one of the
         monomer chains indicated.

      -  : Individual plots for each angle of the selected residue.
         Detailed numeric values are shown in the file.

-  Summary content:

   | box:
   | Statistics included in the above (an example can be observed in
     (6).
