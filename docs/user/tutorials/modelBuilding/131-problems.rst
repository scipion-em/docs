.. _problems:

How to solve some problems that you can find during the execution of the modeling workflow
==========================================================================================

-  | command lines involving communication between *ChimeraX* and *Scipion* (*scipionwrite*, *scipionss*,
     *scipionrs* and *scipioncombine*) do not work:

   | As indicated in `FAQ <https://github.com/scipion-em/scipion-em-chimera/blob/devel/FAQ.rst>`_,
     these commands are plugins installed by the **scipion-em-chimera**
     setup. Firstly, check the right installation of the plugin just
     opening and executing the command line:

   ::

      help scipionwrite

   | If it is installed, a help page will appear. Otherwise, type in the *ChimeraX* GUI
     command line:

   ::

      devel install /path_to_scipion3_plugins/scipion-em-chimera/chimera/Bundles/scipion

   | where *path_to_scipion3_plugins*  is the path to the directory that
     contains Scipion3 plugins.

   | Close the *ChimeraX* GUI and start the protocol again.

-  *Maxit* installation

   -  Remember: *Maxit* requires *flex* and *bison*. Install them with
      sudo apt-get
