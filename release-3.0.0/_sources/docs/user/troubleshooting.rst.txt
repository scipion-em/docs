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

