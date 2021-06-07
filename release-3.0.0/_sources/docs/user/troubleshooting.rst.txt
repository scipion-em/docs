.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _troubleshooting:

===============
Troubleshooting
===============

This page compiles a list of common errors that can appear when
using Scipion.

.. contents::

Launcher scipion3 not found
===========================
The ``scipion3`` launcher is created at the end of the installation. Then, if the installation is not completed
(e.g. Xmipp compilation have failed) it will not be created.

If you want to run something like ``scipion3 config``, but you get an error like

::

    scipion3: command not found

then, consider to run the Scipion's installer in *dry* mode in order to get some hints

::

    python -m scipioninstaller /path/where/you/want/scipion [-venv] -j 4 -dry

where ``-venv`` must be included if you are using virtualenv, whereas it must not if conda is used.

This command above prints a lot of information. Especially, at the end, it prints the content of the launcher. Therefore,
take the text enclosed between horizontal lines and copy it in a file placed at ``<SCIPION_HOME>/scipion3`` and
run ``chmod +x $SCIPION_HOME/scipion3`` to make it executable. That's your launcher.

Updating the installer
======================
Updating the installer may fix several installation issues. It's always a good practice to update it in case you find any issue.

If you've tried to install scipion3 sometime ago, you may have an old installer. To update it run the following commands:

::

    python -m pip uninstall scipion-installer
    python -m pip install scipion-installer

This should bring you the latest published version as show here: https://pypi.org/project/scipion-installer/ 

General error while installing/compiling Xmipp (non-development installations)
==============================================================================
Scipion installation also includes the Xmipp compilation and installation, by default.
You can install only Scipion (without Xmipp) by adding the ``-noXmipp`` flag to the installation command.

Xmipp can be installed separately using the plugin manager or by

::

    scipion3 installp scipion-em-xmipp -j 4


If you are getting an error during the Xmipp compilation, consider to check the
:ref:`Scipion's configuration page <scipion-configuration>` or the
`Xmipp's configuration page <https://github.com/I2PC/xmipp/wiki/Xmipp-configuration-(version-20.07)>`_.

Xmipp bundle is placed at ``<SCIPION_HOME>/software/em/xmippSrc-v3.20.07`` (production mode), see the
`Xmipp structure guide <https://github.com/I2PC/xmipp/wiki/Xmipp-structure>`_ for more information regarding Xmipp.

You can manually set some variables in the ``<SCIPION_HOME>/software/em/xmippSrc-v3.20.07/xmipp.conf``. However, Scipion
will automatically override this config file when recompiling Xmipp. To prevent this, ``export XMIPP_NOCONFIG=True`` or
include ``XMIPP_NOCONFIG=True`` in the ``<SCIPION_HOME>/config/scipion.conf`` prior to trigger a new compilation.

To retry the Xmipp compilation during the Scipion's installation, run

::

    python -m scipioninstaller /path/where/you/want/scipion [-venv] -j 4

Alternatively, if scipion3 is already installed you can go with the plugin manager or by running

::

    scipion3 installb xmippSrc -j 4

If ``ERROR: Could not find target xmippSrc`` is gotten, try to run

::

    scipion3 installp scipion-em-xmipp -j 4


If the problem persist, don't hesitate to :ref:`contact us <contact-us>`.


General error while installing/compiling Xmipp (development installations)
==============================================================================
Scipion installation also includes the Xmipp compilation and installation, by default.
You can install only Scipion (without Xmipp) by adding the ``-noXmipp`` flag to
the installation command.

Xmipp can be installed separately following the
`Xmipp's installation guide <https://github.com/I2PC/xmipp#xmipp-as-a-standalone-bundle-for-developers>`_.

If you are getting an error during the Xmipp compilation, consider to check the
:ref:`Scipion's configuration page<scipion-configuration>` or the
`Xmipp's configuration page <https://github.com/I2PC/xmipp/wiki/Xmipp-configuration-(version-20.07)>`_.

Xmipp bundle is placed at ``<SCIPION_HOME>/xmipp-bundle`` (devel mode), see the
`Xmipp structure guide <https://github.com/I2PC/xmipp/wiki/Xmipp-structure>`_
for more information regarding Xmipp.

