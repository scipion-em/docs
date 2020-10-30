.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _creating-a-workflow-template:

==========================================
Creating a workflow template
==========================================

Associated resources
====================
Here you can find resources associated with this content, like videos or presentations used in courses:

`Course presentation <https://docs.google.com/presentation/d/1KGz6_A2YLtjIBoiLKqhHTBUr2HYhqvAz91WiWWSXNQY/present?usp=sharing>`_
`Facilities workflows <../../facilities/facilities-workflows>`_.

Scipion can export a workflow or a series of protocols to a file.
A ``Scipion workflow file`` contains all the attributes for each protocol
selected in the project window. This file can then be used to create a new
project.

This workflow file can be customized to ask for some values before creating the
project.


Cloning and installing scipion-em-template
==========================================
If you are following a course you might already have done this. This practice starts form the master branch.

.. code-block:: bash

    cd desired/location
    git clone https://github.com/scipion-em/scipion-em-template.git
    cd scipion3/location
    ./scipion3 installp -p scipion-em-template/location --devel


Exporting a workflow
---------------------

When you have a workflow, its protocols can be selected by ctrl-click on
each one. When you have more than one protocol selected, in the Scipion options
bar, ``Export`` option will appear as shown in the following figure:


.. figure:: /docs/images/general/export_workflow.png
   :width: 750
   :alt: Export workflow

.. important::

        For the ``Export`` option to appear, more than one protocol must
        be selected.

After that, you will be able to choose the path where you can
store the file, as well as be able to change its name.

.. important::

          The file extension must be ``json.template`` and must be stored at
          ``myplugin/templates``.

Scipion’s templates are ``JSON files`` (`read more info about JSON files <https://www.json.org>`_).

.. code-block:: json

        [
        {
            "object.className": "MyPluginPrefixHelloWorld",
            "object.id": "2",
            "object.label": "myplugin - Hello world",
            "object.comment": "",
            "_useQueue": false,
            "_prerequisites": "",
            "_queueParams": null,
            "runName": null,
            "runMode": 0,
            "message": "Hello world!",
            "times": 10,
            "previousCount": 0
        },
        {
            "object.className": "MyPluginPrefixHelloWorld",
            "object.id": "84",
            "object.label": "myplugin - Hello world (2)",
            "object.comment": "",
            "_useQueue": false,
            "_prerequisites": "",
            "_queueParams": null,
            "runName": null,
            "runMode": 0,
            "message": "Hello world!",
            "times": 10,
            "previousCount": 0
        },
        {
            "object.className": "MyPluginPrefixHelloWorld",
            "object.id": "118",
            "object.label": "myplugin - Hello world (3)",
            "object.comment": "",
            "_useQueue": false,
            "_prerequisites": "",
            "_queueParams": null,
            "runName": null,
            "runMode": 0,
            "message": "Hello world!",
            "times": 10,
            "previousCount": 0
        }
    ]


Launching the template
----------------------

Scipion uses a command to discover the templates which it searches in its
folders as well as those of the plugins and displays a list of them. The
command is as follows:

.. code-block:: bash

        ./scipion3 template

The following window is loaded once the previous command is executed.

.. figure:: /docs/images/general/template_list.png
   :width: 750
   :alt: Template List

.. note:: Here you can select a template which will appear as follows:
          ``plugin name - template name``. Also note that the template does not
          have any description. Later we will explain how to add it.


After selecting the template, a window will appear allowing you to execute
it.

.. figure:: /docs/images/general/loading_template.png
   :width: 450
   :alt: Loading template

After clicking the ``Start`` button, a project will be generated with the
protocols inside the template and all of them will be schedule as shown in the
figure below:

.. figure:: /docs/images/general/running_template.png
   :width: 750
   :alt: Running a template


Adding a description
--------------------
In order for a description to appear for the template that we have created, it
would only be necessary to write in the header of the template the
description.

.. code-block:: json

        This is an example of a template description
        [
        {
            "object.className": "MyPluginPrefixHelloWorld",
            "object.id": "2",
            "object.label": "myplugin - Hello world",
            "object.comment": "",
            "_useQueue": false,
            "_prerequisites": "",
            "_queueParams": null,
            "runName": null,


.. figure:: /docs/images/general/description_template.png
   :width: 750
   :alt: Description template


Adding dynamic fields
----------------------

In some cases, you may need to ask the user for certain values before creating
and launching the project such as movie's path, sampling rate, dose,... In our
example we want to ask for the ``Message`` and the ``Time`` parameters.


.. figure:: /docs/images/general/customized_template.png
   :width: 750
   :alt: Customized template

See how the ``dynamic fields`` syntax `works <../../facilities/facilities-workflows#creating-custom-dynamic-templates>`_.

Once you think you have it, run it and check Scipion asks for the right values and the
project created works and has the expected parameters.




