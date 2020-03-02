.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _installation-system:

===================
Installation Script
===================

This page will explain the Scipion installation system

.. contents:: Table of Contents


Developers
==========

This section contains advance installation topics that can be useful
for developers.

Repository at GitHub
--------------------
For developers, use this ``git clone`` command instead:

.. code-block:: bash

    git clone git@github.com:I2PC/scipion.git

The Scipion repository was moved from SourceForge to
GitHub (May-2015). If you had a ``git clone`` with the previous Sourceforge address, please update the repository with the following command:

.. code-block:: bash

    git remote set-url origin https://github.com/I2PC/scipion.git

Installing python modules
--------------------------

The modules required in a typical production installation are handled
in ``install/script.py``

Some of these modules utility is restricted to specific cases, so you may
need to install them "by hand" after the standard scipion installation. For example,

.. code-block:: bash

    scipion install pip

If you are in development mode and need a quick and dirty installation of
some new python module, you can use scipion pip to install it:

.. code-block:: bash

    scipion run pip install trendy_python_lib


When the module integration into scipion has been approved, it will be
integrated in ``install/script.py`` as others before it.

Modifying installation script
-----------------------------

Scipion installs several external libraries (like Python, ...) and Python
modules from scratch, mainly using the scripts ``install.py`` and ``script.py``. The latter
contains a list of external libraries, versions, and Python modules to be installed
and their dependencies. To add new libraries or change to new versions, check how to
link:Installation-Script[change the installation script].

Generating Binaries
-------------------

We generate a binary version of Scipion that can be moved
as a whole and work in basically any machine without recompiling. For
that purpose, we use the ``--binary`` flag when installing from a fresh
download and compile in an old Linux for libc compatibility. More details
here about link:Generating-Binaries[how to generate binaries].

Installing on Mac
-----------------

The following page contains our notes on the (not yet available)
link:Installing-on-Mac[installation on Macs].

Install howtos for clusters
----------------------------

link:SDSC-Gordon-Howto[SDSC Gordon]

Installation Script Details
===========================

Overview
---------

* ``install.py script``. Responsible for downloading, unpacking, and installing SCons under the software/install folder. It also sends the output to a log file and stdout.
* ``scipion script``. Everything in Scipion is centralized through this script. This is done to ensure that the environment is controlled and to simplify the user's experience by giving him only one file to look in for searching Scipion actions.

Scenarios
---------

Let's think of the typical installation scenarios as exercises:

* **Exercise 1**: You need the Scipion path to have an additional python
  module in its self-compiled Python. How can you add it to Scipion
  python?
* **Exercise 2**: To fix the version of a specific external library,
  you've decided to compile it with Scipion, so a shared library will be
  placed in the software/lib folder, using it whenever you use Scipion. How
  can you do it?
* **Exercise 3**: A new EM Package, called TRFEMP (The Really
  Fantastic EM Package) has appeared, and you don't want to miss the
  opportunity to test it with Scipion and compare the results with the
  other EM Packages in the market. How can you add it?

Solutions
---------

In most cases, it will be enough to take a look at the definitions of
packages currently in use, in the file ``install/script.py``. The script
is organized to reflect the 3 scenarios (library, python module, EM
package)

If you need to add (or modify) low-level features, ``install/funcs.py`` is
your file.

**Solution to exercise 1**

In Exercise 1, the solution would be very simple. Let's say you're trying to
add the python module paramiko. With every library, every module, and
every EM package in Scipion, there is always a parameter called
"default" that determines whether the library, module or package has to
be built by default with Scipion. That means that if the user doesn't
specify anything, the job will be done. In other case, an option called
"--with-name", with 'name' being the name of the library, module, or package,
will be added to the installation parameters, so the user would be able
to use, for example, ./scipion install --with-paramiko. Let's say we
don't need paramiko by default, but certain installations may need to
install it, then default=false.

The *addModule()* function has the following parameters:

* **name**: the name of the module. 'paramiko' in this case. It is
  mandatory.
* **tar**: the compressed file to download with the sources. In case you
  don't provide it, it will assume name.tgz.
* **buildDir**: the name of the decompressed folder. The tarfile must
  contain a folder with the module, and that may not be "name", so if you
  don't provide it, this will remove "tar.gz" or "tgz" from the tarfile
  and assume the name of the folder is that.
