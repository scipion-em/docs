.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _creating-a-plugin:

=================
Creating a plugin
=================

A **Plugin** for Scipion is a Python module that meets some extra requirements.
Each Plugin contains classes for  protocols, viewers, wizards, etc...allowing to use the functionality of a given EM
package within the Scipion framework.

Since release 2.0.0 ("the pluginized version") we worked hard to make the entire system more de-centralized
and more standard. For that we re-factored the plugins to make them standard Python modules so that their
code can be hosted in independent repositories and therefore, updated in different release cycles.

This document is organized in two main parts:

1. Explanation of the structure of a plugin as a Python module and the required submodules and functionality for Scipion.

2. Necessary files structure and the process for distributing a Plugin in the Python de-facto repository PyPI.


.. contents:: Table of Contents

Where to start: scipion-em-template
===================================

This repository contains a `Scipion template <https://github.com/scipion-em/scipion-em-template>`_ plugin with "git
tags" describing the steps taken to build it. It is the perfect starting point for a practical following of the next
sections. Although this whole page is referred to
`Relion's repository <https://github.com/scipion-em/scipion-em-relion>`_, the template has been conceived to offer a
simple practical example that can be easily edited for a better understanding of Scipion Plugin development. Relion is
a real product with the corresponding complexity, so the recommendation is to follow the explanations approached in this
page and observe them in a real product while creating a simple one based on the template to consolidate the knowledge
and make the process more practical.

Thus, the recommendation is to start from the template as a plugin in developer mode, which means that all the changes
made will be observable in Scipion. To do this:

1.- clone the template repository in a desired location:

.. code-block:: bash

    git clone  git@github.com:scipion-em/scipion-em-template.git scipion-em-myplugin

2.- remove .git folder and start a clean repo

.. code-block:: bash

    cd scipion-em-myplugin
    rm -rf .git
    git init

3.- Install the plugin

.. code-block:: bash

    $SCIPION_HOME/scipion3 installp -p [PATH_WHERE_CLONED]/scipion-em-myplugin --devel

Then, open Scipion and create a new project or open an existing one. The template example can be found in the left
panel, with selected Protocols SPA as selected View in section Tools > Greetings. Another quick access to it consists on
pressing ctrl + F and search for the world 'Hello'.


Naming Conventions
==================

Similar to style guides, conventions are about consistency. Consistency is crucial for a project such as
Scipion and its distributed nature. Despite the final decision is up to the developer of a package, we STRONGLY
recommend the following conventions:

* Repository name: **scipion-em-myplugin**
* Python package name: **scipion-em-myplugin**
* Python module with package code: **myplugin**

This means that it will be a folder named **scipion-em-myplugin** with the structure of a standard Python package
(explained below in the second part) and it will contain a folder **myplugin** that is a Python module
with functions and classes required by Scipion (explained below).


Plugin overview
===============

File tree
---------

The file and folder structure follows the convention established for Python modules.
For example, the Relion plugin has the following structure:

.. code-block:: bash

    $ cd ~/work/development/scipion-em-plugins/scipion-em-relion
    $ tree
    .
    ├── CHANGES.txt
    ├── LICENSE
    ├── MANIFEST.in
    ├── README.rst
    ├── relion
    │   ├── bibtex.py
    │   ├── constants.py
    │   ├── convert
    │   │   ├── __init__.py
    │   │   ├── convert30.py
    │   │   ├── ...
    │   ├── __init__.py
    │   ├── objects.py
    │   ├── protocols
    │   │   ├── __init__.py
    │   │   ├── protocol_assign_optic_groups.py
    │   │   ├── protocol_autopick_log.py
    │   │   ├── protocol_autopick.py
    │   │   ├── ...
    │   ├── protocols.conf
    │   ├── relion_logo.png
    │   ├── tests
    │   │   ├── __init__.py
    │   │   ├── test_convert_relion.py
    │   │   ├── test_protocols_relion3.py
    │   │   ├── ...
    │   ├── viewers
    │   │   ├── __init__.py
    │   │   ├── viewer_base.py
    │   │   ├── ...
    │   ├── wizards.py
    └── setup.py


