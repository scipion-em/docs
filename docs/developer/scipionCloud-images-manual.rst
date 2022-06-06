.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _scipionCloud-images-manual:

==========================
ScipionCloud images manual
==========================

There are two virtual appliances that can be found in the EGI Applications Database: `ScipionCloud <https://appdb.egi.eu/store/vappliance/scipion.v1.0>`_ and `ScipionCloud-GPU <https://appdb.egi.eu/store/vappliance/scipioncloud.gpu>`_.

Remote desktop (noVNC)
----------------------
The machine can be accessed at the URL http://public-ip:8000/vnc.html using password that was set up at contextualization when creating the virtual machine. This session logs as user scipion that can run Scipion but has not admin privileges.

To login with admin privileges you need to ssh to the machine with ubuntu user and the private key related to the public key injected on the virtual machine at creation time.

To resize screen clicks on the Settings icon and choose ``Remote resizing`` as ``Scaling mode``:

.. figure:: /docs/images/cloud/noVNC-resize.png
   :alt: noVNC-resize

To disconnect from the session click on the little arrow that appears on the left (see menu below) and click on the last option:

.. figure:: /docs/images/cloud/noVNC-menu.png
   :alt: noVNC - disconnect

IMPORTANT!! Do not disconnect from the top right corner, as in a physical machine. If you do so the machine will need to be reboot

Software installed
--------------------
These images are based on Ubuntu 16.04 server and they have been built using packer with the configuration available at https://github.com/I2PC/scipion-cloud/tree/master/scipion-ubuntu-16.04.

The following software is installed on the latest version of ScipionCloud images (1.2):
### Scipion
Scipion 1.2 (from github) is installed at /opt/scipion.

There is an icon on desktop that starts scipion.

Note: In the GPU appliance the desktop shortcut start Scipion through VirtualGL, this is to make chimera work on GPU powered machines. If you want to start it from the console run ``vglrun /opt/scipion/scipion``.

EM packages
------------

  * Ctffind4 4.1.10
  * Gctf 1.06
  * Gautomatch 0.53
  * Eman 2.12
  * Frealing 9.07
  * Motioncor2 1.0.5
  * Relion 2.1
  * resmap   1.1.5s2
  * Spider 21.13
  * chimera 1.10.1

To verify installed packages type:

.. code-block:: bash

    scipion install --help

And to install latest version of a package:

.. code-block:: bash

    scipion install package-name

In GPU appliance Relion is compiled with CUDA support. Gctf and Gautomatch only work on GPU powered machines.

Others
-------
* Nvidia driver version 396
* CUDA 8.0 on /usr/local/.
* TurboVNC 2.1.1 on /opt/TurboVNC.
* VirtualGL 2.5.2 on /opt/VirtualGL.
* noVNC on /opt/noVNC.