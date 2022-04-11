Moving from sequence to atomic structure scenario
=================================================

In this section we are going to obtain the initial *model* of our *target* sequence, in
this case the *Hgb* :math:`\alpha` subunit. To perform this task we are going
to use the *Scipion* protocol **chimerax-model from template**. Although this protocol offers several different
possibilities to get the right result (see Appendix :ref:`Model from template <app:modelFromTemplate>` for details and use cases), we are going to consider that we already have a *template*, that we have
found in the previous step and that will be used as protocol input. In
addition, although the protocol also allows to get a model including two
chains modeled simultaneously using the same *template* (multichain modeling), in
our example we are going to model only one chain, the *Hgb* :math:`\alpha`
subunit. :numref:`model_building_scipion_workflow_from_sequence` shows the workflow that we are going to detail in this section. Other possibilities of the protocol usage will be suggested at the end
of the chapter.

.. figure:: Images/Fig66.svg
   :alt: *Scipion* framework detailing the workflow to generate the first model of the human *Hgb* :math:`\alpha` subunit.
   :name: model_building_scipion_workflow_from_sequence
   :align: center
   :width: 100.0%

   *Scipion* framework detailing the workflow to generate the first model of the human *Hgb* :math:`\alpha` subunit.

Downloading the atomic structure
--------------------------------

Once identified the *template* that we are going to use as structural skeleton of
our sequence, we import it into *Scipion* with the protocol **import atomic structure** (see :numref:`model_building_import_atomic_structure` (1) and Appendix :ref:`Import atomic structure <app:importAtomicStructure>`). Select the option for importing the atomic structure from ID (2), write the *PDB*
accession code (3) and execute the protocol (4).

.. figure:: Images/Fig10.svg
   :alt: Importing the atomic structure *1PBX*.
   :name: model_building_import_atomic_structure
   :align: center
   :width: 100.0%

   Importing the atomic structure *1PBX*.

You can visualize the imported structure (5) in *ChimeraX* (:numref:`model_building_chimera_visualization_structure`). By selecting chain *A*
in the upper menu (1) you can distinguish the *Hgb* :math:`\alpha` subunit
(2).

.. figure:: Images/Fig11.svg
   :alt: Atomic structure *1PBX* visualized with :math:`ChimeraX`. *Hgb* :math:`\alpha` subunit (selected chain *A*) is shown green-highlighted.
   :name: model_building_chimera_visualization_structure
   :align: center
   :width: 80.0%

   Atomic structure *1PBX* visualized with :math:`ChimeraX`. *Hgb* :math:`\alpha`
   subunit (selected chain ) is shown green-highlighted.

Structural models of human *metHgb* subunits from templates
---------------------------------------------------------

*Modeller* :cite:p:`sali1993` is one of the computational web services
used by *ChimeraX*, which provides the interface to run the program. Working with *Modeller*
requires a license key, which is provided free of charge for academic
users. *Modeller* allows two types of modeling computations to generate theoretical
models, *template*-based (sequence homology) and *template*-free (*de novo*, only for missing
segments). In this tutorial we are going to consider the first one:
structure prediction by sequence homology. Requirements for this type of
modeling are the *template* structure and a sequence alignment including sequences
of *target* and *template*.

``NOTE before starting:`` We are going to use a *ChimeraX*-derived protocol for the first time in this
tutorial (**chimerax-model from template**, Appendix :ref:`Model from template <app:modelFromTemplate>`). Remark that this use of *ChimeraX* is completely different from the use of *ChimeraX* as a visualization tool,
as we have seen previously. By using the *ChimeraX* graphics window, opening it
from the *Scipion* button *Analyze Results* we can observe protocol results but we CANNOT save
anything. However, using *ChimeraX* as a tool, as it is the case in *Scipion* *ChimeraX*-derived
protocols, we can perform different tasks, taking advantage of the
available *ChimeraX* tools and, finally, we CAN save the obtained results and the
working session.

