.. _scipionCloud-on-amazon-web-services-ec2:

======================================================
ScipionCloud on Amazon Web Services EC2
======================================================

Creating an instance (virtual machine)
======================================

Depending on your computing needs, you can start ScipionCloud on a single node
("instance", in Amazon terminology), or using an elastic HPC cluster.

Amazon EC2 offers a wide range of instance types, that can be check
on `AWS instance types <https://aws.amazon.com/ec2/instance-types/>`_.

* Connect to `AWS console <https://aws.amazon.com/>`_
* Open the EC2 dashboard
* Launch a ScipionCloud instance: Enter "Instances" panel, then click "Launch instance". Follow the wizard filling in the required information:

  * Choose the ScipionCloud AMI: in *"Community AMIs"* section, search for "scipion" and find the latest release. The ScipionCloud AMI is currently available only in Ireland region but if you would like to use it in a different region contact us and we will make a copy there.
  * Choose the instance type, according to how much resources (CPU, RAM, GPU, disk) you want to use. Regarding disk, you can use an integrated SSD disk, or attach an EBS Volumen. Press "Next: Configure instance details"
  * Configure instance:

    * Number of instances: 1
    * Shutdown behavior: stop

  * Add storage: specify the disk size of the system disk (that you can use also for data). Here you can also create a new volume of arbitrary size.
  * Tag instance: Add tag 'Name' and give a descriptive name.
  * Configure security group: by default, SSH is enabled. To use the remote desktop (web based), you need to open ports 443 (HTTPS) and 22 (SSH):
  * Click "Review and Launch", then "Launch"
* In the "Select an existing key pair" panel, select "Create new key pair", type the key pair name and click "Download" key pair. Finally, click "Launch instances" and then "View instances"

Select your instance within the list of instances, and copy its public IP address. You will need this address to connect to the instance, whether via ssh or Remote Desktop.

Wait until the instance is initialized.

Accessing an instance
======================

First, connect with SSH to your instance:

.. code-block:: bash

    chmod 600 path/to/key.pem
    ssh -i path/to/key.pem ubuntu@12.34.56.78 #(use your IP)

There is a performance problem the first time an instance is used
(explanation `[here] <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-initialize.html>`_). If you want to avoid it you could follow instructions there.

Access the remote desktop from a browser with the URL and password provided.

If you see a "Your connection is not secure" warning, click on "Advanced", "Add exception" and "Confirm Security Exception".

This is how the remote desktop will look like:

.. figure:: https://github.com/I2PC/scipion/wiki/images/cloud/noVNC-desktop.png
   :align: center
   :width: 800
   :alt: noVNC-desktop

To resize screen clicks on the Settings icon and choose `Remote resizing` as `Scaling mode`:

.. figure:: https://github.com/I2PC/scipion/wiki/images/cloud/noVNC-resize.png
   :align: center
   :width: 250
   :alt: noVNC-resize

To disconnect from the session click on the little arrow that appears on the left (see menu below) and click on the last option:


.. figure:: https://github.com/I2PC/scipion/wiki/images/cloud/noVNC-menu.png
   :align: center
   :width: 250
   :alt: noVNC-menu

IMPORTANT!! Do not disconnect from the top right corner, as in a physical machine. If you do so the machine will need to be reboot

There is a shortcut for Scipion on the desktop.

The following software is installed on the machine:

* Ubuntu 16
* Scipion on /usr/local/scipion (alias scipion): git installation branch release-1.2 with the following EM Packages:

  * Ctffind4 4.1.8
  * Gctf 1.06
  * Gautomatch 0.53
  * Eman 2.12
  * Frealing 9.07
  * Motioncor2 1.0.2
  * Motioncorr 2.1
  * Relion 2.0
  * resmap   1.1.5s2
  * Spider 21.13
  * chimera 1.10.1

* Nvidia driver version 384
* CUDA 7.5, 8.0 and 9.1 (default cuda links to 7.5).
* TurboVNC 2.1.1 on
* VirtualGL 2.5.2
* noVNC

Managing instances
====================

* Login to `AWS console <https://aws.amazon.com/>`_
* Go to EC2 services
* Select Instances on the left side menu
* Select the instance and either click on ‘Actions’ or Right-click on the instance and select Instance State and the action required.

  * Stop: the instance is turned off, but everything related to it is kept (IP address change unless you use Elastic IPs). You can power it on again with the Start command. While an instance is off, you are only charged for disk use.
  * Terminate: the instance is deleted, and all non-permanent storage dissappear. You should make sure all your data is safe before terminating an instance.
  * Change instance type: This can be useful when running EM workflows since one could start with a small machine for the preprocessing steps, or even with a GPU machine if needed, and then switch to a more powerful machine with higher memory for the classification and refinement steps. In order to change the type the VM needs to be stopped first, then click on "Options" and select "Instance settings / Change instance type".

