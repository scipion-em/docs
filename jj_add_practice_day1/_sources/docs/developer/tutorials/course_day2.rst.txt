.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _developers_day2:

.. contents:: Table of Contents

==================================================
Developers' course Day 2 (Protocols and Viewers):
==================================================

Writing a protocol
==================

In this practice we will see how to create a protocol that performs some useful calculation on volumes. As an illustrative example, in this practice we construct a protocol that performs a low pass filter of a volume using a system call. In particular you will learn to:

* Define a protocol from scratch and letting Scipion know that it exists
* Define a form with a variety of input parameters (FloatParam, EnumParam, PointerParam) and how to hide some of the form parameters depending on specific choices in the form
* How to access basic information of EM objects as their pixel size, box size
* How to invoke a command line in the shell from inside Scipion
* How to register an output object in Scipion so that it can be the input of the next protocol
* How to read images and volumes in Python in order to perform calculations inside the Python routines
* How to construct support functions that help to prevent errors and document the calculations

As preparation for this day, you may watch `Video protocol <https://www.youtube.com/watch?v=y9AMLywnBMw>`_, `source code protocol <https://github.com/scipion-em/scipion-em-template/tree/course1_exDay2>`_, `slides protocol <https://drive.google.com/file/d/1VRO1tdVJsF23av8uGBsJZIA_vazeUEk1/view?usp=sharing>`_

Writing a viewer
================

By default, the viewer of a protocol is made of the default viewers for each one of its outputs. However, you may want to construct specific viewers for your protocol. In Scipion there are two kinds of viewers: with and without forms. You may learn how to do this viewers at:

* Without form: `Video without form <https://www.youtube.com/watch?v=_sxA0O4_rpg>`_, `source code without form <https://github.com/scipion-em/scipion-em-template/tree/course1_exDay2>`_, `slides without form <https://drive.google.com/file/d/1-O1dT-aOtKwhaKBsQuCQSQrmhuuW_PuO/view?usp=sharing>`_.
* With form: `Video with form <https://www.youtube.com/watch?v=eHQrsodO6xQ>`_, `source code with form <https://github.com/scipion-em/scipion-em-template/tree/course1_exDay2b>`_, `slides with form <https://drive.google.com/file/d/1DxH6-Aks-Ix2dOk0pzZn_cD7se8shR6O/view?usp=sharing>`_

In this practice, you will learn how to:

* Access objects from the invoking protocol
* Invoke a Scipion viewer on a Scipion object
* Invoke a Scipion viewer on a file (that is not an object)
* How to construct your own viewer using standard Python libraries

Practice
========

You may try to construct a protocol by yourself. The suggestion is to construct a protocol that subtracts two volumes. You may find a `possible solution here <https://github.com/scipion-em/scipion-em-template/tree/course1_exDay2b>`_.


.. |cite-icon| image:: /docs/images/guis/cite_icon.png
