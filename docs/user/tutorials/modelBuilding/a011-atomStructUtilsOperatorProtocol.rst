.. _`app:atomStructUtilsOperatorProtocol`:

Atomic Structure Chain Operator protocol
========================================

Protocol designed to perform two types of operations with chains from
atomic structures in : a) Chain extraction: An individual chain will be
extracted from a polymeric atomic structure. The extracted chain will be
saved as monomer in a new atomic structure and will not include HETATM
and water molecules. b) Chain addition: One or several chains will be
added to a reference atomic structure. The resulting addition will be
saved as a new polymeric atomic structure.

-  Requirements to run this protocol and visualize results:

   -  plugin:

   -  plugin:

   -  plugin:

-  menu: ( (A))

-  Protocol form parameters ( (B and C)):

   .. figure:: Images_appendix/Fig154.pdf
      :alt: Protocol . A: Protocol location in menu. B: Protocol form to
      extract a chain from an atomic structure. C: Protocol form to add
      one or several chains to an atomic structure.
      :name: fig:app_protocol_atomstructutils_operator_1
      :width: 90.0%

      Protocol . A: Protocol location in menu. B: Protocol form to
      extract a chain from an atomic structure. C: Protocol form to add
      one or several chains to an atomic structure.

   -  : PDBx/mmCIF atomic structure, previously downloaded or generated
      in .

   -  : Two types of operations can be performed with this protocol:

      -  : Extraction of only one chain from a polymeric atomic
         structure. By selecting this option, three additional params
         have to be completed ( (B)):

         -  : Specific chain that has to be extracted. The wizard on the
            right helps the user to select that chain showing the number
            of the starting model structure, the name of the chain, and
            its number of residues.

         -  : The default value (-1) allows to extract the whole chain.
            In case you would like to extract only a fraction of the
            chain, the number of the initial required residue should be
            indicated.

         -  : The default value (-1) allows to extract the whole chain.
            In case you would like to extract only a fraction of the
            chain, the number of the last required residue should be
            indicated.

      -  : Addition of one or several chains to an initial atomic
         structure. By selecting this option, an additional param has to
         be completed ( (C)):

         -  : One or several PDBx/mmCIF atomic structures, previously
            downloaded or generated in .

-  | Protocol execution: Adding specific structure/chain label is
     recommended in section, at the form top. To add the label, open the
     protocol form, press the pencil symbol at the right side of box,
     complete the label in the new opened window, press OK and, finally,
     close the protocol. This label will be shown in the output summary
     content (see below). If you want to run again this protocol, do not
     forget to set to the .
   | Press the red button at the form bottom.

-  Visualization of protocol results:

   | After executing the protocol, press and graphics window will be
     opened by default. Atomic structures and volumes are referred to
     the origin of coordinates in . To show the relative position of
     atomic structure and electron density volume, the three coordinate
     axes are represented; X axis (red), Y axis (yellow), and Z axis
     (blue) (). Coordinate axes and the new atomic structure generated
     are model numbers and , respectively, in panel. Write in command
     line:
   | to check the individual chains included in the new atomic structure
     generated.

-  | Summary content:
   | Since an atomic structure is generated:

   -  | Protocol output (below framework):
      | ;
      | .
      | Pseudoatoms is set to when the structure is made of pseudoatoms
        instead of atoms. Volume is set to when an electron density map
        is associated to the atomic structure.

   -  | box:
      | No summary information.
