.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _advanced-topics:

===========================
Advanced Development Topics
===========================

Advanced Topics
===============

Desktop development
-------------------

Most of the Scipion graphic user interfaces (GUIs) to visualize EM objects
(particles, coordinates, volumes, etc) have been developed in Java, extending
Xmipp ShowJ and Particle Picker. Implementation details are available
:doc:`here <scipion-java>`.

Scipion from the command line
------------------------------

There are many things you can do with Scipion using just the command line, like
running tests, starting the webserver, or opening a ShowJ viewer. Read
this :doc:`page <scipion-commands>` to learn how.

Profiling and Debugging
-----------------------

* Check what can be reused from here: https://github.com/I2PC/xmipp-portal/wiki/DebuggingProfiling, check with Juan if he has some NOTES about profiling
* :doc:`Profiling in C/C++: Valgrind <valgrind-suite-tools-introduction>`
* Profiling Python with :doc:`PyCharm <pycharm-profiling>`
* Profiling Python with :doc:`Intel VTune Profiler <vtune-profiler>`

Scipion and docker
------------------

* `Docker images for Scipion <https://github.com/i2pc/scipion-docker>`_

