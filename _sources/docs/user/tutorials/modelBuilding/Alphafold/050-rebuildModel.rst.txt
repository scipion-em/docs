.. _`rebuildModel`:

Morph the predicted model onto the docked fragments and rebuild the missing parts of the model in the map density 
===============================================================================================================

In this section of the AlphaFold tutorial we are going to rebuild the docked isoform CRA_a of TACAN monomer structure finally obtained in the previous :ref:`section <dockInitialModel>`.

   .. figure:: Images/Fig20_workflow_4.svg
      :alt: Part of the general Scipion workflow performed to rebuild the AlphaFold2 prediction structure of the isoform CRA_a of human TACAN complex.
      :name: model_building_fig20_workflow
      :align: center
      :width: 100.0%

      Part of the general Scipion workflow performed to rebuild the AlphaFold2 prediction structure of the isoform CRA_a of human TACAN complex.

We are going to take advantage of the protocol **phenix-rebuild predicted model** to rebuild the docked structure prediction into the map (protocol :ref:`appendix <app:rebuildPredictedModelProtocol>`). As the title of this section indicates, the rebuild function morphs the predicted model onto the docked fragments and rebuilds the missing parts of the model in the map density. The result, however, depends very much on the map we are working with. In any case, the result can still be improved by additional rounds of processing.

Let us start by opening (:numref:`model_building_fig24_rebuild` (1)) and filling in the protocol form, adding the previously obtained :ref:`predicted AlphaFold2 <getInitialModel>` (2) and :ref:`docked <dockInitialModel>` models (3), and the map (4). After fixing the map resolution limit, increase the number of threads (5) and finally, execute the protocol (6).

   .. figure:: Images/Fig24_protocol_rebuild_model_1.svg
      :alt: Completing the protocol **phenix-rebuild predicted model** (workflow step 11; :numref:`model_building_fig20_workflow`).
      :name: model_building_fig24_rebuild
      :align: center
      :width: 100.0%

      Completing the protocol **phenix-rebuild predicted model** (workflow step 11; :numref:`model_building_fig20_workflow`).

After a quick running, the protocol finishes. Probably due to a file format incompatibility, the tool was unable to morph the predicted structure, as you can check in the results clicking ``Analyze Results``. Nevertheless, we can use the recently obtained docked model (:numref:`model_building_fig23_dock_model`) as template to get a new AlphaFold prediction using this option in the *Phenix* Colab Notebook. With this aim, complete again the **chimerax-alphafold prediction** protocol (:numref:`model_building_fig25_rebuild` (1)) selecting *Google Colab* (2), the *Phenix Colab Notebook* (3), the isoform CRA_a of TACAN protein sequence (4) and the previous docked model (5). Then, execute the protocol (6).

   .. figure:: Images/Fig25_protocol_rebuild_model_3.svg
      :alt: Completing the protocol **chimerax-alphafold prediction** using the Phenix Colab Notebook with template option (workflow step 12; :numref:`model_building_fig20_workflow`).
      :name: model_building_fig25_rebuild
      :align: center
      :width: 100.0%

      Completing the protocol **chimerax-alphafold prediction** using the Phenix Colab Notebook with template option (workflow step 12; :numref:`model_building_fig20_workflow`).

Soon after executing the protocol, the browser window of *Phenix* Colab Notebok opens and stars to run. ``REMARK`` that when a template is used, this template has to be manually uploaded. This task requires clicking the key ``Choose Files`` in the Cell #3 of the browser (:numref:`model_building_fig26_rebuild` (1)).

   .. figure:: Images/Fig26_protocol_rebuild_model_4.svg
      :alt: Cell 3 of the browser of *Phenix* Colab Notebook completed and running.
      :name: model_building_fig26_rebuild
      :align: center
      :width: 100.0%

      Cell 3 of the browser of *Phenix* Colab Notebook completed and running.

After a while the prediction process finishes and the AlphaFold2 predicted structure is shown in *ChimeraX*. :numref:`model_building_fig27_rebuild` details the new prediction (A) and the PAE plot (B). Comparing the accuracy of residues and PAE error with the predictions of monomers and dimers that we have obtained :ref:`before <getInitialModel>`, we can observe that the new one is the best one.

   .. figure:: Images/Fig27_protocol_rebuild_model_5.svg
      :alt: Prediction of isoform CRA_a of human TACAN protein structure obtained using a template in the *Phenix* Colab Notebook. **A**: Protein structure in *ChimeraX* GUI. **B**: PAE plot.
      :name: model_building_fig27_rebuild
      :align: center
      :width: 100.0%

      Prediction of isoform CRA_a of human TACAN protein structure obtained using a template in the *Phenix* Colab Notebook. **A**: Protein structure in *ChimeraX* GUI. **B**: PAE plot.

At this point we can follow the common workflow to process, dock and rebuild the new AlphaFold2 prediction. Starting with the model processing, open the protocol **phenix-process predicted model** (:numref:`model_building_fig28_rebuild` (1)) with the predicted model (2), the B-value column values to consider as minimum to process (3), the PAE file (4), and then execute the protocol (5).

   .. figure:: Images/Fig28_protocol_rebuild_model_6.svg
      :alt: Completing the protocol **phenix-process predicted model** to process the AlphaFold2 prediction obtained using the Phenix Colab Notebook with template option (workflow step 13; :numref:`model_building_fig20_workflow`).
      :name: model_building_fig28_rebuild
      :align: center
      :width: 100.0%

      Completing the protocol **phenix-process predicted model** to process the AlphaFold2 prediction obtained using the Phenix Colab Notebook with template option (workflow step 13; :numref:`model_building_fig20_workflow`).

