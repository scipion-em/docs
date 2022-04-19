Merging 3D Maps and Atomic Structures: Rigid Fitting
====================================================

Once we have the predicted of any structural element included in our
map, to fit that in the volume constitutes the next step in the modeling
workflow. Two protocols have been included in with this purpose,
(Appendix `[app:dockInMapProtocol] <#app:dockInMapProtocol>`__,
:raw-latex:`\citep{Liebschner2019}`) and (Appendix
`[app:chimeraRigidFit] <#app:chimeraRigidFit>`__). The first one allows
automatic fitting of in , while the second one only does it when and are
quite close, thus requiring manual fitting in advance. Although there is
no a general rule to fit and , because it will depend on the particular
problem and on our previous knowledge, in this tutorial we are going to
use application first, followed by the final in . Observe these two new
steps in the modeling workflow in .

.. figure:: Images/Fig67.pdf
   :alt: framework detailing the workflow to fit the first model of the
   human :math:`\alpha` subunit in the map asymmetric unit.
   :name: fig:scipion_workflow_rigidfit
   :width: 100.0%

   framework detailing the workflow to fit the first model of the human
   :math:`\alpha` subunit in the map asymmetric unit.

Initial rigid fit with 
-----------------------

Open protocol ( (1)), and complete the form with the the extracted map
asymmetric unit (2), the map resolution (3), the of atomic structure
previously saved in (4), and the number of copies of this atomic
structure that we’d like to fit in the map, 1 in this case (5). As an
additional exercise you can check the result of fitting two copies of
this structure in the initial input map.

.. figure:: Images/Fig18.pdf
   :alt: Rigid fit with protocol: Filling in the protocol form.
   :name: fig:dockInMap_protocol
   :width: 100.0%

   Rigid fit with protocol: Filling in the protocol form.

After executing the protocol ( (6)), you can check the docking results
clicking in (7). graphics window will be opened () showing the map and
the atomic structure in its initial location (pink) and fitted in the
map (green) ( (1)).

.. figure:: Images/Fig20.pdf
   :alt: Rigid fit with : View of docking results in .
   :name: fig:dockInMap_results
   :width: 85.0%

   Rigid fit with : View of docking results in .

A rough inspection of the in (remark the location of the group, for
example, which should be moved slightly to the right side) shows that
the fitting could be improved a little. The second protocol, , will help
in this purpose.

 Completing rigid fit with 
---------------------------

| : As we already advised previously, we are going to use a -derived
  protocol (, Appendix
  `[app:chimeraRigidFit] <#app:chimeraRigidFit>`__). Remark that this
  use of is completely different from the use of as a visualization
  tool. By using the graphics window, opening it from the button , we
  can observe protocol results but we CANNOT save anything in . However,
  using as a tool, as it is the case in -derived protocols, we can
  perform different tasks, taking advantage of the available tools and,
  finally, we CAN save the obtained results and the working session in .
| To complete the rigid fitting of the generated in the previous step,
  open the protocol , include again the map of the asymmetrical unit
  (2), and the just fitted of the human :math:`\alpha` subunit (3), and
  execute the protocol (4).

.. figure:: Images/Fig21.pdf
   :alt: Completing the rigid fit protocol form.
   :name: fig:chimera_rigid_fit
   :width: 100.0%

   Completing the rigid fit protocol form.

Once opened the graphical window, we can complete the fitting of the to
the , by command line or through the GUI.

-  | By command line, considering that and have numbers and ( (B)):

-  By the GUI: Select in the upper main menu . A small window will be
   opened ( (A)). Select the appropriate to fit in the and press (1) to
   allow the automatic rigid fitting.

| A slight movement to the right perfectly fits and , as can be observed
  in ( (B)). To facilitate the visual inspection of the fitting we can
  replace the view of the map by as indicated in (A). Observe this time
  the right placement of the group in the density.
| To use the side view as additional tool to observe the fit, select in
  the upper main menu .

.. figure:: Images/Fig22.pdf
   :alt: Fit in map with .
   :name: fig:chimera_fit_in_map
   :width: 85.0%

   Fit in map with .

| To track the fitted in we have to save it as fitted :math:`model` of
  the :math:`\alpha` subunit in the command line before closing the
  window:
| The string that we have included as in the command line will allow us
  to follow the atomic structure in a more simple manner. In particular,
  if you click ( (6)) the graphics window will open again and you can
  check the in the the name of the saved atomic structure () in the
  panel of (1). Interestingly, the suffix number of the saved atomic
  structure () stands for the ID protocol number and you can check it by
  simply surfing the mouse over the protocol ( (5)).

.. figure:: Images/Fig23.pdf
   :alt: View in graphics window of the initial of human :math:`\alpha`
   subunit fitted to the asymmetrical unit of the 3D map.
   :name: fig:chimera_fit_results_2
   :width: 85.0%

   View in graphics window of the initial of human :math:`\alpha`
   subunit fitted to the asymmetrical unit of the 3D map.
