.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _understanding-plugin-class:

==============================
Understanding the Plugin class
==============================

.. contents:: Table of contents
    :depth: 3

Associated resources
====================
Here you can find resources associated with this content, like videos or presentations used in courses:

`Course presentation <https://docs.google.com/presentation/d/1coUcXLkDZrNAWtRbcDO-JsPCxsOSrHh8gjMngoLK7WE/edit?usp=sharing>`_

`Detailed documentation <https://scipion-em.github.io/docs/docs/developer/creating-a-plugin#creating-init-py>`_

Starting with scipion-em-template
=================================

Let's go to our template plugin folder and setup everything ready for the practice session:

.. code-block:: bash

   cd scipion-em-template
   git checkout course5_exBase

You might notice a new file `protocol_run_myprogram.py`. Have a look inside.
You will see that this simple protocol only has one step function **runStep** that executes a program via **runJob**.
If you are using PyCharm you will see that **Plugin.getProgram()** function is undefined.

.. figure:: /docs/images/dev/template_practice/practice5_undefined_func.png
   :alt: getProgram is undefined

Open Scipion and create a new project. Open it and search for **my program** protocol (use *Ctrl\+F* to search for the protocols).
As it does not have any input variables, just execute it. It should fail with the following error message:

.. figure:: /docs/images/dev/template_practice/practice5_failed_protocol.png
   :alt: Failed protocol message

Let's start working on the Plugin class from scratch.

Exercise 1 (easy)
-----------------

First, create **myplugin/constants.py** file and define the following constants:

.. code-block:: bash

    MYPROGRAM_HOME = 'MYPROGRAM_HOME'
    MYPROGRAM = 'MYPROGRAM'
    V1_0 = '1.0'

Pay attention that for the first two vars we defined the "name" of the constant (as a string) and not it's value.
Usually it's a good idea if you want to re-use the constant names throughout the plugin code.

Now switch to **__init__.py** file and start populating the Plugin class with homeVar, pathVars, list of supported versions and url (you can put any web address you like).
Don't forget that you need to import constants from the **constants.py** file!
Then add **_defineVariables** class method and define **MYPROGRAM_HOME** as **myprogram-1.0** and **MYPROGRAM** as **example_script.sh**.
Make sure **MYPROGRAM_HOME** points to the path inside software/em folder (where usually all packages are installed).

----

Exercise 2 (easy)
-----------------

We still need to define plugin binaries (and actually create them), so:

.. code-block:: bash

    cd scipion3/software/em
    mkdir myprogram-1.0
    cd myprogram-1.0
    touch example_script.sh
    chmod a+x example_script.sh

.. tip:: It's good to follow the *name-version* (myprogram-1.0) convention when defining the software folder names. This way Scipion can easily detect the version number.

Open **example_script.sh** in any editor and paste the following code:

.. code-block:: bash

    #!/bin/bash
    echo "Starting myprogram..."
    sleep 5
    echo "This script has finished running!"

Save the script. As you can see it will simply print some text after waiting for 5 seconds.
Add **defineBinaries** class method to the Plugin class.
You can provide any value for tar argument (e.g. **tar='myprogram_v1.0.tgz'**) as we have already "installed" the binaries.

Now, remember that we are still missing **getProgram** function for our protocol?
Create it inside the Plugin class and make it return the full path to **MYPROGRAM** (*Hint: you will need to use cls.getHome()*)

----

Exercise 3 (easy)
-----------------

Now let's test the plugin binaries.

.. code-block:: bash

    cd scipion3
    ./scipion3 installb -h

If you see something like

.. code-block:: bash

    myprogram                1.0     [X]

congratulations! You've got the binaries properly defined and installed.
Reopen your Scipion project and restart our protocol.
Once it is finished, check the output log. You should see something similar to:

.. figure:: /docs/images/dev/template_practice/practice5_ex3_finished.png
   :alt: Run finished

Now, imagine a user who wants to use a different binary version.
At the moment we have the default version defined in **_defineVariables** as **1.0**.
For simplicity, let's close the Scipion project and rename our package folder:

.. code-block:: bash

    cd scipion3/software/em
    mv myprogram-1.0 myprogram-1.1

Reopen the project (run `scipion last`) and try to restart the finished protocol. You should see an error message that is raised by **validateInstallation** function from *pyworkflow/plugin.py*:

.. figure:: /docs/images/dev/template_practice/practice5_ex3_missing_var.png
   :alt: Installation validation has failed

This means that the user have to redefine **MYPROGRAM_HOME** to point to version 1.1.
So, redefine it in your **scipion3/config/scipion.conf** file (if you do not have it, execute `./scipion3 config` first to generate the file) and then re-run the protocol:

.. code-block:: bash

    MYPROGRAM_HOME = software/em/myprogram-1.1

.. tip:: You can also define such variables in your shell environment if you like. The priority goes as following: environment > config > default value.

----

Exercise 4 (intermediate)
-------------------------

