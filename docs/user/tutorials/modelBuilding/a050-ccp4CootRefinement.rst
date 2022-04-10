.. _`app:ccp4CootRefinement`:

CCP4 Coot Refinement protocol
=============================

| Protocol designed to interactively fit and refine atomic structures,
  in real space, regarding electron density maps in by using
  :math:`Coot` :raw-latex:`\citep{emsley2010}`. This protocol integrates
  :math:`Coot` 3D graphics display functionality in , supporting
  accession to :math:`Coot` input and output data in the general model
  building workflow.
| :math:`Coot`, acronym of Crystallopgraphic Object-Oriented Toolkit,
  gathers several tools useful to perform mostly interactive modeling
  procedures and is integrated in CCP4 software suite
  (`www.ccp4.ac.uk/ccp4_projects.php <www.ccp4.ac.uk/ccp4_projects.php>`__).
  Initially applicable to X-ray data, some modifications of :math:`Coot`
  also allow to model atomic structures regarding electron density maps
  obtained from cryo-EM (:raw-latex:`\citep{brown2015}`). Additional
  instructions to use :math:`Coot` can be found in
  https://www2.mrc-lmb.cam.ac.uk/personal/pemsley/coot/. Remark in
  https://www2.mrc-lmb.cam.ac.uk/personal/pemsley/coot/web/docs/coot.html#Mousing-and-Keyboarding
  mouse requirements to get the best functioning.

-  Requirements to run this protocol and visualize results:

   -  plugin:

   -  plugin:

   -  CCP4 software suite (from version 7.0.056 to 7.1)

   -  plugin:

-  | menu:
   | ( (A))

-  Protocol form parameters ( (B)):

   .. figure:: Images_appendix/Fig119.pdf
      :alt: Protocol . A: Protocol location in menu. B: Protocol form.
      :name: fig:app_protocol_coot_1
      :width: 90.0%

      Protocol . A: Protocol location in menu. B: Protocol form.

   -  section

      -  : At least one or several electron density maps previously
         downloaded or generated in . The density volume regarding to
         which an atomic structure has to be modeled has to be included
         in this volume list.

      -  : Parameter set to “Yes” by default to perform normalization of
         map electron density levels according to :math:`Coot`
         requirements ([0, 1]). This normalization approximates cryo-EM
         density data to maps obtained from X-ray crystallography
         because it diminishes Z-score (number of standard deviations)
         variation of map values.

      -  : Mandatory param to load an atomic structure previously
         downloaded or generated in . This structure will be fitted and
         refined according to a particular density volume.

      -  : Additional atomic structures previously downloaded or
         generated in that may be helpful in the refinement process.

   -  section

      This section contains :math:`Coot` commands to make easier some
      interactive refinement steps and to save refined atomic
      structures. Their reference volumes will be saved by default with
      the refined atomic structures. Here you are an overview of these
      commands:

      -  Automatically moving from one chain to another in an atomic
         structure:

         -  Press in the keyboard to move from one chain to the previous
            one.

         -  Press to change from one chain to the next one.

      -  | Initializing global variables:
         | Press in your keyboard.

      -  | Semi-automatic refinement of small groups of residues (10 to
           15):
         | As soon as :math:`Coot` protocol is executed, the text file
           will be saved in the project folder ( (1, 2)). This file
           content has to be modified according to our atomic structure
           model in this way:

         -  : has to be replaced by the number of the molecule that has
            to be refined. This number appears detailed in :math:`Coot`
            main menu ( (B, red arrow)).

         -  : has to be replaced by the name of the molecule chain that
            has to be refined.

         -  : , name of the small chain of 10-15 residues, can be
            optionally replaced by other name.

         -  : has to be replaced by the position of the residue from
            which the refinement has to start.

         -  : will be replaced by the desired small step of residues
            that gets flexible enough to select other conformation of
            this auxiliary chain.

         Save text file after its modification. Go to the residue
         position indicated in , initialize global variables with , and
         pres or in the keyboard to refine those residues upstream or
         downstream, respectively.

      -  | Printing environment:
         | Press in the keyboard.

      -  | Saving an atomic structure after an interactive working
           session with :math:`Coot`:
         | window will be opened with :math:`Coot` main menu ( (A)). By
           writing , molecule will be saved by default in . Molecule
           number can be checked in :math:`Coot` main menu ( (B, red
           arrow)). Saving the molecule this way is equivalent to press
           in the keyboard.
         | The number of the specific molecule has to be written in
           brackets to save any other molecule than .
         | Although the name of the saved atomic structure is by default
           ( is the protocol box number, the :math:`model` number and
           the number of times that the molecule has been saved), other
           names/labels of your preference are also allowed. That
           name/label has to be introduced with command, as it is
           detailed in the example ( (A)). The addition of extension is
           not required.
         | If no more interactive sessions with :math:`Coot` are
           planned, after saving the atomic structure, :math:`Coot` will
           be definitively closed by pressing in the keyboard.

         .. figure:: Images_appendix/Fig120.pdf
            :alt: Protocol . A: Saving labeled atomic structure with
            window. B: window.
            :name: fig:app_protocol_coot_2
            :width: 65.0%

            Protocol . A: Saving labeled atomic structure with window.
            B: window.

