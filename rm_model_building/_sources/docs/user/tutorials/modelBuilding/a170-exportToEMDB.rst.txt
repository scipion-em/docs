.. _`app:exportToEMDB`:

Submission to EMDB protocol
===========================

Protocol designed to save in a specified folder main files required to
submit cryo-EM derived electron density maps and derived atomic
structures to EMDB, as well as other additional files that EMDB
encourages to submit (https://deposit-pdbe.wwpdb.org/deposition//).
Although the submission has to be performed online, this protocol tries
to help the user to organize their results in different folders
according to each particular submission date, project, and so on.

-  menu:

   ( (A))

-  Protocol form parameters ( (B)):

   .. figure:: Images_appendix/Fig156.pdf
      :alt: Protocol . A: Protocol location in menu. B: Protocol form.
      :name: fig:export_to_EMDB_1
      :width: 90.0%

      Protocol . A: Protocol location in menu. B: Protocol form.

   -  section

      -  : Param to select the electron density map previously
         downloaded or generated in that you would like to submit to
         EMDB as . The map file will be saved with format. If the has
         the two half maps associated, they will be also saved at the
         same time in the same directory.

      -  : In case you would like to submit other types of maps,
         specially those generated during the postprocessing like
         sharpening maps, select and a new form param () will be opened
         to interrogate about the additional files (.mrc format). Take
         into account that all of them should be previously generated or
         imported in .

      -  : Param to select the FSC file previously generated in that we
         would like to submit to EMDB. This file will be saved with
         format.

      -  : EMDB also encourages to submit masks relevant in
         reconstruction or postprocessing steps. Select if you want to
         include one or several masks and a new form param () will open
         to interrogate about the masks (.mrc format).

      -  : Param to select the file of coordinates from the
         volume-associated atomic structure previously downloaded or
         generated in that we would like to submit to EMDB. This file
         will be saved with format.

      -  : Map image to represent the map in the database.

      -  : Directory specified by the user to save the three above
         selected files. In order to get appropriate data organization,
         a name related with the submission is recommended (date,
         project, number, ...).

-  Protocol execution:

   | Adding specific protocol label is recommended in section, at the
     form top. To add the label, open the protocol form, press the
     pencil symbol at the right side of box, complete the label in the
     new opened window, press OK and, finally, close the protocol. This
     label will be shown in the output summary content (see below). If
     you want to run again this protocol, do not forget to set to the .
   | Press the red button at the form bottom.

   All the previously selected files will be saved in the chosen
   directory after executing the protocol and this can be checked by
   opening that folder. Content of the selected directory:

   -  

   -  

   -  

   -  Folder of additional maps: , which contains , etc.

   -  

   -  Mask folder: , which contains , etc.

   -  Input atomic structure:

   -  Atomic structure complete:

   -  Atomic structure symplified:

   -  

   | As you can see, two coordinate files have been created, complete
     and symplified, to try to satisfy different format demands.
   | No additional specific visualization tools have been added to this
     protocol.

-  Summary content:

   | The summary specifies the path to the directory selected to save
     the files:
