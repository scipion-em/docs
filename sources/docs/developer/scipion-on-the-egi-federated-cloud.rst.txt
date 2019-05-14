.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _scipion-on-the-egi-federated-cloud:

====================================
Scipion in the EGI Federated Cloud
====================================

EGI Federated Cloud is a seamless grid of academic private clouds and virtualised resources, built around open standards and focusing on the requirements of the scientific community.
It can be found under 'Cloud Compute on the `EGI services catalog <https://www.egi.eu/services/>`_.

More information can be found on `EGI Federated Cloud <https://www.egi.eu/federation/egi-federated-cloud/>`_ web site.

How to use Scipion in the EGI Federated Cloud
=============================================
For extended documentation have a look at the `User support <https://wiki.egi.eu/wiki/Federated_Cloud_user_support>`_ site but in summary the steps are:

User registration
-------------------
* Request a X509 certificate.

    Yo can obtain a certificate from your national `IGTF Certificate Authority (CA) <https://www.eugridpma.org/members/worldmap/>`_.
    In Spain the CA in charge of issuing these types of certificates is TCS and the steps for CSIC are:

       * Go to https://digicert.com/sso
       * Write "csic" in the field and select the option with the institution full name. Click on "Start single sign-on"
       * Provide your CSIC intranet credentials
       * Fill up the form, select Grid Premium as the certificate type, expiration date and e-mail
       * Click on "Request  Certificate" and the certificate will be automatically generated and installed on the browser

* Become part of a supported Virtual Organization (VO):

    * List of existing VOs can be found link:http://operations-portal.egi.eu/vo/search[here].
      In our case, due to our participation in MoBrain and Westlife projects we belong to `enmr.eu`. link:https://voms2.cnaf.infn.it:8443/voms/enmr.eu/[Request access].
    * There is a 'test' VO that can be used to try the EGI cloud for 6 months, it is called fedcloud.egi.eu and access can be requested link:https://perun.metacentrum.cz/cert/registrar/?vo=fedcloud.egi.eu[here].
    * It is also possible to create a new VO. Follow their link:https://wiki.egi.eu/wiki/PROC14_VO_Registration[VO Registration procedure] and they can invite sites from the infrastructure to support the VO.

* Most of the EGI services are accessible using the link:https://www.egi.eu/services/check-in/[EGI CheckIn service]. This authentication service accepts different 'Identity Providers':

.. figure:: /docs/images/cloud/EGI-CheckIn-providers.png
   :align: center
   :alt: EGI CheckIn Identity providers

It is possible to login with your X509 certificate (once you upload it to the web browser), using Social network accounts such as Google, or with your EduGAIN credentials, among others.

Accessing the EGI cloud resources
----------------------------------

The user can interact with IaaS cloud resources via programming APIs, command line interfaces or Web dashboards.

* Using the OCCI client

    * Install and configure `OCCI client <https://wiki.egi.eu/wiki/HOWTO11>`_
    * Browse the `Application Database Cloud Marketplace <https://appdb.egi.eu/browse/cloud>`_ the available Virtual Appliances
    * There are two ScipionCloud appliances: one GPU enabled and one for non GPU machines (this one can also be used on a non GPU machine but it has some extra software which is useless and occupy disk space).

On the 'Availability and Usage' section below you should see a list of VO's that endorse this appliance, and for each VO, the list of cloud sites where it can be instantiated.

    * Get the IDs for starting the appliance at one of the sites.
    * `Create a VOMS proxy <https://wiki.egi.eu/wiki/HOWTO11#Proxy_Generation>`_ for getting access to the infrastructure
    * In order to use VAs you will need to perform some contextualisation, which is the process of customising the appliance when it is instantiated on the resources, e.g. entering some credentials to log into the VM.

You have the contextualization script to use on the AppDB entry for the appliance, just modify your public key and vncpassword.

    * Now you can use the client to `start <https://wiki.egi.eu/wiki/FAQ10#How_can_I_start_a_VM.3F>`_ the VM using the IDs obtained from AppDB and passing the contextualization script.
    * Depending on the cloud provider you may need to allocate a public IP for the VM, check this `FAQ <https://wiki.egi.eu/wiki/FAQ10#How_can_I_assign_a_public_IP_to_a_VM.3F>`_ to assign a public IP to a VM in the Federated Cloud.
    * You can connect to the VM and start using it by login using ssh: ``ssh -i YOURPRIVATEKEY ubuntu@VMIP`` (ubuntu is the default username for the Ubuntu images in AppDB) or pointing your web browser to http://VMIP:8000/vnc.html and entering the password you set up on the contextualization script.

The following shows examples of the most useful occi commands. Extended info can be found at the link:https://wiki.egi.eu/wiki/HOWTO11_How_to_use_the_rOCCI_Client[FedCloud OCCI tutorial]. For troubleshooting, you can add "--debug" to any of the commands.

List commands
-------------

