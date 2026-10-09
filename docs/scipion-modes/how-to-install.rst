.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _how-to-install:

==================
Installing Scipion
==================

Scipion is written in python and it is comprised by 3 core pip packages and a launcher (scipion3): scipion-pyworkflow, scipion-em and scipion-app.
All is needed is either conda available or virtualenv to install Scipion.


Installation
============

1. If you do not have **conda** already installed (run ``which conda`` in your console), install Miniforge from its `official GitHub repository <https://github.com/conda-forge/miniforge>`__ or from `conda-forge <https://conda-forge.org/miniforge/>`__ as in the example below. Alternatively, proceed to step 3.

::

    wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh
    bash Miniforge3-Linux-x86_64.sh

During the process:

* Press Enter to scroll through the license agreement.
* Type yes to accept the terms.
* Confirm the default installation path (usually /home/your_user/miniforge3) or introduce the desired path.
* Crucial Step: When asked if you want to initialize Miniforge by running conda init, if you type yes, it ensures your shell is configured automatically, and in you type no, it won't be initialized each time a new terminal is opened, but only when you decide to manually launch it. In terms of Scipion installation, no matter the option chosen, the installer will take it into consideration and will work correspondingly.

2. Make sure you are running **bash** shell (run ``echo $SHELL`` in your console), then initialize conda:

::

    source /path/for/miniforge3/etc/profile.d/conda.sh

3. Activate **base** conda environment and install Scipion installer with **pip3** provided by **conda**.

::

    conda activate
    pip3 install --user scipion-installer

4. Install Scipion core and generate default config files

::

    python3 -m scipioninstaller -conda -noAsk /path/for/scipion
    /path/for/scipion/scipion3 config --overwrite

.. note::
   For HPC admins or curious minds, pass --dry and the installer will just print what it would have done instead of doing it. See https://pypi.org/project/scipion-installer/


5. Create an alias for Scipion launcher in your ``.bashrc`` file:

::

   alias scipion3="/path/for/scipion/scipion3"


Congratulations! You have installed Scipion. But a plain vainilla Scipion is useless. You will need some plugins and binaries associated.


For HPC Clusters
================
Do not let Scipion's plugins install any software. Although many plugins by default will install 3rd party software, HPC clusters probably already have them installed and optimized, so it is recommended in this scenario to CANCEL any installation done by Scipion.

.. note::

    You are going to need one Scipion installation per CPU compatible architecture. 
    
You may also want to protect scipion installation by preventing pip USER installations. 

Open **/path/to/scipion/config/scipion.conf** file and append the variable:

.. code-block:: bash
    
    SCIPION_DONT_INSTALL_BINARIES = True
    PYTHONUSERBASE = $CONDA_PREFIX/lib/python3.8/site-packages

.. note::
   Any value will cancel the installation of binaries

Now you can :ref:`install the plugins <docs/scipion-modes/how-to-install:installing other plugins>` your users have asked for.


3rd party prerequisites (non HPC installations)
==============================================
Most of the software Scipion installs requires GCC (GCC10 recommended) and OpenMPI already installed. CUDA (11.4 recommended) is optional but highly recommended.
Scipion uses conda package manager for installation. Before starting, make sure you do not have other cryo-EM software in your PATH / LD_LIBRARY_PATH as it might conflict with Scipion installation.

For Ubuntu:

::

    sudo apt-get install gcc-10 g++-10 libopenmpi-dev make

For CentOS:

::

    sudo yum -y install epel-release
    sudo yum-config-manager --enable epel
    sudo yum -y install libzstd-devel hdf5-devel gcc gcc-c++ openmpi-devel


Open **/path/for/scipion/config/scipion.conf** file and append the variables below to the end of the file. Make sure they point to correct locations for CUDA, OpenMPI and other software necessary for Xmipp:

::

    CUDA = True
    CUDA_BIN = /usr/local/cuda-11.4/bin
    CUDA_LIB = /usr/local/cuda-11.4/lib64
    MPI_BINDIR = /usr/lib64/mpi/gcc/openmpi/bin
    MPI_LIBDIR = /usr/lib64/mpi/gcc/openmpi/lib
    MPI_INCLUDE = /usr/lib64/mpi/gcc/openmpi/include
    OPENCV = False

See `Configuration guide <scipion-configuration>`_ for more details about these and other possible variables.




Scipion through SBGrid
=======================================

Scipion and Xmipp are also available through SBGrid, a software distribution platform that provides access to a broad collection of structural biology applications, including software for single-particle analysis (SPA), tomography, molecular modelling, and protein structure prediction.

This installation option requires membership in SBGrid. If you are already an SBGrid member and have installed and configured the SBGrid environment, you can install Scipion by running:

::
    sbgrid-cli install scipion

This command installs Scipion and provides access to Xmipp and the Scipion plugins supported by SBGrid, together with the corresponding software dependencies. Many of these applications are already configured to work with the SBGrid environment. Plugin availability and the underlying software may vary depending on your SBGrid access and installation.

For details about the available plugins, configuration, and usage, see the Scipion documentation on SBGrid and the Scipion entry in the SBGrid software catalogue.



Install xmipp
=============
`Xmipp <https://i2pc.github.io/docs/index.html>`__ is a good partner for Scipion in cryoem. It binds to Scipion environment offering more than a `hundred of protocols <https://i2pc.github.io/docs/protocolsMap.html>`__ to use in your SPA workflows It can be installed through Scipion's plugin manager, which handles the installation of the required components.

For detailed instructions, system `requirements <https://i2pc.github.io/docs/Installation/Requirements/index.html>`__ , and configuration options, refer to the Xmipp installation `documentation <https://i2pc.github.io/docs/#>`__.

.. note::
  For HPC clusters the above command should not have installed (compiled) Xmipp. You need to compile it manually following `those steps <https://i2pc.github.io/docs/Installation/Installations/index.html#installation-for-hpc-clusters>`__

.. note::
    If you want to install the devel version `please visit this page <https://i2pc.github.io/docs/Installation/Installations/index.html#standlone-installation>`__


Installing other plugins
========================

To list available plugins you can use the plugin manager (recommended) or, alternatively, use the :ref:`command line tool <install-plugins-command-line>`.

To open the plugin manager, start Scipion (run **scipion3**) and choose **Others** > **Plugin manager** on the top bar. There, any plugin can be
easily installed.

Please, refer to the :ref:`Plugin manager guide <Plugin-Manager>` to get more details about plugin installation options.

If you have binaries installed for some of the plugins you can have a look at :ref:`Linking existing software <linking-existing-software>` page.

Integration with queue engines (slurm, others)
==============================================

To configure Scipion to send jobs to a queue engine like Slurm you will need to edit the :ref:`host file <host-configuration>`

Test the installation
=====================

- Complete some of the Scipion tests:

    - Verify Scipion core plugins by running: ``scipion3 test --grep pyworkflowtests --run`` (<1 min)
    - Verify Xmipp compilation by running ``scipion3 tests pwem.tests.protocols.test_protocols_import_volumes`` (<1 min). Double check by opening the test project and displaying output volumes with Scipion viewer.
    - Check whether CUDA and MPI work properly: ``scipion3 tests xmipp3.tests.test_protocols_xmipp_3d.TestXmippProjMatching`` (2 min)

-  Complete some of the :ref:`Scipion Tutorials <User-Documentation>`.
