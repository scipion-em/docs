.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _scipion-configuration:

=====================
Scipion configuration
=====================
In scipion3, configuration step is optional. Without a configuration file, scipion and the plugins
will run with default values and what is available in the system (usually what is exposed with PATH
and LD_LIBRARY_PATH).

If you want to know what are the default values type:

::

    scipion3 printenv

In the moment default values does not work for you, you are going to need a config file.
Cases for this is to customize installation of some binaries  (xmipp, relion) to use a specific mpi
or cuda version or to tell a plugin to use a specific binary version.

A special case is when you need need scipion3 to be integrated in a cluster. For this you are going
to need a :ref:`host file <host-configuration>`.

Running scipion3 config
=======================
This is the command used to generate config files or analyze them if you already have them.

::

    ./scipion3 config

The configuration files generated with this command are in one location:

* ``<your-scipion-home>/config`` contains configuration files for this Scipion installation,
  which will be applied to everyone using it. There are three files stored here:

        - ``<your-scipion-home>/config/scipion.conf`` with general variables to run scipion,
          install and use external libraries, etc. Also, all plugin-defined variables will be
          added for those plugins already installed.
        - ``<your-scipion-home>/config/hosts.conf`` with the host configuration.
          You can find more about it in the :ref:`host configuration page <host-configuration>`.

* ``~/.config/scipion/scipion.conf`` will be read if present but scipion3 will never generate this file.
This could be useful if you want to overwrite generic scipion3 configuration.

For example, below is an excerpt of
``config/scipion.conf`` adapted for an Ubuntu computer:

::

    [PYWORKFLOW]
    SCIPION_DOMAIN = pwem
    SCIPION_FONT_NAME = Helvetica
    SCIPION_LOG = ~/ScipionUserData/logs/scipion.log
    SCIPION_NOTIFY = True
    SCIPION_SOFTWARE = ${SCIPION_HOME}/software
    (...)

    [PLUGINS]
    CCP4_HOME = %(EM_ROOT)s/ccp4-7.0.056
    CHIMERA_HOME = %(EM_ROOT)s/chimerax-1.0
    CISTEM_HOME = %(EM_ROOT)s/cistem-1.0.0-beta
    (...)

Notice that in the excerpt above, ``CCP4_HOME``, ``CHIMERA_HOME`` and ``CISTEM_HOME``
are set to a certain path, determining a certain version. On the other hand, the
variables that are not defined here will remain by default and a plugin update will
eventually update them.

Run

::

    ./scipion3 config -p pluginPackage

to see the plugin-variables associated to a certain plugin.
Note that ``pluginPackage`` is the package name of the plugin,
check :ref:`the plugin's packages list <Plugins-API>`
(e.g. ``xmipp3`` is the package name for the ``scipion-em-xmipp`` plugin)

Once ``config/scipion.conf`` is changed, run ``./scipion3 config`` again
to make some checks.

If you have configuration files from previous installations, you may
want to use this instead (consider to make a backup of you config files before):

::

    ./scipion3 config --overwrite

Check also the `Xmipp documentation on the configuration <https://github.com/I2PC/xmipp/wiki/Xmipp-configuration-(version-20.07)>`_.


GPU variables
=============

Scipion is not compiling/running anything in GPU but it can provide some
configuration to its plugins and their binaries. Scipion is always passing the
``PATH`` and the ``LD_LIBRARY_PATH`` present in the Scipion launching time.
However, a certain cuda toolkit can be set at ``config/scipion.conf``.

For instance,

::

    CUDA_BIN = /usr/local/cuda-10.1/bin
    CUDA_LIB = /usr/local/cuda-10.1/lib64

where ``CUDA_BIN`` is intended only for compiling proposes (it should contain
the ``nvcc`` compiler) and ``CUDA_LIB`` will be added to the ``LD_LIBRARY_PATH``.

In addition, plugins can define its own cuda config variables in order to be able
to use a different cuda toolkit from one plugin to the other. Then, one can set
some of the following config variables at ``config/scipion.conf``

