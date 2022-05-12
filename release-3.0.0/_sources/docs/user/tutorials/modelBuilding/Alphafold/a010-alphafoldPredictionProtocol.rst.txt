.. _`app:alphafoldPredictionProtocol`:

AlphaFold2 Initial Model Prediction protocol
===========================================

*ChimeraX*-based protocol designed to get AlphaFold2 :cite:p:`jumper2021` atomic structure predictions. Although included in the **scipion-em-chimera** plugin, the protocol **chimerax-alphafold prediction** allows to use, in addition to *ChimeraX* `tools <https://www.rbvi.ucsf.edu/chimerax/data/alphafold-nov2021/af_sbgrid.html>`_, the *PHENIX* `options <https://phenix-online.org/documentation/reference/alphafold.html>`_ to access to Google Colab notebook system.

-  | Requirements to run this protocol and visualize results:

   -  | *Scipion* plugin: **scipion-em**

   -  | *Scipion* plugin: **scipion-em-chimera**

-  | *Scipion* menu: *Model building -> Initial model* (:numref:`model_building_app_protocol_alphafold_prediction_1` (A))

   .. figure:: Images_appendix/Fig309.svg
      :alt: Protocol **chimerax-alphafold prediction**. A: Protocol location in *Scipion* menu. B: Protocol form to get AlphaFold2 structure predictions using *ChimeraX* tools. C: *Idem* using *PHENIX* tools. D: Protocol form to subtract an atomic structure from a map. All possible params are shown.
      :name: model_building_app_protocol_alphafold_prediction_1
      :align: center
      :width: 85.0%

      Protocol **chimerax-alphafold prediction**. A: Protocol location in *Scipion* menu. B: Protocol form to get AlphaFold2 structure predictions using *ChimeraX* tools. C: *Idem* using *PHENIX* tools. D: Protocol form to subtract an atomic structure from a map. All possible params are shown.

-  | Protocol form parameters (:numref:`model_building_app_protocol_alphafold_prediction_1` (B,C,D)):

   | *Input* section:

   -  | *Input 3D Map*: I

   -  | *Select the operation to perform*: 

      -  | *Subtraction*: 


