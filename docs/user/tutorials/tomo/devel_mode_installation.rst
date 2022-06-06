.. include:: <isonum.txt>
.. |icon| image:: /docs/user/tutorials/tomo/Picking_tutorial/Toggle_icon.png
.. |results| image:: /docs/user/tutorials/tomo/Picking_tutorial/Analyze_results.png
.. |wizard| image:: /docs/user/tutorials/tomo/Picking_tutorial/Wizard.png

.. figure:: /docs/user/tutorials/tomo/Picking_tutorial/Scipion_tomo.gif
   :width: 100
   :align: right
   :alt: scipion tomo logo

.. _devel_mode_installation:

====================================================
Installation of Scipion for Tomography in devel mode
====================================================

This guide describes the steps to be followed to install Scipion Tomography and its plugins in development mode. The guide includes a link to the GitHub webpage of the currently available plugins with a more detailed description of their own installation. Note that here the general installation devel installation procedure of a plugin will be addressed, although some plugins might require some extra steps that could be checked on their GitHub webpage.

Joining the Scipion Slack channels
==================================

If you are working in development mode, we strongly suggest joining the Slack channels to get information about the last updates of the plugins. Access to the Slack channel can be requested through the Scipion mailing list:

Installation of scipion-em-tomo plugin
======================================

The first plugin to be installed is scipion-em-tomo. The main role of this plugin is to act as the core for the other Scipion Tomography plugins, as it provides the basic abstractions, methods, and actions that the other plugins will need to communicate and work inside the Scipion framework.

The Github webpage of scipion-em-tomo is available `here <https://github.com/scipion-em/scipion-em-tomo>`_. All the details regarding its installation can be found in their `GitHub documentation <https://github.com/scipion-em/scipion-em-tomo/blob/devel/README.md>`_. We described below the steps to successfully install the plugin

1. Pre-requisites
------------------------------------------------------------------------

* Use scipion v3.0.x
* Use scipion-em-tomo from branch 'tomo'. This is the default branch in the Github webpage, so it will be downloaded unless you change it manually

2. GitHub cloning
------------------------------------------------------------------------

* Using the command line, go to the folder where you would like to download the scipion-em-tomo plugin and run::
    git clone https://github.com/scipion-em/scipion-em-tomo.git

* In the same folder you have executed the previous command, run in the command line::
    scipion installp -p ~/scipion-em-tomo --devel

The previous command will automatically install and configure the plugin inside Scipion in devel mode so it can be used within the Scipion framework

3. Updating a plugin installed in development mode
------------------------------------------------------------------------

Any plugin installed in devel mode should be updated manually through the command line. The following steps describe the steps to be followed:

* Using the terminal, go to the folder where you installed your plugin::
    Example: cd /path/to/your/plugin/folder/scipion-em-tomo

* Once you are inside the folder of the plugin to be updated, run::
    git pull

After executing the previous command, you will be up to date with the latest development version of the plugin. Note that there is no need to install the plugin again, all the new changes will be recognized automatically inside Scipion. In case the changes require a reinstallation of the binaries or the plugin, it will be announced through the main Slack channels.

4. List of Tomography plugins for Scipion
------------------------------------------------------------------------

We provide below the list of Tomography plugins available in Scipion toghether with the link to their Github documentation webpage. It is advisable to check the documentation of the plugin before its installation in case any extra steps need to be followed apart from those described in the example.

* `scipion-em-tomo <https://github.com/scipion-em/scipion-em-imod>`__ (Github documentation available `here <https://github.com/scipion-em/scipion-em-imod/blob/devel/README.md>`__)
* `scipion-em-imod <https://github.com/scipion-em/scipion-em-imod>`__ (Github documentation available `here <https://github.com/scipion-em/scipion-em-imod/blob/devel/README.md>`__)
* `scipion-em-gctf <https://github.com/scipion-em/scipion-em-gctf>`__ (Github documentation available `here <https://github.com/scipion-em/scipion-em-gctf/blob/master/README.rst>`__)
* `scipion-em-tomo3d <https://github.com/scipion-em/scipion-em-tomo3d>`__ (Github documentation available `here <https://github.com/scipion-em/scipion-em-tomo3d/blob/devel/README.rst>`__)
* `scipion-em-tomoviz <https://github.com/scipion-em/scipion-em-tomoviz>`__ (Github documentation available `here <https://github.com/scipion-em/scipion-em-tomoviz/blob/devel/README.rst>`__)
* `scipion-em-pyseg <https://github.com/scipion-em/scipion-em-pyseg>`__ (Github documentation available `here <https://github.com/scipion-em/scipion-em-pyseg/blob/devel/README.rst>`__)
* `scipion-em-tomosegmemtv <https://github.com/scipion-em/scipion-em-tomosegmemtv>`__ (Github documentation available `here <https://github.com/scipion-em/scipion-em-tomosegmemtv/blob/devel/README.rst>`__)
* `scipion-em-aretomo <https://github.com/scipion-em/scipion-em-aretomo>`__ (Github documentation available `here <https://github.com/scipion-em/scipion-em-aretomo/blob/master/README.rst>`__)
* `scipion-em-emantomo <https://github.com/scipion-em/scipion-em-emantomo>`__ (Github documentation available `here <https://github.com/scipion-em/scipion-em-emantomo/blob/devel/README.rst>`__)
* `scipion-em-dynamo <https://github.com/scipion-em/scipion-em-dynamo>`__ (Github documentation available `here <https://github.com/scipion-em/scipion-em-dynamo/blob/devel/README.rst>`__)
* `scipion-em-reliontomo <https://github.com/scipion-em/scipion-em-reliontomo>`__ (Github documentation available `here <https://github.com/scipion-em/scipion-em-reliontomo/blob/devel/README.rst>`__)
* `scipion-em-deepfinder <https://github.com/scipion-em/scipion-em-deepfinder>`__ (Github documentation available `here <https://github.com/scipion-em/scipion-em-deepfinder/blob/master/README.rst>`__)
* `scipion-em-novactf <https://github.com/scipion-em/scipion-em-novactf>`__ (Github documentation available `here <https://github.com/scipion-em/scipion-em-novactf/blob/devel/README.rst>`__)
* `scipion-em-xmipptomo <https://github.com/I2PC/scipion-em-xmipptomo>`__ (Github documentation available `here <https://github.com/I2PC/scipion-em-xmipptomo/blob/devel/README.rst>`__)
* `scipion-em-cryocare <https://github.com/scipion-em/scipion-em-cryocare>`__ (Github documentation available `here <https://github.com/scipion-em/scipion-em-cryocare/blob/devel/README.rst>`__)
* `scipion-em-cistem <https://github.com/scipion-em/scipion-em-cistem>`__ (Github documentation available `here <https://github.com/scipion-em/scipion-em-cryocare/blob/devel/README.rst>`__)
* `scipion-em-emclarity <https://github.com/scipion-em/scipion-em-emclarity>`__ (Github documentation available `here <https://github.com/scipion-em/scipion-em-emclarity/blob/devel/README.rst>`__ - *Under development, not ready for testing*)
* `scipion-em-novaSTA <https://github.com/scipion-em/scipion-em-novaSTA>`__ (Github documentation available `here <https://github.com/scipion-em/scipion-em-novaSTA/blob/main/README.md>`__ - *Under development, not ready for testing*)
* `scipion-em-tomoj <https://github.com/scipion-em/scipion-em-tomoj>`__ (Github documentation available `here <https://github.com/scipion-em/scipion-em-tomoj/blob/master/README.rst>`__ - *Under development, not ready for testing*)
