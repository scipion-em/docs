.. _`app:extractUnitCell`:

Extract asymmetric unit protocol
================================

| Protocol designed to obtain in the smallest asymmetric subunit of an
  electron density map having certain types of rotational symmetry.
| WARNING: This protocol requires the starting volume located in the
  center of coordinate axes to equal the center of symmetry with the
  origin of coordinates.

-  Requirements to run this protocol and visualize results:

   -  plugin: *scipion-em*

   -  plugin: *scipion-em-xmipp*

   -  plugin: *scipion-em-chimera*

-  | menu:
   | *Model building -> Preprocess map* ( (A))

-  Protocol form parameters ( (B)):

   .. figure:: Images_appendix/Fig107.pdf
      :alt: Protocol . A: Protocol location in menu. B: Protocol form.
      :name: fig:app_protocol_extractUnitCell_1
      :width: 90.0%

      Protocol . A: Protocol location in menu. B: Protocol form.

   -  *Input Volume*: Volume already downloaded in from which the
      asymmetric unit will be extracted.

   -  | *Symmetry*: In this protocol, symmetry refers only to rotational
        symmetry, also known in biology as radial symmetry. This
        symmetry is the property of volumes to preserve their shape
        after a partial turn around a symmetry axis.
      | Types of rotational symmetry included in this protocol are shown
        in . Two names appear in each case, the first one corresponds to
        *XMIPP* nomenclature of symmetry because we are using *XMIPP*
        package, and the second one (in brackets) follows the general
        nomenclature. Current nomenclature is :math:`ChimeraX`\ ’s
        nomenclature, which is, in turn, the same symmetry nomenclature
        of the International Union of Cristallography.

      .. figure:: Images_appendix/Fig108.pdf
         :alt: Protocol . Types of rotational symmetry.
         :name: fig:app_protocol_extractUnitCell_2
         :width: 40.0%

         Protocol . Types of rotational symmetry.

      -  Cyclic symmetry *Cn (Cn)*: Only one symmetry axis goes through
         the geometric center of the volume. Two more form parameters
         are shown when this type of symmetry is selected:

         -  *Symmetry Order*: Number of times (*n*) in which a volume
            shows the same shape when the volume rotates around the
            symmetry axis from 0 to 360º. If the same shape is only
            obtained after turning 360º, then *n = 1*. This means that
            the volume has no symmetry. *360º/n* determines the rotation
            angle.

         -  *offset*: Starting angle around Z axis.

      -  Dihedral symmetry *Dn (Dxn)*: Two perpendicular symmetry axes
         go through the geometric center of the volume. As in the case
         of cyclic symmetry, two more form parameters are shown when
         this type of symmetry is selected:

         -  *Symmetry Order*: Number of times (*n*) in which a volume
            shows the same shape when the volume rotates around both
            symmetry axes from 0 to 360º. Analogously, *360º/n*
            determines the rotation angle.

         -  *offset*: Starting angle around Z axis.

      -  Tetrahedral symmetry *T (T222)*: Four symmetry axes go from
         each vertex to the opposing face center (order 3), and three
         symmetry axes join opposing edges (order 2). *Symmetry order =
         12*.

      -  Octahedral symmetry *O (O)*: Three symmetry axes join opposing
         vertices (order 4), four symmetry axes join opposing face
         centers (order 3), and six symmetry axes join opposing edges
         (order 2). *Symmetry order = 24*.

      -  Icosahedral symmetries *I1 (I222), I2 (I222r), I3 (In25), I4
         (In25r)*: Six symmetry axes join opposing vertices (order 5),
         10 symmetry axes join baricenters of opposing faces (order 3),
         and 15 symmetry axes join opposing edges (order 2). *Symmetry
         order = 60*. Each type of icosahedral symmetry depends on its
         initial orientation. Check in
         (https://www.cgl.ucsf.edu/chimerax/docs/user/commands/shape.html)
         each icosahedral symmetry by writing in the command line:
         *shape icosahedron radius 50 orientation* (*222*: default,
         order 2 axes follow XYZ coordinate axes; *222r*: idem rotated
         90º around Z axis; *n25*: an order 2 axis and an order 5 axis
         follow Y and Z axes, respectively, *n25r*: idem rotated 90º
         around Z axis.

   -  *Inner Radius (px)*: Minimal distance from the geometric center
      that delimits inwards the part of the electron density map that
      will be included in the extracted volume. A wizard symbol on the
      right side of this parameter can be helpful to select this radius.

   -  *Outer Radius (px)*: Maximal distance from the geometric center
      that delimits outwards the part of the electron density map to be
      included in the extracted volume. In other words, the part
      extracted of the map electron density will be between the *Inner*
      and the *Outer Radius*. Again, the wizard symbol on the right side
      of this parameter can be helpful to select this radius.

   -  *Expand Factor*: Additional fraction of the asymmetrical unit cell
      that will be included in the extracted volume.

-  Protocol execution:

   | Press the *Execute* red button at the form bottom.
   | Adding specific extracted volume label is recommended in *Run name*
     section, at the form top. To add the label, open the protocol form,
     press the pencil symbol at the right side of *Run name* box,
     complete the label in the new opened window, press OK and, finally,
     close the protocol. If you want to run again this protocol, do not
     forget to set to *Restart* the *Run mode*.

-  Visualization of protocol results:

   After executing the protocol, press *Analyze Results* and a small
   window will be opened (). This window allows you to select between
   *chimerax* (:math:`ChimeraX` graphics window) and *slices*
   (:math:`ShowJ`, the default viewer), to visualize the volume.

   .. figure:: Images_appendix/Fig101.pdf
      :alt: Menu to select a visualization tool.
      :name: fig:app_protocol_volume_2
      :width: 70.0%

      Menu to select a visualization tool.

   -  *chimerax*: :math:`ChimeraX` graphics window

      Initial whole volume and extracted volume appear referred to the
      origin of coordinates in . To show the relative position of the
      volume, the three coordinate axes are represented; X axis (red), Y
      axis (yellow), and Z axis (blue) (). Coordinate axes, initial
      volume, and extracted map asymmetric unit are model numbers *#1*,
      *#2* and *#3*, respectively, in :math:`ChimeraX` *Models* panel.
      Volume coordinates and pixel size can be checked in
      :math:`ChimeraX` main menu *Tools -> Volume Data -> Map
      Coordinates: Origin index/ Voxel size*. WARNING: Take into account
      that coordinates appear in pixels while they have been introduced
      in Å.

   -  *slices*: :math:`ShowJ`

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
      | *xmipp3 - extract asymmetric unit -> ouputVolume*;
      | Volume (x, y, and z dimensions, sampling rate).

   -  | *SUMMARY* box:
      | Empty.
