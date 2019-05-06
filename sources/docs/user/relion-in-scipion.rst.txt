.. _relion-in-scipion:

=================
Relion in Scipion
=================

.. contents:: Table of Contents

=============
Preprocessing
=============

How can I group micrographs in order to have more particles per group?
----------------------------------------------------------------------

In the Relion protocols in Scipion there is an option to create the groups automatically.
You can specify a minimum number of particles in each group or a defocus range.
(See the `original answer in Relion FAQs <https://www3.mrc-lmb.cam.ac.uk/relion/index.php/FAQs#How_can_I_group_micrographs_in_order_to_have_more_particles_per_group.3F>`_

What are groups for anyway?
---------------------------

See the `original answer in Relion FAQs <https://www3.mrc-lmb.cam.ac.uk/relion/index.php/FAQs#What_are_groups_for_anyway.3F>`_

Do I need to downsize my images?
--------------------------------
This is not needed for Relion. (see the `original answer in Relion FAQs <https://www3.mrc-lmb.cam.ac.uk/relion/index.php/FAQs#Do_I_need_to_downsize_my_images.3F>`_
If you still want to downsize your images, you can use either Relion or Xmipp
preprocess particles protocols to do so. (Later you can easily assign angular
assignment to original sized images)

Can I also use the estimated CTF parameters from XMIPP3?
--------------------------------------------------------
Yes. In Scipion you can estimate the CTF with Xmipp or CTFFIND (either 3 or 4)
and
use that estimation in Relion or other protocols.

How do you average your direct-electron detector movies?
--------------------------------------------------------
You can use the movie-alignment protocol to produce the average micrograph from
movies (the same protocol can be used to align frames using motion-corr, Xmipp
optical flow or a combination of both).
Currently there is not wrapper in Scipion for relion_image_handler program.

==============
Classification
==============

Do you have an example of how to run 3D classification?
-------------------------------------------------------

Yes, you can find an example in the Mix-and-Match tutorial from
`[here] <user-documentation>`__

Should I refine my 3D classes in a different program to reach higher resolution?
--------------------------------------------------------------------------------
You may do so in RELION or in others integrated refinement protocols such as:
Frealign, Eman-refine easy or Xmipp projection matching

How can I select images from a STAR file?
-----------------------------------------

You do not need to deal with star files or awk directly. From any output SetOfImages, you can visualize them with Scipion data viewer. From that viewer you can sort, render, re-organize columns and create a subset of images (the same applies for SetOfVolumes, SetOfMicrographs, etc). You can also group images belonging to a given class (either 2D and 3D) and create a new subset.

=============
3D refinement
=============

How can I make a plot of the orientational distribution of my particles?
------------------------------------------------------------------------
Different kind of plots are provided in the Analyze Results of Relion protocols
(FSC, SSNR, Angular distribution)