-  Protocol execution:

   | Adding specific map/structure label is recommended in section, at
     the form top. To add the label, open the protocol form, press the
     pencil symbol at the right side of box, complete the label in the
     new opened window, press OK and, finally, close the protocol. This
     label will be shown in the output summary content (see below). If
     you want to run again this protocol, do not forget to set to the .
     However, if you want to restart the protocol *in the last point*
     that you let it before and continue working with the last file
     saved in , *set to* the .
   | Press the red button at the form bottom.
   | graphics window will be opened after executing the protocol.
     Electron density maps and atomic structures are shown. Although
     steps to follow depend on the specific operation to carry out, a
     list of basic initial tasks and tools could be helpful:

   -  | Check maps and atomic structures definitively loaded in :
      | By opening window (:math:`Coot` main menu) ( (B)).

   -  | Set parameters appropriate to visualize them:
      | Electron density maps are sometimes more difficult to visualize.
        Moving mouse scroll-wheel forward and backward increases or
        reduces, respectively, map contour level. If the volume is still
        invisible, check if map and atomic structures are properly
        fitted. The radius of the density sphere can be modified in
        :math:`Coot` main menu .

   -  Check chain names of each atomic structure, and edit them if
      needed in :math:`Coot` main menu .

   -  Set the text file ( (2)), edit it and save it if needed.

   -  | Set refinement conditions:
      | Click button (upper right side of graphics window) ( (1)) and
        select the four restriction types in window (2).

      .. figure:: Images_appendix/Fig121.pdf
         :alt: Protocol . window.
         :name: fig:app_protocol_coot_3
         :width: 70.0%

         Protocol . window.

   Once those basic parameters are set, some steps to follow in
   refinement process are:

   -  | Check validation parameter windows to have an idea of
        controversial areas and quality of the fitting:
      | Go to main menu , and . Validation windows have to be checked
        throughout the refinement process.

   -  Refine the ends of each chain. Basic interactive refinement
      process requires several steps:

      -  | First, go to an atom included in the area that is going to be
           refined:
         | Go to main menu and select chain and atom.

      -  Assess electron density in that area, and consider the
         possibility of processing part of the residues.

      -  Click the button (upper right side of graphics window) ( (A)
         (1)) to put it active. Next, click two residues of the chain (2
         and 3). A second flexible grey chain overlaps the starting
         chain. That grey chain can be moved in order to get a different
         conformation according to the density map (hidden in (A)).

      -  If refinement parameters get acceptable values, press in window
         ( (B)).

         .. figure:: Images_appendix/Fig122.pdf
            :alt: Protocol . (A) Interactive refinement of the chain
            fragment between residues 2 and 9. (B) Accepting refinement
            window.
            :name: fig:app_protocol_coot_4
            :width: 80.0%

            Protocol . (A) Interactive refinement of the chain fragment
            between residues 2 and 9. (B) Accepting refinement window.

   -  Refine each chain following instructions from Help section:

      -  Go to the residue (main menu ).

      -  Initialize global variables.

      -  | Repeat this loop until reaching the end of the chain:
         | 1.- Press in the keyboard.
         | 2.- Inspect one by one, and fit to the volume density, every
           residue from the small auxiliary chain.
         | 3.- Accept the refinement.

      -  Check validation parameters to focus refinement in specific
         chain areas (main menu ).

   -  After finishing refinement of every chain, save the structure
      (press if has to be definitively closed and not interactive
      anymore).

   -  Close graphics window.

-  Visualization of protocol results:

   After executing the protocol, press and graphics window will be
   opened by default. Atomic structures and volumes are referred to the
   origin of coordinates in . To show the relative position of atomic
   structures and electron density volumes, the three coordinate axes
   are represented; X axis (red), Y axis (yellow), and Z axis (blue) ().
   Coordinate axes, volume, and first atomic structure are model numbers
   , , , respectively, in . Every atomic structure saved during
   refinement process will appear in (). If you want to *visualize
   results in graphics window* you only have to open the protocol *in
   the last point* that you let it before and *set to* the . Close the
   protocol without saving anything in this case.

   .. figure:: Images_appendix/Fig123.pdf
      :alt: Protocol . results visualized in .
      :name: fig:app_protocol_coot_5
      :width: 80.0%

      Protocol . results visualized in .

   Since projects keep every intermediate atomic structure partially
   refined ( (1, 3), users can include any of them in successive
   following modeling workflow steps performed in ().

   .. figure:: Images_appendix/Fig124.pdf
      :alt: Protocol . Browse content after several runs of interactive
      protocol.
      :name: fig:app_protocol_coot_6
      :width: 80.0%

      Protocol . Browse content after several runs of interactive
      protocol.

   .. figure:: Images_appendix/Fig125.pdf
      :alt: Protocol . window that allows to select any of partially
      refined structures.
      :name: fig:app_protocol_coot_7
      :width: 50.0%

      Protocol . window that allows to select any of partially refined
      structures.

-  Summary content:

   -  Protocol output (below framework):

      -  | Each intermediate atomic structure partially refined ():
         | label name selected by the user or common output name ();
         | .
         | Pseudoatoms is set to because the structure is made of atoms
           instead of pseudoatoms. Volume is set to because no electron
           density map is associated to the atomic structure.

      -  | Each input map (saved by default):
         | ;
         | .

      -  | box for each intermediate atomic structure partially refined:
         | label name selected by the user or common output name ()
         | Idem for maps.
