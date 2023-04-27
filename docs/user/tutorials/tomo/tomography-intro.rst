.. include:: <isonum.txt>
.. |icon| image:: /docs/user/tutorials/tomo/Picking_tutorial/Toggle_icon.png
.. |results| image:: /docs/user/tutorials/tomo/Picking_tutorial/Analyze_results.png
.. |wizard| image:: /docs/user/tutorials/tomo/Picking_tutorial/Wizard.png

.. image:: /docs/images/tomography/scipion-tomo-color.png
   :width: 100
   :align: right
   :alt: scipion tomo logo

.. _tomography-intro:

=====================
Tomography in Scipion
=====================

Scipion now talks cryo electron tomography!. It s been a long journey of developing and betatesting the new set
of plugins to make cryoET user friendly and remove some of the main obstacles of this image processing pipepline:
traceability, software interoperability and results visualization.


Integration
===========
In the same way as we've done it for single particle analysis (SPA) we (a set of developers and betatesters) have
integrated most of the relevant software used in cryoET so you, as a user, can forget about moving files around,
launching complicated commands or convert data and metadata. Scipion tomo does it for you. Here is a short list of
the software integrated today (26th April 2023), but since Scipion is exensible by plugins we hope more developers
will join the project to integrate their nice software into this platform.

* Motioncor2 (scipion-em-motioncorr)
* Xmipp (tomo) (scipion-em-xmipptomo)
* Imod (scipion-em-imod)
* Aretomo (scipion-em-aretomo)
* tomo3d (scipion-em-tomo3d)
* IsoNET (scipion-em-isonet)
* NovaCTF (scipion-em-novactf)
* Cistem (scipion-em-cistem)
* gCTF (scipion-em-gctf)
* Eman2: pickings, initial model, alignment and reconstruction (scipion-em-emantomo)
* Dynamo: picking, alignment and reconstruction (scipion-em-dynamo)
* cryoCARE (scipion-em-cryocare)
* crYOLO: picking, filament picking, and training (scipion-em-sphire)
* PySeg (scipion-em-pyseg)
* DeepFinder (scipion-em-deepfinder)
* TomosegmemTV (scipion-em-tomosegmemtv)
* Tomotwin (scipion-em-tomotwin)
* Relion: tomo jobs (scipion-em-reliontomo)
* Susantomo (scipion-em-susantomo)
* Continuousflex (scipion-em-continuousflex)

In brackets, the plugin that integrates the software and in most cases installs it too!

Here you can see how one of our tutorials workflows mixes some of the software integrated.

.. image:: /docs/images/tomography/tomo-workflow.png
   :alt: Tomography workflow with SPA showing software interoperability.

Please, note that relion methods in this case are SPA ones (2D classification and 2D class ranker)
in what we have called the "SPA leap". This is projecting subtomograms on any of the 3 axis
to get 2D particles. Once "flattened" the particles can be send to ANY SPA available protocol,
in this case Relion's 2D classification, but could have used Cryosparc as well. Then with the "subset"
we go back to 3D world filtering the subtomograms based on their 2d SPA averages.


Results and its Visualization
=============================
Visualization is quite important in any image processing pipeline. Scipion has a visualization engine that
with little effort allow developer to integrate existing visualization tools from 3rd party software, or define
new way of visualizing the results.

Here you can se how easily you can visualise a tilt series using the versatile Imod's 3dmod program.

.. image:: /docs/images/tomography/3dmod.gif
   :alt: 3dmod showing a tilt series

However, for viewing a set of tomography CTFs we have developed a custom viewer that plots the
defocus values and resolution along the selected tilt serie and its basic metadata.

.. image:: /docs/images/tomography/tomo-ctf-viewer.png
   :alt: Scipion viewer for a Set of tomography CTFs.

See how many different ways you can visualise any set of 3D coordinates:
Tomoviz (with and without orientations), Dynamo or Eman2, napari, your choice!!.

.. image:: /docs/images/tomography/3dcoordinates-viewers.gif
   :alt: Scipion viewer for a Set of tomography CTFs.

We have been creative also and used Imod's fiducial viewer to plot relion4 projected 3d coordinates
as a way to double check if all is in place before doing relion's per particle per tilt refinement.
Be aware that you can enter relion4 tomogram pipeline having aligned you tilt series with aretomo
(for example). We will "trick" relion4 simulating the imod files it needs!.

.. image:: /docs/images/tomography/relion4-projected-particles.gif
   :alt: Visualisation of 3d coordinates as fiducials in 3dmod.

