.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _customizing-a-workflow-based-on-a-template:

==========================================
Customizing a workflow based on a template
==========================================

Associated resources
====================
Here you can find resources associated with this content, like videos or presentations used in courses:

`Course presentation <https://docs.google.com/presentation/d/1KGz6_A2YLtjIBoiLKqhHTBUr2HYhqvAz91WiWWSXNQY/edit?usp=sharing>`_


Scipion creates a template from a workflow or a series of protocols.
A ``Scipion template`` is nothing more than a file that contains all the attributes,
as well as the values assigned to each of these for each protocol chosen in a
workflow. This file can then be running as a new project.


Creating a Scipion template
----------------------------

When you have a workflow, its protocols can be selected by ctrl-click on
each one. When you have more than one protocol selected, in the Scipion options
bar, ``Export`` option will appear as shown in the following figure:


.. figure:: /docs/images/general/export_workflow.png
   :width: 750
   :alt: Export workflow

.. important::

        For the ``Export`` option to appear, more than one protocol must
        be selected.

After that, you will be able to choose the address where you can
store the file, as well as be able to change its name.

.. important::

        The file extension must be ``json.template`` and must be stored in a
        folder named ``templates`` within the plugins.

Scipion’s templates are JSON files, which are composed by a
list of all the selected protocols in the workflow (`read more info about JSON files <https://www.json.org>`_).

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


Launching a template
--------------------

Scipion uses a command to discover the templates which it searches in its
folders as well as those of the plugins and displays a list of them. The
command is as follows:

.. code-block:: bash

        ./scipion template

The following window is loaded once the previous command is executed.

.. figure:: /docs/images/general/template_list.png
   :width: 750
   :alt: Template List

.. note:: Here you can select a template which will appear as follows:
          ``plugin name - template name``. Also note that the template does not
          have any descriptions. Later we will explain how to add it.


After selecting the template, a window will appear allowing you to execute
it.

.. figure:: /docs/images/general/loading_template.png
   :width: 450
   :alt: Loading template

After clicking the ``Start`` button, a project will be generated where the protocols
that were selected will be scheduled and executed as shown in the figure below:

.. figure:: /docs/images/general/running_template.png
   :width: 750
   :alt: Running a template


Customizing a template
----------------------
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

On the other hand, usually, we always must set the same parameters that are specific for each
protocols, such as movies path, sampling rate, ... In our example it could be
the Message or the Times parameters. Then, in order to avoid manually editing
this parameters by opening every protocol in the workflow, Scipion has a mode
to open modified templates in such a way that a wizard is launched
asking for all that specific parameters, at once.


.. figure:: /docs/images/general/customized_template.png
   :width: 750
   :alt: Customized template

You can fill the form according to your data or just leave all the
displayed fields untouched. As you click on the ``Start`` button,
Scipion should appear with the new project.

For this Scipion mode to appear, templates must be customized.
This link explains in detail `how to customize and launch a dynamic template <https://scipion-em.github.io/docs/docs/facilities/facilities-workflows.html#creating-custom-dynamic-templates>`_.




