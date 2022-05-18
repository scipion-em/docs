.. _`app:dockAndRebuildProtocol`:

Phenix Dock and Rebuild protocol
================================

*PHENIX*-based protocol designed to dock and rebuild AlphaFold2 :cite:p:`jumper2021`, RoseTTAFold :cite:p:`baek2021` and other predicted models in *Scipion*. According to `PHENIX documentation <https://phenix-online.org/version_docs/dev-4380/reference/dock_and_rebuild.html>`_ the tool *dock_and _rebuild* combines the functions of processing, docking and rebuilding predicted models into a cryo EM map. The three previous steps can be run also one by one using specific protocols for :ref:`processing <app:processPredictedProtocol>`, :ref:`docking <app:dockPredictedModelProtocol>` and :ref:`rebuilding <app:rebuildPredictedModelProtocol>`. The shorter way of the combined dock_and_rebuild procedure is more convenient for simple cases. If the result does not seems goood enough, you may always run the three steps individually. Identically, you can start with the whole map as input, or using a manually segmented part of the map and working with the asymmetric unit (see also appendix :ref:`Extract asymmetric unit <app:extractUnitCell>`).

-  | Requirements to run this protocol and visualize results:

   -  | *Scipion* plugin: **scipion-em**

   -  | *Scipion* plugin: **scipion-em-phenix**

   -  | **PHENIX software suite** (tested for version 1.20.1-4487)

   -  | *Scipion* plugin: **scipion-em-chimera**

-  | *Scipion* menu: *Model building -> Flexible fitting*  (:numref:`model_building_app_protocol_dock_and rebuild_1` (A))

   .. figure:: Images_appendices/Fig5_dockrebuildPrediction.svg
      :alt: Protocol **phenix-dock and rebuild predicted model**. A: Protocol location in *Scipion* menu. B: Protocol form.
      :name: model_building_app_protocol_dock_and rebuild_1
      :align: center
      :width: 100.0%

      Protocol **phenix-dock and rebuild predicted model**. A: Protocol location in *Scipion* menu. B: Protocol form.

-  | Protocol form parameters (:numref:`model_building_app_protocol_dock_and rebuild_1` (B)):

   | *Input* section:

  -  | *Predicted AlphaFold2 model*: Any atom structure that the user would like to process. It can be generated as AlphaFold2 prediction through the *Scipion* protocol **chimerax-alphafold prediction** (See Appendix :ref:`AlphaFold2 Initial Model Prediction <app:alphafoldPredictionProtocol>`) or generated outside *Scipion*. In this last case, the predicted atom structure has to be imported previously (look at Appendix :ref:`Import atomic structure <app:importAtomicStructure>`). 

  -  | *Input map*: Electron density map previously downloaded or generated in *Scipion* to fit the atomic structure.

  -  | *High-resolution limit (Å)*: Electron density map resolution.

  -  | *Number of threads*: Advanced param. Depending on the size of *map* and *model*, and the number of *models* to fit the process could be quite slow and you can accelerate it by increasing the number of threads.

  -  | *Extra Params*: Advanced param. Look at `PHENIX documentation <https://phenix-online.org/version_docs/dev-4380/reference/dock_and_rebuild.html>`_ page to include additional params with the appropriate syntaxis.

-  Protocol execution:

   | Adding specific protocol label is recommended in *Run name*
     section, at the form top. To add the label, open the protocol form,
     press the pencil symbol at the right side of *Run name* box,
     complete the label in the new opened window, press OK and, finally,
     close the protocol. This label will be shown in the output summary
     content (see below). If you want to run again this protocol, do not
     forget to set to *Restart* the *Run mode*.

   | Press the *Execute* red button at the form bottom.

-  | Visualization of protocol results:

   | After executing the protocol, press *Analyze Results* in the *Scipion* framework and the *ChimeraX* graphics window will be opened. Atomic structures and volumes are referred to the origin of coordinates in *ChimeraX*. To show the relative position of atomic structures and electron density volume, the three coordinate axes are represented; X axis (red), Y axis (yellow), and Z axis (blue) (:numref:`model_building_app_protocol_volume_3`). Coordinate axes, map, initial predicted model, and dock-and-rebuilt model (suffix *.pdb*) are model numbers *#1*, *#2*, *#3*, and *#4*, respectively, in *ChimeraX Models* panel. Initial model residues predicted by AlphaFold2 are colored according to the alphafold bfactor (*LDDT* values) palette of *ChimeraX* (model #3).

-  | Summary content:

   -  | Protocol output (below framework):
      | *phenix - dock and rebuild predicted model -> ouputPdb*;
      | *AtomStruct (pseudoatoms=True/ False, volume=True/ False)*.
      | Pseudoatoms is set to *True* when the structure is made of
        pseudoatoms instead of atoms. 

   -  | *SUMMARY* box:
      | https://phenix-online.org/version_docs/dev-4380/reference/dock_and_rebuild.html
