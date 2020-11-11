.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _linking-existing-software:

=========================
Linking existing software
=========================

Scipion plugins can install most of the software that integrates and by default it will be done.
You can avoid the installation of the binaries as described
:ref:`here <install-plugins-command-line#install-plugin-without-binaries>`

There are 2 ways to link your own binaries to Scipion plugins, linking the installation folder or by editing the configuration file.

Linking the installation folder
===============================
All the software that Scipion installs, end up at ``SCIPION_HOME/software/em``
(unless you have overwritten this by defining ``EM_ROOT`` variable or ``SCIPION_SOFTWARE``).
In many of the cases the installation engine downloads and extracts tgz files there following a predefined pattern
(``<BINARY NAME>-version``). This means that if you install 'relion-3.1' you will end up with a folder ``relion-3.1.0`` at
``EM_ROOT`` folder (by default ``SCIPION_HOME/software/em``).

In some cases, the plugins need to know the version of the binary behind and is using this pattern to infer the version
from the folder name (relion-*3.1.0* in this case)

Therefore, the home folder name has a special meaning for some plugins. If you have an existing installation
sowewhere/else, the safest way would be to link it where the plugin expects to find it:

::

    ln -s path/to/my/optimeized/relion3.1 SCIPION_HOME/software/em/relion-3.1.0
 
Editing the configuration file
==============================
In other cases, where the plugin does not use the folder name to infer the version, you can alternatively define it's "HOME" variable in
:ref:`scipion's configuration file <scipion-configuration>`. To know what is the variable name you need to define, you can look for the
one that ends in HOME and starts like your software (RELION_HOME, EMAN2_HOME, ...).

::

    scipion3 config -p <pluginPackage>
    scipion3 printenv | grep HOME
     
might be useful to locate the variable name (notice that ``<pluginPackage>`` must be the package name of the plugin,
check :ref:`the plugin's packages list <Plugins-API>`).
