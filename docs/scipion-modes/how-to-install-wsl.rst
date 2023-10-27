.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _how-to-install-wsl:

====================================================
Installing Scipion on Windows System for Linux (WSL)
====================================================

Scipion can directly work on Windows, since it is pure Python. However, Xmipp and many
other software plugins are not available for Windows. Therefore, we recommend to install
it on a Linux system. If you have Windows 10, you can install Scipion on the
Windows Subsystem for Linux (WSL). This is a Linux environment that runs on top of Windows.
We have check that almost all Scipion functionality and plugins performance is preserved
when running on WSL, even for GPU-accelerated protocols.

Installing WSL
==============

Installing WSL is very easy. Just follow the instructions in the
`Microsoft documentation <https://learn.microsoft.com/en-us/windows/wsl/install>`_.
The only thing you need to decide is which Linux distribution to install.
We recommend Ubuntu 20.04 LTS. So, open a PowerShell console and run:

.. code-block:: powershell

    wsl --install -d Ubuntu-20.04    # installs Ubuntu 20.04 LTS
    wsl -l -v                        # lists installed distributions and shows WSL version

check that Ubuntu 20.04 is there and Version is 2.

WSL do not freeze resources prior to need them. This means that real memory used is
exactly the memory currently running by the apps, so you can directly check it with
``wsl free -h`` as `used`).
However, WSL limits the total memory that can be used by Linux to half of the total and all
CPU cores. If you want to increase this limit you can edit the file
**``$HOME/.wslconfig``** and add the following lines:  (probably this file do not exist

.. code-block:: text

    [wsl2]
    #Limits VM memory can be set as whole numbers using GB or MB
    memory=30GB    # Limits VM memory in WSL 2 to 30 GB
    #processors=8  # We do not recommend to limit the number of processors

We recommend to leave the number of processors unlimited, since WSL manages them very well.
However, we recommend to leave some memory for Windows (let's say 2GB of 32GB),
in order to prevent Windows from freezing in a peak memory.

Restart WSL and check that the memory limit is set:

.. code-block:: powershell

    wsl --shutdown
    wsl free -h

It is also interesting to update the Linux distribution. For Ubuntu 20.04, run:

.. code-block:: powershell

    cd $HOME
    wsl  # opens a Linux console

    # from here, you are in a Linux console
    sudo apt update
    sudo apt upgrade

    # Let's store the Windows HOME path in a variable
    echo "export HOME_WIN=$(pwd)" >> ~/.bashrc

    exit  # exits the Linux console and returns to PowerShell

Notice that Windows home is somewhere like ``/mnt/c/Users/<your-win-user>``.
We store this path in a the enviromental variable `HOME_WIN` in order to be able to
use it later.

Also `check this basics commands<https://learn.microsoft.com/en-us/windows/wsl/basic-commands>`_
to get familiar with WSL.

CUDA in WSL
===========

Using CUDA (for developing and for running GPU-accelerated protocols) in WSL is
totally supported by Microsoft and Nvidia
(`check this <https://learn.microsoft.com/en-us/windows/ai/directml/gpu-cuda-in-wsl>`_).

The main point to understand is that Nvidia drivers are not installed in WSL,
but in Windows, and Linux see them in ``/lib/wsl/drivers/``. Same for some CUDA libs,
they are in ``/lib/wsl/lib/``.
So, you need to install Nvidia drivers and CUDA on Windows, and then install CUDA toolkit in WSL.
This is deeply explained in the `this Nvidia documentation
<https://docs.nvidia.com/cuda/wsl-user-guide/index.html#getting-started-with-cuda-on-wsl-2>`_.

Basically, you need to install the latest Nvidia drivers for your GPU in Windows
(if not already installed): `Nvidia drivers <https://www.nvidia.com/Download/index.aspx>`_.

Once a Windows NVIDIA GPU driver is installed on the system, CUDA becomes available within WSL 2.
The CUDA driver installed on Windows host will be stubbed inside the WSL 2 as libcuda.so,
therefore **users must not install any NVIDIA GPU Linux driver within WSL 2.**
One has to be very careful here as the default CUDA Toolkit comes packaged with a driver,
and it is easy to overwrite the WSL 2 NVIDIA driver with the default installation.
We recommend developers to use a separate CUDA Toolkit for WSL 2 (Ubuntu)
available from the CUDA Toolkit Downloads page to avoid this overwriting.

First, remove the old GPG key in the Linux bash console

.. code-block:: powershell

    wsl  # opens a Linux console

    # from here, you are in a Linux console
    sudo apt-key del 7fa2af80

Even though you can install the latest CUDA toolkit, we recommend to install CUDA 11.
So, you can install the CUDA toolkit in Ubuntu 20.04 by finding the WSL-Ubuntu
recipe in the `CUDA Toolkit Downloads page
<https://developer.nvidia.com/cuda-11-8-0-download-archive?target_os=Linux&target_arch=x86_64&Distribution=WSL-Ubuntu&target_version=2.0&target_type=deb_local>`_
> *Linux* > *x86_64* > **WSL-Ubuntu** > *2.0* > *deb (local)*.

Then, follow the recipe there:

.. code-block:: bash

    wget https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/cuda-wsl-ubuntu.pin
    sudo mv cuda-wsl-ubuntu.pin /etc/apt/preferences.d/cuda-repository-pin-600
    wget https://developer.download.nvidia.com/compute/cuda/11.8.0/local_installers/cuda-repo-wsl-ubuntu-11-8-local_11.8.0-1_amd64.deb
    sudo dpkg -i cuda-repo-wsl-ubuntu-11-8-local_11.8.0-1_amd64.deb
    sudo cp /var/cuda-repo-wsl-ubuntu-11-8-local/cuda-*-keyring.gpg /usr/share/keyrings/
    sudo apt-get update
    sudo apt-get -y install cuda

    # check that CUDA is properly installed
    nvcc --version
    nvidia-smi

Probably, ``nvidia-smi`` is not found. This is because it is provided by Windows drivers,
so it is in ``/lib/wsl/lib/nvidia-smi``. So, you can create a link to it in ``/usr/bin``
or wherever accessible from your PATH

.. code-block:: bash

    sudo ln -s /lib/wsl/lib/nvidia-smi /usr/bin/nvidia-smi


Prerequisites
=============

The prerequisites for installing Scipion-Xmipp are the same as for any
`Ubuntu 20.04 <https://github.com/I2PC/xmipp/wiki/Installing-Xmipp-on-Ubuntu-20.04>`_ system.
Basically,

.. code-block::  bash

    sudo apt install -y gcc g++ libfftw3-dev libopenmpi-dev libhdf5-dev python3-numpy python3-pip python3-dev libtiff5-dev libsqlite3-dev default-jdk git cmake

    pip install scons numpy


Installing Scipion
==================

This should be as usual, so `folow the 1, 2 and 3 points of the installation guide
<https://scipion-em.github.io/docs/release-3.0.0/docs/scipion-modes/how-to-install.html>`_.

The, for developers, we recommend to install Scipion and Xmipp using the following command

.. code-block:: bash

    python3 -m scipioninstaller -conda -dev [-httpsClone] -sciBranch devel -xmippBranch devel $HOME_WIN/<scipion-main-folder>

notice that ``-httpsClone`` is optional if you do not have configured git to use ssh-keypairs,
``$HOME_WIN`` is the Windows home folder set in the first section of this file,
and ``<scipion-main-folder>`` is the folder where Scipion will be installed.
In this way, Scipion is in the Windows file system and then,
it is easily accessible from Windows, for example to develop code in a
IDE running directly on Windows.

Configuring Scipion
===================

As it is usual to work with Scipion also on the Windows environ (File browser, IDE, etc),
we recommend to configure Scipion to use the Windows home folder as the root folder.
This is done by editing the ``SCIPION_HOME/config/scipion.conf`` file in such a way that
the path starting with ``~`` are replaced with the ``$HOME_WIN`` variable. i.e.:

.. code-block:: text

    SCIPION_LOG = $HOME_WIN/ScipionUserData/logs/scipion.log
    SCIPION_LOGS = $HOME_WIN/ScipionUserData/logs
    SCIPION_TESTS_OUTPUT = $HOME_WIN/ScipionUserData/Tests
    SCIPION_TMP = $HOME_WIN/ScipionUserData/tmp
    SCIPION_USER_DATA = $HOME_WIN/ScipionUserData

On the other hand,
one typical issue is that Ubuntu see all CPU threads in a single core.
This is not a big deal and does not affect performance.
However, open-mpi sets the maximum slots equals to the number of cores, so just one.
Then, ``mpirun -np 8 echo "Hello world"`` will fail, for instance.
So, you need to add the ``--use-hwthread-cpus`` flag to the command,
i.e. check this now ``mpirun -n 8 --use-hwthread-cpus echo "Hello world"``.
If so, edit the ``SCIPION_HOME/config/hosts.conf`` file in such a way that second line
results in

.. code-block:: text

    PARALLEL_COMMAND = mpirun -np %_(JOB_NODES)d --use-hwthread-cpus %_(COMMAND)s

Notice that you can also use ``--oversubscribe`` flag, but it is not recommended.


Invoking Scipion from Windows
=============================

If you have a fine configuration PowerShell and you want to continue with it,
it is possible to invoke Scipion directly from Windows,
just by prefixing the Scipion launcher with the ``wsl`` wrapper, i.e.

.. code-block:: powershell

    wsl <scipion-main-folder>/scipion3

Take into account that this starts a non-interactive bash session, so ``~/.bashrc``
is not sourced. Then, if ``scipion.config`` contains something like ``$HOME_WIN``,
it will not expanded. So, you need to use the full path in this case.