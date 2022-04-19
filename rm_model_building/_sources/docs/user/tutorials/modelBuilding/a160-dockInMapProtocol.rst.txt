.. _`app:dockInMapProtocol`:

Phenix Dock in Map protocol
===========================

Protocol designed to automatically fit atomic structures to electron
density maps in by using (:raw-latex:`\citep{Liebschner2019}`),
application that uses a convolution-based shape search with which it
finds the parts of the that are similar to the . Additional information
can be found in
http://www.phenix-online.org/documentation/reference/dock_in_map.html.

-  Requirements to run this protocol and visualize results:

   -  plugin:

   -  plugin:

   -  package (tested for versions 1.17.1-3660 and 1.18.2-3874)

   -  plugin:

-  | menu:
   | ( (A))

-  Protocol form parameters ( (B)):

   .. figure:: Images_appendix/Fig113.pdf
      :alt: Protocol . A: Protocol location in menu. B: Protocol form.
      :name: fig:app_protocol_dockInMap_1
      :width: 90.0%

      Protocol . A: Protocol location in menu. B: Protocol form.

   -  : Electron density map previously downloaded or generated in to
      fit the atomic structure.

   -  : Electron density map resolution.

   -  : Atomic structure previously downloaded or generated in to be
      fitted to an electron density map.

   -  : Number of that have to be simultaneously fitted to an electron
      density map.

   -  : Advanced param. Depending on the size of and , and the number of
      to fit the process could be quite slow and you can accelerate it
      by increasing the number of threads.

-  Protocol execution:

   | Adding specific protocol label is recommended in section, at the
     form top. To add the label, open the protocol form, press the
     pencil symbol at the right side of box, complete the label in the
     new opened window, press OK and, finally, close the protocol. This
     label will be shown in the output summary content (see below). If
     you want to run again this protocol, do not forget to set to the .
   | Press the red button at the form bottom.

-  Visualization of protocol results:

   After executing the protocol, press and the graphics window will be
   opened by default. Atomic structures and volumes are referred to the
   origin of coordinates in . To show the relative position of atomic
   structure and electron density volume, the three coordinate axes are
   represented; X axis (red), Y axis (yellow), and Z axis (blue) ().
   Coordinate axes, map, initial unfitted and final fitted atomic
   structure are model numbers , , and , respectively, in panel.

-  Summary content:

   -  | Protocol output (below framework):
      | ;
      | .
      | Pseudoatoms is set to when the structure is made of pseudoatoms
        instead of atoms. Volume is set to when an electron density map
        is associated to the atomic structure.

   -  | box:
      | No summary information
