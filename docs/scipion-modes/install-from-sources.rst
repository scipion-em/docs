.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _install-from-sources:

=======================
Installing from sources
=======================

Step 1: Download
================

You can install Scipion anywhere, as long as you have write permissions.
If you want to share Scipion installation among different users you can
use ``/usr/local`` or a similar path. If it is only for you, you can use
your home directory as well. If you have a previous installation, we
recommend starting this installation fresh in a new folder.

From GitHub
-----------

Clone Scipion repository (install **git** if not present in your
system):

::

    git clone https://github.com/I2PC/scipion.git
    cd scipion 
    git checkout release-2.0.0

Git will create a ``scipion`` directory under your current path; you do
not need to create it manually.

.. _install-deps:

Step 2: Dependencies
====================

To install Scipion from source, some development libraries are required.
You can install them with (this example is for Ubuntu16). See `Installing Dependencies <dependencies>`_ for others distributions):

::

     sudo apt-get install gcc-5 g++-5 cmake openjdk-8-jdk libxft-dev libssl-dev libxext-dev libxml2-dev\
     libreadline6 libquadmath0 libxslt1-dev libopenmpi-dev openmpi-bin  libxss-dev libgsl0-dev libx11-dev\
     gfortran libfreetype6-dev scons libfftw3-dev libopencv-dev curl git


Step 3: Configure and Install
=============================

Configure
---------

After installing the `dependencies <dependencies>`_, you can
proceed to generate configuration files. If you had a previous Scipion
installation, it is a good idea to make a copy of your current config
files ``~/.config/scipion/scipion.conf`` and
``<your_scipion_home>/config/scipion.conf``. Now run:

::

    cd scipion
    ./scipion config

You will be asked to share **scipion usage only** data. Sharing `usage
data <https://scipion-em.github.io/docs/release-2.0.0/docs/developer/collecting-statistics.html>`_
will help to make Scipion better.

This command will generate the configuration files (if not present) and
will try to automatically find configuration paths.

If everything is OK (all green in the output) you can proceed to the
next step. If there is a problem (red colored output), you will need to
edit ``config/scipion.conf`` file in your preferred text editor and run
``./scipion config`` again.

One known change for **Ubuntu 18** are the MPI paths in
``<your_scipion_home>/config/scipion.conf``:

::

   MPI_LIBDIR = /usr/lib/x86_64-linux-gnu/openmpi/lib
   MPI_INCLUDE = /usr/lib/x86_64-linux-gnu/openmpi/include/

The MPI paths in **CentOS** are in:

::

    MPI_BINDIR = /usr/lib64/openmpi/bin
    MPI_LIBDIR = /usr/lib64/openmpi/lib
    MPI_INCLUDE = /usr/include/openmpi-x86_64

Read more about :doc:`editing the configuration
file <scipion-configuration>`.

The file ``config/hosts.conf`` contains some properties of the execution
machine. This configuration file is particularly important for clusters
that use a Queue System. If you are installing Scipion on a cluster, you
probably will want to check :doc:`how to configure an execution
host <host-configuration>`.

Install
-------

To compile and install Scipion, just run:

::

    ./scipion install -j 5

``-j 5`` tells the Scipion installer to use 5 processors (cores) for
compilation. You should adjust this value according to your system.

For convenience, create an **alias** in the ``.bashrc`` file located
in ``/home/<user>/.bashrc`` that allows you to launch Scipion from any
location on your computer.

::

   alias scipion='<your_scipion_home>/scipion'

If you have problems compiling Scipion, see
`Troubleshooting <https://scipion-em.github.io/docs/release-2.0.0/docs/user/troubleshooting.html>`__
page.

Step 4: Installing Xmipp3 and other EM Plugins
==============================================

Scipion can use many EM plugins. It is almost **mandatory to install
scipion-em-xmipp** (i.e. Scipion will run without it but with very
limited functionality).

For users
---------
To list and install plugins including Xmipp, you can use the plugin manager
(recommended) or, alternatively, use the `command line tool <install-plugins-command-line>`__ mentioned for
developers.

To open the plugin manager, please run Scipion

::

   cd scipion
   ./scipion

and choose Configuration > Plugins on the top bar. There, any plugin can be
easyly installed.

Since Xmipp is (almost) mandatory for processing with Scipion,
please **install scipion-em-xmipp** plugin and, then,
**install xmipp-3.19.03 software** by choosing one of these options
`depending on your OS </docs/docs/user/troubleshooting.html
#installing-scipion-xmipp-from-precompiled-bundles>`_:

* *xmippBin_Centos*: Pre-compiled bundle for Cenots OS.
* *xmippBin_Debian*: Pre-compiled bundle for Debian/Ubuntu/OpenSUSE OS.
* *xmippSrc*: Source code to compile in any OS (this option is only available if
  Scipion is installed from sources).

Please refer to the :ref:`Plugin manager guide <Plugin-Manager>` to get
more details about plugin installation options.

For developers
--------------
Developers might want to
build xmipp from the latest development version, please head
`here <https://github.com/I2PC/xmipp/wiki/Migrating-branches-from-nonPluginized-Scipion-to-the-new-Scipion-Xmipp-structure#xmipp>`__
if this is your case. You might also want to check how to :ref:`install
plugins from the command line <install-plugins-command-line>`.


Step 5: Cleaning up (Optional)
==============================

After Scipion is installed and properly working (see how to run tests in
the next section) one could clean some temporary files to free some disk
space after installation.

Remove the files under ``software/tmp`` folder:

::

    rm -rf sofware/tmp/*

The downloaded .tgz files of the EM packages can also be removed:

::

    rm -rf sofware/em/*.tgz

Next Steps
==========

-  Test your installation by running at least the *Small* and *Medium*
   tests mentioned in :ref:`running tests page <Running-Tests>`.
-  Complete some of the :ref:`Scipion Tutorials <User-Documentation>`.