You can manually set some variables in the ``<SCIPION_HOME>/xmipp-bundle/xmipp.conf``.
However, Scipion will automatically override this config file when recompiling Xmipp.
To prevent this, ``export XMIPP_NOCONFIG=True`` or include ``XMIPP_NOCONFIG=True``
in the ``<SCIPION_HOME>/config/scipion.conf`` prior to trigger a new compilation.

To retry the Xmipp compilation during the Scipion's installation, run

::

    python -m scipioninstaller /path/where/you/want/scipion [-venv] -j 4 -dev

Alternatively, if scipion3 is already installed you can go with

::

    scipion3 installb xmippDev -j 4

If ``ERROR: Could not find target xmippDev`` is gotten, try to run

::

    scipion3 installp -p <SCIPION_HOME>/xmipp-bundle/src/scipion-em-xmipp --devel -j 4


If the problem persist, don't hesitate to :ref:`contact us <contact-us>`.


Installing Scipion/Xmipp from precompiled bundles
=================================================

From Scipion's version 3, no precompiled bundles are provided.

The reason is:

  * Scipion is now a set of general Python modules, which are installed from
    'pip' and nothing needs to be compiled anymore.

  * From Scipion's version 3, the installation configuration is more flexible.
    This makes things easier in compiling time,
    but becomes in an explosion of possibilities on final systems configuration
    (mostly related with different versions of common libraries).
    This ends up making it impossible to predict what configuration is on your system,
    to allow us to prepare a precompiled bundle for you.

Nevertheless, we have experimented a noticeable improvement in the stability
in compilation time for the most used Linux distributions (and its most recent versions)
during the beta-testing period.
However, if you are in some troubles, please, don't hesitate to :ref:`contact us <contact-us>`.

Compiling Xmipp to be used in both Intel and AMD cores
======================================================

Xmipp is optimizing the compilation to the architecture found in the compilation
time. However, this is not a good idea if it must run on both AMD and Intel cores
at once (e.g. in a cluster or so). To make more flexible the optimization on the
compilation, then the ``CXXFLAGS`` can be set properly.

Please, just

::

    export CXXFLAGS="-mfma -mavx2 -m3dnow -fomit-frame-pointer -std=c++11 -O3"

before running the Scipion3 installer.

Please, check `Xmipp's configuration page <https://github.com/I2PC/xmipp/wiki/Xmipp-configuration-(version-20.07)>`_
for more details.


Cannot compile with Java
========================

::

    Checking Java configuration...
    /usr/lib/jvm/java-11-openjdk-amd64/bin/javac Xmipp.java
    /bin/sh: 1: /usr/lib/jvm/java-11-openjdk-amd64/bin/javac: not found
    Check the JAVAC
    Cannot compile with Java

Java compiler is missing. Needs to install the jdk-devel version.
In ubuntu would be like:

::

    sudo apt-get install openjdk-11-jdk

or activate a jdk with javac using alternatives.  

If this is not the case, and you have <SCIPION_HOME>/config/scipion.conf (optional),
review the JAVA_XXX variables there. They might be pointing to a non existing JAVA home.


Troubleshooting for previous Scipion's versions
===============================================

Fixing libjbig.so.0 not found in OpenSUSE42.3
---------------------------------------------

When Scipion_Ubuntu precompiled bundle is installed, maybe a "libjbig.so.0 not found" error is raised.
We have observed that OpenSUSE includes libjbig.so.2 and we have checked that is also valid,
thus we propose to link one to the other by

::

  sudo ln -s /usr/lib64/libjbig.so.2 /usr/lib64/libjbig.so.0

Fixing fonts in Ubuntu 18
-------------------------
The Scipion font is not right in Ubuntu 18. A temporary fix for this is to
remove all TK and TCL files in `software/lib` and use the system/conda ones.


Launching Eman boxer protocol
-----------------------------

If you see an error like '*Cannot mix incompatible Qt library (version
0x40806) with this library (version 0x40804)*'. This means the Qt
installed on your computer is conflicting with the Qt distributed with
EMAN2. In most cases it gets solved by removing the Qt that comes with
EMAN2 from ``EMAN2DIR/extlib/lib``.

Relion3 compilation with CUDA8.0 and g++>6
------------------------------------------

