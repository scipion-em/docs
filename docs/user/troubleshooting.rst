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

Fixing fonts in a conda installation
====================================
This will fix the ugly fonts issue when using conda installation

::

    scipion3 run conda remove tk --force
    wget https://anaconda.org/scipion/tk/8.6.10/download/linux-64/tk-8.6.10-h14c3975_1005.tar.bz2
    scipion3 run conda install tk-8.6.10-h14c3975_1005.tar.bz2

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

    scipion3 installp -p scipion-em-xmipp -j 4


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

    scipion3 installp -p scipion-em-xmipp -j 4


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

