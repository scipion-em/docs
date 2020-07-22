.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _ProtGctf:

=========
ProtGctf
=========



gctf - CTF estimation on GPU
----------------------------

This protocol is based on `gctf [1] <http://www.mrc-lmb.cam.ac.uk/kzhang/Gctf>`_ , a GPU accelerated program for Real-Time CTF determination, refinement, evaluation and correction. At this moment movie options, CTF refinement for particles and tilt refinement options are not supported yet.

Input parameters
-----------------

To estimate the CTF you will need to select first the **Input micrographs**,
that can be any `SetOfMicrographs` produced earlier (Fig. 1). Then you can
choose the frequency region to be analyzed. The limiting frequencies must be
such that all zeros of the PSD are contained within those frequencies. There is
a wizard, shown in Fig. 2, that helps in choosing those frequencies. To see
the all available options, choose the _Advanced_ expert level, switch to
``Advanced`` tab and click on the *Help* button for any specific parameter
(Fig. 3).

.. figure:: /docs/images/protocols/gctf/01.ProtGctf.png
   :align: center
   :width: 500
   :alt: GUI input form of the gctf protocol

   Figure 1. GUI input form of the gctf protocol


.. figure:: /docs/images/protocols/grigoriefflab/02.CTFWizard.png
   :align: center
   :width: 500
   :alt: GUI input form of the gctf protocol

   Figure 2. CTF wizard helps to select a downsampling factor and the range of spatial frequencies


.. figure:: /docs/images/protocols/gctf/03.ProtGctfAdvanced.png
   :align: center
   :width: 500
   :alt: GUI input form of the gctf protocol

   Figure 3. Advanced protocol parameters

Analyzing CTF results
-----------------------

The CTFs of good micrographs typically have multiple concentric rings, shown in
Fig. 4 left, extending from the image center towards its edges. Bad micrographs
may lack rings or have very few rings that hardly extend from the image center.
A reason to discard micrographs may be the presence of strongly asymmetric rings
(astigmatism, Fig. 4 center) or rings that fade in a particular direction
(drift, Fig. 4 right).

.. figure:: /docs/images/protocols/grigoriefflab/04.CTFexamples.jpg
   :align: center
   :width: 500
   :alt: GUI input form of the gctf protocol

   Figure 4. CTFs of good, astigmatic and drift micrographs respectively.


When the protocol is finished you may click on the *Analyze Results* button to
show the list of micrographs and their PSD (Fig. 5). To discard micrographs with
bad CTFs you may click with the mouse right button and press _Disable_. Once you
finish the selection, press on the Micrographs button to create a subset of
micrographs with only the enabled ones.


.. figure:: /docs/images/protocols/gctf/05.ProtGctfResults.png
   :align: center
   :width: 700
   :alt: GUI input form of the gctf protocol

   Figure 5. Displaying CTF results


Sometimes the CTF estimation algorithm may fail to find the rings even if they
can be seen by eye. If this is the case, you may help the algorithm to find the
rings by clicking on the image with the mouse right-button and choosing
``Recalculate CTF`` on the menu that appears. A graphical interface will help
you to correctly identify the CTF. You must provide the first CTF zero and the
search range, and then press *OK*. When you finish, press the *Recalculate CTFs*
button.

It is possible to analyze the CTF profiles by right-click on a micrograph row
and selecting the ``Show CTF profile`` option which should open a window shown in
fig. 6. It is also possible to analyze the CTF fitting by selecting the
``Display CTF Analysis`` option. A plot should appear with the 1D profiles
calculated by gctf (fig. 7). This is an interactive plot that can be zoomed to
specific regions among other things.

.. figure:: /docs/images/protocols/gctf/06.ProtGctfCTFProfile.png
   :align: center
   :width: 500
   :alt: GUI input form of the gctf protocol

   Figure 6. CTF profile

.. figure:: /docs/images/protocols/gctf/07.CTFFitting.png
   :align: center
   :width: 500
   :alt: GUI input form of the gctf protocol

   Figure 7. CTF fitting

References
------------

* [1] Zhang K. (2016). Gctf: Real-time CTF determination and correction. JSB, 193: 1-12.



