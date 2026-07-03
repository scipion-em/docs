.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo


.. _facilities:

======================
Scipion for facilities
======================

Facilities overview
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Scipion is a comprehensive platform for cryo-EM data processing that has become a valuable tool for cryo-EM facilities worldwide. By combining a unified processing framework with robust streaming capabilities, Scipion enables facilities to monitor data acquisition in real time while taking advantage of a broad ecosystem of image processing software through a single interface. Today, Scipion is routinely used in numerous cryo-EM facilities around the world.

.. raw:: html

   <iframe src="https://www.google.com/maps/d/u/0/embed?mid=1aPGafshsnSW77ATfBBqXXWFWbh5DxWk&ehbc=2E312F&noprof=1"
           width="700"
           height="480"></iframe>

   <https://www.google.com/maps/d/u/0/edit?mid=1aPGafshsnSW77ATfBBqXXWFWbh5DxWk&usp=sharing>

Streaming Data Processing
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Streaming is one of the key features that makes Scipion particularly well suited for facility environments. As images are acquired by the microscope, Scipion automatically processes incoming data, allowing facility staff and users to monitor the quality of an acquisition without waiting for the session to finish.

Real-time processing provides immediate information about acquisition quality, including motion correction, CTF estimation, particle picking, and other processing metrics. This continuous feedback allows problems to be detected early, reducing unnecessary microscope time and helping users maximize the quality of their datasets.


A Unified Processing Framework
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Unlike standalone processing pipelines, Scipion provides access to a large collection of cryo-EM software packages within a single environment. This allows facilities to benefit from:

* Integration of the best available software for each processing step.
* Complete traceability of processing parameters and results.
* Reproducible workflows that can be easily shared and reused.
* Reliable and accurate processing through validated workflows.

This unified approach simplifies both routine facility operation and user support while maintaining the flexibility required by different acquisition strategies.

Streaming Workflows for Production Environments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Scipion streaming workflows are designed to run efficiently on modern computing infrastructures, making effective use of GPU resources and integrating naturally with workload managers such as **SLURM**.

To facilitate deployment in production environments, the Scipion team provides a collection of stable streaming workflows inside Scipion and located in through `WorkflowHub <https://workflowhub.org/>`_ These workflows implement best practices for automated processing while remaining fully editable, allowing each facility to adapt them to its microscope configuration, computational infrastructure, and experimental requirements.

Installation and Facility Support
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The Scipion team has extensive experience deploying Scipion in cryo-EM facilities, from standalone workstations to large HPC infrastructures. We provide support for installation, configuration, optimization, and integration with local computing resources, including GPU clusters and scheduling systems.


Towards Closed-Loop Data Acquisition
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Scipion is extending its streaming capabilities towards closed-loop acquisition, where processing results can directly influence microscope operation during data collection. Through its integration with `SmartScope <https://docs.smartscope.org/>`_, processing results obtained during the processing on Scipion can be fed back into the screening, enabling data-driven decisions while screening is still in progress.

This feedback loop allows microscope acquisition strategies to be adapted automatically according to live processing results, improving screening efficiency, optimizing microscope usage, and moving towards increasingly autonomous and more efficient cryo-EM data collection.

To enable this functionality, SmartScope and the scipion-em-smartscope plugin must be installed and configured. Scipion provides a dedicated streaming workflow up to the 2D classification stage that includes all the protocols required to implement the feedback loop between image processing and microscope acquisition. This workflow can also serve as a starting point for facilities wishing to customize their own closed-loop acquisition strategies.

.. figure:: /docs/images/facilities/feedbackLoop.png
   :width: 600
   :align: center
   :alt: Feedback loop


OSC-EM (Open Standards Community for EM)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. figure:: /docs/images/facilities/OSCEM.png
   :width: 200
   :alt: scipion logo


OSC-EM is a community-driven effort to standardize metadata across the full lifecycle of electron microscopy (EM) experiments by defining a common schema that spans data acquisition, processing, and deposition.

The core metadata schema is developed in `OSCEM_Schemas` on `GitHub <https://github.com/osc-em/oscem-schemas>`_
This schema is authored in **LinkML**, which allows modular definition of experimental components—such as “sample,” “instrument,” “processing,” and more—and supports export to multiple formats (JSON Schema, JSON-LD, OWL, RDF) to ensure wide interoperability.

OSC-EM aims for strong semantic alignment by reusing existing ontologies when possible: for example, it integrates terms from the CryoEM Ontology, the PDBx/mmCIF dictionary, the Helmholz EM Glossary, and the NeXus-FAIRmat NXem format.
Metadata extraction tools have been developed to work with common acquisition software (e.g., SerialEM, Thermo Fisher EPU), generating JSON files compliant with the OSC-EM schema.

To facilitate data sharing and deposition, OSC-EM also provides a converter from its JSON metadata to the mmCIF format used by repositories like the EM Data Bank (EMDB) and the Protein Data Bank (PDB).

The ``scipion-em-facilities`` plugin allows running the OSCEM protocol, which generates the complete OSCEM metadata schema for each acquisition session.