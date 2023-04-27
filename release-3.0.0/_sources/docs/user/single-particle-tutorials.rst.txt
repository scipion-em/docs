.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _single-particle-tutorials:

Mouse apoferritin image processing in Scipion 3
-----------------------------------------------

.. figure:: /docs/images/Cover_apoferritin.png
   :align: right
   :height: 96
   :alt: Cover_apoferritin.png

This tutorial presents a complete
workflow of Cryo-EM single particles inside Scipion 3. It
demonstrates the combination of different EM-packages with high focus on Xmipp highres. \

*Guide*:

`apoferritin image processing tutorial in scipion3 <../../_static/pdfs/tutotial_scipion3_apoferritin.pdf>`__

You may download a fully solved compressed project (Example_10248_Scipion3.tgz) of this tutorial from
`here <http://scipion.cnb.csic.es/downloads/documentation>`__.

*Workflow*:
`download <http://workflows.scipion.i2pc.es/workflow_detail/36/atom-struct-modeling-demo/>`__\



Relion in Scipion
-----------------

This tutorial is focused on using Relion 4 single particle workflow inside Scipion. It follows the 
processing pipeline described for Relion 4.0 tutorial with
Beta-galactosidase data. \

*Guide*:
`scipion\_tutorial\_relion.pdf <../../_static/pdfs/scipion_tutorial_relion.pdf>`__


Full SPA processing video tutorial
----------------------------------
    4 video tutorials in a
    `list <https://www.youtube.com/watch?v=LAwe9DroypI&list=PLyJiuGnB9hAyxHotd--gKMzCRFpXrSo15>`__
    to go from movies to a 3D volume using betagalactosidase data.

    Part1: Micrograph processing

    .. image:: https://img.youtube.com/vi/LAwe9DroypI/maxresdefault.jpg
        :alt: Part1: Micrograph processing
        :target: https://www.youtube.com/watch?v=LAwe9DroypI

    Part2: Particle picking

    .. image:: https://img.youtube.com/vi/Y1jCY2cZlC0/maxresdefault.jpg
        :alt: Part2: Particle picking
        :target: https://www.youtube.com/watch?v=Y1jCY2cZlC0

    Part3: 2D classification and initial volume

    .. image:: https://img.youtube.com/vi/1fxOmKxqsPY/maxresdefault.jpg
        :alt: Part3: 2D classification and initial volume
        :target: https://www.youtube.com/watch?v=1fxOmKxqsPY

    Part4: 3D Reconstruction and validation

    .. image:: https://img.youtube.com/vi/AmYqywBA10o/maxresdefault.jpg
        :alt: Part4: 3D Reconstruction and validation
        :target: https://www.youtube.com/watch?v=AmYqywBA10o

    Take a look at our `tutorial videos <https://www.youtube.com/user/BiocompWebs>`_ in the Scipion youtube channel.

Know more about the `theory and practice <http://i2pc.es/coss/Docencia/ImageProcessing/imageProcessingInEM.pdf>`_ behind Image Processing in EM.


Initial model estimation
------------------------

.. figure:: /docs/images/00.ReconstructedVolume.png
   :align: right
   :height: 96
   :alt: 00.ReconstructedVolume.png

This tutorial uses different methods to
obtain an initial 3D map. Methods covered are RCT, Ransac, Eman and
Reconstruct Significant.

*Guide*:
`scipion\_tutorial\_initialvolume.pdf <https://github.com/I2PC/scipion/wiki/tutorials/scipion_tutorial_initialvolume.pdf>`__\


Initial volume validation by SAXS
---------------------------------

.. figure:: /docs/images/12.VolumeChimera.png
   :align: right
   :height: 76
   :alt: 00.ReconstructedVolume.png

This tutorial provides a guide to
the validation of the initial volume estimations using SAXS curves in
Scipion.

*Guide*:
`scipion\_tutorial\_SAXS.pdf <https://github.com/I2PC/scipion/wiki/tutorials/tutorial_SAXS.pdf>`__\

Localized reconstruction in Scipion
-----------------------------------

.. figure:: /docs/images/fibre_map.png
   :align: right
   :height: 76
   :alt: 00.ReconstructedVolume.png

In this tutorial, we provide a step-by-step guide for handling symmetry mismatches in single-particle analysis using a new plugin called LocalRec (Ilca et al. 2015) in Scipion (Abrishami et al. 2020).

*Guide*:
`scipion\_tutorial\_localrec.pdf <https://github.com/LSB-Helsinki/tutorials/blob/master/localrec/localrec21_tutorial.pdf?raw=true>`__\
