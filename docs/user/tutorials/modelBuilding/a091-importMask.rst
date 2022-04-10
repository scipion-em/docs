.. _`app:importMask`:

Import mask protocol
====================

Protocol designed to import a mask in from a file of user’s computer.
Modifying the size of a previous mask is possible simply by changing the
mask’s sampling rate.

-  Requirements to run this protocol and visualize results:

   -  plugin:

-  menu: It does not appear in view. Press + and the pop up window to
   search a protocol will be opened (( (A)). Write any word related with
   the title of the protocol that you are looking for in the box. In
   this particular case we have written . Several protocols have been
   found related with this search word. Select the first one dessigned
   for the purpose that we are interested in ().

-  Protocol form parameters ( (B)):

   .. figure:: Images_appendix/Fig304.pdf
      :alt: A. Protocol . A: Window to search the protocol. B: Protocol
      form.
      :name: fig:app_protocol_import_mask
      :width: 90.0%

      A. Protocol . A: Window to search the protocol. B: Protocol form.

-  section

   -  : Open the browser on the right to select in your computer the
      path to the previously saved mask.

   -  (Å/px): Write the new sampling rate rate value in the box.

-  Protocol execution:

   | Adding specific mask label is recommended in section, at the form
     top. To add the label, open the protocol form, press the pencil
     symbol at the right side of box, complete the label in the new
     opened window, press OK, and finally, close the protocol. This
     label will be shown in the output summary content (see below). If
     you want to run again this protocol, do not forget to set to the .
   | Press the red button at the form bottom.

-  Visualization of protocol results:

   After executing the protocol, press and :math:`ShowJ`, the default
   viewer, will allow you to visualize the window of the mask (). The
   :math:`ShowJ` window menu () allows to open the selected map in
   :math:`ChimeraX` graphics window.

   -  : :math:`ShowJ`

      https://github.com/I2PC/scipion/wiki/ShowJ

-  Summary content:

   -  | Protocol output (below framework):
      | ;
      | .

   -  | box:
      | : The specific selected path to the mask in your computer should
        appear here.