.. code-block:: bash

    # Show own compute resources (Virtual Machines)
    occi --endpoint https://carach5.ics.muni.cz:11443  --auth x509 --user-cred myproxy-enmr.pem --voms --action list --resource compute

    # Show own storage resources (Block Storage)
    occi --endpoint https://carach5.ics.muni.cz:11443  --auth x509 --user-cred myproxy-enmr.pem --voms --action list --resource storage

    # Show OS templates (VM images) available
    # You can use one of these templates to instantiate a Virtual Machine (VM)
    occi --endpoint https://carach5.ics.muni.cz:11443  --auth x509 --user-cred myproxy-enmr.pem --voms --action list --resource os_tpl

    # Show resource templates (flavors)  available
    occi --endpoint https://carach5.ics.muni.cz:11443  --auth x509 --user-cred myproxy-enmr.pem --voms --action list --resource resource_tpl

    # Describe any of the resources listed with the above commands
    occi --endpoint https://carach5.ics.muni.cz:11443  --auth x509 --user-cred myproxy-enmr.pem --voms --action describe --resource RESOURCE_URL

Instantiation command
---------------------

.. code-block:: bash
    # Instantiate a VM
    # You have to specify OS template and hardware flavor as mixin parameters (see list commands above)
    occi --endpoint https://carach5.ics.muni.cz:11443  --auth x509 --user-cred myproxy-enmr.pem --voms --action create --resource compute --attribute occi.core.title="ScipionVM" --mixin OS_TEMPLATE --mixin FLAVOUR  --context user_data="file://$PWD/tmpfedcloud.login"

The `user_data` file is a contextualization script that follows ``cloud-init`` syntax.

Storage commands
----------------

.. code-block:: bash

    # Create a Block Storage (BS). occi.storage.size is measured in GB
    occi --endpoint https://carach5.ics.muni.cz:11443  --auth x509 --user-cred myproxy-enmr.pem --voms --action create --resource storage -t occi.storage.size='num(30)',occi.core.title='ScipionBS'
    # Attach BS to VM
    occi --endpoint https://carach5.ics.muni.cz:11443  --auth x509 --user-cred myproxy-enmr.pem --voms --action link --resource VM_URL -j BS_ID
    # Detach BS from VM
    # Note: the storage link can be found in VM description
    occi --endpoint https://carach5.ics.muni.cz:11443  --auth x509 --user-cred myproxy-enmr.pem --voms --action unlink --resource STORAGE_LINK
    # Delete BS
    # Note: you cannot delete the disks that contain VM images
    occi --endpoint https://carach5.ics.muni.cz:11443 --auth x509 --user-cred myproxy-enmr.pem --voms --action delete --resource STORAGE_LINK


Network commands
================

.. code-block:: bash

    # Show available networks
    occi --endpoint https://carach5.ics.muni.cz:11443  --auth x509 --user-cred myproxy-enmr.pem --voms --action list --resource network
    # Attach VM to network
    # Note: sites such as CESNET attach new VMs to the public network by default.
    # This provides a public IP address (if available) for the VM. Other sites, like INFN do not automatically do so.
    # Besides, you might want to include a VM in a private network.
    occi --endpoint https://carach5.ics.muni.cz:11443  --auth x509 --user-cred myproxy-enmr.pem --voms --action link --resource VM_URL -j NETWORK_ID

    # Detach VM from network
    # Note: the network link can be found in the VM description
    occi --endpoint https://carach5.ics.muni.cz:11443  --auth x509 --user-cred myproxy-enmr.pem --voms --action unlink --resource NETWORK_LINK

Life cycle (trigger action)
---------------------------

.. code-block:: bash

    # Start/stop/reboot VM
    # Note: actions to be triggered can be found in the VM description
    occi --endpoint https://carach5.ics.muni.cz:11443  --auth x509 --user-cred myproxy-enmr.pem --voms --action trigger --resource VM_URL --trigger-action ACTION_URL

    # Delete  VM
    # Note: when deleting a VM, any block storage linked to it will remain.
    # Such BS can be either deleted, or attached to other VM.
    occi --endpoint https://carach5.ics.muni.cz:11443  --auth x509 --user-cred myproxy-enmr.pem --voms --action delete --resource VM_URL

* Using the VMOps dashboard

    *  Login to the `dashboard <https://dashboard.appdb.egi.eu/vmops>`_ using your EGI CheckIn credentials
    * Click on "Create a new VM Topology" to start the topology builder wizard, this will guide you through a set of steps:
    * select the Virtual Appliance (VA) you want to start, these are the same shown in the Application Database Cloud Marketplace, you can use the search field to find your VA (only the VAs endorsed by your VO(s) will be shown)
    * select the VO to use when instantiating the VA;
      select the site where to instantiate the VA; and finally
    * select the template (flavour) of the instance that will determine the number of cores, memory, disk space and GPUs used in your VM.
    * Now you will be presented with a summary page where you can further customise your VM by:

        * Adding more VMs to the topology
        * Adding block storage devices to the VMs
        * Define contextualisation parameters (e.g. add new users, execute some script)

    * Click on "Launch" and your deployment will be submitted to the infrastructure

The topology you just created will appear on your "Topologies" with all the details about it, clicking on a VM of a topology will give you details about its status and IP. You can login into the VM with any user you created in the contextualisation parameters, even if you didn't specify any users, the AppDB creates one for you and provides the credentials for login via ssh to the new VM.
If the VM has a default password, remember to replace it with a strong secret password immediately.

`ScipionCloud images <scipionCloud-images-manual>`_