Of course, ChimeraX is integrated to render subtomogram averages like the one at 3.7 Å reached
100% inside Scipion (staring from relion4's HIV capsid tutorial dataset) and before any CTF or tilt series
refinement.

.. image:: /docs/images/tomography/chimerax.gif
   :alt: Zoomed in section in ChimeraX of the HIV capsid at 3.7 Å.

Once you have a decent average you could also map it back to the original tomogram to see in situ features
using xmipptomo map back protocol.

.. image:: /docs/images/tomography/mapback.png
   :alt: Xmipptomo map back done of the HIV capsid.


Validation
==========
As one of our colleagues here uses to say: "The good thing of cryo em methods is that they will
always give you a result. The bad thing is that they will always give you a results". ;-).

In the same way we have done with SPA processing we are crating validations tools to  verify the quality
of your results before going forward. This is already happening with "xmipptomo - subtomo alignemnt consensus",
"tomo - tilt series consensus alignment", "tomoviz - picking consensus" or "xmipp - consensus clustering 3d"

Basic operations
================
Of course all this comes out of the box with all the functionality that scipion already provides for any project:
* Color labeling
* Duplicating a branch of the workflow
* Resetting/restarting a branch of the workflow
* Workflow templates (there are some already for imod automatic tilt series alignment or pySeg picking)
* Workflow planning and scheduling
* Streaming: As of today streaming covers **motion correction + tilt series composition**. More to come!
* Easy subseting: manual or parametrized
* Metadata plotting
* Third party installation. Yes, when authorized, we offer installation (optional) for the software we integrate.
* Filter by normals
* Remove duplicates
* ...

How to get it?
==============
As simple as installing the plugins you want to use. Obviously you first need to get :ref:`scipion installed<how-to-install>`
and then use the :ref:`plugin manager<plugin-manager>` to install the tomography plugins. Each plugin will install the software
behind it integrates (by default) but can be canceled in case you already have it. In this case, see how to
:ref:`link existing software<linking-existing-software>`

One more thing
==============
Please, please ... only cite us, and cite **all the great software we integrate** too!. Citations is what fuels all the software.
Yes, Scipion kind of "hides" in many cases the software it integrates but there is no way to do it otherwise.
For every protocol you have all the references in bibtex format available and quite easily you can get all the references
involved in your project. Please do so!.

.. image:: /docs/images/general/bibtex-export.gif
   :alt: Zoomed in section in ChimeraX of the HIV capsid at 3.7 Å.

Brought to you by
=================
Led by I2PC (at Madrid) but with key contributions of other developers and betatesters all over the world.
We would like to specially congratulate Grigory Sharov for been also here in tomography as well as in SPA,
Antonio Martinez Sanchez (pySeg developer) for assisting us integrating pySeg, Daniel Castaño for guiding
us into Dynamo world, Emmanuel Moebel for integrating deepfinder, Tim Oliver Buchholz for integrating cryoCARE,
Mohamad Harastani for his great job with continuousflex, "Quino" for guiding us into relion4 tomography,
Bram Koster, Borja Rodriguez, Ana Cuervo and Patricia Losana for betatesting since the very begining all this
code we now released. It was painful at times, I know, but I hope it payed off. Of course, the whole Madrid's
developers team (Scipion core and Xmipp developers) and leaders: Jose Maria Carazo and Carlos Oscar Sanchez-Sorzano

Is that it?
===========
NO! But for now you can start enjoying tomography processing but be sure more integrations will come.
In the oven, we have, deepict, per-particle per tilt in eman, subtomogram averaging in xmipp,
streamifying more protocols ... and more importantly, that new "new method" that will appear and
revolutionise the field .... will very likely be integrated.... and YES! M, as soon as
`can run on linux <https://groups.google.com/g/warp-em/c/dAsmMnlULJA/m/CzlgVkJMCAAJ>`_ it will be here too

If you like what you've read, either if you are facility staff, a regular image processing user or a developer,
please, join us at our `discord workspace <https://discord.gg/TzS5VTKQbY>`_: You are very welcome! and the people
there will be happy to assist you.


Additional resources
====================

Here you can find some valuable resources to complement the contents described:

* `Scipion for tomography paper <https://doi.org/10.1016/j.jsb.2022.107872>`_
* :ref:`Tomography tutorials <tomography-tutorials>`
* `Youtube I2PC channel (filtered by "tomography") <https://www.youtube.com/@BiocompWebs/search?query=tomography>`_

