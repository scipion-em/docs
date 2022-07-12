.. _`app:importVolume`:

Import volume protocol
======================

Protocol designed to import electron density maps in *Scipion* from a file of
user’s computer or from the `Electron Microscopy Data Bank (EMDB ) <https://www.ebi.ac.uk/emdb/>`_.

-  | Requirements to run this protocol and visualize results:

   -  | *Scipion* plugin: **scipion-em**

   -  | *Scipion* plugin: **scipion-em-chimera**

-  | *Scipion* menu: *Model building -> Imports* (:numref:`model_building_app_protocol_volume_1` (A))

   .. figure:: Images_appendix/Fig100.svg
      :alt: Protocol **import volumes**. A: Protocol location in *Scipion* menu. B: Protocol form.
      :name: model_building_app_protocol_volume_1
      :align: center
      :width: 90.0%

      Protocol **import volumes**. A: Protocol location in *Scipion* menu. B: Protocol form.

-  | Protocol form parameters (:numref:`model_building_app_protocol_volume_1` (B)):

-  | *Import* section

   -  | *Import from*: Maps can be stored in EMDB or in your own computer. Select thus between these two options:

      -  | *local file*: Select this option if the map is stored in your computer. Several params will appear in this case:

         -  | *Files directory*: Folder that contain one or several volumes (a set of volumes) that you’d like to import. By clicking the folder symbol on the right of *Files directory* box, a browser will be opened to allow you to look for the volume(s)-containing file in your computer. Click the volume that you want to select, if only one volume is going to be loaded. If a set of volumes from the same folder are going to be loaded, click the respective folder.

         -  | *Pattern*: In case you’d like to import a set of volumes, you can include here the common name pattern to all of them. Read *Help* section (question mark) of this parameter and the previous parameter *Files directory* to know about wildcard characters that can be used to generalize patterns.

         -  | *Set half maps*: In case you wouldn’t like to associate half maps as attributes to your map, select the default option *“No”*. Otherwise select the option *“Yes”*. If this is the case, complete the next couple params by looking for each half map in the browser on the right:

            -  | *Path half map1*

            -  | *Path half map2*

         -  | *Pixel size (“sampling rate”)* (Å/px): The size of building blocks (the smallest units) of images depends on the microscope camera and magnification conditions used to get the data.

         -  | *Set origin of coordinates*: You have to choose between setting the default origin of coordinates (option “No”) or another origin of coordinates (“Yes”). The option by default sets the center of the electron density map in the origin of coordinates. This is the preferred option in case you want to run afterwards programs that require symmetry regarding the origin of coordinates, like the **extract asymmetric unit** protocol. If the selected origin of coordinates differs from the map header’s, then a copy of the original map will be generated with the new origin of coordinates in its header. If you decide to set your own origin of coordinates (option “Yes”), a new form parameter (*Offset*) will appear below:

            -  | *Offset*: Write here x, y, and z coordinates of your preference (in Å). Suggestions for coordinates can be obtained by pressing the wizard symbol located on the right side of the *Offset* parameter. In map files with format .mrc, suggested coordinates will be read from the map header.


      -  | *EMDBid*: Select this option if you want to import the density map directly from EMDB. A couple of params will appear in this case:

         -  | *EMDB map ID (integer)*: Write the number of the EMDB map accession.

         -  | *Offset*: Write here x, y, and z coordinates of your preference (in Å). Suggestions for coordinates can be obtained by pressing the wizard symbol located on the right side of the *Offset* parameter. In map files with format ".mrc", suggested coordinates will be read from the map header.

   -  | *Copy files?*: Advanced parameter set to “No” by default because copy density maps unnecessarily duplicates disk space occupied by them, space that could be quite big. Then, by default, volumes will be downloaded by a symbolic link to the file location in your computer. Set this parameter to “Yes” only if you plan to transfer the project to other computers in order to preserve map data in the project.


-  | *Streaming* section

   | Go to this section if you plan simultaneous data acquisition and processing, and select the option “Yes”. By default, considers that you run your processes once you have finished data acquisition (option “No”).

-  | Protocol execution:

   | Adding specific volume label is recommended in *Run name* section,
     at the form top. To add the label, open the protocol form, press
     the pencil symbol at the right side of *Run name* box, complete the
     label in the new opened window, press OK, and finally, close the
     protocol. This label will be shown in the output summary content
     (see below). If you want to run again this protocol, do not forget
     to set to *Restart* the *Run mode*.

   | Press the *Execute* red button at the form bottom.

-  | Visualization of protocol results:

   | After executing the protocol, press *Analyze Results* and a small window will be opened (:numref:`model_building_app_protocol_extractUnitCell_2`). This window allows you to select between *chimerax* (*ChimeraX* graphics window) and *slices* (*ShowJ*, the *Scipion* default viewer), to visualize the volume.

   -  | *chimerax*: *ChimeraX* graphics window

      | Volumes are referred to the origin of coordinates in *ChimeraX*. To show the relative position of the volume, the three coordinate axes are represented; X axis (red), Y axis (yellow), and Z axis (blue) (:numref:`model_building_app_protocol_volume_3`). Coordinate axes and the imported volume are model numbers *#1* and *#2*, respectively, *ChimeraX Models* panel. Volume coordinates and pixel size can be checked in *ChimeraX* main menu *Tools -> Volume Data -> Map coordinates: Origin index/ Voxel size*. 
      | ``WARNING:`` Take into account that coordinates appear in pixels while they have been introduced in Å.

   -  | *slices*: `ShowJ <../../../user/showJ>`_ (:numref:`model_building_app_protocol_volume_4`)

      .. figure:: Images_appendix/Fig103.svg
         :alt: Protocol **import volumes**. Gallery model of *ShowJ* to visualize volume slices.
         :name: model_building_app_protocol_volume_4
         :align: center
         :width: 75.0%

         Protocol **import volumes**. Gallery model of *ShowJ* to visualize volume slices.

-  | Summary content:

   -  | Protocol output (below *Scipion* framework):
      | *pwem - import volumes -> ouputVolume*;
      | *Volume (x, y, and z dimensions, sampling rate)*.

   -  | *SUMMARY* box:
      | Path from which the volume has been downloaded.
      | Sampling rate.
