.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _pycharm:

===========
PyCharm IDE
===========

Getting started
---------------

`Download and install PyCharm <https://www.jetbrains.com/es-es/pycharm/download/#section=linux>`_

Setting Up PyCharm
------------------
It is assumed that Scipion3 has been previously installed.

1. Open PyCharm and create a project
2. Open projects scipion-app, scipion-em and scipion-pyworkflow (use "Attach to project" option).
3. Configure project interpreter, which will be the python of your Scipion3 environment. Go to:

   .. pull-quote::

    File > Settings > Project: [PROJECT_NAME] > Project Interpreter.

   Then, click on the gear icon an select Show All:

   .. figure:: /docs/images/dev-tools/pycharm_set_interpreter.png
      :alt: pycharm set conda python interpreter I

   After that, click on the '+' icon to add a new interpreter:

   .. figure:: /docs/images/dev-tools/pycharm_set_interpreter_2.png
      :alt: pycharm set conda python interpreter II

   Once there select your Environment type (Conda or Virtual Environment) and choose Existing Environment and the corresponding options (Interpreter, Conda Location if Conda).

   * Conda:

   .. figure:: /docs/images/dev-tools/pycharm_set_interpreter_conda.png
      :alt: pycharm set conda python interpreter

   * Virtual environment:

   .. figure:: /docs/images/dev-tools/pycharm_set_interpreter_venv.png
      :alt: pycharm set virtual environment python interpreter

   Note: if the project does not recognize some of the dependencies (for example if they appear underlined in red in the import section at the beginning of a .py file), add the dependency paths manually. To do that, got to File > Settings > Project [PROJECT_NAME], click on the gear icon and select Show All:

   .. figure:: /docs/images/dev-tools/pycharm_interpreter_addPaths_I.png
      :alt: pycharm python interpreter add paths I

   Then, select the interpreter configured at the beginning of the session and click on the directories hierarchy icon (which can be below or at the top right of the window, depending on the PyCharm version).

   .. figure:: /docs/images/dev-tools/pycharm_interpreter_addPaths_II.png
      :alt: pycharm python interpreter add paths II

   Finally, click on ‘+’ icon and add the corresponding paths for scipion-em, scipion-pyworkflow and scipion app.

   .. figure:: /docs/images/dev-tools/pycharm_interpreter_addPaths_III.png
      :alt: pycharm python interpreter add paths III

4. Choose keymap & check keyboard shortcuts: to do this, just go to:

   .. pull-quote::

    File > Settings > Keymap

   Then, select Eclipse (this is the one we use, but you can choose the one which best suits for you. Nevertheless, key shortcuts mentioned from now on will be referred to Eclipse keymap) from the list. If isn't present, click right below the list in 'Get more keymaps in Settings | Plugins', search for Eclipse and install it. After that, Eclipse keymap should appear on the list:

   .. figure:: /docs/images/dev-tools/pycharm_set_keymap.png
      :alt: pycharm set keymap

   Some useful keyboard shortcuts are:
        1. F3: go to definition.
        2. Alt + left arrow: go to previous cursor position.
        3. Alt + right arrow: got to next cursor position.
        4. Ctrl + F: find in file.
        5. Ctrl + H: find in project/location.
        6. Ctrl + O: show file structure.

5. PyCharm configurations: they can be used to easily executed commands in one click. To create a new configuration, click on Add Configuration > '+' icon > python:

   .. figure:: /docs/images/dev-tools/pycharm_create_configuration.png
      :alt: pycharm create configuration

   As an example, the image below shows a pycharm configuration to launch Scipion3:

   .. figure:: /docs/images/dev-tools/pycharm_scipion_config.png
      :alt: pycharm launch Scipion3 configuration example

   It can be observed that very complex executions can be easily carried out with multiple options such as environment variables.

Attaching to Scipion3 processes in PyCharm
------------------------------------------
Scipion launcher is a small python script that will launch a new process at the end. So, the code that you
may want to debug falls probably in the second process (if you are interested on the GUI processes or tests) or even
further in the "third" if you are interested in the protocol steps execution.
To be able to debug reach those processes in PyCharm IDE, you must allow this in your system and then use Pycharm's "Attach to process..." menu. This
can be done temporally, in UBUNTU, typing:

    .. code-block::

       echo 0 | sudo tee /proc/sys/kernel/yama/ptrace_scope

For a permanent modification go `here <https://www.jetbrains.com/help/clion/attaching-to-local-process.html>`_.

See `Debugging Scipion with PyCharm <debugging-scipion>`_ tutorial about debugging Scipion3 processes.
