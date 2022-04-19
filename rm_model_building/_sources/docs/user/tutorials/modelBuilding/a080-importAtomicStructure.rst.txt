.. _`app:importAtomicStructure`:

Import atomic structure protocol
================================

Protocol designed to import an atomic structure in from PDB database or
from a file of the user’s computer.

-  Requirements to run this protocol and visualize results:

   -  plugin:

   -  plugin:

-  menu: ( (A))

-  Protocol form parameters ( (B)):

   .. figure:: Images_appendix/Fig110.pdf
      :alt: Protocol . A: Protocol location in menu. B: Protocol form to
      import the atomic structure from PDB. C: Protocol form to import
      the atomic structure from a file.
      :name: fig:app_protocol_atomicStructure_1
      :width: 80.0%

      Protocol . A: Protocol location in menu. B: Protocol form to
      import the atomic structure from PDB. C: Protocol form to import
      the atomic structure from a file.

   -  : Parameter to select the origin of the atomic structure that you
      want to import. Two options are indicated:

      -  : Select this option if you want to import the atomic structure
         from PDB database. Associated to this option is the next form
         parameter:

         -  : Box to write the accession ID of the desired PDB
            structure. Structure extension .cif/ .pdb. is not required.

      -  : Select this option if you want to import the atomic structure
         from a file. A new parameter appears associated to this option
         ( (C)):

         -  : Box to be completed with the file path. The browser
            located at the right side of the parameter box helps to look
            for the file in the user’s computer.

   -  : If you want to associate a previously downloaded volume in to
      the atomic structure, select that volume here.

-  Protocol execution:

   | Adding specific atomic structure label is recommended in section,
     at the form top. To add the label, open the protocol form, press
     the pencil symbol at the right side of box, complete the label in
     the new opened window, press OK and, finally, close the protocol.
     This label will be shown in the output summary content (see below).
     If you want to run again this protocol, do not forget to set to the
     .
   | Press the red button at the form bottom.

-  Visualization of protocol results:

   After executing the protocol, press and :math:`ChimeraX` graphics
   window will be opened by default (). Atomic structures are referred
   to the origin of coordinates in . To show the relative position of
   the atomic structure, the three coordinate axes are represented; X
   axis (red), Y axis (yellow), and Z axis (blue). Coordinate axes and
   imported atomic structure are model numbers and , respectively, in
   :math:`ChimeraX` panel. If a volume has been associated to the atomic
   structure, coordinate axes and imported atomic structure are model
   numbers and , respectively, in :math:`ChimeraX` panel, whereas
   structure-associated volume has model number . Volume coordinates and
   pixel size can be checked in :math:`ChimeraX` main menu . WARNING:
   Take into account that coordinates appear in pixels.

-  Summary content:

   -  | Protocol output (below framework):
      | ;
      | .
      | Pseudoatoms is set to when the structure is made of pseudoatoms
        instead of atoms. Volume is set to when an electron density map
        is associated to the atomic structure.

   -  | box:
      | Atomic structure imported from ID: / file:
