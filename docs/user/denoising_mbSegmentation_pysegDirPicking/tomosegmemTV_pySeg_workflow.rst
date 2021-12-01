.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _Tutorial-Denoising-Membrane-Segmentation-and-Annotation-and-Directional-Picking:

==================================================================================
Tutorial - Denoising, Membrane Segmentation and Annotation and Directional Picking
==================================================================================

This tutorial covers a part of the full data processing pipeline in cryo electron tomography, concretely from the
tomogram to the initial model generation after having picked the particles. All the data processing has been carried
out in Scipion_, using the plugins listed below for each step:

1. Import tomograms - scipion-em-tomo_

2. Tomogram normalization - scipion-em-imod_

3. Tomogram denoising - scipion-em-jjsoft_

4. Tomogram segmentation, annotation and tomomask (segmemtation) resizing - scipion-em-tomosegmemtv_

5. Assign tomomasks to tomograms - scipion-em-tomo_

6. Directional picking (preseg, graphs, filaments and picking) - scipion-em-pyseg_

7. Remove duplicates (filter picked particles by distance) - scipion-em-tomo3d_

8. Extract particles - scipion-em-emantomo_

9. 2D classification and rot angle randomization - scipion-em-pyseg_

10. Generate an initial model - scipion-em-reliontomo_

Thus, 8 different plugins will be used in this tutorial, highlighting the power of Scipion in terms of interoperability.


.. contents:: Table of Contents

The dataset
===========

The dataset reference used in this tutorial is EMD-10439_, which consists of an in situ tomogram of intact P19 cells
acquired with phase-plate, with a sampling rate of 13.68 Å/voxel and dimensions (X, Y, Z) = (928, 928, 500) pixels.

Preparing the project
=====================
First of all, open a terminal and execute the command scipion3 to run Scipion. After that:

1. Click on button "Create Project".

2. Write a name for it. We'll name it tomo_workshop_2021_tomosegmemTV_pyseg.

3. Click on button "Create".

.. figure:: /docs/user/denoising_mbSegmentation_pysegDirPicking/00_createProject.png
   :width: 400
   :alt: Create Project

Note: the protocols can be located on the left panel of the project interface or directly search via ctrl + f and typing
the keywords that may represent what it is desired to be found, like a plugin name, a protocol name, an action, etc.


.. _ImportTomogram:

Importing the tomogram
======================
Let's begin importing the tomogram. This is the entry point to Scipion, in which external data files are represented as
Scipion objects, which is a common representation of the data used to make all the different packages speak to each
other. To do that, simply look for a protocol named "import tomograms" and click on it. On tab "Import", introduce the
directory in which the tomogram file is located, then the full name or a pattern in the second field and finally the
sampling rate, which is, as mentioned before, 13.68 Å/voxel. Leave the other two tabs with the default values and click
on "Execute" button.

.. figure:: /docs/user/denoising_mbSegmentation_pysegDirPicking/01_ImportTomo.png
   :width: 500
   :alt: Import tomogram

The imported data can be now visualized by clinking on button "Analyze", located on the top right corner of the bottom
panel. This will generate an auxiliary window which will lists the tomograms contained in the set imported. In our case,
there is only one tomogram. To open it with IMOD's viewer 3dmod (integrated as part of plugin scipion-em-imod), simply
double click on it.

.. figure:: /docs/user/denoising_mbSegmentation_pysegDirPicking/01_res_ImportTomo.png
   :width: 500
   :alt: Import tomogram result

Tomogram normalization
=======================
In this step, we are going to divide by two the size of the tomogram in order to make the denoising, segmentation and
annotation steps faster and, in the case of the membranes segmentation and annotation, making it easier to the
algorithm to detect them, because of the enhanced contrast as the binning gets higher. To do that, we are going to use
the protocol called "tomo normalization" from plugin scipion-em-imod. Once the protocol form is on the screen, follow
the steps listed below:

1. To get the pointer to the tomogram previously imported, click on the magnifier icon. This action will open an
auxiliary window which will lists the existing objects of the same type as expected.

2. At this point of the wokflow, we only have the tomogram imported before. Hence, select it.

3. Click on "Select" button.

4. Introduce vale 2 in "Binning" field, to indicate that the resulting tomogram must be half of the size of the input
tomogram. Consequently, the sampling rate of the output tomogram will be the double, as can be observed in the summary
panel at the bottom of the project interface.

.. figure:: /docs/user/denoising_mbSegmentation_pysegDirPicking/02_NormalizeTomo.png
   :width: 650
   :alt: Normalize tomogram

Tomogram denoising
==================

This step is recommended to be carried out before the membrane segmentation, considering that the higher contrast our
data has, the better the membranes will be segmented. To do that, open the protocol "denoise tomogram" from plugin
scipion-em-jjsoft. Once there, click on the magnifier icon and select, on the pop-up window the pointer to the
normalized tomogram (it should be the first on the list, because the objects generated are sorted from newest to
oldest by default). Leave the rest of parameters with the default values and click execute the protocol.

.. figure:: /docs/user/denoising_mbSegmentation_pysegDirPicking/03_DenoiseTomo.png
   :width: 500
   :alt: Denoise tomogram

The denoised tomogram can be displayed proceeding the same as explain in section :ref:`ImportTomogram`. It can be observed
how the contrast has been considerably increased, being the figure on the left the tomogram before the denoising and
the one on the right after the denoising.

.. figure:: /docs/user/denoising_mbSegmentation_pysegDirPicking/03_res_DenoiseTomo.png
   :width: 1000
   :alt: Denoise tomogram result

.. _Scipion: http://scipion.i2pc.es/
.. _scipion-em-tomo: https://github.com/scipion-em/scipion-em-tomo
.. _scipion-em-imod: https://github.com/scipion-em/scipion-em-imod
.. _scipion-em-jjsoft:: https://github.com/scipion-em/scipion-em-jjsoft
.. _scipion-em-tomosegmemtv: https://github.com/scipion-em/scipion-em-tomosegmemtv
.. _scipion-em-pyseg: https://github.com/scipion-em/scipion-em-pyseg
.. _scipion-em-tomo3d: https://github.com/scipion-em/scipion-em-tomo3d
.. _scipion-em-emantomo: https://github.com/scipion-em/scipion-em-emantomo
.. _scipion-em-reliontomo: https://github.com/scipion-em/scipion-em-reliontomo
.. _EMD-10439: https://www.ebi.ac.uk/emdb/EMD-10439?tab=overview
