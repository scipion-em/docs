.. _`dockInitialModel`:

Dock the domains obtained into your cryo-EM  map or unit cell 
==============================================================

In this section of the AlphaFold tutorial we are going to dock the domains obtained by processing the AlphaFold2 prediction structure of the isoform CRA_a of human TACAN protein.

   .. figure:: Images/Fig19_workflow_3.svg
      :alt: Part of the general Scipion workflow performed to dock the AlphaFold2 prediction structure of the isoform CRA_a of human TACAN complex.
      :name: model_building_fig19_workflow
      :align: center
      :width: 100.0%

      Part of the general Scipion workflow performed to dock the AlphaFold2 prediction structure of the isoform CRA_a of human TACAN complex.

The protocol **phenix-dock predicted model** will help us to perform the task of docking structure prediction into the map (protocol :ref:`appendix <app:dockPredictedModelProtocol>`). This protocol is a optimization of the more general one **phenix-dock in map** to be applied to AlphaFold2 predictions (protocol :ref:`appendix <app:dockInMapProtocol>`).

Since the accuracy of the model was higher for the homodimer prediction than for the monomer, we are going to follow the branch of the homodimer prediction in the workflow after the processing (workflow step 10; :numref:`model_building_fig19_workflow`). Although the output processed structure of the protocol **phenix-process predicted model** contains three compact domains (:numref:`model_building_fig15_alphafold_process` (B)), all of them are included in the green PAE region 1 (:numref:`model_building_fig10_alphafold_prediction` (B)). The relative orientation of those domains seem to be right and probably they will be able to dock together. When there is no a clear relationship among domains, *i. e.* there is a high PAE error in the interdomain region, consider the possibility of docking independently each domain. The docking result can improve quite a lot using this strategy. 

Remark that we are talking about docking the model into the map. This is the first time that we mention the experimental map. As metioned :ref:`before <problemToSolveTACAN>`, the experimental map of this isoform of human TACAN is not available and we are going to borrow the map of the first isoform of the protein. We thus have to start importing it in the *Scipion* framework.

Open the protocol **pwem-import volumes** in the *Scipion* menu (:numref:`model_building_fig13_alphafold_docking` (1)) and fill in the form as indicated. Select the option of importing maps from the EMDB databasse (2), write the ID of the map and execute the protocol (4).

   .. figure:: Images/Fig13_protocol_docking_model.svg
      :alt: Filling in the Scipion protocol **pwem-import volumes** to download the map from EMDB (workflow step 9; :numref:`model_building_fig19_workflow`).
      :name: model_building_fig13_alphafold_docking
      :align: center
      :width: 100.0%

      Filling in the Scipion protocol **pwem-import volumes** to download the map from EMDB (workflow step 9; :numref:`model_building_fig19_workflow`).

The downloaded map can be visualized clicking in ``Analyze Results`` (look at the protocol :ref:`appendix <app:importVolume>` for details). With the option *Display volume with chimerax* the map will be shown as in :numref:`model_building_fig14_alphafold_docking`. Reorient the map to observe the C2 symmetry.

   .. figure:: Images/Fig14_protocol_docking_model.svg
      :alt: ChimeraX GUI opened to visualize the map EMD-31441.
      :name: model_building_fig14_alphafold_docking
      :align: center
      :width: 90.0%

      ChimeraX GUI opened to visualize the map EMD-31441.

Once we have the map, let us dock the processed AlphaFold2 predicted structure using the protocol **phenix-dock predicted model**. Open the protocol (:numref:`model_building_fig22_dock_model` (1)) and complete it with the AlphaFold2 prediction of the homodimer obtained with *Chimera21* notebook (2) (:numref:`model_building_fig10_alphafold_prediction` (A)). Include the respective processed prediction (3) (:numref:`model_building_fig15_alphafold_process` (B)). Fill in the *Input map* box with the recently downloaded map (4) (:numref:`model_building_fig14_alphafold_docking`). Update the resolution value of the map, increase the number of processors to speed up the process (5) and, finally, execute the protocol (6).

   .. figure:: Images/Fig22_protocol_dock_model.svg
      :alt: Scipion Protocol **phenix-dock predicted model** completed to dock the isoform CRA_a of TACAN homodimer (workflow step 10; :numref:`model_building_fig19_workflow`).
      :name: model_building_fig22_dock_model
      :align: center
      :width: 100.0%

      Scipion Protocol **phenix-dock predicted model** completed to dock the isoform CRA_a of TACAN homodimer (workflow step 10; :numref:`model_building_fig19_workflow`).


The execution finishes after a while and then you can visualize the results clicking ``Analyze Results``. The *ChimeraX* GUI window will open to show the map and several models. Model #3 is the AlphaFold2 prediction of the homodimer. Model #4 in green is the respective processed model (only one chain). Pink model #5 is the docked model. 

   .. figure:: Images/Fig23_protocol_dock_model.svg
      :alt: ChimeraX GUI opened to visualize the docked model in the map EMD-31441.
      :name: model_building_fig23_dock_model
      :align: center
      :width: 90.0%

      ChimeraX GUI opened to visualize the docked model in the map EMD-31441.

Select the appropriate orientation of the map, the density threshold and the appearance as mesh to better visualize the docked structure.


