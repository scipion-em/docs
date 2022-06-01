.. _introductionToModelWithAlphaFold:

Introduction to Model building with AlphaFold
=============================================

Model building is the process that allows getting the atomic
interpretation of an electron density map. Although an electron density volume can be obtained from different methodologies, in this tutorial we focus on maps obtained by cryo-EM.
AlphaFold predicts the three-dimensional struture of a protein based exclusively on its amino acid sequence using a deep learning system algorithm :cite:p:`jumper2021`, even if no homologous structures are available. 

With this tutorial we are going to learn how to:

-  generate a prediction model using AlphaFold, 

-  process this prediction model removing the low confidence residues,
 
-  fit the remaining high confidence residues in the 3D density map,

-  morph the predicted model onto the docked fragments and then, fill in or rebuild the missing parts of the model in the map density.


The Specimen used in this tutorial will be the protein 
with UniProt ID `Q9BXJ8 <https://www.uniprot.org/uniprot/Q9BXJ8>`_ known  as TACAN. TACAN is an ion channel-like protein that may be involved in sensing mechanical pain and form dimers :cite:p:`tacan`. This protein has been solved recently by electron micrsoopy at 3.66Å resolution (see `EMDB 30495 <https://www.ebi.ac.uk/emdb/EMD-31482>`_ ). There is an atomic model available at PDBe (ID= 7CXR ` <https://www.ebi.ac.uk/pdbe/entry/pdb/7cxr>`_ ) with release date 16-Feb-2022.


   .. figure:: Images/tacan.png
      :alt: Atomic model for the human TACAN dimer protein.
      :name: model_building_tacan
      :width: 50.0%
      :align: center

      Atomic model for the human TACAN dimer protein (EMDB map 30495) obtained using the AlphaFold.

In this tutorial we will assume that only the 3D map and the sequence are known.

