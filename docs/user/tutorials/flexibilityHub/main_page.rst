.. include:: <isonum.txt>

.. |results| image:: /docs/user/tutorials/tomo/Picking_tutorial/Analyze_results.png

.. _Flexibility_Hub_main_page:

====================================================
Flexibility Hub: Advanced CryoEM heterogeneity analysis in Scipion
====================================================

Here we introduce the **Flexiblity Hub**, a new section of Scipion specifically design to define CryoEM flexibility workflows.

Currently, the following softwares have been integrated in the FLexibility Hub framework:

* `Zernike3D <>`__ (available at `scipion-em-flexutils <https://github.com/scipion-em/scipion-em-flexutils>`__)
* `CryoDRGN <>`__ (available at `scipion-em-cryodrgn <https://github.com/scipion-em/scipion-em-cryodrgn>`__)
* `ContinuousFlex <>`__ (available at `scipion-em-cryodrgn <https://github.com/scipion-em/scipion-em-continuousflex>`__)
* `ProDy <>`__ (available at `scipion-em-prody <https://github.com/scipion-em/scipion-em-prody>`__)

Joining the Discord workspace
=============================

If you are working in development mode, we strongly suggest joining `Scipion's Discord workspace  <https://discord.gg/TzS5VTKQbY>`__ to get information about the last updates of the plugins.


Where to start?
=============================

The Flexbility Hub framework is structured around Flexutils Plugin. Flexutils integrates all the data models and analysis tools needed to define flexibility workflows. Moreover, it includes all the Zernike3D related protocols, allowing to start workflows straight away after its installation.

Therefore, Flexutils is the only mandatory component of the Flexibility Hub. Before installing it, please, check that you have Scipion v3.x installed in your system.

Flexutils plugin installation follows the standard installation steps of any other plugin in Scipion:

* Follow `this guide <https://scipion-em.github.io/docs/release-3.0.0/docs/scipion-modes/install-plugins-command-line#regular-install>`__ for production mode installation (from the command line)
*  Follow `this guide <https://scipion-em.github.io/docs/release-3.0.0/docs/scipion-modes/install-plugins-command-line#devel-mode>`__ for devel mode installation (from the command line)


Tutorials
=============================

There are two different tutorials available:

* `Flexibility Hub Starter guide <./Tutorials/starter_guide>`__: Simple workflow focusing on the analysis of ideal landscapes from synthetic particles.
* `Flexibility Hub advanced guide <./Tutorials/advanced_guide>`__: Workflow with real CryoEM data from Empiar, showing the common strategies to address molecular flexibility from experimental particles

In addition, each Plugin integrated in the Flexibility Hub includes guides on the usage of the different protocols it integrates.

Video tutorials are also available `here <https://www.youtube.com/playlist?list=PLuu0votIJpSxTmPLvKRHV3ijadqlxxHfb>`__ describing the interactive tools to explore conformational landscapes.