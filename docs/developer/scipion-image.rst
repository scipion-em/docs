.. _scipion-image:

====================
Scipion image
====================

How to prepare a 'Scipion image'
================================

In short, you need the OS (Debian/Ubuntu), the libraries, Scipion itself, and
the extra features

Preliminary considerations
--------------------------

Disk space: one wants an image small enough to be manageable, while having space
enough for installing everything (excluding user data). Therefore, we recommend a 2 virtual disk setup: the system image (root disk) with 16 GB and the data disk (with enough disk space for all user data)

Note that the data disk will not be always available, so you can not include it
in /etc/fstab "as is". See example below.

Example: setup disk /dev/vdc as data

.. code-block:: bash

    mkfs -t ext4 /dev/vdc
    # Add it as "not automounted" filesystem at /data
    /dev/vdc       /data   ext4    defaults,noauto 0 0
    mount /data
    # "Automount": add next line to crontab
    @reboot sudo mount /data

User accounts: cloud images typically include a standard user account (ubuntu,
cloudadm...) with sudo privileges. In most scenarios (single user without strict
authorization requirements) it is enough with that account.

Operating system
----------------

We recommend Debian/Ubuntu, although you may use any Linux. You can start with
one of the Ubuntu images available in cloud environments. You can also install
your own Ubuntu (for example, when preparing a Virtualbox image)

Libraries
----------

See "`How to install: step 3 <https://scipion-em.github.io/docs/docs/scipion-modes/install-from-sources.html>`_" for a list of the packages you will need.

GPU
~~~~

If you foresee that the end user will have access to a GPU when using the image,
then you should `prepare all the GPU-related stuff <enable-gpu-in-scipion>`_.

Scipion
----------

Proceed with a Scipion installation at /usr/local from GitHub:

.. code-block:: bash

    # we asume you run these commands with the standard account
    cd /usr/local
    sudo mkdir scipion
    sudo chown ${USER} scipion
    git clone https://github.com/I2PC/scipion.git
    cd scipion
    ./scipion config

    # (Optional) GPU features require manual change in config/scipion.conf:
    CUDA = True

    ./scipion install -j 4


(see link:How-to-Install[How to install])

EM packages
~~~~~~~~~~~

We recommend the preinstallation of the following packages (since they are the most popular among users):

.. code-block:: bash

    ./scipion install -j 4  chimera ctffind4 eman2.12 frealign motioncorr relion-1.4 resmap spider

Postinstall
~~~~~~~~~~~
Free some system disk space by removing temporary files:

.. code-block:: bash

    rm -rf /usr/local/scipion/software/tmp/* /usr/local/scipion/software/em/*.tgz

Nice extras
------------
Usually, the VM is far away from the client computer (typically, in the cloud). Therefore, one needs some solution to enjoy low latency remote graphics display ("remote desktop").

Additionally, is pretty uncommon that the VM has a GPU for rendering. Therefore, one needs some solution to use OpenGL applications (like chimera or boxer) without graphics card ("software rendering")

The data disk is available after the image is created. Therefore, one needs some solution that allows the end user to have access to that disk easily.

Remote desktop
~~~~~~~~~~~~~~
We recommend Guacamole. Installing Guacamole with `Portable Services <https://github.com/tranquilinho/ps-scripts>`_  is very easy - just follow `guacamole recipe <https://github.com/tranquilinho/ps-scripts/blob/master/recipes/guacamole>`_:

.. code-block:: bash

    mkdir -p /services/guacamole
    cd /services/guacamole/
    git clone https://github.com/tranquilinho/ps-scripts.git scripts
    /services/guacamole/scripts/recipes/guacamole

By default, guacamole service listens to port 8080. If you want to use other port (like 80), update the port number in /services/guacamole/etc/apache2/service.conf:

.. code-block:: bash

    Listen 80
    <VirtualHost *:80>

By default, guacamole service keeps the guacamole password and does not start
VNC session :1 automatically. You can modify this behavior
in /services/guacamole/etc/service.cfg:

.. code-block:: bash

    readonly guacamole_keep_pass=0
    readonly vnc_on_demand=0
    # if vnc_on_demand is 0, the first time you start the service you will be asked
    # the VNC server password.
    # you can specify what user will run VNC server (default: "ubuntu"):
    readonly vnc_user=scipion

Check guacamole config, /services/guacamole/etc/guacamole/user-mapping.xml:

* Check that the VNC server password is properly set
* Set up guacamole user and password

On boot, these services must be started: guacamole server (guacd), tomcat,
apache, VNC. With `Portable Services <https://github.com/tranquilinho/ps-scripts>`_, it is very easy: just run service-manager start (add it to /etc/init.d)

If you experience problems with autocomplete (using XFCE desktop), in the
file `~/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-keyboard-shortcuts.xml` change the line

.. code-block:: bash

      <property name="&lt;Super&gt;Tab" type="string" value="switch_window_key"/>


to...

.. code-block:: bash

      <property name="&lt;Super&gt;Tab" type="string" value="empty"/>


Software rendering
~~~~~~~~~~~~~~~~~~

We recommend `Mesa <http://www.mesa3d.org/>`_. You can reuse the Portable Services at /services/guacamole to install Mesa easily:

.. code-block:: bash

    /services/guacamole/scripts/build/mesa

Once you have Mesa installed, you need to include it in LD_LIBRARY_PATH (for example, in /etc/bash.bashrc):

.. code-block:: bash

    export LD_LIBRARY_PATH=/services/guacamole/usr/mesa/lib

Cleaning up
~~~~~~~~~~~

Remove history

.. code-block:: bash

    rm -rf ~/.bash_history
    history -c

Snapshots
----------
From the working image, you can take a snapshot anytime. In Amazon, these snapshots are the base for creating the final image (AMI)

Publishing
-----------
Once the image is finished, the user should be able to download it.

In cloud scenarios, there are "image repositories".

Amazon: register the AMI.

FedCloud.

For Virtualbox, just copy the ova file to Scipion web server.