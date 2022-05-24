.. _`app:dockPredictedModelProtocol`:

Phenix Dock Predicted Model protocol 
========================================

*PHENIX*-based protocol designed to dock processed AlphaFold2 :cite:p:`jumper2021`, RoseTTAFold :cite:p:`baek2021` and other predicted models in *Scipion*. According to `PHENIX documentation <https://phenix-online.org/version_docs/dev-4380/reference/dock_predicted_model.html>`_ the tool *dock_predicted_model* uses the connectivity of the model as a restraint so that the docked domains are in a reasonable arrangement. Although the method has been designed to handle with symmetry, you can get usually a better result segmenting manually the map and working with the asymmetric unit (see also appendices :ref:`Extract asymmetric unit <app:extractUnitCell>` and :ref:`Phenix Dock in Map <app:dockInMapProtocol>`). Each domain is docked and refined by rigid-body refinement. When all the domains are docked, the residues are sorted and a single chain is produced.

-  | Requirements to run this protocol and visualize results:

   -  | *Scipion* plugin: **scipion-em**

   -  | *Scipion* plugin: **scipion-em-phenix**

   -  | **PHENIX software suite** (tested for version 1.20.1-4487)

   -  | *Scipion* plugin: **scipion-em-chimera**

-  | *Scipion* menu: *Model building -> Rigid fitting*  (:numref:`model_building_app_protocol_dock_prediction_1` (A))

   .. figure:: Images_appendices/Fig3_processPrediction.svg
      :alt: Protocol **phenix-dock predicted model**. A: Protocol location in *Scipion* menu. B: Protocol form.
      :name: model_building_app_protocol_dock_prediction_1
      :align: center
      :width: 100.0%

      Protocol **phenix-dock predicted model**. A: Protocol location in *Scipion* menu. B: Protocol form.

-  | Protocol form parameters (:numref:`model_building_app_protocol_dock_prediction_1` (B)):

   | *Input* section:

   -  | *Predicted AlphaFold2 model*: Any atom structure that the user would like to process. It can be generated as AlphaFold2 prediction through the *Scipion* protocol **chimerax-alphafold prediction** (See Appendix :ref:`AlphaFold2 Initial Model Prediction <app:alphafoldPredictionProtocol>`) or generated outside *Scipion*. In this last case, the predicted atom structure has to be imported previously (look at Appendix :ref:`Import atomic structure <app:importAtomicStructure>`). 

   -  | *Processed AlphaFold2 model*: Since the protocol **phenix-dock predicted model** is usually the second step in the modeling workflow of AlphaFold2 predictions, it uses the previous processed prediction model, in which all the uncertain residues have been trimmed and the rest of the sequence has been grouped in compact domains. Then, include here the output of the protocol **phenix-dock predicted model** (see appendix :ref:`Process Predicted Model <app:processPredictedProtocol>`).

   -  | *Input map*: Electron density map previously downloaded or generated in *Scipion* to fit the atomic structure.

   -  | *High-resolution limit (Å)*: Electron density map resolution.

   -  | *Number of threads*: Advanced param. Depending on the size of *map* and *model*, and the number of *models* to fit the process could be quite slow and you can accelerate it by increasing the number of threads.

   -  | *Extra Params*: Advanced param. Look at `PHENIX documentation <https://phenix-online.org/version_docs/dev-4380/reference/dock_predicted_model.html>`_ page to include additional params with the appropriate syntaxis.

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

   | After executing the protocol, press *Analyze Results* in the *Scipion* framework and the *ChimeraX* graphics window will be opened. Atomic structures and volumes are referred to the origin of coordinates in *ChimeraX*. To show the relative position of atomic structures and electron density volume, the three coordinate axes are represented; X axis (red), Y axis (yellow), and Z axis (blue) (:numref:`model_building_app_protocol_volume_3`). Coordinate axes, map, initial predicted model,  processed unfitted *model* (suffix *.pdb*) and final fitted atomic structure (suffix *.pdb.pdb*) are model numbers *#1*, *#2*, *#3*, *#4* and *#5*, respectively, in *ChimeraX Models* panel. Initial model residues predicted by AlphaFold2 are colored according to the alphafold bfactor (*LDDT* values) palette of *ChimeraX* (model #3).

-  | Summary content:

   -  | Protocol output (below framework):
      | *phenix - dock predicted model -> ouputPdb*;
      | *AtomStruct (pseudoatoms=True/ False, volume=True/ False)*.
      | Pseudoatoms is set to *True* when the structure is made of
        pseudoatoms instead of atoms. 

   -  | *SUMMARY* box:
      | https://phenix-online.org/version_docs/dev-4380/reference/dock_predicted_model.html 
