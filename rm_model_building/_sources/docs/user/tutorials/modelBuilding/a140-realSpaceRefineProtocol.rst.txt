.. _`app:realSpaceRefineProtocol`:

Phenix Real Space Refine protocol
=================================

Protocol designed to refine in real space an atomic structure into a map
in by using program :raw-latex:`\citep{afonine2018a}`. Integrated in the
:math:`Phenix` software suite (https://www.phenix-online.org/), tool can
be applied to refine cryo-EM-derived models in real space. This program
computes coefficients between map and model-derived map and,
additionally, it assesses the geometry and dihedral-angle combinations
of atomic structures with the aim of getting the best map-fitted
structure by reducing the number of geometry outliers. Validation
:math:`MolProbity` scores are shown at the end of the refinement
process.

-  Requirements to run this protocol and visualize results:

   -  plugin:

   -  plugin:

   -  PHENIX software suite (v. higher than 1.13, tested for versions
      1.16-3549, 1.17.1-3660 and 1.18.2-3874)

   -  plugin:

   -  CCP4 software suite

   -  plugin:

-  | menu:
   | ( (A))

-  Protocol form parameters ( (B)):

   .. figure:: Images_appendix/Fig148.pdf
      :alt: Protocol . A: Protocol location in menu. B: Protocol form.
      :name: fig:app_protocol_real_space_refine_1
      :width: 90.0%

      Protocol . A: Protocol location in menu. B: Protocol form.

   -  : Electron density map previously downloaded or generated in .

   -  : resolution.

   -  : Atomic structure previously downloaded or generated in and
      fitted to the electron density map.

   -  : Advanced param that allows to add a string to the phenix command
      including other program params. Syntax to add extra params: = =

   -  : Advanced param to choose including secondary structure
      restraints. It is set to by default.

   -  : Advanced param that allows select the number of iterations of
      refinement. Although 5 macro-cycles, set by default, is usually
      enough, increasing this value might be helpful when model geometry
      or/and model-to-map fit is poor. The increase in the number of
      macro-cycles will also scale the computing times.

   -  : Box of advanced params that allow to modify the default
      refinement optimization strategy:

      -  : Param set to “Yes” by default to look for the global minimum
         of the model.

      -  : Param set to “No” by default. It considers the movement of
         groups of atoms as a single body.

      -  : Param set to “No” by default. It is used to fit local
         rotamers.

      -  : Param set to “No” by default. It allows distortions of the
         model to match the electron density map.

      -  : Param set to “No” by default. By molecular dynamics this
         param minimizes the energy of the model.

      -  : Param set to “Yes” by default. Model refinement regarding the
         map param that considers temperature factors. This refinement
         step is performed only at the last macro-cycle.

-  | Protocol execution:
   | Adding specific map/structure label is recommended in section, at
     the form top. To add the label, open the protocol form, press the
     pencil symbol at the right side of box, complete the label in the
     new opened window, press OK and, finally, close the protocol. This
     label will be shown in the output summary content (see below). If
     you want to run again this protocol, do not forget to set to the .
   | Press the red button at the form bottom.

-  Visualization of protocol results:

   After executing the protocol, press and the results window will be
   opened ().

   .. figure:: Images_appendix/Fig149.pdf
      :alt: Protocol . Taps to visualize results.
      :name: fig:app_protocol_real_space_refine_2
      :width: 50.0%

      Protocol . Taps to visualize results.

   Five taps are shown in the upper part of the results window (only
   four taps with v. 1.13 identical to those shown in , , and ):

   -  : graphics window will be opened by default. Atomic structure and
      volume are referred to the origin of coordinates in . To show the
      relative position of atomic structure and electron density volume,
      the three coordinate axes are represented; X axis (red), Y axis
      (yellow), and Z axis (blue) ().

   -  : Three different summary tables are shown to describe the results
      obtained from and (). Concerning the atomic , numeric data from
      chains, residues, atoms and geometry are described, as well as
      main statistics. summarizes experimental map box dimensions and
      different values of resolution computed with or without a mask.
       details main real-space correlation coefficients.

      .. figure:: Images_appendix/Fig150_0.pdf
         :alt: Protocol . Summary tables of main results.
         :name: fig:app_protocol_real_space_refine_2_1
         :width: 50.0%

         Protocol . Summary tables of main results.

   -  : Statistics concerning the atomic model, most of them obtained
      from ().

      .. figure:: Images_appendix/Fig150.pdf
         :alt: Protocol . and other statistics of the atomic model.
         :name: fig:app_protocol_real_space_refine_3
         :width: 50.0%

         Protocol . and other statistics of the atomic model.

      -  : List that contains all severe clashes (non-H atoms overlaping
         more than 0.4 Å) found by PROBE. All these clashes can be
         visualized and solved graphically in . If no hydrogens were
         present, REDUCE adds them before running PROBE. The list can be
         saved in a folder selected by the user.

      -  : Method designed to assess the mainchain geometry of the
         atomic model by using protein C\ :sub:`:math:`\alpha`` geometry
         and to identify areas of probable secondary structure. Residues
         that fall outside contours of expected protein behaviour based
         on high-quality datasets are considered outliers.

      -  : C\ :sub:`:math:`\beta`` outliers deviate from ideal positions
         by more than 0.25Å. Ideal C\ :sub:`:math:`\beta`` position is
         determined from the average of the ideal C-N-CA-CB and
         N-C-CA-CB dihedrals. This measure is more sensitive than
         individual measures to both sidechain and mainchain
         misfittings. Its deviation is an indicator of incompatibility
         between sidechain and backbone.

      -  : Residues showing :math:`cis` or :math:`twisted` conformations
         that could be modeling errors. :math:`cis` conformations are
         observed in about 5% of Prolines and 0.03% of general residues.
         Twisted peptides are almost certainly modeling errors.

      -  : Rotamer outlier list contains residues that adopt an unusual
         conformation of :math:`\chi` dihedral angles. These outliers,
         commonly used to characterize the conformation of protein
         sidechains, are detailed in Chi1-Chi2 graph, shown below.

      -  : Rhamachandran outlier list contains residues that show an
         unusual combination of their :math:`\phi` (C-N-CA-C) and
         :math:`\psi` (N-CA-C-N) dihedral angles. Most of the time,
         Ramachandran outliers are a consequence of mistakes during the
         data processing. These outliers are detailed below in
         Rhamachandran graphs.

      -  : Statistics for geometry restraints used in refinement.
         Although in general a fully refined structure should not have
         any outliers, exceptionally there are some of them that are
         obvious in high resolution electron density maps. Types of
         restraints:

         -  : This table indicates the number of outliers and the number
            of restraints (in accordance with the bond length restraints
            library). The list of outliers details the bonded pairs of
            atoms sorted by deviation (higher than 4 sigmas).

         -  : This table indicates the number of outliers and the number
            of restraints (in accordance with the bond angle restraints
            library). The list of outliers details the bonded triplets
            of atoms sorted by deviation (higher than 4 sigmas).

         -  : This table indicates the number of outliers and the number
            of restraints (in accordance with the side chain dihedral
            torsion - chi- angle restraints library). The list of
            outliers details the bonded tetrads of atoms sorted by
            deviation (higher than 4 sigmas).

         -  : This table indicates the number of restraints (in
            accordance with the volume chilarity restraints library).

         -  : This table indicates the number of restraints (in
            accordance with the volume planarity restraints library).

         -  : This table indicates the number of restraints (in
            accordance with the volume parallelity restraints library).

         -  : This table indicates the number of restraints (in
            accordance with the volume non-bonded distance restraints
            library).

      -  : Interactive visualization of outliers (Ramachandran, rotamer
         and C\ :sub:`:math:`\beta``) and severe clashes with .

   -  : Real-space correlation coefficients between map and
      model-derived map ().

      .. figure:: Images_appendix/Fig151.pdf
         :alt: Protocol . Real-space correlation results.
         :name: fig:app_protocol_real_space_refine_4
         :width: 50.0%

         Protocol . Real-space correlation results.

      -  :raw-latex:`\citep{afonine2018b}`:

         -  : Correlation coefficient between the model-derived map and
            the experimental map inside the mask region built around the
            model with a fixed radius. This comparison aims to fit the
            atomic centers.

         -  : Correlation coefficient between the model-derived map and
            the whole experimental map. This comparison aims to assess
            the similarity of maps and remark map densities that have
            not been modeled.

         -  : Correlation coefficient between the model-derived map and
            the experimental map inside the mask region built around the
            model considering only model-derived map regions with the
            highest density values, ignoring regions below a certain
            contouring density threshold. Particularly, in this case the
            N points with the highest density, inside the molecular
            mask, are taken into account. This comparison aims to fit
            the molecular envelope defined by the model-derived map.

         -  : Correlation coefficient between the model-derived map and
            the experimental map that considers only map regions with
            the highest density values, ignoring regions below a certain
            contouring density threshold. Particularly, in this case the
            N points with the highest density, simultaneously present in
            the model-calculated map and in the experimental map, are
            taken into account. This comparison aims to fit the
            strongest peaks in model-derived and experimental maps.

         -  

         -  

      -  :

         -  : Plot of correlation coefficients regarding the chain IDs.
            These correlation coefficient values can be saved in a text
            file in the folder selected by the user.

         -  : Plot of correlation coefficients of each chain residues.
            The specific chain is selected by the user in the chain
            option box. These correlation coefficient values for each
            chain can be saved in a text file in the folder selected by
            the user.

   -  (): Computation of Resolution and FSC.

      .. figure:: Images_appendix/Fig152.pdf
         :alt: Protocol . Experimental data results.
         :name: fig:app_protocol_real_space_refine_5
         :width: 50.0%

         Protocol . Experimental data results.

      -  : Basic statistics about the maps and summary of resolution
         estimates.

         -  : Map cell dimensions (pixels).

         -  | : Resolution estimates computed considering both map
              experimental data and model-derived information(with and
              without mask).
            | : Resolution cutoff beyond which Fourier map coefficients
              are negligibly small. Calculated from the full map or from
              each one of half maps [d99 (half map 1), d99 (half map
              2)].
            | : Overall isotropic B-value.
            | : Resolution cutoff at which the model map is the most
              similar to the target (experimental) map. Requires map and
              model. For d_model to be meaningful, model is expected to
              fit the map as well as possible.
            | : It tries to avoid the blurring of the map.
            | : d_FSC_model_0; Resolution cutoff up to which the model
              and map Fourier coefficients are similar at FSC value 0.
            | : d_FSC_model_0.143; Resolution cutoff up to which the
              model and map Fourier coefficients are similar at FSC
              value 0.143.
            | : d_FSC_model_0.5; Resolution cutoff up to which the model
              and map Fourier coefficients are similar at FSC value 0.5.
            | : d_FSC; Highest resolution at which the experimental data
              are confident. Obtained from FSC curve calculated using
              two half-maps and taken at FSC=0.143. The two half maps
              are required to compute this value.
            | : Radius of the default soft mask used since sharp edges
              resulting from applying a binary map may introduce Fourier
              artifacts.

      -  Fourier shell correlation taps:

         -  (Only if two half maps have been added as inputs): FSC plot
            regarding the resolution (Å) and the spatial frequency (1/Å)
            based on half maps with and without masking. The
            intersections of the curves with FSC = 0.143 are shown. FSC
            plot data can be saved as text file in a folder selected by
            the user.

         -  : FSC plot regarding the resolution (Å) and the spatial
            frequency (1/Å) based on the experimental map and the
            model-derived map with and without masking. The
            intersections of the curves with FSC = 0.5 are shown. FSC
            plot data can be saved as text file in a folder selected by
            the user.

-  Summary content:

   | box:
   | Main :math:`MolProbity` statistics computed by the :math:`Phenix`
     package to assess protein geometry using the same distributions as
     the MolProbity server:

   -  : Percentage of residues assessed that show an unusual combination
      of their :math:`\phi` (C-N-CA-C) and :math:`\psi` (N-CA-C-N)
      dihedral angles.

   -  : Percentage of residues assessed that show an normal combination
      of their :math:`\phi` (C-N-CA-C) and :math:`\psi` (N-CA-C-N)
      dihedral angles. Ramachandran outliers and favored residues are
      detailed in the . Allowed residues are included in the small
      region comprised between favored and outlier regions of that plot.

   -  : Percentage of residues assessed that adopt an unusual
      conformation of :math:`\chi` dihedral angles. Rotamer outliers,
      commonly used to characterize the conformation of protein
      sidechains, are detailed in the Chi1-Chi2 plot.

   -  : Number of residues showing an unusual deviation (higher than
      0.25 Å) of the C\ :math:`\beta` from its ideal position. This
      deviation is an indicator of incompatibility between sidechain and
      backbone.

   -  : Score associated to the number of pairs of non-bonded atoms
      unsually close to each other, showing probable steric overlaps.
      Clashscore is calculated as the number of serious clashes per 1000
      atoms. This value has to be as low as possible.

   -  : :math:`MolProbity` overall score representing the experimental
      resolution expected for the structure model. This value should be
      lower than the actual resolution. The lower the value, the better
      quality of the structure model.
