.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _creating-streaming-protocol:

=============================
Creating a streaming Protocol
=============================

We define a ``Streaming Protocol``  as a processing task that involves the
execution of several steps like any other `Scipion protocol <creating-a-protocol>`_,
but, some execution steps work in parallel. You can read more about defining steps to be executed
in parallel in `Parallelization <parallelization>`_.

We will create a simple protocol that connects to
`EMPIAR <https://www.ebi.ac.uk/pdbe/emdb/empiar/>`_ (Electron Microscopy
Public Image Archive) and downloads  a set of Movies