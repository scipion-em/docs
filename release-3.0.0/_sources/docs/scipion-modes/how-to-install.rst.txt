.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _how-to-install:

=======================
Installing Scipion v3.0
=======================

Prepare installation
====================

pip
===
You need to have python2 or 3 already and pip or pip3. There are several ways to test if pip
is installed. pip comes out of the box with conda.

::

    conda activate

Will bring you pip.

To test if you have pip available type:

::

    python -m pip -V

Other alternatives would be:

::

    python3 -m pip -V
    pip -V
    pip3 -V

If any of these commands does not fail, you have pip. If you don't have it please, check
https://pip.pypa.io/en/stable/installing/ or use your package manager (yum, apt-get,...)
to install pip or pip3.

CUDA (optional, highly recommended):
====================================
Many of the software that Scipion integrates use CUDA. You can have different CUDA versions
installed and choose which CUDA to use for any particular software. Nevertheless, CUDA 10.1
seems to be compatible with the majority of them. We recommend to have CUDA 10.1 installed
and being linked at /usr/local/cuda.  By default scipion point to /usr/local/cuda and xmipp
installation is done against this path.

Conda (optional, recommended if you are not admin)
==================================================
Although conda is not a requirement, conda provides most of the dependencies Scipion and Xmipp
needs and can be installed without being admin.

Miniconda (https://docs.conda.io/en/latest/miniconda.html#linux-installers) would be enough.

Scipion installation
====================
We have prepared some recipes to install Scipion and its companion Xmipp in the most simplified way.
Below you can find some installation hints that could help you to troubleshoot your case. Scipion
can be installed using conda or virtualenv. Conda installation has one drawback: conda will not identify
properly the fonts in your system and you will end up with a font we didn’t intend but readable and
workable. Don't worry there is a `fix for this bellow <install-from-sources#fixing-fonts-in-a-conda-installation>`_.

Ubuntu with conda
-----------------

::

    sudo apt-get install gcc-8 g++-8 libopenmpi-dev make
    conda activate
    export CXX_CUDA=g++-8
    export PATH=$PATH:/usr/local/cuda/bin
    pip install --user scipion-installer
    python -m scipioninstaller /path/where/you/want/scipion -j 4

Ubuntu with virtualenv
----------------------

::

    sudo apt-get install gcc g++ make libopenmpi-dev python3-tk libfftw3-dev libhdf5-dev libtiff-dev libjpeg-dev libsqlite3-dev openjdk-8-jdk
    export PATH=$PATH:/usr/local/cuda/bin
    python -m pip install --user scipion-installer
    python -m scipioninstaller /path/where/you/want/scipion -venv -j 4

CentOS with conda
-----------------

::

    sudo yum install gcc gcc-c++ openmpi-devel
    export PATH=$PATH:/usr/lib64/openmpi/bin/:/usr/local/cuda/bin
    conda activate
    pip install --user scipion-installer
    python3 -m scipioninstaller /path/where/you/want/scipion -j 4


CentOS with virtualenv
----------------------

::

    sudo yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm
    sudo dnf -y --enablerepo=PowerTools install libaec-devel
    sudo yum install gcc gcc-c++ make openmpi-devel python3-devel python3-tkinter wget fftw-devel hdf5-devel libtiff-devel libjpeg-devel sqlite-devel.x86_64 java-1.8.0-openjdk-devel
    export PATH=$PATH:/usr/lib64/openmpi/bin/:/usr/local/cuda/bin
    python3 -m pip install --user scipion-installer
    python3 -m scipioninstaller /path/where/you/want/scipion -venv -j 4


Launching scipion3
------------------
Installation should have created a launching file at <SCIPION_HOME>/scipion3.
For convenience, create an **alias** in the ``.bashrc`` file located
in ``/home/<user>/.bashrc`` that allows you to launch Scipion from any
location on your computer.

::

   alias scipion3='<SCIPION_HOME>/scipion3'

You can always launch it like <SCIPION_HOME>/scipion3 or ./scipion3 (if you are already in
scipion's installation folder)

Installing other EM Plugins
===========================
Scipion3 can use many EM plugins.

If you intend to develop some plugin, check the
**For developers** section below. However, if you only want to use the
plugin, just follow the **For users** section below.

For users
---------
To list and install plugins you can use the plugin manager
(recommended) or, alternatively, use the `command line tool <install-plugins-command-line>`__.

To open the plugin manager, please run Scipion

::

   cd scipion
   ./scipion3

and choose **Others** > **Plugin manager** on the top bar. There, any plugin can be
easily installed.

Please, refer to the :ref:`Plugin manager guide <Plugin-Manager>` to get
more details about plugin installation options.

For developers
--------------
Developers might want to build xmipp from the latest development version, please head
`here <https://github.com/I2PC/xmipp/blob/devel/README.md>`__
if this is your case. You might also want to check how to :ref:`install
plugins from the command line <install-plugins-command-line>`.

Optional steps
==============

Fixing fonts in a conda installation
------------------------------------
This will fix the fonts issue when using a conda installation

::

    conda activate .scipion3env
    conda remove tk --force
    wget https://anaconda.org/scipion/tk/8.6.10/download/linux-64/tk-8.6.10-h14c3975_1005.tar.bz2
    conda install tk-8.6.10-h14c3975_1005.tar.bz2

Test the installation and learn how to use Scipion
--------------------------------------------------
We also provide some :ref:`tests <Running-Tests>` and :ref:`tutorials <User-Documentation>`
to check that all is fine and to learn how to use Scipion.


Configure
---------

In scipion3, configuration step is optional. Without a configuration file, scipion and the plugins
will run with default values and what is available in the system (usually what is exposed with PATH
and LD_LIBRARY_PATH).

Please, check :ref:`Scipion's configuration page <scipion-configuration>` for more details.

Troubleshooting
---------------

If you have problems compiling Scipion, see
`Troubleshooting <https://scipion-em.github.io/docs/release-2.0.0/docs/user/troubleshooting.html>`__
page.



Cleaning up (Optional)
======================

After Scipion is installed and properly working (see how to run tests in
the next section) one could clean some temporary files to free some disk
space after installation.

Remove the files under ``software/tmp`` folder:

::

    rm -rf sofware/tmp/*

The downloaded .tgz files of the EM packages can also be removed:

::

    rm -rf sofware/em/*.tgz

Tests and tutorials
===================

-  Test your installation by running at least the *Small* and *Medium*
   tests mentioned in :ref:`running tests page <Running-Tests>`.
-  Complete some of the :ref:`Scipion Tutorials <User-Documentation>`.

