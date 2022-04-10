.. _`app:chimeraContactsProtocol`:

ChimeraX Contacts protocol
==========================

Protocol designed to obtain contacts favorable and unfavorable (clashes
or close contacts, where atoms are too close together) between any
couple of chains of an atomic structure in by using .

-  Requirements to run this protocol and visualize results:

   -  plugin:

   -  plugin:

-  menu: ( (A))

-  Protocol form parameters ( (B)):

   .. figure:: Images_appendix/Fig155.pdf
      :alt: Protocol . A: Protocol location in menu. B: Protocol form.
      C: Protocol form detailing for symmetry.
      :name: fig:app_protocol_contacts_1
      :width: 90.0%

      Protocol . A: Protocol location in menu. B: Protocol form. C:
      Protocol form detailing for symmetry.

   -  : Param to select one atomic structure previously downloaded or
      generated in with the aim of calculating contacts between any
      couple of chains.

   -  : Param to asign a specific label for each one of the chains of
      the atomic structure. Chain labeling allows to group chains in
      order to get only contacts among chains from different groups.
      When two chains show the same label, contacts between any of these
      chains and an independent chain, or a chain that belongs to a
      different group, will be calculated. However, no contacts will be
      computed between chains included in the same group. (C) shows an
      example of chain grouping in four different groups. Each one of
      these groups includes three chains: . The rest of chains remain as
      independent chains. There is a wizard on the right side of the
      protocol form box to help the user to fill in the form since it
      specifies the names of the different chains included in the input.

   -  : Param that allows the user to select if symmetry has to be
      applied.

      -  | Set to if the input is the asymmetric unit of a macromolecule
           and you’d like to know the contacts between any two chains
           within the asymmetric unit as well as the contacts between
           any chain of the asymmetric unit and a chain from a neighbor
           asymmetric unit. Consider, in this case, that only neighbor
           unit cells located at less than 3Å of the input unit cell
           will be generated.
         | WARNING: Be sure that the origin of coordinates equals the
           symmetry center of the input asymmetric unit, in order to
           generate adjacent asymmetric units able to interact with the
           input asymmetric unit.

      -  Set to if you’d like to know the contacts between any two
         chains within the input.

   -  : If the user selects , an additional protocol param box will
      interrogate about the type of symmetry. In order to reconstruct a
      macromolecule from a unit cell, symmetries allowed are cyclic (),
      dihedral (), tetrahedral (), octahedral (), and eight icosahedral
      symmetries (). Each icosahedral symmetry shows its respective
      orientation
      (https://www.cgl.ucsf.edu/chimerax/docs/user/commands/sym.html):

      -  : orientation ; two-fold symmetry axes along the X, Y, and Z
         axes.

      -  : orientation ; orientation rotated 90about Z.

      -  : orientation ; two-fold symmetry along Y and 5-fold along Z.

      -  : orientation ; orientation rotated 180about X.

      -  : orientation ; two-fold symmetry along X and 3-fold along Z.

      -  : orientation ; orientation rotated 180about Y.

      -  : orientation ; two-fold symmetry along X and 5-fold along Z.

      -  : orientation ; orientation rotated 180about Y.

   -  : After selecting or symmetries, an additional protocol param box
      will interrogate about the symmetry order. A positive integer has
      to be written here. If the integer is no symmetry will be applied.

   -  : After selecting symmetry, an additional protocol param box will
      interrogate about the tetrahedral orientation. The two orientation
      have been included
      (https://www.cgl.ucsf.edu/chimerax/docs/user/commands/sym.html):

      -  : Two-fold symmetry axes along the X, Y, and Z axes, a
         three-fold along axis (1,1,1).

      -  : A three-fold symmetry axis along Z and another three-fold
         axis in the YZ plane.

   -  : Advanced params that allow to modify interatomic distances in
      order to identify not only favorable interactions (by default),
      but also unfavorable ones (clashes) where atoms are too close
      together
      (https://www.cgl.ucsf.edu/chimerax/docs/user/commands/clashes.html).

      -  : Negative cutoff indicates favorable contacts; the default
         value to identify contacts is -0.4 (from 0.0 to -1.0). The
         default value to identify clashes is 0.6 (from 0.4 to 1.0).
         Large positive cutoff identifies the more severe clashes.

      -  : The default value to identify contacts is 0.0, whereas the
         default value to identify clashes is 0.4.

-  Protocol execution:

   | Adding specific structure label is recommended in section, at the
     form top. To add the label, open the protocol form, press the
     pencil symbol at the right side of box, complete the label in the
     new opened window, press OK and, finally, close the protocol. This
     label will be shown in the output summary content (see below). If
     you want to run again this protocol, do not forget to set to the .
   | Press the red button at the form bottom.

-  Visualization of protocol results: After executing the protocol, the
   viewer window will be opened. This window includes three boxes ():

   -  : graphics window will be opened by selecting this option. The
      input atomic structure is shown, as well as the additional
      structure generated, if symmetry has been applied.

   -  : A text file will be opened detailing the number of atomic
      contacts, the models and the chains involved in contacts. Two
      scenarios can be examined:

      -  | If was set to : If no chain groups have been established, all
           contacts between any couple of chains within the input atomic
           structure will be shown. Besides,“non-redundant” contacts
           between any chain of the input unit cell structure and any
           chain of the neighbor unit cells will also be shown. By
           “non-redundant” contacts we define all those contacts that
           cannot be inferred by symmetry. An example of this type of
           contacts is shown in (A). In addition, input atomic structure
           is model , whereas models generated by symmetry will be and
           so on, if several models are generated. Each one of these
           models is supposed to be a neighbor unit cell located at less
           than 3 Å from the input one.
         | WARNING: If no additional models are generated at less than 3
           Å from the input one, consider the possibility that the
           symmetry center of the input structure does not coincide with
           the center of coordinates.

      -  If was set to : If no chain groups have been established, all
         contacts between any couple of chains within the input atomic
         structure will be shown (Example in (A)). There is only one
         model in this case, model .

   -  : This box allows to select a particular interaction between two
      chains to identify the residues involved in that interaction. The
      summary of results will be displayed in a text file. It includes
      the number of atom contacts between the residues of chain 1, model
      1 and the residues of chain 2, model 2.

      -  : Select to display in the text file the number of contacts
         between the residues of chain 2, model 2 and the residues of
         chain 1, model 1. Otherwise, selecting , the default order of
         columns will be shown.

      -  : Maximum number of residues between two residues that allows
         to group these two residues. Then, if two residues are closer
         than this number of residues (distance), they will be grouped.
         In a long list of grouped residues, the distance between two
         consecutive residues has to be lower than the set number of
         residues, 4 by default.

      -  : Select a particular interaction with the scroll arrow on the
         right and view the text file with the summary of contacts for
         that interaction.

-  Summary content:

   -  Protocol output (below framework): No output information.

   -  | box:
      | No summary information.
