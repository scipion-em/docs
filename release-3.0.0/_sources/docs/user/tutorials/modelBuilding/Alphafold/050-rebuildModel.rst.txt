.. _`rebuildModel`:

Morph the predicted model onto the docked fragments and rebuild the missing parts of the model in the map density 
===============================================================================================================

In this section of the AlphaFold tutorial we are going to rebuild the docked TACAN monomer structure finally obtained in the previous :ref:`section <dockInitialModel>`.

   .. figure:: Images/Fig20_workflow_4.svg
      :alt: Part of the general Scipion workflow performed to rebuild the AlphaFold2 prediction structure of the human TACAN complex.
      :name: model_building_fig20_workflow
      :align: center
      :width: 100.0%

      Part of the general Scipion workflow performed to rebuild the AlphaFold2 prediction structure of the human TACAN complex.

We are going to take advantage of the protocol **phenix-rebuild predicted model** to rebuild the docked structure prediction into the map (protocol :ref:`appendix <app:rebuildPredictedModelProtocol>`). As the title of this section indicates, the rebuild function morph the predicted model onto the docked fragments and rebuild the missing parts of the model in the map density. The result, however, depends very much on the map we are working with. In any case, the result anyway can still be improved by additional rounds of processing.

   .. figure:: Images/Fig24_protocol_rebuild_model_1.svg
      :alt: Completing the protocol **phenix-rebuild predicted model** (workflow step 11; :numref:`model_building_fig20_workflow`).
      :name: model_building_fig24_rebuild
      :align: center
      :width: 100.0%

      Completing the protocol **phenix-rebuild predicted model** (workflow step 11; :numref:`model_building_fig20_workflow`).

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

   .. figure:: Images/Fig25_protocol_rebuild_model_3.svg
      :alt: Completing the protocol **chimerax-alphafold prediction** (workflow step 12; :numref:`model_building_fig20_workflow`).
      :name: model_building_fig25_rebuild
      :align: center
      :width: 100.0%

      Completing the protocol **phenix-rebuild predicted model** (workflow step 12; :numref:`model_building_fig20_workflow`).


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

   .. figure:: Images/Fig26_protocol_rebuild_model_4.svg
      :alt: Cell 2 of the browser of *Phenix* Colab Notebook completed and running.
      :name: model_building_fig26_rebuild
      :align: center
      :width: 100.0%

      Cell 2 of the browser of *Phenix* Colab Notebook completed and running.


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

   .. figure:: Images/Fig27_protocol_rebuild_model_5.svg
      :alt: Prediction of TACAN protein structure obtained using a template in the *Phenix* Colab Notebook. **A**: Protein structure in *ChimeraX* GUI. **B**: PAE plot.
      :name: model_building_fig27_rebuild
      :align: center
      :width: 100.0%

      Prediction of TACAN protein structure obtained using a template in the *Phenix* Colab Notebook. **A**: Protein structure in *ChimeraX* GUI. **B**: PAE plot.


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

   .. figure:: Images/Fig28_protocol_rebuild_model_6.svg
      :alt: XXXXXXXXXXXXXXXXXXXXX
      :name: model_building_fig28_rebuild
      :align: center
      :width: 100.0%

      XXXXXXXXXXXXXXXXXXXXX

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

   .. figure:: Images/Fig29_protocol_rebuild_model_7.svg
      :alt: XXXXXXXXXXXXXXXXXXXXX
      :name: model_building_fig29_rebuild
      :align: center
      :width: 100.0%

      XXXXXXXXXXXXXXXXXXXXX


