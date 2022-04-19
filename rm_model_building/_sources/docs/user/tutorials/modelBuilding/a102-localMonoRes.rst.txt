.. _`app:localMonoRes`:

Local MonoRes protocol
======================

Protocol designed to apply the :math:`MonoRes` method
:raw-latex:`\citep{vilas2018}` in . :math:`MonoRes` is an automatic
accurate method developed to compute the local resolution of a 3D map
based on the calculation of the amplitude of the monogenic signal after
filtering the map at different frequencies.

-  Requirements to run this protocol and visualize results:

   -  plugin:

   -  plugin:

   -  plugin:

-  | menu:
   | ( (A))

-  Protocol form parameters ( (B)):

   .. figure:: Images_appendix/Fig207.pdf
      :alt: Protocol . A: Protocol location in menu. B: Protocol form.
      :name: fig:app_localMonoRes_1
      :width: 90.0%

      Protocol . A: Protocol location in menu. B: Protocol form.

   -  : Option “No” has been selected by default, with the box to fill
      in with the volume, imported or generated in . However, since the
      noise estimation needed to determine the local resolution is based
      on half volumes, select “Yes” whenever half volumes are available.
      A couple of boxes will thus be opened to select both half volumes,
      and . If you want an appropriate computation of local resolution
      try to use half maps, or raw average maps otherwise. Avoid using
      postprocessed or sharpened maps.

   -  : Mask that will be overlapped to the map volume in order to
      indicate which points of the map are specimen and which are not.

   -  : Advanced parameter to select part of the specimen that should be
      excluded from the estimation of local resolution, for example in
      viruses to exclude the inner genetic material or in membrane
      proteins to exclude fosfolipids. Remark that we are talking about
      part of the specimen (signal and not noise) in which we are simply
      not interested.

   -  :

      -  : Interval of resolution expected, from the maximum resolution
         ( = 0.0 by default), to the minimal resolution () of the map
         volume. This parameter is empty by default and :math:`MonoRes`
         will try to estimate it. is an advanced parameter that
         indicates the fraction of resolution of each interval in the
         range contained between the max and min resolution.

      -  : Advanced parameter that determines the significance of the
         hypothesis test computed to calculate the resolution (0.95 by
         default).

      -  : Advanced parameter that indicates the density value required
         to get a binary mask in case there is none (0.5 by default).
         Density values below the threshold will be changed to 0 and
         values above the threshold will be changed to 1.

      -  : “No” by default has to be changed to “Yes” if you prefer to
         establish the premise that the noise follows a gaussian
         distribution.

-  | Protocol execution:
   | Adding specific map/structure label is recommended in section, at
     the form top. To add the label, open the protocol form, press the
     pencil symbol at the right side of box, complete the label in the
     new opened window, press OK and, finally, close the protocol. This
     label will be shown in the output summary content (see below). If
     you want to run again this protocol, do not forget to set to the .
   | Press the red button at the form bottom.

-  Visualization of protocol results:

   After executing the protocol, press and a menu window will be opened
   ():

   .. figure:: Images_appendix/Fig209.pdf
      :alt: Protocol . Menu to visualize results.
      :name: fig:app_localMonoRes_2
      :width: 70.0%

      Protocol . Menu to visualize results.

   -  : Map resolution slices are opened with :math:`ShowJ`
      (https://github.com/I2PC/scipion/wiki/ShowJ), the default viewer.

   -  : Original map slices are opened with :math:`ShowJ`.

   -  : Number of map voxels that show a certain resolution.

   -  : Box that allows to display local resolution of map and slices
      according to a specific color code.

      -  : Select the perpendicular axis to visualize the slices. The
         axis is perpendicular to the screen.

      -  : Map slices 34, 45, 56 and 67 of local resolution along the
         axis selected previously.

      -  : Advanced parameter to show by default the 51 local resolution
         slide, or any other selected along the axis selected
         previously.

      -  : Advanced parameter to select the slice number to be shown by
         .

      -  : The resolution map is shown using :math:`ChimeraX`. Left hand
         bar indicates resolution colour code.

      -  

         -  : Highest value of the resolution range.

         -  : Lowest value of the resolution range.

         -  : Number of resolution intervals from the highest to the
            lowest range value.

         -  : Color to apply to the local resolution map
            (http://matplotlib.org/1.3.0/examples/color/colormaps_reference.html).

         : Remark that on the right side you have a wizard to control
         color params.

-  Summary content:

   -  | Protocol output (below framework):
      | ;
      | Volume (x, y, and z dimensions, sampling rate).

   -  | box:
      | and .