::

    XMIPP_CUDA_BIN = None  # Only for compiling purposes (overrides CUDA_BIN)
    XMIPP_CUDA_LIB = None  # Fill to override scipion CUDA_LIB
    RELION_CUDA_BIN = None  # Only for compiling purposes (overrides CUDA_BIN)
    RELION_CUDA_LIB = None  # Fill to override scipion CUDA_LIB
    GAUTOMATCH_CUDA_LIB = None  # Fill to override scipion CUDA_LIB
    GCTF_CUDA_LIB = None  # Fill to override scipion CUDA_LIB
    MOTIONCOR2_CUDA_LIB = None  # Fill to override scipion CUDA_LIB

Check also the `Xmipp-CUDA documentation <https://github.com/I2PC/xmipp/wiki/Xmipp-configuration-(version-20.07)#cuda-configuration>`_.

MPI variables
=============

Scipion uses ``mpi4py`` to launch different steps in parallel and doesn't require
any additional configuration to do that
(see :ref:`host configuration page <host-configuration>` for more details).
However, Scipion can provide MPI configuration to its plugins and their binaries/compilations
by setting the following variables in the ``config/scipion.conf``

::

    MPI_BINDIR = /usr/lib64/mpi/gcc/openmpi/bin
    MPI_LIBDIR = /usr/lib64/mpi/gcc/openmpi/lib
    MPI_INCLUDE = /usr/lib64/mpi/gcc/openmpi/include

Check also the `Xmipp-MPI documentation <https://github.com/I2PC/xmipp/wiki/Xmipp-configuration-(version-20.07)#mpi-configuration>`_.

JAVA variables
==============

Scipion uses ShowJ from Xmipp for visualization proposes and ShowJ is coded in
Java. For that, ``java`` command must be visible to launch ShowJ and visualize
viewers. In addition, Xmipp will look for java libs in compilation time to be
able to generate the ShowJ programs.

You can fix a certain java toolkit by setting the following config variables at
``config/scipion.conf``

::

    JAVA_HOME = /usr/lib/jvm/java-*  # Fill * with you java version
    JAVA_BINDIR = %(JAVA_HOME)s/bin
    JAR = %(JAVA_BINDIR)s/jar
    JAVAC = %(JAVA_BINDIR)s/javac
    JNI_CPPPATH = %(JAVA_HOME)s/include:%(JAVA_HOME)s/include/linux

note that settings above are the default ones, then they will be used if not provided.

Check also the `Xmipp-Java documentation <https://github.com/I2PC/xmipp/wiki/Xmipp-configuration-(version-20.07)#java-configuration>`_.


OpenCV flag
===========

To install Xmipp without OpenCV and, then skipping the programs using it
(Optical Alignment and Volume Enrich),
you can set OPENCV to False in ``scipion.conf``:

::

    OPENCV = False

Check also the `Xmipp-OpenCV documentation <https://github.com/I2PC/xmipp/wiki/Xmipp-configuration-(version-20.07)#opencv-configuration>`_.



Running Scipion in multi-users environment
==========================================

In the case we want to install Scipion on a Cluster for many users, it is
convenient to have a single ``scipion.conf`` file for all of them, otherwise, the
each user must have a config file under his home folder as described above.

We can launch Scipion with the --config parameter: ``--config <scipion.conf PATH>``.
This parameter tells Scipion to be use a configuration file in a specific path.

``--config`` will tell scipion3 to use that config and ONLY that one.

NOTE: Scipion3 installer creates a launcher (python script) called scipion3. That file is
good place to enforce using a common config file:

Fragment of scipion3 script:
::

    (...)
    cmd += "python -m scipion --config  <scipion.conf PATH> %s" % " ".join(sys.argv[1:])
    (...)

To fix the config from the console
::

    ./scipion3 --config <scipion.conf PATH>


======

If you have problems compiling Scipion, see
`Troubleshooting <https://scipion-em.github.io/docs/release-2.0.0/docs/user/troubleshooting.html>`__
page.