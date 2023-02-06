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
icosahedral. Auxiliary data used to create this page is available at https://github.com/I2PC/testDataSym .

For each type we show in this page one image and several links:

- The image is a surface rendering of a volume that displays the symmetry.
- The phantom link contains a phantom that follows the symmetry created using PDB format. These PDB files may be visualized with viewers such as Chimera. A system of coordinates in bild format is available :download:`here <axis.bild>`. In the axis.bild file the *X*, *Y* and *Z* axis are colored in red, yellow and blue respectively.
- The symmetry matrices link contains a file with the symmetry matrices 
- The unit cell link contains a file with the vectors normal to the planes that define the unit cell is available
- the unit cell view link is a chimerax session file showing the unit cell and the normal vector. Whenever avaialble a collection of yellow spheres are shown. This spheres are the angular distribution produced by  a 3D_refinement of a set of a few hundred of particles. The particles are avaialble at https://github.com/I2PC/testDataSym .

Note: Is really hard to see the difference symmetries just looking to the images,
instead download the PDB files, the axis.bild file and visualize them in chimera.
In chimera command line type "represent sphere" to increase the atoms size.

.. contents:: Table of Contents
    :local:

Cyclic of order N (Cn)
----------------------

    **Definition**: N rotations of magnitude 360/N degrees 

    **Scipion Definition**:  N rotations of magnitude 360/N degrees around *Z* axis. Nomenglature **CN** where **N** is the symmetry number.
    
    .. image:: /docs/images/Conventions/Symmetry/c7.png
       :width: 60%
       :alt: c7 phantom


- :download:`phantom <c7.pdb>`
- :download:`symmetry Matrices <c7_mat.txt>`
- :download:`unit cell normal vectors <c7_normal.txt>`
- :download:`unit cell view <c7.cxs>`


Dihedral of order N (Dn)
------------------------

    **Definition**: N rotations of magnitude 360/N degrees around an axis followed by a **reflection** (not a rotation).

    **Scipion Definition (DNp)**: rotation axis = **Z**, reflexion may keep  **X** or **Y** fix, that is, Volume(x,y,z) = Volume(x,-y,-z) (**DNX**) or Volume(x,y,z) = Volume(-x,y,-z) (**DNY**). Nomenglature **DNX** or **DNY** where **N** is the rotation symmetry order and **X** or **Y** refers to the not reflected axis.

D7X
---

    .. image:: /docs/images/Conventions/Symmetry/d7x.png
       :width: 60%
       :alt: d7x symmetry image

- :download:`phantom <d7x.pdb>`
- :download:`symmetry Matrices <d7x_mat.txt>`
- :download:`unit cell normal vectors <d7x_normal.txt>`
- :download:`unit cell view <d7x.cxs>`




D7Y
---
    .. image:: /docs/images/Conventions/Symmetry/d7y.png
       :width: 60%
       :alt: d7y symmetry image

- :download:`phantom <d7y.pdb>`
- :download:`symmetry Matrices <d7y_mat.txt>`
- Symmetry unit cell and normal vectors are the same than **D7Y** (NOTE: not verified, test cryospark)
- :download:`unit cell view <d7y.cxs>`

         
Tetrahedral (T)
---------------

    **Definition**: There are three orthogonal 2-fold rotation axes  in addition to four 3-fold axes, centered between the three orthogonal directions.

    **Scipion Definition)**: 

    **T222**: two-fold symmetry axis along the **X**, **Y**, and **Z** axis, and a three-fold along vector (1,1,1).

    **TZ3**:  three-fold along vector (0, 0, 1), another threefold axis in the **YZ** plane, the **(y, z)** coordinates of this three-fold vector satisfy sign(y)!=sign(z)

    **TZ3R**:  three-fold along vector (0, 0, 1), another threefold axis in the **YZ** plane, the **(y, z)** coordinates of this three-fold vector satisfy sign(y)=sign(z)


T222
----

    .. image:: /docs/images/Conventions/Symmetry/t222.png
       :width: 60%
       :alt: t222 symmetry image

- :download:`phantom <t222.pdb>`
- :download:`symmetry Matrices <t222_mat.txt>`
- :download:`unit cell normal vectors <t222_normal.txt>`
- :download:`unit cell view <t222.cxs>`

TZ3
----

    .. image:: /docs/images/Conventions/Symmetry/tz3.png
       :width: 60%
       :alt: tz3 symmetry image

- :download:`phantom <tz3.pdb>`
- :download:`symmetry Matrices <tz3_mat.txt>`
- :download:`unit cell normal vectors <tz3_normal.txt>`
- :download:`unit cell view <tz3.cxs>`

TZ3R
----

    .. image:: /docs/images/Conventions/Symmetry/tz3r.png
       :width: 60%
       :alt: tz3r symmetry image

- :download:`phantom <tz3r.pdb>`
- :download:`symmetry Matrices <tz3r_mat.txt>`
- :download:`unit cell normal vectors <tz3_normal.txt>`
- :download:`unit cell view <tz3r.cxs>`


Octahedral (O)
--------------

    **Definition**: There are three orthogonal 4-fold rotation axes with additional four 3-fold axes, centered between the three orthogonal directions

    **Scipion Definition (0)**: 3-fold symmetry axis around (.5773502, .5773502, .5773502) 4-fold rotation axis around (0 0 1).

    .. image:: /docs/images/Conventions/Symmetry/o.png
       :width: 60%
       :alt: o symmetry image
              
