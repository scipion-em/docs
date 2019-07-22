.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _pycharm:

===========
PyCharm IDE
===========

Getting started
---------------

* Download PyCharm's community version `[here] <https://www.jetbrains.com/pycharm/download/#section=linux>`_. Install following the instructions for your platform.
* Clone Scipion git repository in your machine:

.. code-block:: bash

    git clone https://github.com/I2PC/scipion.git`

* Create a new Scipion project (Choose "open" in the open project dialog and select your scipion directory).


Launching pycharm
-----------------

There is a couple of things we need to run before starting PyCharm in
order to be able to debug Scipion, using the embedded python console or
use the "Attach to local process" option.

1 Add scipion lib folder to the LD_LIBRARY_PATH

`export LD_LIBRARY_PATH= <SCIPION_HOME>/software/lib/:$LD_LIBRARY_PATH`

There are libraries there that where used to compile Scipion's python and need to be available

2 Allow pycharm to attach to other processes:

These is achieved by:
 `echo 0 | sudo tee /proc/sys/kernel/yama/ptrace_scope`
See more here https://www.jetbrains.com/help/clion/attaching-to-local-process.html

How to setup this may differ depending on your OS and pycharm version.

An idea could be to create a shell script --> launchPycharm.sh.


.. code-block:: bash

    export LD_LIBRARY_PATH= <SCIPION_HOME>/software/lib/:$LD_LIBRARY_PATH
    echo 0 | sudo tee /proc/sys/kernel/yama/ptrace_scope
    pycharm


pycharm, in this case refers to the command launcher that pycharm, or
Jetbrains toolbox app generates.

make it executable and launch it like `./launchPycharm.sh.`

Another option would be to edit such a file to add those 2 lines, somewhere
inside the launcher script.


Configuring the interpreter for plugins
---------------------------------------
A proper configuration ofs pycharm will make your life easier when it comes to
navigate the code from the plugin to Scipion and viceversa. It will allow
pycharm to understand your setup and make better suggestions for importing
code or even identifying bugs. For it,  we need to add a new interpreter,
since scipion provides it's own python. Go to:

.. pull-quote::
 File > Settings > Project > Project interpreter

click on the cog icon, and then "add" menu

.. figure:: /docs/images/dev-tools/pycharm_project_interpreter_add.png
   :alt: pycharm project interpreter add

This will pop up the "Add Python Interpreter" window, select "System interpreter" and look for the python that is under
<SCIPION_HOME>/software/bin/python2.7

.. figure:: /docs/images/dev-tools/pycharm_add_python.png
   :alt: pycharm adding new python interpreter

This should have registered Scipion's python in your pycharm. Now we need to
customize it. Having it selected, press again in the "cog", but this time press
in "Show all". This should pop up the "Project interpreters" window. Select the
recently added interpreter and click on the "pencil" to rename it to
"pythonForPlugins" (e.g.). This is optional but will make more clear why that
interpreter is there and easier to choose in any new plugin project you might
load in pycharm.

.. figure:: /docs/images/dev-tools/pycharm_interpreter_list.png
   :alt: pycharm adding new python interpreter

Lastly, we need to add 3 "dependencies":

- Add <SCIPION_HOME>, so pyworkflow code is found
- Add xmipp python bindings, usually found at <SCIPION_HOME>/software/em/xmipp/bindings/python
- Add xmipp python bindings dependencies, found at <SCIPION_HOME>/software/em/xmipp/lib

.. figure:: /docs/images/dev-tools/pycharm_interpreter_paths.png
   :alt: pycharm adding paths to python interpreter


Configuring the interpreter just for a Scipion "solo" project
-------------------------------------------------------------
In this case you can follow the same steps as above, but avoid adding "pyworkflow"
as a dependency, since it will be naturally found by pycharm. The xmipp binding
is still needed.

For this case it is also advisable to exclude some folders from being indexed:
data and software.

