.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _pycharm:

===========
PyCharm IDE
===========

Getting started
===============

* Download PyCharm's community version `[here] <https://www.jetbrains.com/pycharm/download/#section=linux>`_. Install following the instructions for your platform.
* Clone Scipion git repository in your machine:

.. code-block:: bash

    git clone https://github.com/I2PC/scipion.git`

* Create a new Scipion project (Choose "open" in the open project dialog and select your scipion directory).

Debugging
=========

There is a couple of commands that we need to run before starting PyCharm in
order to be able to debug Scipion and use the "Attach to local process" option.
A handy way is to generate PyCharm's command line launcher and modify it:

1a. Edit .bashrc file and include `LD_LIBRARY_PATH= <our-scipion-home>/software/lib/`

1b. Generate Pycharm's command line launcher

Click on `Tools > Create command line launcher...` and type the desired path to the script.

1c. Find PyCharm's command line launcher if already have one
.. code-block:: bash
    $ which charm
    /usr/local/bin/charm

2. Open the init script as root

.. code-block:: bash
    $ sudo vim /usr/local/bin/charm

3. In the function ``` def process_args(argv):```, add the code in **bold**. Remember to replace ```<your-scipion-home>``` with the right path and save your changes:



.. code-block:: bash

    <pre>
    ...
    elif arg == 'merge' and i == 0:
        args.append(arg)
    <b>elif arg == 'debug':
        os.system("export LD_LIBRARY_PATH=&lt;your-scipion-home&gt;/software/lib/")
        os.system("echo 0 | sudo tee /proc/sys/kernel/yama/ptrace_scope")</b>
    elif arg == '-l' or arg == '--line':

    ...
    </pre>

4. Start pycharm from your terminal with your new debug option - will prompt you to enter your password.

.. code-block:: bash

    $ charm debug
    [sudo] password for <your-user>:

5. Happy debugging!