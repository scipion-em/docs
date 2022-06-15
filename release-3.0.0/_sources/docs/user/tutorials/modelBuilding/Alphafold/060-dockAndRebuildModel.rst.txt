.. _`dockAndRebuildModel`:

Three in one: Processing, docking and rebuilding the model in the map density 
=============================================================================

In this section of the AlphaFold tutorial we are going to process, dock and rebuild the last AlphaFold2 prediction of the isoform CRA_a of TACAN monomer.

   .. figure:: Images/Fig21_workflow_5.svg
      :alt: Part of the general Scipion workflow performed to process, dock and rebuild the AlphaFold2 prediction structure of the isoform CRA_a of human TACAN complex.
      :name: model_building_fig21_workflow
      :align: center
      :width: 100.0%

      Part of the general Scipion workflow performed to process, dock and rebuild the AlphaFold2 prediction structure of the isoform CRA_a of human TACAN complex.

We are going to take advantage of the protocol **phenix-dock and rebuild predicted model** to process, dock and rebuild the last structure prediction (:numref:`model_building_fig27_rebuild` (A)) into the map (protocol :ref:`appendix <app:dockAndRebuildProtocol>`). Our aim is to test this "three in one" tool and compare the result with the one obtained in the :ref:`previous section <rebuildModel>`.

Let us start by opening (:numref:`model_building_fig34_dock_rebuild` (1)) and filling in the protocol form, adding the previously obtained prediction AlphaFold2 structure (2) and the map (3). After setting the map resolution limit (4), increase the number of threads (5) and finally, execute the protocol (6).

   .. figure:: Images/Fig34_protocol_dock_rebuild_model_1.svg
      :alt: Completing the protocol **phenix-dock and rebuild predicted model** (workflow step 16; :numref:`model_building_fig21_workflow`).
      :name: model_building_fig34_dock_rebuild
      :align: center
      :width: 100.0%

      Completing the protocol **phenix-dock and rebuild predicted model** (workflow step 16; :numref:`model_building_fig21_workflow`).

After a while, the "three in one" process finishes and the processed AlphaFold2 predicted structure, docked and morphed into the map, can be visualized in *ChimeraX*. :numref:`model_building_fig35_dock_rebuild` details the fitting of the new prediction. 

   .. figure:: Images/Fig35_protocol_dock_rebuild_model_2.svg
      :alt: ChimeraX GUI opened to visualize the docked and rebuilt model according to the map EMD-31441. The frame show a detail of the structure fitting.
      :name: model_building_fig35_dock_rebuild
      :align: center
      :width: 100.0%

      ChimeraX GUI opened to visualize the docked and rebuilt model according to the map EMD-31441. The frame shows a detail of the structure fitting.

:numref:`model_building_fig37_dock_rebuild` compares this new docked and rebuilt structure with the one obtained in the :ref:`previous section <rebuildModel>`. The two structures seem to be quite similar both in the ordered helices and in the disordered region. We can conclude that the "three in one" tool can perform essentially the same work than the workflow followed previously but in only one step.

   .. figure:: Images/Fig37_protocol_dock_rebuild_model_4.svg
      :alt: ChimeraX GUI opened to compare the structures derived from independent (pink) and unified (green) protocols for processing, docking and rebuilding. 
      :name: model_building_fig37_dock_rebuild
      :align: center
      :width: 80.0%

      ChimeraX GUI opened to compare the structures derived from independent (pink) and unified (green) protocols for processing, docking and rebuilding. 

The same protocol can be applied to other predictions, for example to that obtained for the protein monomer using the *Chimera21 Colab Notebook* (:numref:`model_building_fig8_alphafold_prediction`). Execute the protocol indicated as workflow step 17 (:numref:`model_building_fig21_workflow`) and check the results (:numref:`model_building_fig36_dock_rebuild`). Remark that in this last case we have misssing the connection between horizontal and vertical helices. Despite of that, nevertheless, the remaining predicted structure fits in the right way to the map.

   .. figure:: Images/Fig36_protocol_dock_rebuild_model_3.svg
      :alt: ChimeraX GUI opened to visualize the docked and rebuilt model according to the map EMD-31441. 
      :name: model_building_fig36_dock_rebuild
      :align: center
      :width: 100.0%

      ChimeraX GUI opened to visualize the docked and rebuilt model according to the map EMD-31441. The frame show a detail of the structure fitting.
