.. _introductionToModelWithAlphaFold:

Introduction to Model building with AlphaFold
=============================================

Model building is the process that allows getting the atomic
interpretation of an electron density map. Although an electron density volume can be obtained from different methodologies, in this tutorial we focus on maps obtained by cryo-EM.
AlphaFold predicts the three-dimensional struture of a protein based exclusively on its amino acid sequence using a deep learning system algorithm :cite:p:`jumper2021`, even if no homologous structures are available. 

With this tutorial we are going to learn how to:

-  | a) generate a prediction model using AlphaFold, 

-  | b) process this prediction model removing the low confidence residues,
 
-  | c) fit the remaining high confidence residues in the 3D density map,

-  | d) morph the predicted model onto the docked fragments and then, fill in or rebuild the missing parts of the model in the map density.