If you are getting an error telling that g++ later than 6 is not supported 
by nvcc8, you can set a lower g++ compiler in the ``$SCIPION_HOME/config/scipion.conf``
for instance ``CC=gcc-5`` and ``CXX=g++-5``. To do that you need to have gcc/g++-5 installed.

--------------

Compiling Scipion with OpenCV
-----------------------------

If you have problems compiling Scipion with OpenCV support (CUDA version
>=6.5), e.g. opencv-2.4.9 compilation fails with an error:

::

    Error: target 'software/lib/libopencv_core.so' not built (after running 'make install > /home/user/soft/scipion/software/log/opencv_make_install.log 2>&1')

And log file (``software/log/opencv\_make.log``) shows something like:

::

    [ 9%] Building NVCC (Device) object modules/core/CMakeFiles/cuda_compile.dir/src/cuda/cuda_compile_generated_gpu_mat.cu.o
    /usr/include/string.h: In function ‘void* __mempcpy_inline(void, const void, size_t)’:
    /usr/include/string.h:652:42: error: ‘memcpy’ was not declared in this scope
    return (char *) memcpy (__dest, __src, __n) + __n;
    ^
    CMake Error at cuda_compile_generated_gpu_mat.cu.o.cmake:264 (message):
    Error generating file
    /home/mag/opencv/build_opencv_master/modules/core/CMakeFiles/cuda_compile.dir/src/cuda/./cuda_compile_generated_gpu_mat.cu.o

Then:

1. `Find <https://en.wikipedia.org/wiki/Nvidia_Tesla>`__ the
   micro-architecture name for your GPU card, e.g. Kepler for K40 or
   Fermi for M2070 card
2. ``cd $SCIPION_HOME/software/tmp/opencv-2.4.9``
3. Run
   ``cmake -DCUDA_GENERATION=Kepler -DWITH_CUDA:BOOL=ON -DCMAKE_INSTALL_PREFIX:PATH=/path/to/scipion/software . > /path/to/scipion/software/log/opencv_cmake.log 2>&1``
   substituting correct path and micro-architecture
4. Modify source files in opencv-2.4.9 folder according to
   `this <https://github.com/opencv/opencv/pull/2975/files>`__ and `this
   fix <https://github.com/guysoft/opencv/commit/0a48b9ae776a03e1c4f09e7e3cd0e1c21f3ca75c>`__
5. Re-run ``scipion install``, opencv now should compile cleanly \*\*\*

Scipion freezes after click on open bibtex
------------------------------------------

This likely happens because your machine doesn't have a default program
to open bibtex. Type this in your terminal to set gedit as your default
program for bibtex files:

::

    xdg-mime default gedit.desktop text/x-bibtex

--------------

Compiling Scipion in Opensuse
-----------------------------

Scipion installation in Opensuse sometimes involves a few drawbacks. Once
in the terminal the compilation has been launched,
``./scipion install``, stop the installation (``Crtl+C``). It is
necessary to change the python version (download python 2.7.13). Copy
the download file to ``scipion\software\tmp\`` and edit next file
``scipion\software\install\script.py``

The line in which the python version is specified must be modified by
the downloaded version 2.7.13, it means to substitute the old version
2.7.8 by 2.7.13. Finally we can go to the terminal again and relaunch
the installation by doing ``./scipion install``.

--------------

Endless list of CUDA related errors
-----------------------------------

**Conditions** \* CUDA set to True (in ``config\scipion.conf``) \*
Multiple CUDA versions are installed

**Example**

::

     /usr/local/cuda/include/crt/common_functions.h:64:0: warning: "__CUDACC_VER__" redefined #define __CUDACC_VER__ "__CUDACC_VER__ is no longer supported. Use __CUDACC_VER_MAJOR__, __CUDACC_VER_MINOR__, and __CUDACC_VER_BUILD__ instead." ^ <command-line>:0:0: note: this is the location of the previous definition

::

     /usr/local/cuda/include/device_atomic_functions.h(107): warning: missing return statement at end of non-void function "atomicAdd"

**Cause**

Version conflict while linking

**Fix**

make sure that all paths to \*CUDA\* and \*NVCC\* in
``config\scipion.conf`` are absolute

--------------

Requirement already satisfied
-----------------------------

**Conditions** 1. you had Scipion already installed (from source) 2.
later on you installed numpy again (e.g. with pandas) 3. you want to
reinstall Scipion (from source)

