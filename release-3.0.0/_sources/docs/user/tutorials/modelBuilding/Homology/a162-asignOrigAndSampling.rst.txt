.. _`app:asignOrigAndSampling`:

Protocol to assign map sampling rate and origin of coordinates
==============================================================

Protocol designed to modify the values of sampling rate and origin of
coordinates of electron density maps that are already in the *Scipion* workflow.
Remark that the new map generated in the workflow will associate these
two attributes, samplig rate and origin of coordinates, ``WITHOUT``
modifying the map header. If you want to modify the map header inside *Scipion*,
for example to deposit it to EMDB, you should use the protocol :ref:`export to DB <app:exportToEMDB>`.

-  | Requirements to run this protocol and visualize results:

   -  | *Scipion* plugin: **scipion-em**

-  | *Scipion* menu: It does not appear in *Model building* view. Press ``Ctrl`` +  ``f`` and the pop up window to search a protocol will be opened (:numref:`model_building_app_protocol_assign_orig_and_sampling` (A)). Write any word related with the title of the protocol that you are looking for in the *Search* box. In this particular case we have written *origin*. Several protocols have been found related with this searching word. Select the third one dessigned for the purpose that we are interested in (**pwem-assign orig & sampling**).

   .. figure:: Images_appendix/Fig301.svg
      :alt: Protocol **assign Orig & Sampling**. A: Window to search the protocol. B: Protocol form.
      :name: model_building_app_protocol_assign_orig_and_sampling
      :align: center
      :width: 80.0%

      Protocol **assign Orig & Sampling**. A: Window to search the protocol. B: Protocol form.

-  Protocol form parameters (:numref:`model_building_app_protocol_assign_orig_and_sampling` (B)):

   - | *Input*  section

      -  | *Input Volume*: Include here any map previously downloaded or generated in *Scipion* that you would like to assing a new sampling rate and/or origin of coordinates.

      -  | *Set SamplingRate*: Select *Yes* if you want to give the map a new value of sampling rate. Then, a new form box will appear:

         -  | *Pixel size ("sampling rate")(Å/px)*: Write the new sampling rate value in the box. Remark that you have a wizard on the right to check the current value.

      -  | *Set origin of coordinates*: You have to choose between setting the previously origin of coordinates assigned in *Scipion* (option “No”) or another origin of coordinates (“Yes”). If you decide to set your own origin of coordinates (option “Yes”), a new form parameter (*Offset*) will appear below.

         -  | *Offset*: Write here x, y, and z coordinates of your preference (in Å). As in the case of the *Pixel size*, remark that you have a wizard on the right side of the parameter to check the header current coordinates of the origin.

-  | Protocol execution:

   | Adding specific volume label is recommended in *Run name* section, at the form top. To add the label, open the protocol form, press the pencil symbol at the right side of *Run name* box, complete the label in the new opened window, press OK, and finally, close the protocol. This label will be shown in the output summary content (see below). If you want to run again this protocol, do not forget to set to *Restart* the *Run mode*.

   | Press the *Execute* red button at the form bottom.

-  | Visualization of protocol results:

   | After executing the protocol, press *Analyze Results* and :math:`ShowJ`, the default *Scipion* viewer, will allow you to visualize the *slices* window of the map (:numref:`model_building_app_protocol_assign_orig_and_sampling_2`). The :math:`ShowJ` window menu (*File -> Open with ChimeraX*) allows to open the selected map in *ChimeraX* graphics window.

   -  | *slices*: `ShowJ <../../../user/showJ>`_

      .. figure:: Images_appendix/Fig302.svg
         :alt: Protocol **assign Orig & Sampling**. Gallery model of :math:`ShowJ` to visualize the map slices.
         :name: model_building_app_protocol_assign_orig_and_sampling_2
         :align: center
         :width: 65.0%

         Protocol **assign Orig & Sampling**. Gallery model of :math:`ShowJ` to visualize the map slices.

-  | Summary content:

   -  | Protocol output (below *Scipion* framework):
      | *pwem - assign Orig & Sampling -> ouputVolume*;
      | *Volume (x, y, and z dimensions, NEW sampling rate)*.

   -  | *SUMMARY* box:
      | *New Sampling*: New assigned value of sampling rate.
      | *New Origin*: Coordinates of the new assigned origin of coordinates.
