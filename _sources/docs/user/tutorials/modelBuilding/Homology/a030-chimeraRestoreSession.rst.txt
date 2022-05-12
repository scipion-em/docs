.. _`app:chimeraRestoreSession`:

ChimeraX Restore Session protocol
=================================

Protocol designed to restore *ChimeraX* session, provided that this session has
been saved previously in *Scipion*. Currently, four protocols save *ChimeraX* sessions when *ChimeraX*
commands *scipionwrite*, *scipionss* or *scipioncombine* are used, **chimerax-rigid fit**,  **chimerax-operate**, **chimerax-model from template** and **chimerax-map subtraction** (Appendices :ref:`CHIMERAX Rigid fit <app:chimeraRigidFit>`, :ref:`Operate <app:chimeraOperate>`, :ref:`Model from template <app:modelFromTemplate>` and :ref:`Map subtraction <app:chimeraMapSubtraction>`, respectively). Restored sessions allow inspect any element contained in a previously saved *ChimeraX* session, perform *ChimeraX* operations, and finally save maps or
atomic structures.

-  | Requirements to run this protocol and visualize results:

   -  | *Scipion* plugin: **scipion-em**

   -  | *Scipion* plugin: **scipion-em-chimera**

-  | *Scipion* menu:
   | *Model building -> Tools-Calculators* (:numref:`model_building_app_protocol_chimera_3` (A))

   .. figure:: Images_appendix/Fig118.svg
      :alt: Protocol **chimerax-restore session**. A: Protocol location in *Scipion* menu. B: Protocol form.
      :name: model_building_app_protocol_chimera_3
      :align: center
      :width: 90.0%

      Protocol **chimerax-restore session**. A: Protocol location in *Scipion* menu. B: Protocol form.

-  | Protocol form parameters (:numref:`model_building_app_protocol_chimera_3` (B)):

   -  | *Input* section

      -  | *Input protocols*: Parameter that allows to select a particular protocol in which *ChimeraX* session has been saved in *Scipion*. As it was mentioned before, four protocols support this possibility (*ChimeraX rigid fit*, *ChimeraX operate*, *ChimeraX model from template* and *ChimeraX map subtraction*).

   -  | *Help* section

      | This section contains *ChimeraX* commands required to save *models* according to their reference volumes, which can also be saved if required. Remark that using *scipionwrite* command, session will be saved by default, without prejudice that it may be saved with *scipionss* command. *ChimeraX* sessions can be restored again by using this same **chimerax-restore session** protocol.

-  | Protocol execution:

   | Adding specific protocol label is recommended in *Run name*
     section, at the form top. To add the label, open the protocol form,
     press the pencil symbol at the right side of *Run name* box,
     complete the label in the new opened window, press OK and, finally,
     close the protocol. This label will be shown in the output summary
     content (see below). If you want to run again this protocol, do not
     forget to set to *Restart* the *Run mode*.

   | Press the *Execute* red button at the form bottom.

   | *ChimeraX* graphics window will be opened after executing the protocol showing
     the complete list of elements that appeared in *ChimeraX* graphics window when
     the session was saved, coordinate axes, electron density maps, and
     atomic structures. Steps to follow depend on the specific operation
     to carry out. New volumes or structures may be generated as usual
     in *ChimeraX*, and they can be combined or saved in the common way.

   -  | To combine two or more atomic structures, write in *ChimeraX* command line:

        ::

            scipioncombine #n1,n2

      | *#n1* and *#n2* are the respective *model* numbers of two
        different atomic structures. Optionally you can set the *model* number of the output combined structure *#n3*:

        ::

            scipioncombine #n1,n2 modelid n3

   -  | To save a map or an atomic structure generated with this protocol, write in *ChimeraX* command line:

        ::

            scipionwrite #n prefix userString_

      | Replace *#n* by model numbers shown in *ChimeraX Models* panel. *prefix*
        + string preferred by the user to easily identify the atomic
        structure is optional, although quite recomendable.


   -  | Close *ChimeraX* graphics window.

-  | Visualization of protocol results:

   | After executing the protocol, press *Analyze Results* and *ChimeraX* graphics window will be opened by default. Atomic structures and volumes are referred to the origin of coordinates in *ChimeraX*. To show the relative position of atomic structures and electron density volumes, the three coordinate axes are represented; X axis (red), Y axis (yellow), and Z axis (blue) (:numref:`model_building_app_protocol_volume_3`). In this particular case a *ChimeraX* graphics window identical to the input session will be opened and it will include every element saved lately.

-  | Summary content:

   -  | If an atomic structure is generated:

      -  | Protocol output (below *Scipion* framework):
         | *chimerax - operate -> output atomic structure name, starting
           with the prefix*;
         | *AtomStruct (pseudoatoms=True/ False, volume=True/ False)*.
         | Pseudoatoms is set to *True* when the structure is made of
           pseudoatoms instead of atoms. Volume is set to *True* when an
           electron density map is associated to the atomic structure.

      -  | *SUMMARY* box:
         | Produced files:
         | output atomic structure name, starting with the prefix (.cif
           file)
         | we have some result

   -  | If a volume is generated:

      -  | Protocol output (below *Scipion* framework):
         | *chimerax - operate -> output 3D map name*; *Volume (x, y,
           and z dimensions, sampling rate)*.

      -  | *SUMMARY* box:
         | Produced files:
         | output 3D map name, starting with the prefix (.mrc file)
         | we have some result
