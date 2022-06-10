.. _problemToSolveTACAN:

Problem to solve: Human ion channel TACAN isoform induced by tumor necrosis factor alpha 
========================================================================================

The transmembrane protein TMEM120A, also known as TACAN isoform 1, forms an ion channel involved in adipocite differentiation and in sensing mechanical pain in animals and plants. 
The structure of the homodimer purified or reconstituted in lipid nanodiscs has been recently modeled from cryo-EM data :cite:p:`rong2021`, :cite:p:`xue2021`, :cite:p:`chen2022`. Map and atomic structure of this homodimer, unbound to any ligands is shown in :numref:`model_building_TACAN_figure`. The complex displays C2 symmetry and shape of seesaw rocker. Each protomer is a relativelly small protein of 343 amino acids. The soluble N-terminal domain of each protein is located in the cytosolic side (horizontal helices in :numref:`model_building_TACAN_figure`), and the transmembrane domain is embedded in the lipid bilayer (vertical helices in :numref:`model_building_TACAN_figure`). Each protomer contains a pore putatively devoted to ion transport that seems to be closed at resting state :cite:p:`chen2022`. Although different ligands have been identified bound to the dimer complex, such as the fatty acid metabolism cofactor CoASH, which occupies a small density in the intracellular funnel-like cavity of each monomer :cite:p:`rong2021`, :cite:p:`xue2021`, or cholesterol molecules at the flanks of the two protomers :cite:p:`chen2022`, they seem to dissociate using a detergent solution that allows to get the homodimer unbound to any ligands :cite:p:`rong2021`.

.. figure:: Images/TACAN.svg
   :alt: Map (**A**) , model fit to map (**B**) and model (**C**) of the human TACAN homodimer (isoform 1). 
   :name: model_building_TACAN_figure
   :align: center

   Map (**A**) , model fit to map (**B**) and model (**C**) of the human TACAN homodimer (isoform 1).

The volume of the first isoform of human TACAN complex, at 4 Å resolution, and its atomic interpretation
(:numref:`model_building_TACAN_figure`) are available in the Electron Microscopy Data Bank (*EMDB*) and Protein
Data Bank (*PDB*) with accession numbers `EMD-31441 <https://www.ebi.ac.uk/emdb/EMD-31441>`_  and `PDB 7F3U <https://www.rcsb.org/structure/7F3U>`_, respectively. The isoform of human TACAN complex induced by tumor necrosis factor alpha (isoform CRA_a), nevertheless, has not been structurally solved yet. Both isoforms contain identical sequence in the N-terminal part of the protein but are quite different in the C-terminal part (:numref:`model_building_TACAN_alignment`).

.. figure:: Images/TACAN_alignment.svg
   :alt: Alignment of isoforms 1 (`UniProtKB ID Q9BXJ8 <https://www.uniprot.org/uniprot/Q9BXJ8>`_) and isoform CRA_a (`UniProtKB ID A0A024R4K9 <https://www.uniprot.org/uniprot/A0A024R4K9>`_) of human TACAN protein. 
   :name: model_building_TACAN_alignment
   :align: center

   Alignment of isoforms 1 (`UniProtKB ID Q9BXJ8 <https://www.uniprot.org/uniprot/Q9BXJ8>`_) and isoform CRA_a (`UniProtKB ID A0A024R4K9 <https://www.uniprot.org/uniprot/A0A024R4K9>`_) of human TACAN protein.

This tutorial will guide us in the deduction process of the isoform CRA_a of the human *TACAN* 
atomic structure using the *Scipion* framework and the protein
sequence as starting input data to generate the atomic
structure prediction using the AlphaFold2 method :cite:p:`jumper2021`, :cite:p:`AlphaFold-Multimer2021`. Since there is not an experimental map of the second isoform of human TACAN complex we will borrow the map of the first isoform (:numref:`model_building_TACAN_figure` (A)) to explore the possibility of improving the initial AlphaFold2 prediction and test if the architecture of the isoform CRA_a, in spite of sequence differences, can be adapted to the map of the first isoform at least in part.
