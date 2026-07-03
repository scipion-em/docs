.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo


.. _installation_deployment:


============================
Installation and deployment
============================


Scipion can be deployed in a wide variety of computational environments, ranging from standalone workstations to large HPC infrastructures. Its modular architecture and flexible plugin system make it particularly well suited for cryo-EM facilities, where computing resources, acquisition strategies, and processing requirements often differ from one installation to another.

or production environments, we recommend following the installation guide for which covers best practices for deploying Scipion and configuring GPU-enabled processing nodes.
See the `HPC installation guide <https://scipion-em.github.io/docs/release-3.0.0/docs/scipion-modes/how-to-install.html#for-hpc-clusters>`_ in case you want to installl Scipion in a HPC

To efficiently execute streaming workflows, Scipion integrates with queue management systems such as SLURM, allowing processing jobs to be scheduled automatically while making optimal use of available GPU resources.

See the `SLURM and queue engine configuration <https://scipion-em.github.io/docs/release-3.0.0/docs/scipion-modes/how-to-install.html#integration-with-queue-engines-slurm-others>`_.

Scipion has been successfully deployed in numerous cryo-EM facilities worldwide. Thanks to its plugin-based architecture, each installation can be tailored to the specific needs of a facility by selecting only the required plugins. This flexibility simplifies maintenance while allowing facilities to support different experimental workflows within the same installation.

The Scipion team also provides a collection of validated streaming workflows designed for routine facility operation. These workflows have been tested for robustness in production environments and can be easily customized to match the microscope configuration, computational infrastructure, and standard operating procedures of each facility.

Every facility also operates within its own data management ecosystem. Scipion can be integrated with external Laboratory Information Management Systems (LIMS) and other facility management tools. For example, the Cryo-EM Facility at the CNB-CSIC (Madrid) integrates Scipion with `EMHub <https://3dem.github.io/emdocs/emhub/index.html>`_, providing a complete environment for experiment management, data organization, acquisition monitoring, and automated streaming data processing.

For facilities requiring assistance during deployment or migration, the Scipion development team provides support for installation, configuration, workflow customization, and optimization of streaming processing pipelines. Please  :ref:`Contact Us <contact-us>`