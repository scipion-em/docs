.. figure:: /docs/images/scipion_logo.gif
   :width: 250
   :alt: scipion logo

.. _scipion-java:

============
Scipion Java
============

As you may know `ShowJ <https://scipion-em.github.io/docs/docs/user/user-documentation.html#showj>`_ is our default viewer for most of Scipion
objects and `Particle Picker <https://scipion-em.github.io/docs/docs/user/user-documentation.html#particle-picker>`_ allows us to visualize coordinates or
pick particles either manually or automatically. Scipion source packages related
to ShowJ and Particle Picking include:


* xmipp.ij.commmons : Contains ImageJ-related classes (In ShowJ we use and
  extend ImageJ to display and process images), such as Xmipp canvas with
  customized events, Xmipp image window with our menu and imageplus loader.
* xmipp.jni : Contains Java bindings with Xmipp C++ code
* xmipp.viewer.models : Contains the different table models used to display data
  in ShowJ
* xmipp.viewer.windows : Contains ShowJ main frame and associated dialogs:
  columns editor, plotter, CTF Profile, etc.
* xmipp.viewer.scipion : Contains Scipion extensions of Metadata, GalleryData
  and GalleryJFrame classes
* xmipp.viewer.particlepicker: Contains base classes for particle picking:
  frame, canvas, micrograph, particle dialog, etc.
* xmipp.viewer.particlepicker.training: Contains supervised picker implementation
* xmipp.viewer.particlepicker.tiltpair: Contains tilt pair picker implementation

xmipp.jni package contains java versions of Xmipp core classes for image
processing, such as MetaData or ImageGeneric. A Metadata represents a star file
and it is used to read and store information in Xmipp. ImageGeneric represents
an image in memory. It is used to load and write image files, such as .stk,
.mrc, .vol, etc.

xmipp.viewer.particlepicker.training and xmipp.viewer.particlepicker.tiltpair
packages in turn contain model and GUI packages with data model and windows
respectively.

In the following class diagram, we display ShowJ main classes and its relations:

.. image:: /docs/images/showj-class-diagram.gif
   :alt: showj-class-diagram
   :height: 400

GalleryJFrame and table models are used for data visualization, while
GalleryData is in charge of data manipulation and business logic.
To visualize most data objects in Scipion, DataViews are used. DataViews can
display data in desktop and web using ShowJ or ShowJ Web. These classes are
defined in pyworkflow/em/viewer.py. The developer can specify column visibility,
order, type of viewer (gallery or table), etc. In turn, this configuration is
given as input to ShowJ from the command line.

In the following class diagram, we display particle picker main classes and its
relations:

.. image:: /docs/images/picker-class-diagram.gif
   :alt: Picker Class Diagram
   :height: 400

Base classes ParticlePicker, ParticlePickerJFrame, ParticlePickerCanvas, etc.,
are extended to implement supervised and tilt pair picker. Images are loaded
using ImagePlusLoader and displayed using XmippImageWindow, as in ShowJ.
While ParticlePickerJFrame and ParticlePickerCanvas are used to visualize and
edit coordinates, ParticlePicker contains all the business logic related to the
picking process.

ShowJ and Particle Picker use sockets to communicate with Scipion. The port used
for communication is specified  as an input parameter from the command line.
There are a number of operations that require this functionality:

* creating subsets: We can create subsets of classes, of particles from classes,
  of representatives, of images, of volumes, etc. These subsets are created
  through Scipion buttons added in ScipionGalleryJFrame at the bottom of the
  window. They invoke the creation of the corresponding ProtUserSubset output
  implemented in the protocol_batch module.
* registering coordinates: This socket is implemented in pyworkflow/em/showj.py
  to register picker coordinates. It invokes picker protocol method
  "registerCoords" in order to convert its coordinates into the Scipion format.
* executing object commands: In ShowJ the developer can specify a set of
  commmands to be linked with the object menu (popup menu displayed when the user
  does right click). Eg: Display CTF Fitting, Plot Distance Profile
  (Normal Modes), etc.  Python code related to these actions is executed using
  sockets. The socket handler and the functions related to these actions are
  implemented in pyworkflow/gui/project/project.py

Particle Picker has also been extended to use a generic classifier if provided
with a configuration file specifying classifier autopick and convert commands
and input parameters. This allows us to use it as a wizard to configure
automatic pickers such as Relion autopick, Appion dogpicker or gaussian picker.
A classifier configuration should look like this:

.. code-block:: python

    parameters = diameter,threshold
    diameter.value = 100
    diameter.label = Diameter
    diameter.help = some help
    threshold.value =  0.5
    threshold.label = Threshold
    threshold.help = some help
    autopickCommand = /path/to/scipion/software/em/dogpicker/ApDogPicker.py  --thresh=%(threshold) --diam=%(diameter) --apix=3.54  --image=%(micrograph) --outfile=Tmp/348.outputMicrographs04/%(micrographName).txt
    convertCommand = /path/to/scipion/pyworkflow/apps/pw_convert.py --coordinates --from dogpicker --to xmipp --input  Runs/000348_ProtSplitSet/micrographs4.sqlite --output Tmp/348.outputMicrographs04

Autopick protocols implement wizards that generate this file and launch the
particle picker to adjust parameters (considering the results in several
micrographs) before running an automatic picking for the whole set of
micrographs.