.. _`app:importAtomicStructure`:

Import atomic structure protocol
================================

Protocol designed to import an atomic structure in *Scipion* from PDB database or
from a file of the user’s computer.

-  Requirements to run this protocol and visualize results:

   -  | *Scipion* plugin: **scipion-em**

   -  | *Scipion* plugin: **scipion-em-chimera**

-  | *Scipion* menu: *Model building -> Imports* (:numref:`model_building_app_protocol_atomicStructure_1` (A))

   .. figure:: Images_appendix/Fig110.svg
      :alt: Protocol **import atomic structure**. A: Protocol location in *Scipion* menu. B: Protocol form to import the atomic structure from PDB. C: Protocol form to import the atomic structure from a file.
      :name: model_building_app_protocol_atomicStructure_1
      :align: center
      :width: 80.0%

      Protocol **import atomic structure**. A: Protocol location in *Scipion* menu. B: Protocol form to import the atomic structure from PDB. C: Protocol form to import the atomic structure from a file.

-  | Protocol form parameters (:numref:`model_building_app_protocol_atomicStructure_1` (B)):

   -  | *Import atomic structure from*: Parameter to select the origin of the atomic structure that you want to import. Two options are indicated:

      -  | *id*: Select this option if you want to import the atomic structure from PDB database. Associated to this option is the next form parameter:

         -  | *Atomic structure ID*: Box to write the accession ID of the desired PDB structure. Structure extension *(.cif,.pdb)* is not required.

      -  | *file*: Select this option if you want to import the atomic structure from a file. A new parameter appears associated to this option (:numref:`model_building_app_protocol_atomicStructure_1` (C)):

         -  | *File path*: Box to be completed with the file path. The browser located at the right side of the parameter box helps to look for the file in the user’s computer.

   -  | *Input Volume*: If you want to associate a previously downloaded volume in *Scipion* to the atomic structure, select that volume here.

-  | Protocol execution:

   | Adding specific atomic structure label is recommended in *Run name*
     section, at the form top. To add the label, open the protocol form,
     press the pencil symbol at the right side of *Run name* box,
     complete the label in the new opened window, press OK and, finally,
     close the protocol. This label will be shown in the output summary
     content (see below). If you want to run again this protocol, do not
     forget to set to *Restart* the *Run mode*.

   | Press the *Execute* red button at the form bottom.

-  | Visualization of protocol results:

   | After executing the protocol, press *Analyze Results* and *ChimeraX* graphics window will be opened by default (:numref:`model_building_app_protocol_volume_3`). Atomic structures are referred to the origin of coordinates in *ChimeraX*. To show the relative position of the atomic structure, the three coordinate axes are represented; X axis (red), Y axis (yellow), and Z axis (blue). Coordinate axes and imported atomic structure are model numbers *#1* and *#2*, respectively, in *ChimeraX Models* panel. If a volume has been associated to the atomic structure, coordinate axes and imported atomic structure are model numbers *#2* and *#3*, respectively, in *ChimeraX Models* panel, whereas structure-associated volume has model number *#1*. Volume coordinates and pixel size can be checked in *ChimeraX* main menu *Tools -> Volume Data -> Map Coordinates: Origin index/ Voxel size*. 
   | ``WARNING:`` Take into account that coordinates appear in pixels.

-  | Summary content:

   -  | Protocol output (below *Scipion* framework):
      | *pwem - import atomic structure -> ouputPdb*;
      | *AtomStruct (pseudoatoms=True/ False, volume=True/ False)*.
      | Pseudoatoms is set to *True* when the structure is made of
        pseudoatoms instead of atoms. Volume is set to *True* when an
        electron density map is associated to the atomic structure.

   -  | *SUMMARY* box:
      | Atomic structure imported from ID: / file: *PDB accession ID /
        path*
