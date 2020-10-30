.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _customizing-a-workflow-based-on-a-template:

==========================================
Customizing a workflow based on a template
==========================================

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


.. code-block:: json

        # Here you can write a description of the workflow
        [
        {
            "object.className": "ProtImportParticles",
            "object.id": "2",
            "object.label": "from scipion (particles)",
            "object.comment": "",
            "_useQueue": false,
            "_prerequisites": "",
            "_queueParams": null,
            "runName": null,
            "runMode": 0,
            "importFrom": 4,
            "filesPath": "/home/yunior/Yunior/Projects/Scipion/Descentralization/data/tests/xmipp_tutorial/particles/BPV_particles_aligned.sqlite",
            "filesPattern": null,
            "copyFiles": false,
            "emxFile": null,
            "alignType": 0,
            "mdFile": null,
            "starFile": null,
            "ignoreIdColumn": false,
            "sqliteFile": "/home/yunior/Yunior/Projects/Scipion/Descentralization/data/tests/xmipp_tutorial/particles/BPV_particles_aligned.sqlite",
            "frealignLabel": null,
            "stackFile": null,
            "parFile": null,
            "lstFile": null,
            "haveDataBeenPhaseFlipped": false,
            "acquisitionWizard": null,
            "voltage": 300.0,
            "sphericalAberration": 2.7,
            "amplitudeContrast": 0.1,
            "magnification": 50000,
            "samplingRate": 4.0,
            "dataStreaming": false,
            "timeout": 43200,
            "fileTimeout": 30
        },
        {
            "object.className": "ProtCryoSparcNonUniformRefine3D",
            "object.id": "126",
            "object.label": "Cryosparc Non-Uniform 3D refinement",
            "object.comment": "",
            "_useQueue": false,
            "_prerequisites": "",
            "_queueParams": null,
            "runName": null,

            ....


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

.. note:: Here you can select a template which will appear as follows: ``plugin name - template name``


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