**Example**

::

    Building numpy ...
    python /home/user/Scipion/software/lib/python2.7/site-packages/pip install numpy==1.14.1
    Requirement already satisfied: numpy==1.14.1 in /home/user/.local/lib/python2.7/site-packages
    Error: target '/home/user/Scipion/software/lib/python2.7/site-packages/numpy' not built (after running 'python /home/user/Scipion/software/lib/python2.7/site-packages/pip install numpy==1.14.1')

**Cause**

Numpy version conflict?

**Fix**

uninstall Scipion's version of numpy

::

    scipion run pip uninstall numpy
    rm -rf software/lib/python2.7/site-packages/numpy

run install again

::

    scipion install -j 8

--------------

ImportError: cannot import name HTTPSHandler
--------------------------------------------

**Example**

.. code:: python

    Building pip ...
    python scripts/get-pip.py -I --no-setuptools
    Traceback (most recent call last):
      File "scripts/get-pip.py", line 19177, in <module>
        main()
      File "scripts/get-pip.py", line 194, in main
        bootstrap(tmpdir=tmpdir)
      File "scripts/get-pip.py", line 82, in bootstrap
        import pip
      File "/tmp/tmpXJbtSy/pip.zip/pip/__init__.py", line 16, in <module>
        # *
      File "/tmp/tmpXJbtSy/pip.zip/pip/vcs/subversion.py", line 9, in <module>
      File "/tmp/tmpXJbtSy/pip.zip/pip/index.py", line 30, in <module>
      File "/tmp/tmpXJbtSy/pip.zip/pip/wheel.py", line 39, in <module>
      File "/tmp/tmpXJbtSy/pip.zip/pip/_vendor/distlib/scripts.py", line 14, in <module>
      File "/tmp/tmpXJbtSy/pip.zip/pip/_vendor/distlib/compat.py", line 31, in <module>
    ImportError: cannot import name HTTPSHandler
    Error: target 'scipion/software/lib/python2.7/site-packages/pip' not built (after running 'python scripts/get-pip.py -I --no-setuptools')

**Cause**

Missing libssl-dev

**Fix**

.. code:: bash

    sudo apt-get install libssl-dev
    rm -rf software/bin/python* software/lib/python2.7/
    ./scipion install

--------------

Launching XMIPP3 CL2D protocol
------------------------------

**Error: libmpi.so - No such file or directory**

If executing Xmipp3-cl2d protocol fails with an error:

::

    .../Scipion/Projects/release-1.2.1/scipion/software/em/xmipp/bin/xmipp_mpi_classify_CL2D: error while loading shared libraries: libmpi.so.1: cannot open shared object file: No such file or directory
    ...
    ...
    ...
    Protocol failed: Command 'mpirun -np 4 -bynode  `which xmipp_mpi_classify_CL2D` -i
    Runs/002697_XmippProtCL2D/tmp/input_particles.xmd --odir Runs/002697_XmippProtCL2D/extra --oroot level --nref 8
    --iter 10  --distance correlation --classicalMultiref --nref0 2' returned non-zero exit status 127

This means that the libmpi.so.1 library installed on your computer
cannot open.

**Fix**

Create a symbolic link to this library at the location of the libmpi.so
library (``/usr/lib/`` in Ubunut16 or ``/usr/lib/x86_64-linux-gnu`` in Ubuntu18).

Example:

Assuming that ``ls /usr/lib/libmpi.so`` find a file:

.. code:: bash

    ln -s /usr/lib/libmpi.so /usr/lib/libmpi.so.1

We have experimented something similar with libmpi_cxx.so.1

.. code:: bash

    ln -s /usr/lib/libmpi_cxx.so /usr/lib/libmpi_cxx.so.1

ImportError: libgfortran.so.3
-----------------------------

This has been reported on an UBUNTU-18 machine using binaries, but may
happen at compile time using sources. It was happening when launching
scipion. The error reported looked like this:

