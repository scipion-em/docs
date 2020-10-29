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

When you have a workflow, its protocols can be selected by ctrl-clicking on
each one. When you have more than one protocol selected, in the Scipion options
bar, ``Export`` option will appear as shown in the following figure:


.. figure:: /docs/images/general/export_workflow.png
   :width: 450
   :alt: Export workflow

.. important::

        For the ``Export`` option to appear, more than one protocol must
        be selected.
        The file extension must be ``json.template`` and must be stored in a
        folder named ``templates`` within the plugins.


Scipion uses a command to discover the templates which it searches in its
folders as well as those of the plugins and displays a list of them. The
command is as follows:

.. code-block:: bash

        ./scipion template

The following window is loaded once the previous command is executed.


.. figure:: /docs/images/general/template_list.png
   :width: 450
   :alt: Template List