* **targets**: SCons builders (or pseudo-builders) need targets to work.
  That is how it builds its dependency tree. A builder generates a list of
  targets which will probably be sources for the next builders in the
  dependency tree. An adequate target would be a file/folder that is
  mandatorily generated by the build process. For example, in a python
  module, a folder is usually generated inside
  lib/pythonX.Y/site-packages/ with the name of the module. That is the
  trick used by addModule() function. When you provide a target, it makes
  the untar process dependent on the download one, and the "setup.py
  install" will depend on the untar result, and on the other hand, will
  generate as a target the folder software/lib/python2.7/site-packages/name
  , with 'name' being the target passed as argument. If no target is passed, then
  'name' will be assumed.
* **url**: the URL used to download the tarfile. If no URL is provided,
  then http://scipionwiki.cnb.csic.es/files/scipion/software/python/name
  will be assumed.
* **flags**: the arguments that may be necessary to pass to the Python
  setup.py install call. In any case, --prefix=software will be assumed, so
  every module will be built in the Scipion architecture.
* **deps**: the other elements on which this module may depend.
  Usually other builders' targets may be passed here. Every python module
  (as it may be obvious) depends on Python itself.
* **default**: the yet-to-be-explained default mechanism. If nothing is passed,
  True is assumed (meaning the module will be built by default).

So taking everything into account, it seems like adding paramiko module,
would only need to write (in SConscript file) the following line.

.. code-block:: bash

    addModule(
        'paramiko',
        tar='paramiko-1.14.0.tgz',
        default=False)

This means that if the user runs ``./scipion install --with-paramiko``,
then a so-called paramiko python module is downloaded from
http://scipionwiki.cnb.csic.es/files/scipion/software/python/paramiko-1.14.0.tgz
URL to the `software/tmp` folder, decompressed as
``software/paramiko/paramiko-1.14.0`` and then
``software/bin/python setup.py install --prefix=software`` will be
executed, installing the module under
software/lib/python2.7/site-packages/paramiko. The resulting log will be
stored at `software/log/paramiko.log`. All those actions will be
committed just by adding that simple line.

But... just a moment... wasn't it AddModule() instead of addModule()?
Yes, don't panic. In this case, we've also supplied a function called
addModule in the SConscript file, just to avoid needing to introduce
``deps=[python]`` (automatically adding python dependency). But please,
note that it is the same as typing the line:

.. code-block:: bash

    AddModule(
        'paramiko',
        tar='paramiko-1.14.0.tgz',
        deps=[python],
        default=False)

**Solution to exercise 2**

Exercise 2 is also simple and is an example of how can we compile a
new external library. In this case, developer will only need to add a
line in SConscript, but this time it will be a call to
**`AddLibrary()`**. Let's say it's the sqlite library. If we see the
    AddLibrary() params...

* **name**: similar to AddModule; this will be 'sqlite'.
* **tar**: same as in AddModule; this time we will use
  'sqlite-3.6.23.tgz'. If we don't say anything, it would look for
  'sqlite.tgz'
* **buildDir**: as in AddModule, it will be generated automatically as
  'sqlite-3.6.23' taking it from tar name without the extension.
* **targets**: in libraries, we will expect the build process to
  generate a shared library. Starting from software folder, the targets
  will be taken here. So in this case we will use 'lib/libsqlite3.so' (we
  know that installation procedure will generate that file).
* **url**: as in AddModule, in this case URL can be also guessed, but
  this time the guessed address will be
  http://scipionwiki.cnb.csic.es/files/scipion/software/external/name
  ('name' being 'sqlite' in our case).
* **flags**: as we want to pass, during ./configure process, the line
  "./configure CPPFLAGS=-w CFLAGS=-DSQLITE_ENABLE_UPDATE_DELETE_LIMIT=1",
  we will set flags like flags=['CPPFLAGS=-w',
  'CFLAGS=-DSQLITE_ENABLE_UPDATE_DELETE_LIMIT=1'].
* **autoConfigTarget**: this is very specific for AutoConfig builder. As
  a result of the ./configure execution, some files will be generated, and
  those files modification will be used to detect whether or not the make
  order must be rebuilt. For that purpose, you can pass a specific
  target. Usually this target is the Makefile itself, so by default, if we
  don't say anything, 'Makefile' will be used.