::

    Traceback (most recent call last):
      File "/home/xxx/bin/scipion/pyworkflow/apps/pw_manager.py", line 32, in <module>
        from pyworkflow.gui.project import ProjectManagerWindow
      File "/home/xxx/bin/scipion/pyworkflow/gui/__init__.py", line 27, in <module>
        from gui import *
      File "/home/xxx/bin/scipion/pyworkflow/gui/gui.py", line 34, in <module>
        from pyworkflow.utils.properties import Message, Color, Icon
      File "/home/xxx/bin/scipion/pyworkflow/utils/__init__.py", line 30, in <module>
        from utils import *
      File "/home/xxx/bin/scipion/pyworkflow/utils/utils.py", line 32, in <module>
        import numpy as np
      File "/home/xxx/bin/scipion/software/lib/python2.7/site-packages/numpy/__init__.py", line 153, in <module>
        from . import add_newdocs
      File "/home/xxx/bin/scipion/software/lib/python2.7/site-packages/numpy/add_newdocs.py", line 13, in <module>
        from numpy.lib import add_newdoc
      File "/home/xxx/bin/scipion/software/lib/python2.7/site-packages/numpy/lib/__init__.py", line 18, in <module>
        from .polynomial import *
      File "/home/xxx/bin/scipion/software/lib/python2.7/site-packages/numpy/lib/polynomial.py", line 19, in <module>
        from numpy.linalg import eigvals, lstsq, inv
      File "/home/xxx/bin/scipion/software/lib/python2.7/site-packages/numpy/linalg/__init__.py", line 50, in <module>
        from .linalg import *
      File "/home/xxx/bin/scipion/software/lib/python2.7/site-packages/numpy/linalg/linalg.py", line 29, in <module>
        from numpy.linalg import lapack_lite, _umath_linalg
    ImportError: libgfortran.so.3: cannot open shared object file: No such file or directory

**Cause**: Missing libgfortran.so.3

**Fix** :

The missing library can be installed using:
``sudo apt-get install libgfortran3``

bigtiff in Claudio
------------------

We have updated the tiff library to handle BIGtiff data and it is
available from Scipion version 2.0.0. If you are running Claudio
(v1.2.1) there are some steps you can follow to enable Scipion to work
with bigtiff data. Please, take into account that this hasn't been
extensively tested but all our tests where successful.

**Fix:**

If you are determined to move forward follow this steps:

1. open a terminal and cd to the scipion folder
2. backup your old libtiff files:

::

    mkdir software/lib/old_tiff
    mv software/lib/libtiff* software/lib/old_tiff/

3. modify scipion to use libtiff 4.0.10 (bigtiff lib)

``sed -i -e s/tiff-3.9.4/tiff-4.0.10/ install/script.py``

4. Tell scipion to install bigtiff

``./scipion install tiff --no-xmipp``


Install Xmipp3 in Diocletian
----------------------------

Because we haven't installed
xmipp yet, you'll see a message saying something like this in the
terminal:

::

   Scipion v2.0 (2019-03-12) Diocletian (release-2.0.0-fixes 50b9908)

   >>>>> python  /home/yaiza/Desktop/scipion/pyworkflow/apps/pw_manager.py

   >>> WARNING: Xmipp binaries not found. Ghost active.....BOOOOOO!
      > Please install Xmipp to get full functionality.
   (Configuration->Plugins->scipion-em-xmipp in Scipion manager window)
   
or this one when importing something:

::

   Error: AttributeError
   Description: 'NoneType' object has no attribute 'isImage'
   Traceback:
     File "/home/me/scipion/pyworkflow/protocol/protocol.py", line 1817, in validate
       childErrors = self._validate()

     File "/home/me/scipion/pyworkflow/em/protocol/protocol_import/images.py", line 372, in validate
       errors += self.validateImages()

     File "/home/me/scipion/pyworkflow/em/protocol/protocol_import/images.py", line 354, in validateImages
       ih.isImageFile(imgFn))):

     File "/home/me/scipion/pyworkflow/em/convert/imagehandler.py", line 436, in isImageFile
       return xmippLib.FileName(imgFn).isImage() 

* Open Plugin Manager

.. image:: /docs/images/guis/scipion_config_menu.png
   :alt: Scipion project manager

* Select Xmipp to install it by clicking on the empty checkbox on the left.

.. image:: /docs/images/guis/plugin_manager_install_xmipp.png
   :alt: plugin manager

* Add the number of processors you'd like to use (the more, the merrier!).
  Then click on the install button on the operations tab

