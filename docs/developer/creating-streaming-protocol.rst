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
`EMPIAR <https://www.ebi.ac.uk/pdbe/emdb/empiar/>`__ (Electron Microscopy
Public Image Archive) and downloads a set of Movies and in parallel it will
register them in Scipion.

The general idea of this protocol like this:

.. figure:: /docs/images/general/streaming_idea.gif
   :width: 250
   :alt: Streaming Idea

In this sence, we will implement the following steps:

1. Read the xml file corresponding to a specific EMPIAR dataset which contains
   vital information about this movies dataset (sampling rate, dimension, ...).
2. Download one by one movies until a stop criteria is met (amount of download movies).
3. Register the downloaded movies. This step is in parallel with steps 2.






