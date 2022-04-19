.. _`app:asignOrigAndSampling`:

Protocol to assign map sampling rate and origin of coordinates
==============================================================

Protocol designed to modify the values of sampling rate and origin of
coordinates of electron density maps that are already in the workflow.
Remark that the new map generated in the workflow will associate these
two attributes, samplig rate and origin of coordinates, WITHOUT
modifying the map header. If you want to modify the map header inside ,
for example to deposit it to EMDB, you should use the protocol .

-  Requirements to run this protocol and visualize results:

   -  plugin:

-  menu: It does not appear in view. Press + and the pop up window to
   search a protocol will be opened (( (A)). Write any word related with
   the title of the protocol that you are looking for in the box. In
   this particular case we have written . Several protocols have been
   found related with this searching word. Select the third one
   dessigned for the purpose that we are interested in ().

   .. figure:: Images_appendix/Fig301.pdf
      :alt: Protocol . A: Window to search the protocol. B: Protocol
      form.
      :width: 80.0%

      Protocol . A: Window to search the protocol. B: Protocol form.

-  Protocol form parameters ( (B)):

   -  section

      -  : Include here any map previously downloaded or generated in
         that you would like to assing a new sampling rate and/or origin
         of coordinates.

      -  : Select if you want to give the map a new value of sampling
         rate. Then, a new form box will appear:

         -  (Å/px): Write the new sampling rate rate value in the box.
            Remark that you have a wizard on the right to check the
            current value.

      -  : You have to choose between setting the previously origin of
         coordinates assigned in (option “No”) or another origin of
         coordinates (“Yes”). If you decide to set your own origin of
         coordinates (option “Yes”), a new form parameter () will appear
         below.

         -  : Write here x, y, and z coordinates of your preference (in
            Å). As in the case of the , remark that you have a wizard on
            the right side of the parameter to check the header current
            coordinates of the origin.

-  Protocol execution:

   | Adding specific volume label is recommended in section, at the form
     top. To add the label, open the protocol form, press the pencil
     symbol at the right side of box, complete the label in the new
     opened window, press OK, and finally, close the protocol. This
     label will be shown in the output summary content (see below). If
     you want to run again this protocol, do not forget to set to the .
   | Press the red button at the form bottom.

-  Visualization of protocol results:

   After executing the protocol, press and :math:`ShowJ`, the default
   viewer, will allow you to visualize the window of the map (). The
   :math:`ShowJ` window menu () allows to open the selected map in
   :math:`ChimeraX` graphics window.

   -  : :math:`ShowJ`

      https://github.com/I2PC/scipion/wiki/ShowJ

      .. figure:: Images_appendix/Fig302.pdf
         :alt: Protocol . Gallery model of :math:`ShowJ` to visualize
         the map slices.
         :width: 65.0%

         Protocol . Gallery model of :math:`ShowJ` to visualize the map
         slices.

-  Summary content:

   -  | Protocol output (below framework):
      | ;
      | .

   -  | box:
      | : New assigned value of sampling rate.
      | : Coordinates of the new assigned origin of coordinates.
