.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _how-to-install:

====================
Getting Scipion v2.0
====================

Scipion can be installed using either from **Binaries** or from **Sources**.
From **Binaries**, all the code is precompiled and it is ready to be used as
soon as it is downloaded. Only some dependencies and some configuration must be set.
On the other hand, we also release the Scipion's **Source** code to allow developers
going inside Scipion and, also, for those users that are not able to launch Scipion
from Binaries. Sources is usually more wide compatible than Binaries.
However, Sources compilation might be in some cases a little tricky.

In addition, you can install Scipion anywhere, as long as you have write
permissions. If you want to share Scipion installation among different users
you can use ``/usr/local`` or a similar path.
If it is only for you, you can use your home directory as well.

    **NOTE**: Learn how to `install previous Scipion versions
    <https://github.com/I2PC/scipion/wiki/How-to-Install>`_.

From Binaries
=============

Go to the directory where you want to install Scipion and download it from
`Scipion Download Page <http://scipion.i2pc.es/download_form/>`_. Select
``V2.0-Ubuntu 64bits`` or ``V2.0-CentOS 64bits`` (depending on your OS).
When the download is completed, you should have a compressed file like
``scipion_v2.0_2019-04-23_linux64_Ubuntu.tgz``. Move that file to the
installation directory and decompress it using *tar*:

.. code-block:: bash

    tar scipion_v2.0_2019-04-23_linux64_Ubuntu.tgz

After Scipion software structure is deployed in the *scipion* directory
(see the *pyworkflow*, *software* among other dirs and files), all is ready to
`continue with the installation <install-from-sources#step-2-dependencies>`_.

From Sources
============

Scipion from Sources can be gotten either downloading the **Sources Bundle** or
cloning the Scipion's **GitHub repository**. If you intend to develop Scipion we
strongly recommend to clone the **GitHub repository** in order to be able to
commit your bug fixings and improvements. Alternatively, if you only want to
use Scipion, go for the **Sources Bundle**.

Sources Bundle
--------------

Go to the directory where you want to install Scipion, and download it from
`Scipion Download Page <http://scipion.i2pc.es/download_form/>`_ (select
``V2.0-Source code``). When the download is completed, you should have a
compressed file like ``scipion_v2.0_2019-04-23_source.tgz``. Move that file
to the installation directory and decompress using *tar*:

.. code-block:: bash

    tar scipion_v2.0_2019-04-23_source.tgz

After Scipion software structure is deployed under the *scipion* directory
(see the *pyworkflow*, *software* among other files), all is ready to
`continue with the installation <install-from-sources#step-2-dependencies>`_.

Cloning the Scipion's repository
--------------------------------

Go to the directory where you want to install Scipion and, clone Scipion
repository (install **git** if not present in your system):

::

    git clone https://github.com/I2PC/scipion.git
    cd scipion
    git checkout release-2.0.0

Git will create a *scipion* directory under your current path. Therefore, you do
not need to create it manually.

After Scipion software structure is deployed under the *scipion* directory
(see the *pyworkflow*, *software* among other files), all is ready to
`continue with the installation <install-from-sources#step-2-dependencies>`_.
