.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _importingData:

==============
Importing Data
==============

.. contents:: Table of Contents:

**Introduction**
----------------

In Scipion the import is almost the only place where the user needs to deal directly
with files. In our model each protocol has very well defined inputs and outputs, which
are data objects. These objects (_SetOfMovies_, _SetOfParticles_, _Volume_, _CTFModel_,
etc.) encapsulate the underlying files and formats.
When importing data like _SetOfMovies_, _SetOfMicrographs_ or _SetOfParticles_, the
user provides critical information (such as the **Pixel Size**). This information will not
be requested any more and should be properly propagated.


Since important information is provided during the import step, it is recommended
to take your time to check that all input parameters are correct.
When importing, the binary files are not copied to the project to avoid data
duplication. Instead, soft links are created pointing to the files location. If you
move your project to another computer these links may be broken. There is
an advanced option where you can set _Copy files?_ to **Yes**. In this case, the
project is more self-contained at the price of using more disk space.

The following paragraphs describe supported formats for different import objects.

**CTFs**
--------

Import of CTF estimation results is possible for:

* **.ctfparam** files from Xmipp.
* **.log**/**.txt**/**.out** files from CTFFind3/4. Typically user has to have
_MicName_ctffind3.log_ and _MicName.ctf_ files in the import folder so that both
CTF parameters and power spectrum could be detected.
* **.log** files from Gctf. Similarly to CTFFind, the log files are usually
_MicName_ctffind3.log_ or _MicName_gctf.log_.

**Coordinates**
---------------

Scipion can import coordinates from several picking programs:

* **.box** files from EMAN1/2, Gautomatch
* **.json** files from EMAN2 (_info/*_info.json_ files in EMAN2 project folder)
* **.pos** files from Xmipp3 (STAR format)
* **.star** files from Relion, Gautomatch
* **.txt** files from Appion DogPicker

Coordinates files are supposed to match micrograph names, i.e. _MicName.box_.

In GUI protocol form import can be set to _Auto_ so that Scipion will try to
detect format type by file extension. You can also import simple txt files
containing two columns: ``_X-coord Y-coord_``. In that case origin (1,1) should
be located at the top left corner of the micrograph with X-axis pointing right
and Y-axis pointing downwards. The coordinates mark the box center (fig. 1).

.. figure:: /docs/images/etc/box_coord.png
   :width: 200
   :align: center
   :alt: Box coordinates


For details about import of coordinates inside Xmipp picker interface,
see  `[here] <https://github.com/I2PC/scipion/wiki/Picker#import-coordinates>`_

**Micrographs**
---------------

Micrographs can be imported either directly from files (default option, see the
list of `[supported formats] <https://github.com/I2PC/xmipp-portal/wiki/ImageFormats))>`_ or:

* **emx** - EMX files follow Electron Microscopy Exchange format (details can be found `[here] <http://i2pc.cnb.csic.es/emx/LoadHome.htm>`_
* **scipion** - you can provide **.sqlite** database file created previously with Scipion and containing all associated micrograph metadata
* **xmipp** - Xmipp metadata files (**.md**) are usually produced by import or preprocess protocols.


**Particles**
-------------

Scipion will try to automatically read metadata associated with particles
(alignment, CTF etc. if available). Besides particle set, Scipion might create
_SetOfClasses_ or/and _SetOfMicrographs_ that are associated with imported
particles. The following formats are currently supported:

* **files** - default import mode
* **emx** - EMX files follow Electron Microscopy Exchange format (details can be found `[here] <(http://i2pc.cnb.csic.es/emx/LoadHome.htm))>`_
* **frealign** - FReAlign files. You need to provide both stack file and **.par** file
* **relion** - Relion STAR file, e.g. _itXX_data.star_
* **scipion** - **.sqlite** file created previously with Scipion, e.g. _particles.sqlite_
* **xmipp3** - Xmipp metadata file, e.g. _images.xmd_


**Tilt pairs**
--------------

Protocol **scipion - import tilted micrographs** allows to import tilt pair
images, e.g. from RCT dataset. In this first version of the protocol, pairs
assignment is done by micrograph order but in next versions a wizard will be
provided.

This means the patterns for tilt pair images should be i.e. **img_untilt_*.tif**
and **img_tilt_*.tif**, corresponding to micrographs **img_untilt_01.tif**,
**img_untilt_02.tif** etc. and **img_tilt_01.tif**, **img_tilt_02.tif** etc.


**Movies, volumes, averages, masks etc.**
-----------------------------------------

All other Scipion objects are imported directly from files. Look at the list
of `[supported image formats] <(https://github.com/I2PC/xmipp-portal/wiki/ImageFormats)>`_.
Right now, DM4 files and new IMAGIC format are not fully supported yet
(you still can import such files), but we are working on it.

Movies are expected to be in stack files (e.g., **mrc**, **mrcs** etc.). However,
import of individual frames is also possible (see **Frames** tab in Import
movies protocol GUI).

**Import/export Scipion projects and workflows**
------------------------------------------------

The ability to export/import workflows in Scipion is a great way to reproduce
previous processing steps. It is particularly useful to repeat steps for similar
samples or to share knowledge between users. Scipion stores workflow in a text
file in JSON format that is human-readable and easily editable.

To import existing workflow, in main project window select
**Project > Import workflow** and choose a **.json** file. If you want to export
certain protocols, select >=2 protocol boxes in main project window and
click **Export**.

It is also possible to import whole projects, e.g. from other computer. To do so,
click on *Import project* button in the main Project window  and provide a path
to the project folder (usually in ScipionUserData/Projects). By default, Scipion
will copy the folder and try to fix broken links. You can help it by providing
raw files location.