-  | Preparing your sequence alignment:
   | In addition to the ways to obtain the sequence alignment using *ChimeraX*,
     this alignment can be also generated in the *Scipion* protocol **chimerax-model from template** (Appendix :ref:`Model from template <app:modelFromTemplate>`). This
     protocol allows selecting between pairwise and multiple sequence
     alignments. Besides producing more reliable alignments, especially
     for more distantly related sequences, multiple sequence alignments
     provide more structural information than pairwise alignments; they
     locate conserved regions in the molecule, thus improving
     predictions of structural arrangements due to mutant residues or
     residues that differ between *template* and *target* sequences :cite:p:`pearson2013`. For this reason, in this tutorial
     we are going to perform a multiple sequence alignment.
     Additionally, you can also test the available tools to perform
     pairwise alignments.

   | Besides and sequences, other sequences are needed to accomplish a
     multiple sequence alignment. The type and number of the sequences
     included depends on the sequence conservation, although they have
     to allow differentiating conserved regions. As an example, our
     multiple sequence alignment will include four more :math:`\alpha`
     subunit sequences from organisms located between human and fish in
     the evolutionary scale: (Horse), (Rabbit), (Wild turkey), (Aldabra
     giant tortoise). Download these sequences one by one from database
     filling in the protocol form with the appropriate accession codes,
     , and , respectively (). A similar process has to be followed for
     :math:`\beta` subunit, importing sequences and .

   .. figure:: Images/Fig12.pdf
      :alt: Importing additional sequences to perform the multiple
      sequence alignment.
      :name: fig:multialignment_sequences
      :width: 95.0%

      Importing additional sequences to perform the multiple sequence
      alignment.

-  | Access to in :
   | The protocol allows direct opening of the multiple sequence
     alignment in and then, access to via web service. Fill in the
     protocol form ( (1)), including the previously imported (2), the
     particular chain of interest (use the wizard to select it (3)) and
     the sequence of human :math:`\alpha` subunit (4). Since we plan to
     improve the alignment by including additional sequences to align
     (5), they will have to be added next (6). Finally, select one of
     the multiple sequence alignment tools (7).

   .. figure:: Images/Fig13.pdf
      :alt: Importing the multiple sequence alignment in .
      :name: fig:model_from_template_protocol
      :width: 100.0%

      Importing the multiple sequence alignment in .

   will be opened including this time the multiple sequence alignment
   together with the graphics window (). The selected chain is shown
   green-highlighted in both windows. As you may observe in the
   alignment, :math:`\alpha` subunit is a quite conserved macromolecule;
   there is only one gap in the alignment because (Proline) 47 residue
   disappeared throughout the evolutionary process.

   .. figure:: Images/Fig14.pdf
      :alt: Opening the multiple sequence alignment in .
      :name: fig:chimera_alignment
      :width: 80.0%

      Opening the multiple sequence alignment in .

| To complete the form that will allow us to get some atomic models of
  the sequence in web service, we have two possibilities: a) to select
  (, red arrow) , or b) clicking with the right mouse inside the box (,
  green arrow) and selecting in the pop up window. A new window of will
  be open ( (A)), that we have to fill in. (1) should include the
  sequence. In the section (2) we should include the sequence that we
  would like to model, in this particular case. license key has to be
  included here (3). The number of output models, 5 by default, can be
  also specified (4). Since the target sequence that we would like to
  model should include ( group) we are going to select this choice as
  (5). Finally, press (6) to start the computation of potential models
  for your sequence.

.. figure:: Images/Fig15.pdf
   :alt: (A) Completing the form to access to homology modeling with .
   (B) Resulting . (C) panel.
   :name: fig:modeller
   :width: 70.0%

   (A) Completing the form to access to homology modeling with . (B)
   Resulting . (C) panel.

