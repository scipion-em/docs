Summary of results and submission
=================================

| Once we have selected the best :math:`model` of the whole human *Hgb*
  and obtained good validation scores from , and other validation
  programs, and we have checked that we have the whole volume density
  modeled, we are ready to submit the electron density map and its
  atomic interpretation to public databases and to make public our
  results.

Submission to public databases
------------------------------

Although submission of cryoEM maps and derived atomic structures to
databases has to be done by direct online request
(https://deposit-pdbe.wwpdb.org/deposition/), may contribute to organize
the submission records. The protocol allows to perform this task
(Appendix `[app:exportToEMDB] <#app:exportToEMDB>`__). By using this
protocol we can save the files that you have/want to submit to databases
in a labelled folder and in the appropriate format. details the
protocols of the modeling workflow involved in this task.

.. figure:: Images/Fig78.pdf
   :alt: framework detailing the workflow to submit :math:`cryo-EM`
   results to databases.
   :name: fig:scipion_workflow_submission
   :width: 100.0%

   framework detailing the workflow to submit :math:`cryo-EM` results to
   databases.

When you submit the *map* and the *model* of a :math:`cryo-EM`
experiment, besides these two records, an image of the *map* is also
mandatory to submit. Other maps, such as half maps or
postprocessing-sharpening maps, as well as maks, are also recommended to
submit. In addition, the *FSC* file is strongly encouraged. As you can
see in , we can provide directly from the workflow the *map* and the
*model*, as well as the two sharpening maps. The *map* image can be
attached from a file. We lack, however, from the *FSC* file, since the
*FSC* file is usually generated during the *map* reconstruction process
starting from the half maps, for example with the protocol(, red arrow).
To compute the *FSC* file we could download the half maps from the
database (https://www.ebi.ac.uk/pdbe/entry/emdb/EMD-3488/index)
selecting the *zip* Bundle ( (red arrow)).

.. figure:: Images/Fig77.pdf
   :alt: *EMDB* entry *3488* in *PDBe*
   :name: fig:export_to_EMDB_protocol_1
   :width: 90.0%

   *EMDB* entry *3488* in *PDBe*

The *zip* folder contains the *FSC* file (*emd_3488_fsc.xml*) and the
*map* image (*emd_3488.png*) but, unfortunately, lacks of half maps.
Then, you can use any two half maps and compute the *FSC* file, just to
submit it with the rest of the files.

To save all the relevant files in a single labelled folder, open the
protocol ( (1)), and complete the form with the elements to export:
*Main map* (2), *Additional maps: “Yes”* (3), the two sharpened maps as
additional maps (4), the *FSC* file if you count on it (5), *Atomic
structure* (6) and *Image* (7), previously saved in a known folder.
Then, write the name of the exportation directory path, or find it with
the browser on the right. All submission files will be saved in the
*directory* selected (8). A directory name related with the submission
(number, date, project,...) is recommended.

.. figure:: Images/Fig45.pdf
   :alt: Saving files for submission to EMDB with protocol
   :name: fig:export_to_EMDB_protocol
   :width: 90.0%

   Saving files for submission to EMDB with protocol

After executing the protocol (9), you can check that all files are saved
in the given directory. No additional visualization tools have been
included in this protocol.

Publication of results
----------------------

| Since the atomic interpretation of a certain macromolecule will be
  probably the starting point of relevant mechanistic or biomedical
  studies, summaring and organizing our results constitutes the first
  step to draw the conclusions that will be made public by journals and
  talks. Many different questions can be posed based on the atomic
  structure. Here we are wondering about interactions among members of
  the macromolecule. To answer this question we have included in the
  protocol to identify the residues involved in contacts between any
  couple of interacting molecules. “contacts” involve atoms within
  favorable interaction distances. Unfavourable contacts or severe
  clashes, in which atoms are too close together, although discarded by
  default in the final list of ‘contacts’’, may also be shown by using
  appropriate advanced parameters, as you can see in Appendix
  `[app:chimeraContactsProtocol] <#app:chimeraContactsProtocol>`__.
| As an example, in this tutorial we are going to learn how to get atom
  contacts of human haemoglobin *metHgb* atomic structure *5NI1*,
  associated to the starting map *EMD-3488*. This structure was already
  downloaded from *PDB* by using the protocol ( (1)). According to the
  aim of the analysis, two possible scenarios and the respective
  workflows can be considered to compute contacts: a) infering all
  contacts between any couple of members of the whole macromolecule (
  (3)); b) infering all contacts between any couple of members of the
  asymmetric unit, and between one member of the asymmetric unit and
  another component from a neighbor asymmetric unit ( (5)).

.. figure:: Images/Fig46.pdf
   :alt: workflows inside the red box to get contacts between any two
   chains of a macromolecule (3) and between any two chains of the
   asymmetric unit, and between any chain of the asymmetric unit and a
   chain of a neighbor asymmetric unit (5).
   :name: fig:workflows_contacts
   :width: 90.0%

   workflows inside the red box to get contacts between any two chains
   of a macromolecule (3) and between any two chains of the asymmetric
   unit, and between any chain of the asymmetric unit and a chain of a
   neighbor asymmetric unit (5).

| Since the penultimate step of the second workflow ( (4)) requires
  applying symmetry, we are going to start moving the structure to match
  its symmetry center to the origin of coordinates using the protocol as
  we did previously (), including the whole starting map of the human
  *metHgb* and the imported atomic structure *5NI1* as *Input map* and
  *Input atom structure*, respectively.
