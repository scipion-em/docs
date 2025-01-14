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
(e.g. Xmipp compilation has failed) it will not be created.

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

Fixing the error with locale settings
=====================================

The following error can happen if your locale is set to C (you can see the locale settings with `locale` command)

:: 

    File ".../lib/python3.8/site-packages/tkcolorpicker/colorpicker.py", line 43, in <module>
    if getdefaultlocale()[0][:2] == 'fr':
    TypeError: 'NoneType' object is not subscriptable

The solution is to use our modified tkcolorpicker with a bug fix:

::

    scipion3 pip uninstall tkcolorpicker
    scipion3 pip install git+https://github.com/scipion-em/tkColorPicker@master

Fixing fonts in a conda installation
====================================
This will fix the ugly fonts issue when using conda installation

::

    scipion3 run "conda install -y -c conda-forge tk=*=xft_*"

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

If you are getting an error during the Xmipp compilation, consider to read compilationLog.txt file located in the xmipp floder (by default in scipion2/software/em) and review the `Xmipp's configuration page <https://i2pc.github.io/docs/Utils/ConfigurationF/index.html#configuration-file>`_.

Alternatively, you can go with the plugin manager or by running

::

    scipion3 installb xmippSrc 

If ``ERROR: Could not find target xmippSrc`` is gotten, try to run

::

    scipion3 installp -p scipion-em-xmipp 


If the problem persist, don't hesitate to `contact us https://scipion-em.github.io/docs/release-3.0.0/docs/misc/contact-us.html#contact-us>`__.


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

Please, check `Xmipp's configuration page <https://i2pc.github.io/docs/Utils/ConfigurationF/index.html#configuration-file>`_ for more details.


Xmipp dependencies
======================

HDF5
--------

We sometimes see issues regarding the HDF5 dependency.
We recommend removing all hdf5 versions and install just hdf5-devel. To do that:
```
sudo apt remove hdf5
sudo apt remove hdf5-devel
pip uninstall h5py
```
Remove all files related to hdf5 in /usr/lib64/libhdf5*, /usr/include/hdf5* and .../anaconda3/include/hdf5*. 

We strongy recommend you to install it via your default package manager:
`sudo apt-get install libhdf5-dev` 
If you install it using other package management system (such as Conda), it might lead to compile/link time issues caused by incompatible version being fetched.



Cannot compile with Java
-------------------------

::

    Checking Java configuration...
    /usr/lib/jvm/java-11-openjdk-amd64/bin/javac Xmipp.java
    /bin/sh: 1: /usr/lib/jvm/java-11-openjdk-amd64/bin/javac: not found
    Check the JAVAC
    Cannot compile with Java

Java compiler is missing. Needs to install the jdk-devel version.
In ubuntu would be like:

::

    sudo apt-get install default-jdk

or activate a jdk with javac using alternatives.  

If this is not the case, and you have <SCIPION_HOME>/config/scipion.conf (optional),
review the JAVA_XXX variables there. They might be pointing to a non existing JAVA home.