In main graphics window, lower left corner, you may see the status of
your job. After a while, five possible atomic structures, from now ahead
, are retrieved for the sequence ( (B)) together with their assessment
scores. Column of indicates the score derived from statistical
potentials (values in ; for reliable ). Column (normalized Discrete
Optimized Protein Energy) score depends on the atomic distance (negative
values for the better ). You can check every model numbers in ’s main
menu ( (C)).

For this tutorial we are going to select ( (B), green arrow). Renaming
this model is the first step to save it. We can rename the model by
typing in the command line:

::

        rename #3.2 id #4

The renamed atomic structure will appear in the panel ( (C), green
arrow). To track this new atomic structure in the workflow, we can write
in the command line:

::

        scipionwrite #4 prefix model_from_modeller_3_2_

In case that the (( (A, 5)) didn’t include the group in the retrieved
models, an alternative option to have the model with the group (residue
144 from the atomic structure chain A) could be:

::

        rename #3.2 id #4
        save /tmp/chainA.cif format mmcif models #4
        open /tmp/chainA.cif
        select #2/A:144
        save /tmp/HEME.cif format mmcif models #2 selectedOnly true 
        open /tmp/HEME.cif
        scipioncombine #4,5

        scipionwrite #6 prefix Hgb_alpha_

: We have saved the group of the in a new file that will be opened as .
Finally, the combination of (retrieved aminoacid of the sequence) and (
group of the ) generates a new model that will be saved in . A different
could be selected by the user adding to the last command line .

After closing , you can visualize ( (8)) your full predicted () that
includes the group (1). The string that we have included as in the
command line will allow us to follow the atomic structure in a more
simple manner. You can check the in the the name of the saved atomic
structure () in the panel of (1). Interestingly, the suffix number of
the saved atomic structure () stands for the ID protocol number.

.. figure:: Images/Fig16.pdf
   :alt: Initial of human :math:`\alpha` subunit, including the group
   (blue).
   :name: fig:chimera_model
   :width: 80.0%

   Initial of human :math:`\alpha` subunit, including the group (blue).

In a similar process, you can also obtain the initial atomic structure
of the human :math:`\beta` subunit. Take into account that in this last
case the HEME group is the residue of the chain . The command lines are
similar to the previous case of the :math:`\alpha` subunit if you also
select the .

::

        rename #3.2 id #4
        save /tmp/chainB.cif format mmcif models #4
        open /tmp/chainB.cif
        select #2/B:148
        save /tmp/HEME_B.cif format mmcif models #2 selectedOnly true 
        open /tmp/HEME_B.cif
        scipioncombine #4,5
        setattr #6/A c chain_id B
        scipionwrite #6 prefix Hgb_alpha_

In addition, we have included a command to change the chain of the
second polypeptide from to . In general, to change the chain you have to
write:

::

     setattr #model_number/old_ID c chain_id new_ID
     setattr #model_number/old_ID r chain_id new_ID

Additional exercises for practising
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Since the protocol allows to use other options, inspect by your own
  the possible result obtained by:

#. Using as input only the sequence of the human :math:`\alpha` subunit.

#. Using as input the same atomic structure and the sequences of both
   the human :math:`\alpha` and :math:`\beta` subunits. Improve the
   alignment of the human :math:`\alpha` subunit with additional
   sequences and improve the alignment of the human :math:`\beta`
   subunit with your own sequence alignment that contains about 30
   sequences.

Option of recovering the session
--------------------------------

If for any reason you decide to go back and check a different from the
five initially provided by , you can do it by using protocol (Appendix
`[app:chimeraRestoreSession] <#app:chimeraRestoreSession>`__). This
protocol may be used whenever session had been saved, specifically after
using protocols , , and . In addition to the command line , command
lines and also save session by default. So, if you want to restore a
previous session just open the form (, 1), and include the session that
you’d like to restore (2).

.. figure:: Images/Fig17.pdf
   :alt: Restoring session in .
   :name: fig:restore_session_protocol
   :width: 90.0%

   Restoring session in .
