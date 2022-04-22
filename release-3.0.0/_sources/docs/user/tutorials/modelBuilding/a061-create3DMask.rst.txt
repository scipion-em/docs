.. _`app:create3DMask`:

Create 3D Mask protocol
=======================

Protocol designed to create a mask, *i.e.*, a wrapping surface
able to delimit a volume or subunit of interest, in order to modify the
density values within or outside it. This mask can be created with a
given geometrical shape (sphere, cube, cylinder...) or obtained from
operating on a 3D volume or a previous mask.

-  Requirements to run this protocol and visualize results:

   -  *Scipion* plugin: **scipion-em**

   -  *Scipion* plugin: **scipion-em-xmipp**

-  | *Scipion* menu:
   | *Model building -> Preprocess map* (:numref:`model_building_create3DMask_1` (A))

   .. figure:: Images_appendix/Fig206.svg
      :alt: Protocol **xmipp-create 3d mask**. A: Protocol location in *Scipion* menu. B, C: Protocol form.
      :name: model_building_create3DMask_1
      :align: center
      :width: 90.0%

      Protocol **xmipp-create 3d mask**. A: Protocol location in *Scipion* menu. B, C: Protocol form.

-  Protocol form parameters (:numref:`model_building_create3DMask_1` (B: Mask generation; C: Postprocessing)):

   -  *Mask generation*

      -  *Mask source*: Selection of one of the next three possible
         types of sources for the mask, the map volume provided by the
         user, a specific geometrical design or a feature file.

         #. *Volume*

            -  *Input volume*: Electron density map previously
               downloaded or generated in *Scipion*.

            -  *Operation*: Approach applied to generate the mask:

               #. *Threshold*: By establishing a particular density
                  *Threshold* (write here this threshold value).

               #. *Segment*: Segmentation process according to:

                  - *Number of voxels*\  (write here that value).

                  - *Number of aminoacids*\  (write here that value).

                  - *Dalton mass*\  (write here that value).

                  - *Automatic*

            -  *Only postprocess*: Use only the methods described in the
               tap *Postprocessing* (see below).

         #. *Geometry*

            -  *Sampling Rate (Å/px)*: Size of voxel dimensions in Å.

            -  *Mask size (px)*: Mask dimensions in number of pixels.

            -  *Mask type*: Sphere, box, crown, cylinder, Gaussian,
               raised cosine and raised crown. Dimensions of each one of
               these geometric shapes have to be assigned in pixels:
               Radius of the sphere (half size of the mask by default);
               box size; inner and outer radius of the crown, raised
               cosine and raised crown (half size of the mask by
               default); height of cylinder (mask size by default);
               Gaussian sigma (mask size/6 by default); and border decay
               or fall-off of the two borders of the crown (0 by
               default).

            -  *Shift center of the mask?*: By selecting “Yes”, the mask
               will be shifted to a new origin of coordinates *X, Y, Z*.

         #. *Feature File*: Select with the browser the feature file in
            your computer.

   -  *Postprocessing*

      -  *Remove small objects*: Selection of “Yes” allows to ignore
         ligands of the map volume below a certain size (in voxels).

      -  *Keep largest component*: By selecting “Yes” a mask will be
         generated considering only the largest element of the map
         volume, ignoring the rest.

      -  *Symmetrize mask*: By selecting “Yes” a symmetrized mask will
         be generated according to a specific symmetry group (look at
         `XMIPP Symmetry <https://github.com/I2PC/xmipp-portal/wiki/Symmetry>`_). *c1*
         symmetry indicates no symmetry, by default.

      -  *Apply morphological operation*: Slight modifications of the
         mask can be applied by dilation or erosion of the density
         region (*Structural element size*: One voxel by default).
         Combinations of dilation and erosion allow closing or opening
         empty spaces of density in the map volume.

      -  *Invert the mask*: This option allows to invert the values of
         density regarding the wrapping surface of the mask, masking the
         outer part instead the inner part.

      -  *Smooth borders*: Mask borders can be smoothed by applying a
         convolution of the mask with a Gaussian. The Gaussian sigma (in
         pixels) has to be supplied.

-  | Protocol execution:
   | Adding specific mask label is recommended in *Run name* section, at
     the form top. To add the label, open the protocol form, press the
     pencil symbol at the right side of *Run name* box, complete the
     label in the new opened window, press OK and, finally, close the
     protocol. This label will be shown in the output summary content
     (see below). If you want to run again this protocol, do not forget
     to set to *Restart* the *Run mode*.

   | Press the *Execute* red button at the form bottom.

-  Visualization of protocol results:

   After executing the protocol, press *Analyze Results* and
   `ShowJ <https://scipion-em.github.io/docs/docs/user/showJ>`_, the
   default viewer, will open the mask by slices (:numref:`model_building_create3Dmask_2`). *ShowJ*
   window menu (*File -> Open with ChimeraX*) allows to open the mask
   volume in *ChimeraX* graphics window.

-  Summary content:

   -  | Protocol output (below *Scipion* framework):
      | *xmipp3 - create 3d mask -> ouputMask*;
      | VolumeMask (x, y, and z dimensions, sampling rate).

   -  | *SUMMARY* box:
      | Details about *Mask creation* and *Mask processing*.
