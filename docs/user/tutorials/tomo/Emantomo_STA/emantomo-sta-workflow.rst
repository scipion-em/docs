.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

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
   :width: 400
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

.. figure:: /docs/user/tutorials/tomo/Emantomo_STA/01_ts_view.png
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
   :width: 700
   :align: center
   :alt: Import CTF result

TS alignment and tomogram reconstruction
========================================




*TEMPLATE!*

*SUMMARY:*

That was the last point of this tutorial. If we perform some subtomogram averaging (STA) steps membrane alignment,
particle alignment and subtomogram reconstruction), we can obtain a structure for our ribosomes.


.. _Scipion: http://scipion.i2pc.es/
.. _IMOD: https://bio3d.colorado.edu/imod/
.. _EMAN: https://blake.bcm.edu/emanwiki/EMAN2
.. _crYOLO: https://cryolo.readthedocs.io/en/stable/
.. _scipion-em-tomo: https://github.com/scipion-em/scipion-em-tomo
.. _scipion-em-imod: https://github.com/scipion-em/scipion-em-imod
.. _scipion-em-emantomo: https://github.com/scipion-em/scipion-em-emantomo
.. _scipion-em-gctf: https://github.com/scipion-em/scipion-em-gctf
.. _scipion-em-sphire: https://github.com/scipion-em/scipion-em-sphire
.. _EMPIAR-10064: https://www.ebi.ac.uk/empiar/EMPIAR-10064/
