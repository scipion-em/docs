.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo


.. _facilities:

======================
Scipion for facilities
======================

Facilities Support
==================

Scipion is a powerful platform for **real-time processing** of cryo-EM data, supporting
both **single-particle analysis (SPA)** and **tomography**. It enables facilities to
monitor acquisition sessions in real time, providing immediate feedback on parameters
such as CTF estimation and image alignment. Moreover, Scipion allows data-driven
decision-making during the session, based on live results from particle picking or 2D
classification. A growing map of facilities currently using or planning to adopt Scipion
is being compiled, highlighting its increasing role in modern cryo-EM environments.

Monitoring
----------

Scipion provides comprehensive tools for monitoring the status of data acquisition
sessions. Micrographs can be imported and assessed automatically, with live information
on CTF values, drift, and other quality indicators. This real-time feedback helps both
staff and users detect issues early, evaluate sample and microscope performance, and
adjust acquisition parameters as needed.

OSCEM
-----

The ``scipion-em-facilities`` plugin offers additional tools tailored specifically for
cryo-EM facilities. It is actively used at OSCEM to monitor acquisition sessions and
support daily facility operations. The plugin continues to evolve with new features
designed to simplify instrument management, provide session overviews, and integrate
facility-specific workflows.

Workflows
---------

Scipion includes a collection of **facility-focused workflows** designed to support
routine operations. These workflows are available:

- On `WorkflowHub`_ as publicly accessible, executable workflows.
- Within Scipion itself as ready-to-use **workflow templates**.

They implement different levels of on-the-fly processing—from basic micrograph and CTF
monitoring to more advanced steps such as particle picking and real-time 2D
classification. These workflows help standardize procedures, streamline decision-making,
and ensure consistent data quality throughout acquisition sessions.

.. _WorkflowHub: https://workflowhub.eu/
