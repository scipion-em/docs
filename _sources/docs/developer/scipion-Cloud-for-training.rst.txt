.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _scipion-Cloud-for-training:

=========================================
Scipion Cloud for training
=========================================

AWS for Scipion training (only for the i2pc group)
==================================================

Creating AWS instances for training
----------------------------------------

Only AWS admin user can do that, but these are the steps.

* Login to `[AWS console] <https://aws.amazon.com/>`_
* Go to EC2 services
* Select AMIs on the left side menu
* Select i2pc-cloud-training and click on ``Launch``

.. figure:: /docs/images/cloud/AWSconsole-AMIs.png
   :alt: AWS console - AMIs

* Choose the instance type appropriate for the training. For the usual Workflow (ExtendedBetagal) we normally use p2.xlarge (GPU).
* Click ‘Next: Configure instance details’ and select the number of instances to be created.
* Click ‘Next: Add Storage’ and specify the disk size (30 GB by default).
* Click ‘Next: Add tags’ and specify the following tags:


.. figure:: /docs/images/cloud/AWSconsole-AddTags.png
   :alt: AWS console - Add tags


(UserName must be i2pc-training but Name can be chosen, although it must contain the word training).

* Click ‘Next: Configure Security group’ and select the one named ‘i2pc-training-sg’.

.. figure:: /docs/images/cloud/aws-i2pc-training-sg.png
   :alt: AWS console - Security Groups

ssh is by default restricted to CNB IP range but it could be changed if necessary.

* Click on ‘Review and launch’ and press ‘Launch’.
  A pop-up window will appear to select a security key pair. You can either select key i2pc-training or create a new one.


.. figure:: /docs/images/cloud/AWSconsole-Keypairs.png
   :alt: AWS console - Key pairs

* Click on ‘Launch Instances’ and go to ‘View Instances’ and wait until instances has been initialized (Status Checks)

Instances are by default created with a dynamic IP address. This means that when the instance is restarted the IP changes. AWS allows to create ‘Elastic IPs’ that are fix IPs that can be assigned to an instance. This way even if the instance is restarted the IP is kept, which which might interesting for a multi-day course. The steps to do this are:

* Go to the Left side menu ‘Network and Security’/Elastic IPs
* Click on ‘Allocate new address’
* Once the new IP address appears on the list select it and click on ‘Actions/Associate address’.

By default AWS have a limit of 5 Elastic IPs but this limit can be changed through the AWS support service.

Managing training instances
============================

There is a user called i2pc-training that can only manage training instances (start, stop and reboot). The steps are:

* Login to `AWS console <https://aws.amazon.com/>`_
* Go to EC2 services
* Select Instances on the left side menu
* Select the instance and either click on ‘Actions’ or Right-click on the instance and select Instance State and the action required.


.. figure:: /docs/images/cloud/AWSconsole-managetraininginstances.png
   :alt: AWS console - manage training instances

Accessing training instances
=============================

Once instances are up and running they can be accessed either through ssh or guacamole.

* Ssh: user ubuntu with pubkey i2pc-training
* VNC with password on the following URL https://PUB_IP/vnc.html

The first time you will be warned that connection is not secure and will have to add a security exception).

This is how Desktop on the new machine will look like:

.. figure:: /docs/images/cloud/noVNC-desktop.png
   :alt: noVNC - desktop

To resize screen clicks on the Settings icon and set ``Scaling Mode`` to ``Remote Resizing``:

.. figure:: /docs/images/cloud/noVNC-resize.png
   :alt: noVNC - resize

To disconnect from the session click on the little arrow that appears on the left (see menu below) and click on the last option:

.. figure:: /docs/images/cloud/noVNC-menu.png
   :alt: noVNC - disconnect

IMPORTANT!! Do not disconnect from the top right corner, as in a physical machine. If you do so the machine will need to be reboot.

There is a shortcut for Scipion on the desktop.

The following software is installed on the machine:

* Ubuntu 16
* Scipion on /usr/local/scipion (alias scipion): git installation branch release-1.1.facilities-devel with the following EM Packages:

  * Ctffind4 4.1.8
  * Gctf 1.06
  * Gautomatch 0.53
  * Eman 2.12
  * Frealign 9.07
  * Motioncor2 1.0.2
  * Motioncorr 2.1
  * Relion 2.0
  * resmap   1.1.5s2
  * Spider 21.13
  * chimera 1.10.1

* Scipion devel on /usr/local/scipion_devel (alias scipion_devel): git installation branch model_04_chimerafit
* Nvidia driver version 384
* CUDA 7.5 and 8.0 (default cuda links to 7.5).
* TurboVNC 2.1.1 on
* VirtualGL 2.5.2
* noVNC

The FEICourse finished project can be found under Scipion projects while project raw data is located at /data/relion13_tutorial.

Prices on AWS for Scipion training
=====================================

On AWS you pay for time you consume resources. In this case we have to pay for the time that instances are up running plus the disk space they occupy even when they are stopped. Also, we should pay for downloading data.
Typical GPU instance type used for the course is p2.xlarge and it costs 1.09$/hour in AWS Ireland region.
EBS volume costs 0.133$/GB/month. Downloads costs 0.11$/GB (prices January 2018).

So, for instance, for a typical two days course in Europe (AWS Ireland region) one p2.xlarge instance with a 30 GB disk assuming that machine is up for 16 hours but it exists during 48 hours will have the following cost:

* Instance: 16*1.09$ = 17.44$
* EBS volume: 30*0.133*48/720 = 0.266$
* The cost of downloading final results (maps) which are in order of MB are irrelevant.

Total cost per machine for a 2 days course is around 18$ (tax included).

If Elastic IPs were specified they might imply extra costs. Elastic IPs are free while they are allocated to a running instance, but if the instance is stopped or terminated the IP costs 0.006$/hour, which for a 2 days course might be considered irrelevant.

EGI Federated Cloud for training
==================================
The Federated Cloud has a training infrastructure `service <https://wiki.egi.eu/wiki/Training_infrastructure>`_ that could be used by registered users (EGI checking previous registration needed).

We could also use the FedCloud for training with the following considerations:

* We normally operate through Virtual Organization enmr.eu (Westlife project) but we could also use VO training.egi.eu
* The agreement to use the latest for GPU instances (IISAS) is:

  * 2 VMs with 6 CPU cores, 1 GPU and 12GB of RAM (in normal condition)
  * 4 VMs with 6 CPU cores, 1 GPU and 12GB of RAM (require reservation)

* Non GPU instances are not that restricted using different providers (CESNET, IISAS)
* They have a FedCloud Client UI (Ubuntu 16.04.02) already configured with 40 different training accounts. Every 6h, a cron job updates the proxy for each user with the PUSP generated from the robot. They can create an account for us on that UI. This is useful if we want students to start their own VMs but this is not the normal case.

 * VMs management can be done through VM management dashboard (https://dashboard.appdb.egi.eu), which offers a Web interface for both trainers and students to deploy and manage VMIs from the Marketplace on the training infrastructure.

FedCloud Scipion instance for training
------------------------------------------
Currently there is not a proper image for Scipion training in the FedCloud, however an instance could be launched using the ScipionCloud images on the AppDB and customized for the training.