After executing the protocol press ``Analyze Results`` to check the results menu (:numref:`model_building_fig29_rebuild` (A)).

   .. figure:: Images/Fig29_protocol_rebuild_model_7.svg
      :alt: Results obtained with the Scipion protocol **phenix-process predicted model**. **A**: Menu of results. **B**: Processed model opened (monomer) in ChimeraX GUI viewer. **C**: Remainder sequence fragment excluded from the processed structure.
      :name: model_building_fig29_rebuild
      :align: center
      :width: 100.0%

      Results obtained with the Scipion protocol **phenix-process predicted model**. **A**: Menu of results. **B**: Processed model opened (monomer) in ChimeraX GUI viewer. **C**: Remainder sequence fragment excluded from the processed structure.

Clicking *Structures in ChimeraX* (:numref:`model_building_fig29_rebuild` (A, 1)), the predicted and the processed structures will be simultaneously opened. Whereas the processed structure is still colored according to the AlphaFold2 confidence score, the processed structure is pink colored (:numref:`model_building_fig29_rebuild` (B)). Remark that this processed structure is constituted by **only one domain (chain)** (model #3).  Concerning the remaining fragments of sequence removed, open *Remaining Sequences* in the results' menu (:numref:`model_building_fig29_rebuild` (A, 2)) to observe the text file (C). The sequence is quite similar to the sequence shown in :numref:`model_building_fig15_alphafold_process` (C)).  

Next, run the protocol **phenix-dock predicted model** to dock the structure prediction into the map (protocol :ref:`appendix <app:dockPredictedModelProtocol>`). Open the protocol (:numref:`model_building_fig30_rebuild` (1)) and complete it with the new AlphaFold2 prediction obtained with *Phenix* notebook (2) (:numref:`model_building_fig27_rebuild`). Include the respective processed prediction (3) (:numref:`model_building_fig29_rebuild` (B)). Fill in the *Input map* box with the recently downloaded map (4) (:numref:`model_building_fig14_alphafold_docking`). Update the resolution value of the map, increase the number of processors to speed up the process (5) and, finally, execute the protocol (6).

   .. figure:: Images/Fig30_protocol_rebuild_model_8.svg
      :alt: Scipion Protocol **phenix-dock predicted model** completed to dock the isoform CRA_a of human TACAN protein prediction (workflow step 14; :numref:`model_building_fig20_workflow`).
      :name: model_building_fig30_rebuild
      :align: center
      :width: 100.0%

      Scipion Protocol **phenix-dock predicted model** completed to dock the isoform CRA_a of human TACAN protein prediction (workflow step 14; :numref:`model_building_fig20_workflow`).


Visualize the results clicking ``Analyze Results`` when the execution finishes. The *ChimeraX* GUI window will open to show the map and several models (:numref:`model_building_fig31_rebuild`). Not shown in :numref:`model_building_fig31_rebuild`, models #3 and #4 are the new AlphaFold2 prediction and the processed models, respectively. Pink model #5 is the docked model. 

   .. figure:: Images/Fig31_protocol_rebuild_model_9.svg
      :alt: ChimeraX GUI opened to visualize the docked model in the map EMD-31441.
      :name: model_building_fig31_rebuild
      :align: center
      :width: 90.0%

      ChimeraX GUI opened to visualize the docked model in the map EMD-31441.

Select the appropriate orientation of the map, the density threshold and the appearance as mesh to better visualize the docked structure.

At this point we take advantage of the protocol **phenix-rebuild predicted model** to rebuild the docked structure prediction into the map (protocol :ref:`appendix <app:rebuildPredictedModelProtocol>`). Rebuild function morphs the predicted model onto the docked fragments and rebuilds the missing parts of the model in the map density. Then, open the protocol (:numref:`model_building_fig24_rebuild` (1)) and fill in the protocol form, adding the AlphaFold2 prediction previously obtained (:numref:`model_building_fig27_rebuild`) (2), the docked model (:numref:`model_building_fig31_rebuild`) (3) and the map (4). After fixing the map resolution limit, increase the number of threads (5) and finally, execute the protocol (6).

   .. figure:: Images/Fig32_protocol_rebuild_model_10.svg
      :alt: Completing the protocol **phenix-rebuild predicted model** (workflow step 15; :numref:`model_building_fig20_workflow`).
      :name: model_building_fig32_rebuild
      :align: center
      :width: 100.0%

      Completing the protocol **phenix-rebuild predicted model** (workflow step 15; :numref:`model_building_fig20_workflow`).

The protocol finishes after a while and clicking ``Analyze Results`` results can be checked (:numref:`model_building_fig33_rebuild`). 

   .. figure:: Images/Fig33_protocol_rebuild_model_11.svg
      :alt: ChimeraX GUI opened to visualize the rebuilt model according to the map EMD-31441. **A**: Frontal view. **B**: Lateral view. The frame details structure fitting.
      :name: model_building_fig33_rebuild
      :align: center
      :width: 100.0%

      ChimeraX GUI opened to visualize the rebuilt model according to the map EMD-31441. **A**: Frontal view. **B**: Lateral view. The frame details structure fitting.

The two different views shown in :numref:`model_building_fig33_rebuild` detail the morphing both of horizontal alpha-helices (A, 1) and vertical ones (B, 2). Remark that the new rebuilt model (pink) fits better to the map than the previous docked one (green). The rest of the sequence, however, was unable to adapt its architecture to the map and remains mainly disordered. This result makes sense due to the sequence differences in the C-terminal part of the protein between the two isoforms of the human TACAN protein. Only the sequence identical in both isoforms has been predicted by Alphafold2 and finally morphed according to the map of the first isoform. The rest of the structure of the second isoform remains unpredicted and seems to adopt a quite different architecture than the first isoform. The experimental map of this second isoform CRA_a is thus essential to characterize the structure of the C-terminal part of the second isoform.
