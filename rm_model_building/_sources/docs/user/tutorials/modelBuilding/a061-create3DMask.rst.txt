.. _`app:create3DMask`:

Create 3D Mask protocol
=======================

Protocol designed to create a mask, :math:`i.e.`, a wrapping surface
able to delimit a volume or subunit of interest, in order to modify the
density values within or outside it. This mask can be created with a
given geometrical shape (sphere, cube, cylinder...) or obtained from
operating on a 3D volume or a previous mask.

-  Requirements to run this protocol and visualize results:

   -  plugin:

   -  plugin:

-  | menu:
   | ( (A))

   .. figure:: Images_appendix/Fig206.pdf
      :alt: Protocol . A: Protocol location in menu. B, C: Protocol
      form.
      :name: fig:create3DMask_1
      :width: 90.0%

      Protocol . A: Protocol location in menu. B, C: Protocol form.

-  Protocol form parameters ( (B: Mask generation; C: Postprocessing)):

   -  

      -  : Selection of one of the next three possible types of sources
         for the mask, the map volume provided by the user, a specific
         geometrical design or a feature file.

         #. 

            -  : Electron density map previously downloaded or generated
               in .

            -  : Approach applied to generate the mask:

               #. : By establishing a particular density (write here
                  this threshold value).

               #. : Segmentation process according to:

               #. \*\* (write here that value).

               #. \*\* (write here that value).

               #. \*\* (write here that value).

               #. \*\*

            -  : Use only the methods described in the tap (see below).

         #. 

            -  : Size of voxel dimensions in Å.

            -  : Mask dimensions in number of pixels.

            -  : Sphere, box, crown, cylinder, Gaussian, raised cosine
               and raised crown. Dimensions of each one of these
               geometric shapes have to be assigned in pixels: Radius of
               the sphere (half size of the mask by default); box size;
               inner and outer radius of the crown, raised cosine and
               raised crown (half size of the mask by default); height
               of cylinder (mask size by default); Gaussian sigma (mask
               size/6 by default); and border decay or fall-off of the
               two borders of the crown (0 by default).

            -  : By selecting “Yes”, the mask will be shifted to a new
               origin of coordinates .

         #. : Select with the browser the feature file in your computer.

   -  

      -  : Selection of “Yes” allows to ignore ligands of the map volume
         below a certain size (in voxels).

      -  : By selecting “Yes” a mask will be generated considering only
         the largest element of the map volume, ignoring the rest.

      -  : By selecting “Yes” a symmetrized mask will be generated
         according to a specific symmetry group (look at
         http://xmipp.cnb.csic.es/twiki/bin/view/Xmipp/Symmetry).
         symmetry indicates no symmetry, by default.

      -  : Slight modifications of the mask can be applied by dilation
         or erosion of the density region (: One voxel by default).
         Combinations of dilation and erosion allow closing or opening
         empty spaces of density in the map volume.

      -  : This option allows to invert the values of density regarding
         the wrapping surface of the mask, masking the outer part
         instead the inner part.

      -  : Mask borders can be smoothed by applying a convolution of the
         mask with a Gaussian. The Gaussian sigma (in pixels) has to be
         supplied.

-  | Protocol execution:
   | Adding specific mask label is recommended in section, at the form
     top. To add the label, open the protocol form, press the pencil
     symbol at the right side of box, complete the label in the new
     opened window, press OK and, finally, close the protocol. This
     label will be shown in the output summary content (see below). If
     you want to run again this protocol, do not forget to set to the .
   | Press the red button at the form bottom.

-  Visualization of protocol results:

   After executing the protocol, press and :math:`ShowJ`
   (https://github.com/I2PC/scipion/wiki/ShowJ), the default viewer,
   will open the mask by slices (). The :math:`ShowJ` window menu ()
   allows to open the mask volume in :math:`ChimeraX` graphics window.

-  Summary content:

   -  | Protocol output (below framework):
      | ;
      | VolumeMask (x, y, and z dimensions, sampling rate).

   -  | box:
      | Details about and .