Using external EBS volumes
==========================

ScipionCloud image has a default disk of 30 Gb, which is clearly insufficient for storing real processing EM data.
When creating a Virtual Machine through the EC2 console, it is possible to specify a bigger disk for the VM, but you have to take into account that this disk cannot be resized and will disappear when the VM is terminated.
To avoid this problem it is a good practise to work with external EBS volumes attached to the VM, which can be used to store data and/or Scipion projects.

For a single instance of Scipion you can attach an EBS volume when creating the Virtual Machine from the EC2 console as explained on the section above.

Then log in the machine and follow these instructions:

* If the EBS volume has not been formatted run (assuming your EBS volume is attached on /dev/sdf device):

.. code-block:: bash

    sudo mkfs -t ext4 /dev/xvdf`

* Mount the EBS disk

There is a /data folder where you could mount the disk but it is up to you to decide the mounting point.

.. code-block:: bash

    sudo mount /dev/xvdf /data`

You could also create the EBS volume once the VM is up and running and attach it.
Go to the EC2 console and click on Elastic Block Store / Volumes, select Create Volume and choose size and the same Availability region where the VM is running.
Once the volume is created select it and choose Attach Volume action. Select the VM to which the volume will be attached and device (for instance /dev/sdf).

Then we can proceed with the same instructions as explained above.

Costs on AWS
============
_The following prices are valid on April 2018 on the AWS Ireland region and are tax free._

Using ScipionCloud on AWS will have the following costs:

Computing (instances)
----------------------
Current processing is normally done using GPUs so we present here prices for GPU instance types on AWS.

AWS have different families of GPU instance types (P2, P3 and G3) which features and prices are shown below:

.. figure:: https://github.com/I2PC/scipion/wiki/images/cloud/AWS-P2-prices.jpg
   :align: center
   :width: 500
   :alt: AWS - P2 types

.. figure:: https://github.com/I2PC/scipion/wiki/images/cloud/AWS-G3-prices.jpg
   :align: center
   :width: 500
   :alt: AWS - G3 types

ScipionCloud has been extensively tested on P2 instances. G3 instances are
optimized for graphics but its features and compute capability allow them also
to be used to process with Scipion.

AWS EC2 allows to change type of an existing instance (it should be stopped first).
This can be used to choose the best type for each step of the processing
workflow although it should be carefully evaluated if the time waisted doing
this compensate the performance gained on the step. For instance, if a GPU
type is needed for `movie alignment` and then for `classification`,
`CTF estimation` and `automatic picking` could be done on a non GPU machine to
save some money, but it might not be worth the trouble to do it. However,
`manual picking` which could be a tedious and long task could be done on a less
powerful (and cheaper) machine, or even locally.

Storage
-------
As described above on the `Using external EBS volumes` section, it is recommended
to attach an EBS volume big enough to store raw data and project.

EBS storage costs 0.11$ per GB which makes around 113$ per TB per month.

If the amount of movies to be processed require many TBs there are some
strategies to reduce the bill:

* Process movies locally and transfer only micrographs to the cloud
* Transfer movies to a big EBS but as soon as they are aligned use a smaller EBS disk to continue processing (you could even have two disks, one for raw data and one for project and discard the first one when movies are aligned). You then should be certain that movies will not be required afterwards or you will have to transfer them again (it could compensate anyway if they are needed only at the end of processing). Another possibility will be to move movies from EBS to S3 or Glacier (another cheaper storage on AWS) while you do not need them and retrieve them if needed again.
* Process on streaming: use Scipion streaming mode to process movies as they are transferred. You should take care of removing movies from disk as they are processed since Scipion will not do it.

Transfer data
-------------
AWS does not charge for uploading data into the cloud but it does for downloading
data from it.
First GB per month is free but then it costs 0.09$ per GB (up to 10 TB,
then price slowly decrease).

For a more detailed evaluation of costs and performance you could have a look at
paper [ScipionCloud: An integrative and interactive gateway for large scale
cryo electron microscopy image processing on commercial and academic clouds.](https://doi.org/10.1016/j.jsb.2017.06.004)

`[HPC clusters] <https://github.com/I2PC/scipion/wiki/Scipion-HPC-clusters-on-AWS>`_
-------------------------------------------------------------------------------------