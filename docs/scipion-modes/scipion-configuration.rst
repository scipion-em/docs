.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _scipion-configuration:

=====================
Scipion configuration
=====================
In scipion3, configuration step is optional. Without a configuration file scipion and the plugins
will run with default values and what is available in the system (usually what is exposed with PATH
and LD_LIBRARY_PATH).

In the moment default values does not work for you, you are going to need a config file.
Cases for this is to customize installation of some binaries  (xmipp, relion) to use a specific mpi
or cuda version or to tell a plugin to use a specific binary version.

A special case is when you need need scipion3 to be integrated in a cluster. For this you are going
to need a host.conf file.

Running scipion3 config
=======================
This is the command used to generate config files or analyze them if you already have them.

::

    ./scipion3 config

The configuration files generated with this command are in one location:

* ``<your-scipion-home>/config`` contains configuration files for this Scipion installation,
  which will be applied to everyone using it. There are three files stored here:

        - ``<your-scipion-home>/config/scipion.conf`` with general variables to run scipion,
          install and use external libraries, etc.
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

Once ``config/scipion.conf`` is changed, run ``./scipion config`` again.


Running Scipion in multi-users environment
==========================================

In the case we want to install Scipion on a Cluster for many users, it is
convenient to have a single ``scipion.conf`` file for all of them, otherwise, the
each user must have a config file under his home folder as described above.

We can launch Scipion with the --config parameter: ``--config <scipion.conf PATH>``.
This parameter tells Scipion to be use a configuration file in a specific path.

--config will tell scipion3 to use that config and ONLY that one.

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
