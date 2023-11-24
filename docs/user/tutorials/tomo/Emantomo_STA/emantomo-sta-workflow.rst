.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _emantomo-sta-workflow:

=============================================================
Tutorial - Subtomogram averaging with EMAN plugin for Scipion
=============================================================

.. contents:: Table of Contents

List of Abbreviations
=====================

* STA: subtomogram averaging.
* PPPT: per-particle per-tilt.
* TS: tilt series.
* CTF: contrast transfer function.

Introduction
============

This tutorial illustrates how to carry out a subtomogram averaging (STA) with a per-particle per-tilt (PPPT) approach
using EMAN_ plugin for Scipion combined with others, listed below for each step:

1. Import the tilt series (TS) - scipion-em-tomo_

2. Contrast transfer function (CTF) estimation - scipion-em-imod_

3. TS alignment and tomogram reconstruction - scipion-em-emantomo_

4. Import the 3D coordinates - scipion-em-tomo_

5. Generate the initial model - scipion-em-emantomo_

6. Subtomograms refinement - scipion-em-emantomo_


The dataset
-----------

The dataset used for this tutorial is a subset of EMPIAR-10064_, concretely the TS named mixedCTEM_tomo4.mrc. The
dataset also includes:

* The estimated CTF, carried out with scipion-em-gctf_ and converted with Scipion into IMOD_ CTF format to import it using the corresponding protocol from the plugin scipion-em-imod_.

* A subset of 200 particles picked with crYOLO_ inside Scipion (protocol from the plugin scipion-em-sphire_).

To download the dataset, simply execute in a terminal the following command:

.. code-block::

    scipion3 testdata --download emantomo_tutorial_ribo

The dataset will be downloaded to SCIPION_HOME/data/tests.


Associated resources
--------------------

Here you can find resources associated with this content, like videos or presentations used in courses and other
documentation pages:

* :ref:`Scipion tutorial <scipion-gui>`


Preparing the project
=====================
First of all, open a terminal and execute the command

.. code-block::

    scipion3

to run Scipion. After that:

1. Click on button "Create Project".

2. Write a name for it. We'll name it *Day_3_emantomo_sta*.

3. Click on button "Create".

.. figure:: /docs/user/tutorials/tomo/Emantomo_STA//00_create_project.png
   :width: 500
   :align: center
   :alt: Create Project

Note: the protocols can be located on the left panel of the project interface or directly search via ctrl + f and typing
the keywords that may represent what it is desired to be found, like a plugin name, a protocol name, an action, etc.


.. _Importing the TS:

Importing the TS
================
Let's begin importing the TS. This is the entry point to Scipion, in which external data files are represented as
Scipion objects, that is a common representation of the data used to make all the different packages speak to each
other. To do that, simply look for a protocol named "tomo - import tilt-series" and click on it. On the tab "Import",
fill the following parameters with the corresponding values listed below:

* Files directory: SCIPION_HOME/data/tests/emantomo_tutorial_ribo
* Pattern: {TS}.mrc
* Tilt angles range: from -58 to 58 with a step of 2
* Micorscope voltage (kV): 300
* Pixel size (sampling rate) Å/px: 2.62
* Tilt axis angle (deg.): -3.4
* Dose (electrons/sq.Å) -> Dose per tilt image: 1.7

Leave the rest of the parameters with the default values and click on "Execute" button.

.. figure:: /docs/user/tutorials/tomo/Emantomo_STA/01_import_ts.png
   :width: 500
   :align: center
   :alt: Import TS form

The imported data can be now visualized by clinking on button "Analyze Results", located on the top right corner of the
bottom panel. This will generate an auxiliary window which will list the TS contained in the set imported. In our case,
there is only one TS. To open it with IMOD_ viewer 3dmod (integrated as part of plugin scipion-em-imod_), simply
double click on it.

.. figure:: /docs/user/tutorials/tomo/Emantomo_STA/02_ts_view.png
   :width: 700
   :align: center
   :alt: Import TS result

.. _Importing the CTF:

Importing the CTF
=================
In this step, we are going to use the protocol called "imod - Import tomo CTFs" from plugin scipion-em-imod_. Once the
protocol form is on the screen, fill the following parameters with the values listed below:

* Files directory: SCIPION_HOME/data/tests/emantomo_tutorial_ribo
* Patterns: *.defocus
* Input tilt-series: to get the pointer to the TS previously imported, click on the magnifier icon. This action will open an auxiliary window which will lists the existing objects of the same type as expected.

.. figure:: /docs/user/tutorials/tomo/Emantomo_STA/03_import_ctf_form.png
   :width: 500
   :align: center
   :alt: Import CTF form

Again, the results can be displayed by clicking on the "Analyze Results" button. The default viewer in this case is the
CTF estimation viewer contained in plugin scipion-em-tomo_, that looks like as shown in the figure below:

.. figure:: /docs/user/tutorials/tomo/Emantomo_STA/04_ctf_view.png
   :width: 850
   :align: center
   :alt: Import CTF result

