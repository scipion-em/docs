.. _`app:ccp4CootRefinement`:

CCP4 Coot Refinement protocol
=============================

| Protocol designed to interactively fit and refine atomic structures,
  in real space, regarding electron density maps in *Scipion* by using
  *Coot* :cite:p:`emsley2010`. This protocol integrates
  *Coot* 3D graphics display functionality in *Scipion*, supporting
  accession to *Coot* input and output data in the general model
  building workflow.

| *COOT*, acronym of Crystallopgraphic Object-Oriented Toolkit,
  gathers several tools useful to perform mostly interactive modeling
  procedures and is integrated in CCP4 software suite (`CCP4 <https://www.ccp4.ac.uk/?page_id=204>`_).
  Initially applicable to X-ray data, some modifications of *Coot*
  also allow to model atomic structures regarding electron density maps
  obtained from cryo-EM :cite:p:`brown2015`. Additional
  instructions to use *Coot* can be found in `COOT <https://www2.mrc-lmb.cam.ac.uk/personal/pemsley/coot/>`_. Remark in
  `COOT mouse and keyboard <https://www2.mrc-lmb.cam.ac.uk/personal/pemsley/coot/web/docs/coot.html#Mousing-and-Keyboarding>`_ mouse requirements to get the best functioning.

-  | Requirements to run this protocol and visualize results:

   -  | *Scipion* plugin: **scipion-em**

   -  | *Scipion* plugin: **scipion-em-ccp4**

   -  | **CCP4** software suite (from version 7.0.056 to 7.1)

   -  | *Scipion* plugin: **scipion-em-chimera**

-  | *Scipion* menu:
   | *Model building -> Flexible fitting* (:numref:`model_building_app_protocol_coot_1` (A))

   .. figure:: Images_appendix/Fig119.svg
      :alt: Protocol **ccp4-coot refinement**. A: Protocol location in *Scipion* menu. B: Protocol form.
      :name: model_building_app_protocol_coot_1
      :align: center
      :width: 90.0%

      Protocol **ccp4-coot refinement**. A: Protocol location in *Scipion* menu. B: Protocol form.

