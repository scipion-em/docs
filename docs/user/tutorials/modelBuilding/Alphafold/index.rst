Predicting initial models with AlphaFold
========================================

AlphaFold neural network predicts the 3D coordinates of all heavy atoms for a given protein using solely the primary amino acid sequence as input :cite:p:`jumper2021`. 

In this tutorial we show how to generate AlphaFold models of your sequence and rebuild them using the 3D density map. We use the *Scipion* framework and the approach described in the `PHENIX  <https://phenix-online.org/documentation/reference/alphafold.html>`_ web site and summarized as:


* Get the initial AlphaFold model
* Remove low-confidence residues of the model and break it into compact domains
* Dock the domains obtained in the previous model processing step into your cryo-EM  map or unit cell
* Morph the docked fragments and rebuild the whole predicted model in the map density

Contents
--------
.. toctree::
   :maxdepth: 1
   :numbered:

   005-versionhistory
   007-requirements
   010-introduction
   011-problem2solve
   020-initialModel
   030-processModel
   040-dockModel
   050-rebuildModel

Appendices
----------
.. toctree::
   :maxdepth: 1
   :numbered:

   a010-alphafoldPredictionProtocol
   a020-processPredictedProtocol
   a030-dockPredictedModelProtocol
   a040-rebuildPredictedModelProtocol
   a050-dockAndRebuildProtocol
   
