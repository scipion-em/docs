.. _`app:importSequence`:

Import sequence protocol
========================

Protocol designed to import aminoacid or nucleotide sequences in *Scipion* from
four possible origins (plain text, atomic structures from PDB database
or a file in your computer, text file of the user’s computer, and
*UniProtKB/ GeneBank* databases).

-  | Requirements to run this protocol and visualize results:

   -  | *Scipion* plugin: **scipion-em**

-  | *Scipion* menu: *Model building -> Imports* (:numref:`model_building_app_protocol_sequence_1` (A))

   .. figure:: Images_appendix/Fig104.svg
      :alt: Protocol **import sequence**. A: Protocol location in *Scipion* menu. B: Protocol form.
      :name: model_building_app_protocol_sequence_1
      :align: center
      :width: 90.0%

      Protocol **import sequence**. A: Protocol location in *Scipion* menu. B: Protocol form.

-  | Protocol form parameters (:numref:`model_building_app_protocol_sequence_1` (B)):

   -  | *Sequence ID*: Optional short name to identify your sequence (acronym or number, e. g. *Q05769*). If no ID is assigned by the user, and the sequence has been downloaded from *GeneBank/UniProtKB/PDB* database, the database ID will be selected as *Sequence ID* (Read *Help* section (question mark) to see some examples). Otherwise, *Sequence name* will be set as *Sequence ID*. The *Sequence ID* will be included in sequence alignments in *ChimeraX* to identify the sequence.

   -  | *Sequence name*: Compulsory short name to identify your sequence (example: *PGH2_MOUSE*). Names with certain meaning are recommended. The *Sequence name* will appear in the summary box of the protocol.

   -  | *Sequence description*: Optional description of your sequence. It can include functionality, organism, size, etc. (example: *Prostaglandin G/H synthase 2*). If no description is assigned by the user, and the sequence has been downloaded from *GeneBank/UniProtKB/PDB* database, the database description will be selected as *Sequence description*. Otherwise, no description will be included.

   -  | *Import sequence of*: Selection parameter to choose between *aminoacids* and *nucleotides*. After selecting one of them, a new selection menu will be opened:

      -  | *aminoacids*: Parameter to select one of these four options:

         -  | *plain text*: Select this option if you want to introduce your own single letter aminoacid sequence. Since your sequence will be cleaned according to the standard protein alphabet of 20 aminoacids (*Protein*) or to an extended alphabet that includes 6 additional aminoacids or aminoacid groups (*Extended Protein*), you have to select one of these *IUPAC Protein* alphabets. Read *Help* section (question mark) to know the aminoacids included in each alphabet. Not only non-canonical aminoacids will be cleaned, but also wildcard characters such as *\**, *#*, *?*, *-*, etc... *Write your sequence here* indicates the place where your single letter aminoacid sequence has to be written or paste.

         -  | *atomic structure*: Select this option if you want to download the sequence from an atomic structure (:numref:`model_building_app_protocol_sequence_2` (A)). Select *id* to download your sequence from *PDB* database. Then, write the *PDB ID* (*Atomic structure ID*) and select the chain sequence of your preference (*Chain*). Use the wizard on the right side of *Chain* parameter to select that chain. Follow an analogous process to download the sequence from an atomic structure that you already have in your computer. This time, the *File path* will replace the *Atomic structure ID*. By pressing the folder symbol, a browser will help you to find the structure file.

         -  | *file*: Select this option if your sequence is written in a text file that you already have in your computer (:numref:`model_building_app_protocol_sequence_2` (B)). By pressing the folder symbol, a browser will help you to find the sequence file.

         -  | *UniProtID*: Select this option if you want to download the sequence from *UniProtKB* database (:numref:`model_building_app_protocol_sequence_2` (C)). Write the name/ID of the respective sequence in the parameter box *UniProt name/ID*. An error message appears in case you introduce a wrong ID.

            .. figure:: Images_appendix/Fig105.svg
               :alt: Protocol **import sequence**. Protocol form to import aminoacid sequences from the *PDB* database by indicating its respective *ID* (A), from a file (B), or from *UniProtKB* by writing the database *ID/name* (C).
               :name: model_building_app_protocol_sequence_2
               :align: center
               :width: 70.0%

               Protocol **import sequence**. Protocol form to import aminoacid sequences from the *PDB* database by indicating its respective *ID* (A), from a file (B), or from *UniProtKB* by writing the database *ID/name* (C).

      -  | *nucleotides*: Analogously to *aminoacids* parameter, select one of these four options:

         -  | *plain text*: Parameter to introduce your own single letter nucleotide sequence (:numref:`model_building_app_protocol_sequence_3` (A)). Since your sequence will be cleaned according to the standard nucleic acid alphabet, you have to select one of the next five alphabets. The first three are DNA alphabets and the last two ones are RNA alphabets. Read *Help* section (question mark) to understand each alphabet. The most restricted ones are *Unambiguous DNA* (“A, C, G, T”) and *Unambiguous RNA* (“A, C, G, U”) for DNA and RNA, respectively. The cleaning process also involves wildcard characters such as *\**, *#*, *?*, *-*, etc...

         -  | *atomic structure*: Information described for aminoacids is valid for nucleotides (:numref:`model_building_app_protocol_sequence_3` (B)).

         -  | *file*: Information described for aminoacids is valid for nucleotides (:numref:`model_building_app_protocol_sequence_3` (C)).

         -  | *GeneBank*: Information described for aminoacids is valid for nucleotides, this time replacing *UniProtKB* by *GeneBank* (:numref:`model_building_app_protocol_sequence_3` (D)).

            .. figure:: Images_appendix/Fig106.svg
               :alt: Protocol **import sequence**. Protocol form to write (A) or import nucleotide sequences from *PDB* database by indicating its respective *ID* (B), from a file (C), or from *GeneBank* by writing the database accession number (D).
               :name: model_building_app_protocol_sequence_3
               :align: center
               :width: 70.0%

               Protocol **import sequence**. Protocol form to write (A) or import nucleotide sequences from *PDB* database by indicating its respective *ID* (B), from a file (C), or from *GeneBank* by writing the database accession number (D).

-  | Protocol execution:

   | Adding specific sequence label is recommended in *Run name*
     section, at the form top. To add the label, open the protocol form,
     press the pencil symbol at the right side of *Run name* box,
     complete the label in the new opened window, press OK and, finally,
     close the protocol. This label will be shown in the output summary
     content (see below). If you want to run again this protocol, do not
     forget to set to *Restart* the *Run mode*.

   | Press the *Execute* red button at the form bottom.

-  | Visualization of protocol results:

   | After executing the protocol, press *Analyze Results* and a text editor will be opened in which you can read the sequence in *fasta* format. *Sequence ID* and *Sequence description* are included in the header.

-  | Summary content:

   -  | Protocol output (below *Scipion* framework):
      | *pwem - import sequence -> ouputSequence*;
      | *Sequence name*

   -  | *SUMMARY* box:
      | Sequence of aminoacids/ nucleotides:
      | Sequence *Sequence name* imported from plain text/ atomic
        structure/ file/ UniProt ID.
