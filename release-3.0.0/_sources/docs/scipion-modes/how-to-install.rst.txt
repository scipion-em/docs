.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _how-to-install:

==================
Installing Scipion
==================

Prerequisites
=============

Scipion software requires GCC (GCC8 recommended) and OpenMPI already installed. CUDA (10.1 recommended) is optional but highly recommended.
Scipion uses conda package manager for installation. Before starting, make sure you do not have other cryo-EM software in your PATH / LD_LIBRARY_PATH as it might conflict with Scipion installation.

For Ubuntu:

::

    sudo apt-get install gcc-8 g++-8 libopenmpi-dev make

For CentOS:

::

    sudo yum -y install epel-release
    sudo yum-config-manager --enable epel
    sudo yum -y install libzstd-devel hdf5-devel gcc gcc-c++ openmpi-devel

Installation
============

1. If you do not have **conda** already installed (run ``which conda`` in your console), install `Miniconda <https://docs.conda.io/en/latest/miniconda.html#linux-installers>`__ as in example below. Alternatively, proceed to step 3.

::

    wget https://repo.anaconda.com/miniconda/Miniconda3-py39_4.9.2-Linux-x86_64.sh
    bash Miniconda3-py39_4.9.2-Linux-x86_64.sh -b -p /path/for/miniconda

2. Make sure you are running **bash** shell (run ``echo $SHELL`` in your console), then initialize conda:

::

    source /path/for/miniconda/etc/profile.d/conda.sh

3. Activate **base** conda environment and install Scipion installer with **pip3** provided by **conda**.

::

    conda activate
    pip3 install --user scipion-installer

4. Install Scipion core and generate default config files

::

    python3 -m scipioninstaller -conda -noXmipp -noAsk /path/for/scipion
    /path/for/scipion/scipion3 config --overwrite

5. Open **/path/for/scipion/config/scipion.conf** file and append the variables below to the end of the file. Make sure they point to correct locations for CUDA, OpenMPI and other software necessary for Xmipp:

::

    CUDA = True
    CUDA_BIN = /usr/local/cuda-10.1/bin
    CUDA_LIB = /usr/local/cuda-10.1/lib64
    MPI_BINDIR = /usr/lib64/mpi/gcc/openmpi/bin
    MPI_LIBDIR = /usr/lib64/mpi/gcc/openmpi/lib
    MPI_INCLUDE = /usr/lib64/mpi/gcc/openmpi/include
    OPENCV = False

See `Configuration guide <scipion-configuration>`_ for more details about these and other possible variables.

6. Install `Xmipp <https://github.com/I2PC/xmipp#xmipp>`__ plugin. We have tested Xmipp compilation on the following operating systems: `Ubuntu 16.04 <https://github.com/I2PC/xmipp/wiki/Installing-Xmipp-on-Ubuntu-16.04>`__, `Ubuntu 18.04 <https://github.com/I2PC/xmipp/wiki/Installing-Xmipp-on-Ubuntu-18.04>`__, `Ubuntu 20.04 <https://github.com/I2PC/xmipp/wiki/Installing-Xmipp-on-Ubuntu-20.04>`__, and `Centos 7 <https://github.com/I2PC/xmipp/wiki/Installing-Xmipp-on-CentOS-7-9.2009>`__. A list of dependencies can be found `here <https://github.com/I2PC/xmipp#additional-dependencies>`__. Command example below is using 12 threads



::

    /path/for/scipion/scipion3 installp -p scipion-em-xmipp -j 12 | tee -a install.log

7. Create an alias for Scipion launcher in your ``.bashrc`` file:

::

   alias scipion3="/path/for/scipion/scipion3"

If any of the steps above fails, check `install.log` file for errors and refer to the :ref:`Troubleshooting <troubleshooting>` guide.

Installing other plugins
========================

To list available plugins you can use the plugin manager (recommended) or, alternatively, use the `command line tool <install-plugins-command-line>`_.

To open the plugin manager, start Scipion (run **scipion3**) and choose **Others** > **Plugin manager** on the top bar. There, any plugin can be
easily installed.

Please, refer to the :ref:`Plugin manager guide <Plugin-Manager>` to get more details about plugin installation options.

If you have binaries installed for some of the plugins you can have a look at :ref:`Linking existing software <linking-existing-software>` page.

Clusters configuration
======================

To configure Scipion for a cluster you will need to edit the :ref:`host file <host-configuration>`

Test the installation
=====================

-  Test your installation by running at least the *Small* and *Medium* tests mentioned in the :ref:`Verify installation page <Verify-Installation>`.
-  Complete some of the :ref:`Scipion Tutorials <User-Documentation>`.
