.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _tomography-tutorials:


Tomogram Reconstruction
-----------------------
The main goal of this tutorial is to illustrate the combination of different tomography software
packages in the same Scipion project.

 *Guide*:
 `Tomogram Reconstruction <https://docs.google.com/document/d/1ESIGTwPyunnelq4zCVrSL1BSqn-Qpf0tCcN-vY_mCtk>`_


Manual Tomogram Reconstruction with etomo
-----------------------------------------
This tutorial shows how Scipion incorporates etomo (scipion-em-imod) and how the tomograms can be manually reconstrutedthewith it, inside a Scipion project.

 *Guide*:
 `Manual Tomogram Reconstruction <https://docs.google.com/document/d/1TvdtTAojfAwSeQMfGdkXWIWTC7vobgicbYTq4aX1-H8>`_

Tomogram Reconstruction and Local Resolution Analysis with MonoTomo
-------------------------------------------------------------------
This tutorial shows how to reconstruct a tomogram in Scipion evaluating its local resolution

 *Guide*:
 `Local Resolution of a Tomogram Reconstruction <https://docs.google.com/document/d/1GfyYaHKaKivptV9wu-nRQSRIiq9onsC-I3qAbv25YUE>`_

Picking Tutorial
-----------------
This page will present the different picking protocols and strategies available in Scipion for Tomography and the Plugins where the various programs can be found.
The tutorial will cover from the picking step to the extraction of the coordinates selected in the tomogram, including some useful tools to complement the protocols involved in the picking workflows.

 *Guide*: :ref:`Picking tutorial <tutorial-picking>`


Denoising, Membrane Segmentation and Annotation and Directional Picking
----------------------------------------------------------------------------------

This tutorial covers a part of the full data processing pipeline in cryo electron tomography, concretely from the
tomogram to the initial model generation after having picked the particles.

 *Guide*: :ref:`Denoising, Membrane Segmentation and Annotation and Directional Picking <tomosegmemtv-pyseg-workflow>`


Subtomogram Averaging Ribosome (Part I)
---------------------------------------

In this tutorial, we will describe a basic workflow that goes
from a tomogram containing purified ribosomes to a subtomogram average of the
ribosome. To achieve this task, we will import the data to Scipion and then,
perform a picking, extraction, classification and subtomogram refinement.

 *Guide*:
 `Subtomogram Averaging Ribosome <https://docs.google.com/document/d/1wH9vCDVbjlkMwGiXB3-BsKfNEr-vKgKDry8CRHch9Yk>`_


Subtomogram Averaging HIV (Part II)
------------------------------------
In this first part of the tutorial, we will follow a workflow from tomogram to
subtomogram averaging. Our objective is to reconstruct a protein of the
capsid of the HIV virus, so our particles will have to maintain the orientation
with respect to the virus internal membrane.

 *Guide*:
 `Subtomogram Averaging HIV <https://docs.google.com/document/d/14hFAyyb19SZsXe1i82NN9RP9VW1ZyCEAJJznnEOeA7Q>`_
