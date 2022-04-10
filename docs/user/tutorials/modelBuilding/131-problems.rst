.. _problems:

How to solve some problems that you can find during the execution of the modeling workflow
==========================================================================================

-  | command lines involving communication (, , and ) do not work:
   | As indicated in
     https://github.com/scipion-em/scipion-em-chimera/blob/devel/FAQ.rst,
     these commands are plugins installed by the scipion-em-chimera
     setup. Firstly, check the right installation of the plugin just
     opening and executing the command line:
   | If it is installed, a help page will appear. Otherwise, type in the
     command line:
   | where path_to_scipion3_plugins is the path to the directory that
     contains Scipion3 plugins.
   | Close the GUI and start the protocol again.

-  installation

   -  Remember: requires and . Install them with sudo apt-get
