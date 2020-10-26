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

* `Course presentation <https://docs.google.com/presentation/d/1sACaNZFgH0qWeXE6BLUWEDW3cjYTS4kbojrKvvRp78s/edit?usp=sharing>`_

* `Creating a basic plugin from scipion-em-template <create-a-basic-plugin-from-template>`.

Introduction to template plugin
===============================

What is plugin scipion-em-template?
-----------------------------------
It’s a simple and illustrative plugin designed to be the example which constitutes the first contact of developers with
Scipion Framework.

Which protocols does scipion-em-template contain?
-------------------------------------------------
To check this, open, in PyCharm, file protocols.py and press ctrl + O (Eclipse keymap) to quickly check its contents.
The result of this action should be:

.. figure:: /docs/images/dev/template_practice/practice1_intro_protocol_list.png
   :alt: intro protocol list

Thus, there is only one protocol named **MyPluginPrefixHelloWorld**.

*Note*: there can be more than one protocol in the same .py file, e. g. TS import, which contains the import protocols
for both TS and TS Movies.

Where are my plugin protocols located in Scipion GUI?
-----------------------------------------------------
First of all, it’s necessary to know where are located the plugin protocols which we’re going to work with.

Protocols.conf is the file used for that purpose.

.. figure:: /docs/images/dev/template_practice/practice1_intro_protocols_conf.png
   :alt: intro protocls.conf

Thus, protocol **MyPluginPrefixHelloWorld** located in **Protocols SPA** list, section **Tools**, in protocol group
**Greetings**, under the name of **Hello world**, as can be observed in the figure below.

.. figure:: /docs/images/dev/template_practice/practice1_intro_gui_prot_list.png
   :alt: intro gui protocol list

Protocol GUI overview
---------------------
First of all, let’s have a look at the protocol GUI. To display it, just double click on Hello World. Components and
where the info comes from can be observed in the following figure:

.. figure:: /docs/images/dev/template_practice/practice1_intro_frontend_gui_I.png
   :alt: intro protocol gui

What does it do?
----------------
Protocol frontend
.................
Section and parameter definition are coded in method **_definepParams**, as can be observed in the following example.
The figure below shows how each code section in _defineParams is displayed in the protocol GUI.

.. figure:: /docs/images/dev/template_practice/practice1_intro_frontend_gui_code_II.png
   :alt: intro protocol gui vs code

Project frontend
................
Protocol results and any other relevant information can be displayed on the project GUI implementing methods
**_summary** and **_methods**. The following two figures show how the corresponding code is represented on the project
GUI.

.. figure:: /docs/images/dev/template_practice/practice1_intro_frontend_gui_code_III.png
   :alt: intro project gui vs code - summary

.. figure:: /docs/images/dev/template_practice/practice1_intro_frontend_gui_code_IV.png
   :alt: intro project gui vs code - methods

Backend
.......
Method **_insertAllSteps** is used as main method. All the steps and the order followed in the protocol execution are
managed from here. As it can be observed in the figure below, each step is registered using method
**_insertFunctionStep**, and then they must be declared.

.. figure:: /docs/images/dev/template_practice/practice1_intro_backend_code.png
   :alt: intro backend code

Other elements
..............
The plugin complexity can be increased if required with some other elements, such as wizards, converts, viewers or
plugin specific objects. Concerning this tutorial, we'll focus on wizards.

Wizards are used to get specific information related to execution directly linked, allow the user to carry out complex
operations to generate an indirect input, etc. They’re very versatile. A real example is shown below. It can be observed
that it has its own GUI, and it's able to load a list of images, and dinamically allow the user to mask the desired
region with a ring mask.

.. figure:: /docs/images/dev/template_practice/practice1_intro_real_wizard_ex.png
   :alt: intro real wizard example

Ours will consist in simply offering a list of options, which can be dynamically expanded or edited from code without
editing the frontend code. The corresponding code is shown below:

.. figure:: /docs/images/dev/template_practice/practice1_intro_wizard_code.png
   :alt: intro wizard code
