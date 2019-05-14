.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _Scipion-demo-for-the-course-of-International-School-of-Crystallography:

===========================================================================
Scipion demo for the course of International School of Crystallography
===========================================================================

Here you can find the instructions to set up your machine to be able to follow the Scipion tutorial session.

There will be two options to follow up the tutorial session:

1. To set up your own Scipion machine using VirtualBox:
   A VirtualBox virtual appliance, that you could easily launch from your own
   computer using `[Oracle VirtualBox] <https://www.virtualbox.org/wiki/Downloads>`_
   application, is ready to be downloaded from `[here] <http://scipion.cnb.csic.es/downloads/vm/Scipion_ICS_ubuntu16_40.vdi>`_. Then follow the next steps:

    1.1. Create a new Virtual Machine (Type Linux and Version Ubuntu).

    1.2. Assign at least 6 GB memory and 4 CPUs (Settings > System > Motherboard/Processor).

    1.3. Choose as existing hard disk the virtual appliance downloaded (vdi).

    1.4. Create.

    1.5. Start it and login with user scipion and password scipionICS.
    By default the virtual machine screen is quite small, to resize it open a terminal and type
    xrandr -q and choose the resolution that fits better your laptop screen and
    then set it up with xrandr -s wxh (e.g. 1280x1024) or by Start > Preferences > Monitor Settings.

You can open Scipion by clicking on the desktop shortcut. There are two demo
projects that you can visualize prior to the session (you could try to run some
steps yourself but processing might be slow since number of cores and RAM are
virtualized and not very high and GPU is not present). Raw movies are not present
either to save some disk space.
Project ScipionCombined shows a representative workflow where many of the Scipion
possibilities are shown while project Acquisition_Simulation presents a finished
workflow of `the Acquisition Demo <https://github.com/I2PC/scipion/wiki/Acquisition-simulation-project-for-the-ISC-course>`_.

2. To use a virtual machine on Amazon cloud (AWS):
   A number of AWS instances will be ready during the session to be used by the students. Connections details will be given at that time, and the only required software will be a web browser and a reasonable internet connection.