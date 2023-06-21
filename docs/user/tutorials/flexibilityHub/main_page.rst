.. include:: <isonum.txt>

.. |results| image:: /docs/user/tutorials/tomo/Picking_tutorial/Analyze_results.png

.. _Flexibility_Hub_main_page:

====================================================
Flexibility Hub: Advanced CryoEM heterogeneity analysis in Scipion
====================================================

Here we introduce the **Flexiblity Hub**, a new section of Scipion specifically design to define CryoEM flexibility workflows.

Currently, the following softwares have been integrated in the FLexibility Hub framework:

* Zernike3D (available at `scipion-em-flexutils <https://github.com/scipion-em/scipion-em-flexutils>`__)
* CryoDRGN (available at `scipion-em-cryodrgn <https://github.com/scipion-em/scipion-em-cryodrgn>`__)
* :doc:`ContinuousFlex <Tutorials/MDSPACE_Tutorial_v0>` (available at `scipion-em-continuousflex <https://github.com/scipion-em/scipion-em-continuousflex>`__)
* ProDy (available at `scipion-em-prody <https://github.com/scipion-em/scipion-em-prody>`__)

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

* :doc:`Flexibility Hub Starter guide <Tutorials/starter_guide>`: Simple workflow focusing on the analysis of ideal landscapes from synthetic particles.
* :doc:`Flexibility Hub advanced guide <Tutorials/advanced_guide>`: Workflow with real CryoEM data from Empiar, showing the common strategies to address molecular flexibility from experimental particles

In addition, each Plugin integrated in the Flexibility Hub includes guides on the usage of the different protocols it integrates.

Video tutorials are also available `here <https://www.youtube.com/playlist?list=PLuu0votIJpSxTmPLvKRHV3ijadqlxxHfb>`__ describing the interactive tools to explore conformational landscapes.


Additional materials
=============================

* Instruct course on flexibility analysis and integrative modelling using Scipion. Madrid, June 19 – 23, 2023:
    - Introductory slides to the Flexibility Hub (available `here <https://docs.google.com/presentation/d/1lTuMyWJejke9fMbjKW2Eqpj17I4Eknl3/edit?usp=sharing&ouid=109388499505764890294&rtpof=true&sd=true>`__)
    - Theory on heterogeneity approaches (available `here <https://docs.google.com/presentation/d/1RVUAvAz4zREwGZ4L5IBFcnSPYLcq8Mgj/edit?usp=sharing&ouid=109388499505764890294&rtpof=true&sd=true>`__)
    - Theory slides on flexibility consensus (available `here <https://docs.google.com/presentation/d/1FVUaDBvBOhEuf8SvH24Xel08IaAcGKtr/edit?usp=sharing&ouid=109388499505764890294&rtpof=true&sd=true>`__)
    - Theory slides on ZART and heterogeneity correction (available `here <https://docs.google.com/presentation/d/141Iz7fYErqAJPK24WU3LYMvYMf30QEwL/edit?usp=sharing&ouid=109388499505764890294&rtpof=true&sd=true>`__)