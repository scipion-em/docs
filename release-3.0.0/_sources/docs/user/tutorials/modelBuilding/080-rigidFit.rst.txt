Merging 3D Maps and Atomic Structures: Rigid Fitting
====================================================

Once we have the predicted *model* of any structural element included in our
map, to fit that *model* in the volume constitutes the next step in the modeling
workflow. Two protocols have been included in *Scipion* with this purpose, **phenix-dock in map**
(Appendix :ref:`PHENIX Dock in map <app:dockInMapProtocol>` :cite:p:`Liebschner2019`) and **chimerax-rigid fit** (Appendix :ref:`CHIMERAX Rigid fit <app:chimeraRigidFit>`). The first one allows
automatic fitting of *models* in *maps*, while the second one only does it when *model* and *map* are
quite close, thus requiring manual fitting in advance. Although there is
no a general rule to fit *map* and *model*, because it will depend on the particular
problem and on our previous knowledge, in this tutorial we are going to
use **phenix-dock in map** application first, followed by the final *Fit in map* in **chimerax-rigid fit**. Observe these two new
steps in the modeling *Scipion* workflow in :numref:`model_building_scipion_workflow_rigidfit`.

.. figure:: Images/Fig67.svg
   :alt: *Scipion* framework detailing the workflow to fit the first model of the human *Hgb* :math:`\alpha` subunit in the map asymmetric unit.
   :name: model_building_scipion_workflow_rigidfit
   :align: center
   :width: 100.0%

   *Scipion* framework detailing the workflow to fit the first model of the human *Hgb* :math:`\alpha` subunit in the map asymmetric unit.

Initial rigid fit with *PHENIX dock in map*
-----------------------

Open **phenix-dock in map** protocol (:numref:`model_building_dockInMap_protocol` (1)), and complete the form with the the extracted map
asymmetric unit (2), the map resolution (3), the *model* of atomic structure
previously saved in *ChimeraX* (4), and the number of copies of this atomic
structure that we’d like to fit in the map, 1 in this case (5). As an
additional exercise you can check the result of fitting two copies of
this structure in the initial input map.

.. figure:: Images/Fig18.svg
   :alt: Rigid fit with **phenix-dock in map** protocol: Filling in the protocol form.
   :name: model_building_dockInMap_protocol
   :align: center
   :width: 100.0%

   Rigid fit with **phenix-dock in map** protocol: Filling in the protocol form.

After executing the protocol **phenix-dock in map** (:numref:`model_building_dockInMap_protocol` (6)), you can check the docking results
clicking in *Analyze Results* (7). *ChimeraX* graphics window will be opened (:numref:`model_building_dockInMap_results`) showing the map and
the atomic structure *modeled* in its initial location (pink) and fitted in the
map (green) (:numref:`model_building_dockInMap_results` (1)).

.. figure:: Images/Fig20.svg
   :alt: Rigid fit with **phenix-dock in map**: View of docking results in *ChimeraX*.
   :name: model_building_dockInMap_results
   :align: center
   :width: 85.0%

   Rigid fit with **phenix-dock in map**: View of docking results in *ChimeraX*.

A rough inspection of the *placed_model* in :numref:`model_building_dockInMap_results` (remark the location of the *HEME* group, for
example, which should be moved slightly to the right side) shows that
the fitting could be improved a little. The second protocol, **chimerax-rigid fit**, will help
in this purpose.

Completing rigid fit with *CHIMERAX rigid fit*
---------------------------

| ``NOTE before starting!!!:`` As we already advised previously, we are going to use a *ChimeraX*-derived
  protocol (**chimerax-rigid fit**, Appendix :ref:`CHIMERA Rigid fit <app:chimeraRigidFit>`). Remark that this
  use of *ChimeraX* is completely different from the use of *ChimeraX* as a visualization
  tool. By using the *ChimeraX* graphics window, opening it from the *Scipion* button *Analyze Results*, we
  can observe protocol results but we CANNOT save anything in *Scipion*. However,
  using *ChimeraX* as a tool, as it is the case in *Scipion* *ChimeraX*-derived protocols, we can
  perform different tasks, taking advantage of the available *ChimeraX* tools and,
  finally, we CAN save the obtained results and the working session in *Scipion*.

| To complete the rigid fitting of the *model* generated in the previous step,
  open the protocol **chimerax-rigid fit**, include again the map of the asymmetrical unit
  (2), and the just fitted *model* of the human *metHgb* :math:`\alpha` subunit (3), and
  execute the protocol (4).

.. figure:: Images/Fig21.svg
   :alt: Completing the *ChimeraX* rigid fit protocol form.
   :name: model_building_chimera_rigid_fit
   :align: center
   :width: 100.0%

   Completing the *ChimeraX* rigid fit protocol form.

Once opened the *ChimeraX* graphical window, we can complete the fitting of the *model* to
the *map*, by command line or through the *ChimeraX* GUI.

-  | By *ChimeraX* command line, considering that *map* and *model* have *ID* numbers *#2* and *#3* (:numref:`model_building_chimera_fit_in_map` (B)):
::

     fitmap #3 inMap #2

-  By the *ChimeraX* GUI: Select in the upper main menu *Tools -> Volume Data -> Fit in Map*. A small window will be
   opened (:numref:`model_building_chimera_fit_in_map` (A)). Select the appropriate *model* to fit in the *map* and press *Fit* (1) to
   allow the automatic rigid fitting.

| A slight movement to the right perfectly fits *map* and *model*, as can be observed
  in (:numref:`model_building_chimera_fit_in_map` (B)). To facilitate the visual inspection of the fitting we can
  replace the *surface* view of the map by *mesh* as indicated in (A). Observe this time
  the right placement of the *HEME* group in the *map* density.
| To use the side view as additional tool to observe the fit, select in
  the upper main menu *Tools -> General -> Side View*.

.. figure:: Images/Fig22.svg
   :alt: Fit in map with *ChimeraX*.
   :name: model_building_chimera_fit_in_map
   :align: center
   :width: 85.0%

   Fit in map with *ChimeraX*.

| To track the *ChimeraX* fitted *model* in *Scipion* we have to save it as fitted *model* of
  the *metHgb* :math:`\alpha` subunit in the *ChimeraX* command line before closing the *ChimeraX*
  window:
::

     scipionwrite #3 prefix Hgb_alpha_
     exit

| The string that we have included as *prefix* in the command line will allow us
  to follow the atomic structure in a more simple manner. In particular,
  if you click *Analyze Results* (:numref:`model_building_chimera_rigid_fit` (6)) the *ChimeraX* graphics window will open again and you can
  check the *prefix* in the the name of the saved atomic structure *(Hgb_alpha_Atom_struct_3_003753)* in the *Models*
  panel of :numref:`model_building_chimera_fit_results_2` (1). Interestingly, the suffix number of the saved atomic
  structure *(003753)* stands for the ID protocol number and you can check it by
  simply surfing the mouse over the protocol (:numref:`model_building_chimera_rigid_fit` (5)).

.. figure:: Images/Fig23.svg
   :alt: View in *ChimeraX* graphics window of the initial *model* of human *Hgb* :math:`\alpha` subunit fitted to the asymmetrical unit of the 3D map.
   :name: model_building_chimera_fit_results_2
   :align: center
   :width: 85.0%

   View in *ChimeraX* graphics window of the initial *model* of human *Hgb* :math:`\alpha` subunit fitted to the asymmetrical unit of the 3D map.
