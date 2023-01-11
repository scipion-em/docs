.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

===========================
Symmetries
===========================

Overview
========

This page describes the different symmetries
that a polyhedron with fixed center may have
and the symmetry conventions followed by Scipion. There are five fundamental symmetry classes: cyclical, dihedral, tetrahedral, octahedral and
icosahedral.

For each type we show in this page:

- Surface rendering of a volume that displays the symmetry.
- Atomic structure file (pb format) containing an atomic structure that
  satisfies the symmetry. (The PDB files may be visualized with
  viewers such as Chimera. `Link </docs/docs/images/Conventions/Symmetry/axis.bild>`_ to chimera axis file).
- Definition including the elements of symmetry.
- *X*, *Y* and *Z* axes are colored in red, yellow and blue respectively.

Note: Is really hard to see the difference symmetries just looking to the images,
instead download the PDB files, the axis.bild file and visualize them in chimera.
In chimera command line type "represent sphere" to increase the atoms size.

.. contents:: Table of Contents
    :local:

Cyclic of order N (Cn)
----------------------

    **Definition**: N rotations of magnitude 360/N degrees around an axis.

    **Scipion Definition (CN)**: rotation axis = *Z* axis.

    **PDB**: `link to C7 model </docs/images/Conventions/Symmetry/c7.pdb>`_

    .. figure:: /docs/images/Conventions/Symmetry/c7.png
       :width: 250
       :alt: c7 symmetry image


Dihedral of order N (Dn)
------------------------

    **Definition**: N rotations of magnitude 360/N degrees around an axis followed by a 180 rotation around a second axis. Both axes are perpendicular.

    **Scipion Definition (DNx)**: first axis = *Z*, second axis = *X*.

    **PDB**: `link to D7x model </docs/images/Conventions/Symmetry/d7x.pdb>`_

    .. figure:: /docs/images/Conventions/Symmetry/d7x.png
       :width: 250
       :alt: d7x symmetry image

    **Scipion Definition (DNy)**: first axis = *Z*, second axis = *Y*.

    **PDB**: `link to D7x model </docs/images/Conventions/Symmetry/d7y.pdb>`_

    .. figure:: /docs/images/Conventions/Symmetry/d7y.png
       :width: 250
       :alt: d7y symmetry image

Tetrahedral (T)
---------------

    **Definition**: There are three orthogonal 2-fold rotation axes with in addition four 3-fold axes, centered between the three orthogonal directions

    **Scipion Definition (T222)**: two-fold symmetry axes along the *X*, *Y*, and *Z* axes, a three-fold along axis (1,1,1)

    **PDB**: `link to T222 model </docs/images/Conventions/Symmetry/t222.pdb>`_

    .. figure:: /docs/images/Conventions/Symmetry/t222.png
       :width: 250
       :alt: t222 symmetry image

    **Scipion Definition (Tz3)**: a three-fold symmetry axis along *Z*, another three-fold axis in the *YZ* plane such that rotation about the *X* axis by ~110° is a symmetry operation

    **PDB**: `link to Tz3 </docs/images/Conventions/Symmetry/tz3.pdb>`_

    .. figure:: /docs/images/Conventions/Symmetry/tz3.png
       :width: 250
       :alt: tz3 symmetry image

Octahedral (O)
--------------

    **Definition**: There are three orthogonal 4-fold rotation axes with additional four 3-fold axes, centered between the three orthogonal directions

    **Scipion Definition (0)**: 3-fold symmetry axis around (.5773502, .5773502, .5773502) 4-fold rotation axis around (0 0 1).

    **PDB**: `link to O model </docs/images/Conventions/Symmetry/o.pdb>`_

    .. figure:: /docs/images/Conventions/Symmetry/o.png
       :width: 250
       :alt: o symmetry image

Icosahedral (I)
---------------

   **Definition**: 60 elements of symmetry.  12 5-fold axes, 20 3-fold axes and 30 2-fold axes.

   **Scipion Definition (I222)**:  2-fold axes on *X*, *Y* and *Z* axes. With the positive *Z*-axis pointing at the viewer, the front-most 5-fold vertices are in *YZ* plane, and the front-most 3-fold axis is in the *XZ* plane. As known as no Crowther 222, standard in Heymman et al 2005 article).

   **PDB**: `link to I222 model </docs/images/Conventions/Symmetry/i222.pdb>`_

   .. figure:: /docs/images/Conventions/Symmetry/i222.png
       :width: 250
       :alt: i222 symmetry image

   **Scipion Definition (I222r)**:  2-fold axes on *X*, *Y* and *Z* axes. With the positive *Z*-axis pointing at the viewer, the front-most 5-fold vertices are in *XZ* plane, and the front-most 3-fold axis is in the *YZ* plane. As known as no Crowther 222, standard in Heymman et al 2005 article).

   **PDB**: `link to I222r model </docs/images/Conventions/Symmetry/i222r.pdb>`_

   .. figure:: /docs/images/Conventions/Symmetry/i222r.png
       :width: 250
       :alt: i222r symmetry image

   **Scipion Definition (In25)**: 5fold axis in *Z* and 2-fold in *Y*. With the positive *Z*-axis pointing at the viewer and without taken into account the 5-fold vertex in *Z*, there is one of the front-most 5-fold vertices in -*XZ* plane (note the minus *X*)

   **PDB**: `link to In25 model </docs/images/Conventions/Symmetry/in25.pdb>`_

   .. figure:: /docs/images/Conventions/Symmetry/in25.png
       :width: 250
       :alt: in25 symmetry image

   **Scipion Definition (In25r)**: 5fold axis in *Z* and 2-fold in *Y*. With the positive *Z*-axis pointing at the viewer and without taken into account the 5-fold vertex in *Z*, there is one of the front-most 5-fold vertices in +*XZ* plane (note the plus *X*)

   **PDB**: `link to In25r model </docs/images/Conventions/Symmetry/in25r.pdb>`_

   .. figure:: /docs/images/Conventions/Symmetry/in25r.png
       :width: 250
       :alt: in25r symmetry image

   **Scipion Definition (I2n3)**: 3-fold axis in *Z* and 2-fold in *X*.
   With the positive *Z*-axis pointing at the viewer and without taken into account the 3-fold
   vertex in *Z*, there is one of the front-most 3-fold vertices in -*YZ* plane (note the minus *Y*)

   **PDB**: `link to I2n3 model </docs/images/Conventions/Symmetry/i2n3.pdb>`_

   .. figure:: /docs/images/Conventions/Symmetry/i2n3.png
       :width: 250
       :alt: i2 symmetry image

   **Scipion Definition (I2n3r)**: 3-fold axis in *Z* and 2-fold in *X*.
   With the positive *Z*-axis pointing at the viewer and without taken into account the 3-fold
   vertex in *Z*, there is one of the front-most 3-fold vertices in +*YZ* plane (note the plu *Y*)

   **PDB**: `link to I2n3 model </docs/images/Conventions/Symmetry/i2n3.pdb>`_

   .. figure:: /docs/images/Conventions/Symmetry/i2n3r.png
       :width: 250
       :alt: i2n3r symmetry image
