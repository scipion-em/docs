.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _advanced-topics:

===========================
Symmetries
===========================

Overview
===============

This page describes the different symmetries
that a polyhedron with fixed center may
and the conventions followed by Scipion to
label them. There are five fundamental symmetry classes:
cyclical, dihedral, tetrahedral, octahedral,
icosahedral.




Installation system
-------------------

* `[Installation system for developers] <installation-system>`_


Desktop development
-------------------

Most of the Scipion graphic user interfaces (GUIs) to visualize EM objects
(particles, coordinates, volumes, etc) have been developed in Java, extending
Xmipp ShowJ and Particle Picker. Implementation details are available
`[here] <scipion-java>`_.

Web development
----------------

* `Web developments and tools <web-developers-page>`_
* Conventions: Description of the conventions followed in Scipion.

Scipion from the command line
------------------------------

There are many things you can do with Scipion using just the command line, like
running tests, starting the webserver, or opening a ShowJ viewer. Read
this `[page] <scipion-commands>`_ to learn how.

Profiling and Debugging
-----------------------

* Check what can be reused from here: http://xmipp.cnb.csic.es/twiki/bin/view/Xmipp/DebuggingProfiling, check with Juan if he has some NOTES about profiling
* `Profiling in C/C++: Valgrind <valgrind-suite-tools-introduction>`_
* Debugging in Python: with PyCharm and WinPdb

Virtualization
---------------

* `Preparing a Scipion image <scipion-image>`_

Scipioncloud
-------------

`ScipionCloud <scipion-cloud>`_ main "cloud platforms" are Amazon Web Services (AWS) and EGI Federated Cloud (FedCloud)

* `ScipionCloud on AWS <scipionCloud-on-amazon-web-services-ec2>`_
* `ScipionCloud on FedCloud <scipion-on-the-egi-federated-cloud>`_
* `Deploying an HPC cluster on AWS <scipion-hpc-cluster-on-aws>`_
* `Starcluster instance types (AWS) <aws-instance-types-for-starcluster>`_
* `ScipionCloud deployments <scipion-deployments-on-the-cloud>`_ : on `FedCloud <scipion-deployments-on-the-egi-federated-cloud>`_
* `Preparing a Scipion image <scipion-image/>`_ (useful also for ScipionCloud)

GPU
---
* `GPU purchase guide. Enabling GPU in Scipion <https://scipion-em.github.io/docs/docs/developer/enable-gpu-in-scipion>`_
* `GPU params standardization in Scipion protocols <gpu-params-standardization>`_

Scipion ubiquity
----------------

 * `Scipion demo <scipion-demo>`_
 * Scipion live

References
-----------
* The `original Scipion Wiki <http://scipion.cnb.csic.es/old-docs/bin/view/TWiki/WebHome>`_

