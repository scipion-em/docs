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

1. If you do not have **conda** already installed (run ``which conda`` in your console), install `Miniconda <https://docs.conda.io/en/latest/miniconda.html#linux-installers>`__ as in example below. Alternatively, proceed to step 3.

::

    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
    bash Miniconda3-latest-Linux-x86_64.sh -b -p /path/for/miniconda

2. Make sure you are running **bash** shell (run ``echo $SHELL`` in your console), then initialize conda:

::

    source /path/for/miniconda/etc/profile.d/conda.sh

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

.. code::
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

Install xmipp
=============
Xmipp is a good partner for Scipion in cryoem. It binds to Scipion environment offering file format (stk, vol, mrc, tiff, dm4,...) conversions for many cryo em methods and more than a hundred of protocols to use in your SPA workflows

To install `Xmipp <https://i2pc.github.io/docs/index.html>`__ plugin, please review the `requirements <https://i2pc.github.io/docs/Installation/Requirements/index.html>`__ . If all of them are available in your system you can install it you can install Xmipp from the :ref:`Plugin manager guide <Plugin-Manager>` or from the terminal as this:

::

    /path/for/scipion/scipion3 install -p scipion-em-xmipp  | tee -a install.log

.. note::
  For HPC clusters the above command should not have installed (compiled) xmipp. You need to compile it manually. Go here: https://i2pc.github.io/docs/Installation/Standlone-installation/index.html

.. note::
    If you want to install the devel version `please visit this page <https://i2pc.github.io/docs/Installation/Standlone-installation/index.html#standalone-installation>`__


If any of the steps above fails, check `install.log` file for errors, visit the `documentation <https://i2pc.github.io/docs/#>`__ and do not hesitate to `contact us https://i2pc.github.io/docs/contact.htmlrefer>`__

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
