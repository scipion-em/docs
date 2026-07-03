.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo


.. _facilities:

======================
Scipion for facilities
======================

Facilities overview
---------------------

Scipion is a comprehensive platform for cryo-EM data processing that has become a valuable tool for cryo-EM facilities worldwide. By combining a unified processing framework with robust streaming capabilities, Scipion enables facilities to monitor data acquisition in real time while taking advantage of a broad ecosystem of image processing software through a single interface.

Streaming Data Processing
---------------------------
Streaming is one of the key features that makes Scipion particularly well suited for facility environments. As images are acquired by the microscope, Scipion automatically processes incoming data, allowing facility staff and users to monitor the quality of an acquisition without waiting for the session to finish.

Real-time processing provides immediate information about acquisition quality, including motion correction, CTF estimation, particle picking, and other processing metrics. This continuous feedback allows problems to be detected early, reducing unnecessary microscope time and helping users maximize the quality of their datasets.

A Unified Processing Framework
---------------------------
Unlike standalone processing pipelines, Scipion provides access to a large collection of cryo-EM software packages within a single environment. This allows facilities to benefit from:

* Integration of the best available software for each processing step.
* Complete traceability of processing parameters and results.
* Reproducible workflows that can be easily shared and reused.
* Reliable and accurate processing through validated workflows.

This unified approach simplifies both routine facility operation and user support while maintaining the flexibility required by different acquisition strategies.

Streaming Workflows for Production Environments
---------------------------
Scipion streaming workflows are designed to run efficiently on modern computing infrastructures, making effective use of GPU resources and integrating naturally with workload managers such as **SLURM**.

To facilitate deployment in production environments, the Scipion team provides a collection of stable streaming workflows inside Scipion and located in through `WorkflowHub <https://workflowhub.org/>`_ These workflows implement best practices for automated processing while remaining fully editable, allowing each facility to adapt them to its microscope configuration, computational infrastructure, and experimental requirements.

Installation and Facility Support
---------------------------
The Scipion team has extensive experience deploying Scipion in cryo-EM facilities, from standalone workstations to large HPC infrastructures. We provide support for installation, configuration, optimization, and integration with local computing resources, including GPU clusters and scheduling systems.

Today, Scipion is routinely used in numerous cryo-EM facilities around the world.

.. raw:: html

   <iframe src="https://www.google.com/maps/d/u/0/embed?mid=1aPGafshsnSW77ATfBBqXXWFWbh5DxWk&ehbc=2E312F&noprof=1"
           width="700"
           height="480"></iframe>

   <https://www.google.com/maps/d/u/0/edit?mid=1aPGafshsnSW77ATfBBqXXWFWbh5DxWk&usp=sharing>

Towards Closed-Loop Data Acquisition
---------------------------
Scipion is extending its streaming capabilities towards closed-loop acquisition, where processing results can directly influence microscope operation during data collection. Through its integration with **SmartScope**, processing results obtained during streaming can be fed back into the acquisition workflow, enabling data-driven decisions while screening is still in progress.

This feedback loop allows microscope acquisition strategies to be adapted automatically according to live processing results, improving screening efficiency, optimizing microscope usage, and moving towards increasingly autonomous cryo-EM data collection.
