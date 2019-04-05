
.. _scipion-configuration:

=====================
Scipion configuration
=====================


Running scipion config
======================

This is the command used to generate config files or analyze them if you already have them.

::

    ./scipion config

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

``scipion config`` might tell you it is not able to find some of the
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
    JAVA_HOME = /usr/lib/jvm/java-1.7.0-openjdk-amd64
    JAVA_BINDIR = %(JAVA_HOME)s/bin
    (...)

Once ``config/scipion.conf`` is changed, run ``./scipion config`` again.


If you have configuration files from previous installations, you may
want to use this instead:

::

    ./scipion config --overwrite


GPU variables
=============

To install the GPU programs, you will need to set CUDA to True in
``scipion.conf``. If CUDA is installed in a non-standard location, you
will need to specify where to find CUDA libraries. For this, you can use
the ``LINKFLAGS`` variable of ``scipion.conf``. For example:

::

    CUDA = True
    LINKFLAGS = -L/opt/CUDA/cuda-5.5/lib64