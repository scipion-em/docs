.. _`app:extractUnitCell`:

Extract asymmetric unit protocol
================================

| Protocol designed to obtain in the smallest asymmetric subunit of an
  electron density map having certain types of rotational symmetry.
| WARNING: This protocol requires the starting volume located in the
  center of coordinate axes to equal the center of symmetry with the
  origin of coordinates.

-  Requirements to run this protocol and visualize results:

   -  plugin:

   -  plugin:

   -  plugin:

-  | menu:
   | ( (A))

-  Protocol form parameters ( (B)):

   .. figure:: Images_appendix/Fig107.pdf
      :alt: Protocol . A: Protocol location in menu. B: Protocol form.
      :name: fig:app_protocol_extractUnitCell_1
      :width: 90.0%

      Protocol . A: Protocol location in menu. B: Protocol form.

   -  : Volume already downloaded in from which the asymmetric unit will
      be extracted.

   -  | : In this protocol, symmetry refers only to rotational symmetry,
        also known in biology as radial symmetry. This symmetry is the
        property of volumes to preserve their shape after a partial turn
        around a symmetry axis.
      | Types of rotational symmetry included in this protocol are shown
        in . Two names appear in each case, the first one corresponds to
        nomenclature of symmetry because we are using package, and the
        second one (in brackets) follows the general nomenclature.
        Current nomenclature is :math:`ChimeraX`\ ’s nomenclature, which
        is, in turn, the same symmetry nomenclature of the International
        Union of Cristallography.

      .. figure:: Images_appendix/Fig108.pdf
         :alt: Protocol . Types of rotational symmetry.
         :name: fig:app_protocol_extractUnitCell_2
         :width: 40.0%

         Protocol . Types of rotational symmetry.

      -  Cyclic symmetry : Only one symmetry axis goes through the
         geometric center of the volume. Two more form parameters are
         shown when this type of symmetry is selected:

         -  : Number of times () in which a volume shows the same shape
            when the volume rotates around the symmetry axis from 0 to
            360º. If the same shape is only obtained after turning 360º,
            then . This means that the volume has no symmetry.
            determines the rotation angle.

         -  : Starting angle around Z axis.

      -  Dihedral symmetry : Two perpendicular symmetry axes go through
         the geometric center of the volume. As in the case of cyclic
         symmetry, two more form parameters are shown when this type of
         symmetry is selected:

         -  : Number of times () in which a volume shows the same shape
            when the volume rotates around both symmetry axes from 0 to
            360º. Analogously, determines the rotation angle.

         -  : Starting angle around Z axis.

      -  Tetrahedral symmetry : Four symmetry axes go from each vertex
         to the opposing face center (order 3), and three symmetry axes
         join opposing edges (order 2). .

      -  Octahedral symmetry : Three symmetry axes join opposing
         vertices (order 4), four symmetry axes join opposing face
         centers (order 3), and six symmetry axes join opposing edges
         (order 2). .

      -  Icosahedral symmetries : Six symmetry axes join opposing
         vertices (order 5), 10 symmetry axes join baricenters of
         opposing faces (order 3), and 15 symmetry axes join opposing
         edges (order 2). . Each type of icosahedral symmetry depends on
         its initial orientation. Check in
         (https://www.cgl.ucsf.edu/chimerax/docs/user/commands/shape.html)
         each icosahedral symmetry by writing in the command line: (:
         default, order 2 axes follow XYZ coordinate axes; : idem
         rotated 90º around Z axis; : an order 2 axis and an order 5
         axis follow Y and Z axes, respectively, : idem rotated 90º
         around Z axis.

   -  : Minimal distance from the geometric center that delimits inwards
      the part of the electron density map that will be included in the
      extracted volume. A wizard symbol on the right side of this
      parameter can be helpful to select this radius.

   -  : Maximal distance from the geometric center that delimits
      outwards the part of the electron density map to be included in
      the extracted volume. In other words, the part extracted of the
      map electron density will be between the and the . Again, the
      wizard symbol on the right side of this parameter can be helpful
      to select this radius.

   -  : Additional fraction of the asymmetrical unit cell that will be
      included in the extracted volume.

-  Protocol execution:

   | Press the red button at the form bottom.
   | Adding specific extracted volume label is recommended in section,
     at the form top. To add the label, open the protocol form, press
     the pencil symbol at the right side of box, complete the label in
     the new opened window, press OK and, finally, close the protocol.
     If you want to run again this protocol, do not forget to set to the
     .

-  Visualization of protocol results:

   After executing the protocol, press and a small window will be opened
   (). This window allows you to select between (:math:`ChimeraX`
   graphics window) and (:math:`ShowJ`, the default viewer), to
   visualize the volume.

   .. figure:: Images_appendix/Fig101.pdf
      :alt: Menu to select a visualization tool.
      :name: fig:app_protocol_volume_2
      :width: 70.0%

      Menu to select a visualization tool.

   -  : :math:`ChimeraX` graphics window

      Initial whole volume and extracted volume appear referred to the
      origin of coordinates in . To show the relative position of the
      volume, the three coordinate axes are represented; X axis (red), Y
      axis (yellow), and Z axis (blue) (). Coordinate axes, initial
      volume, and extracted map asymmetric unit are model numbers , and
      , respectively, in :math:`ChimeraX` panel. Volume coordinates and
      pixel size can be checked in :math:`ChimeraX` main menu . WARNING:
      Take into account that coordinates appear in pixels while they
      have been introduced in Å.

   -  : :math:`ShowJ`

      | https://github.com/I2PC/scipion/wiki/ShowJ
      | Each volume can be independently visualized by selecting it in
        the upper menu as the arrow indicates in .

      .. figure:: Images_appendix/Fig109.pdf
         :alt: Protocol . Volume selection with ShowJ.
         :name: fig:app_protocol_extractUnitCell_3
         :width: 70.0%

         Protocol . Volume selection with ShowJ.

-  Summary content:

   -  | Protocol output (below framework):
      | ;
      | Volume (x, y, and z dimensions, sampling rate).

   -  | box:
      | Empty.