| Secondly, we are going to extract the structure of the asymmetric unit
  of the docked *5NI1* structure using the protocol as it is indicated
  in (4). Complete the protocol form including the last docked structure
  *5NI1* as *Atomic structure*. After executing the protocol, the
  graphics window will open. You can select and save the atomic
  structure of the map asymmetric unit writing in the command line:
| *select #2/A,B*
| *save /tmp/chainAB.cif format mmcif models #2 selectedOnly true*
| *open /tmp/chainAB.cif*
| *scipionwrite #3 chainAB\_*
| *exit*

-  | CASE A: Contacts between any couple of members of the whole
     macromolecule ( (3)):
   | This option allows to get all contacts between all couples of
     members of the macromolecule. In the case of the human *metHgb* we
     have depicted all those possible contacts in the (A).

   .. figure:: Images/Fig49.pdf
      :alt: Schema of the human haemoglobin *metHgb* showing protein
      contacts between couples of chains of the whole macromolecule (A)
      and contacts obtained by applying symmetry to the asymmetric unit
      (B).
      :name: fig:schema_contacts
      :width: 90.0%

      Schema of the human haemoglobin *metHgb* showing protein contacts
      between couples of chains of the whole macromolecule (A) and
      contacts obtained by applying symmetry to the asymmetric unit (B).

   The protocol can be used to obtain the contacts depicted. Open this
   protocol ( (1)) and fill in the first *Input* (2) in which no
   symmetry will be applied. Include the docked *5NI1* structure (4) as
   *Atomic structure*. Use the wizard on the right to label the molecule
   chains (5) as they appear in the adjacent window, and execute the
   protocol.

   .. figure:: Images/Fig50.pdf
      :alt: Filling in the protocol form with two different inputs: (2)
      to get atom contacts between couples of chains within the whole
      *metHgb*; (3) to get contacts between any couple of chains within
      the asymmetric unit, and “non-redundant“ contacts between the
      asymmetric unit and another chain of a neighbor asymmetric unit of
      the human haemoglobin *metHgb*.
      :name: fig:contacts_unit cell
      :width: 90.0%

      Filling in the protocol form with two different inputs: (2) to get
      atom contacts between couples of chains within the whole *metHgb*;
      (3) to get contacts between any couple of chains within the
      asymmetric unit, and “non-redundant“ contacts between the
      asymmetric unit and another chain of a neighbor asymmetric unit of
      the human haemoglobin *metHgb*.

   After executing the protocol, all atom contacts between the couples
   of proteins indicated in (A) can be visualized by clicking ( (A)).

   .. figure:: Images/Fig52.pdf
      :alt: (A) Display of results of atom contacts between couples of
      chains within the whole *metHgb*; (B) Display of results of atom
      contacts between couples of chains within the asymmetric unit, and
      ”non-redundant“ contacts between a chain of the asymmetric unit
      and another chain from a neighbor asymmetric unit of the human
      haemoglobin *metHgb*.
      :name: fig:contacts_results
      :width: 90.0%

      (A) Display of results of atom contacts between couples of chains
      within the whole *metHgb*; (B) Display of results of atom contacts
      between couples of chains within the asymmetric unit, and
      ”non-redundant“ contacts between a chain of the asymmetric unit
      and another chain from a neighbor asymmetric unit of the human
      haemoglobin *metHgb*.

   The viewer window of the protocol *contacts* display different
   results ((A)):

   -  *3D Visualization* box: Final atomic structure considered to
      compute contacts that can be visualized with . Press the eye (1)
      to open the structure shown on the right.

   -  *Interacting chains* box: Summary list of all interacting chains,
      similar to the list shown on the right of the (A). Press the eye
      to open it (2).

   -  *Contacts between interacting chains* box: In addition to the
      possibility of changing the order of the interacting chains in the
      display, as well as the maximal distance between residues to group
      them, this box allows to select couples of interacting chains (4)
      and inspect in detail the contacts between them pressing the eye
      on the right (3).

-  | CASE B: Contacts between any couple of members of the asymmetric
     unit and ”non-redundant“ contacts between one member of the
     asymmetric unit and another one from the neighbor asymmetric unit (
     (5)). This second asymmetric unit has been obtained by applying
     symmetry with the protocol . Then, “non-redundant” interaction
     means any interaction that can not be inferred by symmetry. The (B)
     shows the total number of interactions of our example. The
     interactions between the chain *B* of the asymmetric unit (model
     *#1.1*) and the chain *A* of the neighbor asymmetric unit (model
     *#1.2*) are symmetric to the interactions between chain *A* of the
     asymmetric unit (model *#1.1*) and chain *B* of the neighbor
     asymmetric unit (model *#1.2*). Since those interactions can thus
     be inferred by symmetry, they are “redundant” and are absent of the
     final list of contacts.
   | Similarly to the case A, the protocol form has to be open ( (1) )
     and completed as indicated in the second *Input* (3). Include the
     asymmetric unit structure saved with the protocol *operate* (6),
     use the wizard on the right (7) to label the chains as it is shown
     on the right and, finally, include the respective type of symmetry
     of the human *metHgb* (8).
   | Like in the case A, after executing the protocol all non-redundant
     atom contacts between any couple of proteins indicated in (B) can
     be visualized by clicking ( (B)). Besides the lower number of
     contacts displayed, remark that a relevant difference between the
     results of the case A and the case B is the final atomic structure
     visualized with , which discriminates between the starting
     asymmetric unit and the second one generated by symmetry.
   | *Note*: This second possibility of getting protein contacts
     observed in the case B is extremely useful when you have a big
     asymmetric unit, for example of a virus, and you are interested in
     contacts among proteins within the asymmetric unit and with other
     adjacent asymmetric units.