You might have noticed that right now we are using the full path to the binary (**example_script.sh**) in **getProgram** function.
Another possibility would be to use **getEnviron** function to add the package folder to the *PATH*.
Have a look at the presentation slides and find an example of this function. You can also look at the **Environ** class inside *pyworkflow/utils.py*.
Can you now define **getEnviron** function inside the Plugin class so that the myprogram-1.1 path is added to the beginning of the PATH var?

.. tip:: You would need to use **update** function of the **Environ** class and **position=BEGIN**.

If you have given up, checkout the resulting code in the following branch (exercises 1-4 completed):

.. code-block:: bash

    cd scipion-em-template
    git checkout course5_ex1-4

Once the PATH contains the path to our myprogram-1.1, we don't need anymore to define the full path in the **getProgram** function.
Change the function and re-run the protocol. In the output log you should see now only the binary name instead of the full path to the executable.
This was a very simple case, but in principle **getEnviron** function can be used to modify things like *LD_LIBRARY_PATH* or define specific CUDA libraries / MPI versions etc.

.. figure:: /docs/images/dev/template_practice/practice5_ex4_using_env.png
   :alt: The binary is now in the PATH

The **getEnviron** function gets automatically recognised by *pyworklow/protocol.py* when executing the plugin protocols,
however you can also explicitly define the environment inside **runJob** function:

.. code-block:: bash

    self.runJob(program, params, env=Plugin.getEnviron())

Exercise 5 (hard)
-----------------

Let's explore conda-based installation. A lot of new cryo-em software comes with its own conda environment so this seems like an appropriate use case.

First, you need to make sure that you have conda installed (we recommend *miniconda3*). If you have used conda for Scipion installation then there should be no problem.
You also need to know how to activate it, this depends on the system and the SHELL you are using. Below is an example for bash:

.. code-block:: bash

    . /path/to/miniconda3/etc/profile.d/conda.sh

We need to define the following constants in your **scipion3/config/scipion.conf** file:

.. code-block:: bash

    CONDA_ACTIVATION_CMD = . /path/to/miniconda3/etc/profile.d/conda.sh
    MYPROG_ENV_ACTIVATION = conda activate myprogenv-1.0

Add the following functions to the Plugin class:

.. code-block:: bash

    @classmethod
    def getDependencies(cls):
        # try to get CONDA activation command
        condaActivationCmd = cls.getCondaActivationCmd()
        neededProgs = []
        if not condaActivationCmd:
            neededProgs.append('conda')

        return neededProgs

    @classmethod
    def getMyProgEnvActivation(cls):
        """ Remove the scipion home and activate the conda environment. """
        activation = cls.getVar(MYPROG_ENV_ACTIVATION)
        scipionHome = Config.SCIPION_HOME + os.path.sep

        return activation.replace(scipionHome, "", 1)

The first one is used to make sure the "conda" command is available (either after activation or from PATH),
while the second one is required to activate the specific conda environment.

You also need to import **Config** from *pyworkflow.utils* at the top of the file and define **MYPROG_ENV_ACTIVATION** both in **defineVariables** and also the **constants.py** file.

Modify the **getProgram** function so that it concatenates 3 commands:
cls.getCondaActivationCmd(), cls.getMyProgEnvActivation() and the program variable (**example_script.py**).

Now change **addPackage** function inside **defineBinaries**: you need to set **tar=void.tgz** add **commands** argument that will
create and activate a new conda environment. e.g:

.. code-block:: bash

    conda create -y -n myprogenv-1.0 python=3;
    conda activate myprogenv-1.0;
    touch IS_INSTALLED;

Here we did not install any packages inside the new conda env since our simple script is not a python package.

Last, let's modify **getEnviron** function and remove **PYTHONPATH** key from Environ dict - this is required for the virtual environment to work properly within Scipion.

Now we are ready to install myprogram-1.0 with conda environment (remember, we have renamed to myprogram-1.1, so now our binaries are missing if you run `./scipion3 installb -h`)
Execute the following:

.. code-block:: bash

    ./scipion3 installb myprogram

Here we did not provide the version, so the version with **default=True** flag is installed.
If the installation have completed successfully, you are in luck!
Look into **software/em/myprogram-1.0**, you should see IS_INSTALLED empty file.
Remove MYPROGRAM_HOME from the **scipion.conf** file and move our little script back:

.. code-block:: bash

    cd scipion3/software/em
    mv myprogram-1.1/example_script.sh myprogram-1.0/

We are finally ready to run our protocol. If everything went well, you should see something like this:

.. figure:: /docs/images/dev/template_practice/practice5_ex5.png
   :alt: The binary works within new conda environment

Results for this exercise can be found in the following git branch:

.. code-block:: bash

    cd scipion-em-template
    git checkout course5_ex5

Summary
=======

In this tutorial we have explored the Plugin class and its main methods.
Once you get familiar with them you should be able to create **__init__.py** file for your plugin easily.
If you are brave enough, you can have a look at the Sphire plugin code that provides a more complex conda-based installation, use of void.tgz among other things:

https://github.com/scipion-em/scipion-em-sphire/blob/master/sphire/__init__.py
