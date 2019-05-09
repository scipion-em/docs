.. _user-documentation:

Tutorials
=========

Introduction to Scipion
-----------------------

.. figure:: https://github.com/I2PC/scipion/wiki/images/12.VolumeChimera.png
   :align: right
   :height: 96
   :alt: 12.VolumeChimera.png

This tutorial provides a quick
introduction to processing with Scipion. It is designed to take a
short time while illustrating the main concepts. The tutorial uses 3
micrographs from the Grigorieff `BPV
dataset <http://grigoriefflab.janelia.org/papillomavirus>`__. A final
virus 3D map is obtained.

| *Guide*:
  `scipion\_tutorial\_intro.pdf <https://github.com/I2PC/scipion/wiki/tutorials/scipion_tutorial_intro.pdf>`__


Initial model estimation
------------------------

.. figure:: https://github.com/I2PC/scipion/wiki/images/00.ReconstructedVolume.png
   :align: right
   :height: 96
   :alt: 00.ReconstructedVolume.png

This tutorial uses different methods to
obtain an initial 3D map. Methods covered are RCT, Ransac, Eman and
Reconstruct Significant.

*Guide*:
`scipion\_tutorial\_initialvolume.pdf <https://github.com/I2PC/scipion/wiki/tutorials/scipion_tutorial_initialvolume.pdf>`__\ 

Mix-and-match in Scipion
------------------------
.. figure:: https://github.com/I2PC/scipion/wiki/images/betagal.png
   :align: right
   :height: 96
   :alt: 00.ReconstructedVolume.png

This tutorial presents a more complete
workflow of Cryo-EM single particles inside Scipion. It is focused on
demonstrate the combination of different EM-packages. This tutorial
follows the processing pipeline described for Relion 1.3 tutorial with
Beta-galactosidase data. \

*Guide*:
`scipion\_tutorial\_betagal.pdf <https://github.com/I2PC/scipion/wiki/tutorials/scipion_tutorial_betagal.pdf>`__

You may download a fully solved project of this tutorial from
`here <http://scipion.cnb.csic.es/downloads/scipion/data/FEICourse.tgz>`__.

Model Building
--------------
.. figure:: https://github.com/I2PC/scipion/wiki/images/modelbuilding.png
   :align: right
   :height: 96
   :alt: 00.ReconstructedVolume.png

The recent development of single-particle electron
cryo-microscopy (cryo-EM) allows structures to be solved at almost
atomic resolutions. Providing a basic introduction to model building,
this tutorial shows a workflow aimed at obtaining high-quality atomic
models from cryo-EM data by using scipion software
framework..

*Guide*:
`scipion\_tutorial\_modelBuilding.pdf <https://github.com/I2PC/scipion/wiki/tutorials/tutorial_model_building_basic.pdf>`__\ 

*Workflow*:
`download <http://workflows.scipion.i2pc.es/workflow_detail/36/atom-struct-modeling-demo/>`__\ 

Initial volume validation by SAXS
---------------------------------
.. figure:: https://github.com/I2PC/scipion/wiki/images/12.VolumeChimera.png
   :align: right
   :height: 76
   :alt: 00.ReconstructedVolume.png

This tutorial provides a guide to
the validation of the initial volume estimations using SAXS curves in
Scipion.

*Guide*:
`scipion\_tutorial\_SAXS.pdf <https://github.com/I2PC/scipion/wiki/tutorials/tutorial_SAXS.pdf>`__\ 


Full processing video tutorial
------------------------------
4 video tutorials in a
`list <https://www.youtube.com/watch?v=LAwe9DroypI&list=PLyJiuGnB9hAyxHotd--gKMzCRFpXrSo15>`__
to go from movies to a 3D volume using betagalactosidase data.



Graphical interface manuals
===========================

The following guides show you how to perform certain actions using the GUI, like
a general project navigation, installing plugins, pick particles...

.. toctree::
    :maxdepth: 1

    scipion-gui
    plugin-manager
    picker


ShowJ
-----------
`ShowJ <showJ>`__: The default viewer for Scipion objects. It can
display data in gallery and table modes and navigate through
different blocks of data. Single images are opened using Image
Window.


Particle Picker
---------------
`Particle Picker <picker>`__: The Xmipp Particle Picker allows the
user to iterate over the micrographs to pick particles either
manually or automatically, or visualize them. It is the default
viewer for Scipion coordinates.

Processing How To's
===================

Importing Data
--------------------
`Importing Data <importingData>`__: Importing data is the first step
for any Scipion project. Find out how to import movies, micrographs,
CTFs, and particles and which are the formats currently supported.

Creating subsets
----------------------
`Creating subsets <protUserSubSet>`__: Find out how to create subsets
from micrographs, particles, volumes or from 2D/3D classifications.
This tool is valid for results from any package.

.. TODO: How to create 2D masks
.. ----------------------------
.. `How to create 2D masks <Create2DMask>`__: Guide to creating 2D
.. masks, either interactively or through protocols.

FAQ
---------
`FAQ <faq>`__: Frequently Asked Questions


Troubleshooting
---------------------
`Troubleshooting <troubleshooting>`__

Relion in Scipion
-----------------------
`Relion in Scipion <relion-in-scipion>`__: Check how to use Relion inside Scipion.
Some of the original Relion FAQ are addressed.

