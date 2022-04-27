.. _`app:superposePdbsProtocol`:

Phenix Superpose PDBs protocol
==============================

Protocol designed to superpose two atomic structures in *Scipion* by using
*phenix.superpose_pdbs* program :cite:p:`zwartUrl`.
Integrated in the `PHENIX software suite <https://www.phenix-online.org/>`_, *PHENIX* protocol **phenix-superpose pdbs** allows to compare visually
the geometry of two atomic structures by overlapping them. Root mean
square deviation (RMSD) between fixed and moving structures is computed
before and after the superposition.

-  | Requirements to run this protocol and visualize results:

   -  | *Scipion* plugin: **scipion-em**

   -  | *Scipion* plugin: **scipion-em-phenix**

   -  | **PHENIX software suite** (tested for versions 1.13-2998, 1.16-3549, 1.17.1-3660, 1.18.2-3874, 1.19.2-4158 and 1.20.1-4487)

   -  | *Scipion* plugin: **scipion-em-chimera**

-  | *Scipion* menu:
   | *Model building -> Tools-Calculators* (:numref:`model_building_app_protocol_superpose_pdbs_1` (A))

   .. figure:: Images_appendix/Fig153.svg
      :alt: Protocol **phenix-superpose pdbs**. A: Protocol location in *Scipion* menu. B: Protocol form.
      :name: model_building_app_protocol_superpose_pdbs_1
      :align: center
      :width: 90.0%

      Protocol **phenix-superpose pdbs**. A: Protocol location in *Scipion* menu. B: Protocol form.

-  Protocol form parameters (:numref:`model_building_app_protocol_superpose_pdbs_1` (B)):

   -  | *Fixed atomic structure*: Fixed PDBx/mmCIF, previously downloaded or generated in *Scipion*, to which the moving one will be aligned.

   -  | *Moving atomic structure*: PDBx/mmCIF, previously downloaded or generated in *Scipion*, that will be aligned to the fixed one.

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

   After executing the protocol, press *Analyze Results* and *ChimeraX* graphics
   window will be opened by default. Atomic structures and volumes are
   referred to the origin of coordinates in *ChimeraX*. To show the relative
   position of atomic structure and electron density volume, the three
   coordinate axes are represented; X axis (red), Y axis (yellow), and Z
   axis (blue) (:numref:`model_building_app_protocol_volume_3`).

-  Summary content:

   | *SUMMARY* box:
   | RMSD between fixed and moving atoms (start and final values).
