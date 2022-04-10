.. _`app:chimeraRestoreSession`:

ChimeraX Restore Session protocol
=================================

Protocol designed to restore session, provided that this session has
been saved previously in . Currently, four protocols save sessions when
commands , or are used, , , and (Appendices
`[app:chimeraRigidFit] <#app:chimeraRigidFit>`__,
`[app:chimeraOperate] <#app:chimeraOperate>`__,
`[app:modelFromTemplate] <#app:modelFromTemplate>`__ and
`[app:chimeraMapSubtraction] <#app:chimeraMapSubtraction>`__,
respectively). Restored sessions allow inspect any element contained in
a previously saved session, perform operations, and finally save maps or
atomic structures.

-  Requirements to run this protocol and visualize results:

   -  plugin:

   -  plugin:

-  | menu:
   | ( (A))

-  Protocol form parameters ( (B)):

   .. figure:: Images_appendix/Fig118.pdf
      :alt: Protocol . A: Protocol location in menu. B: Protocol form.
      :name: fig:app_protocol_chimera_3
      :width: 90.0%

      Protocol . A: Protocol location in menu. B: Protocol form.

   -  section

      -  : Parameter that allows to select a particular protocol in
         which session has been saved in . As it was mentioned before,
         four protocols support this possibility (, , and ).

   -  section

      This section contains commands required to save :math:`models`
      according to their reference volumes, which can also be saved if
      required. Remark that using command, session will be saved by
      default, without prejudice that it may be saved with command.
      sessions can be restored again by using this same protocol.

-  Protocol execution:

   | Adding specific protocol label is recommended in section, at the
     form top. To add the label, open the protocol form, press the
     pencil symbol at the right side of box, complete the label in the
     new opened window, press OK and, finally, close the protocol. This
     label will be shown in the output summary content (see below). If
     you want to run again this protocol, do not forget to set to the .
   | Press the red button at the form bottom.
   | graphics window will be opened after executing the protocol showing
     the complete list of elements that appeared in graphics window when
     the session was saved, coordinate axes, electron density maps, and
     atomic structures. Steps to follow depend on the specific operation
     to carry out. New volumes or structures may be generated as usual
     in , and they can be combined or saved in in the common way.

   -  | To combine two or more atomic structures:
      | Write in command line:
      | and are the respective :math:`model` numbers of two different
        atomic structures. Optionally you can set the :math:`model`
        number of the output combined structure :

   -  | To save a map or an atomic structure generated with this
        protocol: Write in command line:
      | .
      | Replace by model numbers shown in panel. + string preferred by
        the user to easily identify the atomic structure is optional,
        although quite recomendable.
      | Replace by model numbers shown in panel.

   -  Close graphics window.

-  Visualization of protocol results:

   After executing the protocol, press and graphics window will be
   opened by default. Atomic structures and volumes are referred to the
   origin of coordinates in . To show the relative position of atomic
   structures and electron density volumes, the three coordinate axes
   are represented; X axis (red), Y axis (yellow), and Z axis (blue) ().
   In this particular case a graphics window identical to the input
   session will be opened and it will include every element saved
   lately.

-  Summary content:

   -  If an atomic structure is generated:

      -  | Protocol output (below framework):
         | ;
         | .
         | Pseudoatoms is set to when the structure is made of
           pseudoatoms instead of atoms. Volume is set to when an
           electron density map is associated to the atomic structure.

      -  | box:
         | Produced files:
         | output atomic structure name, starting with the prefix (.cif
           file)
         | we have some result

   -  If a volume is generated:

      -  | Protocol output (below framework):
         | ; .

      -  | box:
         | Produced files:
         | output 3D map name, starting with the prefix (.mrc file)
         | we have some result
