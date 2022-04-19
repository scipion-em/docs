.. _`app:modelFromTemplate`:

Model from Template protocol
============================

| Protocol designed to obtain a structure model for a target sequence in
  . Target structure is predicted by sequence homology using
  :raw-latex:`\citep{sali1993}` web service in .
| WARNING: Working with requires a license key, which can be requested
  free of charge for academic users. Try to have this license key before
  starting the protocol execution.

-  Requirements to run this protocol and visualize results:

   -  plugin:

   -  plugin:

   -  Multiple sequence alignment tools: ,

-  menu: ( (A))

-  Protocol form parameters ( (B)):

   .. figure:: Images_appendix/Fig111.pdf
      :alt: Protocol . A: Protocol location in menu. B: Protocol form:
      Option “template available”. C: Protocol form: Option “looking for
      template”.
      :name: fig:app_protocol_seqHomology_1
      :width: 90.0%

      Protocol . A: Protocol location in menu. B: Protocol form: Option
      “template available”. C: Protocol form: Option “looking for
      template”.

   -  section

      -  : Select if you have found your in a previous similarity
         searching step. Select if you do not have any to start the
         homology modeling and you would like to search for one.

      -  Option ( (B))

         -  : Atomic structure previously downloaded in . This structure
            was selected by sequence homology, i.e. by looking for the
            structurally characterized sequence more similar (with
            higher identity) to the target sequence.

         -  : Specific monomer of the macromolecule that has to be used
            as structure of the . Use the wizard on the right side of
            parameter to select that chain.

         -  : Sequence previously downloaded in . This sequence has to
            be modeled following the structure skeleton of the selected
            .

         -  : :math:`Modeller` provides structural models of the based
            on a sequence alignment, in which at least sequences of and
            have to be included. Three options can be considered to
            improve this alignment:

            #. | : No more sequences are going to be included in the
                 alignment except and sequences. Correlative param:
               | \**\* : Select one of the three available alignment
                 methods, (by default), , .

            #. | if you want to perform a multiple sequence alignment
                 adding other sequences already downloaded in .
                 Additional sequences, others than and sequences, are
                 required to accomplish this multiple alignment.
                 Correlative params:
               | \**\* : Box to complete with the additional sequences
                 used to perform the multiple sequence alignment. All of
                 them were previously downloaded in .
               | \**\* : Select between and methods.

            #. | : If you want to include other sequences in the
                 alignment by providing your own sequence alignment.
                 Correlative param:
               | \**\* : Complete this box with the help of the right
                 side browser including the sequence alignment file that
                 you already have saved in your computer. Different
                 alignment formats are available
                 (https://www.cgl.ucsf.edu/chimerax/docs/user/commands/open.html).
                 An example of alignment in format can be seen below
                 (Use case 3).

         -  : Select if you’d like to obtain a multimer by using two
            sequences and the same multimer . The params to complete the
            option are identical to those already shown, with the
            exception of the , already completed. However, no one of
            those params will appear in case you select in order to
            obtain a by using only one sequence.

      -  Option ( (C))

         -  : Sequence previously downloaded in . This sequence has to
            be modeled following the structure skeleton of the that you
            are going to select among the retrieved entries found by the
            similarity searching tool.

         -  : Select one of the two suggested protein sequence
            databases, PDB and NR. Press the symbol on the right to see
            the meaning of each one. Remark that the NR database allows
            you to get entries with, as well as without, atomic
            structure associated. These ones, which do not provide ,
            could be useful to build a better sequence alignment.

         -  : Select one of the “substitution matrix” to assign a score
            to any couple of residues in the alignment
            (https://www.ncbi.nlm.nih.gov/blast/html/sub_matrix.html).

         -  : Maximum statistic value required to include a retrieved
            element in the hit list.

         -  that you’d like to retrieve from the database.

   -  section

      Follow this section steps to run :math:`Modeller` via web service
      in and to select and save one of the retrieved models in
      framework.

-  Protocol execution:

   | Adding specific template-target label is recommended in section, at
     the form top. To add the label, open the protocol form, press the
     pencil symbol on the right side of box, complete the label in the
     new opened window, press OK and, finally, close the protocol. This
     label will be shown in the output summary content (see below). If
     you want to run again this protocol, do not forget to set to the .
   | Press the red button at the form bottom.
   | Several windows will be opened after executing the protocol with
     different contents according to the distinct form param options.
     Although we are going to detail some of them through several use
     cases (see below), designed to ilustrate different applications of
     this protocol, as well as the procedure to follow in each case, in
     general we can predict the opening of graphics window and a
     sequence alignment window. Usually, in both windows the sequence is
     green highlighted (see an example of these windows in ). Main steps
     to follow ahead are:

   -  Ask for model(s) to :math:`Modeller` by selecting in the main menu
      of graphics window.

   -  Complete the new window opened for with the sequence alignment
      that includes the and with the (s) sequence(s), :math:`Modeller`
      license key, multichain model, number of models retrieved by , and
      options like the building of models with hydrogens, as well as
      :math:`model` inclusion of heteroatoms or water molecules. An
      example of completed :math:`Modeller` window can be observed in
      (A). By pressing the computation starts. The status of the job can
      be checked in the lower left corner of graphics window.

   -  After a while a new panel window will show the retrieved models of
      the sequence ( (B)). Two statistics assess these models: ,
      statistical potentials derived-score, and , normalized Discrete
      Optimized Protein Energy, atomic distance depending-score.
      Reliable models show values higher than 0.7, and negative values
      correspond to better models. Retrieved models can be checked in .
      One of them should be selected ( (C)).

   -  | Rename the selected model, for example to with the command line:

   -  | Save the retrieved model selected according to the new model
        number in the track system () shown in by writing in command
        line:

-  Visualization of protocol results:

   After executing the protocol, press and graphics window will be
   opened by default. Atomic structures are referred to the origin of
   coordinates in . To show the relative position of the atomic
   structure, the three coordinate axes are represented; X axis (red), Y
   axis (yellow), and Z axis (blue) (). Coordinate axes and selected
   atomic structure are model numbers and , respectively, in panel if
   only one structure has been saved.

-  Summary content:

   -  | Protocol output (below framework):
      | ;
      | .
      | Pseudoatoms is set to when the structure is made of pseudoatoms
        instead of atoms. Volume is set to when an electron density map
        is associated to the atomic structure.

   -  | box:
      | Produced files:
      | we have some result

USE CASES
~~~~~~~~~

-  | 
   | Aim: To model a sequence using one chain of a homologous atomic
     structure as , using only the sequences of and in the sequence
     alignment.

   .. figure:: Images_appendix/Fig305.pdf
      :alt: (A) Protocol form of . (B) view of the atomic structure,
      highlighted in green the selected to perform the modeling. (C)
      sequence view panel showing the sequence alignment between the
      sequence, greeen highlighted, and the sequence. (D) Upper part of
      the panel showing the sequence alignment selected, shown in (C),
      and the selected sequence.
      :name: fig:app_protocol_seqHomology_2

      (A) Protocol form of . (B) view of the atomic structure,
      highlighted in green the selected to perform the modeling. (C)
      sequence view panel showing the sequence alignment between the
      sequence, greeen highlighted, and the sequence. (D) Upper part of
      the panel showing the sequence alignment selected, shown in (C),
      and the selected sequence.

   | Protocol execution: Complete the protocol form as indicated in (A).
     Follow the general procedure shown above (Protocol execution
     section). Windows (B) and (C) will appear. Open and complete the
     panel as indicated in (D) and wait for a while. After getting the
     retrieved models, if you want to select, for example, the model ,
     write in the command line:
   | And to close the protocol. Visualize your results.

-  | 
   | Aim: To model simultaneously two sequences to obtain a multichain
     model using two chains of a homologous atomic structure as , using
     other additional sequences than and in the sequence alignment.

   .. figure:: Images_appendix/Fig306.pdf
      :alt: (A) Protocol form of . Remark that two additional sequences
      other than and sequences have been selected to improve both
      alignments. (B) Upper part of the panel showing the two sequence
      alignment selected, shown in (D) and (E), and the two selected
      sequences.(C) view of the atomic structure, highlighted in yellow
      the and in green the selected to perform the modeling. (D)
      sequence view panel showing the sequence alignment between the
      sequence, greeen highlighted, the sequence () and two more
      additional sequences. (E) sequence view panel showing the sequence
      alignment between the sequence, greeen highlighted, the sequence
      () and two more additional sequences.
      :name: fig:app_protocol_seqHomology_3

      (A) Protocol form of . Remark that two additional sequences other
      than and sequences have been selected to improve both alignments.
      (B) Upper part of the panel showing the two sequence alignment
      selected, shown in (D) and (E), and the two selected sequences.(C)
      view of the atomic structure, highlighted in yellow the and in
      green the selected to perform the modeling. (D) sequence view
      panel showing the sequence alignment between the sequence, greeen
      highlighted, the sequence () and two more additional sequences.
      (E) sequence view panel showing the sequence alignment between the
      sequence, greeen highlighted, the sequence () and two more
      additional sequences.

   | Protocol execution: Complete the protocol form as indicated in (A).
     Follow the general procedure shown above (Protocol execution
     section). Windows (C), (D) and (E) will appear. Open and complete
     the panel as indicated in (B) and wait for a while. After getting
     the retrieved models, if you want to select, for example, the model
     , write in the command line:
   | And to close the protocol. Visualize your results.

-  | 
   | Aim: To model simultaneously two sequences to obtain a multichain
     model using two chains of a homologous atomic structure as , using
     your own sequence alignment.

   .. figure:: Images_appendix/Fig307.pdf
      :alt: (A) Protocol form of . Remark that your own sequence
      alignment containing the sequences of and , among others, have
      been selected. (B) Example of sequence alignment in format (file
      “aligned_2.fasta”) that includes the sequence, the sequence () and
      two more additional sequences.
      :name: fig:app_protocol_seqHomology_4

      (A) Protocol form of . Remark that your own sequence alignment
      containing the sequences of and , among others, have been
      selected. (B) Example of sequence alignment in format (file
      “aligned_2.fasta”) that includes the sequence, the sequence () and
      two more additional sequences.

   | Protocol execution: Complete the protocol form as indicated in (A).
     Follow the general procedure shown above (Protocol execution
     section). Remark that you already have a sequence alignment file
     for each saved in your computer. An example can be seen in (B).
     Windows (C), (D) and (E) of previous . Open and complete the panel
     as indicated in (B) and wait for a while. After getting the
     retrieved models, if you want to select, for example, the model ,
     write in the command line:
   | And to close the protocol. Visualize your results.

-  | 
   | Aim: To model a sequence without previous information of a possible
     atomic structure .

   .. figure:: Images_appendix/Fig308.pdf
      :alt: (A) Protocol form of that includes the sequence that we’d
      like to model. (B) Upper part of the panel showing the sequence
      alignment and the sequence selected. (C) graphics window empty
      before opening the atomic structure. (D) sequence view panel
      showing the sequence. (E) BlastProtein panel showing the retrieved
      results from PDB database.
      :name: fig:app_protocol_seqHomology_5

      (A) Protocol form of that includes the sequence that we’d like to
      model. (B) Upper part of the panel showing the sequence alignment
      and the sequence selected. (C) graphics window empty before
      opening the atomic structure. (D) sequence view panel showing the
      sequence. (E) BlastProtein panel showing the retrieved results
      from PDB database.

   | Protocol execution: Complete the protocol form as indicated in (A).
     Follow the general procedure shown above (Protocol execution
     section). Remark that in this case there is no atomic structure.
     Instead, an empty graphics window will appear (C) together with the
     sequence that we’d like to model and retrieved results (E). Note
     that it could take some seconds the opening of the panel. Have a
     look to these results and select one of them as possible of your
     sequence. In this particular case, for example, we are going to
     choose the first one (). Open this atomic structure en by writing
     in the command line:
   | At this point, open the panel and complete it as indicated in (B).
     Wait for a while. After getting the retrieved models, if you want
     to select, for example, the model , write in the command line:
   | And to close the protocol. Visualize your results.
