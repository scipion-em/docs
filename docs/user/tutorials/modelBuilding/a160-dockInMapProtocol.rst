.. _`app:dockInMapProtocol`:

Phenix Dock in Map protocol
===========================

Protocol designed to automatically fit atomic structures to electron
density maps in by using *dock in map*
(:raw-latex:`\citep{Liebschner2019}`), application that uses a
convolution-based shape search with which it finds the parts of the
*map* that are similar to the *model*. Additional information can be
found in
http://www.phenix-online.org/documentation/reference/dock_in_map.html.

-  Requirements to run this protocol and visualize results:

   -  plugin: *scipion-em*

   -  plugin: *scipion-em-phenix*

   -  package (tested for versions 1.17.1-3660 and 1.18.2-3874)

   -  plugin: *scipion-em-chimera*

-  | menu:
   | *Model building -> Rigid fitting* ( (A))

-  Protocol form parameters ( (B)):

   .. figure:: Images_appendix/Fig113.pdf
      :alt: Protocol . A: Protocol location in menu. B: Protocol form.
      :name: fig:app_protocol_dockInMap_1
      :width: 90.0%

      Protocol . A: Protocol location in menu. B: Protocol form.

   -  *Input map*: Electron density map previously downloaded or
      generated in to fit the atomic structure.

   -  *Resolution (Å)*: Electron density map resolution.

   -  *Input atom structure*: Atomic structure previously downloaded or
      generated in to be fitted to an electron density map.

   -  *Atom structure number of copies*: Number of *models* that have to
      be simultaneously fitted to an electron density map.

   -  *Number of threads*: Advanced param. Depending on the size of
      *map* and *model*, and the number of *models* to fit the process
      could be quite slow and you can accelerate it by increasing the
      number of threads.

-  Protocol execution:

   | Adding specific protocol label is recommended in *Run name*
     section, at the form top. To add the label, open the protocol form,
     press the pencil symbol at the right side of *Run name* box,
     complete the label in the new opened window, press OK and, finally,
     close the protocol. This label will be shown in the output summary
     content (see below). If you want to run again this protocol, do not
     forget to set to *Restart* the *Run mode*.
   | Press the *Execute* red button at the form bottom.

-  Visualization of protocol results:

   After executing the protocol, press *Analyze Results* and the
   graphics window will be opened by default. Atomic structures and
   volumes are referred to the origin of coordinates in . To show the
   relative position of atomic structure and electron density volume,
   the three coordinate axes are represented; X axis (red), Y axis
   (yellow), and Z axis (blue) (). Coordinate axes, map, initial
   unfitted *model* and final fitted atomic structure are model numbers
   *#1*, *#2*, *#3* and *#4*, respectively, in *Models* panel.

-  Summary content:

   -  | Protocol output (below framework):
      | *phenix - dock in map -> ouputPdb*;
      | *AtomStruct (pseudoatoms=True/ False, volume=True/ False)*.
      | Pseudoatoms is set to *True* when the structure is made of
        pseudoatoms instead of atoms. Volume is set to *True* when an
        electron density map is associated to the atomic structure.

   -  | *SUMMARY* box:
      | No summary information
