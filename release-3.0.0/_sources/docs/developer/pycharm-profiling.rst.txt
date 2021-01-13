.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _pycharm-profiling:

========================
Out of the box profiling
========================

Pycharm professional (free for educational email accounts) integrates in its GUI a profiling option that is third way to
execute any code apart Run or Debug. Please go `here <https://www.jetbrains.com/help/pycharm/profiler.html#work-with-profiling-results>`_
for more details.

Profiling a script
------------------
The simplest profiling you can do is to have a specific python script that does something you want to profile.

The following code will use Scipion Manager to list the available projects

.. code-block:: python

    from scipion.__main__ import main

    # Initialize scipion environment
    main(justinit=True)

    from pyworkflow.project import Manager, Project

    # Create a new project
    manager = Manager()

    for i, p in enumerate(manager.listProjects()):
        print(p)


.. note:: Note that main(justinit=True) is needed to initialize Scipion using the config file and have full API functionality.

Run configuration
-----------------

Now you are going to need to have a specific pycharm run configuration. Fill:

1. Script path: point to your performance script .py file
2. Environment variables:  You need to add SCIPION_HOME, and LD_LIBRARY_PATH

Once done you should br able to run, debug or profile your script

.. note:: See `skipping scipion launcher <tutorials/debugging-scipion.html#skipping-the-scipion3-launcher-in-pycharm-configurations>`_  for a more detailed explanation.
