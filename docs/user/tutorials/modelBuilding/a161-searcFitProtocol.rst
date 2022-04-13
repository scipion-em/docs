.. _`app:searchFit`:

Phenix Search and Fit a sequence in the map density
===================================================

| Protocol designed to obtain in the fitting of the experimental map and
  a small sequence for which we were able to trace the skeleton of
  :math:`\alpha` carbons. The process finishes with the refinement in
  the real space of the structure candidates. These potential fitted
  structures will be shown ranked by its map-model fitting score. For
  more information about the real space refinement have a look to
  Appendix [app:realSpaceRefineProtocol],
  :raw-latex:`\citep{afonine2018a}`.

-  Requirements to run this protocol and visualize results:

   -  plugin:

   -  plugin:

   -  package (tested for version 1.18.2-3874)

   -  plugin:

   -  CCP4 software suite (from version 7.0.056 to 7.1)

   -  plugin:

-  | menu:
   | ( (A))

-  | Protocol form parameters ( (B)):
   | : Since the process of fitting several structures in the density
     map takes quite a long time we suggest to increase the number of to
     accelerate the execution of the protocol.

   .. figure:: Images_appendix/Fig_search_fit.pdf
      :alt: Protocol . A: Protocol location in menu. B: Protocol form.
      :width: 90.0%

      Protocol . A: Protocol location in menu. B: Protocol form.

   -  : Electron density map previously downloaded or generated in to
      fit the atomic structure.

   -  : Electron density map resolution.

   -  : Atomic structure previously imported or generated in to be
      fitted to an electron density map. Structures from do not make
      sense here due to the purpose of the protocol of fitting partially
      traced models. Some residues of this model could be traced as .

   -  : Advance param. First line of extra params that the user would
      like to add to the real space refiment process that will be
      performed in the last step before retrieving the structure
      candidates of the atomic structure fitted to the density map.

   -  : Sequence of the atomic structure that we want to fit in the
      density map. This sequence has previously imported in . The next
      two wizards allow to delimit exactly the part of the sequence that
      has to be considered by selecting the first and last residues of
      this sequence (position and type of residue):

      -  
      -  

   -  : Advanced param. Second line of extra params that can be added to
      the script. This script is generated in the mutation process that
      allows to retrieve all possible atomic structures of a certain
      length starting in the first residue selected and ending in the
      last one selected.

   -  : Go to Appendix [app:realSpaceRefineProtocol].

-  Protocol execution:

   | Adding specific protocol label is recommended in section, at the
     form top. To add the label, open the protocol form, press the
     pencil symbol at the right side of box, complete the label in the
     new opened window, press OK and, finally, close the protocol. This
     label will be shown in the output summary content (see below). If
     you want to run again this protocol, do not forget to set to the .
   | Press the red button at the form bottom.

-  Visualization of protocol results:

   After executing the protocol, press and the pop up viewer window will
   open. This window allows to observe the retrieved models as well as
   the map-model fitting scores for all structures (by default) or for a
   selection of them ().

   .. figure:: Images_appendix/Fig_search_fit_2.pdf
      :alt: Viewer window of the protocol .
      :width: 50.0%

      Viewer window of the protocol .

   -  : graphics window will be opened by default. Map and atomic
      structures are referred to the origin of coordinates in . To show
      the relative position of the density volume and the atomic
      structures, the three coordinate axes are represented; X axis
      (red), Y axis (yellow), and Z axis (blue) (). Coordinate axes,
      map, initial untraced and final fitted atomic structures are
      models numbers , , and from to , respectively, in panel. The
      different retrieved fitted models are ordered according to the
      map-model fitting score value.

   -  : To observe the total number of retrieved fitted models, maintain
      the default value (). Otherwise, write in the box the desired
      maximum number of models to see. We presume that the atomic
      structures selected will be the best ones since they have the
      highest map-model fitting scores. The selected number of
      structures will be open in instead the total number of them.

   -  : In order to make easier the observation of the atomic
      structures, a small fraction of the map density can be selected
      (3Å by default).

   -  : Plot of map-model fitting scores of the protocol retrieved
      models. The average and standard deviation values are also shown.
      The values have been computed considering the total number of
      models. When only a certain number of the models has been selected
      in the item , the fitting score values of those selected models
      will be remarked in red.

-  Summary content:

   -  | Protocol output (below framework):
      | ;
      | .
      | ;
      | .
      | ;
      | .
      | ;
      | .
      | ;
      | .
      | Pseudoatoms is set to when the structure is made of pseudoatoms
        instead of atoms. Volume is set to when an electron density map
        is associated to the atomic structure.

   -  | box:
      | No summary information
