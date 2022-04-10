.. _`app:importSequence`:

Import sequence protocol
========================

Protocol designed to import aminoacid or nucleotide sequences in from
four possible origins (plain text, atomic structures from PDB database
or a file in your computer, text file of the user’s computer, and
databases).

-  Requirements to run this protocol and visualize results:

   -  plugin:

-  menu: ( (A))

-  Protocol form parameters ( (B)):

   .. figure:: Images_appendix/Fig104.pdf
      :alt: Protocol . A: Protocol location in menu. B: Protocol form.
      :name: fig:app_protocol_sequence_1
      :width: 90.0%

      Protocol . A: Protocol location in menu. B: Protocol form.

   -  : Optional short name to identify your sequence (acronym or
      number, e. g. ). If no ID is assigned by the user, and the
      sequence has been downloaded from database, the database ID will
      be selected as (Read section (question mark) to see some
      examples). Otherwise, will be set as . The will be included in
      sequence alignments in to identify the sequence.

   -  : Compulsory short name to identify your sequence (example: ).
      Names with certain meaning are recommended. The will appear in the
      summary box of the protocol.

   -  : Optional description of your sequence. It can include
      functionality, organism, size, etc... (e.g. ). If no description
      is assigned by the user, and the sequence has been downloaded from
      database, the database description will be selected as .
      Otherwise, no description will be included.

   -  : Selection parameter to choose between and . After selecting one
      of them, a new selection menu will be opened:

      -  : Parameter to select one of these four options:

         -  : Select this option if you want to introduce your own
            single letter aminoacid sequence. Since your sequence will
            be cleaned according to the standard protein alphabet of 20
            aminoacids () or to an extended alphabet that includes 6
            additional aminoacids or aminoacid groups (), you have to
            select one of these alphabets. Read section (question mark)
            to know the aminoacids included in each alphabet. Not only
            non-canonical aminoacids will be cleaned, but also wildcard
            characters such as , , , , etc... indicates the place where
            your single letter aminoacid sequence has to be written or
            paste.

         -  : Select this option if you want to download the sequence
            from an atomic structure ( (A)). Select to download your
            sequence from database. Then, write the () and select the
            chain sequence of your preference (). Use the wizard on the
            right side of parameter to select that chain. Follow an
            analogous process to download the sequence from an atomic
            structure that you already have in your computer. This time,
            the will replace the . By pressing the folder symbol, a
            browser will help you to find the structure file.

         -  : Select this option if your sequence is written in a text
            file that you already have in your computer ( (B)). By
            pressing the folder symbol, a browser will help you to find
            the sequence file.

         -  : Select this option if you want to download the sequence
            from database ( (C)). Write the name/ID of the respective
            sequence in the parameter box . An error message appears in
            case you introduce a wrong ID.

            .. figure:: Images_appendix/Fig105.pdf
               :alt: Protocol . Protocol form to import aminoacid
               sequences from the database by indicating its respective
               (A), from a file (B), or from by writing the database
               (C).
               :name: fig:app_protocol_sequence_2
               :width: 70.0%

               Protocol . Protocol form to import aminoacid sequences
               from the database by indicating its respective (A), from
               a file (B), or from by writing the database (C).

      -  : Analogously to parameter, select one of these four options:

         -  : Parameter to introduce your own single letter nucleotide
            sequence ( (A)). Since your sequence will be cleaned
            according to the standard nucleic acid alphabet, you have to
            select one of the next five alphabets. The first three are
            DNA alphabets and the last two ones are RNA alphabets. Read
            section (question mark) to understand each alphabet. The
            most restricted ones are (“A, C, G, T”) and (“A, C, G, U”)
            for DNA and RNA, respectively. The cleaning process also
            involves wildcard characters such as , , , , etc...

         -  : Information described for aminoacids is valid for
            nucleotides ( (B)).

         -  : Information described for aminoacids is valid for
            nucleotides ( (C)).

         -  : Information described for aminoacids is valid for
            nucleotides, this time replacing by ( (D)).

            .. figure:: Images_appendix/Fig106.pdf
               :alt: Protocol . Protocol form to write (A) or import
               nucleotide sequences from database by indicating its
               respective (B), from a file (C), or from by writing the
               database accession number (D).
               :name: fig:app_protocol_sequence_3
               :width: 70.0%

               Protocol . Protocol form to write (A) or import
               nucleotide sequences from database by indicating its
               respective (B), from a file (C), or from by writing the
               database accession number (D).

-  Protocol execution:

   | Adding specific sequence label is recommended in section, at the
     form top. To add the label, open the protocol form, press the
     pencil symbol at the right side of box, complete the label in the
     new opened window, press OK and, finally, close the protocol. This
     label will be shown in the output summary content (see below). If
     you want to run again this protocol, do not forget to set to the .
   | Press the red button at the form bottom.

-  Visualization of protocol results:

   After executing the protocol, press and a text editor will be opened
   in which you can read the sequence in format. and are included in the
   header.

-  Summary content:

   -  | Protocol output (below framework):
      | ;

   -  | box:
      | Sequence of aminoacids/ nucleotides:
      | Sequence imported from plain text/ atomic structure/ file/
        UniProt ID.
