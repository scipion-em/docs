.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _scipion-configuration:

=====================
Scipion configuration
=====================


Running scipion config
======================

This is the command used to generate config files or analyze them if you already have them.

::

    ./scipion3 config

The configuration files generated with this command are in two locations:

* ``~/.config/scipion/scipion.conf`` contains  the configuration specific for the current user.

* ``<your-scipion-home>/config`` contains configuration files for this Scipion installation,
  which will be applied to everyone using it. There are three files stored here:

        - ``<your-scipion-home>/config/scipion.conf`` with general variables to run scipion,
          install and use external libraries, etc.
        - ``<your-scipion-home>/config/hosts.conf`` with the host configuration.
          You can find more about it in the :ref:`host configuration page <host-configuration>`.
        - ``<your-scipion-home>/config/protocols.conf`` with the list of protocols available in the Scipion
          installation. Not to be messed with unless you're a developer and have a good known reason to do so.

``scipion3 config`` might tell you it is not able to find some of the
paths. In this case, you should edit ``config/scipion.conf`` to reflect
your system's configuration. For example, below is an excerpt of
``config/scipion.conf`` adapted for an Ubuntu computer:

::

    (...)
    [BUILD]
    CC = gcc
    CXX = g++
    (...)
    MPI_LIBDIR = /usr/lib
    MPI_INCLUDE = /usr/include/mpi
    MPI_BINDIR = /usr/bin
    (...)
    JAVA_HOME = /usr/lib/jvm/java-8-openjdk
    JAVA_BINDIR = %(JAVA_HOME)s/bin
    (...)

Once ``config/scipion.conf`` is changed, run ``./scipion3 config`` again.


If you have configuration files from previous installations, you may
want to use this instead:

::

    ./scipion3 config --overwrite


GPU variables
=============

To install the GPU programs, you will need to set CUDA to True in
``scipion.conf``. If CUDA is installed in a non-standard location, you
will need to specify where to find CUDA libraries. For this, you can use
the ``LINKFLAGS`` variable of ``scipion.conf``. For example:

::

    CUDA = True
    LINKFLAGS = -L/opt/CUDA/cuda-8.0/lib64
    
OpenCV flag
===========

To install Xmipp without OpenCV and, then skipping the programs using it (Optical Alignment and Volume Enrich), you will need to set OPENCV to False in ``scipion.conf``:

::

    OPENCV = False


Running Scipion in multi-users environment
==========================================

In the case we want to install Scipion on a Cluster for many users, it is
convenient to have a single ``scipion.conf`` file for all of them, otherwise, the
each user must have a config file under his home folder as described above.

We can launch Scipion with the --config parameter: ``--config <scipion.conf PATH>``.
This parameter tells Scipion to be use a configuration file in a specific path.

IMPORTANT!!!!!

In this case, the config file must be a union of the ``~/.config/scipion/scipion.conf``  and
``<your-scipion-home>/config` and be placed in an accessible path to all users.


::

    ./scipion3 --config <scipion.conf PATH>
