.. _`app:exportToEMDB`:

Submission to wwPDB protocol
===========================

Protocol designed to save in a specified folder main files required to
submit cryo-EM derived electron density maps and derived atomic
structures to `wwPDB <https://deposit-pdbe.wwpdb.org/deposition//>`_, as well as other additional files that wwPDB encourages to submit. Although the submission has to be performed online, this protocol tries
to help the user to organize their results in different folders according to each particular submission date, project, and so on.

-  *Scipion* menu:

   *Model building -> Exports* (:numref:`model_building_export_to_EMDB_1` (A))

   .. figure:: Images_appendix/Fig156.svg
      :alt: Protocol **export to wwPDB**. A: Protocol location in *Scipion* menu. B: Protocol form.
      :name: model_building_export_to_EMDB_1
      :align: center
      :width: 90.0%

      Protocol **export to wwPDB**. A: Protocol location in *Scipion* menu. B: Protocol form.

-  Protocol form parameters (:numref:`model_building_export_to_EMDB_1` (B)):

   -  | *Input* section

      -  | *Main EM map to export*: Param to select the electron density map previously downloaded or generated in *Scipion* that you would like to submit to EMDB as *main map*. The map file will be saved with *.mrc* format. If the *main map* has the two half maps associated, they will be also saved at the same time in the same directory.

      -  | *Additional maps to export?*: In case you would like to submit other types of maps, specially those generated during the postprocessing like sharpening maps, select *Yes* and a new form param (*Additional EM maps to export*) will be opened to interrogate about the additional files (.mrc format). Take into account that all of them should be previously generated or imported in *Scipion*.

      -  | *FSC to export*: Param to select the FSC file previously generated in *Scipion* that we would like to submit to EMDB. This file will be saved with *.xml* format.

      -  | *Masks to export?*: EMDB also encourages to submit masks relevant in reconstruction or postprocessing steps. Select *Yes* if you wish to include one or several masks and a new form param (*Masks to export*) will open to interrogate about the masks (.mrc format).

      -  | *Atomic structure to export*: Param to select the file of coordinates from the volume-associated atomic structure previously downloaded or generated in *Scipion* that we would like to submit to EMDB. This file will be saved with *.cif* format.

      -  | *Image to export*: Map image to represent the map in the database.

      -  | *Export to directory*: Directory specified by the user to save the three above selected files. In order to get appropriate data organization, a name related with the submission is recommended (date, project, number, ...).

-  | Protocol execution:

   | Adding specific protocol label is recommended in *Run name* section, at the form top. To add the label, open the protocol form, press the pencil symbol at the right side of *Run name* box, complete the label in the new opened window, press OK and, finally, close the protocol. This label will be shown in the output summary content (see below). If you want to run again this protocol, do not forget to set to *Restart* the *Run mode*.

   | Press the *Execute* red button at the form bottom.

   All the previously selected files will be saved in the chosen directory after executing the protocol and this can be checked by opening that folder. Content of the selected directory:

   -  | *main_map.mrc*

   -  | *half_map_1.mrc*

   -  | *half_map_2.mrc*

   -  | Folder of additional maps: *addMaps*, which contains *map_01.mrc, map_02.mrc*, etc.

   -  | *FSC_file_name.xml*

   -  | Mask folder: *masks*, which contains *mask_01, mask_02*, etc.

   -  | Input atomic structure: *atomic_structure_file_name.cif/pdb*

   -  | Atomic structure complete: *coordinates.cif*

   -  | Atomic structure symplified: *symplified_atom_structure.cif*

   -  | *image.png*

   | As you can see, two coordinate files have been created, complete and symplified, to try to satisfy different format demands.

   | No additional specific visualization tools have been added to this protocol.

-  Summary content:

   | The summary specifies the path to the directory selected to save the files:
   | *Data available at: path*
