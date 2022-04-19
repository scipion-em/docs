.. _`app:superposePdbsProtocol`:

Phenix Superpose PDBs protocol
==============================

Protocol designed to superpose two atomic structures in by using
*phenix.superpose_pdbs* program :raw-latex:`\citep{zwartUrl}`.
Integrated in the :math:`Phenix` software suite
(https://www.phenix-online.org/), protocol allows to compare visually
the geometry of two atomic structures by overlapping them. Root mean
square deviation (RMSD) between fixed and moving structures is computed
before and after the superposition.

-  Requirements to run this protocol and visualize results:

   -  plugin: *scipion-em*

   -  plugin: *scipion-em-phenix*

   -  PHENIX software suite (tested for versions 1.16-3549, 1.17.1-3660
      and 1.18.2-3874)

   -  plugin: *scipion-em-chimera*

-  | menu:
   | *Model building -> Tools-Calculators* ( (A))

-  Protocol form parameters ( (B)):

   .. figure:: Images_appendix/Fig153.pdf
      :alt: Protocol . A: Protocol location in menu. B: Protocol form.
      :name: fig:app_protocol_superpose_pdbs_1
      :width: 90.0%

      Protocol . A: Protocol location in menu. B: Protocol form.

   -  *Fixed atomic structure*: Fixed PDBx/mmCIF, previously downloaded
      or generated in , to which the moving one will be aligned.

   -  *Moving atomic structure*: PDBx/mmCIF, previously downloaded or
      generated in , that will be aligned to the fixed one.

-  | Protocol execution:
   | Adding specific moving_structure/fixed_structure label is
     recommended in *Run name* section, at the form top. To add the
     label, open the protocol form, press the pencil symbol at the right
     side of *Run name* box, complete the label in the new opened
     window, press OK and, finally, close the protocol. This label will
     be shown in the output summary content (see below). If you want to
     run again this protocol, do not forget to set to *Restart* the *Run
     mode*.
   | Press the *Execute* red button at the form bottom.

-  Visualization of protocol results:

   After executing the protocol, press *Analyze Results* and graphics
   window will be opened by default. Atomic structures and volumes are
   referred to the origin of coordinates in . To show the relative
   position of atomic structure and electron density volume, the three
   coordinate axes are represented; X axis (red), Y axis (yellow), and Z
   axis (blue) ().

-  Summary content:

   | *SUMMARY* box:
   | RMSD between fixed and moving atoms (start and final values).
