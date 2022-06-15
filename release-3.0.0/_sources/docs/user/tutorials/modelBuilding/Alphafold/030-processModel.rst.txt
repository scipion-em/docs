.. _`processInitialModel`:

Remove low-confidence residues of the model and break it into compact domains
=============================================================================

In this section of the AlphaFold tutorial we are going to cover the first step to handle AlphaFold2 prediction structures (:numref:`model_building_fig16_workflow`), performing the processing of the  AlphaFold2 prediction structure of the human TACAN protein (isoform CRA_a).

   .. figure:: Images/Fig18_workflow_2.svg
      :alt: Part of the general Scipion workflow performed to process the AlphaFold2 prediction structure of the isoform CRA_a of human TACAN complex.
      :name: model_building_fig18_workflow
      :align: center
      :width: 100.0%

      Part of the general Scipion workflow performed to process the AlphaFold2 prediction structure of the isoform CRA_a of human TACAN complex.

Although there are more general ways of processing AlphaFold2 predictions, for example using *Scipion* protocols such as **chimerax-operate** (:ref:`appendix <app:chimeraOperate>`) or **ccp4-coot refinement** (:ref:`appendix <app:ccp4CootRefinement>`), we are going to use here the *PHENIX* derived *Scipion* protocol **phenix-process predicted model** to remove the less accurate part of the predicted structure and to split it into compact domains. Look at this protocol :ref:`appendix <app:processPredictedProtocol>` for details.
In this workflow we are going to use the previously obtained AlphaFold predicted structures (best models) running the *Chimera21* Colab Notebook of the isoform CRA_a of TACAN monomer (:numref:`model_building_fig8_alphafold_prediction`) and homodimer (:numref:`model_building_fig10_alphafold_prediction`) to compare results .

Processing the monomer initial model
---------------------------------------

Open the protocol **phenix-process predicted model** and fill in the form as indicated in :numref:`model_building_fig11_alphafold_process` (B). 

   .. figure:: Images/Fig11_protocol_process_model.svg
      :alt: Filling in the Scipion protocol **phenix-process predicted model** (workflow step 7; :numref:`model_building_fig18_workflow`). **A**: Protocol in the Modeling panel menu. **B**: Form param completed to process the AlphaFold2 prediction.
      :name: model_building_fig11_alphafold_process
      :align: center
      :width: 100.0%

      Filling in the Scipion protocol **phenix-process predicted model** (workflow step 7; :numref:`model_building_fig18_workflow`). **A**: Protocol in the Modeling panel menu. **B**: Form param completed to process the AlphaFold2 prediction.

Include the previously obtained Alphafold prediction (:numref:`model_building_fig11_alphafold_process` (B, 2)). Since the prediction structure file contains the confidence score values (LDDT) in the B-value column, we are going to select the default option *LDDT (AlphaFold2)* to complete the param *Contents of B-value field* (:numref:`model_building_fig11_alphafold_process` (B, 3)). In order to keep only confident residues (pLDDT > 70), the default minimum LDDT value is maintained. To add the information about the relative orientations of domains, the PAE file obtained with the structure prediction is also included (4) and the rest of params are maintained by default. Execute the protocol (5) and when it finishes press ``Analyze Results`` to check the results menu (:numref:`model_building_fig12_alphafold_process` (A)).

   .. figure:: Images/Fig12_protocol_process_model.svg
      :alt: Results obtained with the Scipion protocol **phenix-process predicted model**. **A**: Menu of results. **B**: Processed model (monomer) opened in ChimeraX GUI viewer. **C**: Remainder sequence fragment excluded from the processed structure.
      :name: model_building_fig12_alphafold_process
      :align: center
      :width: 100.0%

      Results obtained with the Scipion protocol **phenix-process predicted model**. **A**: Menu of results. **B**: Processed model (monomer) opened in ChimeraX GUI viewer. **C**: Remainder sequence fragment excluded from the processed structure.

Clicking *Structures in ChimeraX* (:numref:`model_building_fig12_alphafold_process` (A, 1)) the predicted and the processed structures will be simultaneously opened. Whereas the processed structure is still colored according to the AlphaFold2 confidence score, the processed structure displays a neutral pink color since the confidence score values of the B-vale column are not present in the structure file anymore. They have been replaced by the calculated B-values. This processed structure of the isoform CRA_a of TACAN monomer is shown in (:numref:`model_building_fig12_alphafold_process` (B)). Remark that this processed structure is the model #3 whereas the predicted structure is the hide model #2. As you can see, **two independent compact domains** have been generated. Finally, if you want to check if there are remaining fragments of sequence removed (15 consecutive residues is the minimum remainder sequence length by default) open *Remaining Sequences* in the results' menu (:numref:`model_building_fig12_alphafold_process` (A, 2)) and a text file pop up window will be opened (C). In this particular case, the remaining sequence contains most part of the unstructured C-terminal end of the protein.

Processing the homodimer initial model
-----------------------------------------

Open again the protocol **phenix-process predicted model** (workflow step 8; :numref:`model_building_fig18_workflow`) and fill in the form as indicated in :numref:`model_building_fig11_alphafold_process` (B). This time include the homodimer AlphaFold2 best model prediction obtained using the *Chimera21* Colab Notebook (:numref:`model_building_fig10_alphafold_prediction`) and its respective PAE file. The rest of protocol params remain identical. Execute the protocol and press ``Analyze Results`` to check the results menu (:numref:`model_building_fig15_alphafold_process` (A)).

   .. figure:: Images/Fig15_protocol_process_model.svg
      :alt: Results obtained with the Scipion protocol **phenix-process predicted model**. **A**: Menu of results. **B**: Processed model opened (homodimer) in ChimeraX GUI viewer. **C**: Remainder sequence fragment excluded from the processed structure.
      :name: model_building_fig15_alphafold_process
      :align: center
      :width: 100.0%

      Results obtained with the Scipion protocol **phenix-process predicted model**. **A**: Menu of results. **B**: Processed model opened (homodimer) in ChimeraX GUI viewer. **C**: Remainder sequence fragment excluded from the processed structure.

Clicking *Structures in ChimeraX* (:numref:`model_building_fig15_alphafold_process` (A, 1)), the predicted and the processed structures will be simultaneously opened. Whereas the processed structure is still colored according to the AlphaFold2 confidence score, the processed structure show different colors to distinguish the **three independent compact domains** that have been generated (:numref:`model_building_fig15_alphafold_process` (B)). Remark that this processed structure is the model #3 whereas the predicted structure is the hide model #2. As you can see only one of the protomers has been processed, the chain B of the AlphaFold2 predicted structure. Concerning the remaining fragments of sequence removed, open *Remaining Sequences* in the results' menu (:numref:`model_building_fig15_alphafold_process` (A, 2)) and you can compare the text file (C) with the previous one generated for the monomer (:numref:`model_building_fig12_alphafold_process` (C)). As you can see, the remaining sequence obtained from processing the homodimer is 4 residues shorter at the N-terminal end than the remaining sequence obtained from processing the monomer.  