TS alignment and tomogram reconstruction
========================================

Let's open the protocol named "emantomo TS align & tomo rec" from plugin scipion-em-emantomo_. Fill it with the
following values:

* Parallel --> Threads: 12

*Tab Input:*

* Tilt Series: select the corresponding object using the magnifier icon.

*Tab TS alignment:*

Leave all the parameters with the default values.

*Tab Tomogram reconstruction:*

* Expert level: Advanced
* Thickness (pix.): 96
* Correct rotation: Yes
* Extra pad: Yes

Leave the rest of the parameters with the default values.

.. figure:: /docs/user/tutorials/tomo/Emantomo_STA/05_align_ts_tomo_rec_form.png
   :width: 1000
   :align: center
   :alt: Align TS and tomo rec form

Let's have a look at the tomogram reconstructed. To do that, right-click on the tomograms output listed in the summary
tab located on the lower half of the project main window and select "Open with ImodViewer".

.. figure:: /docs/user/tutorials/tomo/Emantomo_STA/06a_imod_open_viewer.png
   :width: 400
   :align: center
   :alt: Open IMOD viewer


Then, a new window containing the list of tomograms (only one in this case) will be generated. Double click on it to
launch the selected viewer with that data. It should look like the figure below:

.. figure:: /docs/user/tutorials/tomo/Emantomo_STA/06b_imod_viewer_tomogram.png
   :width: 500
   :align: center
   :alt: Tomogram displayed with IMOD viewer


Importing the 3D coordinates
============================
To import the provided coordinates, open the protocol named "tomo - import 3D coords from scipion" from the plugin
scipion-em-tomo_. Fill the following parameters with these values:

* Scipion sqlite file: SCIPION_HOME/data/tests/coordinates.sqlite
* Input tomogras: select the corresponding object from the list displayed after having clicked on the magnifier icon.
* Box size [pix]: 36

.. figure:: /docs/user/tutorials/tomo/Emantomo_STA/07_import_coords_form.png
   :width: 500
   :align: center
   :alt: Import coordinates form

Let's use tho do that, right-click on the output object listed in the project's summary panel, and select "Open with
Eman":

.. figure:: /docs/user/tutorials/tomo/Emantomo_STA/08_emantomo_open_viewer.png
   :width: 400
   :align: center
   :alt: Open EMAN viewer

On the list displayed, double click on the set of coordinates listed. They should look like this:

.. figure:: /docs/user/tutorials/tomo/Emantomo_STA/09_eman_viewer_coords.png
   :width: 1000
   :align: center
   :alt: Coordinates displayed with EMAN viewer

*Note:*

Once the viewer is closed, a new window will appear to ask if you want to save the protocol output. It is because some
viewers, like this one, allow the user to add or remove elements (coordinates in this case). In nothing was changed or
you don't want to save the changes done from the viewer, simply select "No".

Particle extraction from the TS
===============================
This protocol uses the CTF estimation, TS alignment and coordinates data to go back to the TS and crop an image for
each particle for each tilt image (PPPT approach) and the uses them to reconstruct a 3d particle. To carry out this
step, let's open the protocol "emantomo - Extraction from TS" from plugin scipion-em-emantomo_ and fill the following
parameters with the values listed below:

* Threads: 12
* Expert Level: Advanced
* Coordinates: select the corresponding object clicking on the magnifier button.
* CTF tomo series: select the corresponding object clicking on the magnifier button.
* Tilt series with alignment, non-interpolated: clicking on the magnifier icon will display a list of two available objects, which correspond to the imported TS and the TS with alignment data from the previous step. This is the one that must be selected, that should appear the first in the list.
* Flip Z axis in tomogram? No
* Box size unbinned (pix.): 144
* Binning factor: 4 (thus, the generated particles box size will be 144 / 4 = 36 pix.).
* Contrast threshold for 2D particle removal: 0.5 (remove gold beads).
* Minimum distance between particles (Å): 150 (as 300Å is the highest ribosome size value from its size ranges).


.. figure:: /docs/user/tutorials/tomo/Emantomo_STA/10_extract_particles_from_ts_form.png
   :width: 550
   :align: center
   :alt: Extract particles from TS form

The best way to check if the particles were correctly referred to the TS is to display with the IMOD_ viewer the
generated result called projected2DCoordinates. It will show the extracted particles over the TS, as can be observed in
the figure below:

.. figure:: /docs/user/tutorials/tomo/Emantomo_STA/11_tilt_particles_with_imod_viewer.png
   :width: 500
   :align: center
   :alt: Tilt particles displayed with IMOD's viewer

Also, the generated subtomograms can also be displayed. Let's select in this case, the Scipion metadata viewer. It
should look like as shown in the figure below:

.. figure:: /docs/user/tutorials/tomo/Emantomo_STA/12_subtomograms_displayed_with_scipion.png
   :width: 500
   :align: center
   :alt: Subtomograms displayed with Scipion metadata viewer

