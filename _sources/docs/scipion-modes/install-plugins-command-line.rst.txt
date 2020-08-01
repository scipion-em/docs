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

    ./scipion3 installp --help

This will also show the instructions to use the installp command line
tool.

Checking plugin updates
-----------------------

::

     scipion3 installp --checkUpdates

Listing plugin binaries
-----------------------

This will show the available binaries for our installed plugins:

::

    scipion3 installb --help

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

    scipion3 installp -p ~/scipion-em-relion --devel

Changes made to the plugin should now be available when you launch
Scipion.

Regular install
~~~~~~~~~~~~~~~

To install one of the plugins from the list run the install
command with the name of the
package. For example, to install Relion using 5 processors:

::

    ./scipion3 installp -p scipion-em-relion -j 5

You may replace ``-j 5`` by the number of cores available in your
machine or remove it altogether if you only wish to use one (will be
slow). You can also install multiple packages with a single install
command:

::

    ./scipion3 installp -p scipion-em-xmipp -j 5 -p scipion-em-relion -j 5 -p scipion-em-cistem

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

    ./scipion installb

This should show something like:

::

    [. . . ]
    Example: scipion3 installb cistem relion-3.1

    Available binaries: ([ ] not installed, [X] seems already installed)
    chimerax                 1.0     [X]
    cistem                   1.0.0-beta[X]
    cryolo                   1.6.1   [X]
    cryolo_model             201910  [ ]     202002_N63[X]
    cryolo_negstain_model    20190226[ ]
    ctffind4                 4.1.13  [ ]
    deepLearningToolkit      0.2     [X]
    dynamo                   1.146   [X]
    eman                     2.3     [ ]     2.31    [X]     3.0.0-alpha[X]
    gautomatch               0.53    [ ]     0.56    [X]
    gctf                     1.06    [ ]     1.18    [X]
    imod                     4.10.42 [X]
    janni_model              20190703[ ]
    maxit                    10.1    [X]
    motioncor2               1.2.3   [ ]     1.2.6   [ ]     1.3.0   [ ]     1.3.1   [X]     1.3.2   [X]
    relion                   3.0     [ ]     3.1.0   [ ]
    resmap                   1.95    [X]
    xmippSrc                 3.20.07b1[ ]

Now we can install our preferred binaries:

::

    scipion3 installb relion-3.1 -j 5
