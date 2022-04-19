.. _`app_localMonoRes`:

Local MonoRes protocol
======================

Protocol designed to apply the :math:`MonoRes` method
:raw-latex:`\citep{vilas2018}` in . :math:`MonoRes` is an automatic
accurate method developed to compute the local resolution of a 3D map
based on the calculation of the amplitude of the monogenic signal after
filtering the map at different frequencies.

-  Requirements to run this protocol and visualize results:

   -  plugin: *scipion-em*

   -  plugin: *scipion-em-xmipp*

   -  plugin: *scipion-em-chimera*

-  | menu:
   | *Model building -> Preprocess map* ( (A))

-  Protocol form parameters ( (B)):

   .. figure:: Images_appendix/Fig207.pdf
      :alt: Protocol . A: Protocol location in menu. B: Protocol form.
      :name: fig:app_localMonoRes_1
      :width: 90.0%

      Protocol . A: Protocol location in menu. B: Protocol form.

   -  *Would you like to use half volumes?*: Option “No” has been
      selected by default, with the box *Input Volume* to fill in with
      the volume, imported or generated in . However, since the noise
      estimation needed to determine the local resolution is based on
      half volumes, select “Yes” whenever half volumes are available. A
      couple of boxes will thus be opened to select both half volumes,
      *Volume Half 1* and *Volume Half 2*. If you want an appropriate
      computation of local resolution try to use half maps, or raw
      average maps otherwise. Avoid using postprocessed or sharpened
      maps.

   -  *Binary Mask*: Mask that will be overlapped to the map volume in
      order to indicate which points of the map are specimen and which
      are not.

   -  *Exclude area*: Advanced parameter to select part of the specimen
      that should be excluded from the estimation of local resolution,
      for example in viruses to exclude the inner genetic material or in
      membrane proteins to exclude fosfolipids. Remark that we are
      talking about part of the specimen (signal and not noise) in which
      we are simply not interested.

   -  *Extra parameters*:

      -  *Resolution Range (Å)*: Interval of resolution expected, from
         the maximum resolution (*High* = 0.0 by default), to the
         minimal resolution (*Low*) of the map volume. This parameter is
         empty by default and :math:`MonoRes` will try to estimate it.
         *Step* is an advanced parameter that indicates the fraction of
         resolution of each interval in the range contained between the
         max and min resolution.

      -  *Significance*: Advanced parameter that determines the
         significance of the hypothesis test computed to calculate the
         resolution (0.95 by default).

      -  *Mask threshold*: Advanced parameter that indicates the density
         value required to get a binary mask in case there is none (0.5
         by default). Density values below the threshold will be changed
         to 0 and values above the threshold will be changed to 1.

      -  *Consider noise gaussian?*: “No” by default has to be changed
         to “Yes” if you prefer to establish the premise that the noise
         follows a gaussian distribution.

-  | Protocol execution:
   | Adding specific map/structure label is recommended in *Run name*
     section, at the form top. To add the label, open the protocol form,
     press the pencil symbol at the right side of *Run name* box,
     complete the label in the new opened window, press OK and, finally,
     close the protocol. This label will be shown in the output summary
     content (see below). If you want to run again this protocol, do not
     forget to set to *Restart* the *Run mode*.
   | Press the *Execute* red button at the form bottom.

-  Visualization of protocol results:

   After executing the protocol, press *Analyze Results* and a menu
   window will be opened ():

   .. figure:: Images_appendix/Fig209.pdf
      :alt: Protocol . Menu to visualize results.
      :name: fig:app_localMonoRes_2
      :width: 70.0%

      Protocol . Menu to visualize results.

   -  *Show resolution slices*: Map resolution slices are opened with
      :math:`ShowJ` (https://github.com/I2PC/scipion/wiki/ShowJ), the
      default viewer.

   -  *Show original volume slices*: Original map slices are opened with
      :math:`ShowJ`.

   -  *Show resolution histogram*: Number of map voxels that show a
      certain resolution.

   -  *Colored resolution Slices and Volumes*: Box that allows to
      display local resolution of map and slices according to a specific
      color code.

      -  *Slice axis*: Select the perpendicular axis to visualize the
         slices. The *Z* axis is perpendicular to the screen.

      -  *Show colored slices*: Map slices 34, 45, 56 and 67 of local
         resolution along the axis selected previously.

      -  *Show selected slice*: Advanced parameter to show by default
         the 51 local resolution slide, or any other selected along the
         axis selected previously.

      -  *Show slice number*: Advanced parameter to select the slice
         number to be shown by *Show selected slice*.

      -  *Show Resolution map in ChimeraX*: The resolution map is shown
         using :math:`ChimeraX`. Left hand bar indicates resolution
         colour code.

      -  

         -  *Color scale options*: Highest value of the resolution
            range.

         -  *Lowest*: Lowest value of the resolution range.

         -  *Intervals*: Number of resolution intervals from the highest
            to the lowest range value.

         -  *Color set*: Color to apply to the local resolution map
            (http://matplotlib.org/1.3.0/examples/color/colormaps_reference.html).

         *Note*: Remark that on the right side you have a wizard to
         control color params.

-  Summary content:

   -  | Protocol output (below framework):
      | *xmipp3 - local MonoRes -> resolution_Volume*;
      | Volume (x, y, and z dimensions, sampling rate).

   -  | *SUMMARY* box:
      | *Highest resolution* and *Lowest resolution*.