Generate the initial volume
===========================
Once we have the particles extracted, it's time to calculate an initial volume with them. To do that, open the protocol
named "emantomo - Initial model pppt" rom plugin scipion-em-emantomo_ and fill the following as listed below:

* Threads: 12

*Tab Input*

* Particles: select the corresponding object by clicking on the magnifier icon.
* Reference volume (opt.): leave this empty.

*Tab Optimization*

* No. iterations: 10
* Leave the rest of the parameters with the default values.

.. figure:: /docs/user/tutorials/tomo/Emantomo_STA/13_initial_volume_form.png
   :width: 800
   :align: center
   :alt: Initial volume form

The generated output will be a set of averages, one for each class specified. In this case there will be only one as
the number of classes introduced in the protocol form was 1. Sometimes it can be very useful to specify more than one
class even if there is only one class, and then select the best one, as sometimes the convergence is not reached and
the result is not good. On the other hand, the higher number of classes introduced, the longer it will take the
protocol to finish. Said that, let's open our initial model, in this case with ChimeraX_. It should look like as
in the figure below:

.. figure:: /docs/user/tutorials/tomo/Emantomo_STA/14_initial_volume_chimerax.png
   :width: 500
   :align: center
   :alt: Initial volume displayed with ChimeraX_

Subtomogram refinement
======================
Finally, let's use the generated initial model and the extracted subtomograms to generate a refined average. To do that,
let's open the protocol "emantomo - subtomogram refinement pppt" from the plugin scipion-em-emantomo_, and fill the
following parameters with the values specified below:

* Threads: 12

*Tab Input:*

* Particles: use the magnifier icon and select the particles extracted from the TS.
* Reference volume (opt.): again, click on the magnifier icon and select the item 1 from the set of averages generated in the previous protocol.

.. figure:: /docs/user/tutorials/tomo/Emantomo_STA/15_select_item_from_set.png
   :width: 400
   :align: center
   :alt: Select item from set

*Tab Refinement:*

* 3D map filtering: local

Leave the rest of the parameters with the default values.

Regarding the parameter "Iteration information" in the tab "Refinement", it admits combinations of four types of
refinements, which are:

* p: 3d particle translation-rotation.
* t: subtilt translation.
* r: subtilt translation-rotation.
* d: subtilt defocus.

The default value is p,p,p,t,p,p,t,r,d. It can be compacted using the corresponding character followed by the
desired number of iterations of that type, e. g., p3 = p,p,p.

.. figure:: /docs/user/tutorials/tomo/Emantomo_STA/16_subtomogram_refinement_form.png
   :width: 800
   :align: center
   :alt: Subtomogram refinement form

This protocol generates 3 outputs, that are:

* The refined average.
* The refined subtomograms.
* The FSC curves.

Let's display it:

* The refined average, using ChimeraX_:

.. figure:: /docs/user/tutorials/tomo/Emantomo_STA/16_refined_avg_chimerax.png
   :width: 500
   :align: center
   :alt: Refined average displayed with ChimeraX_

* The refined subtomograms, displayed with Scipion metadata vierwer:

.. figure:: /docs/user/tutorials/tomo/Emantomo_STA/17_refined_subtomos_scipion_viewer.png
   :width: 500
   :align: center
   :alt: Refined subtomograms displayed with Scipion metadata vierwer

* The FSC curves, displayed with Scipion FSC viewer.

.. figure:: /docs/user/tutorials/tomo/Emantomo_STA/18_fsc_curves_scipion.png
   :width: 500
   :align: center
   :alt: Refined subtomograms displayed with Scipion metadata vierwer

Tutorial workflow template
==========================
The processing workflow followed in this tutorial can be executed as a Scipion template by executing the following
command in a terminal:

.. code-block::

    scipion3 template

And then selecting the one named 2023_12_emantomo_sta_tutorial_workflow.

.. figure:: /docs/user/tutorials/tomo/Emantomo_STA/19_scipion_template_gui.png
   :width: 650
   :align: center
   :alt: Scipion template GUI

It will generate a Scipion project with all the protocols and parameter values of each used in this tutorial.


.. _Scipion: http://scipion.i2pc.es/
.. _IMOD: https://bio3d.colorado.edu/imod/
.. _EMAN: https://blake.bcm.edu/emanwiki/EMAN2
.. _crYOLO: https://cryolo.readthedocs.io/en/stable/
.. _ChimeraX: https://www.cgl.ucsf.edu/chimerax/
.. _scipion-em-tomo: https://github.com/scipion-em/scipion-em-tomo
.. _scipion-em-imod: https://github.com/scipion-em/scipion-em-imod
.. _scipion-em-emantomo: https://github.com/scipion-em/scipion-em-emantomo
.. _scipion-em-gctf: https://github.com/scipion-em/scipion-em-gctf
.. _scipion-em-sphire: https://github.com/scipion-em/scipion-em-sphire
.. _EMPIAR-10064: https://www.ebi.ac.uk/empiar/EMPIAR-10064/
