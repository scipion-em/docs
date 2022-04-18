.. _`app:chimeraContactsProtocol`:

ChimeraX Contacts protocol
==========================

Protocol designed to obtain contacts favorable and unfavorable (clashes
or close contacts, where atoms are too close together) between any
couple of chains of an atomic structure in *Scipion* by using *ChimeraX*.

-  Requirements to run this protocol and visualize results:

   -  *Scipion* plugin: **scipion-em**

   -  *Scipion* plugin: **scipion-em-chimera**


-  *Scipion* menu: *Model building -> Tools-Calculators* (:numref:`model_building_app_protocol_contacts_1` (A))


-  Protocol form parameters (:numref:`model_building_app_protocol_contacts_1` (B)):

   .. figure:: Images_appendix/Fig155.svg
      :alt: Protocol **chimerax-contacts**. A: Protocol location in *Scipion* menu. B: Protocol form. C: Protocol form detailing *Chain Labelling* for *I222r* symmetry.
      :name: model_building_app_protocol_contacts_1
      :align: center
      :width: 90.0%

      Protocol **chimerax-contacts**. A: Protocol location in *Scipion* menu. B: Protocol form. C: Protocol form detailing *Chain Labelling* for *I222r* symmetry.

   -  *Atomic Structure*: Param to select one atomic structure
      previously downloaded or generated in *Scipion* with the aim of calculating
      contacts between any couple of chains.


   -  *Chain Labeling*: Param to asign a specific label to each one of
      the chains of the atomic structure. Chain labeling allows to group
      chains in order to get only contacts among chains from different
      groups. When two chains show the same label, contacts between any
      of these chains and an independent chain, or a chain that belongs
      to a different group, will be calculated. However, no contacts
      will be computed between chains included in the same group. :numref:`model_building_app_protocol_contacts_1` (C)
      shows an example of chain grouping in four different groups. Each
      one of these groups includes three chains: *h1: [A, B, C];  h2: [D, E, F];  h3: [G, H, I];  h4: [J, K, L];  tx1: [Q, R, S]*. The rest of chains
      remain as independent chains. There is a wizard on the right side
      of the *Chain Labeling* protocol form box to help the user to fill
      in the form since it specifies the names of the different chains
      included in the *Atomic Structure* input.

   -  *Apply symmetry*: Param that allows the user to select if symmetry
      has to be applied.

      -  | Set to *Yes* if the *Atomic Structure* input is the
           asymmetric unit of a macromolecule and you’d like to know the
           contacts between any two chains within the asymmetric unit as
           well as the contacts between any chain of the asymmetric unit
           and a chain from a neighbor asymmetric unit. Consider, in
           this case, that only neighbor unit cells located at less than
           3Å of the input unit cell will be generated.

         | ``WARNING:`` Be sure that the origin of coordinates equals the
           symmetry center of the input asymmetric unit, in order to
           generate adjacent asymmetric units able to interact with the
           input asymmetric unit.

      -  Set to *No* if you’d like to know the contacts between any two
         chains within the *Atomic Structure* input.

   -  *Symmetry*: If the user selects *Yes*, an additional protocol
      param box will interrogate about the type of symmetry. In order to
      reconstruct a macromolecule from a unit cell, symmetries allowed
      are cyclic (*Cn*), dihedral (*Dn*), tetrahedral (*T*), octahedral
      (*O*), and eight icosahedral symmetries (*I*). Each icosahedral
      symmetry shows its respective *ChimeraX* orientation
      (https://www.cgl.ucsf.edu/chimerax/docs/user/commands/sym.html):

      -  *I222*: *ChimeraX* orientation *222*; two-fold symmetry axes along the X,
         Y, and Z axes.

      -  *I222r*: *ChimeraX* orientation *222r*; *ChimeraX* orientation *222* rotated 90 degrees about
         Z.

      -  *In25*: *ChimeraX* orientation *n25*; two-fold symmetry along Y and 5-fold
         along Z.

      -  *In25r*: *ChimeraX* orientation *n25r*; *ChimeraX* orientation *n25* rotated 180 degrees about
         X.

      -  *I2n3*: *ChimeraX* orientation *2n3*; two-fold symmetry along X and 3-fold
         along Z.

      -  *I2n3r*: *ChimeraX* orientation *2n3r*; *ChimeraX* orientation *2n3* rotated 180 degrees about
         Y.

      -  *I2n5*: *ChimeraX* orientation *2n5*; two-fold symmetry along X and 5-fold
         along Z.

      -  *I2n5r*: *ChimeraX* orientation *2n5r*; *ChimeraX* orientation *2n5* rotated 180 degrees about
         Y.

   -  *Symmetry Order*: After selecting *Cn* or *Dn* symmetries, an
      additional protocol param box will interrogate about the symmetry
      order. A positive integer has to be written here. If the integer
      is *1* no symmetry will be applied.

   -  *Tetrahedral orientation*: After selecting *T* symmetry, an
      additional protocol param box will interrogate about the
      tetrahedral orientation. The two *ChimeraX* orientations have been included
      (https://www.cgl.ucsf.edu/chimerax/docs/user/commands/sym.html):

      -  *222*: Two-fold symmetry axes along the X, Y, and Z axes, a
         three-fold along axis (1,1,1).

      -  *z3*: A three-fold symmetry axis along Z and another three-fold
         axis in the YZ plane.

   -  *Fit params for clashes and contacts*: Advanced params that allow
      to modify interatomic distances in order to identify not only
      favorable interactions (by default), but also unfavorable ones
      (clashes) where atoms are too close together
      (https://www.cgl.ucsf.edu/chimerax/docs/user/commands/clashes.html).

      -  *cutoff (Angstroms)*: Negative cutoff indicates favorable
         contacts; the default value to identify contacts is -0.4 (from
         0.0 to -1.0). The default value to identify clashes is 0.6
         (from 0.4 to 1.0). Large positive cutoff identifies the more
         severe clashes.

      -  *allowance (Angstroms)*: The default value to identify contacts
         is 0.0, whereas the default value to identify clashes is 0.4.

-  Protocol execution:

   | Adding specific structure label is recommended in *Run name*
     section, at the form top. To add the label, open the protocol form,
     press the pencil symbol at the right side of *Run name* box,
     complete the label in the new opened window, press OK and, finally,
     close the protocol. This label will be shown in the output summary
     content (see below). If you want to run again this protocol, do not
     forget to set to *Restart* the *Run mode*.

   | Press the *Execute* red button at the form bottom.

-  Visualization of protocol results: After executing the **chimerax-contacts** protocol, the
   viewer window will be opened. This window includes three boxes (:numref:`model_building_contacts_results`):

   -  *3D Visualization*: *ChimeraX* graphics window will be opened by selecting
      this option. The input atomic structure is shown, as well as the
      additional structure generated, if symmetry has been applied.

   -  *Interacting chains*: A text file will be opened detailing the
      number of atomic contacts, the models and the chains involved in
      contacts. Two scenarios can be examined:

      -  | If *Apply symmetry* was set to *Yes*: If no chain groups have
           been established, all contacts between any couple of chains
           within the input atomic structure will be shown.
           Besides,“non-redundant” contacts between any chain of the
           input unit cell structure and any chain of the neighbor unit
           cells will also be shown. By “non-redundant” contacts we
           define all those contacts that cannot be inferred by
           symmetry. An example of this type of contacts is shown in :numref:`model_building_schema_contacts`
           (A). In addition, input atomic structure is model *#1.1*,
           whereas models generated by symmetry will be *#1.2, #1.3* and
           so on, if several models are generated. Each one of these
           models is supposed to be a neighbor unit cell located at less
           than 3 Å from the input one.

         | ``WARNING:`` If no additional models are generated at less than 3
           Å from the input one, consider the possibility that the
           symmetry center of the input structure does not coincide with
           the center of coordinates.

      -  If *Apply symmetry* was set to *No*: If no chain groups have
         been established, all contacts between any couple of chains
         within the input atomic structure will be shown (Example in :numref:`model_building_schema_contacts`
         (A)). There is only one model in this case, model *#1*.

   -  *Contacts between interacting chains*: This box allows to select a
      particular interaction between two chains to identify the residues
      involved in that interaction. The summary of results will be
      displayed in a text file. It includes the number of atom contacts
      between the residues of chain 1, model 1 and the residues of chain
      2, model 2.

      -  *Swap chain columns in the summary of contacts*: Select *Yes*
         to display in the text file the number of contacts between the
         residues of chain 2, model 2 and the residues of chain 1, model
         1. Otherwise, selecting *No*, the default order of columns will
         be shown.

      -  *Distance to group residues (Number of residues)*: Maximum
         number of residues between two residues that allows to group
         these two residues. Then, if two residues are closer than this
         number of residues (distance), they will be grouped. In a long
         list of grouped residues, the distance between two consecutive
         residues has to be lower than the set number of residues, 4 by
         default.

      -  *Select two interacting chains and get the summary of
         contacts*: Select a particular interaction with the scroll
         arrow on the right and view the text file with the summary of
         contacts for that interaction.

-  Summary content:

   -  Protocol output (below *Scipion* framework): No output information.

   -  | *SUMMARY* box:
      | No summary information.