.. _standard-submodules:

Standard submodules
-------------------

Required
~~~~~~~~

Scipion plugins are usually composed by the following submodules:

\__init__.py
^^^^^^^^^^^^

This file is required in Python modules and it is executed when the module is imported. It is explained in detail below
in section Creating __init__.py_.

Protocols
^^^^^^^^^

In this submodule all the protocols of the plugin should be implemented.
Usually a plugin provides many protocols, so the most common case is to have a
submodule folder with its own ``__init__.py`` and one .py file per each protocol class.

Tests
^^^^^

We strongly recommend to follow Test-Driven-Development, so this is the place where all plugin tests should go.
It is important to create different test cases from the beginning of the plugin development.

bibtex.py
^^^^^^^^^

This submodule is not supposed to be imported directly, it should contain the bibtex string
literal as the Python doc string. Scipion will take care of parsing the bibtex reference and
incorporate into the plugin module.

.. code-block:: python

    """
    @article{Scheres2012a,
    title = "A Bayesian View on Cryo-EM Structure Determination ",
    journal = "JMB",
    volume = "415",
    number = "2",
    pages = "406 - 418",
    year = "2012",
    issn = "0022-2836",
    doi = "http://dx.doi.org/10.1016/j.jmb.2011.11.010",
    url = "http://www.sciencedirect.com/science/article/pii/S0022283611012290",
    author = "Scheres, Sjors H.W.",
    keywords = "cryo-electron microscopy, three-dimensional reconstruction, maximum a posteriori estimation "
    }

    @article{Scheres2012b,
    title = "RELION: Implementation of a Bayesian approach to cryo-EM structure determination ",
    journal = "JSB",
    volume = "180",
    number = "3",
    pages = "519 - 530",
    year = "2012",
    issn = "1047-8477",
    doi = "http://dx.doi.org/10.1016/j.jsb.2012.09.006",
    url = "http://www.sciencedirect.com/science/article/pii/S1047847712002481",
    author = "Scheres, Sjors H.W.",
    keywords = "Electron microscopy, Single-particle analysis, Maximum likelihood, Image processing, Software development "
    }
    [. . .]

Optional / If necessary
~~~~~~~~~~~~~~~~~~~~~~~

constants.py
^^^^^^^^^^^^

This submodule should contain all the constants that can be later imported in protocols etc. If there are only few of
them, there is no need for a separate constants.py file.

.. code-block:: python

    from collections import OrderedDict

    import pwem.emlib.metadata as md

    # ----------------- Constants values ----------------------

    RELION_HOME = 'RELION_HOME'
    RELION_CUDA_LIB = 'RELION_CUDA_LIB'

    # Supported versions:
    V3_0 = '3.0'
    V3_1 = '3.1'

    MASK_FILL_ZERO = 0
    MASK_FILL_NOISE = 1

Convert
^^^^^^^

This submodule might contain all functions used for conversion between Scipion objects and metadata files needed
by the programs inside the plugin. In cases when there are only few conversion functions, the
submodule folder can be replaced by a single ``convert.py`` file.

Viewers
^^^^^^^

A plugin can also define viewers for existing objects or new protocols.
Since many built-in viewers are provided by Scipion, plugins do not define many viewers,
so a ``viewers.py`` will serve as submodule.

Wizards
^^^^^^^

Wizards need to be defined for protocols/parameters, but many base classes are already provided.
Here again the ``wizards.py`` submodule is usually enough.

.. _protocols.conf:

protocols.conf
^^^^^^^^^^^^^^

This submodule contains the location of all protocols in the Scipion Protocols Tree View.
This file is optional in Python modules and it is loaded when the module is imported if it exists.
If the file does not exist, the protocols will be loaded in the All view. Scipion will take care of
parsing the file and incorporating its contents into Scipion's Tree View. For example, the Relion ``protocol.conf`` has
the following structure:

.. code-block:: cfg

    [PROTOCOLS]
    Protocols SPA = [
        {"tag": "section", "text": "Imports", "icon": "bookmark.gif", "children": [
        {"tag": "protocol", "value": "ProtImportMovies",      "text": "import movies"},
        {"tag": "protocol", "value": "ProtImportMicrographs", "text": "import micrographs"},
        {"tag": "protocol", "value": "ProtImportParticles",   "text": "import particles"},
        {"tag": "protocol", "value": "ProtImportVolumes",     "text": "import volumes"},
        {"tag": "section", "text": "more", "openItem": "False", "children": [
        {"tag": "protocol", "value": "ProtImportCoordinates",   "text": "import coordinates"},
        {"tag": "protocol", "value": "ProtImportCTF",   "text": "import ctfs"},
        {"tag": "protocol", "value": "ProtImportPdb",   "text": "import atomic structure"},
        {"tag": "protocol", "value": "ProtImportAverages",    "text": "import averages"},
        {"tag": "protocol", "value": "ProtImportMask",        "text": "import masks"}
        ]}
        ]},
        {"tag": "section", "text": "Movies", "openItem": "False", "children": [
        {"tag": "protocol", "value": "ProtRelionMotioncor", "text": "default"}
        ]},
        {"tag": "section", "text": "Micrographs", "children": [
        {"tag": "protocol_group", "text": "CTF estimation", "openItem": "False", "children": [
        {"tag": "section", "text": "more", "openItem": "False", "children": [
        {"tag": "protocol", "value": "ProtRelionExportCtf", "text": "default"}
        ]}
        ]}
        ]},
        {"tag": "section", "text": "Particles", "children": [
        {"tag": "protocol_group", "text": "Picking", "openItem": "False", "children": [
        {"tag": "protocol", "value": "ProtRelion2Autopick", "text": "default"},
      {"tag": "protocol", "value": "ProtRelionAutopickLoG", "text": "default"}
        ]},
        {"tag": "protocol_group", "text": "Extract", "openItem": "False", "children": [
        {"tag": "protocol", "value": "ProtRelionExtractParticles", "text": "default"},
        {"tag": "section", "text": "more", "openItem": "False", "children": [
        {"tag": "protocol", "value": "ProtRelionExportParticles", "text": "default"}
        ]}
        ]},
        {"tag": "protocol_group", "text": "Preprocess", "openItem": "False", "children": [
        {"tag": "protocol", "value": "ProtRelionPreprocessParticles", "text": "default"}
        ]},
        {"tag": "protocol_group", "text": "Filter", "openItem": "False", "children": []},
        {"tag": "protocol_group", "text": "Mask", "openItem": "False", "children": []}
        ]},
        {"tag": "section", "text": "2D", "children": [
        {"tag": "protocol_group", "text": "Align", "openItem": "False", "children": [
        {"tag": "protocol", "value": "ProtRelionCenterAverages", "text": "default"},
        {"tag": "section", "text": "more", "openItem": "False", "children": []}
        ]},
        {"tag": "protocol_group", "text": "Classify", "openItem": "False", "children": [
        {"tag": "protocol", "value": "ProtRelionClassify2D", "text": "default"},
        {"tag": "section", "text": "more", "openItem": "False", "children": []}
        ]}
        ]},
        {"tag": "section", "text": "3D", "children": [
        {"tag": "protocol_group", "text": "Initial volume", "openItem": "False", "children": [
        {"tag": "protocol", "value": "ProtRelionInitialModel", "text": "default"},
        {"tag": "section", "text": "more", "openItem": "False", "children": []}
        ]},
        {"tag": "protocol_group", "text": "Preprocess", "openItem": "False", "children": [
        {"tag": "protocol", "value": "ProtRelionCreateMask3D", "text": "default"},
        {"tag": "section", "text": "more", "openItem": "False", "children": []}
        ]},
        {"tag": "protocol_group", "text": "Classify", "openItem": "False", "children": [
        {"tag": "protocol", "value": "ProtRelionClassify3D", "text": "default"}
        ]},
        {"tag": "protocol_group", "text": "Refine", "openItem": "False", "children": [
        {"tag": "protocol", "value": "ProtRelionRefine3D", "text": "default"},
      {"tag": "protocol", "value": "ProtRelionCtfRefinement", "text": "default"},
      {"tag": "protocol", "value": "ProtRelionBayesianPolishing", "text": "default"},
      {"tag": "protocol", "value": "ProtRelionMultiBody", "text": "default"},
        {"tag": "section", "text": "more", "openItem": "False", "children": []}
        ]},
        {"tag": "protocol_group", "text": "Postprocess", "openItem": "False", "children": [
        {"tag": "protocol", "value": "ProtRelionPostprocess", "text": "default"}
        ]},
        {"tag": "protocol_group", "text": "Analysis", "openItem": "False", "children": [
        {"tag": "section", "text": "Heterogeneity", "openItem": "False", "children": []},
        {"tag": "section", "text": "Validation", "openItem": "False", "children": []},
        {"tag": "section", "text": "Resolution", "openItem": "False", "children": [
        {"tag": "protocol", "value": "ProtRelionLocalRes", "text": "default"}
        ]},
        {"tag": "section", "text": "more", "openItem": "False", "children": [
        {"tag": "protocol", "value": "ProtRelionExpandSymmetry", "text": "default"},
      {"tag": "protocol", "value": "ProtRelionSubtract", "text": "default"},
      {"tag": "protocol", "value": "ProtRelionSymmetrizeVolume", "text": "default"}
        ]}
        ]},
        {"tag": "protocol_group", "text": "Reconstruct", "openItem": "False", "children": [
        {"tag": "protocol", "value": "ProtRelionReconstruct", "text": "default"}
        ]}
        ]},
        {"tag": "section", "text": "Tools", "openItem": "False", "children": [
        {"tag": "protocol_group", "text": "Sets", "openItem": "False", "children": [
        {"tag": "protocol", "value": "ProtSubSet",   "text": "default"},
        {"tag": "protocol", "value": "ProtUnionSet", "text": "default"},
        {"tag": "protocol", "value": "ProtSplitSet", "text": "default"}
        ]}
        ]},
        {"tag": "section", "text": "Exports", "openItem": "False", "children": [
        {"tag": "protocol", "value": "ProtRelionExportCtf", "text": "default"},
      {"tag": "protocol", "value": "ProtRelionExportParticles", "text": "default"},
        {"tag": "protocol", "value": "ProtExportDataBases", "text": "export to DB"}]
        }]


logo.png
^^^^^^^^

PNG image that will be be shown in the GUIs of the plugin protocols within Scipion framework.

.gitignore file
---------------

This file is required for Git. Here is an example:

.. code-block:: none

    #### Eclipse and so on
    .project
    .cproject
    .pydevproject
    .classpath
    .idea

    #### Python
    build/
    dist/
    *.egg-info/
    *.egg
    *.py[cod]
    __pycache__/
    *.so
    *~

PyPI-related files
------------------

These files are required for PyPI distribution. More information about this can be found on the
`pip packaging guide <https://packaging.python.org/tutorials/packaging-projects/#setup-cfg>`_ .

* **LICENSE**: license file for plugin code
* **CHANGES.txt**: version history
* **README.rst**: long description of your plugin (for PyPI catalog)
* **MANIFEST.in**: includes links to ``README`` and ``LICENSE`` files
* **setup.py**: this is a build script for PyPI distribution, containing important information about your plugin.

Read the :ref:`Publishing the plugin to PyPI <publishing-to-pypi>` section below for more details on these files.

.. _Creating __init__.py:

Creating __init__.py
====================

It is common to add here imports
related with Scipion's pyworkflow, and to import values from the ``constants.py`` file. We also define the logo and
plugin-level references:

.. code-block:: python

    import os
    import pyworkflow.utils as pwutils
    import pwem

    from .constants import *

    _logo = "relion_logo.png"
    _references = ['Scheres2012a', 'Scheres2012b', 'Kimanius2016', 'Zivanov2018']


Define the Plugin class
-----------------------

Additionally, it is necessary to add a Plugin class (subclass from :class:`pwem.Plugin`), which contains much of the
logic related with the plugin's variables, environment, associated binaries and paths.

.. code-block:: python

    class Plugin(pwem.Plugin):
        _homeVar = RELION_HOME
        _supportedVersions = [V3_0, V3_1]


_homeVar
~~~~~~~~
In the case of scipion-em-relion, the plugin is associated to some binaries. In ``_homeVar``, we point to the variable that
has the path to the binaries. It is a good practice to define this in ``constants.py``, as it is done here.
As we will see later, this has a default value, but it can also be overwritten by the user.

_supportedVersions
~~~~~~~~~~~~~~~~~~

Here we store which versions of the binaries are supported by this plugin.

_defineVariables
~~~~~~~~~~~~~~~~

Here is where we give the Plugin's environment variables a default value. In the case of Relion, we only have the
``RELION_HOME``, which points to the binaries of the plugin and by default would be ``relion-3.1``

.. code-block:: python

    @classmethod
    def _defineVariables(cls):
        cls._defineEmVar(RELION_HOME, 'relion-3.1')

There are two functions defined in the :doc:`plugin class </api/pwem.Plugin>` that may be useful here:
``_defineEmVar`` and ``_defineVar``. The first one will add the path to ``software/em`` to the variable
(which is the default place to install binaries). The second will store the value as is.
We only need ``defineEmVar`` in Relion, since the binary location is the only variable we'll declare.

getEnviron
~~~~~~~~~~
We can also overwrite the function ``getEnviron`` if there are any modifications we need to do in the environment
variables in order to run the plugin.

.. code-block:: python

    @classmethod
    def getEnviron(cls):
        """ Setup the environment variables needed to launch Relion. """
        environ = pwutils.Environ(os.environ)
        binPath = os.pathsep.join([cls.getHome('bin'),
                                   pwem.Config.MPI_BINDIR])
        libPath = os.pathsep.join([cls.getHome('lib'),
                                   cls.getHome('lib64'),
                                   pwem.Config.MPI_LIBDIR,
                                   ])

        if binPath not in environ['PATH']:
            environ.update({'PATH': binPath,
                            'LD_LIBRARY_PATH': libPath,
                            }, position=pwutils.Environ.BEGIN)

        # Take Scipion CUDA library path
        cudaLib = environ.get(RELION_CUDA_LIB, pwem.Config.CUDA_LIB)
        environ.addLibrary(cudaLib)

        if 'RELION_MPI_LIB' in os.environ:
            environ.addLibrary(os.environ['RELION_MPI_LIB'])

        if 'RELION_MPI_BIN' in os.environ:
            environ.set('PATH', os.environ['RELION_MPI_BIN'],
                        position=pwutils.Environ.BEGIN)
        return environ

Implement validateInstallation() (Optional)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In the plugin class, we can overwrite the validateInstallation function. In the case of Relion this is not overwritten,
so this plugin will use Scipion's default validate installation. You can check the current implementation in
``scipion-pyworkflow/pyworkflow/plugin.py``.

Defining the plugin binaries (Optional)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The next step is to add the code responsible for the installation of the binaries.
We redefine ``defineBinaries`` in our ``RelionPlugin`` class in the **`__init__.py`**.
Please note how we have added ``default=True`` to the latest relion binaries. - this means that
this binary will be installed automatically when we get this plugin (unless specified otherwise).

.. code-block:: python

    # this goes inside class RelionPlugin(Plugin):
    @classmethod
    def defineBinaries(cls, env):
        # Define FFTW3 path variables
        relion_vars = {'FFTW_LIB': env.getLibFolder(),
                       'FFTW_INCLUDE': env.getIncludeFolder()}

        relion_commands = [('cmake -DGUI=OFF -DCMAKE_INSTALL_PREFIX=./ .', []),
                           ('make -j %d' % env.getProcessors(),
                            ['bin/relion_refine'])]

        env.addPackage('relion', version='3.0',
                       url='https://github.com/3dem/relion/archive/3.0.tar.gz',
                       commands=relion_commands,
                       updateCuda=True,
                       vars=relion_vars)

        env.addPackage('relion', version='3.1',
                       tar='relion-3.1.tgz',
                       commands=relion_commands,
                       updateCuda=True,
                       vars=relion_vars,
                       default=True)


You can find more information about how to add a packages or a module `[here] <scipion-installation-system>`_.

Creating the protocols
======================

You can read more detailed information on the :doc:`implementation of protocol <creating-a-protocol>`.

.. _publishing-to-pypi:

Publishing the Plugin to PyPI
=============================

We'll explain below the steps followed to convert the package into a pip module that we can
upload to pypi. Most of these steps are not scipion-specific, so it is recommended to check an external source if you
have doubts about pip packaging (like https://python-packaging.readthedocs.io/en/latest/index.html or
https://packaging.python.org/tutorials/distributing-packages ).

Add PyPI files
--------------

First we'll add four files to the folder ``scipion-em-relion``: ``CHANGES.txt``, ``setup.py``, ``MANIFEST.in``,
``README.rst``.

setup.py
~~~~~~~~

This is the most important one. It needs to call the setup function with, at least, the required arguments.
Here we present a synthesized version:

.. code-block:: python

    from setuptools import setup, find_packages
    from codecs import open
    from os import path

    here = path.abspath(path.dirname(__file__))

    # Get the long description from the README file
    with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()

    setup(
        name='scipion-em-relion',  # Required
        version='3.0.0',  # Required
        description='A python wrapper to use relion within Scipion',  # Required
        long_description=long_description,  # Optional
        url='https://github.com/scipion-em/scipion-em-relion',  # Optional, but very important
        author='Relion authors',  # Optional
        author_email='some@human.com',  # Optional
        keywords='scipion cryoem imageprocessing scipion-3.0',  # Optional
        packages=find_packages(),
        install_requires=['scipion-em'],
        package_data={  #!!!!!! Required if we have a logo!!!!!
           'relion': ['logo.png'],
        }
        entry_points={  # Required for plugin discovery
        'pyworkflow.plugin': 'relion = relion'
        },
    )

Pay special attention to entry_points, that is the mechanism to tell scipion that this is a scipion plugin.

CHANGES.txt (optional)
~~~~~~~~~~~~~~~~~~~~~~

This file records a short description of the modifications made with each release of the pip package.
.. code-block::

    v1.0.0, 23/04/2018 -- First commit

MANIFEST.in (optional)
~~~~~~~~~~~~~~~~~~~~~~

The ``MANIFEST.in`` is needed so that our ``.txt`` file is included when we do the distribution
(or many other non ``*.py`` extensions, please check these
`docs on non-code-files <https://python-packaging.readthedocs.io/en/latest/non-code-files.html>`_
if you need to include such files).

**IMPORTANT**: if you have non-python files like images (except the logo), docs, scripts, you have to specify them here,
otherwise they will be excluded from PyPi distribution! An example below recursively includes all files in
spider/scripts folder.

.. code-block:: none

    include *.txt
    recursive-include spider/scripts *

Also, you will need to add/uncomment the following line into ``setup.py``:
``include_package_data=True``

Installing via pip locally
--------------------------

Remove previous installation from Scipion
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove binaries - if it applies. If you didn't have a prior binary installation (i.e. you're building this plugin new
from scratch), go to next step.

.. code-block:: bash

    rm -rf $SCIPION_HOME/software/em/relion*


.. _devel-mode:

Working in devel mode
~~~~~~~~~~~~~~~~~~~~~

If you want to use the sources of a plugin in a "live" way (meaning that changes in the plugin code will be reflected),
you can use the ``PYTHONPATH`` as described above. Additionally, if you want to test the whole plugin as a pip package
(not only a python module) you can alternatively follow these two steps:

1. git clone the plugin repository to any local folder, in case of a third party plugin

.. code-block:: bash

    git clone git@github.com:scipion-em/scipion-em-myplugin.git /home/me/myplugin


2. Install it in "devel" mode:

.. code-block:: bash

    $SCIPION_HOME/scipion3 installp -p /home/me/myplugin --devel


Testing the Plugin
~~~~~~~~~~~~~~~~~~
Once you think your :ref:`standard submodules <standard-submodules>` have some basic functionality, and the plugin ins installed
you're ready to test how your code behaves within Scipion. It has to have a pip package structure.

Once installed you are ready to troubleshoot your plugin structure with:

.. code-block:: bash

    scipion3 inspect relion

* List your tests and copy the one you want to run:

.. code-block:: bash

    scipion3 test --grep relion


Get plugins.json
~~~~~~~~~~~~~~~~

Scipion requests a json list of available plugins from http://scipion.i2pc.es/getplugins and uses metadata from
pypi to filter which packages are available for the current Scipion version. Since we want to test our pip
plugin before we upload it to pypi, we will read locally a file like the one provided in the website,
with our plugin added.

Download json file
^^^^^^^^^^^^^^^^^^

In a directory of your choice, add a ``plugins.json`` file with the appropriate info for your plugin - you can save
`Scipion's plugins.json <http://scipion.i2pc.es/getplugins>`_ and add your plugin's data.

.. code-block:: json

    {
        "scipion-em-relion": {
            "name":"relion",
            "pipName": "scipion-em-relion",
            "pluginSourceUrl":"/path/to/your/scipion-em-relion"
        }
    }

Note that when you add the key ``pluginSourceUrl``, Scipion will use pip to install the plugin from that directory
(i.e. pip will copy the ``relion`` folder to python's ``site-packages`` folder). If this key is missing, Scipion will
try to install from https://pypi.org/. Once you do this installation, changes made in your development folder
will **NOT** be present in the copy used by Scipion. You would have to uninstall and go back to development mode
using the variable ``PYTHONPATH`` or installing with the ``--devel`` flag as stated in the
:ref:`working in devel mode section <devel-mode>`.

Add SCIPION_PLUGIN_JSON variable
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the ``VARIABLES`` section of your ``~/.config/scipion/scipion.conf``, add variable ``SCIPION_PLUGIN_JSON``. If
you don't add this variable, Scipion will read the json from http://scipion.i2pc.es/getplugins instead of reading
your local json copy. If you use PyCharm to run Scipion, you can also add it as environment variable in your run
configuration. Remember to replace the example provided with the right path:

.. code-block:: ini

    [VARIABLES]
    SCIPION_NOTES_PROGRAM =
    SCIPION_NOTES_ARGS =
    SCIPION_NOTES_FILE = notes.txt
    SCIPION_NOTIFY = False
    SCIPION_PLUGIN_JSON=/home/desktop/yaiza/plugins.

Installation script
~~~~~~~~~~~~~~~~~~~

Scipion has a script to handle plugin installation / uninstallation. We have a few (un)installation
choices:

* Installing plugin and default binaries:

.. code-block:: bash

    $SCIPION_HOME/scipion3 installp -p scipion-em-relion

This command does two things:
1. Gets the package from pypi
2. Installs the default binaries (those that had ``default=True`` in the ``registerPluginBinaries`` function).

If no errors happen, we get an output similar to this one:

.. code-block:: bash

    scipion3 installp -p scipion-em-relion

    Scipion v3.0 () devel

    Building scipion-em-relion ...
    /home/azazello/.conda/envs/.scipion3env/bin/python -m pip install scipion-em-relion==3.0.0
    Collecting scipion-em-relion==3.0.0
    Downloading scipion-em-relion-3.0.0.tar.gz (21 kB)
    Requirement already satisfied: scipion-em in ./scipion-em (from scipion-em-relion==3.0.0) (1.0.2)
    ...
    Successfully built scipion-em-relion
    Installing collected packages: scipion-em-relion
    Successfully installed scipion-em-relion-3.0.0
    Done (1.94 seconds)
    Building relion-3.1
    ...
    Done (132.00 seconds)


* Uninstalling plugin and all binaries installed

.. code-block:: bash

    $SCIPION_HOME/scipion3 uninstallp -p scipion-em-relion

* We can use the flag --noBin to both install and uninstall without binaries:

.. code-block:: bash

    $SCIPION_HOME/scipion3 installp -p scipion-em-relion --noBin

* Install specific plugin binaries (only works if we have done ``installp`` first).

.. code-block:: bash

    $SCIPION_HOME/scipion3 installb relion-3.1

* Uninstall specific plugin binaries

.. code-block:: bash

    $SCIPION_HOME/scipion3 uninstallb relion-3.0

Running your tests
------------------

* With your plugin and binaries installed, it is recommended to run some of your plugin's tests to check
  everything is in order:

  .. code-block:: bash

    scipion3 test relion.tests.test_***


* Open the test project:

.. code-block:: bash

    scipion3 last

First, inspect the protocol output to make sure there's nothing weird; then, open the
protocol box to see if our logo and references are there. It's important to do this step because
if we don't open the GUI we won't be able to detect logo related issues.

Add your own DataSet (if necessary)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you need an additional dataset you can do this and host it where ever you want/can.
Let's assume you need a new dataset...

* usually you work first locally until you are happy with your data set.
* Decide where to host it and upload it. For that scipion3 will:
* Generate a ``MANIFEST`` file
* rsync it to your server, you will need to provide a login info (like user@server.com, and a remote folder location.
* type something like:

.. code-block:: bash

    scipion3 testdata --upload myplugin123_testdata -l user@server.com -rf /path/at/the/server/for/your/datasets


Please note that the dataset name must be unique, so better prefix it with the plugin name. ``-l`` is the login for your
server and ``-rf`` is the remote folder where to rsync your files.

 * Refer to it in your tests, at you tests ``folder/__init__.py``:

.. code-block:: python

  DataSet(name='myplugin123_testdata',
          folder='myplugin123_testdata',
          files={
                 'file1': 'file1.txt'
                 ...},
          url='http://wwww.server.com/datasets')

NOTE: url parameter should be a valid url where your dataset is being published.
TIP: I haven't tried, but doing the upload yourself, to generate the MANIFEST and then adding your datasets + MANIFEST
to github might also work if you later point to the gitraw url?? (disclaimer...has not been tested.)

Create and upload distribution
------------------------------

To upload your distribution to pypi, you'll need to `create an account
<https://packaging.python.org/tutorials/distributing-packages/#create-an-account>`_.

* Install twine if you don't have it (latest stable compatible with Python 3.8 is version 3.1.1)

.. code-block:: bash

    pip install twine==3.1.1


* Create the source distribution (at least! You can also create a Built distribution. Read more in the official
  `packaging guide <https://packaging.python.org/tutorials/packaging-projects/#generating-distribution-archives>`_)

.. code-block:: bash

    cd $PLUGIN_HOME
    rm -rf dist/*    # To clean the already uploaded modules
    scipion3 python setup.py sdist

It is convenient to check your ``*egg-info/SOURCES.TXT`` and see if you miss any file (pay special attention to
non-python files that you might have forgot to include in ``MANIFEST.in`` or in your ``setup.py``, like the logo).

* Upload the distribution **WITH EARLIEST COMPATIBLE SCIPION VERSION IN THE COMMENTS**.

.. code-block:: bash

    cd $PLUGIN_HOME && twine upload dist/* -c "scipion-3.0"

This means that this release we're uploading will be available for Scipion version 3.0 or higher.
The scipion version must follow the pattern used above (scipion-X.Y(.Z))
Now our plugin is on `PyPI <https://pypi.org/project/scipion-em-relion>`_.

Install from pip
----------------

* Uninstall plugin:

.. code-block:: bash

    $SCIPION_HOME/scipion3 uninstallp -p scipion-em-relion

* Remove ``SCIPION_PLUGIN_JSON`` from ``~/.config/scipion/scipion.conf``  IF YOUR PLUGIN IS IN ALREADY IN
  http://scipion.i2pc.es/getplugins. IF NOT DON'T DO THIS. Just remove ``pluginSourceUrl`` from your plugin's dict.

* Install

.. code-block:: bash

    $SCIPION_HOME/scipion3 installp -p scipion-em-relion

* Test again (yes, again)

  .. code-block:: bash

      scipion3 test relion.tests.test_***