- :download:`phantom <o.pdb>`
- :download:`symmetry Matrices <o_mat.txt>`
- :download:`unit cell normal vectors <o_normal.txt>`
- :download:`unit cell view <o.cxs>`


Icosahedral (I)
---------------

   **Definition**: 60 elements of symmetry.  12 5-fold axes, 20 3-fold axes and 30 2-fold axes.

I222
----

   **Scipion Definition (I222)**:  2-fold axes on *X*, *Y* and *Z* axes. With the positive *Z*-axis pointing at the viewer, the front-most 5-fold vertices are in *YZ* plane, and the front-most 3-fold axis is in the *XZ* plane. As known as no Crowther 222, standard in Heymman et al 2005 article).


   .. image:: /docs/images/Conventions/Symmetry/i222.png
       :width: 60%
       :alt: i222 symmetry image

- :download:`phantom <i222.pdb>`
- :download:`symmetry Matrices <i222_mat.txt>`
- :download:`unit cell normal vectors <i222_normal.txt>`
- :download:`unit cell view <i222.cxs>`


I222r
----

   **Scipion Definition (I222r)**:  2-fold axes on *X*, *Y* and *Z* axes. With the positive *Z*-axis pointing at the viewer, the front-most 5-fold vertices are in *XZ* plane, and the front-most 3-fold axis is in the *YZ* plane. As known as no Crowther 222, standard in Heymman et al 2005 article).


   .. image:: /docs/images/Conventions/Symmetry/i222r.png
       :width: 60%
       :alt: i222r symmetry image

- :download:`phantom <i222r.pdb>`
- :download:`symmetry Matrices <i222r_mat.txt>`
- :download:`unit cell normal vectors <i222r_normal.txt>`
- :download:`unit cell view <i222r.cxs>`


In25
----

   **Scipion Definition (In25)**: 5fold axis in *Z* and 2-fold in *Y*. With the positive *Z*-axis pointing at the viewer and without taken into account the 5-fold vertex in *Z*,  the front-most 5-fold vertice is in -*XZ* plane (note the minus *X*)


   .. image:: /docs/images/Conventions/Symmetry/in25.png
       :width: 60%
       :alt: in25 symmetry image

- :download:`phantom <in25.pdb>`
- :download:`symmetry Matrices <in25_mat.txt>`
- :download:`unit cell normal vectors <in25_normal.txt>`
- :download:`unit cell view <in25.cxs>`



In25r
----

   **Scipion Definition (In25r)**:  5fold axis in *Z* and 2-fold in *Y*. With the positive *Z*-axis pointing at the viewer and without taken into account the 5-fold vertex in *Z*,  the front-most 5-fold vertice is in +*XZ* plane (note the plus *X*)


   .. image:: /docs/images/Conventions/Symmetry/in25r.png
       :width: 60%
       :alt: in25r symmetry image

- :download:`phantom <in25r.pdb>`
- :download:`symmetry Matrices <in25r_mat.txt>`
- :download:`unit cell normal vectors <in25r_normal.txt>`
- :download:`unit cell view <in25r.cxs>`


In23
----

   **Scipion Definition (I2n3)**: 3-fold axis in *Z* and 2-fold in *X*.
   With the positive *Z*-axis pointing at the viewer and without taken into account the 3-fold
   vertex in *Z*, the front-most 3-fold vertices is in -*YZ* plane (note the minus *Y*)

   .. image:: /docs/images/Conventions/Symmetry/i2n3.png
       :width: 60%
       :alt: i2n3 symmetry image

- :download:`phantom <i2n3.pdb>`
- :download:`symmetry Matrices <i2n3_mat.txt>`
- :download:`unit cell normal vectors <i2n3_normal.txt>`
- :download:`unit cell view <i2n3.cxs>`


In23r
----

   **Scipion Definition (I2n3r)**: 3-fold axis in *Z* and 2-fold in *X*.
   With the positive *Z*-axis pointing at the viewer and without taken into account the 3-fold
   vertex in *Z*, the front-most 3-fold vertices in +*YZ* plane (note the plus *Y*)


   .. image:: /docs/images/Conventions/Symmetry/i2n3r.png
       :width: 60%
       :alt: i2n3r symmetry image

- :download:`phantom <i2n3r.pdb>`
- :download:`symmetry Matrices <i2n3r_mat.txt>`
- :download:`unit cell normal vectors <i2n3r_normal.txt>`
- :download:`unit cell view <i2n3r.cxs>`



I2n5
----

   **Scipion Definition (I2n5)**: 2-fold symmetry along x and 5-fold along z. It has a 2-fold axis in +Z-Y plane (note signs)


   .. image:: /docs/images/Conventions/Symmetry/i2n5.png
       :width: 60%
       :alt:  i2n5 symmetry image

- :download:`phantom <i2n5.pdb>`
- :download:`symmetry Matrices <i2n5_mat.txt>`
- :download:`unit cell normal vectors <i2n5_normal.txt>`
- :download:`unit cell view <i2n5.cxs>`


I2n5r
----

   **Scipion Definition (I2n5r)**: 2-fold symmetry along x and 5-fold along z. It has a 2-fold axis in +Z+Y plane (note plus signs)


   .. image:: /docs/images/Conventions/Symmetry/i2n5r.png
       :width: 60%
       :alt: i2n5r symmetry image

- :download:`phantom <i2n5r.pdb>`
- :download:`symmetry Matrices <i2n5r_mat.txt>`
- :download:`unit cell normal vectors <i2n5r_normal.txt>`
- :download:`unit cell view <i2n5r.cxs>`