-  | Protocol form parameters (:numref:`model_building_app_protocol_coot_1` (B)):

   -  | *Input* section

      -  | *Input Volume/s*: At least one or several electron density maps previously downloaded or generated in *Scipion*. The density volume regarding to which an atomic structure has to be modeled has to be included in this volume list.

      -  | *Normalize*: Parameter set to “Yes” by default to perform normalization of map electron density levels according to *Coot* requirements ([0, 1]). This normalization approximates cryo-EM density data to maps obtained from X-ray crystallography because it diminishes Z-score (number of standard deviations) variation of map values.

      -  | *Atomic structure to be refined*: Mandatory param to load an atomic structure previously downloaded or generated in *Scipion*. This structure will be fitted and refined according to a particular density volume.

      -  | *Other reference atomic structures*: Additional atomic structures previously downloaded or generated in *Scipion* that may be helpful in the refinement process.

   -  | *Help* section

      | This section contains *Coot* commands to make easier some interactive refinement steps and to save refined atomic structures. Their reference volumes will be saved by default with the refined atomic structures. Here you are an overview of these commands:

      -  | Automatically moving from one chain to another in an atomic structure:

         -  | Press ``x`` in the keyboard to move from one chain to the previous one.

         -  | Press ``X`` to change from one chain to the next one.

      -  | Initializing global variables:
         | Press ``U`` in your keyboard.

      -  | Semi-automatic refinement of small groups of residues (10 to
           15):

         | As soon as *Coot* protocol is executed, the text file *coot.ini* will be saved in the project folder */Runs/00XXXX_CootRefine/extra/* (:numref:`model_building_app_protocol_coot_6` (1, 2)). This file content has to be modified according to our atomic structure model in this way:

         -  | *imol*: *#0* has to be replaced by the number of the molecule that has to be refined. This number appears detailed in *Coot* main menu *Display Manager* (:numref:`model_building_app_protocol_coot_2` (B, red arrow)).

         -  | *aa_main_chain*: *A* has to be replaced by the name of the molecule chain that has to be refined.

         -  | *aa_auxiliary_chain*: *AA*, name of the small chain of 10-15 residues, can be optionally replaced by other name.

         -  | *aaNumber*: *#100* has to be replaced by the position of the residue from which the refinement has to start.

         -  | *step*: *#10* will be replaced by the desired small step of residues that gets flexible enough to select other conformation of this auxiliary chain.

         | Save *coot.ini* text file after modifying it. Go to the residue position indicated in *aaNumber*, initialize global variables with ``U``, and pres ``z`` or ``Z`` in the keyboard to refine those *aaNumber* residues upstream or downstream, respectively.

      -  | Printing *Coot* environment:
         | Press ``E`` in the keyboard.

      -  | Saving an atomic structure after an interactive working
           session with *Coot*:

         | *Coot Python Scripting* window will be opened with *Coot* main menu *Calculate -> Scripting... -> Python...* (:numref:`model_building_app_protocol_coot_2` (A)). By writing *scipion_write()*, molecule *#0* will be saved by default in *Scipion*. Molecule number can be checked in *Coot* main menu *Display Manager* (:numref:`model_building_app_protocol_coot_2` (B, red arrow)). Saving the molecule this way is equivalent to press ``w`` in the keyboard.

         | The number *#n* of the specific molecule has to be written in brackets to save any other molecule than *#0*.

         | Although the name of the saved atomic structure is *coot_XXXXXX_Imol_YYYY_version_ZZZZ.pdb* by default (*XXXXXX* is the protocol box number, *YYYY* the *model* number and *ZZZZ* the number of times that the molecule has been saved), other names/labels of your preference are also allowed. That name/label has to be introduced with *scipion_write()* command, as it is detailed in the example (:numref:`model_building_app_protocol_coot_2` (A)). The addition of *.pdb* extension is not required.

         | If no more interactive sessions with *Coot* are planned, after saving the atomic structure, *Coot* can be definitively closed by pressing ``e`` in the keyboard.

         .. figure:: Images_appendix/Fig120.svg
            :alt: Protocol **ccp4-coot refinement**. A: Saving labeled atomic structure with *Coot Python Scripting* window. B: *Display Manager* window.
            :name: model_building_app_protocol_coot_2
            :align: center
            :width: 65.0%

            Protocol **ccp4-coot refinement**. A: Saving labeled atomic structure with *Coot Python Scripting* window. B: *Display Manager* window.

-  | Protocol execution:

   | Adding specific map/structure label is recommended in *Run name*
     section, at the form top. To add the label, open the protocol form,
     press the pencil symbol at the right side of *Run name* box,
     complete the label in the new opened window, press OK and, finally,
     close the protocol. This label will be shown in the output summary
     content (see below). If you want to run again this protocol, do not
     forget to set to *Restart* the *Run mode*. However, if you want to
     restart the protocol *in the last point* that you let it before and
     continue working with the last file saved in *Coot*, *set to Continue*
     the *Run mode*.

   | Press the *Execute* red button at the form bottom.

   | *Coot* graphics window will be opened after executing the protocol.
     Electron density maps and atomic structures are shown. Although
     steps to follow depend on the specific operation to carry out, a
     list of basic initial tasks and tools could be helpful:

   -  | Check maps and atomic structures definitively loaded in *Coot*:
      | By opening *Display Manager* window (*Coot* main menu) (:numref:`model_building_app_protocol_coot_2`
        (B)).

   -  | Set parameters appropriate to visualize them:

      | Electron density maps are sometimes more difficult to visualize.
        Moving mouse scroll-wheel forward and backward increases or
        reduces, respectively, map contour level. If the volume is still
        invisible, check if map and atomic structures are properly
        fitted. The radius of the density sphere can be modified in *Coot* main menu *Edit -> Map Parameters ... -> Global map properties window*.

   -  | Check chain names of each atomic structure, and edit them if needed in *Coot* main menu *Edit -> Change Chain IDs...*.

   -  | Set the text file *coot.ini* (:numref:`model_building_app_protocol_coot_6` (2)), edit it and save it if needed.

   -  | Set refinement conditions:
      | Click *Refine/Regularize control* button (upper right side of *Coot*
        graphics window) (:numref:`model_building_app_protocol_coot_3` (1)) and select the four restriction types in
        *Refinement and regularization Parameters* window (2).

      .. figure:: Images_appendix/Fig121.svg
         :alt: Protocol **ccp4-coot refinement**. *Refinement and regularization Parameters* window.
         :name: model_building_app_protocol_coot_3
         :align: center
         :width: 70.0%

         Protocol **ccp4-coot refinement**. *Refinement and regularization Parameters* window.

   | Once those basic parameters are set up, some steps to follow in the refinement process are:

   -  | Check validation parameter windows to have an idea of
        controversial areas and quality of the fitting:
      | Go to *Coot* main menu *Validation -> Ramachandran Plot*, *Validation
        -> Density fit analysis* and *Validate -> Rotamer analysis*.
        Validation windows have to be checked throughout the refinement
        process.

   -  | Refine the ends of each chain. Basic interactive refinement process requires several steps:

      -  | First, go to an atom included in the area that is going to be
           refined:
         | Go to *Coot* main menu *Draw -> Go To Atom...* and select chain and
           atom.

      -  | Assess electron density in that area, and consider the possibility of processing part of the residues.

      -  | Click the button *Real Space Refine Zone* (upper right side of *Coot* graphics window) (:numref:`model_building_app_protocol_coot_4` (A) (1)) to put it active. Next, click two residues of the chain (2 and 3). A second flexible grey chain overlaps the starting chain. That grey chain can be moved in order to get a different conformation according to the density map (hidden in :numref:`model_building_app_protocol_coot_4` (A)).

      -  | If refinement parameters get acceptable values, press *Accept* in *Accept Refinement?* window (:numref:`model_building_app_protocol_coot_4` (B)).

         .. figure:: Images_appendix/Fig122.svg
            :alt: Protocol **ccp4-coot refinement**. (A) Interactive refinement of the chain fragment between residues 2 and 9. (B) Accepting refinement window.
            :name: model_building_app_protocol_coot_4
            :align: center
            :width: 80.0%

            Protocol **ccp4-coot refinement**. (A) Interactive refinement of the chain fragment between residues 2 and 9. (B) Accepting refinement window.

   -  | Refine each chain following instructions from Help section:

      -  | Go to the residue *aaNumber* (main menu *Draw -> Go To Atom...*).

      -  | Initialize global variables.

      -  | Repeat this loop until reaching the end of the chain:
         | 1.- Press ``z`` in the keyboard.
         | 2.- Inspect one by one, and fit to the volume density, every
           residue from the small auxiliary chain.
         | 3.- Accept the refinement.

      -  | Check validation parameters to focus refinement in specific chain areas (*Coot* main menu *Validate -> Density fit analysis*).

   -  | After finishing refinement of every chain, save the structure (press ``e`` if *Coot* has to be definitively closed and not interactive anymore).

   -  | Close *Coot* graphics window.

-  | Visualization of protocol results:

   | After executing the protocol, press *Analyze Results* and *ChimeraX* graphics window will be opened by default. Atomic structures and volumes are referred to the origin of coordinates in *ChimeraX*. To show the relative position of atomic structures and electron density volumes, the three coordinate axes are represented; X axis (red), Y axis (yellow), and Z axis (blue) (:numref:`model_building_app_protocol_volume_3`). Coordinate axes, volume, and first atomic structure are model numbers *#1*, *#2*, *#3*, respectively, in *ChimeraX Model Panel*. Every atomic structure saved during refinement process will appear in *Model Panel* (:numref:`model_building_app_protocol_coot_5`). If you want to *visualize results in Coot graphics window* you only have to open the protocol *in the last point* that you let it before and *set to Continue* the *Run mode*. Close the *Coot* protocol without saving anything in this case.

   .. figure:: Images_appendix/Fig123.svg
      :alt: Protocol **ccp4-coot refinement**. *Coot* results visualized in *ChimeraX*.
      :name: model_building_app_protocol_coot_5
      :align: center
      :width: 80.0%

      Protocol **ccp4-coot refinement**. *Coot* results visualized in *ChimeraX*.

   Since *Scipion* projects keep every intermediate atomic structure partially
   refined (:numref:`model_building_app_protocol_coot_6` (1, 3), users can include any of them in successive
   following modeling workflow steps performed in *Scipion* (:numref:`model_building_app_protocol_coot_7`).

   .. figure:: Images_appendix/Fig124.svg
      :alt: Protocol **ccp4-coot refinement**. Browse content after several runs of interactive *Coot* protocol.
      :name: model_building_app_protocol_coot_6
      :align: center
      :width: 80.0%

      Protocol **ccp4-coot refinement**. Browse content after several runs of interactive *Coot* protocol.

   .. figure:: Images_appendix/Fig125.svg
      :alt: Protocol **ccp4-coot refinement**. *Scipion* window that allows to select any of *Coot* partially refined structures.
      :name: model_building_app_protocol_coot_7
      :align: center
      :width: 50.0%

      Protocol **ccp4-coot refinement**. *Scipion* window that allows to select any of *Coot* partially refined structures.

-  | Summary content:

   -  | Protocol output (below *Scipion* framework):

      -  | Each *Coot* intermediate atomic structure partially refined (*#n*):
         | *ccp4 - coot refinement ->* label name selected by the user
           or common output name
           (*coot_XXXXXX_Imol_YYYY_version_ZZZZ.pdb*);
         | *AtomStruct (pseudoatoms=False, volume=False)*.
         | Pseudoatoms is set to *False* because the structure is made
           of atoms instead of pseudoatoms. Volume is set to *False*
           because no electron density map is associated to the atomic
           structure.

      -  | Each *Coot* input map (saved by default):
         | *ccp4 - coot refinement -> output3DMap_XXXX*;
         | *Volume (x, y, and z dimensions, sampling rate)*.

      -  | *SUMMARY* box for each *Coot* intermediate atomic structure
           partially refined:
         | label name selected by the user or common output *Coot* name
           (*coot_XXXXXX_Imol_YYYY_version_ZZZZ.pdb*)
         | *Idem* for maps.
