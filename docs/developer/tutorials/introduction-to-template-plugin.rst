.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _introduction-to-template-plugin:

===============================
Introduction to template plugin
===============================

Associated resources
====================
Here you can find resources associated with this content, like videos or presentations used in courses:

* `Course presentation <https://docs.google.com/presentation/d/1sACaNZFgH0qWeXE6BLUWEDW3cjYTS4kbojrKvvRp78s/present?usp=sharing>`_

* `Creating a basic plugin from scipion-em-template <creating-a-basic-plugin-from-template>`_

The template plugin
===================

What is scipion-em-template?
----------------------------
It’s a simple and illustrative plugin designed to be an example for developers to get familiar with Scipion Framework.

Which protocols does scipion-em-template contain?
-------------------------------------------------
To check this, open in PyCharm file protocols.py and press **Ctrl+O** (Eclipse keymap) to quickly check its contents.
The result of this action should be:

.. figure:: /docs/images/dev/template_practice/practice1_intro_protocol_list.png
   :alt: intro protocol list

Thus, there is only one protocol named **MyPluginPrefixHelloWorld**.

*Note*: there can be more than one protocol in the same .py file, e. g. TiltSeries import which contains the import protocols
for both TiltSeries and TiltSeries Movies.

Where are my plugin protocols located in Scipion GUI?
-----------------------------------------------------
**Protocols.conf** is the file used for that purpose.

.. figure:: /docs/images/dev/template_practice/practice1_intro_protocols_conf.png
   :alt: intro protocols.conf

Thus, the protocol **MyPluginPrefixHelloWorld** located in **Protocols SPA** list, section **Tools**, in protocol group
**Greetings**, under the name of **Hello world**, as can be observed in the figure below.

.. figure:: /docs/images/dev/template_practice/practice1_intro_gui_prot_list.png
   :alt: intro gui protocol list

Protocol GUI overview
---------------------
First of all, let’s have a look at the protocol GUI. To display it, just double click on **Hello World**.
Below is the protocol GUI form in which you can see where the information comes from:

.. figure:: /docs/images/dev/template_practice/practice1_intro_frontend_gui_I.png
   :alt: intro protocol gui

What does it do?
----------------
Protocol frontend
.................

Section and parameter definition are encoded in the method ``_defineParams``, as can be observed in the following example.
The figure below shows how each code section in ``_defineParams`` is getting displayed in the protocol GUI.

.. figure:: /docs/images/dev/template_practice/practice1_intro_frontend_gui_code_II.png
   :alt: intro protocol gui vs code

Project frontend
................

Protocol results and any other relevant information can be displayed in the project GUI window using methods
``_summary`` and ``_methods``. The following two figures show how the corresponding
code is represented in the project GUI.

.. figure:: /docs/images/dev/template_practice/practice1_intro_frontend_gui_code_III.png
   :alt: intro project gui vs code - summary

.. figure:: /docs/images/dev/template_practice/practice1_intro_frontend_gui_code_IV.png
   :alt: intro project gui vs code - methods

Protocol backend
................

Method ``_insertAllSteps`` is used as main method. All the protocol execution steps and their order is
defined here. As can be seen in the figure below, each step is registered using method
``_insertFunctionStep**``, and then they must be declared.

.. figure:: /docs/images/dev/template_practice/practice1_intro_backend_code.png
   :alt: intro backend code

Other elements
..............

The plugin complexity can be increased if required with some other elements such as wizards, converts, viewers or
plugin specific objects. Here we'll only touch the wizards concept.

Wizards are used to get specific user input in an interactive manner. Most often they help a user to optimize
protocol options and parameters before the protocol starts running. They’re very versatile. A real example is shown below.
You can see a wizard that has its own GUI and it's able to load a list of images and interactively allow the user to mask the desired
region of an image.

.. figure:: /docs/images/dev/template_practice/practice1_intro_real_wizard_ex.png
   :alt: intro real wizard example

In the `follow-up tutorial <creating-a-basic-plugin-from-template>`_ we will construct a simple wizard that offers a list of options,
which can be changed without editing the protocol GUI form code.
The corresponding code is shown below:

.. figure:: /docs/images/dev/template_practice/practice1_intro_wizard_code.png
   :alt: intro wizard code
