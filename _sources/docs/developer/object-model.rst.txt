.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _object-model:

============
Object model
============

The base Scipion Object Model is implemented in file: https://github.com/scipion-em/scipion-pyworkflow/blob/devel/pyworkflow/object.py.

The following diagram was generated from that file:
(``pyreverse -o svg -p object .../scipion-pyworkflow/pyworkflow/object.py -k``).
It illustrates the base class ``Object`` and derived classes.

.. image:: /docs/images/classes_object.svg

.. image:: /docs/images/classes_objectFull.svg
    :alt: Diagram with base Scipion Object Model containing class methods.
