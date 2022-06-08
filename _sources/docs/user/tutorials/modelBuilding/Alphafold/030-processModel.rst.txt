.. _`processInitialModel`:

Remove low-confidence residues of the model and break it into compact domains
=============================================================================

Following with the small workflow basic to get and handle AlphaFold structures (Fig. workflow) we cover in this section of the tutorial the processing of AlphaFold predictions. Although there are more general ways of processing these predictions, for example using *Scipion* protocols such as **chimerax-operate** (:ref:`appendix <app:chimeraOperate>`) or **ccp4-coot refinement** (:ref:`appendix <app:ccp4CootRefinement>`), we are going to use here the *PHENIX* derived *Scipion* protocol **phenix-process predicted model** to remove the less accurate part of the predicted structure and to split it into compact domain. Look at this protocol :ref:`appendix <app:processPredictedProtocol>` for details.
In this workflow we are going to use the previously obtained AlphaFold predicted structure of TACAN monomer (best model) running the *Chimera21* Colab Notebook (:numref:`model_building_fig8_alphafold_prediction`).


Open the protocol **phenix-process predicted model** and fill in the form as indicated in :numref:`model_building_fig11_alphafold_process` (B). 

   .. figure:: Images/Fig11_protocol_process_model.svg
      :alt: Filling in the Scipion protocol **phenix-process predicted model**. **A**: Protocol in the Modeling panel menu. **B**: Form param completed to process the AlphaFold2 prediction.
      :name: model_building_fig11_alphafold_process
      :align: center
      :width: 100.0%

      Filling in the Scipion protocol **phenix-process predicted model**. **A**: Protocol in the Modeling panel menu. **B**: Form param completed to process the AlphaFold2 prediction.

Include the previously obtained Alphafold prediction (:numref:`model_building_fig11_alphafold_process` (B, 2)). Since the prediction structure file contains the confidence score values (LDDT) in the B-value column, we are going to select the default option *LDDT (AlphaFold2)* to complete the param *Contents of B-value field* (:numref:`model_building_fig11_alphafold_process` (B, 3)). In order to keep only confident residues (pLDDT > 70), the default minimum LDDT value is maintained. To add the information about the relative orientations of domains, the PAE file obtained with the structure prediction is also included (4) and the rest of params are maintained by default. Execute the protocol (5) and when it finishes press ``Analyze Results`` to check the results menu (:numref:`model_building_fig12_alphafold_process` (A)).

   .. figure:: Images/Fig12_protocol_process_model.svg
      :alt: Results obtained with the Scipion protocol **phenix-process predicted model**. **A**: Menu of results. **B**: Processed model opened in ChimeraX GUI viewer. **C**: Remainder sequence fragment excluded from the processed structure.
      :name: model_building_fig12_alphafold_process
      :align: center
      :width: 100.0%

      Results obtained with the Scipion protocol **phenix-process predicted model**. **A**: Menu of results. **B**: Processed model opened in ChimeraX GUI viewer. **C**: Remainder sequence fragment excluded from the processed structure.

Clicking *Structures in ChimeraX* (:numref:`model_building_fig12_alphafold_process` (A, 1)) the predicted and the processed structures will be simultaneously opened. Whereas the processed structure is still colored according to the AlphaFold2 confidence score, the processed structure displays a neutral color since the confidence score values of the B-vale column are not present in the structure file anymore. They have been replaced by the calculated B-values.This processed structure of the TACAN monomer is shown in (:numref:`model_building_fig12_alphafold_process` (B)). Remark that this processed structure is the model #3 whereas the predicted structure is the hide model #2. As you can see, two independent structure chains have been generated. Finally, if you want to check if there are remaining fragments of sequence removed (XX consecutive residues) open *Remaining Sequences* in the results' menu (:numref:`model_building_fig12_alphafold_process` (A, 2)) and a text file pop up window will be opened (C). In this particular case, the remaining sequence contains most part of the unstructured C-terminal end of the protein.
