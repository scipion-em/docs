Get the initial model 
=====================

Predicting the three-dimensional (3D) structure of a protein 
from its sequence alone remains an unsolved problem. However,
some programs as AlphaFold2 are able to predict the 3D atomic coordinates of a large collection of folded protein structures with remarcable accuracy :cite:p:`jumper2021`, :cite:p:`AlphaFold-Multimer2021`.

Alphafold2 execution can take up to hours for a single protein, it needs more than 2 TB of disk space and the use of a GPU card is recommendable to speed up the execution of processes. The *Scipion* protocol **chimerax-alphafold prediction** has implemented the possibility of running Alphafold2 in your own computer selecting the option *Local AlphaFold* (:numref:`model_building_fig1_alphafold_prediction` (4), see :ref:`Appendix <app:alphafoldPredictionProtocol>` for details). 

   .. figure:: Images/Fig1_protocol_prediction.svg
      :alt: Protocol **chimerax-alphafold prediction** detailing the 4 different options to available in *Scipion* to retrieve AlphaFold predicted models.
      :name: model_building_fig1_alphafold_prediction
      :align: center
      :width: 100.0%

      Protocol **chimerax-alphafold prediction** detailing the 4 different options to available in *Scipion* to retrieve AlphaFold predicted models.

There are, nevertheless, different options that enable researchers retrieve AlphaFold2 predicted models if they lack of these computational resources and, with this aim, the *Scipion* protocol **chimerax-alphafold prediction** has also implemented three options to retrieve AlphaFold2 predicted models. The first two options take advantage of the AlphaFold protein structure `database <https://alphafold.ebi.ac.uk/>`_ and give users the possibility of retrieving AlphaFold predicted models of the protein in which users are interested (option *EBI Database (identical sequence)*, :numref:`model_building_fig1_alphafold_prediction` (1)) or, if that protein is not included in the database yet, of a homologous protein (option *EBI Database (homologous sequence)* :numref:`model_building_fig1_alphafold_prediction` (2)). Look at :ref:`Appendix <app:alphafoldPredictionProtocol>` for use cases. Take into account, however, that although the database is constantly growing with new additional predictions, the protein relevant for the user might not have close homologous. Executing Alphafold2 is thus required. The third option implemented in the *Scipion* protocol **chimerax-alphafold prediction** enables the user run the program taking advantage of two independent solutions based on Google Colaboratory (:numref:`model_building_fig1_alphafold_prediction` (3), option *Google Colab*) involving *Phenix* and *Chimera21* Colab Notebooks, respectively.

In this tutorial we will use one of the solutions involving the option *Google Colab* to create an initial atomic model of the protein *TACAN*. As mentioned before *TACAN* is a homodimer of the protein with Uniprot ID `A0A024R4K9 <https://www.uniprot.org/uniprot/A0A024R4K9/>`_. Let us start by importing the sequence *A0A024R4K9* (:numref:`model_building_fig2_alphafold_prediction`) using the protocol **pwem-import-sequence**. Clomplete the protocol form with your prefered name of the sequence (1), the type of sequence (2, aminoacids), the database source (3, UniProt), and the UniProt ID (4). Finally, execute the protocol (5). Look at protocol :ref:`appendix <app:alphafoldPredictionProtocol>` for details. 

   .. figure:: Images/Fig2_protocol_prediction.svg
      :alt: Completing the *Scipion* protocol **pwem-import-sequence** to import the sequence of TACAN protein from UniProt database.
      :name: model_building_fig2_alphafold_prediction
      :align: center
      :width: 80.0%

      Completing the *Scipion* protocol **pwem-import-sequence** to import the sequence of TACAN protein from UniProt database.

