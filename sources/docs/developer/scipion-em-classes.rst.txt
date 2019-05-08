.. _scipion-em-classes:

=======================
Scipion EM Classes
=======================

Electron microscopy image processing follows a common workflow.
Protocols for the different image processing steps are represented below
(click on image to see full size image).

.. figure:: https://cdn.rawgit.com/wiki/I2PC/scipion/images/classes_protocol.svg
   :align: center
   :width: 900
   :height: 300
   :alt: General EM protocols hierarchy

Fig. 1. General EM protocols hierarchy

Data objects processed on these protocols are the following:

.. figure:: https://cdn.rawgit.com/wiki/I2PC/scipion/images/classes_data.svg
   :align: center
   :width: 900
   :alt: Electron microscopy data objects

Fig. 2. Electron microscopy data objects

Each package provides its own implementation of the different protocols, e.g.: Xmipp.

.. figure:: https://cdn.rawgit.com/wiki/I2PC/scipion/images/classes_xmipp_protocols.svg
   :align: center
   :width: 900
   :height: 300
   :alt: Xmipp EM protocols hierarchy

Fig. 3. Xmipp EM protocols hierarchy

*Note:* These diagrams were generated using *pyreverse* in the following
way:

.. code-block:: bash

    pyreverse -A -o png -p protocol pyworkflow/em/protocol* --only-classnames

* **-A**: looks for all ancestors in all classes
* *-o* : specifies output format
* **-p**: generates output files using project name provided

In this example we used *`pyworkflow/em/protocol*`* as input to generate
protocols hierarchy only.

If you get a "No such file or directory" error, you might need to
install graphviz

.. code-block:: bash

    `sudo apt-get install graphviz`
