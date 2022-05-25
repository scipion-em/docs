.. _`app:alphafoldPredictionProtocol`:

AlphaFold2 Initial Model Prediction protocol
===========================================

*ChimeraX*-based protocol designed to get AlphaFold2 :cite:p:`jumper2021` atomic structure predictions. Although included in the **scipion-em-chimera** plugin, the protocol **chimerax-alphafold prediction** allows to use, in addition to *ChimeraX* `tools <https://www.rbvi.ucsf.edu/chimerax/data/alphafold-nov2021/af_sbgrid.html>`_, the *PHENIX* `options <https://phenix-online.org/documentation/reference/alphafold.html>`_ to access to Google Colab notebook system.

-  | Requirements to run this protocol and visualize results:

   -  | *Scipion* plugin: **scipion-em**

   -  | *Scipion* plugin: **scipion-em-chimera**

-  | *Scipion* menu: *Model building -> Initial model* (:numref:`model_building_app_protocol_alphafold_prediction_1` (A))

   .. figure:: Images_appendices/Fig6_alphaFoldPrediction.svg
      :alt: Protocol **chimerax-alphafold prediction**. A: Protocol location in *Scipion* menu. B: Protocol form to retrieve AlphaFold2 structure predictions from EMDB (identical sequence). C: Protocol form to retrieve AlphaFold2 structure predictions from EMDB (homologous sequence) D: Protocol form to predict atomic structures using Google Colab notebooks to run AlphaFold2. E: Protocol form to predict atomic structures running AlphaFold2 in your own computer.
      :name: model_building_app_protocol_alphafold_prediction_1
      :align: center
      :width: 100.0%

      Protocol **chimerax-alphafold prediction**. A: Protocol location in *Scipion* menu. B: Protocol form to retrieve AlphaFold2 structure predictions from EMDB (identical sequence). C: Protocol form to retrieve AlphaFold2 structure predictions from EMDB (homologous sequence). D: Protocol form to predict atomic structures using Google Colab notebooks to run AlphaFold2. E: Protocol form to predict atomic structures running AlphaFold2 in your own computer.

-  | Protocol form parameters (:numref:`model_building_app_protocol_alphafold_prediction_1` (B, C, D, E)):

   | *Input* section:

   -  | *Input 3D Map*: I

   -  | *Select the operation to perform*: 

      -  | *Subtraction*: 