Protein sequences are the only input required to predict the atomic structure of a complex running AlphaFold2. Templates from PDB or a particular user's template can also be included as inputs depending on the Colab Notebook. In this tutorial we are going to execute two different examples using *Phenix* and *Chimera21* Colab Notebooks, respectively in the *Scipion* protocol **chimerax-alphafold prediction**. In the first one we will execute AlphaFold2 based on *Phenix* Colab Notebook and a single copy of the sequence as input. Fill in the protocol form as indicated in :numref:`model_building_fig3_alphafold_prediction`. Select *Google Colab* option (1), *Phenix* Colab Notebook (2), include the sequence of TACAN protein (3) and execute the protocol (4). For details go to protocol :ref:`appendix <app:alphafoldPredictionProtocol>`.

   .. figure:: Images/Fig3_protocol_prediction.svg
      :alt: **A**: Completing the *Scipion* protocol **chimerax-alphafold prediction** to predict the structure of TACAN protein with AlphaFold2 using *Phenix* Colab Notebook. **B**: Warning message about the requirement of RAM. **C**: Warning message about the authorship of the Notebook.
      :name: model_building_fig3_alphafold_prediction
      :align: center
      :width: 100.0%

      **A**: Completing the *Scipion* protocol **chimerax-alphafold prediction** to predict the structure of TACAN protein with AlphaFold2 using *Phenix* Colab Notebook. **B**: Warning message about the requirement of RAM. **C**: Warning message about the authorship of the Notebook.

After executing the protocol a couple of warning messages usually appear (:numref:`model_building_fig3_alphafold_prediction` (B and C)). Accept them with *OK* and *Run anyway*, respectively, to run the AlphaFold2 prediction. The browser of *Phenix* Colab Notebook them will start to run, as you can observe in each of the independent running cells (:numref:`model_building_fig4_alphafold_prediction` (3, 4)), although control running and stopping of all of them is possible openning the *Runtime* menu (:numref:`model_building_fig4_alphafold_prediction` (1)). Take into account that you need a Google account (2) and the sequence of the protein should be written in the form (4).

   .. figure:: Images/Fig4_protocol_prediction.svg
      :alt: Browser of *Phenix* Colab Notebook completed with the TACAN protein sequence and running.
      :name: model_building_fig4_alphafold_prediction
      :align: center
      :width: 100.0%

      Browser of *Phenix* Colab Notebook completed with the TACAN protein sequence and running.

We will execute two different versions alphafold. In the first one a single copy of the sequence will be provided ans therefore only half protein will be created (see figure YYYYa), in the second execution we will provide both copies (see figure ZZZZa)

If you click on "Analyze Results" three windows will pop-up (see figure WWWW). The first one (WWWWa) shows the atomic model using chimerax, the second one (WWWWWb) provides a map of the multiple alignment coverage, that is, given a multiple alignment containing N proteins how many of this N protein contain each one of the problem protein aminoacids. Finally the third windows (WWWWc) show a plot with the value of PAE (Predicted Aligned Error). This plot reports AlphaFold’s expected position error 
at residue x, when the predicted and true structures are aligned on residue y.

-----------
caption figure XXXX: **Import sequence** protocol. Provide a string in **Sequence Name** this value will be use to identify the sequence in the future, then select the option "UniProt ID" and provide the uniport ID in the cell labeled "UniProt NameID"

caption figure YYYY: **Alphafold prediction protocol**
Select Unitprot ID ...


-----------

comment best -> scipion onject // scipionwrite // amber relaxation // script mouse.py

# Is there any way to programmatically prevent Google Colab from disconnecting on a timeout?
# Google Colab notebooks have an idle timeout of 90 minutes and absolute timeout of 12 hours.
# This means, if user does not interact with his Google Colab notebook for more than 90 minutes,
#  its instance is automatically terminated. Also, maximum lifetime of a Colab instance is 12 hours.
#
# Run this code in your Desktop, Then point mouse arrow over (colabs left panel - file section)
# directory structure on any directory this code will keep clicking on directory on every 30 seconds
# so it will expand and shrink every 30 seconds so your session will not get expired Important
# - you have to run this code in your pc 

