.. _protGemPicker:

====================
ProtGemPicker
====================

igbmc - auto-picking
--------------------

This auto-picking protocol is based on a highly parallel correlation-based
particle picking tool, `gEMpicker <http://gem.loria.fr/gEMpicker/>`_, developed
at INRIA and IGBMC, France [1]. The program uses template-matching approach,
when reference images are correlated with a set of micrographs in order to
locate single particles similar to the references. To achieve high processing
speeds, the calculations can be performed on multiple GPUs and CPU cores.

Input parameters
-----------------

To launch auto-picking you will need to select first the **Input micrographs**,
that can be any `SetOfMicrographs` produced earlier (Fig. 1). Though the program
can accept images up to 4096x4096 pixels size, it is recommended to coarse the m
icrographs to speed up the calculations. Then you have to select **Input references**,
that can be any `SetOfAverages`: either 2D class averages, calculated before, or
reprojections of the known 3D structure (in this case, you have to import your
reprojections as Averages). Note that the pixel size of the micrographs and the
references should be the same. Also, we have noticed that low-pass filtering
both micrographs and references gives better results. If the input micrographs
and references do no have the same contrast (e.g., white particles on a dark
background), select the option ``References have inverted contrast``.

Among other options the most important one is the ``Threshold range``: cross-correlation
peaks only within specified range will be selected as particles. Usually, you
should first run the protocol on a few micrographs with different defocus level
to optimize threshold and other parameters before starting auto-picking on a
whole dataset.

Additionally, you can provide a mask for the references, either a circular
(you might use a wizard for this) or a custom one. The number of masks should be
either one (a single mask for all references) or equal the number of references
(one mask per reference). In the latter case, the order of the masks should
correspond to the order of references. Of course, image size and pixel size of
the references and masks should be the same.


.. figure:: /docs/images/protocols/igbmc/01.ProtGemPicker.png
   :align: center
   :width: 500
   :alt: GUI input form of the gEMpicker protocol

   Figure 1. GUI input form of the gEMpicker protocol.


To see all available options, choose the _Advanced_ expert level and click on
the *Help* button for any specific parameter (Fig. 2).


.. figure:: /docs/images/protocols/igbmc/02.ProtGemPickerAdvanced.png
   :align: center
   :width: 500
   :alt: Advanced protocol parameters

   Figure 2. Advanced protocol parameters


Analyzing results
------------------
When the protocol is finished you may click on the *Analyze Results* button,
that will launch Xmipp particle picker window and display picked particles for
each micrograph (Fig. 3).


.. figure:: /docs/images/protocols/igbmc/03.ProtGemPickerResults.png
   :align: center
   :width: 500
   :alt: Displaying picking results

   Figure 3. Displaying picking results

Sometimes the picking algorithm may fail to find the particles. If this is the
case, you may help it by playing with threshold values as well as some advanced
parameters, i.e. ``Max distance between particles``.

References
-------------
* [1] Hoang T. V., Cavin X., Schultz P., Ritchie D. W. (2013). gEMpicker: a highly parallel GPU-accelerated particle picking tool for cryo-electron microscopy. BMC Structural Biology, 13(25): 1 - 10.