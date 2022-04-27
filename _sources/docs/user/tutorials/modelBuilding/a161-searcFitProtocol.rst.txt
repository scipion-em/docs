.. _`app:searchFit`:

Phenix Search Fit protocol
===================================================

| Phenix Search and Fit a sequence in the map densityProtocol designed to fit in *Scipion* a small sequence for which we were able to trace the skeleton of :math:`\alpha` carbons in the experimental map. The process finishes with the refinement in the real space of the structure candidates. These potential fitted structures will be shown ranked by its map-model fitting score. For more information about the real space refinement have a look to Appendix :ref:`Phenix Real space refine <app:realSpaceRefineProtocol>` :cite:p:`afonine2018a`.

-  | Requirements to run this protocol and visualize results:

   -  | *Scipion* plugin: **scipion-em**

   -  | *Scipion* plugin: **scipion-em-phenix**

   -  | **PHENIX software suite** (tested for versions 1.18.2-3874, 1.19.2-4158 and 1.20.1-4487)

   -  | *Scipion* plugin: **scipion-em-ccp4**

   -  | **CCP4 software suite** (from version 7.0.056 to 7.1)

   -  | *Scipion* plugin: **scipion-em-chimera**

-  | *Scipion* menu: *Model building -> Flexible fitting* (:numref:`model_building_app_phenix_search_fit_1` (A))

   .. figure:: Images_appendix/Fig_search_fit.svg
      :alt: Protocol **phenix-search fit**. A: Protocol location in *Scipion* menu. B: Protocol form.
      :name: model_building_app_phenix_search_fit_1
      :align: center
      :width: 90.0%

      Protocol **phenix-search fit**. A: Protocol location in *Scipion* menu. B: Protocol form.

-  | Protocol form parameters (:numref:`model_building_app_phenix_search_fit_1` (B)):
   | ``NOTE:`` Since the process of fitting several structures in the density map takes quite a long time we suggest to increase the number of *MPI* to accelerate the execution of the protocol.

   -  | *Input volume*: Electron density map previously downloaded or generated in *Scipion* to fit the atomic structure.

   -  | *Resolution (Å)*: Electron density map resolution.

   -  | *Input atom structure*: Atomic structure previously downloaded or generated in *Scipion* to be fitted to an electron density map. Structures from *PDB* do not make sense here due to the purpose of the protocol of fitting partially traced models. Some residues of this model could be traced as *ALA*.

   -  | *Extra Params*: Advance param. First line of extra params that the user would like to add to the *PHENIX* real space refiment process that will be performed in the last step before retrieving the structure candidates of the atomic structure fitted to the density map.

   -  | *Test sequence*: Sequence of the atomic structure that we want to fit in the density map. This sequence has previously imported in *Scipion*. The next two wizards allow to delimit exactly the part of the sequence that has to be considered by selecting the first and last residues of this sequence (position and type of residue):

      - | *First residue
  
      - | *Last residue 

   -  | *Extra Params*: Advanced param. Second line of extra params that can be added to the *Coot* script. This script is generated in the mutation process that allows to retrieve all possible atomic structures of a certain length starting in the first residue selected and ending in the last one selected.

   -  | *Additional Advanced Params for real space refinement*: Go to Appendix:ref:`Real space refine <app:realSpaceRefineProtocol>`.

-  Protocol execution:

   | Adding specific protocol label is recommended in *Run name* section, at the
     form top. To add the label, open the protocol form, press the
     pencil symbol at the right side of *Run name* box, complete the label in the
     new opened window, press OK and, finally, close the protocol. This
     label will be shown in the output summary content (see below). If
     you want to run again this protocol, do not forget to set to *Restart* the *Run mode*.

   | Press the *Execute* red button at the form bottom.

-  Visualization of protocol results:

   After executing the protocol, press *Analyze Results* and the pop up viewer window will
   open. This window allows to observe the retrieved models as well as
   the map-model fitting scores for all structures (by default) or for a
   selection of them (:numref:`model_building_app_phenix_search_fit_2`).

   .. figure:: Images_appendix/Fig_search_fit_2.svg
      :alt: Viewer window of the protocol **phenix-search fit**.
      :name: model_building_app_phenix_search_fit_2
      :align: center
      :width: 50.0%

      Viewer window of the protocol **phenix-search fit**.

   -  | *Show volume and atomic structures in ChimeraX*: *ChimeraX* graphics window will be opened by default. Map and atomic structures are referred to the origin of coordinates in *ChimeraX*. To show the relative position of the density volume and the atomic structures, the three coordinate axes are represented; X axis (red), Y axis (yellow), and Z axis (blue) (:numref:`model_building_app_protocol_volume_3`). Coordinate axes, map, initial untraced and final fitted atomic structures are models numbers *#1*, *#2*, *#3* and from *#4* to *#n*, respectively, in *ChimeraX Models* panel. The different retrieved fitted models are ordered according to the map-model fitting score value.

   -  | *Max. Number Atom Structs.*: To observe the total number of retrieved fitted models, maintain the default value (*1000*). Otherwise, write in the box the desired maximum number of models to see. We presume that the atomic structures selected will be the best ones since they have the highest map-model fitting scores. The selected number of structures will be open in *ChimeraX* instead the total number of them.

   -  | *Show Area around input atomic structure (Å)*: In order to make easier the observation of the atomic structures, a small fraction of the map density can be selected (3Å by default).

   -  | *Summary Plot*: Plot of map-model fitting scores of the protocol retrieved models. The average and standard deviation values are also shown. The values have been computed considering the total number of models. When only a certain number of the models has been selected in the item *Max. Number Atom Structs.*, the fitting score values of those selected models will be remarked in red.

-  | Summary content:

   -  | Protocol output (below *Scipion* framework):
      | *phenix - search fit -> ouputAtomStruct 0*;
      | *AtomStruct (pseudoatoms=False, volume=False)*.
      | *phenix - search fit -> ouputAtomStruct 1*;
      | *AtomStruct (pseudoatoms=False, volume=False)*.
      | *phenix - search fit -> ouputAtomStruct 2*;
      | *AtomStruct (pseudoatoms=False, volume=False)*.
      | *phenix - search fit -> ouputAtomStruct 3*;
      | *AtomStruct (pseudoatoms=False, volume=False)*.
      | *phenix - search fit -> ouputAtomStruct 4*;
      | *AtomStruct (pseudoatoms=False, volume=False)*.

      | Pseudoatoms is set to *True* when the structure is made of pseudoatoms instead of atoms. Volume is set to *True* when an electron density map is associated to the atomic structure.

   -  | *SUMMARY* box:
      | No summary information
