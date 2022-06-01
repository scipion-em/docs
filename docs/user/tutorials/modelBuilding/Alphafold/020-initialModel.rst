Get the initial model 
=====================

Predicting the three-dimensional (3D) structure of a protein 
from its sequence alone remains an unsolved problem. However,
some programs as AlphaFold2 are able to predict the 3D atomic coordinates of a large collection of folded protein structures with remarcable accuracy.

Alphafold2 execution can take up to hours for a single protein,  needs more than 2 TB of disk space and requires a GPU card. To enable researchers without these resources to use AlphaFold2, independent solutions based on Google Colaboratory were developed.

We will use one of this solutions to create an initial atomic model of the protein *TACAN*. As mentioned before *TACAN* is a homodimer of the protein with Uniprot ID *A0A024R4K9* (link to https://www.uniprot.org/uniprot/A0A024R4K9). Let us start by imporintg twice the sequence *A0A024R4K9* (see figure XXX-A) using the protocol *pwem-import-sequence* followed by executing alphafold (protocol *chimera-alphafold*) as shown in figure XXXXb (see the figure caption for a description of the main parameters or go to appendix XXXX for a more in detail description).

We will execute two different versions alphafold. In the first one a single copy of the sequence will be provided ans therefore only half protein will be created (see figure YYYYa), in the second execution we will provide both copies (see figure ZZZZa)

If you click on "Analyze Results" three windows will pop-up (see figure WWWW). The first one (WWWWa) shows the atomic model using chimerax, the second one (WWWWWb) provides a map of the multiple alignment coverage, that is, given a multiple alignment containing N proteins how many of this N protein contain each one of the problem protein aminoacids. Finally the third windows (WWWWc) show a plot with e the value of PAE (Predicted Aligned Error). This plot reports AlphaFold’s expected position error 
at residue x, when the predicted and true structures are aligned on residue y.


