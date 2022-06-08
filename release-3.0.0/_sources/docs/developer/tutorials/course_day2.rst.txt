.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _course_day2:

=====================
Protocols and Viewers
=====================

Writing a protocol
==================

In this tutorial we will see how to create a protocol that performs some useful calculation on volumes.
As an illustrative example, in this practice we construct a protocol that performs a low pass filter
of a volume using a system call. In particular you will learn to:

* Define a protocol from scratch and letting Scipion know that it exists
* Define a form with a variety of input parameters (FloatParam, EnumParam, PointerParam) and how to hide some of the form parameters depending on specific choices in the form
* How to access basic information of EM objects as their pixel size, box size etc.
* How to invoke a command line in the shell from inside Scipion
* How to register an output object in Scipion so that it can be used as an input for the next protocol
* How to read images and volumes in Python in order to perform calculations inside the Python routines
* How to construct support functions that help to prevent errors and document the calculations

You can choose to:

* watch `the video tutorial <https://www.youtube.com/watch?v=y9AMLywnBMw>`_
* look at the `source code <https://github.com/scipion-em/scipion-em-template/tree/course1_exDay2>`__
* or check the `presentation slides <https://drive.google.com/file/d/1VRO1tdVJsF23av8uGBsJZIA_vazeUEk1/view?usp=sharing>`__

Writing a viewer
================

In Scipion there are two kinds of viewers: with and without GUI forms.

By default any protocol output will be displayed using Scipion default viewer (without any form).
This will depend on the type of Scipion object being displayed (Volume, SetOfParticles etc.)
However, you may want to construct specific viewers for your protocol.

In this practice you will learn how to:

* Access objects from the invoking protocol
* Invoke a Scipion viewer for a Scipion object
* Invoke a Scipion viewer for a file (that is not an object)
* How to construct your own viewer using standard Python libraries

You can learn how to create viewers:

* Without a form: `video tutorial <https://www.youtube.com/watch?v=_sxA0O4_rpg>`__, `source code <https://github.com/scipion-em/scipion-em-template/tree/course1_exDay2>`__, `presentation slides <https://drive.google.com/file/d/1-O1dT-aOtKwhaKBsQuCQSQrmhuuW_PuO/view?usp=sharing>`__.
* With a GUI form: `video tutorial <https://www.youtube.com/watch?v=eHQrsodO6xQ>`__, `source code <https://github.com/scipion-em/scipion-em-template/tree/course1_exDay2b>`__, `presentation slides <https://drive.google.com/file/d/1DxH6-Aks-Ix2dOk0pzZn_cD7se8shR6O/view?usp=sharing>`__

Practice
========

As an exercise you may try to construct a protocol by yourself.
The suggestion is to construct a protocol that subtracts two volumes.
You may find a `possible solution here <https://github.com/scipion-em/scipion-em-template/tree/course1_exDay2b>`_.
