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

5. Directional picking (preseg, graphs, filaments and picking) - scipion-em-pyseg_

6. Remove duplicates (filter picked particles by distance) - scipion-em-tomo3d_

7. Extract particles - scipion-em-emantomo_

8. 2D classification and rot angle randomization - scipion-em-pyseg_

9. Generate an initial model - scipion-em-reliontomo_

Thus, 8 different plugins will be used in this tutorial, highlighting the power of Scipion in terms of interoperability.


.. contents:: Table of Contents

Associated resources
====================

Here you can find resources associated with this content, like videos or presentations used in courses and other
documentation pages:

`Basic actions with Scipion <https://scipion-em.github.io/docs/docs/user/scipion-gui.html#scipion-gui>`_

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


.. _Importing the Tomogram:

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
   :width: 700
   :alt: Import tomogram result

.. _Tomogram normalization:

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

The denoised tomogram can be displayed proceeding the same as explain in section `Importing the Tomogram`_. It can be observed
how the contrast has been considerably increased, being the figure on the left the tomogram before the denoising and
the one on the right after the denoising.

.. figure:: /docs/user/denoising_mbSegmentation_pysegDirPicking/03_res_DenoiseTomo.png
   :width: 1000
   :alt: Denoise tomogram result

Membrane segmentation
=====================

Membrane segmentation and annotation constitute the pre-processing steps for the membrane particles picking with PySeg.
The first step will be carried out with protocol "tomogram segmentation" from plugin scipion-em-tomosegmemtv. Open the
protocol mentioned and follow the steps listed and illustrated below:

1. Click on Advanced radio button. This action is present in all the protocols that offer advanced parameters and its
used to show them.

2. Select the denoised tomogram pointer in field "Input tomograms".

3. Set the "Membrane thickness" parameter to *1* voxel. This is a good and recommended strategy to get the membranes closer
to an over-detection scenario than the opposite, which would be the resulting scenario with higher values. In our case,
this is the best way to proceed, due to the fact that we're going to annotate the membranes in the next step with the
Membrane Annotator tool, which provides residual structures cleaning tools. Hence, with a low value of this parameter,
we'll obtain less discontinuities in the membranes, but more false positives. The first condition takes to a simpler
annotation step in one or two steps per vesicle instead of having to annotate part by part in case of many
discontinuities. On the other side, the false positives can be easily removed with the annotation tool.

4. Set the parameter "Membrane scale factor" to *8* voxels. This parameter is used to define the effective neighbourhood
of the membranes considered in the calculations (voting process). Hence, this value is recommended to be low for thin
membranes and high for thick membranes, and considering the sampling rate of the tomograms whose vesicles are going to
be segmented.

5. Set the parameter "Membrane strength threshold" to *0.01*. This parameter is used to tune the amount of output
membrane points and remove false positives. Lower values will provide more membrane points, at the risk of generating
false positives. Thus, this is a critical value when an annotation step is going to be carried out, because a very low
value will make most of the structures found in the tomogram to be connected, so it won't be possible to annotate them
separately. On the other hand, higher values will provide a higher probability of the structures to be disconnected,
but if the value is too high more discontinuities may be present in the structures detected.

6. Set the parameter "Sigma for the initial gaussian processing" to *0.5*. The input tomogram is subjected to an
initial Gaussian filtering aiming at reducing the noise so as to determine the derivatives more robustly. By default,
a standard deviation of 1.0 voxel is considered. If the membranes are very thin or are very close to each other,
use lower values (e.g. 0.5).

7. Set the parameter "Keep all the generated files" to *Yes* to save all the intermediate results obtained in the
different steps carried out internally by tomosegmemTV.


.. figure:: /docs/user/denoising_mbSegmentation_pysegDirPicking/04_MembranesSegmentation.png
   :width: 500
   :alt: Vesicles segmentation

Note: in this example all the parameter values provided have been tuned previously, but in the normal scenario consists
of some executions until getting the desired result. Even more, sometimes it is necessary to go back from the membrane
annotator to tune some parameter to, for example, get the membranes less connected. On the other hand, it is
recommended to keep all the files when you are not familiarized with the algorithm so, if the membranes get lost in the
final result, the intermediate results can be analyzed to determine when they got lost and, as a consequence, know
know which parameter should be tuned. For a more detailed explanation, click HERE --> AÑADIR REFERENCIA A TEORÍA DE
TOMOSEGMEMTV.

