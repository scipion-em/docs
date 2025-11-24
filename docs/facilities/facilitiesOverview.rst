.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo


.. _facilities:

======================
Scipion for facilities
======================

Facilities overviews
---------------------

Scipion is a powerful platform for **real-time processing** of cryo-EM data, supporting
both **single-particle analysis (SPA)** and **tomography**. It enables facilities to
monitor acquisition sessions in real time, providing immediate feedback on parameters
such as CTF estimation and image alignment. Moreover, Scipion allows data-driven
decision-making in real time, based on live results from particle picking or 2D
classification. A growing map of facilities currently using or planning to adopt Scipion
is being compiled, highlighting its increasing role in modern cryo-EM environments.
If you are running a Cryo EM facility and want more info, please :ref:`contact us <contact-us>`

.. raw:: html

   <iframe src="https://www.google.com/maps/d/u/0/embed?mid=1aPGafshsnSW77ATfBBqXXWFWbh5DxWk&ehbc=2E312F&noprof=1"
           width="700"
           height="480"></iframe>

   <https://www.google.com/maps/d/u/0/edit?mid=1aPGafshsnSW77ATfBBqXXWFWbh5DxWk&usp=sharing>

Installation and Deployment
---------------------------

Scipion can be deployed in a wide range of computational environments, from local
workstations to large HPC clusters. Our team has extensive experience assisting
facilities with installation and configuration on `HPC systems <https://scipion-em.github.io/docs/release-3.0.0/docs/scipion-modes/how-to-install.html#for-hpc-clusters>`_, ensuring optimal
integration with job schedulers, storage architectures and GPU resources.

Container-based deployment solutions are also supported, providing a simplified and
reproducible installation path using technologies such as Docker or Singularity/Apptainer.
These solutions are particularly useful for facilities that require isolated or
maintainable environments.

Scipion can additionally be installed within the `**SBGrid** software environment <https://sbgrid.org/software/titles/scipion>`_, making
it easy for facilities already using SBGrid to incorporate Scipion seamlessly into their
existing ecosystem.

If required, expert support is available to guide facilities through the installation and
validation process, helping tailor Scipion to their specific infrastructure and workflow
needs.


Monitoring
----------

Scipion provides comprehensive tools for monitoring the status of data acquisition
sessions. Micrographs can be imported and assessed automatically, with live information
on CTF values, drift, and other quality indicators. This real-time feedback helps both
staff and users detect issues early, evaluate sample and microscope performance, and
adjust acquisition parameters as needed. You can see `an example here <https://scipion.cnb.csic.es/scipionbox/lastHTMLReport/>`_
For more details, visit :ref:`sumamary reports <summary-reports>`
.. figure:: /docs/images/facilities/monitorS.png
   :width: 700
   :alt: monitor Summary view


Workflows for SPA
------------------

Scipion includes a collection of **facility-focused workflows** designed to support
routine operations. These workflows are available:

- On `WorkflowHub <https://workflowhub.eu>`_ as publicly accessible, executable workflows.
- Within Scipion itself as ready-to-use **workflow templates**.

They implement different levels of on-the-fly processing—from basic micrograph and CTF
monitoring to more advanced steps such as particle picking and real-time 2D
classification. These workflows help standardize procedures, streamline decision-making,
and ensure consistent data quality throughout acquisition sessions.


Running streaming
------------------

Learn `how to create, import, export and launch streaming workflows <facilities-workflows>`_.

OSCEM
-----

OSC-EM (Open Standards Community for EM)
-----------------------------------------
.. figure:: /docs/images/facilities/OSCEM.png
   :width: 200
   :alt: scipion logo


OSC-EM is a community-driven effort to standardize metadata across the full lifecycle
of electron microscopy (EM) experiments by defining a common schema that spans data
acquisition, processing, and deposition.

The core metadata schema is developed in `OSCEM_Schemas` on `GitHub <https://github.com/osc-em/oscem-schemas>`_
This schema is authored in **LinkML**, which allows modular definition of experimental
components—such as “sample,” “instrument,” “processing,” and more—and supports export
to multiple formats (JSON Schema, JSON-LD, OWL, RDF) to ensure wide interoperability.

OSC-EM aims for strong semantic alignment by reusing existing ontologies when possible:
for example, it integrates terms from the CryoEM Ontology, the PDBx/mmCIF dictionary,
the Helmholz EM Glossary, and the NeXus-FAIRmat NXem format.
Metadata extraction tools have been developed to work with common acquisition software
(e.g., SerialEM, Thermo Fisher EPU), generating JSON files compliant with the OSC-EM schema. 

To facilitate data sharing and deposition, OSC-EM also provides a converter from its JSON
metadata to the mmCIF format used by repositories like the EM Data Bank (EMDB) and
the Protein Data Bank (PDB).  

The ``scipion-em-facilities`` plugin allows running the OSCEM protocol, which generates
the complete OSCEM metadata schema for each acquisition session.
