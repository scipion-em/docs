.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo


.. _installation_deployment:


============================
Installation and deployment
============================

Scipion can be deployed in a wide range of computational environments, from local
workstations to large HPC clusters. Our team has extensive experience assisting
facilities with installation and configuration on `HPC systems <https://scipion-em.github.io/docs/release-3.0.0/docs/scipion-modes/how-to-install.html#for-hpc-clusters>`_, ensuring optimal
integration with job schedulers, storage architectures and GPU resources.

Container-based deployment solutions are also supported, providing a simplified and
reproducible installation path using technologies such as Docker or Singularity/Apptainer.
These solutions are particularly useful for facilities that require isolated or
maintainable environments.

To efficiently execute streaming workflows, Scipion integrates with queue management systems such as SLURM, allowing processing jobs to be scheduled automatically while making optimal use of available GPU resources. See the `SLURM and queue engine configuration <https://scipion-em.github.io/docs/release-3.0.0/docs/scipion-modes/how-to-install.html#integration-with-queue-engines-slurm-others>`_.

Scipion can additionally be installed within the `**SBGrid** software environment <https://sbgrid.org/software/titles/scipion>`_, making
it easy for facilities already using SBGrid to incorporate Scipion seamlessly into their
existing ecosystem.

Scipion has been successfully deployed in numerous cryo-EM facilities worldwide. Thanks to its plugin-based architecture, each installation can be tailored to the specific needs of a facility by selecting only the required plugins. This flexibility simplifies maintenance while allowing facilities to support different experimental workflows within the same installation. The Scipion team also provides a collection of validated streaming workflows designed for routine facility operation. These workflows have been tested for robustness in production environments and can be easily customized to match the microscope configuration, computational infrastructure, and standard operating procedures of each facility. Every facility also operates within its own data management ecosystem. Scipion can be integrated with external Laboratory Information Management Systems (LIMS) and other facility management tools. For example, the Cryo-EM Facility at the CNB-CSIC (Madrid) integrates Scipion with `EMHub <https://3dem.github.io/emdocs/emhub/index.html>`_, providing a complete environment for experiment management, data organization, acquisition monitoring, and automated streaming data processing.

If required, expert support is available to guide facilities through the installation and
validation process, helping tailor Scipion to their specific infrastructure and workflow
needs. :ref:`Contact Us <contact-us>`