.. image:: /docs/images/guis/plugin_manager_install_xmipp_install_button.png
   :alt:  plugin manager install xmipp

* Now we can check the progress on the Output log tab (or go make some coffee, Xmipp
  installation will take a bit!).
  You might have to refresh the logs by clicking on the refresh symbol on the right.
  Please note that messages might not appear in order if we are using more than 1 processor.

.. image:: /docs/images/guis/plugin_manager_xmipp_install_logs.png
   :alt: install xmipp logs

* When the operation gets a green check, it's done!

.. image:: /docs/images/guis/plugin_manager_xmipp_done.png
   :alt: install xmipp logs

**Note**: if xmipp installation fails, you might have to uninstall it with the plugin manager:

.. image:: /docs/images/guis/plugin_manager_xmipp_uninstall.png
   :alt: uninstall xmipp

And manually remove leftover elements:

::

   rm -rf software/em/xmipp*

* Now when we close and re-launch Scipion, we should get no messages.

::

  ./scipion

   Scipion v2.0 (2019-03-12) Diocletian (release-2.0.0-fixes 50b9908)

   >>>>> python  /home/yaiza/Desktop/scipion/pyworkflow/apps/pw_manager.py
   

scikit-learn installation fails
-------------------------------

If you are getting error while scipion tries to install scikit-learn python package, something like:

::

  00086:   Building scikit-learn ...
  00087:   /home/fanhc/Programs/scipion/software/bin/python /home/fanhc/Programs/scipion/software/lib/python2.7/site-packages/pip install scikit-learn==0.17
  00088:   Collecting scikit-learn==0.17
  00089:     Using cached https://files.pythonhosted.org/packages/60/b8/c420dce3f72d95e06f7c1e50a6e705f4e8b6078d7d6db38425ac77ae3fab/scikit-learn-0.17.tar.gz
  00090:   Building wheels for collected packages: scikit-learn
  00091:     Building wheel for scikit-learn (setup.py): started
  00092:     Building wheel for scikit-learn (setup.py): finished with status 'error'
  00093:     Running setup.py clean for scikit-learn
  00094:   Failed to build scikit-learn
  00095:   Installing collected packages: scikit-learn
  00096:     Running setup.py install for scikit-learn: started
  00097:       Running setup.py install for scikit-learn: finished with status 'error' 

Try to run:

::

  scipion python -m pip install scikit-learn==0.17.1

sh_alignment installation fails
-------------------------------

Some program in Xmipp use the **sh_alignent** library. If you get some of the errors
below try the following:

* **swig: Command not found**: Install ``swig`` in your computer,
  ie. ``sudo apt-get install swig`` (``yum`` in Centos distros and ``zypper`` in OpenSUSE).


Deep consensus fail due to index out of run.
--------------------------------------------

We have find a bug reporting the following error:

::

    133   consensusNpixels = consensusRadius* boxSize
    134
    135   # Add the rest of coordinates
    136   Ncurrent = N0
    137   for n in range(1, len(coords_files)):
    138     for coord in coords[n]:  <----------------------- BUG
        coord = array([2379,  102])
        coords = [array([[3543,  222],
       [3757,  133],
      ...3935],
       [3063, 3935],
       [ 712, 3944]]), array([[1136,  280],
       [2388, 2416],
      ... 120],
       [1788,  624],
       [2608, 3204]]), array([[ 663, 3811],
       [ 287, 3688],
      ... 162],
       [3048,  159],
       [2379,  102]])]
        n = 3
    139       if Ncurrent > 0:
    140         dist = np.sum((coord - allCoords[0:Ncurrent])**2, axis=1)
    141         imin = np.argmin(dist)
    142         if sqrt(dist[imin]) < consensusNpixels:

This bug should be fixed for versions after v19.04. However, to fix it in
prior versions, please download the bug-fixed file to your Xmipp installation.

::

    wget -O $(scipionBIN run printenv | grep XMIPP_HOME | sed 's/.*=//')/bin/xmipp_coordinates_consensus https://raw.githubusercontent.com/I2PC/xmipp/devel/applications/scripts/coordinates_consensus/coordinates_consensus.py

Please, ensure it has executable permissions

::

    chmod a+x $(scipionBIN run printenv | grep XMIPP_HOME= | sed 's/.*=//')/bin/xmipp_coordinates_consensus
