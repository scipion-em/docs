.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _advanced-topics:

===========================
Advanced Development Topics
===========================

Advanced Topics
===============

Installation system
-------------------

* `Installation system for developers <installation-system>`_


Desktop development
-------------------

Most of the Scipion graphic user interfaces (GUIs) to visualize EM objects
(particles, coordinates, volumes, etc) have been developed in Java, extending
Xmipp ShowJ and Particle Picker. Implementation details are available
`here <scipion-java>`_.

Scipion from the command line
------------------------------

There are many things you can do with Scipion using just the command line, like
running tests, starting the webserver, or opening a ShowJ viewer. Read
this `page <scipion-commands>`_ to learn how.

Profiling and Debugging
-----------------------

* Check what can be reused from here: https://github.com/I2PC/xmipp-portal/wiki/DebuggingProfiling, check with Juan if he has some NOTES about profiling
* `Profiling in C/C++: Valgrind <valgrind-suite-tools-introduction>`_
* Profiling Python with `PyCharm <pycharm-profiling>`_
* Profiling Python with `Intel VTune Profiler <vtune-profiler>`_

Virtualization
---------------

* `Preparing a Scipion image <scipion-image>`_

Scipioncloud
-------------

ScipionCloud main "cloud platforms" are Amazon Web Services (AWS) and EGI Federated Cloud (FedCloud)

* `ScipionCloud on AWS <scipionCloud-on-amazon-web-services-ec2>`_
* `ScipionCloud on FedCloud <scipion-on-the-egi-federated-cloud>`_
* `Starcluster instance types (AWS) <aws-instance-types-for-starcluster>`_
* `ScipionCloud deployments <scipion-deployments-on-the-cloud>`_ : on `FedCloud <scipion-deployments-on-the-egi-federated-cloud>`_

GPU
---
* `GPU purchase guide. Enabling GPU in Scipion <https://scipion-em.github.io/docs/docs/developer/enable-gpu-in-scipion>`_
* `GPU params standardization in Scipion protocols <gpu-params-standardization>`_