* **deps**: same behavior as in AddModule, but in this case, no dep is
  asumed by default.
* **default**: if nothing is passed, True is assumed.

We can then write, to solve the exercise, the following line in
SConscript:

.. code-block:: bash

    sqlite = env.AddLibrary(
        'sqlite',
        tar='sqlite-3.6.23.tgz',
        targets=['lib/libsqlite3.so'],
        flags=['CPPFLAGS=-w',
               'CFLAGS=-DSQLITE_ENABLE_UPDATE_DELETE_LIMIT=1'])

That line will cause scons execution to download
http://scipionwiki.cnb.csic.es/files/scipion/software/external/sqlite-3.6.23.tgz
to software/tmp folder, then unpacked to software/tmp/sqlite-3.6.23
folder, then configured with the order "./configure 'CPPFLAGS=-w
CFLAGS=-DSQLITE_ENABLE_UPDATE_DELETE_LIMIT=1'" and finally executed
'make install' on that folder. The resulting log will be stored at
software/log/sqlite_configure.log and software/log/sqlite_make.log

**Solution to exercise 3**

The exercise 3 aims at building a new EM Package called 'TRFEMP'. In
this case we will use the *`AddPackage()`* pseudo-builder. This one has the
arguments described below:

* **name**: As usual, we need a key to name the package. In this case,
  we will use 'TRFEMP'
* **tar**: Same behavior as in the other pseudo-builders. If we don't
  say anything, it will assume the file 'TRFEMP.tgz'.
* **buildDir**: Imagine that TRFEMP packages a folder named trfemp-1.0,
  and inside it, there's a Unix folder, where the configure script is placed.
  Then buildDir will be 'trfemp-1.0/unix'. If we don't pass any parameters,
  TRFEMP would be used.
* **url**: As we placed this file in
  http://scipionwiki.cnb.csic.es/files/scipion/software/em/TRFEMP.tgz
  address, there's no need to explicitly indicate the URL. It will be automatically
  generated.
* **extraActions**: Packages follow a workflow that is a little bit different
  from modules and libraries. They're not supposed to compile as usual
  with ./configure && make && make install, but they're supposed to be a
  little bit complicated. In case the compilation can be driven
  unattended, then there's a way to provided the orders to Scipion
  installer and let it compile. Otherwise, or just because we already have
  the package compiled in our system, there is a way to automatically link
  an already present and compiled package, and this is by using the option
  --with-name=/path/to/package/home (using package name instead of "name"
  and the proper path). In that case there will be a link created in
  software/em/name pointing to that installation. Now imagine that TRFEMP
  can be simply compiled by executing 2 commands. The first one is
  "./configure --funny-option", and among others, that command generates a
  Makefile, which can be executed by using "make --very-funny-option"
  creating a trfemp binary. The extraActions param expects a list of
  tuples. Each tuple is built in the form (target, command), so in this
  case, we would configure extraActions=[('Makefile', './configure
  --funny-option'), ('trfemp', 'make --very-funny-option')].
* **deps**: Deps will behave as usually.
* **default**: Like the rest of the cases.

To include the TRFEMP Package, add to `install/script.py` something
like...

.. code-block:: bash

    env.AddPackage('TRFEMP',
                   buildDir='trfemp-1.0/unix',
                   extraActions=[('Makefile', './configure --funny-option'),
                                         ('trfemp', 'make --very-funny-option')],
                   default=False)

If the TRFEMP package is not installed, executing
``./scipion install TRFEMP`` will proceed with the download, unpacking,
etc.


**Xmipp**

Xmipp is installed by default with a similar philosophy: ``scipion`` uses
``install/script.py`` to call ``install/scons.py``.

``scons.py`` runs SCons using scipion environment (python binary,
variables, etc).

Actual Xmipp installation steps (following SCons conventions) are
defined in `software/em/xmipp/scipion_sconscript`

Most of the configuration of Xmipp compilation is done with environment
variables. For example, if you need to specify CUDA settings, you can
define the variables `CUDA_SDK_PATH`, `CUDA_LIB_PATH` and `CUDA`. As
usual, it is easier to set those variables in the scipion config files.
Again, for CUDA it would mean to edit `scipion.conf`, set `CUDA` to True
(and change the other variables if needed).
