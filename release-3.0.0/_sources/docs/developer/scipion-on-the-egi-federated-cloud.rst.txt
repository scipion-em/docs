.. figure:: /docs/images/cloud/ScipionCloud_icon.png
   :width: 250
   :alt: ScipionCloud logo

.. _scipion-on-the-egi-federated-cloud:

====================================
Scipion in the EOSC
====================================
The European Open Science Cloud (EOSC) initiative offers researchers a virtual environment with open and seamless services for storage, management, analysis and re-use of research data, across borders and scientific disciplines by federating data infrastructures.

EOSC resources can be accessed from the `EOSC portal <https://eosc-portal.eu/>`_.

ScipionCloud is being developed as one of the EOSC-Synergy thematic `services <https://www.eosc-synergy.eu/supporting-science/scipion/>`_ and it is now available as a service in the EOSC portal.

A detailed tutorial for the service can be found in the EOSC-Synergy moodle platform for training.

.. image:: /docs/images/cloud/ScipionCloud-EOSCSynergy.png
   :width: 250
   :alt: ScipionCloud tutorial
   :target: https://moodle.learn.eosc-synergy.eu/course/view.php?id=141


How to use Scipion in the EOSC
==============================

This service is offered by the Instruct Image Processing Center (`I2PC <http://i2pc.es/>`_) as a complement to the Instruct Access Projects. After the I2PC staff has finished processing the granted project the user can request the service to continue processing the data in a virtual server (or cluster) deployed on EOSC cloud resources. This virtual server has Scipion installed as well as most of the plugins and external packages used by the community, accesible as a virtual desktop from a web browser.

The service can be requested from the `EOSC marketplace <https://marketplace.eosc-portal.eu/services/scipioncloud>`_ providing information about your project. The I2PC team will review it and assuming there are free hardware resources in one of the associated cloud sites a virtual infrastructure will be created for you.

Then you will receive an email with the URL to access the virtual infrastructure and the password to login. You will also be informed about the hardware specifications of the infrastructure and limit time to use it. Your publickey will be required to be injected in the infrastructure to allow you to copy your data.

Information on how to use the infrastructure can be found `here <scipion-infrastructure-cloud-usage>`_.

The infrastructure setup has a limited time but in case you need more time you could request it sending an email to i2pc and an extension might be granted depending on the pending requests.

In any case you will have some time to download project and results.

The service can also be deployed in your own cloud resources, either openstack site or AWS, accessing directly the `Infrastructure Manager <https://marketplace.eosc-portal.eu/services/infrastructure-manager-im>`_ service also in the EOSC marketplace following `this <https://github.com/I2PC/scipion-docker#deploy-scipion-using-im-dashboard>`_ instructions.

How to acknowledge the use Scipion in the EOSC
==============================================

Please do not forget to acknowledge the use of this infrastructure by adding the following paragraph to your publication (change IFCA by the appropiate site):

“This work made use of ScipionCloud and the resources provided by the IFCA cloud site, which have been partially supported by the project 'European Open Science Cloud - Expanding Capacities by building Capabilities' (EOSC-SYNERGY), funded by the RI Horizon 2020 Program of the European Commission under Grant Agreement No. 857647.”




