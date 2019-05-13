.. _protCtfFind:

=======================
ProtCTFFind
=======================

grigoriefflab - ctffind
------------------------

With this protocol you can calculate the PSD (Power Spectral Density) and
estimate the CTF parameters (defocus U, defocus V, defocus angle, etc) for a
set of micrographs using `ctffind <http://grigoriefflab.janelia.org/ctf>`_ [1, 2].
The algorithm consists of computing a PSD from each input micrograph,
estimating the PDS's background, subtracting it from the original PSD, and
evaluating the similarity between theoretical CTF functions and the remaining
oscillatory signal.

Input parameters
-----------------

To estimate the CTF you will need to select first the **Input micrographs**,
that can be any `SetOfMicrographs` produced earlier (Fig. 1). Then you can choose
the frequency region to be analyzed. The limiting frequencies must be such that
all zeros of the PSD are contained within those frequencies. There is a wizard,
shown in Fig. 2, that helps in choosing those frequencies. To see the full
available options, choose the _Advanced_ expert level and click on the *Help*
button for any specific parameter (Fig. 3). The CTFFind protocol allows to use
either the ctffind3 or ctffind4 program (the latest has been reported to be about
ten times faster than its predecessor).

.. figure:: https://github.com/I2PC/scipion/wiki/images/protocols/grigoriefflab/01.CTFFind.png
   :align: center
   :width: 500
   :alt: GUI input form of the ctffind protocol

   Figure 1. GUI input form of the ctffind protocol

.. figure:: https://github.com/I2PC/scipion/wiki/images/protocols/grigoriefflab/02.CTFWizard.png
   :align: center
   :width: 500
   :alt: CTF wizard helps

   Figure 2. CTF wizard helps to select a downsampling factor and the range of spatial frequencies


.. figure:: https://github.com/I2PC/scipion/wiki/images/protocols/grigoriefflab/03.CTFFindAdvanced.png
   :align: center
   :width: 500
   :alt: Advanced protocol parameters

   Figure 3. Advanced protocol parameters

Analyzing CTF results
----------------------

The CTFs of good micrographs typically have multiple concentric rings, shown
in Fig. 4 left, extending from the image center towards its edges. Bad micrographs
may lack rings or have very few rings that hardly extend from the image center.
A reason to discard micrographs may be the presence of strongly asymmetric rings
(astigmatism, Fig. 4 center) or rings that fade in a particular direction (drift, Fig. 4 right).


.. figure:: https://github.com/I2PC/scipion/wiki/images/protocols/grigoriefflab/04.CTFexamples.jpg
   :align: center
   :width: 500
   :alt: Advanced protocol parameters

   Figure 4. CTFs of good, astigmatic and drift micrographs respectively.


When the protocol is finished you may click on the *Analyze Results* button to show the list of micrographs and their PSD (Fig. 5). To discard micrographs with bad CTFs you may click with the mouse right button and press _Disable_. Once you finish the selection, press on the Micrographs button to create a subset of micrographs with only the enabled ones.

.. figure:: https://github.com/I2PC/scipion/wiki/images/protocols/grigoriefflab/05.CTFResult.png
   :align: center
   :width: 700
   :alt: Advanced protocol parameters

   Figure 5. Displaying CTF results

Sometimes the CTF estimation algorithm may fail to find the rings even if they
can be seen by eye. If this is the case, you may help the algorithm to find the
rings by clicking on the image with the mouse right-button and choosing ``Recalculate CTF`` on the menu that appears. A graphical interface will help you to correctly identify the CTF. You must provide the first CTF zero and the search range, and then press *OK*. When you finish, press the *Recalculate CTFs* button.

It is possible to analyze the CTF profiles by right-click on a micrograph row
and selecting the ``Show CTF profile`` option which should open a window shown
in fig. 6. It is also possible to analyze the CTF fitting by selecting the
``Display CTF fitting`` option. A plot should appear with the 1D profiles
calculated by ctffind4 (fig. 7). This is an interactive plot that can be zoomed
to specific regions among other things.


.. figure:: https://github.com/I2PC/scipion/wiki/images/protocols/grigoriefflab/06.CTFProfile.png
   :align: center
   :width: 500
   :alt: Advanced protocol parameters

   Figure 6. CTF profile.


.. figure:: https://github.com/I2PC/scipion/wiki/images/protocols/grigoriefflab/07.CTFFitting.png
   :align: center
   :width: 500
   :alt: Advanced protocol parameters

   Figure 7. CTF fitting.


References
-----------

* [1] Mindell, J. A. and Grigorieff, N. (2003). Accurate determination of local defocus and specimen tilt in electron microscopy. JSB, 142: 334 – 347.
* [2] Rohou, A. and Grigorieff, N. (2015). CTFFIND4: Fast and accurate defocus estimation from electron micrographs. JSB, 192: 216 – 221.