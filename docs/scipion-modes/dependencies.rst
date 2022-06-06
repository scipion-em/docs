.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _dependencies:

=========================
Dependencies
=========================


-  For ubuntu 16:

::

    sudo apt-get install gcc-5 g++-5 cmake openjdk-8-jdk libxft-dev libssl-dev libxext-dev libxml2-dev\
     libreadline6 libquadmath0 libxslt1-dev libopenmpi-dev openmpi-bin  libxss-dev libgsl0-dev libx11-dev\
     gfortran libfreetype6-dev scons libfftw3-dev libopencv-dev curl git libbz2-dev

-  For ubuntu 18:

::

    sudo apt-get install gcc-5 g++-5 cmake openjdk-8-jdk libxft-dev libssl-dev libxext-dev\
     libxml2-dev libreadline7 libquadmath0 libxslt1-dev libopenmpi-dev openmpi-bin\
     libxss-dev libgsl0-dev libx11-dev gfortran libfreetype6-dev scons libfftw3-dev libopencv-dev curl git

-  For debian 9.7:

::

    sudo apt-get install gcc-5 g++-5 cmake openjdk-8-jdk libxft-dev libssl-dev libxext-dev\
     libxml2-dev libreadline7 libquadmath0 libxslt1-dev libopenmpi-dev openmpi-bin\
     libxss-dev libgsl-dev libx11-dev gfortran libfreetype6-dev scons libfftw3-dev libopencv-dev curl git

- For OpenSUSE 42.3

::

   sudo zypper in gcc-c++ gcc5 gcc5-c++ cmake java-1_8_0-openjdk-devel libXft-devel-32bit openssl-devel\
    libXext-devel-32bit libxml2-devel-32bit libreadline6 libquadmath0 libxslt1 openmpi-devel libXss1\
    libX11-devel-32bit libgfortran4 gcc-fortran libfreetype6 scons libfftw3-3 fftw3-devel libfftw3_threads3\
    libopencv3_1 opencv-devel curl git

Note: We have observed that libjbig.so.0 is not found in OpenSUSE42.3. However, OpenSUSE42.3 contains libjbig.so.2 and it is also valid. Therefore, please link one to the other by

::

 sudo ln -s /usr/lib64/libjbig.so.2 /usr/lib64/libjbig.so.0

- For OpenSUSE 15.0

::

 sudo zypper in gcc-c++ cmake java-1_8_0-openjdk-devel libXft-devel-32bit openssl-devel\
    libXext-devel-32bit libxml2-devel-32bit libreadline6 libquadmath0 libxslt1 openmpi-devel\
    libXss1 libX11-devel-32bit libgfortran4 gcc-fortran libfreetype6 scons libfftw3-3\
    fftw3-devel libfftw3_threads3 libopencv3_3 curl git

- Fedora

::

  yum install gcc gcc-g++ cmake java-1.8.0-openjdk-devel.x86_64 libXft-devel.x86_64\
   openssl-devel.x86_64 libXext-devel.x86_64  libxml++.x86_64 libquadmath-devel.x86_64\
   libxslt.x86_64 openmpi-devel.x86_64  gsl-devel.x86_64  libX11.x86_64  gcc-gfortran.x86_64 git

Note: Use **dnf install** instead of **yum** if your Fedora is recent

- For Centos 6 and Centos 7

::

   sudo yum install gcc gcc-c++ cmake java-1.8.0-openjdk-devel libXft-devel openssl-devel libXext-devel\
    libxml2-devel readline-devel libquadmath libxslt-devel openmpi-devel libX11-devel libgfortran\
    freetype-devel scons fftw-devel opencv-devel curl centos-release-scl devtoolset-4 python27 git

 Note: To be able to run python 2.7 (Scipion requirement), run ``scl enable python27 bash``.


-  **Note 2** - CUDA recommendations:

The following table contains the current compatibility of the plugins
that use CUDA and have some restrictions with the CUDA versions. To
maximize compatibility with all plugins we recommend to install
**CUDA-10.1**, but it's up to you to choose a different version depending
on the plugins you'd like to use (depending on this you might not need
CUDA at all).

+------------------------+------------+------------+------------+------------+------------+------------+
| Cuda version ->        |     8.0    |     9.0    |     9.1    |     9.2    |    10.1    |    10.2    |
+========================+============+============+============+============+============+============+
| motioncor2  (1.3.2)    |      X     |            |            |      X     |      X     |      X     |
+------------------------+------------+------------+------------+------------+------------+------------+
| gctf (1.18)            |      X     |      X     |      X     |            |      X     |            |
+------------------------+------------+------------+------------+------------+------------+------------+
| gautomatch (0.56)      |      X     |            |            |            |      X     |            |
+------------------------+------------+------------+------------+------------+------------+------------+