The result obtained should look like the figure below.

.. figure:: /docs/user/denoising_mbSegmentation_pysegDirPicking/04_res_MembranesSegmentation.png
   :width: 500
   :alt: Vesicles segmentation result

Hint: the recommended procedure is to work with one or two tomograms of the set to tune the parameters and then use
that configuration with all the set.

Membrane annotation
===================

Once the membranes have been successfully segmented, they need to be annotated, which means to manually add a numerical
label to each to indicate the software that they represent different entities. This step will be carried out with the
protocol "annotate segmented membranes" from plugin scipion-em-tomosegmemTV. This is an interactive protocol which
generate an auxiliary window that lists the tomograms to be annotated and allow the user to execute the membrane
annotator tool by double clicking on it. It also indicates which of them have been annotated and which are still
pending to be processed. The only parameter present in this protocol is the pointer to the tomomasks (segmentations).

Note: It may take a few seconds to be displayed after double clicking on one tomogram from the list shown in the
auxiliary window.

.. figure:: /docs/user/denoising_mbSegmentation_pysegDirPicking/05_MembranesAnnotation.png
   :width: 1000
   :alt: Vesicles annotation

Membrane Annotator overview
---------------------------

The following subsections will describe how to use the membrane annotation tool. But before that, let's have a quick
look at its interface and components:

.. figure:: /docs/user/denoising_mbSegmentation_pysegDirPicking/05_MembranesAnnotator_overview.png
   :width: 650
   :alt: Membrane Annotator overview

Here is a brief explanation of each of the component enumerated in the figure above:

1. Tools shortcuts: it offers useful functionalities to work with the structures found in the loaded tomogram, like the
zoom in/out or the click and drag.

2. Density thresholding tools: the thresholding is the starting point of every labelling procedure. It's value can be
updated using the slider or introducing a value in the corresponding textbox.

3. Z slice navigation tools: another textbox and another slider are provided to navigate through the Z slices of the
tomogram and locate all vesicles desired to be annotated.

