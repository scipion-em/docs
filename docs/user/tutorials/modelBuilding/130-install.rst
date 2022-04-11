A Note on Software Installation
===============================

All the protocols shown in this document are available in the stable
release *3.0.6* (code name *Eugenius*). This is a major release in which
protocols are published as “plugins”. Required plugins for each protocol
are indicated in respective Appendices. Follow the instructions to
install each plugin (https://github.com/scipion-em/).

In addition to the standard and *scipion plugins* installation, you need
to install the following packages:

-  **CCP4** (v. 7.0.056 or higher; protocols have been tested with v.
   7.1): Connect to http://www.ccp4.ac.uk/download/#os=linux and follow
   instructions.

-  **Phenix**: Connect to https://www.phenix-online.org/download/ and
   follow instructions. Protocols have been tested for versions
   1.13-2998, 1.16-3549, 1.17.1-3660 and 1.18.2-3874.

-  **Clustal Omega**: *sudo apt-get install clustalo* (in ubuntu).

-  **MUSCLE**: *sudo apt-get install muscle* (in ubuntu).

Finally, (1) edit the file * /.config/scipion/scipion.conf* and set the
right values for the variables *CCP4_HOME* and *PHENIX_HOME*, and (2)
execute *scipion config –update*
