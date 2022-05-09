.. _`app:processPredictedProtocol`:

Phenix Process Predicted Model protocol
=======================================

*PHENIX*-based protocol designed to process AlphaFold2 :cite:p:`jumper2021`, RoseTTAFold :cite:p:`baek2021` and other predicted models in *Scipion*. According to `PHENIX documentation <https://phenix-online.org/documentation/reference/process_predicted_model.html>`_ the tool *process_predicted_model* starts replacing the confidence values (LDDT) or error estimates (RMSD) included in the B-factor column of a predicted atom structure by B or pseudo-B values. Then, it removes the lowest confidence residues (high B-values) and, optionally, it splits the model into compact domains. 

-  | Requirements to run this protocol and visualize results:

   -  | *Scipion* plugin: **scipion-em**

   -  | *Scipion* plugin: **scipion-em-phenix**

   -  | **PHENIX software suite** (tested for version 1.20.1-4487)

   -  | *Scipion* plugin: **scipion-em-chimera**

-  | *Scipion* menu: *Model building -> Initial model* (:numref:`model_building_app_protocol_process_prediction_1` (A))

   .. figure:: Images_appendices/Fig1_processPrediction.svg
      :alt: Protocol **phenix-process predicted model**. A: Protocol location in *Scipion* menu. B: Protocol form.
      :name: model_building_app_protocol_process_prediction_1
      :align: center
      :width: 100.0%

      Protocol **phenix-process predicted model**. A: Protocol location in *Scipion* menu. B: Protocol form.

-  | Protocol form parameters (:numref:`model_building_app_protocol_process_prediction_1` (B)):

   | *Input* section:

   -  | *Predicted AlphaFold2 model*: Any atom structure that the user would like to process. It can be generated as AlphaFold2 prediction through the *Scipion* protocol **chimerax-alphafold prediction** (See Appendix :ref:`AlphaFold2 Initial Model Prediction <app:alphafoldPredictionProtocol>`) or generated outside *Scipion*. In this last case, the predicted atom structure has to be imported previously (look at Appendix :ref:`Import atomic structure <app:importAtomicStructure>`). 

   -  | *Contents of B-value field*: Three different types of values can be represented in the B-factor column of any atom structure file and the user should select one of them:

	-  | *LDDT (AlphaFold2)*: LDDT stands for *local-distance difference test* and computes the accuracy of the backbone prediction. AlphaFold 2 produces a per-residue confidence score (pLDDT, predicted LDDT) that varies between 0 (bad) and 100 (good). Only values above 70 are accepted for confident residues. Although 70 is considered the default value, the user can modify this value through the next parameter:

		-  | *Minimum LDDT value*: Cutoff confidence value used to remove low-confidence residues. A minimum LDDT of 70 (default value) corresponds to a maximum RMSD of 1.5.

	-  | *RMSD*: Root Mean Square Deviation as confidence value in Angstroms. Residues with values higher than 1.5 are not acceptable. An empirical formula converts LDDT values in error estimates (`PHENIX documentation <https://phenix-online.org/documentation/reference/process_predicted_model.html>`_).

	-  | *B-value*: Single number generated from the fluctuations of the atoms in all the frames.

	-  | *Remove low-confidence residues*:

	-  | *Processing option: Maximum domains*:

	-  | *Processing option: Minimum domain length (residues)*:

	-  | *Extra Params*:
