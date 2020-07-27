.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _scipionCloud-AMI-manual:

===============================
ScipionCloud AMI manual
===============================


Remote desktop (noVNC)
----------------------

To resize screen clicks on the Settings icon and choose ``Remote resizing`` as ``Scaling mode``:

.. figure:: /docs/images/cloud/noVNC-resize.png
   :align: center
   :alt: noVNC-resize


To disconnect from the session click on the little arrow that appears on the left (see menu below) and click on the last option:

.. figure:: /docs/images/cloud/noVNC-menu.png
   :align: center
   :alt: noVNC - disconnect

IMPORTANT!! Do not disconnect from the top right corner, as in a physical machine. If you do so the machine will need to be reboot

Software installed
--------------------

The AMI is based on Ubuntu 16.04 server AMI.

The following software is installed on the machine:

Scipion
~~~~~~~~

The latest stable release of Scipion (from github) is installed at:

.. code-block:: bash

    /usr/local/scipion

There is an icon on desktop that starts scipion. There is also an alias to run it from terminal.

Note: Both alias and desktop shortcut start Scipion through VirtualGL, this is to make chimera work on GPU powered machines.

EM packages
~~~~~~~~~~~~

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

To verify installed packages type:

.. code-block:: bash

    scipion install --help

And to install latest version of a package:

.. code-block:: bash
    scipion install package-name

Relion is compiled with CUDA support.

Others
~~~~~~~~

* Nvidia driver version 387
* CUDA 7.5, 8.0 and 9.1 (default cuda links to 7.5) on /usr/local/.
* TurboVNC 2.1.1 on /opt/TurboVNC.
* VirtualGL 2.5.2 on /opt/VirtualGL.
* noVNC on /opt/noVNC.


