.. _`app:chimeraRigidFit`:

ChimeraX Rigid Fit protocol
===========================

Protocol designed to manually fit atomic structures to electron density
maps in by using . If and are quite close, e.g. after running protocol,
automatic fitting is also possible. Fitted atomic structures generated
by using this protocol can be saved in after executing specific
commands.

-  Requirements to run this protocol and visualize results:

   -  plugin:

   -  plugin:

-  | menu:
   | ( (A))

-  Protocol form parameters ( (B)):

   .. figure:: Images_appendix/Fig116.pdf
      :alt: Protocol . A: Protocol location in menu. B: Protocol form.
      :name: fig:app_protocol_chimera_1
      :width: 90.0%

      Protocol . A: Protocol location in menu. B: Protocol form.

   -  section

      -  : Mandatory param to load the electron density previously
         downloaded or generated in to fit the atomic structure.

      -  : :math:`Idem`. If additional maps, others than the previous ,
         are needed.

      -  : Mandatory param to load the atomic structure previously
         downloaded or generated in to be fitted to an electron density
         map.

      -  : Atomic structures others than the that can help in the rigid
         body fitting process.

   -  section

      This section contains commands required to save according to their
      reference volumes, which can also be saved if required. Remark
      that using command, session will be saved by default, without
      prejudice that it may be saved with command. sessions can be
      restored by using protocol. In addition allows to combine several
      atomic structures in a unique .

-  Protocol execution:

   | Adding specific map/structure label is recommended in section, at
     the form top. To add the label, open the protocol form, press the
     pencil symbol at the right side of box, complete the label in the
     new opened window, press OK and, finally, close the protocol. This
     label will be shown in the output summary content (see below). If
     you want to run again this protocol, do not forget to set to the .
   | Press the red button at the form bottom.
   | graphics window will be opened after executing the protocol. The
     electron density map and the atomic structure are shown. Main steps
     to complete the rigid body fitting are:

   -  | If density map and atomic structure are quite close to each
        other:
      | Go to main menu and select . A small window will be opened. Once
        the right atomic structure and the electron density volume have
        been selected, fit them by clicking .
      | : The same result can be obtained by typing in the command line
        , with and model numbers of and .

   -  If and are far from each other, start the fitting process
      interactively activating and inactivating objects alternatively to
      finally get and close enough to go to the previous step.
      Otherwise, consider the possibility of running before the
      protocol.

   -  | To combine two or more atomic structures:
      | Write in command line:
      | and are the respective :math:`model` numbers of two different
        atomic structures. Optionally you can set the :math:`model`
        number of the output combined structure :

   -  | Save fitted regarding the by writing in command line:
      | .
      | Replace by model numbers shown in panel. + string preferred by
        the user to easily identify the atomic structure is optional,
        although quite recomendable.

   -  Close graphics window.

-  Visualization of protocol results:

   After executing the protocol, press and graphics window will be
   opened by default. Atomic structures and volumes are referred to the
   origin of coordinates in . To show the relative position of and , the
   three coordinate axes are represented; X axis (red), Y axis (yellow),
   and Z axis (blue) (). Coordinate axes, map, and atomic structure are
   model numbers , , and , respectively, in panel in the most simple
   case.

-  Summary content:

   -  If only the atomic structure has been saved by command:

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

   -  If both the atomic structure and its reference electron density
      map have been saved by command:

      -  | Protocol output (below framework):
         | ; .
         | ;
         | .
         | Pseudoatoms is set to when the structure is made of
           pseudoatoms instead of atoms. Volume is set to when an
           electron density map is associated to the atomic structure.

      -  | box:
         | Produced files:
         | Map_name file, starting with the prefix (.mrc)
         | we have some result
