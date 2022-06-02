Problem to solve: Human ion channel-like protein TACAN
======================================================

The transmembrane protein TMEM120A, also known as TACAN, forms an ion channel involved in adipocite differentiation and in sensing mechanical pain in animals and plants. 
The structure of the homodimer purified or reconstituted in lipid nanodiscs, displaying C2 symmetry and shape of seesaw rocker, has been recently modeled from cryo-EM data :cite:p:`rong2021`, :cite:p:`xue2021`, :cite:p:`chen2022`. The monomer is a relativelly small protein of 343 amino acids. The soluble N-terminal domain of each protomer is located in the cytosolic side, and the transmembrane domain is embedded in the lipid bilayer. Each protomer contains a pore putatively devoted to ion transport that seems to be closed at resting state :cite:p:`chen2022`. Although different ligands have been identified bound to the dimer complex, such as the fatty acid metabolism cofactor CoASH that occupies a small density in the intracellular funnel-like cavity of each monomer :cite:p:`rong2021`, :cite:p:`xue2021` (:numref:`TACAN_figure`) or cholesterol molecules at the flanks of the two protomers :cite:p:`chen2022`, they seem to dissociate using a detergent solution that allows to get the homodimer unbound to any ligands :cite:p:`rong2021`.

.. figure:: Images/TACAN.svg
   :alt: Map (cyan) and model of human TACAN homodimer (blue and grey) as shown in `3DBIONOTES-WS <https://3dbionotes.cnb.csic.es/?queryId=EMD-24230>`_. Each protomer appears bound to its respective fatty acid metabolism cofactor CoASH.
   :name: TACAN_figure
   :align: center

   Map (cyan) and model of human TACAN homodimer (blue and grey) as shown in `3DBIONOTES-WS <https://3dbionotes.cnb.csic.es/?queryId=EMD-24230>`_. Each protomer appears bound to its respective fatty acid metabolism cofactor CoASH.

The volume, at 3.24 Å resolution, and its atomic interpretation
(:numref:`TACAN_figure`) are available in the Electron Microscopy Data Bank (*EMDB*) and Protein
Data Bank (*PDB*) with accession numbers `EMD-24230 <https://www.ebi.ac.uk/emdb/EMD-24230>`_  and `PDB 7N7P <https://www.rcsb.org/structure/7N7P>`_, respectively.

This tutorial will guide us in the deduction process of the human *TACAN*
atomic structure using the *Scipion* framework, the 3D map and the protein
sequence as starting input data to generate the atomic
structure prediction using the AlphaFold2 method :cite:p:`jumper2021`.
