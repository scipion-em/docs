.. _`app:importMask`:

Import mask protocol
====================

Protocol designed to import a mask in *Scipion* from a file of user’s computer.
Modifying the size of a previous mask is possible simply by changing the
mask’s sampling rate.

-  | Requirements to run this protocol and visualize results:

   -  | *Scipion* plugin: **scipion-em**

-  | *Scipion* menu: It does not appear in *Model building* view. Press ``Ctrl`` + ``f`` and the pop up window to search a protocol will be opened (:numref:`model_building_app_protocol_import_mask` (A)). Write any word related with the title of the protocol that you are looking for in the *Search* box. In this particular case we have written *mask*. Several protocols have been found related with this searching word. Select the first one dessigned for the purpose that we are interested in (*pwem - import mask*).

   .. figure:: Images_appendix/Fig304.svg
      :alt: Protocol **import mask**. A: Window to search the protocol. B: Protocol form.
      :name: model_building_app_protocol_import_mask
      :align: center
      :width: 90.0%

      Protocol **import mask**. A: Window to search the protocol. B: Protocol form.

-  | Protocol form parameters (:numref:`model_building_app_protocol_import_mask` (B)):

-  | *Import* section

   -  | *Mask path*: Open the browser on the right to select in your computer the path to the previously saved mask.

   -  | *Pixel size (“sampling rate”)* (Å/px): Write the new sampling rate value in the box.

-  | Protocol execution:

   | Adding specific mask label is recommended in *Run name* section, at
     the form top. To add the label, open the protocol form, press the
     pencil symbol at the right side of *Run name* box, complete the
     label in the new opened window, press OK, and finally, close the
     protocol. This label will be shown in the output summary content
     (see below). If you want to run again this protocol, do not forget
     to set to *Restart* the *Run mode*.

   | Press the *Execute* red button at the form bottom.

-  | Visualization of protocol results:

   | After executing the protocol, press *Analyze Results* and *ShowJ*, the default *Scipion* viewer, will allow you to visualize the *slices* window of the mask (:numref:`model_building_create3Dmask_2`). The *ShowJ* window menu *(File -> Open with ChimeraX)* allows to open the selected map in *ChimeraX* graphics window.

   -  | *slices*: `ShowJ <../../../user/showJ>`_

-  | Summary content:

   -  | Protocol output (below *Scipion* framework):
      | *pwem - import mask -> ouputMask*;
      | *VolumeMask (x, y, and z dimensions, sampling rate)*.

   -  | *SUMMARY* box:
      | *Mask file imported from*: The specific selected path to the
        mask in your computer should appear here.
