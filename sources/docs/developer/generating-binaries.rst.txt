.. _generating-binaries:

=====================
Generating Binaries
=====================

For a new Scipion release we generate a "binary" version (a Scipion installation
that can be moved as a whole and work in basically any machine without
recompiling). The main difference is the ``--binary`` flag when installing from a
fresh download, that will later change the RPATH of the binaries.

In order to get the maximum libc compatibility, it is recommended to
generate the binary package in a computer running an old Linux. One
option is a Centos-6.5 virtual machine (see below for details).

The following steps summarize how to generate the binaries in a Centos_64
virtual machine.


Getting ready: tagging release in git
=====================================

*In your local system*, move to the branch from where the bundle will be done
(usually the master branch).

.. code-block::
    cd scipion
    git checkout <branch name>

Ensure that https://github.com/I2PC/scipion/blob/bd81c8c3b3fb9ce30546b1e8835c3b543f130553/scipion#L43[Version, NickName and DateRelase] variables are updated in the scipion script

.. code-block::
    more scipion

Make a git tag to the last commit in that branch

.. code-block::
    git tag v1.2


replace ``v1.2`` for the right version number.


Accessing the Virtual machine
=============================

We have set up a Centos 6.5 virtual machine to generate the Scipion bundles.
This VM is on heisenberg (user scipion) and the following commands are useful to
manage it:

* List existing VMs
.. code-block::
    VBoxManage list vms

(machine is called "CentOS_64")

List running vms
=================

.. code-block::
    VBoxManage list runningvms


if CentOS_64 is not listed, then

Start the VM
============

.. code-block::
    VBoxHeadless -startvm "CentOS_64" &


Access the VM from heisenberg
=============================

Wait a bit till it starts and then access via ssh

.. code-block::
    ssh -p 2222 xmipp@127.0.0.1

(pass: 'V1rtu4l.')

* Stop VM

It is recommended to stop the VM once bundles are done and copied out of the machine.
----
VBoxManage controlvm CentOS_64 poweroff
----


== Bundle creation

Once in the machine where we will do the bundle (see above to log in CentOS_64).

We must get the repository. For generating the binaries we do not need the whole repository history (option `--depth 1`).
----
git clone --depth 1 https://github.com/I2PC/scipion.git
----

* Moving to a certain branch (not for normal bundles)

If you want to make a bundle from a certain branch (e.g. to make a beta), you need to do instead:
----
git clone --depth 1 https://github.com/I2PC/scipion.git -b branch-name
----

* Generate the Source zipped tar
----
python scipion/pyworkflow/install/tar.py source
----

This script will create the zipped tar file skipping temporary files and build artifacts.
The script should print the tar command used:

----
 tar czf scipion_devel__source.tgz \
--exclude=.git --exclude='*.o' --exclude='*.os' --exclude='*pyc' \
--exclude='*.mrc' --exclude='*.stk' --exclude='*.gz'  \
--exclude='software/tmp/*' --exclude='*.scons*' --exclude='config/*.conf' scipion
----

* Create a Basic Installation
----
cd scipion
./scipion config
./scipion install --binary -j 5
cd ..
python scipion/pyworkflow/install//tar.py linux64
----

In this CentOS machine the `./scipion config` should complain about the MPI variables.
You will need to correct with mpi directories. For example:

----
MPI_BINDIR = /usr/lib64/openmpi-1.10/bin
MPI_LIBDIR = /usr/lib64/openmpi-1.10/lib
MPI_INCLUDE = /usr/include/openmpi-1.10-x86_64
----


* Install other EM packages (not for normal bundles)

----
cd scipion
./scipion install --no-xmipp --binary -j 5 relion-1.4
./scipion install --no-xmipp bsoft-1.9.0 chimera ctffind ctffind4 dogpicker eman2.11 frealign motioncorr resmap spider summovie unblur
cd ..
python scipion/scripts/tar.py linux64-em-packages
----



Now, two file are in the home directory `scipion_<version>_<date>_source.tgz` and `scipion_<version>_<date>_linux-64.tgz`. The first is the source package of the software, whereas the second is the precompilated binaries package.