4. View panel: it allows to visualize different representations of the loaded data:

    4.1 Original - current tomogram data

    4.2 Filter - input of the density thresholding operations.

    4.3 Threshold - output of the density thresholding operations.

    4.4 Label - Result of "Update Labels" operation (assign to each structure a label which is its size in voxels.

    4.5 Material - Result of the manual labelling. It shows the annotated membranes with the assigned value.

5. Crop panel: it can be used to crop the tomogram oroviding the X, Y and Z ranges and clicking in button "Update".

6. Size Threshold panel: it can be used to perform three different operations:

    6.1 Update Labels: automatic labelling of the structures found depending in the density threshold value. It assigns,
        by default, the size of each structure as label. It will update the view to the view "Label".

    6.2 Display Cursor: it's used to check the size of each structure. One click on it will activate the cursor mode,
        which will display the value of the pixel selected. To finish this cursor mode, click again on the previous
        button, whose name will be now "Stop Cursor". This functionality is very useful to determine if, for example,
        the different parts of a discontinuous structure have been detected as parts of the same structure of not and
        manually annotate them coherently.

    6.3 Size Thresholding: it can be used to remove undesired sizes of structures, like the ones which are too small.
        To do that, simply introduce a size value in the textbox and click on the button "S. Th.".

7. Set Material panel: it works like the "Display Cursor" functionality explained in 6.2, but to annotate the desired
structures. To do that, click on button "Display Cursor" to activate the cursor mode. Then select a structure by
clicking on it (until here it's the same as before) and finally introduce a value in the corresponding textbox before
clicking again on the cursor button (renamed to "Change Lbl.") to stop it and automatically execute the labelling of
the selected structure, shown in view "Material".

8. Results panel: it has two buttons, one to save the automatic size labels calculated when clicking on button "Update
Labels" and the other to save the manually annotated structures. IMPORTANT: working from Scipion, this step is required
to be carried out once all the desired vesicles have been annotated.

9. Log panel: it registers the main actions that have been carried out by the user.

10. Tomogram file name: informative.

11. Data visualization panel.

Target vesicles
---------------
It can be observed that three of the vesicles (squared in the figure below) contain most of the membrane ribosomes.
These are the ones we're going to annotate.

.. figure:: /docs/user/denoising_mbSegmentation_pysegDirPicking/05_MembranesAnnotator_targets.png
   :width: 650
   :alt: Membrane Annotator targets

Density thresholding
--------------------
First of all, let's set the density threshold value [2] to *0.05*. This value offers a clean and continuous view of the
different structures present in the loaded tomogram.

Hint: to get an intuition of how the variations in the density threshold value affects the data, it's very recommendable
to test different values until a promising visualization is obtained.

.. figure:: /docs/user/denoising_mbSegmentation_pysegDirPicking/05_MembranesAnnotator_thresholding.png
   :width: 650
   :alt: Membrane Annotator thresholding

To check the results, click on button "Update Labels" [6]. The result of this operation should look like as the figure
below. It can be observed that the segmentation and density thresholding values were correctly determined because all
the target structures present different colors, which means different sizes. In some cases, like in target 1, there are
two or more different colors (sizes) for the same vesicle, but this is more than normal in the case of our data (in
situ tomogram). This can be solved annotating the different parts with the same label.

.. figure:: /docs/user/denoising_mbSegmentation_pysegDirPicking/05_MembranesAnnotator_autoLabel.png
   :width: 650
   :alt: Membrane Annotator update labels

On the other hand, it's recommendable to check that both parts of target 2 are of the same size. It can be easily done
with the button "Display Cursor" from panel "Size Thresholding" [6]. The result is that in this case both parts are of
the same size, which means that most of the whole changing shape through the slices was very well segmented.

.. _Manual annotation of the target 1:

Manual annotation of the target 1
---------------------------------

The first target membrane has been detected in two unconnected parts of different sizes (colors), as shown below (the
size is shown in the index label of the tooltip. The background size will be always 0). It can be observed that target
3 has different size, so it's not connected to the orange part of target 1 and that the blue part of target one can be
annotated with the same label as the orange one to get the full membrane annotated.

.. figure:: /docs/user/denoising_mbSegmentation_pysegDirPicking/05_MembranesAnnotator_target1_1.png
   :width: 650
   :alt: Membrane Annotator target 1 sizes

The procedure followed to check the sizes was:

1. Click on the magnifier with a cross icon from "Tools shortcuts" [1].

2. Create a zoom window clicking and dragging around the target 1 vesicle to zoom in. When the zoom mode is active, it
can be smoothly controlled with the mouse wheel.

3. Click on button "Display Cursor" from panel "Size Threshold" [6] and click on the structure whose size is desired to
be displayed. To fine tune the position of the cursor, use the arrow keys from the keyboard.
Note: to generate multiple tooltips, right click on the current tooltip and select option "Create New Data Tip" or
directly press shift + left click.

4. To finish the cursor mode, click on the same button pressed to activate it, but now called "Stop Cursor".

Let's annotate now the orange part of target one with label 1 (Use the zoom in tool if necessary, as explained before):

.. figure:: /docs/user/denoising_mbSegmentation_pysegDirPicking/05_MembranesAnnotator_target1_2.png
   :width: 650
   :alt: Membrane Annotator target 1 annotation

1. Click on button "Display Cursor" from panel "Set Material" [7].

2. Click on the membrane and, before clicking on the same button (now named "Change Lbl."), be sure that the clicked
pixel belongs to a structure (index must be grater than 0).

3. Leave the textbox "Label" value as 1. If we we annotating the target 2 o target 3 vesicles, this value should have
to be set to 2 or 3, respectively.

4. Finally, click on the button "Change Lbl." to annotate that part of target 1 vesicle with label 1. This action will
display automatically the view "Material" from the panel "View" [4], as can be observed in the figure below.

.. figure:: /docs/user/denoising_mbSegmentation_pysegDirPicking/05_MembranesAnnotator_target1_3.png
   :width: 650
   :alt: Membrane Annotator target 1 material view part

If we repeat this procedure with the blue part of target 1 vesicle (annotatin it with label 1), the result should look
like as shown in the figure below.

.. figure:: /docs/user/denoising_mbSegmentation_pysegDirPicking/05_MembranesAnnotator_target1_4.png
   :width: 650
   :alt: Membrane Annotator target 1 material view full

Manual annotation of the target 2
---------------------------------

Proceeding the same as explain in section `Manual annotation of the target 1`_, it can be observed that the target has
been detected in two different parts (upper part, with a size of 111171 voxels and lower part, of size 10330 voxels),
just the same as what happened with target 1. Moreover, the inner small vesicle and the top left structure are
disconnected from target 2, because they have different sizes (see figure below).

.. figure:: /docs/user/denoising_mbSegmentation_pysegDirPicking/05_MembranesAnnotator_target2_1.png
   :width: 650
   :alt: Membrane Annotator target 2 sizes

Hence, we can proceed to the manual annotation, this time with label 2. The final result of the target 2 vesicle
annotation is shown in the figure below.

.. figure:: /docs/user/denoising_mbSegmentation_pysegDirPicking/05_MembranesAnnotator_target2_2.png
   :width: 650
   :alt: Membrane Annotator target 2 material view full

Manual annotation of the target 3
---------------------------------

This is the easiest one, identified as a continuous structure. So we can directly annotate it with label 3. The result
of the three membranes annotated can be observed in the figure below.

.. figure:: /docs/user/denoising_mbSegmentation_pysegDirPicking/05_MembranesAnnotator_target3.png
   :width: 650
   :alt: Membrane Annotator target 3 material view full

Save the annotated vesicles and finish the interactive annotation protocol
--------------------------------------------------------------------------

To successfully save the results of the annotation, follow the steps enumerated below:

1. Click on button "Save Materials" from panel Results [8].

2. If everything goes fine, the first line of the "Log Panel" [9], should be "Materials were correctly saved".

3. Close Membrane Annotator and check that the status of the tomogram listed in the auxiliary window has been updated
to "DONE". Finally, close the auxiliary window.

4. The protocol box should have now update its state to inactive. If not, refresh the project interface (refresh icon
is located at the top right corner of the project panel).

.. figure:: /docs/user/denoising_mbSegmentation_pysegDirPicking/05_MembranesAnnotator_saveResults.png
   :width: 400
   :alt: Membrane Annotator save results and exit

Analyze the annotated membranes
---------------------------

If we click on button "Analyze Results" in the lower panel of the project interface, the 3D visualization tool from
plugin scipion-em-tomo3d is launched. It allows the user to observe the membranes annotated placed on the full tomogram
or by slices, as shown in the figure below.

.. figure:: /docs/user/denoising_mbSegmentation_pysegDirPicking/05_MembranesAnnotator_tomo3dviewer.png
   :width: 1000
   :alt: Membrane Annotator results with tomo3d

Resize the tomomasks (segmentations)
====================================

After having carried out the segmentation and annotation of the vesicles in a smaller size to improve both performance
and contrast (explained in section `Tomogram normalization`_), the segmented and annotated data must be resied to its
previous size for the picking of the membrane particles (smaller sampling rate will make the picking algorithms easier
and even possible to find the desired densities). This operation will be carried out with protocol "Resize segmented or
annotated volume" from plugin scipion-em-tomosegmemtv. The tomomasks desired to be resized and the tomograms to which
they have to be referred and resized to their size are the arguments required to be filled. Select the pointer to the
annotation protocol output for the first and the pointer to the imported tomogram for the second.

.. figure:: /docs/user/denoising_mbSegmentation_pysegDirPicking/06_resize_tomoMasks.png
   :width: 500
   :alt: Resize tomomasks protocol

We're referring the tomomasks to the imported tomograms and not to the denoised ones to carry out the picking procedure
with the less processed data as possible, for two main reasons:

1. PySeg graphs calculations expect the data not to be filtered, so it will provide the best result with unfiltered
(e. g. not denoised) data.

2. Avoid all the interpolations and mathematical treatment of the data at the pint of identifying small structures,
increasing the probabilities of the picked objects to be a physical entity instead of a mathematical artifact,

*SUMMARY:*

At this point we have the membranes segmented, annotated, at the correct size and referred to the imported tomograms.
Thus, we're ready for the picking.



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
