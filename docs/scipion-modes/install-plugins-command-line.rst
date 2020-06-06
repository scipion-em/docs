.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _install-plugins-command-line:

========================================
Installing plugins from the command line
========================================

This guide contains examples to show the different options available to
install and uninstall plugins and their binaries.

Listing
=======

Listing plugins
---------------

You can see the up-to-date list of available plugins with this command:

::

    ./scipion installp --help

This will also show the instructions to use the installp command line
tool.

Checking plugin updates
-----------------------

::

     scipion installp --checkUpdates

Listing plugin binaries
-----------------------

This will show the available binaries for our installed plugins:

::

    scipion installb --help

Installing
==========

Installing plugins
------------------

Devel mode
~~~~~~~~~~

Installing a plugin in devel mode is handy to make changes to the plugin
locally and test them in Scipion immediately. Let's use relion as an
example. First, we clone the repo, for example in our home ( ``~`` ):

::

    git clone git@github.com:scipion-em/scipion-em-relion.git

Now we should have the plugin in ``~/scipion-em-relion``. We can install
in devel mode by pointing the path after the ``-p`` flag:

::

    scipion installp -p ~/scipion-em-relion --devel

Changes made to the plugin should now be available when you launch
Scipion.

Regular install
~~~~~~~~~~~~~~~

To install one of the plugins from the list (by default, all plugins are
installed in ``../lib/python3.8/site-packages`` and their binaries
in ``software/em``), run the install command with the name of the
package. For example, to install Relion using 5 processors:

::

    ./scipion installp -p scipion-em-relion -j 5

You may replace ``-j 5`` by the number of cores available in your
machine or remove it altogether if you only wish to use one (will be
slow). You can also install multiple packages with a single install
command:

::

    ./scipion installp -p scipion-em-xmipp -j 5 -p scipion-em-relion -j 5 -p scipion-em-cistem

Installing binaries
-------------------

Install plugin without binaries
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can install a plugin and its binaries in two steps. For this, first
we install the plugin without binaries:

::

    ./scipion installp -p scipion-em-relion -j 5 --noBin

Install specific binaries
~~~~~~~~~~~~~~~~~~~~~~~~~

We list all available binary versions:

::

    ./scipion installb --help

This should show something like:

::

    [. . . ]
    Example: /home/yaiza/git/scipion/scipion installb cistem relion-3.1

    Available binaries: ([ ] not installed, [X] seems already installed)
                 relion       3.0 [ ]      3.1 [X]
               xmippBin   3.20.07 [ ]
               xmippSrc   3.20.07 [ ]

Now we can install our preferred binaries:

::

    scipion installb relion-3.1 -j 5
