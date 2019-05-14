.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _install-from-binaries:

===========================================
How to Install Scipion v2.0 using binaries
===========================================


Installing Scipion v2.0 in 3 Steps
==========================================

Step 1: Download
-----------------
You can install Scipion anywhere, as long as you have write permissions. If you
want to share Scipion installation among different users you can use ``/usr/local``
or a similar path. If it is only for you, you can use your home directory as well.

Go to the directory where you want to install Scipion, and download it:

Go to `Scipion Download Page <http://scipion.i2pc.es/download_form/>`_, select
precompiled binaries and fill the download form (this information is only used
for download statistics). When the download is completed, you should have a
compressed file like ``scipion_v2.0_2019-04-23_linux64_Ubuntu.tgz`` or
``scipion_v2.0_2019-04-23_linux64_CentOS7.tgz`` depend of the operating system
that you have. Move that file to the installation directory and decompress
using *tar*:

.. code-block:: bash

    tar scipion_v2.0_2019-04-23_linux64_Ubuntu.tgz


Step 2: Dependencies
---------------------

If you have download the Scipion binary version, you only need to install some
dependencies (this example is for Ubuntu16). See for
`Installing Dependencies <https://scipion-em.github.io/docs/release-2.0.0/docs/scipion-modes/install-from-sources#step-2-dependencies>`_):

.. code-block:: bash

     sudo apt-get install gcc-5 g++-5 cmake openjdk-8-jdk libxft-dev libssl-dev libxext-dev libxml2-dev\
     libreadline6 libquadmath0 libxslt1-dev libopenmpi-dev openmpi-bin  libxss-dev libgsl0-dev libx11-dev\
     gfortran libfreetype6-dev scons libfftw3-dev libopencv-dev curl git


Step3: Configure and Install
----------------------------

After installing the dependencies, you can proceed to `generate configuration files <https://scipion-em.github.io/docs/release-2.0.0/docs/scipion-modes/install-from-sources#step-3-configure-and-install>`_.


