.. _problemToSolveTACAN:

Problem to solve: Human ion channel-like protein TACAN
======================================================

The transmembrane protein TMEM120A, also known as TACAN, forms an ion channel involved in adipocite differentiation and in sensing mechanical pain in animals and plants. 
The structure of the homodimer purified or reconstituted in lipid nanodiscs has been recently modeled from cryo-EM data :cite:p:`rong2021`, :cite:p:`xue2021`, :cite:p:`chen2022`. Map and atomic structure of this homodimer, unbound to any ligands is shown in :numref:`TACAN_figure`. The complex displays C2 symmetry and shape of seesaw rocker. Each protomer is a relativelly small protein of 343 amino acids. The soluble N-terminal domain of each protein is located in the cytosolic side (horizontal helixes in :numref:`TACAN_figure`), and the transmembrane domain is embedded in the lipid bilayer (vertical helixes in :numref:`TACAN_figure`). Each protomer contains a pore putatively devoted to ion transport that seems to be closed at resting state :cite:p:`chen2022`. Although different ligands have been identified bound to the dimer complex, such as the fatty acid metabolism cofactor CoASH, which occupies a small density in the intracellular funnel-like cavity of each monomer :cite:p:`rong2021`, :cite:p:`xue2021` or cholesterol molecules at the flanks of the two protomers :cite:p:`chen2022`, they seem to dissociate using a detergent solution that allows to get the homodimer unbound to any ligands :cite:p:`rong2021`.

.. figure:: Images/TACAN.svg
   :alt: Map (**A**) , model fit to map (**B**) and model (**C**) of human TACAN homodimer. 
   :name: TACAN_figure
   :align: center

   Map (**A**) , model fit to map (**B**) and model (**C**) of human TACAN homodimer. 

The volume, at 4 Å resolution, and its atomic interpretation
(:numref:`TACAN_figure`) are available in the Electron Microscopy Data Bank (*EMDB*) and Protein
Data Bank (*PDB*) with accession numbers `EMD-31441 <https://www.ebi.ac.uk/emdb/EMD-31441>`_  and `PDB 7F3U <https://www.rcsb.org/structure/7F3U>`_, respectively.

This tutorial will guide us in the deduction process of the human *TACAN*
atomic structure using the *Scipion* framework, the 3D map, and the protein
sequence as starting input data to generate the atomic
structure prediction using the AlphaFold2 method :cite:p:`jumper2021`, :cite:p:`AlphaFold-Multimer2021`.
