.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _picker:

============
Xmipp Picker
============

Overview
========

The Xmipp picker allows us to iterate over the micrographs to pick
particles either manually or automatically, or visualize them (Fig. 1).
It is the default viewer for Scipion coordinates. It provides different
tools to make easier the picking process. At first, from the picker GUI,
the active micrograph is loaded. In order to pick particles we can navigate
over the micrograph using the mouse right click and zoom in/out the image using
Shift + mouse scroll. After some training we can activate autopick to
pick particles automatically.

.. figure:: /docs/images/guis/picker.png
   :width: 800
   :align: center
   :alt: Picker main GUI

   Fig. 1. Picker main GUI


Toolbar
=======

From the toolbar we can select particle size, color and shapes: circle,
square, center. Also to speed the picking process up we can use the tool
|center-tool|. This tool centers particles automatically, using templates
(see section Window: Particles and Templates). The |zoom-tool| button, when
activated, allows the user to retain magnification and source rectangle when
switching from one micrograph to another.

Menu
====

Import Coordinates
------------------

If we have done some picking before, we can import coordinates from
previous projects. Formats supported include Eman, Relion or Xmipp (Fig.
2). Import can be done from a folder or from files. If import from folder
is used, micrograph coordinates are loaded from the file name that
results from adding the prefix and suffix specified to the micrograph name.
If required, we can also invert X or Y axis, or apply some scale factor
to coordinates.

.. figure:: /docs/images/guis/import.png
    :width: 400
    :align: center
    :alt: Import particles dialog

    Fig. 2. Import particles dialog

Filters
-------

To increase signal to noise ratio, micrographs are filtered using
Gaussian Blur and Enhance Contrast, although different filters can be
applied. Available filters include: Bandpass Filter, Anisotropic
Diffusion, Invert LUT, etc. These filters are part of the ImageJ image
processing software. When selected every time an image is loaded they
are applied. For more advanced operations we can open ImageJ and process
image manually.

Windows: Particles and Templates
--------------------------------

Templates represent the different views of the particles available for a
sample. The user must specify its number so that each template can be
calculated automatically as we pick particles (using cross-correlation)
(Fig. 3). They are used to center particles and to train classifier for
autopicking.


.. figure:: /docs/images/guis/templates.png
    :width: 400
    :align: center
    :alt: Templates

    Fig. 3. Templates

Particles picked can be displayed and centered using particles
window, shown below, since this window provides more detail.

.. figure:: /docs/images/guis/particles.png
    :width: 400
    :align: center
    :alt: Templates

    Figure 4. Particles

Help
----

From the help menu the user can access this url or visualize help tips.

.. figure:: /docs/images/guis/tips.png
    :width: 600
    :align: center
    :alt: Help tips

    Figure 5. Help tips

Autopick
--------

Autopick option allows us to pick particles automatically using Xmipp
classifier. At first it needs to be trained providing a rectangle
(detected automatically) fully picked, containing at least 15 particles.
If previous micrographs have been picked they are also used for
training. Once selected every time a new micrograph is loaded particles
are picked automatically. Particles added or deleted after automatic
picking can be used to correct classifier learning. Particles picked can
be filtered using threshold and explore attributes. Threshold attribute
allows us to dismiss particles based on its score. Explore attribute
allows us to limit the profusion of particles automatically picked.

Output Coordinates
------------------

Finally after we have done some manual/supervised picking and feel
confident with the results we can register output coordinates into
Scipion using Add Coordinates button. An output set of coordinates will
be created as protocol output.


.. |center-tool| image:: /docs/images/guis/center.png
.. |zoom-tool| image:: /docs/images/guis/zoom.png