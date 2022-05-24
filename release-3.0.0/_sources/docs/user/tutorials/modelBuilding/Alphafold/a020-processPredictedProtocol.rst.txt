.. _`app:processPredictedProtocol`:

Phenix Process Predicted Model protocol
=======================================

*PHENIX*-based protocol designed to process AlphaFold2 :cite:p:`jumper2021`, RoseTTAFold :cite:p:`baek2021` and other predicted models in *Scipion*. According to `PHENIX documentation <https://phenix-online.org/documentation/reference/process_predicted_model.html>`_ the tool *process_predicted_model* starts replacing the confidence values (LDDT) or error estimates (RMSD) included in the B-factor column of a predicted atom structure by B or pseudo-B values. Then, it removes the lowest confidence residues (high B-values) and, optionally, it splits the model into compact domains. 

-  | Requirements to run this protocol and visualize results:

   -  | *Scipion* plugin: **scipion-em**

   -  | *Scipion* plugin: **scipion-em-phenix**

   -  | **PHENIX software suite** (tested for version 1.20.1-4487)

   -  | *Scipion* plugin: **scipion-em-chimera**

-  | *Scipion* menu: *Model building -> Initial model*  (:numref:`model_building_app_protocol_process_prediction_1` (A))

   .. figure:: Images_appendices/Fig1_processPrediction.svg
      :alt: Protocol **phenix-process predicted model**. A: Protocol location in *Scipion* menu. B: Protocol form (option *LDDT (AlphaFold2)* in param *Contents of B-value field*. C: Protocol form (option *RMSD* in param *Contents of B-value field*. D: Warning message about the average of values included in the atomic structure *B-value* field. E: Warning message about the minimum number of sequential residues that satisfy the *minimum LDDT* or *maximum RMSD* selected value.
      :name: model_building_app_protocol_process_prediction_1
      :align: center
      :width: 100.0%

      Protocol **phenix-process predicted model**. A: Protocol location in *Scipion* menu. B: Protocol form (option *LDDT (AlphaFold2)* in param *Contents of B-value field*. C: Protocol form (option *RMSD* in param *Contents of B-value field*. D: Warning message about the average of values included in the atomic structure *B-value* field. E: Warning message about the minimum number of sequential residues that satisfy the *minimum LDDT* or *maximum RMSD* selected value.

-  | Protocol form parameters (:numref:`model_building_app_protocol_process_prediction_1` (B)):

   | *Input* section:

   -  | *Predicted AlphaFold2 model*: Any atom structure that the user would like to process. It can be generated as AlphaFold2 prediction through the *Scipion* protocol **chimerax-alphafold prediction** (See Appendix :ref:`AlphaFold2 Initial Model Prediction <app:alphafoldPredictionProtocol>`) or generated outside *Scipion*. In this last case, the predicted atom structure has to be imported previously (look at Appendix :ref:`Import atomic structure <app:importAtomicStructure>`). 

   -  | *Contents of B-value field*: Three different types of values can be represented in the B-factor column of any atom structure file and the user should select one of them:

	-  | *LDDT (AlphaFold2)*: *LDDT* stands for *local-distance difference test* and computes the accuracy of the backbone prediction. AlphaFold 2 produces a per-residue confidence score (pLDDT, predicted LDDT) that varies between 0 (bad) and 100 (good). Fractional values (from 0 to 1) are also accepted. Only values above 70 (or 0.70) are accepted for confident residues. In case you selected by mistake *LDDT* as content of B-value field when values correspond to *RMSD*, a warning message will appear before running the protocol (:numref:`model_building_app_protocol_process_prediction_1` (D)). Although 70 is considered the default *LDDT* value, the user can modify this value through the next parameter:

		-  | *Minimum LDDT value*: Cutoff confidence value used to remove low-confidence residues. A minimum *LDDT* of 70 (default value) corresponds to a maximum RMSD of 1.5. A warning message will appear in case that less than 5 sequential residues are found at this minimum *LDDT* value (:numref:`model_building_app_protocol_process_prediction_1` (E)).

	-  | *RMSD*: Root Mean Square Deviation as confidence value in Angstroms (:numref:`model_building_app_protocol_process_prediction_1` (C)). For RoseTTAFold, the B-value field is RMSD. Residues with values higher than 1.5 are not acceptable. An empirical formula converts LDDT values in error estimates (`PHENIX documentation <https://phenix-online.org/documentation/reference/process_predicted_model.html>`_). In case you selected by mistake *RMSD* as content of B-value field when values correspond to *LDDT*, a warning message will appear before running the protocol (:numref:`model_building_app_protocol_process_prediction_1` (D)). Although 1.5 is considered the default *RMSD* value, the user can modify this value through the next parameter:

		-  | *Maximun RMSD value*: Cutoff confidence value used to remove low-confidence residues. A maximum RMSD of 1.5 (default value) corresponds to a minimum LDDT of 70. A warning message will appear in case that less than 5 sequential residues are found at this maximun *RMSD* value (:numref:`model_building_app_protocol_process_prediction_1` (E)).

	-  | *PAE file*: PAE stands for *Predicted Aligned Error*. Matrix of predicted aligned errors (e.g., from AlphaFold2), NxN matrix of RMSD values, N = number of residues in model. Alternative to splitting by compact regions. In this case the splitting will try to minimize predicted aligned errors in each grouping, selecting mainly the different domains of the structure.

	-  | *B-value*: Single number generated from the fluctuations of the atoms in all the frames. The protocols starts transforming both *LDDT* and *RMSD* to *B-value* and then process the structure.

   -  | *Remove low-confidence residues*: According to the threshold selected as *Minimum LDDT value* or *Maximun RMSD value*, whichever is specified.

   -  | *Processing option: Maximum domains*: Selecting this option the closest domains will merge to reduce the final number of domains to the selected value.

   -  | *Processing option: Minimum domain length (residues)*: Only domains of this length will be kept. In terms of size (in Angstroms), 15 Angstroms is the approximate size of domains to be found. This is the resolution that will be used to make a domain map. If you are getting too many domains, try making domain_size bigger (maximum 70 Angstroms). 

   -  | *Extra Params*: Advanced param. Look at `PHENIX documentation <https://phenix-online.org/documentation/reference/process_predicted_model.html>`_ page to include additional params with the appropriate syntaxis.

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

   | After executing the protocol, press *Analyze Results* in the *Scipion* framework and a pop up window will open by default (:numref:`model_building_app_protocol_process_prediction_2`). 

   .. figure:: Images_appendices/Fig2_processPrediction.svg
      :alt: Viewer window showing the result menu of protocol **phenix-process predicted model**.
      :name: model_building_app_protocol_process_prediction_2
      :align: center
      :width: 50.0%

      Viewer window showing the result menu of protocol **phenix-process predicted model**.

   | Clicking *Structures in ChimeraX*, the *ChimeraX* graphics window will be opened. Atomic structures are referred to the origin of coordinates in *ChimeraX*. To show the relative position of atomic structures, the three coordinate axes are represented; X axis (red), Y axis (yellow), and Z axis (blue) (:numref:`model_building_app_protocol_volume_3`). Coordinate axes, initial predicted model and processed one are model numbers *#1*, *#2* and *#3*, respectively, in *ChimeraX Models* panel. Initial model residues predicted by AlphaFold2 are colored according to the alphafold bfactor (*LDDT* values) palette of *ChimeraX* (model #2).

   | Clicking *Remaining Sequences*, a text file window will be opened including the different aminoacid residue fragments that been removed or deleted in the model. 15 residues is the minimum size set to write the sequence in this file. Smaller fragments will be ignored. When empty, the *Remaining Sequences* menu element will be hide. 

-  | Summary content:

   -  | Protocol output (below framework):
      | *phenix - process predicted model -> ouputPdb*;
      | *AtomStruct (pseudoatoms=True/ False, volume=True/ False)*.
      | Pseudoatoms is set to *True* when the structure is made of
        pseudoatoms instead of atoms. 

   -  | *SUMMARY* box:
      | https://phenix-online.org/version_docs/dev-4380/reference/process_predicted_model.html 
